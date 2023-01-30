# git概述

分布式版本控制工具

* 集中式版本控制：

中央服务器，存在单点故障

* 分布式版本控制：

断网情况下也能进行开发，每个客户端保存整个项目（包含历史记录）

* 工作机制：工作区：写代码的地方：代码在磁盘存放的位置

  ​                  git add(将工作区代码添加到暂存区)

  ​                     暂存区：临时存储（可删）

  ​                  git commit（将暂存区代码提交到本地库）

  ​                  本地库：（生成历史版本，删不掉）

* git和代码托管中心（远程库）

* 1. 局域网

  gitlab

  2. 互联网

  GitHub(国外)

  Gitee（国内）

# git常用命令

| 命令名称                             | 作用           |
| ------------------------------------ | -------------- |
| git config --global user.name 用户名 | 设置用户签名   |
| git config --global user.email 邮箱  | 设置用户签名   |
| git init                             | 初始化本地库   |
| git status                           | 查看本地库状态 |
| git add 文件名                       | 添加到暂存区   |
| git commit -m "日志信息" 文件名      | 提交到本地库   |
| git reflog                           | 查看历史记录   |
| git reset --hard 版本号              | 版本穿梭       |

### 设置用户签名

1. 基本语法

git config --global user.name 用户名  

git config --global user.email 邮箱

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /d/桌面
$ git config --global user.name zoey

25634@▒▒▒▒▒▒▒▒ MINGW64 /d/桌面
$ git config --global user.email zoey@git.com

```

```
查看user
磁盘：window/OS/用户/25634（即@号前面的名称）/.gitconfig/
右键edit with notepad++(记事本)(打开)

```

```
[user]
	name = zoey
	email = zoey@git.com

```

设置用户签名与将来登录GitHub无任何关系

首次安装必须设置一下，否则无法提交代码

### 初始化本地库

1. 基本语法

git init

2. 在文件夹中打开（新建git-demo)

```

25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo
$ git init
Initialized empty Git repository in E:/git-space/git-demo/.git/


```

```
有一个空的git 库在。。。此时会在git-demo内生成一个.git文件（默认隐藏，显示：查看->显示->隐藏的项目
```

### 查看本地库状态

1. 基本语法

git status

```git
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git status
On branch master

No commits yet ~~(没有提交过东西and没有东西需要提交)~~

nothing to commit (create/copy files and use "git add" to track)

```

将文件复制到git-demo内

```git
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ ll(查看目录的文件)
total 8
-rw-r--r-- 1 25634 197609 5072 Jan 29 16:55 markdown语法笔记1.md

25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ cat markdown语法笔记1.md（查看文件的内容）

```

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ tail -n 1 markdown语法笔记1.md（查看末尾第一行的内容）

```

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        "markdown\350\257\255\346\263\225\347\254\224\350\256\2601.md"
（未被追踪的文件）：
文件还在工作区内，没有add到暂存区
nothing added to commit but untracked files present (use "git add" to track)

```

### 添加到暂存区

1. 基本语法

git add

2. ```
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
   $ git add markdown语法笔记1.md
   
   ```

   有时候：

   ```
   warning:LF will be replaced by CRLF in hello.txt.
   （文件中的换行符被替换（一般不用管））
   ```

   再次git status

   ```
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
   $ git status
   On branch master
   
   No commits yet
   
   Changes to be committed:
     (use "git rm --cached <file>..." to unstage)
           new file:   "markdown\350\257\255\346\263\225\347\254\224\350\256\2601.md"
   （如果想要删除，则使用git rm --cached <file>..."）
   
   ```

   * 删除：

   ```
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
   $ git rm --cached markdown语法笔记1.md
   rm 'markdown语法笔记1.md'
   （rm:删除（暂存区文件））
   ```

   

### 提交本地库

1. 基本语法：

git commit -m"日志信息" 文件名(-m:提交日志信息)

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git commit -m"markdown语法1" markdown语法笔记1.md
[master (root-commit) 92996ec] markdown语法1（分支添加，（92996ec为版本号）
 1 file changed, 286 insertions(+)（一个文件被改变，16行内容被插入）
 create mode 100644 "markdown\350\257\255\346\263\225\347\254\224\350\256\2601.md"


```

再次查看本地库

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git status
On branch master
nothing to commit, working tree clean

```

查看引用日志信息：git reflog

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git reflog
92996ec (HEAD -> master) HEAD@{0}: commit (initial): markdown语法1

```

查看详细日志：git log

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git log
commit 92996ece1a2e11e6d6afeb87aa5556a472325c02 (HEAD -> master)（完整版版本号）
Author: zoey <zoey@git.com>
Date:   Sun Jan 29 22:07:12 2023 +0800

    markdown语法1


```

### 修改文件

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ vim markdown语法笔记1.md
（修改文件）
```

