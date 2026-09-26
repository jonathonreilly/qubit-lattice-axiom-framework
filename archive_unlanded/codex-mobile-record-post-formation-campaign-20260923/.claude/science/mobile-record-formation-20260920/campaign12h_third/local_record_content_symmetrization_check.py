"""Finite controls for supplied local exchange cooling of record contents.
No field model is imported. Exact modular rank supplements the general proof.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import numpy as np
from scipy.linalg import expm, eigvals
HERE=Path(__file__).resolve().parent

def rank_mod(a, prime=65521):
    a=np.array(a,dtype=np.int64,copy=True)%prime; row=0
    for col in range(a.shape[1]):
        pivot=next((i for i in range(row,a.shape[0]) if a[i,col]),None)
        if pivot is None: continue
        a[[row,pivot]]=a[[pivot,row]]
        a[row]=a[row]*pow(int(a[row,col]),-1,prime)%prime
        for i in range(row+1,a.shape[0]):
            if a[i,col]: a[i]=(a[i]-a[i,col]*a[row])%prime
        row+=1
        if row==a.shape[0]:break
    return row

def onehot(w,k):return np.eye(k,dtype=np.int64)[list(w)].ravel()

def case(counts):
    n,k=sum(counts),len(counts)
    words=[w for w in product(range(k),repeat=n)
           if tuple(Counter(w)[a] for a in range(k))==counts]
    index={w:i for i,w in enumerate(words)}; dim=len(words)
    jumps2,rows,adj=[],[],[set() for _ in words]
    for x,y in [(i,i+1) for i in range(n-1)]:
        for alpha in range(k):
            for beta in range(alpha+1,k):
                twice=np.zeros((dim,dim),dtype=np.int64); deltas=[]
                for i,w in enumerate(words):
                    if (w[x],w[y])!=(alpha,beta):continue
                    z=list(w);z[x],z[y]=z[y],z[x];z=tuple(z);j=index[z]
                    twice[i,i]+=1;twice[j,i]+=1;twice[i,j]-=1;twice[j,j]-=1
                    adj[i].add(j);adj[j].add(i)
                    deltas.append(onehot(z,k)-onehot(w,k))
                if not deltas:continue
                assert all(np.array_equal(v,deltas[0]) for v in deltas)
                assert not np.any(twice@np.ones(dim,dtype=np.int64))
                gram4=twice.T@twice
                assert np.array_equal(gram4@gram4,4*gram4)
                assert not np.any(twice@twice)
                jumps2.append(twice)
                rows.append({"edge":[x,y],"colors":[alpha,beta],
                             "spectator_pairs":len(deltas),
                             "fixed_displacement":deltas[0].tolist()})
    reached,frontier={0},[0]
    while frontier:
        v=frontier.pop()
        for w in adj[v]-reached:reached.add(w);frontier.append(w)
    assert len(reached)==dim
    # Column-major vectorization. 4 times the Lindblad generator is integer.
    generator4=np.zeros((dim*dim,dim*dim),dtype=np.int64)
    identity=np.eye(dim,dtype=np.int64); rate=np.zeros((dim,dim))
    for a in jumps2:
        gram4=a.T@a
        anti=np.kron(identity,gram4)+np.kron(gram4.T,identity)
        assert not np.any(anti%2)
        generator4+=np.kron(a,a)-anti//2;rate+=gram4/4
    target_int=np.ones((dim,dim),dtype=np.int64).ravel(order="F")
    trace=identity.ravel(order="F")
    assert not np.any(generator4@target_int)
    assert not np.any(trace@generator4)
    rank=rank_mod(generator4);assert rank==dim*dim-1
    generator=generator4/4; ev=eigvals(generator)
    assert np.count_nonzero(abs(ev)<1e-9)==1
    assert max(ev.real)<1e-10
    gap=min(-v.real for v in ev if abs(v)>1e-9);assert gap>0
    target=np.ones((dim,dim))/dim
    initial=np.zeros((dim,dim));initial[0,0]=1
    projector=np.outer(target.ravel(order="F"),trace)
    integrated=-np.linalg.solve(generator+projector,
                  (initial-target).ravel(order="F")).reshape((dim,dim),order="F")
    total_events=np.trace(rate@integrated).real;assert total_events>0
    dynamics=[]
    for time in (.5,3.,20.):
        rho=(expm(time*generator)@initial.ravel(order="F")).reshape((dim,dim),order="F")
        assert np.linalg.norm(rho-rho.T)<1e-10
        assert abs(np.trace(rho)-1)<1e-10
        assert np.linalg.eigvalsh(rho).min()>-1e-10
        dynamics.append({"time":time,"Dicke_fidelity":float(np.sum(rho)/dim),
          "trace_distance":float(np.abs(np.linalg.eigvalsh(rho-target)).sum()/2),
          "instantaneous_jump_rate":float(np.trace(rate@rho))})
    return {"counts":counts,"dimension":dim,"jump_families":rows,
      "configuration_graph_connected":True,
      "integer_scaled_generator_rank_mod_65521":rank,
      "exact_complex_kernel_dimension_certificate":1,
      "numerical_decay_gap":float(gap),
      "expected_total_cooling_events_from_first_word":float(total_events),
      "dynamics":dynamics}

def occupied_sublattice_graph(d,length):
    sites=[x for x in product(range(length),repeat=d) if sum(x)%2==0]
    vertices=set(sites);reached={sites[0]};frontier=[sites[0]]
    while frontier:
        x=frontier.pop()
        for a in range(d):
            for b in range(a+1,d):
                for sa in (-1,1):
                    for sb in (-1,1):
                        y=list(x);y[a]=(y[a]+sa)%length;y[b]=(y[b]+sb)%length
                        y=tuple(y);assert y in vertices
                        if y not in reached:reached.add(y);frontier.append(y)
    assert reached==vertices
    return {"dimension":d,"period":length,"A_vertices":len(sites),
            "face_diagonal_graph_connected":True}

def main():
    source=Path(__file__).read_bytes()
    out={"created_utc":datetime.now(timezone.utc).isoformat(),
         "script":{"path":str(Path(__file__).resolve()),"bytes":len(source),
                   "sha256":hashlib.sha256(source).hexdigest()},
         "cases":[case(c) for c in [(2,1),(2,2),(1,1,1),(2,1,1),(3,2)]],
         "geometry":[occupied_sublattice_graph(d,6) for d in (2,3)],
         "status":"Author controls passed for engineered local color exchange cooling.",
         "scope":"Finite count sectors; coherent Dicke preparation, no autonomous native implementation or uniform gap claim."}
    (HERE/"LOCAL_RECORD_CONTENT_SYMMETRIZATION_RESULTS.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
