#!/usr/bin/env python3
"""Closure of (K3) with the second tier of (MD_j) on hard-core--mapped. Text 21.7 of parts/upper-chain.md.

That file's bound reads eps_j <= C(L) x_j |A|^C ( exp(-c_t D) + z_j^(1/2) exp(-c_s D) ), with c_t absolute and c_s(L) a
negative power of L, about 0.1 L^(-5/2) at d = 2 by its numerics. The question: must the class's rate kappa come down
to about c_s^(1/2), which would break kappa L >> log L, or does a two-tier profile close with kappa absolute?

Profile. g_j(n) := min(n', (n' lambda_j)^(1/2)), n' := min(n, M_j), M_j := exp(lambda_j / 5), and
    Phi_j(n) := exp(-kappa g_j(n)) + zeta_j exp(-kappa_s g_j(n)),  zeta_j := exp(-C_Z lambda_j),
kappa := min(c_t, c_t^(1/2)) / 32, kappa_s := min(c_s / 16, c_s / (32 kappa)).
Inequality, with k_m := floor(m L / 2), B_j := C_B x_j^(1/2), r' := (1/kappa) log(32 B'), for r' <= m <= M':
    L^4 ( 4 B_j Phi_j(k_m) + C_1 tau_j(m)^(1/2) ) <= (1/4) B' Phi'(m),
    tau_j(m) := inf_k { C(L) x_j m^C ( exp(-c_t m/(4k)) + z_j^(1/2) exp(-c_s m/(4k)) ) + exp(-lambda' k) + C m^4 exp(-lambda_j m/(40 k)) }.

First registration, written before the first run: zeta_j = z_j^(1/4).
T1: the inequality holds at every grid point meeting the floor conditions below, with L in {5, 9, 15, 25}, lambda' in
    {100, 200, 400, 600}, l_1 in {0.01, 0.1}, C_Z in {1, 2}, c_t = 1, c_s = 0.1 L^(-5/2), C = 8, C(L) = L^8, C_B = L^10,
    C_1 = 10, x_j = 100 lambda_j. Floors: (M' lambda')^(1/2) kappa (exp(l_1/10) - 1) >= log(16 L^4), and the same with kappa_s.
T2: the single-tier profile, Phi_j(n) := exp(-kappa g_j(n)), FAILS the inequality at some admissible point.
T3: C_Z = 1 is enough: T1 holds at C_Z = 1 alone.
First run: T1 FAILED, smallest log margin -54.137. T3 FAILED, -51.331. T2 PASS, one-tier margin -8.4e25.

Diagnosis, by hand, after that run. (i) With zeta = z^(1/4) the source has exactly the profile's power of z, so nothing is
left to absorb m^(C/2), and max_m m^4 exp(-kappa_s g(m)) is exp(4 log(64 / (kappa_s^2 lambda)) - 8). (ii) For
m_c <= m <= m_1 the profile is in its second tier and the gain of k_m has not started: L^4 zeta exp(-kappa_s g_j(k_m)) is
above zeta exp(-kappa_s g'(m)) by up to 16 L^4. So the crossing m_c, where kappa g'(m_c) = log(1 / zeta), must lie beyond m_1.

Second registration, written before the second run: zeta_j := z_j^(1/8), and
    ell := log(64 L^4 (x_j / x')^(1/2)), Lambda_*(L) := kappa ell / (kappa_s ((L/2)^(1/2) - 1)),
    (TT) log(1 / zeta') >= ell + 2 Lambda_* + 4 log(64 / (kappa_s^2 lambda')) .
T1': on the same grid and floors, with C_Z := (right side of (TT)) / lambda', the inequality holds at every m on a log grid
    of 1500 points in [r', M'], refined by 300 points around the crossing.
T3': with C_Z := Lambda_* / (4 lambda') at the same points, the inequality FAILS somewhere, so (TT) is not an artefact of
    the proof. PASS means it fails.
Second run: T1' FAILED, smallest log margin -2.022 at (L, lambda', l_1, m) = (5, 200, 0.01, 784), which is m = r'. T3' PASS,
-10.931 at (25, 600, 0.01, 1.2e9).

Diagnosis, by hand, after that run. At L = 5, lambda' = 200, r' = 784 is above lambda', so the bottom of the range is already
stretched, and the first tier alone gives kappa (g_j(k_(r')) - g'(r')) = 7.2 against log(16 L^4) + log 4 = 9.2 + 1.4 - 1.4.
This has nothing to do with the second tier: it is a bound on L and lambda against the first tier at the start of the range.

Third registration, written before the third run: (FT) kappa (g_j(k_(r')) - g'(r')) >= log(64 L^4 (x_j / x')^(1/2)).
T1'': on the same grid and floors, restricted to points meeting (FT), with C_Z by (TT), the inequality holds at every m of the
    same log grid. At least one point must remain for each L, or this FAILS as vacuous. Margins are printed per L.
Third run: T1'' PASS, smallest log margins 3.380, 3.893, 12.292, 22.112 at L = 5, 9, 15, 25, on 2, 6, 6, 5 points.
"""
import math
import resource

