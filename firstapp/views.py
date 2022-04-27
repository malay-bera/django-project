from django.shortcuts import render
from firstapp.models import Country, State
from rest_framework.response import Response
from rest_framework import views
# Create your views here.
class ABC(views.APIView):
    def get(self, request):
        return Response('Hi....')

class InsertCountry(views.APIView):
    def post(self, request):
        request_data=request.data
        country_name=request_data['country_name']
        country_code=request_data['country_code']
        Country.objects.create(country_name=country_name,country_code=country_code)
        res={
            'status':1,
            'message':"Country Insert Sucessfully"
        }
        return Response(res)


class UpdateCountry(views.APIView):
    def put(self, request,id):
        request_data=request.data
        country_id=id
        country_name=request_data['country_name']
        country_code=request_data['country_code']
        Country.objects.filter(id=country_id).update(country_name=country_name,country_code=country_code)
        res={
            'status':1,
            'message':"Country Update Sucessfully"
        }
        return Response(res)

class DeleteCountry(views.APIView):
    def delete(self, request,id):
        request_data=request.data
        country_id=id
        Country.objects.filter(id=country_id).delete()
        res={
            'status':1,
            'message':"Country Delete Sucessfully"
        }
        return Response(res)


class GetAllCountry(views.APIView):
    def get(self, request):
        data=Country.objects.all()
        res=[]
        for each_country in data:
            res.append({
                'id':each_country.id,
                'country_name':each_country.country_name,
                'country_code':each_country.country_code,
            })
        return Response(res)
class InsertState(views.APIView):
    def post(self, request):
        request_data=request.data
        state_name=request_data['state_name']
        state_code=request_data['state_code']
        country_id=request_data['country_id']
        State.objects.create(state_name=state_name,state_code=state_code,country_id=country_id)
        res={
            'status':1,
            'message':"State Insert Sucessfully"
        }
        return Response(res)


class UpdateState(views.APIView):
    def put(self, request,id):
        request_data=request.data
        state_id=id
        state_name=request_data['state_name']
        state_code=request_data['state_code']
        country_id=request_data['country_id']
        State.objects.filter(id=state_id).update(state_name=state_name,state_code=state_code,country_id=country_id)
        res={
            'status':1,
            'message':"State Update Sucessfully"
        }
        return Response(res)

class DeleteState(views.APIView):
    def delete(self, request,id):
        request_data=request.data
        state_id=id
        State.objects.filter(id=state_id).delete()
        res={
            'status':1,
            'message':"State Delete Sucessfully"
        }
        return Response(res)

class GetCountryWiseState(views.APIView):
    def get(self, request,id):
        data=Country.objects.filter(id=id).first()
        res=[]
        state_data=State.objects.filter(country_id=id)
        for each_state in state_data:
            res.append({
                'id':each_state.id,
                'state_name':each_state.state_name,
                'state_code':each_state.state_code,
            })
        array={
            'country_id':data.id,
            'country_name':data.country_name,
            'country_code':data.country_code,
            'state':res
        }
        return Response(array)