"""T50 test: which bridges carry the atmospheric-gap hit, hidden-input sensitivity, look-elsewhere bounds.
Repo untouched. Numbers copied from scripts/frontier_dm_neutrino_atmospheric_scale_theorem.py (main 7146fe17a7).
Pre-registration: PREREG.md (same folder), written before this ran."""
import math, itertools
import numpy as np

PI = math.pi
ALPHA_BARE = 1/(4*PI)
PLAQ = 0.5934
M_PL = 1.2209e19            # unreduced, as in the runner
C0 = (7/8)**0.25
G = 0.653
OBS = 2.453e-3              # runner's Dm2_31 target
V_MEAS = 246.22
GEV2EV = 1e9

def alpha_of(P):
    return ALPHA_BARE / P**0.25

A0 = alpha_of(PLAQ)

def chain(alpha=A0, g=G, y=None, kB=8, kA=7, r='half', C=C0, v=None, Mpl=M_PL, vexp=16):
    """Dm2_31 (eV^2) and pieces. r: eps/B ('half' -> alpha/2) or number."""
    if y is None: y = g*g/64
    if v is None: v = Mpl*C*alpha**vexp
    rr = alpha/2 if r == 'half' else r
    M1 = Mpl*alpha**kB*(1-rr)
    MA = Mpl*alpha**kA
    m3 = y*y*v*v/M1*GEV2EV
    m1 = y*y*v*v/MA*GEV2EV
    m2 = y*y*v*v/(Mpl*alpha**kB*(1+rr))*GEV2EV
    return dict(dm31=m3*m3-m1*m1, dm21=m2*m2-m1*m1, m1=m1, m2=m2, m3=m3, v=v, M1=M1, y=y)

def dev(x, ref=OBS): return x/ref-1

def geo(y=None, g=G, v=V_MEAS, Mpl=M_PL, k=8):
    """Geometric-midpoint form: M_1 = Mpl^(1-k/16) v^(k/16); k=8 -> sqrt(Mpl v). No alpha_LM. m_1 neglected."""
    if y is None: y = g*g/64
    M1 = Mpl**(1-k/16)*v**(k/16)
    m3 = y*y*v*v/M1*GEV2EV
    return m3*m3

print("=== A. reproduce and leave-one-out ===")
b = chain()
print(f"alpha_LM={A0:.6f}  step 1/alpha={1/A0:.4f}  v={b['v']:.3f} GeV  M1={b['M1']:.4e} GeV  y={b['y']:.6e}")
print(f"m3={b['m3']:.5e} eV m2={b['m2']:.5e} m1={b['m1']:.5e}  Dm2_31={b['dm31']:.4e} ({dev(b['dm31']):+.2%})  Dm2_21={b['dm21']:.3e}")
print(f"m1^2/m3^2 = {b['m1']**2/b['m3']**2:.4%}")
loo = {
 'k_A=6 (heavier singlet)':dict(kA=6),
 'k_A=5':dict(kA=5),
 'k_A=-50 (m1->0)':dict(kA=-50),   # run 1 had k_A=8,9,100 rows, illegal (they break M_A > M_B); removed
 'eps/B=0 (drop P-c)':dict(r=0.0),
 'eps/B=0.041 (old benchmark)':dict(r=0.041),
 'C=1 (drop (7/8)^(1/4))':dict(C=1.0),
 'C=(7/8)^(1/2)':dict(C=(7/8)**0.5),
 'v=measured 246.22 (formula for M1 kept)':dict(v=V_MEAS),
 'drop both eps and C':dict(r=0.0, C=1.0),
}
for k, kw in loo.items():
    d = chain(**kw)['dm31']
    print(f"  {k:42s} Dm2_31={d:.4e}  {dev(d):+.2%}")
print("A4 geometric-mean form (measured v, no alpha_LM, m1 neglected):")
for g in (0.653, 0.6517, 0.6531):
    d = geo(g=g); print(f"  g={g}: Dm2={d:.4e} ({dev(d):+.2%})   m3={math.sqrt(d):.5f} eV")
