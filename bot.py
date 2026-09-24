import time
import requests

TELEGRAM_BOT_TOKEN = "8702775425:AAHCrMCk0oi1clcl_yZ7LjMAU0vuz9Vh4Mk"
TELEGRAM_CHAT_ID = " @my_crypto_alert_1998_bot"

TARGET_COIN = "BTCUSDT"
PRICE_THRESHOLD = 50000.0

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Error sending message: {e}")

def check_prices():
    url = "https://api.coindcx.com/exchange/ticker"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        for item in data:
            if item.get("market") == TARGET_COIN:
                current_price = float(item.get("last_price", 0))
                if current_price >= PRICE_THRESHOLD:
                    send_telegram_alert(f"🔔 ALERT: {TARGET_COIN} reached {current_price}!")
                break
    except Exception as e:
        print(f"Error checking price: {e}")

if __name__ == "__main__":
    check_prices()
        
