#!/usr/bin/env python

"""
Load as much meta-data as possible about a commit and push it to an SQS queue.
"""

import os
from boto import connect_sqs
from boto.sqs.jsonmessage import JSONMessage


def send(ui, repo, **kwargs):
    # Extract configuration from the hgrc config file.
    aws_access_key_id = ui.config("hgsqs", "aws_access_key_id", default=None)
    aws_secret_access_key = ui.config("hgsqs", "aws_secret_access_key",
                                      default=None)
    queue_names = ui.config("hgsqs", "queues", default="")

    if aws_access_key_id is None or aws_secret_access_key is None:
        ui.warn("warning: hgsqs is enabled but missing aws config\n")
        return 0

    queue_names = [n.strip() for n in queue_names if n.strip()]

    if not queue_names:
        ui.warn("warning: hgsqs is enabled but missing queues\n")
        return 0

    ctx = repo[None]
    msg = {
        "repo": os.path.basename(repo.root),
        "rev": ctx.rev(),
        # "hex": ctx.hex(),
        "user": ctx.user(),
        "date": ctx.date(),
        "files": ctx.files(),
        "description": ctx.description(),
        "branch": ctx.branch(),
    }

    conn = connect_sqs(aws_access_key_id, aws_secret_access_key)

    for name in queue_names:
        queue = conn.get_queue(name)
        if queue is None:
            queue = conn.create_queue(name)
        queue.set_message_class(JSONMessage)
        queue.write(queue.new_message(msg))
        ui.warn("sent changeset to {} SQS queue\n".format(name))

    return 0