print(f"  chain M1/sqrt(Mpl*v_formula) = {b['M1']/math.sqrt(M_PL*b['v']):.5f};  sqrt(C)/(1-a/2) = {math.sqrt(C0)/(1-A0/2):.5f}")
ybest = math.sqrt(math.sqrt(OBS)/GEV2EV*math.sqrt(M_PL*V_MEAS)/V_MEAS**2)
print(f"  y needed (geo form, target {OBS}) = {ybest:.5e};  g^2/64 = {G*G/64:.5e} ({G*G/64/ybest-1:+.2%})")

print("\n=== elasticities d ln Dm2 / d ln x (chain form, finite difference) ===")
def el(f, x0, h=1e-4):
    return (math.log(f(x0*(1+h)))-math.log(f(x0*(1-h))))/(math.log(1+h)-math.log(1-h))
print(f"  alpha_LM: {el(lambda a: chain(alpha=a)['dm31'], A0):.2f}   g: {el(lambda g: chain(g=g)['dm31'], G):.2f}"
      f"   M_Pl: {el(lambda m: chain(Mpl=m)['dm31'], M_PL):.2f}")
print(f"  geo form: v: {el(lambda v: geo(v=v), V_MEAS):.2f}  g: {el(lambda g: geo(g=g), G):.2f}  M_Pl: {el(lambda m: geo(Mpl=m), M_PL):.2f}")
for nm, f, x0 in (('alpha_LM', lambda a: chain(alpha=a)['dm31'], A0), ('g', lambda g: chain(g=g)['dm31'], G)):
    lo = None
    # find +-5% band edges around obs (relative to target) by scanning
    xs = np.linspace(x0*0.9, x0*1.1, 20001)
    ok = [x for x in xs if abs(dev(f(x))) < 0.05]
    print(f"  {nm}: window for |dev|<5%  {min(ok)/x0-1:+.3%} .. {max(ok)/x0-1:+.3%} of nominal")

print("\n=== B1. scale at which g is read (one-loop SM g2, b2=-19/6) ===")
MZ = 91.1876
def g2_at(mu, g0=G, mu0=MZ):
    return 1/math.sqrt(1/g0**2 + (19/3)/(16*PI**2)*math.log(mu/mu0))
for name, mu in (('m_Z', MZ), ('v', 246.22), ('1 TeV', 1e3), ('1e6 GeV', 1e6), ('M_1', b['M1']), ('M_Pl', M_PL)):
    g = g2_at(mu); d = chain(g=g)['dm31']
    print(f"  mu={name:8s} g2={g:.4f}  Dm2_31={d:.3e} ({dev(d):+.1%}) {'IN' if abs(dev(d))<0.05 else 'out'}")
mus = np.exp(np.linspace(math.log(10), math.log(1e4), 4000))
ok = [m for m in mus if abs(dev(chain(g=g2_at(m))['dm31'])) < 0.05]
print(f"  5% window in mu: {min(ok):.0f} .. {max(ok):.0f} GeV  (width {math.log(max(ok)/min(ok)):.2f} e-folds of ~{math.log(M_PL/MZ):.1f} to M_Pl)")
print(f"  g_bare=1 at the lattice scale (y=1/64): Dm2 = {chain(g=1.0)['dm31']:.3e} ({dev(chain(g=1.0)['dm31']):+.0%}) = x{chain(g=1.0)['dm31']/OBS:.1f}")

print("\n=== B2. quenched -> dynamical-taste plaquette (T31 attacker's dP, taken as input) ===")
for dP in (0.0, 0.021, 0.037, 0.065):
    a = alpha_of(PLAQ+dP)
    c = chain(alpha=a)   # formula chain: v, M1 both from alpha
    gm = geo()           # geometric form, measured v: no alpha_LM
    print(f"  dP={dP:+.3f} alpha={a:.5f} ({a/A0-1:+.2%}) v_formula={c['v']:.1f} GeV  chain Dm2={c['dm31']:.3e} ({dev(c['dm31']):+.1%})  geo-form Dm2={gm:.3e} ({dev(gm):+.1%})")
    # chain with measured v but M1 from alpha
    c2 = chain(alpha=a, v=V_MEAS); print(f"          M_1 from alpha_LM, v measured: Dm2={c2['dm31']:.3e} ({dev(c2['dm31']):+.1%})")

print("\n=== B3. Planck mass convention ===")
Mred = M_PL/math.sqrt(8*PI)
for name, m in (('unreduced 1.2209e19', M_PL), ('reduced 2.435e18', Mred)):
    d = chain(Mpl=m)['dm31']; e = geo(Mpl=m)
    print(f"  {name:22s} chain Dm2={d:.3e} ({dev(d):+.0%})   geo-form Dm2={e:.3e} ({dev(e):+.0%})")

