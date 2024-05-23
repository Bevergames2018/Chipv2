from gpt4all import GPT4ALL
model = GPT4ALL("mistral-7b-instruct-v0.1.Q4_0.gguf")

output = model.prompt("hello")
print(output)