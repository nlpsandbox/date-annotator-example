# nlp-sandbox-date-annotator-example

[![GitHub Stars](https://img.shields.io/github/stars/data2health/nlp-sandbox-date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-date-annotator-example)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/data2health/nlp-sandbox-date-annotator-example)
[![GitHub CI](https://img.shields.io/github/workflow/status/data2health/nlp-sandbox-date-annotator-example/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-date-annotator-example)
[![GitHub License](https://img.shields.io/github/license/data2health/nlp-sandbox-date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-date-annotator-example)
<!-- [![GitHub Release](https://img.shields.io/github/release/data2health/nlp-sandbox-date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-date-annotator-example/releases) -->
<!-- [![Docker Stars](https://img.shields.io/docker/stars/nlpsandbox/date-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/data2health/nlp-sandbox-date-annotator-example) -->

An example implementation of the NLP Sandbox Date Annotator

## Development

### Requirements

- Node
- Java (required by openapi-generator)

## Install

    npm install

## Generate initial server

Download the OpenAPI specification file *openapi.yaml* for the Date Annotator
from XXX and save it to the root folder of this GitHub repository

    curl -O -s https://.../openapi.yaml

Display help information about openapi-generator

    npx openapi-generator --help

Identify the server generator that you want to use from this list

    npx openapi-generator list

Generate the server codebase using the selected generator (here `python-flask`)

    npx openapi-generator generate -i openapi.yaml -g python-flask -o src/server

That's it! You can now start the server by following the instructions given in
*src/server/README.md* (TODO add URL).