#!/usr/bin/env python3
"""Finite block unitary controls; no campaign model or bilateral implementation.
The infinite translation formula is used only to compare a buffered input.
"""
from pathlib import Path
from itertools import product
import json
import numpy as np
import sympy as s
from scipy.sparse import csr_matrix

HERE=Path(__file__).resolve().parent
LABELS=((0,0),(0,0),(1,0),(1,0),(0,1),(0,1))
D=len(LABELS)

def rotation(i,j):
    u=s.eye(D);u[i,i]=u[j,j]=s.Rational(3,5)
    u[i,j]=-s.Rational(4,5);u[j,i]=s.Rational(4,5)
    return u

phase=s.diag(1,1,1,s.I,1,1)
U1=rotation(0,2)*rotation(2,4)*rotation(0,5)*phase
U2=rotation(0,4)*rotation(1,3)*rotation(2,5)
assert U1.conjugate().T*U1==s.eye(D)
assert U2.conjugate().T*U2==s.eye(D)

def blocks(L):
    coords=tuple(product(range(L+2),repeat=2));index={n:i for i,n in enumerate(coords)}
    grouped={}
    for i,v in enumerate(LABELS):
        for n in coords:
            m=tuple(x+y for x,y in zip(n,v))
            grouped.setdefault(m,[]).append((i,i*len(coords)+index[n]))
    return coords,grouped

def finite_lift(u,L,exact=False):
    coords,grouped=blocks(L);dim=D*len(coords)
    rows=[];cols=[];vals=[]
    for m,entries in grouped.items():
        complete=all(1<=x<=L+1 for x in m)
        if complete:
            assert sorted(i for i,_ in entries)==list(range(D))
            by_i=dict(entries)
            for i in range(D):
                for j in range(D):
                    if u[i,j]!=0:
                        rows.append(by_i[i]);cols.append(by_i[j]);vals.append(u[i,j])
        else:
            for _,idx in entries:rows.append(idx);cols.append(idx);vals.append(1)
    if exact:
        return s.SparseMatrix(dim,dim,{(i,j):v for i,j,v in zip(rows,cols,vals)})
    return csr_matrix((np.asarray(vals,dtype=complex),(rows,cols)),shape=(dim,dim))

# Entire finite-space identities, not just the buffered initial subspace.
L0=2
V1=finite_lift(U1,L0,True);V2=finite_lift(U2,L0,True)
V12=finite_lift(U2*U1,L0,True)
assert V1.conjugate().T*V1==s.eye(V1.rows)
assert V2*V1==V12
coords,_=blocks(L0)
E1,E2=s.sqrt(2),s.sqrt(3)
hs=[E1*v[0]+E2*v[1] for v in LABELS]
hr=[E1*n[0]+E2*n[1] for n in coords]
ht=[a+b for a in hs for b in hr]
for (i,j),v in V1.todok().items():
    assert s.expand((ht[i]-ht[j])*v)==0
# A cyclic wrap would violate energy conservation; it is not our boundary rule.
wrong_wrap_change=s.simplify(E1+(L0+1)*E1)
assert wrong_wrap_change!=0

u1=np.asarray(U1,dtype=complex);u2=np.asarray(U2,dtype=complex);ut=u2@u1
rows=[]
for L in (3,7,15,31):
    coords,_=blocks(L);nb=len(coords)
    b=np.zeros(L+2)
    b[1:L+1]=np.sqrt(2/(L+1))*np.sin(np.pi*np.arange(1,L+1)/(L+1))
    beta=np.kron(b,b)
    assert abs(np.vdot(beta,beta)-1)<2e-14
    overlap=float(np.dot(b[1:],b[:-1]))
    assert abs(overlap-np.cos(np.pi/(L+1)))<2e-14
    d1=2*np.sin(np.pi/(2*(L+1)))
    embed=np.kron(np.eye(D),beta[:,None])
    v1=finite_lift(u1,L);v2=finite_lift(u2,L)
    actual=v2@(v1@embed)
    one=finite_lift(ut,L)@embed
    assert np.max(np.abs(actual-one))<2e-14
    ideal=embed@ut
    diff=actual-ideal
    isometry_error=float(np.sqrt(max(0,np.linalg.eigvalsh(diff.conj().T@diff)[-1])))
    assert isometry_error<=2*d1+2e-13
    # Maximally entangled input supplies a reference-sensitive density control.
    psi=(actual/np.sqrt(D)).reshape(D,nb,D)
    rho=np.einsum('anr,bns->arbs',psi,psi.conj()).reshape(D*D,D*D)
    target=(ut/np.sqrt(D)).reshape(-1)
    density_difference=rho-np.outer(target,target.conj())
    reference_error=float(np.sum(np.abs(np.linalg.eigvalsh(density_difference))))
    eta=min(2,4*d1)
    assert reference_error<=eta+2e-12
    # Energy balance for a coherent arbitrary input, with flags in its six-vector.
    x=np.asarray([1,1j,2,-1,0.5,1-1j],complex);x/=np.linalg.norm(x)
    out=(actual@x).reshape(D,nb)
    hn=np.asarray([float(a) for a in hs])
    rn=np.asarray([np.sqrt(2)*n[0]+np.sqrt(3)*n[1] for n in coords])
    initial=float(np.dot(abs(x)**2,hn)+np.dot(abs(beta)**2,rn))
    final=float(np.dot(np.sum(abs(out)**2,axis=1),hn)+np.dot(np.sum(abs(out)**2,axis=0),rn))
    expected_supply=(L+1)/2*(np.sqrt(2)+np.sqrt(3))
    assert abs(np.dot(abs(beta)**2,rn)-expected_supply)<2e-12
    assert abs(initial-final)<2e-12
    rows.append({'L':L,'battery_dimension':nb,'total_dimension':D*nb,
       'nearest_shift_overlap':overlap,'isometry_operator_norm_error':isometry_error,
       'proved_isometry_bound':float(2*d1),'reference_input_trace_norm_error':reference_error,
       'proved_channel_bound':float(eta),'initial_battery_mean':expected_supply,
       'energy_balance_residual':abs(initial-final),
       'same_battery_composition_residual':float(np.max(abs(actual-one)))})

result={'scope':'Two arbitrary six-dimensional unitaries, two noncommensurate positive gaps, genuine finite battery boundaries',
 'exact_small_L':L0,'exact_full_unitarity':True,'exact_composition':True,
 'exact_energy_commutation':True,'wrong_cyclic_wrap_energy_change':str(wrong_wrap_change),
 'rows':rows,'claim_status':'Author consistency control; analytic arbitrary-dimension proof is in the note'}
(HERE/'FINITE_BATTERY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
