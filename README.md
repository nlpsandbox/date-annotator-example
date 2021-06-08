[![nlpsandbox.io](https://nlpsandbox.github.io/nlpsandbox-themes/banner/Banner@3x.png)](https://nlpsandbox.io)

# NLP Sandbox Date Annotator Example

[![GitHub Release](https://img.shields.io/github/release/nlpsandbox/date-annotator-example.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-example/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/nlpsandbox/date-annotator-example/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-example/actions)
[![GitHub License](https://img.shields.io/github/license/nlpsandbox/date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-example/blob/develop/LICENSE)
[![Docker](https://img.shields.io/badge/docker-blue.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=nlpsandbox&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMy4yIDcuOS0xLjctMXYxMS40bDkuOSA1LjdWMTIuNkw1LjYgOS4zIDMuMiA3Ljl6bTE3LjEtMS4zIDEuNS0uOUwxMiAwIDIuMiA1LjdsMi42IDEuNS4xLjEgMS43IDEgNS41IDMuMiA1LjEtMyAzLjEtMS45ek0xMiA5LjUgOS4zIDcuOSA3LjQgNi44bC0xLjctMS0uMS0uMWgtLjFMMTIgMS45bDYuNSAzLjhMMTYuMyA3IDEyIDkuNXptOC44LTEuNi0yLjQgMS40LS41LjItNS4zIDMuMVYyNGw5LjktNS43VjYuOWwtMS43IDF6IiBmaWxsPSIjZmZmIi8+PC9zdmc+)](https://www.synapse.org/#!Synapse:syn25828638 "Get the Docker image of this tool on NLPSandbox.io")
[![Docker](https://img.shields.io/badge/leaderboard-blue.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=nlpsandbox&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMy4yIDcuOS0xLjctMXYxMS40bDkuOSA1LjdWMTIuNkw1LjYgOS4zIDMuMiA3Ljl6bTE3LjEtMS4zIDEuNS0uOUwxMiAwIDIuMiA1LjdsMi42IDEuNS4xLjEgMS43IDEgNS41IDMuMiA1LjEtMyAzLjEtMS45ek0xMiA5LjUgOS4zIDcuOSA3LjQgNi44bC0xLjctMS0uMS0uMWgtLjFMMTIgMS45bDYuNSAzLjhMMTYuMyA3IDEyIDkuNXptOC44LTEuNi0yLjQgMS40LS41LjItNS4zIDMuMVYyNGw5LjktNS43VjYuOWwtMS43IDF6IiBmaWxsPSIjZmZmIi8+PC9zdmc+)](https://www.synapse.org/#!Synapse:syn22277123/wiki/608544 "View the performance of this tool on nlpsandbox.io")
[![Discord](https://img.shields.io/discord/770484164393828373.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://nlpsandbox.io/discord "Realtime support / chat with the community and the team")

## Introduction

[NLPSandbox.io] is an open platform for benchmarking modular natural language
processing (NLP) tools on both public and private datasets. Academics, students,
and industry professionals are invited to browse the available tasks and
participate by developing and submitting an NLP Sandbox tool.

This repository provides an example implementation of the [NLP Sandbox Date
Annotator API] written in Python-Flask. An NLP Sandbox date annotato takes as
input a clinical note (text) and outputs a list of predicted date annotations
found in the clinical note. Here dates are identified using regular expressions.

This tool is provided to NLP developers who develop in Python as a starting
point to package their own date annotator as an NLP Sandbox tool (see section
[Development](#Development)). This section also describes how to generate a tool
"stub" using [openapi-generator] for 50+ programming languages-frameworks. This
repository includes a GitHub CI/CD workflow that lints, tests, builds and pushes
a Docker image of this tool to Synapse Docker Registry. This image of this
example tool can be submitted as-is on NLPSandbox.io to benchmark its
performance -- just don't expect a high performance!


## Contents

- [Specification](#Specification)
- [Requirements](#Requirements)
- [Usage](#Usage)
  - [Running with Docker](#Running-with-Docker)
  - [Running with Python](#Running-with-Python)
  - [Accessing this NLP Sandbox tool User
    Interface](#Accessing-this-NLP-Sandbox-tool-User-Interface)
- [Development](#Development)
  - [Development requirements](#Development-requirements)
  - [Creating a GitHub repository](#Creating-a-GitHub-repository)
  - [Configuring the CI/CD workflow](#Configuring-the-CI/CD-workflow)
  - [Enabling version updates](#Enabling-version-updates)
  - [Generating a new NLP Sandbox tool using
    openapi-generator](#Generating-a-new-NLP-Sandbox-tool-using-openapi-generator)
  - [Keeping your tool up-to-date](#Keeping-your-tool-up-to-date)
  - [Testing](#Testing)
  - [Preventing an NLP Sandbox tool from connecting to remote
    servers](#Preventing-an-NLP-Sandbox-tool-from-connecting-to-remote-servers)
- [Versioning](#Versioning)
  - [GitHub release tags](#GitHub-release-tags)
  - [Docker image tags](#Docker-image-tags)
- [Benchmarking on NLPSandbox&#46;io](#Benchmarking-on-NLPSandbox&#46;io)
- [Contributing](#Contributing)
- [License](#License)

## Specification

- NLP Sandbox schemas version: 1.1.2
- NLP Sandbox tool version: 1.1.2
- Docker image: [docker.synapse.org/syn22277123/date-annotator-example]


## Requirements

- [Docker Engine] >=19.03.0


## Usage

### Running with Docker

The command below starts this NLP Sandbox date annotator locally.

```console
docker compose up --build
```

You can stop the container run with `Ctrl+C`, followed by `docker compose down`.

### Running with Python

Create a Conda environment.

```console
conda create --name date-annotator python=3.9
conda activate date-annotator
```

Install and start this NLP Sandbox date annotator.

```console
cd server && pip install -r requirements.txt
python -m openapi_server
```

### Accessing this NLP Sandbox tool User Interface

This NLP Sandbox tool provides a web interface that you can use to annotate
clinical notes. This web client has been automatically generated by
[openapi-generator]. To access the UI, open a new tab in your browser and
navigate to one of the following address depending on whether you are running
the tool using Docker (production) or Python (development).

- Using Docker: http://localhost/ui
- Using Python: http://localhost:8080/ui


## Development

This section describes how to develop your own NLP Sandbox date annotator in
Python-Flask and other programming languages-frameworks. This example tool is
also available in Java in the GitHub repository
[nlpsandbox/date-annotator-example-java].

### Development requirements

- [Node] >=14
- [Java] >=1.8 (required by [openapi-generator])
- [Conda] >=4 and/or [Python] >= 3.7
- [Synapse.org] user account to push the image to [docker.synapse.org]

### Creating a GitHub repository

Depending on the language-frameworks you want to develop with:

- Python-Flask: create a new repository from this [this GitHub template].
- Java-Spring: create a new repository from the GitHub repository
  [nlpsandbox/date-annotator-example-java].
- Other languages-frameworks: create a brand-new GitHub repository before
  generating a NLP Sandbox tool stub in section [XXX].

You can also use a different code repository hosting service like [GitLab] and
[Bitbucket].

### Configuring the CI/CD workflow

This repository includes a GitHub [CI/CD workflow] that lints, tests, builds and
pushes a Docker image of this tool to Synapse Docker Registry. Only the images
that have been pushed to Synapse Docker Resgitry can be submitted to
[NLPSandbox.io] benchmarks for now.

After creating your GitHub repository, you need to configure the CI/CD workflow
if you want to benefit from automatic lint checks, tests and Docker builds.

1. Create two [GitHub secrets]
   - `SYNAPSE_USERNAME`: Your [Synapse.org] username.
   - `SYNAPSE_TOKEN`: A [personal access token] that has the permissions `View`,
     `Download` and `Modify`.
2. In the [CI/CD workflow], update the environment variable `docker_repository`
   with the value `docker.synapse.org/<synapse_project_id>/<docker_image>`
   where:
   - `<synapse_project_id>`: the Synapse ID of a project you have created on
     [Synapse.org].
   - `<docker_image>` is the name of your image/tool.

### Enabling version updates

This repository includes a [Dependabot configuration] that instructs GitHub to
let you know when an update is available for one of your dependencies (e.g.
Python, Node, Docker). Dependabot will automatically open a PR when an update is
available. If you have configured the CI/CD workflow that comes with this
repository, the workflow will automatically run and notify you if the update is
breaking your code. You can then resolve the issue before merging the PR, hence
making the update effective.

For more information on Dependabot, please visit the GitHub page [Enabling and
disabling version updates].

### Generating a new NLP Sandbox tool using openapi-generator

The development of new NLP Sandbox tools is streamlined by using the
[openapi-generator] to generate tool "stubs" for more than 50 programming
languages and frameworks. Here a date annotator stub refers to an initial
implementation that has been automatically generated by [openapi-generator] from
the [NLP Sandbox Date Annotator API] specification.

Run the command below to get the list of languages-framework supported by the
[openapi-generator] (under the section `SERVER generators`).

```console
npx @openapitools/openapi-generator-cli list
```

Generate the date annotator stub from an empty GitHub repository (here in
Python-Flask):

```console
mkdir server
npx @openapitools/openapi-generator-cli generate \
  -g python-flask \
  -o server \
  -i https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/openapi.json
```

where the option `-i` refers to the OpenAPI specification of the [NLP Sandbox
Date Annotator API].

The URL is composed of different elements:

- `date-annotator` - The type of NLP Sandbox tool to generate. The list of all
  the NLP Sandbox tool types available is defined in the [NLP Sandbox schemas].
- `latest` - The latest stable version of the [NLP Sandbox schemas]. This token
  can be replaced by a specific release version `x.y.z` of the [NLP Sandbox
  schemas].

### Keeping your tool up-to-date

The NLP Sandbox schemas is updated after receiving contribution from the
community. For example, the [Patient schema] may include in the future
additional information that NLP Sandbox tools can leverage to generate more
accurate predictions.

After an update of the NLP Sandbox schemas, [NLPSandbox.io] will only accept to
evaluate tools that implement the latest version of the schemas. It is therefore
important to keep your tools up-to-date and re-submit them so that they continue
to appear in the leaderboards and to be used by the community.

This GitHub repository includes a workflow that checks daily if a new release of
the [NLP Sandbox schemas] is available, in which case a PR will be created.
Follow the steps listed below to update your tool.

1. Checkout the branch created by the workflow.

       git checkout <branch_name>

2. Re-run the same [openapi-generator] command you used to generate the tool
   stub. If you started from an existing tool implementation like the one
   included in this GitHub repository, run the following command to update your
   tool to the latest version of the [NLP Sandbox schemas] (this command would
   be defined in `package.json`).

       npm run generate:server:latest

3. Review the updates made to this tool in [NLP Sandbox schemas CHANGELOG].

4. Review and merge the changes. If you are using VS Code, this step can be
   performed relatively easily using the section named "Source Control". This
   section lists the files that have been modified by the generator. When
   clicking on a file, VS Code shows side-by-side the current and updated
   version of the file. Changes can be accepted or rejected at the level of an
   entire file or for a selection of lines.

5. Submit your updated tool to [NLPSandbox.io].

### Testing

If you started from an existing tool implementation like the one included in
this GitHub repository, run the following command to lint and test your tool.

```console
npm run lint
npm run test
```

For Python-Flask tools:

- The linter configuration is defined in [server/setup.cfg](server/setup.cfg).
- The configuration of the unit and integration tests lives in
  [server/tox.ini](server/tox.ini).

### Preventing an NLP Sandbox tool from connecting to remote servers

The NLP Sandbox promotes the development of tools that are re-usable,
reproducible, portable and cloud-ready. The table below describes how preventing
a tool from connecting to remote server contributes to some of these tool
properties.

Property        | Description
----------------|------------
Reproducibility | The output of a tool may not be reproducible if the tool depends on external resources, for example, that may no longer be available in the future.
Security        | A tool may attempt to upload sensitive information to a remote server.

The Docker Compose configuration included with this GitHub repository
([docker-compose.yml](docker-compose.yml)) prevents the tool container to
establish remote connection. This is achieved through the use of a `internal`
Docker network and the presence of the Nginx container placed in front of the
tool container. One benefit is that you can test your tool locally and ensure
that it works fine while it does not have access to the internet. Note that when
being evaluated on [NLPSandbox.io], additional measures are put in place to
prevent tools from connecting to remote servers.


## Versioning

### GitHub release tags

This repository uses [semantic versioning] to track the releases of this tool.
This repository uses "non-moving" GitHub tags, that is, a tag will always point
to the same git commit once it has been created.

### Docker image tags

The artifact published by the [CI/CD workflow] of this GitHub repository is a
Docker image pushed to the Synapse Docker Registry. This table lists the image
tags pushed to the registry.

| Tag name                    | Moving | Description
|-----------------------------|--------|------------
| `latest`                    | Yes    | Latest stable release.
| `edge`                      | Yes    | Latest commit made to the default branch.
| `edge-<sha>`                | No     | Same as above with the reference to the git commit.
| `<major>.<minor>.<patch>`   | No     | Stable release.

You should avoid using a moving tag like `latest` when deploying containers in
production, because this makes it hard to track which version of the image is
running and hard to roll back.


## Benchmarking on NLPSandbox&#46;io

Visit [nlpsandbox.io] for instructions on how to submit your NLP Sandbox tool
and evaluate its performance.

## Contributing

Thinking about contributing to this project? Get started by reading our
[contribution guide].

## License

[Apache License 2.0]

<!-- Links -->

[nlpsandbox.io]: https://www.synapse.org/nlpsandbox
[docker.synapse.org/syn22277123/date-annotator-example]: https://www.synapse.org/#!Synapse:syn25828638
[Synapse.org]: https://synapse.org
[openapi-generator]: https://github.com/OpenAPITools/openapi-generator
[contribution guide]: .github/CONTRIBUTING.md
[Apache License 2.0]: https://github.com/nlpsandbox/date-annotator-example/blob/main/LICENSE
[Docker Engine]: https://docs.docker.com/engine/install/
[Node]: https://nodejs.org/en/
[Java]: https://www.java.com/en/download/help/download_options.html
[Conda]: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
[Python]: https://www.python.org/downloads/
[docker.synapse.org]: https://synapse.org
[GitLab]: https://about.gitlab.com/
[Bitbucket]: https://bitbucket.org/product
[GitHub secrets]: https://docs.github.com/en/actions/reference/encrypted-secrets
[personal access token]: https://help.synapse.org/docs/Managing-Your-Account.2055405596.html
[CI/CD workflow]: .github/workflows/ci.yml
[Dependabot configuration]: .github/dependabot.yml
[Enabling and disabling version updates]: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/enabling-and-disabling-version-updates
[NLP Sandbox schemas]: https://github.com/nlpsandbox/nlpsandbox-schemas
[nlpsandbox/nlpsandbox-schemas]: https://github.com/nlpsandbox/nlpsandbox-schemas
[NLP Sandbox Date Annotator API]: https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/docs/
[this GitHub template]: https://github.com/nlpsandbox/date-annotator-example/generate
[nlpsandbox/date-annotator-example-java]: https://github.com/nlpsandbox/date-annotator-example-java
[Patient schema]: https://github.com/nlpsandbox/nlpsandbox-schemas/blob/develop/openapi/commons/components/schemas/Patient.yaml
[semantic versioning]: https://semver.org/
[NLP Sandbox schemas CHANGELOG]: .github/CHANGELOG.md
