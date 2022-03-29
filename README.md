# Syntax Of Redoc

## Overview

Redoc is a markup language, all special things are in `[]`.


## Terms Translation Table

#### A
|English|中文|说明|
|-|-|-|
abstract class                          |抽象类
abstract machine                        |抽象机器
access                                  |访问       |读取或改动标量对象
access check                            |访问检查
access control                          |访问控制
access specifier                        |访问说明符
acquire                                 |获取
active member                           |活跃成员
addition operator                       |加法运算符
additive operator                       |加性运算符
address                                 |地址
address-of operator                     |取地址运算符
aggregate                               |聚合，聚合对象
aggregate initialization                |聚合初始化
aggregate type                          |聚合类型
algorithm                               |算法
alias                                   |别名
alias declaration                       |别名声明
alias template                          |别名模板
alignment                               |对齐
alignment requirement                   |对齐要求
allocate                                |分配
allocation function                     |分配函数
alternative token                       |代用记号
ambiguity                               |歧义
amendment                               |文档修订
amortized constant                      |摊销常量
and operator                            |与运算符
apply                                   |运用，实施，适用于
arbitrary-positional stream             |可任意定位流   |可seek
architecture                            |体系结构
argument                                |实参，实际参数 |函数，函数式宏，模板，throw
argument-dependent name lookup          |依赖于实参的名字查找
arithmetic                              |算术的
arithmetic exception                    |算术异常
arithmetic type                         |算术类型
array                                   |数组
array declarator                        |函数声明符
array element                           |数组元素
array of N T                            |T 的 N 元素数组
array of unknown bound of T             |T 的边界未知数组
array-to-pointer conversion             |数组向指针转换
arrow operator                          |箭头运算符
as-if rule                              |“如同”规则     |以可观察行为为准
asm definition                          |asm 定义式
assembler                               |汇编器，汇编
assertion                               |断言
assignment                              |赋值
assignment expression                   |赋值表达式
assignment operator                     |赋值运算符
associated class                        |关联类
associated namespace                    |关联命名空间
atomic                                  |原子性
attach to module                        |附属于模块
attribute                               |特性标注，特性
attribute declaration                   |特性标注声明
automatic storage duration              |自动存储期
await-expression                        |等待表达式
awaitable                               |可等待体

#### B
|English|中文|说明|
|-|-|-|
barrier                                 |关卡
base characteristic                     |基础特征
basic character set                     |基本字符集
basic execution character set           |基本执行字符集
basic source character set              |基本源字符集
behavior                                |行为
binary                                  |二进制，二元
binary fold                             |二元折叠
binary left fold                        |二元左折叠
binary operator                         |二元运算符
binary right fold                       |二元右折叠
bit                                     |位
bit-field                               |位字段
bitwise and operator                    |按位与运算符
bitwise negation operator               |按位反运算符
bitwise or operator                     |按位或运算符
bitwise xor operator                    |按位亦或运算符
block                                   |1. 代码块 <br>2. 阻塞
block declaration                       |块声明式
block scope                             |块作用域
block statement                         |块语句
boolean                                 |布尔
boolean conversion                      |布尔转换
break statement                         |break 语句
built-in operator                       |内建运算符
byte                                    |字节

