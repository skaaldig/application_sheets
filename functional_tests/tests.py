import unittest
import time

from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_list_of_forms_loads(self):
        # User goes to url page loads.

        self.browser.get(self.live_server_url)
        self.assertIn('Application Information', self.browser.title)

        # User sees a dropdown menu
        drop_down = self.browser.find_element_by_class_name('dropdown')
        self.assertEqual('Select Your Application', drop_down.text)

        # User presses button and 4 dropdown items appear
        expected_items = ['flow measurement', 'level measurement',
                'pressure','temperature', 'valves']

        drop_down_items = self.browser.find_elements_by_class_name('dropdown-item')
        drop_down_true = all(item.get_attribute('innerHTML').lower() in expected_items for item in drop_down_items)
        self.assertEqual(drop_down_true, True)

        # User presses on Level Measurement
        level_item = drop_down_items[1]
        self.assertEqual(level_item.get_attribute('innerHTML').lower(), expected_items[1])
        time.sleep(1)
        drop_down.click()
        level_item.click()
        time.sleep(1)

        # User is redirected to new page
        self.assertEqual(self.browser.current_url, self.live_server_url + '/level-measurement/')
        

        # User 
