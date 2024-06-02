from django.shortcuts import render
from django.http import JsonResponse
import json
import boto3


def home(request):
    return render(request, 'index.html')


def sign_upload(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        file_name = data['file_name']


        s3_client = boto3.client(
            's3',
            endpoint_url="https://s3.ir-thr-at1.arvanstorage.ir",
            aws_access_key_id='5c719c97-99a3-4e81-940e-a7af8bc5c15a',
            aws_secret_access_key='66ee8a5a1ebae6163a672d87adcda04769d7bf61fbc897765140c49d4a2723ff'
        )

        response = s3_client.generate_presigned_post(
            'upser',
            file_name,
            Fields={
                'acl': 'public-read'
            },
            Conditions=[
                {'acl': 'public-read'}
            ],
            ExpiresIn=3600
        )
        return JsonResponse(response)
