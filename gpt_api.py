import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("gpt_key")
text="""
{
"city": "city"
}
"""
class GPT_API:
    def __init__(self):
        pass
    def update(self,messages, role, content):
        messages.append({"role": role, "content": content})
        return messages
    def get_response(self,messages):
        response= openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response['choices'][0]['message']['content']
    def get_city(self):
        messages=[]
        messages = self.update(messages, "user", f'please give me name of city by random, your response should be like this:\n {text}')
        model_response = self.get_response(messages)
        messages = self.update(messages, "assistant" , model_response)
        return model_response