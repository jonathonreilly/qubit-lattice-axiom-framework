#!/usr/bin/env python3
"""Cycle 707b - erratum: the weak-field rival action formula is misstated.

Scope is deliberately small.  This runner establishes ONE thing: which action
expressions sit in which of the landed universality classes, and that the
formula Probe P4 names as the rival to valley-linear is not the formula that
was measured.

It makes no claim about why any exponent takes the value it does, supplies no
mechanism, and does not touch admission (c)'s derivation status.  An earlier
version of this cycle did all three and was rejected for overreach; the
rejected content is recorded in `PR_BACKLOG_707.md` and is not reissued here.

Background.  The landed ACTION_UNIQUENESS_NOTE establishes, on one fixed
ordered-lattice family, three universality classes keyed to the leading power
`p` of the field in the action's valley depth `1 - g(f)`:

    p = 0.5  sublinear    F~M = 0.50
    p = 1    linear       F~M = 1.00   (Newtonian)
    p = 2    superlinear  F~M = 2.00

Probe P4 writes, in three separate places, that the rival to valley-linear is
`S = L*sqrt(1 - phi)` and that it gives `F~M = 0.50`.

Rows:

  R1  the leading power of each named expression, exact closed-form depths
  R2  what the probe source actually measures
  R3  the three expressions carrying the "spent-delay / sqrt" name, compared
  R4  control: the depth forms agree with `1 - g(f)` where subtraction is safe
"""

import math

FAILURES = []
PASSES = []


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASSES if ok else FAILURES).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# Each entry gives g(f) and the valley depth `1 - g(f)` in a RATIONALIZED form.
# Evaluating `1 - g(f)` directly at f ~ 1e-9 destroys the answer to
# cancellation -- for g = 1 - f^2 it underflows to exactly zero.  R4 checks the
# closed forms against `1 - g(f)` at moderate f, where that subtraction is safe.
FORMS = {
    "L(1-f)        valley-linear":  (lambda f: 1 - f,             lambda f: f,                          1.0),
    "L*exp(-f)":                    (lambda f: math.exp(-f),      lambda f: -math.expm1(-f),            1.0),
    "L/(1+f)":                      (lambda f: 1 / (1 + f),       lambda f: f / (1 + f),                1.0),
    "L*sqrt(1-f)   <- P4's rival":  (lambda f: math.sqrt(1 - f),  lambda f: f / (1 + math.sqrt(1 - f)), 1.0),
    "L(1-sqrt f)   <- measured":    (lambda f: 1 - math.sqrt(f),  lambda f: math.sqrt(f),               0.5),
    "L(1-f^2)":                     (lambda f: 1 - f * f,         lambda f: f * f,                      2.0),
}


def leading_power(depth, f=1e-9, ratio=10.0):
    return math.log(depth(f * ratio) / depth(f)) / math.log(ratio)


def r1_leading_powers():
    ok = True
    for name, (_, depth, expected) in FORMS.items():
        p = leading_power(depth)
        print(f"      {name:30s} p = {p:.6f}   (class {expected})")
        if abs(p - expected) > 1e-6:
            ok = False
    check("R1 leading power of each named expression", ok, f"{len(FORMS)} expressions")


def r2_what_the_probe_measures():
    """The probe's `action_value()` defines the sqrt mode as L*(1 - sqrt(f)).

    Reproduced here rather than imported, so the runner stays self-contained:

        if action_mode == "valley_sqrt":
            return L * (1.0 - np.sqrt(f))

    The square root is on the FIELD.  Its depth is sqrt(f), leading power 1/2 --
    consistent with the measured F~M = 0.50.
    """
    def valley_sqrt(L, f):
        return L * (1.0 - math.sqrt(f))

    depth = lambda f: 1.0 - valley_sqrt(1.0, f)
    p = leading_power(depth, f=1e-9)
    matches_measured_class = abs(p - 0.5) < 1e-9

    # P4's expression, by contrast, is linear: 1 - sqrt(1-f) = f/2 + f^2/8 + ...
    p4_depth = lambda f: f / (1 + math.sqrt(1 - f))
    p_p4 = leading_power(p4_depth, f=1e-9)
    ratio_to_half = p4_depth(1e-10) / 1e-10
    p4_is_linear = abs(p_p4 - 1.0) < 1e-9 and abs(ratio_to_half - 0.5) < 1e-6

    check(
        "R2 the probe's `valley_sqrt` is L*(1-sqrt f), power 1/2; P4's L*sqrt(1-f) is power 1",
        matches_measured_class and p4_is_linear,
        f"p[valley_sqrt]={p:.6f}, p[P4]={p_p4:.6f}, P4 depth/f -> {ratio_to_half:.8f}",
    )


