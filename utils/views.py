# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
import requests

class ip(View):
    def get(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
    	    hip =  request.META['HTTP_X_FORWARDED_FOR'].split(",")[0]
        else:
            hip = request.META['REMOTE_ADDR']
        ip_response = requests.get(f'http://www.cip.cc/{hip}', headers={'user-agent': 'curl'})
        #ip_response = requests.get(f'http://ip.taobao.com/service/getIpInfo.php?ip={hip}')
        #ip_info = ip_response.json()
        #if ip_info['code'] == 0:
            #tip,tcountry,tregion,tcity,tisp = ip_info['data']['ip'],ip_info['data']['country'],ip_info['data']['region'],ip_info['data']['city'],ip_info['data']['isp']
            #return HttpResponse(f'{tip},{tcountry},{tregion},{tcity},{tisp}\n')
        #else:
        return HttpResponse(ip_response.text)
