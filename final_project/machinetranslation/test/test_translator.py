import unittest
import re

from translator import french_to_english, english_to_french

class TestMyModule(unittest.TestCase):
          def test_french_to_english(self):
              self.assertEqual(french_to_english(re.DOTALL) is None, False)
              self.assertEqual(french_to_english("Bonjour"), "Hello")

          def test_englishToFrench(self):
              self.assertEqual(english_to_french(re.DOTALL) is  None, False)            
              self.assertEqual(english_to_french("Hello"), "Bonjour")

if __name__ == "__main__":
         unittest.main()

