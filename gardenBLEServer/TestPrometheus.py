import unittest
import prometheus

class TestPromethus(unittest.TestCase):

    def test_should_be_able_to_create_instance_with_name(self):
        instance = prometheus.Instance(name='Foo')
        self.assertEqual(instance.getName(), 'Foo')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()