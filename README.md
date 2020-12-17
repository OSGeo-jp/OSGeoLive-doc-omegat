# OSGeoLive-doc-omegat

OSGeoLive-docの日本語翻訳を、OmegaTという翻訳支援ソフトを利用して進めるプロジェクトです。

## OmegaTの設定

OSGeoLive翻訳管理(https://docs.google.com/spreadsheets/d/1FyDI0iaG-v-VsocWrUyDmfabBbb5CD08VNrTTdhgcgQ/edit?usp=sharing) の [翻訳の手順] シートの内容をチェックしてください。

## 管理者メンテナンス作業

※将来的にはGitHub Actionsに移行の予定です。

### Python関連ライブラリのインストール

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### 訳文のreST文法チェック

1. OmegaTの [環境設定] より、 [編集] / [原文と同じ訳文を許可] をチェックONし、 [確定] ボタンをクリック
2. OmegaT上での翻訳作業で一区切りついたら、 [プロジェクト] / [訳文ファイルを生成] メニューを選択して、訳文ファイルを生成
3. ターミナル上で下記を実行して、reST文法にエラーがないか確認
   ```bash
   $ source venv/bin/activate
   $ python3 tools/check_target.py [訳文フォルダのパス(デフォルト: target)]
   ```
4. reST文法エラーがある場合は、翻訳を修正し、上記2~3の手順を再度実施

### OSGeoLive-doc / Transifex からの原文の同期

1. 最新の翻訳済みpoファイルを `source` フォルダにコピー  
   OSGeo-jpのOSGeoLive-docリポジトリ(https://github.com/OSGeo-jp/OSGeoLive-doc) の `transifex_ja` ブランチより、 `locale/ja/LC_MESSAGES` を `source` フォルダにコピー
2. poファイルからtmxファイルに変換(※必要に応じて実施)
   ```bash
   $ bash tools/po2tmxconv.sh
   ```
3. `source` フォルダ内の追加・変更分をGitでコミット・プッシュ

### Transifex への訳文のアップロード

1. ターミナル上で下記を実行して、訳文をフォーマット
   ```bash
   $ source venv/bin/activate
   $ python3 tools/format_target.py [原文フォルダのパス(デフォルト: source)] [訳文フォルダのパス(デフォルト: target)]
   ```
2. `source` フォルダと `target` フォルダを比較して、有意な変更のあった訳文ファイルのみ、Transifexにアップロード