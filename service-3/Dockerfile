# syntax=docker/dockerfile:1.3

####################################################################################################
# Stage: base-deps
FROM node:lts-alpine AS base-deps

ENV WORKSPACE_PATH=/workspace/service-3
WORKDIR /workspace/service-3

COPY package.json package-lock.json ./
RUN npm install --production

EXPOSE 80
# EXPOSE 8080

####################################################################################################
# Stage: dev-deps
FROM base-deps AS dev-deps

# Install dev dependencies
RUN npm install --dev

####################################################################################################
# Stage: dev-test
FROM dev-deps AS dev-test

ARG BUILD_TYPE

LABEL build-type=$BUILD_TYPE
LABEL git-hash=$GIT_HASH
LABEL git-tag=$GIT_TAG

ENV NODE_ENV="development"

RUN npm install -g http-server

COPY . .
RUN npm run build

CMD [ "http-server", "dist" ]

####################################################################################################
# Stage: prod
FROM nginx:stable-alpine as prod

ARG BUILD_TYPE
ARG GIT_HASH
ARG GIT_TAG

LABEL build-type=$BUILD_TYPE
LABEL git-hash=$GIT_HASH
LABEL git-tag=$GIT_TAG

ENV NODE_ENV="production"

COPY --from=dev-test /workspace/service-3/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
