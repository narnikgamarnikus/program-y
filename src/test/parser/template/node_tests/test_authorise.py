import xml.etree.ElementTree as ET

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.authorise import TemplateAuthoriseNode
from programy.parser.template.nodes.word import TemplateWordNode
from programy.config.sections.brain.brain import BrainConfiguration
from programy.config.sections.brain.security import BrainSecurityConfiguration

from test.parser.template.base import TemplateTestsBaseClass

class TemplateAuthoriseNodeTests(TemplateTestsBaseClass):

    def test_node_init(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        node = TemplateAuthoriseNode()
        node.role = "root"
        self.assertIsNotNone(node)
        self.assertEqual("root", node.role)

        root.append(node)
        self.assertEqual(len(root.children), 1)

        self.assertEqual("AUTHORISE (role=root)", node.to_string())

    def test_to_xml_service_no_content(self):
        root = TemplateNode()

        node = TemplateAuthoriseNode()
        node.role = "root"
        self.assertIsNotNone(node)

        root.append(node)
        self.assertEqual(len(root.children), 1)

        xml = root.xml_tree(self.bot, self.clientid)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual('<template><authorise role="root" /></template>', xml_str)

    def test_to_xml_service_with_content(self):
        root = TemplateNode()

        node = TemplateAuthoriseNode()
        node.role = "root"
        self.assertIsNotNone(node)

        node.append(TemplateWordNode("Hello"))

        root.append(node)
        self.assertEqual(len(root.children), 1)

        xml = root.xml_tree(self.bot, self.clientid)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual('<template><authorise role="root">Hello</authorise></template>', xml_str)
