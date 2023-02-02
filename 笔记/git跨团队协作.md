## 跨团队协作

![1](https://gitee.com/plant-fish/garden/raw/master/git%202.1.png)

<img src="E:\训练营内容\git2.2.png" alt="2" style="zoom: 50%;" /

![2](https://gitee.com/plant-fish/garden/raw/master/git2.2.png)

![3](https://gitee.com/plant-fish/garden/raw/master/git2.3.png)

之后可以clone,修改/在线编辑

* ![4](https://gitee.com/plant-fish/garden/raw/master/git2.4.png)

修改后pull request发送拉取请求~~P25未来可以研究~~

* ![5](https://gitee.com/plant-fish/garden/raw/master/git2.5.png)

在个人页面可以查看别人发来的请求

## SSH免密登录

push时不用登录

1. 看到·一个警告

   ![3.1](https://gitee.com/plant-fish/garden/raw/master/git3.1.png)

2. c->window->用户->25634~~(用户名）~~->.ssh

   [^.ssh不存在，要自己生成，（未使用过电脑），否则要先删了]: 

   ![3.2](https://gitee.com/plant-fish/garden/raw/master/git3.2.png)

3. 在这里打开git

   ![3.3](https://gitee.com/plant-fish/garden/raw/master/git3.3.png)

4. 生成.ssh

   * 使用：ssh-keygen -t -C 邮箱

     ```
     ssh-keygen -t rsa -C git@github.com:plant-fish/hi.git
     （生成公/私钥  运用哪种加密算法 著名加密算法 描述 邮箱）
     ```

     敲3次enter

     ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 ~
     $ ssh-keygen -t rsa -C git@github.com:plant-fish/hi.git
     Generating public/private rsa key pair.
     Enter file in which to save the key (/c/Users/25634/.ssh/id_rsa):
     Created directory '/c/Users/25634/.ssh'.
     Enter passphrase (empty for no passphrase):
     Enter same passphrase again:
     Your identification has been saved in /c/Users/25634/.ssh/id_rsa
     Your public key has been saved in /c/Users/25634/.ssh/id_rsa.pub
     The key fingerprint is:
     SHA256:C/yhSA7BAgBZd4g9sDt9QmasUvGJEOu1TiAtDnuIkOg git@github.com:plant-fish/hi.git
     The key's randomart image is:
     +---[RSA 3072]----+
     |O+++...          |
     |+*.B+o           |
     |X.B.B.           |
     |O*oO..           |
     |=E*o+ + S        |
     | oo= + + o       |
     |   .o . o        |
     |                 |
     |                 |
     +----[SHA256]-----+
     ```

   * 出现.ssh

   * pub是公钥，另一个是私钥

     ![3.4](https://gitee.com/plant-fish/garden/raw/master/git3.4.png)

   * ```
     25634@▒▒▒▒▒▒▒▒ MINGW64 ~
     $ cd .ssh/
     
     25634@▒▒▒▒▒▒▒▒ MINGW64 ~/.ssh
     $ ll
     total 5
     -rw-r--r-- 1 25634 197609 2622 Feb  1 11:55 id_rsa
     -rw-r--r-- 1 25634 197609  586 Feb  1 11:55 id_rsa.pub
     
     25634@▒▒▒▒▒▒▒▒ MINGW64 ~/.ssh
     $ cat id_rsa.pub
     ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDcE44Za2Lb6E74W2buzDvkYwQdcmkiuX5/clCxnTjIhBvNmoxdawE/jf6UvSJ46TmlIkIseTZ/Sw1o42cbxRMd4TLY2NykFni79KESAmRQPw6LxixoxbDfmkLL+9lKkSjduj79nm6yLnrTmkec8aztuTEiUba4gTROg5da+2DKV826Y87UVSKPnU1IFAxdTRCObzz8jb7Zbah5J06HXzvT32YYewy1WYjETfcq+0BrUy6NET/Rr8AenYD4pzoFfsF2gcDntjGxBvQYDLcx7ilLW+Vo4mXUgKx61xISvAZa187+CQBvM2hhTnnn6F5lKbTNpSEDyiBLvMSf7CtXf4DvVuhVGmvz8AEEJ4YzgxPS3hXFbBoKnsTltFN/yVyOCEYKXIrDo5JJ8Cz3IiBAgp0YKAd3qHsJHYa2+lS06AourAdaXembz0QQQmEYJdh+KUz0yscnXViaVMnG5z6aEpMO3Yt6h68D0YJN9wpkhh+1p0aXLILlQTLY2EQGzTCYojM= git@github.com:plant-fish/hi.git
     
     ```

   * 将

     ```
     ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDcE44Za2Lb6E74W2buzDvkYwQdcmkiuX5/clCxnTjIhBvNmoxdawE/jf6UvSJ46TmlIkIseTZ/Sw1o42cbxRMd4TLY2NykFni79KESAmRQPw6LxixoxbDfmkLL+9lKkSjduj79nm6yLnrTmkec8aztuTEiUba4gTROg5da+2DKV826Y87UVSKPnU1IFAxdTRCObzz8jb7Zbah5J06HXzvT32YYewy1WYjETfcq+0BrUy6NET/Rr8AenYD4pzoFfsF2gcDntjGxBvQYDLcx7ilLW+Vo4mXUgKx61xISvAZa187+CQBvM2hhTnnn6F5lKbTNpSEDyiBLvMSf7CtXf4DvVuhVGmvz8AEEJ4YzgxPS3hXFbBoKnsTltFN/yVyOCEYKXIrDo5JJ8Cz3IiBAgp0YKAd3qHsJHYa2+lS06AourAdaXembz0QQQmEYJdh+KUz0yscnXViaVMnG5z6aEpMO3Yt6h68D0YJN9wpkhh+1p0aXLILlQTLY2EQGzTCYojM= git@github.com:plant-fish/hi.git
     ```

     复制贴到

     ![3.5](https://gitee.com/plant-fish/garden/raw/master/git3.5.png)

     ![3.6](https://gitee.com/plant-fish/garden/raw/master/git3.6.png)

     ![3.7](https://gitee.com/plant-fish/garden/raw/master/git3.7.png)

     ![git3.8](https://gitee.com/plant-fish/garden/raw/master/git3.8.png)

     ![git3.9](https://gitee.com/plant-fish/garden/raw/master/git3.9.png)
     
     ```
     
     25634@▒▒▒▒▒▒▒▒ MINGW64 /e/git-space/git-demo2
     $ git clone git@github.com:plant-fish/hi.git
     Cloning into 'hi'...
     The authenticity of host 'github.com (20.205.243.166)' can't be established.
     ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
     This key is not known by any other names.
     Are you sure you want to continue connecting (yes/no/[fingerprint])? yes（第一次出现，回答yes）
     Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
     remote: Enumerating objects: 25, done.
     remote: Counting objects: 100% (25/25), done.
     remote: Compressing objects: 100% (20/20), done.
     remote: Total 25 (delta 3), reused 21 (delta 2), pack-reused 0
     Receiving objects: 100% (25/25), 13.38 KiB | 3.34 MiB/s, done.
     Resolving deltas: 100% (3/3), done.
     
     ```
     
     

## IDEA集成git

### 忽略规则文件

* 规则文件与项目实际功能无关，不参与服务器上的部署运行，把它们忽略能屏蔽IDEA工具间的差异

1. 创建忽略规则文件git.ignore(为了便于~/.gitconfig文件引用，建议放在用户目录下)

2. 什么文件不要就写*.文件类型

   模板：

   ```
   # Compiled class file
   *.class
   
   # Log file
   *.log
   
   # BlueJ files
   *.ctxt
   
   # Mobile Tools for Java (J2ME)
   .mtj.tmp/# Package Files #
   *.jar
   *.war
   *.nar
   *.ear
   *.zip
   *.tar.gz
   *.rar
   
   hs_err_pid*
   
   .classpath
   .project
   .settings
   target
   .idea
   *.iml
   ```

   ![4.1](https://gitee.com/plant-fish/garden/raw/master/git4.1.png)

   打开git.config

   ![git4.2](https://gitee.com/plant-fish/garden/raw/master/git4.2.png)

   补充![git4.3](https://gitee.com/plant-fish/garden/raw/master/git4.3.png)

   P27不在继续

