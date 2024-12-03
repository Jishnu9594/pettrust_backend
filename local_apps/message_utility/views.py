from .task import single_send_mail, multiple_send_mail
from django.template.loader import render_to_string

def mail_handler(mail_type=None, to=None, subject=None, data=None, template=None, cc=None, bcc=None, reply_to=None):
    if to and subject and data and template:
        # Render the message from the template
        message = render_to_string(template, context={'data': data})

        if mail_type == 'single':
            # Send a single email
            send = single_send_mail.delay(subject=subject, message=message, to_list=to, cc_list=cc, bcc_list=bcc, reply_to=reply_to)
            return send
        elif mail_type == 'multiple':
            # Send multiple emails
            send = multiple_send_mail.delay(subject=subject, message=message, to_list=to, cc_list=cc, bcc_list=bcc, reply_to=reply_to)
            return send
        else:
            return False
    else:
        print('Email view failed due to missing parameters.')
        return False