import numpy as np

RSS_LIMIT_GB = 2.0


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


def lae(*xs):
    return float(np.logaddexp.reduce(np.array(xs, dtype=float)))


def g(n, lam):
    M = math.exp(lam / 5)
    np_ = min(n, M)
    return min(np_, (np_ * lam) ** 0.5)


def log_phi(n, lam, kappa, kappa_s, cz, two_tier):
    gg = g(n, lam)
    a = -kappa * gg
    if not two_tier:
        return a
    return lae(a, -cz * lam - kappa_s * gg)


def log_tau(m, lam_p, lam_j, x_j, ct, cs, log_z_half, CL, C):
    k = np.geomspace(1.0, max(1.0, m / 8), 300)
    pre = math.log(CL) + math.log(x_j) + C * math.log(m)
    t1 = pre - ct * m / (4 * k)
    t2 = pre + log_z_half - cs * m / (4 * k)
    t3 = -lam_p * k
    t4 = math.log(10) + 4 * math.log(m) - lam_j * m / (40 * k)
    tot = np.logaddexp(np.logaddexp(t1, t2), np.logaddexp(t3, t4))
    return float(tot.min())


def constants(L):
    ct, cs = 1.0, 0.1 * L ** -2.5
    kappa = min(ct, ct**0.5) / 32
    kappa_s = min(cs / 16, cs / (32 * kappa))
    return ct, cs, kappa, kappa_s


def margin(m, L, lam_p, l1, cz, two_tier, zpow):
    """zpow is the power p with z^(1/2) = zeta^p: 2 for zeta = z^(1/4), 4 for zeta = z^(1/8)."""
    ct, cs, kappa, kappa_s = constants(L)
    lam_j = lam_p + l1
    x_p, x_j = 100 * lam_p, 100 * lam_j
    CB, CL, C, C1 = float(L) ** 10, float(L) ** 8, 8.0, 10.0
    Bp, Bj = CB * x_p**0.5, CB * x_j**0.5
    km = math.floor(m * L / 2)
    log_z_half = -zpow * cz * lam_j
    lhs = 4 * math.log(L) + lae(
        math.log(4 * Bj) + log_phi(km, lam_j, kappa, kappa_s, cz, two_tier),
        math.log(C1) + 0.5 * log_tau(m, lam_p, lam_j, x_j, ct, cs, log_z_half, CL, C),
    )
    rhs = math.log(0.25 * Bp) + log_phi(m, lam_p, kappa, kappa_s, cz, two_tier)
    return rhs - lhs


def admissible(L, lam_p, l1):
    _, _, kappa, kappa_s = constants(L)
    f = (math.exp(lam_p / 5) * lam_p) ** 0.5 * (math.exp(l1 / 10) - 1)
    return f * kappa >= math.log(16 * L**4) and f * kappa_s >= math.log(16 * L**4)


def tt_terms(L, lam_p, l1):
    _, _, kappa, kappa_s = constants(L)
    ell = math.log(64 * L**4 * ((lam_p + l1) / lam_p) ** 0.5)
    lam_star = kappa * ell / (kappa_s * ((L / 2) ** 0.5 - 1))
    return ell, lam_star, 4 * math.log(64 / (kappa_s**2 * lam_p))


def grid_m(L, lam_p, n, center=None, n_center=0):
    _, _, kappa, _ = constants(L)
    rp = (1 / kappa) * math.log(32 * float(L) ** 10 * (100 * lam_p) ** 0.5)
    lo, hi = math.log(rp), lam_p / 5
    ms = np.exp(np.linspace(lo, hi, n))
    if center is not None and n_center and lo < math.log(center) < hi:
        c = math.log(center)
        ms = np.concatenate([ms, np.exp(np.linspace(max(lo, c - 3), min(hi, c + 3), n_center))])
    return ms


