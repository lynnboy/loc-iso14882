__version__ = "0.1"

generalindex = 'generalindex'
headerindex = 'headerindex'
libraryindex = 'libraryindex'
grammarindex = 'grammarindex'
impldefindex = 'impldefindex'
conceptindex = 'conceptindex'
xrefindex = 'xrefindex'
xrefdelta = 'xrefdelta'

class Index:
    def __init__(self, name):
        self.name = name
        self.items = dict()

    def add(self, name, description):
        pass

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
    glossary[xrefindex].add(_1, f'({ref(_1)})')

