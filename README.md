# hgsqs - Mercurial to SQS hook

hgsqs provides a simple hook to send changeset information to SQS queues. This
could be useful if you want to collect information from mercurial commits or
integrate with other systems. It's perfect if you're running on AWS and are too
lazy to setup a real queue system or maybe you're just in the middle of a
message queuing obsession.

## Requirements
 - Python 2.7+
 - hgapi
 - boto

## Installation
```
pip install hgsqs
```

## Configuration
Put that in the .hg/hgrc of your project:
```
[hooks]
incoming.hgsqs = hgsqs

[hgsqs]
aws_access_key_id = FILL-IN
aws_secret_access_key = THE-BLANKS
queues = commit-analytics,irc-notifications,ticket-system
```

Then make sure your IAM user has the right permissions on these tables:
 - CreateQueue
 - GetQueueUrl
 - SendMessage
