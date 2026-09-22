#!/usr/bin/env python3
"""Bounded algebra/geometry/dynamics controls for conditional local RK cooling.

The general proof is in the companion note. Modular rank certificates are
finite exact controls over rational complex matrices, not all-volume proofs.
"""
from __future__ import annotations

from collections import Counter, deque
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import scipy.linalg as la
import scipy.sparse as ss
import sympy as sp

OUT=Path(__file__).resolve().parent


def local_algebra():
    # A flippable pair plus an unaffected nonflippable spectator.
    l=sp.Matrix([[1,-1,0],[1,-1,0],[0,0,0]])/2
    pm=l.T*l;pp=l*l.T;eye=sp.eye(3)
    assert pm**2==pm and pp**2==pp and pm*pp==sp.zeros(3)
    assert l*l==sp.zeros(3) and l.T*l==pm and l*l.T==pp
    z=sp.diag(-1,1,1)
    x=sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
    assert l==-z*pm and pm==(x*x-x)/2
    assert z*(eye-x)*x/2==l
    t=sp.symbols('t',positive=True)
    v=sp.Matrix([1,t,7])
    assert sp.simplify(pm*v-(1-t)/(1+t)*l.T*v)==sp.zeros(3,1)
    a,b=sp.symbols('a b',real=True)
    def channel(q):
        k0=eye+(q-1)*pm
        return sp.kronecker_product(k0,k0)+(1-q*q)*sp.kronecker_product(l,l)
    assert (channel(a)*channel(b)-channel(a*b)).applyfunc(sp.expand)==sp.zeros(9)
    d=sp.kronecker_product(l,l)-(sp.kronecker_product(eye,pm)+sp.kronecker_product(pm,eye))/2
    assert (-sp.diff(channel(a),a).subs(a,1)/2-d).applyfunc(sp.expand)==sp.zeros(9)
    fuel=sp.diag(1,0);spent=sp.diag(0,1);down=sp.Matrix([[0,0],[1,0]])
    c=sp.kronecker_product(l,down)+sp.kronecker_product(l.T,down.T)
    assert c**3==c
    assert c*c==sp.kronecker_product(pm,fuel)+sp.kronecker_product(pp,spent)
    # Two outcome-number sectors encode conversion of one fuel into two records.
    resource=sp.kronecker_product(eye,2*spent+2*fuel)
    assert c*resource==resource*c
    return {'dimension':3,'partial_isometry':'exact','Weimer_Eq12_identity':'exact',
            'separating_exponential_pair_identity':'exact rational t control',
            'fresh_channel_composition':'Phi_a Phi_b = Phi_(ab), exactly',
            'generator':'-d_a Phi_a at a=1 divided by2 equals D[L]',
            'fuel_dilation':'C^3=C and C^2=Pm*fuel+Pp*spent, exactly',
            'resource_limit':'N+2Pfuel only; no claim of commutation with the full interacting RK Hamiltonian'}


def matching_matrix(dim,pairs):
    m=np.zeros((dim,dim),dtype=np.int64)
    for a,b in pairs:
        m[a,a]+=1;m[b,a]+=1;m[a,b]-=1;m[b,b]-=1
    return m


def bad_orientation_control():
    l1=sp.Matrix(matching_matrix(4,[(0,1),(2,3)]))/2
    l2=sp.Matrix(matching_matrix(4,[(1,2),(3,0)]))/2
    u=sp.ones(4,1)/2
    v=sp.Matrix([1,1,-1,-1])/2
    w=sp.Matrix([-1,1,1,-1])/2
    pw=v*v.T+w*w.T;rho=pw/2
    assert sp.Matrix.vstack(l1,l2).rank()==3
    assert l1*u==sp.zeros(4,1) and l2*u==sp.zeros(4,1)
    assert l1*v==sp.zeros(4,1) and l1*w==-v
    assert l2*v==w and l2*w==sp.zeros(4,1)
    dissip=lambda l,r:l*r*l.T-(l.T*l*r+r*l.T*l)/2
    assert dissip(l1,rho)+dissip(l2,rho)==sp.zeros(4)
    h=l1.T*l1+l2.T*l2
    assert h*rho==rho*h and h*v==v and h*w==w
    # Constant displacements for each matching force F0=F2 and F1=F3.
    f=sp.symbols('f0:4')
    equations=sp.Matrix([f[1]-f[0]-f[3]+f[2],f[2]-f[1]-f[0]+f[3]])
    solution=sp.linsolve(list(equations),f)
    assert solution==sp.FiniteSet((f[2],f[3],f[2],f[3]))
    return {'L1':str(l1),'L2':str(l2),'common_dark_dimension':1,
            'orthogonal_stationary_density':str(rho),'purity':str(sp.trace(rho*rho)),
            'stationary_residual':'zero exactly, with H=0 or H=sum Pminus',
            'constant_displacement_constraint':str(solution),
            'conclusion':'Connected matching graph and unique common dark vector alone are insufficient.'}


