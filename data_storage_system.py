from abc import ABC,abstractmethod


class Data_Storage(ABC):

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def  load(self):
        pass

    @abstractmethod
    def  delete(self):
        pass


class File_Based_Storage(Data_Storage):
    def save(self):
        print("Save File Based ")
    
    def load(self):
        print("Load File Based")

    def delete(self):
        print("Delete File Based")


class  Database_Storage(Data_Storage):
    def save(self):
        print("Save Database")

    def load(self):
        print("Load Database")
        
    def delete(self):
        print("Delete Database")



file_based_storage = File_Based_Storage()

database_storage = Database_Storage()

file_based_storage.load()
file_based_storage.save()
file_based_storage.delete()
print()
database_storage.load()
database_storage.save()
database_storage.delete()
