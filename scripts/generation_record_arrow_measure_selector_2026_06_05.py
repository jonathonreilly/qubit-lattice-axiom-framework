"""GENERATION_RECORD_ARROW_MEASURE_SELECTOR -- exact arrow/measure checks.

Given the two-letter generation Record alphabet with dimensions (1,2), the
measure/arrow choice can be represented by a one-parameter prior

    pi_gamma(letter) proportional to dim(letter)^gamma.

The positive theorem here is conditional but sharp:

    relative-entropy ascent toward pi_gamma stabilizes the dial coordinate
    s = gamma.

Thus:
    gamma=0  record-letter/block-count prior -> s=0, r=1/2, Q=2/3;
    gamma=1  dimension/Born prior            -> s=1, r=1,   Q=1.

The runner does not derive the physical gamma. It isolates the remaining
arrow/measure gate as the choice gamma=0 versus gamma=1 (or an intermediate
prior).
"""

from __future__ import annotations

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def simp(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand_log(expr, force=True))


def main() -> int:
    s, gamma, lam = sp.symbols("s gamma lam", real=True)
    ln2 = sp.log(2)
    x = sp.exp(s * ln2)       # x = 2^s = doublet/singlet sector-readout ratio
    y = sp.exp(gamma * ln2)   # y = 2^gamma = prior doublet/singlet ratio

    # Generation dial identities.
    rho = x
    r_of_s = rho / 2
    q_of_s = sp.Rational(1, 3) + sp.Rational(2, 3) * r_of_s
    check("dial.1 sector ratio rho=2^s gives r=rho/2=2^(s-1)",
          simp(r_of_s - sp.exp((s - 1) * ln2)) == 0)
    check("dial.2 Koide observable is Q(s)=1/3+(2/3)2^(s-1)",
          simp(q_of_s - (sp.Rational(1, 3) + sp.Rational(2, 3) * sp.exp((s - 1) * ln2))) == 0)
    check("dial.3 endpoints: s=0 -> Q=2/3 and s=1 -> Q=1",
          simp(q_of_s.subs(s, 0) - sp.Rational(2, 3)) == 0
          and simp(q_of_s.subs(s, 1) - 1) == 0)

    # Record-letter distribution p(s) and dim^gamma prior pi(gamma).
    p0 = 1 / (1 + x)
    p1 = x / (1 + x)
    pi0 = 1 / (1 + y)
    pi1 = y / (1 + y)

    check("prior.1 record-letter probabilities sum to one",
          simp(p0 + p1 - 1) == 0,
          f"p0={p0}; p1={p1}")
    check("prior.2 dim^gamma prior probabilities sum to one",
          simp(pi0 + pi1 - 1) == 0,
          f"pi0={pi0}; pi1={pi1}")
    check("prior.3 gamma=0 prior is equal record-letter/block-count weighting",
          simp(pi0.subs(gamma, 0) - sp.Rational(1, 2)) == 0
          and simp(pi1.subs(gamma, 0) - sp.Rational(1, 2)) == 0)
    check("prior.4 gamma=1 prior is dimension/Born weighting (1,2)",
          simp(pi0.subs(gamma, 1) - sp.Rational(1, 3)) == 0
          and simp(pi1.subs(gamma, 1) - sp.Rational(2, 3)) == 0)

    # Relative entropy arrow: maximize -D_KL(p(s) || pi(gamma)).
    # Use the logistic closed form to avoid branch-ambiguous simplification of
    # log(exp(real_symbol)).
    neg_kl = sp.log(1 + x) - sp.log(1 + y) + p1 * (gamma - s) * ln2
    d_neg_kl = simp(sp.diff(neg_kl, s))
    d_expected = -(s - gamma) * ln2**2 * x / (1 + x) ** 2
    curvature = simp(sp.diff(neg_kl, s, 2).subs(s, gamma))
    curvature_expected = -ln2**2 * y / (1 + y) ** 2

    check("arrow.1 relative-entropy arrow derivative is -(s-gamma)(log2)^2 2^s/(1+2^s)^2",
          simp(d_neg_kl - d_expected) == 0,
          f"d/ds[-KL]={d_expected}")
    check("arrow.2 stationary setting is exactly s=gamma",
          simp(d_neg_kl.subs(s, gamma)) == 0)
    check("arrow.3 curvature at s=gamma is negative",
          simp(curvature - curvature_expected) == 0
          and float(curvature_expected.subs(gamma, 0)) < 0
          and float(curvature_expected.subs(gamma, 1)) < 0,
          f"curvature={curvature_expected}")

    # Endpoint consequences.
    s_star = gamma
    r_star = simp(r_of_s.subs(s, s_star))
    q_star = simp(q_of_s.subs(s, s_star))
    check("endpoint.1 dim^gamma prior stabilizes r*=2^(gamma-1)",
          simp(r_star - sp.exp((gamma - 1) * ln2)) == 0,
          f"r*={r_star}")
    check("endpoint.2 dim^gamma prior stabilizes Q*=1/3+(2/3)2^(gamma-1)",
          simp(q_star - (sp.Rational(1, 3) + sp.Rational(2, 3) * sp.exp((gamma - 1) * ln2))) == 0,
          f"Q*={q_star}")
    check("endpoint.3 record-letter arrow gamma=0 stabilizes s=0, r=1/2, Q=2/3",
          simp(r_star.subs(gamma, 0) - sp.Rational(1, 2)) == 0
          and simp(q_star.subs(gamma, 0) - sp.Rational(2, 3)) == 0)
    check("endpoint.4 dimension/Born arrow gamma=1 stabilizes s=1, r=1, Q=1",
          simp(r_star.subs(gamma, 1) - 1) == 0
          and simp(q_star.subs(gamma, 1) - 1) == 0)

    # Gradient-flow sign checks around the two endpoints.
    d0 = d_expected.subs(gamma, 0)
    d1 = d_expected.subs(gamma, 1)
    check("A5.1 record-letter arrow moves negative s upward and positive s downward",
          float(d0.subs(s, -1)) > 0 and float(d0.subs(s, 1)) < 0)
    check("A5.2 dimension/Born arrow moves s=0 upward toward s=1 and s=2 downward",
          float(d1.subs(s, 0)) > 0 and float(d1.subs(s, 2)) < 0)

    # Discrete relaxation map to the selected prior. The fixed point is gamma
    # with multiplier 1-lam, stable for 0<lam<2. We test common cases exactly.
    relax = s + lam * (gamma - s)
    check("A6.1 discrete relaxation map has fixed point s=gamma",
          simp(relax.subs(s, gamma) - gamma) == 0)
    check("A6.2 relaxation multiplier is 1-lambda",
          simp(sp.diff(relax, s) - (1 - lam)) == 0)
    check("A6.3 half-step relaxation stabilizes both record-letter and dimension priors",
          abs(float((1 - lam).subs(lam, sp.Rational(1, 2)))) < 1
          and simp(relax.subs({gamma: 0, lam: sp.Rational(1, 2)}) - s / 2) == 0
          and simp(relax.subs({gamma: 1, lam: sp.Rational(1, 2)}) - (s + 1) / 2) == 0)

    # Firewall: the same algebra supports both endpoints; gamma is not derived.
    check("A7.1 both gamma=0 and gamma=1 are valid stable supplied arrows",
          simp(d_neg_kl.subs({gamma: 0, s: 0})) == 0
          and simp(d_neg_kl.subs({gamma: 1, s: 1})) == 0)
    check("A7.2 the theorem leaves gamma as a free measure/arrow input",
          gamma in r_star.free_symbols and gamma in q_star.free_symbols,
          "physical selection of gamma is not supplied by this runner")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print("FINDING: a dim^gamma record-arrow prior stabilizes s=gamma.")
    print("         gamma=0 gives Q=2/3; gamma=1 gives Q=1.")
    print("         The physical arrow/measure choice remains the named gate.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
