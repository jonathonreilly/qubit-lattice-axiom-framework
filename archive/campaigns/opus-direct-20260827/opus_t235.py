"""
T235 - the U(1) of R154 is LOCAL, and the axioms already have it.

R154 found a quantised Berry curvature in the phase the rule discards.  The
sharper statement: the rule
      phi(x,y) = |<psi_x|psi_y>|^2
is invariant under INDEPENDENT phases at every site,
      psi_x -> e^{i theta_x} psi_x ,
because |e^{-i th_x} e^{i th_y} <psi_x|psi_y>|^2 = |<psi_x|psi_y>|^2.
That is a LOCAL gauge symmetry, not a global one -- and the reason is the Qubit
axiom itself: possibilities are STATES (rays / density matrices), so the phase is
not physical.

If the origin is projectivity rather than the enlargement, the same U(1) must
already be there at M2(C), i.e. in the axioms AS WRITTEN, where CP^1 = S^2.
Checked for both.
"""
import numpy as np

rng = np.random.default_rng(41)

def rand_states(shape, n):
    z = rng.normal(size=shape+(n,)) + 1j*rng.normal(size=shape+(n,))
    return z/np.linalg.norm(z, axis=-1, keepdims=True)

def measure(psi, edges_axes):
    """mu = prod over nearest-neighbour edges of |<psi_x|psi_y>|^2"""
    logm = 0.0
    for ax in edges_axes:
        ov = np.abs(np.sum(np.conj(psi)*np.roll(psi, -1, ax), axis=-1))**2
        logm += np.sum(np.log(np.maximum(ov, 1e-300)))
    return logm

print("=== 1. is the MEASURE invariant under independent per-site phases? ===")
for n, name in ((2, "M2(C): CP^1 = S^2   (the axioms as written)"),
                (4, "M4(C): CP^3         (the proposal)")):
    L = 6; d = 3 if n == 2 else 4
    psi = rand_states((L,)*d, n)
    th = rng.uniform(0, 2*np.pi, (L,)*d)
    psi2 = psi*np.exp(1j*th)[..., None]
    a = measure(psi, range(d)); b = measure(psi2, range(d))
    print(f"   {name}")
    print(f"      log mu unchanged to {abs(a-b):.2e}   (independent phase at every site)")

print("\n=== 2. how big is the gauge redundancy? ===")
for n in (2, 4):
    print(f"   M{n}(C): normalised C^{n} has real dimension {2*n-1}; "
          f"CP^{n-1} has {2*(n-1)};  difference = {2*n-1-2*(n-1)} (one U(1))")

print("\n=== 3. Berry curvature for the AXIOMS AS WRITTEN: M2(C) on Z^3 ===")
def plaquette(psi, mu, nu):
    lk = lambda p, q: np.sum(np.conj(p)*q, axis=-1)
    a = lk(psi, np.roll(psi,-1,mu))
    b = lk(np.roll(psi,-1,mu), np.roll(np.roll(psi,-1,mu),-1,nu))
    c = lk(np.roll(np.roll(psi,-1,mu),-1,nu), np.roll(psi,-1,nu))
    e = lk(np.roll(psi,-1,nu), psi)
    return np.angle(a*b*c*e)

L = 8
psi = rand_states((L,)*3, 2)                 # CP^1 states on Z^3
# equilibrate lightly under the Born-point rule so it is not pure noise
for sweep in range(1500):
    for parity in (0, 1):
        i,j,k = np.indices((L,)*3); mask = ((i+j+k) % 2 == parity)
        prop = psi + 0.6*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
        prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
        wo = np.ones(psi.shape[:3]); wn = np.ones(psi.shape[:3])
        for ax in range(3):
            for s in (1,-1):
                nb = np.roll(psi, s, ax)
                wo *= np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                wn *= np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
        acc = (rng.random(psi.shape[:3]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
        psi[acc] = prop[acc]

th = rng.uniform(0, 2*np.pi, (L,)*3)
for (mu,nu) in ((0,1),(1,2),(0,2)):
    F  = plaquette(psi, mu, nu)
    F2 = plaquette(psi*np.exp(1j*th)[...,None], mu, nu)
    gi = np.max(np.abs(np.angle(np.exp(1j*(F-F2)))))
    tot = F.sum(axis=(mu,nu))/(2*np.pi)
    print(f"   plane ({mu},{nu}): gauge-inv {gi:.1e}   mean|F| {np.mean(np.abs(F)):.4f} rad"
          f"   flux/2pi in [{tot.min():+.3f},{tot.max():+.3f}]"
          f"   max|dist to integer| {np.max(np.abs(tot-np.round(tot))):.1e}")

print("""
=== reading ===
  The local U(1) and its quantised curvature do NOT require the enlargement.
  They follow from the Qubit axiom's possibilities being STATES rather than
  vectors, and are already present at M2(C) on Z^3 -- i.e. in the axioms as
  written.""")
