#!/usr/bin/env python3
"""Independent actual-cubic two-particle and local algebra controls."""
from pathlib import Path
from itertools import product,combinations_with_replacement,permutations
import json,math
import numpy as np
import sympy as sy
from scipy import sparse
from scipy.sparse.linalg import expm_multiply,eigsh
from scipy.linalg import expm
HERE=Path(__file__).resolve().parent

def curl(L):
    pts=list(product(range(L),repeat=3));ix={x:i for i,x in enumerate(pts)}
    rows=[];cols=[];values=[]
    for x in pts:
        for i,j,k in permutations(range(3)):
            eps=int(sy.LeviCivita(i,j,k))
            for sign in [-1,1]:
                y=list(x);y[j]=(y[j]+sign)%L
                rows.append(3*ix[x]+i);cols.append(3*ix[tuple(y)]+k);values.append(eps*sign)
    return pts,sparse.csr_matrix((values,(rows,cols)),shape=(3*len(pts),)*2,dtype=int)

def physical_two_particle(C):
    modes=C.shape[0];bs=[(a,b) for a in range(modes) for b in range(a+1,modes) if a//3!=b//3]
    lookup={s:i for i,s in enumerate(bs)};cc=C.tocsc();rows=[];cols=[];values=[]
    for col,(a,b) in enumerate(bs):
        for src,other in [(a,b),(b,a)]:
            for pos in range(cc.indptr[src],cc.indptr[src+1]):
                dst=cc.indices[pos]
                if dst//3==other//3:continue
                rows.append(lookup[tuple(sorted((dst,other)))]);cols.append(col);values.append(cc.data[pos]/2)
    return bs,sparse.csr_matrix((values,(rows,cols)),shape=(len(bs),)*2)

def free_two_particle(C):
    bs=list(combinations_with_replacement(range(C.shape[0]),2));lookup={a:i for i,a in enumerate(bs)}
    cc=C.tocsc();rows=[];cols=[];values=[]
    for col,ab in enumerate(bs):
        occ={x:ab.count(x) for x in set(ab)}
        for src,mult in occ.items():
            after=occ.copy();after[src]-=1
            for pos in range(cc.indptr[src],cc.indptr[src+1]):
                dst=cc.indices[pos];new=after.copy();new[dst]=new.get(dst,0)+1
                out=tuple(sorted(x for x,n in new.items() for _ in range(n)))
                rows.append(lookup[out]);cols.append(col)
                values.append(cc.data[pos]/2*math.sqrt(mult*(after.get(dst,0)+1)))
    return bs,sparse.csr_matrix((values,(rows,cols)),shape=(len(bs),)*2)

def pair_vector(bs,v,w=None):
    if w is None:return np.array([v[a]*v[a] if a==b else math.sqrt(2)*v[a]*v[b] for a,b in bs])
    return np.array([math.sqrt(2)*v[a]*w[a] if a==b else v[a]*w[b]+v[b]*w[a] for a,b in bs])

def single(pts,L,q,pol,t,c):
    s=np.sin(2*np.pi*np.array(q)/L)
    X=np.array([[0,-s[2],s[1]],[s[2],0,-s[0]],[-s[1],s[0],0]])
    u=expm(t*c*X)[:,pol]
    phase=np.exp(2j*np.pi*(np.array(pts)@np.array(q))/L)/math.sqrt(len(pts))
    return (phase[:,None]*u).ravel()

def cubic_covariance(pts,C,L):
    ix={x:i for i,x in enumerate(pts)};count=0
    for p in permutations(range(3)):
        for signs in product([-1,1],repeat=3):
            R=np.zeros((3,3),int)
            for i in range(3):R[i,p[i]]=signs[i]
            if round(np.linalg.det(R))!=1:continue
            rows=[];cols=[];vals=[]
            for x in pts:
                y=tuple((R@np.array(x))%L)
                for i in range(3):rows.append(3*ix[y]+i);cols.append(3*ix[x]+p[i]);vals.append(signs[i])
            T=sparse.csr_matrix((vals,(rows,cols)),shape=C.shape)
            assert (T@C-C@T).nnz==0;count+=1
    return count

def local_algebra():
    t=[]
    for i in range(3):
        a=sy.zeros(4);a[0,i+1]=1;t.append(a)
    n=sy.diag(0,1,1,1);checks=0
    for i,j in product(range(3),repeat=2):
        E=sy.zeros(4);E[j+1,i+1]=1
        assert t[i]*t[j].T-t[j].T*t[i]==int(i==j)*(sy.eye(4)-n)-E
        assert t[i]*t[j]-t[j]*t[i]==sy.zeros(4);checks+=2
    # A pair of occupied cells proves that the diagonal 2m/V constant can be sharp.
    E=sy.diag(1,0,0);occupied_defect=-(2*sy.eye(9)+sy.kronecker_product(E,sy.eye(3))+sy.kronecker_product(sy.eye(3),E))
    assert max(abs(x) for x in occupied_defect.eigenvals())==4
    return dict(exact_local_relations=checks,two_occupied_cell_diagonal_defect_norm_times_volume=4)

def run_case(L):
    pts,C=curl(L);V=len(pts);assert (C-C.T).nnz==0
    rotations=cubic_covariance(pts,C,L)
    pb,hc=physical_two_particle(C);bb,free=free_two_particle(C);lookup={a:i for i,a in enumerate(bb)}
    physical=np.array([lookup[a] for a in pb]);mask=np.ones(len(bb),bool);mask[physical]=False
    diff=free[physical][:,physical]-hc;assert diff.nnz==0
    assert (hc-hc.T).nnz==0
    c=.4;mu=1.;q=(1,0,0);r=(0,1,0)
    v=single(pts,L,q,1,0,c);w=single(pts,L,r,0,0,c)
    psi=(pair_vector(bb,v)+pair_vector(bb,v,w))/math.sqrt(2)
    assert abs(np.vdot(psi,psi)-1)<3e-14
    eps=2/math.sqrt(V);alpha=np.linalg.norm(psi[physical]);phi=psi[physical]/alpha
    # Direct compression of each spatial projection to the six Fourier modes.
    E=np.column_stack([single(pts,L,z,i,0,c) for z in [q,r] for i in range(3)])
    compression_max=0.
    for x in range(V):
        vals=np.linalg.eigvalsh(E[3*x:3*x+3].conj().T@E[3*x:3*x+3])
        compression_max=max(compression_max,float(vals.max()))
        assert np.max(abs(vals-np.array([0,0,0,2/V,2/V,2/V])))<3e-15
    rows=[]
    for tau in [.1,.5,1.]:
        t=L*tau
        v=single(pts,L,q,1,t,c);w=single(pts,L,r,0,t,c)
        evolved=(pair_vector(bb,v)+pair_vector(bb,v,w))/math.sqrt(2)
        collision=float(np.linalg.norm(evolved[mask]));assert collision<=eps+1e-13
        # A free evolution assembled only from one-particle 3-by-3 matrices.
        if tau==.1:
            sparse_free=expm_multiply(-1j*t*c*free,psi)
            free_error=float(np.linalg.norm(evolved-sparse_free));assert free_error<1e-12
        actual=expm_multiply(-1j*t*c*hc,phi)
        embedded=np.zeros(len(bb),complex);embedded[physical]=actual
        error=float(np.linalg.norm(embedded-evolved));bound=eps*(1+2*c*math.sqrt(3)*abs(t))+eps**2
        assert error<=bound+1e-12
        qvec=np.zeros_like(evolved);qvec[mask]=evolved[mask]
        forcing=float(np.linalg.norm((c*free@qvec)[physical]));assert forcing<=2*c*math.sqrt(3)*eps+1e-12
        cont_v=single(pts,L,q,1,0,c) # Compare continuum symbol directly in its fixed polarization space below.
        rows.append(dict(tau=tau,physical_time=t,collision_norm=collision,collision_bound=eps,
                         vector_error=error,Duhamel_bound=bound,forcing_norm=forcing))
    e0=float(eigsh(hc,k=1,which='SA',return_eigenvectors=False)[0]) if L==3 else None
    if e0 is not None:assert 2*mu+c*e0>=2*(mu-c*math.sqrt(3))-1e-12
    symbols=[]
    for z in [q,r,(1,1,1)]:
        Q=2*np.pi*np.array(z);delta=L*np.sin(Q/L)-Q
        value=c*np.linalg.norm(delta);bound=c*np.linalg.norm(Q)**3/(6*L**2)
        assert value<=bound+1e-13
        symbols.append(dict(mode=z,operator_error=value,cubic_sine_bound=bound))
    return dict(side=L,physical_dimension=len(pb),boson_dimension=len(bb),proper_rotation_controls=rotations,
                direct_compression_equal=True,initial_collision_probability=float(1-alpha**2),
                spatial_compression_max_norm=compression_max,free_evolution_reconstruction_error=free_error,
                two_particle_laboratory_bottom=None if e0 is None else 2*mu+c*e0,
                two_particle_lower_bound=2*(mu-c*math.sqrt(3)),evolutions=rows,symbol_checks=symbols)

def main():
    out=dict(local_algebra=local_algebra(),cubic_cases=[])
    for L in [3,4]:
        row=run_case(L);out['cubic_cases'].append(row);print(json.dumps(row),flush=True)
    out['scope']='Two actual three-dimensional cubic tori; fixed two-particle sector. Floating dynamics corroborate the analytic estimate. No positive-density, long-scaled-time or original-record claim.'
    (HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['local_algebra']))

if __name__=='__main__':main()
