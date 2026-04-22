# Telegram Emoji ID Bot

This bot extracts the `custom_emoji_id` from custom emojis sent to it, allowing you to quickly get the IDs of any premium emojis.

## Deployment with Coolify (Docker Compose)

This project includes a `docker-compose.yml` and `Dockerfile` perfectly set up for Coolify.

### Steps to Deploy:
1. Push this code to your Git repository (GitHub, GitLab, etc.).
2. Go to your Coolify dashboard.
3. Click **Add New Resource** -> **Git Repository** (Public or Private depending on your repo).
4. Select the repository and branch.
5. Select **Docker Compose** as your build pack/deployment method. Coolify will automatically detect the `docker-compose.yml` file.
6. Navigate to the **Environment Variables** section on Coolify and add your Telegram Bot Token securely:
   - Key: `BOT_TOKEN`
   - Value: `your_telegram_bot_token_here`
7. Click **Deploy**!

## Running Locally with Docker

If you want to test the bot locally using Docker:

1. Create a `.env` file in the root directory and add your token:
   ```env
   BOT_TOKEN=your_telegram_bot_token
   ```
2. Start the bot using Docker Compose:
   ```bash
   docker-compose up -d --build
   ```
3. To view the bot logs:
   ```bash
   docker logs -f emoji_id_bot
   ```

## Running Locally with Python

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Make sure your `.env` file is set up.
3. Run the script:
   ```bash
   python bot.py
   ```