def geometry(shape,periodic):
    ndim=len(shape);vertices=list(itertools.product(*[range(n) for n in shape]))
    vset=set(vertices)
    def shift(v,a):
        q=list(v);q[a]+=1
        if periodic:q[a]%=shape[a]
        q=tuple(q)
        return q if q in vset else None
    edges=[]
    for v in vertices:
        for a in range(ndim):
            w=shift(v,a)
            if w is not None:edges.append((v,a,w))
    ei={(v,a):j for j,(v,a,w) in enumerate(edges)}
    faces=[]
    for v in vertices:
        for a,b in itertools.combinations(range(ndim),2):
            va=shift(v,a);vb=shift(v,b)
            if va is None or vb is None:continue
            if (va,b) not in ei or (vb,a) not in ei:continue
            raised=(ei[(v,a)],ei[(va,b)])
            lowered=(ei[(vb,a)],ei[(v,b)])
            assert len(set(raised+lowered))==4
            faces.append({'origin':v,'axes':(a,b),'raised':raised,'lowered':lowered,
                          'r':sum(1<<e for e in raised),'l':sum(1<<e for e in lowered)})
    return vertices,edges,faces


def pairs_from_component(states,faces):
    index={c:i for i,c in enumerate(states)};pairs=[]
    for p in faces:
        row=[]
        for c in states:
            if c&p['r']==0 and c&p['l']==p['l']:
                other=c^p['r']^p['l'];assert other in index
                row.append((index[c],index[other]))
        pairs.append(row)
    return pairs


def component(seed,faces):
    seen={seed};q=deque([seed]);tree=[]
    while q:
        c=q.popleft()
        for p,face in enumerate(faces):
            r,l=face['r'],face['l']
            if (c&r==0 and c&l==l) or (c&r==r and c&l==0):
                d=c^r^l
                if d not in seen:seen.add(d);q.append(d);tree.append((c,d,p))
    return sorted(seen),tree


def gauss(c,vertices,edges):
    values={v:0 for v in vertices}
    for j,(v,a,w) in enumerate(edges):
        e=2*((c>>j)&1)-1;values[v]+=e;values[w]-=e
    return tuple(values[v] for v in vertices)


def flux(c,edges,ndim):
    return tuple(sum(2*((c>>j)&1)-1 for j,(v,b,w) in enumerate(edges) if a==b and v[a]==0)
                 for a in range(ndim))


def component_controls(shape,periodic,seed=None):
    vertices,edges,faces=geometry(shape,periodic)
    census=None
    if seed is None:
        assert len(edges)<=12
        unseen=set(range(1<<len(edges)));groups=[]
        while unseen:
            states,tree=component(min(unseen),faces);unseen.difference_update(states)
            groups.append((states,tree))
        states,tree=max(groups,key=lambda x:len(x[0]))
        seed=states[0];census=dict(sorted(Counter(len(a) for a,b in groups).items()))
    else:states,tree=component(seed,faces)
    d=len(states);pairs=pairs_from_component(states,faces)
    assert len(tree)==d-1
    charges=gauss(seed,vertices,edges);assert all(gauss(c,vertices,edges)==charges for c in states)
    fs=[sum(3**j*(2*((c>>j)&1)-1) for j in range(len(edges))) for c in states]
    assert len(set(fs))==d
    counts=[];jumps=[]
    for p,row in zip(faces,pairs):
        delta=2*(sum(3**j for j in p['raised'])-sum(3**j for j in p['lowered']))
        assert all(fs[b]-fs[a]==delta for a,b in row)
        m=ss.csr_matrix(matching_matrix(d,row));pp=m@m.T;pm=m.T@m
        assert (m@m).nnz==0
        assert (pm@pm-4*pm).nnz==0 and (pp@pp-4*pp).nnz==0
        assert np.max(abs(m@np.ones(d)))==0
        counts.append({'origin':p['origin'],'axes':p['axes'],'pairs':len(row),'constant_delta_F2':delta})
        jumps.append(m)
    if periodic:
        fl=flux(seed,edges,len(shape));assert all(flux(c,edges,len(shape))==fl for c in states)
    else:fl=None
    result={'shape':shape,'periodic':periodic,'vertices':len(vertices),'links':len(edges),'plaquettes':len(faces),
            'seed_bits':seed,'component_dimension':d,'all_components_census':census,
            'component_states_sha256':hashlib.sha256(json.dumps(states).encode()).hexdigest(),
            'spanning_tree_edges':len(tree),'gauss_twice':charges,'flux_twice':fl,
            'separating_F2_distinct_values':len(set(fs)),'local_controls':counts,
            'verification':'All local partial-isometry matrices, Gauss values, flip displacements and tree transitions checked exactly.'}
    return result,jumps


def rank_mod(a,p=65537):
    a=np.array(a,dtype=np.int64)%p;r=0
    for col in range(a.shape[1]):
        candidates=np.flatnonzero(a[r:,col])
        if not len(candidates):continue
        q=r+int(candidates[0]);a[[r,q]]=a[[q,r]]
        a[r]=(a[r]*pow(int(a[r,col]),-1,p))%p
        below=np.flatnonzero(a[r+1:,col])+r+1
        if len(below):a[below]=(a[below]-a[below,col,None]*a[r,None,:])%p
        r+=1
        if r==a.shape[0]:break
    return r


