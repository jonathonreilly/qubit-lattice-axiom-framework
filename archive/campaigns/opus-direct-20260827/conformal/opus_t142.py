"""T142 - WHAT QUANTIZING THE GEOMETRY ACTUALLY COSTS.

Owner question: what happens to every lane if the geometry is QUANTIZED rather
than continuous?  The sharpest casualty is the variational principle -- the Regge
field equation, the exact linearisation, the graviton and the bridge are all
statements about DERIVATIVES with respect to squared edge lengths.  Quantize
l^2 to a grid of spacing q and there are no derivatives.

Rather than argue this, measure it.  Two concrete questions:

(1) IS FLAT SPACE STILL A SOLUTION?  Flat space is an exact stationary point of
    S = sum_h A_h delta_h in the continuum (first variation vanishes identically).
    Under quantization the nearest allowed configurations sit a distance q away,
    so the question becomes whether S still has no first-order response along the
    allowed moves.  Measure S at the discrete neighbours.

(2) HOW MUCH GEOMETRY IS LOST?  A gravitational wave of strain eps enters as
    l^2 -> l^2 (1 + eps ...).  If eps < q the wave rounds away entirely -- there
    is a MINIMUM REPRESENTABLE STRAIN, which is a physical prediction rather than
    a technicality.  Measure the recovered d^2S against the continuous answer as
    a function of eps/q, i.e. how many quanta a wave needs before the framework's
    graviton result comes back.

Units: q is the quantum of l^2 in units of a^2, so q = 1 means l^2 is an integer
number of a^2 -- the strongest form of 'integer in Planck cubes'."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t114b import build, S_of

L=4
verts,vid,tops,edges,emid,edir,base_len=build(L)
S0=S_of(tops,edges,base_len)
h=1.0/L
l2_0=np.array([base_len[e]**2 for e in range(len(base_len))])
print(f"T142  quantizing the geometry.  L={L}, {len(edges)} edges, S(flat) = {S0:.2e}")
print(f"      squared edge lengths at flat: {sorted(set(np.round(l2_0/h**2,9)))} in units of a^2")
print(f"      (axis edges 1, face diagonals 2, ... -- already integers on the flat lattice)")
print()
print("(1) is flat space still a solution?  S at the discrete neighbours, q = quantum of l^2/a^2")
rng=np.random.default_rng(4)
for q in (1.0,0.25,0.05):
    vals=[]
    for trial in range(6):
        step=rng.choice([-1.0,1.0],size=len(l2_0))*q*h*h
        l2=l2_0+step
        if np.any(l2<=0): continue
        s=S_of(tops,edges,np.sqrt(l2))
        vals.append(s if s is not None else np.nan)
    vals=np.array([v for v in vals if v is not None and np.isfinite(v)])
    if len(vals)==0: print(f"      q={q:<6}  all neighbours degenerate (simplices fail to close)"); continue
    print(f"      q={q:<6}  S at 1-quantum neighbours: mean {vals.mean():+.4e}  "
          f"range [{vals.min():+.3e}, {vals.max():+.3e}]  -> {'BOTH SIGNS' if vals.min()<0<vals.max() else 'one sign'}")
print("      (S=0 at flat; both signs means flat is a saddle, as it already is in the")
print("       continuum -- the Regge action is not bounded below.  Not a new problem.)")
print()
print("(2) minimum representable strain: recovered d^2S vs the continuous answer")
kv=2*np.pi*1*np.array([0.0,1.0,0.0,0.0]); k2=float(kv@kv)
ep=np.zeros((4,4)); ep[2,2]=1.0; ep[3,3]=-1.0          # diagonal TT, the clean channel
def d2S(eps,q=None):
    def l2_of(s):
        out=l2_0.copy()
        for key,e in edges.items():
            u=edir[key]
            out[e]=float(u@u)+s*np.cos(float(kv@emid[key]))*float(u@ep@u)
        if q is not None:
            out=np.round(out/(q*h*h))*(q*h*h)           # snap to the allowed grid
        return out
    a=l2_of(eps); b=l2_of(-eps)
    if np.any(a<=0) or np.any(b<=0): return None
    Sp=S_of(tops,edges,np.sqrt(a)); Sm=S_of(tops,edges,np.sqrt(b))
    if Sp is None or Sm is None: return None
    return (Sp-2*S0+Sm)/eps**2
cont=d2S(1e-3)
print(f"      continuous d^2S/(k^2 V) = {cont/k2:.6f}   (the R74 diagonal-TT channel)")
print(f"      {'q (l^2 quantum)':>16} {'strain eps':>12} {'eps/q':>9} {'quantized d^2S/(k^2 V)':>24} {'vs continuous':>14}")
for q in (1.0,0.1,0.01):
    for eps in (0.5*q,2.0*q,10.0*q,100.0*q):
        if eps>0.5: continue
        v=d2S(eps,q=q)
        if v is None: print(f"      {q:16g} {eps:12.4g} {eps/q:9.1f} {'degenerate':>24}"); continue
        print(f"      {q:16g} {eps:12.4g} {eps/q:9.1f} {v/k2:24.6f} {v/cont:14.4f}")
print()
print("   eps/q >> 1 needed to recover the continuum value = a wave must carry many")
print("   quanta of l^2 before the framework's graviton result survives quantization.")
