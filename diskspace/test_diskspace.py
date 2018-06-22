import unittest
from diskspace import (
    subprocess_check_output,
    bytes_to_readable,
    print_tree,
    show_space_list
)

class TestDiskspace(unittest.TestCase):
    def test_subprocess_check_output(self):
        command = 'du -d 1 /home/daniel/Documentos/tecprog/05--danielmarques28'
        output = subprocess_check_output(command)

        self.assertEqual(str, type(output))
        self.assertIsNot('', output)

    def test_bytes_to_readable(self):
        blocks = 12
        output = bytes_to_readable(blocks)

        self.assertEqual(str, type(output))
        self.assertEqual('6.00Kb', output)
        
        blocks = 24
        output = bytes_to_readable(blocks)

        self.assertEqual(str, type(output))
        self.assertEqual('12.00Kb', output)

        
