import logging
import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_response(prompt: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    result = completion.choices[0].message.content
    logging.info(f"Generated response: {result}")
    return result
