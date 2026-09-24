#!/usr/bin/env python3
'Finite computations supporting: Exact symmetries of a supplied finite ice transfer; numerical maximum-modulus sector levels on 2 by 8 and 4 by 4 sections compared with a Gaussian lattice rate. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_LAYER_TRANSFER_BRANCH_HAS_THE_DISPERSION_OF_A_MASSLESS_NEAREST_NEIGHBOUR_LATTICE_FIELD_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_ZERO_FLUX_LAYER_CHAIN_GAP_CLOSES_AS_THE_SMALLEST_TRANSVERSE_WAVENUMBER_BOUNDED_THEOREM_NOTE_2026-09-23.md')

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


class Layer:
    def __init__(self, a, b):
        self.a, self.b, self.n = a, b, 1 << a
        self.R = row_tensor(a)
        idx = np.arange(1 << (a * b))
        S = np.zeros(len(idx), dtype=np.int64)
        for y in range(b):
            for x in range(a):
                S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)
        self.mask = (S == 0).astype(float)
        self.N = len(idx)
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

    def top(self, kx, ky):
        m = self.mask

        def f(u):
            v = self.proj(u * m, kx, ky) * m
            w = self.T(v.real) + 1j * self.T(v.imag)
            return self.proj(w * m, kx, ky) * m
        op = LinearOperator((self.N, self.N), matvec=f, dtype=complex)
        ev, vec = eigsh(op, k=1, which="LM", tol=1e-10, maxiter=20000)
        v = vec[:, 0]
        # the complement v -> 1 - v reverses the index order; parity = <v, C v> / <v, v>
        return float(ev[0]), float((np.vdot(v, v[::-1]) / np.vdot(v, v)).real)


def field(qs):
    return float(np.arccosh(1 + sum(1 - np.cos(q) for q in qs)))


print("== A. Translations ==")
L28, L44 = Layer(2, 8), Layer(4, 4)
rng = np.random.default_rng(7)
comm = []
for L in (L28, L44):
    x = rng.standard_normal(L.N)
    scale = np.abs(L.T(x)).max()
    comm.append(max(np.abs(L.T(L.ty(x)) - L.ty(L.T(x))).max(), np.abs(L.T(L.tx(x)) - L.tx(L.T(x))).max()) / scale)
check('Finite diagnostic 1; scope and exceptions are in the companion note', max(comm) < 1e-12, f"largest relative defect {max(comm):.1e}")
compl = []
for L in (L28, L44):
    x = rng.standard_normal(L.N)
    compl.append(np.abs(L.T(x[::-1])[::-1] - L.T(x)).max() / np.abs(L.T(x)).max())
check('Finite diagnostic 2; scope and exceptions are in the companion note', max(compl) < 1e-12, f"largest relative defect {max(compl):.1e}")
print()

print("== B. The strip 2 x 8 ==")
pi = np.pi
# physical wavenumber (0, q) sits at occupation wavenumber (pi, q + pi); lam_0 is the top of the (0, 0) sector
lam0, par0 = L28.top(0.0, 0.0)
full_op = LinearOperator((L28.N, L28.N), matvec=lambda u: L28.mask * L28.T(L28.mask * u), dtype=float)
full0 = float(eigsh(full_op, k=1, which="LM", tol=1e-10, maxiter=20000)[0][0])
res28 = {m: L28.top(pi, 2 * pi * m / 8) for m in range(8)}
occ = {m: abs(res28[m][0]) for m in res28}
D28 = {m: np.log(lam0 / occ[m]) for m in occ}
qs = {5: pi / 4, 6: pi / 2, 7: 3 * pi / 4}
dev28 = {m: D28[m] / field([qs[m]]) - 1 for m in qs}
check('Finite diagnostic 3; scope and exceptions are in the companion note',
      abs(lam0 - full0) < 1e-6 * full0 and abs(full0 - 4727353.1633) < 1e-3 and all(abs(d) < 0.01 for d in dev28.values()),
      ", ".join(f"q={qs[m]:.4f}: D={D28[m]:.4f} field={field([qs[m]]):.4f}" for m in qs))
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      all(abs(occ[m] - occ[8 - m]) < 1e-6 * occ[m] for m in (1, 2, 3)))
print()

print("== C. The square 4 x 4 ==")
lam0_44, par0_44 = L44.top(0.0, 0.0)
pts = {(3, 2): (pi / 2, 0.0), (3, 3): (pi / 2, pi / 2), (3, 0): (pi / 2, pi), (2, 3): (0.0, pi / 2)}
res44 = {mm: L44.top(2 * pi * mm[0] / 4, 2 * pi * mm[1] / 4) for mm in pts}
D44 = {mm: np.log(lam0_44 / abs(res44[mm][0])) for mm in pts}
dev44 = {mm: D44[mm] / field(pts[mm]) - 1 for mm in pts}
ratio = D44[(3, 3)] / D44[(3, 2)]
fratio = field(pts[(3, 3)]) / field(pts[(3, 2)])
check('Finite diagnostic 5; scope and exceptions are in the companion note',
      all(abs(dev44[mm]) < 0.02 for mm in ((3, 2), (3, 3), (3, 0))),
      ", ".join(f"{pts[mm]}: D={D44[mm]:.4f} field={field(pts[mm]):.4f}" for mm in ((3, 2), (3, 3), (3, 0))).replace("1.5707963267948966", "pi/2").replace("3.141592653589793", "pi"))
check('Finite diagnostic 6; scope and exceptions are in the companion note',
      abs(ratio / fratio - 1) < 0.01 and abs(D44[(3, 2)] - D44[(2, 3)]) < 1e-8,
      f"ratio {ratio:.4f} vs field {fratio:.4f}")
print()

print("== D. The lowest branch points are the gaps of open PR #8864 ==")
check('Finite diagnostic 7; scope and exceptions are in the companion note',
      abs(8 * D28[5] - 5.9434) < 1e-4 and abs(D44[(3, 2)] - 1.29627) < 1e-5,
      f"{8 * D28[5]:.5f}, {D44[(3, 2)]:.6f}")
print()

print("== E. The branch is odd under the complement ==")
branch = [res28[m] for m in (1, 2, 3, 5, 6, 7)] + list(res44.values())
check('Finite diagnostic 8; scope and exceptions are in the companion note',
      lam0 > 0 and lam0_44 > 0 and min(par0, par0_44) > 1 - 1e-8
      and all(lev < 0 and par < -1 + 1e-8 for lev, par in branch),
      f"{len(branch)} branch states, parities in [{min(p for _, p in branch):.9f}, {max(p for _, p in branch):.9f}]")
print()
print("maximum checked relative eigenpair residual:", max(EIGENPAIR_RESIDUALS, default=0.0))
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
