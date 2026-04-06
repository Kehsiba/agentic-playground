from ollama import chat


response = chat(
    model='qwen3',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
print(response.message.content)