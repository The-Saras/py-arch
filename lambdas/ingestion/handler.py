def lambda_handler(event, context):
    print("Lambda 1 was triggered!")
    return {
        "statusCode" : 200,
        "body" : "Lambda 1 was triggered successfully"
    }