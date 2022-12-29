<!-- markdownlint-disable no-inline-html MD050 MD038 -->
# Syntax Of Redoc

## Overview

Redoc is a markup language, all special things are in `[]`.

## Keyword Tables

### Keywords 关键字

|||||||
|-|-|-|-|-|-|
`alignas` |`alignof`|`asm`|`auto`|`bool`|`break`|
`case`|`catch`|`char`|`char8_t`|`char16_t`|`char32_t`|
`class`|`concept`|`const`|`consteval`|`constexpr`|`constinit`|
`const_cast`|`continue`|`co_await`|`co_return`|`co_yield`|`decltype`
`default`|`delete`|`do`|`double`|`dynamic_cast`|`else`|
`enum`|`explicit`|`export`|`extern`|`false`|`float`|
`for`|`friend`|`goto`|`if`|`inline`|`int`|
`long`|`mutable`|`namespace`|`new`|`noexcept`|`nullptr`|
`operator`|`private`|`protected`|`public`|`register`|`reinterpret_cast`|
`requires`|`return`|`short`|`signed`|`sizeof`|`static`|
`static_assert`|`static_cast`|`struct`|`switch`|`template`|`this`|
`thread_local`|`throw`|`true`|`try`|`typedef`|`typeid`|
`typename`|`union`|`unsigned`|`using`|`virtual`|`void`|
`volatile`|`wchar_t`|`while`

### Alternative Representations 标识符替代表示

|||||||
|-|-|-|-|-|-|
`and`| `and_eq`| `bitand`| `bitor`| `compl`| `not`
`not_eq`| `or`| `or_eq`| `xor`| `xor_eq`

### Contextual Keywords 语境关键字

|||||
|-|-|-|-|
`final`| `import`| `module`| `override`

### Preprocessing Operators 预处理运算符

|||||
|-|-|-|-|
`#`|`##`|`%:`|`%:%:`

### Operators & Punctuators 运算符和标点

||||||||||
|-|-|-|-|-|-|-|-|-|
`{`|`}`|`[`|`]`|`(`|`)`
`<:`|`:>`|`<%`|`%>`|`;`|`:`|`...`
`?`|`::`|`.`|`.*`|`->`|`->*`|`~`
`!`|`+`|`-`|`*`|`/`|`%`|`^`|`&`|`\|`
`=`|`+=`|`-=`|`*=`|`/=`|`%=`|`^=`|`&=`|`\|=`
`==`|`!=`|`<`|`>`|`<=`|`>=`|`<=>`|`&&`|`\|\|`
`<<`|`>>`|`<<=`|`>>=`|`++`|`--`|`,`

### Fold Operators 折叠运算符

||||||||||
|-|-|-|-|-|-|-|-|-|
`+` |`-` |`*` |`/` |`%` |`^` |`&` |`\|` |`<<` |`>>`
`+=`|`-=`|`*=`|`/=`|`%=`|`^=`|`&=`|`\|=`|`<<=`|`>>=`|`=`
`==`|`!=`|`<` |`>` |`<=`|`>=`|`&&`|`\|\|`|`,` |`.*` |`->*`

### 文字运算符

|||||
|-|-|-|-|
`static_cast`|`dynamic_cast`|`const_cast`|`reinterpret_cast`
`new`|`delete`|`delete[]`
`sizeof`|`sizeof...`|`alignof`
`noexcept`|`throw`|`typeid`|`requires`
`co_await`|`co_yield`

## Syntax Terms

### Lexical Convensions 词法约定

