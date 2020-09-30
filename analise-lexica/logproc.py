# ------------------------------------------------------------
# Processing a log file
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'TIMESTAMP',
    'PROC',
    'MESSAGE'
] 

def t_TIMESTAMP(t):
    # Regular expression for TIMESTAMP
    r'[0-2][0-9]:[0-5][0-9]:[0-5][0-9].[0-9]{1,6}\ [-+][0-9]{4}(?=\t)'
    t.type = 'TIMESTAMP'
    return t

def t_PROC(t):
    # Regular expression for PROC
    r'\t[A-Za-z\.-]*\t'
    t.type = 'PROC'
    t.value = t.value[1:len(t.value) - 1]
    return t

def t_MESSAGE(t):
    # Regular expression for MESSAGE
    r'[^\t]*\n'
    t.type = 'MESSAGE'
    t.value = t.value[:len(t.value) - 1]
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


class LogProcLexer:
    data = None
    lexer = None
    def __init__(self):
        fh = open("log", 'r')
        self.data = fh.read()
        fh.close()
        self.lexer = lex.lex()
        self.lexer.input(self.data)

    def collect_messages(self):
        # Do your magic here
        tokens = []
        while True:
            token = self.lexer.token()
            if not token:
                break 
            if token.type == 'PROC' and token.value == "kernel":
                token = self.lexer.token()
                if token.type == 'MESSAGE':
                    tokens.append(token)
        return tokens
        
if __name__ == '__main__':
    print(LogProcLexer().collect_messages())
    
