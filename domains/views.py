from .dnstwist import DomainFuzz
from base.models import Company
from django.shortcuts import render

def domains(request, company_id):

    company = Company.objects.get(id=company_id)
    service = 'reputation_check'
    name = company.name
    domain = company.domain
    fuzz = DomainFuzz(domain)
    fuzz.generate()
    for o in fuzz.domains:
        domain_name = o['domain-name']
    print(fuzz.domains)
    print(len(fuzz.domains))

    count = len(fuzz.domains)

    return render(request, 'reputation.html', {
        'fuzz': fuzz.domains,
        'domain': domain,
        'count': count,
        'name': name,
        'service': service,
    })