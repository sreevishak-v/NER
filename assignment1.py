import streamlit as st
import spacy
import en_core_web_sm
from newspaper import Article
from spacy import displacy

nlp = en_core_web_sm.load()

st.title("NER ASSIGNMENT")

if (st.button("ABOUT")):
    st.text("FIRST NLP ASSIGNMENT")
    st.info("THIS APP WILL TAKE AN INPUT FROM THE USER AND THEN PRINTS THE NAMED ENTITIES")

select=st.selectbox("select one of the options:",['Text','URL'])

if select=='Text':
    text=st.text_area("Enter text")

    if (st.button("Click to Analyze")):
        doc=nlp(text)
        ent_html=displacy.render(doc, style="ent", jupyter=False)
        # Display the entity visualization in the browse:
        st.markdown(ent_html, unsafe_allow_html=True)
else:
    text=(st.text_area("ENTER URL"))

    if (st.button("Click to Analyze")):
        article=Article(text)
        article.download()
        article.parse()
        doc=nlp(article.text)
        ent_html=displacy.render(doc,jupyter=False,style='ent')
        st.markdown(ent_html,unsafe_allow_html=True)