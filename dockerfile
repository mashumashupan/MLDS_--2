# ベースイメージの指定
FROM python:3.10-slim-buster

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係ファイルのコピー
COPY requirements.txt .

# 必要なパッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのファイルをコピー
COPY . /app

# コンテナがリッスンするポート番号を指定
EXPOSE 8888

# サーバーを起動するコマンド
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
