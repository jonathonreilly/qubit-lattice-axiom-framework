#!/usr/bin/env python3
"""f3: Omega^2 channel: lattice charged-scalar polarisation, marginal coefficient vs log(1/m).
Criteria: checks/f3_criteria.md (written before this script)."""
import itertools, sys, time
import numpy as np

t0 = time.time(); OUT = []; fails = []
def say(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s, flush=True)
def crit(name, ok, detail):
    say(f"[{name}] {'PASS' if ok else 'FAIL'} :: {detail}")
    if not ok: fails.append(name)

# ---------- (A) torus validation ----------
n = 4; d = 4; m2 = 1.0; V = n ** d
coords = np.array(list(itertools.product(range(n), repeat=d)))
idx = np.arange(V).reshape((n,) * d)
def site(x): return idx[tuple(np.mod(x, n))]
links = [(x, mu) for x in range(V) for mu in range(d)]
def M_of(A):
    """A: dict (x, mu) -> real; returns Hermitian M with phi^* M phi = sum |phi(x+mu) - e^{iA}phi(x)|^2 + m2|phi|^2."""
    M = m2 * np.eye(V, dtype=complex)
    for x in range(V):
        for mu in range(d):
            xp = site(coords[x] + np.eye(d, dtype=int)[mu])
            a = A.get((x, mu), 0.0)
            w = np.zeros(V, complex); w[xp] += 1.0; w[x] -= np.exp(-1j * a)   # w^dag phi = phi(xp) - e^{ia} phi(x)
            M += np.outer(w, w.conj())
    return M
M0 = M_of({}); G0 = np.linalg.inv(M0)
def Vmat(x, mu):
    xp = site(coords[x] + np.eye(d, dtype=int)[mu])
    Vm = np.zeros((V, V), complex); Vm[x, xp] = 1j; Vm[xp, x] = -1j
    return Vm
# exact Hessian -tr(G V_a G V_b), a = (x,1), b = (0,2)  [direction indices 0 and 1 in code]
Vb = Vmat(0, 1)
GVb = G0 @ Vb
Pi_exact = np.zeros(V)
for x in range(V):
    Pi_exact[x] = -np.real(np.trace(G0 @ Vmat(x, 0) @ GVb))
# momentum-sum formula, Pi_12(z), z = x - y (y = 0)
qs = 2 * np.pi * coords / n
om = np.sum(2 - 2 * np.cos(qs), axis=1); g = 1 / (om + m2)
Pi_mom = np.zeros(V)
for x in range(V):
    z = coords[x]
    ph = np.exp(1j * (qs @ z))           # e^{i q' z}
    # sum_{q,q'} g g' e^{i(q'-q)z} (e^{iq'_1} - e^{-iq_1})(e^{iq_2} - e^{-iq'_2}) / V^2
    a1 = np.exp(1j * qs[:, 0]); b2 = np.exp(1j * qs[:, 1])
    Sp = g * ph                           # over q'
    Sq = g * ph.conj()                    # over q
    # expand product: (e^{iq'_1} - e^{-iq_1})(e^{iq_2} - e^{-iq'_2})
    t1 = np.sum(Sp * a1) * np.sum(Sq * b2)
    t2 = -np.sum(Sp * a1 * b2.conj()) * np.sum(Sq)
    t3 = -np.sum(Sp) * np.sum(Sq * a1.conj() * b2)
    t4 = np.sum(Sp * b2.conj()) * np.sum(Sq * a1.conj())
    Pi_mom[x] = np.real(t1 + t2 + t3 + t4) / V ** 2
eA1 = np.abs(Pi_exact - Pi_mom).max()
# finite-difference Hessian of log det M_A (step h), via log det(1 + G0 (M_A - M0))
h = 1e-4
def f(A):
    s, ld = np.linalg.slogdet(np.eye(V) + G0 @ (M_of(A) - M0)); return ld
eA2 = 0.0
for x in [0, 1, 5, 21, 85, 170, 255]:
    fd = (f({(x, 0): h, (0, 1): h}) - f({(x, 0): h, (0, 1): -h}) - f({(x, 0): -h, (0, 1): h})
          + f({(x, 0): -h, (0, 1): -h})) / (4 * h * h)
    eA2 = max(eA2, abs(fd - Pi_exact[x]))
crit("A", eA1 <= 1e-6 and eA2 <= 1e-6,
     f"momentum vs exact -tr(GVGV): {eA1:.1e}; finite-difference (h=1e-4, 7 links) vs exact: {eA2:.1e}")
say(f"   (t={time.time()-t0:.0f}s)")

