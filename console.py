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
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "City": City,
        "Amenity": Amenity,
        "State": State,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit program when EOF is reached"""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of a given class"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.classes[arg]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instances"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = parse(arg)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Destroys an instance"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = parse(arg)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = self.parse(arg)
        obj_list = []
        if len(arg) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
        else:
            args = self.parse(arg)
            if args[0] in HBNBCommand.classes:
                for key, objs in storage.all().items():
                    if args[0] in key:
                        obj_list.append(objs)
            else:
                print("** class doesn't exist **")
                return
        for obj in obj_list:
            print(obj)

    def parse(self, arg):
        """helps to parse user typed input"""
        return tuple(arg.split())

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute"""
        args = parse(arg)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            line3 = args[3]
            line3 = line3.strip('"')
            line3 = line3.strip("'")
            setattr(storage.all()[key], args[2], cast(line3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value name missing **")

    def do_count(self, arg):
        """show count of instances"""
        if arg in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if arg in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
