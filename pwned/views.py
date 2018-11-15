from django.shortcuts import render

import requests
from base.models import Company
import json


def pwned_account(request, company_id):

    service = 'breachedaccount'
    company = Company.objects.get(id=company_id)
    email = company.email
    name = company.name
    headers = {'api-version': "2", 'User-Agent': "pupleproto"}
    response = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/%s' %email, headers=headers)
    # response = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/%s' %service)
    status_code = response.status_code
    print(status_code)
    breach_date = ""
    added_date = ""
    modified_date = ""
    pwn_count = ""
    description = ""
    encrypted = ""
    breaches = []
    if status_code != 404:
        have_i_been_pwned_response = json.loads(response.content.decode("utf-8"))

        pwned = response.content
        content_type = response.headers['content-type']
        for breach in have_i_been_pwned_response:
            item = {
                'name': breach['Name'],
                'date': breach['BreachDate'],
                'description': breach['Description']
            }
            breaches.append(item)
        print(breaches)
        return render(request, 'pwned.html', {
            'name': name,
            'service': service,
            'email': email,
            'status_code': status_code,
            'content_type': content_type,
            'breach_date': breach_date,
            'added_date': added_date,
            'modified_date': modified_date,
            'pwn_count': pwn_count,
            'description': description,
            'encrypted': encrypted,
            'pwned': pwned,
            'breaches': breaches
        })
    else:
        return render(request, 'not_pwned.html', {
            'name': name,
            'service': service,
            'email': email,
            'status_code': status_code
        })