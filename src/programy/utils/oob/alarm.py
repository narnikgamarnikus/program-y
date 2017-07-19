import logging

from programy.utils.oob.oob import OutOfBoundsProcessor
import xml.etree.ElementTree as ET

"""
<oob><alarm><message><star/></message><get name="sraix"/></alarm></oob>
alarm
	message
	<text>
	
<alarm><hour>11</hour><minute>30</minute></alarm></oob>
alarm
	hour
	min

"""

class AlarmOutOfBoundsProcessor(OutOfBoundsProcessor):

    def __init__(self):
        OutOfBoundsProcessor.__init__(self)
        self._hour = None
        self._min = None
        self._message = None

    def parse_oob_xml(self, oob: ET.Element):
        for child in oob:
            if child.tag == 'hour':
                self._hour = child.text
            elif child.tag == 'min':
                self._min = child.text
            elif child.tag == 'message':
                self._message = child.text
            else:
                logging.error ("Unknown child element [%s] in alarm oob"%(child.tag))

            if self._hour is not None and self._min is not None:
                return True
            if self._message is not None:
                return True

            logging.error("Invalid alarm oob command, either hour,min or message ")
            return False

    def execute_oob_command(self, bot, clientid):
        if self._message is not None:
            logging.info("AlarmOutOfBoundsProcessor: Showing alarm=%s", self._message)
        elif self._hour is not None and self._min is not None:
            logging.info("AlarmOutOfBoundsProcessor: Setting alarm for %s:%s"%(self._hour, self._min))
        return ""
