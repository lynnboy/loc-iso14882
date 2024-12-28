__version__ = "0.1"

import uuid

def applyTo(l:list, **kw) : pass
def text(a) -> str: return a
def secNumberStyle(a): return a
def headerStyleAtLevel(**kw): return ''
def br(): return '[br]'
def pushRight(a): return a
def tagStyle(a): return a
def ensuremath(a): return a
def hyperref(a, **kw): return a
def tablerefname(): return ''
def figurerefname(): return ''
def mathmode(): return True
def count(a): return 1

generalindex = 'generalindex'
headerindex = 'headerindex'
libraryindex = 'libraryindex'
grammarindex = 'grammarindex'
impldefindex = 'impldefindex'
conceptindex = 'conceptindex'
xrefindex = 'xrefindex'
xrefdelta = 'xrefdelta'

lastcorechapter = 'cpp'
firstlibchapter = 'support'
lastlibchapter = 'exec'

class Index:
    refid = 0

    def __init__(self, name):
        self.name = name
        self.items = []
    @staticmethod
    def item(value):
        if type(value) is not dict:
            item = { 'key': value, 'text': value }
        Index.refid += 1
        item.refid = Index.refid
        return item

    def add(self, value, description = None, order= None, styler = None, *contents):
        item = self.item(value)
        if description:
            item.description = description

        self.items.append(item)

        return f"[.index#{item['refid']}]"

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

@applyTo(['#', '#:tab', '#:fig', '#:note'])
def ref(refid, **kw): #instruction, args, refid, content, context
    return '__link__0'

@applyTo(['section', 'section:chapter', 'section:annex', 'section:def'])
def addxref(refid, **kw): #instruction, args, refid, content, context
    return glossary[xrefindex].add({'key': refid, 'description': f'({ref(refid)})'})

@applyTo(['section', 'section:chapter', 'section:annex', 'section:def'])
def customlabel(instruction, args, refid, content, context):
    seqNode = '.'.join(context.nestSeq(instruction))
    seqNo = context.seqNo(instruction)
    secChar = chr(ord('A'))
    if instruction == 'section:chapter': reflabel = text(f"Clause {seqNo}")
    elif instruction == 'section:annex': reflabel = text(f"Annex {secChar}")
    else: reflabel = seqNode
    if instruction == 'section:annex':
        label = secNumberStyle(text(f"Annex {secChar}"))
        if len(args) > 0: label += ' ' + text(f'({args[0]})')
        label += br() + content
    else: label = content
    labelrow = headerStyleAtLevel(level = context.nestLevel('section'), contents = [
        f"{secNumberStyle(seqNode)} {content}",
        pushRight(tagStyle(f'[=`[]{refid}[=`]]'))
        ])
    return labelrow

@applyTo(['#:cite@super'])
def supercite(_1):
    return '<sup>' + cite(_1) + '</sup>'

# locations
@applyTo(['%'])
def indextext(_1, **kw) -> str:
    return index[generalindex].add(_1)
@applyTo(['%@lib@raw'])
def indexlibrary(_1, **kw):
    return index[libraryindex].add(_1)
@applyTo(['%@hdr'])
def indexhdr(_1, **kw):
    return index[headerindex].add(idxhdr(_1))
@applyTo(['%@concept'])
def indexconcept(_1, **kw):
    return index[conceptindex].add(_1)
@applyTo(['%@gram'])
def indexgram(_1, **kw):
    return index[grammarindex].add(_1)
@applyTo(['%@impldef'])
def indeximpldef(_1, **kw):
    return index[impldefindex].add(_1, order = text(_1))
@applyTo(['%@defn'])
def indexdefn(_1, **kw) -> str: return indextext(_1)
def idxbfpage(_1): return f"[.textbf {_1}]"
@applyTo(['%@grammar'])
def indexgrammar(_1):
    return indextext(_1) + indexgram(_1, styler = idxbfpage)

@applyTo(['?impldef'])
def impldef(_1):
    return indeximpldef(_1) + text("implementation-defined")
@applyTo(['?impldef@plain'])
def impldefplain(_1):
    return index[impldefindex].add(_1) + text("implementation-defined")

# appearance
@applyTo(['`'], at=['%', '% !'])
def idxcode(_1:str): return {'key': _1, text: tcode(_1)}
def idxconcept(_1:str): return {'key': _1, text: tcode(_1)}
def idxexposconcept(_1:str): return {'key': _1, text: tcode(placeholder(_1))}
def idxhdr(_1:str): return {'key': _1, text: tcode(f"<{_1}>")}
@applyTo(['~'], at=['%', '% !'])
def idxgram(_1:str): return {'key': _1, text: gterm(_1)}
def idxterm(_1:str): return {'key': _1, text: term(_1)}
def idxxname(_1:str): return {'key': f"__{_1}", text: xname(_1)}