#### C
|English|中文|说明|
|-|-|-|
cache                                   |高速缓存
call                                    |调用
capture                                 |俘获
capture by copy                         |按复制俘获
captured by reference                   |按引用俘获
carry a dependency to                   |传递依赖给
case label                              |case 标号
cast                                    |强制转换，类型强制转换
cast away constness                     |强制移除常量性
catch                                   |捕获
character                               |字符
character container type                |字符容器类型   |`basic_string`等模板的类型形参
character set                           |字符集
class                                   |类
class declaration                       |类声明式
class definition                        |类定义式
class granding friendship               |授予友元关系
class member                            |类成员
class member access expression          |类成员访问表达式
class member access operator            |类成员访问运算符
class scope                             |类作用域
class specifier                         |类说明符
class template deduction                |类模板推断
class template                          |类模板
clause                                  |子句
closure object                          |闭包对象
closure type                            |闭包类型
collating element                       |校排元素   |一些语言中会将多个字符合并当做一个字符校排
comma expression                        |逗号表达式
comma operator                          |逗号运算符
comment                                 |注释
common initial sequence                 |共同起始序列
common type                             |公共类型
compile                                 |编译
complete object                         |完整对象
complete type                           |完整类型
compliance                              |遵从性
component                               |组件
composite pointer type                  |组合指针类型
compound assignment expression          |复合赋值表达式
compound assignment operator            |复合赋值运算符
compound statement                      |复合语句   |块语句，语句块，花括号
compound type                           |复合类型
concept                                 |概念
concurrency                             |并发性
concurrent                              |并发的
conditional expression                  |条件表达式
conditional operator                    |条件运算符
conditionally-supported                 |有条件支持的   |编译器实现可以选择不支持
conflict                                |冲突
conformance requirements                |一致性规定
conjunction                             |合取
const cast                              |const 强制转换
const safety                            |const 安全性
constant                                |常量
constant expression                     |常量表达式
constant initializer                    |常量初始化式
constant subexpression                  |常量子表达式   |不妨碍其外围表达式成为核心常量表达式
constexpr constructor                   |constexpr 构造函数
constexpr function                      |constexpr 函数
constexpr if statement                  |constexpr if 语句
constexpr specifier                     |constexpr 说明符
constituent expression                  |成分表达式
constness                               |常量性
construct                               |语言构造
constructor                             |构造函数
consume                                 |消费
container                               |容器
context                                 |语境，上下文
contextually converted to bool          |按语境转换为 bool
continue statement                      |continue 语句
contravariant                           |逆变
conversion                              |类型转换，转换
conversion function                     |转换函数
conversion rank                         |转换等级
converted constant expression           |经转换的常量表达式
converting constructor                  |转换构造函数
copy                                    |复制，副本
copy assignment operator                |复制赋值运算符
copy constructor                        |复制构造函数
copy-initialization                     |复制初始化
core constant expression                |核心常量表达式
corresponding instance                  |对应实例       |实现所对应的抽象机器
covariant                               |协变
create                                  |创建
cv pointer to cv T                      |cv T 的 cv 指针
cv-decomposition                        |cv 分解
cv-qualification                        |cv 限定
cv-qualification signature              |cv 限定签名
cv-qualifier                            |cv 限定符


#### D
|English|中文|说明|
|-|-|-|
data                                    |数据
data member                             |数据成员
data race                               |数据竞争
data structure                          |数据结构
data type                               |数据类型
deallocate                              |回收
deallocation function                   |回收函数
decay                                   |退化
declaration                             |声明式，声明   |代码结构称为‘声明式’
declaration statement                   |声明语句
declarative region                      |声明区
declarator                              |声明符
declare                                 |声明
decltype specifier                      |decltype 说明符
decode                                  |解码
decrement operator                      |减量运算符
deduce                                  |推断
deduction guide                         |推断导引
default argument                        |默认实参
default argument promotion              |默认实参提升
default behavior                        |缺省行为   |某些函数，如果程序不提供就采用实现的缺省版本
default constructor                     |默认构造函数
default label                           |default 标号
default member initializer              |默认成员初始化式
default-initialization                  |默认初始化
defaulted                               |预置的，默认的，缺省的
defaulted function                      |预置函数
define                                  |定义
definition                              |定义式，定义   |代码结构称为‘定义式’，实体称为‘定义’
delegating constructor                  |委派构造函数
delete                                  |删除
delete expression                       |delete 表达式
delete operator                         |delete 运算符
deleted                                 |已删除的，弃置的
deleted definition                      |弃置定义式
deleted function                        |弃置函数
dependency-ordered before               |按依赖序早于
dependent name                          |待决名字
deprecated                              |被摒弃的   |因为有某种问题而不建议使用的，未来会被移除的功能设施
derived class                           |派生类
designated initializer                  |定名初始化式
destroy                                 |销毁
destruction                             |销毁
destructor                              |析构函数
device                                  |设备
diagnosable rule                        |可诊断规则
diagnostic message                      |诊断消息   |编译器报错
digraph                                 |二连符
direct base class                       |直接基类
direct-initialization                   |直接初始化
direct-list-initialization              |直接列表初始化     |直接进行的列表初始化
direct-non-list-initialization          |直接非列表初始化   |直接进行的其他初始化
directive                               |指令
directive-introducing token             |指令发起记号
disambiguation                          |歧义消解
discarded statement                     |弃用语句
discarded-value expression              |弃值表达式
disjunction                             |析取
division operator                       |除法运算符
do statement                            |do 语句
dot operator                            |点运算符
dynamic                                 |动态
dynamic cast                            |动态强制转换
dynamic initialization                  |动态初始化
dynamic storage duration                |动态存储期
dynamic type                            |动态类型       |纯右值的动态类型编译期已知

