import os
import sys

current_dir = os.path.dirname(__file__)

arch = ""
with os.popen("dpkg --print-architecture") as f:
    arch = f.readline()

arch = arch.rstrip()

assert (len(sys.argv) > 2)

user_name = sys.argv[1]
user_email = sys.argv[2]

with open(os.path.join(current_dir, "Dockerfile"), "w+") as docker_file:
    if arch == "arm64":
        docker_file.write("FROM arm64v8/ubuntu:20.04\n\n")
    docker_file.writelines(["SHELL [\"/bin/bash\", \"-c\"]\n",
                           "\n",
                            "ARG DEBIAN_FRONTEND=noninteractive\n",
                            "ENV TZ=America/New_York\n",
                            "\n",
                            "RUN apt update && apt install -y build-essential clang-format cmake cppcheck libcurl4-openssl-dev nlohmann-json3-dev python3-pip libfmt-dev libgtest-dev git g++-10\n",
                            "RUN pip install -U pytest-flake8 autopep8\n",
                            "RUN  echo \"    IdentityFile ~/.ssh/id_rsa\" >> /etc/ssh/ssh_config\n",
                            "\n",
                            "RUN git config --global alias.url 'config --get remote.origin.url'\n",
                            "RUN git config --global alias.rbe \"!f() { REMOTE_URL=\$(git url); REFS=\$'refs/heads/'; git ls-remote --heads \$REMOTE_URL \"\$REFS\$1\" | wc -l; }; f\" #remote branch exists. returns 1 for true and 0 for false\n",
                            "RUN git config --global alias.cb  'symbolic-ref --short HEAD'  #current branch name\n",
                            "RUN git config --global alias.mg  \"log --graph --abbrev-commit --format=format:'%C(cyan)%h%C(reset) - %C(yellow)%d%C(reset) %C(white)%s%C(reset) %C(green)<%an>%C(reset) %C(dim white)%aD%C(reset)' --all\" #display the diff graph\n",
                            "RUN git config --global alias.cp  'cherry-pick'\n",
                            "RUN git config --global alias.cpc  '!git cp --continue'\n",
                            "RUN git config --global alias.cpa  '!git cp --abort'\n",
                            "RUN git config --global alias.cm  'commit -m' #commit with message eg: commit -m \"Issue Fixed\"\n",
                            "RUN git config --global alias.co  checkout\n",
                            "RUN git config --global alias.us  'reset HEAD' #unstage\n",
                            "RUN git config --global alias.dc  'checkout --' #discard\n",
                            "RUN git config --global alias.dca  '!git dc .' #discardall\n",
                            "RUN git config --global alias.filelog  'log -u'\n",
                            "RUN git config --global alias.mf  'fetch -p -t origin' #fetch from origin\n",
                            "RUN git config --global alias.new  '!git mf && git nb' #new branch after fetching origin\n",
                            "RUN git config --global alias.po  'push origin'\n",
                            "RUN git config --global alias.ms  '!git mf && git status && git mg' #This will fetch, show you the status and display the graph\n",
                            "RUN git config --global alias.rn  'branch -m' #rename branch\n",
                            "RUN git config --global alias.em  'commit --amend' #edit message\n",
                            "RUN git config --global alias.rs \"!f() { i=\${1-1}; j=1; while [ \"\$j\" -le \"\$i\" ]; do git reset --soft HEAD^; j=\$(( j + 1 )); done }; f\" #delete last N commits but keep all changes (1 by default)\n",
                            "RUN git config --global alias.rh \"!f() { i=\${1-1}; j=1; while [ \"\$j\" -le \"\$i\" ]; do git reset --hard HEAD^; j=\$(( j + 1 )); done }; f\" #delete last N commits and all changes (1 by default)\n",
                            "RUN git config --global alias.nb \"!f() { MYBRANCH=origin/master; git checkout -b \$1 \${2-\$MYBRANCH}; }; f\"  #new branch without fetching from remote\n",
                            "RUN git config --global alias.myfilediff \"!f() { MYBRANCH=\$(git cb); git diff --name-only \$MYBRANCH \${1-origin/master}; }; f\"\n",
                            "RUN git config --global alias.myfulldiff \"!f() { MYBRANCH=\$(git cb); git diff \${1-origin/master} \$MYBRANCH; }; f\"\n",
                            "RUN git config --global alias.ci \"!f() { git show --pretty=fuller --name-status \$1; }; f\" #commit info\n",
                            "RUN git config --global alias.sm \"!f() { git log --all --oneline --grep=\$1; }; f\" #searchmessage\n",
                            "RUN git config --global alias.mp \"!f() { MYBRANCH=\$(git cb); git po \$MYBRANCH:\${1-\$MYBRANCH}; }; f\"  #mypush. branch name will be current branch name\n",
                            "RUN git config --global alias.mpf \"!f() { MYBRANCH=\$(git cb); git po -f \$MYBRANCH:\${1-\$MYBRANCH}; }; f\"  #mypushforce\n",
                            "RUN git config --global alias.fb \"!f() { git describe --contains \$1 | cut -d'~' -f1; }; f\" #find build in which commit is included\n",
                            "RUN git config --global alias.fr 'rev-parse --abbrev-ref --symbolic-full-name @{u}' #find parent branch\n",
                            "RUN git config --global alias.mr \"!f() { REMOTE=\$(git fr); git rebase \$REMOTE; }; f\" #rebase\n",
                            "RUN git config --global alias.rc 'rebase --continue'\n",
                            "RUN git config --global alias.ra 'rebase --abort'\n",
                            "RUN git config --global alias.tc 'rev-list -n 1' #find commit on which this tag exists\n",
                            "RUN git config --global alias.lc \"!f() { COMMENT=\${1-\\\"tmp\\\"}; git add *; git cm \\\"\$COMMENT\\\"; }; f\" #lazycommit. It will stage everything and make a commit with default commit message \"tmp\"\n",
                            "RUN git config --global alias.lp \"!f() { git lc \\\"\$1\\\"; BRANCH=\$(git cb); git mp \${2-\$BRANCH}; }; f\"  #lazypush. It will do lazycommit and then push your branch to origin.\n",
                            "RUN git config --global alias.lpf \"!f() { git lc \\\"\$1\\\"; BRANCH=\$(git cb); git mpf \${2-\$BRANCH}; }; f\" #lazypushforce\n",
                            "RUN git config --global alias.cwl \"!f() { MSG=\$(git log -1 --pretty=%B); git commit -m \\\"\$MSG\\\"; git em; }; f\" #create a commit with same message as last commit and give option to edit commit message\n\n",
                            "RUN git clone https://github.com/zeromq/libzmq && mkdir -p libzmq/build && cd libzmq/build && cmake .. && make -j4 install\n",
                            "RUN git clone https://github.com/zeromq/cppzmq && mkdir -p cppzmq/build && cd cppzmq/build && cmake .. && make -j4 install\n\n",
                            ])

    docker_file.write("RUN git config --global user.name \"%s\"\n" % user_name)
    docker_file.write(
        "RUN git config --global user.email \"%s\"\n" % user_email)
