#!/usr/bin/env python3
"""Independent physical-bit ring algebra, connectivity and full generator."""
from __future__ import annotations

from collections import Counter, deque
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import sparse
from scipy.sparse.linalg import expm_multiply

OUT=Path(__file__).resolve().parent


def bit(b,i,k): return (b>>(i%k))&1
def occupations(b,k): return tuple(bit(b,i,k)^bit(b,i-1,k) for i in range(k))
def can_hop(b,i,k): return bit(b,i-1,k)!=bit(b,i+1,k)
def can_birth(b,i,k): return bit(b,i-1,k)==bit(b,i,k)==bit(b,i+1,k)


def graph_checks():
    rows=[]
    for k in [4,6,8,10]:
        seen=set(); components=[]
        for root in range(1<<k):
            if root in seen: continue
            todo=deque([root]);seen.add(root);part=[]
            while todo:
                b=todo.popleft();part.append(b)
                for i in range(k):
                    if can_hop(b,i,k):
                        dest=b^(1<<i)
                        assert sum(occupations(dest,k))==sum(occupations(b,k))
                        if dest not in seen: seen.add(dest);todo.append(dest)
            n=sum(occupations(root,k))
            active=sum(any(can_birth(b,i,k) for i in range(k)) for b in part)
            if n<k: assert active>0,(k,n,part)
            else: assert len(part)==1 and active==0
            distinct_patterns={occupations(b,k) for b in part}
            # Every nonzero, nonfull component projects onto every N-site subset.
            if 0<n<k: assert len(distinct_patterns)==int(sp.binomial(k,n))
            components.append((n,len(part),active,len(distinct_patterns)))
        grouped=Counter(components)
        rows.append({"K":k,"physical_bit_states":1<<k,"components":len(components),
                     "summary":[{"N":key[0],"states_per_component":key[1],
                                 "active_states_per_component":key[2],
                                 "occupation_patterns_per_component":key[3],"multiplicity":n}
                                for key,n in sorted(grouped.items())]})
    return rows


def matrices(k, exact=False):
    d=1<<k
    zero=lambda: sp.zeros(d) if exact else np.zeros((d,d),complex)
    t=zero(); vp=[];vm=[];hop=[];occ=[];ef=[]
    for b in range(d):t[b^(d-1),b]=1
    for i in range(k):
        plus=zero();minus=zero();h=zero();n=zero();e=zero()
        for b in range(d):
            n[b,b]=occupations(b,k)[i]
            e[b,b]=sp.Rational(2*bit(b,i,k)-1,2) if exact else bit(b,i,k)-.5
            if can_hop(b,i,k):h[b^(1<<i),b]=1
            if can_birth(b,i,k):
                (plus if bit(b,i,k)==0 else minus)[b^(1<<i),b]=1
        vp.append(plus);vm.append(minus);hop.append(h);occ.append(n);ef.append(e)
    n=sum(occ,zero())
    return t,vp,vm,hop,occ,ef,n


