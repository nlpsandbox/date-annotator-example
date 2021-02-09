# NLP Sandbox Date Annotator Example

[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/nlp-sandbox-date-annotator-example.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-date-annotator-example/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/nlp-sandbox-date-annotator-example/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-date-annotator-example)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/nlp-sandbox-date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-date-annotator-example)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/date-annotator-example)
[![Discord](https://img.shields.io/discord/770484164393828373.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://discord.gg/Zb4ymtF "Realtime support / chat with the community and the team")

An example implementation of the [NLP Sandbox Date Annotator].

## Overview

This repository provides a Python-Flask implementation of the [NLP Sandbox Date
Annotator]. The Date Annotator is one of the first NLP Tools that can be
benchmarked on nlpsandbox.io. A Date Annotator takes as input one clinical notes
as well as information about the patient and outputs a list of predicted date
annotations found in the clinical note.

- Date Annotator API version: 0.3.1
- Tool version: 0.x.y
- Docker image: [nlpsandbox/date-annotator-example]

## Model

This implementation relies on simple regular expressions to identify the
location of date strings in a clinical note.

## Creating your own NLP Tool

This implementation is provided as an example that Developers can use to quick
start the development of a new model by create a new repository from this
[GitHub template] (see below). The Docker image built and published
automatically by the CI/CD workflow of this repository can be submitted "as it
is" to the [NLP Sandbox] to benchmark its performance if you wish to try
submitting first (don't expect a high performance!).

## Usage

### Running with Docker

The command below starts the Date Annotator locally.

    docker-compose up

### Running with Python

We recommend using a Conda environment to install and run the Date Annotator.

    conda create --name nlp-sandbox-date-annotator-example python=3.9.1
    conda activate nlp-sandbox-date-annotator-example

Install and start the Date Annotator.

    cd server/
    pip install -r requirements.txt
    cd server && python -m openapi_server

### Annotating clinical notes

The Date Annotator provides a web interface that you can use to annotate
clinical notes. The address of this interface depends on whether you run the
Date Annotator using Docker (production mode) or using Python development
server.

- Using Docker: http://localhost
- Using Python: http://localhost:8080/api/v1/ui/

## Development

This section describes how you can start developing your own Date Annotator that
you can then submit for evaluation to the NLP Sandbox.

### Requirements

- [Node JS](https://nodejs.org/)
- Java (required by [OpenAPITools/openapi-generator])

### Creating a new GitHub repository

Depending on the programming language-framework

- If you develop in Python-Flask, create a new repository from this [GitHub
  template].
- If you develop in Java-Spring, create a new repository from the GitHub
  template [nlpsandbox/date-annotator-example-java].

If you prefer to developed using another language or if you want to learn how
this repository has been generated, go to the section [Creating a new GitHub
repository from scratch](#Creating-a-new-GitHub-repository-from-scratch).

### Configuring the CI/CD workflow

This repository provides a GitHub CI/CD workflow that performs the following
actions:

- Lint the Python code and Docker files.
- Test this NLP tool (integration tests).
- Build this NLP tool as a Docker image and publish it to DockerHub.

If you wish to enable the above CI/CD actions for your repository, please:

1. Create a public or private Docker repository on DockerHub (or another Docker
   registry).
2. Add the following GitHub Secrets to your repository to specify the
   credentials that the CI/CD workflow will use to push the Docker image to the
   registry.
    - `DOCKERHUB_PASSWORD`
    - `DOCKERHUB_USERNAME`
3. In the CI/CD workflow (.github/workflows/ci.yml), update the environment
   variable listed below with the name of your docker repository.
    - `docker_repository`

Note that the credentials used to push the Docker image to DockerHub must have
the permission `Admin` to push the README of your repository to DockerHub and
complete successfully the CI/CD workflow.

### Docker tags

The CI/CD workflow builds and pushes the following tags to the docker registry:

- The tag `edge` is created when a commit is pushed to the default branch of
  this repository (`develop`).
- The tags `latest`, `x`, `x.y`, `x.y.z` are created when the GitHub release
  `x.y.z` is created.
- The tag `nighlty` is created every night everyday at 10am UTC.

### Creating a new GitHub repository from scratch

TBA

### Updating your repository after the release of a new API version

TBA

### Testing the NLP tool

TBA

## License

[Apache License 2.0]

<!-- One option is to [create a GitHub repository based on this template repository][create_gh_repo_from_template]
if you plan to write your code in Python. This repository comes with a GitHub
workflow that will help you implementing good practices and notify you when a
new version of the OpenAPI specification for this NLP Tool is available. The
GitHub workfow also includes a job to automatically submit your Date Annotator
to the NLP Sandbox for evaluation.

Alternatively, follow the steps listed below to generate an initial implementation
of the Date Annotator using one of the many languages and framework supported by
[OpenAPITools/openapi-generator].

Start by downloading the latest version of the [NLP Sandbox Date Annotator OpenAPI specification]
and save this file to the root folder of your project.

    curl -f -O https://sage-bionetworks.github.io/nlp-sandbox-schemas/date-annotator/latest/openapi.yaml

Create the file *package.json* with this content:

    {
        "name": "awesome-date-annotator",
        "version": "1.0.0",
        "license": "Apache-2.0",
        "devDependencies": {
            "@openapitools/openapi-generator-cli": "^1.0.18-4.3.1"
        },
        "scripts": {
            "test": "tox"
        }
    }

Install the dependencies listed in *package.json*

    npm install

Display help information about `openapi-generator`

    ./node_modules/.bin/openapi-generator --help

Identify the server generator that you want to use from this list

    ./node_modules/.bin/openapi-generator list

Generate the server codebase using the selected generator (here `python-flask`)

    ./node_modules/.bin/openapi-generator \
        generate -i openapi.yaml -g python-flask -o server

That's it! You can now start the Data Annotator server using the instructions
given in the section [Running using Python](#Running-with-Python). -->

<!-- ### Update the codebase when a new OpenAPI spec is available (TO UPDATE)

When a new API has been released there are 2 ways to update this repository
with the new specification.

The procedure in both cases starts with:

1. Look at  https://github.com/Sage-Bionetworks/nlp-sandbox-schemas repository.
2. Identify if a newer version of the spec has been released since the developer created his tool OR since last time he updated it.
3. Download the latest version of the spec: https://sage-bionetworks.github.io/nlp-sandbox-schemas/date-annotator/latest/openapi.yaml
4. run the command :

    npx @openapitools/openapi-generator-cli generate -i openapi.yaml -g python-flask -o server.


This will generate an output file dist.yaml in the current directory. It should output the following:

    $ npm run build openapi/date-annotator/openapi.yaml

    > nlp-sandbox-schemas@0.1.6 build ~/nlp-sandbox-schemas
    > openapi bundle -o dist $npm_config_entrypoint "openapi/date-annotator/openapi.yaml"

    bundling openapi/date-annotator/openapi.yaml...
    📦 Created a bundle for openapi/date-annotator/openapi.yaml at dist.yaml in 28ms.

Next to re-generate the flask app using one  of two methods.

The first is the easiest and least error prone if you are worried about overriding existing files.
One can generate a new flask app in a "test" directory and compare results between the old and new
directories . This is done with the command:

    npx @openapitools/openapi-generator-cli \
        generate -i dist.yaml -g python-flask -o server

Then compare the ~/nlp-sandbox-data-annotated-example-updated/server to your existing ~/nlp-sandbox-data-annotated-example/server directory to see
what was updated.

The other method, once you are more confident, is to lay the files on top of the existing repository you've already checked with the command:

    openapi-generator generate -i dist.yaml -g python-flask -o ~/nlp-sandbox-data-annotated-example/server

If one wants to prevent certain files you know have already been customized then add those file names
cto the ~/nlp-sandbox-data-annotated-example/server/.openapi-generator-ignore file before running the preceding command.

Then use git to see what is updated and if you overwrote any files you wanted
to preserve. One can revert those changes and add those files to the .openapi-generator-ignore file for next time there is an update. -->


<!-- ### Generate a Spring Boost server stub

Generate the initial server stub from the OpenAPI specification

    mkdir server
    ./node_modules/.bin/openapi-generator-cli \
        generate -i openapi.yaml -g spring -o server

Build and start the server with Maven

    cd server
    mvn package
    java -jar target/openapi-spring-0.1.6.jar

The API documentation UI is now available at http://localhost:8080. -->

<!-- Links -->


[NLP Sandbox Date Annotator API]: https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/docs/
[NLP Sandbox Date Annotator]: https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/
[nlpsandbox/date-annotator-example]: https://hub.docker.com/r/nlpsandbox/date-annotator-example
[GitHub template]: https://github.com/nlpsandbox/date-annotator-example/generate
[NLP Sandbox]: nlpsandbox.io
[nlpsandbox/date-annotator-example-java]: https://github.com/nlpsandbox/date-annotator-example-java
[Apache License 2.0]: https://github.com/nlpsandbox/date-annotator-example/blob/develop/LICENSE


[NLP Sandbox Date Annotator OpenAPI specification]: https://github.com/Sage-Bionetworks/nlp-sandbox-schemas
[OpenAPITools/openapi-generator]: https://github.com/OpenAPITools/openapi-generator
[create_gh_repo_from_template]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template