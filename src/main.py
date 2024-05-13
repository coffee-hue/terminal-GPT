import openai
import configparser
import asyncio
import aiohttp
import json

config = configparser.ConfigParser()
config.read('src/config.ini')

class gpt:
    try:
        token = config["BEAR_TOKEN"]["token"]
    except Exception as e:
        print(f"Failed loading configuration file - {e}")
        token = ""
    headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }

    async def ask_question():
        
        while True:
            question = input("What is your question? ")

            match question:
                case "quit":
                    break
                case "exit":
                    break
                case _:
                    answer = await send_answer_question(question)
                    print(answer)


async def send_answer_question(question):
    data = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
            "role": "user",
            "content": question
            }
        ]
        })

    async with aiohttp.ClientSession() as sess:
        async with sess.request("POST",url="https://api.openai.com/v1/chat/completions", headers=gpt.headers, data=data) as response:
                response.raise_for_status()
                answer = await response.json()

    return answer["choices"][0]