def first_registration():
    worst_two, worst_two_cz1, worst_one = math.inf, math.inf, math.inf
    n_adm = 0
    for L in (5, 9, 15, 25):
        for lam_p in (100.0, 200.0, 400.0, 600.0):
            for l1 in (0.01, 0.1):
                if not admissible(L, lam_p, l1):
                    continue
                n_adm += 1
                ms = grid_m(L, lam_p, 240)
                for cz in (1.0, 2.0):
                    for m in ms:
                        v = margin(float(m), L, lam_p, l1, cz, True, 2)
                        worst_two = min(worst_two, v)
                        if cz == 1.0:
                            worst_two_cz1 = min(worst_two_cz1, v)
                for m in ms:
                    worst_one = min(worst_one, margin(float(m), L, lam_p, l1, 1.0, False, 2))
    rss_guard()
    print(f"first registration, admissible points: {n_adm}")
    print(f"T1: smallest log margin, two tiers = {worst_two:.3f} (claim >= 0)")
    print(f"T2: smallest log margin, one tier = {worst_one:.4g} (claim < 0)")
    print(f"T3: smallest log margin, two tiers, C_Z = 1 = {worst_two_cz1:.3f} (claim >= 0)")
    print("T1", "PASS" if worst_two >= 0 and n_adm > 0 else "FAIL")
    print("T2", "PASS" if worst_one < 0 else "FAIL")
    print("T3", "PASS" if worst_two_cz1 >= 0 and n_adm > 0 else "FAIL")


def second_registration():
    worst, worst_low = math.inf, math.inf
    at, at_low = None, None
    n_adm = 0
    for L in (5, 9, 15, 25):
        for lam_p in (100.0, 200.0, 400.0, 600.0):
            for l1 in (0.01, 0.1):
                if not admissible(L, lam_p, l1):
                    continue
                n_adm += 1
                _, _, kappa, _ = constants(L)
                ell, lam_star, poly = tt_terms(L, lam_p, l1)
                cz = (ell + 2 * lam_star + poly) / lam_p
                g_cross = cz * lam_p / kappa
                # m at the crossing: g'(m) = g_cross, exponential regime if g_cross <= lam_p, stretched beyond
                center = g_cross if g_cross <= lam_p else g_cross**2 / lam_p
                for m in grid_m(L, lam_p, 1500, center, 300):
                    v = margin(float(m), L, lam_p, l1, cz, True, 4)
                    if v < worst:
                        worst, at = v, (L, lam_p, l1, float(m))
                cz_low = lam_star / (4 * lam_p)
                g_cross_low = cz_low * lam_p / kappa
                center_low = g_cross_low if g_cross_low <= lam_p else g_cross_low**2 / lam_p
                for m in grid_m(L, lam_p, 1500, center_low, 300):
                    v = margin(float(m), L, lam_p, l1, cz_low, True, 4)
                    if v < worst_low:
                        worst_low, at_low = v, (L, lam_p, l1, float(m))
    rss_guard()
    print(f"second registration, admissible points: {n_adm}")
    print(f"T1': smallest log margin under (TT) = {worst:.3f} at (L, lambda', l_1, m) = {at} (claim >= 0)")
    print(f"T3': smallest log margin at Lambda_*/4 = {worst_low:.3f} at {at_low} (claim < 0)")
    print("T1'", "PASS" if worst >= 0 and n_adm > 0 else "FAIL")
    print("T3'", "PASS" if worst_low < 0 else "FAIL")


def first_tier_ok(L, lam_p, l1):
    _, _, kappa, _ = constants(L)
    rp = (1 / kappa) * math.log(32 * float(L) ** 10 * (100 * lam_p) ** 0.5)
    gain = g(math.floor(rp * L / 2), lam_p + l1) - g(rp, lam_p)
    return kappa * gain >= math.log(64 * L**4 * ((lam_p + l1) / lam_p) ** 0.5)


def third_registration():
    per_l = {}
    for L in (5, 9, 15, 25):
        worst, n_adm = math.inf, 0
        for lam_p in (100.0, 200.0, 400.0, 600.0):
            for l1 in (0.01, 0.1):
                if not admissible(L, lam_p, l1) or not first_tier_ok(L, lam_p, l1):
                    continue
                n_adm += 1
                _, _, kappa, _ = constants(L)
                ell, lam_star, poly = tt_terms(L, lam_p, l1)
                cz = (ell + 2 * lam_star + poly) / lam_p
                g_cross = cz * lam_p / kappa
                center = g_cross if g_cross <= lam_p else g_cross**2 / lam_p
                for m in grid_m(L, lam_p, 1500, center, 300):
                    worst = min(worst, margin(float(m), L, lam_p, l1, cz, True, 4))
        per_l[L] = (n_adm, worst)
    rss_guard()
    for L, (n, w) in per_l.items():
        print(f"T1'': L = {L}: {n} points, smallest log margin = {w:.3f}")
    ok = all(n >= 1 and w >= 0 for n, w in per_l.values())
    print("T1''", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    first_registration()
    second_registration()
    third_registration()
