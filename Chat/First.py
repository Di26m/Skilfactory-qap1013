import openai

openai.api_key = "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"
openai.api_key = "sk-..."  # supply your API key however you choose

image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")