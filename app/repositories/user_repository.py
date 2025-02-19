from sqlalchemy.orm import Session
from app.models.user import User
from app.services.auth_service import hash_password


def create_user_repository(db: Session, user):
    try :
        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "status": "success",
            "data": user
        }
    except Exception as e:
        db.rollback()
        return None

def get_user_by_id_repository(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()

    if user is None:
        raise None

    return {
        "status": "success",
        "data": user
    }

def get_user_by_email_repository(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise None

    return {
        "status": "success",
        "data": user
    }


def recover_password_repository(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        return None

    hashed_password = hash_password(password)
    user.senha = hashed_password

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "status": "success",
        "user": user
    }
