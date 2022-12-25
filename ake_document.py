class AkeDocument:
    def __init__(self, location: str, **kwargs):
        """
        :param: location: String to file location.
        :param: kwargs: keyword arguments to be passed to the retrieve methods of each corpus.
            :keyword:str doc_id: id of the document.

        Document type interface. Represents a document in the corpus of a dataset.
        Different datasets use different templates to represent a document.
        AKEDocument class creates an interface for a class for each different dataset.
        """
        self.id: str = self.set_id(location, **kwargs)
        self.location: str = location
        self.title: str = self.retrieve_title(**kwargs)
        self.abstract: str = self.retrieve_abstract(**kwargs)
        self.body: str = self.retrieve_body(**kwargs)
        self.kwargs: dict = kwargs  # kept for use in any function

    def set_id(self, name: str, **kwargs) -> str:
        """
        creates an id for the document
        :param name: id given to the document
        :return: id of the document defaults to file location
        """
        doc_id = name
        if "doc_id" in kwargs.keys():
            doc_id = kwargs["doc_id"]
        return doc_id

    def retrieve_title(self, **method_args) -> str:
        return "default title"

    def retrieve_abstract(self, **method_args) -> str:
        return "default abstract"

    def retrieve_body(self, **method_args) -> str:
        return "default body"


if __name__ == "__main__":
    # Test parameters given as kwargs
    doc = AkeDocument(location="Mylocation", doc_id="Docname")
    print(doc.id, doc.location)
    # Test no kwargs
    doc = AkeDocument("Mylocation2")
    print(doc.id, doc.location)
