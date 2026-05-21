import requests

async def list_me(acess_token: str):
    r = requests.request(
        method="GET",
        headers={
            "Authorization": f"Bearer {acess_token}"
        },
        url="http://127.0.0.1:8000/user/me"
    )

    print(r.json())
