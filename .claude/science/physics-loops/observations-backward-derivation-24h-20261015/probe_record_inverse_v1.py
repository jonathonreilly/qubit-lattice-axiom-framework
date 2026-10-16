"""Exact/synthetic controls for conditional record-law inverse reconstruction."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
import sympy as s

P=Path(__file__).resolve().parent
checks=[]
def check(name,ok,**data):
    assert bool(ok),name
    checks.append({'name':name,'passed':True,**data})

u,y,p,r=s.symbols('u y p r',positive=True)
for rr in [s.Rational(1,2),s.Integer(1),s.Integer(2),s.Integer(3)]:
    inv0=(p*y**rr)**(1/rr)
    inv1=(p+(1-p)*y**rr)**(1/rr)
    # Real-positive branch simplification is explicit; 0<p<1 and 0<y<1.
    for pp in [s.Rational(1,4),s.Rational(2,3)]:
        c0=s.powdenest((inv0**rr/p).subs(p,pp),force=True)
        c1=s.powdenest(((inv1**rr-p)/(1-p)).subs(p,pp),force=True)
        assert s.simplify(c0-y**rr)==0 and s.simplify(c1-y**rr)==0
check('CDF conjugate branch inverse identities',True,measures=4,probabilities=2)

def interval(word,policy):
    l=Q(0);w=Q(1);past=()
    for bit in word:
        pp=policy(past)
        if bit:l+=w*pp;w*=1-pp
        else:w*=pp
        past=past+(bit,)
    return l,w
fixed=lambda past:Q(1,3)
adaptive=lambda past:Q(1,4) if sum(past)%2==0 else Q(2,3)
for policy in [fixed,adaptive]:
    for n in range(1,9):
        intervals=sorted(interval(word,policy) for word in product([0,1],repeat=n))
        assert intervals[0][0]==0 and intervals[-1][0]+intervals[-1][1]==1
        assert all(a+w==b for (a,w),(b,v) in zip(intervals[:-1],intervals[1:]))
        assert sum(w for l,w in intervals)==1
check('fixed and adaptive cylinders form an exact partition',True,max_depth=8)

# A nonuniform physical-coordinate family is integrated through its CDF,
# rather than relabeling counts after simulation.
for rr in [Q(1,2),Q(1),Q(2),Q(3)]:
    for word in product([0,1],repeat=5):
        l,w=interval(word,adaptive)
        # Physical endpoints are l^(1/r),(l+w)^(1/r); their F_r mass is w.
        a=s.Rational(l.numerator,l.denominator)**(s.Rational(rr.denominator,rr.numerator))
        b=s.Rational((l+w).numerator,(l+w).denominator)**(s.Rational(rr.denominator,rr.numerator))
        mass=s.powdenest(b**s.Rational(rr.numerator,rr.denominator),force=True)-s.powdenest(a**s.Rational(rr.numerator,rr.denominator),force=True)
        assert s.simplify(mass-s.Rational(w.numerator,w.denominator))==0
check('different invariant measures give identical record cylinders',True,measures=4,words=32)

# Doubling after the conditional renewal map skips one initial bit at p=1/2.
for n in range(1,7):
    counts={word:0 for word in product([0,1],repeat=n)}
    for k in range(4**n):
        v=Q(2*k+1,2*4**n);word=[]
        for j in range(n):
            bit=int(v>=Q(1,2));word.append(bit)
            v=4*v;v-=v.numerator//v.denominator
        counts[tuple(word)]+=1
    assert set(counts.values())=={2**n}
check('nonmonotone post-map has same finite iid record law',True,max_depth=6,scope='Exact dyadic partition enumeration; proof gives all depths.')

v,z=s.symbols('v z',real=True)
pair=s.integrate(s.integrate(v-z,(z,0,v))+s.integrate(z-v,(z,v,1)),(v,0,1))
check('integrated Lipschitz conditional-TV constant',pair==s.Rational(1,3))

# rho=1+a(2v-1): q_I=1+b(2v-1), b=a*w/[1+a(2l+w-1)].
# Exact TV=|b|/4; compare with the general K*w/(6m) bound.
rows=[]
for aa in [Q(-3,4),Q(1,4),Q(3,4)]:
    K=2*abs(aa);m=1-abs(aa);max_ratio=Q(0)
    for n in range(1,9):
        for word in product([0,1],repeat=n):
            l,w=interval(word,adaptive)
            bar=1+aa*(2*l+w-1);b=aa*w/bar
            tv=abs(b)/4;bound=K*w/(6*m)
            assert tv<=bound
            max_ratio=max(max_ratio,tv/bound)
    rows.append({'initial_slope_parameter':str(aa),'max_actual_to_bound':str(max_ratio)})
check('conditional forgetting bound across every controlled history',True,max_depth=8,rows=rows)

rare=[]
for n in range(0,12):
    l,w=interval((0,)*n,lambda past:Q(1,2));prob=w*w
    bar=s.integrate(2*(s.Rational(w.numerator,w.denominator)*v),(v,0,1))
    conditional=s.simplify(2*s.Rational(w.numerator,w.denominator)*v/bar)
    nextprob=s.integrate(conditional,(v,0,s.Rational(1,2)))
    assert conditional==2*v and nextprob==s.Rational(1,4) and prob==Q(1,4**n)
    rare.append({'n':n,'history_probability':str(prob),'next_zero_probability':str(nextprob)})
check('rare-history failure of uniform conditional relaxation',True,rows=rare)

def standard_step(v):
    bit=int(v>=Q(1,2));return bit,2*v-bit
for n in range(1,9):
    for word in product([0,1],repeat=n):
        v=interval(word,lambda past:Q(1,2))[0]
        got=[]
        for i in range(n):bit,v=standard_step(v);got.append(bit)
        assert tuple(got)==word and v==0
        for i in range(4):bit,v=standard_step(v);assert bit==0 and v==0
check('every finite prefix has an eventually-zero exceptional point',True,max_depth=8)

result={'source_sha256':hashlib.sha256((P/'NETWORK_EVOLUTION_BLOCK06_v1.md').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'summary':{'passed':len(checks),'failed':0},'empirical_test':False,'scope':'Conditional inverse/forgetting theorems and explicit counterfamilies; no initial state, detector map or Born rule selected.'}
text=json.dumps(result,indent=2)+'\n';(P/'RECORD_INVERSE_CONTROLS_v1.json').write_text(text);print(text,end='')
