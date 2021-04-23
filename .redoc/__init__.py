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
        self.items = []
    @staticmethod
    def item(value):
        if (type(value) is not dict):
            item = { key: value, text: value }
        Index.refid += 1
        item.refid = refid
        return item

    def add(self, value, description = None, *contents):
        item = self.item(value)
        if description:
            item.description = description
        
        items.add(item)

        return f"[.index#{item.refid}]"

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
    return glossary[xrefindex].add({key: _1, description: f'({ref(_1)})'})

# locations
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
def indeximpldef(_1):
    return index[impldefindex].add(_1, order = text(_1))
def indexdefn(_1): return indextext(_1)
def idxbfpage(_1): return f"[.textbf {_1}]"
def indexgrammar(_1):
    return indextext(_1) + indexgram(_1, styler = idxbfpage)

def impldef(_1):
    return indeximpldef(_1) #+ text("implementation-defined")
def impldefplain(_1):
    return index[impldefindex].add(_1) #+ text("implementation-defined")

# appearance
def idxcode(_1:str): return {key: _1, text: tcode(_1)}
def idxconcept(_1:str): return {key: _1, text: tcode(_1)}
def idxexposconcept(_1:str): return {key: _1, text: tcode(placeholder(_1))}
def idxhdr(_:str): return {key: _1, text: tcode(f"<{_1}>")}
def idxgram(_:str): return {key: _1, text: gterm(_1)}
def idxterm(_:str): return {key: _1, text: term(_1)}
def idxxname(_:str): return {key: f"__{_1}", text: xname(_1)}

# library index entries
def indexlibraryglobal(_1:str): return indexlibrary(idxcode(_1))
def indexlibraryctor(_1:str): return indexlibrary(idxcode(_1), sub = text("constructor"))
def indexlibrarydtor(_1:str): return indexlibrary(idxcode(_1), sub = text("destructor"))
def indexlibrarymember(_1:str, _2:str):
    return indexlibrary(idxcode(_1), sub=idxcode(_2)) + indexlibrary(idxcode(_2), sub=idxcode(_1))
def indexlibraryzombie(_1:str): return indexlibrary(idxcode(_1), sub = text("zombie"))

def libglobal(_1:str): return indexlibraryglobal(_1) + _1
def libmember(_1:str, _2:str): return indexlibrarymember(_1, _2) + _1

# index for library headers
def libheader(_1:str): return indexhdr(_1) + tcode(f"<{_1}>")
def indexheader(_1:str): return indextext(idxhdr(_1)) + index[headerindex].add(idxhdr(_1), styler=idxbfpage)
def libheaderdef(_1:str): return indexheader(_1) + tcode(f"<{_1}>")
def libnoheader(_1:str): return indextext(idxhdr(_1), sub=text("absence thereof")) + tcode(f"<{_1}>")
def libheaderrefx(_1:str, _2:str): return libheader(_1) + iref(_2)
def libheaderref(_1:str): return libheaderrefx(_1, f"{_1}.syn")
def libdeprheaderref(_1:str): return libheaderrefx(_1, f"depr.{_1}.syn")

# code and definitions embedded in text.
def tcode(_1:str): return f"[.texttt {_1}]"    # TODO: highlighting
def term(_1:str): return f"[.textit {_1}]"
def gterm(_1:str): return f"[.textit {_1}]"
def keyword(_1:str): return tcode(_1) + indextext(idxcode(_1))
def grammarterm(_1:str): return indexgram(idxgram(_1)) + gterm(_1)
def regrammarterm(_1:str): return gterm(_1)
def placeholder(_1:str): return f"[.textit {_1}]"    # TODO: highlighting
def exposid(_1:str): return tcode(placeholder(_1))
def defnxname(_1:str): return indextext(idxxname(_1)) + xname(_1)
def defnlibxname(_1:str): return indexlibrary(idxxname(_1)) + xname(_1)

