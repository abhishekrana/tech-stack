# syntax=docker/dockerfile:1.3

####################################################################################################
# Stage: base-deps
FROM golang:1.21-bullseye as base-deps

ENV WORKSPACE_PATH=/workspace/migrations
WORKDIR /workspace/migrations

COPY src/migrations/go.mod src/migrations/go.sum ./src/migrations/
RUN cd src/migrations && go mod download

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

COPY src/migrations/go.mod src/migrations/go.sum src/migrations/
COPY files files
COPY src/migrations/cmd src/migrations/cmd
COPY src/migrations/internal src/migrations/internal

RUN cd src/migrations \
    && CGO_ENABLED=0 GOOS=linux go build -a -o ${WORKSPACE_PATH}/migrate cmd/*.go

CMD ["bash", "-c", "${WORKSPACE_PATH}/migrate"]

####################################################################################################
# Stage: prod
FROM base-deps AS prod

ARG BUILD_TYPE
ARG GIT_HASH
ARG GIT_TAG

LABEL build-type=$BUILD_TYPE
LABEL git-hash=$GIT_HASH
LABEL git-tag=$GIT_TAG

COPY src/migrations/go.mod src/migrations/go.sum src/migrations/
COPY files files
COPY src/migrations/cmd src/migrations/cmd
COPY src/migrations/internal src/migrations/internal

RUN cd src/migrations \
    && CGO_ENABLED=0 GOOS=linux go build -a -o ${WORKSPACE_PATH}/migrate cmd/*.go

CMD ["bash", "-c", "${WORKSPACE_PATH}/migrate"]
