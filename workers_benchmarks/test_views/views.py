import json
from . import r as redis
from . import session
from django.http.response import HttpResponse
from django.db import transaction
from test_views.models import A, B, C, D, E


def __create_simple_data(n):
    with transaction.atomic():
        e = E(n=n)
        e.save()
        d = D(e=e)
        d.save()
        c = C(d=d)
        c.save()
        b = B(c=c)
        b.save()
        a = A(b=b)
        a.save()


def __session_request(delay):
    r = session.get("http://httpbin.org/delay/{}".format(delay))
    return r


def simple_json(request):
    return HttpResponse(json.dumps({"a": "b"}))


def simple_requests(request, n=0):
    r = __session_request(n)
    return HttpResponse(status=r.status_code)


def create_data(request, n=0):
    __create_simple_data(n)
    return HttpResponse(json.dumps(n))


def read_data(request):
    pk = E.objects.all()[0].pk
    return HttpResponse()


def create_data_in_redis(request, n=0):
    redis.set("a", n)
    return HttpResponse(status=200)


def read_data_in_redis(request, k="a"):
    return HttpResponse(redis.get("a"))


def request_and_read_redis(request):
    r = __session_request(0)
    return HttpResponse(redis.get("a"))


def read_redis_and_request(request):
    rd = redis.get("a")
    r = __session_request(0)
    return HttpResponse(rd)


def create_data_and_read_redis(request):
    __create_simple_data(0)
    return HttpResponse(redis.get("a"))


def read_redis_and_create_data(request):
    rd = redis.get("a")
    __create_simple_data(0)
    return HttpResponse(rd)
