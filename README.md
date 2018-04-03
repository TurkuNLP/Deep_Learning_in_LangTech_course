# Deep Learning in Human Language Technology course
Course materials for the 2018 course *TKO_2101 Natural Language Processing* renamed from 2019 onwards to *TKO_8965 Deep Learning in Human Language Technology*. University of Turku.

[UTU Moodle page](https://moodle.utu.fi/course/view.php?id=13402)

# How to attend the course

* We expect you to **take notes during the lecture**, the online materials support, but not replace lectures. It is highly unlikely you can pass the course by simply reading through the online materials.
* If you cannot make it to a lecture, find a friend who can share their notes with you.

# Computers and accounts

* The course takes place in the linux classroom. You will receive user accounts and passwords during the first demo session.
* Coursework will happen on the remote server **vm0964.kaj.pouta.csc.fi**, you will receive user accounts and passwords during the first demo session. You can also access this server from home using **ssh** (on linux/Mac) and **putty ssh** (windows).
* See [running_code.ipynb](running_code.ipynb) for details on the various machines

# Topic 1: Elementary classification

Bag of words text classification with neural networks. On the lectures, we work our way through basic neural network models, their training, and application to classification. Materials:

* [bow_classifier.ipynb](bow_classifier.ipynb)
* [bow_classifier-reuters.ipynb](bow_classifier-reuters.ipynb)
* [read_imdb.ipynb](read_imdb.ipynb)
* [read_news.ipynb](read_news.ipynb)
* [data/imdb_train.json](data/imdb_train.json)
* [data/reuters_51cls.json](data/reuters_51cls.json)

# Topic 2: Word embeddings

What are word embeddings, how to train and use those. On the lectures, we show how weights inside a bag-of-words classifier actually turns out to be a numerical representation of word meaning. Materials:

* [bow_model_load_inspect_imdb.ipynb](bow_model_load_inspect_imdb.ipynb)
* [word_embeddings.ipynb](word_embeddings.ipynb)
* [bow_classifier_with_embeddings.ipynb](bow_classifier_with_embeddings.ipynb)


# Topic 3: Properties of word embeddings

Interesting properties of word embeddings, especially their multilingual mapping

* [embedding_properties.ipynb](embedding_properties.ipynb)

# Topic 4: Text classification with conv-nets

Introduction to convolutional neural networks, how to apply them to text and what they are doing

* [NLP_Week3.pptx](NLP_Week3.pptx)
* [seq2label_conv.ipynb](seq2label_conv.ipynb)
* [cnn_filters.ipynb](cnn_filters.ipynb)
* [cnn_text_task.ipynb](cnn_text_task.ipynb)

# Projects and grading

* Completing a small-group project is mandatory
* Completing milestone 1 gives you grade 1
* Each of the milestones 2 and 3 gives you an extra grade
* i.e. completing all milestones of a project gives you grade 3
* Exam can give you extra 2 grades, you only need to take it if you want grade 4 or 5



