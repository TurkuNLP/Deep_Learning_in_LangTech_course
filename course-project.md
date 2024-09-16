# Course project

To complete the course, successful completion of the project described here is required (basic project outline). A project successfully completed with the bonus task gives +1 to grade, however, this will not lift your grade from fail to pass.

Use [this template](course_project_template.ipynb) for your project.

## Group work

The project can be completed either individually or as a group of two people. Group projects have some additional requirements; see below.

## Basic project outline

The project involves creating a transformer-based classifier for a multilingual text classification task. Specifically, you should

1. Select a multilingual text classification corpus to work on. (see below)
2. Read the paper presenting the corpus as well as any other relevant published materials about the corpus to assure you understand the data.
3. Identify what is the random baseline performance (select the label randomly) as well as expected performance for recent machine learned models for this corpus. The paper describing the data may help you here.
4. Write code to
	1. download the corpus
	2. perform any necessary sampling and preprocessing (see below)
	3. train a transformer-based classifier on the **English** training set, evaluating performance on the **English** validation set
	4. perform hyperparameter optimization
	5. evaluate your final model on the **English** test set
	6. perform cross-lingual experiments (see below)
5. Write a summary of
	1. what you learned about the corpus
	2. your results
	3. how your results relate to the state of the art (i.e. the best published results) / expected performance
	4. if completed as a group project, a section detailing who did what on some level of detail

### Multilingual text classification corpora

We suggest the following corpora to work on. (If you'd prefer to suggest any other multilingual text classification corpus, get in touch with us on Discord!)

* **Corpus name:** mteb/amazon_reviews_multi
* **Labels:** Star rating 1–5
* **Languages:** English, German, Spanish, French, Japanese, Chinese
* **Subset sizes (per language):** train:200K, validation:5K, test:5K
* **Description:** Amazon product reviews dataset for multilingual text classification. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. books, appliances, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language. More information in the [paper](https://aclanthology.org/2020.emnlp-main.369/).

**Note:** The original [paper](https://aclanthology.org/2020.emnlp-main.369/) suggest using mean absolute error (MAE) instead of classification accuracy for this task to account for the ordinal nature of the ratings. However, **you can treat this as a standard classification task with five labels and measure classification accuracy.**

### Sampling

You are free to downsample the training and validation data in case training with the full dataset becomes too heavy. Describe the corpus statistics (especially label distribution) after sampling in order to demonstrate that the sampling is done reasonably.

### Cross-lingual experiments

The idea of the cross-lingual experiments is to simulate the situation of *I would like to have a sentiment classifier for a language but I don't have any training data for that language*. In this case, the zero-shot cross-lingual transfer is an option.

Report at least the following cross-lingual experiments:
  1. Train on English --> Evaluate on English (baseline).
  2. Train on at least one language other than English --> Evaluate on English (zero-shot cross-lingual transfer), compare with the baseline results. You can also mix several non-English languages in your training data if you wish.

Remember to use a multilingual pre-trained language model in cross-lingual experiments. You can use for example [`xlm-roberta-base`](https://huggingface.co/xlm-roberta-base) or [`bert-base-multilingual-cased`](https://huggingface.co/bert-base-multilingual-cased).

## Bonus task

As an optional bonus task, you may also do the following. Completing this bonus task in addition to the basic project gives +1 to your grade. Note that if you are doing the project as a group of two, there is an additional requirement in the bonus part.

### Bonus task: Zero-shot with generative language model

The bonus task involves testing an alternative approach to zero-shot transfer utilizing generative language models. In here, the task is to prompt an existing conversational/chat/intruct fine-tuned generative model to do the classification.

This involves the following basic structure:
  1. Select a reasonable generative model to work on. Preferably, the model should be somehow instruction fine-tuned (instruct, chat, conversation). Keep in mind that Colab has somewhat limited resources, so pay attention to model sizes. You can use e.g. [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2).
  2. Downsample the test data.
  3. Write a prompt where you define the task the model is suppose to do, and include one example at a time.
  4. Extract the model predicted labels from the genrated output.
  5. Calculate accuracy and compare it to the previous results (baseline, zero-shot cross-lingual transfer).
  **6. For group projects only:** Make a detailed error analysis where you compare the classifier and generative approaches zero-shot cross-lingual transfer. How many examples (a) both predicted correctly, (b) both predicted wrong, (c) classifier predicted correctly but generative model wrong, and (d) generative predicted correctly but classifier wrong. Use here the downsampled test data. Manually inspect some examples (10-20) which both models predicted wrong, do these look difficult or easy to you?

Notes:
* In able to run a generative model in Colab, model quantization is recommended. See [documentation](https://huggingface.co/docs/accelerate/usage_guides/quantization) and [an example notebook](https://github.com/TurkuNLP/intro-to-nlp/blob/master/text_generation_pipeline_conversational.ipynb).
* Some models require authentication: You need to create a HuggingFace account and accept *terms and conditions* to be able to use the model. 

## Returning your project

Return your project as a Python notebook (following [this template](course_project_template.ipynb)) that includes both execution results and the descriptions detailed above.
