#!/usr/bin/python3
"""Defines the console"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """helps to parse user typed input"""
    return tuple(arg.split())


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

    def default(self, arg):
        """Default behavior for cmd module"""
        mthds = ['create', 'show', 'update', 'all', 'destroy', 'count']
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cmd = cls[1].split('(')
            args = cmd[1].split(')')

            if cls[0] in HBNBCommand.classes and cmd[0] in mthds:
                arg = cmd[0] + ' ' + cls[0] + ' ' + args[0]
                return self.onecmd(arg)

        print("*** Unknown syntax: {}".format(arg))
        return False

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
        args = parse(arg)
        obj_list = []
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for objs in storage.all().values():
                if len(args) > 0 and args[0] == objs.__class__.__name__:
                    obj_list.append(objs.__str__())
                elif len(args) == 0:
                    obj_list.append(objs.__str__())
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute"""
        args = parse(arg)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                cast = type(eval(args[3]))
                line3 = args[3]
                line3 = line3.strip('"')
                line3 = line3.strip("'")
                setattr(storage.all()[key], args[2], cast(line3))
                storage.all()[key].save()
            else:
                print("** no instance found **")
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** class doesn't exist **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, arg):
        """show count of instances"""
        args = arg.split('.')
        if arg in HBNBCommand.classes:
            count = sum(1 for key in storage.all() if arg in key)
            print(count)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
