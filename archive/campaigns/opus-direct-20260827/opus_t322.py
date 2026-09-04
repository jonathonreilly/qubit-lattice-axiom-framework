"""
T322 - does the framework possess ANY scale other than the lattice spacing?

"Did we get mass" reduces to this. The packet's spectrum is 0 (six protected
Goldstones, R178/R195) and O(1/a) (the monopole, R164/R165). A mass hierarchy
needs a scale that SEPARATES from a. The only candidate in a statistical model
is the correlation length xi.

Measure the connected correlator of the record field at the Born point and
extract xi. Two outcomes, both informative:
  xi ~ O(1) lattice units  -> one scale only; no hierarchy is expressible
  xi >> a                  -> a second scale exists and the question reopens

CONTROL that decides whether the number means anything: the Born point sits in
the ORDERED phase, where Goldstones make the connected correlator a POWER law
(1/r in d=3), not an exponential. Fitting an exponential to a power law always
returns some finite xi, so the fit form must be tested, not assumed. Both forms
are fitted and their residuals compared.
"""
import numpy as np
L=32; SW=1200; BURN=400
idx=np.indices((L,L,L))
par=(idx.sum(axis=0)%2).astype(bool)
def sweep(v,rng):
    for sub in (True,False):
        m=(par==sub)
        nbs=np.stack([np.roll(v,s,ax) for ax in range(3) for s in (1,-1)],axis=0)
        new=rng.normal(size=v.shape); new/=np.linalg.norm(new,axis=-1,keepdims=True)
        do=np.einsum('n...c,...c->n...',nbs,v); dn=np.einsum('n...c,...c->n...',nbs,new)
        wo=np.prod(1.0+do,axis=0); wn=np.prod(1.0+dn,axis=0)
        acc=((wn>=wo)|(rng.random(wo.shape)*wo<wn))&m&(wo>0)&(wn>=0)
        v=np.where(acc[...,None],new,v)
    return v
rng=np.random.default_rng(3)
v=rng.normal(size=(L,L,L,3)); v/=np.linalg.norm(v,axis=-1,keepdims=True)
acc=np.zeros(L//2+1); cnt=0
for sw in range(SW):
    v=sweep(v,rng)
    if sw>=BURN and sw%8==0:
        M=v.mean(axis=(0,1,2))                      # subtract the condensate
        w=v-M
        F=np.fft.fftn(w,axes=(0,1,2))
        S=np.sum(np.abs(F)**2,axis=-1)
        C=np.real(np.fft.ifftn(S))/L**3
        prof=np.array([C[r,0,0]+C[0,r,0]+C[0,0,r] for r in range(L//2+1)])/3
        acc+=prof; cnt+=1
C=acc/cnt
r=np.arange(1,L//2+1); c=C[1:]
print(f"L={L}, {cnt} measurements.  connected correlator C(r) (condensate removed)\n")
print("    r     C(r)")
for i in range(0,len(r),2): print(f"  {r[i]:4d}   {c[i]:.6e}")
good=(c>0)
rr=r[good]; cc=c[good]
sel=(rr>=2)&(rr<=L//2-2)
# exponential fit  log C = a - r/xi
A=np.vstack([np.ones(sel.sum()),-rr[sel]]).T
be,rese,_,_=np.linalg.lstsq(A,np.log(cc[sel]),rcond=None)
xi=1/be[1] if be[1]>0 else np.inf
# power fit  log C = a - p log r
A2=np.vstack([np.ones(sel.sum()),-np.log(rr[sel])]).T
bp,resp,_,_=np.linalg.lstsq(A2,np.log(cc[sel]),rcond=None)
re_=np.sqrt(rese[0]/sel.sum()) if len(rese) else np.nan
rp_=np.sqrt(resp[0]/sel.sum()) if len(resp) else np.nan
print(f"\n  exponential fit:  xi = {xi:.3f} a        rms resid {re_:.4f}")
print(f"  power-law fit:    C ~ r^-{bp[1]:.3f}      rms resid {rp_:.4f}")
print(f"\n  better form: {'POWER LAW (massless)' if rp_<re_ else 'exponential (massive)'}")
print("  a power law means xi is infinite and the exponential xi is an artefact of")
print("  fitting the wrong form -- i.e. NO second scale, not a small one.")
