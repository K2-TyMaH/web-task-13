from typing import List
from datetime import datetime, timedelta

from sqlalchemy import or_, and_
from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, user: User, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.user_id == user.id).offset(skip).limit(limit).all()


async def get_contact_by_id(contact_id: int, user: User, db: Session) -> Contact:
    return db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()


async def get_contacts_by_info(information: str, user: User, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.user_id == user.id).filter(or_(Contact.firstname == information,
                                                                           Contact.lastname == information,
                                                                           Contact.email == information, )).all()


async def get_contacts_7days_birthdays(user: User, db: Session) -> List[Contact]:
    contacts = db.query(Contact).filter(Contact.user_id == user.id).all()
    current_date = datetime.now()
    end_date = current_date + timedelta(days=7)
    birthdays_7days_list = []
    for contact in contacts:
        this_year_birthday = contact.birthday.replace(year=current_date.year)
        if current_date < this_year_birthday <= end_date:
            birthdays_7days_list.append(contact)
    return birthdays_7days_list


async def create_contact(body: ContactModel, user: User, db: Session) -> Contact:
    contact = Contact(
        firstname=body.firstname,
        lastname=body.lastname,
        email=body.email,
        phone=body.phone,
        birthday=body.birthday,
        user_id=user.id
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactModel, user: User, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    if contact:
        contact.firstname = body.firstname
        contact.lastname = body.lastname
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        db.commit()
    return contact


async def remove_contact(contact_id: int, user: User, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact
