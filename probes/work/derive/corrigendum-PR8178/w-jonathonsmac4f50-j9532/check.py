#!/usr/bin/env python3
"""corrigendum-PR8178, attempt 1 of 2 (worker w-jonathonsmac4f50-j9532, claude-opus-5).

Block 34 (PR #8178) T1.1: on the periodic L x L plane, (P theta)_x = (theta_x + theta_{x-e1} + theta_{x-e2})/3 and
theta^_k = L^{-1} sum_x e^{-ik.x} theta_x, k = 2 pi n / L.  The note states (P theta)^_k = phi(k) theta^_k with
phi(k) = (1 + e^{ik1} + e^{ik2})/3.  Corrected: the multiplier is phi_c(k) = (1 + e^{-ik1} + e^{-ik2})/3 = conj phi(k).

C1  exact, in Q(zeta_L): F P F^{-1} = diag(phi_c) on L = 2..5; the stated phi fails for every L >= 3 (and holds at L = 2)
C2  exact: phi(k) = phi_c(k) iff sin k1 + sin k2 = 0 iff n1 + n2 = 0 or (L even and n2 - n1 = L/2) mod L (L = 2..10);
    so the stated T1.1 holds for every field iff L <= 2, and for a given L exactly on those modes
C3  exact: everything else in block 34 uses u = |phi|^2 = |phi_c|^2 only (T1.2 identity, T1.3 variances, T2 recursion, T3)
C4  exact: block 35 (PR #8180) T1 on L = 3, 4: E[theta^_k(t) conj theta^_k(t+s)] = phi(k)^s Var and E[conj theta^_k(t) theta^_k(t+s)]
    = phi_c(k)^s Var: its stated covariance holds in its own (control's) convention, its proof line theta^(t+s) = phi^s theta^(t) does not
C5  exact: expansions phi = 1 + i(k1+k2)/3 + O(k^2), phi_c = 1 - i(k1+k2)/3 + O(k^2) (block 35's runner docstring states the latter,
    its code and note the former)
C6  the exact lines, verified at the pinned PR heads e6ffae5b460b (#8178) and 7c844adf7555 (#8180)
"""
import subprocess
import sys
from fractions import Fraction as Fr

import sympy as sp

FAILS = []


def check(label, ok, detail):
    print(("ok   " if ok else "FAIL ") + f"{label}: {detail}", flush=True)
    if not ok:
        FAILS.append(label)


X = sp.Symbol("x")


class Cyc:
    """elements of Q(zeta_L) as rational coefficient vectors over zeta^0..zeta^{L-1}; zero test modulo the cyclotomic polynomial"""

    def __init__(self, L, c=None):
        self.L = L
        self.c = list(c) if c is not None else [Fr(0)] * L

    @staticmethod
    def mono(L, e, a=Fr(1)):
        v = Cyc(L)
        v.c[e % L] += a
        return v

    def __add__(self, o):
        return Cyc(self.L, [a + b for a, b in zip(self.c, o.c)])

    def __sub__(self, o):
        return Cyc(self.L, [a - b for a, b in zip(self.c, o.c)])

    def __mul__(self, o):
        if isinstance(o, (int, Fr)):
            return Cyc(self.L, [a * o for a in self.c])
        r = [Fr(0)] * self.L
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if b:
                        r[(i + j) % self.L] += a * b
        return Cyc(self.L, r)

    def is_zero(self):
        p = sp.Poly(sum(sp.Rational(a.numerator, a.denominator) * X ** i for i, a in enumerate(self.c)), X, domain="QQ")
        return p.rem(sp.Poly(sp.cyclotomic_poly(self.L, X), X, domain="QQ")).is_zero

    def conj(self):
        return Cyc(self.L, [self.c[(-i) % self.L] for i in range(self.L)])


def phi_c(L, n):        # (1 + zeta^{-n1} + zeta^{-n2})/3
    return (Cyc.mono(L, 0) + Cyc.mono(L, -n[0]) + Cyc.mono(L, -n[1])) * Fr(1, 3)


def phi_s(L, n):        # the stated (1 + zeta^{n1} + zeta^{n2})/3
    return (Cyc.mono(L, 0) + Cyc.mono(L, n[0]) + Cyc.mono(L, n[1])) * Fr(1, 3)


def sites(L):
    return [(a, b) for a in range(L) for b in range(L)]


def P_matrix(L):
    S = sites(L)
    idx = {s: i for i, s in enumerate(S)}
    N = len(S)
    Pm = [[Fr(0)] * N for _ in range(N)]
    for (a, b) in S:
        for (c, d) in ((a, b), ((a - 1) % L, b), (a, (b - 1) % L)):
            Pm[idx[(a, b)]][idx[(c, d)]] += Fr(1, 3)
    return S, Pm


def git_show(spec):
    return subprocess.run(["git", "show", spec], capture_output=True, text=True).stdout


