#!/usr/bin/env python3
'Finite computations supporting: Numerical comparisons of selected momentum-sector rates across finite ice strips and flux sectors, with complement-parity distinctions. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_FLUX_SECTOR_PHOTON_RISE_IS_WAVENUMBER_INDEPENDENT_AND_A_SECOND_BRANCH_CROSSES_BELOW_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_LAYER_TRANSFER_BRANCH_HAS_THE_DISPERSION_OF_A_MASSLESS_NEAREST_NEIGHBOUR_LATTICE_FIELD_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_STATIC_PHOTON_STIFFENS_IN_A_BACKGROUND_FLUX_AND_SATURATION_LEAVES_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md')

import sys
import time

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh as _eigsh
EIGENPAIR_RESIDUALS = []
def eigsh(op, *args, **kwargs):
    rng = np.random.default_rng(20260924)
    if "v0" not in kwargs:
        v0 = rng.standard_normal(op.shape[0])
        if np.issubdtype(op.dtype, np.complexfloating):
            v0 = v0 + 1j*rng.standard_normal(op.shape[0])
        kwargs["v0"] = v0
    values, vectors = _eigsh(op, *args, **kwargs)
    for j, value in enumerate(values):
        v = vectors[:, j]; applied = op @ v
        residual = np.linalg.norm(applied-value*v)/max(1.0, abs(value)*np.linalg.norm(v), np.linalg.norm(applied))
        assert np.isfinite(residual) and residual < 1e-8, residual
        EIGENPAIR_RESIDUALS.append(float(residual))
    return values, vectors


PASS = FAIL = 0
T0 = time.time()
print("Evidence boundary: finite computations and bin diagnostics; no certified spectral enclosure, confidence coverage, particle claim or limit theorem.")


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


def row_tensor(a):
    n = 1 << a
    R = np.zeros((n, n, n, n))
    bits = lambda z: [(z >> i) & 1 for i in range(a)]
    for h in range(n):
        hb = bits(h)
        hdeg = [hb[(x - 1) % a] + hb[x] for x in range(a)]
        for w in range(n):
            wb = bits(w)
            for i in range(n):
                ib = bits(i)
                for o in range(n):
                    ob = bits(o)
                    need = [3 - hdeg[x] - ib[x] - ob[x] - wb[x] for x in range(a)]
                    if all(t in (0, 1) for t in need):
                        R[sum(t << x for x, t in enumerate(need)), o, w, i] += 1
    return R


class Prism:
    def __init__(self, a, b):
        self.a, self.b, self.n, self.A, self.N = a, b, 1 << a, a * b, 1 << (a * b)
        self.R = row_tensor(a)
        idx = np.arange(self.N)
        S = np.zeros(self.N, dtype=np.int64)
        for y in range(b):
            for x in range(a):
                S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)
        self.S = S
        self.rot = np.array([((v << 1) | (v >> (a - 1))) & (self.n - 1) for v in range(self.n)])

    def T(self, phi):
        n, b = self.n, self.b
        A = phi.reshape((n,) * b)
        A = np.einsum("...,ij->...ij", A, np.eye(n))
        for r in range(b):
            A = np.tensordot(A, self.R, axes=([r, b], [2, 3]))
            A = np.moveaxis(A, [b, b + 1], [r, b])
        return np.einsum("...ii->...", A).reshape(-1)

    def ty(self, u):
        return np.transpose(u.reshape((self.n,) * self.b), axes=list(range(1, self.b)) + [0]).reshape(-1)

    def tx(self, u):
        A = u.reshape((self.n,) * self.b)
        for ax in range(self.b):
            A = np.take(A, self.rot, axis=ax)
        return A.reshape(-1)

    def proj(self, u, kx, ky):
        out = np.zeros(self.N, dtype=complex)
        cy = u.astype(complex)
        for jy in range(self.b):
            cx = cy
            for jx in range(self.a):
                out += np.exp(-1j * (kx * jx + ky * jy)) * cx
                cx = self.tx(cx)
            cy = self.ty(cy)
        return out / (self.a * self.b)

    def top(self, s, k=None):
        # T maps the flux S of one layer to -S, so a flux sector is |S| = s
        m = (np.abs(self.S) == s).astype(float)
        sel = np.where(m > 0)[0]
        if k is None and len(sel) <= 400:
            cols = []
            for i in sel:
                e = np.zeros(self.N)
                e[i] = 1.0
                cols.append(self.T(e)[sel])
            M = np.column_stack(cols)
            return float(np.max(np.abs(np.linalg.eigvals(M))))
        if k is None:
            op = LinearOperator((self.N, self.N), matvec=lambda u: m * self.T(m * u), dtype=float)
            return float(abs(eigsh(op, k=1, which="LM", tol=1e-11, maxiter=50000)[0][0]))

        def f(u):
            v = self.proj(u * m, *k) * m
            w = self.T(v.real) + 1j * self.T(v.imag)
            return self.proj(w * m, *k) * m
        op = LinearOperator((self.N, self.N), matvec=f, dtype=complex)
        return float(abs(eigsh(op, k=1, which="LM", tol=1e-10, maxiter=50000)[0][0]))