# library index entries
@applyTo(['%@lib'])
def indexlibraryglobal(_1:str): return indexlibrary(idxcode(_1))
@applyTo(['%@lib@misc'])
def indexlibrarymisc(_1:str,_2:str): return indexlibrary(idxcode(_1), sub = _2)
@applyTo(['%@lib@ctor'])
def indexlibraryctor(_1:str): return indexlibrarymisc(_1, text("constructor"))
@applyTo(['%@lib@dtor'])
def indexlibraryctor(_1:str): return indexlibrarymisc(_1, text("destructor"))
@applyTo(['%@lib@memberx'])
def indexlibrarymemberx(_1:str, _2:str): return indexlibrary(idxcode(_1), sub=idxcode(_2))
@applyTo(['%@lib@member', '%@lib@spec'])
def indexlibrarymember(_1:str, _2:str): return indexlibrarymemberx(_1, _2) + indexlibrarymemberx(_2, _1)
@applyTo(['%@lib@member@expos'])
def indexlibrarymemberexpos(_1:str, _2:str): return indexlibrarymember(_1, _2)
@applyTo(['%@lib@zombie'])
def indexlibraryzombie(_1:str): return indexlibrary(idxcode(_1), sub = text("zombie"))

@applyTo(['`:lib', '?libglobal'], within=['codeblock'])
def libglobal(_1:str): return indexlibraryglobal(_1) + _1
@applyTo(['?libmember'], within=['codeblock'])
def libmember(_1:str, _2:str): return indexlibrarymember(_1, _2) + _1
@applyTo(['?libspec'], within=['codeblock'])
def libspec(_1:str, _2:str): return indexlibrarymember(_1, _2) + _1

# index for library headers
@applyTo(['?libheader'])
def libheader(_1:str): return indexhdr(_1) + tcode(f"<{_1}>")
@applyTo(['%@hdr@def'])
def indexheader(_1:str): return index[headerindex].add(idxhdr(_1), styler=idxbfpage)
@applyTo(['?libheader@def'])
def libheaderdef(_1:str): return indexheader(_1) + tcode(f"<{_1}>")
@applyTo(['?libheader@no'])
def libnoheader(_1:str): return indextext(idxhdr(_1), sub=text("absence thereof")) + tcode(f"<{_1}>")
@applyTo(['?libheader@ref#{refid}'])
def libheaderrefx(_1:str, refid:str): return libheader(_1) + iref(refid)
@applyTo(['?libheader@ref'])
def libheaderref(_1:str): return libheaderrefx(_1, f"{_1}.syn")
@applyTo(['?libheader@ref@depr'])
def libdeprheaderref(_1:str): return libheaderrefx(_1, f"depr.{_1}.syn")

# code and definitions embedded in text.
@applyTo(['`'])
def tcode(_1:str): return f"[.texttt {_1}]"    # TODO: highlighting
@applyTo(['+:%'])
def term(_1:str): return f"[.textit {_1}]"
@applyTo(['~'], within=['%', '% !', 'codeblock'])
def gterm(_1:str): return f"[.textsf.textit {_1}]"
@applyTo(['~@fake', '~@loc', '~@fmt'])
def fakegrammarterm(_1:str): return gterm(_1)
@applyTo(['`:key', '`@def'])
def keyword(_1:str): return tcode(_1) + indextext(idxcode(_1))
@applyTo(['`@def@lib'])
def defnlib(_1:str): return tcode(_1) + indexlibrary(idxcode(_1))
@applyTo(['~'])
def grammarterm(_1:str): return indexgram(idxgram(_1)) + gterm(_1) #if not within('codeblock') else gterm(_1)
@applyTo(['~:re'])
def regrammarterm(_1:str): return f"[.textit {_1}]"
@applyTo(['^'])
def placeholder(_1:str): return f"[.textit {_1}]"    # TODO: highlighting
@applyTo(['*'])
def exposid(_1:str): return tcode(placeholder(_1))
@applyTo(['?defnxname'])
def defnxname(_1:str): return indextext(idxxname(_1)) + xname(_1)
@applyTo(['?defnxname@lib'])
def defnlibxname(_1:str): return indexlibrary(idxxname(_1)) + xname(_1)

