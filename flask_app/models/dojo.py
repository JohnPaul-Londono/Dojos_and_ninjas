from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninjas

class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls): #not pulling data because only retrieving information.
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninja").query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(Dojos(dojo))
        return dojos

    @classmethod 
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL("dojos_and_ninja").query_db(query,data)


    @classmethod
    def show_ninja(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"#WHERE dojos.id = %(id)s;
        all_ninjas = connectToMySQL("dojos_and_ninja").query_db(query,data)
        dojo = cls(all_ninjas[0])
        for dojo_ninjas in all_ninjas:
            new_data = {
                "id": dojo_ninjas["ninjas.id"],
                "first_name": dojo_ninjas["first_name"],
                "last_name": dojo_ninjas["last_name"],
                "age": dojo_ninjas["age"],
                "created_at": dojo_ninjas["ninjas.created_at"],
                "updated_at": dojo_ninjas["ninjas.updated_at"],
                "dojo_id": dojo_ninjas["dojo_id"]
            }
            dojo.ninjas.append(Ninjas(new_data))
        return dojo