from fastapi import FastAPI, Path, Query, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from uuid import uuid4, UUID


# FastAPI uygulamasını oluştur
app = FastAPI()


from fastapi import FastAPI, Form

# Firebase'e bağlan
import firebase_admin
from firebase_admin import credentials,firestore
credentialData = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(credentialData)

firestoreDb = firestore.client()

# Todo modeli için güncelleme yapılacak alanları belirt
class TodoUpdate(BaseModel):
    description: Optional[str] = Field(min_length=3, max_length=200)
    short_description: Optional[str] 
    tags: Optional[List[str]] 
    title: Optional[List[str]] 


todoList = []

# Ana sayfa için bir GET endpointi tanımla
@app.get("/", summary="Say Greeting")
def say_greeting():
    return "Giriş"

# Yeni bir Todo kaydı oluşturmak için bir POST endpointi tanımla
@app.post("/todos", summary="Create a Todo record", tags=["Todo"])
def createTodo(description: str = Form(...), short_description: str = Form(...), tags: str = Form(...), title: str = Form(...)):
    if not (description and short_description and tags and title):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All fields are required")

    if len(description) < 3 or len(short_description) < 3 or len(tags) < 3 or len(title) < 3:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All fields must be at least 3 characters long")

    if not (description.isalpha() and short_description.isalpha() and tags.isalpha() and title.isalpha()):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All fields must be strings")

    todo_data = {
        'description': description,
        'short_description': short_description,
        'tags': tags.split(','),  # Assumes tags are comma-separated
        'title': title
    }
    todoOut = dict(id=len(todoList)+1, **todo_data)
    todoList.append(todoOut)
    firestoreDb.collection('data').add(todo_data)
    return {"data":  todoOut}   
 
# Tüm Todo kayıtlarını almak için bir GET endpointi tanımla 
@app.get("/todos/all", summary="Get all Todo records", tags=["Todo"])
def getAllTodos():
    todos_ref = firestoreDb.collection('data')
    todos = [doc.to_dict() for doc in todos_ref.stream()]
    return {"data": todos}
    
# Belirli bir todo kaydını almak için bir GET endpointi tanımla 
@app.get("/todos/{doc_id}", summary="Bir Todo Kaydını Al", tags=["Todo"])
def getTodo(doc_id: str):
    doc_ref = firestoreDb.collection('data').document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        todo_data = doc.to_dict()
        return {"data": todo_data}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": f"{doc_id} numaralı belge bulunamadı"})

 
# Belirli bir Todo kaydını silmek için bir DELETE endpointi tanımla 
@app.delete("/todos/{doc_id}", summary="Delete a Todo record", tags=["Todo"])
def deleteTodo(doc_id: str):
    doc_ref = firestoreDb.collection('data').document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.delete()
        return {"message": f"Document with ID {doc_id} deleted successfully"}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": f"Document with ID {doc_id} not found"})
        
 # Belirli bir Todo kaydını güncellemek için bir PUT endpointi tanımla       
@app.put("/todos/{doc_id}", summary="Update a Todo record", tags=["Todo"])
def updateTodo(doc_id: str, todo_update: TodoUpdate):
    doc_ref = firestoreDb.collection('data').document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.update(todo_update.dict())
        return {"message": f"Document with ID {doc_id} updated successfully"}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": f"Document with ID {doc_id} not found"})