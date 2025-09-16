import sympy as sp
def factorize_expression(expr):


  x = sp.symbols('x')
  y = sp.symbols('y')
  try:
    expression= sp.simplify(expr)
    factored_expr = sp.factor(expr)
    return factored_expr
  except Exception as e:
    return str(e)


expression = [
  'x**2 +2*x + 1',
  'x**2 - 4 ',
  'x**2 +4*x+4',
  'x*y+x+y+1'
]

for expr in expression:
  factored_expr = factorize_expression(expr)
  print(f'Expression: {expr}')
  print(f'Factored Expression : {factored_expr}')
  print('----')



a = "owl" 
while not a .isprintable():
  print(a.upper())

else:

  print(a)

bomb = ["Bang","BOOM","pow"]

print(6*bomb)
print(5*bomb)
print(6*bomb)
print(5*bomb)

