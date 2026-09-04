"""
T291 - the dilution verdict: extrapolate the diluted lattice's OWN artifact.

The control-normalised collapse still carries a 1/s artifact, and the diluted
row's artifact is NOT the pure lattice's: the pure lattice's is ~1.0/s (R188),
the diluted one runs at ~1/(D s) because the diffusion constant rescales the
probing scale. So dividing by the control does not remove it -- it leaves a
residual ~ (1/D - 1)/s, which is +4% at p=0.85, x=0.10 and shrinks with s.

So fit each row's own artifact:  C(p,s) = A_p + B_p/s,  over L = 40,48,56 at
fixed x, and read A_p (the extrapolated collapse) and B_p (its artifact).
Checks that make the fit falsifiable rather than decorative:
  - A must be 1.000 for the p=1.00 control (nothing else is calibrated);
  - B for p=1.00 must come out ~1.0, matching R188's independent measurement;
  - B for p<1 should be near 1/D if the artifact is simply rescaled by D.
"""
import numpy as np, os
_xc=np.array([0.0,0.05,0.10,0.20,0.35,0.50]); _rc=np.array([1.0,1.01150,1.02374,1.05038,1.09533,1.14569])
_cf=np.polyfit(_xc,_rc-1.0,3); R_cont=lambda x: 1.0+np.polyval(_cf,x)
xs=np.array([0.10,0.16,0.24,0.34,0.46]); Ls=[40,48,56]; ps=[1.00,0.85,0.70]
d={}
for L in Ls:
    for p in ps:
        fn=f"t290_{L}_{int(p*100)}.npy"
        if os.path.exists(fn): d[(L,p)]=np.load(fn)
print(f"rows: {sorted(d.keys())}\n")
C={}; Dm={}
for (L,p),v in d.items():
    Rtil,D,q,s=v; C[(L,p)]=q*D**1.5*Rtil/R_cont(D*xs); Dm[(L,p)]=D
print("=== ABSOLUTE collapse C = q D^1.5 Rtil / R_cont(Dx) ===")
print("     L    p     "+"".join(f"  x={x:.2f}" for x in xs))
for L in Ls:
    for p in ps:
        if (L,p) in C: print(f"   {L:3d}  {p:.2f}   "+" ".join(f"{v:7.4f}" for v in C[(L,p)])
                             +("   <-- control" if p>=1.0 else ""))
print("\n=== fit C = A + B/s over L at fixed x, per p ===")
for p in ps:
    Lok=[L for L in Ls if (L,p) in C]
    if len(Lok)<2: continue
    A=[];B=[]
    for k,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in Lok]); cv=np.array([C[(L,p)][k] for L in Lok])
        b,a=np.polyfit(1.0/sv,cv,1); A.append(a); B.append(b)
    A=np.array(A); B=np.array(B); Dmean=np.mean([Dm[(L,p)].mean() for L in Lok])
    tag="  <-- must be A=1.000, B~1.0 (R188)" if p>=1.0 else f"   1/D = {1/Dmean:.3f}"
    print(f"  p={p:.2f}  A = "+" ".join(f"{v:7.4f}" for v in A)+f"   mean {A.mean():7.4f}")
    print(f"           B = "+" ".join(f"{v:7.3f}" for v in B)+f"   mean {B.mean():7.3f}{tag}")
print("\n=== control-normalised extrapolated collapse  A(p)/A(1.00) ===")
Aall={}
for p in ps:
    Lok=[L for L in Ls if (L,p) in C]
    if len(Lok)<2: continue
    Aall[p]=np.array([np.polyfit(1.0/np.array([x/(2*np.pi/L)**2 for L in Lok]),
                                 np.array([C[(L,p)][k] for L in Lok]),1)[1] for k,x in enumerate(xs)])
for p in ps:
    if p>=1.0 or p not in Aall or 1.00 not in Aall: continue
    r=Aall[p]/Aall[1.00]
    print(f"  p={p:.2f}   "+" ".join(f"{v:7.4f}" for v in r)+f"   mean {r.mean():7.4f}")
