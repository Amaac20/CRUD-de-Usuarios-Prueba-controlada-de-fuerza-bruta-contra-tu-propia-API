from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel
from typing import Optional

app = FastAPI()

class User(SQLModel):
    id: int
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True

db_users = [
    User(id=1, username="Amanda", password="Cherry", is_active=True),
    User(id=2, username="Mateo", password="mosh2", is_active=True),
    User(id=3, username="Julian", password="2468", is_active=False),
    User(id=4, username= "Evangeline", password= "osiris", is_active= True)]
current_id = 5

@app.post("/users")
def create_user(user: User):
    global current_id

    for u in db_users:
        if u.username == user.username:
            return {"error": "El username ya existe"}

    user.id = current_id
    current_id += 1

    db_users.append(user)
    return user

@app.get("/users")
def get_users():
    return db_users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in db_users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in db_users:
        if user.id == user_id:
            user.username = updated_user.username
            user.email = updated_user.email
            user.is_active = updated_user.is_active
            return user

    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in db_users:
        if user.id == user_id:
            db_users.remove(user) 
            return {"mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.post("/login")
def login(user: User):
    for u in db_users:
        if u.username == user.username and u.password == user.password:
            return {"mensaje": "Login exitoso"}

    return {"mensaje": "Login fallido"}