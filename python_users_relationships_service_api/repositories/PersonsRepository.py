from neo4j import GraphDatabase
from db_config import driver

class PersonsRepository(object):

    def add_person(self, id, name, email, login, password):
        #Añade un nodo nuevo a la base de datos
        with driver.session() as session:
            result = session.run("CREATE (n:Person{id:$_id, name:$_name, email:$_email, login:$_login, password:$_password})"
                                 ,_id=id, _name=name, _email=email, _login=login, _password=password).value()
            return result

    def get_all_persons(self):
        #Consulta todos los nodos de la base de datos
        with driver.session() as session:
            result = session.run("MATCH (n:Person) RETURN n.id as id LIMIT 25").data()
            return result

    def get_person_by_name(self, name):
        #Consulta un nodo por su nombre, actualmente no se debe usar
        with driver.session() as session:
            result = session.run("MATCH (n:Person{name:'" +name+ "'})").data()
            return result

    def get_friends(self, personId):
        #Consulta los amigos de un nodo
        with driver.session() as session:
            result = session.run("MATCH (n:Person{id:$id})-[:FRIEND]->(fof) RETURN fof.id as id", id=int(personId)).data()
            print(str(result))
            return result

    def get_friends_from_my_friends(self, personId):
        #Consulta los amigos de los amigos de un nodo
        with driver.session() as session:
            result = session.run("MATCH (n:Person{id:$id})-[:FRIEND]->(myFriends)-[:FRIEND]->(othersFriends) RETURN othersFriends.id as id", id=int(personId)).data()
            return result

    def add_new_relationship(self, personId1, personId2):
        #Relaciona dos nodos como amigos
        with driver.session() as session:
            result = session.run("MERGE (n:Person{id:$id1})\n"
                                 "MERGE (m:Person{id:$id2})\n"
                                 "MERGE (n)-[:FRIEND]->(m)-[:FRIEND]->(n)", id1=int(personId1), id2=int(personId2)).data()
            return result
    
    def delete_relationship(self, personId1, personId2):
        #Elimina una relación de amistad
        with driver.session() as session:
            result = session.run("MATCH (n:Person{id:$id1})-[r1:FRIEND]->(m:Person{id:$id2})-[r2:FRIEND]->(n)\n"
                                 "DELETE r1, r2", id1=int(personId1), id2=int(personId2))
        return result
        