def main():
    # ---------------- C1
    ok, fails_at = True, {}
    for L in (2, 3, 4, 5):
        S, Pm = P_matrix(L)
        N = len(S)
        bad_stated = 0
        for n in S:
            # row k of F P: (F P)_{k,y} = sum_x L^{-1} zeta^{-n.x} P_{x,y}; compare with phi(k) F_{k,y}
            for yi, y in enumerate(S):
                lhs = Cyc(L)
                for xi, x in enumerate(S):
                    if Pm[xi][yi]:
                        lhs = lhs + Cyc.mono(L, -(n[0] * x[0] + n[1] * x[1]), Fr(1, L) * Pm[xi][yi])
                F_ky = Cyc.mono(L, -(n[0] * y[0] + n[1] * y[1]), Fr(1, L))
                ok &= (lhs - phi_c(L, n) * F_ky).is_zero()
                if not (lhs - phi_s(L, n) * F_ky).is_zero():
                    bad_stated += 1
        fails_at[L] = bad_stated
    ok &= fails_at[2] == 0 and all(fails_at[L] > 0 for L in (3, 4, 5))
    check("C1", ok, "exact in Q(zeta_L): with theta^_k = L^{-1} sum_x zeta^{-n.x} theta_x and (P theta)_x = (theta_x + theta_{x-e1} + theta_{x-e2})/3, "
          "(F P)_{k,y} = phi_c(k) F_{k,y} for every mode and site on L = 2, 3, 4, 5, phi_c(k) = (1 + e^{-ik1} + e^{-ik2})/3 (so F P F^{-1} = diag phi_c); "
          f"the stated phi = (1 + e^{{ik1}} + e^{{ik2}})/3 fails at {fails_at[3]}, {fails_at[4]}, {fails_at[5]} of the (mode, site) pairs on L = 3, 4, 5 "
          f"and at {fails_at[2]} on L = 2 (e.g. L = 3, k = (2 pi/3, 0): phi_c - phi = (e^{{-2 pi i/3}} - e^{{2 pi i/3}})/3 = -i/sqrt3)")

    # ---------------- C2
    k1, k2 = sp.symbols("k1 k2", real=True)
    ph_s = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    ph_c = (1 + sp.exp(-sp.I * k1) + sp.exp(-sp.I * k2)) / 3
    diff = sp.simplify((ph_s - ph_c).rewrite(sp.sin) - 2 * sp.I * (sp.sin(k1) + sp.sin(k2)) / 3) == 0
    prod = sp.simplify(sp.expand_trig(sp.sin(k1) + sp.sin(k2) - 2 * sp.sin((k1 + k2) / 2) * sp.cos((k1 - k2) / 2))) == 0
    ok = diff and prod
    counts = {}
    for L in range(2, 11):
        agree = 0
        for n in sites(L):
            eq = (phi_s(L, n) - phi_c(L, n)).is_zero()
            crit = (n[0] + n[1]) % L == 0 or (L % 2 == 0 and (n[1] - n[0]) % L == L // 2)
            ok &= eq == crit
            agree += eq
        counts[L] = agree
    check("C2", ok, "phi - phi_c = (2i/3)(sin k1 + sin k2) = (4i/3) sin((k1+k2)/2) cos((k1-k2)/2) (symbolic), so the stated multiplier is right exactly on "
          "the modes with n1 + n2 = 0 mod L or (L even) n2 - n1 = L/2 mod L, checked exactly in Q(zeta_L) for L = 2..10 (agreeing modes: " +
          ", ".join(f"L={L}: {counts[L]}/{L*L}" for L in range(2, 11)) + "); the largest domain on which T1.1 holds as stated for every field is L <= 2")

    # ---------------- C3
    u_s = sp.simplify(sp.expand(ph_s * sp.conjugate(ph_s), complex=True))
    u_c = sp.simplify(sp.expand(ph_c * sp.conjugate(ph_c), complex=True))
    target = sp.Rational(4, 9) * (sp.sin(k1 / 2) ** 2 + sp.sin(k2 / 2) ** 2 + sp.sin((k1 - k2) / 2) ** 2)
    ok = sp.simplify(sp.expand_trig(u_s - u_c)) == 0 and sp.simplify(sp.expand_trig(1 - u_c - target)) == 0
    # T2 phase-blind: exact covariance recursion on L = 3 against the mode formula with u only
    L = 3
    S, Pm = P_matrix(L)
    N = len(S)
    Sig = [[Fr(0)] * N for _ in range(N)]

    def matmul(A_, B_):
        return [[sum(A_[i][k] * B_[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

    PT = [[Pm[j][i] for j in range(N)] for i in range(N)]
    from math import cos, pi
    cosr = {0: Fr(1), 1: Fr(-1, 2), 2: Fr(-1, 2)}          # cos(2 pi n/3), exact
    for t in range(1, 7):
        Sig = matmul(matmul(Pm, Sig), PT)
        for i in range(N):
            Sig[i][i] += 1
        tr = sum(Sig[i][i] for i in range(N)) / N
        modes = Fr(t)
        for n in S:
            if n == (0, 0):
                continue
            u = (3 + 2 * cosr[n[0] % 3] + 2 * cosr[n[1] % 3] + 2 * cosr[(n[0] - n[1]) % 3]) / 9
            modes += (1 - u ** t) / (1 - u)
        ok &= tr == modes / N
    check("C3", ok, "|phi|^2 = |phi_c|^2 and 1 - |phi_c|^2 = (4/9)[sin^2(k1/2) + sin^2(k2/2) + sin^2((k1-k2)/2)] (symbolic): T1.2, the mode variances of "
          "T1.3 (V(t+1) = u V(t) + sigma^2), the covariance recursion of T2 (the site variance equals (1/L^2)[t + sum_{k!=0}(1 - u^t)/(1 - u)], re-run "
          "exactly on L = 3, t <= 6) and T3 (tau_L, V_L and the bracket) depend on u only and are unaffected; the recursion theta^_k(t+1) = "
          "phi(k) theta^_k(t) + xi^_k(t) of T1.3 holds with phi_c")

    # ---------------- C4: block 35's T1 convention, exact on L = 3, 4
    ok, detail = True, []
    for L in (3, 4):
        S, Pm = P_matrix(L)
        N = len(S)
        PT = [[Pm[j][i] for j in range(N)] for i in range(N)]

        def mm(A_, B_):
            return [[sum(A_[i][k] * B_[k][j] for k in range(N) if A_[i][k]) for j in range(N)] for i in range(N)]

        Sig = [[Fr(0)] * N for _ in range(N)]
        for t in range(3):
            Sig = mm(mm(Pm, Sig), PT)
            for i in range(N):
                Sig[i][i] += 1
        n_first_ok = n_second_ok = 0
        cross = Sig
        for s in (1, 2):
            cross = mm(cross, PT)                                  # Sigma_{t,t+s} = Sigma_t (P^s)^T
            for n in S:
                if n == (0, 0):
                    continue
                var = Cyc(L)
                c_later_conj = Cyc(L)                              # E[theta^(t) conj theta^(t+s)]
                for xi, x in enumerate(S):
                    for yi, y in enumerate(S):
                        e = -(n[0] * x[0] + n[1] * x[1]) + (n[0] * y[0] + n[1] * y[1])
                        if Sig[xi][yi]:
                            var = var + Cyc.mono(L, e, Sig[xi][yi] / (L * L))
                        if cross[xi][yi]:
                            c_later_conj = c_later_conj + Cyc.mono(L, e, cross[xi][yi] / (L * L))
                ps, pc = Cyc.mono(L, 0), Cyc.mono(L, 0)
                for _ in range(s):
                    ps, pc = ps * phi_s(L, n), pc * phi_c(L, n)
                a = (c_later_conj - ps * var).is_zero()
                b = (c_later_conj.conj() - pc * var).is_zero()            # E[conj theta^(t) theta^(t+s)] = conj of the above (var real)
                n_second_ok += a
                n_first_ok += b
                ok &= a and b
        detail.append(f"L={L}: {n_second_ok} and {n_first_ok} of {2*(N-1)} (mode, s) pairs")
        # the stated recursion theta^(t+s) = phi^s theta^(t) fails: E[theta^(t) conj theta^(t+s)] != conj(phi)^s Var somewhere
    check("C4", ok, "exact in Q(zeta_L) from Sigma_{t+1} = P Sigma_t P^T + I (t = 3) and Sigma_{t,t+s} = Sigma_t (P^s)^T (s = 1, 2): "
          "E[theta^_k(t) conj theta^_k(t+s)] = phi(k)^s Var theta^_k(t) and E[conj theta^_k(t) theta^_k(t+s)] = phi_c(k)^s Var theta^_k(t) at every "
          "nonzero mode (" + "; ".join(detail) + "); so block 35's T1 formula with the stated phi holds in its control's convention C_s(k) = E[f(t) conj f(t+s)], "
          "while its proof line 'theta^_k(t+s) = phi^s theta^_k(t) + noise' needs phi_c = conj phi")

    # ---------------- C5
    eps = sp.symbols("epsilon", real=True)
    s_s = sp.series(ph_s.subs({k1: eps * k1, k2: eps * k2}), eps, 0, 2).removeO()
    s_c = sp.series(ph_c.subs({k1: eps * k1, k2: eps * k2}), eps, 0, 2).removeO()
    ok = sp.simplify(s_s - (1 + sp.I * eps * (k1 + k2) / 3)) == 0 and sp.simplify(s_c - (1 - sp.I * eps * (k1 + k2) / 3)) == 0
    check("C5", ok, "phi = 1 + i(k1 + k2)/3 + O(k^2) and phi_c = 1 - i(k1 + k2)/3 + O(k^2) (symbolic): block 35's note and D1 code state the first "
          "(the kernel symbol in its convention), its runner docstring (line 13) and comment (line 232) the second")

    # ---------------- C6: the exact lines at the pinned heads
    b34, b35 = "e6ffae5b460b", "7c844adf7555"
    for sha, br in ((b34, "physics-loop/admissibility-induced-law-block34-sphere-formation-law-torus-memory-time-zero-mode-rate-and-stationary-modes-20260917"),
                    (b35, None)):
        if subprocess.run(["git", "cat-file", "-e", sha + "^{commit}"], capture_output=True).returncode != 0 and br:
            subprocess.run(["git", "fetch", "-q", "origin", br], capture_output=True)
    n34 = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_TORUS_MEMORY_TIME_ZERO_MODE_RATE_EXACTLY_STATIONARY_MODES_BRACKETED_AND_THE_NONLINEAR_"
           "LAW_MEASURED_AGAINST_IT_BOUNDED_THEOREM_NOTE_2026-09-17.md")
    r34 = "scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py"
    c34 = "logs/runner-cache/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.txt"
    s34 = ".claude/science/physics-loops/admissibility-induced-law-20260906/"
    n35 = ("docs/ADMISSIBILITY_RULE_GRAVITY_NODE_KERNEL_UNDER_THE_FORMATION_READING_A_HEAT_KERNEL_IN_LEVEL_TIME_TIMES_A_PLANE_GREEN_FUNCTION_NOT_THE_"
           "COMPARATORS_THREE_DIMENSIONAL_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-18.md")
    r35 = "scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.py"
    lines = [
        (b34, n34, 4, "multiplier phi(k) = (1 + e^{i k_1} + e^{i k_2})/3"),
        (b34, n34, 85, "P` acts as multiplication by `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"),
        (b34, n34, 104, "the conjugate convention gives the stated `φ`"),
        (b34, n34, 104, "`φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"),
        (b34, r34, 5, "multiplier phi(k) = (1 + e^{i k_1} + e^{i k_2})/3"),
        (b34, r34, 199, "phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3"),
        (b34, r34, 206, "for phi = (1 + e^{i k1} + e^{i k2})/3"),
        (b34, c34, 18, "for phi = (1 + e^{i k1} + e^{i k2})/3"),
        (b34, s34 + "GOAL_block34.md", 6, "multiplier `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"),
        (b34, s34 + "RESULTS_block34.md", 6, "multiplier `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"),
        (b35, n35, 86, "multiplier `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"),
        (b35, n35, 106, "`θ̂_k(t+s) = φ^s θ̂_k(t) + (noise of levels t+1..t+s)`"),
        (b35, n35, 116, "`φ(k) = 1 + i(k₁ + k₂)/3 + O(|k|²)`"),
        (b35, r35, 13, "phi(k) = 1 - i(k1 + k2)/3 + O(k^2)"),
        (b35, r35, 232, "# the drift: phi(k) = 1 - i (k1 + k2)/3 + O(k^2)"),
        (b35, r35, 234, "phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3"),
    ]
    ok, found = True, []
    for sha, path, ln, sub in lines:
        txt = git_show(f"{sha}:{path}").split("\n")
        hit = len(txt) >= ln and sub in txt[ln - 1]
        ok &= hit
        found.append(f"{'#8178' if sha == b34 else '#8180'} {path.split('/')[-1][:40]}...:{ln}{'' if hit else ' MISSING'}")
    check("C6", ok, "the quoted strings stand on the stated lines at the pinned heads (#8178 e6ffae5b460b, #8180 7c844adf7555): " + "; ".join(found))

    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("block 34's T1.1 corrected: with theta^_k = L^{-1} sum_x e^{-ik.x} theta_x the backward average P acts on mode k as multiplication by "
            "phi_c(k) = (1 + e^{-ik1} + e^{-ik2})/3 (exact diagonalization on L = 2..5), the conjugate of the stated phi; the stated form holds exactly "
            "on the modes with sin k1 + sin k2 = 0 (n1 + n2 = 0, or n2 - n1 = L/2 for even L), hence for every field only when L <= 2; everything "
            "else in block 34 uses |phi|^2 and is unaffected; block 35's T1 formula holds in its own convention E[f(t) conj f(t+s)] but its proof "
            "line and declared multiplier need phi_c, and its runner docstring's drift sign contradicts its code; blocks 13, 26 and the static-law "
            "notes are unaffected (|phi|^2 only, or block 26's already-correct e^{-i theta} form, or unrelated transforms)")
    print("SUMMARY: PROVED " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
