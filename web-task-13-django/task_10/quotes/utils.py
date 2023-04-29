from pymongo import MongoClient


def get_mongodb():
    client = MongoClient('mongodb+srv://tymah:13572468@mycluster.6ekshk8.mongodb.net/?retryWrites=true&w=majority')
    db = client.django_task_10
    return db




