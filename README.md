
# 📩 Telegram Mesaj Botu

Bu proje, kullanıcıların Telegram botu aracılığıyla belirli bir tarih ve saatte otomatik mesaj göndermelerini sağlar.

This project allows users to schedule automatic messages via a Telegram bot at a specific date and time.

---

## 🚀 Özellikler / Features

- Kullanıcıdan bot token, chat ID, mesaj içeriği, tarih ve saat alır.
- Belirlenen tarihte ve saatte mesajı otomatik gönderir.
- Flask tabanlı web arayüzü ile kolay kullanım.
- Planlama sonrası ekranda başarı bildirimi.

---

## 📦 Kurulum / Installation

### Gereksinimler / Requirements

```bash
pip install flask python-telegram-bot schedule
```

### Uygulamayı Başlat / Run the Application

```bash
python bot.py
```

Tarayıcınızda [http://localhost:5000](http://localhost:5000) adresine giderek formu doldurun.

---

## 🤖 Bot Token ve Chat ID Nasıl Alınır? / How to Get Bot Token and Chat ID?

### 1. Telegram Bot Oluşturma / Create a Telegram Bot

1. Telegram’da `@BotFather` hesabına gidin.
2. `/newbot` komutunu yazın.
3. Botunuza bir isim ve kullanıcı adı verin.
4. Size verilen `Bot Token` bilgisini kaydedin. Örnek:

```
1234563232789:UvWxYz1ewqweeqqwe23456789
```

---

### 2. Chat ID Alma / Get Chat ID

#### Kişisel Chat ID

1. Telegram’da `@userinfobot` veya `@getmyid_bot` botunu açın.
2. Başlatın ve size özel Chat ID’yi alacaksınız. Örnek:

```
123456789
```
## 🟢 Botu Başlatmayı Unutmayın / Don’t Forget to Start Your Bot

Oluşturduğunuz botun size mesaj gönderebilmesi için **önce sizin tarafınızdan başlatılması gerekir.**

### Nasıl Başlatılır?

1. Telegram uygulamasında botunuzun kullanıcı adını aratın (örnek: `@mycustombot`).
2. Botu açın.
3. **"Başlat" (Start)** butonuna tıklayın.
4. Artık bot mesaj göndermeye hazır! ✅

> 💡 Eğer bot bir gruba veya kanala mesaj gönderecekse, botun orada **yönetici** yetkisine sahip olması gerektiğini unutmayın.

---

## 📝 Kullanım / Usage

1. `http://localhost:5000` adresine gidin.
2. Aşağıdaki alanları doldurun:
   - 🤖 Bot Token
   - 💬 Chat ID
   - 📨 Mesaj İçeriği
   - 📅 Gönderim Tarihi (YYYY-AA-GG)
   - 🕒 Gönderim Saati (HH:MM)
3. 🚀 “Başlat” butonuna tıklayın.
4. “✅ Bot planlandı!” bildirimi ekranın altında görünecektir.

---

