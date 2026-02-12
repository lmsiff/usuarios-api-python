from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate):
        new_user = User(
            name=user.name,
            email=user.email,
            age=user.age
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def find_all(self):
        return self.db.query(User).all()
