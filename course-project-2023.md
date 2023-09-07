# Course project

To complete the course, successful completion of the project described here is required (basic project outline). A project successfully completed with the bonus task gives +1 to grade, however, this will not lift your grade from fail to pass.

Use [this template](todo) for your project.

## Group work

The project can be completed either individually or as a group of two people. Group projects have some additional requirements; see below.

## Basic project outline

The project involves creating a transformer-based classifier for a multilingual text classification task. Specifically, you should

1. Select a multilingual text classification corpus to work on. (see below)
2. Read the paper presenting the corpus as well as any other relevant published materials about the corpus to assure you understand the data.
3. Identify what is the random baseline performance (select the label randomly) as well as the state-of-the-art performance (i.e. the best published results) for this corpus. [Leaderboards](https://huggingface.co/spaces/autoevaluate/leaderboards) or the paper describing the data may help you here.
4. Write code to
	1. download the corpus
	2. perform any necessary sampling and preprocessing (see below)
	3. train a transformer-based classifier on the **English** training set, evaluating performance on the **English** validation set
	4. perform hyperparameter optimization
	5. evaluate your final model on the **English** test set
	6. perform multilingual and cross-lingual experiments (see below)
5. Write a summary of
	1. what you learned about the corpus
	2. your results
	3. how your results relate to the state of the art
	4. if completed as a group project, a section detailing who did what on some level of detail

### Multilingual text classification corpora

We suggest the following corpora to work on. (If you'd prefer to suggest any other multilingual text classification corpus, get in touch with us on Discord!)

* **Corpus name:** amazon_reviews_multi
* **Labels:** Star rating 1–5
* **Languages:** English, German, Spanish, French, Japanese, Chinese
* **Subset sizes (per language):** train:200K, validation:5K, test:5K
* **Description:** Amazon product reviews dataset for multilingual text classification. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. ‘books’, ‘appliances’, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language. More information in the [paper](https://aclanthology.org/2020.emnlp-main.369/).

**Note:** The original [paper](https://aclanthology.org/2020.emnlp-main.369/) suggest using mean absolute error (MAE) instead of classification accuracy for this task to account for the ordinal nature of the ratings. However, **you can treat this as a standard classification task with five labels and measure classification accuracy.**

### Sampling

You are free to downsample the training and validation data in case training with the full dataset becomes too heavy. Describe the corpus statistics (especially label distribution) after sampling in order to demonstrate that the sampling is done reasonably.

### Multilingual and cross-lingual experiments

Report at least the following multilingual and cross-lingual experiments:
  1. Train on English --> Evaluate on English (baseline).
  2. Train on English + at least one other language --> Evaluate on English, compare to baseline results. Does this improve the performance?
  3. Train on at least one language other than English --> Evaluate on English (zero-shot cross-lingual transfer), compare to baseline results. This mimics the setting of *I would like to have a sentiment classifier a language but I don't have any training data for that language*.

Remember to use a multilingual pre-trained language model.

## Bonus task

As an optional bonus task, you may also do the following. Completing this bonus task in addition to the basic project gives +1 to your grade.

[TODO]

## Returning your project

Return your project as a Python notebook (following [this template](todo)) that includes both execution results and the descriptions detailed above.
