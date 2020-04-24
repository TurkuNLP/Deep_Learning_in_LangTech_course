# Deep Learning in Human Language Technology course

Materials for the University of Turku course *TKO_8965 Deep Learning in Human Language Technology* (previously named *TKO_2101 Natural Language Processing*).

[UTU Moodle page](https://moodle.utu.fi/course/view.php?id=13402)

# How to attend the course

* We expect you to **take notes during the lecture**. The online materials support, but do not replace the lectures. It is highly unlikely you can pass the course by simply reading through the online materials.
* If you cannot make it to a lecture, find a friend who can share their notes with you.

# Computers and accounts

* The course takes place in the linux classroom. You will receive user accounts and passwords during the first demo session.
* See [running_code.ipynb](running_code.ipynb) for details on the various machines

# Topic 1: Feed-forward NNs and the BoW model

Bag of words text classification with neural networks. On the lectures, we work our way through basic neural network models, their training, and application to classification.

* [Bag-of-words text classification - notebook](bow_classifier.ipynb)
* [Classifier word vector analysis - notebook](bow_classifier_features.ipynb)
* [Word embeddings - notebook](word_embeddings.ipynb)
* [BoW classifier with pretrained word embeddings - notebook](bow_classifier_embeddings_simpler.ipynb)

# Topic 2: Convolutional Neural Networks

Convolutional neural networks and their use in natural language processing.

* [Sequence to Label with CNNs - notebook](seq2label_conv.ipynb)
* [CNN filter interpretation - notebook](cnn_filters.ipynb)
* [Pytorch CNN model - notebook](cnn_model_pytorch.ipynb)

# Topic 3: Properties of word embeddings

Interesting properties of word embeddings, especially their multilingual mapping

* [embedding_properties.ipynb](embedding_properties.ipynb)
* [data/analogy_eng.txt](data/analogy_eng.txt)
* [data/analogy_fin.txt](data/analogy_fin.txt)

# Topic 4: Text classification with conv-nets

Introduction to convolutional neural networks, how to apply them to text and what they are doing

* [NLP_Week3.pptx](NLP_Week3.pptx)
* [seq2label_conv.ipynb](seq2label_conv.ipynb)
* [cnn_filters.ipynb](cnn_filters.ipynb)
* [cnn_text_task.ipynb](cnn_text_task.ipynb)

# Topic 5: Sequence labeling and recurrent neural networks

Introduction to recurrent neural networks (LSTMs) and sequence labeling (named entity recognition and part-of-speech tagging)

* [POS tagging](pos.ipynb)
* [POS tagging with feature embeddings](pos_with_features.ipynb)
