# LOLMakeCustom

==================================================
       【LOLMakeCustom】Discord Bot for LoL
        自動チーム分け＆能力成長Bot
==================================================

📦 同梱物
--------------------------------------------------
- README.txt              ← この説明書
- .gitignore              ← データ保管用スクリプト
- requirements.txt        ← 使用ライブラリ一覧
- LOLMakeCustom_bot/
    ├─main.py            ← メインスクリプト
    ├─keep_alive.py      ← Replit用（Renderでは不要）
    └─data/
        ├─ abilities.json      ← プレイヤーの能力値保存
        ├─ history.json        ← 試合結果・戦績の保存
        └─ last_teams.json     ← 直近のチーム構成保存

🐍 必要環境
--------------------------------------------------
- Python 3.8以上
- Discord Developerアカウント
- DiscordサーバーへのBot追加権限
- 実行環境（Render推奨 / Replit可 / ローカルでもOK）

⚙️ セットアップ手順（Render向け）
--------------------------------------------------
① [Discord Developer Portal] でBotを作成
　→ https://discord.com/developers/applications

② Botの「トークン」を取得しておく（後で使う）

③ このプロジェクトをRenderにデプロイ
　手順参考: https://render.com/docs/deploy-python

⑤ 必要ライブラリをインストール（ローカルの場合）

pip install -r requirements.txt
⑥ main.py を実行すればBotが起動！



📡 常時起動について（オプション）
--------------------------------------------------
- Renderを使えば常時稼働可能（無料枠あり）
- Replitを使う場合は keep_alive.py を使って UptimeRobot と連携

📝 よく使うコマンド（例）
--------------------------------------------------
- !hello：Botの起動確認
- !ability：能力値登録
- !join @user レーン1 レーン2：参加登録
- !make_teams：自動チーム編成
- !swap @user1 @user2：2人のレーン入れ替え
- !win A / !win B：勝敗報告 → 能力値自動更新
- !show_custom @user：カスタム戦績表示

※全コマンドは「!help_mc_detail」に記載！

🙋‍♂️ よくある質問（FAQ）
--------------------------------------------------
Q. Botが反応しません！
→ Botがサーバーに参加しているか、トークンが正しいか確認してください。

Q. JSONファイルが空です！
→ 最初は空でOKです。コマンドを使えば自動的にデータが追加されます。

📬 サポート
--------------------------------------------------
不具合報告・カスタマイズ依頼は以下までご連絡ください。
📸 X（旧Twitter）: @deco39deco or @owsc_39
discord：@harapeko_o
https://discord.gg/Vjn4Gxys

--------------------------------------------------
Copyright © 2025 deco
このBotは非公式ファンツールであり、Riot Gamesとは無関係です。
--------------------------------------------------


