#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
