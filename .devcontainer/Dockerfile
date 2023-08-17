# syntax=docker/dockerfile:1.3

ARG VARIANT=0.1.0
FROM tech-stack-base:${VARIANT}

ARG USER_UID=$USER_UID
ARG USER_GID=$USER_UID

# Setup non-root user
ARG USERNAME=$USERNAME
RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}
ENV HOME=/home/${USERNAME}

# Persist bash history across sessions/container rebuilds
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && sudo mkdir /commandhistory \
    && sudo touch /commandhistory/.bash_history \
    && sudo chown -R ${USERNAME} /commandhistory \
    && echo ${SNIPPET} >> "${HOME}/.bashrc"

# Bash completion
RUN cat ~/.bashrc | grep 'source /usr/share/bash-completion/completions/task.bash' || \
    echo "source /usr/share/bash-completion/completions/task.bash" >>~/.bashrc
RUN poetry completions bash >> ~/.bash_completion

ENV PIP_DEFAULT_TIMEOUT=60 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1

# Service-1
COPY --chown=${USERNAME}:${USERNAME} service-1/pyproject.toml service-1/poetry.lock ${HOME}/service-1/
RUN --mount=type=cache,target=~/.cache/pypoetry \
    cd ${HOME}/service-1 \
    && poetry install