def defn(_1:str): return defnx(_1, _1)
def defnx(_1:str, _2:str): return indexdefn(_2) + f"[.textit {_1}]"
def defnadj(_1:str, _2:str):        # TODO: multilang
    return indextext(f"{_1} {_2}", see={key:_2, sub:{key:_1}})
        + indexdefn(_2, sub=_1) + f"[.textit {_1} {_2}]"

def brk(): return '[=newline]'
def Cpp(): return 'C++'
def CppIII(): return Cpp() + ' 2003'
def CppXI(): return Cpp() + ' 2011'
def CppXIV(): return Cpp() + ' 2014'
def CppXVII(): return Cpp() + ' 2017'
def opt(_1:str): return _1 + ensuremath(f"_\mathit{{_{text('opt')}}}")
def bigoh(_1:str): return ensuremath(f"\mathscr{{O}}({_1})")

# States and operators
def state(_1:str, _2:str): return tcode(_1) + ensuremath(f"_{{{_2}}}")
def bitand(): return ensuremath(f"\mathbin{{\mathsf{{bitand}}}}")
def bitor(): return ensuremath(f"\mathbin{{\mathsf{{bitor}}}}")
def xor(): return ensuremath(f"\mathbin{{\mathsf{{xor}}}}")
def rightshift(): return ensuremath(f"\mathbin{{\mathsf{{rshift}}}}")
def leftshift(_1:str): return ensuremath(f"\mathbin{{\mathsf{{lshift}}_{{{_1}}}}}")

# Notes and examples
def noteintro(_1:str): return f"[=`[][.textid {_1}]: "
def noteoutro(_1:str): return f"[.textid [=thinsp][=--][=thinsp]end {_1}]"
def note(_1): return noteintro(text('Note')) + _1 + noteoutro(text('note'))
def example(_1): return noteintro(text('Example')) + _1 + noteoutro(text('example'))

# Library function descriptions
def Fundescx(_1:str): return f"[.textit {_1}]"
def Fundesc(_1:str): return Fundescx(_1) + ": "
def required(_1:str): return Fundesc(text('Required behavior'))
def requires(_1:str): return Fundesc(text('Requires'))
def constraints(_1:str): return Fundesc(text('Constraints'))
def mandates(_1:str): return Fundesc(text('Mandates'))
def expects(_1:str): return Fundesc(text('Expects'))
def effects(_1:str): return Fundesc(text('Effects'))
def ensures(_1:str): return Fundesc(text('Ensures'))
def returns(_1:str): return Fundesc(text('Returns'))
def throws(_1:str): return Fundesc(text('Throws'))
def default(_1:str): return Fundesc(text('Default behavior'))
def complexity(_1:str): return Fundesc(text('Complexity'))
def remarks(_1:str): return Fundesc(text('Remarks'))
def errors(_1:str): return Fundesc(text('Error conditions'))
def sync(_1:str): return Fundesc(text('Synchronization'))
def implimits(_1:str): return Fundesc(text('Implementation limits'))
def replaceable(_1:str): return Fundesc(text('Replaceable'))
def returntype(_1:str): return Fundesc(text('Return type'))
def cvalue(_1:str): return Fundesc(text('Value'))
def ctype(_1:str): return Fundesc(text('Type'))
def ctypes(_1:str): return Fundesc(text('Types'))
def dtype(_1:str): return Fundesc(text('Default type'))
def ctemplate(_1:str): return Fundesc(text('Class template'))
def templalias(_1:str): return Fundesc(text('Alias template'))

# Cross reference
def xref(): return f"[.textsc {text('See also:')}] "
def xrefc(_1:str): return xref() + "ISO C " + _1

def iref(_1:str): return f'[=nbsp]({ref(_1)})'
def tref(_1:str): return hyperref(tablerefname() + '[=nbsp]' + ref(f'tab:{_1}'), target = f'tab:{_1}')
def fref(_1:str): return hyperref(figurerefname() + '[=nbsp]' + ref(f'fig:{_1}'), target = f'fig:{_1}')

def NTS(_1:str): return f'[.textsc {_1}]'
def ntbs(): return NTS('ntbs')
def ntmbs(): return NTS('ntmbs')

