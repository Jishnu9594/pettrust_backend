# utils.py

import csv
from io import StringIO
from django.core.mail import send_mail
from django.template.loader import render_to_string
from threading import Thread
import logging


def generate_leads_spreadsheet(lead_data_list):
    """
    Generate CSV spreadsheet from list of lead data.
    """
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=lead_data_list[0].keys())
    writer.writeheader()
    writer.writerows(lead_data_list)
    return output.getvalue()


logger = logging.getLogger(__name__)

def async_send_mail(subject, template, context, recipient_list):
    def send():
        try:
            # Render the email content with the provided template and context
            email_body = render_to_string(template, {'data': context})

            send_mail(
                subject=subject,
                message='',  # Optional plain text version
                html_message=email_body,  # HTML content
                from_email='pettrustmarketing@gmail.com',  # Replace with your sender's email
                recipient_list=recipient_list,
            )
            logger.info(f"Email successfully sent to: {recipient_list}")
        except Exception as e:
            logger.error(f"Failed to send email to {recipient_list}: {e}", exc_info=True)

    # Start the email sending in a separate thread
    Thread(target=send).start()
