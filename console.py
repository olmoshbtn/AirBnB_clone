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


classes_dic = {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review}

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

"""
    def do_show



    show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ show)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
