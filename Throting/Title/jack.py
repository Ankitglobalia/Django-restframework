from rest_framework .throttling import UserRateThrottle

class Jackthrottrate(UserRateThrottle):
    scope='Jack'