def shifts(a, b, ms, sectors=(0, 2, 4)):
    P = Prism(a, b)
    lam = {s: P.top(s) for s in sectors}
    out = {}
    for m in ms:
        k = (np.pi, np.pi + 2 * np.pi * m / b)
        D = {s: np.log(lam[s] / P.top(s, k)) for s in sectors}
        out[m] = (D[0], {s: D[s] - D[0] for s in sectors if s})
    return out


res = {
    (2, 4): shifts(2, 4, (1, 2), (0, 2)),
    (2, 6): shifts(2, 6, (1, 2, 3)),
    (2, 8): shifts(2, 8, (1, 2, 3, 4)),
    (2, 10): shifts(2, 10, (1, 2, 5)),
}

print("== A. The rise does not follow the wavenumber ==")
small = {(2, 6): (1, 2), (2, 8): (1, 2, 3), (2, 10): (1, 2)}
okA = True
lines = []
for s, ms in small.items():
    d2 = [res[s][m][1][2] for m in ms]
    d0 = [res[s][m][0] for m in ms]
    okA &= max(d2) / min(d2) < 1.25 and max(d0) / min(d0) > 1.6
    lines.append(f"{s[0]}x{s[1]}: d_2 " + ", ".join(f"{x:.5f}" for x in d2) + " (D_0 " + ", ".join(f"{x:.3f}" for x in d0) + ")")
check('Finite diagnostic 1; scope and exceptions are in the companion note', okA, "; ".join(lines))
print()

print("== B. The rise is quadratic in the background ==")
ratios = [res[s][m][1][4] / res[s][m][1][2] for s, ms in small.items() for m in ms]
check('Finite diagnostic 2; scope and exceptions are in the companion note', all(4.0 <= r <= 4.5 for r in ratios),
      ", ".join(f"{r:.2f}" for r in ratios))
print()

print("== C. At fixed density the rise shrinks with the cross-section ==")
x4, x8 = res[(2, 4)][1][1][2], res[(2, 8)][2][1][4]
check('Finite diagnostic 3; scope and exceptions are in the companion note',
      abs(x4 - 0.0436) < 5e-4 and abs(x8 - 0.0323) < 5e-4 and x8 < x4, f"{x4:.5f}, {x8:.5f}")
print()

print("== D. A second branch at the zone boundary ==")
zb = {s: res[s][s[1] // 2][1][2] for s in res}
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      all(-0.19 < v < -0.11 for v in zb.values()), ", ".join(f"{a}x{b}: {v:+.4f}" for (a, b), v in zb.items()))
print()
print("== E. The second branch is not a photon ==")
P8 = Prism(2, 8)


def top_state(s, k):
    m = (np.abs(P8.S) == s).astype(float)

    def f(u):
        v = P8.proj(u * m, *k) * m
        w = P8.T(v.real) + 1j * P8.T(v.imag)
        return P8.proj(w * m, *k) * m
    op = LinearOperator((P8.N, P8.N), matvec=f, dtype=complex)
    ev, vec = eigsh(op, k=1, which="LM", tol=1e-10, maxiter=50000)
    v = vec[:, 0]
    # the complement v -> 1 - v reverses the index order
    return float(ev[0].real), float((np.vdot(v, v[::-1]) / np.vdot(v, v)).real)


zb_flux, zb_zero = top_state(2, (np.pi, 0.0)), top_state(0, (np.pi, 0.0))
small_flux = top_state(2, (np.pi, np.pi + 2 * np.pi / 8))
check('Finite diagnostic 5; scope and exceptions are in the companion note',
      zb_flux[0] > 0 and zb_flux[1] > 1 - 1e-6 and zb_zero[0] < 0 and zb_zero[1] < -1 + 1e-6
      and small_flux[0] < 0 and small_flux[1] < -1 + 1e-6,
      f"q = pi: flux sector level {'+' if zb_flux[0] > 0 else '-'}, parity {zb_flux[1]:+.3f}; zero flux level {'+' if zb_zero[0] > 0 else '-'}, parity {zb_zero[1]:+.3f}; "
      f"q = pi/4 flux sector parity {small_flux[1]:+.3f}")
print()
print("maximum checked relative eigenpair residual:", max(EIGENPAIR_RESIDUALS, default=0.0))
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
