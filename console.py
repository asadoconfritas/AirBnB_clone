#!/usr/bin/python3
"""
This script containts the entry point of
the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter"""
    intro = ""
    prompt = "(hbtn) "
    file = None

    def do_EOF(self, arg):
        """EOF Quits from the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
