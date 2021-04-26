# Bot-Manager

Django backend for managing bots.

Deployed on custom VPS [swagger](http://84.201.152.104:8000/swagger/)

## API Endpoints

- `telegram-bot/` for managing bots entries.
   - On object creation, setup webhook to recieve updates
   - On object deletion, remove active webhook


- `rest-auth/` for authorization and registration.
   - handles authorization and registration
   

- `bot/<bot_token>` for receiving webhook updates
   - webhook will send updates to this endpoint until acknowledged


- `swagger/` for swagger documentation
   - used for interacting with api

## Architecture
### Webhooks
Because of possible number of simultaneous running bots, polling will be inefficient.

Instead of polling, telegram allows setting up a webhook to receive updates.
Webhooks allow lower network usage and faster updates.

### Telegram bot API
Default telegram server allows only https connections with SSL certificate 
and limits available ports. \
[Telegram bot API](https://github.com/tdlib/telegram-bot-api) server is easier to set up, as it allows 
http connections, and it is possible to receive webhook updates on any host:port.

### Diagram
![](https://i.imgur.com/JsYBdma.png)

## How to use?
1. Obtain new token for telegram bot from Botfather. 
2. Open [swagger](http://84.201.152.104:8000/swagger/) 
3. Register using rest-auth/register endpoint
4. Click "Authorize" in the top left and Paste received token as "Token YOUR_TOKEN" 
5. Using telegram-bot endpoint post your bot name and token
6. Now your bot will respond with the same message
7. To delete your bot use delete method on telegram-bot.

## How to deploy?

1. clone this repo
   `git clone https://github.com/matveyplevako/Bot-Manager.git`
2. create `.env` file:

To get TELEGRAM_API ID and HASH go to [telegram.org](https://core.telegram.org/api/obtaining_api_id)
```env
TELEGRAM_API_ID=id
TELEGRAM_API_HASH=hash

ALLOWED_HOST= hostname, where backend will be running
DJANGO_SECRET=
TELEGRAM_BOT_SERVER_HOST= telegram bot server host
TELEGRAM_BOT_SERVER_PORT=
WEBHOOK_HOST= where to send webhook updates
WEBHOOK_PORT= 

POSTGRES_HOST= postgres credentials
POSTGRES_USER=
POSTGRES_PORT=
POSTGRES_PASSWORD=
POSTGRES_DB=
```

### Example
```env
TELEGRAM_API_ID=3560000
TELEGRAM_API_HASH=77e505cf4162944b6b3ba36000000000

ALLOWED_HOST="84.201.152.104"
DJANGO_SECRET="123456secret123456"
TELEGRAM_BOT_SERVER_HOST="http://telegram-bot-server"
TELEGRAM_BOT_SERVER_PORT="8081"
WEBHOOK_HOST="http://84.201.152.104"
WEBHOOK_PORT="80"

POSTGRES_HOST="postgres"
POSTGRES_USER=rootuser
POSTGRES_PORT=5432
POSTGRES_PASSWORD=password
POSTGRES_DB=db
```
3. run `docker-compose up -d`