#### E
|English|中文|说明|
|-|-|-|
ECMA, European Computer Manufacturers Association   |ECMA，欧洲计算机制造商协会
elaborated type specifier               |详述类型说明符
element                                 |元素
eligible special member function        |合格的特殊成员函数
empty declaration                       |空声明
empty statement                         |空语句
encapsulate                             |封装
enclosing class                         |外围类
enclosing namespace                     |外围命名空间
enclosing scope                         |外围作用域
encode                                  |编码
endian                                  |端序
entity                                  |实体
entry                                   |入口       |函数，catch，代码块
enumeration                             |枚举
enumeration scope                       |枚举作用域
enumeration specifier                   |枚举说明符
enumeration type                        |枚举类型
enumerator                              |枚举符
equality                                |相等
equality operator                       |相等运算符
equivalence                             |等价
equivalence class                       |等价类 |正则表达式，[=a=]，匹配校排等价字符
error                                   |错误，误差
escape character                        |转义字符
escape sequence                         |转义序列
evaluation                              |求值
exception                               |异常
exception handler                       |异常处理器
exception specification                 |异常说明
execute                                 |执行，运行
execution agent                         |执行代理
execution character set                 |执行字符集
execution step                          |执行步骤
explicit                                |显式，明确
explicit instantiation declaration      |显式实例化生命式
explicit specialization                 |显式特化式
explicit specifier                      |explicit 说明符
explicit type conversion                |显式类型转换
explicitly captured                     |显式俘获
explicitly defaulted function           |显式预置的函数
exponent                                |指数
export declaration                      |导出声明式
exported declaration                    |被导出声明式
exposure                                |显露式
expression                              |表达式
expression-equivalent                   |按表达式等价   |表达式求值的真实效果相同（？）
extend namespace                        |扩展命名空间
extended alignment                      |扩充对齐
extended character set                  |扩展字符集
extended execution character set        |扩展执行字符集
extended integer type                   |扩充整数类型
extended signed integer type            |扩充有符号整数类型
extended source character set           |扩展源字符集
extended unsigned integer type          |扩充无符号整数类型
extension                               |扩展           |实现提供的额外功能
extern specifier                        |extern 说明符
external linkage                        |外部连接       |跨翻译单元可见

#### F
|English|中文|说明|
|-|-|-|
facet                                   |刻面
facility                                |功能设施   |语言功能或程序库组件
failure                                 |失败，故障
fallthrough statement                   |直落语句
fault                                   |故障，错误
feature                                 |功能特性，特性
fence                                   |栅栏，内存栅栏
field                                   |字段
file                                    |文件           |可观察行为
final overrider                         |最终覆盖函数
finite state machine                    |有限状态机     |用于实现正则表达式的数据结构
floating conversion                     |浮点转换
floating-integral conversion            |浮点整形转换
floating-point                          |浮点
floating-point promotion                |浮点提升
fold expression                         |折叠表达式
for statement                           |for 语句
format specifier                        |格式说明符     |正则表达式中被替换部分的格式说明
forward declaration                     |前置声明式
forward progress                        |向前进展，进展
fraction                                |小数，分数
free store                              |自由存储       |new/delete 或 malloc() 等所管理的堆内存
freestanding implementation             |自立式实现     |无操作系统支持
friend                                  |友元
friend class                            |友元类
friend function                         |友元函数
friend specifier                        |friend 说明符
full-expression                         |全表达式
function                                |函数
function body                           |函数体
function call expression                |函数调用表达式
function call operator                  |函数调用运算符
function declaration                    |函数声明式
function declarator                     |函数声明符
function definition                     |函数定义式
function object                         |函数对象
function overloading                    |函数重载
function parameter pack                 |函数形参包组
function pointer conversion             |函数指针转换
function pointer type                   |函数指针类型
function prototype                      |函数原型
function scope                          |函数作用域
function specifier                      |函数说明符
function template                       |函数模板
function try block                      |函数 try 块
function-like macro                     |函数式宏
function-to-pointer conversion          |函数向指针转换
fundamental alignment                   |基础对齐
fundamental type                        |基础类型

