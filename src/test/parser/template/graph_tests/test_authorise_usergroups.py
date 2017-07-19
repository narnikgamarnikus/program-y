import xml.etree.ElementTree as ET

from programy.parser.exceptions import ParserException
from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.authorise import TemplateAuthoriseNode
from programy.config.sections.brain.brain import BrainConfiguration
from programy.config.sections.brain.security import BrainSecurityConfiguration

from test.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient


class TemplateGraphAuthoriseTests(TemplateGraphTestClient):

    def get_brain_config(self):
        brain_config = BrainConfiguration()
        brain_config.security._authorisation = BrainSecurityConfiguration("authorisation")
        brain_config.security.authorisation._classname = "programy.utils.security.authorise.usergroupsauthorisor.BasicUserGroupAuthorisationService"
        brain_config.security.authorisation._denied_srai = "ACCESS_DENIED"
        brain_config.security.authorisation._usergroups = "$BOT_ROOT/usergroups.yaml"
        return brain_config

    def test_authorise_with_role_as_attrib_access_allowed(self):
        template = ET.fromstring("""
			<template>
				<authorise role="root">
				Hello
				</authorise>
			</template>
			""")

        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertEqual(len(ast.children), 1)

        auth_node = ast.children[0]
        self.assertIsNotNone(auth_node)
        self.assertIsInstance(auth_node, TemplateAuthoriseNode)
        self.assertIsNotNone(auth_node.role)
        self.assertEqual("root", auth_node.role)

        result = auth_node.resolve(self.test_bot, "console")
        self.assertIsNotNone(result)
        self.assertEqual("Hello", result)

    def test_authorise_with_role_as_attrib_access_denied(self):
        template = ET.fromstring("""
                <template>
                    <authorise role="denied">
                    Hello
                    </authorise>
                </template>
                """)

        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertEqual(len(ast.children), 1)

        auth_node = ast.children[0]
        self.assertIsNotNone(auth_node)
        self.assertIsInstance(auth_node, TemplateAuthoriseNode)
        self.assertIsNotNone(auth_node.role)
        self.assertEqual("denied", auth_node.role)
