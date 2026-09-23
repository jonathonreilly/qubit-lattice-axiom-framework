"""Independent cube local-rule controls; no previous or author builder imported."""
from pathlib import Path
import hashlib,json,itertools,math
from collections import defaultdict
from fractions import Fraction
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
EDGES=[(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7)]
A={0,3,5,6};CHORDS=[5,8,9,10,11];TREE=[i for i in range(12) if i not in CHORDS]
q0=tuple(int(v in A) for v in range(8));zero=(0,)*12;SEED=(q0,zero)
INC=sp.zeros(8,12)
for e,(u,v) in enumerate(EDGES):INC[u,e]=1;INC[v,e]=-1
TREE_MINOR=INC[:7,TREE];assert abs(TREE_MINOR.det())==1

def fields(q,m=(0,)*5):
    source=sp.Matrix([q[v]-int(v in A) for v in range(8)])
    E=sp.zeros(12,1)
    for e,val in zip(CHORDS,m):E[e]=val
    sol=TREE_MINOR.inv()*(source-INC*E)[:7,0]
    for e,val in zip(TREE,sol):E[e]=val
    assert INC*E==source
    return tuple(map(int,E))

CYCLE=sp.Matrix.hstack(*(sp.Matrix(fields(q0,tuple(int(j==k) for j in range(5)))) for k in range(5)))
assert INC*CYCLE==sp.zeros(8,5)

def grade(q):return sum(q[a]==0 for a in A)
def physical(q,E,S=None):
    return all(sum((E[e] if u==v else -E[e] if w==v else 0) for e,(u,w) in enumerate(EDGES))==q[v]-int(v in A) for v in range(8)) and (S is None or max(map(abs,E))<=S)
def weight(E,k,S):
    if S is None:return Fraction(1)
    if abs(E)>S or abs(E+k)>S:return 0.
    return math.sqrt(max(0.,1-E*(E+k)/(S*(S+1))))

def hops(state,S=None):
    q,E=state
    for e,(u,v) in enumerate(EDGES):
        for origin,dest,direction in ((u,v,1),(v,u,-1)):
            if q[origin] and not q[dest]:
                k=-direction*q[origin];w=weight(E[e],k,S)
                if not w:continue
                qq=list(q);qq[dest]=qq[origin];qq[origin]=0
                EE=list(E);EE[e]+=k
                out=(tuple(qq),tuple(EE));assert physical(*out,S)
                yield out,-w,e,k

def hop(v,which_grade,S=None):
    out=defaultdict(complex)
    for state,c in v.items():
        for dest,w,e,k in hops(state,S):
            if grade(dest[0])==which_grade:out[dest]+=c*w
    return {s:c for s,c in out.items() if c}

def h2(v,S=None):return {s:-c for s,c in hop(hop(v,1,S),0,S).items()}
def h4(v,S=None):
    out=defaultdict(complex,h2(h2(v,S),S));z=v
    for w in (1,2,1,0):z=hop(z,w,S)
    for s,c in z.items():out[s]-=c/2
    return {s:c for s,c in out.items() if c}

def births(v,S=None,coherent=False):
    out=defaultdict(lambda:defaultdict(complex))
    for (q,E),c in hop(v,1,S).items():
        for e,(u,w) in enumerate(EDGES):
            if q[u] or q[w]:continue
            for sigma in (-1,1):
                a=weight(E[e],sigma,S)
                if not a:continue
                qq=list(q);qq[u]=sigma;qq[w]=-sigma
                if grade(qq):continue
                EE=list(E);EE[e]+=sigma
                dest=(tuple(qq),tuple(EE));assert physical(*dest,S)
                out[e if coherent else (e,sigma)][dest]-=c*a
    return {j:{s:c for s,c in v.items() if c} for j,v in out.items()}

def birth_adjoint(v,j,S=None):
    e,sigma=j;u,w=EDGES[e];middle={}
    for (q,E),c in v.items():
        if q[u]!=sigma or q[w]!=-sigma:continue
        a=weight(E[e],-sigma,S)
        if not a:continue
        qq=list(q);qq[u]=qq[w]=0;EE=list(E);EE[e]-=sigma
        middle[tuple(qq),tuple(EE)]=-c*a
    return hop(middle,0,S)

