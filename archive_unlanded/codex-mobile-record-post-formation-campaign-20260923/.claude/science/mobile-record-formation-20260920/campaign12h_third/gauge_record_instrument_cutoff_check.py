#!/usr/bin/env python3
"""Bounded exact operator checks and finite cyclic/reference diagnostics.

The all-size history estimate is the separate analytic proof. Numerics here
do not prove that estimate, identify a physical phase, or certify rounding.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar
from scipy import sparse
from scipy.sparse.linalg import expm_multiply

OUT=Path(__file__).resolve().parent


def rep(e,s):return (e+s)%(2*s+1)-s


def shift2(s,delta):
    basis=list(itertools.product(range(-s,s+1),repeat=2))
    lookup={v:i for i,v in enumerate(basis)}
    u=np.zeros((len(basis),len(basis)),dtype=np.int64)
    for col,v in enumerate(basis):
        u[lookup[tuple(rep(v[j]+delta[j],s) for j in range(2))],col]=1
    return u,basis


def exact_event_bounds():
    rows=[]
    for s in (2,3,4):
        u,basis=shift2(s,(1,0));w,_=shift2(s,(1,1));dim=len(basis)
        eye=np.eye(dim,dtype=np.int64)
        # Full birth amplitudes, including the uniform charge orientation,
        # are integer matrices divided by four.
        nums=[(u if q==1 else u.T)@(eye+b*(w if eta==1 else w.T))
              for q in (1,-1) for b in (1,-1) for eta in (1,-1)]
        assert np.array_equal(sum(k.T@k for k in nums),16*eye)
        weighted=[]
        for link,radius in ((0,2),(1,1)):
            weights=np.array([4**abs(v[link]) for v in basis],dtype=np.int64)
            gram=sum(k.T@(weights[:,None]*k) for k in nums)
            assert np.array_equal(gram,np.diag(np.diag(gram)))
            slack=16*(4**radius)*weights-np.diag(gram)
            assert np.min(slack)>=0
            weighted.append({'link':link,'radius':radius,
                             'minimum_integer_weighted_slack':int(np.min(slack)),
                             'exact_squared_growth_factor':4**radius})
        big=s+2;ub,bb=shift2(big,(1,0));wb,_=shift2(big,(1,1))
        ib=np.eye(len(bb),dtype=np.int64);lookup={v:i for i,v in enumerate(bb)}
        emb=np.zeros((len(bb),dim),dtype=np.int64)
        for j,v in enumerate(basis):emb[lookup[v],j]=1
        big_nums=[(ub if q==1 else ub.T)@(ib+b*(wb if eta==1 else wb.T))
                  for q in (1,-1) for b in (1,-1) for eta in (1,-1)]
        difference=np.vstack([kb@emb-emb@ks for kb,ks in zip(big_nums,nums)])
        bad=np.array([abs(v[0])>=s-1 or abs(v[1])>=s for v in basis])
        assert np.count_nonzero(difference[:,~bad])==0
        squared=difference.T@difference/16
        top=float(np.linalg.eigvalsh(squared).max())
        assert top<=4+1e-12
        # If one incorrectly uses net shift radius one on the first link,
        # agreement can fail on the supposedly interior layer.
        wrongly_good=np.array([abs(v[0])<=s-1 and abs(v[1])<=s-1 for v in basis])
        wrong_nonzero=int(np.count_nonzero(difference[:,wrongly_good]))
        assert wrong_nonzero>0
        rows.append({'S':s,'input_dimension':dim,'exact_instrument_normalization':'16 I / 16',
                     'weighted_growth_at_lambda_log2':weighted,
                     'correct_interior_discrepancy':'exact zero',
                     'largest_squared_dilation_discrepancy_numeric':top,
                     'underestimated_radius_countercontrol_nonzero_entries':wrong_nonzero})
    return rows


def hamiltonian_weighted_controls():
    rows=[]
    for s in (1,2,3,5):
        u,basis=shift2(s,(1,1));dim=len(basis)
        coeff=.17+.11j
        diagonal=np.diag([2.3*a*a+.7*b*b+.9*a*b for a,b in basis])
        h=diagonal+coeff*u+coeff.conjugate()*u.T
        for link in (0,1):
            weights=np.array([2.**abs(v[link]) for v in basis])
            tilted=weights[:,None]*h/weights[None,:]
            anti=(tilted-tilted.conj().T)/(2j)
            actual=float(np.linalg.norm(anti,2));bound=1.5*abs(coeff)
            assert actual<=bound+2e-13
            rows.append({'S':s,'link':link,'anti_Hermitian_norm':actual,
                         'two_J_sinh_log2':bound,'large_diagonal_cancels':True})
    return rows


def compensator_control():
    # Occupation states 0,1,2; events and sensitivities are deliberately
    # state-dependent, including mutually exclusive events and a terminal state.
    events=[(0,1,.7,2),(1,0,.4,1),(1,2,1.1,2)]
    lam=math.log(1.7);cap=sum(rate*(math.exp(lam*s)-1) for _,_,rate,s in events)
    tilted=np.zeros((3,3));ordinary=np.zeros((3,3))
    for src,dst,rate,s in events:
        tilted[dst,src]+=rate*math.exp(lam*s);tilted[src,src]-=rate
        ordinary[dst,src]+=rate;ordinary[src,src]-=rate
    init=np.array([1.,0.,0.]);rows=[]
    for t in (.1,1.,3.):
        mgf=float(np.ones(3)@expm(t*tilted)@init)
        assert mgf<=math.exp(cap*t)+1e-12
        # Integral of predictable pre-event exponential using a block system.
        block=np.zeros((4,4));block[:3,:3]=tilted
        for src,_,rate,s in events:block[3,src]+=rate*math.exp(lam*(s-1))
        integral=float((expm(t*block)@np.r_[init,0.])[3])
        prefactor=sum(rate*math.exp(lam*(s-1)) for _,_,rate,s in events)
        bound=prefactor*math.expm1(cap*t)/cap
        assert integral<=bound+1e-11
        rows.append({'t':t,'counting_MGF':mgf,'MGF_bound':math.exp(cap*t),
                     'pre_event_compensator_integral':integral,'compensator_bound':bound})
    return rows


def cutoff_bound(s,t,m0=1,beta=.7,j=.13):
    def calc(lam):
        total=0.
        for radius in (2,1):
            a=2*j*math.sinh(lam)+beta*math.expm1(lam*radius)
            c=4*j+2*beta*math.exp(lam*(radius-1))
            exponent=-lam*(s-m0)
            if a*t>600:return float('inf')
            total+=math.exp(exponent)*c*math.expm1(a*t)/a
        return total
    opt=minimize_scalar(calc,bounds=(1e-5,4.),method='bounded',options={'xatol':1e-12})
    return float(opt.fun),float(opt.x)


def cyclic_generator(s,beta=.7,j=.13,electric=.09):
    # Two oppositely oriented parallel links form one gauge cycle.
    # The vacuum has E1=E2, and records q,-q have E1-E2=q mod (2S+1).
    # This is a small supplied graph, not an embedding in the fundamental Z3.
    m=2*s+1;eye=sparse.eye(m,format='csr');w=sparse.lil_matrix((m,m),dtype=complex)
    for col in range(m):w[(col+1)%m,col]=1
    w=w.tocsr()
    configs=[(0,0)]+[(q,b) for q in (1,-1) for b in (1,-1)]
    basis=[[(rep(e+q,s),e) for e in range(-s,s+1)] for q,b in configs]
    width=m*m;parts={}
    for c,((q,b),fields) in enumerate(zip(configs,basis)):
        diag=np.array([electric*(e1*e1+1.3*e2*e2)+.02*b*e1 for e1,e2 in fields])
        h=sparse.diags(diag)-j*(w+w.getH())
        g=-1j*(sparse.kron(eye,h)-sparse.kron(h.T,eye))
        if c==0:g-=beta*sparse.eye(width)
        parts[c,c]=g
        if c:
            gain=sparse.csr_matrix((width,width),dtype=complex)
            for eta in (1,-1):
                k=(eye+b*(w if eta==1 else w.getH()))/math.sqrt(8)
                gain+=(beta/2)*sparse.kron(k.conjugate(),k)
            parts[c,0]=gain
    gen=sparse.bmat([[parts.get((a,b)) for b in range(5)] for a in range(5)],format='csr')
    initial=np.zeros(5*width,complex);psi=np.zeros(m,complex);psi[s]=1/math.sqrt(2);psi[s+1]=1j/math.sqrt(2)
    initial[:width]=np.outer(psi,psi.conj()).reshape(-1,order='F')
    return gen,initial,basis


def distance(states,bases,other,otherbases):
    total=0.;marktv=0.;badprob=0.
    m=len(bases[0]);n=len(otherbases[0])
    for c in range(5):
        a=states[c*m*m:(c+1)*m*m].reshape(m,m,order='F')
        b=other[c*n*n:(c+1)*n*n].reshape(n,n,order='F')
        union=sorted(set(bases[c])|set(otherbases[c]));idx={e:i for i,e in enumerate(union)}
        mat=np.zeros((len(union),len(union)),complex)
        ai=[idx[e] for e in bases[c]];bi=[idx[e] for e in otherbases[c]]
        mat[np.ix_(ai,ai)]+=a;mat[np.ix_(bi,bi)]-=b
        total+=float(np.abs(np.linalg.eigvalsh((mat+mat.conj().T)/2)).sum())/2
        marktv+=abs(float(np.trace(a-b).real)) if m==n else abs(float((np.trace(a)-np.trace(b)).real))
        q=0 if c==0 else (1 if c<=2 else -1)
        badprob+=sum(float(a[i,i].real) for i,(e1,e2) in enumerate(bases[c]) if e1-e2!=q)
    return total,marktv/2,badprob


def finite_time_diagnostics():
    ref_s=28
    rg,ri,rb=cyclic_generator(ref_s)
    rows=[]
    for t in (.2,.7,1.4):
        reference=expm_multiply(t*rg,ri)
        ref_bound,ref_lambda=cutoff_bound(ref_s,t)
        for s in (2,3,5,8,12):
            gen,init,bases=cyclic_generator(s)
            state=expm_multiply(t*gen,init)
            dist,marktv,gaussbad=distance(state,bases,reference,rb)
            bound,lam=cutoff_bound(s,t)
            assert dist<=bound+ref_bound+3e-11
            assert marktv<=dist+2e-12
            assert gaussbad<=bound+3e-11
            m=2*s+1
            vacuum=float(np.trace(state[:m*m].reshape(m,m,order='F')).real)
            assert abs(vacuum-math.exp(-.7*t))<3e-12
            rows.append({'S':s,'T':t,'half_trace_distance_to_large_cyclic':dist,
                         'final_permanent_mark_total_variation':marktv,
                         'embedded_integer_Gauss_violation_probability':gaussbad,
                         'bound_B_raw':bound,'selected_lambda':lam,
                         'large_reference_S':ref_s,'large_reference_B_raw':ref_bound,
                         'large_reference_selected_lambda':ref_lambda,
                         'vacuum_probability':vacuum,'predicted_vacuum_probability':math.exp(-.7*t)})
    return rows


def main():
    result={'status':'PASS','exact_birth_operator_controls':exact_event_bounds(),
            'Hamiltonian_weighted_norm_controls':hamiltonian_weighted_controls(),
            'state_dependent_counting_and_compensator_controls':compensator_control(),
            'finite_CQ_time_diagnostics':finite_time_diagnostics(),
            'failed_attempts':[],
            'limits':'Exact event identities use integer arithmetic. Spectral and time diagnostics use floating point, without interval-rounding certification. Reference cutoff error uses the displayed analytic candidate theorem; it is not an independent proof of that theorem. No infinite-volume or long-time limit.'}
    (OUT/'GAUGE_RECORD_INSTRUMENT_CUTOFF_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
