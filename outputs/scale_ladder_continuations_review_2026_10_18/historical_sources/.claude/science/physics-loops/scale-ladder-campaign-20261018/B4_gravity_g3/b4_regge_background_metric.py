#!/usr/bin/env python3
"""B4 / kernel 1b: is the Regge kernel's 'no birefringence' structural or tuned?

The repo's Kuhn-complex Regge Hessian uses flat edge lengths |v| (Euclidean background metric delta,
tick edges on the same footing as space by the supplied kinetic-isotropy primitive c_t = c_s).
Here the same complex is given a general constant background metric g0 (flat lengths
sqrt(v^T g0 v)); the dihedral-angle functions are the repo's own R4.THETA / R4.AREA (functions of
squared lengths only).  Test: the leading O(k^2) effective metric symbol equals c * EH[g0]
(linearised Einstein-Hilbert about g0).  If so, the only S4-allowed leading-order freedom of this
kernel family is the background metric itself, which yields ONE common cone for both TT
polarisations: birefringence is structurally absent; the speed value (=1) is the c_t = c_s choice.
Floating-point finite diagnostics.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, *[".."] * 5))
sys.path.insert(0, os.path.join(REPO, "scripts"))
sys.path.insert(0, HERE)

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4  # noqa: E402
from common_spin2 import check_factory, eh_tensor, gauge_variation_operator, matrix_symbol_to_tensor, \
    tt_dispersion  # noqa: E402

check, ST = check_factory()
D = 4


def make_kernel(g0):
    def q_of(cls):
        v = np.array(R4.DIRS15[cls], float)
        return float(v @ g0 @ v)

    def tri_rows(tri, k):
        a_row = np.zeros(15, complex)
        d_row = np.zeros(15, complex)
        vts = [np.array(x) for x in tri]
        qvals, einfo = [], []
        for (i, j) in [(0, 1), (0, 2), (1, 2)]:
            cls, anc = R4.edge_class(tuple(vts[i]), tuple(vts[j]))
            qvals.append(q_of(cls))
            einfo.append((cls, anc, np.sqrt(q_of(cls))))
        Aout = R4.AREA(*qvals)
        for n, (cls, anc, ell) in enumerate(einfo):
            a_row[cls] += 2 * ell * float(Aout[1 + n]) * np.exp(1j * np.dot(k, anc))
        deficit = 2 * np.pi
        for vs in R4.STARS[tri]:
            loc = {v: i for i, v in enumerate(vs)}
            hinge_local = sorted([loc[tri[0]], loc[tri[1]], loc[tri[2]]])
            miss = tuple(sorted([i for i in range(5) if i not in hinge_local]))
            qv, edata = [], []
            for (i, j) in R4.PAIRS5:
                cls, anc = R4.edge_class(vs[i], vs[j])
                qv.append(q_of(cls))
                edata.append((cls, anc, np.sqrt(q_of(cls))))
            out = R4.THETA[miss](*qv)
            deficit -= float(out[0])
            for n, (cls, anc, ell) in enumerate(edata):
                d_row[cls] -= 2 * ell * float(out[1 + n]) * np.exp(1j * np.dot(k, anc))
        return a_row, d_row, deficit

    def Q(k):
        out = np.zeros((15, 15), complex)
        for tri in R4.TRI_CLASSES:
            a, d, _ = tri_rows(tri, k)
            out += 0.5 * (np.outer(np.conj(a), d) + np.outer(np.conj(d), a))
        return out

    def Mmap(k):
        Mm = np.zeros((15, 10), complex)
        for ci, v in enumerate(R4.DIRS15):
            vv = np.array(v, float)
            ell = np.sqrt(vv @ g0 @ vv)
            z = np.dot(k, vv) / 2.0
            ph = np.exp(1j * z) * np.sinc(z / np.pi)
            for hj, (a, b) in enumerate(R4.HCOMPS):
                H = np.zeros((4, 4))
                H[a, b] += 1.0
                if a != b:
                    H[b, a] += 1.0
                Mm[ci, hj] = ph * (vv @ H @ vv) / (2 * ell)
        return Mm

    def Gmap(k):
        Gm = np.zeros((15, 4), complex)
        for ci, v in enumerate(R4.DIRS15):
            vv = np.array(v, float)
            ell = np.sqrt(vv @ g0 @ vv)
            Gm[ci, :] = (np.exp(1j * np.dot(k, vv)) - 1.0) * (g0 @ vv) / ell
        return Gm

    max_def = max(abs(tri_rows(t, np.zeros(4))[2]) for t in R4.TRI_CLASSES)
    return Q, Mmap, Gmap, max_def


def leading_schur(Q, Mmap):
    M0 = Mmap(np.zeros(4)).real
    U, _, _ = np.linalg.svd(M0, full_matrices=True)
    N = U[:, 10:]
    w, v = np.linalg.eigh(N.T @ Q(np.zeros(4)).real @ N)
    massive = np.abs(w) > 1e-9 * np.abs(w).max()
    Nm = N @ v[:, massive]

    def S(k):
        M = Mmap(k)
        Qk = Q(k)
        A = M.conj().T @ Qk @ M
        B = M.conj().T @ Qk @ Nm
        return A - B @ np.linalg.solve(Nm.T @ Qk @ Nm, B.conj().T)

    def lead(n, eps=2e-3):
        n = np.asarray(n, float)
        ev = lambda x: 0.5 * (S(x * n) + S(-x * n))  # noqa: E731
        return (4 * ev(eps) / eps ** 2 - ev(2 * eps) / (2 * eps) ** 2) / 3.0
    return lead, int(massive.sum()), w


J = np.ones((4, 4))
cases = {
    "tick length 1.1 : g0 = diag(1,1,1,1.21)": np.diag([1.0, 1.0, 1.0, 1.21]),
    "anisotropic space: g0 = diag(1,1.2,0.9,1)": np.diag([1.0, 1.2, 0.9, 1.0]),
    "S4-invariant tilt: g0 = I + 0.1 (J - I)": np.eye(4) + 0.1 * (J - np.eye(4)),
}
gv = gauge_variation_operator(D)
for name, g0 in cases.items():
    print(f"\n== background {name} ==")
    Q, Mmap, Gmap, max_def = make_kernel(g0)
    check(f"[{name}] flat background: all deficits vanish", max_def < 1e-12, f"max |deficit| {max_def:.1e}")
    k = np.array([0.7, -0.4, 1.3, 0.2])
    r = np.linalg.norm(Q(k) @ Gmap(k)) / np.linalg.norm(Q(k)) / np.linalg.norm(Gmap(k))
    check(f"[{name}] g0-displacement gauge directions are null at a generic momentum", r < 1e-12, f"{r:.1e}")
    lead, nm, w = leading_schur(Q, Mmap)
    print(f"   non-metric k=0 eigenvalues {np.round(w, 6)} ({nm} massive)")
    T = matrix_symbol_to_tensor(lead, D)
    imr = np.abs(T.imag).max() / np.abs(T.real).max()
    T = T.real
    EHg = eh_tensor(D, g0)
    c = (T @ EHg) / (EHg @ EHg)
    res = np.linalg.norm(T - c * EHg) / np.linalg.norm(T)
    EH0 = eh_tensor(D)
    c0 = (T @ EH0) / (EH0 @ EH0)
    res0 = np.linalg.norm(T - c0 * EH0) / np.linalg.norm(T)
    gvar = np.abs(gv(T[:, None])).max() / np.abs(T).max()
    print(f"   |Im|/|Re| {imr:.1e}; gauge variation {gvar:.1e}; T = c*EH[g0], c = {c:+.8f}, "
          f"residual {res:.2e}  (vs EH[delta]: residual {res0:.2e}); sqrt(det g0)/2 = {np.sqrt(np.linalg.det(g0)) / 2:.8f}")
    check(f"[{name}] leading effective symbol = c * EH[g0] (not EH[delta])", res < 1e-7 and res0 > 1e-3,
          f"residual {res:.2e}")
    if np.allclose(g0, np.diag(np.diag(g0))):
        for dn, nv in (("[100]", (1, 0, 0)), ("[110]", (1, 1, 0)), ("[111]", (1, 1, 1))):
            rr = tt_dispersion(T, D, nv, w2max=3.0)
            ns = np.array(nv, float) / np.linalg.norm(nv)
            ginv = np.linalg.inv(g0)
            expect = (ns @ ginv[:3, :3] @ ns) / ginv[3, 3]          # g^{ab} k_a k_b = 0 with k_tau = i omega
            print(f"   {dn}: roots {[(round(a, 9), m) for a, _, m, _ in rr]}; EH[g0] cone predicts {expect:.9f}")
            check(f"[{name}] {dn}: both TT polarisations on the single g0 cone (multiplicity 2)",
                  len(rr) == 2 and all(abs(a - expect) < 1e-7 and m == 2 for a, _, m, _ in rr))

print(f"\nTOTAL: PASS={ST['PASS']} FAIL={ST['FAIL']}")
