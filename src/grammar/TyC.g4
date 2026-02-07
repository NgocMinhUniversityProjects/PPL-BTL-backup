grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// Define grammar rules here

// Code styles:
//  avoid + * ?, use another explicit rule
//  none of the non-terminals shall reference hard strings, use a terminnal instead
//  if anything is an identifier, dont....just use ID, use a template name to better know what that ID is for
//  there should be a space b4 the last ; of the linne

//empty program succeed (see example test) so main is not required
program: decl_list EOF ;

decl_list : non_empty_decl_list | ;
non_empty_decl_list : decl non_empty_decl_list | decl ;
decl : struct_decl | func_decl ;

struct_decl : KEYWORD_STRUCT ID LB struct_member_decl_list RB SM ;
struct_member_decl_list : non_empty_struct_member_decl_list | ;
non_empty_struct_member_decl_list : struct_member_decl non_empty_struct_member_decl_list | struct_member_decl ;
struct_member_decl : explicit_type ID SM; // SM is not a separator here but rather part of the, SM is required even tho its the last element

struct_literal : LB struct_literal_members RB ;
struct_literal_members : expr_list | ;
expr_list : expr CM struct_literal_members | expr ;

func_decl : return_type ID LP param_list RP LB statement_list RB ;

return_type : explicit_type | KEYWORD_TYPE_VOID | ;
param_list : non_empty_param_list | ;
non_empty_param_list : param_decl CM param_list | param_decl ;
param_decl : explicit_type ID ;

statement_list : non_empty_statement_list | ; 
non_empty_statement_list : statement non_empty_statement_list | statement ;
statement : var_decl_statement | block_statement | if_statement | while_statement | for_statement | switch_statement | break_statement | continue_statement | return_statement | expr_statement ;

block_statement : LB statement_list RB ;

var_decl_statement : var_decl SM;
var_decl : type_decl ID EQ expr | type_decl ID ;
type_decl : explicit_type | KEYWORD_TYPE_AUTO ;

if_statement : KEYWORD_IF LP expr RP statement | if_else_statement ;
if_else_statement : KEYWORD_IF LP expr RP statement KEYWORD_ELSE statement ;

while_statement : KEYWORD_WHILE LP expr RP statement ;

for_statement : KEYWORD_FOR LP for_init SM for_cond SM for_update RP statement ;
for_init : var_decl | expr | ;
for_cond : expr | ;
for_update : assignment_expr | inc_or_dec_expr | ;

switch_statement : KEYWORD_SWITCH LP expr RP LB case_list RB ;
case_list : non_empty_case_list | ;
non_empty_case_list : case_element non_empty_case_list | case_default non_empty_case_list | case_element ;

case_element : KEYWORD_CASE expr CL statement_list;
case_default : KEYWORD_DEFAULT CL statement_list;

break_statement : KEYWORD_BREAK SM ;
continue_statement : KEYWORD_CONTINUE SM ;
return_statement : KEYWORD_RETURN expr SM | KEYWORD_RETURN SM ;

expr_statement : expr SM ;

// naming scheme of expressions is
// + expr_pred_x denotes the expression of precedence x, higher precedeence should execute before lower ones if i do this correctly
// + expr_... is at this site only, internal to exprs, dont reference these elsewhere
// + meanwhiles ..._expr is the opposite, for use outsides, like inc_or_dec_expr, used in description of for statement
// 

expr : expr_pred_0 ;

expr_pred_0  : assignment_expr | expr_pred_1 ;  //assign =
expr_pred_1  : expr_pred_1 OP_OR expr_pred_2 | expr_pred_2 ;                             //and &&
expr_pred_2  : expr_pred_2 OP_AND expr_pred_3 | expr_pred_3 ;                            //or ||
expr_pred_3  : expr_pred_3 (OP_EQ | OP_NEQ) expr_pred_4 | expr_pred_4 ;                  //compare euqality == !=
expr_pred_4  : expr_pred_4 (OP_LT | OP_LEQ | OP_GT | OP_GEQ) expr_pred_5 | expr_pred_5 ; //compare magitude 
expr_pred_5  : expr_pred_5 (OP_ADD | OP_SUB) expr_pred_6 | expr_pred_6 ;                 //binary add sub
expr_pred_6  : expr_pred_6 (OP_MUL | OP_DIV | OP_MOD) expr_pred_7 | expr_pred_7 ;        //binary * / %
expr_pred_7  : (OP_NOT | OP_SUB | OP_ADD) expr_pred_7 | expr_pred_8 ;                    //unary ! + -
expr_pred_8  : (OP_INC | OP_DEC) expr_pred_8  | expr_pred_9 ;                            //prefix  ++ --
expr_pred_9  : expr_pred_9 (OP_INC | OP_DEC) | expr_pred_10 ;                            //postfix ++ --
expr_pred_10 : expr_pred_10 DOT ID | operand ;                                           //struct member acces

// these for use else where
// these enfoces at least 1 of their respective recur (before possibly moving up the precedence chain)
expr_prefix_inc_or_dec : (OP_INC | OP_DEC) expr_pred_8 ;
expr_postfix_inc_or_dec : expr_pred_9 (OP_INC | OP_DEC) ;
inc_or_dec_expr : expr_prefix_inc_or_dec | expr_postfix_inc_or_dec ; //use in for statement

assignment_expr : ID EQ expr_pred_0 | expr_member_access EQ expr_pred_0 ; //use in for statement

expr_member_access : expr_pred_10 DOT ID ;

