#!/usr/bin/env python3
"""Free coupled vacuum coefficient: Pauli formula vs real-space CAR action."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=[]
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh,null_space
S=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
T=np.array([(-S[2]-1j*S[0])/2,(-S[2]-1j*S[1])/2,-S[2]/2])


def band(p):
    d=np.stack([np.sin(p[...,0]),np.sin(p[...,1]),2.5-np.cos(p).sum(axis=-1)],axis=-1)
    e=np.linalg.norm(d,axis=-1);n=np.divide(d,e[...,None],out=np.zeros_like(d),where=e[...,None]>1e-12)
    n=np.where((e<1e-12)[...,None],np.array([0.,0.,1.]),n)
    return e,n


def vertices(p,k):
    mid=p+k/2;out=np.zeros((len(p),3,3))
    out[:,0,0]=-np.cos(mid[:,0]);out[:,0,2]=-np.sin(mid[:,0])
    out[:,1,1]=-np.cos(mid[:,1]);out[:,1,2]=-np.sin(mid[:,1])
    out[:,2,2]=-np.sin(mid[:,2]);return out


def current_weight(n,n2,b,P):
    pair=np.einsum('pia,pja->pij',b,b)
    nb=np.einsum('pa,pia->pi',n,b);n2b=np.einsum('pa,pia->pi',n2,b)
    out=.5*((1+np.einsum('pa,pa->p',n,n2))*np.einsum('ij,pij->p',P,pair)-2*np.einsum('ij,pi,pj->p',P,nb,n2b))
    assert out.min()>-2e-12 and out.max()<3+2e-12
    return np.maximum(out,0)


def coefficient(L):
    index=np.array(list(itertools.product(range(L),repeat=3)));p=2*math.pi*index/L;V=len(p)
    e,n=band(p);norm=energy=soft=0.;ward=0.;softcut=1.
    for ind in index[1:]:
        k=2*math.pi*ind/L;s=2*np.sin(k/2);w=np.linalg.norm(s);P=np.eye(3)-np.outer(s,s)/(w*w)
        e2,n2=band(p+k);b=vertices(p,k)
        # h(p)-h(p+k) in Pauli coordinates; keep actual d at exact zero nodes.
        d=np.stack([np.sin(p[:,0]),np.sin(p[:,1]),2.5-np.cos(p).sum(axis=1)],axis=1)
        d2=np.stack([np.sin(p[:,0]+k[0]),np.sin(p[:,1]+k[1]),2.5-np.cos(p+k).sum(axis=1)],axis=1)
        ward=max(ward,float(np.max(np.abs(np.einsum('i,pia->pa',s,b)-(d-d2)))))
        weight=current_weight(n,n2,b,P);den=w+e+e2
        summ=(weight/(w*den**2)).sum();norm+=summ;energy+=(weight/(w*den)).sum()
        if w<softcut:soft+=summ
    assert ward<2e-13
    # Two conjugate charge species cancel the single-species factor1/2.
    return {'L':L,'volume':V,'paired_first_correction_norm_density':norm/V**2,'paired_second_energy_coefficient_magnitude':energy/V**2,'photon_frequency_below_one_norm_density':soft/V**2,'exact_node_count':int(np.sum(e<1e-12)),'ward_max_error':ward}


def car_hop(bits,a,i):
    assert bits>>i&1 and not(bits>>a&1)
    sign=(-1)**((bits&((1<<i)-1)).bit_count());bits^=1<<i
    sign*=(-1)**((bits&((1<<a)-1)).bit_count());return bits|(1<<a),sign


def physical_fock_check():
    L=3;x=np.array(list(itertools.product(range(L),repeat=3)));V=len(x);p=2*math.pi*x/L;lookup={tuple(z):i for i,z in enumerate(x)}
    e,n=band(p);W=np.zeros((2*V,2*V),complex);H=np.zeros_like(W);us=[]
    for z in range(V):
        hp=np.einsum('a,aij->ij',e[z]*n[z],S);ev,u=eigh(hp);us.append(u)
        for a in range(V):
            phase=np.exp(1j*x[a]@p[z])/math.sqrt(V)
            W[2*a:2*a+2,z]=phase*u[:,0];W[2*a:2*a+2,V+z]=phase*u[:,1]
    for a,xx in enumerate(x):
        H[2*a:2*a+2,2*a:2*a+2]+=2.5*S[2]
        for i in range(3):
            yy=xx.copy();yy[i]=(yy[i]+1)%L;b=lookup[tuple(yy)]
            H[2*a:2*a+2,2*b:2*b+2]+=T[i];H[2*b:2*b+2,2*a:2*a+2]+=T[i].conj().T
    assert np.linalg.norm(W.conj().T@W-np.eye(2*V))<1e-12
    assert np.linalg.norm(H@W-W*np.r_[-e,e])<1e-12
    vac=(1<<V)-1;value=0.;matrix_error=0.;states=0;trace_error=0.
    for kind in x[1:]:
        k=2*math.pi*kind/L;s=2*np.sin(k/2);w=np.linalg.norm(s);polar=null_space(s[None,:]);jband=[]
        for i in range(3):
            J=np.zeros_like(H)
            for a,xx in enumerate(x):
                yy=xx.copy();yy[i]=(yy[i]+1)%L;b=lookup[tuple(yy)]
                phase=np.exp(1j*(xx@k+k[i]/2))/math.sqrt(V)
                J[2*a:2*a+2,2*b:2*b+2]+=-1j*phase*T[i]
                J[2*b:2*b+2,2*a:2*a+2]+=1j*phase*T[i].conj().T
            Jb=W.conj().T@J@W;jband.append(Jb);trace_error=max(trace_error,abs(np.trace(Jb[:V,:V])))
            bcoef=vertices(p,k)
            for pp,pi in enumerate(x):
                rr=lookup[tuple((pi+kind)%L)]
                target=us[rr][:,1].conj()@np.einsum('a,aij->ij',bcoef[pp,i],S)@us[pp][:,0]/math.sqrt(V)
                matrix_error=max(matrix_error,abs(Jb[V+rr,pp]-target))
        for pol in polar.T:
            vertex=sum(pol[i]*jband[i] for i in range(3))/math.sqrt(2*w)
            fock={}
            for i in range(V):
                for a in range(V,2*V):
                    bits,sgn=car_hop(vac,a,i);ampl=sgn*vertex[a,i]/(w+e[a-V]+e[i]);fock[bits]=fock.get(bits,0)+ampl
            states+=len(fock);value+=sum(abs(a)**2 for a in fock.values())
    pred=coefficient(L)['paired_first_correction_norm_density']
    observed=2*value/V
    assert matrix_error<1e-12 and trace_error<1e-12
    assert abs(observed-pred)<1e-13
    return {'L':L,'fermion_modes':2*V,'occupied_modes':V,'one_photon_particle_hole_basis_entries':states,'physical_current_band_matrix_error':matrix_error,'vacuum_current_trace_error':float(trace_error),'paired_direct_CAR_norm_density':observed,'paired_momentum_norm_density':pred,'difference':abs(observed-pred)}


def run():
    t=time.time();fock=physical_fock_check();rows=[coefficient(L) for L in [4,6,8,10,12]]
    assert all(np.isfinite(r['paired_first_correction_norm_density']) and r['paired_first_correction_norm_density']>0 for r in rows)
    assert rows[1]['exact_node_count']==2 and rows[-1]['exact_node_count']==2
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'real_space_CAR_vs_momentum':fock,'finite_reference_coefficients':rows,'seconds':time.time()-t},indent=2))

if __name__=='__main__':run()
