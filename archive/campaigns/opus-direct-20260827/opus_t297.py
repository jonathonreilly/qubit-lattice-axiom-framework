"""
T297 - is the +-6% scatter probe noise or DISORDER-REALISATION scatter?

The stochastic pipeline reproduces the exact Bloch answer to 1.4% (T295), yet
the p=0.85 collapse ratio scatters +-5.8% across L=40,48,56,72.  Each L used a
DIFFERENT random dilution, so that spread may be genuine sample-to-sample
fluctuation of the disordered medium, not instrument error.

Decisive test: hold L fixed and vary only the disorder seed.  If the seed-to-seed
spread is ~6%, realisation scatter is the limit and more probes would not help --
averaging over realisations would.
"""
import numpy as np
from scipy.sparse import diags
from opus_t288 import build, giant, cheb_trace, K_pure
_xc=np.array([0.0,0.05,0.10,0.20,0.35,0.50]); _rc=np.array([1.0,1.01150,1.02374,1.05038,1.09533,1.14569])
_cf=np.polyfit(_xc,_rc-1.0,3); R_cont=lambda x: 1.0+np.polyval(_cf,x)
L=48; xs=np.array([0.10,0.16,0.24,0.34,0.46]); kap=2*np.pi/L; s=xs/kap**2; h=0.05
def row(p,seed):
    g=giant(L,p,seed); idx=np.where(g)[0]; n=len(idx)
    rng=np.random.default_rng(101); Z=rng.choice([-1.0,1.0],size=(n,32))
    Ks={};Vs={}
    for ei in (-2,-1,0,1,2):
        A,m=build(L,ei*h,g); ms=m[idx]
        Dm=diags(1.0/np.sqrt(ms)); B=(Dm@A[idx][:,idx]@Dm).tocsr(); del A
        Ks[ei]=cheb_trace(B,s,Z,float(abs(B).sum(axis=1).max())*1.02); Vs[ei]=ms.sum(); del B
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    Rtil=(4*np.pi*s)**1.5*d2(Ks)/d2(Vs); D=(K_pure(L,s)/Ks[0])**(2.0/3.0)
    return (n/L**3)*D**1.5*Rtil/R_cont(D*xs)
seeds=[11,23,37,51,67]
print(f"L={L}, h=0.05, nz=32, five disorder seeds; probe vectors IDENTICAL across seeds")
base={}
for p in (1.00,0.85,0.70):
    print(f"\n  p={p:.2f}")
    ms=[]
    for sd in seeds:
        c=row(p,sd) if p<1.0 else row(1.00,11)
        base.setdefault(p,{})[sd]=c
        print(f"    seed {sd:3d}  "+" ".join(f"{v:7.4f}" for v in c)+f"   mean {c.mean():7.4f}")
        ms.append(c.mean())
        if p>=1.0: break
    if p<1.0:
        ms=np.array(ms); print(f"    seed-to-seed: mean {ms.mean():.4f}  sd {ms.std(ddof=1):.4f}  spread {ms.max()-ms.min():.4f}")
print("\n  ratio to the p=1 control, per seed:")
for p in (0.85,0.70):
    r=np.array([ (base[p][sd]/base[1.00][11]).mean() for sd in seeds ])
    print(f"   p={p:.2f}  "+" ".join(f"{v:.4f}" for v in r)
          +f"   mean {r.mean():.4f}  sd {r.std(ddof=1):.4f}")
