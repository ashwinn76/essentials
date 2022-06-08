# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.234.0/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use ubuntu-22.04 or ubuntu-18.04 on local arm64/Apple Silicon): ubuntu-22.04, ubuntu-20.04, ubuntu-18.04

FROM ubuntu:22.04

COPY ./setup_git_aliases.sh /tmp/
RUN chmod +x /tmp/setup_git_aliases.sh && /tmp/setup_git_aliases.sh && rm -f /tmp/setup_git_aliases.sh

COPY ./install_cpp_reqs.sh /tmp/
RUN chmod +x /tmp/install_cpp_reqs.sh && /tmp/install_cpp_reqs.sh && rm -f /tmp/install_cpp_reqs.sh

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>


