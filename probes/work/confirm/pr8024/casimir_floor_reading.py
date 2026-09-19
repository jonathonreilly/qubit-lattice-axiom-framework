#!/usr/bin/env python3
"""J:confirm:J-attack-g-PR8024 - independent test of the finder's HIT on PR #8024 (block 34, volume-uniform gap): 'the stated
Casimir floor C >= 4 with equality at (1,0), (0,1) fails: C(1,0) = 8/3'.

Different machinery from the finder (who evaluated the closed form C(p,q) = (2/3)(p^2+pq+q^2+3p+3q) and compared it with 4):
  * the note's sentence is read from the PR branch and parsed for what 'this polynomial' refers to;
  * the Casimirs are computed from scratch in the trace-orthonormal convention Tr(T^a T^b) = delta^{ab}: Gell-Mann matrices for
    the fundamental (1,0) and antifundamental (0,1), structure constants for the adjoint (1,1), and the symmetric square for (2,0)
    (sympy, exact), then compared with (2/3)(p^2+pq+q^2+3p+3q);
  * E = (3/(2a)) C (the note's K_e = (3/(2a))(-Delta_e)) is formed and its minimum over nonzero labels located;
  * the plaquette counts are recounted in closed form (products of ranges) for L = 1..12.
Prints 'HIT: confirmed - ...' only if the note's floor fails under its own antecedent; otherwise 'SUMMARY: not reproduced - ...'.
"""
import itertools
import re
import subprocess
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "codex/volume-uniform-gap-block34-20260907"
NOTE = "docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md"


def show(path):
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"origin/{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def gell_mann():
    I = sp.I
    L = [sp.zeros(3, 3) for _ in range(8)]
    L[0][0, 1] = L[0][1, 0] = 1
    L[1][0, 1], L[1][1, 0] = -I, I
    L[2][0, 0], L[2][1, 1] = 1, -1
    L[3][0, 2] = L[3][2, 0] = 1
    L[4][0, 2], L[4][2, 0] = -I, I
    L[5][1, 2] = L[5][2, 1] = 1
    L[6][1, 2], L[6][2, 1] = -I, I
    L[7][0, 0] = L[7][1, 1] = 1 / sp.sqrt(3)
    L[7][2, 2] = -2 / sp.sqrt(3)
    return L


