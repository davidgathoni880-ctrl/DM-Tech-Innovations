

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import json

from core.gemini_service import ask_gemini


def chat_page(request):
    return render(request, "ai_assistant/chat.html")


@require_POST
def chat(request):
    try:
        data = json.loads(request.body)
        message = data.get("message", "").strip()

        if not message:
            return JsonResponse(
                {"error": "Please enter a message."},
                status=400
            )

        response = ask_gemini(message)

        return JsonResponse({
            "response": response
        })

    except Exception as e:
        return JsonResponse(
            {"error": "Sorry, something went wrong. Please try again."},
            status=500
        )