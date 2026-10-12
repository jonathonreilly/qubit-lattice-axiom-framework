"""Author controls: exact binary Pauli algebra, independent dense assembly.

Finite diagnostics only. No unbounded-domain/thermodynamic proof is numerical.
"""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/MICROSCOPIC_JOINT_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MICROSCOPIC_CURRENT_IMPLEMENTATION_BOUNDED_THEOREM_NOTE_2026-10-12.md"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from math import factorial, prod
import hashlib
import json
import platform

import numpy as np
from scipy.linalg import expm
import scipy

ZC = (F(0), F(0))
ONE = (F(1), F(0))
PHASE = [ONE, (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1))]
EMPTY = (frozenset(), frozenset())
ROWS = []


def cmul(a,b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def add(*polys):
    out={}
    for p in polys:
        for w,c in p.items():
            old=out.get(w,ZC);v=(old[0]+c[0],old[1]+c[1])
            if v != ZC: out[w]=v
            elif w in out:del out[w]
    return out


def scale(p,c):
    c=c if isinstance(c,tuple) else (F(c),F(0))
    return {w:cmul(c,v) for w,v in p.items() if cmul(c,v)!=ZC}


def word(items,c=1):
    x=frozenset(i for i,v in items if v in 'XY')
    z=frozenset(i for i,v in items if v in 'YZ')
    return {(x,z):(F(c),F(0))}


def multiply(p,q):
    out={}
    for (x,z),a in p.items():
        for (v,w),b in q.items():
            xx=x^v;zz=z^w
            power=(len(x&z)+len(v&w)-len(xx&zz)+2*len(z&v))%4
            out=add(out,{(xx,zz):cmul(cmul(a,b),PHASE[power])})
    return out


def comm(p,q):
    return add(multiply(p,q),scale(multiply(q,p),-1))


def shift(p,k):
    return {(frozenset(x+k for x in a),frozenset(x+k for x in b)):c
            for (a,b),c in p.items()}


def support(p):
    return set().union(*(a|b for a,b in p)) if p else set()


def deriv(a,density):
    sa=support(a);sd=support(density)
    if not sa or not sd:return {}
    return scale(add(*(comm(shift(density,k),a)
                       for k in range(min(sa)-max(sd),max(sa)-min(sd)+1))),PHASE[1])


def current(h):
    sh=support(h);radius=max(abs(x) for x in sh)
    return add(*(scale(comm(h,shift(h,k)),(F(0),F(k,2)))
                 for k in range(-2*radius,2*radius+1)))


def orbit_sums(p):
    out={}
    for w,c in p.items():
        sites=w[0]|w[1]
        if not sites:continue
        out=add(out,shift({w:c},-min(sites)))
    return out


def divergence_primitive(p):
    assert not orbit_sums(p)
    a={}
    for w,c in p.items():
        sites=w[0]|w[1]
        if not sites:continue
        v=min(sites);base=shift({w:c},-v)
        if v>0:a=add(a,*(scale(shift(base,k),-1) for k in range(v)))
        if v<0:a=add(a,*(shift(base,k) for k in range(v,0)))
    return a


def serial(p):
    rows=[]
    for (x,z),c in p.items():
        letters=' '.join(f'{"Y" if i in x and i in z else "X" if i in x else "Z"}{i}'
                         for i in sorted(x|z)) or 'I'
        rows.append({'word':letters,'real':str(c[0]),'imag':str(c[1])})
    return sorted(rows,key=lambda x:x['word'])


def l1(p):
    return sum(abs(c[0])+abs(c[1]) for c in p.values())


def record(name,ok,**data):
    row={'name':name,'passed':bool(ok),**data};ROWS.append(row)
    print(json.dumps(row,sort_keys=True),flush=True)


def algebra_controls():
    hbad=add(word([(0,'Z'),(1,'Z')]),word([(0,'X')]))
    pbad=current(hbad)
    pexpected=add(word([(0,'Z'),(1,'Y')],-1),word([(-1,'Z'),(0,'Y')],-1))
    record('negative_fixture_current_exact',pbad==pexpected,current=serial(pbad))
    simple=word([(0,'Z'),(1,'Y')],-2)
    record('current_density_improvement_is_null',not orbit_sums(add(pbad,scale(simple,-1))))
    qbad=deriv(pbad,hbad)
    qsimple=deriv(simple,hbad)
    qexpected=add(word([(1,'X')],-4),word([(0,'Y'),(1,'Y')],-4),
                  word([(0,'Z'),(1,'X'),(2,'Z')],-4),word([(0,'Z'),(1,'Z')],4))
    record('negative_fixture_q_density_exact',qsimple==qexpected,q=serial(qsimple))
    expected=add(word([(0,'Y')],-8),word([(-1,'Y'),(0,'X')],8),
                 word([(0,'X'),(1,'Y')],8),word([(-1,'Z'),(0,'Y'),(1,'Z')],-8))
    z=word([(0,'Z')]);actual=add(deriv(deriv(z,pbad),hbad),scale(deriv(deriv(z,hbad),pbad),-1))
    record('generic_current_conservation_mutant_rejected',actual==expected and bool(actual),
           commutator_action=serial(actual),exact_l1=str(l1(actual)))
    for letter in 'XYZ':
        a=word([(0,letter)])
        bracket=add(deriv(deriv(a,pbad),hbad),scale(deriv(deriv(a,hbad),pbad),-1))
        record('finite_jacobi_density_'+letter,bracket==deriv(a,qbad))
    hgood=add(word([(0,'X'),(1,'X')]),word([(0,'Y'),(1,'Y')]))
    pgood=current(hgood);qgood=deriv(pgood,hgood)
    zero=not orbit_sums(qgood)
    a=divergence_primitive(qgood) if zero else {}
    record('positive_xx_current_has_nonzero_null_density',bool(qgood) and zero,
           q=serial(qgood),orbit_sums=serial(orbit_sums(qgood)))
    record('positive_q_divergence_reconstruction',zero and qgood==add(a,scale(shift(a,1),-1)),
           primitive=serial(a))
    for letter in 'XYZ':
        probe=word([(0,letter)])
        bracket=add(deriv(deriv(probe,pgood),hgood),scale(deriv(deriv(probe,hgood),pgood),-1))
        record('positive_complete_site_basis_'+letter,not bracket and not deriv(probe,qgood))
    divergence=add(word([(0,'Z')]),word([(1,'Z')],-1))
    record('nonzero_density_does_not_imply_nonconservation',bool(divergence) and
           all(not deriv(word([(0,p)]),divergence) for p in 'XYZ'),density=serial(divergence))
    dropped=word([(0,'Z')])
    record('drop_divergence_term_detected',bool(deriv(word([(0,'X')]),dropped)),
           action=serial(deriv(word([(0,'X')]),dropped)))
    record('one_observable_test_is_insufficient',not deriv(word([(0,'Z')]),dropped) and
           bool(deriv(word([(0,'X')]),dropped)))
    return hgood,pgood,hbad,pbad,expected


def histories(seed,colors):
    states={frozenset(seed):1}
    for color in colors:
        length={'r':2,'b':3}[color];new=defaultdict(int)
        for union,count in states.items():
            starts={x-k for x in union for k in range(length)}
            for x in starts:new[union|frozenset(range(x,x+length))]+=count
        states=new
    return sum(states.values()),max(map(len,states)),len(states)


def mixed_controls():
    rejects=0
    for seed in [{0},{0,8}]:
        for colors in ['rb','br','rrrbbb','bbbrrr','rbrbrb']:
            count,size,nstates=histories(seed,colors);a=len(seed);n=len(colors)
            jprod=prod(2 if c=='r' else 3 for c in colors)
            bound=jprod*prod(a+2*k for k in range(n));wrong=jprod*a**n
            rejects+=count>wrong
            record('mixed_history_'+str(sorted(seed))+'_'+colors,count<=bound and size<=a+2*n,
                   count=count,bound=bound,max_union=size,states=nstates,
                   omitted_growth_bound=wrong,omitted_growth_detected=count>wrong)
    record('mixed_history_growth_mutant_detected',rejects>0,detected_cases=rejects)
    for n in [1,2,5,9]:
        a=3;r=2;x=F(1,20);y=F(1,10);p=prod(a+r*k for k in range(n))
        direct=sum(x**m*y**(n-m)*p/F(factorial(m)*factorial(n-m)) for m in range(n+1))
        grouped=(x+y)**n*p/F(factorial(n))
        record('mixed_majorant_binomial_'+str(n),direct==grouped,coefficient=str(direct),
               scope='Arithmetic grouping only; not independent evidence for the history bound')


I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.diag([1,-1]).astype(complex)
MATS={'X':X,'Y':Y,'Z':Z}


def tensor_word(items,n):
    d={i % n:p for i,p in items};v=np.array([[1]],dtype=complex)
    assert len(d)==len(items),'Control volume too small: support aliases'
    for i in range(n):v=np.kron(v,MATS[d[i]] if i in d else I)
    return v


def polynomial_dense(p,n):
    out=np.zeros((2**n,2**n),dtype=complex)
    for (x,z),c in p.items():
        items=[(i,'Y' if i in x and i in z else 'X' if i in x else 'Z') for i in sorted(x|z)]
        out+=complex(float(c[0]),float(c[1]))*tensor_word(items,n)
    return out


def norm(a):return float(np.linalg.norm(a,2))


def dense_controls(expected):
    n=6;dim=2**n
    for label in ['xx','zx']:
        hs=[]
        for k in range(n):
            if label=='xx':hs.append(tensor_word([(k,'X'),((k+1)%n,'X')],n)+
                                     tensor_word([(k,'Y'),((k+1)%n,'Y')],n))
            else:hs.append(tensor_word([(k,'Z'),((k+1)%n,'Z')],n)+tensor_word([(k,'X')],n))
        H=sum(hs)
        # Adjacent ordered pair once, independently of the sparse current code.
        P=sum(1j*(hs[k]@hs[(k+1)%n]-hs[(k+1)%n]@hs[k]) for k in range(n))
        C=H@P-P@H
        A=tensor_word([(0,'Z')],n)
        bracket=-(C@A-A@C)
        if label=='xx':record('dense_periodic_xx_commutes',norm(C)<1e-12,commutator_norm=norm(C),sites=n)
        else:record('dense_negative_current_action_matches_exact_polynomial',
                    norm(bracket-polynomial_dense(expected,n))<1e-12 and norm(bracket)>1,
                    residual=norm(bracket-polynomial_dense(expected,n)),action_norm=norm(bracket),sites=n)
        u=.037;v=.029;UH=expm(1j*u*H);UP=expm(1j*v*P)
        defect=norm(UH@UP-UP@UH)
        record('dense_unitary_product_'+label,defect<1e-12 if label=='xx' else defect>1e-3,
               defect=defect,u=u,v=v,
               reverse_order_is_nondiscriminating=(label=='xx'))
        # In tracial GNS both adjoint generators and their commutator kill I.
        omega=np.eye(dim)/np.sqrt(dim)
        vacuum_residual=norm(C@omega-omega@C)
        record('tracial_vacuum_only_test_'+label,vacuum_residual<1e-12 and
               (norm(bracket)>1 if label=='zx' else True),vacuum_residual=vacuum_residual,
               local_action_norm=norm(bracket),nondiscriminating_vacuum_test=True)
    # Discrete projective ambiguity at fixed group elements, not continuous
    # commuting one-parameter automorphism groups.
    AX=np.kron(X.conj(),X);AZ=np.kron(Z.conj(),Z)
    record('discrete_projective_implementers',norm(AX@AZ-AZ@AX)<1e-12 and norm(X@Z-Z@X)>1,
           adjoint_commutator=norm(AX@AZ-AZ@AX),unitary_commutator=norm(X@Z-Z@X),
           common_fixed_vector_dimension=int(2-np.linalg.matrix_rank(np.vstack([X-I,Z-I]))))


def main():
    *_,expected=algebra_controls();mixed_controls();dense_controls(expected)
    out={'recorded_utc':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),
         'role':'Author finite controls; independent review pending',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
         'rows':ROWS,'total':len(ROWS),'failed':sum(not x['passed'] for x in ROWS)}
    # Canonical execution reports through stdout; the original adjacent JSON and all calculations are preserved in the packet.
    print(json.dumps({k:out[k] for k in ['total','failed','source_sha256']}),flush=True)
    print('per_element: exact finite Pauli currents, Jacobi densities and local divergence identities are checked against stated fixtures.')
    print('per_site: a complete qubit one-site basis is exercised with finite support bookkeeping; no physical self-adjoint model is constructed.')
    print('per_mode: checked and not executed — no particle spectral mode, mass shell or asymptotic particle sector is tested by these controls.')
    print('per_block: finite mixed-color histories and six-site matrices are checked; finite predicates do not establish unbounded domains.')
    print('lattice_wide: checked and not executed — the thermodynamic and strong-commutation statements require the analytic conditional proof.')
    print("TOTAL: PASS=" + str(out["total"] - out["failed"]) + " FAIL=" + str(out["failed"]))
    print("SCOPE: Finite predicates only; no unbounded-domain, thermodynamic or physical-realization certificate.")
    raise SystemExit(bool(out['failed']))


if __name__=='__main__':main()
