"""
T217 - does the consistent record measure DETERMINE a dynamics?

R112: the axioms "do not supply the formation site, probability, or rate" and
declare dynamics absent.  R136: the consistent record measure is
    mu(c) ∝ prod_{edges} phi(v_x . v_y),  phi = 1 + lam (v.v').
Any positive measure mu has a canonical positive Hamiltonian: take any Markov
generator L reversible w.r.t. mu and set

    H = - D^{1/2} L D^{-1/2},     D = diag(mu)

Then H is symmetric, H >= 0, and H sqrt(mu) = 0 -- sqrt(mu) is the ground state
at energy zero.  If this holds, the record measure fixes the GROUND STATE while
the jump rates fix the SPECTRUM.  That would make R112's "declared absent"
precise: what is missing is exactly the rates, not a whole dynamics.

Tested with TWO different reversible rate choices (Metropolis and heat-bath).
If the ground state is the same and the gap differs, the split is real.

(A) also checks reflection positivity: the edge kernel K(v,v') = 1 + lam v.v'
on S^2 must be positive semidefinite for the transfer operator to be positive.
Funk-Hecke predicts eigenvalues 4pi (l=0, x1) and 4pi lam/3 (l=1, x3), rest 0.
"""
import numpy as np, itertools
from numpy.polynomial.legendre import leggauss

# ---------------------------------------------------------------- (A) kernel
print("=== (A) spectrum of the edge kernel on S^2 (reflection positivity) ===")
NT, NP = 40, 80
ct, wt = leggauss(NT); ph = 2*np.pi*np.arange(NP)/NP
V = np.array([[np.sqrt(1-c*c)*np.cos(p), np.sqrt(1-c*c)*np.sin(p), c]
              for c in ct for p in ph])
W = np.array([w*(2*np.pi/NP) for w in wt for _ in ph])
for lam in (1.0, 0.5, -0.5):
    K = (1 + lam*(V@V.T))*np.sqrt(np.outer(W, W))
    ev = np.sort(np.linalg.eigvalsh(K))[::-1]
    print(f"  lam={lam:+4.1f}: top eigenvalues {ev[:5].round(6)}   "
          f"min {ev[-1]:+.2e}   PSD? {'YES' if ev[-1] > -1e-9 else 'NO'}")
    print(f"          Funk-Hecke predicts 4pi={4*np.pi:.6f} (x1), "
          f"4pi*lam/3={4*np.pi*lam/3:.6f} (x3), rest 0")

# ------------------------------------------------------- (B) the Hamiltonian
MENU = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], float)
M = 6; DOT = MENU @ MENU.T

def build(nsite, edges, lam):
    cfg = list(itertools.product(range(M), repeat=nsite))
    mu = np.array([np.prod([1+lam*DOT[c[a], c[b]] for a, b in edges]) for c in cfg])
    mu = mu/mu.sum()
    return cfg, mu

def hamiltonian(cfg, mu, nsite, rates):
    # restrict to the SUPPORT of mu: at lam=1 antiparallel neighbours are
    # forbidden (phi = 0), so those configurations carry zero probability and
    # are not part of the state space.
    keep = [i for i in range(len(cfg)) if mu[i] > 0]
    cfg = [cfg[i] for i in keep]; mu = mu[keep]; mu = mu/mu.sum()
    idx = {c: i for i, c in enumerate(cfg)}
    n = len(cfg)
    L = np.zeros((n, n))
    for i, c in enumerate(cfg):
        for s in range(nsite):
            for w in range(M):
                if w == c[s]: continue
                cc = list(c); cc[s] = w
                j = idx.get(tuple(cc))
                if j is None: continue               # outside the support
                L[j, i] += rates(mu[i], mu[j])       # rate c -> cc
    np.fill_diagonal(L, 0.0)
    L[np.diag_indices(n)] = -L.sum(axis=0)
    # reversibility gives S = D^-1 L D symmetric, with D = diag(sqrt(mu)),
    # and S sqrt(mu) = 0.  (D L D^-1 is the WRONG order and is not symmetric.)
    D = np.sqrt(mu)
    H = -(L/D[:, None])*D[None, :]
    return 0.5*(H+H.T), H, mu

metropolis = lambda mi, mj: min(1.0, mj/mi)
heatbath   = lambda mi, mj: mj/(mi+mj)

print("\n=== (B) H = -D^1/2 L D^-1/2 for the consistent record measure ===")
for label, nsite, edges in (("3-site path", 3, [(0,1),(1,2)]),
                            ("4-site ring", 4, [(0,1),(1,2),(2,3),(3,0)])):
    for lam in (0.5, 1.0):
        cfg, mu = build(nsite, edges, lam)
        print(f"\n  {label}, lam={lam}   ({len(cfg)} configs, "
              f"{int(np.sum(mu>0))} in the support of mu)")
        gs = {}
        for rname, r in (("Metropolis", metropolis), ("heat-bath ", heatbath)):
            Hs, Hraw, mus = hamiltonian(cfg, mu, nsite, r)
            asym = np.max(np.abs(Hraw - Hraw.T))
            ev, U = np.linalg.eigh(Hs)
            g = U[:, 0]
            if g.sum() < 0: g = -g
            sq = np.sqrt(mus); sq = sq/np.linalg.norm(sq)
            resid = np.max(np.abs(Hs @ sq))
            ov = abs(g @ sq)
            gs[rname] = g
            print(f"    {rname}: symmetry err {asym:.1e}   min eig {ev[0]:+.2e}   "
                  f"H sqrt(mu) = {resid:.2e}   |<gs|sqrt(mu)>| = {ov:.12f}   "
                  f"gap = {ev[1]:.6f}")
        d = np.max(np.abs(gs["Metropolis"] - gs["heat-bath "]))
        print(f"    ground states from the two rate choices differ by {d:.2e}"
              f"   -> {'SAME ground state' if d < 1e-8 else 'DIFFERENT'}")
