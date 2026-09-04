"""
T279 - the collapse test, with the corrected D AND the occupancy factor q.

Derived BEFORE seeing the diluted numbers:

Weyl's law for B = M^{-1/2} A M^{-1/2} counts the low modes by the GEOMETRIC box
volume L^3 -- they are box-spanning plane waves, so N(lambda) = L^3 (lambda/D)^{3/2}/6pi^2
independent of how many sites were deleted.  (Check: at p=1 this reproduces
L^3 [e^{-2s}I0(2s)]^3 ~ L^3 (4 pi s)^{-3/2}.)  But V2 sums the mass over OCCUPIED
sites only, so V2 = q * (int sqrt g)_2 with q = n/L^3.  Hence

    Rtil(x) = (1/q) D^{-3/2} R_cont(D x)

Two tests, one absolute and one that needs no normalisation at all:
  ABSOLUTE:  q * D^{3/2} * Rtil_inf(x) / R_cont(D x) == 1
  SHAPE   :  Rtil_inf(x)/Rtil_inf(x0) == R_cont(D x)/R_cont(D x0)
             -- q and D^{3/2} cancel identically; only D inside the argument
             survives, so this tests the CURVATURE term alone.
Omitting q would make p=0.85 read 1/0.849 = 1.18 and p=0.70 read 1/0.699 = 1.43,
i.e. manufacture a failure of the curvature term out of the volume term.
"""
import numpy as np
from opus_t275 import R_cont, giant
d=np.load("t277_raw.npz"); xs=d["xs"]; Ls=d["Ls"]; ps=d["ps"]; RT=d["RT"]
Dm=np.load("t278_D.npy")
q=np.array([[giant(int(L),float(p),11).sum()/L**3 for p in ps] for L in Ls])
print("occupancy q = n/L^3 (giant component):")
for i,L in enumerate(Ls): print(f"   L={L:3d}  "+"  ".join(f"p={p:.2f}: {q[i,j]:.4f}" for j,p in enumerate(ps)))
print("\nD (LOBPCG):")
for i,L in enumerate(Ls): print(f"   L={L:3d}  "+"  ".join(f"p={p:.2f}: {Dm[i,j]:.5f}" for j,p in enumerate(ps)))
print("\nraw Rtil(x):")
for i,L in enumerate(Ls):
    for j,p in enumerate(ps):
        print(f"   L={L:3d} p={p:.2f}  "+" ".join(f"{v:8.4f}" for v in RT[i,j]))

inf={}
for j,p in enumerate(ps):
    row=[]
    for i,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in Ls])
        B,A=np.polyfit(1.0/sv,RT[:,j,i],1); row.append((A,B))
    inf[j]=row
print("\n=== ABSOLUTE:  q * D^1.5 * Rtil_inf(x) / R_cont(D x)    (1.000 = survives) ===")
print("    p     q      D      "+"".join(f"  x={x:.2f}" for x in xs)+"    B(mean)")
for j,p in enumerate(ps):
    D=Dm[-1,j]; Q=q[-1,j]
    c=[Q*D**1.5*inf[j][i][0]/R_cont(D*xs[i]) for i in range(len(xs))]
    print(f"  {p:.2f} {Q:6.4f} {D:7.4f}   "+" ".join(f"{v:7.4f}" for v in c)
          +f"   {np.mean([inf[j][i][1] for i in range(len(xs))]):7.3f}")
print("\n=== SHAPE (q and D^1.5 cancel; tests the curvature term alone) ===")
print("    p      D      "+"".join(f"  x={x:.2f}" for x in xs))
for j,p in enumerate(ps):
    D=Dm[-1,j]
    r=[inf[j][i][0]/inf[j][0][0] for i in range(len(xs))]
    t=[R_cont(D*xs[i])/R_cont(D*xs[0]) for i in range(len(xs))]
    print(f"  {p:.2f} {D:7.4f}   "+" ".join(f"{a/b:7.4f}" for a,b in zip(r,t)))
