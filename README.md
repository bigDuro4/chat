# chat

## Overview
Simple chat bot that goes into detail about historical events the way a teacher would

## 🚀 Installation & Usage

Follow these steps to install, configure, and run the History-Oriented Gemini AI Bot.
## Prerequisites 
- Python 3.10
- Gemini API Key

## Demo
Go to Gemini AI Studio > Click on Api Keys > Click Create to Generatw

### 1. Clone the repository
```bash
git clone https://github.com/your-username/history-gemini-bot.git
cd history-gemini-bot
```


## 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

## 3. Retrieve Api Key
Go to Google AI studio 
<img width="2186" height="941" alt="image" src="https://github.com/user-attachments/assets/c4438652-1d3c-48cb-9c63-bdc0dc601f3e" />

Click Get API Key
<img width="1660" height="568" alt="image" src="https://github.com/user-attachments/assets/03ce5c9d-ff64-4264-a651-32ec3380d8bb" />

## 4. Install Dependencies
```bash
pip install -r requirements.txt
```
In requirements you will have :

```bash
python-dotenv
google-genai
```

## 5. Create a .env file in the project root and store the key:
```bash
Gemini_api_key= your_key_here
```

## 6. Run the App
```bash
python talkapp.py
```
## 7. Run Tests
```bash
pytest -q
```
## Project structure
```bash
chat/
  talkapp.py
  requirements.txt
  tests/
    test_chat.py
```
### Things to improve
- More in depth analysis


