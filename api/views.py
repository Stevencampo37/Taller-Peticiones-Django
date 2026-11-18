from django.views import View
from django.http import JsonResponse


class EndpointView(View):

    def get(self, request):
        return JsonResponse({
            "metodo": "GET",
            "crud": "READ",
            "mensaje": "Consulta realizada"
        })

    def post(self, request):
        return JsonResponse({
            "metodo": "POST",
            "crud": "CREATE",
            "mensaje": "Registro creado"
        })

    def put(self, request, id):
        return JsonResponse({
            "metodo": "PUT",
            "crud": "UPDATE",
            "mensaje": f"Registro {id} actualizado"
        })

    def delete(self, request, id):
        return JsonResponse({
            "metodo": "DELETE",
            "crud": "DELETE",
            "mensaje": f"Registro {id} eliminado"
        })