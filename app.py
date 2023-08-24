import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']
print(image_url)

https://oaidalleapiprodscus.blob.core.windows.net/private/org-OKlHcGEWPrcQcdzRYNUXA7PP/user-4tMxmVauCjB085nx40emdbWo/img-8n50hfFi4W4aODPMptlSjfPh.png?st=2023-08-24T16%3A45%3A22Z&se=2023-08-24T18%3A45%3A22Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-08-23T18%3A57%3A06Z&ske=2023-08-24T18%3A57%3A06Z&sks=b&skv=2021-08-06&sig=U3hKRLFDapTGc0Z3d7bMBIZskQzBkPkwLn9mp7CkdJY%3D