def loss(v,S=None):
    out=defaultdict(complex)
    for j,w in births(v,S).items():
        for s,c in birth_adjoint(w,j,S).items():out[s]+=c
    return {s:c for s,c in out.items() if c}

def plus(a,b,factor=1):
    out=defaultdict(complex,a)
    for s,c in b.items():out[s]+=factor*c
    return {s:c for s,c in out.items() if c}
def scalar(a,x):return {s:x*c for s,c in a.items()}
def inner(a,b):return sum(complex(c).conjugate()*b.get(s,0) for s,c in a.items())

def faces():
    answer=[]
    for bit in range(3):
        other=[j for j in range(3) if j!=bit]
        for fixed in (0,1):
            v=fixed<<bit;verts=[v,v^(1<<other[0]),v^(1<<other[0])^(1<<other[1]),v^(1<<other[1])]
            cycle=[0]*12
            for u,w in zip(verts,verts[1:]+verts[:1]):
                edge=(min(u,w),max(u,w));cycle[EDGES.index(edge)]=1 if u<w else -1
            assert INC*sp.Matrix(cycle)==sp.zeros(8,1)
            answer.append(tuple(cycle))
    return answer
FACES=faces()

def first_sector_controls():
    rotor=h4({SEED:1})
    expected={SEED:60}
    for cycle in FACES:
        for sign in (-1,1):expected[q0,tuple(sign*x for x in cycle)]=-2
    assert rotor==expected
    one=list(hops(SEED));two=hop(hop({SEED:1},1),2)
    assert len(one)==12 and len(two)==42 and inner(two,two)==168
    rows=[]
    for S in (1,2,4,8):
        assert h2({SEED:1},S)=={SEED:-12}
        assert h4({SEED:1},S)==expected
        assert loss({SEED:1},S)=={SEED:48}
        js=births({SEED:1},S);jc=births({SEED:1},S,True)
        assert len(js)==24 and all(inner(v,v)==2 for v in js.values())
        assert len(jc)==12 and all(inner(v,v)==4 for v in jc.values())
        plaq=(q0,FACES[0]);got=loss({plaq:1},S);C=S*(S+1)
        expected_loss=48-32/C+8/(C*C)
        assert len(got)==1 and abs(got[plaq]-expected_loss)<1e-12
        rows.append({'S':S,'zero_field_H2':-12,'zero_field_H4_diagonal':60,'zero_field_H4_oriented_face_outputs':12,
                     'zero_field_loss_without_kappa':48,'unit_plaquette_loss_without_kappa':float(got[plaq].real),
                     'formula_loss':expected_loss})
    # Exact H2 electric identity on a declared collection of physical fields.
    checked=[]
    for m in itertools.product((-1,0,1),repeat=5):
        E=fields(q0,m);S=max(1,max(map(abs,E)));C=S*(S+1)
        got=h2({(q0,E):1},S)
        target=-12+sum(e*e for e in E)/C
        assert set(got).issubset({(q0,E)}) and abs(got.get((q0,E),0)-target)<1e-12
        r=loss({(q0,E):1},S)
        assert set(r).issubset({(q0,E)}) and -1e-12<=r.get((q0,E),0).real<=48+1e-12
        checked.append({'m':m,'S':S})
    return {'first_sector_rows':rows,'N4_grade2_outputs':len(two),'Z_norm_squared':int(inner(two,two).real),
            'physical_field_samples':len(checked),'max_sample_spin':max(r['S'] for r in checked),
            'H4_rotor_formula':'60 I - 2 sum over six square faces (U_face+U_face_dagger)',
            'face_cycle_vectors':[list(f) for f in FACES]}

def clock_counterexample():
    # At S=1 all nonzero link weights are exactly one. Integer complex arithmetic
    # therefore gives this derivative with no quadrature or asymptotic fit.
    def generator(v):
        H=plus(scalar(h2(v,1),2),v,24)
        H=plus(H,h4(v,1));H=plus(H,v,-60)
        return plus(scalar(H,-1j),loss(v,1),-.5)
    v={SEED:1};a=generator(v);b=generator(a);c=generator(b)
    d1=2*inner(v,a).real;d2=2*inner(v,b).real+2*inner(a,a).real
    d3=2*inner(v,c).real+6*inner(a,b).real
    assert d1==-48 and d2==48**2 and d3==-48**3+96*14
    return {'parameters':{'S':1,'K':1,'delta':1,'kappa':1},'survival_derivative_1':d1,'survival_derivative_2':d2,
            'survival_derivative_3':d3,'Exp48_derivative_3':-48**3,
            'difference_from_Exp48_t_cubed_coefficient':(d3+48**3)/6,
            'conclusion':'Zero field does not have an exact finite-spin Exp(48 kappa) first clock. The ordinary joint-spin limiting first clock is exponential.'}

