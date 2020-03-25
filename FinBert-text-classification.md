# Text classification

This project is about text classification. You will develop a text classification system that identifies different kinds of online texts, such as news, blogs and opinionated texts. We will refer to these text categories as registers. If you want to learn more about online registers and their automatic identification, you can read, e.g., our paper [Toward Multilingual Identification of Online Registers] (https://www.aclweb.org/anthology/W19-6130/).


The data for this project consists of ~7500 documents with manual annotations on their register. The registers are identified using a relatively detailed, hierarchical taxonomy. The taxonomy consists of 8 main categories that are divided into a large number of subregisters. The taxonomy is described at the end of this page (TODO). The table includes also the abbreviations that are used in the data.

The documents are based on a (almost) random sample of the Finnish Internet. For each document, the annotators have aimed at marking the subregister category. In this case, the document has two register labels: the subregister label and the main register label to which the subregister belongs. For instance, a document annotated as a news article would have the label NE for News and the corresponding higher level register label NA for Narrative. However, in some cases, the document does not seem to fit any of the subregisters. In this case, the document can be given only one label: the main register label, such as NA for Narrative. Finally, some documents may display characteristics of several register categories. In this case, the annotator can mark several register labels for one single document. Consequently, the document may have up to four labels. This would be the case case if a document is annotated both as a Personal blog (subregister label PB + corresponding higher level register label NA) and Review (subregister label RV + corresponding higher level register label OP).

# Milestone 1
