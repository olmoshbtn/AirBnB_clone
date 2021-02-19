#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes_dic = {
    "BaseModel": BaseModel, "User": User, "State": State, "City": City,
    "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand line interpreter implementation"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """method to exit the program"""
        return True

    def do_EOF(self, line):
        """method to exit cleanly"""
        return True

    def emptyline(self):
        """method to bypassing empty line entered and
        not executing previous command"""
        pass

    def help_quit(self):
        """method to print help for quit method"""
        print("This is a method to exit the program")

    def help_EOF(self):
        """method to print help for EOF method"""
        print("This is a method to exit the program cleanly")

    def do_create(self, line):
        """method to create, save to json
        and print id of a new instance of BaseModel"""
        command = line.split()
        if len(command) == 0:
            print("** class name missing **")
            return False
        elif command[0] not in classes_dic:
            print("** class doesn't exist **")
            return False
        elif command[0] in classes_dic:
            new__object = classes_dic[command[0]]()
        print(new__object.id)
        new__object.save()

    def do_show(self, line):
        """method to print the string representation
        based on the class name and id"""
        command = line.split()
        if len(command) == 0:
            print("** class name missing **")
            return False
        if command[0] not in classes_dic:
            print("** class doesn't exist **")
            return False
        if len(command) == 1:
            print("** instance id missing **")
        if len(command) == 2:
            new__object = command[0] + "." + command[1]
            if new__object not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[new__object])

    def do_destroy(self, line):
        """method to delete an instance based on the class name and id,
        saving the change into the JSON file"""
        command = line.split()
        if len(command) == 0:
            print("** class name missing **")
            return False
        if command[0] not in classes_dic:
            print("** class doesn't exist **")
            return False
        if len(command) == 1:
            print("** instance id missing **")
        if len(command) == 2:
            new__object = command[0] + "." + command[1]
            if new__object not in models.storage.all():
                print("** no instance found **")
            else:
                models.storage.all().pop(new__object)
                models.storage.save()

    def do_all(self, line):
        """method to print all string representation of all instances
        based or not on the class name"""
        try:
            tokens = line.split()
        except ValueError:
            return None
        objects = models.storage.all()
        if len(tokens) < 1:
            print([str(obj) for obj in objects.values()])
        else:
            cls = models.getmodel(tokens[0])
            if cls is None:
                print("** class doesn't exist **")
            else:
                matches = []
                for obj in objects.values():
                    if type(obj) is cls:
                        matches.append(str(obj))
                print(matches)

    def do_update(self, line):
        """method to update the instance based on the class name
        and id by adding or updating attribute"""
        command = line.split()
        if len(command) == 0:
            print("** class name missing **")
        if command[0] not in classes_dic:
            print("** class doesn't exist **")
        if len(command) == 1:
            print("** instance id missing **")
        if command[0] + "." + command[1] not in models.storage.all():
                print("** no instance found **")
        if len(command) == 2:
            print("** attribute name missing **")
        if len(command) == 3:
            print("** value missing **")
        else:
            new__object = models.storage.all().get(
                command[0] + '.' + command[1])
            setattr(new__object, command[2], command[3][1:-1])
            new__object.save()

    # help update
    def help_create(self):
        print("Usage: create <valid class name>")

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
