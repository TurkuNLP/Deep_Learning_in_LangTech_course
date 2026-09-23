# Course project

To complete the course, successful completion of the project described in the **basic project outline** below is required.
A project successfully completed with the bonus task gives +1 to your grade; however, **this will not lift an otherwise failing grade to passing**.

**Group work** (optional): the project can be completed either individually or as a group of two people. Group projects have some additional requirements; see below. If you do a group work, indicate it very clearly at the beginning, and also each group member should submit the project on moodle.

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

## Bonus task: Multi-label Text Classification

The bonus task involves extending the basic project to a multi-label classification. In multi-label classification, a single text instance can be assigned multiple valid labels simultaneously. To complete the bonus task, you need to read up on multi-label classification methodologies and perform all the steps in the basic project outline using a multi-label dataset. 

**Evaluation:** When evaluating your models, standard accuracy is often insufficient for multi-label tasks. You must identify and use appropriate multi-label metrics (e.g., Macro/Micro F1-score). In your written summary, include a discussion on the specific challenges of multi-label classification, the metrics you chose, and how your models handled multiple labels.

### Example Multi-label Datasets

You may search for your own multi-label text classification corpus, or select one of the following examples:

*   **[SemEval2014Task4](https://huggingface.co/datasets/alexcadillon/SemEval2014Task4):** A popular dataset for Aspect-Based Sentiment Analysis. Restaurant and laptop reviews can contain multiple different aspects (e.g., "food", "service", "price") within the same sentence, making it a multi-label task to identify all present aspects and their polarities.
*   **[Civil Comments](https://huggingface.co/datasets/google/civil_comments):** A dataset of public online comments annotated for toxicity. A single comment in the dataset can be simultaneously tagged with multiple overlapping attributes, such as *toxic*, *severe_toxicity*, *obscene*, *threat*, *insult*, *identity_attack*, and *sexual_explicit*.
*   **[DBPedia Classes](https://huggingface.co/datasets/DeveloperOats/DBPedia_Classes):** A large-scale dataset for classifying Wikipedia articles. Articles are mapped to the DBpedia ontology, and since an entity or article can belong to multiple overlapping classes, it serves as a robust multi-label text classification benchmark.
*   **[WOS Hierarchical Multi-label](https://huggingface.co/datasets/marcelsun/wos_hierarchical_multi_label_text_classification):** A dataset containing abstracts of published academic papers from the Web of Science. It requires hierarchical multi-label text classification, predicting both the parent domains and the specific sub-domains for each abstract.

## Group projects

For the group projects (maximum of **2 students** per group), you have to complete an additional manual annotation and analysis. In addition to the basic project outline, groups must complete the following steps:

1. Manual Annotation:
   * Randomly sample 100 instances from your chosen dataset's test set.
   * Individually and independently, both students in the group must manually label these 100 instances without looking at the dataset's original labels or each other's answers.
   * Important: Your manually annotated datasets (e.g., saved as CSV or JSON files) must be submitted alongside your code and properly loaded within your project's main notebook so your results can be reproduced.

2. Inter-Annotator Agreement (IAA):
   * Compare your independent annotations and calculate a standard Inter-Annotator Agreement metric (e.g., Cohen's Kappa). 
   * Discuss the cases where you disagreed. What made those specific instances difficult to classify?

3. Comparison with Ground Truth:
   * Compare your manual labels against the actual, original labels provided in the dataset.
   * How accurate were you as human annotators? Did you discover any potential errors or biases in the dataset's gold standard labels?

4. Model Evaluation on Hand-labeled Data:
   * Run your three optimized models (prompted generative, fine-tuned generative, and fine-tuned bidirectional) specifically on this subset of 100 hand-labeled instances.
   * Compare the performance of your models against your own human performance on this exact same data slice.

### Summary / Report Additions:
In your final written summary, include a dedicated section for this group work. You should report your Inter-Annotator Agreement score, discuss the qualitative difficulties in labeling the data, and provide the comparative analysis between human performance and model performance. Finally, as stated in the basic outline, ensure you include a short section detailing how the workload (including coding and report writing) was distributed between the two group members.

## Returning your project

Return your project as a Python notebook (following [this template](https://github.com/TurkuNLP/Deep_Learning_in_LangTech_course/blob/master/course_project_template_2025.ipynb)) that includes both execution results and the descriptions detailed above. For group projects, each group member should submit the project work separately on moodle.

## AI policy

[The general AI guidance](https://intranet.utu.fi/en/sites/ai/Pages/AI-in-studying.aspx) of the university applies. As you will notice, it is rather positive towards the use of AI, but also stresses that 1) you are responsible for the content, 2) you must be open about the use of AI, and 3) you can use it to support but not replace own work and thinking. Most importantly: it is not OK to generate large parts of the project end-to-end without own contribution. Whatever you hand out must be the result of your own critical thinking, and you must thoroughly understand the handed out solution or project, and be able to answer questions about it if asked. If you use AI in any capacity in your project, you must briefly describe the way you used it. If you do not describe it, we will assume AI was not used.