from django.shortcuts import render
from rpc4django import rpcmethod

# Create your views here.


def home_page(request):
    return render(request, 'home_page.html')


@rpcmethod(name='license_server.license_api', signature=['str'])
def license_api(test_args):
    return test_args
