from ake_document import AkeDocument
import pathlib


class KrapivinDoc(AkeDocument):
    """
    Document from Krapivin2009 dataset
    :argument: location: file location in string format
    :keyword: title: title of the document
    :keyword: abstract: abstract of the document
    :keyword: body: body of the document
    """

    def __init__(self, location: str, **kwargs):
        AkeDocument.__init__(self, location, **kwargs)
        print(f"{self.location}-{self.id}")

    def __str__(self):
        return self.id

    def __repr__(self):
        representation = f"KrapivinDoc @ {self.location}"
        return representation

    def retrieve_title(self, **method_args) -> str:
        if "title" in method_args:
            title_argument: str = method_args["title"]
            return title_argument
        return "default title"

    def retrieve_abstract(self, **method_args) -> str:
        if "abstract" in method_args:
            title_abstract: str = method_args["abstract"]
            return title_abstract
        return "default abstract"

    def retrieve_body(self, **method_args) -> str:
        if "abstract" in method_args:
            title_body: str = method_args["body"]
            return title_body
        return "default body"

    def parsefile(location: pathlib.Path) -> dict:
        cwd: pathlib.Path = pathlib.Path.cwd()
        file = cwd / location
        text = file.read_text()
        temporary_separator = "031081"
        txt = text.replace("--T", temporary_separator) \
            .replace("--A", temporary_separator) \
            .replace("--B", temporary_separator) \
            .split(temporary_separator)
        x = txt
        title = x[1]
        abstract = x[2]
        body = x[3]
        return {"title": title, "abstract": abstract, "body": body}


if __name__ == "__main__":
    # Create object
    doc = KrapivinDoc("Location of doc", doc_id="Name of doc")
    # Test str and repr functions
    assert doc.id == "Name of doc"
    assert doc.location == "Location of doc"
    # Test other functions
    doc_id = "ID of Doc"
    title = "The test doc title"
    abstract = "The test doc abstract"
    body = "The test doc body"
    doc = KrapivinDoc(
        "LOCATION OF TEST DOC",
        doc_id="ID of Doc",
        title=title,
        abstract=abstract,
        body=body,
        other="other keywords")
    try:
        assert doc.title == title
        assert doc.id == doc_id
        assert doc.abstract == abstract
        assert doc.body == body
    except AssertionError:
        print("KrapivinDoc:: TESTS FAILED - There was an AssertionError")
        print(doc.title, doc.id, doc.abstract, doc.body)
    else:
        print("KrapivinDoc:: TESTS without file access PASSED")
    # cwd: pathlib.Path = pathlib.Path.cwd()
    # file = cwd / "testdoc.txt"
    # text = file.read_text()
    # temporary_separator = "031081"
    # txt = text.replace("--T", temporary_separator)\
    #     .replace("--A", temporary_separator)\
    #     .replace("--B", temporary_separator)\
    #     .split(temporary_separator)
    # x=txt
    # title = x[1]
    # abstract = x[2]
    # body = x[3]
    # print("TITLE:\n",title)
    # print("ABSTRACT:\n",abstract)
    # print("*********************************************")
    # print(pathlib.Path.cwd())
    kwds = KrapivinDoc.parsefile("testdoc.txt")
    doc2 = KrapivinDoc("testdoc.txt", **kwds)
    print("TEST2")
    print(doc2.title)
    print(doc2.abstract)
    kwds = KrapivinDoc.parsefile("testdoc.txt")
    kwds.update(doc_id="blue")
    doc3 = KrapivinDoc("testdoc.txt", **kwds)
    print("TEST3")
    print(doc3.id)
    print(doc3.title)
    print(doc3.abstract)
