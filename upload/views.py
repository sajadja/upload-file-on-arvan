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
            aws_access_key_id='c6bdd3a6-cb85-4a30-8c02-512d3869e8fe',
            aws_secret_access_key='5ec861e032e2f377d243cf2a339d9c0b167cd623d55f98999fe92e0bb4409020'
        )

        response = s3_client.generate_presigned_post(
            'test-upload-file',
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
