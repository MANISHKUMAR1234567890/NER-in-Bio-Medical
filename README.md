#Named Entity Recognition In Biomedical 
#Overview
This project focuses on Named Entity Recognition (NER) in the biomedical domain. NER aims to locate and classify named entities in text into predefined categories such as the names of persons, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc. In the biomedical domain, NER involves identifying entities like diseases, chemicals etc. from biomedical literature.


#Features
Implementation of various NER models (spacy's en_ner_bc5cdr_md , scibert , bluebert ) suitable for biomedical texts.
Utilizing tner/bc5cdr dataset for this project.
Performance evaluation using the accuracy , precision , recall and f1-score.
Deployment of en_ner_bc5cdr_md model after training using streamlit.


#Installation
To get started with the project, clone the repository and install the required dependencies:

git clone https://github.com//biomedical-ner.git
cd biomedical-ner
pip install -r requirements.txt

