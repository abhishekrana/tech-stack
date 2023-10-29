# syntax=docker/dockerfile:1.3

####################################################################################################
# Stage: base-deps
FROM golang:1.21-bullseye as base-deps

ENV WORKSPACE_PATH=/workspace/app-1
WORKDIR /workspace/app-1

COPY src/app-1/go.mod src/app-1/go.sum ./src/app-1/
RUN cd src/app-1 && go mod download

EXPOSE 5000

####################################################################################################
# Stage: dev-deps
FROM base-deps AS dev-deps

# Install dev dependencies

####################################################################################################
# Stage: dev-test
FROM dev-deps AS dev-test

ARG BUILD_TYPE

LABEL build-type=$BUILD_TYPE
LABEL git-hash=$GIT_HASH
LABEL git-tag=$GIT_TAG

COPY src/app-1/go.mod src/app-1/go.sum src/app-1/
COPY src/app-1/cmd src/app-1/cmd
COPY src/app-1/internal src/app-1/internal

RUN cd src/app-1 \
    && CGO_ENABLED=0 GOOS=linux go build -a -o ${WORKSPACE_PATH}/orders cmd/*.go

CMD ["bash", "-c", "${WORKSPACE_PATH}/orders"]

####################################################################################################
# Stage: prod
FROM base-deps AS prod

ARG BUILD_TYPE
ARG GIT_HASH
ARG GIT_TAG

LABEL build-type=$BUILD_TYPE
LABEL git-hash=$GIT_HASH
LABEL git-tag=$GIT_TAG

COPY src/app-1/go.mod src/app-1/go.sum src/app-1/
COPY src/app-1/cmd src/app-1/cmd
COPY src/app-1/internal src/app-1/internal

RUN cd src/app-1 \
    && CGO_ENABLED=0 GOOS=linux go build -a -o ${WORKSPACE_PATH}/orders cmd/*.go

CMD ["bash", "-c", "${WORKSPACE_PATH}/orders"]
