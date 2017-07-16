import boto3


def lamda_sendMessage(event, context):
    if not (('subject' in event) and ('message' in event) and ('from' in event) and ('name' in event)):
        return {"code": 1, "message": "Must preovide all values"}
    if event['subject'] != "" and event['message'] != "" and event['from'] != "" and event['name'] != "":
        toEmail = "email@domain.com"
        fromEmail = "email@domain.com"
        replyTo = event['from']
        name = event['name']
        subject = event['subject'] + " - " + name
        message = event['message']

        client = boto3.client('ses')
        response = client.send_email(
            Source=fromEmail,
            Destination={
                'ToAddresses': [
                    toEmail,
                ],
            },
            Message={
                'Subject': {
                    'Data': subject,
                    'Charset': 'utf8'
                },
                'Body': {
                    'Text': {
                        'Data': message,
                        'Charset': 'utf8'
                    }
                }
            },
            ReplyToAddresses=[
                replyTo
            ]
        )

        print response['MessageId']
        return {'code': 0, 'message': 'success'}
