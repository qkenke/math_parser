import operator
import ast 
from pathlib import Path

class ExpressionEvaluator:
    def __init__(self):
        self.variables = {}#dict is here because you need to store values and variables which will be used in eval_()
        self.operators = {#this dict is here makes a match with functions -> operator 
            ast.Add:operator.add,
            ast.Sub:operator.sub,
            ast.Mult:operator.mul,
            ast.Div:operator.truediv,
            ast.USub:operator.neg
        }
    def assign(self,name:str, value:float):#def assign stores name and value becouse dict is keys:values
        self.variables[name] = value
    def evaluate(self,expr:str)-> float:#ast.parse splits an expression into a tree and takes 'root' of expression
        try:
            node = ast.parse(expr, mode='eval').body#.body its whole expression. Its property of expression that contains BinOp knot.
            return self._eval(node)#values return to _eval function and calculate
        except Exception as e:
            raise ValueError(f'Mistake in calculate of expression: {e}')
    def _eval(self,node):#calculator that calc expression 
        if isinstance(node, ast.BinOp):#ast.BinOp works with 2 + 3 * 4 and 2 + 3 expressions.Its knot of tree 
            left = self._eval(node.left)#left value of expression
            right = self._eval(node.right)#right value
            op_type = type(node.op)#operator like +, -, *, / 
            if op_type in self.operators:
                return self.operators[op_type](left,right)#here we call function by key and return result. Here we calc expression
        elif isinstance(node, ast.UnaryOp):#UnaryOp work with negative expressions 
            operand = self._eval(node.operand)
            op_type = type(node.op)
            return self.operators[op_type](operand)#return result
        elif isinstance(node, ast.Constant):# work with numbers without operators, so you return a number
            return node.value 
        elif isinstance(node, ast.Name):#that ast.Name work with variables like x,y,z. node.id strors like x = 1 in self varibles dict
            if node.id in self.variables:
                return self.variables[node.id]
            else:
                raise ValueError(f'Unknown variable: {node.id}')#if you wrote x and nothing you get a ValueError 
        else:
            raise TypeError(f'Unacceptable element')
if __name__ == '__main__':
    calc = ExpressionEvaluator()
    while True:
        user = input('>>>').strip()
        if user == 'exit':
            break
        if '=' in user:#calc the equation
            try:
                name,expr = user.split('=', 1)
                name = name.strip()
                expr = expr.strip()
                value =  calc.evaluate(expr)
                print(f'{name} = {value}')
                calc.assign(name,value)
            except Exception as e:
                print('Error:',e)
        else: 
            try:
                result = calc.evaluate(user)
                print(result)
            except Exception as e:
                print('Error:',e)

