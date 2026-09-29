#!/usr/bin/env python3
"""J:attack-g:PR9351 -- PROOF STEP BY BRUTE FORCE: the block identities of the "Exact reduction" section of the square microscopic spectral certificate note, verified literally by enumeration.

The steps attacked (as written in the note): for the two-record square sector (edges oriented A = {0,2} -> B = {1,3}; fields E = (n, q0-1-n, -q1-n, q2-1+q1+n) with all entries in [-S, S]; a legal outward hop
lowers its edge field by one with amplitude sqrt(1 - E_e(E_e - 1)/C), C = S(S+1); W counts vacant A sites; A, B contain the negative hop sign; Z = BA):
  (s1) P has n = -S..S and W = 2 has m = -S..S-1;
  (s2) A*A = 4 I - 4 n^2/C (diagonal);
  (s3) Z|n> = 2 [d_(n-1)|n-1> + d_n|n>], d_m = 1 - m(m+1)/C, exterior d_(-S-1) = d_S = 0 ("the two orders of each allowed matching");
  (s4) "Each fully-B state has four reverse-hop weights squared d_m, while no W=1 state reaches two different fully-B states; this proves BB* = 4 diag(d_m)";
  (s5) 0 <= d_m <= 1;
  (s6) at rotor order (all hop amplitudes 1) BB* = 4 I and A*(B*B)^2 A = 4 N0 with N0 = Z*Z having diagonal 8 and adjacent 4;
  (s7) N = Z*Z has diagonal 4(d_(n-1)^2 + d_n^2) and adjacent 4 d_n^2;
  (s8) the eliminated block Q = [[(1 - lam) I, sqrt(x) B*], [sqrt(x) B, (2 - lam) I]] is positive definite exactly when lam < 1 and (1 - lam)(2 - lam) > 4x max_m d_m (so under (1 - lam)(2 - lam) > 4x for 0 <= d <= 1).
Each step is executed exactly (sympy rationals / square roots) for S = 1..5 and in floating point for S up to 12 (labelled), from the definitions above only: the matrices A and B are built by enumerating
states and hops, never from the note's block formulas. Prints SUMMARY: and, only if a step fails, HIT:.
"""
import itertools
import sys
import time

import numpy as np
import sympy as sp

T0 = time.time()
RESULTS, FIRED = [], []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def build(S, exact=True, rotor=False):
    """Enumerate the sector and return (states by W, A: W1 <- W0, B: W2 <- W1) with the negative hop sign; amplitudes sqrt(1 - E(E-1)/C), or 1 at rotor order."""
    C = S * (S + 1)
    edges = [(0, 1), (0, 3), (2, 1), (2, 3)]
    by = {0: [], 1: [], 2: []}
    for q in itertools.product((0, 1), repeat=4):
        if sum(q) != 2:
            continue
        for n in range(-S, S + 1):
            E = (n, q[0] - 1 - n, -q[1] - n, q[2] - 1 + q[1] + n)
            if all(-S <= e <= S for e in E):
                by[sum(1 - q[a] for a in (0, 2))].append((q, E))
    idx = {w: {s: i for i, s in enumerate(by[w])} for w in by}
    amp = (lambda E: sp.sqrt(sp.Integer(1) - sp.Rational(E * (E - 1), C))) if exact else (lambda E: np.sqrt(max(0.0, 1 - E * (E - 1) / C)))
    if rotor:
        amp = lambda E: (sp.Integer(1) if exact else 1.0)
    zero = sp.Integer(0) if exact else 0.0

    def block(w_from, w_to):
        M = sp.zeros(len(by[w_to]), len(by[w_from])) if exact else np.zeros((len(by[w_to]), len(by[w_from])))
        for j, (q, E) in enumerate(by[w_from]):
            for k, (a, b) in enumerate(edges):
                if q[a] == 1 and q[b] == 0:
                    a2 = amp(E[k])
                    if (a2 != 0) if exact else (a2 > 1e-14):
                        q2 = list(q); q2[a] = 0; q2[b] = 1; E2 = list(E); E2[k] -= 1
                        key = (tuple(q2), tuple(E2))
                        if rotor and key not in idx[w_to]:
                            continue                                   # rotor order on a finite window: hops leaving the window are dropped (interior identities only)
                        M[idx[w_to][key], j] += -a2
        return M
    return by, block(0, 1), block(1, 2)


