from flask import Flask, redirect
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.getenv("https://discordapp.com/api/webhooks/1499147387527237784/--MmQlV9AAbfPsoBO2GJcOxrRVZ3zR0UdonTznFov6j1rMQM-VwQRtmZzjgn29iUMj_n")
REDIRECT_URL = "https://google.com"

@app.route("/")
def home():
    try:
        requests.post(
            WEBHOOK_URL,
            json={"content": "👀 Кто-то перешёл по ссылке"},
            timeout=5
        )
    except:
        pass

    return redirect(REDIRECT_URL)


if name == "__main__":
    port=int(os.environ.get("PORT", 10000)
    app.run(host="0.0.0.0", port=port)
