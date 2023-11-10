import requests


class Auth:
    def getUser(request):
        return requests.get(
            f'http://172.16.239.2:8000/users/user', cookies={"jwt": request.COOKIES.get('jwt')})
