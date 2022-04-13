import requests


def buscar_avatar(usuario):
    """
    Busca o Avatar de um usuario no GitHub
    :param usuario: str com o nome do usuario no GitHub
    :return:str com o nome do avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
