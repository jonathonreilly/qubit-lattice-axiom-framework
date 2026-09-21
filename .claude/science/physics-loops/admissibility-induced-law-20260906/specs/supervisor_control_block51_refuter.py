"""Block 51 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic expansion and integration, numerical quadrature of the
DISCRETE streaming operator, and a Fourier solution on a grid).
W1  the streaming difference of a smooth field expanded symbolically to second order: -s.grad + (1/2) sum_k |s_k| d_k^2 (in units of 1/sqrt 3).
W2  the sphere moments <|s_k|> = 1/2, <s_x^2 |s_x|> = 1/4, <s_x^2 |s_y|> = 1/8 and <s_x s_y |s_z|> = 0 by symbolic integration.
W3  the curl of (d_x^3, d_y^3, d_z^3)(1/r) symbolically; its value 70/2187 along z at (1, 2, 2).
W4  the discrete streaming operator applied to a longitudinal local-equilibrium wave of momentum, integrated over the sphere by quadrature:
    its damping along an axis, a face diagonal and a body diagonal is as 2 : 3/2 : 4/3 (an isotropic viscous operator would give equal values).
W5  the creeping inflow with a viscous term of cubic symmetry, solved by Fourier transform on a 96^3 grid: isotropic for eta = 0; for eta = 1/2 the
    ratio of the inflow along the axes to that along the body diagonals is the same, within a few per cent, in two shells: it does not decay.
Floating point is used in W4 and W5 (controls, not the runner)."""
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import integrate

ROOT = Path(__file__).resolve().parents[5]
results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
x, y, z, h = sp.symbols("x y z h")
s1, s2, s3 = sp.symbols("s1 s2 s3", positive=True)                     # a content in the first octant
f = sp.Function("f")
expr = s1 * (f(x - h, y, z) - f(x, y, z)) + s2 * (f(x, y - h, z) - f(x, y, z)) + s3 * (f(x, y, z - h) - f(x, y, z))
ser = sp.series(expr, h, 0, 3).removeO().doit()
want = -h * (s1 * sp.diff(f(x, y, z), x) + s2 * sp.diff(f(x, y, z), y) + s3 * sp.diff(f(x, y, z), z)) + sp.Rational(1, 2) * h ** 2 * (s1 * sp.diff(f(x, y, z), x, 2) + s2 * sp.diff(f(x, y, z), y, 2) + s3 * sp.diff(f(x, y, z), z, 2))
report("W1", sp.simplify(ser - want) == 0, "symbolic: the streaming difference of a smooth field is -h s.grad f + (h^2/2) sum_k |s_k| d_k^2 f + O(h^3)")

# ------------------------------------------------------------------------------------------------ W2
th, ph = sp.symbols("theta phi", positive=True)
cx, cy, cz = sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)


def octant_mean(e):
    return sp.simplify(8 * sp.integrate(sp.integrate(e * sp.sin(th), (th, 0, sp.pi / 2)), (ph, 0, sp.pi / 2)) / (4 * sp.pi))


