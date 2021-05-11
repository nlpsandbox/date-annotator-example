# NLP Sandbox Date Annotator Example

[![GitHub Release](https://img.shields.io/github/release/nlpsandbox/date-annotator-example.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-example/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/nlpsandbox/date-annotator-example/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-example/actions)
[![GitHub License](https://img.shields.io/github/license/nlpsandbox/date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-example/blob/develop/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/date-annotator-example)
[![Discord](https://img.shields.io/discord/770484164393828373.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://nlpsandbox.io/discord "Realtime support / chat with the community and the team")
[![nlpsandbox.io](https://img.shields.io/badge/nlp_sandbox-leaderboard-blue.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMjAuMiAxNS40VjguNmMxLjktLjUgMy4zLTIuMiAzLjMtNC4yIDAtMi40LTItNC40LTQuNC00LjRzLTQuNCAyLTQuNCA0LjRjMCAuNS4xIDEgLjMgMS41TDguNSA5LjVjLS43LTEuMi0yLjEtMi0zLjYtMi0yLjQgMC00LjQgMi00LjQgNC40czIgNC40IDQuNCA0LjRjMS4zIDAgMi40LS41IDMuMi0xLjRsNi43IDMuOWMtLjEuMi0uMS41LS4xLjggMCAyLjQgMiA0LjQgNC40IDQuNHM0LjQtMiA0LjQtNC40YzAtMi0xLjQtMy43LTMuMy00LjJ6TTQuOSAxNC4yYy0xLjIgMC0yLjItMS0yLjItMi4yczEtMi4yIDIuMi0yLjIgMi4yIDEgMi4yIDIuMi0xIDIuMi0yLjIgMi4yem0xNC4yLTEyYzEuMiAwIDIuMiAxIDIuMiAyLjJzLTEgMi4yLTIuMiAyLjItMi4yLTEtMi4yLTIuMiAxLTIuMiAyLjItMi4yem0tMy40IDE0LjZMOS4yIDEzYy4xLS4zLjEtLjcuMS0xdi0uM2w3LTRjLjUuNCAxLjEuNyAxLjcuOXY2LjhjLS45LjItMS43LjctMi4zIDEuNHptMy40IDVjLTEuMiAwLTIuMi0xLTIuMi0yLjJzMS0yLjIgMi4yLTIuMiAyLjIgMSAyLjIgMi4yLTEgMi4yLTIuMiAyLjJ6IiBmaWxsPSIjZmZmIi8+PC9zdmc+)](https://nlpsandbox.io/tools/date-annotator/leaderboard "View the performance of this tool on nlpsandbox.io")

[date-annotator-leaderboard]: https://www.synapse.org/#!Synapse:syn22277124/wiki/608039

Example implementation of the [NLP Sandbox Date Annotator]

## Overview

This repository provides a Python-Flask implementation of the [NLP Sandbox Date
Annotator]. The Date Annotator is one of the first NLP Tools that can be
benchmarked on [nlpsandbox.io]. A Date Annotator takes as input a clinical
note and outputs a list of predicted date annotations found in the clinical
note.

### Specification

- Date Annotator API version: 1.1.0
- Tool version: 1.1.0
- Docker image: [nlpsandbox/date-annotator-example]

## Model

This NLP tool relies on simple regular expressions to identify the location of
date strings in a clinical note.

This implementation is provided as an example that Developers can use to quick
start the development of a new model by creating a repository from this [GitHub
template] (see below).

The CI/CD workflow of this repository will automatically build and publish a
Docker image to DockerHub. The model can then be submitted as-is to the [NLP
Sandbox], if you wish to benchmark its performance -- just don't expect a high
performance!

## Usage

### Running with Docker

The command below starts the Date Annotator locally.

    docker-compose up --build

You can stop the container run with `Ctrl+C`, followed by `docker-compose down`.

### Running with Python

We recommend using a Conda environment to install and run the Date Annotator.

    conda create --name date-annotator python=3.9.1
    conda activate date-annotator

Install and start the Date Annotator.

    cd server/
    pip install -e .
    python -m openapi_server

### Accessing the UI

The Date Annotator provides a web interface that you can use to annotate
clinical notes. The address of this interface depends on whether you run the
Date Annotator using Docker (production mode) or the Python development
server.

- Using Docker: http://localhost/ui
- Using Python: http://localhost:8080/ui

## Development

This section describes how you can start developing your own Date Annotator that
you can then submit for evaluation to the NLP Sandbox.

### Requirements

- [Node JS](https://nodejs.org/)
- Java (required by [OpenAPITools/openapi-generator])

### Creating a new GitHub repository

This step will depend on your preferred programming language-framework.

- If you develop in Python-Flask, create a new repository from this [GitHub
  template].
- If you develop in Java-Spring, create a new repository from the GitHub
  template [nlpsandbox/date-annotator-example-java].

If you prefer to develop using another language or if you want to learn how this
repository has been generated, go to the section [Creating a new Date Annotator
from scratch](#Creating-a-new-Date-Annotator-from-scratch).

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
- The tag `nightly` is created every night everyday at 10am UTC.

### Creating a new Date Annotator from scratch

Follow the steps listed below to generate an initial implementation - also
called "stub" - of the Date Annotator using one of the many languages and
framework supported by [OpenAPITools/openapi-generator].

1. Download the latest OpenAPI specification of the [NLP Sandbox Date Annotator].

       curl -fO https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/openapi.yaml

2. Copy the file [package.json] from this repository to your project.
3. Install the development tools defined in *package.json*

       npm ci

4. Display the help information of `openapi-generator-cli`

       ./node_modules/.bin/openapi-generator-cli --help

5. Display the list of programming languages-framework supported by the OpenAPI
   generator to create SERVER stubs.

       ./node_modules/.bin/openapi-generator-cli list

6. Generate the server stub using the generator of your choice (here
   `python-flask`). The option `-o` is to specify the name of the folder where
   the files generated will be saved.

       mkdir server
       ./node_modules/.bin/openapi-generator-cli \
           generate -i openapi.yaml -g python-flask -o server

7. Start your new NLP tool locally by following the instructions outlines in the
   section [Running with Python](#Running-with-Python). Open the page
   http://localhost:8080/ui in your browser to navigate to the web interface of
   the tool. You can now start implementing the different controllers of the
   tools in the folder *server/openapi_server/controllers*. Use the controllers
   defined in this repository as a reference.

### Updating your tool after the release of a new API version

The NLP Sandbox Team and community may introduce changes to the OpenAPI
specifications of the NLP Sandbox Tools. For example, the [Patient schema] may
include in the future a new property that this tool could leverage to generate
more accurate predictions. When this happens, the version of the tool
specifications will be bumped. The latest version of each specification can be
found in the README of the repository [nlpsandbox/nlpsandbox-schemas].

Here is the protocol that we apply to update this example Date Annotator when a
new release of the Date Annotator specification is available:

1. Create a new branch

       git checkout -b update-to-specification-x.y.z

2. Download the latest OpenAPI specification of the Date Annotator.

       curl -fO https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/openapi.yaml

3. Re-run the OpenAPI generator using the same command that you have used to
   generated the initial server stub.

       npm run generate:server openapi.yaml

4. Review and merge the changes. If you are using VS Code, this step can be
   performed relatively easily using the section named "Source Control". This
   section lists the files that have been modified by the generator. When
   clicking on a file, VS Code shows side-by-side the current and updated
   version of the file. Changes can be accepted or rejected at the level of an
   entire file or selected lines.

### Testing the NLP tool

This command will check that your Python code adheres to the style guide defined
for this project (see [server/setup.cfg](server/setup.cfg)).

    npm run lint

The command below will run the unit and integration tests.

    npm run test

### Versioning

This package uses [semantic versioning] for releasing new versions. Creating a
GitHub release of this repository will trigger the CI/CD workflow which will in
turn build the new Docker image for this tool before publishing it to DockerHub.

We recommend to include the following information at the top of your README:

- `Date Annotator API version`: The version of the Date Annotator specification
  implemented by the tool.
- `Tool version`: The version of the tool.

Initially, it may be tempting to align the tool version to the API version. As
you improve your tool and fix bugs, you will likely release more than one
version of your tool for the same API version. Note that for the sake of
reproducibility, it is encouraged to not reuse version tags.

## Benchmarking

Visit [nlpsandbox.io] for instructions on how to submit your tool and evaluate
its performance on public and private datasets.

## Contributing

Thinking about contributing to this project? Get started by reading our
[Contributor Guide](CONTRIBUTING.md).

## License

[Apache License 2.0]

<!-- Links -->

[nlpsandbox.io]: https://www.synapse.org/nlpsandbox
[NLP Sandbox]: https://www.synapse.org/nlpsandbox
[NLP Sandbox Date Annotator]: https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/docs/
[nlpsandbox/date-annotator-example]: https://hub.docker.com/r/nlpsandbox/date-annotator-example
[GitHub template]: https://github.com/nlpsandbox/date-annotator-example/generate
[NLP Sandbox]: nlpsandbox.io
[nlpsandbox/date-annotator-example-java]: https://github.com/nlpsandbox/date-annotator-example-java
[Apache License 2.0]: https://github.com/nlpsandbox/date-annotator-example/blob/develop/LICENSE
[Patient schema]: https://github.com/nlpsandbox/nlpsandbox-schemas/blob/develop/openapi/commons/components/schemas/Patient.yaml
[nlpsandbox/nlpsandbox-schemas]: https://github.com/nlpsandbox/nlpsandbox-schemas
[semantic versioning]: https://semver.org/
[OpenAPITools/openapi-generator]: https://github.com/OpenAPITools/openapi-generator
