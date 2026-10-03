"""A9 task 3: lone-hole odds p0 under quiet linear formation rules (supplied toys).

A lone hole x has all six neighbours recorded. By Q1 the recorded neighbours'
possibilities agree with their records, so they are pure locked states |r_y>.
The hole's formation chance is p0 = tr(F_eff rho_x), F_eff = <R|F|R> (2x2).
Its floor over the hole's own possibilities is lambda_min(F_eff); a positive
floor gives exponential filling of enclosed holes (A4, 3.1e).

Rules (each F annihilates its own quiet vacuum; none adopted):
  ferro  : F = sum_y P_singlet(x,y) / 3.5     (vacuum: aligned product states)
  klein  : F = P_{S=7/2}(star)                (vacuum: nearest-neighbour singlet coverings)
  cluster: F = (1 - X_x prod_y Z_y)/2         (vacuum: 3D cluster state; privileges X/Z axes)
Record contents: Haar-random, Z-menu with equal odds, or all equal.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np

rng = np.random.default_rng(11)
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1.0, -1.0]).astype(complex)
I = np.eye(2)


def op_on(ops, n=7):
    out = np.array([[1.0 + 0j]])
    for q in range(n):
        out = np.kron(out, ops.get(q, I))
    return out


# ferro: singlet projectors on the six bonds (x = qubit 0)
Ps_list = []
for y in range(1, 7):
    SS = sum(op_on({0: S / 2, y: S / 2}) for S in (X, Y, Z))
    Ps_list.append(0.25 * np.eye(128) - SS)
Fsum = sum(Ps_list)
lam_max = np.linalg.eigvalsh(Fsum).max()
F_ferro = Fsum / lam_max
# klein
Stot = [sum(op_on({q: S / 2}) for q in range(7)) for S in (X, Y, Z)]
S2 = sum(s @ s for s in Stot)
lam, vec = np.linalg.eigh(S2)
sel = np.isclose(lam, 3.5 * 4.5)
F_klein = vec[:, sel] @ vec[:, sel].conj().T
# cluster
K = op_on({0: X, 1: Z, 2: Z, 3: Z, 4: Z, 5: Z, 6: Z})
F_cluster = (np.eye(128) - K) / 2
rules = {"ferro": F_ferro, "klein": F_klein, "cluster": F_cluster}
print(f"ferro normalisation: max eigenvalue of sum of six singlet projectors = {lam_max:.6f} (expect 3.5)")


def f_eff(F, rs):
    # contract neighbours 1..6 with locked states rs
    T = F.reshape([2] * 14)
    for k, r in enumerate(rs, start=1):
        pass
    big = np.array([[1.0 + 0j]])
    vecR = np.array([1.0 + 0j])
    for r in rs:
        vecR = np.kron(vecR, r)
    # F acts on x (x) neighbours; F_eff[a,b] = <a, R| F |b, R>
    Fe = np.zeros((2, 2), complex)
    for a in range(2):
        for b in range(2):
            va = np.kron(np.eye(2)[a], vecR); vb = np.kron(np.eye(2)[b], vecR)
            Fe[a, b] = va.conj() @ F @ vb
    return Fe


def haar_qubit():
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    return v / np.linalg.norm(v)


samplers = {
    "Haar-random contents": lambda: [haar_qubit() for _ in range(6)],
    "Z-menu, equal odds  ": lambda: [np.eye(2, dtype=complex)[rng.integers(2)] for _ in range(6)],
    "all contents equal  ": (lambda: (lambda r: [r] * 6)(haar_qubit())),
}
NS = 3000
for sname, samp in samplers.items():
    res = {k: [] for k in rules}
    half = {k: [] for k in rules}
    for _ in range(NS):
        rs = samp()
        for k, F in rules.items():
            Fe = f_eff(F, rs)
            ev = np.linalg.eigvalsh((Fe + Fe.conj().T) / 2)
            res[k].append(ev[0]); half[k].append(np.trace(Fe).real / 2)
    print(f"{sname}:")
    for k in rules:
        a = np.array(res[k]); h = np.array(half[k])
        print(f"   {k:8s} floor lambda_min: min={a.min():.3e} median={np.median(a):.3e} "
              f"fraction with zero floor (<1e-12) = {np.mean(a < 1e-12):.3f};  p0 for an equal-odds hole: mean={h.mean():.3e}")
