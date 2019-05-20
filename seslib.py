import boto3
from botocore.exceptions import ClientError
AWS_REGION = "us-west-2"
CHARSET = "UTF-8"

def get_client():
    return boto3.client('ses', region_name=AWS_REGION)

# Creating a template
def createTemplate(TemplateName, SubjectPart, HtmlPart, TextPart):
    client = get_client()
    response = client.create_template(
      Template = {
        'TemplateName' : TemplateName,
        'SubjectPart'  : SubjectPart,
        #'TextPart'     : TextPart,
        'HtmlPart'     : HtmlPart,
      }
    )
    return response

# Template gets deleted
def deleteTemplate(TemplateName):
    client = get_client()
    response = client.delete_template(
            TemplateName = TemplateName
        )
    return response

# Template gets updated
def updateTemplate(TemplateName, SubjectPart, HtmlPart, TextPart):
    client = get_client()
    response = client.update_template(
        Template={
            'TemplateName': TemplateName,
            'SubjectPart' : SubjectPart,
            # 'TextPart'    : TextPart,
            'HtmlPart'    : HtmlPart,
        }
    )
    return response

# Returns a list of templates created till now.
def getTemplates():
    client = get_client()
    response = client.list_templates(MaxItems=10)
    return response

# Simple function which send emai, it doesn't require building templates in itself
# It uses a template which is already created.
# It will be a robust and efficient way to send email.
def sendTemplatedEmail(TemplateName, NAME, SENDER, RECIPIENT):
    SENDER = NAME + " <" + SENDER + ">"
    client = get_client()
    try:
        response = client.send_templated_email(
            Source=SENDER,
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ]
            },
            Template=TemplateName,
            TemplateData='{ \"REPLACEMENT_TAG_NAME\":\"REPLACEMENT_VALUE\" }'
        )
    except ClientError as e:
        response = e.response['Error']['Message']
        print(e.response['Error']['Message'])

    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    return response

# Simple function which send email, it requires building templates in itself.
def sendEmail(NAME, SENDER, RECIPIENT, SUBJECT, BODY_TEXT):
    client = get_client()
    BODY_HTML = """
        <html>
        <head></head>
        <body>
          <h1> """ + str(BODY_TEXT) + """ </h1>
        </body>
        </html>
    """
    SENDER = NAME + " <" + SENDER + ">"
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        response = e.response['Error']['Message']
        print(e.response['Error']['Message'])

    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    return response

