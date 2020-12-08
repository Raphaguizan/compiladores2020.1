import unittest
import tatsu
from impiler import Impiler
from pi import run

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_pi_aut(self, file_name, outR):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        pi_ast = self.parser.parse(source, semantics=Impiler())
        (trace, step, out, dt) = run(pi_ast, color=False)
        self.assertEqual(str(out), outR)


    def test_exp(self):
        outResp = "[[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]]"
        
        self.__test_pi_aut('examples/test1.imp2', outResp)
        
if __name__ == '__main__':
    unittest.main()
