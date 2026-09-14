"""Charged four-cycle: independently assembled flux-basis clock/rotor dynamics."""
from pathlib import Path
import json,math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

L=4;g=.7;r=.25;kappa=1/g**2;time=.65

def flux(a,b,n):
    charge=np.zeros(L,dtype=int);charge[a]+=1;charge[b]-=1
    return tuple(np.r_[np.cumsum(charge)[:L-1],0]+n)

def divergence(e):return tuple(e[i]-e[(i-1)%L] for i in range(L))

def assemble(S,cyclic):
    N=2*S+1;basis=[]
    for a in range(L):
        for b in range(L):
            for n in range(-S,S+1):
                e=flux(a,b,n)
                if cyclic:e=tuple((v+S)%N-S for v in e)
                if all(abs(v)<=S for v in e):basis.append((a,b,e))
    ix={v:i for i,v in enumerate(basis)};rows=[];cols=[];vals=[]
    def add(i,target,z):
        if cyclic:target=(target[0],target[1],tuple((v+S)%N-S for v in target[2]))
        if target in ix:rows.append(ix[target]);cols.append(i);vals.append(z)
    for i,(a,b,e) in enumerate(basis):
        lam=lambda n:g*g*N*N/(2*math.pi**2)*math.sin(math.pi*n/N)**2 if cyclic else g*g*n*n/2
        add(i,(a,b,e),sum(lam(v) for v in e)+kappa)
        for orient in [-1,1]:add(i,(a,b,tuple(v+orient for v in e)),-kappa/2)
        for l in range(L):
            x=l;y=(l+1)%L
            for pos,species,charge in [(a,0,1),(b,1,-1)]:
                if pos==y:
                    new=list(e);new[l]+=charge
                    add(i,(x if species==0 else a,x if species==1 else b,tuple(new)),r)
                if pos==x:
                    new=list(e);new[l]-=charge
                    add(i,(y if species==0 else a,y if species==1 else b,tuple(new)),r)
    H=coo_matrix((vals,(rows,cols)),shape=(len(basis),len(basis))).tocsr()
    assert np.linalg.norm((H-H.T).data)<1e-12
    init=np.zeros(len(basis));init[ix[(0,0,(0,)*L)]]=1
    state=expm_multiply(-1j*time*H,init)
    assert abs(np.vdot(state,state)-1)<1e-12
    return basis,state

reference,psi=assemble(40,False);lookup=dict(zip(reference,psi));J=2*r+kappa/2
lam=1.0;C=math.exp(2*J*time*math.sinh(lam));A4=(4/(math.e*lam))**4
reference_bound=2*time*L*J*math.exp(-2*40+2*J*time*math.sinh(2))
out=[]
for S in [1,2,3,4,6,8,12,16,24,32]:
    basis,phi=assemble(S,True);N=2*S+1
    overlap=sum(np.conjugate(lookup.get(v,0))*z for v,z in zip(basis,phi))
    err2=max(0,2-2*overlap.real);err=math.sqrt(err2)
    alias=0
    for (a,b,e),z in zip(basis,phi):
        q=[0]*L;q[a]+=1;q[b]-=1
        if divergence(e)!=tuple(q):alias+=abs(z)**2
    bound=min(2,4*time*L*J*math.exp(-lam*S)*C + math.pi**2*g*g*time/(6*N*N)*A4*L*C)
    assert err<=bound+reference_bound+1e-10
    out.append({'N':N,'dimension':len(basis),'state_norm_error':err,'N_squared_error':N*N*err,'modulo_alias_probability':alias,'proved_bound':bound})
p=Path(__file__).with_name('BLOCK1_CLOCK_ROTOR_CHECK.json');p.write_text(json.dumps({'reference_S':40,'reference_dimension':len(reference),'reference_truncation_bound':reference_bound,'time':time,'g':g,'r':r,'kappa':kappa,'cases':out},indent=2)+'\n')
print('reference truncation bound',reference_bound)
for z in out:print(z)
