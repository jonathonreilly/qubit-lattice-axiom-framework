"""
T287 - the dilution verdict, read against the control.

T286's p=1.00 row is the control: identical pipeline, identical probe vectors,
identical s grid. Its deviation from 1.000 is the pipeline's own error, so the
statistic with common-mode error removed is  collapse(p)/collapse(p=1).
That is what R184 reached for ("comparing rows measured identically") but could
not use, because its D was 39% wrong at p=0.70 and its normalisation omitted q.
Both absolute and control-normalised are reported, so the gap between what the
pipeline can resolve and what the physics says stays visible.
"""
import numpy as np, os, glob
_xc=np.array([0.0,0.05,0.10,0.20,0.35,0.50]); _rc=np.array([1.0,1.01150,1.02374,1.05038,1.09533,1.14569])
_cf=np.polyfit(_xc,_rc-1.0,3); R_cont=lambda x: 1.0+np.polyval(_cf,x)
xs=np.array([0.10,0.16,0.24,0.34,0.46]); Ls=[40,56,72]; ps=[1.00,0.85,0.70]
d={}
for L in Ls:
    for p in ps:
        fn=f"t286_{L}_{int(p*100)}.npy"
        if os.path.exists(fn): d[(L,p)]=np.load(fn)
have=sorted(d.keys()); print(f"rows available: {len(have)}/9")
C={}
for (L,p),v in d.items():
    Rtil,D,q,s=v; C[(L,p)]=q*D**1.5*Rtil/R_cont(D*xs)
print("\n=== ABSOLUTE:  q * D^1.5 * Rtil / R_cont(D x) ===")
print("     L    p     "+"".join(f"  x={x:.2f}" for x in xs))
for L in Ls:
    for p in ps:
        if (L,p) in C:
            print(f"   {L:3d}  {p:.2f}   "+" ".join(f"{v:7.4f}" for v in C[(L,p)])
                  +("   <-- control, must be 1.000" if p>=1.0 else ""))
print("\n=== CONTROL-NORMALISED:  collapse(p)/collapse(p=1)   (1.000 = survives) ===")
print("     L    p     "+"".join(f"  x={x:.2f}" for x in xs)+"     mean")
for L in Ls:
    for p in ps:
        if p>=1.0 or (L,p) not in C or (L,1.00) not in C: continue
        r=C[(L,p)]/C[(L,1.00)]
        print(f"   {L:3d}  {p:.2f}   "+" ".join(f"{v:7.4f}" for v in r)+f"   {r.mean():7.4f}")
print("\n=== 1/s artifact removed (fit over available L at fixed x) ===")
print("     p     "+"".join(f"  x={x:.2f}" for x in xs)+"     mean")
for p in ps:
    if p>=1.0: continue
    Lok=[L for L in Ls if (L,p) in C and (L,1.00) in C]
    if len(Lok)<2: print(f"   {p:.2f}   (only {len(Lok)} L available)"); continue
    out=[]
    for k,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in Lok])
        rv=np.array([C[(L,p)][k]/C[(L,1.00)][k] for L in Lok])
        out.append(np.polyfit(1.0/sv,rv,1)[1])
    out=np.array(out); print(f"   {p:.2f}   "+" ".join(f"{v:7.4f}" for v in out)+f"   {out.mean():7.4f}   [L={Lok}]")
print("\nD_heat spread (flat => a single D exists at that p; rising => it runs):")
for L in Ls:
    for p in ps:
        if (L,p) in d:
            D=d[(L,p)][1]; print(f"   L={L:3d} p={p:.2f}  "+" ".join(f"{v:6.4f}" for v in D)+f"   {D.max()/D.min():.3f}x")
