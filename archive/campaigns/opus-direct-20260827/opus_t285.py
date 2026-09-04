"""
T285 - the dilution verdict, read against the control rather than against 1.

T281's p=1.00 control reads 1.010-1.037 at L=72 (it must be exactly 1.000):
the stochastic trace is relatively noisier at large s, where the trace is small
and dominated by few modes. That is 1.5-5.6% propagated through D^{3/2} -- too
coarse for a 1%-resolution absolute statement.

But the p=1.00 row IS the control, measured through the identical pipeline with
the identical probe vectors and s grid. So the statistic with the common-mode
pipeline error removed is
      collapse(p) / collapse(p=1)
which is what R184 reached for ("comparing rows measured identically") but
could not use, because its D was wrong by 39% at p=0.70 and its normalisation
omitted q.

Reported both ways, absolute and control-normalised, so the difference between
"what the pipeline can resolve" and "what the physics says" stays visible.
"""
import numpy as np
from opus_t275 import R_cont
d=np.load("t281_raw.npz")
xs=d["xs"]; Ls=d["Ls"]; ps=d["ps"]; RT=d["RT"]; DD=d["DD"]; QQ=d["QQ"]
C={}
for i,L in enumerate(Ls):
    for j,p in enumerate(ps):
        D=DD[i,j]; C[(L,p)]=QQ[i,j]*D**1.5*RT[i,j]/R_cont(D*xs)
print("=== ABSOLUTE:  q * D^1.5 * Rtil / R_cont(D x) ===")
print("     L    p     "+"".join(f"  x={x:.2f}" for x in xs))
for i,L in enumerate(Ls):
    for j,p in enumerate(ps):
        tag="   <-- control, must be 1.000" if p>=1.0 else ""
        print(f"   {L:3d}  {p:.2f}   "+" ".join(f"{v:7.4f}" for v in C[(L,p)])+tag)
print("\n=== CONTROL-NORMALISED:  collapse(p) / collapse(p=1)  (1.000 = survives) ===")
print("     L    p     "+"".join(f"  x={x:.2f}" for x in xs)+"     mean")
for i,L in enumerate(Ls):
    for j,p in enumerate(ps):
        if p>=1.0: continue
        r=C[(L,p)]/C[(L,1.00)]
        print(f"   {L:3d}  {p:.2f}   "+" ".join(f"{v:7.4f}" for v in r)+f"   {r.mean():7.4f}")
print("\n=== after removing the 1/s artifact (fit over L at fixed x) ===")
print("     p     "+"".join(f"  x={x:.2f}" for x in xs)+"     mean")
for j,p in enumerate(ps):
    if p>=1.0: continue
    out=[]
    for k,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in Ls])
        rv=np.array([C[(L,p)][k]/C[(L,1.00)][k] for L in Ls])
        out.append(np.polyfit(1.0/sv,rv,1)[1])
    out=np.array(out)
    print(f"   {p:.2f}   "+" ".join(f"{v:7.4f}" for v in out)+f"   {out.mean():7.4f}")
print("\nD_heat(s) actually used (flat => a single D exists; rising => it runs):")
for i,L in enumerate(Ls):
    for j,p in enumerate(ps):
        sp=DD[i,j].max()/DD[i,j].min()
        print(f"   L={L:3d} p={p:.2f}  "+" ".join(f"{v:6.4f}" for v in DD[i,j])+f"   spread {sp:.3f}x")