operand_func_call : ID LP operand_list RP ;
operand_list : non_empty_operand_list | ;
non_empty_operand_list : operand CM non_empty_operand_list | operand ;
operand : INT_LIT | STR_LIT | FLOAT_LIT | struct_literal | operand_func_call | sub_expr | ID;
sub_expr : LP expr RP ;

explicit_type : KEYWORD_TYPE_INT | KEYWORD_TYPE_FLOAT | KEYWORD_TYPE_STR | ID ; //not void nor auto here, those are used in very specific places

// Lexer section

// keywords
KEYWORD_TYPE_VOID : 'void' ;
KEYWORD_TYPE_INT : 'int' ;
KEYWORD_TYPE_AUTO : 'auto' ;
KEYWORD_TYPE_FLOAT : 'float' ;
KEYWORD_TYPE_STR : 'string' ;

KEYWORD_SWITCH : 'switch' ;
KEYWORD_CASE : 'case' ;
KEYWORD_DEFAULT : 'default';

KEYWORD_IF : 'if' ;
KEYWORD_ELSE : 'else' ;
KEYWORD_FOR : 'for';
KEYWORD_WHILE : 'while' ;
KEYWORD_RETURN : 'return' ;
KEYWORD_BREAK : 'break';
KEYWORD_CONTINUE : 'continue';

KEYWORD_STRUCT : 'struct' ;

// operators, in decresinng length order
OP_EQ  : '==';
OP_NEQ : '!=';
OP_LEQ : '<=';
OP_GEQ : '>=';
OP_OR  : '||';
OP_AND : '&&';
OP_INC : '++';
OP_DEC : '--';
OP_ADD : '+' ;
OP_DIV : BACKSLASH ;
OP_SUB : '-' ;
OP_MUL : '*' ;
OP_MOD : '%' ;
OP_NOT : '!' ;
OP_LT  : '<' ;
OP_GT  : '>' ;

//symbols
DOT : '.'; 
EQ : '=';
fragment BACKSLASH : '/' ; //fragment is fine since none of the parser rules uses this

LP  : '(' ; // Parenthesis
RP  : ')' ;
LB  : '{' ; // Brace
RB  : '}' ;
CM  : ',' ;
SM  : ';' ;
CL  : ':' ; // colon

DOUBLE_QUOTE : '"' ;
fragment UNDERSCORE : '_' ;

//literals 
INT_LIT : DIGIT_LIST ; //diigt list only -xxx is allowed but thats the job of the unary - 
fragment NULLABLE_DIGIT_LIST : DIGIT | ;
fragment DIGIT_LIST : DIGIT DIGIT_LIST | DIGIT ;
fragment DIGIT : [0-9] ;

FLOAT_LIT : FLOATLIT_HAS_DECIMAL EXPONENT_PART_OR_NULL | DIGIT_LIST EXPONENT_PART;
fragment FLOATLIT_HAS_DECIMAL : NULLABLE_DIGIT_LIST DOT DIGIT_LIST | DIGIT_LIST DOT NULLABLE_DIGIT_LIST ;
fragment EXPONENT_PART : [eE] EXPONENT_SIGN DIGIT_LIST ;
fragment EXPONENT_PART_OR_NULL : EXPONENT_PART | ;
fragment EXPONENT_SIGN : OP_ADD | OP_SUB | ;

//string literal
STR_LIT : DOUBLE_QUOTE STR_LIT_CHAR_LIST DOUBLE_QUOTE 
{
self.text = self.text[1:-1]
} ;
fragment STR_LIT_CHAR_LIST : NON_EMPTY_STR_LIT_CHAR_LIST | ;
fragment NON_EMPTY_STR_LIT_CHAR_LIST : STR_LIT_ALLOW_CHARS NON_EMPTY_STR_LIT_CHAR_LIST | STR_LIT_ALLOW_CHARS ;
fragment STR_LIT_ALLOW_CHARS : STR_LIT_ESCAPED_CHARS | ~[\u0100-\uFFFF\n\r"] ; 

STR_LIT_ESCAPED_CHARS : BACKSLASH ALLOW_ESCAPES {
c = self.text[1]
cm = {"b":"\b","f":"\f","r":"\r","n":"\n","t":"\t","\"":"\"","\\":"\\"}
self.text = cm[c]
} ; //I want this to be a fragment but fragments cant have actions, and putting these inside STR_LIT would be complicated, its probably fine
fragment ALLOW_ESCAPES : [bfrnt"\\] ;

//ID
ID : (LETER | UNDERSCORE) ID_CHAR_LIST; //last here is intentional as any keywords above is matched first
fragment ID_ALLOW_CHAR : [a-zA-Z0-9_];
fragment ID_CHAR_LIST : NON_EMPTY_ID_CHAR_LIST | ;
fragment NON_EMPTY_ID_CHAR_LIST : ID_ALLOW_CHAR NON_EMPTY_ID_CHAR_LIST | ID_ALLOW_CHAR ;
fragment LETER : [a-zA-Z] ;

//skips
WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
LINE_COMMENT : '//' ~[\n\r]* -> skip ;

//errors
ERROR_CHAR: [\u0100-\uFFFF] ; //?? not mentioned anywhere but check in example test so keeping
ILLEGAL_ESCAPE : BACKSLASH . //proper escapes is already caught by this point
{
self.text = self.text[1:] # strips openning quote
} ; 
UNCLOSE_STRING : DOUBLE_QUOTE ~[\n\r"]* ([\n\r] | EOF) 
{
self.text = self.text[1:]
while self.text.endswith("\n") or self.text.endswith("\r"):
    self.text = self.text[:-1]
} ;