def r3_three_expressions_one_name():
    """Three expressions carry the spent-delay / sqrt name.  Two share a class.

    (1) geometric, ACTION_CROSSOVER_NOTE:  S = dl - sqrt(dl^2 - L^2)
    (2) measured,  ACTION_UNIQUENESS_NOTE: S = L(1 - f^0.5)
    (3) P4:                                S = L*sqrt(1 - phi)

    With dl = L(1+eps), (1) expands as L[(1+eps) - sqrt(2 eps + eps^2)]
    -> L[1 - sqrt(2 eps)], so its depth goes as sqrt(eps): power 1/2, with
    coefficient sqrt(2).  So (1) and (2) agree; (3) is the outlier.
    """
    def geometric_depth(eps, L=1.0):
        dl = L * (1.0 + eps)
        return L - (dl - math.sqrt(dl * dl - L * L))

    p_geo = leading_power(geometric_depth, f=1e-9)
    coeff = [geometric_depth(e) / math.sqrt(2 * e) for e in (1e-7, 1e-8, 1e-9)]
    coeff_converges = all(abs(c - 1.0) < 1e-3 for c in coeff) and (
        abs(coeff[-1] - 1.0) < abs(coeff[0] - 1.0)
    )

    p_measured = leading_power(math.sqrt, f=1e-9)
    p_p4 = leading_power(lambda f: f / (1 + math.sqrt(1 - f)), f=1e-9)

    one_and_two_agree = abs(p_geo - p_measured) < 1e-3
    three_is_outlier = abs(p_p4 - 1.0) < 1e-9 and abs(p_p4 - p_geo) > 0.4

    print(f"      (1) geometric   p = {p_geo:.6f}   depth/sqrt(2 eps) -> {coeff[-1]:.6f}")
    print(f"      (2) measured    p = {p_measured:.6f}")
    print(f"      (3) P4          p = {p_p4:.6f}")

    check(
        "R3 the geometric spent-delay and the measured form share p=1/2; P4's formula is the outlier",
        abs(p_geo - 0.5) < 1e-3 and coeff_converges and one_and_two_agree and three_is_outlier,
        "so P4 misstates the formula, not the intended class",
    )


def r4_depth_forms_control():
    """The rationalized depths must agree with `1 - g(f)` where that is safe."""
    ok = True
    worst = 0.0
    for name, (g, depth, _) in FORMS.items():
        for f in (1e-3, 1e-2, 0.1, 0.25):
            err = abs(depth(f) - (1 - g(f)))
            worst = max(worst, err)
            if err > 1e-12 * max(1.0, abs(depth(f))):
                ok = False
    # and the direct subtraction really does fail deep in the weak field,
    # which is why the closed forms are used at all
    underflows = (1 - (1 - (1e-9) ** 2)) == 0.0
    check(
        "R4 control: closed-form depths match 1-g(f) at moderate f; direct subtraction underflows at 1e-9",
        ok and underflows,
        f"worst disagreement {worst:.3e}; direct 1-(1-f^2) at f=1e-9 gives exactly 0",
    )


def main() -> int:
    print("Cycle 707b - erratum: which action formula is in which class")
    print("=" * 74)
    r1_leading_powers()
    r2_what_the_probe_measures()
    r3_three_expressions_one_name()
    r4_depth_forms_control()
    print("=" * 74)
    print(f"{len(PASSES)} PASS / {len(FAILURES)} FAIL")
    for f in FAILURES:
        print(f"  FAILED: {f}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
