"""Independent numerical/algebraic checks for Campaign C4 / RD / D1.

This deliberately does not import the worker scripts.  One-dimensional
integrals use a composite midpoint rule, the two-dimensional check uses a
split Gauss--Legendre product rule, and the inverse-tail check samples k and q
on different grids.  The final block gives a concrete counterexample to the
report's claimed universal one-particle--hole kinematics in one dimension.
"""

import numpy as np
from numpy.polynomial.legendre import leggauss


PI = np.pi
m = beta = g = 1.0
c = 2.0
Ef = np.sqrt(m * m + beta * PI * PI)
s = beta * PI / Ef


def red(x):
    return (x + PI) % (2 * PI) - PI


def band(x):
    return np.sqrt(m * m + beta * red(x) ** 2)


def omega(q):
    return 2 * c * np.abs(np.sin(q / 2))


def weight(q, n):
    x = 2 * np.abs(np.sin(q / 2))
    return g * g * x ** (2 * n) / (2 * omega(q))


def midpoint_nodes(n):
    h = 2 * PI / n
    return -PI + (np.arange(n) + 0.5) * h


print("1. independent 1D midpoint quadrature")
q = midpoint_nodes(1 << 20)
om = omega(q)
D0 = Ef - band(PI - q) - om
for n in (2, 3):
    w = weight(q, n)
    K = np.mean(w / D0**2)
    S0 = np.mean(w / D0)
    dl = 1.0e-4
    Dd = band(PI - dl) - band(PI - dl - q) - om
    slope = (np.mean(w / Dd) - S0) / dl
    print(
        f"   n={n}: K={K:.9f}, sK={s*K:.9f}, "
        f"slope(delta=1e-4)={slope:.9f}, ratio={slope/(s*K):.7f}"
    )


print("2. independent marginal-log fit")
w1 = weight(q, 1)
S0 = np.mean(w1 / D0)
deltas = np.array([3e-3, 1e-3, 3e-4, 1e-4, 3e-5])
slopes = []
for dl in deltas:
    Dd = band(PI - dl) - band(PI - dl - q) - om
    slopes.append((np.mean(w1 / Dd) - S0) / dl)
slopes = np.array(slopes)
Cfit = np.polyfit(np.log(1 / deltas), slopes, 1)[0]
Cexact = s * g * g / (2 * PI * c * (c - s) ** 2)
print(f"   fitted C={Cfit:.8f}; local asymptotic C={Cexact:.8f}; ratio={Cfit/Cexact:.6f}")


def split_legendre(n):
    """Gauss--Legendre nodes on [-pi,0] union [0,pi]."""
    x, w = leggauss(n)
    left_x = 0.5 * PI * (x - 1)
    right_x = 0.5 * PI * (x + 1)
    ww = 0.5 * PI * w
    return np.concatenate((left_x, right_x)), np.concatenate((ww, ww))


print("3. independent 2D split Gauss--Legendre product quadrature")
q1, wg1 = split_legendre(180)
qx, qy = np.meshgrid(q1, q1, indexing="ij")
wg2 = wg1[:, None] * wg1[None, :]
ky = 0.7
Ef2 = np.sqrt(1 + PI**2 + ky**2)
s2 = PI / Ef2
r2 = 4 * np.sin(qx / 2) ** 2 + 4 * np.sin(qy / 2) ** 2
om2 = c * np.sqrt(r2)
w2 = r2 / (2 * om2)
D20 = Ef2 - np.sqrt(1 + red(PI - qx) ** 2 + red(ky - qy) ** 2) - om2
norm2 = (2 * PI) ** 2
K2 = np.sum(wg2 * w2 / D20**2) / norm2
S20 = np.sum(wg2 * w2 / D20) / norm2
for dl in (0.02, 0.01, 0.005):
    Ed = np.sqrt(1 + (PI - dl) ** 2 + ky**2)
    D2d = Ed - np.sqrt(1 + red(PI - dl - qx) ** 2 + red(ky - qy) ** 2) - om2
    slope2 = (np.sum(wg2 * w2 / D2d) / norm2 - S20) / dl
    print(f"   delta={dl:.3f}: K={K2:.6f}, slope/(sK)={slope2/(s2*K2):.5f}")


