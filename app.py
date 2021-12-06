from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
#tambahkan ini#########################
import requests
import json
url = "https://api.kawalcorona.com/indonesia/"
response = requests.get(url)
parsed = response.json()[0]
negara = parsed["name"]
positif = parsed["positif"]
sembuh = parsed["sembuh"]
meninggal = parsed["meninggal"]
########################################
app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('lIKFwU/TgvvYQAVMTT0V3L/Q4MJUnjZFb4TdtVb4xeb3YRAVMkRusqyAiIifWjdhFzwiWPT0u8F4B9iB1ILEjXqWEjNEy9xvClCqk8xnFjPVfl1MLFsJ/k6nam1Y94ksJNiLuuU0poOvR905pXJ8JwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f470cac6f78984857d780a3b2a5e90fd')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
# 處理訊息

@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    msg_from_user = event.message.image
    if msg_from_user == 'Data-covid':
    	message = ImageSendMessage(
            original_content_url='https://i.imgur.com/41lXWjP.png',
            preview_image_url='https://i.imgur.com/41lXWjP.png'
        )
        line_bot_api.reply_message(event.reply_token, message)
       
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