#### G
|English|中文|说明|
|-|-|-|
generic lambda expression               |泛型 lambda 表达式
global                                  |全局的
global namespace                        |全局命名空间
global object                           |全局对象
global scope                            |全局作用域
global variable                         |全局变量
glvalue                                 |泛左值
goto statement                          |goto 语句
grammar                                 |文法
greater-than operator                   |大于运算符
greater-than-or-equal-to operator       |大于或等于运算符

#### H
|English|中文|说明|
|-|-|-|
handler                                 |处理器     |捕获并处理异常的代码块
handler function                        |处理函数   |`new_handler`等
happens after                           |发生晚于
happens before                          |发生早于
header                                  |头文件
header unit                             |头文件单元 |模块
high-order bit                          |高序位
hosted implementation                   |宿主式实现 |在操作系统下运行

#### I
|English|中文|说明|
|-|-|-|
identifier                              |标识符
identifier label                        |标识符标号
IEC, International Electrotechnical Commission  |IEC，国际电工委员会
IEEE, Institute of Electrical and Electronic    |IEEE，电气与电子工程师协会
if statement                            |if 语句
ill-formed                              |非良构的   |语法或语义无效的代码
immediate subexpression                 |直接子表达式
implementation                          |实现
implementation limits                   |实现限额
implementation-defined                  |由实现定义的   |编译器实现自行决定的某些良构代码的行为
implicit                                |隐式，暗中，隐含
implicit conversion sequence            |隐式转换序列
implicit type conversion                |隐式类型转换
implicitly captured                     |隐式俘获
implicitly declared function            |隐式声明的函数
import                                  |导入
import declaration                      |导入声明式
impose                                  |施加
incomplete type                         |不完整类型
incomplete-defined object type          |定义不完整的对象类型
increment operator                      |增量运算符
indeterminately sequenced               |未定顺序的
indirect base class                     |间接基类
indirection operator                    |间接运算符
inequality operator                     |不相等运算符
initialization                          |初始化
initialize                              |初始化
initializer                             |初始化式
injected class name                     |注入类名
inline function                         |内联函数
inline namespace                        |内联命名空间
inline specifier                        |inline 说明符
inline variable                         |内联变量
input                                   |输入
instance                                |实例
instantiate                             |实例化，落实
instantiation                           |实例化式，实例化   |模板实体落实为具体实体
instantiation unit                      |实例化单元
integer                                 |整数
integer conversion rank                 |整数转换等级
integer type                            |整数类型
integral constant expression            |整型常量表达式
integral conversion                     |整形转换
integral promotion                      |整形提升
integral type                           |整型类型
inter-thread happens before             |线程间发生早于
interactive device                      |交互设备   |I/O 设备，可观察行为
internal linkage                        |内部连接
invalid                                 |无效，非法
invocation                              |调用，执行
invoke                                  |调用，执行 |多用于除函数之外的场合，如宏等
iostream                                |输入输出流, I/O 流
ISO, International Organization for Standardization |ISO，国际标准化组织
iteration statement                     |循环语句，重复语句
iterator                                |迭代器

#### J
|English|中文|说明|
|-|-|-|
join                                    |合并（线程）
jump statement                          |跳转语句

#### K
|English|中文|说明|
|-|-|-|
keyword                                 |关键字

