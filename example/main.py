import os
from dotenv import load_dotenv

load_dotenv()

def main():
    import requests

    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_KEY')}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": "Can you please let us know more details about you",
    })
    print(output)

if __name__ == "__main__":
    main()
