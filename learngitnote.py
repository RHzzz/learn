git note
git add ***.py ***.text
git commit -m "***"
git status

#日志
git log
git log --pretty=oneline
git reflog

#回退
git reset --hard head^

#修改
git checkout -- hello.py


#远程库
Quick setup — if you’ve done this kind of thing before
or	

SSH
git@github.com:RHzzz/learn.git
We recommend every repository include a README, LICENSE, and .gitignore.

…or create a new repository on the command line
echo "# learn" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:RHzzz/learn.git
git push -u origin master
…or push an existing repository from the command line
git remote add origin git@github.com:RHzzz/learn.git
git push -u origin master
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

Quick setup — if you’ve done this kind of thing before
or	
HTTPS

We recommend every repository include a README, LICENSE, and .gitignore.

…or create a new repository on the command line
echo "# learn" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/RHzzz/learn.git
git push -u origin master
…or push an existing repository from the command line
git remote add origin https://github.com/RHzzz/learn.git
git push -u origin master
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.