#### L
|English|中文|说明|
|-|-|-|
label                                   |标号
labeled statement                       |带标号语句
lambda expression                       |lambda 表达式
language linkage                        |语言连接
latch                                   |门栓
layout-compatible enumeration           |布局兼容枚举
layout-compatible type                  |布局兼容类型
left shift operator                     |左移运算符
less-than operator                      |小于运算符
less-than-or-equal-to operator          |小于或等于运算符
lexical                                 |词法
library                                 |程序库
lifetime                                |生存期
line                                    |行，文本行
link                                    |连接   |将已翻译实体收集并组合成程序映像
linkage                                 |连接，连接性
linkage specification                   |连接说明
list                                    |列表
list-initialization                     |列表初始化
literal                                 |字面量
literal type                            |字面类型
local                                   |局部，局部的
local                                   |局部的
local class                             |局部类
local class                             |局部类
local lambda expression                 |局部 lambda 表达式
local scope                             |局部作用域
local variable                          |局部变量
locale                                  |地域
locale-specific                         |地域特有的
lock                                    |锁，锁定
lock-free                               |无锁
locus                                   |位点
logical and operator                    |逻辑与运算符
logical negation operator               |逻辑非运算符
logical or operator                     |逻辑或运算符
low-order bit                           |低序位
lower bound                             |下界
lvalue                                  |左值
lvalue-to-rvalue conversion             |左值向右值转换

#### M
|English|中文|说明|
|-|-|-|
macro                                   |宏
match                                   |匹配   |正则表达式模式与目标文本发生对应
materialize                             |实质化
member                                  |成员
member function                         |成员函数
member type                             |成员类型
memory                                  |内存
memory location                         |内存位置
memory management                       |内存管理
memory model                            |内存模型
modification order                      |改动顺序
modifier function                       |改动函数
most derived class                      |全派生类
most derived object                     |全派生对象
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
multiplicative operator                 |乘性运算符
mutable specifier                       |mutable 说明符
mutex                                   |互斥体

#### N
|English|中文|说明|
|-|-|-|
name                                    |名字
name hiding                             |名字隐藏
name lookup                             |名字查找
name mangling                           |名字重整
named                                   |具名的
namespace                               |命名空间
namespace alias                         |命名空间别名
namespace definition                    |命名空间定义式
namespace scope                         |命名空间作用域
narrow character                        |窄字符
necessarily reachable                   |必定可达
nest                                    |嵌套
nested class                            |嵌套类
nested name                             |嵌套名
nested name specifier                   |嵌套名说明符
nested type                             |嵌套类型
new expression                          |new 表达式
new operator                            |new 运算符
no diagnostic is required               |无须诊断
noexcept expression                     |noexcept 表达式
noexcept function of () cv ref returning| T  T 为返回类型的 () cv ref 的 noexcept 函数
noexcept operator                       |noexcept 运算符
non-allocating form                     |非分配形式
non-throwing exception specification    |无抛出异常说明
non-vacuous initialization              |非无为初始化
normalized                              |正规化的
normative                               |规范性的   |作为正式内容的文本章节或参考文献
null                                    |空
null character                          |空字符
null member pointer conversion          |空成员指针转换
null member pointer value               |空成员指针值
null pointer                            |空指针
null pointer constant                   |空指针常量
null pointer conversion                 |空指针转换
null pointer literal                    |空指针字面量
null pointer value                      |空指针值
null statement                          |空语句
null-terminated                         |空终结

#### O
|English|中文|说明|
|-|-|-|
object                                  |对象
object expression                       |对象表达式
object model                            |对象模型
object pointer type                     |对象指针类型
object representation                   |对象表示
object-like macro                       |对象式宏
observable behavior                     |可观察行为
observer function                       |探察函数
obstruction-free                        |无阻碍
odr-used                                |ODR 式使用
one-definition rule                     |单一定义规则，ODR
opaque enum declaration                 |笼统枚举声明式
operand                                 |操作数
operator                                |运算符
operator overloading                    |运算符重载
or operator                             |或运算符
ordinary character literal              |普通字符字面量
ordinary string literal                 |普通字符串字面量
output                                  |输出
over-aligned                            |过量对齐
overflow                                |溢出
overload                                |重载
overload resolution                     |重载决议
overloaded function                     |重载函数
overloaded operator                     |重载运算符
override                                |覆盖
overrider                               |覆盖函数

