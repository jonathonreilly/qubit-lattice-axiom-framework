#!/usr/bin/env python3
"""Independent exact local operator identities and a scope countercontrol."""
from pathlib import Path
from itertools import product
import json
import sys
sys.dont_write_bytecode=True
import sympy as s
from link_witness_check import INDEX,LOOKUP,hop,physical,matching_state,flux_divergence

HERE=Path(__file__).resolve().parent
# Basis order: tail qutrit, link spin, head qutrit; matter order 0,+,-;
# link order +,-. No torus initial state is used in these operator equations.
I3=s.eye(3);I2=s.eye(2)
Q=s.diag(0,1,-1);n=Q**2;q=I3-n
E=s.diag(s.Rational(1,2),-s.Rational(1,2))
U=s.Matrix([[0,1],[0,0]])
ap=s.zeros(3);ap[1,0]=1
am=s.zeros(3);am[2,0]=1
def tensor(a,b,c):return s.kronecker_product(a,b,c)
Gx=tensor(I3,E,I3)-tensor(Q,I2,I3)
Gy=-tensor(I3,E,I3)-tensor(I3,I2,Q)
Nr=tensor(n,I2,I3)+tensor(I3,I2,n)
F=tensor(I3,s.diag(0,1),I3)
hp=tensor(ap.T,U.T,ap)  # positive record tail->head lowers E
hm=tensor(am.T,U,am)    # negative record tail->head raises E
bp=tensor(ap,U,am)
bm=tensor(am,U.T,ap)
commutators={}
for name,O in [('hop_plus',hp),('hop_minus',hm),('birth_plus',bp),('birth_minus',bm)]:
    assert Gx*O-O*Gx==s.zeros(18) and Gy*O-O*Gy==s.zeros(18)
    change=2 if name.startswith('birth') else 0
    assert Nr*O-O*Nr==change*O
    commutators[name]={'both_local_Gauss_commutators':'0','record_number_change':change}
assert bp.T*bp==tensor(q,s.diag(0,1),q)
assert bm.T*bm==tensor(q,s.diag(1,0),q)
assert bp.T*bp+bm.T*bm==tensor(q,I2,q)
assert F*bp-bp*F==-bp and F*bm-bm*F==bm
assert F*hp-hp*F==hp and F*hm-hm*F==-hm
# F=Nrecord/2 is not in general a hopping-invariant sector. One negative
# link is a valid matching, but its positive endpoint can move forward.
e,sign=LOOKUP[(INDEX[(0,0,0)],INDEX[(1,0,0)])]
assert sign==1
mask=1<<e
initial=(flux_divergence(mask),mask)
assert physical(initial) and matching_state(initial)
out=hop(initial,INDEX[(1,0,0)],INDEX[(2,0,0)])
assert out is not None and physical(out)
assert initial[1].bit_count()==1 and out[1].bit_count()==2
assert sum(a!=0 for a in out[0])==2
assert not matching_state(out)
result={'basis_dimension':18,'operator_commutators':commutators,
        'birth_plus_loss_without_beta':'q_x q_y P_(E=-1/2)',
        'birth_minus_loss_without_beta':'q_x q_y P_(E=+1/2)',
        'sum_birth_losses_without_beta':'q_x q_y',
        'total_birth_hazard_on_vacant_edge':'beta, not 2 beta, when both supplied channels have coefficient sqrt(beta)',
        'F_changes':{'hop_plus_forward':1,'hop_minus_forward':-1,'birth_plus':-1,'birth_minus':1},
        'matching_sector_countercontrol':{'initial_negative_link':[[0,0,0],[1,0,0]],
            'legal_positive_hop':[[1,0,0],[2,0,0]],'initial_F':1,'final_F':2,'record_count':2,
            'conclusion':'Matching-sector geometry alone does not block hopping; the neutral witness needs its specific surrounding charge pattern.'}}
(HERE/'LOCAL_OPERATOR_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
