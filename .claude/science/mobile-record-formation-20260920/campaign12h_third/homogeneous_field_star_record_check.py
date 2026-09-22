#!/usr/bin/env python3
"""Homogeneous field-star penalty: exact local identities and finite controls.

The volume-uniform density estimate is proved in the companion note. These
controls check its algebra, the Gauss-sector specialization, and complete
finite live-formation dynamics without changing any frozen earlier runner.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import time

import numpy as np
import scipy.linalg as la
import scipy.sparse as ss

import record_density_and_fast_defect_check as density
import hardcore_record_ring_and_formation_check as ring

OUT=Path(__file__).resolve().parent


def local_star_identities():
    rows=[]
    for name,nv,edges,a in [('same_edge',2,[(0,1)],{0}),
                          ('shared_A',3,[(0,1),(0,2)],{0}),
                          ('shared_B',3,[(0,1),(2,1)],{0,2}),
                          ('disjoint',4,[(0,1),(2,3)],{0,2})]:
        basis,bs,vs,k,n,nb,vac=density.local_model(nv,edges,a)
        ra=[sum((m[x]-int(x in a))**2 for x in range(nv)) for m,b in basis]
        twice_r=ss.diags(ra,format='csr',dtype=np.int64)
        minus_a=ss.diags([sum(m[x]==-1 for x in a) for m,b in basis],format='csr',dtype=np.int64)
        assert density.sparse_zero(twice_r-k-4*minus_a)
        for e,(vp,vm) in enumerate(vs):
            assert density.sparse_zero(twice_r@vp-vp@twice_r)
            assert density.sparse_zero(twice_r@vm-vm@twice_r-4*vm)
        for refinement in ('plus_coherent','minus_coherent','charge_resolved'):
            for e,(vp,vm) in enumerate(vs):
                js=[vp+vm] if refinement=='plus_coherent' else [vp-vm] if refinement=='minus_coherent' else [vp,vm]
                loss=sum((j.T@j for j in js),ss.csr_matrix(twice_r.shape,dtype=np.int64))
                twice_dstar=sum((2*j.T@twice_r@j for j in js),ss.csr_matrix(twice_r.shape,dtype=np.int64))-loss@twice_r-twice_r@loss
                assert density.sparse_zero(twice_dstar-8*vm.T@vm)
            rows.append({'geometry':name,'full_dimension':len(basis),'refinement':refinement,
                         'exact_birth_star_energy_identities':True})
    return rows


def first_excursion_counts():
    rows=[];rng=random.Random(2026092220)
    for shape in ((6,6),(6,6,6)):
        vertices,edges,faces=ring.geometry_source.geometry(shape,True)
        d=len(shape);vid={v:i for i,v in enumerate(vertices)}
        aset={i for i,v in enumerate(vertices) if sum(v)%2==0}
        c=sum(1<<e for e,(v,axis,w) in enumerate(edges) if sum(v[b] for b in range(d) if b!=axis)%2==0)
        for trial in range(3):
            if trial:
                for _ in range(10*len(faces)):
                    f=rng.choice(faces);rr,ll=f['r'],f['l']
                    if (c&rr==0 and c&ll==ll) or (c&rr==rr and c&ll==0):c^=rr^ll
            assert ring.geometry_source.gauss(c,vertices,edges)==(0,)*len(vertices)
            eligible=[];incident={a:[] for a in aset}
            for e,(v,axis,w) in enumerate(edges):
                x,y=vid[v],vid[w];a,b=(x,y) if x in aset else (y,x)
                outward_sign=1 if x==a else -1
                outward_bit=((c>>e)&1) if outward_sign==1 else 1-((c>>e)&1)
                incident[a].append((e,b,outward_bit))
                if outward_bit:eligible.append((a,b,e))
            distributions=Counter()
            for a,b,ehop in eligible:
                # The traversed edge was outward positive and is now negative.
                # A+ birth raises a remaining negative outward field; A- birth
                # lowers a positive one. The traversed neighbor is occupied.
                counts=Counter()
                for e,neighbor,outward_bit in incident[a]:
                    bit=0 if e==ehop else outward_bit
                    if neighbor==b:continue
                    charge_a=1 if bit==0 else -1
                    target_r=1 if charge_a==1 else 3
                    counts[target_r]+=1
                assert counts==Counter({1:d,3:d-1})
                assert sum(counts.values())==2*d-1
                distributions[tuple(sorted(counts.items()))]+=1
            assert len(eligible)==d*len(vertices)//2
            rows.append({'shape':shape,'configuration_hex':hex(c),'first_hops':len(eligible),
                         'each_first_excursion_energy_over_Delta':1,
                         'birth_targets_with_star_energy_1':d,
                         'birth_targets_with_star_energy_3':d-1,
                         'mean_bare_target_energy_over_Delta':(4*d-3)/(2*d-1),
                         'all_first_hops_checked':True})
    return rows


def square_controls():
    basis,hop,pen,n,jumps,gh=ring.square_model((1,0,1,0),allow_birth=True)
    dim=len(basis);rv=[];kv=[];mv=[]
    for matter,bits in basis:
        div=[bits[x]-bits[(x-1)%4] for x in range(4)]
        assert all(div[x]==matter[x]-int(x in (0,2)) for x in range(4))
        r=sum(x*x for x in div)/2
        k=sum(matter[x]==0 for x in (0,2))+sum(matter[x]!=0 for x in (1,3))
        m=sum(x==-1 for x in matter)
        assert r==k/2+2*sum(matter[x]==-1 for x in (0,2))
        assert r>=m and r>=k/2
        rv.append(r);kv.append(k);mv.append(m)
    before=[i for i,v in enumerate(n) if v==2]
    assert all(rv[i]==pen[i] for i in before)
    low=[i for i,v in enumerate(rv) if v==0]
    after=[i for i,v in enumerate(n) if v==4]
    assert len(low)==2 and all(rv[i]==1 for i in after)
    ham_t=np.array(hop,dtype=float);js=[np.array(j,dtype=float) for j in jumps]
    loss=sum(j.T@j for j in js);rr=np.diag(rv);mm=np.diag(mv)
    assert np.array_equal(sum((j.T@rr@j-.5*(j.T@j@rr+rr@j.T@j) for j in js),np.zeros_like(rr)),np.zeros_like(rr))
    ident=np.eye(dim);rho0=np.zeros((dim,dim),complex);rho0[low[0],low[0]]=1
    rows=[];cost=[]
    for delta in (4096.,16384.,65536.,262144.):
        tt=(delta**3/2)**.25;beta=1.;eps=tt/delta
        ham=delta*rr+tt*ham_t
        generator=-1j*(np.kron(ident,ham)-np.kron(ham.T,ident))
        for j in js:generator+=beta*(np.kron(j,j)-.5*np.kron(ident,j.T@j)-.5*np.kron((j.T@j).T,ident))
        for tau in (.25,.5,1.):
            rho=(la.expm(tau*generator)@rho0.reshape(-1,order='F')).reshape((dim,dim),order='F')
            assert np.linalg.norm(rho-rho.conj().T)<1e-9
            assert abs(np.trace(rho)-1)<2e-9 and la.eigvalsh(rho).min()>-1e-9
            star=float(np.trace(rr@rho).real)/4
            births=float(np.trace(mm@rho).real)/4
            # Degree two (d=1) has no energy-raising A-minus birth channel.
            bound=8*eps**2*(1+beta*tau)**2
            assert 0<=births<=star+1e-9<=bound+1e-8
            rows.append({'Delta':delta,'J':1.,'beta':beta,'time':tau,'epsilon':eps,
                         'star_energy_density_over_Delta':star,
                         'mean_births_per_vertex':births,'uniform_density_upper':bound,
                         'trace_error':float(abs(np.trace(rho)-1))})
        vals,vec=la.eigh(ham[np.ix_(before,before)])
        psi=np.zeros(dim,complex);psi[before]=vec[:,0];energy=vals[0]
        adj=sum((j.T@ham@j-.5*(j.T@j@ham+ham@j.T@j) for j in js),np.zeros_like(ham))
        rate=float(np.vdot(psi,loss@psi).real);power=float(np.vdot(psi,adj@psi).real)
        assert rate>0 and abs(power/rate-(delta-energy))<1e-7*delta
        cost.append({'Delta':delta,'low_eigenenergy':float(energy),'birth_rate':rate,
                     'mean_power_supplied_by_formation':power,
                     'energy_per_birth_over_Delta':power/(rate*delta),
                     'exact_power_identity_residual_over_Delta':float((power/rate-delta+energy)/delta)})
    return {'physical_dimension':dim,'basis':basis,'star_penalty_over_Delta':rv,
            'number_of_created_pairs':mv,'fixed_number_penalty_equals_original':True,
            'live_controls':rows,'energy_ledger_controls':cost}


def main():
    start=time.monotonic();deps={}
    for name,want in [('record_density_and_fast_defect_check.py','64bd01ac51dbaaf129c39766c3701834bcf23929a9d086d3d322773c7674bf94'),
                      ('hardcore_record_ring_and_formation_check.py','3c3cb5c32bd66f95668c5b6667aca711d5cfc6ddd95146ee6d0b92f18cbebbf7')]:
        deps[name]=hashlib.sha256((OUT/name).read_bytes()).hexdigest();assert deps[name]==want
    data={'status':'PASS','dependencies':deps,'local_star_identities':local_star_identities(),
          'bulk_first_excursions':first_excursion_counts(),'finite_square':square_controls(),
          'runtime_seconds':time.monotonic()-start,
          'scope':'The Hamiltonian is homogeneous; the selected external Gauss-charge sector and initial checkerboard remain supplied. Uniform mean density control is not uniform field-dynamics convergence.'}
    text=json.dumps(data,indent=2)+'\n';(OUT/'HOMOGENEOUS_FIELD_STAR_RECORD_RESULTS.json').write_text(text);print(text,end='')


if __name__=='__main__':main()
