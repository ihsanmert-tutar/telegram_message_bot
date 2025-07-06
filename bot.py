from flask import Flask, request, render_template_string
import schedule, time, threading, asyncio
import telegram
from datetime import datetime, date

app = Flask(__name__)
user_settings = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    global user_settings
    message_html = ""

    if request.method == 'POST':
        user_settings = {
            "token": request.form['token'],
            "chat_id": request.form['chat_id'],
            "message": request.form['message'],
            "send_time": request.form['send_time'],
            "send_date": request.form['send_date']
        }
        start_scheduler(user_settings)
        # HTML olarak alert kutusu
        message_html = "<div class='alert alert-success mt-3 text-center'>✅ Bot planlandı!</div>"

    # HTML dosyasını oku ve yerine ekle
    with open("form.html", encoding="utf-8") as f:
        html = f.read()

    return render_template_string(html.replace("<!--PLAN_MESSAGE-->", message_html))


def start_scheduler(settings):
    schedule.clear()
    bot = telegram.Bot(token=settings['token'])

    target_date = settings['send_date']  # örn: "2025-07-06"
    target_time = settings['send_time']  # örn: "08:00"

    async def send():
        now_date = date.today().isoformat()
        now_time = datetime.now().strftime('%H:%M')

        if now_date == target_date and now_time == target_time:
            await bot.send_message(chat_id=settings['chat_id'], text=settings['message'])
            print(f"✔ Mesaj gönderildi: {now_date} {now_time}")
            return schedule.CancelJob  # sadece 1 kez çalışsın

    def job():
        asyncio.run(send())

    schedule.every(1).minutes.do(job)  # her dakika kontrol et

# Arka planda zamanlayıcıyı çalıştır
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=run_schedule, daemon=True).start()

if __name__ == '__main__':
    app.run(debug=True)
