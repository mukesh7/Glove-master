# Glove-master

GloVe: Global Vectors for Word Representation
If you want word vectors trained on massive web datasets, you need only download one of these text files! Pre-trained word vectors are made available under the Public Domain Dedication and License.

# Train word vectors on a new corpus

If the web datasets above don't match the semantics of your end use case, you can train word vectors on your own corpus.

```
$ git clone https://github.com/stanfordnlp/glove
$ cd glove && make
$ ./demo.sh
```

The demo.sh script you have to give path to CORPUS and VOCAB File. It collects unigram counts, constructs and shuffles cooccurrence data, and trains a simple version of the GloVe model. It also runs a word analogy evaluation script in python to verify word vector quality. More details about training on your own corpus can be found by reading demo.sh or the src/README.md

# Training Details with sample data
```
python word2vec.py -train wiki_news.txt -model cbow_vectors.txt -cbow 1 -negative 0 -dim 150 -batch 20000 -alpha 0.075 -window 5 -min-count 10 -processes 8 -binary 0
python process_cbow.py
mv cbow_vectors.txt GloVe-master/
cd GloVe-master
python eval/python/evaluate.py --vocab_file cbow_vocab.txt --vectors_file cbow_vectors.txt --test_file gujtest1.txt
```
