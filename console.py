#!/usr/bin/python3
"""This module supplies the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbhb) '

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()