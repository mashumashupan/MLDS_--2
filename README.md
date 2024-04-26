# CIFAR-100 Image Classification API

このプロジェクトは、CIFAR-100データセットを使用して画像分類を行うAPIを提供します。APIはTensorFlowを用いて構築され、FastAPIを使用して展開されます。このREADMEでは、プロジェクトをローカルのARM Macでセットアップし、実行する手順を説明します。

## 前提条件

- Apple Silicon (ARMベース)を搭載したMac
- Docker Desktop for Macがインストールされていること

## プロジェクトのセットアップ

### 1. リポジトリのクローン

プロジェクトのリポジトリをローカルにクローンします。

```bash
git clone <リポジトリのURL>
cd <クローンしたディレクトリ>
```

### 2. Dockerイメージのビルド

Dockerfileを使用してプロジェクトのDockerイメージをビルドします。

```bash
docker build -t cifar100-classification-api .
```

### 3. Dockerコンテナの実行

ビルドしたイメージからDockerコンテナを起動します。

```bash
docker run cifar100-classification-api
```

これにより、FastAPIサーバーがポート8000で起動し、ローカルマシンの同ポートにバインドされます。

## APIの使用方法

APIは、`POST /classify-image/` エンドポイントを介して画像ファイルを受け取り、その画像の分類結果とスコアを返します。以下は、curlを使用した例です。

```bash
curl -X 'POST' \
  'http://localhost:8000/classify-image/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path_to_your_image.jpg;type=image/jpeg'
```

## ヘルスチェック

APIが正しく動作しているかを確認するために、ブラウザから以下のURLにアクセスします。

```
http://localhost:8000/docs
```
