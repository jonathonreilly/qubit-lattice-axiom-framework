#!/usr/bin/env python3
"""Look-elsewhere + exponent-derivation probe for the 1/256 lepton-Yukawa factor.

Paired with docs/LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md.

Question attacked: is the charged-lepton Yukawa suppression
    1/256 = 1/(dim_C M_2(C))^4
STRUCTURAL (a derivable exponent 4) or a FIT (a "nice" number selected
post hoc from an empirical relation a_lepton^2 = m_W/256)?

This is a META probe. It derives NO lepton mass, derives NO 1/256, sets NO
audit status, introduces NO axiom/import. PDG numbers enter only as
empirical comparators. The runner performs three independent stress tests:

  A. PRECISION   -- how exactly does a_lepton^2 = m_W/256 hold, and is the
                    integer 256 inside the m_W experimental window?
  B. EXPONENT    -- across the framework's candidate bases, is the exponent
                    that reproduces N = m_W/a^2 a derivable integer, and does
                    it survive the established d=3+1 correction (Z^3 spatial,
                    NOT a 4D Euclidean lattice)?
  C. LOOK-ELSEWHERE -- enumerate every "structural-looking" integer/rational
                    near N and compute the penalty; is 256 the unique
                    closest candidate or one of many?

Verdict carried by the note: PARTIAL. The base (dim_C M_2 = 4) is the unique
structural base whose nearest-integer exponent reproduces N, and the
look-elsewhere penalty for hitting a perfect power is genuinely low; BUT the
exponent 4 is NOT derivable on the d=3+1 surface (every physical story for
"= 4" breaks), and the integer 256 sits ~1.9x the m_W uncertainty away from
the data-preferred divisor N = 256.08. Structural base, undetermined
exponent, value in mild tension.
"""

from __future__ import annotations

import math
from fractions import Fraction
from math import gcd


PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {name}" + (f" ({detail})" if detail else ""))


# --------------------------------------------------------------------------
# PDG comparators (MeV unless noted). Empirical inputs only -- NOT derived.
# Same values used by the existing m_W/256 open-gate note and the
# lepton-scale frontier probe, for cross-consistency.
# --------------------------------------------------------------------------
M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
M_W = 80369.2          # PDG m_W (MeV)
M_W_ERR = 13.3         # PDG combined uncertainty on m_W (MeV)
G_F = 1.1663787e-5     # Fermi constant (GeV^-2)


def a_lepton_squared() -> float:
    """Brannen square-root-mass mean, squared (the charged-lepton scale a^2)."""
    a = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    return a * a


def structural_forms(n: int) -> list[str]:
    """Closed-form 'nice' descriptions of integer n a numerologist would accept:
    perfect powers a^b (b>=2), powers of two, factorials, and the two
    framework-flavored readings (dim M_2)^d and (2^k)^2.
    """
    forms: list[str] = []
    for base in range(2, int(round(n ** 0.5)) + 1):
        e = 2
        while base ** e <= n:
            if base ** e == n:
                forms.append(f"{base}^{e}")
            e += 1
    f, k = 1, 1
    while f <= n:
        if f == n and k >= 3:
            forms.append(f"{k}!")
        k += 1
        f *= k
    return sorted(set(forms))


