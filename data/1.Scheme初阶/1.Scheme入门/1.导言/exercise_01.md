scheme编程语言由小盖伊·史提尔和杰拉德·杰伊·萨斯曼在1975年设计。是Lisp的两种主要方言之一。

它是一种多范式编程语言，你既可以以纯函数式的风格来编程，也可以以面向过程，面向对象甚至于逻辑式的风格来使用。

Scheme自设计以来以其独特的品味著称：计算机语言不应该进行功能的堆砌，而应该尽可能减少弱点和限制，使剩下的功能显得必要。

Scheme的主要特征是Lisp的括号风格和卫生宏。

Scheme是一种动态强类型语言。

Scheme拥有众多的编译器和解释器。在本教程中用到的是Chez Scheme，由Kent Dybvig在1985年发布。它是Scheme最快的实现之一，并因其优良的特性成为了Dr Racket和Idris2的后端。

为什么学习Scheme？

1. 加深对JavaScript的理解。

JavaScript受到Scheme巨大的影响，以至于可以算是Scheme的方言。学习Scheme可以帮助你加深对JavaScript的理解，特别是回调函数的使用方式。

2. 习惯函数式编思维。

虽然Scheme属于多范式编程语言，但其最原生，最自然的方式是函数式编程。熟练使用Scheme能让你熟练地以函数式的风格思考。不同于Haskell，在你需要局部和全局变量的时候，你可以自由的使用它，只是要小心副作用。

3. 尝试不同风格的编程。

Lisp作为编程语言学习的终点，在学习Lisp之后，你不会再对新的编程语言充满好奇。有看尽千帆的胸有成竹。到那一天，你会有自己的Lisp编译器…


本文的目标读者为具有一定编程基础和经验的业内人士。


在学习中，如果需要更详尽的文档：

[Scheme编程语言 第四版](https://www.scheme.com/tspl4/)

[ChezScheme 9.5操作手册](https://cisco.github.io/ChezScheme/csug9.5/csug.html)

这里有不完全翻译的中文版

[Scheme编程语言 第四版](https://guenchi.github.io/TSPL/) [镜像](https://guenchi.gitlab.io/TSPL/)

[ChezScheme 9.5操作手册](https://guenchi.github.io/CSUG/)  [镜像](https://guenchi.gitlab.io/CSUG/)


*** 安装ChezScheme编译器 ***

* Windows

推荐使用WSL安装。这是最简单的使用方式。

* MacOS

```bash
$ brew install chezscheme
```


* FreeBSD

```bash
$ pkg install chez-scheme-9.5.6
```

* Linux

```bash
$ sudo apt-get install chezscheme
```

* 从源码编译：

[https://github.com/cisco/ChezScheme](https://github.com/cisco/ChezScheme)


安装结束后可以用

```bash
$ chezscheme
```
启动

```bash
Chez Scheme Version 9.5.2
Copyright 1984-2019 Cisco Systems, Inc.

> 
```

*** 这个`>`开头的程序提示符称为REPL，即Read-Eval-Print loop，"读取求值打印循环"，可是LISP的独创，由L. Peter Deutsch和Edmund Berkeley在1964年为DPD-1实现LISP实现创造。***

如今REPL已经成为程序运行时的标配，在之后的学习中你会慢慢发现，LISP和Scheme是怎样深刻影响程序设计语言发展的.

在本教程的一开始我们使用REPL来即时应用我们的程序，但是当程序扩展到一定规模，我们就需要使用编辑器来简化我们的编写流程。

这里推荐的是编辑器是VSCode，同时配合vscode-chez插件，它是由Scheme中文社区的[@chclock](https://github.com/chclock)开发的。

下面来输出我们的第一个Hello World:

Scheme提供了底层的输出输出流端口读取和写入,在这里我们只使用最简单的使用方式：

```scheme
> (display "Hello,World!")
```

*** 所有的Scheme语句都由小括号"("包裹")"，它表示以括号内的第一个元素为函数，剩下的元素为参数求值。 ***

这个简单的程序输出
```scheme
> (display "Hello,World!")
Hello,World!
> 
```
除了display, Scheme还提供了write来向标准输出流中输出：

```scheme
> (write "Hello,World!")
"Hello,World!"
> 
```

*** write输出的内容可以被Scheme程序再次从输出流中读取。而display则以更简洁的形式将内容打印到控制台窗口。 ***


