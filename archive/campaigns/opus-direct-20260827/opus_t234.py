"""
T234 - the half of the overlap the rule throws away.

The admissibility rule at the Born point is
      phi(x,y) = |<psi_x|psi_y>|^2
i.e. the MODULUS SQUARED of a complex number living on each edge.  The PHASE of
that same number is a U(1) connection on edges, and its holonomy around a
plaquette is a Berry curvature living on 2-CELLS:

      F_{mu nu}(x) = arg[ <psi_x|psi_{x+mu}> <psi_{x+mu}|psi_{x+mu+nu}>
                          <psi_{x+mu+nu}|psi_{x+nu}> <psi_{x+nu}|psi_x> ]

(the standard gauge-invariant lattice plaquette phase; independent of each
site's arbitrary phase, which is what makes it meaningful on CP^n).

Why it matters: R40 derived a U(1) field strength on plaquettes and R42 observed
that gravitational curvature lives on hinges (degree d-2), the two coinciding
ONLY at d = 4.  If the record field's own discarded phase IS that plaquette
curvature, R42's coincidence becomes a statement about the framework's own two
curvatures rather than two separately-derived ones.

Checked here: (1) the phase is gauge invariant, (2) the curvature is non-zero,
(3) it sums to a quantised Chern number over a closed 2-surface.
"""
import numpy as np, time

def evolve(L, nwarm, seed=31, t=1.0):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(L,)*4+(4,)) + 1j*rng.normal(size=(L,)*4+(4,))
    psi /= np.linalg.norm(psi, axis=-1, keepdims=True)
    idx = np.indices((L,)*4); A = (idx.sum(axis=0) % 2 == 0); B = ~A
    def half(mask, cone):
        nb = []
        for ax in range(4):
            nb.append(np.roll(psi,1,ax)); nb.append(np.roll(psi,-1,ax))
        prop = psi + cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
        prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
        wo = np.ones(psi.shape[:4]); wn = np.ones(psi.shape[:4])
        for n in nb:
            wo *= (1-t) + t*np.abs(np.sum(np.conj(psi)*n,axis=-1))**2
            wn *= (1-t) + t*np.abs(np.sum(np.conj(prop)*n,axis=-1))**2
        acc = (rng.random(psi.shape[:4]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
        psi[acc] = prop[acc]
        return acc[mask].mean()
    cone = 1.0
    for s in range(nwarm):
        a = 0.5*(half(A,cone)+half(B,cone))
        if s % 100 == 99:
            cone *= 1.15 if a > 0.55 else (0.87 if a < 0.35 else 1.0)
            cone = min(max(cone,0.02),4.0)
    return psi

def link(p, q):
    """<p|q> as an array over sites"""
    return np.sum(np.conj(p)*q, axis=-1)

def plaquette(psi, mu, nu):
    a = link(psi, np.roll(psi, -1, mu))
    b = link(np.roll(psi, -1, mu), np.roll(np.roll(psi, -1, mu), -1, nu))
    c = link(np.roll(np.roll(psi, -1, mu), -1, nu), np.roll(psi, -1, nu))
    d = link(np.roll(psi, -1, nu), psi)
    return np.angle(a*b*c*d)

L = 8
t0 = time.time()
psi = evolve(L, 4000)
print(f"Z^4 with M4(C) states at the Born point, L={L}  [{time.time()-t0:.0f}s]\n")

print("=== 1. is the plaquette phase gauge invariant? ===")
F = plaquette(psi, 0, 1)
rng = np.random.default_rng(5)
ph = np.exp(1j*rng.uniform(0, 2*np.pi, psi.shape[:4]))
psi2 = psi*ph[..., None]                     # arbitrary per-site phase
F2 = plaquette(psi2, 0, 1)
print(f"   max |F(psi) - F(psi x random per-site phase)| = "
      f"{np.max(np.abs(np.angle(np.exp(1j*(F-F2))))):.2e}")

print("\n=== 2. is the curvature non-zero? ===")
for (mu, nu) in ((0,1),(0,3),(1,2),(2,3)):
    Fm = plaquette(psi, mu, nu)
    print(f"   plane ({mu},{nu}): mean |F| = {np.mean(np.abs(Fm)):.4f} rad, "
          f"rms = {np.sqrt(np.mean(Fm**2)):.4f}, mean F = {np.mean(Fm):+.2e}")

print("\n=== 3. is the total flux through a closed 2-surface quantised? ===")
print("   sum of F over a full (mu,nu) torus slice, in units of 2 pi:")
for (mu, nu) in ((0,1),(0,3),(1,2),(2,3)):
    Fm = plaquette(psi, mu, nu)
    # the CLOSED 2-surface is the (mu,nu) torus at fixed transverse position,
    # so sum over (mu,nu) -- not over the complement, which is not closed.
    tot = Fm.sum(axis=(mu, nu)) / (2*np.pi)   # one number per transverse site pair
    print(f"   plane ({mu},{nu}): min {tot.min():+.4f}  max {tot.max():+.4f}  "
          f"max |dist to integer| = {np.max(np.abs(tot-np.round(tot))):.2e}")