m_first, m_same, m_other = octant_mean(cx), octant_mean(cx ** 3), octant_mean(cx ** 2 * cy)
mixed = sp.integrate(sp.integrate(cx * cy * sp.Abs(cz) * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
report("W2", (m_first, m_same, m_other) == (sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 8)) and mixed == 0, f"symbolic: <|s_x|> = {m_first}, <s_x^2 |s_x|> = {m_same}, <s_x^2 |s_y|> = {m_other}, <s_x s_y |s_z|> = {mixed}")

# ------------------------------------------------------------------------------------------------ W3
X, Y, Z = sp.symbols("X Y Z", real=True)
chi = 1 / sp.sqrt(X ** 2 + Y ** 2 + Z ** 2)
curl_z = sp.simplify(sp.diff(sp.diff(chi, Y, 3), X) - sp.diff(sp.diff(chi, X, 3), Y))
val = sp.nsimplify(curl_z.subs({X: 1, Y: 2, Z: 2}))
report("W3", val == sp.Rational(70, 2187) and sp.simplify(curl_z) != 0, f"symbolic: the z-component of the curl of (d_x^3, d_y^3, d_z^3)(1/r) is {sp.factor(curl_z)}; at (1, 2, 2) it is {val}")

# ------------------------------------------------------------------------------------------------ W4
def damping(pol, qvec):
    """Even (dissipative) part of the DISCRETE streaming operator on the local-equilibrium wave u = pol cos(q.x), projected on pol (units 1/sqrt 3)."""
    pol = np.array(pol, float) / np.linalg.norm(pol)

    def integrand(t, p):
        s = np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
        # a record arriving along axis k changes the phase by -sign(s_k) q_k; the even part of cos(phase shift) - 1 is cos(q_k) - 1
        hop = sum(abs(s[k]) * (np.cos(qvec[k]) - 1) for k in range(3))
        return 3 * (pol @ s) ** 2 * hop * np.sin(t) / (4 * np.pi)

    val, _ = integrate.dblquad(integrand, 0, 2 * np.pi, 0, np.pi)
    return val


q = 0.05
axis = damping((1, 0, 0), (q, 0, 0))
face = damping((1, 1, 0), (q / np.sqrt(2), q / np.sqrt(2), 0))
body = damping((1, 1, 1), (q / np.sqrt(3),) * 3)
ok = abs(axis / face - 4 / 3) < 2e-3 and abs(axis / body - 3 / 2) < 2e-3
report("W4", ok, f"quadrature of the discrete streaming operator on a longitudinal local-equilibrium momentum wave of wave number {q}: damping along an axis, a face diagonal and a body diagonal {axis:.6e}, {face:.6e}, {body:.6e}; ratios {axis / face:.4f} and {axis / body:.4f} (4/3 and 3/2 from 1 + sum of the fourth powers of the direction cosines; an isotropic operator would give 1 and 1)")

# ------------------------------------------------------------------------------------------------ W5
N = 96
k1 = 2 * np.pi * np.fft.fftfreq(N)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
K = [KX, KY, KZ]
k2 = KX ** 2 + KY ** 2 + KZ ** 2
k2[0, 0, 0] = 1.0
idx = np.indices((N, N, N))
rel = np.stack([(idx[a] + N // 2) % N - N // 2 for a in range(3)]).astype(float)
r = np.sqrt((rel ** 2).sum(axis=0)); r[0, 0, 0] = 1.0
rhat = rel / r
cos15 = np.cos(np.radians(15.0))


def cone(dirs):
    sel = np.zeros((N, N, N), bool)
    for d in dirs:
        u = np.array(d, float); u /= np.linalg.norm(u)
        sel |= np.abs(rhat[0] * u[0] + rhat[1] * u[1] + rhat[2] * u[2]) > cos15
    return sel


AX = cone([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
BD = cone([(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)])


def ratio(eta, rmin, rmax):
    den = [k2 + eta * K[i] ** 2 for i in range(3)]
    s = sum(K[i] ** 2 / den[i] for i in range(3)); s[0, 0, 0] = 1.0
    phat = np.exp(-0.5 * 1.5 ** 2 * k2) / s
    g = [np.real(np.fft.ifftn(-1j * K[i] * phat / den[i])) for i in range(3)]
    gr = (g[0] * rhat[0] + g[1] * rhat[1] + g[2] * rhat[2]) * r ** 2
    shell = (r >= rmin) & (r <= rmax)
    return gr[AX & shell].mean() / gr[BD & shell].mean()


iso = ratio(0.0, 8, 12)
near, far = ratio(0.5, 8, 12), ratio(0.5, 12, 18)
report("W5", abs(iso - 1) < 0.005 and near > 1.3 and abs(far / near - 1) < 0.08 and far >= near - 0.01, f"Fourier solution on a 96^3 grid: axes over body diagonals = {iso:.4f} for eta = 0; for eta = 1/2: {near:.3f} in the shell 8 to 12 and {far:.3f} in the shell 12 to 18: the direction dependence does not decay")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
