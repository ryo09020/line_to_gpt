from openai import OpenAI
import os
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]
)

stream = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[{"role": "user", "content": "君の性格について教えてくれ"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")