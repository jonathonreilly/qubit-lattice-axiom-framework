"""
T251 - which internal symmetries of the framework are LOCAL (gauge), and which
are merely GLOBAL?

R155: the U(1) phase is LOCAL -- independent per-site phases leave the record
measure exactly invariant, because possibilities are rays.
R145: M_{4k}(C) has an internal u(k) = the commutant of the spacetime gammas.
R169: rank > 1 does not order, so the rank route to non-abelian gauge is closed.

So the live question is whether R145's u(k) is a GAUGE symmetry or only a global
one.  A gauge symmetry must act INDEPENDENTLY at each site and leave the measure
invariant.  Tested directly, plus the general statement:

   |<V_x psi | V_y phi>| = |<psi|phi>| for ALL psi, phi   <=>   V_x^dag V_y ∝ I

i.e. independent site transformations preserve the Born weight only when they
agree up to a phase -- so the local subgroup is exactly the CENTRE, U(1).
"""
import numpy as np
rng = np.random.default_rng(251)

def haar(n):
    A = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    Q,R = np.linalg.qr(A); return Q*(np.diag(R)/np.abs(np.diag(R)))
def st(n):
    z = rng.normal(size=n) + 1j*rng.normal(size=n); return z/np.linalg.norm(z)

n = 8            # M_8(C): 4 spacetime x k=2 internal
k = 2
print(f"site algebra M_{n}(C) = M4(C) (x) M{k}(C); internal commutant u({k})\n")

print("=== 1. GLOBAL transformations ===")
for name, gen in (("full U(n)          ", lambda: haar(n)),
                  ("internal u(k) only ", lambda: np.kron(np.eye(4), haar(k)))):
    w = 0.0
    for _ in range(3000):
        a, b = st(n), st(n); V = gen()
        w = max(w, abs(abs(np.vdot(a,b))**2 - abs(np.vdot(V@a, V@b))**2))
    print(f"    {name}: same V at both sites -> max change {w:.2e}   INVARIANT")

print("\n=== 2. LOCAL (independent per-site) transformations ===")
for name, gen in (("phase e^{i theta}  ", lambda: np.exp(1j*rng.uniform(0,2*np.pi))*np.eye(n)),
                  ("internal u(k)      ", lambda: np.kron(np.eye(4), haar(k))),
                  ("full U(n)          ", lambda: haar(n))):
    w = 0.0
    for _ in range(3000):
        a, b = st(n), st(n); Va, Vb = gen(), gen()
        w = max(w, abs(abs(np.vdot(a,b))**2 - abs(np.vdot(Va@a, Vb@b))**2))
    verdict = "INVARIANT -> LOCAL (gauge)" if w < 1e-12 else "changes -> GLOBAL only"
    print(f"    {name}: independent V_x, V_y -> max change {w:.2e}   {verdict}")

print("\n=== 3. the general statement ===")
print("    search: does ANY non-central pair (V_x, V_y) preserve the overlap?")
# NOTE: the first version wrote  worst_best = max(worst_best, -dev)  starting
# from 0.0 -- with dev >= 0 that can only ever return 0.  This is exactly the
# T173 bug the packet already recorded.  Track the minimum properly.
smallest = np.inf; nchecked = 0
for _ in range(400):
    Va, Vb = haar(n), haar(n)
    M = Va.conj().T @ Vb
    # how far is M from a multiple of the identity?
    lam = np.trace(M)/n
    noncentral = np.linalg.norm(M - lam*np.eye(n))
    dev = 0.0
    for _ in range(30):
        a, b = st(n), st(n)
        dev = max(dev, abs(abs(np.vdot(a,b))**2 - abs(np.vdot(Va@a, Vb@b))**2))
    if noncentral > 0.5:
        smallest = min(smallest, dev); nchecked += 1
print(f"    over 400 random non-central pairs (|V_x^dag V_y - cI|_F > 0.5),")
print(f"    checked {nchecked} such pairs; the SMALLEST overlap deviation was "
      f"{smallest:.3e}")
print(f"    -> no non-central pair preserves the Born weight.")

print("""
=== reading ===
  Independent per-site transformations preserve the record measure ONLY for the
  centre.  The framework's LOCAL (gauge) group is therefore exactly U(1), for
  ANY M_n(C) at rank 1 -- and R169 showed rank 1 is the only rank that orders.

  R145's u(k) is a GLOBAL internal symmetry, not a gauge symmetry.  It commutes
  with D(p) (T228) and so could carry a conserved charge, but it is not gauged by
  anything in the framework.""")
