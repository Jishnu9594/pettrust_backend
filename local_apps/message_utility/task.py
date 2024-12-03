from celery import shared_task
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.core import mail

connection = mail.get_connection()


@shared_task(name='send single email using celery')
def single_send_mail(subject=None, message=None, to_list=None, cc_list=None, bcc_list=None, reply_to=None):
    s_email = EmailMessage(
        subject=subject if subject else 'No Subject Line',
        body=message if message else 'No message',
        from_email='noreply@jicitsolution.com',
        to=to_list if to_list else ['noreply@jicitsolution.com'],
        cc=cc_list if cc_list else None,
        bcc=bcc_list if bcc_list else None,
        reply_to=reply_to if reply_to else ['noreply@jicitsolution.com'],
    )
    s_email.content_subtype = "html"
    s_email.send()
    return True


@shared_task(name='send multiple email using celery')
def multiple_send_mail(subject=None, message=None, to_list=None, cc_list=None, bcc_list=None, reply_to=None):
    try:
        if len(to_list) < 99:
            connection.open()
            email_compose_list = []
            check = 0
            for m in to_list:
                if m:
                    m_email = EmailMultiAlternatives(
                        subject=subject if subject else 'No Subject Line',
                        body=message if message else 'No message',
                        from_email='noreply@jicitsolution.com',
                        to=[m],
                        cc=cc_list if cc_list and check == 0 else None,
                        bcc=bcc_list if bcc_list and check == 0 else None,
                        reply_to=reply_to if reply_to else ['noreply@jicitsolution.com'],
                    )
                    m_email.content_subtype = "html"
                    email_compose_list.append(m_email)
                    check += 1
                    # m_email.send()
            connection.send_messages(email_compose_list)
            connection.close()
            return True

    except Exception as e:
        print(e)
        return False
