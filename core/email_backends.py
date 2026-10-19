
import json
import logging
import os
from email.utils import parseaddr
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)


class BrevoEmailBackend(BaseEmailBackend):
    """Send Django emails through the Brevo transactional email API."""

    api_url = "https://api.brevo.com/v3/smtp/email"

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        api_key = os.getenv("BREVO_API_KEY")
        if not api_key:
            raise ImproperlyConfigured(
                "BREVO_API_KEY is not configured."
            )

        sent_count = 0

        for message in email_messages:
            sender_name, sender_email = parseaddr(
                message.from_email or settings.DEFAULT_FROM_EMAIL
            )

            if not sender_email:
                raise ImproperlyConfigured(
                    "DEFAULT_FROM_EMAIL must contain a valid email address."
                )

            payload = {
                "sender": {
                    "name": sender_name or "DavieTech Innovations",
                    "email": sender_email,
                },
                "to": [{"email": address} for address in message.recipients()],
                "subject": message.subject or "",
                "textContent": message.body or "",
            }

            for content, mimetype in getattr(message, "alternatives", []):
                if mimetype == "text/html":
                    payload["htmlContent"] = content
                    break

            request = Request(
                self.api_url,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "accept": "application/json",
                    "content-type": "application/json",
                    "api-key": api_key,
                },
                method="POST",
            )

            try:
                with urlopen(request, timeout=15) as response:
                    if 200 <= response.status < 300:
                        sent_count += 1
                    else:
                        raise RuntimeError(
                            f"Brevo returned HTTP {response.status}."
                        )

            except HTTPError as exc:
                error_body = exc.read().decode("utf-8", errors="replace")
                logger.error(
                    "Brevo rejected an email: HTTP %s: %s",
                    exc.code,
                    error_body,
                )
                raise

            except URLError as exc:
                logger.error("Could not connect to Brevo: %s", exc.reason)
                raise

        return sent_count
