import pathlib
from krapivin_document import KrapivinDoc

# Get path of folder containing corpus
path = pathlib.Path.cwd()
corpus = path / "Krapivin2009" / "all_docs_abstacts_refined"
# Print all filenames in corpus
# for file in corpus.iterdir():
#    print(file)
# List of all text files
textfiles = [x for x in corpus.glob("*.txt")];
# Create Document objects from the previous list
docs = [KrapivinDoc(x, **KrapivinDoc.parsefile(x)) for x in textfiles]
# Print Document titles
i: int = 0
for x in docs:
    i = i + 1
    print(f"{i}.\t{100 * len(x.abstract) / len(x.body):.2f}% {x.title}")
