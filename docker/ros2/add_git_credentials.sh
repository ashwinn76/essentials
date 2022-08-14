#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "Please state your name and email so that git credentials can be added"
fi

DIR=$(dirname $0)

sudo echo "RUN git config --global user.name \"$1\"" >> "${DIR%/}/Dockerfile"
sudo echo "RUN git config --global user.email \"$2\"" >> "${DIR%/}/Dockerfile"