def run():
    global_ok = True
    # ---- exact, S = 1..5
    for S in range(1, 6):
        C = S * (S + 1)
        by, A, B = build(S)
        d = lambda m: sp.Integer(1) - sp.Rational(m * (m + 1), C)
        ns = sorted({E[0] for q, E in by[0]}); ms = sorted({E[0] for q, E in by[2]})
        s1 = ns == list(range(-S, S + 1)) and ms == list(range(-S, S)) and len(by[0]) == 2 * S + 1 and len(by[2]) == 2 * S
        # order the W0 and W2 bases by n and m
        o0 = sorted(range(len(by[0])), key=lambda i: by[0][i][1][0]); o2 = sorted(range(len(by[2])), key=lambda i: by[2][i][1][0])
        Ao = A[:, o0]; Bo = B[o2, :]
        AA = sp.simplify(Ao.T * Ao)
        s2 = AA == sp.diag(*[sp.Integer(4) - sp.Rational(4 * n * n, C) for n in ns])
        Z = sp.simplify(Bo * Ao)
        Zx = sp.zeros(len(ms), len(ns))
        for jn, n in enumerate(ns):
            for m_ in (n - 1, n):
                if m_ in ms:
                    Zx[ms.index(m_), jn] += 2 * d(m_)
        s3 = sp.simplify(Z - Zx) == sp.zeros(*Z.shape) and d(-S - 1) == 0 and d(S) == 0
        BB = sp.simplify(Bo * Bo.T)
        rows = []
        for i2 in range(len(by[2])):
            rows.append(sorted(sp.simplify(B[i2, j] ** 2) for j in range(B.shape[1]) if B[i2, j] != 0))
        m_of = lambda i2: by[2][i2][1][0]
        four = all(len(r) == 4 and all(v == d(m_of(i2)) for v in r) for i2, r in enumerate(rows))
        unique = all(sum(1 for i2 in range(B.shape[0]) if B[i2, j] != 0) <= 1 for j in range(B.shape[1]))
        s4 = four and unique and sp.simplify(BB - sp.diag(*[4 * d(m) for m in ms])) == sp.zeros(*BB.shape)
        s5 = all(0 <= d(m) <= 1 for m in range(-S - 1, S + 1))
        Nx = sp.simplify(Z.T * Z)
        Ny = sp.zeros(len(ns), len(ns))
        for jn, n in enumerate(ns):
            Ny[jn, jn] = 4 * ((d(n - 1) ** 2 if n - 1 >= -S - 1 else 0) + (d(n) ** 2 if n <= S else 0))
            if jn + 1 < len(ns):
                Ny[jn, jn + 1] = Ny[jn + 1, jn] = 4 * d(n) ** 2
        s7 = sp.simplify(Nx - Ny) == sp.zeros(*Nx.shape)
        ok = s1 and s2 and s3 and s4 and s5 and s7
        global_ok &= ok
        check(f"S = {S} (exact): (s1) state counts, (s2) A*A = 4I - 4n^2/C, (s3) Z formula, (s4) four reverse weights d_m + uniqueness + BB* = 4 diag(d_m), (s5) 0 <= d <= 1, (s7) Z*Z entries", ok,
              f"dims W0/W1/W2 = {len(by[0])}/{len(by[1])}/{len(by[2])}; s1 {s1}, s2 {s2}, s3 {s3}, s4 {s4} (four weights {four}, unique {unique}), s5 {s5}, s7 {s7}; {time.time() - T0:.0f} s")
        if not ok:
            FIRED.append(f"S = {S}: a block identity fails ({dict(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s7=s7)})")
    # ---- rotor order (s6): exact with amplitudes 1 on a window; boundary excluded by taking S large and looking at interior indices
    S = 6
    by, A, B = build(S, rotor=True)
    o0 = sorted(range(len(by[0])), key=lambda i: by[0][i][1][0]); o2 = sorted(range(len(by[2])), key=lambda i: by[2][i][1][0])
    Ao = A[:, o0]; Bo = B[o2, :]
    BBs = Bo * Bo.T
    Z = Bo * Ao
    N0 = Z.T * Z
    L = 2 * S + 1
    inner = list(range(1, L - 1))
    inner2 = list(range(2, len(by[2]) - 2))
    s6a = all(BBs[i, i] == 4 and all(BBs[i, j] == 0 for j in range(BBs.shape[1]) if j != i) for i in inner2)
    lhs = Ao.T * (Bo.T * Bo) ** 2 * Ao
    inner3 = list(range(2, L - 2))
    s6b = all(sp.simplify(lhs[i, j] - 4 * N0[i, j]) == 0 for i in inner3 for j in inner3)
    s6c = all(N0[i, i] == 8 for i in inner) and all(N0[i, i + 1] == 4 for i in inner[:-1])
    check("(s6) rotor order (amplitudes 1, S = 6 window, exact, interior sites): BB* = 4I, A*(B*B)^2 A = 4 N0, N0 has diagonal 8 and adjacent 4", s6a and s6b and s6c, f"BB* = 4I {s6a}; A*(B*B)^2 A = 4 Z*Z {s6b}; N0 (8, 4) {s6c}")
    if not (s6a and s6b and s6c):
        FIRED.append("rotor-order identities fail")
    # ---- (s8) positivity of Q, floating point, S up to 12
    rng = np.random.default_rng(1)
    bad = 0; tested = 0; worst = 0.0
    for S in (2, 4, 8, 12):
        C = S * (S + 1)
        by, A, B = build(S, exact=False)
        for _ in range(400):
            lam = rng.uniform(-2, 1.4); x = rng.uniform(0.0, 0.6)
            Q = np.block([[(1 - lam) * np.eye(B.shape[1]), np.sqrt(x) * B.T], [np.sqrt(x) * B, (2 - lam) * np.eye(B.shape[0])]])
            pos = np.linalg.eigvalsh(Q).min() > 1e-9
            ms = np.array([E[0] for q, E in by[2]]); dm = 1 - ms * (ms + 1) / C
            crit = (lam < 1) and ((1 - lam) * (2 - lam) - 4 * x * dm.max() > 1e-9)
            crit_neg = (lam >= 1) or ((1 - lam) * (2 - lam) - 4 * x * dm.max() < -1e-9)
            tested += 1
            if crit and not pos or (crit_neg and pos):
                bad += 1
    check("(s8) the eliminated block Q is positive definite exactly when lam < 1 and (1 - lam)(2 - lam) > 4 x max d_m (1600 random (lam, x) over S = 2, 4, 8, 12; FLOATING POINT eigenvalues)", bad == 0, f"{bad} disagreements in {tested} tests")
    if bad:
        FIRED.append("positivity criterion for the eliminated block disagrees with the eigenvalues")
    # ---- control: the literal comparison must be able to fail (a shifted d_m in the Z formula, and 4I - 4n^2/(C+1) for A*A)
    S = 3; C = S * (S + 1)
    by, A, B = build(S)
    o0 = sorted(range(len(by[0])), key=lambda i: by[0][i][1][0]); o2 = sorted(range(len(by[2])), key=lambda i: by[2][i][1][0])
    Ao = A[:, o0]; Bo = B[o2, :]
    ns = list(range(-S, S + 1)); ms = list(range(-S, S))
    dd = lambda m: sp.Integer(1) - sp.Rational(m * (m + 1), C)
    Zw = sp.zeros(len(ms), len(ns))
    for jn, n in enumerate(ns):
        for m_, dm_ in ((n - 1, dd(n)), (n, dd(n - 1))):                 # shifted: the two d's exchanged
            if m_ in ms:
                Zw[ms.index(m_), jn] += 2 * dm_
    AAw = sp.diag(*[sp.Integer(4) - sp.Rational(4 * n * n, C + 1) for n in ns])
    ctrl_ok = sp.simplify(Bo * Ao - Zw) != sp.zeros(len(ms), len(ns)) and sp.simplify(Ao.T * Ao - AAw) != sp.zeros(len(ns), len(ns))
    check("(control) the literal comparisons fail for a shifted Z formula and for 4I - 4n^2/(C + 1) (S = 3): the test discriminates", ctrl_ok, "")
    if not ctrl_ok:
        FIRED.append("the comparison does not discriminate (control did not fail)")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: STEP FAILS: " + FIRED[0])
        print("HIT: PR #9351 proof step fails when executed literally: " + "; ".join(FIRED))
        sys.exit(1)
    print("SUMMARY: pattern has no purchase on this note: every block identity of the exact reduction (state counts, A*A, the Z formula, the four reverse weights and BB*, 0 <= d <= 1, the rotor-order identities, Z*Z, the positivity "
          "criterion of the eliminated block) holds literally when A and B are built by enumerating states and hops")


if __name__ == "__main__":
    run()