@applyTo(['+'])
def defn(_1:str): return defnx(_1, _1)
@applyTo(['+ %'])
def defnx(_1:str, _2:str): return indexdefn(_2) + f"[.textit {_1}]"
@applyTo(['+:adj %!'])
def defnadj(_1:str, _2:str):        # TODO: multilang
    return indextext(f"{_1} {_2}", see={'key':_2, 'sub':{'key':_1}}) + \
        indexdefn(_2, sub=_1) + f"[.textit {_1} {_2}]"

@applyTo(['?brk'])
def brk(): return '[=zwsp]'
def Cpp(): return 'C++'
def CppIII(): return Cpp() + ' 2003'
def CppXI(): return Cpp() + ' 2011'
def CppXIV(): return Cpp() + ' 2014'
def CppXVII(): return Cpp() + ' 2017'
def CppXX(): return Cpp() + ' 2020'
def CppXXIII(): return Cpp() + ' 2023'
def CppXXVI(): return Cpp() + ' 2026'
def IsoCUndated(): return 'ISO/IEC 9899'
def IsoC(): return IsoCUndated() + ':2018'
def IsoFloatUndated(): return 'ISO/IEC 60559'
def IsoPosixUndated(): return 'ISO/IEC/IEEE 9945'
def IsoPosix(): return f'{IsoPosixUndated()}:2009'
def opt(_1:str): return _1 + ensuremath(fr"_\mathit{{_{text('opt')}}}")
@applyTo(['?bigoh'])
def bigoh(_1:str): return ensuremath(fr"\mathscr{{O}}({_1})")
def O(): return r'\mathscr{O}'

# States and operators
def state(_1:str, _2:str): return tcode(_1) + ensuremath(f"_{{{_2}}}")
def bitand(): return ensuremath(fr"\mathbin{{\mathsf{{bitand}}}}")
def bitor(): return ensuremath(fr"\mathbin{{\mathsf{{bitor}}}}")
def xor(): return ensuremath(fr"\mathbin{{\mathsf{{xor}}}}")
def rightshift(): return ensuremath(fr"\mathbin{{\mathsf{{rshift}}}}")
def leftshift(_1:str): return ensuremath(fr"\mathbin{{\mathsf{{lshift}}_{{{_1}}}}}")

# Notes and examples
def noteintro(_1:str): return f"[=`[][.textid {_1}]: "
def noteoutro(_1:str): return f"[.textid [=thinsp][=--][=thinsp]end {_1}]"
def note(_1, x): return noteintro(text('Note') + ' ' + (x or count(note))) + _1 + noteoutro(text('note'))
def example(_1): return noteintro(text('Example') + ' ' + count(example)) + _1 + noteoutro(text('example'))

# Library function descriptions
@applyTo(['?Fundesc'])
def Fundescx(_1:str): return f"[.textit {_1}]"
def Fundesc(_1:str): return Fundescx(_1) + ": "
def recommended(_1:str): return Fundesc(text('Recommended practice'))
def required(_1:str): return Fundesc(text('Required behavior'))
def requires(_1:str): return Fundesc(text('Requires'))
def constraints(_1:str): return Fundesc(text('Constraints'))
def mandates(_1:str): return Fundesc(text('Mandates'))
def expects(_1:str): return Fundesc(text('Preconditions'))
def effects(_1:str): return Fundesc(text('Effects'))
def ensures(_1:str): return Fundesc(text('Postconditions'))
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
def xref(_1:str): return f"[.textsc {text('See also:')} {_1}]"
def xrefc(_1:str): return xref(f'{IsoC()}, {_1}')
@applyTo(['?termref# [!]'])
def termref(_1:str, _2:str, _3:str): return f'[.textit {_2}]{_3} ({ref(_1)})'

def iref(_1:str): return f'[=nbsp]({ref(_1)})'
def tref(_1:str): return hyperref(tablerefname() + '[=nbsp]' + ref(f'tab:{_1}'), target = f'tab:{_1}')
def fref(_1:str): return hyperref(figurerefname() + '[=nbsp]' + ref(f'fig:{_1}'), target = f'fig:{_1}')

@applyTo(['span:ucode', '&:ucode'])
def ucode(_1:str): return f'[.small {_1.upper()}]'
@applyTo(['span:uname', '&:uname'])
def uname(_1:str): return f'[.textsc {_1}]'
def unicode(_1:str,_2:str): return ucode(_1) + ' ' + uname(_2)
def NTS(_1:str): return f'[.textsc {_1}]'
def ntbs(): return NTS('ntbs')
def ntmbs(): return NTS('ntmbs')

