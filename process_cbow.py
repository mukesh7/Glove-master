import numpy as np
file_word = open("cbow_vectors.txt", 'r')
file_out = open("GloVe-master/cbow_vocab.txt", 'w')
file_vocab = open("GloVe-master/vocab.txt",'r')
dictionary = {}
for line in file_vocab:
    st = line.split(' ')
    dictionary[st[0]] = st[1]
for line in file_word:
    st = line.split(' ')
    file_out.write(st[0])
    file_out.write(' ')
    file_out.write(dictionary[st[0]])
file_word.close()
file_vocab.close()
file_out.close()
