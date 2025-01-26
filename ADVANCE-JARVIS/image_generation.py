from openai import OpenAI
import user_config
import requests
from PIL import Image
import webbrowser

client = OpenAI(api_key=user_config.openai_key)

def generate_image(prompt):

  response = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    n=1,
    size="1024x1024",
    quality="standard",
  )


  image_url=response.data[0].url
  data = requests.get(image_url).content
  f=open("img.jpg","wb")
  f.write(data)
  f.close()

  webbrowser.open(image_url)

generate_image("A girl eating ice-cream")