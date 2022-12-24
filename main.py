import os
from pprint import pprint
import openai

# Set the API key
openai.api_key = "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"

prompt = (
  f"""
    A table summarizing the fruits from Goocrux:\n\nThere are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy. There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. Pounits are a bright green color and are more savory than sweet. There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them.
  
  | Fruit | Color | Flavor |
  """
)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

pprint(response)