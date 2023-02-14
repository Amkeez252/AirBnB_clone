NBCommand().onecmd("asdasd.update()".format(id))
        self.assertEqual(f.getvalue(), expectect)
        with patch('sys.stdout', new=StringIO()) as f:
            expectect = "*** Unknown syntax: User.update()\n"
            HBNBCommand().onecmd("User.update()".format(id))
        self.assertEqual(f.getvalue(), expectect)

    def test_count(self):
        """Validate count method"""
        try:
            os.remove("file.json")
        except Exception as f:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("id.count()")
            expectect = "*** Unknown syntax: id.count()\n"
        self.assertEqual(f.getvalue(), expectect)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count(d)")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: User.count(d)\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()d")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: User.count()d\n')