print("\n=== C1. documented-alternatives grammar (81 members) ===")
def coverage(preds, w=0.0488, lo=OBS/10, hi=OBS*10):
    """fraction of ln-target axis in [lo,hi] within +-w (ln) of some prediction (5% -> ln1.05=0.0488)."""
    iv = sorted((math.log(p)-w, math.log(p)+w) for p in preds if p > 0)
    L0, L1 = math.log(lo), math.log(hi)
    tot, cur_s, cur_e = 0.0, None, None
    for s, e in iv:
        s, e = max(s, L0), min(e, L1)
        if e <= s: continue
        if cur_e is None or s > cur_e:
            if cur_e is not None: tot += cur_e-cur_s
            cur_s, cur_e = s, e
        else: cur_e = max(cur_e, e)
    if cur_e is not None: tot += cur_e-cur_s
    return tot/(L1-L0)
G1 = []
for kB, r, ydiv, cp in itertools.product((7, 8, 9), (0.0, 0.041, 'half'), (64, 32, 128), (0.25, 0.0, 0.5)):
    d = chain(kB=kB, kA=kB-1, r=r, y=G*G/ydiv, C=(7/8)**cp)['dm31']
    G1.append((kB, r, ydiv, cp, d))
preds = [x[-1] for x in G1]
h5 = [x for x in G1 if abs(dev(x[-1])) < 0.05]; h35 = [x for x in G1 if abs(dev(x[-1])) < 0.035]
print(f"  members={len(G1)}  hits<5%: {len(h5)}  hits<3.5%: {len(h35)}  coverage(5%, target in [obs/10, obs*10]) = {coverage(preds):.1%}")
for x in h5: print("    hit:", x[:4], f"Dm2={x[4]:.3e} ({dev(x[4]):+.1%})")
print(f"  members with prediction within a factor 10 of obs: {sum(1 for p in preds if OBS/10<p<OBS*10)}")

print("\n=== C2. y-grammar in geometric-midpoint form ===")
Y = {}
for a_, b_, c_, d_ in itertools.product((1, 2), range(0, 9), (0, 1), (0, 1)):
    y = G**a_/(2**b_*3**c_*math.sqrt(2)**d_)
    Y[(a_, b_, c_, d_)] = y
print(f"  distinct y-forms: {len(Y)}  (range {min(Y.values()):.2e} .. {max(Y.values()):.2e})")
preds2 = []; hits5 = []; hits35 = []
for k in range(1, 16):
    for key, y in Y.items():
        d = geo(y=y, k=k); preds2.append(d)
        if abs(dev(d)) < 0.05: hits5.append((k, key, d))
        if abs(dev(d)) < 0.035: hits35.append((k, key, d))
print(f"  (k,y) pairs={len(preds2)}  hits<5%: {len(hits5)}  hits<3.5%: {len(hits35)}  coverage = {coverage(preds2):.1%}")
for h in hits5[:12]: print("    hit: k=%d (a,b,c,d)=%s Dm2=%.3e (%+.1f%%)" % (h[0], h[1], h[2], 100*dev(h[2])))
# stricter y-grammar: only the two-parameter form g^a/2^b
Y2 = [(a_, b_) for a_ in (1, 2) for b_ in range(0, 9)]
pr3 = [geo(y=G**a_/2**b_, k=k) for k in range(1, 16) for a_, b_ in Y2]
h3 = [(k, ab) for k in range(1, 16) for ab in Y2 if abs(dev(geo(y=G**ab[0]/2**ab[1], k=k))) < 0.05]
print(f"  stricter grammar g^a/2^b only: pairs={len(pr3)} hits<5%: {len(h3)} {h3}  coverage = {coverage(pr3):.1%}")
# single-formula local p-value at achieved offsets
step = 1/A0; lnstep = math.log(step)
for tol_m in (0.0175, 0.025):   # +-1.75% and +-2.5% in mass (=3.5% / 5% in Dm2)
    print(f"  single-member local p at +-{tol_m:.2%} in mass on the ladder step 1/alpha={step:.2f}: {2*math.log(1+tol_m)/lnstep:.2%}")