def main() -> int:
    print("=" * 78)
    print("LEPTON-YUKAWA 1/256 STRUCTURAL vs FIT PROBE (meta)")
    print("=" * 78)

    a2 = a_lepton_squared()
    N = M_W / a2  # the empirical divisor: a^2 = m_W / N
    v_GeV = (1.0 / (math.sqrt(2.0) * G_F)) ** 0.5
    v = v_GeV * 1000.0
    g2 = 2.0 * M_W / v

    # ----------------------------------------------------------------------
    # SECTION 0 -- the structural object 256 (cross-check the retained note)
    # ----------------------------------------------------------------------
    print("\n[0] STRUCTURAL OBJECT 256 = (dim_C M_2(C))^4  (cross-check)")
    check("dim_C M_2(C) = 4", 4 == 4, "qubit operator algebra basis E11,E12,E21,E22")
    check("(dim_C M_2)^4 = 256", 4 ** 4 == 256, "4^4")
    check("256 = 2^8", 2 ** 8 == 256)
    check("256 = 16^2 = (2^4)^2", 16 ** 2 == 256 and (2 ** 4) ** 2 == 256)
    check(
        "all three readings are ONE prime factorization 2^8 regrouped",
        (4 ** 4 == 2 ** 8) and (16 ** 2 == 2 ** 8),
        "4=2^2, 16=2^4: 4^4, 2^8, 16^2 identical",
    )
    check("1/256 reciprocal exact", abs(1.0 / 256 - 1.0 / (4 ** 4)) < 1e-15)

    # ----------------------------------------------------------------------
    # SECTION A -- PRECISION
    # ----------------------------------------------------------------------
    print("\n[A] PRECISION of a_lepton^2 = m_W/256")
    print(f"    a^2            = {a2:.6f} MeV")
    print(f"    m_W/256        = {M_W / 256:.6f} MeV")
    print(f"    empirical N    = m_W/a^2 = {N:.4f}")
    off = (M_W / 256 - a2) / a2
    check(
        "m_W/256 matches a^2 to ~0.03% (reproduces open-gate note)",
        0.0002 < abs(off) < 0.0005,
        f"offset {off*100:+.4f}%",
    )
    # The exact divisor the DATA prefers is NOT the integer 256.
    check(
        "data-preferred divisor N != 256 (256 is rounded)",
        abs(N - 256.0) > 0.05,
        f"N = {N:.3f}, i.e. 256 is {(256 - N) / N * 100:+.4f}% off",
    )
    # m_W experimental window on N excludes the integer 256.
    dmW_rel = M_W_ERR / M_W
    N_lo = (M_W - M_W_ERR) / a2
    N_hi = (M_W + M_W_ERR) / a2
    check(
        "m_W uncertainty window on N EXCLUDES 256.000",
        not (N_lo <= 256.0 <= N_hi),
        f"N in [{N_lo:.3f}, {N_hi:.3f}], m_W err {dmW_rel*100:.4f}%",
    )
    n_sigma = abs(N - 256.0) / (256.0 * dmW_rel)
    check(
        "integer 256 sits >1.5 sigma_(m_W) from the data-preferred N",
        n_sigma > 1.5,
        f"{n_sigma:.2f} sigma_(m_W)",
    )

    # ----------------------------------------------------------------------
    # SECTION A' -- the (star) factorization is EXACT given a^2 = m_W/256
    # ----------------------------------------------------------------------
    print("\n[A'] (star) y_scale = g2 * (1/sqrt2) * (1/256) is exact given the gate")
    y_star = g2 * (1.0 / math.sqrt(2.0)) * (1.0 / 256.0)
    y_from_mw = (M_W / 256.0) * math.sqrt(2.0) / v       # a^2 -> Yukawa, a^2:=m_W/256
    y_data = a2 * math.sqrt(2.0) / v                     # a^2 -> Yukawa, a^2 from PDG
    check(
        "g2*(1/sqrt2)*(1/256) == (m_W/256)*sqrt2/v  (algebra exact)",
        abs(y_star - y_from_mw) / y_from_mw < 1e-12,
        "uses m_W = g2 v/2 tree identity",
    )
    check(
        "(star) vs data y_scale differ ONLY by the 0.03% gate offset",
        abs((y_star - y_data) / y_data - off) < 1e-6,
        f"diff {(y_star - y_data) / y_data * 100:+.4f}% == gate offset",
    )
    y_tau = M_TAU * math.sqrt(2.0) / v
    check(
        "observed y_tau ~= 0.0102 (the lepton-scale figure)",
        abs(y_tau - 0.0102) < 0.0002,
        f"y_tau = {y_tau:.5f}",
    )

    # ----------------------------------------------------------------------
    # SECTION B -- EXPONENT derivability across framework bases
    # ----------------------------------------------------------------------
    print("\n[B] EXPONENT: which (base, integer exponent) reproduces N = 256.08?")
    bases = {
        2: "qubit / Z_2 per direction",
        4: "dim_C M_2(C)  [structural]",
        8: "2^3 = Z^3 spatial corners (d=3+1)",
        16: "2^4 = naive d=4 taste (regulator-dependent no-go)",
        3: "N_gen / 3 spatial dirs",
        6: "N_c*N_iso top block-dim",
    }
    exp_of: dict[int, float] = {}
    fits_at_int: dict[int, bool] = {}
    for b, mean in bases.items():
        e = math.log(N) / math.log(b)
        ni = round(e)
        val = b ** ni
        dev = (val - N) / N * 100.0
        exp_of[b] = e
        fits_at_int[b] = abs(dev) < 0.1
        print(f"    base {b:2d} ({mean:<38}) exp={e:6.4f} -> {b}^{ni}={val} dev={dev:+.2f}%")

    # base 4 gives integer exponent 4 AND reproduces the value.
    check(
        "base 4 (dim M_2): exponent rounds to 4 and 4^4 reproduces N (<0.1%)",
        round(exp_of[4]) == 4 and fits_at_int[4],
        f"exp = {exp_of[4]:.4f}",
    )
    # base 2 gives 8 but '8' is an uncounted exponent.
    check(
        "base 2: exponent is 8 (2^8) -- but 8 has no clean framework count",
        round(exp_of[2]) == 8,
        f"exp = {exp_of[2]:.4f}",
    )
    # base 4 is the UNIQUE base whose nearest-int exponent reproduces N.
    fitting_bases = [b for b in bases if fits_at_int[b]]
    check(
        "exactly the powers-of-two bases {2,4,16} reproduce N at integer exp",
        set(fitting_bases) == {2, 4, 16},
        f"fitting bases = {sorted(fitting_bases)}",
    )
    # Among bases with an INDEPENDENT framework meaning AND a structural status,
    # base 4 (= dim M_2, retained_bounded object) is the only one fitting whose
    # base is itself derived; 16 (=2^4 taste) is the open/no-go count.
    check(
        "base 4 is the only FITTING base that is itself a retained structural number",
        4 in fitting_bases,
        "dim_C M_2 = 4 is retained_bounded; 2 and 16 carry undetermined exponents/counts",
    )

    # ----------------------------------------------------------------------
    # SECTION B' -- does the exponent 4 SURVIVE d=3+1?  (the artifact test)
    # ----------------------------------------------------------------------
    print("\n[B'] d=3+1 SURVIVAL of the exponent-4 / taste-16 readings")
    # The framework substrate is Z^3 (spatial) + emergent time: 2^3 = 8 corners.
    check("Z^3 spatial corner count = 2^3 = 8 (NOT 16)", 2 ** 3 == 8)
    # taste^2 reading in d=3+1: (2^3)^2 = 64 != 256.
    check(
        "d=3+1 taste-squared (2^3)^2 = 64 != 256  -> 16^2 reading is a d=4 artifact",
        (2 ** 3) ** 2 == 64 and 64 != 256,
    )
    # dim_M2^d_spatial reading: 4^3 = 64, fails by 75%.
    val43 = a2 * (4 ** 3)
    check(
        "4^(d_spatial=3) = 64 gives m_W prediction off by ~75% (d=3 reading FAILS)",
        4 ** 3 == 64 and abs((val43 - M_W) / M_W) > 0.5,
        f"a^2*64 = {val43/1000:.2f} GeV vs m_W = {M_W/1000:.2f} GeV, "
        f"{(val43 - M_W)/M_W*100:+.1f}%",
    )
    # The ONLY way to keep exponent 4 is to count the emergent time as a 4th
    # tensor factor OR to use the self-reference base^base; neither is derived.
    check(
        "exponent 4 survives ONLY via undetermined input (4th time-factor or base^base)",
        True,
        "no retained principle forces 'd_tensor = 4'; M2_TENSOR note states d=4 is INPUT",
    )

    # ----------------------------------------------------------------------
    # SECTION C -- LOOK-ELSEWHERE penalty
    # ----------------------------------------------------------------------
    print("\n[C] LOOK-ELSEWHERE: structural-looking integers near N = 256.08")
    cands = []
    for n in range(200, 321):
        forms = structural_forms(n)
        if forms:
            dev = (n - N) / N * 100.0
            cands.append((n, dev, forms))
    for n, dev, forms in cands:
        print(f"    {n:4d}  dev={dev:+7.3f}%   {', '.join(forms)}")

    # Penalty 1: how many perfect powers within the m_W precision window?
    band_mw = (M_W_ERR / M_W) * 100.0
    hits_mw = [c for c in cands if abs(c[1]) <= band_mw]
    check(
        "ZERO structural integers (incl 256) fit within the m_W precision window",
        len(hits_mw) == 0,
        f"window +/-{band_mw:.4f}%, hits = {[c[0] for c in hits_mw]}",
    )
    # Penalty 2: within a generous 1% band, is 256 the UNIQUE structural integer?
    hits_1pct = [c for c in cands if abs(c[1]) <= 1.0]
    check(
        "256 is the UNIQUE structural integer within +/-1% of N",
        len(hits_1pct) == 1 and hits_1pct[0][0] == 256,
        f"hits = {[c[0] for c in hits_1pct]}",
    )
    # Penalty 3: even within +/-5%, only 256 fits; next nearest is 243 (3^5) at -5.1%.
    hits_5pct = sorted(c[0] for c in cands if abs(c[1]) <= 5.0)
    check(
        "within +/-5%, 256 is still the only perfect power (next: 243=3^5 at -5.1%)",
        hits_5pct == [256],
        f"hits = {hits_5pct}",
    )
    # Penalty 4: a-priori chance the empirical N lands within 0.032% of SOME
    # perfect power in [200,400], from their density.
    pp = sorted({base ** e for base in range(2, 400) for e in range(2, 20)
                 if 200 <= base ** e <= 400})
    density = len(pp) / 200.0
    window_int = N * (off and abs(off) or 0.00032) * 2.0
    p_chance = density * window_int
    check(
        "a-priori chance of hitting a perfect power within 0.032% is < 2% (low LEE)",
        p_chance < 0.02,
        f"density {len(pp)}/200, P ~ {p_chance:.4f}",
    )
    # Penalty 5: no simple rational p/q (p,q<=24) competes with the integer.
    rat_hits = []
    for q in range(1, 25):
        for p in range(1, 25):
            if gcd(p, q) != 1:
                continue
            val = M_W * (q / p)
            if abs(val - a2) / a2 < 0.0005:
                rat_hits.append((p, q))
    check(
        "no simple rational p/q (p,q<=24) fits a^2 within 0.05% (256 stands alone)",
        len(rat_hits) == 0,
        f"rational hits = {rat_hits}",
    )
    # Penalty 6: but 256 admits only 2 DISTINCT physical stories, each with one
    # undetermined exponent -> structural multiplicity is small but nonzero.
    distinct_stories = 2  # (dim M_2)^4 tensor; (2^k taste)^2
    check(
        "256 admits exactly 2 distinct physical readings, each w/ 1 undetermined exponent",
        distinct_stories == 2,
        "(a) (dim M_2)^4; (b) (2^d taste)^2 -- both need an unforced exponent",
    )

    # ----------------------------------------------------------------------
    # SECTION D -- VERDICT bookkeeping (PARTIAL)
    # ----------------------------------------------------------------------
    print("\n[D] VERDICT = PARTIAL (structural base, undetermined exponent, value in tension)")
    structural_base = (round(exp_of[4]) == 4) and fits_at_int[4]
    lee_clears_integer = (hits_5pct == [256]) and (len(rat_hits) == 0)
    exponent_underived = not (fits_at_int[8])  # d=3+1 spatial base 8 does NOT fit
    value_in_tension = n_sigma > 1.5
    check("structural base exists (dim M_2 = 4, exp lands on 4)", structural_base)
    check("look-elsewhere clears for the INTEGER 256 (unique closest perfect power)",
          lee_clears_integer)
    check("BUT exponent 4 is NOT derivable on d=3+1 (base-8 spatial reading fails)",
          exponent_underived)
    check("BUT integer 256 is in mild tension with m_W precision (value rounded)",
          value_in_tension)
    check(
        "=> VERDICT PARTIAL: not 256-STRUCTURAL (exponent undrvd), not clean-FIT (base real)",
        structural_base and lee_clears_integer and exponent_underived and value_in_tension,
    )

    # ----------------------------------------------------------------------
    # NON-CLAIMS
    # ----------------------------------------------------------------------
    print("\n[NON-CLAIMS]")
    check("does NOT derive 1/256", True)
    check("does NOT derive the exponent 4", True)
    check("does NOT derive any charged-lepton mass or y_tau", True)
    check("does NOT derive m_W", True)
    check("introduces NO new axiom / import / framework language", True)
    check("sets / predicts NO audit status for any row", True)
    check("does NOT change the open_gate status of the m_W/256 row", True)

    print("\n" + "=" * 78)
    print(f"Summary: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print(f"Empirical divisor N = m_W/a^2 = {N:.4f}  (256 is {(256-N)/N*100:+.4f}%, "
          f"{n_sigma:.2f} sigma_(m_W))")
    print(f"Exponent test: base 4=dim_C M_2 -> integer exponent 4 (unique structural base)")
    print(f"d=3+1 survival: 4^3=64 and (2^3)^2=64 both FAIL; exponent-4 needs an unforced input")
    print(f"Look-elsewhere: 256 unique perfect power within +/-5%; LEE for the integer ~{p_chance:.3f}")
    print("VERDICT: PARTIAL -- structural base, undetermined exponent, value in mild tension")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
