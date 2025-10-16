import os
from openai import OpenAI

class LLMClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError('OpenAI API key required in environment or passed to LLMClient')
        self.client = OpenAI(api_key=self.api_key)

    def chat(self, messages, model='gpt-4', max_tokens=800, temperature=0.2):
        # messages: list of {'role','content'}
        resp = self.client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return resp.choices[0].message.content