def EXPO(_1:str): return f'[.textit {_1}]'
def expos(): return EXPO(text('exposition only'))
def impdef(): return EXPO(text('implementation-defined'))
@applyTo(['?impdefx'])
def impdefx(_1): return indeximpldef(_1) + EXPO(text('implementation-defined'))
def notdef(): return EXPO(text('not defined'))

def UNSP(_1:str): return f'[.textit[.texttt {_1}]]'
def unspec(): return UNSP(text('unspecified'))
def unspecbool(): return UNSP(text('unspecified-bool-type'))
def seebelow(): return UNSP(text('see below'))
@applyTo(['?seeref#refid'])
def seeref(refid:str): return UNSP(text(f'see[=nbsp]{ref(refid)}'))
def unspecuniqtype(): return UNSP(text('unspecified unique type'))

def unun(): return '__'
def xname(_1:str): return tcode(f'__{_1}')
def mname(_1:str): return tcode(f'__{_1}__')

def commentellip(): return tcode('/* ... */')

# Concepts
def oldconceptname(_1:str): return f"Cpp17{_1}"
@applyTo(['^:oc'])
def oldconcept(_1:str): return f"[.textit Cpp17{_1}]"
@applyTo(['^:oc@def'])
def defnoldconcept(_1:str): return defn(f'Cpp17{_1}')
def idxoldconcept(_1:str): return {'key': f'Cpp17{_1}', 'text': f'[.textit Cpp17{_1}]'}
@applyTo(['^:newoc'])
def newoldconcept(_1:str): return f"[.textit {_1}]"
@applyTo(['^:newoc@def'])
def defnnewoldconcept(_1:str): return defn(_1)
def idxnewoldconcept(_1:str): return {'key': _1, 'text': f'[.textit {_1}]'}

@applyTo(['`:cname'])
def cname(_1:str): return tcode(_1)
def ecname(_1:str): return tcode(placeholder(_1))
def libconceptx(_1:str, _2:str): return cname(_1) + indexconcept(idxconcept(_2))
@applyTo(['`:c'])
def libconcept(_1:str): return libconceptx(_1, _1)
@applyTo(['`:c@def'])
def deflibconcept(_1:str):
    return cname(_1) + indexlibrary(idxconcept(_1)) \
        + indexconcept(idxconcept(_1), styler=idxbfpage)
@applyTo(['*:c'])
def exposconcept(_1:str): return ecname(_1) + indexconcept(idxexposconcept(_1))
@applyTo(['*:c@def'])
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
def mullo(): return '[.math mullo]'
def mulhi(): return '[.math mulhi]'
def cedef(): return '[.mathrel [.mathop :]=]'

class Context: pass
class ParserBase: pass

def within(*x):pass
def at(*x):pass

def section(ctx:Context): pass
def document(ctx:Context):
    def attribute(ctx:Context): pass
    ctx.expects({
        'attribute': attribute,
    })
def include(): pass
block = {
    'section': section,
    'document': document,
    'include': include,
}
def langtag(): pass
def inlinecode(): pass
# def index(): pass
def subindex(): pass
def setkey(): pass
def see(): pass
def span(): pass
#def ref(): pass
def macro(): pass
def eval(): pass
#def placeholder(): pass
def definition(): pass
def quote(): pass
#def exposid(): pass
def math(): pass
def markup(): pass
#def grammarterm(): pass
#def exposid(): pass
def comment(): pass
def syntax_alt(): pass
def table_cell(): pass
def table_row(): pass

def table(): pass
def syntax(): pass
def rule(): pass
def formula(): pass

inline = {
    ':': langtag,
    '`': inlinecode,
    '%': see if at(index) else None,
    '#': ref,
    '=': macro,
    '^': placeholder,
    '+': definition,
    '*': exposid,
    '$': math,
    '.': markup,
    '"': None, # quote
    '@': setkey if at(index, subindex) else None,
    '~': grammarterm,
    '!': subindex if at(index, subindex, see) else None,
    '&': span,
    '*': exposid,
    '-': table_row if within(table) else None,
    '/': comment,
    '|': table_cell if within(table) else syntax_alt if within(rule) else None,
    '?': eval,
    '\\': None,
    '<': None,
    '>': None,
    ';': None,
    "'": None,
    '{': None,
    '}': None,
    '_': None,
}
class Parser(ParserBase):

    def handle(self): pass