#### P
|English|中文|说明|
|-|-|-|
pack expansion                          |包组展开式
pair                                    |对偶
parallel                                |并行的
parameter                               |形参，形式参数 |函数，catch，函数式宏，模板
parameter pack                          |形参包组
parameter-type-list                     |形参类型列表   |函数签名
parenthesized expression                |带括号表达式
partial order                           |偏序，非严格偏序，半序 |自反，反对称，传递，不要求完全性，如 <=
partial specialization                  |部分特化，部分特化式
placeholder                             |占位符
placeholder type deduction              |占位符类型推断
placement allocation function           |放置式分配函数
placement deallocation function         |放置式回收函数
placement new                           |放置式 new
point of declaration                    |声明点
point of definition                     |定义点
pointer                                 |指针
pointer arithmetic                      |指针算术
pointer conversion                      |指针转换
pointer declarator                      |指针声明符
pointer to member                       |成员指针
pointer to member conversion            |成员指针转换
pointer to member declarator            |成员指针声明符
pointer to member of X of type cv T     |cv T 类型的 X 的成员指针
pointer to member operator              |成员指针运算符
pointer to T                            |T 的指针，指向 T 的指针
pointer-interchangable                  |指针可相互转换
polymorphic                             |多态的
POSIX, Portable Operating System Interface  |POSIX，可移植操作系统接口
postfix                                 |后缀
postfix decrement operator              |后置减量运算符
postfix expression                      |后缀表达式
postfix increment operator              |后置增量运算符
potential scope                         |潜在作用域
potentially concurrent                  |潜在并发
potentially evaluated                   |潜在求值的
potentially throwing                    |潜在抛出异常的     |有能力抛出异常
prefix                                  |前缀
prefix decrement operator               |前置减量运算符
prefix increment operator               |前置增量运算符
preprocess                              |预处理
preprocessing directive                 |预处理指令
preprocessing token                     |预处理记号
primary equivalence class               |主等价类   |校排中具有相同主排序键的字符或字符串
primary expression                      |初等表达式
primary sort key                        |主排序键   |校排中仅按主题字符形状分类的排序字符
primary template                        |主模板
private                                 |私有
program                                 |程序
program-defined specialization          |由程序定义的特化式
program-defined type                    |由程序定义的类型
programming language                    |程序设计语言
projection                              |投射       |算法对输入元素进行自定义变换
promise                                 |承诺
prospective destructor                  |预期析构函数
protected                               |受保护
prototype                               |原型
prvalue                                 |纯右值
pseudo destructor call                  |伪析构函数调用
public                                  |公用，公开
punctuator                              |标点，标点符号
pure virtual function                   |纯虚函数
purview                                 |视野

#### Q
|English|中文|说明|
|-|-|-|
qualification                           |限定，限定性
qualified name                          |限定名
qualifier                               |限定符

#### R
|English|中文|说明|
|-|-|-|
radix point                             |小数点
range                                   |范围
range-based for statement               |基于范围的 for 语句
raw string literal                      |原始字符串字面量
reachable                               |可达的
reaching scope                          |可达作用域
recursive function call                 |递归函数调用
ref-qualifier                           |引用限定符 |函数类型，成员函数的 & 或 &&
reference                               |引用
reference declarator                    |引用声明符
reference to cv T                       |cv T 的引用
reference to T                          |T 的引用，指代 T 的引用
reference type                          |引用类型，T& 或 T&&
referenceable type                      |可被引用的类型 |可以创建 T& 的类型 T，包括引用类型
regex                                   |正则表达式
region                                  |区，区域
regular expression                      |正则表达式
reinterpret cast                        |重解释强制转换
relational operator                     |关系运算符
relaxed                                 |宽松的
relaxed atomic operation                |宽松原子性操作
relaxed pointer safety                  |宽松指针安全性
release                                 |释放
release sequence                        |释放序列
remainder operator                      |求余运算符
replacement function                    |替代函数   |程序定义的用以替换实现的缺省函数的函数，如`operator new`
repositional stream                     |可重定位流 |可 seek 到之前经过的位置
representation                          |表示
required behavior                       |预期行为   |由标准规定的行为，实现或程序提供的函数应当遵守
requirement                             |规定，要求
requires-clause                         |requires 子句
reserved                                |保留的     |规定使用权属于标准或实现的名字或实体
reserved function                       |保留函数
restriction                             |限制，要求
resumption                              |恢复
return                                  |返回
return statement                        |return 语句，返回语句
return type                             |返回类型
return value                            |返回值
right shift operator                    |右移运算符
rounding                                |舍入
run                                     |运行
runtime type identification             |运行时类型标识
rvalue                                  |右值

