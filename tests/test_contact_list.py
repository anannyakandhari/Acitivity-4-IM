import unittest
from contact_list.contact_list import ContactList
from PySide6.QtWidgets import QApplication

app = QApplication([])  # needed to create widgets

class TestContactList(unittest.TestCase):
    def test_add_remove_methods_exist(self):
        window = ContactList()
        self.assertTrue(hasattr(window, "_ContactList__on_add_contact"))
        self.assertTrue(hasattr(window, "_ContactList__on_remove_contact"))

if __name__ == "__main__":
    unittest.main()
