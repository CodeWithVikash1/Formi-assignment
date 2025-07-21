from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return JsonResponse({"message": "Formi API Working ✅"})

@csrf_exempt
def classify_query(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            query = data.get("query", "").lower()
            if "availability" in query or "available" in query:
                return JsonResponse({"intent": "room_availability"})
            elif "cancel" in query or "cancellation" in query:
                return JsonResponse({"intent": "cancellation_policy"})
            elif "price" in query or "cost" in query:
                return JsonResponse({"intent": "pricing_info"})
            else:
                return JsonResponse({"intent": "general_query"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)