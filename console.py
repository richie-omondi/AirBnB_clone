#!/usr/bin/python3
""" The entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ The command processor """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exi the interpreter """

    def help_help(self):
        """ Prints the help command description """
        print("Gives description of a given command")

    def emptyline(self):
        """ Do nothing when an empty line is entered """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
