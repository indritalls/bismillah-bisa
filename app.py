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
line_bot_api = LineBotApi('GUw/Sdi+cGaiCtLq8ZdrYaOMTLk4K1Tc6R0DRiEH/vBqQljRKQ3pJq+oN1sYKNSeSqIPRMJS/H1sBEBIJuxLat77L1VtPgRBnssLOC48ICWaIEk1f9oixGL+aeqgL7mEe6hjk7HUwjSAqjdLBeQA0gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('923c01d65919b7ae347b0749bde3bb6d')
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
            original_content_url='https://upload.wikimedia.org/wikipedia/id/thumb/6/60/Ada_Apa_Denga_Cinta_2.jpg/220px-Ada_Apa_Denga_Cinta_2.jpg',
            preview_image_url='https://upload.wikimedia.org/wikipedia/id/thumb/6/60/Ada_Apa_Denga_Cinta_2.jpg/220px-Ada_Apa_Denga_Cinta_2.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
       
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)