"""T34 - Richardson of the PER-EDGE (Regge-equation-level) B at matched s k^2."""
import numpy as np, sys, re
def load(fn):
    d={}
    for ln in open(fn):
        p=ln.split()
        if len(p)==9 and p[0] in ('TT','conf','V0a','tran'):
            d[(p[0],float(p[1]))]=(float(p[3]),float(p[4]),float(p[5]),float(p[6]),float(p[8]))
    return d
a=load(sys.argv[1] if len(sys.argv)>1 else "out_t32_L32.txt")
b=load(sys.argv[2] if len(sys.argv)>2 else "t32_L64.log")
k2=(2*np.pi/32)**2
print("T34  per-edge B/B_pred: Richardson (4 b64 - b32)/3 at matched s k^2")
print(f"{'pol':>5} {'s32':>5} {'s64':>5} {'s k^2':>7} {'B32':>8} {'B64':>8} {'B_cont':>8} "
      f"{'A32':>7} {'A64':>7} {'|corr12|':>8} {'res/Bx2 (64)':>12}")
rows={}
for (t,s) in sorted(a):
    if (t,4*s) not in b: continue
    A32,B32,pr32,c12,rb32=a[(t,s)]; A64,B64,pr64,c1264,rb64=b[(t,4*s)]
    Bc=(4*B64-B32)/3
    rows.setdefault(t,[]).append((s*k2,Bc))
    print(f"{t:>5} {s:5.1f} {4*s:5.1f} {s*k2:7.3f} {B32:8.4f} {B64:8.4f} {Bc:8.4f} "
          f"{A32:7.4f} {A64:7.4f} {c1264:8.4f} {rb64:12.3e}")
print()
for t,v in rows.items():
    v=np.array(v)
    for i0 in (0,1,2):
        if len(v)-i0<2: continue
        M=np.stack([np.ones(len(v)-i0),v[i0:,0]],1); c,*_=np.linalg.lstsq(M,v[i0:,1],rcond=None)
        print(f"  {t:>5}: linear in s k^2 over [{v[i0,0]:.3f},{v[-1,0]:.3f}] -> B* = {c[0]:8.4f}")
