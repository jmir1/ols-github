# ols-github
use [moritzgloeckl/overleaf-sync](https://github.com/moritzgloeckl/overleaf-sync) to sync you overleaf projects to github, without a premium subscription  
  
i'll explain a possible way to use this here:
## prerequisites
1. clone this repo with ``git clone https://github.com/jmir1/ols-github.git`` and move into it with ``cd ols-github``
2. proper ssh authentication for your github account so you dont have to enter your password every time you push (technically only necessary for automated execution)
3. make a private (or public if you want all your projects to be public lol) repo and clone it with something like ``git clone git@github.com:user/project-repo.git``
5. install ols (``pip3 install overleaf-sync``/``pip install overleaf-sync``)
6. use ols to login to your account with ``cd project-repo && ols login``
7. replace USERNAME and PASSWORD in ``run.py`` to your login info for overleaf.com
## usage
- ``cd project-repo && python3 run.py`` this will first sync with the git repo, then sync ALL your projects on overleaf and then commit and push to your repo (if anything changed)
- you can also make a cron job like ``*/15 * * * * cd /path/to/project-repo && /pythonpath/python3 /path/to/run.py`` to sync your projects every 15 minutes! you will want ssh authentication, otherwise it will not work and probably break something, idk
## PROBLEMS:
- if you have projects with the same name, only one or none will be synchronized (idk, it's best you rename them anyway, right?)
- if you rename a project, the one with the old name won't be deleted from your local folder or the git repo, you'll have to do that yourself
## DISCLAIMER:
if something goes wrong, this might change files unpredictably in your overleaf project
