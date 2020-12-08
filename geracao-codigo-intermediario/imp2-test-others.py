import unittest
import tatsu
from impiler import Impiler
from pi import run

class TestOthers(unittest.TestCase):
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
        # esse exemplo mostra que o return ignora tudo o que vem depois dele dentro de uma função
        # a função retorna |x+1 se x < 5| x+5 se x = 5| x+10 se x > 5
        outResp = "[4, 10, 23]"
        
        self.__test_pi_aut('examples/test2.imp2', outResp)
        
if __name__ == '__main__':
    unittest.main()
