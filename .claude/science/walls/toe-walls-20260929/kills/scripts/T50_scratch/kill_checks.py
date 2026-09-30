"""T50 kill checks (Claude Sonnet 5.5, same family as attacker). Repo untouched.
Uses the attacker's chain() and geo() by import-by-copy so numbers are comparable.
K1 g-window of the midpoint form vs chain form; K2 repo-documented g values; K3 chain-vs-geo decomposition;
K4 gate power on C and eps/B; K5 T51 joint window keeps M_1; K6 alternative target values; K7 mu window of geo form."""
import math, sys
import numpy as np

PI = math.pi
ALPHA_BARE = 1/(4*PI); PLAQ = 0.5934
M_PL = 1.2209e19; C0 = (7/8)**0.25; G = 0.653; OBS = 2.453e-3; V_MEAS = 246.22; GEV2EV = 1e9
A0 = ALPHA_BARE/PLAQ**0.25
MZ = 91.1876

def chain(alpha=A0, g=G, y=None, kB=8, kA=7, r='half', C=C0, v=None, Mpl=M_PL):
    if y is None: y = g*g/64
    if v is None: v = Mpl*C*alpha**16
    rr = alpha/2 if r == 'half' else r
    M1 = Mpl*alpha**kB*(1-rr); MA = Mpl*alpha**kA
    m3 = y*y*v*v/M1*GEV2EV; m1 = y*y*v*v/MA*GEV2EV
    return m3*m3-m1*m1
def geo(g=G, v=V_MEAS, Mpl=M_PL, y=None):
    if y is None: y = g*g/64
    M1 = math.sqrt(Mpl*v)
    m3 = y*y*v*v/M1*GEV2EV
    return m3*m3
dev = lambda x, ref=OBS: x/ref-1

print("K1 g-window (|dev|<5% of 2.453e-3) as a range of g:")
for nm, f in (("chain", lambda g: chain(g=g)), ("midpoint(geo)", lambda g: geo(g=g))):
    gs = np.linspace(0.60, 0.70, 200001); ok = [g for g in gs if abs(dev(f(g))) < 0.05]
    print(f"  {nm:14s} g in [{min(ok):.4f}, {max(ok):.4f}]  (nominal 0.653: {dev(f(0.653)):+.2%})")

print("\nK2 documented / conventional g values (repo: G_WEAK_FROM_FRAMEWORK_NOTE_2026-05-03 bounded g_2(v)=0.6480; PDG g_2(M_Z)=0.6517; 0.653 runner):")
for g in (0.6480, 0.6475, 0.6517, 0.653):
    print(f"  g={g:.4f}  chain {dev(chain(g=g)):+.2%}   midpoint {dev(geo(g=g)):+.2%}")

print("\nK7 mu window of the midpoint form (one-loop SM g2 from 0.653 at M_Z, b2=-19/6):")
def g2_at(mu, g0=G, mu0=MZ): return 1/math.sqrt(1/g0**2 + (19/3)/(16*PI**2)*math.log(mu/mu0))
mus = np.exp(np.linspace(math.log(10), math.log(1e4), 6000))
for nm, f in (("chain", chain), ("midpoint", geo)):
    ok = [m for m in mus if abs(dev(f(g=g2_at(m)))) < 0.05]
    print(f"  {nm:9s} 5% window in mu: {min(ok):.0f} .. {max(ok):.0f} GeV ; at v=246: {dev(f(g=g2_at(246.22))):+.2%}")

print("\nK3 chain vs midpoint decomposition (Dm2 ratios)")
c = chain(); g_ = geo()
print(f"  chain/midpoint = {c/g_:.4f}  (difference {c/g_-1:+.2%}, the 'extra' content of the chain)")
print(f"  drop C only: x{chain(C=1.0)/c:.4f};  drop eps/B only: x{chain(r=0.0)/c:.4f};  drop both: x{chain(C=1.0,r=0.0)/c:.4f}")
print(f"  vs target: chain {dev(c):+.2%}; drop C {dev(chain(C=1.0)):+.2%}; drop eps {dev(chain(r=0.0)):+.2%}; drop both {dev(chain(C=1.0,r=0.0)):+.2%}")
print("  => every removal of C and/or eps/B exits the 5% gate in the chain form; the gate does test them individually.")

print("\nK4 gate power: which C exponents and eps/B values stay inside 5% (chain form)?")
ex = [p for p in np.linspace(-0.2, 0.8, 10001) if abs(dev(chain(C=(7/8)**p))) < 0.05]
print(f"  C=(7/8)^p in gate for p in [{min(ex):.3f}, {max(ex):.3f}] (nominal 0.25)")
rs = [r for r in np.linspace(0, 0.2, 20001) if abs(dev(chain(r=r))) < 0.05]
print(f"  eps/B in gate for [{min(rs):.4f}, {max(rs):.4f}] (nominal alpha/2={A0/2:.4f}; 0.041 old fit inside)")

print("\nK5 T51 joint window: lightest RH eigenvalue M_1 = x(1-r)*B (units of M_Pl*alpha^8)")
xs = (2.89831413339407, 3.049019002821463); rr = (0.667459439859965, 0.6872623905976495)
# corners of the T51 joint region are not a rectangle; sample the boundary numbers T51 gives via S5:
for nm, x, r in (("T51 S5 feasible pt", 2.970, 0.6780), ("retained", 1.0, 0.0453339)):
    print(f"  {nm:20s} x(1-r) = {x*(1-r):.4f}   (T50 chain: 1-alpha/2 = {1-A0/2:.4f}; log-midpoint factor sqrt(C) = {math.sqrt(C0):.4f})")
print(f"  T51 rectangle extremes of x(1-r): {xs[0]*(1-rr[1]):.3f} .. {xs[1]*(1-rr[0]):.3f}")
# T50's Dm2_31 if M_1 is held at T51's feasible value (m3 from lightest RH eigenvalue, singlet m1 negligible)
def dm31_from_M1(fac):
    y = G*G/64; v = M_PL*C0*A0**16; M1 = M_PL*A0**8*fac
    m3 = y*y*v*v/M1*GEV2EV; m1 = y*y*v*v/(M_PL*A0**7)*GEV2EV; return m3*m3-m1*m1
for fac in (0.9547, 0.9563, 1.0):
    print(f"  T50 chain with M_1 = {fac:.4f} M_Pl alpha^8: Dm2_31 = {dm31_from_M1(fac):.4e} ({dev(dm31_from_M1(fac)):+.2%})")

print("\nK6 alternative target value (recalled current-fit 2.511e-3; not a repo number)")
for t in (2.453e-3, 2.511e-3):
    print(f"  target {t:.3e}: chain {dev(chain(),t):+.2%}  midpoint {dev(geo(),t):+.2%}  midpoint at g=0.6517 {dev(geo(g=0.6517),t):+.2%}")
