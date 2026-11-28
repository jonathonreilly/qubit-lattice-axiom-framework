"""Independent 2x2 complex-matrix readout of saved configurations; no sampling."""
import json
from pathlib import Path
import sys
import numpy as np
from batch import SCRATCH,HERE,gate,sha,utc

def matrix(q):
    z=np.empty(q.shape[:-1]+(2,2),dtype=complex)
    z[...,0,0]=q[...,0]-1j*q[...,3]
    z[...,0,1]=-q[...,2]-1j*q[...,1]
    z[...,1,0]=q[...,2]-1j*q[...,1]
    z[...,1,1]=q[...,0]+1j*q[...,3]
    return z

def adj(a):return a.swapaxes(-1,-2).conj()
def trace(a):return np.trace(a,axis1=-2,axis2=-1).real/2

def check(item):
    L,T,model=item['L'],item['T'],item['model']
    n=2*T*T if model=='face' else 4 if model=='p4' else 2
    raw=np.fromfile(SCRATCH/(item['tag']+'.cfg'),dtype=np.float64).reshape(-1,4)
    norm=float(np.max(abs(np.sum(raw*raw,axis=1)-1)))
    p=matrix(raw[:n*L*L].reshape(n,L,L,4))
    gauge=model=='gh' and item['coupling']>=0
    a=matrix(raw[n*L*L:].reshape(2,L,L,4)) if gauge else None
    predicted=np.empty((2,5,L))
    for axis in (0,1):
        # C++ index i=x+L*y. Matrix arrays have axes field,y,x.
        direction=1-axis
        spatial=2 if direction==0 else 1
        for c,r in enumerate(item.get('lengths',(1,4,8,16))):
            other=np.roll(p,-r,axis=spatial)
            if gauge:
                u=np.broadcast_to(np.eye(2),(L,L,2,2)).copy()
                for z in range(r):u=u@np.roll(a[direction],-z,axis=spatial-1)
                other=u[None,...]@other
            val=trace(adj(p)@other).mean(axis=0)
            predicted[axis,c]=val.mean(axis=0 if axis==0 else 1)
        if gauge:
            hol=a[0]@np.roll(a[1],-1,axis=1)@adj(np.roll(a[0],-1,axis=0))@adj(a[1])
            plaquette=trace(hol)
        elif model=='gh':plaquette=np.ones((L,L))
        elif model=='p4':plaquette=trace(p[0]@p[1]@adj(p[2])@adj(p[3]))
        else:
            plaquette=np.zeros((L,L))
            for y in range(T):
                for x in range(T):
                    s=x+T*y;sx=(x+1)%T+T*y;sy=x+T*((y+1)%T)
                    plaquette+=trace(p[2*s]@p[2*sx+1]@adj(p[2*sy])@adj(p[2*s+1]))/(T*T)
        predicted[axis,4]=plaquette.mean(axis=0 if axis==0 else 1)
    saved=np.memmap(SCRATCH/(item['tag']+'.f32'),dtype=np.float32,mode='r').reshape(-1,2,5,L)[-1]
    error=float(np.max(abs(predicted-saved)))
    if error>1e-6 or norm>1e-10:raise RuntimeError('independent matrix readout failed')
    gate()  # Includes the process peak-RSS stop after matrix allocations.
    return dict(tag=item['tag'],max_readout_error=error,max_norm_error=norm,
                configuration_sha256=sha(SCRATCH/(item['tag']+'.cfg')))

def main():
    phase=sys.argv[1]
    done=json.loads((HERE/(phase+'_batch.json')).read_text())
    if not done['all_reaped']:raise RuntimeError('sampler still running')
    gate()
    plan=json.loads((HERE/(phase+'_plan.json')).read_text())['chains']
    # The first hot chain of each distinct coupling, at each beta, on the small size.
    selected=[];seen=set()
    for c in plan:
        key=(c['model'],c['beta'],c['coupling'],c['T'])
        if c['hot']==1 and key not in seen:
            seen.add(key);selected.append(c)
    records=[check(c) for c in selected]
    out=dict(ended=utc(),path='independent complex-matrix multiplication',records=records,
             scientific_status='GUIDE only, no proof discharge')
    (HERE/(phase+'_verification.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(configurations=len(records),max_readout_error=max(r['max_readout_error'] for r in records))))

if __name__=='__main__':main()
