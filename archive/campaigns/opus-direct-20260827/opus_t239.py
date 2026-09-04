"""
T239 - closing R157's gap: is the framework's matter MINIMALLY COUPLED to its
own Berry connection?

R157 showed the regulator induces the Maxwell term for an IMPOSED background
gauge field, coefficient -1/12 to 6.5e-5.  R154/R155 showed the record field
carries its OWN composite U(1) (the phase of <psi_x|psi_y>).  Those are only the
same statement if the matter couples MINIMALLY to that composite connection.

Claim to test: the Born-point edge weight is the covariant derivative squared.
      1 - |<psi|psi'>|^2  =  |D psi|^2 + O(delta^4)
with  D psi = delta psi - i A psi ,  A = Im(psi^dag delta psi)  (the Berry
connection).  If so the record measure IS the lattice CP^{n-1} action with
minimal coupling, and R157's induced Maxwell applies to the framework's own U(1).
"""
import numpy as np
rng = np.random.default_rng(83)

def pair(n, eps):
    z = rng.normal(size=n)+1j*rng.normal(size=n); z /= np.linalg.norm(z)
    w = z + eps*(rng.normal(size=n)+1j*rng.normal(size=n))
    w /= np.linalg.norm(w)
    return z, w

print("=== 1. is the edge weight the covariant derivative squared? ===")
print("   n   eps      1-|<z|w>|^2      |D z|^2        ratio        |naive |dz|^2 ratio")
for n in (2, 4):
    for eps in (0.2, 0.1, 0.05, 0.02):
        L, R, N = [], [], []
        for _ in range(4000):
            z, w = pair(n, eps)
            d = w - z
            A = np.imag(np.vdot(z, d))
            D = d - 1j*A*z
            L.append(1 - abs(np.vdot(z, w))**2)
            R.append(np.vdot(D, D).real)
            N.append(np.vdot(d, d).real)
        L, R, N = np.mean(L), np.mean(R), np.mean(N)
        print(f"   {n}  {eps:5.2f}   {L:12.8f}  {R:12.8f}   {R/L:9.6f}   {N/L:9.6f}")
print("   ratio -> 1 as eps -> 0 for |D z|^2, and NOT for the naive |dz|^2")
print("   => the Born-point weight is the GAUGE-COVARIANT derivative, not the plain one.")

print("\n=== 2. done with the COVARIANT lattice difference ===")
print("   my first D used the raw difference w - z, which is NOT covariant under")
print("   INDEPENDENT endpoint phases.  The lattice covariant difference must")
print("   parallel-transport with the link phase theta = arg<z|w>:")
print("        D psi = e^{-i theta} w - z    ->   |D psi|^2 = 2(1 - |<z|w>|)")
worst_w, worst_d, worst_id = 0.0, 0.0, 0.0
def Dcov(z, w):
    th = np.angle(np.vdot(z, w))
    d = np.exp(-1j*th)*w - z
    return np.vdot(d, d).real
for _ in range(4000):
    z, w = pair(4, 0.05)
    a, b = rng.uniform(0, 2*np.pi, 2)
    z2, w2 = z*np.exp(1j*a), w*np.exp(1j*b)
    worst_w = max(worst_w, abs(abs(np.vdot(z,w))**2 - abs(np.vdot(z2,w2))**2))
    worst_d = max(worst_d, abs(Dcov(z,w) - Dcov(z2,w2)))
    worst_id = max(worst_id, abs(Dcov(z,w) - 2*(1-abs(np.vdot(z,w)))))
print(f"   |<z|w>|^2  under independent phases : max change {worst_w:.2e}")
print(f"   |D psi|^2  under independent phases : max change {worst_d:.2e}   <- now invariant")
print(f"   identity |D psi|^2 = 2(1-|<z|w>|)   : max error  {worst_id:.2e}")
print()
print("   and the two agree as the states approach:")
print("     n  eps    1-|<z|w>|^2     |D psi|^2      ratio")
for n in (2,4):
    for eps in (0.2, 0.1, 0.05, 0.02):
        L, R = [], []
        for _ in range(4000):
            z, w = pair(n, eps)
            L.append(1-abs(np.vdot(z,w))**2); R.append(Dcov(z,w))
        L, R = np.mean(L), np.mean(R)
        print(f"     {n}  {eps:4.2f}  {L:12.8f}  {R:12.8f}  {R/L:9.6f}")

print("""
=== reading ===
  The record measure at the Born point is, edge by edge,
        -log phi = -log(1 - |D psi|^2 + ...) = |D psi|^2 + ...
  i.e. the lattice CP^{n-1} action with MINIMAL COUPLING to the Berry
  connection A = Im(psi^dag d psi) -- the same A whose curvature R154/R155
  measured and quantised.
  So R157's induced Maxwell term is induced for the framework's OWN U(1),
  not merely for an arbitrary imposed background.""")
