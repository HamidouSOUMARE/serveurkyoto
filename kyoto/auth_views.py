from dj_rest_auth.views import LoginView

class CustomLoginView(LoginView):
    def get_response(self):
        response_data = super().get_response()
        # Vous pouvez ajouter des données supplémentaires à la réponse ici si nécessaire
        return response_data
