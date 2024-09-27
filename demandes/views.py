from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Demande
import json


@csrf_exempt  # Permet les requêtes POST sans token CSRF (uniquement pour les API)
def create_demande_api(request):
    if request.method == 'POST':
        try:
            # Extraction des données JSON de la requête
            data = json.loads(request.body)

            # Récupération des données du corps de la requête
            selected_option = data.get('selected_option')
            moto_option = data.get('moto_option', '')
            annulation = data.get('annulation', False)
            purchase_date = data.get('purchase_date')
            project_purchase = data.get('project_purchase', False)
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            phone = data.get('phone')
            address = data.get('address')
            postal_code = data.get('postal_code')
            city = data.get('city')
            parking_address = data.get('parking_address', False)
            birth_date = data.get('birth_date')
            vehicle_brand = data.get('vehicle_brand')
            engine_capacity = data.get('engine_capacity')
            model = data.get('model', '')
            type = data.get('type', '')
            registration_number = data.get('registration_number', '')
            first_registration_date = data.get('first_registration_date')
            acquisition_date = data.get('acquisition_date')

            # Créer une nouvelle demande et enregistrer dans la base de données
            demande = Demande.objects.create(
                selected_option=selected_option,
                moto_option=moto_option,
                annulation=annulation,
                purchase_date=purchase_date,
                project_purchase=project_purchase,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                postal_code=postal_code,
                city=city,
                parking_address=parking_address,
                birth_date=birth_date,
                vehicle_brand=vehicle_brand,
                engine_capacity=engine_capacity,
                model=model,
                type=type,
                registration_number=registration_number,
                first_registration_date=first_registration_date,
                acquisition_date=acquisition_date
            )

            # Si tout se passe bien, renvoyer une réponse de succès
            return JsonResponse({'success': True, 'message': 'Demande créée avec succès!'}, status=201)

        except json.JSONDecodeError:
            # Gérer les erreurs de décodage JSON
            return JsonResponse({'success': False, 'message': 'Données JSON invalides'}, status=400)
        except Exception as e:
            # Gérer toute autre exception
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    # Si la requête n'est pas POST, renvoyer une erreur
    return JsonResponse({'success': False, 'message': 'Méthode non autorisée'}, status=405)
