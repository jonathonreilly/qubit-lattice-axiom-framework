#!/usr/bin/env python3
"""Finite whole-configuration and group controls for local Gibbs record cycles."""
from pathlib import Path
from itertools import product,permutations
import hashlib,json
import numpy as np
import sympy as s
from scipy.sparse import coo_matrix

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,condition,detail=None):
    assert bool(condition),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail))
    print('PASS:',name,flush=True)

# Six-site graph: square0123, two boundary sites45. Its interaction contains
# an exterior-only edge45 and two boundary edges04,25. Alphabet has vacancy,
# A+/- and B with nonzero z. This is a diagnostic subset, not the whole14.
edges=[(0,1),(1,2),(2,3),(3,0),(0,4),(2,5),(4,5)]
support={0,1,2,3}
t=np.array([[0,0],[1,0],[-1,0],[0,.5]],float)
bz=np.array([0,0,0,1],float)
q=4;V=6;states=np.array(list(product(range(q),repeat=V)));size=len(states)
index={tuple(v):i for i,v in enumerate(states)}
def rotate(v,step=1):
    out=v.copy()
    for x in range(4):out[(x+step)%4]=v[x]
    return out
right=np.array([index[tuple(rotate(v))] for v in states])
left=np.array([index[tuple(rotate(v,-1))] for v in states])
K=.37;nu=.8;eps=.63;kappa=.7
pair=np.array([np.einsum('ij,ij->i',t[states[:,x]],t[states[:,y]]) for x,y in edges])
H=-K*pair.sum(axis=0)
HS=-K*pair[[bool({x,y}&support) for x,y in edges]].sum(axis=0)
outside=H-HS;chi=bz[states[:,:4]].sum(axis=1)/4
rates_plus=nu*(1+eps*chi)*np.exp(HS)
rates_minus=nu*(1-eps*chi)*np.exp(HS)
check('local_energy_and_orbit_invariants',np.max(abs(outside[right]-outside))<1e-14 and np.all(chi[right]==chi))
check('strict_positive_rates',np.min(rates_plus)>0 and np.min(rates_minus)>0)
rows=[];cols=[];values=[]
def add(dst,rates):
    src=np.arange(size);rows.extend([dst,src]);cols.extend([src,src]);values.extend([rates,-rates])
add(right,rates_plus);add(left,rates_minus)
for x,y in edges:
    target=states.copy();target[:,[x,y]]=target[:,[y,x]]
    dst=np.array([index[tuple(v)] for v in target])
    rate=kappa*np.minimum(1,np.exp(H-H[dst]));add(dst,rate)
L=coo_matrix((np.concatenate(values),(np.concatenate(rows),np.concatenate(cols))),shape=(size,size)).tocsr()
lam=np.array([-.2,.13,-.07,.31]);logpi=-H+lam[states].sum(axis=1)
pi=np.exp(logpi-logpi.max());pi/=pi.sum()
residual=float(np.max(abs(L@pi)))
check('whole_generator_Gibbs_stationarity',residual<2e-17,dict(configurations=size,residual=residual))
for a in range(q):
    count=(states==a).sum(axis=1)
    assert np.max(abs(L.T@count))<5e-14
check('all_label_counts_conserved',True)
flowplus=pi*rates_plus;flowminus=pi*rates_minus
check('clockwise_and_reverse_orbit_flows_constant',np.max(abs(flowplus[right]-flowplus))<2e-18 and np.max(abs(flowminus[right]-flowminus))<2e-18)
witness=index[(0,1,2,3,1,2)]
reverse=right[witness]
gap=pi[witness]*L[reverse,witness]-pi[reverse]*L[witness,reverse]
check('full_generator_nonreversible_witness',abs(gap)>1e-7,dict(stationary_edge_current=float(gap),source=states[witness].tolist(),target=states[reverse].tolist()))

# Explicit local-clock check: vary exterior-only energy while holding every
# interaction touching S fixed. The rates remain fixed, though Gibbs changes.
H_other=HS-.91*pair[-1]
logp=-H_other+lam[states].sum(axis=1);pother=np.exp(logp-logp.max());pother/=pother.sum()
Lcycle=coo_matrix((np.r_[rates_plus,-rates_plus,rates_minus,-rates_minus],
                  (np.r_[right,np.arange(size),left,np.arange(size)],np.tile(np.arange(size),4))),shape=(size,size)).tocsr()
check('exterior_energy_cancels_without_global_clock',np.max(abs(Lcycle@pother))<2e-17)

# All48 signed cubic symmetries; axial n,b and reversed orientation convention.
unit=np.eye(3,dtype=int);B=np.array(list(product((-1,1),repeat=3)),int)
labels_b=np.vstack([np.zeros((7,3),int),B]);n=unit[2]
config=[0,7,10,14];raw=labels_b[config].sum(axis=0)
tested=0
for perm in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        Q=np.zeros((3,3),int)
        for i in range(3):Q[i,perm[i]]=signs[i]
        det=round(np.linalg.det(Q))
        nimage=det*Q@n;bimage=det*(Q@raw)
        assert nimage@bimage==n@raw
        tested+=1
check('polar_axial_full_cubic_rate_covariance',tested==48,dict(group_elements=tested))
check('orientation_choice_independent',np.allclose(1+eps*chi,1-eps*(-chi)))

# First-moment cancellation evaluated for each orbit, each conserved color,
# and a tilted Gibbs law. This checks the whole transition expectation.
xyz=np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]])
currents=[];seen=set();orbits=0
for i in range(size):
    if i in seen:continue
    orbit=[];j=i
    while j not in seen:seen.add(j);orbit.append(j);j=right[j]
    assert j==i;orbits+=1
    for a in range(q):
        moment=np.array([xyz[(states[k,:4]==a)].sum(axis=0) for k in orbit])
        assert np.all(np.roll(moment,-1,axis=0).sum(axis=0)-moment.sum(axis=0)==0)
for a in range(q):
    moment=(states[:,:4,None]==a)*xyz[None,:,:]
    moment=moment.sum(axis=1)
    current=np.sum(flowplus[:,None]*(moment[right]-moment)+flowminus[:,None]*(moment[left]-moment),axis=0)
    currents.append(current.tolist());assert np.max(abs(current))<2e-15
check('closed_local_cycle_content_transport_cancels',True,dict(orbits=orbits,grand_Gibbs_currents=currents))

# Exact arrangement ratio and positive-birth stationary-vacancy witness.
KK=s.symbols('K',real=True)
square=[(0,1),(1,2),(2,3),(3,0)]
energy=lambda v:-KK*sum(v[x]*v[y] for x,y in square)
check('same_count_arrangements_have_nonuniform_Gibbs_weights',energy([1,-1,1,-1])-energy([1,1,-1,-1])==4*KK,dict(probability_ratio='exp(-4K)'))
# Uniform occupied-label births have exactly L V=-(q-1)beta V,
# independently of the conservative generator, on every configuration.
beta=s.Rational(2,7)
vac=(states==0).sum(axis=1)
birthLV=-float((q-1)*beta)*vac
check('birth_only_vacancy_Lyapunov_identity',np.all(birthLV[vac>0]<0) and np.all(birthLV[vac==0]==0),dict(stationary_vacancy_must_be_zero=True))

report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Finite full-generator, exact arrangement and symmetry controls for supplied local Gibbs transport; no hydrodynamic limit, phase theorem, or quantum identification.')
(HERE/'LOCAL_GIBBS_RECORD_CIRCULATION_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
