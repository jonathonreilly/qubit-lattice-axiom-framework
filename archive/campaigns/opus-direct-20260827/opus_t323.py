"""
T323 - is T322's xi = 4.6a a real scale, or a finite-size artefact?

T322 fitted the connected correlator and got xi = 4.604a, exponential beating
power law. My control there was inadequate: subtracting the SAMPLE mean forces
sum_r C(r) ~ 0, which bends the tail down and makes a power law look
exponential. Note 4.604/32 = 0.144, suspiciously proportional to L.

The decisive control is the one I should have used: vary L.
   xi proportional to L  -> finite-size artefact; NO second scale
   xi independent of L   -> a genuine correlation length, and the framework has
                            a scale other than the spacing (which would matter)

Also reported: the TRANSVERSE correlator taken about the instantaneous
magnetisation direction, which is the physically correct Goldstone channel and
does not require subtracting a sample mean at all.
"""
import numpy as np
def run(L,SW=1100,BURN=350,seed=3):
    idx=np.indices((L,L,L)); par=(idx.sum(axis=0)%2).astype(bool)
    rng=np.random.default_rng(seed)
    v=rng.normal(size=(L,L,L,3)); v/=np.linalg.norm(v,axis=-1,keepdims=True)
    accC=np.zeros(L//2+1); accT=np.zeros(L//2+1); cnt=0
    for sw in range(SW):
        for sub in (True,False):
            m=(par==sub)
            nbs=np.stack([np.roll(v,s,ax) for ax in range(3) for s in (1,-1)],axis=0)
            new=rng.normal(size=v.shape); new/=np.linalg.norm(new,axis=-1,keepdims=True)
            do=np.einsum('n...c,...c->n...',nbs,v); dn=np.einsum('n...c,...c->n...',nbs,new)
            wo=np.prod(1.0+do,axis=0); wn=np.prod(1.0+dn,axis=0)
            acc=((wn>=wo)|(rng.random(wo.shape)*wo<wn))&m&(wo>0)&(wn>=0)
            v=np.where(acc[...,None],new,v)
        if sw>=BURN and sw%8==0:
            M=v.mean(axis=(0,1,2)); Mh=M/np.linalg.norm(M)
            w=v-M                                    # T322's channel
            F=np.fft.fftn(w,axes=(0,1,2)); S=np.sum(np.abs(F)**2,axis=-1)
            C=np.real(np.fft.ifftn(S))/L**3
            accC+=np.array([ (C[r,0,0]+C[0,r,0]+C[0,0,r])/3 for r in range(L//2+1)])
            t=v-np.einsum('...c,c->...',v,Mh)[...,None]*Mh     # transverse channel
            Ft=np.fft.fftn(t,axes=(0,1,2)); St=np.sum(np.abs(Ft)**2,axis=-1)
            Ct=np.real(np.fft.ifftn(St))/L**3
            accT+=np.array([ (Ct[r,0,0]+Ct[0,r,0]+Ct[0,0,r])/3 for r in range(L//2+1)])
            cnt+=1
    return accC/cnt, accT/cnt
def xi_of(C,L):
    r=np.arange(1,L//2+1); c=C[1:]
    s=(r>=2)&(r<=L//2-2)&(c>0)
    if s.sum()<4: return np.nan
    A=np.vstack([np.ones(s.sum()),-r[s]]).T
    b=np.linalg.lstsq(A,np.log(c[s]),rcond=None)[0]
    return 1/b[1] if b[1]>0 else np.inf
print("control: does xi track L?   xi ~ 0.14 L would mean finite-size artefact\n")
print("    L     xi (mean-subtracted)   xi/L      xi (transverse)   xi/L")
for L in (16,24,32,48):
    C,T=run(L)
    x1=xi_of(C,L); x2=xi_of(T,L)
    print(f"  {L:4d}   {x1:12.3f}        {x1/L:.4f}   {x2:12.3f}     {x2/L:.4f}")
print("\n  xi/L constant  => artefact, no second scale")
print("  xi constant    => a genuine correlation length")
