import logging

from programy.utils.oob.oob import OutOfBoundsProcessor
import xml.etree.ElementTree as ET

"""
<dialog><title>Which contact?</title><list><get name="contactlist"/></list></dialog>
dialog
	title
	list

"""

class DialogOutOfBoundsProcessor(OutOfBoundsProcessor):

    def __init__(self):
        OutOfBoundsProcessor.__init__(self)
        self._title = None
        self._list = None

    def parse_oob_xml(self, oob: ET.Element):
        for child in oob:
            if child.tag == 'title':
                self._title = child.text
            elif child.tag == 'list':
                self._list = child.text
            else:
                logging.error ("Unknown child element [%s] in dialog oob"%(child.tag))

            if self._title is not None and \
                self._list is not None:
                return True

            logging.error("Invalid dialog oob command")
            return False

    def execute_oob_command(self, bot, clientid):
        logging.info("DialogOutOfBoundsProcessor: Dialog=%s", self._title)
        return ""
