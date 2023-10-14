#!/usr/bin/python3
"""Defines the console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter"""
    prompt = "(hbnb) "
    classses = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }

    def precmd(self, arg):
        """Parses command input"""
        pass

    def emptyline(EOF):
        """Do nothing on an empty line"""
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit program when EOF is reached"""
        print()
        return True

    def check_class(self, class_name):
        """checks if clss_name is valid"""
        if class_name is not self.classes:
            print("** class doesnt exist **")
            return False
        return True

    def do_create(self, arg):
        """Creates a new instance of a given class"""

        """checks the classes"""
        if not self.check_class(arg):
            return

        """Saves the instance"""
        instance = HBNBCommand.classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instances"""
        pass

    def do_destroy(self, arg):
        """Destroys an instance"""
        pass

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        pass

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
