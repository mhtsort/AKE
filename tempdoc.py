from ake_document import AkeDocument
class Tempdoc(AkeDocument):
    def __init__(self, location: str, **kwargs):
        AkeDocument.__init__(self, location, **kwargs)

    def __str__(self):
        return self.id


if __name__ == "__main__":
    doc = Tempdoc("HERE", doc_id="Docname")
    print(doc, doc.location)
