import logging
import xml.etree.ElementTree as ET

from programy.utils.oob.oob import OutOfBoundsProcessor

"""
Example: <oob><dial>07777777777</dial></oob>
"""
class DialOutOfBoundsProcessor(OutOfBoundsProcessor):

    def __init__(self):
        OutOfBoundsProcessor.__init__(self)
        self._number = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob.text is not None:
            self._number = oob.text
            return True
        else:
            logging.error("Unvalid dial oob command - missing dial text!")
            return False

            return self.execute_oob_command(bot, clientid)

    def execute_oob_command(self, bot, clientid):
        logging.info("DialOutOfBoundsProcessor: Dialing=%s", self._number)
        return ""
