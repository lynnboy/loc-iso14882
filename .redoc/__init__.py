__version__ = "0.1"

import uuid

generalindex = 'generalindex'
headerindex = 'headerindex'
libraryindex = 'libraryindex'
grammarindex = 'grammarindex'
impldefindex = 'impldefindex'
conceptindex = 'conceptindex'
xrefindex = 'xrefindex'
xrefdelta = 'xrefdelta'

class Index:
    refid = 0
    def __init__(self, name):
        self.name = name
        self.items = dict()

    def add(self, name, description=None):
        refid += 1
        items[name] = {
            name: name,
            description: description,
            refid: refid
        }
        return f"[.index#{refid}]"

index = {
    generalindex: Index(generalindex),
    headerindex: Index(headerindex),
    libraryindex: Index(libraryindex),
    grammarindex: Index(grammarindex),
    impldefindex: Index(impldefindex),
    conceptindex: Index(conceptindex),
}
glossary = {
    xrefindex: Index(xrefindex),
    xrefdelta: Index(xrefdelta),
}

# \rSecindex{general}{#1}
# \rSecindex{library}{#1}

def ref(_1):
    return '__link__0'

def addxref(_1):
    return glossary[xrefindex].add(_1, description = f'({ref(_1)})')

def indextext(_1):
    return index[generalindex].add(_1)

def indexlibrary(_1):
    return index[libraryindex].add(_1)

def indexhdr(_1):
    return index[generalindex].add(idxhdr(_1)) + index[headerindex].add(idxhdr(_1))

def indexconcept(_1):
    return index[conceptindex].add(_1)

def indexgram(_1):
    return index[grammarindex].add(_1)
