import streamlit as st
import spacy
from spacy import displacy
#from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper import Article

st.title("Named Entity Recognizer")

st.info("This app will take an input from the user and then prints the named entities")

text1 = st.text_area("Enter a paragraph")
text2 = st.text_area("Enter the URL")

if(st.button("Submit")):
  if text1:  
    doc = nlp(text1)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    # Display the entity visualization in the browser:
    st.markdown(ent_html, unsafe_allow_html=True)
  else:
    
    article = Article(text2)  
    article.download()
    article.parse()  
    print(article.text)
    doc = nlp(article.text)
    ent_html = displacy.render(doc, jupyter=False, style='ent')
    st.markdown(ent_html, unsafe_allow_html=True)