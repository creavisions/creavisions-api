from datetime import datetime
from uuid import uuid4
import os
from dotenv import load_dotenv
import yaml
import openai
import requests

# configure app
event_id = f"{datetime.now().strftime('%d%m%Y-%H%M%S')}-{str(uuid4())}"
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
try:
    with open('metadata.yml', 'r', encoding='UTF-8') as metadata_yml:
        metadata = yaml.safe_load(metadata_yml)
except yaml.YAMLError as exc:
    raise RuntimeError('Error loading metadata yml') from exc

# request image using openai
response = openai.Image.create(
    prompt=metadata['image']['prompt'],
    n=metadata['image']['count'],
    size=metadata['image']['size']
)

# download generated image as png
image_url = response['data'][0]['url']
print(image_url)
data = requests.get(image_url, timeout=metadata['http']['timeout']).content
with open(f"image-{event_id}.png", 'wb', encoding='UTF-8') as image_file:
    image_file.write(data)
    image_file.close()
