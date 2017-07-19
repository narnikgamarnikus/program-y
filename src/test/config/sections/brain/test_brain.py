import unittest

from programy.config.sections.brain.brain import BrainConfiguration
from programy.config.file.yaml_file import YamlConfigurationFile
from programy.config.sections.client.console import ConsoleConfiguration

class BrainConfigurationTests(unittest.TestCase):

    def test_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
            brain:
                overrides:
                  allow_system_aiml: true
                  allow_learn_aiml: true
                  allow_learnf_aiml: true
            
                defaults:
                  default-get: unknown
                  default-property: unknown
                  default-map: unknown
                  learn-filename: y-bot-learn.aiml

                nodes:
                  pattern_nodes: $BOT_ROOT/config/pattern_nodes.conf
                  template_nodes: $BOT_ROOT/config/template_nodes.conf
            
                binaries:
                  save_binary: false
                  load_binary: false
                  binary_filename: $BOT_ROOT/output/y-bot.brain
                  load_aiml_on_binary_fail: false
                  dump_to_file: $BOT_ROOT/output/braintree.txt
            
                files:
                    aiml:
                        files: $BOT_ROOT/aiml
                        extension: .aiml
                        directories: true
                        errors: $BOT_ROOT/output/y-bot_errors.txt
                        duplicates: $BOT_ROOT/output/y-bot_duplicates.txt
                    sets:
                        files: $BOT_ROOT/sets
                        extension: .txt
                        directories: false
                    maps:
                        files: $BOT_ROOT/maps
                        extension: .txt
                        directories: false
                    denormal: $BOT_ROOT/config/denormal.txt
                    normal: $BOT_ROOT/config/normal.txt
                    gender: $BOT_ROOT/config/gender.txt
                    person: $BOT_ROOT/config/person.txt
                    person2: $BOT_ROOT/config/person2.txt
                    predicates: $BOT_ROOT/config/predicates.txt
                    pronouns: $BOT_ROOT/config/pronouns.txt
                    properties: $BOT_ROOT/config/properties.txt
                    triples: $BOT_ROOT/config/triples.txt
                    preprocessors: $BOT_ROOT/config/preprocessors.conf
                    postprocessors: $BOT_ROOT/config/postprocessors.conf
            
                security:
                    authentication:
                        classname: programy.utils.security.authenticate.passthrough.PassThroughAuthenticationService
                        denied_srai: AUTHENTICATION_FAILED
                    authorisation:
                        classname: programy.utils.security.authorise.passthrough.PassThroughAuthorisationService
                        denied_srai: AUTHORISATION_FAILED

                oob:
                  default:
                    classname: programy.utils.oob.default.DefaultOutOfBoundsProcessor
                  dial:
                    classname: programy.utils.oob.dial.DialOutOfBoundsProcessor
                  email:
                    classname: programy.utils.oob.email.EmailOutOfBoundsProcessor

                services:
                    REST:
                        classname: programy.utils.services.rest.GenericRESTService
                        method: GET
                        host: 0.0.0.0
                    Pannous:
                        classname: programy.utils.services.pannous.PannousService
                        url: http://weannie.pannous.com/api
                    Pandora:
                        classname: programy.utils.services.pandora.PandoraService
                        url: http://www.pandorabots.com/pandora/talk-xml
                    Wikipedia:
                        classname: programy.utils.services.wikipediaservice.WikipediaService        
        """, ConsoleConfiguration(), ".")

        brain_config = BrainConfiguration()
        brain_config.load_config_section(yaml, ".")

        self.assertIsNotNone(brain_config.overrides)
        self.assertTrue(brain_config.overrides.allow_system_aiml)
        self.assertTrue(brain_config.overrides.allow_learn_aiml)
        self.assertTrue(brain_config.overrides.allow_learnf_aiml)

        self.assertIsNotNone(brain_config.defaults)
        self.assertEqual("unknown", brain_config.defaults.default_get)
        self.assertEqual("unknown", brain_config.defaults.default_property)
        self.assertEqual("unknown", brain_config.defaults.default_map)
        self.assertEqual("y-bot-learn.aiml", brain_config.defaults.learn_filename)

        self.assertIsNotNone(brain_config.nodes)
        self.assertEquals("./config/pattern_nodes.conf", brain_config.nodes.pattern_nodes)
        self.assertEquals("./config/template_nodes.conf", brain_config.nodes.template_nodes)

        self.assertIsNotNone(brain_config.binaries)
        self.assertFalse(brain_config.binaries.save_binary)
        self.assertFalse(brain_config.binaries.load_binary)
        self.assertEquals("./output/y-bot.brain", brain_config.binaries.binary_filename)
        self.assertFalse(brain_config.binaries.load_aiml_on_binary_fail)
        self.assertEquals("./output/braintree.txt", brain_config.binaries.dump_to_file)

        self.assertIsNotNone(brain_config.files)
        self.assertIsNotNone(brain_config.files.aiml_files)
        self.assertEqual("./aiml", brain_config.files.aiml_files.files)
        self.assertEqual(".aiml", brain_config.files.aiml_files.extension)
        self.assertTrue(brain_config.files.aiml_files.directories)
        self.assertEqual("./output/y-bot_errors.txt", brain_config.files.aiml_files.errors)
        self.assertEqual("./output/y-bot_duplicates.txt", brain_config.files.aiml_files.duplicates)

        self.assertIsNotNone(brain_config.files.set_files)
        self.assertEqual("./sets", brain_config.files.set_files.files)
        self.assertEqual(".txt", brain_config.files.set_files.extension)
        self.assertFalse(brain_config.files.set_files.directories)

        self.assertIsNotNone(brain_config.files.map_files)
        self.assertEqual("./maps", brain_config.files.map_files.files)
        self.assertEqual(".txt", brain_config.files.map_files.extension)
        self.assertFalse(brain_config.files.map_files.directories)

        self.assertEqual(brain_config.files.denormal, "./config/denormal.txt")
        self.assertEqual(brain_config.files.normal, "./config/normal.txt")
        self.assertEqual(brain_config.files.gender, "./config/gender.txt")
        self.assertEqual(brain_config.files.person, "./config/person.txt")
        self.assertEqual(brain_config.files.person2, "./config/person2.txt")
        self.assertEqual(brain_config.files.predicates, "./config/predicates.txt")
        self.assertEqual(brain_config.files.pronouns, "./config/pronouns.txt")
        self.assertEqual(brain_config.files.properties, "./config/properties.txt")
        self.assertEqual(brain_config.files.triples, "./config/triples.txt")
        self.assertEqual(brain_config.files.preprocessors, "./config/preprocessors.conf")
        self.assertEqual(brain_config.files.postprocessors, "./config/postprocessors.conf")

        self.assertIsNotNone(brain_config.security)
        self.assertIsNotNone(brain_config.security.authorisation)
        self.assertIsNotNone(brain_config.security.authentication)

        self.assertIsNotNone(brain_config.oob)
        self.assertIsNotNone(brain_config.oob.oobs())
        self.assertIsNotNone(brain_config.oob.default())
        self.assertIsNotNone(brain_config.oob.oob("dial"))
        self.assertIsNotNone(brain_config.oob.oob("email"))

        self.assertIsNotNone(brain_config.services)
        self.assertTrue(brain_config.services.exists("REST"))
        self.assertTrue(brain_config.services.exists("Pannous"))
        self.assertTrue(brain_config.services.exists("Pandora"))
        self.assertTrue(brain_config.services.exists("Wikipedia"))
        self.assertFalse(brain_config.services.exists("Other"))