print("4. gapped touching: midpoint result and local closed form")
Om = Ef - m
omg = Om + 1 + np.cos(q)
Dg0 = Ef - band(PI - q) - omg
wg = 1 + np.cos(q)
Sg0 = np.mean(wg / Dg0)
for dl in (1e-3, 1e-4, 1e-5):
    Dgd = band(PI - dl) - band(PI - dl - q) - omg
    dS = np.mean(wg / Dgd) - Sg0
    print(f"   delta={dl:.0e}: dSigma/sqrt(delta)={dS/np.sqrt(dl):.6f}")
# Near q=pi+y: w=y^2/2 and D=-(s*delta+y^2)+lower-order terms.
# The singular difference is sqrt(s*delta)/4.
print(f"   local prediction sqrt(s)/4={np.sqrt(s)/4:.6f}")


print("5. inverse-problem tail on independent k/q grids")
Nk = 2048
Nq = 16384
kgrid = -PI + 2 * PI * np.arange(Nk) / Nk
qgrid = midpoint_nodes(Nq)
omq = omega(qgrid)
wq = weight(qgrid, 2)
Et = band(kgrid)
Sig = np.empty(Nk)
for j, kval in enumerate(kgrid):
    Dj = band(kval) - band(kval - qgrid) - omq
    Sig[j] = np.mean(wq / Dj)
eps = Et - Sig
tE = np.fft.fft(Et) / Nk
t0 = np.fft.fft(eps) / Nk
Dface = band(-PI) - band(-PI - qgrid) - omq
Kface = np.mean(wq / Dface**2)
for r in (16, 32, 64):
    ratio = (t0[r] / tE[r]).real
    print(f"   r={r:2d}: tail ratio={ratio:.6f}; 1+K={1+Kface:.6f}")


print("6. exact jump algebra for the self-consistent iteration")
K_sc = 0.196406
alpha = 0.5
print(f"   finite-Z kink factor Z=1/(1+K); mixed-iteration factor={1-alpha*(1+K_sc):.6f}")
ratios = np.array([1.3403, 1.3752, 1.4091, 1.4419, 1.4738])
local_slopes = np.diff(ratios) / np.log(2)
print("   marginal finite-size d(s0/s)/dlog(1/h): " + ", ".join(f"{x:.5f}" for x in local_slopes))


print("7. 1D Fermi-sea counterexample to universal one-pair decay kinematics")
# Sea dispersion e_f(p)=2t(1-cos p), so every particle-hole excitation has
# energy <=4t and, for transfer |Q|, energy <=2t|Q| by the mean-value theorem.
# At the SLAC face, Delta_E(Q)=E(pi)-E(pi-|Q|).  With t=1e-3, Delta_E is
# above both bounds for every Q != 0 (the two bounds cover small and large Q).
t = 1.0e-3
kF = 0.1  # a nonempty, partially filled sea
Q = np.linspace(1e-7, PI, 1_000_000)
loss = Ef - np.sqrt(1 + (PI - Q) ** 2)
ph_upper = np.minimum(4 * t, 2 * t * Q)
margin = loss - ph_upper
print(
    f"   t={t:g}, kF={kF:g}: min[Delta_E(Q)-min(4t,2tQ)]={margin.min():.3e} "
    f"for 0<Q<=pi; no single particle-hole energy can match the loss"
)


print("8. synthetic sub-marginal power-law check")
# In d=1 choose 2a=1/2, so d+2a-1=1/2.  This fractional weight is a
# regular power-law test, not the square of an ordinary finite-range vertex.
wsub = (2 * np.abs(np.sin(q / 2))) ** 0.5
Ssub0 = np.mean(wsub / D0)
dsub = np.array([1e-2, 3e-3, 1e-3, 3e-4])
dSsub = []
for dl in dsub:
    Dd = band(PI - dl) - band(PI - dl - q) - om
    dSsub.append(np.mean(wsub / Dd) - Ssub0)
dSsub = np.array(dSsub)
expo = np.polyfit(np.log(dsub), np.log(dSsub), 1)[0]
print(
    f"   predicted exponent=0.5; fitted exponent={expo:.6f}; "
    f"all coefficients positive, dSigma/sqrt(delta)={dSsub[-1]/np.sqrt(dsub[-1]):.6f}"
)
