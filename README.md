# skill_tree_scheme

`Scheme技能树`是[技能森林](https://gitcode.net/csdn/skill_tree)的一部分。

## 编辑环境初始化

```
pip install -r requirements.txt
```

## 目录结构说明
技能树编辑仓库的 data 目录是主要的编辑目录，目录的结构是固定的

* 技能树`骨架文件`：
    * 位置：`data/tree.json`
    * 说明：该文件是执行 `python main.py` 生成的，请勿人工编辑
* 技能树`根节点`配置文件：
    * 位置：`data/config.json`
    * 说明：可编辑配置关键词等字段，其中 `node_id` 字段是生成的，请勿编辑
* 技能树`难度节点`：
    * 位置：`data/xxx`，例如: `data/1.Scheme初阶`
    * 说明：
        * 每个技能树有 3 个等级，目录前的序号是必要的，用来保持文件夹目录的顺序
        * 每个目录下有一个 `config.json` 可配置关键词信息，其中 `node_id` 字段是生成的，请勿编辑
* 技能树`章节点`：
    * 位置：`data/xxx/xxx`，例如：`data/1.Scheme初阶/1.Scheme简介`
    * 说明：
        * 每个技能树的每个难度等级有 n 个章节，目录前的序号是必要的，用来保持文件夹目录的顺序
        * 每个目录下有一个 `config.json` 可配置关键词信息，其中 `node_id` 字段是生成的，请勿编辑
* 技能树`知识节点`：
    * 位置：`data/xxx/xxx`，例如：`data/1.Scheme初阶/1.Scheme简介`
    * 说明：
        * 每个技能树的每章有 n 个知识节点，目录前的序号是必要的，用来保持文件夹目录的顺序
        * 每个目录下有一个 `config.json`
            * 其中 `node_id` 字段是生成的，请勿编辑
            * 其中 `keywords` 可配置关键字字段
            * 其中 `children` 可配置该`知识节点`下的子树结构信息，参考后面描述
            * 其中 `export` 可配置该`知识节点`下的导出习题信息，参考后面描述

## `知识节点` 子树信息结构

例如 `data/1.Scheme初阶/1.Scheme简介/1.HelloWorld/config.json` 里配置对该知识节点子树信息结构，这个配置是可选的：
```json
{
    // ...

    "children": [
    {
        "XX开发入门": {
          "keywords": [
            "XX开发",
          ],
          "children": [],
          "keywords_must": [
            "XX"
          ],
          "keywords_forbid": []
        }
    }
  ],
}
```

## `知识节点` 的导出习题编辑

例如 `data/1.Scheme初阶/1.Scheme简介/1.HelloWorld/config.json` 里配置对该知识节点导出的习题

```json
{
    // ...
    "export": [
        "helloworld.json"
    ]
}
```

helloworld.json 的格式如下：
```bash
{
  "type": "code_options",
  "author": "xxx",
  "source": "helloworld.md",
  "notebook_enable": false,
  "exercise_id": "xxx"
}
```

其中 
* "type": "code_options" 表示是一个选择题
* "author" 可以放作者的 CSDN id，
* "source" 指向了习题 MarkDown文件
* "notebook_enable" 目前都是false
* "exercise_id" 是工具生成的，不填


习题格式模版如下：

````mardown
# {标题}

{习题描述}

以下关于上述游戏代码说法[正确/错误]的是？

## 答案

{目标选项}

## 选项

### A

{混淆选项1}

### B

{混淆选项2}

### C

{混淆选项3}

````

## 技能树合成

在根目录下执行 `python main.py` 会合成技能树文件，合成的技能树文件: `data/tree.json`
* 合成过程中，会自动检查每个目录下 `config.json` 里的 `node_id` 是否存在，不存在则生成
* 合成过程中，会自动检查每个知识点目录下 `config.json` 里的 `export` 里导出的习题配置，检查是否存在`exercise_id` 字段，如果不存在则生成
* 在 节 目录下根据需要，可以添加一些子目录用来测试代码。
* 开始技能树构建之旅，GoodLuck! 

## FAQ

**难度目录是固定的么？**

1. data/xxx 目录下的子目录是固定的初/中/高三个难度等级目录

**如何增加章目录？**

1. 在VSCode里打开项目仓库
2. 在对应的难度等级目录新建章目录，例如在 data/1.xxx初阶/ 下新建章文件夹，data/1.xxx初阶/1.yyy
3. 在项目根目录下执行 python main.py 脚本，会自动生成章的配置文件 data/1.xxx初阶/1.yyy/config.json

**如何增加节目录?**:
1. 直接在VSCode里创建文件夹，例如 "data/1.xxx初阶/1.yyy/2.zzz"
2. 项目根目录下执行 python main.py 会自动为新增节创建配置文件 data/1.xxx初阶/1.yyy/2.zzz/config.json

**如何在节下新增一个习题**:
1. 在"data/1.xxx初阶/1.yyy/2.zzz" 目录下添加一个 markdown 文件编辑，例如 yyy.md，按照习题markdown格式编辑习题。
2. md编辑完后，可以再次执行  python main.py 会自动生成同名的 yyy.json，并将 yyy.json 添加到config.json 的export数组里。
3. yyy.json里的author信息放作者 CSDN ID。