def all_words(number):
    result=[]
    for occupied in itertools.combinations(range(8),number):
        if not A.issubset(occupied):continue
        for minus in itertools.combinations(occupied,(number-4)//2):
            result.append(tuple(0 if i not in occupied else -1 if i in minus else 1 for i in range(8)))
    return result

def later_loss_controls():
    counts=[]
    for q in all_words(6):
        state=(q,fields(q));v={state:1};js=births(v);r=loss(v)
        assert len(js)==8 and all(len(out)==1 for out in js.values())
        assert r[state]==8 and sum(abs(c) for c in r.values())==16
        for j,out in js.items():
            back=birth_adjoint(out,j)
            assert len(back)==2 and all(c==1 for c in back.values())
            for (_,E),c in out.items():assert max(abs(a-b) for a,b in zip(E,state[1]))<=1
        counts.append({'q':list(q),'resolved_paths':len(js),'diagonal_loss':8,'absolute_Gram_column_sum':16})
    # A compact physical interference counterexample to the false upper bound 8 I.
    first=births({SEED:1})[(0,1)]
    seed=next(iter(first));r=loss({seed:1});other=max((s for s in r if s!=seed),key=lambda s:r[s].real)
    assert loss({other:1})[other]==8
    pair={seed:1/math.sqrt(2),other:1/math.sqrt(2)}
    expectation=inner(pair,loss(pair)).real
    assert expectation>8
    rows=[]
    for S in (2,4,8,16):
        if not all(physical(*s,S) for s in pair):continue
        val=inner(pair,loss(pair,S)).real
        rows.append({'S':S,'compact_two_state_loss_expectation':val})
    assert rows[-1]['compact_two_state_loss_expectation']>8
    return {'all_36_P_words':counts,'rotor_compact_pair_expectation':expectation,
            'off_diagonal_Gram_coefficient':r[other].real,
            'compact_pair_states':[{'q':list(q),'E':list(E)} for q,E in pair],
            'finite_spin_countercontrols':rows,
            'uniform_bound_proof':'Every resolved B column has at most one path and every output row at most two predecessors. Every input has eight paths. The nonnegative Gram absolute row/column sums are at most16, including physical boundary suppression. Thus 0<=R6_S<=16 I.',
            'coherent_loss':'Opposite newborn charge patterns have orthogonal output ranges for each edge, so resolved/coherent Gram sums agree.'}

def terminal_escape_counterexample():
    q=all_words(8)[0];e0=fields(q);cycle=tuple(map(int,CYCLE[:,0]))
    rows=[]
    for n in (4,8,16):
        E=tuple(a+n*b for a,b in zip(e0,cycle));S=max(map(abs,E))
        assert physical(q,E,S)
        assert not h2({(q,E):1},S) and not h4({(q,E):1},S) and not births({(q,E):1},S)
        rows.append({'n':n,'S':S,'max_abs_E':max(map(abs,E)),'N8_probability':1,'window_R2_probability':int(max(map(abs,E))<=2)})
    return {'rows':rows,'scope':'Logical topology counterexample in absorbing terminal states. These states are not asserted to be the outputs of the stipulated original initialization.'}

def main():
    result={'graph':{'edges':EDGES,'A':sorted(A),'chords':CHORDS,'tree_minor_determinant':int(TREE_MINOR.det()),'cycle_matrix':np.array(CYCLE).astype(int).tolist()},
            'first_sector':first_sector_controls(),'finite_clock_counterexample':clock_counterexample(),
            'later_loss':later_loss_controls(),'terminal_topology_counterexample':terminal_escape_counterexample()}
    (HERE/'CUBE_CONSEQUENCE_CONTROLS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
