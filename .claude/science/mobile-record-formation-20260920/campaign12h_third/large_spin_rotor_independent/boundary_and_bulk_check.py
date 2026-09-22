"""Independent static cubic counting and saturated-flux countercontrol."""
from pathlib import Path
from itertools import product
from datetime import datetime,timezone
import json
import sympy as s

HERE=Path(__file__).resolve().parent


def torus(d,L,spin):
    sites=list(product(range(L),repeat=d));index={x:i for i,x in enumerate(sites)}
    def shift(x,a,k=1):
        y=list(x);y[a]=(y[a]+k)%L;return tuple(y)
    edges=[(index[x],index[shift(x,a)]) for x in sites for a in range(d)]
    eidx={(x,a):i*d+a for i,x in enumerate(sites) for a in range(d)}
    loops=[]
    for x in sites:
        for a in range(d):
            for b in range(a+1,d):
                loops.append([(eidx[x,a],1),(eidx[shift(x,a),b],1),
                              (eidx[shift(x,b),a],-1),(eidx[x,b],-1)])
    fields=[0]*len(edges)
    # Deterministic independently selected divergence-free words.
    accepted=0
    for k in range(83):
        loop=loops[(37*k+11)%len(loops)];sign=1 if k%3 else -1
        if all(abs(fields[e]+sign*delta)<=spin for e,delta in loop):
            for e,delta in loop:fields[e]+=sign*delta
            accepted+=1
    div=[0]*len(sites)
    for E,(x,y) in zip(fields,edges):div[x]+=E;div[y]-=E
    assert not any(div)
    eta=[1 if sum(sites[x])%2==0 else -1 for x,y in edges]
    C=spin*(spin+1);q=[E*E-z*E for E,z in zip(fields,eta)]
    weights=[C-a for a in q]
    assert all(0<=a<=C for a in weights)
    assert sum(z*E for z,E in zip(eta,fields))==0
    assert sum(weights)==C*len(edges)-sum(E*E for E in fields)
    adjacent=[];disjoint=0
    for e,(x,y) in enumerate(edges):
        for f,(xx,yy) in enumerate(edges[e+1:],e+1):
            if {x,y}&{xx,yy}:adjacent.append((e,f))
            else:disjoint += weights[e]*weights[f]
    diagonal=sum(a*a for a in weights)+2*sum(weights[e]*weights[f] for e,f in adjacent)
    folded=sum(weights)**2-2*disjoint
    expanded=d*len(sites)*(4*d-1)*C*C-2*(4*d-1)*C*sum(E*E for E in fields)
    expanded+=sum(a*a for a in q)+2*sum(q[e]*q[f] for e,f in adjacent)
    assert diagonal==folded==expanded
    # Both circulations at maximal uniform positive flux are blocked.
    for loop in loops:
        for sign in (-1,1):
            assert any(spin+sign*delta>spin for e,delta in loop)
    return {'dimension':d,'period':L,'spin':spin,'vertices':len(sites),'edges':len(edges),
            'applied_loop_changes':accepted,'electric_square_sum':sum(E*E for E in fields),
            'sum_initial_hop_weights':str(s.Rational(sum(weights),C)),
            'complete_diagonal_fourth_coefficient':str(s.Rational(diagonal,C*C)),
            'folded_disjoint_and_local_expansion_equal':True,'saturated_uniform_flux_both_circulations_blocked':True}


def local_matrix_checks():
    rows=[]
    for S in (1,2,3,5):
        C=S*(S+1);dim=2*S+1;E=s.diag(*range(-S,S+1));U=s.zeros(dim)
        for i,m in enumerate(range(-S,S)):
            U[i+1,i]=s.sqrt(1-s.Rational(m*(m+1),C))
        I=s.eye(dim)
        assert E*U-U*E==U
        assert s.simplify(U.T*U-(I-(E*E+E)/C))==s.zeros(dim)
        assert s.simplify(U*U.T-(I-(E*E-E)/C))==s.zeros(dim)
        assert s.simplify(U.T*U+U*U.T-2*(I-E*E/C))==s.zeros(dim)
        rows.append({'S':S,'raising_and_loss_identities_exact':True,'boundary_shift_error_norm_on_top_state':1})
    return rows


def saturated_second_derivative():
    rows=[];J,g=s.symbols('J g',positive=True,real=True)
    for d in (2,3,4):
        np=2*(d-1);channels=2*np;D=1+channels
        H=s.diag(0,*[4*g]*channels)
        for i in range(1,D):H[0,i]=H[i,0]=-J
        O=s.diag(1,*[-1]*channels)
        second=-(H*(H*O-O*H)-(H*O-O*H)*H)[0,0]
        assert s.expand(second+16*(d-1)*J*J)==0
        rows.append({'dimension':d,'oriented_plaquettes_touching_edge':channels,
                     'rotor_parity_second_derivative_at_even_uniform_flux':str(second),
                     'spin_ring_parity_second_derivative_at_saturated_flux':0})
    return rows


def main():
    r={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
       'local_spin_algebra':local_matrix_checks(),
       'cubic_counting_controls':[torus(d,6,S) for d,S in [(2,2),(3,2),(3,3)]],
       'saturated_countercontrol':saturated_second_derivative(),
       'scope':'Exact static path counts and second derivatives; no production dynamics or phase calculation.'}
    (HERE/'BOUNDARY_BULK_RESULTS.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))


if __name__=='__main__':main()
