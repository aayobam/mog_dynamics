from django.core.mail import EmailMessage, send_mail



# send mail shipping/logistics status notification to clients.
class LogisticNotification():
    def __init__(self, email_subject, email_body, sender_email, receiver_email, reply_to):
        self.email_subject = email_subject
        self.email_body = email_body
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.reply_to = reply_to

    def mail_user(self):
        msg = EmailMessage(
            subject=self.email_subject,
            body=self.email_body,
            from_email=self.sender_email,
            to=[str(self.receiver_email)],
            reply_to=[self.reply_to,],
        )
        msg.send(fail_silently=True)
        return True

    def mail_admin(self):
        msg = EmailMessage(
            subject=self.email_subject,
            body=self.email_body,
            from_email=self.sender_email,
            to=[str(self.receiver_email)],
            reply_to=[self.reply_to,],
        )
        msg.send(fail_silently=True)
        return True


# send mail notification to users and admins after successful subscription
class ShippingNotification():
    def __init__(self, email_subject, email_body, sender_email, receiver_email):
        self.email_subject = email_subject
        self.email_body = email_body
        self.sender_email = sender_email
        self.receiver_email = receiver_email

    def mail_user(self):
        send_mail(
            subject=self.email_subject,
            message=self.email_body,
            from_email=self.sender_email,
            recipient_list=[self.receiver_email,],
            fail_silently=False,
        )
        return True
        
    def mail_admin(self):
        send_mail(
            subject=self.email_subject,
            message=self.email_body,
            from_email=self.sender_email,
            recipient_list=[self.receiver_email,],
            fail_silently=False,
        )
        return True