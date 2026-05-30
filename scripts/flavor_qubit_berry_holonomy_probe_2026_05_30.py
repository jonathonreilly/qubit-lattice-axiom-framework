#!/usr/bin/env python3
"""Qubit-factor Berry holonomy of the loop delta:0->2pi of the mass-embedded circulant
H(a,|b|e^{i delta}) on R^3(x)C^2 -- the off-index probe named by the equivariant-eta
complementarity. Gauge-invariant Wilson-loop discretization. HONEST NEGATIVE.

  B1 (pure phase loop, no gap): Berry phase = -pi for ALL |b| -- pins to a topological
     half-winding (the 'w pin'), r-blind. Does NOT give 2/9 and does not select r.
  B2 (native gap a*sigma_z, the physical embedding r=|b|^2/a^2): Berry phase is continuous
     and r-selective, |gamma|=pi(1-1/sqrt(1+r)); at r=1/2 it is 0.5765 rad -- NOT 2/9 in any
     normalization (2/9 rad -> r=0.158; (2/9)*2pi -> r=2.24). r=1/2 is not pinned.
  B3 value-coincidence: cos^2(theta)=1/(1+r) equals Q=1/3+2r/3 ONLY at r=1/2 (both 2/3);
     they are different functions of r -> a crossing, NOT a derivation of r=1/2.
"""
import numpy as np

sx = np.array([[0,1],[1,0]], complex)
sy = np.array([[0,-1j],[1j,0]], complex)
sz = np.array([[1,0],[0,-1]], complex)

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def berry(Hfun, n=4000, band='lower'):
    vecs = []
    for d in np.linspace(0, 2*np.pi, n, endpoint=False):
        w, V = np.linalg.eigh(Hfun(d))
        vecs.append(V[:, 0 if band == 'lower' else len(w)-1])
    prod = 1.0 + 0j
    for i in range(n):
        prod *= np.vdot(vecs[i], vecs[(i+1) % n])
    return -np.angle(prod)

def main():
    passed = []; two9 = 2/9

    # B1: no gap -> -pi for all |b| (winding pin)
    vals = [berry(lambda d, bm=bm: bm*(np.cos(d)*sx + np.sin(d)*sy)) for bm in (0.3, 0.7071, 1.0, 2.0)]
    b1 = all(abs(abs(v) - np.pi) < 1e-6 for v in vals)
    passed.append(check("B1 pure phase loop pins to -pi for all |b| (topological 'w pin', r-blind)",
                        b1, f"Berry={[round(v,4) for v in vals]} (all = -pi)"))

    # B2: gapped loop r-selective; r=1/2 -> 0.5765 rad != 2/9
    a = 1.0; bmag = np.sqrt(0.5)
    g = berry(lambda d: a*sz + bmag*(np.cos(d)*sx + np.sin(d)*sy))
    g_an = -np.pi*(1 - 1/np.sqrt(1.5))
    not_2_9 = abs(abs(g) - two9) > 0.1 and abs(abs(g) - two9*np.pi) > 0.1 and abs(abs(g) - two9*2*np.pi) > 0.1
    passed.append(check("B2 gapped loop r-selective; r=1/2 -> 0.5765 rad, NOT 2/9 in any normalization",
                        abs(abs(g) - abs(g_an)) < 1e-4 and not_2_9,
                        f"|Berry(r=1/2)|={abs(g):.6f}; 2/9={two9:.4f}, (2/9)pi={two9*np.pi:.4f}, (2/9)2pi={two9*2*np.pi:.4f}"))
    # which r gives 2/9 rad: r=0.158, not 1/2
    r_for_2_9 = 1/(1 - two9/np.pi)**2 - 1
    passed.append(check("B2b 2/9 rad picks r=0.158 (not 1/2); r=1/2 not pinned by 2/9",
                        abs(r_for_2_9 - 0.158) < 0.005, f"r(|Berry|=2/9 rad)={r_for_2_9:.4f}"))

    # B3: cos^2 theta = Q only at r=1/2 (value crossing, not derivation)
    cross = []
    for r in (0.25, 0.5, 0.75):
        Q = 1/3 + 2*r/3; c2 = 1/(1+r)
        cross.append((abs(Q - c2) < 1e-9) == (abs(r - 0.5) < 1e-9))
    passed.append(check("B3 cos^2theta=1/(1+r) equals Q=1/3+2r/3 ONLY at r=1/2 (crossing, not derivation)",
                        all(cross), "different functions of r; agree only at the point we want to derive"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: the qubit-factor Berry holonomy does NOT derive 2/9 or pin r=1/2. Pure phase")
    print("loop -> topological winding pin (r-blind); gapped loop -> continuous r-selective phase")
    print("that misses 2/9 and does not single out r=1/2. The off-index Berry route converges,")
    print("once more, on the irreducible r=1/2 / generation-chiral pin -- which it does not supply.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
