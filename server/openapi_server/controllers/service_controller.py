from flask import jsonify

from openapi_server.models.service import Service  # noqa: E501


def service():  # noqa: E501
    """Get service information

    Get information about the service # noqa: E501


    :rtype: Service
    """
    service = Service(
        name="date-annotator-example",
        version="0.1.6",
        license="Apache-2.0",
        repository="github:Sage-Bionetworks/nlp-sandbox-date-annotator-" +
                   "example",
        description="An example implementation of the NLP Sandbox Date" +
                    " Annotator",
        author="The NLP Sandbox Team",
        author_email="thomas.schaffter@sagebionetworks.org",
        url="https://github.com/Sage-Bionetworks/nlp-sandbox-date-" +
            "annotator-example"
    )

    return jsonify(service), 200
