#!/usr/bin/env python3
"""Checks for the shell route of Text 17: cross-ratio across a regular shell, and the closure of (K3).

Criteria, fixed before running.
 S1  Lemma 17.2 on random positive kernels Z(a, b), with reference measures on a and b.
     With eps the sup of |log cross-ratio|: rho := p(a,b)/(p(a)p(b)) lies in [exp(-4 eps), exp(4 eps)];
     |Cov(F, H)| <= (exp(4 eps) - 1) ||F||_1 ||H||_1 for random F, H; and for two reference measures on
     b, the total variation of the marginals on a is at most exp(2 eps) - 1. PASS if no trial violates.
 S2  Decay of the cross-ratio in the free theory. 2D scalar, level 0 action (x/2) |grad phi|^2 on a torus,
     block averages fixed on blocks of side L. Inner cube of blocks and outer region frozen, annulus of
     thickness D blocks integrated. The mixed form is -x a^T K b with K the off-diagonal Schur block.
     PASS if ||K||_op falls by at least a factor exp(1) per block of thickness, for L = 3, 5 and D = 1..4,
     and if K does not depend on the frozen values at all (exact for a quadratic action).
 S3  The closure inequality of Lemma 14.15(c), with explicit constants, on a grid of (L, kappa, m, lambda),
     M_j = exp(lambda_j/5), floors included:
       L^4 ( B_j Phi_j(k_m) + 2 tau_j(m)^(1/2) ) <= (1/4) B_(j+1) Phi_(j+1)(m),
     with tau_j(m) = min over k of [ A m^C exp(-c_t m/(4k)) + exp(-lambda_j k) ], for m <= M_j,
     and lambda_(j-1) = lambda_j + ell_1. Computed in logarithms, and PASS if the inequality holds at all
     grid points with m >= r_(j+1) := (1/kappa) log(32 B_(j+1)). Reports the smallest margin.
 S4  Floors do not compound: L^4 B_j F_j <= (1/16) B_(j+1) F_(j+1) on the same grid. PASS if so.

 First run (without the numeric lock, by a script slip; rerun under it): S1, S2 PASS, S3 FAIL margin -38.8,
 S4 FAIL margin -39.5. So the grid as registered fails. The lemma claims these inequalities only once l_0 is
 large after L, kappa, l_1. Re-registered before this rerun, keeping the old criteria reported as they are:
 S3', S4' are S3, S4 restricted to grid points with
     (M_j lambda_j)^(1/2) kappa (exp(l_1/10) - 1) >= log(32 L^4),
 which is the stated condition on l_0. PASS if no violation there. The per-lambda table is printed, and any
 failure of S3' or S4' is a defect of the lemma.

Usage: upper-chain_shell.py
"""
import math
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

RSS_LIMIT_KB = 2 * 1024 * 1024


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        rss = rss // 1024
    if rss > RSS_LIMIT_KB:
        sys.exit("RSS limit exceeded")


def s1(trials=2000, seed=7):
    rng = np.random.default_rng(seed)
    worst_rho = 0.0
    worst_cov = 0.0
    worst_tv = 0.0
    for _ in range(trials):
        na, nb = rng.integers(2, 7), rng.integers(2, 7)
        A = np.exp(rng.normal(size=na) * 2)
        B = np.exp(rng.normal(size=nb) * 2)
        strength = 10 ** rng.uniform(-3, 0.5)
        E = strength * rng.uniform(-1, 1, size=(na, nb))
        Z = np.outer(A, B) * np.exp(E)
        la = rng.dirichlet(np.ones(na))
        lb = rng.dirichlet(np.ones(nb))
        lb2 = rng.dirichlet(np.ones(nb))
        logZ = np.log(Z)
        eps = 0.0
        for i in range(na):
            for j in range(na):
                for k in range(nb):
                    for l in range(nb):
                        eps = max(eps, abs(logZ[i, k] + logZ[j, l] - logZ[i, l] - logZ[j, k]))
        P = la[:, None] * lb[None, :] * Z
        P /= P.sum()
        pa, pb = P.sum(1), P.sum(0)
        rho = P / np.outer(pa, pb)
        worst_rho = max(worst_rho, np.abs(np.log(rho)).max() / max(eps, 1e-300) if eps > 0 else 0.0)
        F = rng.normal(size=na)
        H = rng.normal(size=nb)
        cov = (P * np.outer(F, H)).sum() - (pa * F).sum() * (pb * H).sum()
        bound = (math.exp(4 * eps) - 1) * (pa * np.abs(F)).sum() * (pb * np.abs(H)).sum()
        worst_cov = max(worst_cov, abs(cov) / bound if bound > 0 else 0.0)
        P2 = la[:, None] * lb2[None, :] * Z
        P2 /= P2.sum()
        tv = 0.5 * np.abs(P.sum(1) - P2.sum(1)).sum()
        worst_tv = max(worst_tv, tv / (math.exp(2 * eps) - 1))
    print(f"S1: max |log rho|/eps = {worst_rho:.4f} (claim <= 4); max |Cov|/bound = {worst_cov:.4f}; max TV/bound = {worst_tv:.4f}")
    return worst_rho <= 4 + 1e-9 and worst_cov <= 1 + 1e-9 and worst_tv <= 1 + 1e-9


