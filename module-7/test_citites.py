#|Maddison Montijo | Assignment 7.2 | Class 325

import unittest

from city_functions import get_country_info

class test_city_country(unittest.TestCase):
    def test_city_country(self):
        """Do we get the correct city and country?"""
        country_info = get_country_info("Chile","Santiago")
        self.assertEqual(country_info,"Chile Santiago")

       
#|Fun Note : I wrote the city and country backwards leading to an error.

if __name__ == '__main__':
    unittest.main()
    