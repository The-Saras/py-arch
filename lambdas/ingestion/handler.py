import json
import boto3

sns = boto3.client(
    "sns",
    endpoint_url="http://host.docker.internal:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
)

TOPIC_ARN = "arn:aws:sns:us-east-1:000000000000:entity-events"


def lambda_handler(event, context):
    print("Lambda 1 was triggered!")
    print("Received event:", event)

    entity_event = {
        "eventType": "ENTITY_CREATED",
        "entityId": event["entityId"],
        "name": event["name"],
    }

    response = sns.publish(
        TopicArn=TOPIC_ARN,
        Message=json.dumps(entity_event),
    )

    print("Published to SNS:", response["MessageId"])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Entity event published",
            "messageId": response["MessageId"],
        }),
    }

    