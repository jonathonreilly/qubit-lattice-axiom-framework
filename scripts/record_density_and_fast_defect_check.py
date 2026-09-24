#!/usr/bin/env python3
"""Exact local operator checks and finite controls for live record density.

No numerical finite-size experiment establishes the volume-uniform estimate;
that estimate is proved in the companion note. Full local tensor products are
used for the loss identities, including both record charges.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/record_density_and_fast_defect_check.py', 'scripts/hardcore_record_ring_and_formation_check.py')

import hashlib
import itertools
import json
from pathlib import Path
import time

import numpy as np
import scipy.linalg as la
import scipy.sparse as ss
import sympy as sp

import hardcore_record_ring_and_formation_check as ring

OUT=Path(__file__).resolve().parent


def sparse_zero(a):
    a=a.tocsr();a.eliminate_zeros()
    return a.nnz==0


def local_model(nv,edges,a_sites):
    basis=list(itertools.product(itertools.product((0,1,-1),repeat=nv),
                                 itertools.product((0,1),repeat=len(edges))))
    ix={s:i for i,s in enumerate(basis)};size=len(basis)
    entries_b=[[] for _ in edges];entries_v=[[[],[]] for _ in edges]
    kval=[];nval=[];nbval=[];vac=[]
    for i,(m,bits) in enumerate(basis):
        kval.append(sum(m[x]==0 if x in a_sites else m[x]!=0 for x in range(nv)))
        nval.append(sum(v!=0 for v in m));nbval.append(sum(m[x]!=0 for x in range(nv) if x not in a_sites))
        vac.append([int(m[x]==m[y]==0) for x,y in edges])
        for e,(x,y) in enumerate(edges):
            assert x in a_sites and y not in a_sites
            if m[x]!=0 and m[y]==0 and 0<=bits[e]-m[x]<=1:
                mm=list(m);bb=list(bits);mm[y]=m[x];mm[x]=0;bb[e]-=m[x]
                entries_b[e].append((ix[(tuple(mm),tuple(bb))],i))
            if m[x]==m[y]==0:
                q=1 if bits[e]==0 else -1
                mm=list(m);bb=list(bits);mm[x]=q;mm[y]=-q;bb[e]+=q
                entries_v[e][0 if q==1 else 1].append((ix[(tuple(mm),tuple(bb))],i))
    def mat(entries):
        row,col=zip(*entries) if entries else ([],[])
        return ss.csr_matrix((np.ones(len(entries),dtype=np.int64),(row,col)),shape=(size,size))
    b=[mat(e) for e in entries_b];vs=[[mat(e) for e in pair] for pair in entries_v]
    k=ss.diags(kval,format='csr',dtype=np.int64);n=ss.diags(nval,format='csr',dtype=np.int64);nb=ss.diags(nbval,format='csr',dtype=np.int64)
    return basis,b,vs,k,n,nb,[ss.diags([v[e] for v in vac],format='csr',dtype=np.int64) for e in range(len(edges))]


def local_identities():
    rows=[]
    for name,nv,edges,a in [('same_edge',2,[(0,1)],{0}),
                          ('shared_A',3,[(0,1),(0,2)],{0}),
                          ('shared_B',3,[(0,1),(2,1)],{0,2}),
                          ('disjoint',4,[(0,1),(2,3)],{0,2})]:
        basis,b,vs,k,n,nb,vac=local_model(nv,edges,a)
        for e in range(len(edges)):
            assert sparse_zero(k@b[e]-b[e]@k-2*b[e])
            assert sparse_zero(n@b[e]-b[e]@n)
            assert sparse_zero(vs[e][0].T@vs[e][0]+vs[e][1].T@vs[e][1]-vac[e])
            for v in vs[e]:
                assert sparse_zero(k@v-v@k)
                assert sparse_zero(n@v-v@n-2*v)
                assert sparse_zero(nb@v-v@nb-v)
        for refinement in ('plus_coherent','minus_coherent','charge_resolved'):
            js=[]
            for v,w in vs:
                js.append([v+w] if refinement=='plus_coherent' else [v-w] if refinement=='minus_coherent' else [v,w])
            for e,hop in enumerate(b):
                for f,(x,y) in enumerate(edges):
                    loss=sum((j.T@j for j in js[f]),ss.csr_matrix(hop.shape,dtype=np.int64))
                    twice=sum((2*j.T@hop@j for j in js[f]),ss.csr_matrix(hop.shape,dtype=np.int64))-loss@hop-hop@loss
                    shared=set(edges[e])&set(edges[f])
                    if e==f or not shared:want=ss.csr_matrix(hop.shape,dtype=np.int64)
                    else:
                        other=next(iter(set(edges[f])-shared))
                        empty=ss.diags([int(m[other]==0) for m,bits in basis],format='csr',dtype=np.int64)
                        want=-empty@hop
                    assert sparse_zero(twice-want),(name,refinement,e,f)
                    dk=sum((2*j.T@k@j for j in js[f]),ss.csr_matrix(k.shape,dtype=np.int64))-loss@k-k@loss
                    dn=sum((2*j.T@n@j for j in js[f]),ss.csr_matrix(n.shape,dtype=np.int64))-loss@n-n@loss
                    assert sparse_zero(dk) and sparse_zero(dn-4*vac[f])
            rows.append({'geometry':name,'full_dimension':len(basis),'refinement':refinement,
                         'all_exact_local_identities':True})
    return rows


def fast_defect():
    # Exact hard-core plus-record star, with the stated external boundary
    # offsets. Two particles, not a one-particle surrogate.
    offset=(sp.Rational(1),sp.Rational(1,2),sp.Rational(1,2))
    basis=[]
    for m in itertools.product((0,1),repeat=3):
        if sum(m)!=2:continue
        for bits in itertools.product((0,1),repeat=2):
            ee=[sp.Rational(2*b-1,2) for b in bits]
            div=(sum(ee),-ee[0],-ee[1])
            if all(div[x]+offset[x]-m[x]==0 for x in range(3)):basis.append((m,bits))
    assert len(basis)==3;ix={s:i for i,s in enumerate(basis)};hop=sp.zeros(3)
    penalty=[sum(m[x] for x in (1,2))-1 for m,b in basis]
    for i,(m,bits) in enumerate(basis):
        for e,y in enumerate((1,2)):
            for src,dst,sgn in ((0,y,-1),(y,0,1)):
                if not m[src] or m[dst] or not 0<=bits[e]+sgn<=1:continue
                mm=list(m);bb=list(bits);mm[src]=0;mm[dst]=1;bb[e]+=sgn
                hop[ix[(tuple(mm),tuple(bb))],i]=-1
    low=[i for i,e in enumerate(penalty) if e==0];high=[i for i,e in enumerate(penalty) if e==1]
    second=-hop.extract(low,high)*hop.extract(high,low)
    assert second==-sp.ones(2)
    D,t,E=sp.symbols('Delta t E',positive=True)
    char=sp.factor((E*sp.eye(3)-D*sp.diag(*penalty)-t*hop).det())
    assert sp.expand(char-E*(E*E-D*E-2*t*t))==0
    rows=[]
    for delta in (256.,1024.,4096.,16384.,65536.):
        tt=(delta**3/2)**.25
        split=(np.sqrt(delta**2+8*tt*tt)-delta)/2
        rows.append({'Delta':delta,'J_ring':1.,'t':tt,'leading_defect_exchange':tt*tt/delta,
                     'exact_exchange_from_splitting':split/2,
                     'nominal_loss_scale_beta_epsilon2':tt*tt/(delta*delta),
                     'product_exchange_and_nominal_loss_at_beta1':tt**4/delta**3})
    return {'basis':basis,'boundary_offsets':list(offset),'relative_penalties':penalty,
            'hop_matrix':hop.tolist(),'second_order_matrix_over_t2_over_Delta':second.tolist(),
            'characteristic_polynomial':str(char),'fixed_J_scaling':rows,
            'scope':'Three-site coherent exchange only. Its divergent speed does not prove finite disturbance of a many-body field.'}


def finite_live_controls():
    basis,hop,pen,n,js,gh=ring.square_model((1,0,1,0),allow_birth=True)
    dim=len(basis);h=np.array(hop,dtype=float);number=np.diag(n).astype(float)
    kk=np.diag([sum(m[x]==0 for x in (0,2))+sum(m[x]!=0 for x in (1,3)) for m,bits in basis]).astype(float)
    jj=[np.array(j,dtype=float) for j in js];loss=sum(j.T@j for j in jj)
    low=[i for i,v in enumerate(pen) if v==0];before=[i for i,v in enumerate(n) if v==2]
    rho0=np.zeros((dim,dim),complex);rho0[low[0],low[0]]=1
    ident=np.eye(dim);rows=[];cost=[]
    for delta in (4096.,16384.,65536.,262144.):
        tt=(delta**3/2)**.25;beta=1.;eps=tt/delta
        ham=delta*np.diag(pen)+tt*h
        generator=-1j*(np.kron(ident,ham)-np.kron(ham.T,ident))
        for j in jj:generator+=beta*(np.kron(j,j)-.5*np.kron(ident,j.T@j)-.5*np.kron((j.T@j).T,ident))
        for tau in (.25,.5,1.):
            rho=(la.expm(tau*generator)@rho0.reshape(-1,order='F')).reshape((dim,dim),order='F')
            assert np.linalg.norm(rho-rho.conj().T)<1e-9
            assert abs(np.trace(rho)-1)<2e-9 and la.eigvalsh(rho).min()>-1e-9
            defects=float(np.trace(kk@rho).real)/4
            births=float(np.trace((number-2*ident)@rho).real)/8
            # On C4 the graph degree is 2d=2, so d=1 and C_d=2.
            d=1.;cc=d*(4*d-2)
            bound_k=eps**2*(4*d+2*cc*beta*tau)**2
            bound_b=d*beta*eps**2*(16*d*d*tau+8*d*cc*beta*tau*tau+4*cc*cc*beta*beta*tau**3/3)
            assert defects<=bound_k+1e-8 and births<=bound_b+1e-8
            rows.append({'Delta':delta,'J':1.,'beta':beta,'time':tau,'epsilon':eps,
                         'defect_density':defects,'density_bound':bound_k,
                         'expected_births_per_vertex':births,'birth_density_bound':bound_b,
                         'trace_error':float(abs(np.trace(rho)-1))})
        eigen,vec=la.eigh(ham[np.ix_(before,before)])
        psi=np.zeros(dim,complex);psi[before]=vec[:,0];energy=eigen[0]
        adj=sum((j.T@ham@j-.5*(j.T@j@ham+ham@j.T@j) for j in jj),np.zeros_like(ham))
        rate=float(np.vdot(psi,loss@psi).real);power=float(np.vdot(psi,adj@psi).real)
        assert rate>0 and abs(power/rate-(2*delta-energy))<1e-7*delta
        cost.append({'Delta':delta,'low_eigenenergy':float(energy),'birth_rate':rate,
                     'mean_power_supplied_by_formation':power,'energy_per_birth_over_Delta':power/(rate*delta),
                     'exact_identity_residual_over_Delta':float((power/rate-2*delta+energy)/delta)})
    return {'physical_dimension':dim,'controls':rows,'energy_ledger_controls':cost}


def main():
    start=time.monotonic()
    dep=hashlib.sha256((OUT/'hardcore_record_ring_and_formation_check.py').read_bytes()).hexdigest()
    assert dep=='1fcb36a522dddc70b4b51edc4f4a20d713dd3c8fb1e292e2cdc5ff07bcb59649'
    data={'status':'PASS','ring_dependency_sha256':dep,'exact_local_identities':local_identities(),
          'fast_defect_star':fast_defect(),'finite_live_density':finite_live_controls(),
          'runtime_seconds':time.monotonic()-start}
    text=json.dumps(data,indent=2,default=str)+'\n'
    (OUT/'RECORD_DENSITY_AND_FAST_DEFECT_RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__':main()
