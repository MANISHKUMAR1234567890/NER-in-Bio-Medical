                                     *Named Entity Recognition In Biomedical* 


                                                 
                                                *Overview*

                                                
This project focuses on Named Entity Recognition (NER) in the biomedical domain. NER aims to locate and classify named entities in text into predefined categories such as the names of persons, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc. In the biomedical domain, NER involves identifying entities like diseases, chemicals etc. from biomedical literature.

                                                *Features*

                                                
Implementation of various NER models (spacy's en_ner_bc5cdr_md , scibert , bluebert ) suitable for biomedical texts.
Utilizing tner/bc5cdr dataset for this project.
Performance evaluation using the accuracy , precision , recall and f1-score.
Deployment of en_ner_bc5cdr_md model after training using streamlit.



                                              *Installation*


To get started with the project, clone the repository and install the required dependencies:

https://github.com/MANISHKUMAR1234567890/NER-in-Bio-Medical.git


*cd NER-in-Bio-Medical*


pip install -r requirements.txt




                                                    Data

                                                    
This project uses publicly available biomedical datasets.



                                                Training and Evaluation 

Pretrained model "en_ner_bc5cdr_md" model from the spacy library and "allanai/scibert_scivocab_uncased" and "bionlp/bluebert_pubmed_mimic_uncased_L-12_H-768_A-12" model from the transformers library are trained on the dataset "tner/bc5cdr" with different epoch size. Then the  trained model's performance are evaluated using accuracy, precision, recall and f1 score.


                                                 Deployment


The model "en_ner_bc5cdr_md" after training on different epoch size is deployed which give good precision using streamlit.Then styling is added using the CSS.


                                 


                                                  Contact

For any questions or quiries, please contact:

linkedin.com/in/manish-kumar-79b2a8276
