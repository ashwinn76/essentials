FROM althack/ros2:galactic-full

SHELL ["/bin/bash", "-c"]

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

RUN apt update && apt install -y build-essential clang-format-11 cmake cppcheck libcurl4-openssl-dev nlohmann-json3-dev python3-pip libfmt-dev
RUN pip install pytest-flake8

USER ros

RUN git config --global alias.url 'config --get remote.origin.url'
RUN git config --global alias.rbe "!f() { REMOTE_URL=\$(git url); REFS=\$'refs/heads/'; git ls-remote --heads \$REMOTE_URL \"\$REFS\$1\" | wc -l; }; f" #remote branch exists. returns 1 for true and 0 for false
RUN git config --global alias.cb  'symbolic-ref --short HEAD'  #current branch name
RUN git config --global alias.mg  "log --graph --abbrev-commit --format=format:'%C(cyan)%h%C(reset) - %C(yellow)%d%C(reset) %C(white)%s%C(reset) %C(green)<%an>%C(reset) %C(dim white)%aD%C(reset)' --all" #display the diff graph
RUN git config --global alias.cp  'cherry-pick'
RUN git config --global alias.cpc  '!git cp --continue'
RUN git config --global alias.cpa  '!git cp --abort'
RUN git config --global alias.cm  'commit -m' #commit with message eg: commit -m "Issue Fixed"
RUN git config --global alias.co  checkout
RUN git config --global alias.us  'reset HEAD' #unstage
RUN git config --global alias.dc  'checkout --' #discard
RUN git config --global alias.dca  '!git dc .' #discardall
RUN git config --global alias.filelog  'log -u'
RUN git config --global alias.mf  'fetch -p -t origin' #fetch from origin
RUN git config --global alias.new  '!git mf && git nb' #new branch after fetching origin
RUN git config --global alias.po  'push origin'
RUN git config --global alias.ms  '!git mf && git status && git mg' #This will fetch, show you the status and display the graph
RUN git config --global alias.rn  'branch -m' #rename branch
RUN git config --global alias.em  'commit --amend' #edit message
RUN git config --global alias.rs "!f() { i=\${1-1}; j=1; while [ "\$j" -le "\$i" ]; do git reset --soft HEAD^; j=\$(( j + 1 )); done }; f" #delete last N commits but keep all changes (1 by default)
RUN git config --global alias.rh "!f() { i=\${1-1}; j=1; while [ "\$j" -le "\$i" ]; do git reset --hard HEAD^; j=\$(( j + 1 )); done }; f" #delete last N commits and all changes (1 by default)
RUN git config --global alias.nb "!f() { MYBRANCH=origin/master; git checkout -b \$1 \${2-\$MYBRANCH}; }; f"  #new branch without fetching from remote
RUN git config --global alias.myfilediff "!f() { MYBRANCH=\$(git cb); git diff --name-only \$MYBRANCH \${1-origin/master}; }; f"
RUN git config --global alias.myfulldiff "!f() { MYBRANCH=\$(git cb); git diff \${1-origin/master} \$MYBRANCH; }; f"
RUN git config --global alias.ci "!f() { git show --pretty=fuller --name-status \$1; }; f" #commit info
RUN git config --global alias.sm "!f() { git log --all --oneline --grep=\$1; }; f" #searchmessage
RUN git config --global alias.mp "!f() { MYBRANCH=\$(git cb); git po \$MYBRANCH:\${1-\$MYBRANCH}; }; f"  #mypush. branch name will be current branch name
RUN git config --global alias.mpf "!f() { MYBRANCH=\$(git cb); git po -f \$MYBRANCH:\${1-\$MYBRANCH}; }; f"  #mypushforce
RUN git config --global alias.fb "!f() { git describe --contains \$1 | cut -d'~' -f1; }; f" #find build in which commit is included
RUN git config --global alias.fr 'rev-parse --abbrev-ref --symbolic-full-name @{u}' #find parent branch
RUN git config --global alias.mr "!f() { REMOTE=\$(git fr); git rebase \$REMOTE; }; f" #rebase
RUN git config --global alias.rc 'rebase --continue'
RUN git config --global alias.ra 'rebase --abort'
RUN git config --global alias.tc 'rev-list -n 1' #find commit on which this tag exists
RUN git config --global alias.lc "!f() { COMMENT=\${1-\"tmp\"}; git add *; git cm \"\$COMMENT\"; }; f" #lazycommit. It will stage everything and make a commit with default commit message "tmp"
RUN git config --global alias.lp "!f() { git lc \"\$1\"; BRANCH=\$(git cb); git mp \${2-\$BRANCH}; }; f"  #lazypush. It will do lazycommit and then push your branch to origin.
RUN git config --global alias.lpf "!f() { git lc \"\$1\"; BRANCH=\$(git cb); git mpf \${2-\$BRANCH}; }; f" #lazypushforce
RUN git config --global alias.cwl "!f() { MSG=\$(git log -1 --pretty=%B); git commit -m \"\$MSG\"; git em; }; f" #create a commit with same message as last commit and give option to edit commit message

