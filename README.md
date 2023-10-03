# WiLI

## WiLIについて
なくしもの捜索用ROS2パッケージ群です。<br>
名前はWhere is a Lost Itemの頭文字から取りました。

## 概要
本リポジトリはWiLIについての資料です。<br>
まだメモ書きレベルです。

## 構成ROSパッケージ
作成中
* [wili_io](https://github.com/MaruKazeMaru/wili_io)&emsp;HTTPサーバ機能&amp;データベースの読み書き
* [wili_suggester](https://github.com/MaruKazeMaru/wili_suggester)&emsp;HMMパラメータ+遷移失敗確率からなくしもの位置を推定&amp;実際のなくしもの位置から遷移失敗確率を学習

今後作成
* wili_hmm&emsp;利用者の位置推移からHMMパラメータを学習
* wili_kalman&emsp;カメラ画像内の二次元コード位置+9軸センサのセンサ値から利用者の位置を推定、実験用

作成中断
* [wili_bridge](https://github.com/MaruKazeMaru/wili_bridge)&emsp;ソケット通信サーバ、やりたかったことはwili_ioへ引き継ぎ
* [wili_db](https://github.com/MaruKazeMaru/wili_db)&emsp;データベースの読み書き、wili_ioの派生(フォーク?)元

## WiLIを利用したサジェストアプリ
webブラウザからなくしもの位置の推定結果などを確認するアプリを作成中です。<br>
詳細は[web/web.md](./web/web.md)にあります。