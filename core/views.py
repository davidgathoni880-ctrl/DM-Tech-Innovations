from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import ContactMessage


def home(request):
    return render(request, "core/home.html")

def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def services(request):
    return render(request, "core/services.html")


def pricing(request):
    return render(request, "core/pricing.html")


def contact(request):
    if request.method == "POST":

        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save message to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

       
        # EMAIL 1: Notification to website owner
       

        email_subject = f"New Contact Message: {subject}"

        text_content = f"""
DavieTechInnovations
New Contact Form Submission

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

This message was submitted through the DavieTechInnovations website.
"""

        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>New Contact Message</title>
</head>

<body style="margin:0; padding:0; background:#f4f6f8;
font-family:Arial, Helvetica, sans-serif;">

    <div style="max-width:650px; margin:30px auto;
    background:#ffffff; border-radius:10px; overflow:hidden;
    box-shadow:0 2px 10px rgba(0,0,0,0.08);">

        <div style="background:#0d6efd; padding:25px; color:white;">
            <h1 style="margin:0; font-size:24px;">
                DavieTechInnovations
            </h1>

            <p style="margin:8px 0 0; font-size:15px;">
                New Contact Form Submission
            </p>
        </div>

        <div style="padding:30px;">

            <h2 style="margin-top:0; color:#222;">
                You have received a new message
            </h2>

            <table style="width:100%; border-collapse:collapse;
            margin-top:20px;">

                <tr>
                    <td style="padding:10px 0; font-weight:bold;">
                        Name:
                    </td>

                    <td style="padding:10px 0;">
                        {name}
                    </td>
                </tr>

                <tr>
                    <td style="padding:10px 0; font-weight:bold;">
                        Email:
                    </td>

                    <td style="padding:10px 0;">
                        <a href="mailto:{email}">
                            {email}
                        </a>
                    </td>
                </tr>

                <tr>
                    <td style="padding:10px 0; font-weight:bold;">
                        Subject:
                    </td>

                    <td style="padding:10px 0;">
                        {subject}
                    </td>
                </tr>

            </table>

            <div style="margin-top:25px; padding:20px;
            background:#f8f9fa; border-left:4px solid #0d6efd;
            border-radius:5px;">

                <h3 style="margin-top:0;">
                    Message
                </h3>

                <p style="white-space:pre-line;
                line-height:1.6; color:#444;">
                    {message}
                </p>

            </div>

            <div style="margin-top:30px; text-align:center;">

                <a href="mailto:{email}?subject=Re: {subject}"
                style="display:inline-block; padding:12px 25px;
                background:#0d6efd; color:white;
                text-decoration:none; border-radius:5px;
                font-weight:bold;">

                    Reply to {name}

                </a>

            </div>

        </div>

        <div style="padding:20px; background:#f1f3f5;
        text-align:center; color:#777; font-size:13px;">

            <p style="margin:0;">
                This notification was generated automatically
                by the DavieTechInnovationss website.
            </p>

        </div>

    </div>

</body>
</html>
"""

        email_message = EmailMultiAlternatives(
            subject=email_subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_NOTIFICATION_EMAIL],
        )

        email_message.attach_alternative(
            html_content,
            "text/html",
        )

        email_message.send(fail_silently=False)

      
        # EMAIL 2: Confirmation to customer
       
        customer_subject = (
            "Thank You for Contacting DavieTechInnovations"
        )

        customer_text = f"""
Dear {name},

Thank you for contacting DavieTechInnovations.

We have successfully received your message and our team
will review it and get back to you as soon as possible.

Your message details:

Subject: {subject}

Message:
{message}

Thank you for choosing DavieTechInnovations.

Best regards,
DavieTechInnovations
ICT & Digital Solutions
"""

        customer_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thank You</title>
</head>

<body style="margin:0; padding:0; background:#f4f6f8;
font-family:Arial, Helvetica, sans-serif;">

    <div style="max-width:650px; margin:30px auto;
    background:#ffffff; border-radius:10px; overflow:hidden;
    box-shadow:0 2px 10px rgba(0,0,0,0.08);">

        <div style="background:#0d6efd; padding:30px;
        color:white; text-align:center;">

            <h1 style="margin:0;">
                DavieTechInnovations
            </h1>

            <p style="margin:8px 0 0;">
                ICT &amp; Digital Solutions
            </p>

        </div>

        <div style="padding:30px;">

            <h2 style="color:#222;">
                Thank You, {name}!
            </h2>

            <p style="color:#444; line-height:1.7;">
                Thank you for contacting
                <strong>DavieTechInnovations</strong>.
                We have successfully received your message.
            </p>

            <p style="color:#444; line-height:1.7;">
                Our team will review your request and get back
                to you as soon as possible.
            </p>

            <div style="margin-top:25px; padding:20px;
            background:#f8f9fa; border-left:4px solid #0d6efd;
            border-radius:5px;">

                <h3 style="margin-top:0;">
                    Your Message
                </h3>

                <p>
                    <strong>Subject:</strong> {subject}
                </p>

                <p style="white-space:pre-line;
                line-height:1.6; color:#444;">
                    {message}
                </p>

            </div>

            <p style="margin-top:30px;
            color:#444; line-height:1.7;">

                We appreciate your interest in our services
                and look forward to assisting you.

            </p>

            <p style="color:#444;">
                Best regards,<br>
                <strong>DavieTechInnovations</strong><br>
                ICT &amp; Digital Solutions
            </p>

        </div>

        <div style="padding:20px; background:#f1f3f5;
        text-align:center; color:#777; font-size:13px;">

            <p style="margin:0;">
                This is an automated confirmation email.
            </p>

            <p style="margin:8px 0 0;">
                DavieTechInnovations 
            </p>

        </div>

    </div>

</body>
</html>
"""

        customer_email = EmailMultiAlternatives(
            subject=customer_subject,
            body=customer_text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )

        customer_email.attach_alternative(
            customer_html,
            "text/html",
        )

        customer_email.send(fail_silently=False)

        # Success message shown on website
        messages.success(
            request,
            "Message sent successfully! We will get back to you soon."
        )

        return redirect("home")

    return render(request, "core/contact.html")