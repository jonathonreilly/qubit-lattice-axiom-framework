import itertools,json,time
from pathlib import Path
from fractions import Fraction as F
import sympy as s
start=time.monotonic()
rows=[]
for t in range(1,9):
    errors=0;total=0
    for initial in itertools.product(range(2),repeat=2):
        for route in itertools.product(range(2),repeat=t):
            cache=list(initial)
            for j in route: cache[j]=0
            errors+=cache[0]!=cache[1];total+=1
    assert F(errors,total)==F(1,2**t)
    rows.append({'t':t,'error':str(F(errors,total))})
# Four mismatch states, not author 16-state settings-plus-cache chain.
stationary=[]
for v in [s.Rational(1,8),s.Rational(1,2),s.Rational(3,4),s.Integer(1)]:
  for q in [s.Rational(1,5),s.Rational(1,2),s.Rational(4,5)]:
    states=list(itertools.product(range(2),repeat=2)); T=s.zeros(4)
    for i,m in enumerate(states):
      for flips in states:
        prob=s.prod(v if f else 1-v for f in flips)
        for j,w in [(0,q),(1,1-q)]:
          new=[a^b for a,b in zip(m,flips)];new[j]=0
          T[i,states.index(tuple(new))]+=prob*w
    a,b,c,d=s.symbols('a b c d'); pi=s.Matrix([a,b,c,d])
    sol=s.solve(list(T.T*pi-pi)+[sum(pi)-1],[a,b,c,d])
    pi=pi.subs(sol)
    win=sum(pi[i] for i,m in enumerate(states) if m[0]==m[1])
    rho=1-2*v
    predicted=(1+q*(1-q)*rho*(1/(1-q*rho)+1/(1-(1-q)*rho)))/2
    assert s.simplify(win-predicted)==0
    stationary.append({'nu':str(v),'q':str(q),'win':str(win)})
# Explicit context-selected exception to an unconditional event-rate formulation.
exception_rows=[{'x':x,'y':y,'exception':x^y,'output':x^y if x^y else 0} for x,y in itertools.product(range(2),repeat=2)]
result={'exact_transients':rows,'mismatch_stationary':stationary,'exception_counterexample':{'rows':exception_rows,'lambda':'1/2','win':'1','claimed_without_selection_condition':'3/4'},'elapsed_seconds':time.monotonic()-start}
Path(__file__).with_name('independent_results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