```
修改后按ese退出，按shift：，输入wq
（ese:退出编辑模式）
（：:退出底线模式）
（w:保存）
（q:退出）
（wq:保存并退出)
```

再次查看本地库:

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   "markdown\350\257\255\346\263\225\347\254\224\350\256\2601.md"
（文件被修改了，没有add)
no changes added to commit (use "git add" and/or "git commit -a")


```

add+commit:

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git add markdown语法笔记1.md

25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   "markdown\350\257\255\346\263\225\347\254\224\350\256\2601.md"


25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git commit -m"markdown语法1" markdown语法笔记1.md
[master 30a3fe5] markdown语法1
 1 file changed, 4 insertions(+), 2 deletions(-)


```

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git reflog
30a3fe5 (HEAD -> master) HEAD@{0}: commit: markdown语法1（指针指向第二个版本）
92996ec HEAD@{1}: commit (initial): markdown语法1

25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ cat markdown语法笔记1.md（查看.md)
​```

```

> ctrl+l清屏

### 版本穿梭

* 查看历史版本

1. 基本语法

git reflog 查看版本信息

git log 查看版本详细信息

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git reflog
30a3fe5 (HEAD -> master) HEAD@{0}: commit: markdown语法1
92996ec HEAD@{1}: commit (initial): markdown语法1

25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git log
commit 30a3fe54f7b2aed3b3fb2ec51fb048a31d054473 (HEAD -> master)
Author: zoey <zoey@git.com>
Date:   Sun Jan 29 22:29:35 2023 +0800

    markdown语法1

commit 92996ece1a2e11e6d6afeb87aa5556a472325c02
Author: zoey <zoey@git.com>
Date:   Sun Jan 29 22:07:12 2023 +0800

    markdown语法1

```



* 版本穿梭

1. 基本语法

git reset --hard 版本号

2. ```
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
   $ git reset --hard 30a3fe5
   HEAD is now at 30a3fe5 markdown语法1
   
   ```

3. status(修改2次之后)

```
25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
$ git reflog
92996ec (HEAD -> master) HEAD@{0}: reset: moving to 92996ec（穿越到
30a3fe5 HEAD@{1}: reset: moving to 30a3fe5（穿越到
30a3fe5 HEAD@{2}: commit: markdown语法1
92996ec (HEAD -> master) HEAD@{3}: commit (initial): markdown语法1


```

4. 在.git中的HEAD右键打开（记事本）能看到在master的分支上

   ```
   ref: refs/heads/master
   ```

   在.git中refs->heads->master右键打开查看版本号

![文件夹显示](https://gitee.com/plant-fish/garden/raw/master/git.png)

5. head->master->版本号指向的版本，版本穿梭改动master指向的版本号

### git分支操作

* 关于分支的概述（P15）日后可以了解

| 命令名称            | 作用                       |
| ------------------- | -------------------------- |
| git branch 分支名   | 创建分支                   |
| git branch -v       | 查看分支                   |
| git checkout 分支名 | 切换分支                   |
| git merge 分支名    | 把指定分支合并到当前分支上 |

* 查看分支

1. 基本语法

 git branch -v

2. ```
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
   $ git branch -v
   * master 92996ec markdown语法1
   
   ```

* 创建分支

  1. 基本语法

  git branch 分支名

  2. ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git branch try
     
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git branch -v
     * master 92996ec markdown语法1
       try    92996ec markdown语法1
     
     ```

* 切换分支

  1. 基本语法

     git checkout 文件名

  2. ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git checkout try
     Switched to branch 'try'
     
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (try)（已切换到try分支）
     $
     
     ```

     查看：

  3. ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (try)
     $ git branch -v
       master 92996ec markdown语法1
     * try    92996ec markdown语法1
     (*号指向当前分支)
     
     ```

  4. 此时可以cat ->add->commit修改版本在try分支上

     切换分支相当于head->master改为head->try

     磁盘中.git/master打开后最后的master改变

     refs的版本号也改变

### 合并分支

* **想把try分支合并到master分支上，则需要在master分支上进行操作**（master被修改，try内容不变

1. 基本语法

   git merge 要合并的分支名

2. ```
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
   $ git merge try
   Already up to date.
   
   ```

3. 代码冲突问题：两个分支在同一个文件同一个位置有2个不同的修改（没有手动实操过）

   （后续可补

   ```
   CONFLICT (content):Merge conflict in hello.txt
   （。冲突：在hello.txt内有冲突）
   Automatic merge failed:fix conflicts and then commit the result
   （自动合并失败
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master/MERGING)（正在合并中，说明没有合并成功）
   
   ```

   此时要手动打开文件，即vim hello.txt

   ```
   不同的位置显示如下：
   <<<<<HEAD
   .................（代码内容）
   =========
   ...................（代码内容）
   >>>>>>>try（分支）
   
   ```

   修改时要将< = > 号删去

   之后w q保存

   添加暂存区git add 文件名

   提交本地库git commit -m ""**不带文件名**

   之后能发现MERGING消失，变为正常

