import unittest

from programy.utils.oob.email import EmailOutOfBoundsProcessor
import xml.etree.ElementTree as ET

class DefaultOutOfBoundsProcessorTests(unittest.TestCase):

    def test_email_processor_invalid(self):
        oob_processor = EmailOutOfBoundsProcessor()
        self.assertIsNotNone(oob_processor)
        oob_content = ET.fromstring("<email>process</email>")
        self.assertFalse(oob_processor.parse_oob_xml(oob_content))

    def test_email_processor_valid(self):
        oob_processor = EmailOutOfBoundsProcessor()
        self.assertIsNotNone(oob_processor)
        oob_content = ET.fromstring("<email><to>me@me.com</to><subject>test</subject><body>test body</body></email>")
        self.assertFalse(oob_processor.parse_oob_xml(oob_content))

        #self.assertEqual("", oob_processor.process_out_of_bounds(None, "console", oob_content))