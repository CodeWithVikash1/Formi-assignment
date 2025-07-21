from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils.data_loader import load_all_data

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
    
@csrf_exempt
def retrieve_info(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            intent = data.get('intent')
            all_data = load_all_data()

            if intent == "room_availability":
                return JsonResponse({"rooms": all_data["rooms"][:5]})  # 5 rooms for sample

            elif intent == "general_rules":
                return JsonResponse({"rules": all_data["rules"]})

            elif intent == "staff_info":
                return JsonResponse({"queries": all_data["queries"]})

            elif intent == "pricing":
                return JsonResponse({"pricing": all_data["pricing"]})

            else:
                return JsonResponse({"message": "Intent not recognized"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)