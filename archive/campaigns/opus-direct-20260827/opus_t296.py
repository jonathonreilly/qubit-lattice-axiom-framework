"""
T296 - dilution verdict on the h=0.05 / nz=32 dataset, FOUR lattice sizes.

t288 completed after all (L=40,56,72) and t290 supplied L=48, so the h=0.05 set
spans L = 40,48,56,72.  Its L=48 control matches the EXACT Bloch answer (T294)
to 0.2%, which is the reason to trust this set over the h=0.10 rerun.

Control that decides whether the extrapolation may be reported at all:
  A(p=1) must be 1.000 and B(p=1) must be ~+1.0 (R188's independently measured
  artifact coefficient).  T291 failed exactly this -- B went NEGATIVE -- and its
  numbers were withheld.  Same gate here.
"""
import numpy as np, os
_xc=np.array([0.0,0.05,0.10,0.20,0.35,0.50]); _rc=np.array([1.0,1.01150,1.02374,1.05038,1.09533,1.14569])
_cf=np.polyfit(_xc,_rc-1.0,3); R_cont=lambda x: 1.0+np.polyval(_cf,x)
xs=np.array([0.10,0.16,0.24,0.34,0.46]); ps=[1.00,0.85,0.70]
EX={48:np.array([1.2132,1.1516,1.1349,1.1435,1.1698])}     # exact Bloch, T294
d={}
for L in (40,48,56,72):
    for p in ps:
        for pre in ("t290_","t288_"):
            fn=f"{pre}{L}_{int(p*100)}.npy"
            if os.path.exists(fn) and (L,p) not in d: d[(L,p)]=np.load(fn)
Ls=sorted({L for (L,p) in d})
print(f"lattice sizes: {Ls}\n")
C={}
for (L,p),v in d.items():
    Rtil,D,q,s=v; C[(L,p)]=q*D**1.5*Rtil/R_cont(D*xs)
print("=== raw Rtil, p=1 control vs EXACT (the reason to trust this set) ===")
for L in Ls:
    if L in EX:
        r=d[(L,1.00)][0]
        print(f"   L={L}: "+" ".join(f"{v:7.4f}" for v in r)+"   dev vs exact "
              +" ".join(f"{v:+6.2%}" for v in r/EX[L]-1))
print("\n=== absolute collapse C ===")
print("     L    p     "+"".join(f"  x={x:.2f}" for x in xs))
for L in Ls:
    for p in ps:
        if (L,p) in C: print(f"   {L:3d}  {p:.2f}   "+" ".join(f"{v:7.4f}" for v in C[(L,p)])
                             +("   <-- control" if p>=1.0 else ""))
print("\n=== fit C = A + B/s over the four L at fixed x ===")
A={};B={}
for p in ps:
    Lok=[L for L in Ls if (L,p) in C]
    aa=[];bb=[]
    for k,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in Lok]); cv=np.array([C[(L,p)][k] for L in Lok])
        b,a=np.polyfit(1.0/sv,cv,1); aa.append(a); bb.append(b)
    A[p]=np.array(aa); B[p]=np.array(bb)
    gate="   <-- GATE: A must be 1.000, B ~ +1.0" if p>=1.0 else ""
    print(f"  p={p:.2f}  A = "+" ".join(f"{v:7.4f}" for v in A[p])+f"  mean {A[p].mean():7.4f}{gate}")
    print(f"          B = "+" ".join(f"{v:7.3f}" for v in B[p])+f"  mean {B[p].mean():7.3f}")
ok = abs(A[1.00].mean()-1)<0.03 and B[1.00].mean()>0.5
print(f"\n  control gate: {'PASSED' if ok else 'FAILED -- extrapolated numbers withheld'}")
if ok:
    print("\n=== extrapolated collapse, control-normalised: A(p)/A(1.00) ===")
    for p in ps:
        if p>=1.0: continue
        r=A[p]/A[1.00]
        print(f"  p={p:.2f}   "+" ".join(f"{v:7.4f}" for v in r)+f"   mean {r.mean():7.4f}")
