        elif len(cmd_line) == 1:
            print("** instance id missing **")
        else:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance not in models.storage.all():
                print("** no instance found **")
            elif len(cmd_line) < 3:
                print("** attribute name missing **")
            elif len(cmd_line) < 4:
                print("** value missing **")
            elif cmd_line[2] not in untouchable:
                ojb = objets[instance]
                ojb.__dict__[cmd_line[2]] = cmd_line[3]
                ojb.updated_at = datetime.now()
                ojb.save()

    def do_count(self, line):
        "count instances of the class"

        cmd_line = line.split()

        if cmd_line[0] not in allowed_class:
            return
        else:
            counter = 0
            keys_list = models.storage.all().keys()
            for search in keys_list:
                len_search = len(cmd_line[0])
                if search[:len_search] == cmd_line[0]:
                    counter += 1
                    # print(search)
            print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
