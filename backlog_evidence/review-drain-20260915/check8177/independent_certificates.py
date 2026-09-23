import resource, signal
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
signal.alarm(180)
from fractions import Fraction
from itertools import product
import ast, pathlib
s=pathlib.Path('/private/tmp/review-drain-20260915/drain-author-slot/scripts/admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17.py')
tree=ast.parse(s.read_text())
certnode=next(n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='certs' for t in n.targets))
certs=eval(compile(ast.Expression(certnode),str(s),'eval'),{'Fraction':Fraction})
def slot(n,a,b):
 return sum((a**q.count('P')*b**q.count('A') for q in product('EPA',repeat=n) if q.count('P')<=1),Fraction())
for (c,p,q,r),(t,D,U,F) in certs.items():
 e1=Fraction(q**3+4*r**3,p**3+q**3+4*r**3)
 e2=max(Fraction(p*q*q+4*r**3,p*q*(p+q)+4*r**3),Fraction(r*q*q+r*r*(p+q)+2*r**3,r*(p*p+q*q)+r*r*(p+q)+2*r**3))
 a=t*U;b=e2*U/t**c;f=1+e1*F/t**3;down=1+3*(t+e2/t**c)*D
 computed=(slot(2,a,b)*down*f**6,slot(3,a,b)*f**6,slot(3,a,b)*down*f**5)
 assert all(x>=y for x,y in zip((D,U,F),computed))
 assert e1*slot(3,a,b)*down*f**6<Fraction(1,10**5)
 print('certificate',c,p,q,r,'PASS')
# A D entry reached from a processed successor leaves zero processed capacity.
exact=sum(1 for z in product('EPA',repeat=2) if z.count('P')==0)
relaxed=sum(1 for z in product('EPA',repeat=2) if z.count('P')<=1)
assert (exact,relaxed)==(4,8)
print('D entry processed incoming child: exact remaining assignments',exact,'formula assignments',relaxed,'OVERCOUNT CONFIRMED')
