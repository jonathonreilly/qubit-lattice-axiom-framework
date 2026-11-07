#!/usr/bin/env python3
"""Contraction of the irrelevant quadratic data through the class lift. Consumer: Lemma 2 of `library/gauge-taylor-contraction.md`, second proof.

Written before running. Trivial background. The class lift of a coarse plane wave A'(p) is H := first block of Sad#^-1 (0, A') of `library/fibre-propagator.md`, at one level, with fine units. Take the test functional Z(X) := sum over fine sites of |grad d X|^2, a dimension-6 quadratic form in X, of symbol (q ^)^* |q-hat|^2 (q ^). Then Z o lift at coarse momentum p should have, per coarse cell:

 Pi(L, p) := Z(H) / ( |p-hat' ^ A'|^2 min(|p-hat'|, 1)^2 ),  with Z(H) = ||grad d H||^2 = ||d^dagger d H||^2 on the fine lattice, in d = 2, 3, 4,

where p-hat' is the coarse symbol. Scaling: H has potential amplitude 1/L for A' of unit potential, so the n = 0 part is L^d (1/L^2) (|p|/L)^4 (|p'|)^... In level-1 momentum: Pi(L, p) ~ L^{d - 6} at all p.

PRE-STATED criteria.
 D0. The identity ||grad d H||^2 = ||d^dagger d H||^2 on the fine lattice, to 1e-9 relative. (d H is closed, and the identity reads (d d^dagger + d^dagger d) = -Delta on 2-forms.)
 D1. For each d, L: sup over a grid of p with |p|_inf >= 0.05 of Pi(L, p) L^{6 - d} is at most 2 times its value at the smallest L in that d. d = 2: L = 3, 5, 7, 9, 11. d = 3: L = 3, 5, 7. d = 4: L = 3, 5.
 D2. Small p: Pi(L, p) at p = (s, s/2, 0, ...) with s = 0.4, 0.2, 0.1, 0.05 stays bounded: the largest value at most 2 times the value at s = 0.4. This is the statement that no alias feeds an F^2 term or a lower term. A failure here means the form is not O(p^4) in F^2 units.
 D3. Polarisation: A' transverse to p at real p. A longitudinal A' gives H pure gauge, so d H = 0 to 1e-10 relative: a control on the class solution.
FAIL if any of D0-D3 fails.

Limits. Trivial background, one level, one quadratic test functional. It says nothing on orders 3, 4, for which the second proof is sums over aliases, and nothing on the source. Analyticity in the strip is from the Combes-Thomas step of Theorem F, and it is not tested here: a first draft had a criterion for it, which I removed before any run, as the continuation of the adjoint needs its own code. RSS guard 2 GB.
"""
import importlib.util
import itertools
import os
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sharp", os.path.join(HERE, "hard-core--mapped_sharp.py"))
sh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh)


def solve(B, p, Ap):
    d, V, nb = B.d, B.V, B.nb
    Dd, dm, r, Qo = B.ops(p)
    rn = r / np.linalg.norm(r)
    Pr = np.eye(V, dtype=complex) - rn.conj()[:, None] @ rn[None, :]
    K = dm.conj().T @ dm + Dd.conj().T @ Pr @ Dd
    S = np.zeros((nb + d, nb + d), dtype=complex)
    S[:nb, :nb] = K
    S[:nb, nb:] = Qo.conj().T
    S[nb:, :nb] = Qo
    sol = np.linalg.solve(S, np.concatenate([np.zeros(nb, dtype=complex), Ap]))
    return sol[:nb], dm, Dd


def grad_two_form(B, p, F):
    """Fine gradient of a two-form: returns the array of (T_nu - 1) F for each nu."""
    out = []
    n2 = len(B.pairs)
    V = B.V
    for nu in range(B.d):
        T = B.T(nu, p)
        for k in range(n2):
            out.append((T - np.eye(V)) @ F[k * V : (k + 1) * V])
    return np.concatenate(out)


def coarse_symbols(p):
    return np.exp(1j * np.asarray(p, dtype=complex)) - 1


def transverse(p):
    """A real unit polarisation orthogonal to the coarse symbol, for real p."""
    ph = coarse_symbols(p)
    d = len(p)
    # Two-dimensional: the rotation of ph in the plane of its two largest components.
    idx = np.argsort(-np.abs(ph))[:2]
    a = np.zeros(d, dtype=complex)
    a[idx[0]] = np.conj(ph[idx[1]])
    a[idx[1]] = -np.conj(ph[idx[0]])
    a /= np.linalg.norm(a)
    # Orthogonal in the sense sum conj(ph_mu) a_mu = 0.
    return a


def curl_norm2(ph, a):
    return float(np.linalg.norm(np.outer(ph, a) - np.outer(a, ph)) ** 2 / 2)


def pi_value(B, p):
    a = transverse(p)
    # Coarse curvature of the plane wave.
    ph = coarse_symbols(p)
    H, dm, Dd = solve(B, p, a)
    F = dm @ H
    gF = grad_two_form(B, p, F)
    z1 = float(np.linalg.norm(gF) ** 2)
    z2 = float(np.linalg.norm(dm.conj().T @ F) ** 2)
    den = curl_norm2(ph, a) * min(np.linalg.norm(ph), 1.0) ** 2
    return z1 / den, z1, z2


def longitudinal(B, p):
    ph = coarse_symbols(p)
    a = ph / np.linalg.norm(ph)
    H, dm, Dd = solve(B, p, a)
    return float(np.linalg.norm(dm @ H) / np.linalg.norm(H))


def grid(d, n=5):
    vals = [np.pi * (k + 1) / n for k in range(n)]
    return [np.array(q) for q in itertools.combinations_with_replacement(vals, d) ]


def main():
    ok = True
    print("D0, D1, D3", flush=True)
    for d, Ls, n in ((2, (3, 5, 7, 9, 11), 6), (3, (3, 5, 7), 4), (4, (3, 5), 3)):
        base = None
        for L in Ls:
            B = sh.Bloch(d, L)
            best, worst0, worst3 = 0.0, 0.0, 0.0
            for p in grid(d, n):
                v, z1, z2 = pi_value(B, p)
                best = max(best, v)
                worst0 = max(worst0, abs(z1 - z2) / max(z1, 1e-300))
                worst3 = max(worst3, longitudinal(B, p))
                guard()
            scaled = best * L ** (6 - d)
            if base is None:
                base = scaled
            good = worst0 <= 1e-9 and scaled <= 2 * base and worst3 <= 1e-10
            ok = ok and good
            print(f" d={d} L={L}: sup Pi={best:.5e} scaled by L^(6-d)={scaled:.4f} D0={worst0:.1e} D3={worst3:.1e}: {good} rss={rss_gb():.2f}GB", flush=True)
    print("D2", flush=True)
    for d, L in ((2, 5), (2, 9), (3, 5), (4, 3)):
        B = sh.Bloch(d, L)
        vals = []
        for s in (0.4, 0.2, 0.1, 0.05):
            p = np.zeros(d)
            p[0], p[1] = s, s / 2
            vals.append(pi_value(B, p)[0])
        good = max(vals) <= 2 * vals[0]
        ok = ok and good
        print(f" D2 d={d} L={L}: {[f'{v:.5e}' for v in vals]}: {good}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