# ---------- infinite volume ----------
def nodes(npt, m, full=False):
    u, w = np.polynomial.legendre.leggauss(npt)
    s = m / 2; a = np.arcsinh(np.pi / s)
    if full:                                  # [-pi, pi]
        q = s * np.sinh(a * u); wq = w * s * a * np.cosh(a * u)
    else:                                     # [0, pi]
        uu = (u + 1) / 2; q = s * np.sinh(a * uu); wq = w / 2 * s * a * np.cosh(a * uu)
    return q, wq

def beta_inf(m, npt):
    q, wq = nodes(npt, m)
    c = np.cos(q); s = np.sin(q); om1 = 2 - 2 * c
    tot = 0.0
    for i1 in range(npt):
        for i2 in range(npt):
            om = om1[i1] + om1[i2] + om1[:, None] + om1[None, :] + m * m
            gg = 1 / om
            I = (-32 * gg ** 4 * s[i1] ** 2 * s[i2] ** 2 + 4 * gg ** 3 * s[i1] ** 2 * c[i2]
                 + 4 * gg ** 3 * s[i2] ** 2 * c[i1] - gg ** 2 * c[i1] * c[i2])
            tot += wq[i1] * wq[i2] * np.einsum("i,j,ij->", wq, wq, I)
    return -16 * tot / (2 * np.pi) ** 4      # beta = -d1 d2 F(0)

def F_inf(k, m, npt):
    q, wq = nodes(npt, m, full=True)
    tot = 0.0
    Q3, Q4 = np.meshgrid(q, q, indexing="ij"); W34 = np.outer(wq, wq)
    for i1 in range(npt):
        for i2 in range(npt):
            q1, q2 = q[i1], q[i2]
            om = lambda a, b, cc, dd: (2 - 2 * np.cos(a)) + (2 - 2 * np.cos(b)) + (2 - 2 * np.cos(cc)) + (2 - 2 * np.cos(dd)) + m * m
            g1 = 1 / om(q1, q2, Q3, Q4)
            g2 = 1 / om(q1 + k[0], q2 + k[1], Q3 + k[2], Q4 + k[3])
            val = g1 * g2 * (np.exp(1j * (q1 + k[0])) - np.exp(-1j * q1)) * (np.exp(1j * q2) - np.exp(-1j * (q2 + k[1])))
            tot += wq[i1] * wq[i2] * np.sum(W34 * val)
    return tot / (2 * np.pi) ** 4

# (B) transversality
F0 = F_inf(np.zeros(4), 0.2, 24)
crit("B", abs(F0) <= 1e-9, f"|F(0)| at m=0.2 = {abs(F0):.1e}")
# informational: analytic derivative vs finite differences of F at m = 0.4
hk = 1e-3
fdb = -np.real(F_inf([hk, hk, 0, 0], 0.4, 24) - F_inf([hk, -hk, 0, 0], 0.4, 24) - F_inf([-hk, hk, 0, 0], 0.4, 24)
               + F_inf([-hk, -hk, 0, 0], 0.4, 24)) / (4 * hk * hk)
say(f"   [info] beta(m=0.4): analytic-derivative quadrature {beta_inf(0.4, 24):.8f}, finite-difference {fdb:.8f}")
say(f"   (t={time.time()-t0:.0f}s)")

# (D) quadrature, (C) slope
b40 = beta_inf(0.05, 40); b56 = beta_inf(0.05, 56)
crit("D", abs(b40 - b56) / 2 <= 1e-5, f"c_Gamma(0.05): n=40 {b40/2:.8f}, n=56 {b56/2:.8f}, diff {abs(b40-b56)/2:.1e}")
ms = [0.4, 0.2, 0.1, 0.05]
cG = {m: beta_inf(m, 56) / 2 for m in ms}
c0 = 1 / (48 * np.pi ** 2)
devs = []
for a, b in zip(ms[:-1], ms[1:]):
    sl = (cG[b] - cG[a]) / np.log(a / b)
    devs.append(abs(sl / c0 - 1))
    say(f"   pair ({a},{b}): slope x 48pi^2 = {sl/c0:.5f}")
okC = devs[-1] <= 0.02 and all(devs[i + 1] <= devs[i] for i in range(len(devs) - 1))
crit("C", okC, f"|slope*48pi^2 - 1| along pairs: " + ", ".join(f"{x:.4f}" for x in devs))
say("   c_Gamma(m): " + ", ".join(f"m={m}: {cG[m]:.6f}" for m in ms))
say(f"f3 done: {'ALL PASS' if not fails else 'FAIL: ' + ','.join(fails)}; wall {time.time()-t0:.1f}s")
with open(sys.argv[1] if len(sys.argv) > 1 else "f3_out.txt", "w") as fh:
    fh.write("\n".join(OUT) + "\n")
