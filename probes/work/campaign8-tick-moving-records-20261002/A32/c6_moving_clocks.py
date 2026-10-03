"""
A32 check C6: what survives of A5's "relativity at low speed" when the possibilities change smoothly (Option R).

Supplied toy: continuous-time lattice Dirac block H(k) = sin(k) sigma_x + m sigma_z (1D) and the 3D naive
4x4 form H = sum_i sin(k_i) alpha_i + m beta. A moving internal clock = two internal states whose rest
energies differ (masses m -/+ delta/2, internal energy entering as mass, as in A5 T2.5). Its rate relative to
rest is R = (d omega/d m)|_k / (d omega/d m)|_{k=0} = m/omega (Feynman-Hellmann: <dH/dm> = d omega/dm).

Claims checked:
 (1) 1D exact: R^2 = 1 - v^2 / cos^2 k   (continuous-time lattice), vs A5's stepped walk R^2 = 1 - v^2/cos^2 m.
 (2) deviation from Lorentz sqrt(1-v^2) is -v^2 tan^2 k: second order in the lattice momentum.
 (3) Feynman-Hellmann: the upper band's <sigma_z> = m/omega = R (a formation weight that scales like the mass
     operator would count proper time; a number-type weight counts lattice time).
 (4) 3D naive Dirac: R^2 - (1 - v^2) = - sum_i sin^4 k_i / omega^2.
"""
import signal
import numpy as np
signal.alarm(55)
sx = np.array([[0, 1], [1, 0]], complex); sz = np.diag([1.0, -1.0]).astype(complex)

def omega1(k, m):
    return np.sqrt(np.sin(k) ** 2 + m ** 2)

print("C6. Moving internal clocks under smooth lattice change (1D two-band block)")
print("  m      k       v          R=m/omega      sqrt(1-v^2/cos^2k)   |diff|      sqrt(1-v^2)    R^2-(1-v^2)    -v^2 tan^2 k   <sigma_z>_upper")
h = 1e-6
maxdiff = 0.0
for m in [0.05, 0.3, 0.8]:
    for k in [0.01, 0.1, 0.4, 1.0]:
        w = omega1(k, m)
        v = (omega1(k + h, m) - omega1(k - h, m)) / (2 * h)
        dwdm = (omega1(k, m + h) - omega1(k, m - h)) / (2 * h)
        R = dwdm / 1.0
        pred = np.sqrt(1 - v ** 2 / np.cos(k) ** 2)
        Hk = np.sin(k) * sx + m * sz
        e, V = np.linalg.eigh(Hk)
        up = V[:, 1]
        sz_up = np.real(up.conj() @ sz @ up)
        maxdiff = max(maxdiff, abs(R - pred), abs(sz_up - m / w))
        print(f"  {m:<6} {k:<7} {v:<10.6f} {R:<14.10f} {pred:<20.10f} {abs(R-pred):<11.2e} {np.sqrt(1-v**2):<14.10f} {R**2-(1-v**2):<14.6e} {-v**2*np.tan(k)**2:<14.6e} {sz_up:.10f}")
print(f"  max |R - sqrt(1 - v^2/cos^2 k)| and |<sigma_z> - m/omega| over the table: {maxdiff:.2e} (finite-difference step 1e-6)")

print("\n  3D naive Dirac (4x4): R^2 - (1 - v^2) vs -sum sin^4 k_i / omega^2")
rng = np.random.default_rng(6)
worst = 0.0
for trial in range(6):
    m = rng.uniform(0.05, 0.6)
    kk = rng.normal(size=3) * 0.2
    def om(kv, mm):
        return np.sqrt(np.sum(np.sin(kv) ** 2) + mm ** 2)
    w = om(kk, m)
    v = np.array([(om(kk + h * e, m) - om(kk - h * e, m)) / (2 * h) for e in np.eye(3)])
    R = (om(kk, m + h) - om(kk, m - h)) / (2 * h)
    lhs = R ** 2 - (1 - v @ v)
    rhs = -np.sum(np.sin(kk) ** 4) / w ** 2
    worst = max(worst, abs(lhs - rhs))
    print(f"    m={m:.3f} |k|={np.linalg.norm(kk):.3f} |v|={np.linalg.norm(v):.4f}: lhs={lhs:.6e} rhs={rhs:.6e}")
print(f"  worst |lhs - rhs| = {worst:.2e}")

print("\n  Physical size of the lattice deviation v^2 tan^2 k ~ v^2 (p a / hbar)^2 at a = Planck length (EXACT arithmetic):")
GeV_per_EP = 1 / 1.2209e19
for name, pGeV, vv in [("muon g-2 ring, p = 3.09 GeV", 3.09, 0.9994), ("Li+ ions at 0.34c (Ives-Stilwell type)", 2.35, 0.34),
                       ("1 PeV cosmic-ray proton", 1e6, 1.0)]:
    ka = pGeV * GeV_per_EP
    print(f"    {name:<40} k a = {ka:.2e}   v^2 tan^2(ka) = {vv**2*np.tan(ka)**2:.2e}")
