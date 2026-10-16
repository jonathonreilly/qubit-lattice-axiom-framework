"""Conditional game and covariance controls, with an exposed literature comparator."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,math
import sympy as s
import mpmath as mp

P=Path(__file__).resolve().parent;checks=[]
def check(name,ok,**kw):
    assert bool(ok),name
    checks.append({'name':name,'passed':True,**kw})

strategies=list(product([0,1],repeat=4))
scores=[]
for a0,a1,b0,b1 in strategies:
    scores.append(sum(((a0,a1)[x]^(b0,b1)[y])==x*y for x,y in product([0,1],repeat=2)))
check('all deterministic local response tables',max(scores)==3 and set(scores)=={1,3},tables=16)
for tx,ty in product([F(0),F(1,100),F(1,5),F(1,2)],repeat=2):
    maximum=F(0)
    for sx,sy in product([-1,1],repeat=2):
        px=F(1,2)+sx*tx;py=F(1,2)+sy*ty
        probs={(x,y):(px if x else 1-px)*(py if y else 1-py) for x,y in product([0,1],repeat=2)}
        for a0,a1,b0,b1 in strategies:
            score=sum(prob for (x,y),prob in probs.items() if ((a0,a1)[x]^(b0,b1)[y])==x*y)
            maximum=max(maximum,score)
    assert maximum==1-(F(1,2)-tx)*(F(1,2)-ty)
check('conditional independent input-bias bound is sharp',True,bias_pairs=16)

bad_tau=F(3,4)
check('out-of-domain bias counterexample preserved',F(1)>1-(F(1,2)-bad_tau)**2,loose_tau=str(bad_tau))

def tail(N,k,q):
    if k<=0:return F(1)
    if k>N:return F(0)
    return sum(F(math.comb(N,j))*q**j*(1-q)**(N-j) for j in range(k,N+1))
q=F(3,4)
for N in range(1,14):
    for k in range(0,N+2):
        hi=tail(N-1,k-1,q);lo=tail(N-1,k,q)
        assert hi>=lo
        assert max(pp*hi+(1-pp)*lo for pp in [F(0),q/2,q])==tail(N,k,q)
check('fixed-horizon adversarial-memory induction',True,max_horizon=13)

mp.mp.dps=65;tau=mp.mpf('1.08e-5');qmp=mp.mpf(3)/4+tau-tau*tau
literature_tail=mp.fsum(mp.binomial(245,j)*qmp**j*(1-qmp)**(245-j) for j in range(196,246))
check('published-input tail reconstruction',mp.mpf('.038')<literature_tail<mp.mpf('.040'),N=245,wins=196,tau=str(tau),conditional_win_bound=str(qmp),tail=str(literature_tail),game_score=str(F(8)*(F(196,245)-F(1,2))),data_role='exposed published summary, no raw-data or independent empirical test')

axes_a=[s.Matrix([0,0,1]),s.Matrix([1,0,0])]
axes_b=[s.Matrix([-1,0,-1])/s.sqrt(2),s.Matrix([1,0,-1])/s.sqrt(2)]
rows=[]
for gamma in [s.Rational(1,2),1,2,3]:
    Es=[]
    for a,b in product(axes_a,axes_b):
        dot=s.simplify(a.dot(b));E=-s.sign(dot)*abs(dot)**gamma
        probs={(r,ss):s.simplify((1+r*ss*E)/4) for r,ss in product([-1,1],repeat=2)}
        assert s.simplify(sum(probs.values())-1)==0 and all(v>=0 for v in probs.values())
        for r in [-1,1]:assert s.simplify(sum(probs[r,ss] for ss in [-1,1])-s.Rational(1,2))==0
        for ss in [-1,1]:assert s.simplify(sum(probs[r,ss] for r in [-1,1])-s.Rational(1,2))==0
        Es.append(E)
    schsh=s.simplify(Es[0]+Es[1]+Es[2]-Es[3]);expected=4*(1/s.sqrt(2))**gamma
    assert s.simplify(abs(schsh)-expected)==0
    rows.append({'gamma':str(gamma),'CHSH_magnitude':str(expected),'numeric':float(expected)})
check('rotation-invariant no-signaling counterfamily',True,rows=rows,scope='Pair tables only; no multisystem composition or physical implementation asserted.')

# Axial covariance plus axis reversal and aligned calibration, in a supplied
# affine vector-state model, leaves the coefficient k=1.
dx,dy,dz,c=s.symbols('dx dy dz c',real=True)
rot90=s.Matrix([[0,-1,0],[1,0,0],[0,0,1]])
d=s.Matrix([dx,dy,dz]);sol=s.solve(list(rot90*d-d)+[2*c,c+dz-1],[dx,dy,dz,c],dict=True)
check('affine response coefficient at the reference axis',sol==[{c:0,dx:0,dy:0,dz:1}],solution=str(sol))
for gamma in [s.Rational(1,2),1,2,3]:
    first=(1/s.sqrt(2))**gamma;second=1/s.sqrt(2)
    assert (s.simplify(first-second)==0)==(gamma==1)
check('two history mixtures expose the sufficient-state premise',True)

result={'source_sha256':hashlib.sha256((P/'NETWORK_EVOLUTION_BLOCK08_v2.md').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'summary':{'passed':len(checks),'failed':0},'empirical_test':False,'scope':'Known causal/game reconstruction plus explicit pair-law counterfamily and conditional affinity selector; no network law or initial state derived.'}
text=json.dumps(result,indent=2)+'\n';(P/'CAUSAL_NEIGHBORHOOD_CONTROLS_v2.json').write_text(text);print(text,end='')
