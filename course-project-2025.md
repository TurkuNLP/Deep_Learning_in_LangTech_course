# Course project

To complete the course, successful completion of the project described in the **basic project outline** below is required.
A project successfully completed with the bonus task gives +1 to your grade; however, **this will not lift an otherwise failing grade to passing**.

**Group work** (optional): the project can be completed either individually or as a group of two people. Group projects have some additional requirements; see below.

## Basic project outline

The project involves training and evaluating transformer-based classifiers for a text classification task. You should compare the following three approaches:

1. Prompting a generative (GPT-like) model
2. Fine-tuning a generative (GPT-like) model
3. Fine-tuning a bidirectional (BERT-like) model

Specifically, you should complete the following steps

1. Select a text classification corpus to work on. (see below)
2. Read the paper presenting the corpus as well as any other relevant published materials about the corpus to assure you understand the data.
3. Identify what is the random baseline performance (selecting the label randomly) as well as expected performance for recent machine learning models for this corpus. The paper describing the data may help you here.
4. Select a generative model and a bidirectional model to work on. (see below)
5. Write code to
   - download the corpus
   - perform any necessary sampling and preprocessing (see below)
   - for each approach (1, 2, and 3), optimize your method while evaluating performance on the validation set
     - prompting approach (1): optimize your prompt, taking any few-shot examples from the training set
     - fine-tuning approaches (2 and 3): perform hyperparameter optimization while training on the training set
   - evaluate the approaches on the test set
6. Write a summary of
   - what you learned about the corpus
   - your results
   - how your results relate to the state of the art (i.e. the best published results) / expected performance
   - if completed as a group project, a section detailing who did what

### Text classification corpora

Choose one of the following corpora to work on. (If you'd prefer to suggest a corpus not listed here, get in touch with us on Discord! We recommend corpora with binary labels to keep things simple.)

| Corpus name | Labels | Subset sizes  | Description |
| ------------- | ------ | ------------- | ----------- |
| [imdb](https://huggingface.co/datasets/imdb) | neg pos | train:25000 unsupervised:50000 test:25000 | Large Movie Review Dataset. This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training, and 25,000 for testing. There is additional unlabeled data for use as well. |
| [amazon_polarity](https://huggingface.co/datasets/amazon_polarity) | negative positive | train:3600000 test:400000 | The Amazon reviews dataset consists of reviews from amazon. The data span a period of 18 years, including ~35 million reviews up to March 2013. Reviews include product and user information, ratings, and a plaintext review.  |
| [rotten_tomatoes](https://huggingface.co/datasets/rotten_tomatoes) | neg pos | train:8530 validation:1066 test:1066 | Movie Review Dataset. This is a dataset of containing 5,331 positive and 5,331 negative processed sentences from Rotten Tomatoes movie reviews. This data was first used in Bo Pang and Lillian Lee, ``Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales.'', Proceedings of the ACL, 2005.  |
| [sst2](https://huggingface.co/datasets/sst2) | negative positive | train:67349 validation:872 test:1821 | The Stanford Sentiment Treebank consists of sentences from movie reviews and human annotations of their sentiment. The task is to predict the sentiment of a given sentence. We use the two-way (positive/negative) class split, and use only sentence-level labels.  |

**Note**: if you choose a corpus that does not have a validation set, you should split off a random portion of the training data to use for validation.

#### Sampling

You are free to downsample the training and validation data in case training with the full dataset is too slow. Describe the corpus statistics (especially label distribution) after sampling in order to demonstrate that the sampling is done reasonably.

### Models

You are free to use any generative and bidirectional models that are expected to be applicable to the task (e.g. are trained at least on English).
We recommend using comparatively small models to keep compute time down and choosing generative and bidirectional models of broadly similar sizes to make the comparison more meaningful.
For the generative model we recommend to select a model that has been trained to follow instructions. For example, you could consider the following:

* Bidirectional model: [`google-bert/bert-base-cased`](https://huggingface.co/google-bert/bert-base-cased)
* Generative model: [`HuggingFaceTB/SmolLM-135M-Instruct`](https://huggingface.co/HuggingFaceTB/SmolLM-135M-Instruct)

## Bonus task: comparison of base models

The bonus task involves comparison between two different generative and two different bidirectional models.
To complete the bonus task, you need to perform steps 4. and 5. in the basic project outline twice, optimizing the prompt and model hyperparameters separately for each of the models.

We recommend selecting models that are expected to provide different performance, e.g. an older and a more recent model or a monolingual model and a multilingual one.

### Group projects

For group projects only: include a detailed error analysis where you compare the three approaches. How many examples 
(a) all predicted correctly, 
(b) all got wrong, 
(c) one predicted correctly but the others wrong, and
(d) two predicted correctly but one wrong.
If a prediction from a generative model was incorrect, was it because it failed to generate any label (e.g. unsystematic output format) or because it generated an incorrect label?

## Returning your project

Return your project as a Python notebook (following [this template](https://github.com/TurkuNLP/Deep_Learning_in_LangTech_course/blob/master/course_project_template_2025.ipynb)) that includes both execution results and the descriptions detailed above.