def exact_controls():
    k=4;t,vp,vm,hops,occ,ef,n=matrices(k,True)
    chi=sp.symbols('chi',real=True)
    beta=[sp.Integer(x) for x in [1,2,3,5]]
    h=sum((sp.Integer(i+1)*q for i,q in enumerate(hops)),sp.zeros(16))
    h0=sum((sp.Rational(i+2,7)*q for i,q in enumerate(occ)),sp.zeros(16))+sp.Rational(3,7)*t
    h+=h0
    a=sp.diag(*[chi**((k-int(n[b,b]))//2) for b in range(16)])*t
    dual=sp.I*(h*a-a*h)
    number_dual=sp.zeros(16);gamma=sp.zeros(16)
    for b,p,m in zip(beta,vp,vm):
        loss=b*(p.T*p+m.T*m);gamma+=loss
        dual+=b*(p.T*a*p+m.T*a*m+chi*(p.T*a*m+m.T*a*p))-(loss*a+a*loss)/2
        number_dual+=b*(p.T*n*p+m.T*n*m+chi*(p.T*n*m+m.T*n*p))-(loss*n+n*loss)/2
    for i,o in enumerate(occ):dual+=(i+1)*(o*a*o-(o*a+a*o)/2)
    assert dual.applyfunc(sp.expand)==sp.zeros(16)
    assert number_dual==2*gamma
    for e in ef:
        assert e*n==n*e and e*t==-t*e
        assert e*a*e-a/4 == -a/2
    assert a.subs(chi,0)==sp.diag(*[int(n[b,b]==k) for b in range(16)])*t

    # Abstract anti-T alone does not guarantee the electric-monitoring identity.
    sx=sp.Matrix([[0,1],[1,0]]);sz=sp.diag(1,-1)
    abstract_t=sp.kronecker_product(sp.eye(2),sx)
    abstract_n=sp.kronecker_product(sp.diag(0,2),sp.eye(2))
    abstract_e=sp.kronecker_product(sx,sz)/2
    abstract_a=sp.kronecker_product(sp.diag(sp.Rational(1,2),1),sx)
    residual=abstract_e*abstract_a*abstract_e-abstract_a/4+abstract_a/2
    assert abstract_e**2==sp.eye(4)/4
    assert abstract_e*abstract_t==-abstract_t*abstract_e
    assert abstract_e*abstract_n!=abstract_n*abstract_e
    assert residual!=sp.zeros(4)

    # Additional N,T-commuting dissipators need not preserve completion.
    # P projects onto one noncontact two-hole occupation pattern, including its
    # complementary field state. The number-conserving feedback jump cancels H.
    hhop=sum(hops,sp.zeros(16))
    pattern=occupations(3,k)
    p=sp.diag(*[int(occupations(b,k)==pattern) for b in range(16)])
    assert sp.trace(p)==2 and p*gamma==sp.zeros(16)
    rho=p/2
    feedback=p+2*sp.I*p*hhop
    assert feedback*n==n*feedback and feedback*t==t*feedback
    adj=feedback.conjugate().T
    drift=-sp.I*(hhop*rho-rho*hhop)+feedback*rho*adj-(adj*feedback*rho+rho*adj*feedback)/2
    for o in occ:drift+=o*rho*o-(o*rho+rho*o)/2
    assert drift==sp.zeros(16)
    assert sp.trace(n*rho)==2
    return {"K":4,"symbolic_chi_weighted_dual_residual":"zero for all chi",
            "number_dual":"2 Gamma","zero_chi_observable":"full-sector T",
            "electric_monitoring_dual":"-delta A/2 per link, using [E,N]=0",
            "missing_count_commutator_counterexample_residual":str(residual),
            "broader_jump_completion_countercontrol":{
                "occupation_pattern":pattern,"basis_indices":[b for b in range(16) if p[b,b]],
                "jump":"L=P+2 i P H_hop","stationary_density":"P/2",
                "record_count":2,"full_count":4,"full_exact_drift":"zero",
                "scope":"Additional arbitrary N,T-commuting jumps are allowed by the count identity, not the monitored-Hamiltonian completion proof."}}


def liouvillian(chi,delta=0.):
    k=4;t,vp,vm,hops,occ,ef,n=matrices(k)
    dim=1<<k;eye=sparse.eye(dim,format='csr',dtype=complex)
    h=sum((x*m for x,m in zip([.7,1.1,.9,1.4],hops)),np.zeros((dim,dim),complex))
    h+=sum((.31*(i+1)*m for i,m in enumerate(occ)),np.zeros((dim,dim),complex))+.23*t
    kron=lambda a,b:sparse.kron(a,b,format='csr')
    h=sparse.csr_matrix(h)
    gen=-1j*(kron(eye,h)-kron(h.T,eye))
    for beta,pp,mm in zip([.5,.8,1.2,1.7],vp,vm):
        p=sparse.csr_matrix(pp);m=sparse.csr_matrix(mm)
        loss=beta*(p.getH()@p+m.getH()@m)
        gen+=beta*(kron(p.conjugate(),p)+kron(m.conjugate(),m)
                   +chi*(kron(m.conjugate(),p)+kron(p.conjugate(),m)))
        gen-=.5*(kron(eye,loss)+kron(loss.T,eye))
    for rate,oo in zip([.6,1.1,.9,.7],occ):
        o=sparse.csr_matrix(oo)
        gen+=rate*(kron(o.conjugate(),o)-.5*(kron(eye,o)+kron(o.T,eye)))
    if delta:
        e=sparse.csr_matrix(ef[0])
        gen+=delta*(kron(e.conjugate(),e)-.25*sparse.eye(dim*dim,format='csr'))
    return gen,t,n


def finite_evolution():
    k=4;dim=16
    cat=np.zeros(dim,complex);cat[0]=cat[15]=1/np.sqrt(2)
    initial=np.outer(cat,cat.conj()).reshape(-1,order='F')
    full=[b for b in range(dim) if sum(occupations(b,k))==k]
    rows=[]
    for chi,delta in [(-1,0),(-.5,0),(0,0),(.5,0),(1,0),(.5,.3)]:
        gen,t,n=liouvillian(chi,delta)
        ident=np.eye(dim).reshape(-1,order='F')
        trace_res=float(np.linalg.norm(ident@gen))
        assert trace_res<1e-12
        a=np.diag([chi**((k-int(n[b,b].real))//2) for b in range(dim)])@t
        tests=[]
        for time in [.2,1.,4.,200.]:
            rho=expm_multiply(time*gen,initial).reshape(dim,dim,order='F')
            full_prob=float(np.trace(rho[np.ix_(full,full)]).real)
            value=complex(np.trace(a@rho))
            expected=chi**(k//2)*np.exp(-delta*time/2)
            assert abs(value-expected)<5e-11,(chi,delta,time,value,expected)
            mineig=float(np.linalg.eigvalsh((rho+rho.conj().T)/2).min())
            assert mineig>-2e-11
            tests.append({"t":time,"full_probability":full_prob,
                          "weighted_T":value.real,"predicted_weighted_T":float(expected),
                          "imaginary_residual":abs(value.imag),"minimum_density_eigenvalue":mineig})
        target=np.array([[1,chi**2 if delta==0 else 0],[chi**2 if delta==0 else 0,1]],complex)/2
        final_error=float(np.linalg.norm(rho[np.ix_(full,full)]-target))
        assert 1-full_prob<2e-9 and final_error<2e-9,(chi,delta,full_prob,final_error)
        rows.append({"chi":chi,"electric_delta_on_one_link":delta,
                     "trace_preservation_residual":trace_res,"checks":tests,
                     "terminal_matrix_residual_at_t200":final_error})
    return {"generator_dimension":dim*dim,"full_basis":full,"rows":rows,
            "scope":"Numerical full Liouvillian control with nonuniform hopping, births and monitoring, and nonzero occupation/T-preserving H0. Not a uniform-volume rate estimate."}


def main():
    result={"status":"PASS","ring_connectivity":graph_checks(),"exact_controls":exact_controls(),
            "full_finite_generator":finite_evolution(),"failed_attempts":[]}
    (OUT/'COUNT_RING_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