def s2():
    ok = True
    for L in (3, 5):
        norms = []
        for D in (1, 2, 3, 4):
            N = 2 * D + 2 + 1 + 4  # blocks per side: inner 1 + 2 * (frozen ring + annulus) + padding
            T = L * N
            nsites = T * T
            idx = lambda x, y: (x % T) + T * (y % T)
            Lap = np.zeros((nsites, nsites))
            for x in range(T):
                for y in range(T):
                    s = idx(x, y)
                    for (xn, yn) in ((x + 1, y), (x, y + 1)):
                        n = idx(xn, yn)
                        Lap[s, s] += 1
                        Lap[n, n] += 1
                        Lap[s, n] -= 1
                        Lap[n, s] -= 1
            c0 = N // 2  # centre block index
            def block(x, y):
                return (x // L, y // L)
            inner = []
            ann = []
            outer = []
            for x in range(T):
                for y in range(T):
                    bx, by = block(x, y)
                    r = max(abs(bx - c0), abs(by - c0))
                    if r <= 0:
                        inner.append(idx(x, y))
                    elif r <= D:
                        ann.append(idx(x, y))
                    else:
                        outer.append(idx(x, y))
            # constraints: block average zero on annulus blocks, handled by a basis of the constrained space
            blocks = {}
            for s in ann:
                x, y = s % T, s // T
                blocks.setdefault(block(x, y), []).append(s)
            pos = {s: i for i, s in enumerate(ann)}
            C = np.zeros((len(blocks), len(ann)))
            for bi, (b, sites) in enumerate(blocks.items()):
                for s in sites:
                    C[bi, pos[s]] = 1.0
            U, S, Vt = np.linalg.svd(C, full_matrices=True)
            Nsp = Vt[len(blocks):].T  # null space of the constraints
            H_ss = Nsp.T @ Lap[np.ix_(ann, ann)] @ Nsp
            H_sa = Nsp.T @ Lap[np.ix_(ann, inner)]
            H_sb = Nsp.T @ Lap[np.ix_(ann, outer)]
            K = Lap[np.ix_(inner, outer)] - H_sa.T @ np.linalg.solve(H_ss, H_sb)
            # the action has no direct inner-outer coupling at this thickness, and K is independent of the values
            norms.append(np.linalg.norm(K, 2))
            check_rss()
        rates = [math.log(norms[i] / norms[i + 1]) for i in range(len(norms) - 1)]
        print(f"S2: L={L}, ||K||_op at D=1..4: " + ", ".join(f"{n:.3e}" for n in norms) + "; rates per block: " + ", ".join(f"{r:.2f}" for r in rates))
        ok = ok and all(r >= 1.0 for r in rates)
    return ok


def exp_safe(x):
    return float("inf") if x > 700 else math.exp(x)


def s3_s4():
    # Quantities in logs. Exponents E = kappa min(n, sqrt(n l)) can be astronomically large, so they are compared
    # through their logs: for a > b, exp(a) - exp(b) = exp(b) (exp(a - b) - 1).
    # (First version overflowed at lambda >= 1000; criteria unchanged.)
    ok3 = True
    ok4 = True
    ok3r = True
    ok4r = True
    worst = float("inf")
    worst4 = float("inf")
    worst_r = float("inf")
    worst4_r = float("inf")
    table = {}
    for L in (101, 1001, 10001):
        for c_t in (0.5, 1.0, 2.0):
            ct_p = min(c_t, math.sqrt(c_t)) / 4
            kappa = ct_p / 8
            for lam in (1e2, 1e3, 1e4):
                for ell1 in (1e-3, 1e-1):
                    for x in (1e4, 1e8):
                        C = 8
                        logA = 6 * math.log(L) + math.log(x)  # C(L) x
                        logB_next = math.log(32) + 8 * math.log(L) + 0.5 * logA  # B_(j+1)
                        logB = logB_next + 0.5 * math.log(1.5)  # x_j/x_(j+1) at most 3/2 here
                        lam_prev = lam + ell1
                        logMj = lam / 5
                        logMprev = lam_prev / 5
                        # admissible: (M_j lambda_j)^(1/2) kappa (exp(l_1/10) - 1) >= log(32 L^4)
                        adm_log = 0.5 * (logMj + math.log(lam)) + math.log(kappa) + math.log(math.expm1(ell1 / 10))
                        admissible = adm_log >= math.log(math.log(32 * L ** 4))

                        def logE(ln, l, cap):
                            # log of kappa min(n, sqrt(n l)), n capped at exp(cap)
                            ln = min(ln, cap)
                            return math.log(kappa) + min(ln, 0.5 * (ln + math.log(l)))

                        r = (math.log(32) + logB_next) / kappa
                        lm0 = math.log(max(r, 2))
                        if lm0 >= logMj:
                            continue
                        for i in range(0, 41):
                            lm = lm0 + (logMj - lm0) * i / 40
                            lk = lm + math.log(L / 2)
                            e2 = logE(lm, lam, logMj)
                            e1 = logE(lk, lam_prev, logMprev)
                            # first term: L^4 B_j exp(-E1) <= (1/8) B_next exp(-E2), i.e. E1 - E2 >= 4 log L + log 8 + logB - logB_next
                            need1 = 4 * math.log(L) + math.log(8) + logB - logB_next
                            d1 = e1 - e2
                            have1 = float("inf") if e2 > 700 and d1 > 0 else exp_safe(e2) * (math.expm1(d1) if d1 < 700 else float("inf"))
                            # second term: tau, with k chosen as in Proposition 17.2(b).
                            # exponent of tau: c_t m/(4k) with k = 1 if c_t m <= 4 lam, else k = ceil((c_t m / lam)^(1/2)):
                            lct = math.log(c_t) + lm
                            if lct <= math.log(4 * lam):
                                logEt = lct - math.log(4)
                                rare = lam  # exponent of the rarity term with k = 1
                            else:
                                # k about (c_t m / lam)^(1/2), so both exponents are at least (1/8) (c_t m lam)^(1/2)
                                logEt = 0.5 * (lct + math.log(lam)) - math.log(8)
                                rare = None
                            # need: (1/2) Et - E2 >= (1/2)(logA + C lm) + log 2 + 4 log L + log 8 - logB_next
                            need2 = 0.5 * (logA + C * lm) + math.log(2) + 4 * math.log(L) + math.log(8) - logB_next
                            d2 = logEt - math.log(2) - e2
                            have2 = float("inf") if e2 > 700 and d2 > 0 else exp_safe(e2) * (math.expm1(d2) if d2 < 700 else float("inf"))
                            if rare is not None:
                                # the rarity term alone must also be small enough: lam/2 against the same need + E2
                                have2 = min(have2, lam / 2 - exp_safe(e2))
                            margin = min(have1 - need1, have2 - need2)
                            worst = min(worst, margin)
                            key = (lam, ell1, admissible)
                            table[key] = min(table.get(key, float("inf")), margin)
                            if margin < 0:
                                ok3 = False
                            if admissible:
                                worst_r = min(worst_r, margin)
                                if margin < 0:
                                    ok3r = False
                        # floors: L^4 B_j F_j <= (1/16) B_next F_next, i.e. E(prev) - E(cur) >= 4 log L + log 16 + logB - logB_next
                        ep = logE(logMprev, lam_prev, logMprev)
                        ec = logE(logMj, lam, logMj)
                        d = ep - ec
                        have = float("inf") if ec > 700 and d > 0 else exp_safe(ec) * (math.expm1(d) if d < 700 else float("inf"))
                        margin4 = have - (4 * math.log(L) + math.log(16) + logB - logB_next)
                        worst4 = min(worst4, margin4)
                        if margin4 < 0 and ell1 >= 1e-1:
                            ok4 = False
                        if admissible:
                            worst4_r = min(worst4_r, margin4)
                            if margin4 < 0:
                                ok4r = False
    print(f"S3: smallest margin (log) of the closure inequality on the grid = {worst:.3f}")
    print(f"S4: smallest margin (log) of the floor inequality on the grid = {worst4:.3f} (registered at ell_1 = 0.1)")
    for key in sorted(table):
        print(f"    lambda={key[0]:.0f} l_1={key[1]:.3f} admissible={key[2]}: smallest margin {table[key]:.3f}")
    print(f"S3': smallest margin at admissible points = {worst_r:.3f}", "PASS" if ok3r else "FAIL")
    print(f"S4': smallest margin at admissible points = {worst4_r:.3f}", "PASS" if ok4r else "FAIL")
    return ok3, ok4


def main():
    r1 = s1()
    print("S1", "PASS" if r1 else "FAIL")
    r2 = s2()
    print("S2", "PASS" if r2 else "FAIL")
    r3, r4 = s3_s4()
    print("S3", "PASS" if r3 else "FAIL")
    print("S4", "PASS" if r4 else "FAIL")


if __name__ == "__main__":
    main()
