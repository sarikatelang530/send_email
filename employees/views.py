
from django.http import JsonResponse
from django.template.loader import render_to_string
# from django.core.mail import send_mail
from datetime import date
from .models import Employee

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_birthday_emails(request):
    # Get the current month and day
    global response
    today = date.today()
    current_month = today.month
    current_day = today.day

    employees = Employee.objects.filter(birthday__month=current_month, birthday__day=current_day)

    if employees:
        for employee in employees:
            # Create and send birthday email using a template
            subject = 'Happy Birthday!'
            message = render_to_string('birthday.html', {'employee': employee})
            from_email = 'xyz@gmail.com' # Your email address
            recipient_list = [employee.email]
            response = send_mail(subject, message, from_email, recipient_list)

        return JsonResponse({'response': response})
    else:
        print("no events are scheduled for the current period")
        return JsonResponse({'message': 'no events are scheduled for the current period'})


def send_work_anniversary_emails(request):
    global response
    # Get the current month and day
    today = date.today()
    current_month = today.month
    current_day = today.day

    employees = Employee.objects.filter(work_anniversary__month=current_month, work_anniversary__day=current_day)

    if employees:
        for employee in employees:
            # Create and send work anniversary email using a template
            subject = 'Work Anniversary!'
            message = render_to_string('workAnniversary.html', {'employee': employee})
            from_email = 'xyz@gmail.com' # Your email address
            recipient_list = [employee.email]
            response = send_mail(subject, message, from_email, recipient_list)

        return JsonResponse({'response': response})
    else:
        print("no events are scheduled for the current period")
        return JsonResponse({'message': 'no events are scheduled for the current period'})


def send_mail(subject, message, from_email, recipient_list):
    # Email server settings
    smtp_server = "smtp.gmail.com"  # Update with your SMTP server address
    smtp_port = 587  # Update with the appropriate port for your SMTP server
    smtp_username = 'xyz@gmail.com'  # Your email address
    smtp_password = 'obziilfwhuxuodht'  # Your email password or app-specific password

    # Sender and recipient email addresses
    recipient_email = recipient_list

    for receiver_email in recipient_email:

        # Create the MIME message
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "html"))

        # Connect to the SMTP server and send the email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Enable TLS encryption
                server.login(smtp_username, smtp_password)
                server.sendmail(from_email, receiver_email, msg.as_string())
            print(f"Email sent successfully to {receiver_email}.")
            return f"Email sent successfully to {receiver_email}."
        except Exception as e:
            print(f"Email could not be sent: {e}")
            return f"Email could not be sent: {e}, recipient_email: {receiver_email}"


