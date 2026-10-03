"""
A36 check C6: a clock made of the possibilities and tuned by the records around it (no memory, no shared
clock), and why it gives random, not set, formation times.

Supplied toy in the record-tick shape: Heisenberg change H = J * SWAP on every bond, compressed onto records
(each recorded neighbour with content r adds the field J|r><r| to an unrecorded site, A27 Step 1a).
Two unrecorded neighbours x and z; x has k_x recorded neighbours, z has k_z, all with content r (the calm,
aligned case). One excitation (a spin opposite to r) is shared between x and z, starting at z.
Formation weight at x (gated, A32 D24 form): F = gamma |-r><-r|_x, in continuous time (a rate).
In the one-excitation subspace {flip at z, flip at x}: H = [[J k_x, J], [J, J k_z]] (a flip at x
leaves the field energy J k_z on z, and vice versa), so the excitation
rings between x and z at Omega = J sqrt((k_x - k_z)^2 + 4): a pitch set by the records.
Checked: (a) Omega from the spectrum vs the formula; (b) the density of the formation time at x has
peaks spaced 2 pi / Omega (phase-locked to the ringing); (c) the formation time is random: its spread
across one ringing period stays order 1 for every gamma (no rule linear in the possibilities makes it set).
"""
import signal
import numpy as np
signal.alarm(55)
J = 1.0

def density(kx, kz, gamma, T=40.0, n=40001):
    H = np.array([[J * kx, J], [J, J * kz]], complex)       # basis: (flip at z, flip at x)
    Heff = H - 0.5j * gamma * np.diag([0.0, 1.0])
    lam, V = np.linalg.eig(Heff)
    Vi = np.linalg.inv(V)
    psi0 = np.array([1.0, 0.0], complex)
    a = Vi @ psi0
    t = np.linspace(0, T, n)
    psi = (V[:, None, :] * (a[None, :] * np.exp(-1j * np.outer(t, lam)))[None]).sum(axis=2)  # 2 x n
    p_x = np.abs(psi[1]) ** 2
    return t, gamma * p_x, np.sum(np.abs(psi) ** 2, axis=0)

print("C6. Ringing pitch at x set by the records: Omega = J sqrt((k_x-k_z)^2 + 4)")
for kx, kz in ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1)):
    E = np.linalg.eigvalsh(np.array([[J * kx, J], [J, J * kz]]))
    Om = E[1] - E[0]
    t, f, norm = density(kx, kz, gamma=0.05)
    # peak spacing of the formation-time density (local maxima)
    m = (f[1:-1] > f[:-2]) & (f[1:-1] > f[2:])
    pk = t[1:-1][m]
    sp = np.mean(np.diff(pk[:6]))
    print(f"  k_x={kx}, k_z={kz}: Omega spectrum {Om:.6f}, formula {J*np.sqrt((kx-kz)**2+4):.6f};"
          f" peak spacing of formation density {sp:.5f} vs 2pi/Omega {2*np.pi/Om:.5f};"
          f" swing at x {4/((kx-kz)**2+4):.3f}")

print("\nC6b. Is the formation time set? Probability of forming within the first ringing period, and the")
print("     spread (std) of the formation time in units of the period, k_x = k_z = 1:")
for gamma in (0.05, 0.5, 2.0, 8.0, 50.0):
    t, f, norm = density(1, 1, gamma, T=200.0, n=200001)
    per = 2 * np.pi / 2.0
    dt = t[1] - t[0]
    P = np.sum(f) * dt
    mean = np.sum(t * f) * dt / P
    std = np.sqrt(np.sum((t - mean) ** 2 * f) * dt / P)
    first = np.sum(f[t <= per]) * dt
    print(f"  gamma={gamma:<6} P(formed by T)={P:.4f}  P(in first period)={first:.4f}  std/period={std/per:.3f}")

print("\nC6c. Scan of gamma (k_x = k_z = 1): the smallest spread of the formation time, in ringing periods")
best = (9, None)
for gamma in np.geomspace(0.3, 30, 41):
    t, f, norm = density(1, 1, gamma, T=120.0, n=120001)
    per = np.pi
    dt = t[1] - t[0]
    P = np.sum(f) * dt
    mean = np.sum(t * f) * dt / P
    std = np.sqrt(np.sum((t - mean) ** 2 * f) * dt / P)
    if std / per < best[0]:
        best = (std / per, gamma, mean / per)
print(f"  smallest std/period = {best[0]:.3f} at gamma = {best[1]:.3f} J (mean formation time {best[2]:.3f} periods)")