def main():
    note = show(NOTE)
    para = next(l for l in note.splitlines() if "this polynomial is at least" in l)
    m = re.search(r"C\(p,q\)=\(2/3\)\(p²\+pq\+q²\+3p\+3q\), hence E\(p,q\)=\[p²\+pq\+q²\+3p\+3q\]/a for every p,q>=0\. For a nonzero label "
                  r"this polynomial is at least4, with equality only at \(1,0\) and \(0,1\)", para)
    energy = "first nonzero energy4/a" in para
    conv = "K_e=(3/(2a))(-Delta_e)" in para
    print(f"[note] the floor sentence directly follows 'E(p,q)=[p²+pq+q²+3p+3q]/a': {bool(m)}; 'first nonzero energy4/a': {energy}; "
          f"K_e=(3/(2a))(-Delta_e): {conv}")

    # Casimirs in the trace-orthonormal convention Tr(T^a T^b) = delta^{ab}: T^a = lambda^a / sqrt(2)
    lam = gell_mann()
    T = [l / sp.sqrt(2) for l in lam]
    ortho = all(sp.simplify((T[a] * T[b]).trace() - (1 if a == b else 0)) == 0 for a in range(8) for b in range(8))
    Cf = sp.simplify(sum((t * t for t in T), sp.zeros(3, 3)))
    Tbar = [-t.conjugate() for t in T]
    Cbar = sp.simplify(sum((t * t for t in Tbar), sp.zeros(3, 3)))
    # structure constants [T^a, T^b] = i f_abc T^c with Tr(T^c T^d) = delta: f_abc = -i Tr([T^a,T^b] T^c)
    f = [[[sp.simplify(-sp.I * ((T[a] * T[b] - T[b] * T[a]) * T[c]).trace()) for c in range(8)] for b in range(8)] for a in range(8)]
    Tad = [sp.Matrix(8, 8, lambda b, c: -sp.I * f[a][b][c]) for a in range(8)]
    Cad = sp.simplify(sum((t * t for t in Tad), sp.zeros(8, 8)))
    # (2,0): symmetric square of the fundamental
    basis = [(i, j) for i in range(3) for j in range(i, 3)]

    def sym_rep(X):
        Mx = sp.zeros(6, 6)
        for c, (i, j) in enumerate(basis):
            # action on e_i e_j (symmetrized): X e_i (x) e_j + e_i (x) X e_j
            vec = {}
            for k in range(3):
                for (u, v, coef) in ((k, j, X[k, i]), (i, k, X[k, j])):
                    key = tuple(sorted((u, v)))
                    vec[key] = vec.get(key, 0) + coef
            for key, val in vec.items():
                r = basis.index(key)
                Mx[r, c] += val
        return Mx
    # use a normalized basis for Hermiticity is unnecessary: the Casimir is basis independent
    Ts = [sym_rep(t) for t in T]
    Csym = sp.simplify(sum((t * t for t in Ts), sp.zeros(6, 6)))
    C = lambda p, q: sp.Rational(2, 3) * (p * p + p * q + q * q + 3 * p + 3 * q)
    got = {"(1,0)": Cf, "(0,1)": Cbar, "(1,1)": Cad, "(2,0)": Csym}
    want = {"(1,0)": C(1, 0), "(0,1)": C(0, 1), "(1,1)": C(1, 1), "(2,0)": C(2, 0)}
    cas_ok = ortho and all(got[k] == want[k] * sp.eye(got[k].shape[0]) for k in got)
    print(f"[casimir] trace-orthonormal generators: {ortho}; C(1,0), C(0,1), C(1,1), C(2,0) from matrices = "
          f"{[str(sp.simplify(got[k][0, 0])) for k in got]}, closed form {[str(want[k]) for k in want]}: {cas_ok}")

    a = sp.symbols("a", positive=True)
    Eab = {(p, q): sp.simplify(sp.Rational(3, 2) / a * C(p, q)) for p, q in itertools.product(range(0, 25), repeat=2)}
    quad_ok = all(sp.simplify(Eab[k] - (k[0] ** 2 + k[0] * k[1] + k[1] ** 2 + 3 * k[0] + 3 * k[1]) / a) == 0 for k in Eab)
    nz = {k: v for k, v in Eab.items() if k != (0, 0)}
    mn = min(sp.simplify(v * a) for v in nz.values())
    argmin = sorted(k for k, v in nz.items() if sp.simplify(v * a) == mn)
    print(f"[energy] E = (3/(2a)) C = [p^2+pq+q^2+3p+3q]/a on {len(Eab)} labels: {quad_ok}; min over nonzero labels of a E = {mn} at "
          f"{argmin}; C there = {C(1, 0)}")

    def counts(L):
        wg = 3 * max(L - 1, 0) ** 3
        ind = 3 * L * max(L - 1, 0) ** 2
        return wg, ind
    brute = []
    for L in range(1, 13):
        anchors = sum(1 for x in itertools.product(range(L), repeat=3) if all(c + 1 < L for c in x))
        ind = 0
        for x in itertools.product(range(L), repeat=3):
            for i, j in ((0, 1), (0, 2), (1, 2)):
                if x[i] + 1 < L and x[j] + 1 < L:
                    ind += 1
        brute.append((3 * anchors, ind) == counts(L) and 3 * anchors - ind == -3 * max(L - 1, 0) ** 2)
    print(f"[counts] whole-group 3(L-1)^3 and individual 3L(L-1)^2 (difference 3(L-1)^2), L = 1..12: {all(brute)}")

    if m and energy and conv and cas_ok and quad_ok and mn == 4 and argmin == [(0, 1), (1, 0)] and all(brute):
        print("SUMMARY: not reproduced - the note's floor 'this polynomial is at least 4, with equality only at (1,0) and (0,1)' "
              "follows 'E(p,q)=[p²+pq+q²+3p+3q]/a' and is true of that bracket (min 4 exactly at (1,0), (0,1)); it is consistent with "
              "C(1,0) = C(0,1) = 8/3 (recomputed from trace-orthonormal Gell-Mann generators, with C(1,1) = 6 and C(2,0) = 20/3 "
              "matching (2/3)(p^2+pq+q^2+3p+3q)) through E = (3/(2a))C, giving the note's 'first nonzero energy 4/a'. The finder "
              "applied the floor to C instead of to E's bracket; the plaquette counts hold, as the finder also found")
        return 0
    print("HIT: confirmed - the note's floor fails under its own reading (see the lines above)")
    print("SUMMARY: confirmed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
