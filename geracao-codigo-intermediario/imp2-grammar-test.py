import unittest
import tatsu                            

class TestImpGrammar(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_parse(self, file_name, ast):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        print(str(self.parser.parse(source)))
        #self.assertEqual(str(self.parser.parse(source)), ast)
    def test_cmd_parse0(self):
        '''
        Escreva um programa Imp examples/cmd-test0.imp2 que tenha a árvore sintática dada
        pela string passada como segundo parâmetro de __test_parse.
        '''
        self.__test_parse('examples/cmd-test0.imp2', "")

  
if __name__ == '__main__':
    unittest.main()
