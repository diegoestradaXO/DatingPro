#Proyceto 2 de Algoritmos y Estructura de Datos
#DatingPro: recomendaciones con graph database usando Neo4J
#Autores:
#Michael Chan 18562 
#Diego Estrada 18540
#Isabel Ortiz 18176

from neo4j import GraphDatabase

class Database(object):
    #Crea la base de datos
    def __init__(self, uri,user,password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    #Cierra la base de datos
    def close(self):
        self._driver.close()
    def user_to_food(cls, tx, param1, param2):
        tx.run("MATCH (a:User) WHERE a.name = $param1 "
                "MATCH (b:Food) WHERE b.typeOfFood = $param2 "
                "MERGE (a)-[:LIKES]->(b)",
            param1=param1, param2=param2)
    def match_food(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_food, param1, param2)

    def user_to_city(cls, tx, param1, param2):
        tx.run("MATCH (a:User) WHERE a.name = $param1 "
                "MATCH (b:City) WHERE b.name = $param2 "
                "MERGE (a)-[:LIVES_IN]->(b)",
            param1=param1, param2=param2)
    def match_city(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_city, param1, param2)
    
    def user_to_music(cls, tx, param1, param2):
        tx.run("MATCH (a:User) WHERE a.name = $param1 "
                "MATCH (b:Music) WHERE b.genre = $param2 "
                "MERGE (a)-[:LISTEN]->(b)",
            param1=param1, param2=param2)
    def match_music(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_music, param1, param2)

    #Crea un nodo segun el tipo indicado
    def add_user(self, name, user, password, age, num):
        with self._driver.session() as session:
            return session.write_transaction(self.create_user_node, name, user, password, age, num)
    @staticmethod
    def create_user_node(tx, name, user, password, age, num):
        tx.run("CREATE (:User {name: $name, user: $user, password: $password, age: $age, num: $num})",
         name=name, user=user, password=password, age=age, num=num)

    def verifyAccount(self, user, password):
        results=[]
        matchQuery = "MATCH (u:User {user: '" + user + "', password: '" + password + "'}) RETURN u"
            # Execute the CQL query
        with self._driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(matchQuery)
            for node in nodes:
                results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
            return results

    def verifyExistence(self, nodeType, param):
        if(nodeType == "Music"):
            results=[]
            matchQuery = "MATCH (x:Music {genre: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Movie"):
            results=[]
            matchQuery = "MATCH (x:Movie {genre: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Food"):
            results=[]
            matchQuery = "MATCH (x:Food {type: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "City"):
            results=[]
            matchQuery = "MATCH (x:City {name: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results

    #def add_food(self, typeOfFood):
     #   with self._driver.session() as session:
      #      return session.write_transaction(self.create_food_node, typeOfFood)
    #@staticmethod
    #def create_food_node(tx, typeOfFood):
     #   tx.run("CREATE (:Food {typeOfFood: $typeOfFood})",
      #   typeOfFood=typeOfFood)


    #def add_movie(self, genre):
     #   with self._driver.session() as session:
      #      return session.write_transaction(self.create_movie_node, genre)
    #@staticmethod
    #def create_movie_node(tx, genre):
     #   tx.run("CREATE (:Movie {genre: $genre})",
      #   genre=genre)

    #def add_music(self, genre):
     #   with self._driver.session() as session:
      #      return session.write_transaction(self.create_music_node, genre)
    #@staticmethod
    #def create_music_node(tx, genre):
     #   tx.run("CREATE (:Music {genre: $genre})",
      #   genre=genre)     

    #def add_city(self, name):
     #   with self._driver.session() as session:
      #      return session.write_transaction(self.create_city_node, name)
    #@staticmethod
    #def create_city_node(tx, name):
     #   tx.run("CREATE (:City {name: $name})",
      #   name=name)

    def make_a_match(self, relation, param1, param2):
        with self._driver.session() as session:
            return session.write_transaction(self.create_a_match, relation, param1, param2)
                    

    def create_a_match(cls, tx, relation, param1, param2):
        if(relation == "userToFood"):
           tx.run("MATCH (a:User) WHERE a.name = $param1 "
           "MERGE (b:Food {typeOfFood: $param2})"
           "MERGE (a)-[:LIKES]->(b)",
           param1=param1, param2=param2)
        elif(relation == "userToMovie"):
            tx.run("MATCH (a:User) WHERE a.name = $param1 "
                    "MERGE (b:Movie {genre: $param2})"
                    "MERGE (a)-[:WATCH]->(b)",
                    param1=param1,param2=param2)
        elif(relation == "userToMusic"):
            tx.run("MATCH (a:User) WHERE a.name = $param1 "
                    "MERGE (b:Music {genre: $param2})"
                    "MERGE (a)-[:LISTEN]->(b)",
                    param1=param1,param2=param2)
        elif(relation == "userToCity"):
            tx.run("MATCH (a:User) WHERE a.name = $param1 "
                    "MERGE (b:City {name: $param2})"
                    "MERGE (a)-[:LIVES_IN]->(b)",
                    param1=param1,param2=param2)                
             

