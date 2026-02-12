from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate

router = APIRouter(prefix="/api/users")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    repository.create(user)
    return {"message": "Usuário cadastrado com sucesso!"}

@router.get("")
def list_users(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    users = repository.find_all()
    return {
        "data": users,
        "count": len(users)
    }