def dynamics_controls(jumps,label):
    dim=jumps[0].shape[0];assert dim<=20
    eye=np.eye(dim,dtype=np.int64)
    h8=np.zeros((dim,dim),dtype=np.int64)
    real8=np.zeros((dim*dim,dim*dim),dtype=np.int64)
    k=np.zeros((dim,dim),complex)
    for p,ms in enumerate(jumps):
        m=ms.toarray();pm4=m.T@m;gamma=p+1;hh=(-1)**p*(p+2)
        h8+=2*hh*pm4
        real8+=gamma*(2*np.kron(m,m)-np.kron(eye,pm4)-np.kron(pm4,eye))
        k+=gamma*pm4/4
    imag8=-(np.kron(eye,h8)-np.kron(h8.T,eye))
    # 8*G has integral real/imaginary coefficients; 256^2=-1 mod65537.
    p=65537;assert 256*256%p==p-1
    rank=rank_mod(real8+256*imag8,p)
    assert rank==dim*dim-1,(label,dim,rank)
    # Exact integer annihilation of uu^T; the rank lower bound plus this
    # kernel proves rational-complex nullity exactly one.
    target_vector=np.ones(dim*dim,dtype=np.int64)
    assert np.max(abs(real8@target_vector))==0 and np.max(abs(imag8@target_vector))==0
    gen=(real8+1j*imag8)/8
    eig=la.eigvals(gen);zero=abs(eig)<1e-9
    assert sum(zero)==1 and np.max(eig[~zero].real)<-1e-8
    gap=float(-np.max(eig[~zero].real))
    u=np.ones(dim)/np.sqrt(dim);target=np.outer(u,u)
    trace=np.eye(dim).reshape(-1,order='F')
    assert np.max(abs(trace@gen))<1e-12
    # Occupation reward Poisson equation: remove the stationary pole by
    # adding the spectral projection target*trace. K has zero target mean.
    stationary=np.outer(target.reshape(-1,order='F'),trace)
    reward_vec=k.T.reshape(-1,order='F')
    reward=la.solve(-(gen.T)+stationary.T,reward_vec)
    assert np.max(abs(-gen.T@reward-reward_vec))<1e-10
    times=[0.,.3,1.,3.,12./gap]
    starts=[('basis0',np.diag([1]+[0]*(dim-1))),('mixed',np.eye(dim)/dim),('target',target)]
    rows=[]
    for name,rho in starts:
        rv=rho.reshape(-1,order='F');expected=complex(reward@rv)
        assert abs(expected.imag)<1e-10 and expected.real>-1e-10
        seq=[]
        for t in times:
            rt=(la.expm(t*gen)@rv).reshape((dim,dim),order='F')
            assert la.norm(rt-rt.conj().T)<1e-10 and abs(np.trace(rt)-1)<1e-10
            assert la.eigvalsh(rt).min()>-1e-10
            infidelity=float((1-u@rt@u).real)
            assert infidelity>-1e-10
            seq.append({'time':t,'target_infidelity':infidelity,
                        'half_trace_distance':float(sum(abs(la.eigvalsh(rt-target)))/2),
                        'jump_intensity':float(np.trace(k@rt).real)})
        assert seq[-1]['half_trace_distance']<2e-5
        rows.append({'initial':name,'expected_total_jumps':expected.real,'transients':seq})
    return {'label':label,'dimension':dim,'gamma_p':'p+1','h_p':'(-1)^p (p+2)',
            'rank_of_8G_mod65537':rank,'exact_complex_nullity':1,
            'numerical_Liouvillian_decay_gap':gap,'poisson_reward_residual':float(np.max(abs(-gen.T@reward-reward_vec))),
            'results':rows,'limit':'Finite controls only, no claimed uniform gap or volume scaling.'}


def main():
    result={'status':'PASS','local_algebra':local_algebra(),'bad_orientation_countercontrol':bad_orientation_control()}
    geometries=[];dynamics=[]
    for shape in [(2,2),(3,2),(2,2,2)]:
        row,jumps=component_controls(shape,False);geometries.append(row)
        dynamics.append(dynamics_controls(jumps,'open_'+str(shape)))
    shape=(2,2,2);vertices,edges,faces=geometry(shape,True)
    seed=sum((1<<j) for j,(v,a,w) in enumerate(edges) if sum(v[b] for b in range(3) if b!=a)%2==0)
    row,jumps=component_controls(shape,True,seed);geometries.append(row)
    result['geometries']=geometries;result['small_dynamics']=dynamics
    result['proof_boundary']='General convergence uses the analytic separating-F invariant-subspace proof in the note. This runner does not prove a thermodynamic phase or a native record compiler.'
    (OUT/'LOCAL_GAUGE_RECORD_COOLING_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
