# Wikipedia Bot

## Description

Wikipedia Bot is a chatbot created to provide information from Wikipedia. The bot uses the Wikipedia API to get data and provides users with a user-friendly interface for searching and reading articles.

## Of Functionality

1. **Information search:** Users can use the bot to search for articles on various topics. The bot provides brief information about the articles found.

2. **Reading articles:** Users can request the full text of an article on a topic of interest to them, and the bot will provide the content of the article from Wikipedia.

3. **Links and sources:** The bot provides links and sources related to the selected article so that users can explore the topic more deeply.

## Instructions for use

1. **Installation:**
- Clone the repository: `git clone https://github.com/kamolgks/wikipedia_bot.git `
- Go to the project directory: `cd wikipedia_bot`
- Install dependencies: `pip install -r requirements.txt `

2. **Bot Token with BotFather:**
- Get your bot token in BotFather.
- Insert the bot token into the configuration file (`config.py`).

```python
# config.py

TOKEN = getenv("BOT_TOKEN", "Your bot token")
```

3. **Launching the bot:**
- Launch the bot: `python main.py`
- The bot is ready to be used in your chat.

## Usage examples

<img src="./assets/images/v1.jpg">

<img src="./assets/images/v2.jpg">

## Contribution to the project

If you want to contribute to the development of the project, create a branch, make changes and submit a merge request.

## License

This project is distributed under the [GNU GENERAL PUBLIC LICENSE v3.0](LICENSE). You are free to use, modify and distribute it in accordance with the terms of the license.

**Thanks for using Wikipedia Bot!**