def EXPO(_1:str): return f'[.textit {_1}]'
def expos(): return EXPO(text('exposition only'))
def impdef(): return EXPO(text('implementation-defined'))
def impdefx(_1): return indeximpldef(_1) + EXPO(text('implementation-defined'))
def notdef(): return EXPO(text('not defined'))

def UNSP(_1:str): return f'[.textit[.texttt {_1}]]'
def unspec(): return UNSP(text('unspecified'))
def unspecbool(): return UNSP(text('unspecified-bool-type'))
def seebelow(): return UNSP(text('see below'))
def seeref(_1:str): return UNSP(text(f'see[=nbsp]{ref(_1)}'))
def unspecuniqtype(): return UNSP(text('unspecified unique type'))

def unun(): return '__'
def xname(_1:str): return tcode(f'__{_1}')
def mname(_1:str): return tcode(f'__{_1}__')

def commentellip(): return tcode('/* ... */')

# Concepts
def oldconcept(_1:str): return f"[.textit Cpp17{_1}]"
def oldconceptdef(_1:str): return defn(f'Cpp17{_1}')
def idxoldconcept(_1:str): return {key: f'Cpp17{_1}', text: f'[.textit Cpp17{_1}]'}
def newoldconcept(_1:str): return f"[.textit {_1}]"
def newoldconceptdef(_1:str): return defn(_1)
def idxnewoldconcept(_1:str): return {key: _1, text: f'[.textit {_1}]'}

def cname(_1:str): return tcode(_1)
def ecname(_1:str): return tcode(placeholder(_1))
def libconceptx(_1:str, _2:str): return cname(_1) + indexconcept(idxconcept(_2))
def libconcept(_1:str): return libconceptx(_1, _1)
def deflibconcept(_1:str):
    return cname(_1) + indexlibrary(idxconcept(_1))
        + indexconcept(idxconcept(_1), styler=idxbfpage)
def exposconcept(_1:str): return ecname(_1) + indexconcept(idxexposconcept(_1))
def defexposconcept(_1:str):
    return ecname(_1) + indexconcept(idxexposconcept(_1), styler=idxbfpage)

# Ranges
def Range(_1, _2, _3, _4): return tcode(f"{_1}{_3},[=nbsp]{_4}{_2}")
def crange(_1, _2): return Range('[=`[]', '[=`]]', _1, _2)
def brange(_1, _2): return Range('(', '[=`]]', _1, _2)
def orange(_1, _2): return Range('(', ')', _1, _2)
def range(_1, _2): return Range('[=`[]', ')', _1, _2)

# Change descriptions
def diffhead(_1:str): return f"[.textbf {_1}:] "
def diffdef(_1:str): return '[br]' + diffhead(_1)
def diffref(*args:str):
    if len(args) < 2: title = text('Affected-subclause:')
    else: title = text('Affected-subclauses:')
    if len(args) == 1: refs = ref(args[0])
    if len(args) == 2: refs = '[=nbsp]and[=nbsp]'.join([ref(arg) for arg in args])
    if len(args) > 2: refs = ([f'{ref(arg)},[=nbsp]' for arg in args[:-1]]) + 'and[=nbsp]' + ref(args[-1])
    return f"[.textbf {title}] {refs}"
def change(): return diffdef(text('Change'))
def rationale(): return diffdef(text('Rationale'))
def effect(): return diffdef(text('Effect on original feature'))
def effectafteritemize(): return diffhead(text('Effect on original feature'))
def difficulty(): return diffdef(text('Difficulty of converting'))
def howwide(): return diffdef(text('How sidely used'))

# Miscellaneous
def stage(_1:str): return f"[item]" + text(f'Stage {_1}:')
def doccite(_1): return f"[.textit {_1}]"
def cvqual(_1:str): return f"[.textit {_1}]"
def cv(): return "\mathit{cv}" if mathmode() else cvqual('cv')
def numconst(_1:str): return f"[.textsl {_1}]"
def logop(_1:str): return f"[.footnotesize {_1}]"