4. 合并本质也是改变head->master的指针

## 团队协作

### 团队协作机制

* 团队内协作

  1. 本地库~~push~~(推送到代码托管中心)push需要权限

  2. 代码托管中心~~clone~~(复制到自己的本地库)

  3. ~~pull~~（拉取到自己的本地库）

* 跨团队协作

  1. 远程库1~~fork~~远程库2

  2. 远程库2~~clone~~合作方的本地库

  3. 合作方本地库~~push~~远程库2

  4. 远程库2~~pull request~~（拉去申请）--->远程库1审核----->~~merge~~合并修改—>pull到自己的本地库

  

## GitHub

* 网址：https://github.com/

### 远程仓库操作

| 命令名称                           | 作用                                                     |
| ---------------------------------- | -------------------------------------------------------- |
| git remote                         | 查看当前所有远程地址别名                                 |
| git remote add 别名 远程地址       | 起别名                                                   |
| git push 别名 分支                 | 推送本地分支上的内容到远程仓库                           |
| git clone 远程地址                 | 将远程仓库的内容克隆到本地                               |
| git pull 远程库地址别名 远程分支名 | 将远程仓库对于分支最新内容拉下来后于当前本地分支直接合并 |

1. 创建远程仓库别名

   * 基本语法

     git remote -v 查看当前所有远程地址别名

     git remote add 别名 远程地址

   * ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git remote -v
     
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git remote add hi https://github.com/plant-fish/hi.git
     
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git remote -v
     hi      https://github.com/plant-fish/hi.git (fetch)
     hi      https://github.com/plant-fish/hi.git (push)
     
     ```

2. 推送本地分支到远程库

   * 基本语法

     git push 别名 分支*如果没有设置别名，可以直接输入地址，当还是要接分支名*

   * ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git push helloworld master
   Enumerating objects: 3, done.
     Counting objects: 100% (3/3), done.
     Delta compression using up to 16 threads
     Compressing objects: 100% (3/3), done.
     Writing objects: 100% (3/3), 2.01 KiB | 2.01 MiB/s, done.
     Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
     remote:
     remote: Create a pull request for 'master' on GitHub by visiting:
     remote:      https://github.com/plant-fish/helloworld/pull/new/master
     remote:
     To https://github.com/plant-fish/helloworld.git
      * [new branch]      master -> master
     
     ```
     
     <img src="E:\训练营内容\git1提交修改.png" alt="git1提交修改" style="zoom:33%;" />![git1编辑上传代码](E:\训练营内容\git1编辑上传代码.png)
     

3. 拉取远程库到本地库

   * 基本语法：

     git pull 别名 分支名

   * ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git pull helloworld master
     remote: Enumerating objects: 5, done.
     remote: Counting objects: 100% (5/5), done.
     remote: Compressing objects: 100% (3/3), done.
     remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
     Unpacking objects: 100% (3/3), 701 bytes | 58.00 KiB/s, done.
     From https://github.com/plant-fish/helloworld
      * branch            master     -> FETCH_HEAD
        92996ec..39b936b  master     -> helloworld/master
     Updating 92996ec..39b936b
     Fast-forward
      "markdown\350\257\255\346\263\225\347\254\224\350\256\2601.md" | 3 ++-
      1 file changed, 2 insertions(+), 1 deletion(-)
     
     ```

   * ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ git status
     On branch master
     nothing to commit, working tree clean
     （自动拉到本地库）
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo (master)
     $ cat markdown语法笔记1.md
     
     ```

​     - **用不同的身份登录要在window/控制面板/用户账户/凭据管理器  window凭据-》普通凭据**<img src="E:\训练营内容\git1凭据管理器.png" alt="git1凭据管理器" style="zoom: 33%;" />



4. 克隆远程库到本地库

   * 基本语法：git clone 地址

   * ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo2
     $ git clone https://github.com/plant-fish/hi.git
     Cloning into 'hi'...
     remote: Enumerating objects: 17, done.
     remote: Counting objects: 100% (17/17), done.
     remote: Compressing objects: 100% (14/14), done.
     remote: Total 17 (delta 0), reused 14 (delta 0), pack-reused 0
     Receiving objects: 100% (17/17), 6.01 KiB | 6.01 MiB/s, done.
     
     ```

   * 查看别名发现

     ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo2
     $ git status
     fatal: not a git repository (or any of the parent directories): .git
     
     ```

     

   * 进入文件：cd

   ```
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo2
   $ cd hi
   
   25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo2/hi (main)
   $
   
   ```

   * 查看别名

     ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo2/hi (main)
     $ git remote -v
     origin  https://github.com/plant-fish/hi.git (fetch)
     origin  https://github.com/plant-fish/hi.git (push)
     （已建好别名）
     ```

     







