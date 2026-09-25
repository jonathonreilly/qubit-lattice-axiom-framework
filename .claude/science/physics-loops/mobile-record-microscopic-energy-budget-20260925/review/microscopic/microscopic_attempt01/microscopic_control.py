#!/usr/bin/env python3
"""Own complete physical square matrices and mixed-state bridge diagnostics."""
import hashlib
import itertools
import json
import math
import time
from pathlib import Path
import numpy as np

EDGES=((0,2),(0,3),(1,2),(1,3))


def physical(word):
    q,e=word
    div=[e[0]+e[1],e[2]+e[3],-e[0]-e[2],-e[1]-e[3]]
    assert div==[q[i]-(i<2) for i in range(4)]


def words_for(q,S):
    d=[q[i]-(i<2) for i in range(4)]
    for t in range(-S,S+1):
        e=(t,d[0]-t,-d[2]-t,d[1]+d[2]+t)
        if max(map(abs,e))<=S:
            w=tuple(q),e
            physical(w)
            yield w


def step(w,a,b,i,shift,newa,newb,S):
    q,e=w
    q1,e1=list(q),list(e)
    if S is None:
        weight=1.
    else:
        C=S*(S+1)
        defect=e[i]*(e[i]+shift)
        assert 0<=defect<=C
        if defect==C:
            return None
        weight=math.sqrt(1-defect/C)
    e1[i]+=shift
    q1[a],q1[b]=newa,newb
    out=tuple(q1),tuple(e1)
    physical(out)
    if S is not None:
        assert max(map(abs,e1))<=S
    return out,weight


def Fpaths(w,a,S):
    q,e=w
    if not q[a]:
        return []
    return [answer for i,(aa,b) in enumerate(EDGES)
            if aa==a and not q[b]
            if (answer:=step(w,a,b,i,-q[a],0,q[a],S)) is not None]


def jpath(w,i,sign,S):
    a,b=EDGES[i];q,e=w
    if q[a] or q[b]:
        return None
    return step(w,a,b,i,sign,sign,-sign,S)


def path_matrix(inputs,action):
    columns=[];outputs=set()
    for w in inputs:
        col={}
        for y,value in action(w):
            col[y]=col.get(y,0.)+value
        columns.append(col);outputs.update(col)
    index={w:i for i,w in enumerate(sorted(outputs))}
    mat=np.zeros((len(index),len(inputs)))
    for j,col in enumerate(columns):
        for w,value in col.items():
            mat[index[w],j]=value
    return mat


def common_matrices(pwords):
    pair=path_matrix(pwords,lambda w:[
        (z,xy*yz) for y,xy in Fpaths(w,0,None)
        for z,yz in Fpaths(y,1,None)])
    magnetic=-2*pair.T@pair
    gamma=np.zeros_like(magnetic)
    for i,(a,b) in enumerate(EDGES):
        for sign in (-1,1):
            def action(w):
                ans=[]
                for y,v in Fpaths(w,a,None):
                    item=jpath(y,i,sign,None)
                    if item is not None:
                        z,u=item;ans.append((z,v*u))
                return ans
            B=path_matrix(pwords,action)
            gamma+=B.T@B
    D=np.array([sum(x*x for x in w[1]) for w in pwords],float)
    return np.diag(D)+magnetic,gamma,D,magnetic


