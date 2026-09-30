"""Independent rational determinant-sign counts; no author code imports."""
from fractions import Fraction as Q
from pathlib import Path
import json
P=Path(__file__).parent

def inertia_det(diagonal,off):
    # Leading principal determinants, rather than LDL division pivots.
    older=Q(1);previous=diagonal[0]
    if not previous:raise ArithmeticError('zero leading determinant')
    signs=[1,1 if previous>0 else -1]
    for k in range(1,len(diagonal)):
        current=diagonal[k]*previous-off[k-1]**2*older
        if not current:raise ArithmeticError('zero leading determinant')
        signs.append(1 if current>0 else -1)
        older,previous=previous,current
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def finite(S,K,delta,E,alter_off=False):
    C=S*(S+1);x=delta/(K*C);lam=x*x*E/delta
    assert lam<1 and (1-lam)*(2-lam)>4*x
    ns=list(range(-S,S+1));diag=[4*K*n*n-E*(1+4*x-lam) for n in ns];off=[Q(0)]*(2*S)
    # Assemble Z*R^-1 Z by W2 row outer products, keeping only actual W2 states.
    for m in range(-S,S):
        d=1-Q(m*(m+1),C);r=(1-lam)*(2-lam)-4*x*d
        z=2*d;term=delta*z*z/r;i=m+S
        diag[i]-=term;diag[i+1]-=term;off[i]-=term
    if alter_off:off=[v*Q(99,100) for v in off]
    return inertia_det(diag,off)

def rotor(L,K,delta,E,alter_off=False):
    tail=4*K*(L+1)**2-8*delta
    assert E<tail
    beta=4*delta**2/(tail-E)
    diag=[4*K*n*n-4*delta-E for n in range(-L,L+1)]
    off=[-2*delta]*(2*L)
    if alter_off:off=[v*Q(99,100) for v in off]
    plain=inertia_det(diag,off)
    diag[0]-=beta;diag[-1]-=beta
    lower=inertia_det(diag,off)
    assert plain==lower, ('sandwich inconclusive',plain,lower)
    return plain

finite_rows=[json.loads(s) for s in (P/'rational_spectral_certificate.jsonl').read_text().splitlines()]
rotor_rows=[json.loads(s) for s in (P/'rotor_tail_certificate.jsonl').read_text().splitlines()]
results=[]
# Nontrivial ratio at S20 independently reconstructs 14 endpoint counts.
for row in finite_rows:
    if row['S']!=20 or Q(row['delta'])==1:continue
    intervals=[tuple(map(Q,iv)) for iv in row['energy_intervals']]
    counts=[[finite(row['S'],Q(row['K']),Q(row['delta']),e) for e in iv] for iv in intervals]
    assert counts==[[j,j+1] for j in range(7)]
    assert all(b-a==Q(2,10**9) for a,b in intervals)
    for j,(a,b) in enumerate(intervals[1:]):
        assert tuple(map(Q,row['gap_intervals'][j]))==(a-intervals[0][1],b-intervals[0][0])
    wrong_bracket=[finite(20,Q(1),Q(row['delta']),e+Q(1,1000)) for e in intervals[0]]
    wrong_coefficient=[finite(20,Q(1),Q(row['delta']),e,True) for e in intervals[0]]
    assert wrong_bracket!=[0,1] and wrong_coefficient!=[0,1]
    results.append(dict(type='finite',S=20,delta=row['delta'],counts=counts,shifted_ground_bracket_counts=wrong_bracket,off_diagonal_fault_counts=wrong_coefficient))
for row in rotor_rows:
    intervals=[tuple(map(Q,iv)) for iv in row['energy_intervals']]
    counts=[[rotor(row['L'],Q(row['K']),Q(row['delta']),e) for e in iv] for iv in intervals]
    assert counts==[[j,j+1] for j in range(7)]
    assert all(b-a==Q(2,10**9) for a,b in intervals)
    for j,(a,b) in enumerate(intervals[1:]):
        assert tuple(map(Q,row['gap_intervals'][j]))==(a-intervals[0][1],b-intervals[0][0])
    wrong=[rotor(row['L'],Q(row['K']),Q(row['delta']),e,True) for e in intervals[0]]
    assert wrong!=[0,1]
    results.append(dict(type='infinite_rotor',L=row['L'],delta=row['delta'],counts=counts,off_diagonal_fault_counts=wrong))
print(json.dumps(results,indent=2))

AUDIT_TIMEOUT_SEC = 180
