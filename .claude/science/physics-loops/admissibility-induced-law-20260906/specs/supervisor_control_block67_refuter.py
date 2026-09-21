#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 67 (floating point; machinery disjoint from the exact runner's: brute-force stationary points of the
full non-linear ledger in all 250 variables of a 7x7x7 box, with no unit-source potential anywhere, as in block 60's control).

W1  the spread amplitude (bare energies from the runner's charges) and the record: brute-force stationary points; the ledger of each, the flux of chi
    and of N through the walls, their first moments.
W2  the record that keeps the BARE ENERGY instead: what happens to the ledger and to both monopoles.
W3  is there a record that keeps BOTH monopoles?  scan the record's bare energy.
W4  formation at each of the five sites: the dipole's jump against Q'(y - Xbar), and its mean over three odds."""
import numpy as np
from scipy.optimize import root

SIDE = 7
NEIGH = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
INT = [(x,y,z) for x in range(1,SIDE-1) for y in range(1,SIDE-1) for z in range(1,SIDE-1)]
IDX = {s:i for i,s in enumerate(INT)}; NI = len(INT); K = 0.75

def full(v, wall):
    a = np.full((SIDE,)*3, wall, dtype=float)
    for s,i in IDX.items(): a[s] = v[i]
    return a

def lap(a, s): return sum(a[s[0]+d[0], s[1]+d[1], s[2]+d[2]] for d in NEIGH) - 6*a[s]

def grad(z, masses):
    u, lam = full(z[:NI], 0.0), full(z[NI:], 0.0); w, chi = np.exp(u), np.exp(lam/2); Nf = w*chi
    g = np.zeros(2*NI)
    for s,i in IDX.items():
        g[i] = w[s]*(masses.get(s,0.0) + 8*K*chi[s]*lap(chi,s)); g[NI+i] = 0.5*chi[s]*8*K*(w[s]*lap(chi,s) + lap(Nf,s))
    return g

def solve(masses, start=None):
    sol = root(lambda z: grad(z, masses), np.zeros(2*NI) if start is None else start, method="hybr", tol=1e-13)
    assert sol.success
    u, lam = full(sol.x[:NI], 0.0), full(sol.x[NI:], 0.0); w, chi = np.exp(u), np.exp(lam/2)
    return w, chi, w*chi, sol.x

def wall_moments(field):
    out = np.zeros(4)
    for x in range(SIDE):
        for y in range(SIDE):
            for z in range(SIDE):
                s = (x,y,z)
                if s in IDX: continue
                for d in NEIGH:
                    t = (x+d[0], y+d[1], z+d[2])
                    if t in IDX: out += (field[t]-1.0)*np.array([1.0, x, y, z])
    return out

if __name__ == "__main__":
    # bare energies of the runner's spread amplitude (charges 1/2, 1/3, 1/5, 1/4, 1/6 at the five sites), from the exact runner's printout: total 9.841
    import fractions
    sites = [(3,3,3),(4,3,3),(3,4,3),(2,3,3),(3,3,2)]; Q = np.array([1/2, 1/3, 1/5, 1/4, 1/6])
    # reconstruct the masses by a linear-algebra potential ONLY to set up the problem; the stationary points below are found without it
    A = np.zeros((NI,NI))
    for s,i in IDX.items():
        A[i,i] = 6
        for d in NEIGH:
            t = (s[0]+d[0], s[1]+d[1], s[2]+d[2])
            if t in IDX: A[i,IDX[t]] = -1
    G = np.linalg.inv(A); idx = [IDX[s] for s in sites]
    chi_at = 1 + G[np.ix_(idx,idx)]@Q; m = 8*K*Q*chi_at; masses = {s: m[i] for i,s in enumerate(sites)}
    print(f"[W1] bare energies {m.round(4)}, total {m.sum():.4f}")
    w, chi, Nf, z0 = solve(masses)
    mom_chi, mom_N = wall_moments(chi), -wall_moments(Nf)
    ledger = sum(masses[s]*w[s] for s in sites) + 8*K*sum(Nf[s]*lap(chi,s) for s in INT) + 8*K*mom_chi[0]*0
    print(f"     spread amplitude, brute force: flux of chi = {mom_chi[0]:.6f} (sum Q = {Q.sum():.6f}); flux of 1 - N = {mom_N[0]:.6f}; first moments of chi's flux {mom_chi[1:].round(5)} against sum Q x = {(Q[:,None]*np.array(sites)).sum(0).round(5)}")
    y = (3,3,3); gyy = G[IDX[y],IDX[y]]; Qt = Q.sum(); m_rec = 8*K*Qt*(1 + Qt*gyy)
    w2, chi2, N2, z2 = solve({y: m_rec})
    mc2, mN2 = wall_moments(chi2), -wall_moments(N2)
    print(f"     record keeping the ledger (bare energy {m_rec:.4f}): flux of chi = {mc2[0]:.6f}; flux of 1 - N = {mN2[0]:.6f}; dipole jump {(mc2[1:]-mom_chi[1:]).round(5)}")
    print(f"     8K x flux of chi: {8*K*mom_chi[0]:.5f} -> {8*K*mc2[0]:.5f} (kept);  clocks' monopole: {mom_N[0]:.5f} -> {mN2[0]:.5f} (jumps by {mN2[0]-mom_N[0]:+.5f})")

    print("\n[W2] the record that keeps the BARE ENERGY:")
    w3, chi3, N3, z3 = solve({y: m.sum()}, start=z2)
    mc3, mN3 = wall_moments(chi3), -wall_moments(N3)
    print(f"     flux of chi {mc3[0]:.5f} (was {mom_chi[0]:.5f}: the ledger falls by {8*K*(mom_chi[0]-mc3[0]):.5f});  clocks' monopole {mN3[0]:.5f} (was {mom_N[0]:.5f})")

    print("\n[W3] scan of the record's bare energy: which value keeps the lengths' monopole, which the clocks'?")
    start = z3; rows = []
    for mr in np.linspace(6.0, 26.0, 11):
        w4, chi4, N4, start = solve({y: mr}, start=start)
        rows.append((mr, wall_moments(chi4)[0], -wall_moments(N4)[0]))
    for mr, a, b in rows: print(f"     bare energy {mr:6.2f}: lengths' monopole {a:.5f} (target {mom_chi[0]:.5f}); clocks' monopole {b:.5f} (target {mom_N[0]:.5f})")
    rows = np.array(rows)
    m_len = np.interp(mom_chi[0], rows[:,1], rows[:,0]); m_clk = np.interp(mom_N[0], rows[:,2], rows[:,0]) if rows[:,2].max() >= mom_N[0] else float("nan")
    print(f"     lengths' monopole kept at bare energy ~{m_len:.3f}; clocks' monopole kept at ~{m_clk:.3f} (the clocks' monopole of ONE body is bounded by 1/(2 g_yy) = {1/(2*gyy):.4f}): two different records")

    print("\n[W4] formation at each of the five sites, ledger kept: the dipole's jump against Q'(y - Xbar); mean over odds:")
    Xbar = (Q[:,None]*np.array(sites)).sum(0)/Qt; jumps = []
    for s in sites:
        gs = G[IDX[s],IDX[s]]; wq, chiq, Nq, _ = solve({s: 8*K*Qt*(1 + Qt*gs)}, start=z2)
        jmp = wall_moments(chiq)[1:] - mom_chi[1:]; jumps.append(jmp)
        print(f"     y = {s}: jump {jmp.round(5)} against {(Qt*(np.array(s)-Xbar)).round(5)}")
    jumps = np.array(jumps); p = m/m.sum()
    for name, odds in (("p/chi (the charges)", Q/Qt), ("p", p), ("p/chi^2", (p/chi_at**2)/np.sum(p/chi_at**2))):
        print(f"     odds proportional to {name}: mean jump {(odds[:,None]*jumps).sum(0).round(6)}")
