# Text classification

This project is about text classification. You will develop a text classification system that identifies different kinds of online texts, such as news, blogs and opinionated texts. We will refer to these text categories as registers. If you want to learn more about online registers and their automatic identification, you can read, e.g., our paper [Toward Multilingual Identification of Online Registers] (https://www.aclweb.org/anthology/W19-6130/).

# Data and register labels
The data for this project consist of ~7500 documents with manual annotations on their register. You can download it from TODO. The documents are based on a (almost) random sample of the Finnish Internet. The registers are identified using a relatively detailed, hierarchical taxonomy. The taxonomy consists of 8 main categories that are divided into a large number of subregisters. The taxonomy is described at the end of this page. The table includes also the abbreviations that are used in the data.

The challenge with online documents is that it is not always easy to identify the specific registers categories of the documents. Furthermore, another issue is that a document may display characteristics of several registers. For instance, a blog post may simultaneously seem like a product review. To deal with these challenges, we have followed the following guidelines:
* For each document, the annotators have aimed at marking the specific subregister category. When this is possible, the document has two register labels: the subregister label and the main register label to which the subregister belongs. For instance, a document annotated as a news article would have the label NE for News and the corresponding higher level register label NA for Narrative. 
* In some cases, the document does not seem to fit any of the subregisters. In this case, the document can be given only one label: the main register label, such as NA for Narrative. 
* Some documents may display characteristics of several register categories. In this case, the annotator can mark several register labels for one single document. Consequently, the document may have up to four labels. This would be the case case if a document is annotated both as a Personal blog (subregister label PB + corresponding higher level register label NA) and Review (subregister label RV + corresponding higher level register label OP).

# Milestone 1.1: Bag-of-words classifier (multi-class)
Train a bag-of-words classifier to predict the register categories. In this milestone, the setting is multi-class, so the register label combinations form the classes, e.g. NA_NE and NA_NE_OP_OB. Evaluate your model and report your results with different hyperparameters.

# Milestone 1.2: Recurrent Neural Network Classifier (multi-class)
Modify your codes from milestone 1.1 to use recurrent neural networks (e.g. LSTM or biLSTM) in the classifier. Evaluate your model and report your results with different hyperparameters.

# Milestone 2.1: Deep contextual representations with Bert (multi-class)
Train a Bert classifier to predict the register categories. Similar to Milestone 1, the setting is multi-class, and the evaluations should include results with different hyperparameters.

# Milestone 2.2: Error analysis
Compare the errors made by the classifiers you have trained from milestones 1 and 2.1. Are there any patterns? How do the errors one model makes differ from those made by another.

# Milestone 3.1: Bert (multi-LABEL)
Train two multi-label classifiers, one using non-deep contextual representations, the other using Bert. In this setting, each label is assigned independently. Do hyperparameter optimization on these classifiers.

# Milestone 3.2: Model comparison
Compare the results of these two classifiers. Do the two models predict in the same way? Analyze the predictions in terms of label-specific differences.

# Register classes and abbreviations

NA Narrative

* NE NA    New reports / news blogs
* SR NA    Sports reports
* PB NA    Personal blog
* HA NA    Historical article
* FC NA    Fiction
* TB NA    Travel blog
* CB NA    Community blogs
* OA NA    Online article

OP  Opinion
* OB OP  Personal opinion blogs
* RV OP  Reviews
* RS OP  Religious blogs/sermons
* AV OP  Advice

IN Informational description
* JD IN  Job description
* FA IN  FAQs
* DT IN  Description of a thing
* IB IN  Information blogs
* DP IN  Description of a person
* RA IN  Research articles
* LT IN  Legal terms / conditions
* CM IN  Course materials
* EN IN  Encyclopedia articles
* RP IN  Report

ID Interactive discussion
* DF ID  Discussion forums
* QA ID  Question-answer forums

HI  How-to/instructions
* RE HI  Recipes

IP IG  Informational persuasion
* DS IG  Description with intent to sell
* EB IG  News-opinion blogs / editorials

Lyrical LY
* PO LY  Poems
* SL LY  Songs

Spoken SP
* IT SP Interviews
* FS SP Formal speeches

Others OS
* MT OS Machine-translated / generated texts
