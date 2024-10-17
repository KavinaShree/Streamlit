import os
import streamlit as st #important
from openai import OpenAI
#from google.colab import userdata
#from IPython.display import Image

client = st.secrets(api_key = os.environ['openai_api_key'])

#Story
def story_gen(prompt):
  system_prompt = """
  You are a highly acclaimed author known for crafting captivating short fiction stories.Given a concept, create a short story that reflects the core themes of the provided prompt, with an happy and positive conclusion. Ensure the story is concise, engaging, and no longer than 150 words."""

  response = client.chat.completions.create(
      model='gpt-4o-mini',
      messages = [
          { "role": "system","content":system_prompt},
          { "role": "user","content":prompt},
          ],
      temperature = 1.3,
      max_tokens = 1000
  )
  return response.choices[0].message.content

#cover prompt design
def design_gen(prompt):
  system_prompt = """
  You will given a short story. Geneerate a prompt for a cover art that 
  is suitable for the story. The prompt is for dall-e-2.
  """
  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          { "role": "system","content":system_prompt},
          { "role": "user","content":prompt},
      ],
      temperature = 1.3,
      max_tokens = 2000
  )
  return response.choices[0].message.content


#cover art
def art_gen(prompt):
  response = client.images.generate(
      model = 'dall-e-2',
      prompt = prompt,
      size = '1024x1024',
      n=1
  )
  return response.data[0].url

prompt = st.text_input("Enter a prompt")
if st.button("Generate"):
  story = (story_gen(prompt))
  design = design_gen(story)
  art = art_gen(story)

  st.caption(design)
  st.divider()
  st.write(story)
  st.divider()
  st.image(art)