#### S
|English|中文|说明|
|-|-|-|
safely-derived pointer                  |安全衍生指针
scalar                                  |标量
scalar type                             |标量类型
scope                                   |作用域，范围
scope resolution operator               |作用域解析运算符
scoped enumeration                      |有作用域枚举
scoped enumerator                       |有作用域枚举符
selection statement                     |选择语句
semantics                               |语义
semaphore                               |信号量
sequence                                |序列   |容器的一种
sequenced after                         |按顺序晚于
sequenced before                        |按顺序早于
sequential consistency                  |顺序一致性
shift operator                          |移位运算符
side effect                             |副作用
signal                                  |信号
signal handler                          |信号处理函数
signature                               |签名   |名字，形参类型列表，外围类，命名空间，尾部 requires，（模板）返回类型，模板头，（特化）模板实参
signed                                  |有符号
signed integer type                     |有符号整数类型
similar type                            |相似类型
sizeof operator                         |sizeof 运算符
source character set                    |源字符集
source file                             |源文件
specialization                          |特化式，特例   |代码结构为‘特化式’，实体为‘特例’
specialize                              |特化
specifier                               |说明符
stable algorithm                        |稳定算法   |保留输入元素顺序
standard conversion sequence            |标准转换序列
standard integer type                   |标准整数类型
standard signed integer type            |标准有符号整数类型
standard unsigned integer type          |标准无符号整数类型
standard-layout class                   |标准布局类
standard-layout type                    |标准布局类型
statement                               |语句
static                                  |静态
static assertion                        |静态断言
static cast                             |静态强制转换
static initialization                   |静态初始化
static specifier                        |static 说明符
static storage duration                 |静态存储期
static type                             |静态类型   |表达式的可声明类型
static_assert declaration               |static_assert 声明式
stop token                              |停止令牌
storage                                 |存储
storage class specifier                 |存储类说明符
storage duration                        |存储期
storage management                      |存储管理
stream                                  |流 |输入或输出流
strict                                  |严格的
strict partial order                    |严格偏序，拟序 |反自反，反对称，传递，不要求完全性，如 <
strict total order                      |严格全序   |具有完全性的严格偏序，完整的 <
strict weak order                       |严格弱序   |连通的严格偏序，不可比较关系为等价关系，如 <
string                                  |字符串
struct                                  |结构体
structure tag                           |结构体标签
structured binding declaration          |结构化绑定声明式
sub-expression                          |子表达式   |正则表达式：括号标记的部分
subexpression                           |子表达式
subnormal                               |次正规的
subobject                               |子对象
subscript operator                      |下标运算符
substatement                            |子语句
suspension                              |暂停
switch statement                        |switch 语句
synchronization                         |同步
synchronize                             |同步
synchronize with                        |同步于
syntactic category                      |语法范畴   |BNF 产生式非终结符
syntax                                  |语法
syntax notation                         |语法表示法

