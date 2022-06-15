git config --global alias.url 'config --get remote.origin.url'
git config --global alias.rbe "!f() { REMOTE_URL=\$(git url); REFS=\$'refs/heads/'; git ls-remote --heads \$REMOTE_URL \"\$REFS\$1\" | wc -l; }; f" #remote branch exists. returns 1 for true and 0 for false
git config --global alias.cb  'symbolic-ref --short HEAD'  #current branch name
git config --global alias.mg  "log --graph --abbrev-commit --format=format:'%C(cyan)%h%C(reset) - %C(yellow)%d%C(reset) %C(white)%s%C(reset) %C(green)<%an>%C(reset) %C(dim white)%aD%C(reset)' --all" #display the diff graph
git config --global alias.cp  'cherry-pick'
git config --global alias.cpc  '!git cp --continue'
git config --global alias.cpa  '!git cp --abort'
git config --global alias.cm  'commit -m' #commit with message eg: commit -m "Issue Fixed"
git config --global alias.co  checkout
git config --global alias.us  'reset HEAD' #unstage
git config --global alias.dc  'checkout --' #discard
git config --global alias.dca  '!git dc .' #discardall
git config --global alias.filelog  'log -u'
git config --global alias.mf  'fetch -p -t origin' #fetch from origin
git config --global alias.new  '!git mf && git nb' #new branch after fetching origin
git config --global alias.po  'push origin'
git config --global alias.ms  '!git mf && git status && git mg' #This will fetch, show you the status and display the graph
git config --global alias.rn  'branch -m' #rename branch
git config --global alias.em  'commit --amend' #edit message
git config --global alias.rs "!f() { i=\${1-1}; j=1; while [ "\$j" -le "\$i" ]; do git reset --soft HEAD^; j=\$(( j + 1 )); done }; f" #delete last N commits but keep all changes (1 by default)
git config --global alias.rh "!f() { i=\${1-1}; j=1; while [ "\$j" -le "\$i" ]; do git reset --hard HEAD^; j=\$(( j + 1 )); done }; f" #delete last N commits and all changes (1 by default)
git config --global alias.nb "!f() { MYBRANCH=origin/master; git checkout -b \$1 \${2-\$MYBRANCH}; }; f"  #new branch without fetching from remote
git config --global alias.myfilediff "!f() { MYBRANCH=\$(git cb); git diff --name-only \$MYBRANCH \${1-origin/master}; }; f"
git config --global alias.myfulldiff "!f() { MYBRANCH=\$(git cb); git diff \${1-origin/master} \$MYBRANCH; }; f"
git config --global alias.ci "!f() { git show --pretty=fuller --name-status \$1; }; f" #commit info
git config --global alias.sm "!f() { git log --all --oneline --grep=\$1; }; f" #searchmessage
git config --global alias.mp "!f() { MYBRANCH=\$(git cb); git po \$MYBRANCH:\${1-\$MYBRANCH}; }; f"  #mypush. branch name will be current branch name
git config --global alias.mpf "!f() { MYBRANCH=\$(git cb); git po -f \$MYBRANCH:\${1-\$MYBRANCH}; }; f"  #mypushforce
git config --global alias.fb "!f() { git describe --contains \$1 | cut -d'~' -f1; }; f" #find build in which commit is included
git config --global alias.fr 'rev-parse --abbrev-ref --symbolic-full-name @{u}' #find parent branch
git config --global alias.mr "!f() { REMOTE=\$(git fr); git rebase \$REMOTE; }; f" #rebase
git config --global alias.rc 'rebase --continue'
git config --global alias.ra 'rebase --abort'
git config --global alias.tc 'rev-list -n 1' #find commit on which this tag exists
git config --global alias.lc "!f() { COMMENT=\${1-\"tmp\"}; git add *; git cm \"\$COMMENT\"; }; f" #lazycommit. It will stage everything and make a commit with default commit message "tmp"
git config --global alias.lp "!f() { git lc \"\$1\"; BRANCH=\$(git cb); git mp \${2-\$BRANCH}; }; f"  #lazypush. It will do lazycommit and then push your branch to origin.
git config --global alias.lpf "!f() { git lc \"\$1\"; BRANCH=\$(git cb); git mpf \${2-\$BRANCH}; }; f" #lazypushforce
git config --global alias.cwl "!f() { MSG=\$(git log -1 --pretty=%B); git commit -m \"\$MSG\"; git em; }; f" #create a commit with same message as last commit and give option to edit commit message



# C++ requirements
sudo apt update

sudo apt install -y build-essential

sudo apt install -y clang-format-11

sudo apt install -y cmake

sudo apt install -y cppcheck

sudo apt install -y libcurl4-openssl-dev

sudo apt install -y nlohmann-json3-dev



# Python requirements
sudo apt install -y python3-pip

pip3 install pytest-flake8
