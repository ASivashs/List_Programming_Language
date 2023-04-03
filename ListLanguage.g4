grammar ListLanguage;

program: sub_program* statement*;

block: statement+;


statement: assign_element
        | print
        | if_block
        | sub_program_call
        | for_block
        | return_def
        | range
        | while_block
        | input
        | method
        ;

// OPERATIONS
assign_element: (get_element
            | ID COMMA?)+ ASSIGN
            ( list_init
            | elem_init
            | queue_init
            | tree
            | operations
            | input
            | get_element
            | method
            | ID COMMA?)+
            ;
operations: OPEN_PAREN* (variables_and_num (ADD | MINUS | MUL | DIV)?)+ operation_list? CLOSE_PAREN*;
get_element: ID OPEN_BRACK NUM CLOSE_BRACK;

// INIT
queue_init: OPEN_PAREN (elem_init COMMA?)* CLOSE_PAREN;
list_init: OPEN_BRACK (elem_init COMMA?)* CLOSE_BRACK;
elem_init: type;
tree: OPEN_BRACK (elem_init tree tree?)* CLOSE_BRACK;

// IF
if_block: if_init elif* else?;
if_init: IF OPEN_PAREN variables_and_num compare variables_and_num CLOSE_PAREN OPEN_BRACE block CLOSE_BRACE;
else: ELSE OPEN_PAREN block CLOSE_PAREN;
elif: ELIF OPEN_PAREN variables_and_num compare variables_and_num CLOSE_PAREN OPEN_BRACE block CLOSE_BRACE;
compare: EQUALS
        | ADD
        | MINUS
        | MUL
        | DIV
        | GREATER_THAN
        | GT_EQ
        | LESS_THAN
        | LT_EQ
        ;

// FOR
for_block: for_init else?;
for_init: FOR OPEN_PAREN variables IN variables_and_num CLOSE_PAREN OPEN_BRACE block CLOSE_BRACE;

// WHILE
while_block: while_init else?;
while_init: WHILE OPEN_PAREN variables_and_num compare variables_and_num CLOSE_PAREN OPEN_BRACE (block)+ CLOSE_BRACE;

// DEF
sub_program: DEF ID OPEN_PAREN type (COMMA type)* CLOSE_PAREN OPEN_BRACE (block)+ CLOSE_BRACE;
sub_program_call: ID OPEN_PAREN type (COMMA type)* CLOSE_PAREN;

// BASE FUNC
print: PRINT OPEN_PAREN (variables_and_num COMMA?)* CLOSE_PAREN;
range: RANGE OPEN_PAREN variables_and_num CLOSE_PAREN;
input: INPUT OPEN_PAREN CLOSE_PAREN;
return_def: RETURN ID
        | NUM
        ;
method: variables POINT_FOR_M methods OPEN_PAREN variables_and_num? CLOSE_PAREN;

// VARIABLES
methods: GET
        | POP
        | APPEND
        | REMOVE
        | CLEAR
        ;
variables: ID
        | elem_init
        | sub_program_call
        | get_element
        ;
variables_and_num: variables
                | NUM
                ;
type: NUM
    | ID
    ;
operation_list: ADD
            | MINUS
            | DIV
            | MUL
            | POW
            ;


// CONST
INPUT:  'input';
PRINT:  'print';
RANGE:  'range';
DEF:    'def';
FOR:    'for';
WHILE:  'while';
IN:     'in';
IF:     'if';
ELSE:   'else';
ELIF:   'elif';
GET:    'get';
POP:    'pop';
APPEND: 'append';
REMOVE: 'remove';
CLEAR:  'clear';
RETURN: 'return';

TWO_POINT:      ':';
POINT_FOR_M:    '.';
COMMA:          ',';
OPEN_CLOSE_EL:  '"';
OPEN_PAREN:     '(';
CLOSE_PAREN:    ')';
OPEN_BRACK:     '[';
CLOSE_BRACK:    ']';
OPEN_BRACE:     '{';
CLOSE_BRACE:    '}';

ASSIGN:     '=';
ADD:        '+';
MINUS:      '-';
MUL:        '*';
DIV:        '/';
POW:        '**';
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS :    '==';
GT_EQ :     '>=';
LT_EQ :     '<=';
NOT_EQ_1 :  '<>';
NOT_EQ_2 :  '!=';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUM: [1-9][0-9]*|[0];

WS: [ \t\r\n]+ -> skip;