def fixture(S):
    C=S*(S+1);eps=1/math.sqrt(C)
    w2=[]
    for slots in itertools.combinations(range(4),2):
        q=[int(i in slots) for i in range(4)]
        w2.extend(words_for(q,S))
    w2=sorted(w2);idx={w:i for i,w in enumerate(w2)}
    w4=[]
    for minus in range(4):
        q=[-1 if i==minus else 1 for i in range(4)]
        w4.extend(words_for(q,S))
    w4=sorted(w4);idx4={w:i for i,w in enumerate(w4)}
    dim=len(w2)
    Fs=[]
    for a in range(2):
        F=np.zeros((dim,dim))
        for col,w in enumerate(w2):
            for y,v in Fpaths(w,a,S):
                F[idx[y],col]+=v
        Fs.append(F)
    W=np.array([sum(x==0 for x in w[0][:2]) for w in w2])
    pi=np.flatnonzero(W==0);pwords=[w2[i] for i in pi]
    T=-sum(F+F.T for F in Fs)
    M=sum((F.T@F)[np.ix_(pi,pi)] for F in Fs)
    hcommon,gammacommon,D,H4rotor=common_matrices(pwords)
    Delta=np.diag(D/C)
    C0=M+Delta
    compensated=np.zeros((dim,dim));compensated[np.ix_(pi,pi)]=C0
    A=T[:,pi].copy();A[W!=1,:]=0
    Z=T@A;Z[W!=2,:]=0
    H4=M@M-(M@C0+C0@M)/2-Z.T@Z/2
    pair=Fs[1]@Fs[0][:,pi]
    H4local=-2*pair.T@pair-(M@Delta+Delta@M)/2
    assert np.max(np.abs(H4-H4local))<2e-12
    small=np.diag(W)+eps*T+eps*eps*compensated
    values,vectors=np.linalg.eigh(small)
    select=values<.5
    assert np.count_nonzero(select)==len(pi)
    eig0=vectors[:,select]
    QP=eig0@eig0[pi,:].T
    gram=QP[pi,:]
    gv,gu=np.linalg.eigh(gram)
    assert gv.min()>.5
    iso=QP@((gu/np.sqrt(gv))@gu.T)
    assert np.max(np.abs(iso.T@iso-np.eye(len(pi))))<3e-13
    H=small/eps**4
    Hlow=iso.T@H@iso
    target=np.diag(D)+H4
    low_error=float(np.linalg.norm(Hlow-target,ord=2))
    assert low_error < 500*eps*eps
    gamma=np.zeros((dim,dim));gamma_coherent=np.zeros_like(gamma)
    gamma_spin=np.zeros((len(pi),len(pi)))
    for i,(a,b) in enumerate(EDGES):
        channels=[]
        for sign in (-1,1):
            j=np.zeros((len(w4),dim))
            for col,w in enumerate(w2):
                item=jpath(w,i,sign,S)
                if item is not None:
                    y,v=item;j[idx4[y],col]+=v
            channels.append(j)
            gamma+=j.T@j/eps**2
            B=j@Fs[a][:,pi]
            gamma_spin+=B.T@B
        coherent=channels[0]+channels[1]
        gamma_coherent+=coherent.T@coherent/eps**2
    assert np.max(np.abs(gamma-gamma_coherent))<1e-11
    assert np.max(np.abs(gammacommon-8*np.eye(len(pi))))<1e-12
    ground=vectors[:,0]
    eground=float(values[0]/eps**4)
    chi=iso.T@ground
    assert abs(np.dot(chi,chi)-1)<3e-13
    energy_common=float(chi@hcommon@chi)
    ground_rate=float(ground@gamma@ground)
    gamma0=float(chi@gammacommon@chi)
    high_indices=np.flatnonzero(~select)
    cross=vectors[:,high_indices].T@gamma@ground
    high_index=int(high_indices[np.argmax(np.abs(cross))])
    high=vectors[:,high_index]
    ehigh=float(values[high_index]/eps**4)
    rhigh=float(high@gamma@high)
    x=float(high@gamma@ground)
    p=eps**4/2
    mixed=[]
    for z in (-1.,0.,1.,.5j):
        energy=(1-p)*eground+p*ehigh
        rate=(1-p)*ground_rate+p*rhigh+2*math.sqrt(p*(1-p))*float(np.real(z*x))
        assert rate>=0
        assert energy-eground>0
        assert abs(rate-gamma0)<100*eps
        mixed.append({"coherence":str(z),"rotated_high_weight":p,
            "actual_mean_energy":energy,"mean_energy_excess":energy-eground,
            "actual_rate":rate,"normalized_low_common_rate":gamma0,
            "rate_difference_over_epsilon":(rate-gamma0)/eps,
            "common_low_energy":energy_common})
    zero=((1,1,0,0),(0,0,0,0))
    evec=np.zeros(len(pi));evec[pwords.index(zero)]=1
    dressed=iso@evec
    bare=np.zeros(dim);bare[idx[zero]]=1
    bare_energy=float(bare@H@bare)
    assert abs(bare_energy-4/eps**2)<1e-9
    assert float(bare@gamma@bare)==0
    full=((1,1,1,-1),(S//2-1,1-S//2,-S//2,S//2))
    physical(full)
    assert full in idx4
    # All sites occupied: every microscopic hop, compensation and jump is zero.
    assert not any(Fpaths(full,a,S) for a in range(2))
    assert not any(jpath(full,i,sign,S) for i in range(4) for sign in (-1,1))
    row={"S":S,"epsilon":eps,"N2_dimension":dim,"N4_dimension":len(w4),
        "low_cluster_dimension":len(pi),"high_cluster_minimum":float(values[~select].min()),
        "canonical_low_remainder_norm":low_error,
        "canonical_low_remainder_over_epsilon_squared":low_error/eps**2,
        "ground_energy":eground,"common_compressed_infimum":float(np.linalg.eigvalsh(hcommon)[0]),
        "normalized_low_common_energy":energy_common,
        "normalized_low_D":float(np.dot(chi*chi,D)),
        "finite_spin_magnetic_form_error":float(chi@(H4-H4rotor)@chi),
        "actual_ground_rate":ground_rate,
        "effective_spin_ground_rate":float(chi@gamma_spin@chi),
        "common_ground_rate":gamma0,
        "ground_bare_high_weight":float(np.sum(ground[W>0]**2)),
        "ground_rotated_high_weight":float(1-np.dot(chi,chi)),
        "bare_P_mean_energy":bare_energy,
        "dressed_P_mean_energy":float(dressed@H@dressed),
        "bare_P_rate":0.,"dressed_P_rate":float(dressed@gamma@dressed),
        "bare_dressed_trace_distance":2*math.sqrt(max(0,1-float(bare@dressed)**2)),
        "full_occupancy_escaping_word":{"q":full[0],"E":full[1],
            "D":0,"microscopic_energy":0,"microscopic_rate":0,"stationary_exact":True},
        "mixed_state_rows":mixed}
    return row


def main():
    t=time.perf_counter()
    rows=[fixture(S) for S in (4,8,12,16,24)]
    print(json.dumps({"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "couplings":{"K":1,"delta":1,"kappa":1},
        "scope":"Own complete physical square finite-spin matrices; finite floating diagnostics, not degree-six root36 evidence or a proof of asymptotic uniformity.",
        "rows":rows,"all_assertions_passed":True,"elapsed_seconds":time.perf_counter()-t},indent=2))


if __name__=="__main__":
    main()
