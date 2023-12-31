#!/usr/bin/python3
"""Command interpreter"""


import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    clases = ["BaseModel", "User", "Place",
              "State", "City", "Amenity", "Review"]

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exits the program with EOF"""
        return True

    def help_help(self):
        """Show help message"""

    def emptyline(self):
        """No action on empty line"""
        pass

    def do_create(self, args):
        """Creates an instance for the input class sent"""
        try:
            obj = getattr(sys.modules[__name__], args)()
            print(obj.id)
            obj.save()
        except Exception:
            if not args:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Shows the specific instance for the given ID"""
        input = args.split()
        if len(input) < 1:
            print("** class name missing **")
        elif input[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(input) < 2:
            print("** instance id missing **")
        else:
            key = input[0] + "." + input[1]
            dict = models.storage.all()
            if key in dict:
                print(dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Destroys the specific instance for the given ID"""
        input = args.split()
        if len(input) < 1:
            print("** class name missing **")
        elif input[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(input) < 2:
            print("** instance id missing **")
        else:
            key = input[0] + "." + input[1]
            dict = models.storage.all()
            if key in dict:
                del dict[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Shows all the instances or only the given one"""
        input = args.split()
        if len(input) < 1:
            dict = models.storage.all()
            new_list = []
            for key, value in dict.items():
                new_list.append(str(value))
            print(new_list)
        elif input[0] not in self.clases:
            print("** class doesn't exist **")
        else:
            dict = models.storage.all()
            new_list = []
            for key, value in dict.items():
                if key.split(".")[0] == input[0]:
                    new_list.append(str(value))
            print(new_list)

    def do_update(self, args):
        """Updated an instance for the given id"""
        input = args.split()
        if len(input) < 1:
            print("** class name missing **")
        elif input[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(input) < 2:
            print("** instance id missing **")
        elif input[0] + "." + input[1] not in models.storage.all():
            print("** no instance found **")
        elif len(input) < 3:
            print("** attribute name missing **")
        elif len(input) < 4:
            print("** value missing **")
        else:
            dict = models.storage.all()
            key = input[0] + "." + input[1]
            for k, v in dict.items():
                if key == k:
                    v.__dict__[input[2]] = eval(input[3])
                    v.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
