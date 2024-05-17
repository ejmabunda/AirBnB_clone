#!/usr/bin/python3
"""
This module supplies the command interpreter for the HBNB project.
It includes a console that uses the cmd module.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class:
    This class is the command interpreter for the HBNB project.
    It includes methods to handle commands such as quit,
    EOF, and emptyline.
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program.

        Args:
            line (str): Not used, but required.

        Returns:
            True to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        EOF (End Of File) command to exit the program.

        Args:
            line (str): Not used, but required.

        Returns:
            True to exit the program.
        """
        print()
        return True

    def do_emptyline(self, line):
        """
        Empty line command. If the user inputs an empty line,
        nothing should be executed and the prompt should be
        displayed again.

        Args:
            line (str): Not used, but required.
        """
        pass

    def precmd(self, line):
        """
        This method is executed just before the line is interpreted,
        but after the input prompt is generated and issued.

        Args:
            line (str): The line to be executed.

        Returns:
            The line stripped of leading and trailing whitespaces.
        """
        return line.strip()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
