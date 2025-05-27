import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()

def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS abilities (
            user_id TEXT PRIMARY KEY,
            top INT,
            jg INT,
            mid INT,
            adc INT,
            sup INT
        );
        CREATE TABLE IF NOT EXISTS last_teams (
            id SERIAL PRIMARY KEY,
            team_name TEXT,
            user_id TEXT,
            lane TEXT,
            ability INT
        );
         CREATE TABLE IF NOT EXISTS history (
            user_id TEXT PRIMARY KEY,
            wins INT DEFAULT 0,
            losses INT DEFAULT 0,
            top_wins INT DEFAULT 0,
            top_losses INT DEFAULT 0,
            jg_wins INT DEFAULT 0,
            jg_losses INT DEFAULT 0,
            mid_wins INT DEFAULT 0,
            mid_losses INT DEFAULT 0,
            adc_wins INT DEFAULT 0,
            adc_losses INT DEFAULT 0,
            sup_wins INT DEFAULT 0,
            sup_losses INT DEFAULT 0
         );


    """)
    conn.commit()

def set_ability(user_id, top, jg, mid, adc, sup):
    cursor.execute("""
        INSERT INTO abilities (user_id, top, jg, mid, adc, sup)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (user_id)
        DO UPDATE SET top=%s, jg=%s, mid=%s, adc=%s, sup=%s;
    """, (user_id, top, jg, mid, adc, sup, top, jg, mid, adc, sup))
    conn.commit()

def get_all_abilities():
    cursor.execute("SELECT * FROM abilities;")
    return cursor.fetchall()

def save_last_teams(team_data):
    cursor.execute("DELETE FROM last_teams;")  # 毎回初期化
    for team_name, members in team_data.items():
        for lane, user in members.items():
            cursor.execute("""
                INSERT INTO last_teams (team_name, user_id, lane, ability)
                VALUES (%s, %s, %s, %s);
            """, (team_name, user["name"], lane, user["value"]))
    conn.commit()

def load_last_teams():
    cursor.execute("SELECT team_name, user_id, lane, ability FROM last_teams;")
    rows = cursor.fetchall()
    team_data = {"A": {}, "B": {}}
    for team_name, user_id, lane, ability in rows:
        team_data[team_name][lane] = {"name": user_id, "value": ability}
    return team_data

def update_history(user_id, win, lane):
    cursor.execute("SELECT * FROM history WHERE user_id=%s;", (user_id,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO history (user_id) VALUES (%s);", (user_id,))
    if win:
        cursor.execute(f"""
            UPDATE history SET
                wins = wins + 1,
                {lane}_wins = {lane}_wins + 1
            WHERE user_id = %s;
        """, (user_id,))
    else:
        cursor.execute(f"""
            UPDATE history SET
                losses = losses + 1,
                {lane}_losses = {lane}_losses + 1
            WHERE user_id = %s;
        """, (user_id,))
    conn.commit()

def get_history(user_id):
    cursor.execute("SELECT * FROM history WHERE user_id=%s;", (user_id,))
    return cursor.fetchone()

