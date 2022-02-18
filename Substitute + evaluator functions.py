import re

opp_sign = lambda i: '+-'[i>0]+str(abs(i))


def repl(n,st):
  return re.sub(r'x(\^?)',lambda c: f"*({n}){'**' if c[1] else ''}",re.sub(r'((?<=\D)|(?<=^))(?=x)','1',st))


def solve():

  st,roots = input("your polynomial, please: "),[]
  end =int(re.search(r'(\d+)$',st)[1])

  for i in range(1,end+1):

  if end%i==0:
    if eval(repl(i,st)) == 0: roots.append(i)
  if end%-i==0:
    if eval(repl(-i,st)) == 0: roots.append(-i)

	return'solutions: '+str(sorted(roots))