#### T
|English|中文|说明|
|-|-|-|
target constructor                      |目标构造函数
template                                |模板
template argument                       |模板实参
template argument deduction             |模板实参推断
template instantiation                  |模板实例化
template non-type parameter             |模板非类型形参 |三种模板形参之一
template parameter                      |模板形参
template parameter pack                 |模板形参包组
template parameter scope                |模板形参作用域
template template parameter             |模板模板形参   |三种模板形参之一
template type parameter                 |模板类型形参   |三种模板形参之一
temporary                               |临时对象
temporary expression                    |临时对象表达式
temporary materialization conversion    |临时对象实质化转换
term                                    |术语
terminate                               |终止
thread                                  |线程
thread of execution                     |执行线程，线程
thread storage duration                 |线程存储期
thread_local specifier                  |thread_local 说明符
thread-local variable                   |线程局部变量
throw                                   |抛出
token                                   |记号
top-level cv-qualifier                  |顶层 cv 限定符
total order                             |全序，非严格全序，线序 |具有完全性的偏序，完整的 <=
traceable pointer                       |可追踪指针
trailing requires-clause                |尾部 requires 子句 |模板函数
trailing return type                    |尾部返回类型
traits class                            |特征类     |提供与某个主类型形参有关的静态自定义能力，模板类
translate                               |翻译       |编译
translation phase                       |翻译阶段
translation unit                        |翻译单元
trivial class                           |平凡类
trivial copy constructor                |平凡复制构造函数
trivial default constructor             |平凡默认构造函数
trivial destructor                      |平凡析构函数
trivial move constructor                |平凡移动构造函数
trivial type                            |平凡类型
trivially copyable class                |可平凡复制类
trivially copyable type                 |可平凡复制类型
truncation                              |截断
tuple                                   |元组
type                                    |类型
type identification                     |类型标识
type pun                                |类型双关
type specifier                          |类型说明符
typedef declaration                     |typedef 声明式
typedef specifier                       |typedef 说明符
typename specifier                      |typename 说明符

#### U
|English|中文|说明|
|-|-|-|
UCS, Universal Multiple-Octet Coded Character Set   |UCS，通用字符集，通用多八位编码字符集
unary                                   |一元
unary fold                              |一元折叠
unary left fold                         |一元左折叠
unary minus operator                    |一元减运算符
unary operator                          |一元运算符
unary plus operator                     |一元加运算符
unary right fold                        |一元右折叠
unblock                                 |解除阻塞
undefined                               |未定义的
undefined behavior                      |UB，未定义行为     |任意可能行为
underlying type                         |底层类型
unevaluated operand                     |免求值操作数
unexpanded parameter pack               |未展开形参包组
Unicode                                 |Unicode，统一码
union                                   |联合体
union-like class                        |类似联合体的类
universal character name                |通用字符名
unnamed class                           |无名类
unnamed enumeration                     |无名枚举
unnamed namespace                       |无名命名空间
unqualified name                        |未限定名
unscoped enumeration                    |无作用域枚举
unscoped enumerator                     |无作用域枚举符
unsequenced                             |无顺序的
unsigned                                |无符号
unsigned integer type                   |无符号整数类型
unspecified                             |未指明的
unspecified behavior                    |未指明的行为   |多种允许可能行为中的某一种
upper bound                             |上界
user provided function                  |用户提供的函数
user-declared                           |用户声明的
user-defined conversion                 |用户定义转换
user-defined literal                    |用户定义字面量
using declaration                       |using 声明式
using directive                         |using 指令
usual arithmetic conversions            |一般算术转换

#### V
|English|中文|说明|
|-|-|-|
valid                                   |有效，合法
valid but unspecified state             |有效但未指明的状态     |被移动后的状态
value                                   |值
value category                          |值类别
value computation                       |值计算
value representation                    |值表示
value-initialize                        |值初始化
variable                                |变量
variable template                       |变量模板
variadic function                       |变参函数
variadic template                       |变参模板
variant                                 |变体
variant member                          |可变成员
viable                                  |可行的
virtual                                 |虚的
virtual base                            |虚基类
virtual function                        |虚函数
virtual function call                   |虚函数调用
virtual specifier                       |virtual 说明符
visible                                 |可见
visit                                   |视察，访问
void                                    |空
volatile                                |易失的     |免除编译器优化，可观察行为

#### W
|English|中文|说明|
|-|-|-|
weak order                              |弱序   |自反，传递，连通，不要求反对称性，如某些 <=
well-formed                             |良构的     |语法和语义没有问题的代码
while statement                         |while 语句
whitespace                              |空白，空格
wide character                          |宽字符

#### X
|English|中文|说明|
|-|-|-|
xvalue                                  |临限值

#### Y
|English|中文|说明|
|-|-|-|
yield-expression                        |产出表达式

#### Z
|English|中文|说明|
|-|-|-|
zero-initialization                     |零初始化

