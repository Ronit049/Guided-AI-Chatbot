from openai import OpenAI
from dotenv import load_dotenv
import os

from prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_llm(memory):

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + memory

    )

    return response.choices[0].message.content