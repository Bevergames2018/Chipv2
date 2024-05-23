from gpt4all import GPT4All
model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

output = model.prompt("hello")
print(output)