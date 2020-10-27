import spacy
from spacy.lang.en import English
import common as c
import numpy as np
# Load the spacy model: nlp
nlp = spacy.load('en_core_web_md')

# Calculate the length of sentences
n_sentences = len(c.sentences)

# Calculate the dimensionality of nlp
embedding_dim = nlp.vocab.vectors_length

# Initialize the array with zeros: X
X = np.zeros((n_sentences, embedding_dim))

# Iterate over the sentences
for idx, sentence in enumerate(c.sentences):
    # Pass each each sentence to the nlp object to create a document
    doc = nlp(sentence)

    # for ent in doc.ents:
    #     print(ent.text, ent.label_)
    
    # Save the document's .vector attribute to the corresponding row in X
    X[idx, :] = doc.vector

#print(X)