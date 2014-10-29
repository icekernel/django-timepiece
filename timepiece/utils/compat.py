from django import VERSION as DJANGO_VERSION
from django.db import transaction

if DJANGO_VERSION[0] > 1 or (DJANGO_VERSION[0]==1 and DJANGO_VERSION[1] >= 7):

    from django.http import JsonResponse
    atomic = transaction.atomic

else:
    import json
    from django.http import HttpResponse

    def JsonResponse(data, encoder=None, **kwargs):
        return HttpResponse(json.dumps(data, cls=encoder),
                            mimetype='application/json', **kwargs)

    atomic = transaction.commit_on_success
