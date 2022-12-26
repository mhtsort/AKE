# AKE
## Automatic Keyword Extraction

Automatic Keyword Extraction Methods Comparison

### Environment Set Up

1. Δημιουργήθηκε φάκελος με το όνομα AKE (Automatic Keyword Extraction).

2. VSCode: Ανοίγουμε το φάκελο AKE.

3. VSCode: Ανοίγουμε terminal και δημιουργούμε virtual environment.

   ```console
   AKE> virtualenv venv_ake
   ```

4. Δημιουργούμε αρχείο requirements.

   > ```
   > console pip freeze > requirements.txt
   > ```
   >
   > Για να χρησιμοποιήσουμε στη συνέχεια το αρχείο αυτό
   >
   > ```
   > console pip install -r requirements.txt
   > ```
   >
   > 

## Documentation

### By file

* **ake_document.py**

  Basic class representing a document. Used as a parent class for every document type. Different datasets contain document data organized in a different manner. For example some datasets contain one file per document and use markup to delimit abstract from main text. Other datasets divide each document in multiple files, each representing a part of the document or other data. eg authors, keywords etc

* **krapivin_document.py**

  Class derived from ake_document representing a document from Krapivin2009 datasets. More classes of this kind to follow.

* **temp.py**

  Temporary file for tests. Liable to change. 

* **tempdoc.py**

  Temporary file for tests. Liable to change.

* **requirements.txt**

  Lists project dependencies. Used during setup by pip.
