from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import math

from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

#import gensim
#from gensim.models import Word2Vec

import torch  
from transformers import BertTokenizer,BertModel


import spacy


def magnitude(v):
    sum = 0
    for n in v:
        sum += n * n
    return math.sqrt(sum)

# Load spaCy model with GloVe word embeddings
nlp = spacy.load("en_core_web_md")

# Sample sentences
sentence1 = "Veth is married to Yeza"
sentence2 = "Jester pranked a lord"


##BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') 
model = BertModel.from_pretrained("bert-base-uncased")

inputs = tokenizer(sentence1, return_tensors="pt", padding=True, truncation=True)
outputs = model(**inputs)
sentence_embedding1 = torch.mean(outputs.last_hidden_state, dim=1).squeeze().detach().numpy()

inputs = tokenizer(sentence2, return_tensors="pt", padding=True, truncation=True)
outputs = model(**inputs)
sentence_embedding2 = torch.mean(outputs.last_hidden_state, dim=1).squeeze().detach().numpy()

cosine = np.dot(sentence_embedding1,sentence_embedding2)/(magnitude(sentence_embedding1)*magnitude(sentence_embedding2))
print("Cosine Similarity (BERT):", cosine)








s1 = sentence1.split()
s2 = sentence2.split()
sentences = [s1, s2]

#model = Word2Vec(sentences, min_count=1)
#print(model.wv["student"])

# Tokenize the sentence and calculate the sentence embedding
doc = nlp(sentence1)
sentence_embedding1 = doc.vector
doc = nlp(sentence2)
sentence_embedding2 = doc.vector


#print(sentence_embedding1)
#print(sentence_embedding2)

# Create CBOW model
#model1 = gensim.models.Word2Vec(data, min_count = 1, 
#                              vector_size = 100, window = 5)
#print(data)
#print(model1)

#cosine_sim = cosine_similarity([sentence_embedding1],[sentence_embedding2])

# Print the cosine similarity score
#print("Cosine Similarity:", cosine_sim[0][0])

cosine = np.dot(sentence_embedding1,sentence_embedding2)/(magnitude(sentence_embedding1)*magnitude(sentence_embedding2))
print("Cosine Similarity:", cosine)