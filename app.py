import streamlit as st
from spacy import displacy
import spacy
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
with st.sidebar:
    selected = option_menu("Main Menu", ["Home","Text","Upload", 'About'],
        icons=['house', 'line','upload','exclamation'], menu_icon="cast", default_index=0)
    selected

model_path = 'D:\\ML projects\\internship work nith\\trained_model'
model = spacy.load(model_path)
def process_and_visualize(text):
    # Load your SpaCy model
    doc = model(text)
    return doc

# Define the CSS for background image and custom styling
styling = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/premium-photo/abstract-digital-network-connected-by-dots-lines_878954-444.jpg");
background-size: cover;
color:white;


}
[data-testid="stApp"]{
display: flex;
justify-content: center;
align-items: center;
height: 100vh;
width: 100vw;
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
background-image:url("https://img.freepik.com/premium-photo/abstract-digital-network-connected-by-dots-lines_878954-444.jpg");
background-size:cover;

}

</style>
"""

# Inject CSS into the Streamlit app
st.markdown(styling, unsafe_allow_html=True)

# # Main title
# st.title("Biomedical NER")


# Display content based on menu selection
if selected == "Home":
    st.markdown("<h1 style='text-align: center;font-family: feelfree;'>Welcome to Biomedical NER</h1>",unsafe_allow_html=True)

    st.markdown(
        "<h3 style='text-align: center;'>Easily identify and classify biomedical entities in your text with our interactive tool.</h3>",
        unsafe_allow_html=True)
    # st.image(
    #     "https://th.bing.com/th/id/OIP.WpdNHLN7mrq7qjvE1H5fsQAAAA?pid=ImgDet&w=150&h=150&c=7&dpr=1.5", use_column_width=True)
    st.markdown("<p style='text-align: center;'>Go to the side-bar menu option to explore the application.</p>",
                unsafe_allow_html=True)

elif selected == "Text":
    st.title("Biomedical NER")
    user_input = st.text_area("Enter medical content", height=250, max_chars=None)
    if st.button("Check Results", key="text-button"):
        if user_input:
            doc = process_and_visualize(user_input)
            if doc.ents:
                html = displacy.render(doc, style="ent", jupyter=False)
                st.write(html, unsafe_allow_html=True)
            else:
                st.write("No named entities related to biomedical are found in the text.")
        else:
            st.warning("Please provide the input based on the selected method.")
elif selected == "Upload":
    st.title("Biomedical NER")
    uploaded_file = st.file_uploader("Upload a .txt file", type=['txt'])
    if uploaded_file is not None:
        text = uploaded_file.read().decode('utf-8')
        if st.button("Check Results", key="file-button"):
            if text:

                doc = process_and_visualize(text)
                if doc.ents:
                    html = displacy.render(doc, style="ent", jupyter=False)
                    st.write(html, unsafe_allow_html=True)
                else:
                    st.write("No named entities related to biomedical are found in the text.")
            else:
                st.warning("Please provide the input based on the selected method.")


elif selected=="About":
    st.subheader("About")
    st.write("Welcome to the Biomedical Named Entity Recognition! This application is designed to identify and classify entities such as diseases,and chemicals in biomedical text. Named Entity Recognition is a crucial task in Natural Language Processing (NLP) that involves detecting and categorizing key information within a text. In the biomedical domain, this task is especially important for extracting valuable insights from scientific literature, clinical notes, and research papers.")
    st.write("This application is  specifically targets the recognition of biomedical entities, enabling researchers and practitioners to quickly and accurately identify important terms related to diseases and chemicals.")

