from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from companies.models import Company
from companies.models import Team
from companies.serializers import CompanySerializer
from companies.serializers import TeamSerializer

class TeamView(APIView):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, format=None, **kwargs):
        #antes pegar o company id para verificar se o time pertence aquela empresa
        if kwargs.get('company_id'):
        	try:
        		company = Company.objects.get(id=kwargs['company_id'])
        	except ObjectDoesNotExist:
                return Response({"error": "could not find team"}    , status=400)	
        if kwargs.get('team_id'):
            try:
            	#verificar aqui se esse team pertence a company?
                team = Team.objects.get(id=kwargs['team_id'])
                team_data = TeamSerializer(team)
                return Response(team_data.data)
            except ObjectDoesNotExist:
                return Response({"error": "could not find team"}    , status=400)
        else:
            all_teams = Team.objects.all()
            all_teams_serialized = TeamSerializer(all_teams, many=True)
            return Response(all_teams_serialized.data)

    def post(self, request, format=None, **kwargs):
        response = Response()
        new_team = Team(**kwargs)
        new_team.save()

        if new_team:
            response.status_code = 201
        else:
            response.status_code = 400
        return response