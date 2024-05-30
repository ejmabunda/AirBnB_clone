#!/usr/bin/python3
"""This module defines the HBNBCommand class, which serves as the command interpreter.
"""

import cmd
import json
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Custom command interpreter for the AirBnB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D).
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file), and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            instance = storage.all().get(f"{class_name}.{instance_id}")
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (saves the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            instance = storage.all().get(f"{class_name}.{instance_id}")
            if instance:
                del storage.all()[f"{class_name}.{instance_id}"]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of instances
        based on the class name.
        """
        args = arg.split()
        instances = []
        if not args:
            for instance in storage.all().values():
                instances.append(str(instance))
        else:
            try:
                class_name = args[0]
                for instance in storage.all().values():
                    if instance.__class__.__name__ == class_name:
                        instances.append(str(instance))
            except NameError:
                print("** class doesn't exist **")
                return
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating an attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            if len(args) < 3:
                print("** instance id missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** attribute name missing **")
                return
            attribute_value = args[3]
            instance = storage.all().get(f"{class_name}.{instance_id}")
            if instance:
                setattr(instance, attribute_name, attribute_value)
                instance.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")



if __name__ == "__main__":
    HBNBCommand().cmdloop()
