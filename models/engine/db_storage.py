#!/usr/bin/python3
"""
Module the defines the new class engine 'DBStorage'.
"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.user import User
from os import getenv
import models.place
import models.state

class DBStorage:
    """
    New storage engine.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Public instance method to create the engine.
        """
        bnb_user = getenv("HBNB_MYSQL_USER")
        bnb_pwd = getenv("HBNB_MYSQL_PWD")
        bnb_host = getenv("HBNB_MYSQL_HOST")
        bnb_db = getenv("HBNB_MYSQL_DB")
        bnb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
                f"mysql+mysqldb://{bnb_user}:{bnb_pwd}@{bnb_host}/{bnb_db}",
                pool_pre_ping=True,
        )

        if bnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None, id=None):
        """
        Query on all the objects of the current database session.
        """
        Allcls = [User, Place, Amenity, City, State, Review]
        res = {}

        if cls is not None:
            if id is not None:
                obj = self.__session.query(cls).get(id)
                if obj is not None:
                    clsName = obj.__class__.__name__
                    keyName = clsName + "." + str(obj.id)
                    res[keyName] = obj
            else:
                for obj in self.__session.query(cls).all():
                    clsName = obj.__class__.__name__
                    keyName = clsName + "." + str(obj.id)
                    res[keyName] = obj
        else:
            for clss in Allcls:
                if id is not None:
                    obj = self.__session.query(clss).get(id)
                    if obj is not None:
                        clsName = obj.__class__.__name__
                        keyName = clsName + "." + str(obj.id)
                        res[keyName] = obj
                else:
                    for obj in self.__session.query(clss).all():
                        clsName = obj.__class__.__name__
                        keyName = clsName + "." + str(obj.id)
                        res[keyName] = obj
        return res

    def reload(self):
        """
        Reloads the current database session.
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
                sessionmaker(
                    bind=self.__engine,
                    expire_on_commit=False
                )
        )
        self.__session = Session()

    def new(self, obj):
        """
        Adds a new objects to the current database session.
        """
        if obj:
            self.__session.add(obj)

    def search(self, cls, id):
        """
        Searches the current database session.
        """
        data = self.all(cls)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """
        Closes the current database session.
        """
        self.__session.close()
