# Spot-the-Bot
This repository represents the work on Spot the Bot Project for Thai and Atikamekw languages

additional resources can be found here: [Resources on google drive](https://drive.google.com/drive/folders/1UlUlQJD7eCQFL42PyB8tkrx2mkOGm2WQ?usp=sharing)



## Thai Language:

1- we start by literature extraction from websites for Thai language, multiple links for files were extracted from multiple websites [(code)](https://github.com/faresGh97/Spot-the-Bot/blob/main/Thai/Thai_Text_Extraction.ipynb), mainly links for Thai literature from websites where extracted from [libgen](https://libgen.is/search.php?req=thai&open=0&res=25&view=simple&phrase=1&column=language) and from [archive](https://archive.org/details/booksbylanguage_thai?&sort=-week&page=126), those links represents literature in multiple files format (txt or Pdf).

2- we download literature files associated with the extracted links mentioned in the previous step [(code)](https://github.com/faresGh97/Spot-the-Bot/blob/main/Thai/Thai_Text.ipynb), in this step around 6000 literature text were prepared in order to be used in the next step which is cleaning and stemming.

3- in this step [(code)](https://github.com/faresGh97/Spot-the-Bot/blob/main/Thai/Thai_preprocessing.ipynb), cleaning for the extracted files from the previous text has been done based on the multiple criteria’s, first, we start by removing the unwanted text tokens from the extracted text (foreign symbols, numbers, punctuations). Second, we preform stop-words removal. Third: we preform lemmatization: since Thai language does not have the concept of spaces to separate the words in a sentence, rather a Thai speaker can understand Thai text based on the context, and also Thai language does not have the concept of prefixes and suffixes to differentiate the time of the verbs for example, hence, we decided to preform word tokenization task instead, multiple models were tested to preform word tokenization (pythainlp , deepcut, attcut), we decided to use [attcut](https://pythainlp.github.io/attacut/overview.html) library to preform word tokenization  , which is a transformer model that achieved a fast and solid output when concerned about word tokenization task for Thai language, hence for each file we extracted from the step above, a processed file was generated that contains tokens extracted from the base file separated by white spaces. Finally, we generate a clean Corpus file that contains in each line the title of the literature file and the tokens extracted from the literature file in one line, meaning one line in the Corpus = one literature file for each file from the 6000 literatures extracted in the previous step.

4- we preform Tfid matrixes and then SVDs matrixes in order to get the final embeddings of words in Thai [(code)](https://github.com/faresGh97/Spot-the-Bot/blob/main/Thai/Thai_Embeddings.ipynb) based on the clean corpus file extracted from the step above. Multiple matrixes have been extracted in this step.



## Atikamekw:

1- since this language is a tribal language in north America region (in Montreal, Canada specifically), there was no literature to be found for this language, thus we extracted Wikipedia articles for this languages, thus for each article in [Atikamekw wikipedia,](https://atj.wikipedia.org/wiki/Kotakahi:Toutes_les_pages) a text file representing the content of this article has been extracted [(code)](https://github.com/faresGh97/Spot-the-Bot/blob/main/Atikamekw/Atikamekw_Text_Extraction.ipynb), which resulted in 1583 files that contains Atikamekw text.

2- cleaning and lemmatization of the text has been done in this step [(code)](https://github.com/faresGh97/Spot-the-Bot/blob/main/Atikamekw/Atikamekw%20Limma.ipynb). First, we preform text cleaning the same way we did for Thai language (without the stop-words removal step), then we preform lemmatization, for the same reasons mentioned above we couldn’t find a lemmatization tool for this language, hence a self-made lemmatization class has been made based on the lexicon literature and websites that explained the grammatical rules for this language, we mentioned:
        a- Atikamekw Morphology and Lexicon, 1978, Beland, Jean Pierre [eng]
        b- Manuel D'Initation a la Langue Atikamekw, 2020, Cercle Kisis [frn]
        c- [verbs conjunction](https://verbes.atikamekw.atlas-ling.ca/) [frn]
after lemmatization a preprocessed text file for each of the articles mentioned above was generated, and a corpus file from the processed files was generated.

3- we preform Tfid matrixes and then SVDs matrixes in order to get the final embeddings of words in Atikamekw [(code)](https://github.com/faresGh97/Spot-the-Bot/blob/main/Atikamekw/Atikamekw_embeddings.ipynb) based on the clean corpus file extracted from the step above. Multiple matrixes have been extracted in this step.