Original   |中文   |章节    |定义
|-|-|-|-|
*hex-quad*                  |*hex-四位*     | [lex.charset] | *十六进制数字* **{4}**
*universal-character-name*  |*通用字符名*   | [lex.charset] | `\u` *hex-四位* **{1,2}**
*preprocessing-token*       |*预处理记号*   | [lex.pptoken] | *头文件名* \|<br> *import-关键字* \|<br> *module-关键字* \|<br> *export-关键字* \|<br> *标识符* \|<br> *预处理数字* \|<br>*字符字面量* \|<br> *用户定义字符字面量* \| <br>*字符串字面量* \|<br> *用户定义字符串字面量* \|<br>其他所有 *通用字符名*
*token*                     |*记号*         | [lex.token]   | *标识符* \| *关键字* \| *字面量* \| *运算符或标点*
*header-name*               |*头文件名*     | [lex.header]  | `<` *h-字符序列* `>` \| `"` *q-字符序列* `"`
*h-char-sequence*           |*h-字符序列*   | [lex.header]  | *h-字符*__+__
*h-char*                    |*h-字符*       | [lex.header]  | 源字符集 - ( 换行 \| `>` )
*q-char-sequence*           |*q-字符序列*   | [lex.header]  | *q-字符*__+__
*q-char*                    |*q-字符*       | [lex.header]  | 源字符集 - ( 换行 \| `"` )
*pp-number*                 |*预处理数字*   | [lex.ppnumber]| `.`__?__ *数字* ( `.` \| *标识符继续* \| `'` (*数字* \|*非数字*) \| [`eEpP`] *正负号* )__\*__
*identifier*                |*标识符*       | [lex.name]    | *标识符开头* *标识符继续*__\*__
*identifier-start*          |*标识符开头*   | [lex.name]    | *非数字* \| *通用字符名* ∈ <XID_Start>
*identifier-continue*       |*标识符继续*   | [lex.name]    | *数字* \| *非数字* \| *通用字符名* ∈ <XID_Continue>
*nondigit*                  |*非数字*       | [lex.name]    | [`a-zA-Z_`]
*digit*                     |*数字*         | [lex.name]    | [`0-9`]
*keyword*                   |*关键字*       | [lex.key]     | *标识符* ∈ **关键字表**
*preprocessing-op-or-punc*  |*预处理运算符或标点*| [lex.operators] | *预处理运算符* \| *运算符或标点*
*preprocessing-operator*    |*预处理运算符* | [lex.operators] | `#` \| `##` \| `%:` \| `%:%:`
*operator-or-punctuator*    |*运算符或标点* | [lex.operators] | *预处理记号* ∈ **运算符和标点**
*literal*                   |*字面量*       | [lex.literal.kinds] | *整数字面量* \|<br> *字符字面量* \|<br> *浮点字面量* \|<br> *字符串字面量* \|<br> *布尔字面量* \|<br> *指针字面量* \|<br> *用户定义字面量*
*integer-literal*           |*整数字面量*   | [lex.icon]    | *二进制字面量* \| *八进制字面量* \| *十进制字面量* \| *十六进制字面量*
*binary-literal*            |*二进制字面量* | [lex.icon]    | (`0b` \| `0B`) *二进制数字* (`'`__?__ *二进制数字*)__\*__
*octal-literal*             |*八进制字面量* | [lex.icon]    | `0` (`'`__?__ *八进制数字*)__\*__
*decimal-literal*           |*十进制字面量* | [lex.icon]    | *非零数字* (`'`__?__ *数字*)__\*__
*hexadecimal-literal*       |*十六进制字面量* | [lex.icon]  | *十六进制前缀* *十六进制数字序列*
*binary-digit*              |*二进制数字*   | [lex.icon]    | [`01`]
*octal-digit*               |*八进制数字*   | [lex.icon]    | [`0-7`]
*nonzero-digit*             |*非零数字*     | [lex.icon]    | [`1-9`]
*hexadecimal-prefix*        |*十六进制前缀* | [lex.icon]    | `0x` \| `0X`
*hexadecimal-digit-sequence*|*十六进制数字序列*| [lex.icon] | *十六进制数字* (`'`__?__ *十六进制数字*)__\*__
*hexadecimal-digit*         |*十六进制数字* | [lex.icon]    | [`0-9a-fA-F`]
*integer-suffix*            |*整数后缀*     | [lex.icon]    | *unsigned-后缀* (*long-后缀* \| *long-long-后缀* \| *size-后缀*)__?__ \|<br> (*long-后缀* \| *long-long-后缀* \| *size-后缀*) *unsigned-后缀*__?__
*unsigned-suffix*           |*unsigned-后缀*| [lex.icon]    | `u` \| `U`
*long-suffix*               |*long-后缀*    | [lex.icon]    | `l` \| `L`
*long-long-suffix*          |*long-long-后缀*| [lex.icon]   | `ll` \| `LL`
*size-suffix*               |*size-后缀*    | [lex.icon]    | `z` \| `Z`
*character-literal*         |*字符字面量*   | [lex.ccon]    | *编码前缀*__?__ `'` *c-字符序列* `'`
*encoding-prefix*           |*编码前缀*     | [lex.ccon]    | `u8` \| `u` \| `U` \| `L`
*c-char-sequence*           |*c-字符序列*   | [lex.ccon]    | *c-字符*__\*__
*c-char*                    |*c-字符*       | [lex.ccon]    | *基本-c-字符* \| *转义序列* \| *通用字符名*
*basic-c-char*              |*基本-c-字符*  | [lex.ccon]    | **基本源字符集** - (`'` \| `\` \| 换行)
*escape-sequence*           |*转义序列*     | [lex.ccon]    | *简单转义序列* \| *数值转义序列* \| *有条件转义序列*
*simple-escape-sequence*    |*简单转义序列* | [lex.ccon]    | `\` *简单转义序列字符*
*simple-escape-sequence-char* |*简单转义序列字符* | [lex.ccon] | [`'"?\abfnrtv`]
*numeric-escape-sequence*   |*数值转义序列* | [lex.ccon]    | *八进制转义序列* \| *十六进制转义序列*
*octal-escape-sequence*     |*八进制转义序列*| [lex.ccon]   | `\` *八进制数字*__{1,3}__
*hexadecimal-escape-sequence*|*十六进制转义序列*| [lex.ccon]| `\x` *十六进制数字*__\+__
*conditional-escape-sequence*|*有条件转义序列*| [lex.ccon]  | `\` *有条件转义序列字符*
*conditional-escape-sequence-char*|*有条件转义序列字符*|[lex.ccon]| **基本源字符集** - ([`0-9'"?\abfnrtvuUx`])
*floating-point-literal*    |*浮点字面量*   | [lex.fcon]    | *十进制浮点字面量* \| *十六进制浮点字面量*
*decimal-floating-point-literal* |*十进制浮点字面量*|[lex.fcon]| (*小数常量* *指数部分*__?__ \| *数字序列* *指数部分*) *浮点后缀*__?__
*hexadecimal-floating-point-literal*|*十六进制浮点字面量*|[lex.fcon]| *十六进制前缀* (*十六进制小数常量* \| *十六进制数字序列*) *二进制指数部分* *浮点后缀*__?__
*fractional-constant*       |*小数常量*     | [lex.fcon]    | *数字序列*__?__ `.` *数字序列* \| *数字序列* `.`
*hexadecimal-fractional-constant*|*十六进制小数常量*|[lex.fcon]| *十六进制数字序列*__?__ `.` *十六进制数字序列* \| *十六进制数字序列* `.`
*exponent-part*             |*指数部分*     | [lex.fcon]    | [`eE`] *正负号*__?__ *数字序列*
*binary-exponent-part*      |*二进制指数部分*| [lex.fcon]   | [`pP`] *正负号*__?__ *数字序列*
*sign*                      |*正负号*       | [lex.fcon]    | [`+-`]
*digit-sequence*            |*数字序列*     | [lex.fcon]    | *数字* (`'`__?__ *数字*)__*__
*floating-point-suffix*     |*浮点后缀*     | [lex.fcon]    | [`flFL`]
*string-literal*            |*字符串字面量* | [lex.string]  | *编码前缀*__?__ (`"` *s-字符序列*__?__ `"` \| `R` *原始字符串*)
*s-char-sequence*           |*s-字符序列*   | [lex.string]  | *s-字符*__+__
*s-char*                    |*s-字符*       | [lex.string]  | *基本-s-字符* \| *转义序列* \| *通用字符名*
*basic-s-char*              |*基本-s-字符*  | [lex.string]  | **基本源字符集** - (`"` \| `\` \| 换行)
*raw-string*                |*原始字符串*   | [lex.string]  | `"` *d-字符序列*__?__ `(` *r-字符序列* `)` *d-字符序列*__?__ `"`
*r-char-sequence*           |*r-字符序列*   | [lex.string]  | *r-字符*__+__
*r-char*                    |*r-字符*       | [lex.string]  | **源字符集** - (`)` *d-字符序列*__?__ `"`)
*d-char-sequence*           |*d-字符序列*   | [lex.string]  | *d-字符*__+__
*d-char*                    |*d-字符*       | [lex.string]  | **源字符集** - ([` ()\`] \| **控制字符**)
*boolean-literal*           |*布尔字面量*   | [lex.bool]    | `false` \| `true`
*pointer-literal*           |*指针字面量*   | [lex.nullptr] | `nullptr`
*user-defined-literal*      |*用户定义字面量*| [lex.ext]    | *用户定义整数字面量* \|<br> *用户定义浮点字面量* \|<br> *用户定义字符串字面量* \|<br> *用户定义字符字面量*
*user-defined-integer-literal*|*用户定义整数字面量*|[lex.ext]| (*十进制字面量* \| *八进制字面量* \| *十六进制字面量* \| *二进制字面量*) *ud-后缀*
*user-defined-floating-point-literal*|*用户定义浮点字面量*|[lex.ext]| (*小数常量* *指数部分*__?__ \| *数字序列* *指数部分* \| *十六进制前缀* (*十六进制小数常量* \| *十六进制数字序列*) *二进制指数部分*) *ud-后缀*
*user-defined-string-literal*|*用户定义字符串字面量*|[lex.ext]| *字符串字面量* *ud-后缀*
*user-defined-character-literal*|*用户定义字符字面量*|[lex.ext]| *字符字面量* *ud-后缀*
*ud-suffix*                 |*ud-后缀*      | [lex.ext]     | *标识符*

### Basics 基本概念

Original   |中文   |章节    |定义
|-|-|-|-|
*translation-unit*          |*翻译单元*     | [basic.link]  | *声明式序列* \|<br> *全局模块分段*__?__ *模块声明式* *声明式序列*__?__ *私有模块分段*__?__

### Expressions 表达式

Original   |中文   |章节    |定义
|-|-|-|-|
*primary-expression*        |*初等表达式*   | [expr.prim]   | *字面量* \|<br> `this` \|<br> `(` *表达式* `)` \|<br> *标识表达式* \|<br> *lambda-表达式* \|<br> *折叠表达式* \|<br> *requires-表达式*
*id-expression*             |*标识表达式*   | [expr.prim.id.general] | *无限定标识* \| *限定标识*
*unqualified-id*            |*无限定标识*   | [expr.prim.id.unqual] | *标识符* \|<br> *运算符函数标识* \|<br> *转换函数标识* \|<br> *字面量运算符标识* \|<br> `~` *类型名* \|<br> `~` *decltype-说明符* \|<br> *模板标识*
*qualified-id*              |*限定标识*     | [expr.prim.id.qual] | *嵌套名说明符* `template`__?__ *无限定标识*
*nested-name-specifier*     |*嵌套名说明符* | [expr.prim.id.qual] | ( ∅ \| *类型名* \| *命名空间名* \| *decltype-说明符* ) `::` ( ( *标识符* \| `template`__?__ *简单模板标识* ) `::`)__*__
*lambda-expression*         |*lambda-表达式*| [expr.prim.lambda.general] | *lambda-引导符* ( ∅ \| `<` *模板形参列表* `>` *requires-子句*__?__ ) *lambda-声明符* *复合语句*
*lambda-introducer*         |*lambda-引导符*| [expr.prim.lambda.general] | `[` *lambda-俘获式*__?__ `]`
*lambda-declarator*         |*lambda-声明符*| [expr.prim.lambda.general] | *lambda-说明符序列* \|<br>`(` *形参声明子句* `)` *lambda-说明符序列* *requires-子句*__?__
*lambda-specifiers*         |*lambda-说明符序列*|[expr.prim.lambda.general]| *声明说明符序列*__?__ *noexcept-说明符*__?__ *属性说明符序列*__?__ *尾部返回类型*__?__
*lambda-capture*            |*lambda-俘获式*| [expr.prim.lambda.capture] | *默认俘获符* \| (*默认俘获符* `,`)__?__ *俘获符列表*
*capture-default*           |*默认俘获符*   | [expr.prim.lambda.capture] | `&` \| `=`
*capture-list*              |*俘获符列表*   | [expr.prim.lambda.capture] | *俘获符* ( `,` *俘获符* )__*__
*capture*                   |*俘获符*       | [expr.prim.lambda.capture] | *简单俘获符* \| *带初始化俘获符*
*simple-capture*            |*简单俘获符*   | [expr.prim.lambda.capture] | `&`__?__ *标识符* `...`__?__ \| `*`__?__ `this`
*init-capture*              |*带初始化俘获符*| [expr.prim.lambda.capture] | `&`__?__ `...`__?__ *标识符* *初始化式*
*fold-expression*           |*折叠表达式*   | [expr.prim.fold] | `(` *转型表达式* *折叠运算符* `...` `)` \|<br> `(` `...` *折叠运算符* *转型表达式* `)` \|<br> `(` *转型表达式* *折叠运算符* `...` *折叠运算符* *转型表达式* `)`
*fold-operator*             |*折叠运算符*   | [expr.prim.fold] | *预处理记号* ∈ **折叠运算符**
*requires-expression*       |*requires-表达式*| [expr.prim.req.general] | `requires` *规定形参列表*__?__ *规定体*
*requirement-parameter-list*|*规定形参列表* | [expr.prim.req.general] | `(` *形参声明子句* `)`
*requirement-body*          |*规定体*       | [expr.prim.req.general] | `{` *规定序列* `}`
*requirement-seq*           |*规定序列*     | [expr.prim.req.general] | *规定*__+__
*requirement*               |*规定*         | [expr.prim.req.general] | *简单规定* \| *类型规定* \| *复合规定* \| *嵌套规定*
*simple-requirement*        |*简单规定*     | [expr.prim.req.simple] | *表达式* `;`
*type-requirement*          |*类型规定*     | [expr.prim.req.type] | `typename` *嵌套名说明符*__?__ *类型名* `;`
*compound-requirement*      |*复合规定*     | [expr.prim.req.compound] | `{` *表达式* `}` `noexcept`__?__ *返回类型规定*__?__ `;`
*return-type-requirement*   |*返回类型规定* | [expr.prim.req.compound] | `->` *返回约束*
*nested-requirement*        |*嵌套规定*     | [expr.prim.req.nested] | `requires` *约束表达式* `;`
*postfix-expression*        |*后缀表达式*   | [expr.post.general] | *初等表达式* \|<br> *后缀表达式* `[` *表达式或花括号初始化列表* `]` \|<br> *后缀表达式* `(` *表达式列表*__?__ `)` \|<br> (*简单类型说明符* \| *typename-说明符*) (`(` *表达式列表*__?__ `)` \| *花括号初始化列表*) \|<br> *后缀表达式* (`.`\|`->`) `template`__?__ *标识表达式* \|<br> *后缀表达式* (`++`\|`--`) \|<br> (`dynamic_cast`\|`static_cast`\|`reintepret_cast`\|`const_cast`) `<` *类型标识* `>` \|<br> `typeid` `(` (*表达式*\|*类型标识*) `)`
*expression-list*           |*表达式列表*   | [expr.post.general] | *初始化式列表*
*unary-expression*          |*一元表达式*   | [expr.unary.general] | *后缀表达式* \|<br> (*一元运算符*\|`++`\|`--`) *转型表达式* \|<br> *等待表达式* \|<br> `sizeof` (*一元表达式* \| `(` *类型标识* `)` \| `...` `(` *标识符* `)`) \|<br> `alignof` `(` *类型标识* `)` \|<br> *noexcept-表达式* \|<br> *new-表达式* \|<br> *delete-表达式*
*unary-operator*            |*一元运算符*   | [expr.unary.general] | `*` \| `&` \| `+` \| `-` \| `!` \| `~`
*await-expression*          |*等待表达式*   | [expr.await]  | `co_await` *转型表达式*
*new-expression*            |*new-表达式*   | [expr.new]    | `::`__?__ `new` *new-放置* (*new-类型标识* \| `(` *类型标识* `)`) *new-初始化式*__?__
*new-placement*             |*new-放置*     | [expr.new]    | `(` *表达式列表* `)`
*new-type-id*               |*new-类型标识* | [expr.new]    | *类型说明符序列* *new-声明符*__?__
*new-declarator*            |*new-声明符*   | [expr.new]    | *指针运算符*__\*__ *非指针-new-声明符*__?__
*noptr-new-declarator*      |*非指针-new-声明符*| [expr.new] | `[` *表达式*__?__ `]` *属性说明符序列*__?__ (`[` *常量表达式* `]` *属性说明符序列*__?__)__\*__
*new-initializer*           |*new-初始化式* | [expr.new]    | `(` *表达式列表*__?__ `)` \| *带花括号初始化列表*
*delete-expression*         |*delete-表达式*| [expr.delete] | `::`__?__ `delete` (`[` `]`)__?__ *转型表达式*
*cast-expression*           |*转型表达式*   | [expr.cast]   | ( `(` *类型标识* `)` )__\*__ *一元表达式*
*pm-expression*             |*成员指针表达式*| [expr.mptr.oper] | ( *转型表达式* (`.*`\|`->*`) )__\*__ *转型表达式*
*multiplicative-expression* |*乘性表达式*   | [expr.mul]    | ( *成员指针表达式* (`*`\|`/`\|`%`))__\*__ *成员指针表达式*
*additive-expression*       |*加性表达式*   | [expr.add]    | *乘性表达式* ((`+`\|`-`) *乘性表达式*)__\*__
*shift-expression*          |*移位表达式*   | [expr.shift]  | *加性表达式* ((`<<`\|`>>`) *加性表达式*)__\*__
*compare-expression*        |*比较表达式*   | [expr.spaceship] | *移位表达式* (`<=>` *移位表达式*)__\*__
*relational-expression*     |*关系表达式*   | [expr.rel]    | *比较表达式* ((`<`\|`>`\|`<=`\|`>=`) *比较表达式*)__\*__
*equality-expression*       |*相等性表达式* | [expr.eq]     | *关系表达式* ((`==`\|`!=`) *关系表达式*)__\*__
*and-expression*            |*与表达式*     | [expr.bit.and] | *相等性表达式* (`&` *相等性表达式*)__\*__
*exclusive-or-expression*   |*异或表达式*   | [expr.xor]    | *与表达式* (`^` *与表达式*)__\*__
*or-expression*             |*或表达式*     | [expr.or]     | *异或表达式* (`|` *异或表达式*)__\*__
*logical-and-expression*    |*逻辑与表达式* | [expr.log.and] | *或表达式* (`&&` *或表达式*)__\*__
*logical-or-expression*     |*逻辑或表达式* | [expr.log.or] | *逻辑与表达式* (`||` *逻辑与表达式*)__\*__
*conditional-expression*    |*条件表达式*   | [expr.cond]   | *逻辑或表达式* (*逻辑或表达式* `?` *表达式* `:` *赋值表达式*)__?__
*yield-expression*          |*产出表达式*   | [expr.yield]  | `co_yield` (*赋值表达式* \| *花括号初始化列表*)
*throw-expression*          |*throw-表达式* | [expr.throw]  | `throw` *赋值表达式*__?__
*assignment-expression*     |*赋值表达式*   | [expr.ass]    | *条件表达式* \| *产出表达式* \| *throw-表达式* \|<br> *逻辑或表达式* *赋值运算符* *初始化式子句*
*assignment-operator*       |*赋值运算符*   | [expr.ass]    | `=` \| `*=` \| `/=` \| `%=` \| `+=` \| `-=` \| `>>=` \| `<<=` \| `&=` \| `^=` \| `\|=`
*expression*                |*表达式*       | [expr.comma]  | *赋值表达式* (`,` *赋值表达式*)__\*__
*constant-expression*       |*常量表达式*   | [expr.const]  | *条件表达式*

### Statements 语句

Original   |中文   |章节    |定义
|-|-|-|-|
*statement*                 |*语句*         | [stmt.pre]    | *带标号语句* \|<br> *属性说明符序列*__?__ *表达式语句* \|<br> *属性说明符序列*__?__ *复合语句* \|<br> *属性说明符序列*__?__ *选择语句* \|<br> *属性说明符序列*__?__ *循环语句* \|<br> *属性说明符序列*__?__ *跳转语句* \|<br> *声明语句* \|<br> *属性说明符序列*__?__ *try-块*
*init-statement*            |*初始化语句*   | [stmt.pre]    | *表达式语句* \| *简单声明式*
*condition*                 |*条件*         | [stmt.pre]    | *表达式* \|<br> *属性说明符序列*__?__ *声明说明符序列* *声明符* *花括号或等号初始化式*
*labeled-statement*         |*带标号语句*   | [stmt.label]  | *属性说明符序列*__?__ (*标识符* \| `case` *常量表达式* \| `default` ) `:` *语句*
*expression-statement*      |*表达式语句*   | [stmt.expr]   | *表达式*__?__ `;`
*compound-statement*        |*复合语句*     | [stmt.block]  | `{` *语句序列*__?__ `}`
*statement-seq*             |*语句序列*     | [stmt.block]  | *语句*__\+__
*selection-statement*       |*选择语句*     | [stmt.select.general] | `if` `constexpr`__?__ `(` *初始化语句*__?__ *条件* `)` *语句* (`else` *语句*)__?__ \|<br>`if` `!`__?__ `consteval` *复合语句* (`else` *语句*)__?__ \|<br> `switch` `(` *初始化语句*__?__ *条件* `)` *语句*
*iteration-statement*       |*循环语句*     | [stmt.iter.general] | `while` `(` *条件* `)` *语句* \|<br> `do` *语句* `while` `(` *表达式* `)` `;` \|<br> `for` `(` *初始化语句* *条件*__?__ `;` *表达式*__?__ `)` *语句* \|<br> `for` `(` *初始化语句*__?__ *for-范围声明式* `:` *for-范围初始化式* `)` *语句*
*for-range-declaration*     |*for-范围声明式*| [stmt.iter.general] | *属性说明符序列*__?__ *声明说明符序列* *声明符* \|<br> *属性说明符序列*__?__ *声明说明符序列* *引用限定符*__?__ `[` *标识符列表* `]`
*for-range-initializer*     |*for-范围初始化式*| [stmt.iter.general] | *表达式或花括号初始化列表*
*jump-statement*            |*跳转语句*     | [stmt.jump.general] | `break` `;` \| `continue` `;` \|<br> `return` *表达式或花括号初始化列表*__?__ `;` \| *协程返回语句* \|<br> `goto` *标识符* `;`
*coroutine-return-statement*|*协程返回语句* | [stmt.return.coroutine] | `co_return` *表达式或花括号初始化列表*__?__ `;`
*declaration-statement*     |*声明语句*     | [stmt.dcl]    | *块声明式*

### Declarations 声明

Original   |中文   |章节    |定义
|-|-|-|-|
*declaration-seq*           |*声明式序列*   | [dcl.pre]     | *声明式*__\+__
*declaration*               |*声明式*       | [dcl.pre]     | *块声明式* \| *无声明说明符函数声明式* \| *函数定义式* \|<br> *模板声明式* \| *推断导引* \| *显式实例化式* \| *显式特化式* \|<br> *导出声明式* \| *连接说明* \| *命名空间定义式* \|<br> *空声明式* \| *属性声明式* \| *模块导入声明式*
*block-declaration*         |*块声明式*     | [dcl.pre]     | *简单声明式* \| *asm-声明式* \| *命名空间别名定义式* \|<br> *using-声明式* \| *using-枚举声明式* \| *using-指令* \|<br> *static_assert-声明式* \| *别名声明式* \| *笼统枚举声明式*
*nodeclspec-function-declaration*|*无声明说明符函数声明式*| [dcl.pre] |*属性说明符序列*__?__ *声明符* `;`
*alias-declaration*         |*别名声明式*   | [dcl.pre]     | `using` *标识符* *属性说明符序列*__?__ `=` *定义类型标识* `;`
*simple-declaration*        |*简单声明式*   | [dcl.pre]     | *声明说明符序列* *带初始化声明符列表*__?__ `;` \|<br> *属性说明符序列* *声明说明符序列* *带初始化声明符列表* `;` \|<br> *属性说明符序列*__?__ *声明说明符序列* *引用限定符*__?__ `[` *标识符列表* `]` 初始化式 `;`
*empty-declaration*         |*空声明式*     | [dcl.pre]     | `;`
*attribute-declaration*     |*属性声明式*   | [dcl.pre]     | *属性说明符序列* `;`
*decl-specifier*            |*声明说明符*   | [dcl.spec.general] | *存储类说明符* \| *定义类型说明符* \| *函数声明符* \|<br> `friend` \| `typedef` \| `constexpr` \| `consteval` \| `constinit` \| `inline`
*decl-specifier-seq*        |*声明说明符序列*| [dcl.spec.general] | *声明说明符*__\+__ *属性说明符序列*__?__
*storage-class-specifier*   |*存储类说明符* | [dcl.stc]     | `static` \| `thread_local` \| `extern` \| `mutable`
*function-specifier*        |*函数声明符*   | [dcl.fct.spec] | `virtual` \| `explicit` \| `explicit` `(` *常量表达式* `)`
*typedef-name*              |*typedef-名*   | [dcl.typedef] | *标识符* \| *简单模板标识*
*type-specifier*            |*类型说明符*   | [dcl.type.general] | *简单类型说明符* \| *详述类型说明符* \| *typename-说明符* \| *cv-限定符*
*type-specifier-seq*        |*类型说明符序列*| [dcl.type.general] | *类型说明符*__\+__ *属性说明符序列*__?__
*defining-type-specifier*   |*定义类型说明符*| [dcl.type.general] | *类型说明符* \| *类说明符* \| *枚举说明符*
*defining-type-specifier-seq*|*定义类型说明符序列*| [dcl.type.general] | *定义类型说明符*__\+__ *属性说明符序列*__?__

## Terms Translation Table

### A

|English|中文|说明|
|-|-|-|
abstract class                          |抽象类     |包含纯虚函数
abstract machine                        |抽象机器
access                                  |访问       |读取或改动标量对象
access check                            |访问检查
access control                          |访问控制
access specifier                        |访问说明符
acquire                                 |获取       |同步操作
active member                           |活跃成员
active variable                         |活跃变量   |自动存储期变量在作用域中其声明符之后均活跃
addition operator                       |加法运算符
additive expression                     |加性表达式 |`mul_expr + mul_expr`, `mul_expr - mul_expr`。内建：一般算术转换，指针+/-整型，指针-指针（`ptrdiff_t`）
additive operator                       |加性运算符 |`+`, `-`
address                                 |地址
address-of operator                     |取地址运算符   |一元运算符/表达式，`&`，结果为指针或成员指针，不支持位字段<br>成员指针必须为限定标识且无括号，不考虑`mutable`<br>函数：根据语境进行重载决议
aggregate                               |聚合，聚合对象
aggregate initialization                |聚合初始化
aggregate type                          |聚合类型
algorithm                               |算法
alias                                   |别名
alias declaration                       |别名声明   |`using A=T`，与`typedef`语义相同<br>`template<...> using A=...`，别名模板，不可定义类或枚举
alias template                          |别名模板
alignment                               |对齐
alignment requirement                   |对齐要求   |类型给出的地址对齐要求
alignment specifier                     |对齐说明符 |`alignas`
`alignof` expression                    |`alignof` 表达式|一元表达式。整型常量表达式。`alignof(T)`完整类型的对齐要求
allocate                                |分配
allocated type                          |被分配类型 |new 表达式创建对象的类型：完整对象类型，非抽象类或其数组，可cv
allocation function                     |分配函数   |`operator new`, `operator new []`
alternative token                       |代用记号   |二联符+保留字 `and` 等，11个位和逻辑运算符
ambiguity                               |歧义
amendment                               |文档修订
amortized constant                      |摊销常量
and expression                          |与表达式   |`eq_expr & eq_expr`。内建：按位与，一般算术转换
and operator                            |与运算符   |`&`
appearance-ordered before               |按表现顺序早于 |静态变量初始化顺序：同一UT或UT间接口依赖+出现顺序
apply                                   |运用，实施，适用于
arbitrary-positional stream             |可任意定位流   |可seek
architecture                            |体系结构
argument                                |实参，实际参数 |函数，函数式宏，模板，throw
argument-dependent name lookup          |依赖于实参的名字查找   |调用无限定函数时查找函数的过程：<br>1. 先查找局部声明或类成员，或者非函数，<br>2. 然后查找：关联命名空间成员，关联实体的友元，与关联实体附属于相同模块
arithmetic                              |算术的
arithmetic exception                    |算术异常
arithmetic type                         |算术类型       |整型、浮点
array                                   |数组
array declarator                        |函数声明符
array delete expression                 |数组 delete 表达式|`delete [] p`
array element                           |数组元素
array of N T                            |T 的 N 元素数组
array of unknown bound of T             |T 的边界未知数组
array-to-pointer conversion             |数组向指针转换 |TempMatC
arrow operator                          |箭头运算符
as-if rule                              |“如同”规则     |以可观察行为为准
asm definition                          |asm 定义式
assembler                               |汇编器，汇编
assertion                               |断言
assignment                              |赋值
assignment expression                   |赋值表达式     |`ass_expr @= v`。内建：rhs SeqB lhs SeqB 赋值 SeqB 表达式结果<br>摒弃向volatile赋值。rhs隐式转换为lhs类型<br>支持花括号传参
assignment operator                     |赋值运算符     |`=`，组合赋值：乘、加、移位、按位
associated character encoding           |关联字符编码   |字符或字符串字面量前缀指定的编码，无前缀的不可编码或多字符类型为 `int`
associated class                        |关联类
associated entities                     |关联实体       |依赖于实参查找中为实参类型确定的实体集合：<br>- 类或枚举：自身，外围类，基类<br>- 类模板特例：模板类型实参的关联实体，模板模板实参的模板及其外围类<br>- 指针、数组、函数、成员指针：目标类型，被指类，形参和返回类型的关联实体<br>- 实参为重载集合：取并集，+模板类型实参的关联实体
associated namespace                    |关联命名空间   |依赖于实参查找中确定的查找范围：每个关联实体的所在内层（非内联）命名空间（及其所有内联）
atomic                                  |原子性
attach to module                        |附属于模块
attribute                               |属性标注，属性 |`[[]]`语法，支持名字空间。<br>位置：声明式之前影响所有实体，类型说明符之后影响类型，标识之后影响实体
attribute-declaration                   |属性声明式     |仅有属性的空声明，不是块声明式
automatic storage duration              |自动存储期
await-expression                        |等待表达式     |一元表达式。暂停协程等待操作数计算完成<br>不能在`catch`中等待<br>对显式`co_await`：尝试调用承诺的`await_transform`，尝试调用`operator await`，获得可等待对象<br>`await_ready`查询是否需暂停，`await_suspend`实施暂停（支持串联），`await_resume`获得结果
awaitable                               |可等待体

### B

|English|中文|说明|
|-|-|-|
backslash                               |反斜杠     |`\`，用于转义，行拼接等
barrier                                 |关卡
base characteristic                     |基础特征
base-2 representation                   |以 2 为基的表示    |整数的二进制值表示
base N integer                          |以 N 为基的整数    |进制
basic character set                     |基本字符集
basic execution character set           |基本执行字符集 |96基本源字符 + `\a`, `\b`, `\r`, `\0`
basic execution wide-character set      |基本执行宽字符集
basic source character set              |基本源字符集   |只有96个字符，至少兼容 ASCII 和 EBCDIC
behavior                                |行为
belong                                  |属于（作用域） |实体属于其声明式的目标作用域
binary                                  |二进制，二元
binary fold                             |二元折叠       |展开包组和一个表达式
binary left fold                        |二元左折叠     |`expr op ... op pack`
binary operator                         |二元运算符
binary right fold                       |二元右折叠     |`pack op ... op expr`
bit                                     |位
bit-field                               |位字段         |一种实体
bitwise and operator                    |按位与运算符
bitwise negation operator               |按位反运算符   |一元运算符/表达式，`~`，整型、无作用域枚举，提升
bitwise or operator                     |按位或运算符
bitwise xor operator                    |按位亦或运算符
block                                   |1. 代码块 <br>2. 阻塞
block-declaration                       |块声明式       |可作为语句的声明式：声明变量或函数的，引入现有实体名字或类型前向声明的，执行运算的（asm、静态断言），不包括空声明式，不允许函数定义和模板
block scope                             |块作用域       |作用域的一种，包含执行代码的代码块：块语句，选择、循环及其子语句，`catch(){}`的整体
block statement                         |块语句         |语句的一种，`{}`
block variable                          |块变量         |块作用域的变量
block with forward progress guarantee delegation |带有向前进展保证委托的阻塞|线程阻塞于线程集合全部完成，保证至少一个线程不比被阻塞线程弱，即确保总保证不会减弱
boolean                                 |布尔
boolean conversion                      |布尔转换       |0->`false`, 非0->`true`
boolean literal                         |布尔字面量     |`true`, `false`，类型为`bool`
bound                                   |（名字）绑定   |（除友元和限定名外）声明式在其目标作用域中与名字绑定，<br>块的外部声明式在直接作用域中绑定，<br>无作用域枚举符/匿名联合成员在父作用域中绑定，<br>注入类名
break statement                         |break 语句     |跳出到循环或switch之后
built-in operator                       |内建运算符
byte                                    |字节           |基本存储单元

### C

|English|中文|说明|
|-|-|-|
cache                                   |高速缓存
call                                    |调用
call by reference                       |按引用调用     |按引用传递参数
call by value                           |按值调用       |按值传递参数
capture                                 |俘获，俘获符   |俘获符：语法结构，代表闭包数据成员，可指定初始化
capture by copy                         |按复制俘获
capture by reference                    |按引用俘获
capture-default                         |默认俘获符
carry a dependency to                   |传递依赖给 CDep|其值被后者所用（直接，或按顺序写+读）时<br>短路（逻辑、条件、逗号）和`kill_dependency`打破依赖<br>传递依赖是按顺序早于的子集
case label                              |case 标号
cast                                    |转型，类型强制转换
cast away constness                     |强制移除常量性
cast expression                         |转型表达式     |`(T)unary-expr`。可为`const_cast`，`static_cast`，`reinterpret_cast`的组合效果<br>`D*`到`B*`忽略访问性检查。不完整类型指针转型可能因MI而UB
catch                                   |捕获
character                               |字符
character container type                |字符容器类型   |`basic_string`等模板的类型形参
character encoding                      |字符编码
character literal                       |字符字面量     |预处理记号，也是记号，支持编码前缀，转义序列
character set                           |字符集
class                                   |类
class declaration                       |类声明式
class definition                        |类定义式
class granding friendship               |授予友元关系
class-head                              |类头           |类定义式中花括号前的部分
class member                            |类成员         |一种实体
class member access expression          |类成员访问表达式 |后缀表达式。`a.idexpr`，`p->idexpr`
class member access operator            |类成员访问运算符 |内建：`p->m`=>`(*p).m`
class-name                              |类名       |标识符或简单模板标识
class scope                             |类作用域   |作用域的一种，包括类成员说明，加上体外带限定成员
class-specifier                         |类说明符   |类的定义体
class template deduction                |类模板推断
class template                          |类模板
clause                                  |子句
closure object                          |闭包对象   |lambda表达式纯右值
closure type                            |闭包类型   |lambda表达式对象的类型，匿名唯一化，捕获为成员，重载`()`，函数指针转换
co_await expression                     |co_await 表达式
co_return statement                     |co_return 语句 |等价于`{p.return_value(initor); goto final_suspend;}`，void时为`p.return_void()`<br>协程无`co_return`相当于无参`co_return`
co_yield expression                     |co_yield 表达式
code point                              |代码点     |字符在字符集中的数值
coherence requirements                  |协调性规定 |写-写、写-读、读-写、读-读协调性
collating element                       |校排元素   |一些语言中会将多个字符合并当做一个字符校排
comma operator                          |逗号运算符 |`ass_expr, ass_expr`。内建：lhs SeqB rhs，左侧其值。
comment                                 |注释       | `/* */`，`// \n`
common initial sequence                 |共同起始序列
common type                             |公共类型
compare expression                      |比较表达式 |`shift_expr <=> shift_expr`。内建：算术类型进行一般算术转换，禁止bool混合，禁止除整型到浮点外的窄化<br>整型`strong_ordering`，浮点`partial_ordering`，以合成指针类型比较指针，可比较时为`strong_ordering`
compile                                 |编译
complete-class context                  |完整类语境 |在类说明符之内需要将类当做完整类型的语境，如内联代码部分
complete object                         |完整对象   |不是子对象的对象
complete type                           |完整类型
compliance                              |遵从性
component                               |组件
component name                          |成分名     |无限定标识：名字、类型名、模板标识部分<br>限定标识：各嵌套名和无限定标识的成分名
composite pointer type                  |组合指针类型   |兼容两个指针操作数的指针类型
compound assignment expression          |复合赋值表达式
compound assignment operator            |复合赋值运算符 |乘：`*/%`，加：`+-`，移位：`<<>>`，按位：`&^|`
compound requirement                    |复合规定   |`{ expr } noexcept -> T;`
compound statement                      |复合语句   |块语句，语句块，花括号。块作用域
compound type                           |复合类型   |数组、函数、指针、引用、类、联合体、枚举、成员指针
concept                                 |概念
concept-definition                      |概念定义式 |定义概念时模板头后面的部分，决定概念语义
concurrency                             |并发性
concurrent                              |并发的
concurrent foreward progress guarantees |并发向前进展保证   |实现保证线程终将有进展，无关其他线程
condition                               |条件       |语法结构：if/while/switch/for中的条件部分。非switch：Ctx2Bool，switch：Ctx2Int+IntP<br>不能声明函数、数组，不能定义类、枚举。仅允许constexpr说明符
conditional escape sequence             |有条件转义序列 |编译器实现支持的其他单字符转移序列
conditional expression                  |条件表达式     |`logor_expr ? expr : asgn_expr`。操作数1 Ctx2Bool，短路，支持`throw`，支持两个同类型位字段<br>类型不同时，尝试隐式转换为另一个，但不允许歧义<br>部分保留左值性。右值时进行一般算术转换或取合成指针类型
conditional inclusion                   |条件包含       |预处理，`#if`，`#ifdef` 等
conditional operator                    |条件运算符     |`?:`。不可重载
conditionally-supported                 |有条件支持的   |编译器实现可以选择不支持
conflict                                |冲突           |两个求值至少一个改动
conformance requirements                |一致性规定
conjunction                             |合取
const_cast                              |const 转型
const cast expression                   |const 转型表达式 |后缀表达式，`const_cast<T>(v)`<br>Ptr=>T*，Lv=>T&，GLv=>T&&，类PRv=>T&&（临时对象）
const object                            |const 对象     |const T 的对象或其非 mutable 子对象
const-qualified                         |const 限定的
const safety                            |const 安全性
const volatile object                   |const volatile 对象    |const volatile T 的对象、const T 的 volatile 子对象、volatile T 的 const 子对象，非 mutable
const-volatile-qualified                |const volatile 限定的
constant                                |常量
constant destruction                    |常量销毁       |非类类型，或具有constexpr析构函数且销毁为核心常量表达式
constant expression                     |常量表达式     |PRv核心常量表达式：所有引用也为常量，指针具有静态存储期地址，排除直接函数的地址<br>GLv核心常量表达式：静态存储期非临时对象或常量临时对象，非直接函数
constant initialization                 |常量初始化     |静态/线程变量或临时对象以常量初始化<br>运行时直接具有初始化结果
constant-initialized                    |以常量初始化   |变量或临时对象的初始化的全表达式是常量表达式，允许调用constexpr构造函数
constant initializer                    |常量初始化式
constant subexpression                  |常量子表达式   |不妨碍其外围表达式成为核心常量表达式
consteval if statement                  |consteval if 语句  |`if constval { ... }`，`if !consteval`，检测显然常量求值
consteval specifier                     |consteval 说明符   |仅修饰函数，隐含内联，非析构函数、new或delete
constexpr constructor                   |constexpr 构造函数 |除函数规定外，隐含调用的所有构造函数应为constexpr
constexpr destructor                    |constexpr 析构函数 |除函数规定外，隐含调用的所有析构函数应为constexpr
constexpr function                      |constexpr 函数     |以`constexpr`或`consteval`修饰的函数<br>字面量类型，非协程；代码中无goto、静态或线程变量；构造或析构的类无虚基类<br>不可能常量求值则非良构但无须诊断
constexpr if statement                  |constexpr if 语句  |`if constexpr (cond) ...`，检测编译期常量
constexpr specifier                     |constexpr 说明符   |修饰变量或函数，隐含内联
constinit specifier                     |constinit 说明符   |修饰静态或线程存储期的变量，保证静态初始化
constituent expression                  |成分表达式     |表达式、初始化式等结构中的各表达式
constness                               |常量性
construct                               |语言构造
constructor                             |构造函数
consume                                 |消费           |同步操作
container                               |容器
context                                 |语境，上下文
contextually converted to bool          |按语境转换为 bool  |IFF可声明`bool t(e);`
contextually implicitly converted to T  |按语境隐式转换为 T |IFF找到表达式类型C向语句可接受的类型T的非显式转换函数，且T唯一
contextual keyword                      |语境关键字，上下文关键字   |仅在特定语境中具有特殊含义：`final` `override` `import` `module`
continue statement                      |continue 语句  |跳出到循环末尾继续循环
contravariant                           |逆变
control character                       |控制字符       |代码点 0-1F，7F-9F
conversion                              |类型转换，转换
conversion function                     |转换函数
conversion-function-id                  |转换函数标识   |`operator T`
conversion rank                         |转换等级
converted constant expression           |经转换的常量表达式
converting constructor                  |转换构造函数
copy                                    |复制，副本
copy assignment operator                |复制赋值运算符
copy constructor                        |复制构造函数
copy-initialization                     |复制初始化
core constant expression                |核心常量表达式 |排除：常量外的`this`和虚函数，非constexpr函数，未定义或不满足要求的constexpr函数，UB，volatile，reinterpret_cast，lambda中ODR，非全局且配对的分配/回收，协程，throw，RTTI，asm，va_arg
coroutine                               |协程
corresponding declarations              |对应声明式     |引入相同名字的声明式，排除：其一为using，其一为类型，或二者为不同签名的函数（模板）
corresponding instance                  |对应实例       |实现所对应的抽象机器
covariant                               |协变
create                                  |创建
CTAD, constructor template argument deduction   |构造函数模板实参推断   |可利用推断导引
current class                           |当前类         |当前位置最内层类作用域
cv pointer to cv T                      |cv T 的 cv 指针
cv-combined type                        |cv 合并类型
cv-decomposition                        |cv 分解
cv-qualification                        |cv 限定
cv-qualification signature              |cv 限定签名    |最长限定分解的除顶层 cv 外的各级 cv
cv-qualifier                            |cv 限定符      |类型说明符的一种，可与其他说明符组合
cv-unqualified                          |无 cv 限定的

### D

|English|中文|说明|
|-|-|-|
data                                    |数据
data member                             |数据成员
data race                               |数据竞争   |潜在并发+非原子性+无HapB，UB
data structure                          |数据结构
data type                               |数据类型
deallocate                              |回收
deallocation function                   |回收函数   |`operator delete`, `operator delete[]`
decay                                   |退化
declaration                             |声明式，声明   |代码结构称为‘声明式’，引入实体的名字，类型和编译期存在性
declaration statement                   |声明语句   |除虚无初始化变量外，跳转不能使变量活跃<br>静态/线程变量初始化异常时认为未初始化，同步保护并发初始化，递归UB
declarative *nested-name-specifier*     |声明性*嵌套名说明符* |用于定名类型，不能有decltype，应当为模板
declarative region                      |声明区
declarator                              |声明符
declare                                 |声明
decltype specifier                      |decltype 说明符
decode                                  |解码
decrement operator                      |减量运算符
deduce                                  |推断
deduction guide                         |推断导引
default argument                        |默认实参
default argument promotion              |默认实参提升   |调用前提升所有实参（IntP、FltP)
default behavior                        |缺省行为       |某些函数，如果程序不提供就采用实现的缺省版本
default constructor                     |默认构造函数
default label                           |default 标号
default member initializer              |默认成员初始化式
default template argument               |默认模板实参   |模板形参的默认实参
default-initialization                  |默认初始化
defaulted                               |预置的，默认的，缺省的
defaulted function                      |预置函数
define                                  |定义
defining type specifier                 |定义类型说明符 |类型说明符，加上类说明符和枚举说明符
definition                              |定义式，定义   |代码结构称为‘定义式’，实体称为‘定义’，实体的内容和连接时存在性
definition domain                       |定义域         |指是否处于私有模块分段，定义域影响内联函数/变量定义的可达性
delegating constructor                  |委派构造函数
delete                                  |删除
delete expression                       |delete 表达式  |一元表达式。单对象/数组。操作数为对象指针或类类型（按语境转换为对象指针）。<br>操作数必须为空指针值或`new`的结果指针，允许不完整类型但当心UB。<br>数组静态/动态类型必须相似。单对象允许虚析构或由销毁用 delete 负责销毁对象<br>与new配合支持存储扩展分配的回收
`delete` operator                       |`delete` 运算符|调用回收函数`operator delete`或`operator delete[]`<br>名字查找先作用域后全局。虚析构函数定义点处选择回收函数。有销毁用函数时仅考虑它们<br>支持`align_val_t`和`size_t`参数，`destroying_delete_t`标明销毁用函数
deleted                                 |已删除的，弃置的
deleted definition                      |弃置定义式
deleted function                        |弃置函数
dependency-ordered before               |按依赖序早于 DepB  |以跨线程值传递确定的顺序：原子性写-读某值+线程内CDep
dependent name                          |待决名字   |依赖于模板的名字，实例化时决定具体含义
deprecated                              |被摒弃的   |因为有某种问题而不建议使用的，未来会被移除的功能设施
derived class                           |派生类
designated initializer                  |定名初始化式
destroy                                 |销毁
destroying operator delete              |销毁用 delete 运算符   |成员，非数组，`(T*, destroying_delete_t, ...)`，由此函数负责析构；只要提供就排除非销毁函数
destruction                             |销毁
destructor                              |析构函数
device                                  |设备
diagnosable rule                        |可诊断规则
diagnostic message                      |诊断消息   |编译器报错
digraph                                 |二联符，合成符     |6个：`<%`,`%>`,`<:`,`:>`,`%:`,`%:%:`->`{`,`}`,`[`,`]`,`#`,`##`
direct base class                       |直接基类
direct-initialization                   |直接初始化
direct-list-initialization              |直接列表初始化     |直接进行的列表初始化
direct-non-list-initialization          |直接非列表初始化   |直接进行的其他初始化
directive                               |指令
directive-introducing token             |指令发起记号
disambiguation                          |歧义消解
discarded statement                     |弃用语句       |`constexpr if` 排除的语句
discarded-value expression              |弃值表达式     |仅保留副作用，一些 volatile 访问表达式进行L2R转换（保留读内存副作用）
disjunction                             |析取
division operator                       |除法运算符
do statement                            |do 语句
dot operator                            |点运算符
dynamic                                 |动态
dynamic cast expression                 |动态转型表达式 |后缀表达式，`dynamic_cast<T>(v)`，若T不指向v的类型或其基类则要求v多态<br>按需查询RTTI：可转换为v的全派生对象中v的无歧义公开派生类对象，或全派生对象的无歧义公开基类对象<br>引用转换失败抛出`bad_cast`
dynamic initialization                  |动态初始化     |除静态初始化外的所有初始化，运行时发生<br>可以推迟到主函数/线程启动函数开始之后，但早于使用同UT中的任何非内联
dynamic storage duration                |动态存储期
dynamic type                            |动态类型       |纯右值的动态类型编译期已知

### E

|English|中文|说明|
|-|-|-|
ECMA, European Computer Manufacturers Association   |ECMA，欧洲计算机制造商协会
elaborated-type-specifier               |详述类型说明符 |仅引入类型种类和名字，前向声明
element                                 |元素
eligible special member function        |合格的特殊成员函数
ellipsis                                |省略号     |`...`：形参包组（模板、函数），包组展开，折叠展开；变参函数
ellipsis parameter                      |省略号形参 |`va_xxx`变参函数
empty-declaration                       |空声明式   |仅有`;`的声明式，不是块语句
empty-statement                         |空语句     |仅有`;`的语句
encapsulate                             |封装
enclosing class                         |外围类
enclosing namespace                     |外围命名空间
enclosing scope                         |外围作用域
encode                                  |编码
encoding prefix                         |编码前缀   |`L`, `u`, `u8`, `U`
end-of-line indicator                   |行结束指示符   |`\n`，`\r\n`，等
endian                                  |端序
entity                                  |实体       |值、对象、引用、结构化绑定、函数、枚举符、类型、类成员、位字段、模板、模板特例、命名空间、包组
entry                                   |入口       |函数，catch，代码块
enumerated type                         |枚举类型
enumeration                             |枚举
enumeration scope                       |枚举作用域 |作用域的一种，包括枚举符列表
enumeration type                        |枚举类型
enumerator                              |枚举符     |一种实体，类型化具名常量值
enum-specifier                          |枚举说明符 |枚举的定义体
equality                                |相等
equality expression                     |相等性表达式   |`rel_expr == rel_expr`等。内建：算术类型一般算术转换，指针和成员指针进行合成指针类型比较<br>成员指针比较，虚函数和无继承关系时未指明顺序
equality operator                       |相等性运算符   |`==`, `!=`
equivalence                             |等价
equivalence class                       |等价类 |正则表达式，[=a=]，匹配校排等价字符
error                                   |错误，误差
escape character                        |转义字符
escape sequence                         |转义序列   |简单、数值、有条件转义序列
evaluation                              |求值       |表达式的求值包括值计算和副作用
exception                               |异常
exception-declaration                   |异常声明式 |catch中的异常变量声明式，仅支持一个异常，支持省略号，不支持默认值，不支持占位符？
exception handler                       |异常处理器
exception specification                 |异常说明
exclusive-or expression                 |异或表达式     |`and_expr ^ and_expr`。内建：按位异或，一般算术转换
exclusive-or operator                   |异或运算符     |`^`
execute                                 |执行，运行
execution agent                         |执行代理
execution character set                 |执行字符集     |LC_CTYPE
execution step                          |执行步骤       |线程的可观察行为：终止，volatile访问，完成I/O、同步或原子性操作
execution wide-character set            |执行宽字符集   |LC_CTYPE
explicit                                |显式，明确
explicit instantiation declaration      |显式实例化声明式   |指定某个模板特例应当 ODR 式存在
explicit specialization                 |显式特化式     |改变模板针对特定模板实参时的内容，实体种类应当与主模板一致
explicit specifier                      |explicit 说明符|`explicit`或`explicit(expr)`，类体内构造函数/转换函数，常量表达式Ctx2Bool
explicit type conversion                |显式类型转换   |后缀表达式。写法：转型、函数式、运算符`XX_cast`、初始化
explicitly captured                     |显式俘获       |指定其*简单俘获符*
explicitly defaulted function           |显式预置的函数
exponent                                |指数
export declaration                      |导出声明式
module-keyword                          |导出关键字     |预处理记号，在预处理阶段支持模块
exported declaration                    |被导出声明式
exposure                                |显露式         |声明式中除函数体、初始化式、友元外指名了TU局部实体
expression                              |表达式
expression-equivalent                   |按表达式等价   |表达式求值的真实效果相同（？）
extend namespace                        |扩展命名空间
extended alignment                      |扩充对齐       |EA > `alignof(max_align_t)`
extended character set                  |扩展字符集
extended execution character set        |扩展执行字符集
extended integer type                   |扩充整数类型   |扩充有符号、无符号整数
extended signed integer type            |扩充有符号整数类型
extended source character set           |扩展源字符集
extended unsigned integer type          |扩充无符号整数类型
extension                               |扩展           |实现提供的额外功能
extern specifier                        |extern 说明符  |变量或函数非定义声明式，外部连接。允许声明不完整类型的实体
external linkage                        |外部连接       |跨翻译单元可见

### F

|English|中文|说明|
|-|-|-|
facet                                   |刻面
facility                                |功能设施   |语言功能或程序库组件
failure                                 |失败，故障
fallthrough statement                   |直落语句
fault                                   |故障，错误
feature                                 |功能特性，特性
fence                                   |栅栏，内存栅栏 |无关内存位置的同步操作
field                                   |字段
file                                    |文件           |可观察行为
final overrider                         |最终覆盖函数
finite state machine                    |有限状态机     |用于实现正则表达式的数据结构
floating-integral conversion            |浮点整形转换   |f->i：截断；i->f：尽可能精确
floating-point                          |浮点
floating-point conversion               |浮点转换       |除提升外任意浮点间转换
floating-point literal                  |浮点字面量     |后缀：'fFlL'，十进制'eE'，十六进制'0x|0X' + 'pP'，指数部分仍为10进制
floating-point type                     |浮点类型       |`float`, `double`, `long double`
floating-point promotion                |浮点提升       |float -> double
fold expression                         |折叠表达式
for-range-declaration                   |for-范围声明式 |范围式for语句的变量声明式
for statement                           |for 语句
format specifier                        |格式说明符     |正则表达式中被替换部分的格式说明
forward declaration                     |前置声明式
forward progress                        |向前进展，进展 |保证线程会产生副作用，或其他线程可见的行为：同步或原子性操作
fraction                                |小数，分数
free store                              |自由存储       |new/delete 或 malloc() 等所管理的堆内存
freestanding implementation             |自立式实现     |无操作系统支持
friend                                  |友元
friend class                            |友元类
friend function                         |友元函数
friend specifier                        |friend 说明符
full-expression                         |全表达式       |免求值操作数，常量表达式，直接调用，声明的初始化式，出作用域的销毁，非子表达式且非全表达式一部分的表达式
function                                |函数           |一种实体，不是对象
function-body                           |函数体         |指定代码或`=default`、`=delete`
function call expression                |函数调用表达式 |后缀表达式
function call operator                  |函数调用运算符 |内建：静态、非静态、虚、析构/伪析构，`a(b,...)`, a SeqB b, b IndSeq, b SeqB 函数体
function declaration                    |函数声明式     |非`typedef`简单声明式，类型为函数类型
function declarator                     |函数声明符
function-definition                     |函数定义式
function object                         |函数对象
function overloading                    |函数重载
function parameter pack                 |函数形参包组
function parameter scope                |函数形参作用域 |作用域的一种，形参声明子句（不只函数）所在声明符范围，有体则包含体
function pointer conversion             |函数指针转换   |去掉noexcept约束
function pointer type                   |函数指针类型
function prototype                      |函数原型
function scope                          |函数作用域
function specifier                      |函数说明符     |`virtual`，`explicit`, `explicit(expr)`
function template                       |函数模板
function-try-block                      |函数-try-块    |整个函数放入`try...catch`中
function-like macro                     |函数式宏
function-to-pointer conversion          |函数向指针转换 |函数或静态成员函数
fundamental alignment                   |基础对齐       |FA <= `alignof(max_align_t)`
fundamental type                        |基础类型       |算术（整型、浮点）, `void`, `nullptr_t`

### G

|English|中文|说明|
|-|-|-|
generic lambda expression               |泛型 lambda 表达式
global                                  |全局的
global module                           |全局模块
global-module-fragment                  |全局模块分段   |
global namespace                        |全局命名空间
global object                           |全局对象
global scope                            |全局作用域     |整个程序，全局命名空间的命名空间作用域
global variable                         |全局变量
glvalue                                 |泛左值     |具有识别性的值（可取地址），结果为实体：LValue+XValue
glyph                                   |字形       |字符图形，书写效果
goto statement                          |goto 语句
grammar                                 |文法
greater-than operator                   |大于运算符
greater-than-or-equal-to operator       |大于或等于运算符

### H

|English|中文|说明|
|-|-|-|
handler                                 |处理器     |捕获并处理异常的代码块
handler function                        |处理函数   |`new_handler`等
happens after                           |发生晚于 HapA
happens before                          |发生早于 HapB  |确定任意两求值的顺序：线程内SeqB或线程间ITHB
header                                  |头文件
header name                             |头文件名   |预处理记号，`<[~>]*>` 或 `"[~"]*"`，仅属于 `#include`，`import`，`__has_include`
header unit                             |头文件单元 |模块
high-order bit                          |高序位     |最高有效位
hosted implementation                   |宿主式实现 |在操作系统下运行

### I

|English|中文|说明|
|-|-|-|
identifier                              |标识符     |预处理记号，也是记号，符合 Unicode 标识符文法 XID_Start XID_Continue*
identifier label                        |标识符标号
IEC, International Electrotechnical Commission  |IEC，国际电工委员会
IEEE, Institute of Electrical and Electronic    |IEEE，电气与电子工程师协会
if statement                            |if 语句
ill-formed                              |非良构的   |语法或语义无效的代码
immediate function                      |直接函数       |以`consteval`修饰的函数
immediate function context              |直接函数语境   |直接函数的作用域，或consteval if作用域中
immediate invocation                    |直接调用       |直接函数调用链的入口
immediate scope                         |直接作用域     |最小的外围作用域
immediate subexpression                 |直接子表达式   |应当在文法位置执行的表达式：成分表达式、隐含函数调用、lambda的捕获的初始化、默认实参、聚合的默认成员初始化式
implementation                          |实现
implementation limits                   |实现限额
implementation-defined                  |由实现定义的   |编译器实现自行决定的某些良构代码的行为
implicit                                |隐式，暗中，隐含
implicit conversion                     |隐式转换       |iff可声明`T t=e;`，e可隐式转换为 T
implicit conversion sequence            |隐式转换序列   |实现隐式转换的序列：SCSeq+UDefC+SCSeq
implicit type conversion                |隐式类型转换
implicit-lifetime class                 |隐式生存期类   |
implicit-lifetime type                  |隐式生存期类型 |标量、隐式生存期类，数组
implicitly captured                     |隐式俘获       |ODR使用但未列为俘获符
implicitly create object                |隐式创建对象
implicitly declared function            |隐式声明的函数
import                                  |导入
import declaration                      |导入声明式
import-keyword                          |导入关键字 |预处理记号，在预处理阶段支持模块
impose                                  |施加
inclusive-or expression                 |或表达式   |`xor_expr | xor_expr`。内建：按位或，一般算术转换
inclusive-or operator                   |或运算符   |`|`
incomplete type                         |不完整类型 |`void`，`T[]`，（类作用域外）无定义式的类，某些枚举
incomplete-defined object type          |定义不完整的对象类型   |仅声明的类、某些情况的枚举、未知边界数组
increment operator                      |增量运算符
indeterminate value                     |不确定值   |自动或动态对象的初始化前内容
indeterminately sequenced               |未定顺序的 |线程内，顺序早于或晚于，不重叠
indirect base class                     |间接基类
indirection operator                    |间接运算符     |一元运算符/表达式，`*`，左值
inequality operator                     |不相等运算符
inhabit                                 |居于           |声明式居于其直接作用域（模板形参作用域单算）
init-statement                          |初始化语句     |if/switch/for中第一部分，声明并初始化变量
initialization                          |初始化
initialize                              |初始化
initializer                             |初始化式   |`(expr,...)`，`{...}`，`=expr`，`={...}`
injected-class-name                     |注入类名   |当做成员名的类名
inline function                         |内联函数   |优先内联展开，跨UT多定义
inline namespace                        |内联命名空间
inline specifier                        |inline 说明符  |变量或函数。首个声明式决定是否内联
inline variable                         |内联变量   |跨UT多定义
input                                   |输入
instance                                |实例
instantiate                             |实例化，落实
instantiation                           |实例化式，实例化   |模板实体落实为具体实体
instantiation unit                      |实例化单元         |根据已翻译翻译单元中的模板表示，为程序所需要的特例生成的二进制代码
integer                                 |整数
integer conversion rank                 |整数转换等级       |宽度越小等级越小，与符号性无关，标准>扩展，`bool`最小，字符等级与底层类型相同
integer literal                         |整数字面量         |后缀：符号性`u|U`，类型`l|L|ll|LL|z|Z`<br>前缀：进制`0|0b|0B|0x|0X`
integer type                            |整数类型   |整数*8、字符*5、`bool`
integral constant expression            |整型常量表达式
integral conversion                     |整形转换   |除提升外的任意整型间转换，除bool外同余值
integral promotion                      |整形提升   |低于int的整型、字符、无作用域枚举，转为足够宽的int及以上最低类型<br>整型位字段提升到int
integral type                           |整型类型   |整数*8、字符*5、`bool`
inter-thread happens before             |线程间发生早于 ITHB|明确跨线程顺序性：<br>SeqB、Sync、DepB的跨线程组合<br>DepB+SeqB不足以提供有序性
interactive device                      |交互设备   |I/O 设备，可观察行为
interface dependency                    |接口依赖   |被导入模块
internal linkage                        |内部连接   |翻译单元内可见
intervening scope                       |介入作用域 |即目标的每层不包含声明点的外围作用域
invalid                                 |无效，非法
invalid pointer value                   |无效指针值
invocation                              |调用，执行
invoke                                  |调用，执行 |多用于除函数之外的场合，如宏等
iostream                                |输入输出流, I/O 流
ISO, International Organization for Standardization |ISO，国际标准化组织
iteration statement                     |循环语句，重复语句 |while, do-while, for, for-range
iterator                                |迭代器

### J

|English|中文|说明|
|-|-|-|
join                                    |合并（线程）
jump statement                          |跳转语句

### K

|English|中文|说明|
|-|-|-|
keyword                                 |关键字     |无条件关键字 + `import` `export` `module`

### L

|English|中文|说明|
|-|-|-|
label                                   |标号           |标识符标号具有独立命名空间，函数作用域。`switch`中的`case`和`default`
labeled statement                       |带标号语句
lambda-expression                       |lambda-表达式  |函数对象/闭包，有捕获捕获，可泛型可约束，返回`auto`（推断或尾部返回类型）
language linkage                        |语言连接
latch                                   |门栓
layout-compatible enumeration           |布局兼容枚举
layout-compatible                       |布局兼容       |相同类型、布局兼容枚举、布局兼容的标准布局类
left shift operator                     |左移运算符
less-than operator                      |小于运算符
less-than-or-equal-to operator          |小于或等于运算符
lexical                                 |词法   |如何以字符构成语法记号
library                                 |程序库
lifetime                                |生存期
line                                    |行，文本行
link                                    |连接   |将已翻译实体收集并组合成程序映像
linkage                                 |连接，连接性   |可被连接器认作同一：无连接、内部、外部、模块
linkage-specification                   |连接说明   |指定语言连接`extern "xxx"`
list                                    |列表
list-initialization                     |列表初始化
literal                                 |字面量     |字符/字符串/数值，以及自定义变体，布尔，指针
literal operator                        |字面量运算符       |用户字面量的函数，非模板有类型化和原始两种，`operator "" X(T)`, `operator "" X(const char*)`
literal operator template               |字面量运算符模板   |用户字面量的函数模板，数值模板和字符串模板两种，无函数形参
literal suffix literal                  |字面量后缀         |字面量运算符（模板）中的标识符，即字面量后缀
literal type                            |字面类型           |void、标量、引用，字面类型的数组，constexpr构造和析构，非 volatile 数据
local                                   |局部，局部的
local class                             |局部类
local entity                            |局部实体           |自动变量，自动变量的结构化绑定，*this
local lambda expression                 |局部 lambda 表达式
local scope                             |局部作用域
local variable                          |局部变量
locale                                  |地域
locale-specific                         |地域特有的
lock                                    |锁，锁定
lock-free                               |免锁           |不会被阻塞，仍可能被妨碍（比如CAS循环等）
lock-free execution                     |免锁执行       |“免妨碍”，不会阻碍唯一未锁定线程
locus                                   |位点           |声明点
logical-and expression                  |逻辑与表达式   |`or_expr && or_expr`。内建：逻辑与，Ctx2Bool，短路
logical-and operator                    |逻辑与运算符   |`&&`
logical negation operator               |逻辑非运算符   |一元运算符/表达式，`!`，Ctx2Bool
logical-or expression                   |逻辑或表达式   |`logand_expr || logand_expr`。内建：逻辑或，Ctx2Bool，短路
logical-or operator                     |逻辑或运算符   |`||`
logical source line                     |逻辑源文本行   |行拼接后的结果
lookup context                          |查找语境       |成员限定名：对象表达式的类型，其他：嵌套名说明符指名的类型或命名空间等。若限定查找未找到则再进行无限定查找
lookup set                              |查找集合       |类成员名字查找的中间结果，包含声明式集合和所属子对象集合
low-order bit                           |低序位         |最低有效位
lower bound                             |下界
lvalue                                  |左值           |并非临限值XValue的泛左值
lvalue-to-rvalue conversion             |左值向右值转换 |非函数、非数组，GLv->PRv，非类类型去掉cv

### M

|English|中文|说明|
|-|-|-|
macro                                   |宏
macro invocation                        |宏调用     |代码文本中使用宏
make progress                           |取得进展   |线程发生执行步骤，阻塞或调用未完成的免锁执行函数
manifestly constant-evaluated           |显然常量求值的 |常量表达式，constexpr if的条件，直接调用，约束求值，从来初始化的初始化式
match                                   |匹配       |正则表达式模式与目标文本发生对应
materialize                             |实质化
member                                  |成员
member-declaration                      |成员声明式 |可以作为类成员的声明式：比块声明式多出空声明式、模板、函数定义、位字段，支持成员函数特有的语言特性，不支持结构化绑定，不支持成员变量占位符类型
member-specification                    |成员说明   |类体的内容，包括成员声明式和访问说明符
member function                         |成员函数
member-qualified name                   |成员限定名 |限定名的一类，`a.`或`p->`后面的无限定标识或`X::`中的成分名
member type                             |成员类型
memory                                  |内存
memory location                         |内存位置   |非位字段或最长连续非零宽位字段
memory management                       |内存管理
memory model                            |内存模型
modification order                      |改动顺序   |对某原子性对象的所有改动，无竞争有顺序
modifier function                       |改动函数
module                                  |模块
module-declaration                      |模块声明式 |
module-keyword                          |模块关键字 |预处理记号，在预处理阶段支持模块
module-import-declaration               |模块导入声明式 |
module linkage                          |模块连接   |模块内跨翻译单元可见
module unit                             |模块单元   |模块机制支持的程序表示
more cv-qualified                       |更加 cv 限定的
most derived class                      |全派生类   |非基类子对象的类对象的类型
most derived object                     |全派生对象 |非基类子对象的对象
move                                    |移动
move assignment                         |移动赋值
move assignment operator                |移动赋值运算符
move construction                       |移动构造
move constructor                        |移动构造函数
multibyte character                     |多字节字符
multibyte encoding                      |多字节编码
multicharacter literal                  |多字符字面量
multidimensional array                  |多维数组
multiplication operator                 |乘法运算符
multiplicative expression               |乘性表达式 |`pm_expr * pm_expr`等，内建：一般算数转换，`%`要求整型/无作用域枚举
multiplicative operator                 |乘性运算符 |`*`, `/`, `%`
mutable specifier                       |mutable 说明符 |非静态数据成员，免除const
mutex                                   |互斥体

### N

|English|中文|说明|
|-|-|-|
name                                    |名字<br>指名       |标识符、运算符函数标识、字面量运算符标识、转换函数标识<br>声明式包含：模板名、概念名、标识表达式、类型的说明符、闭包类型的lambda、重载集合时，指名相应实体
name hiding                             |名字隐藏
name lookup                             |名字查找   |遇到名字时确定其含义
name mangling                           |名字重整
named                                   |具名的
named by                                |被（表达式或转换）指名 |变量：标识表达式<br>函数：被重载决议选中（还包括new/delete）（排除纯虚函数的全限定名或成员指针）
named module                            |具名模块
namespace                               |命名空间       |一种实体，名字的层级管理设施
namespace alias                         |命名空间别名
namespace-body                          |命名空间体     |每个命名空间定义式的体
namespace-definition                    |命名空间定义式 |
namespace-name                          |命名空间名     |标识符：原名或别名
namespace scope                         |命名空间作用域 |作用域的一种，合并该命名空间的所有体，加上体外带限定成员
narrow character type                   |窄字符类型     |普通（三种`char`），`char8_t`
narrow string literal                   |窄字符串字面量 |普通和UTF-8
necessarily reachable                   |必定可达
nest                                    |嵌套
nested class                            |嵌套类
nested name                             |嵌套名
nested name specifier                   |嵌套名说明符
nested requirement                      |嵌套规定   |`requires constraint_expr;`
nested type                             |嵌套类型
nested within                           |嵌套于     |子对象，被提供存储的对象
new expression                          |new 表达式 |一元表达式。以初始化式推断占位符类型，获得被分配类型：对象或数组<br>以初始化式推断未知边界数组大小的顶层边界，顶层数组大小检查：静态检查核心常量表达式，动态失败则抛出`bad_array_new_length`<br>支持缺省全局分配省略（如常量求值中）。支持分配扩展
new-extended alignment                  |new 扩充对齐   |NEA > `__STDCPP_DEFAULT_NEW_ALIGNMENT__`
new-line                                |换行       |`\n`
`new` operator                          |`new` 运算符   |对象/数组。调用分配函数`operator new`或`operator new[]`，异常失败时尽量调用对应回收函数、元素销毁<br>名字查找先作用域后全局。new 扩充对齐类型优先尝试带对齐函数，反之不带对齐函数优先。后附放置实参<br>无初始化式为默认初始化，否则直接初始化，分配 SeqB 初始化式求值，对象初始化 SeqB new返回值
no diagnostic is required               |无须诊断
no linkage                              |无连接     |仅限作用域内可见
nodeclspec-function-declaration         |无声明说明符函数声明式 |模板：声明构造函数、析构函数、转换函数
`noexcept` expression                   |`noexcept` 表达式  |一元表达式。整型常量表达式（`bool`）。是否潜在抛出
noexcept function of () cv ref returning| T  T 为返回类型的 () cv ref 的 noexcept 函数
`noexcept` operator                     |`noexcept` 运算符  |免求值表达式，`noexcept(expr)`
nominable declaration                   |可提名声明式       |类/命名空间某点之前的目标为该作用域（或其内联）的居于非块作用域的声明式，即引入了实体成员而不关心是否绑定名字
non-allocating form                     |非分配形式
non-encodable character literal         |不可编码字符字面量 |字面量关联的字符编码所不支持的字符
non-initialization odr-use              |非初始化 ODR 式使用|非由静态/线程变量初始化导致的 ODR 式使用
non-static data member                  |非静态数据成员
non-throwing exception specification    |无抛出异常说明
non-vacuous initialization              |非无为初始化
normalized                              |正规化的
normative                               |规范性的   |作为正式内容的文本章节或参考文献
null                                    |空
null character                          |空字符     |`'\0'`
null member pointer conversion          |空成员指针转换 |空指针常量->成员指针类型的空成员指针值
null member pointer value               |空成员指针值   |具体成员指针类型的空成员指针值，不指向任何成员
null pointer                            |空指针
null pointer constant                   |空指针常量 |包括`nullptr`和`0`等，不是空指针值
null pointer conversion                 |空指针转换 |空指针常量->指针类型的空指针值
null pointer literal                    |空指针字面量   |唯一的指针字面量，`nullptr`，类型为`std::nullptr_t`
null pointer value                      |空指针值   |具体指针类型的空指针值，二进制表示可能不为全0
null statement                          |空语句     |没有表达式的表达式语句
null-terminated                         |空终结
null wide character                     |空宽字符   |`L'\0'`
numeric escape sequence                 |数值转义序列   |`\ooo`，`\hh` 八进制最多三个，十六进制无限制
numeric literal operator template       |数值字面量运算符模板   |自定义数值字面量的通配，`<char...> T operator "" X()`

### O

|English|中文|说明|
|-|-|-|
object                                  |对象       |一种实体
object declaration                      |对象声明式 |非`typedef`简单声明式，类型非函数类型
object expression                       |对象表达式 |`a.m`和`a.*pm`中的`a`
object model                            |对象模型
object pointer type                     |对象指针类型   |指向对象类型或`void`
object representation                   |对象表示   |全部`sizeof(T)`个字节
object type                             |对象类型   |非函数、引用、`void`
object-like macro                       |对象式宏
observable behavior                     |可观察行为
observer function                       |探察函数
obstruction-free                        |免妨碍     |唯一未阻塞线程执行免锁执行必将完成
odr-usable                              |可 ODR 式使用  |词法作用域中排除并未被俘获的变量
odr-used                                |ODR 式使用 |- 变量：潜在求值指名（排除不涉及地址的使用方式：弃值或l2r转换）<br>- 结构化绑定：潜在求值<br>- *this：显式或隐式潜在求值this<br>- 函数：潜在求值指名（非纯虚函数仅需声明）<br>- 类的new/delete：定义类的构造/析构函数，或虚析构中被选中<br>- 类的构造/析构/复制/移动赋值：参与其他类的初始化/销毁/成员赋值
one-definition rule                     |单一定义规则，ODR  |各翻译单元中的类型定义应当严格等价，生成的程序映像中的实体定义应当唯一
opaque-enum-declaration                 |笼统枚举声明式 |不声明枚举符，但指定底层类型，完整的前向声明
operand                                 |操作数
operator                                |运算符
operator-or-punctuator                  |运算符或标点   |记号的一种，包括运算符记号和 `{}[]()...` 等和替代表示
operator overloading                    |运算符重载
or operator                             |或运算符
order of evaluation                     |求值顺序
ordered initialization                  |有序初始化     |静态变量初始化：非模板特例变量，非内联变量
ordinary character literal              |普通字符字面量 |除不可编码和多字符外，类型为 `char`，编码为执行字符集
ordinary character type                 |普通字符类型   |`char`, `signed char`, `unsigned char`
ordinary string literal                 |普通字符串字面量   |类型为`const char[n]`，编码为执行字符集
output                                  |输出
over-aligned type                       |过量对齐类型   |类型的对齐为扩充对齐EA
overflow                                |溢出，上溢
overload                                |重载
overload resolution                     |重载决议   |
overloaded function                     |重载函数
overloaded operator                     |重载运算符
override                                |覆盖
overrider                               |覆盖函数

### P

|English|中文|说明|
|-|-|-|
pack                                    |包组           |一种实体，概念上类似`tuple`，用于`...`
pack expansion                          |包组展开式
padding bits                            |填充位         |对象表示中不属于值表示的位
pair                                    |对偶
parallel                                |并行的
parallel forward progress guarantees    |并行向前进展保证   |启动后提供并发保证。线程池
parameter                               |形参，形式参数 |函数，catch，函数式宏，模板
parameter-declaration                   |形参声明式     |函数、lambda、推断导引、模板、requires（不支持默认实参、省略号和占位符推断？）
parameter-declaration-clause            |形参声明子句   |可调用体的参数列表部分，同上
parameter pack                          |形参包组
parameter-type-list                     |形参类型列表   |函数签名
parent scope                            |父作用域       |作用域的直接作用域（模板形参作用域单算）
parenthesized expression                |带括号表达式
partial order                           |偏序，非严格偏序，半序 |自反，反对称，传递，不要求完全性，如 <=
partially-ordered initialization        |部分有序初始化 |静态变量初始化：非模板特例的内联变量
partial specialization                  |部分特化，部分特化式
phases of translation                   |翻译阶段       |1. 物理字符->源字符，换行符<br>2. 行接合<br>3. 预处理记号分析<br>4. 执行预处理<br>5. 转义处理<br>6. 字符串拼接<br>7. 编译：记号分析，AST，语义分析等<br>8. 连接，按需实例化<br>9. 连接程序库
physical source file character          |物理源文件字符 |根据文件编码获得的字符
physical source line                    |物理源文本行
placeholder                             |占位符
placeholder type deduction              |占位符类型推断
placement allocation function           |放置式分配函数
placement deallocation function         |放置式回收函数 |形参与对应放置式分配函数匹配，会在new表达式失败时自动调用，若不唯一则忽略
placement new-expression                |放置式 new-表达式|放置式语法的 new 表达式`new (args) T`
point of declaration                    |声明点         |实体声明生效的位点：<br>- 变量/函数/形参在声明符（包括初始化式）之后，<br>- 注入类名和函数预定义变量在`{`前，<br>- 其他（类型、枚举符、using、概念、命名空间等）在标识符（列表）之后
point of definition                     |定义点
pointer                                 |指针
pointer arithmetic                      |指针算术
pointer conversion                      |指针转换       |空指针转换，cv T*->cv void*（地址不变），cv D*->cv B*（地址调整）
pointer declarator                      |指针声明符
pointer literal                         |指针字面量     |`nullptr`，类型为`std::nullptr_t`
pointer to member                       |成员指针       |数据成员指针，成员函数指针
pointer to member conversion            |成员指针转换   |空成员指针转换，cv T(B::*)->cv T(D::*)
pointer to member declarator            |成员指针声明符
pointer to member expression            |成员指针表达式 |`cast-expr .* cast-expr` `cast-expr ->* cast-expr`。成员函数：检查对象的`&`/`&&`
pointer to member of X of type cv T     |cv T 类型的 X 的成员指针
pointer to member operator              |成员指针运算符 |`.*` 和 `->*`，`p->*mp`等价于`(*(p)).*mp`
pointer to T                            |T 的指针，指向 T 的指针
pointer-interchangable                  |指针可相互转换 |相同地址值：相同对象、联合体与成员、标准布局类与首成员或基类子对象（不包括数组与首元素）
polymorphic                             |多态的
POSIX, Portable Operating System Interface  |POSIX，可移植操作系统接口
postfix                                 |后缀
postfix decrement expression            |后置减量表达式 |后缀表达式
postfix decrement operator              |后置减量运算符 |内建：结果为原值副本PRv，改动Lv，摒弃volatile，读取 SeqB 改动
postfix expression                      |后缀表达式     |初等、下标、函数调用、函数式转型、成员访问、后缀增减、X_cast、typeid
postfix increment expression            |后置增量表达式 |后缀表达式
postfix increment operator              |后置增量运算符 |内建：结果为原值副本PRv，改动Lv，摒弃volatile，读取 SeqB 改动
potential result                        |潜在结果       |用于挑出某些表达式中并非 ODR 式使用变量的标识表达式
potential scope                         |潜在作用域
potentially concurrent                  |潜在并发       |跨线程，跨信号处理函数
potentially conflict                    |潜在冲突       |对应声明式代表了不同实体，或被覆盖实体无法再使用（形参、选择/循环的条件、捕获异常不能被覆盖）
potentially-constant                    |潜在常量       |constexpr变量、引用、const整型
potentially constant evaluated          |潜在常量求值   |显然常量求值的，潜在求值的，花括号的直接子表达式，模板中取地址
potentially-evaluated                   |潜在求值的     |除免求值（`sizeof`等情况）外的一切表达式/转换，编译期或运行时求值
potentially-overlapping subobject       |潜在重叠子对象 |基类子对象、`[no_unique_address]`NSDM，允许空类对象的存储优化
potentially throwing                    |潜在抛出异常的 |有能力抛出异常
pragma                                  |语用       |预处理指令，预处理运算符
precede                                 |先于       |表达式在名字使用点之前：同UT时在其之前或居于其可达的类作用域，跨UT时模块导入指定先于关系，内部连接不能跨UT
precedence                              |优先级
prefix                                  |前缀       |字符字面量，字符串字面量：编码前缀和 `R`
prefix decrement operator               |前置减量运算符 |一元表达式，摒弃volatile，结果为原对象Lv
prefix increment operator               |前置增量运算符 |一元表达式，摒弃volatile，结果为原对象Lv
preprocess                              |预处理
preprocessing directive                 |预处理指令
preprocessing number                    |预处理数字 |预处理记号，`[.]? [0-9] ( [.] | [']? [0-9a-zA-Z_] | [eEpP] [-+] )*`
preprocessing operator                  |预处理运算符       |由预处理器操作的运算符：`#`, `##`, `%:`, `%:%:`
preprocessing operators and punctuators |预处理运算符与标点 |预处理记号，预处理运算符+运算符或标点
preprocessing token                     |预处理记号 |预处理指令工作对象，预处理后转换为记号
primary equivalence class               |主等价类   |校排中具有相同主排序键的字符或字符串
primary expression                      |初等表达式 |字面量、this、括号、标识表达式、lambda、折叠、requires
primary sort key                        |主排序键   |校排中仅按主题字符形状分类的排序字符
primary template                        |主模板
primary token                           |首选记号   |代用记号所等价的记号
private                                 |私有
private-module-fragment                 |私有模块分段   |用于支持单TU模块，非导出部分
program                                 |程序       |连接起来的翻译单元
program-defined specialization          |由程序定义的特化式
program-defined type                    |由程序定义的类型
programming language                    |程序设计语言
projection                              |投射       |算法对输入元素进行自定义变换
promise object                          |承诺对象
prospective destructor                  |预期析构函数
protected                               |受保护
prototype                               |原型
provides storage                        |提供存储   |字节数组对象为放置构造对象提供存储
prvalue                                 |纯右值     |对表达式仅使用其值而不涉及识别性，结果为值
pseudo-destructor                       |伪析构函数 |标量类型的析构函数
pseudo destructor call                  |伪析构函数调用 |无操作但结束生存期
public                                  |公用，公开
punctuator                              |标点，标点符号
pure virtual function                   |纯虚函数
purview                                 |视野

### Q

|English|中文|说明|
|-|-|-|
qualification                           |限定，限定性
qualification-combined type             |限定合并类型   |多级指针/数组的公共类型。非顶层各级 cv 限定符合并，向发生合并层级的所有外层添加 const
qualification decomposition             |限定分解       |多级指针/成员指针/数组的分解方式
qualified name                          |限定名         |限定标识，using-声明符，typename-说明符，和具有`A::B`结构的各种说明符等中的终端名，以及成员限定名
qualified name lookup                   |限定名查找     |一般在查找语境中查找，命名空间还考虑内联命名空间，找不到则进一步查找 uing-指令引入的命名空间
qualifier                               |限定符

### R

|English|中文|说明|
|-|-|-|
radix point                             |小数点
range                                   |范围
range-based for statement               |基于范围的 for 语句|等价于`init; auto && r = initor; auto b = begin(r); auto e = end(r); for (; b!=e; ++b) { decl = *b; ... }`<br>对类类型尝试`r.begin()`和`r.end()`
raw literal operator                    |原始字面量运算符   |`operator "" X(const char*)`，数值字面量的通配运算符之一
raw string literal                      |原始字符串字面量   |避免转义等处理的字符串，分隔串用于识别边界`)`，如`R"xx()xx"`
reachable                               |可达，可达的
reaching scope                          |可达作用域
read-read coherence                     |读-读协调性    |原子性 M 的 RA HapB RB，则两个值符合 M 的改动顺序
read-write coherence                    |读-写协调性    |原子性 M 的 RA HapB WB，则两个值符合 M 的改动顺序
recursive function call                 |递归函数调用
ref-qualifier                           |引用限定符     |函数类型，成员函数的 & 或 &&
reference                               |引用           |一种实体，不是对象，别名
reference declarator                    |引用声明符
reference-related to                    |引用相关
reference to cv T                       |cv T 的引用
reference to T                          |T 的引用，指代 T 的引用
reference type                          |引用类型，T& 或 T&&
referenceable type                      |可被引用的类型 |可以创建 T& 的类型 T，包括引用类型
regex                                   |正则表达式
region                                  |区，区域
regular expression                      |正则表达式
reinterpret cast expression             |重解释转型表达式 |后缀表达式，`reinterpret_cast<T>(v)`<br>函数指针兼容，对象指针兼容，成员指针兼容，指针<=>整数（枚举），通过指针完成引用转换
relational expression                   |关系表达式     |`cmp_expr < cmp_expr` 等。内建：算术进行一般算术转换，指针以合成指针类型比较<br>指针部分顺序：数组下标、成员声明顺序
relational operator                     |关系运算符     |`<`, `>`, `<=`, `>=`
relaxed                                 |宽松的
relaxed atomic operation                |宽松原子性操作 |不是同步操作，但不会竞争
relaxed pointer safety                  |宽松指针安全性
release                                 |释放       |同步操作
release sequence                        |释放序列   |某原子性对象上[释放+读改写*n]的最大序列
remainder operator                      |求余运算符
replacement function                    |替代函数   |程序定义的用以替换实现的缺省函数的函数，如`operator new`
repositional stream                     |可重定位流 |可 seek 到之前经过的位置
representation                          |表示
required behavior                       |预期行为   |由标准规定的行为，实现或程序提供的函数应当遵守
requirement                             |规定，要求 |简单规定、类型规定、复合规定、嵌套规定
requires-clause                         |requires 子句
reserved                                |保留的     |规定使用权属于标准或实现的名字或实体
reserved function                       |保留函数
reserved identifier                     |保留标识符 |`__` 开头或 `_[A-Z]` 开头的任何标识符，以及 `_` 开头的全局命名空间成员
restriction                             |限制，要求
resumption                              |恢复
return                                  |返回
return statement                        |return 语句，返回语句|允许在void函数中返回void类型操作数<br>复制初始化，但允许复制消除。结果初始化 SeqB 临时对象销毁 SeqB 局部变量销毁
return type                             |返回类型
return value                            |返回值
right shift operator                    |右移运算符
rounding                                |舍入
run                                     |运行
runtime type identification             |运行时类型标识
rvalue                                  |右值       |纯右值PRValue+临限值XValue

### S

|English|中文|说明|
|-|-|-|
safely-derived pointer                  |安全衍生指针
scalar                                  |标量
scalar type                             |标量类型   |算术、枚举、指针、成员指针、`nullptr_t`
scope                                   |作用域，范围
scope resolution operator               |作用域解析运算符   |`::`
scoped enumeration                      |有作用域枚举
scoped enumerator                       |有作用域枚举符
selection statement                     |选择语句       |if, switch
semantics                               |语义
semaphore                               |信号量
sequence                                |序列   |容器的一种
sequenced after                         |按顺序晚于 SeqA
sequenced before                        |按顺序早于 SeqB    |线程内顺序性：全表达式，运算符结果值早于操作数值，函数实参和函数后缀表达式早于函数体，等待表达式处的切换
sequential consistency                  |顺序一致性     |如同存在全局顺序
shift expression                        |移位表达式     |`add_expr << add_expr` `add_expr >> add_expr`<br>内建：左移、算术右移，IntP，操作数1 SeqB 操作数2
shift operator                          |移位运算符     |`<<`, `>>`
side effect                             |副作用 |读volatile，改，调用 I/O 库函数
signal                                  |信号
signal handler                          |信号处理函数
signature                               |签名   |名字，形参类型列表，外围类，命名空间，尾部 requires，（模板）返回类型，模板头，（特化）模板实参
signed                                  |有符号
signed integer type                     |有符号整数类型 |标准、扩充有符号整数
similar type                            |相似类型       |两个同级数多级指针/数组中，不考虑cv，允许数组的无边界/有边界差异外，其余相同
simple-capture                          |简单俘获符     |不带有初始化式，直接指名被俘获变量的俘获符
simple-declaration                      |简单声明式     |声明变量、函数的普通声明式（包括结构化绑定）：属性+一系列声明说明符+声明符的列表<br>声明类、枚举时可以没有声明符
simple escape sequence                  |简单转义序列   |`\ '"?\abfnrtv`
simple requirement                      |简单规定       |表达式有效性：`expr;`
simple-template-id                      |简单模板标识   |模板标识，名字为标识符（不包括运算符/字面量函数）
simply happens before                   |简单发生早于 SimpHB|不使用消费操作时的简单模型：线程内SeqB或线程间Sync
single-object delete expression         |单对象 delete 表达式|`delete p`
single search                           |单次搜索       |名字查找步骤，找到先于搜索点的目标作用域中的全部声明式，using-声明式替换为目标声明式，类/枚举可被隐藏
`sizeof` expression                     |`sizeof` 表达式|一元表达式。整形常量表达式。非潜在重叠对象的大小，窄字符为1，其他由实现定义
`sizeof` operator                       |`sizeof` 运算符|免求值表达式或类型标识：`sizeof expr`或`sizeof(T)`<br>包组元素个数，包组展开：`sizeof...P`
source character set                    |源字符集
source file                             |源文件
space character                         |空格字符   |` `
spaceship operator                      |飞船运算符 |`<=>`
specialization                          |特化式，特例   |代码结构为‘特化式’，实体为‘特例’
specialize                              |特化
specifier                               |说明符
stable algorithm                        |稳定算法   |保留输入元素顺序
standard conversion sequence            |标准转换序列   |隐式转换：(Lv2Rv|A2Ptr|F2Ptr)?+(IntP|FltP|IntC|FltC|FIC|PtrP|MptrP|BoolC)?+FPtrC?+QualC?
standard integer type                   |标准整数类型   |标准有符号、无符号整数
standard signed integer type            |标准有符号整数类型 |`signed char`, `short`, `int`, `long`, `long long`
standard unsigned integer type          |标准无符号整数类型 |`unsigned char`, `unsigned short`, `unsigned int`, `unsigned long`, `unsigned long long`
standard-layout class                   |标准布局类
standard-layout type                    |标准布局类型   |标量、标准布局类，数组
stateful character encoding             |有状态字符编码
statement                               |语句
static                                  |静态
static assertion                        |静态断言
static cast expression                  |静态转型表达式 |后缀表达式，`static_cast<T>(v)`<br>指针或引用：vB!=>D，左值=>T&，临限值=>T&&<br>转换：ICS，直接初始化的ICS，聚合首元素的ICS
static data member                      |静态数据成员
static initialization                   |静态初始化     |静态/线程变量的常量/零初始化，运行前发生。允许动->静优化
static member function                  |静态成员函数
static specifier                        |static 说明符  |成员：共享，命名空间：UT内部连接，局部：存储期
static storage duration                 |静态存储期
static type                             |静态类型   |表达式的可声明类型
static_assert declaration               |static_assert 声明式|常量表达式，Ctx2Bool
stop token                              |停止令牌
storage                                 |存储
storage class specifier                 |存储类说明符   |`static`, `thread_local`, `extern`, `mutable`
storage duration                        |存储期     |静态、线程、自动、动态
storage management                      |存储管理
stream                                  |流 |输入或输出流
strict                                  |严格的
strict partial order                    |严格偏序，拟序 |反自反，反对称，传递，不要求完全性，如 <
strict total order                      |严格全序   |具有完全性的严格偏序，完整的 <
strict weak order                       |严格弱序   |连通的严格偏序，不可比较关系为等价关系，如 <
string                                  |字符串
string literal                          |字符串字面量   |预处理记号，也是记号，编码前缀，数组（常量左值）
string literal operator template        |字符串字面量运算符模板 |`template<A a> A operator "" X()`，`A` 为支持字符串的字面量类型
stringize                               |字符串化       |预处理功能，获得预处理记号的字面量，`#a` -> `"a"`
strongly happens before                 |强发生早于 StrgHB  |不允许消费操作时，全局顺序性：线程内SeqB，线程间Sync，SeqB+SimpHB+SeqB
struct                                  |结构体
structure tag                           |结构体标签
structured binding                      |结构化绑定     |实体的一种，一组变量的语法糖
structured binding declaration          |结构化绑定声明式   |`[]`语法的简单声明式，仅允许`static`, `thread_local`, `auto` 或 cv<br>初始化式为`=ass_expr`,`{ass_expr}`或`(ass_expr)`，数组或非联合体类类型
sub-expression                          |子表达式   |正则表达式：括号标记的部分
subexpression                           |子表达式
subnormal                               |次正规的
subobject                               |子对象     |被其他对象包含：成员、基类、元素
subscript expression                    |下标表达式 |后缀表达式
subscript operator                      |下标运算符 |内建：数组GLv或指针PRv、枚举或整型，等价于`*(a+b)`，`a` SeqB `b`，可交换<br>摒弃逗号表达式，预备多维下标
substatement                            |子语句     |不包括选择和循环中的初始化语句
suffix                                  |后缀       |整数字面量，浮点字面量：`sSlLuUfFzZ`，自定义字面量
suitable created object                 |适当创建的对象
surrogate code point                    |代用代码点 |UCS 代用字符的代码点，为 UTF16 用于编码高值字符，D800-DFFF
suspension                              |暂停
suspension context                      |暂停语境   |函数中允许 `co_await` 的语境
switch statement                        |switch 语句
synchronization operation               |同步操作   |一些原子性操作和互斥体操作<br>消费(consume)、获取(aquire)、释放(release)、获取并释放，宽松(relaxed)操作不是同步<br>对内存位置的操作或无关内存位置的栅栏
synchronize                             |同步
synchronize with                        |同步于
syntactic category                      |语法范畴   |BNF 产生式非终结符
syntax                                  |语法
syntax notation                         |语法表示法

### T

|English|中文|说明|
|-|-|-|
target constructor                      |目标构造函数
target scope                            |目标作用域     |声明式所居作用域（友元/限定名/详述类型/块外部声明式等的目标例外）
template                                |模板           |一种实体，基于参数生成（实例化）其他实体
template argument                       |模板实参
template argument deduction             |模板实参推断
template-declaration                    |模板声明式     |声明或定义模板化实体（包括概念），引入模板形参的作用域
template-head                           |模板头         |模板声明中声明实体前指定模板形参及其约束的部分
template-id                             |模板标识       |无限定标识的一种，指名模板化实体的特例
template instantiation                  |模板实例化
template non-type parameter             |模板非类型形参 |三种模板形参之一
template-parameter                      |模板形参
template parameter pack                 |模板形参包组
template parameter scope                |模板形参作用域 |作用域的一种，模板形参列表到被模板化声明式末尾，模板模板形参的形参范围<br>模板形参作用域对其他名字透明，仅对模板形参有效
template specialization                 |模板特例，模板特化式   |模板特例：一种实体，模板基于参数落实的实体
template template parameter             |模板模板形参   |三种模板形参之一
template type parameter                 |模板类型形参   |三种模板形参之一
temporary expression                    |临时对象表达式
temporary materialization conversion    |临时对象实质化转换 |纯右值->临限值，类对象必须可销毁
temporary object                        |临时对象
term                                    |术语
terminal name                           |终端名     |using-声明符的目标，语言构造中最后一个成分名
terminate                               |终止
thread                                  |线程
thread of execution                     |执行线程，线程
thread storage duration                 |线程存储期
thread_local specifier                  |thread_local 说明符|成员：需加`static`，块：暗含`static`
thread-local variable                   |线程局部变量
three-way comparison                    |三路比较   |比较表达式，`e1 <=> e2`
throw                                   |抛出
throw-expression                        |throw表达式|`throw e`：抛出，`throw`重新抛出当前处理的异常
token                                   |记号       |编译器理解的语法元素：标识符，关键字，字面量，运算符或标点
token concatenation                     |记号拼接   |预处理功能，`a ## b` -> `ab`
top-level cv-qualifier                  |顶层 cv 限定符
total order                             |全序，非严格全序，线序 |具有完全性的偏序，完整的 <=
traceable pointer                       |可追踪指针
trailing *requires-clause*              |尾部 *requires-子句* |模板函数
trailing return type                    |尾部返回类型
traits class                            |特征类     |提供与某个主类型形参有关的静态自定义能力，模板类
translate                               |翻译       |编译
translated translation unit             |已翻译的翻译单元   |非模板的二进制代码，模板的二进制表示
translation phase                       |翻译阶段
translation unit                        |翻译单元   |预处理后的完整文件，声明式序列，或模块结构
transparently replaceable               |可透明替换 |可进行`new (&o) T()`：存储重叠，非const，非空大小
trivial class                           |平凡类
trivial copy constructor                |平凡复制构造函数
trivial default constructor             |平凡默认构造函数
trivial destructor                      |平凡析构函数
trivial move constructor                |平凡移动构造函数
trivial type                            |平凡类型       |标量、平凡类，数组
trivially copyable class                |可平凡复制类
trivially copyable type                 |可平凡复制类型 |可用`memcpy`复制：标量、可平凡复制类，数组
truncation                              |截断
tuple                                   |元组
TU-local                                |翻译单元局部   |实体为内部连接或非嵌套无名类型，
type                                    |类型           |一种实体，决定值表示的意义
type identification                     |类型识别       |`typeid`
type-only lookup                        |仅限类型查找   |仅查找类型
type-parameter                          |类型形参       |模板形参，包括类型和模板，支持包组、默认实参
type pun                                |类型双关
type requirement                        |类型规定       |类型有效性：`typename T;`
type specifier                          |类型说明符     |简单、详述、typename、cv
typedef declaration                     |typedef 声明式 |带有`typedef`的简单声明式
typedef-name                            |typedef-名     |类型别名，`typedef`或`using`，可为模板<br>无名类的首个typedef名为连接名，这种类应当与C结构体兼容：无成员代码，无基类
typedef specifier                       |typedef 说明符 |
typeid expression                       |typeid 表达式  |后缀表达式。`<typeinfo>`，返回`type_info`或其派生类对象左值，存续直到程序结束<br>非多态对象为免求值操作数，多态对象查询RTTI，全派生对象的动态类型<br>查询空指针解引用的对象抛出`bad_typeid`
typename specifier                      |typename 说明符|指定待决名是类型

### U

|English|中文|说明|
|-|-|-|
UCS, Universal Multiple-Octet Coded Character Set   |UCS，通用字符集，通用多八位编码字符集
ud-suffix                               |ud-后缀    |用户定义字面量后缀，用于查找字面量运算符（模板）函数
unary                                   |一元
unary fold                              |一元折叠       |仅展开包组
unary left fold                         |一元左折叠     |`... op pack`
unary minus operator                    |一元减运算符   |一元运算符/表达式，算术、无作用域枚举，提升整型和枚举，无符号同余
unary operator                          |一元运算符     |`&`：取地址，`*`：间接，`+`：正，`-`：负，`!`：非，`~`：反
unary plus operator                     |一元加运算符   |一元运算符/表达式，算术、指针、无作用域枚举，提升整型和枚举
unary right fold                        |一元右折叠     |`pack op ...`
unblock                                 |解除阻塞
undefined                               |未定义的
undefined behavior                      |UB，未定义行为 |任意可能行为
underlying type                         |底层类型
unevaluated operand                     |免求值操作数   |编译期语法结构，仅获得类型/元信息，不求值
unexpanded parameter pack               |未展开形参包组
Unicode                                 |Unicode，统一码
union                                   |联合体
union-like class                        |类似联合体的类
universal-character-name                |UCN，通用字符名|概念上兼容任何字符集的字符集，UCS，`\uxxxx`, `\Uxxxxxxxx`
unnamed class                           |无名类
unnamed enumeration                     |无名枚举
unnamed namespace                       |无名命名空间
unordered initialization                |无序初始化     |静态变量初始化：模板特例变量
unqualified name                        |无限定名       |没有前置限定（`::`,`.`,`->`等）的名字
unqualified name lookup                 |无限定名查找   |对无限定名在直接作用域中进行无限定搜索：<br>转换函数中的无限定名先依照转换函数标识的方式查找一次，<br>有限定的友元声明先在指定作用域中查找一次
unqualified search                      |无限定搜索     |对无限定名在指定作用域进行逐层搜索的过程
unscoped enumeration                    |无作用域枚举
unscoped enumerator                     |无作用域枚举符
unsequenced                             |无顺序的       |可重叠执行：操作数、子表达式的求值
unsigned                                |无符号
unsigned integer type                   |无符号整数类型 |标准、扩充无符号整数
unspecified                             |未指明的
unspecified behavior                    |未指明的行为   |多种允许可能行为中的某一种
upper bound                             |上界
user provided function                  |用户提供的函数
user-declared                           |用户声明的
user-defined character literal          |用户定义字符字面量     |预处理记号，记号，字符字面量+后缀，类型运算符 `operator "" X(Tchar t)`
user-defined conversion                 |用户定义转换
user-defined floating-point literal     |用户定义浮点字面量     |无后缀浮点字面量+自定义后缀，先类型后通配，类型运算符只支持`long double`
user-defined integer literal            |用户定义整数字面量     |无后缀整数字面量+自定义后缀，先类型后通配，类型运算符只支持`unsigned long long`
user-defined literal                    |用户定义字面量         |数值/字符/字符串字面量+字面量后缀，字面量运算符（模板）函数
user-defined string literal             |用户定义字符串字面量   |预处理记号，记号，字符串字面量+后缀，支持字符串拼接，先模板后非模板`operator "" X(const Tchar*, size_t)`
using-declaration                       |using-声明式           |引入已有实体的名字，所在位置限制其种类，没有连接
using-directive                         |using-指令             |引入其中所有已有可达实体的名字
using-enum-declaration                  |using-枚举声明式       |作用类似using-指令，引入所有已有枚举符的名字
usual arithmetic conversions            |一般算术转换           |操作数->公共类型->结果
UTF, Unicode Transformation Format      |UTF，Unicode 转换格式
UTF-8 string literal                    |UTF-8 字符串字面量     |前缀为`u8`，类型为`const char8_t[n]`
UTF-16 string literal                   |UTF-16 字符串字面量    |前缀为`u`，类型为`const char16_t[n]`
UTF-32 string literal                   |UTF-32 字符串字面量    |前缀为`U`，类型为`const char32_t[n]`

### V

|English|中文|说明|
|-|-|-|
vacuous initialization                  |无为初始化 |无实际动作（平凡）的默认初始化
valid                                   |有效，合法
valid but unspecified state             |有效但未指明的状态     |被移动后的状态
value                                   |值         |一种实体，对象的状态
value category                          |值类别     |glvalue: lvalue, xvalue; rvalue: xvalue, prvalue
value computation                       |值计算
value representation                    |值表示     |构成对象状态的位的值，排除填充位
value-initialize                        |值初始化
variable                                |变量       |对象或引用，不包括非静态数据成员引用
variable template                       |变量模板
variadic function                       |变参函数   |以`...`形参结尾的函数，需要`va_XX`<br>以函数形参包组结尾的函数
variadic template                       |变参模板
variant                                 |变体
variant member                          |可变成员
viable                                  |可行的
virtual                                 |虚的
virtual base                            |虚基类
virtual function                        |虚函数
virtual function call                   |虚函数调用
virtual specifier                       |virtual 说明符 |虚成员函数
visible                                 |可见
visible side effect                     |可见副作用 |非原子性ML的可见性由发生早于HapB关系决定
visit                                   |视察，访问
void                                    |空
volatile                                |易失的     |免除编译器优化，可观察行为
volatile object                         |volatile 对象  |volatile T 的对象或其子对象
volatile-qualified                      |volatile 限定的

### W

|English|中文|说明|
|-|-|-|
weak order                              |弱序   |自反，传递，连通，不要求反对称性，如某些 <=
weakly parallel forward progress guarantees |弱并行向前进展保证   |不保证进展，但可与带保证委托阻塞配合来保证进展
well-formed                             |良构的     |语法和语义没有问题的代码
while statement                         |while 语句
whitespace                              |空白       |空白字符和注释
whitespace character                    |空白字符   |``, `\t`, `\v`, `\f`, `\n`, `\r` 等
wide character                          |宽字符
wide character literal                  |宽字符字面量   |类型为 `wchar_t`，除不可编码和多字符外，编码为执行宽字符
wide string literal                     |宽字符串字面量 |类型为 `const wchar_t[n]`，编码为执行宽字符
write-read coherence                    |写-读协调性    |原子性 M 的 WA HapB RB，则两个值符合 M 的改动顺序
write-write coherence                   |写-写协调性    |原子性 M 的 WA HapB WB，则两个值符合 M 的改动顺序

### X

|English|中文|说明|
|-|-|-|
xvalue                                  |临限值 |将被重用的对象，有地址但可作为右值

### Y

|English|中文|说明|
|-|-|-|
yield-expression                        |产出表达式     |`co_yield expr`。等价于`co_await p.yield_value(expr)`

### Z

|English|中文|说明|
|-|-|-|
zero-initialization                     |零初始化       |未以常量初始化的静态/线程变量在线程启动时置零
