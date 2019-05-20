import seslib
import json

# Required details to send email
name = "Anshul Warade"
sender = "warade.anshul@gmail.com"
recipient = "anshul@brightmoney.co"
subject = "A dummy email from AWS SES"
body_text = "Hey, how you doin?"

# Things required to create a template, I skipped TextPart
# TODO: See if textpart is important or not.
TemplateName = 'Welcome_template'
SubjectPart = "Welcome to the Bright Customer family {name}!".format(name=name)
HtmlPart = """
		<html>
        <head></head>
        <body>
          <p> Hello {name}, </p>
          <p> Thank you for believing in us, 
          	  By default AWS SES only provides us a sandbox environment in order to prevent spamming. 
          	  In this you will only be able to send and receive emails from verified email addresses.
          </p>
        </body>
        </html>
""".format(name = name)

# response = seslib.sendEmail(name, sender, recipient, subject, body_text)
# print(json.dumps(response, indent=2))

# response = seslib.createTemplate(TemplateName, SubjectPart, HtmlPart, None)
# print(json.dumps(response, indent=2))

# response = seslib.deleteTemplate(TemplateName)
# print(json.dumps(response, indent=2))

# response = seslib.updateTemplate(TemplateName, SubjectPart, HtmlPart, None)
# print(json.dumps(response, indent=2))

# response = seslib.getTemplates()
# print(json.dumps(response, indent=2))

response = seslib.sendTemplatedEmail(TemplateName, name, sender, recipient)
print(json.dumps(response, indent=2))