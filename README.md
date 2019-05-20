# Practical things:
1. Send an Email Through Amazon SES Using an AWS SDK
To send an email using the Amazon SES API, you can use the Query interface directly, or you can use an AWS SDK to handle low-level details such as assembling and parsing HTTP requests and responses. 

2. Setup for python
Install the required package for python
```
pip3 install boto3
```

Before moving to send email from sender to recipient, we need to first verify the emails.

How to verify emails?
    • Sign in to the AWS Management Console and open the Amazon SES console at https://console.aws.amazon.com/ses/. 
    • In the console, use the region selector to choose the AWS Region where want to verify the email address.

After verifying emails you need to configure few things.
1. Install cli of aws – pip install awscli
2. Configure settings by – aws configure
3. It will ask for keys, to get keys you have to go to “my security credentials” in the dropdown menue of aws profile. 
It will ask for default region also, go for what you will be adding in the ses.py file which we will be using to send the emails.

Follow out this link for writing a file for sending emails:
https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html
with following changes + commenting the configurationSet variable.
```
SENDER = "Anshul Warade <warade.anshul@gmail.com>"
RECIPIENT = "anshul@brightmoney.co"
# Following region should be the same when you configured your credentials.
AWS_REGION = "us-west-2"
```
3. Using the information above, create a library (seslib)
Usage:
```
seslib.sendEmail(name, sender, recipient, subject, body_text)
```
