# OSGeoLive-doc-omegat

OSGeoLive-docの日本語翻訳を、OmegaTという翻訳支援ソフトを利用して進めるプロジェクトです。

## 作業メモ(macOS環境, 暫定)

1. Translate Toolkitのインストール

   ```bash
   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt
   ```
2. 最新の翻訳済みpoファイルをsourceフォルダにコピー  
   OSGeo-jpのOSGeoLive-docリポジトリ(https://github.com/OSGeo-jp/OSGeoLive-doc/tree/ja_all_po_files) の `ja_all_po_files` ブランチより、 `locale/ja/LC_MESSAGES` を `source` フォルダにコピー
3. poファイルからtmxファイルに変換
   ```bash
   bash tools/po2tmxconv.sh
   ```
