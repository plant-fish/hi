## 字体
```

*斜体* or _斜体_
**粗体**
***加粗斜体***
~~删除线~~
```

*斜体*

**粗体**

***加粗斜体***

~~删除线~~

## 分级标题

```
一级标题
====================
二级标题
-------------------
```

```
#一级标题
##二级标题
###三级标题
。
。
######六级标题
```

## 链接{#x}

### 行内式

[]里链接标题，（）链接地址，（）内的""可为链接指定title属性，title属性可加可不加，效果是鼠标悬停时会出现文字。链接地址与连接标题前有个空格。

```
 [garden](https://github.com/plant-fish/hi.git)
 
  [garden](https://github.com/plant-fish/hi.git "garden")
```

welcome [garden](https://github.com/plant-fish/)

 welcome [garden](https://github.com/plant-fish/ "garden")

### 参考式

```
我的仓库有[github][1],[gitee][2]等

[1]:https://github.com/plant-fish/hi.git
[2]:https://nobug
```

我的仓库有[github][1],[gitee][2]等

[1]:https://github.com/plant-fish/
[2]:https://nobug

### 自动链接

用<>包起来

```
<https://github.com/plant-fish/>
```

<https://github.com/plant-fish/>

## 锚点

* 只支持在标题后插入
* 在标题后{#标记}，然后在文档其他地方写上链接

```
链接{#x}

go to [链接](#x)
```

go to[链接](#x)

## 列表

### 无序列表

* 使用*，+，-,表示

```
- ok
- no
- yes
-后面有空格
```

- ok
- no
- yes
- 退出按enter

### 有序列表

数字+英文句号+空格

```
1. 欧克
2. 耶
3. 欧
```

1. 欧克
2. 耶
3. 欧

### 定义型列表

名词+解释

```
<dl>
<dt>Markdown</dt>
<dd>轻量级文本标记语言，可以转换成html，pdf等格式
（左侧有一个可见的冒号和四个不可见的空格）</dd>
<dt>代码块</dt>
<dd>这是代码块的定义（左侧有一个可见的冒号和四个不可见的空格）
        代码块（左侧有八个不可见的空格）</dd>
</dl>
```

<dl>
<dt>Markdown</dt>
<dd>轻量级文本标记语言，可以转换成html，pdf等格式
（左侧有一个可见的冒号和四个不可见的空格）</dd>
<dt>代码块</dt>
<dd>这是代码块的定义（左侧有一个可见的冒号和四个不可见的空格）
        代码块（左侧有八个不可见的空格）</dd>
</dl>

### 列表缩进

* ```
  *   This is the first list item.
  *   Here is the second list item.
  
      I need to add another paragraph below the second list item.
  
  *   And here is the third list item.
  ```

* 

* Vdi二段起i m find think you g r o l r

  di二段起i m find think you g r o ·

* hello，it is me ho are you g e i u  f o  w g u f s a j f k h d j f l s a f s d l f l s a d h f k s sd h j k a l f h j w e wo p q f u   f g j k l f g j a s l f g j s k l f g u e w p段落结束

  

  ### 包含引用的列表

  ```
  * abandon:
      > fist
      > two
  ```

  * abandon:

    > fist
    >
    > two

  ### 包含代码区块的引用

  缩进2次

  ```
  	1. <代码>
  ```

  	1. <#include studio>

  ### 特殊情况

  不小心产生项目列表时，即将数字认为列表序号，可在数字后面加

  ```
  1980\. for the great worth
  ```

  1980\. for the great worth

  ## 引用

  在被引用文本前加>符号

  ```
  > for the great worth
  > you do seem to realize that you will not talk me out of my plans for the object in question 
  ```

  > for the great worth
  > you do seem to realize that you will not talk me out of my plans for the object in question 

  

  也可只在整个段落的第一行加>

  ```
  > for the great worth
    you do seem to realize that you will not talk me out of my plans for the object in question 
  ```

  > for the great worth
  > you do seem to realize that you will not talk me out of my plans for the object in question 

  ### 引用的多层嵌套

  加上不同数量的>

  ```
  >>for which i am gad
  >>>it would be a shame to wear the wings off owls arguing over this for the reat of our lives
  ```

  >>for which i am gad
  >>
  >>>it would be a shame to wear the wings off owls arguing over this for the reat of our lives



###    引用其他要素

​    标题列表，代码区块等



## 插入图像

### 行内式

！【图片】（地址“备注”）

```
findone:
![something](https://helena666.lofter.com/post/309d1108_2b6bcda02"something")
```

findone:
![something](https://helena666.lofter.com/post/309d1108_2b6bcda02"something")



### 参考式

语法说明：

在文档要插入图片的地方写![图片Alt][标记]

在文档的最后写上[标记]:图片地址 “Title”

```
findone:
![something][hhhh]

[hhhh]:(https://helena666.lofter.com/post/309d1108_2b6bcda02"something")
```

findone:
![something][hhhh]

[hhhh]:(https://helena666.lofter.com/post/309d1108_2b6bcda02"something")

## 目录

在段落中【TOC】



 
