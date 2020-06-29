import os
from dotenv import load_dotenv
load_dotenv()

# API TOKEN
API_TOKEN = os.environ['API_TOKEN']

# 対応するメッセージがなかった場合に反応するメッセージ
DEFAULT_REPLY = "I dont't understand you."

# Botが実行するスクリプトを配置するディレクトリパスのリスト
PLUGINS = ['plugins']
