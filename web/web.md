# WiLI、webブラウザ

### サブドメインにアクセス
1. NGINX(OpenResty)+Redisで動的リバースプロキシ、ポート転送
1. ROS2側でWiLIのHTTPサーバーがリッスン
1. 推定結果orモデルのパラメータをJSONで返す

現状ROS2側はポート番号、サブドメイン名がハードコーディング。ROS2 launchに引数を渡す方法がわからないため。

### サブじゃないドメインにアクセス
まだ作業始めていない

1. NGINX+Gunicorn+Flaskで普通にHTML返す
1. JavaScriptのFetchAPIか何かでサブドメインにアクセス、推定結果など取得
1. CanvasかWebGLで可視化

## NGINXの設定ファイル
[nginx/conf.d](./nginx/conf.d/)内にある。

## 参考
* Redisのインストール
  * [Ubuntu 20.04にRedisをインストールしてセキュリティを保護する方法](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04-ja)<br>
  10/03
* NGINX+Redisでの動的リバースプロキシ
  * [Nginxで動的リバースプロキシの設定をするメモ](https://blog.ssrf.in/post/2017-08-09-dynamic-reverse-proxy-with-nginx/)<br>
  10/03
  * [lua-nginx-module の紹介 ならびに Nginx+Lua+Redisによる動的なリバースプロキシの実装案](https://hiboma.hatenadiary.jp/entry/20120205/1328448746)<br>
  10/03
* NGINX
  * [Nginxでまず静的ファイルのみ表示してみる（Nginxその2](https://snowtree-injune.com/2020/10/30/nginx-static-dj014/)<br>
  10/03
