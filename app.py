import streamlit as st
import spacy
from spacy import displacy


model_path = 'D:\\ML projects\\internship work nith\\trained_model'
model = spacy.load(model_path)

st.header("Biomedical NER")
def process_and_visualize(text):
    doc = model(text)
    return doc

user_input = st.text_area(label='Enter medical content', height=250, max_chars=None)

if st.button("Check Results"):
    if user_input:
      doc = process_and_visualize(user_input)
      if doc.ents:
            html = displacy.render(doc, style="ent", jupyter=False)
            st.write(html, unsafe_allow_html=True)
      else:
            st.write("No named entities related to biomedical is found in the text.")
    else:
        st.warning("Please enter some text to recognize.")


