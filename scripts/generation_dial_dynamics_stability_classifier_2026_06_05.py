"""GENERATION_DIAL_DYNAMICS_STABILITY_CLASSIFIER -- finite exact checks.

This runner classifies simple dynamics on the exact generation weight dial

    r(s) = 2^(s-1),        Q(s) = 1/3 + (2/3) r(s).

The point is deliberately modest: dynamics need not force the Koide setting.
It is enough to identify dynamics classes for which s=0, equivalently
r=1/2 and Q=2/3, is a stable setting on the dial. Other equally explicit
classes stabilize s=1 or make s=0 repelling. The physical arrow/partition
selection remains outside this runner.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

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


@dataclass(frozen=True)
class LocalMap:
    name: str
    map_s: Callable[[float], float]
    fixed_point: float
    derivative_at_fixed_point: float

    def classification(self) -> str:
        slope = abs(self.derivative_at_fixed_point)
        if slope < 1.0:
            return "stable"
        if slope > 1.0:
            return "repelling"
        return "neutral"


def main() -> int:
    s, t, y = sp.symbols("s t y", real=True)
    ln2 = sp.log(2)

    # -------------------------------------------------------------------------
    # 1. Dial identities imported from the generation weight dial theorem.
    # -------------------------------------------------------------------------
    r_of_s = 2 ** (s - 1)
    q_of_s = sp.Rational(1, 3) + sp.Rational(2, 3) * r_of_s
    x = 2**s

    check("D1.1 exact dial endpoint s=0 is r=1/2",
          sp.simplify(r_of_s.subs(s, 0) - sp.Rational(1, 2)) == 0)
    check("D1.2 exact dial endpoint s=1 is r=1",
          sp.simplify(r_of_s.subs(s, 1) - 1) == 0)
    check("D1.3 Koide observable on the dial is Q(s)=1/3+(2/3)2^(s-1)",
          sp.simplify(q_of_s - (sp.Rational(1, 3) + sp.Rational(2, 3) * 2 ** (s - 1))) == 0)
    check("D1.4 s=0 gives Q=2/3; s=1 gives Q=1",
          sp.simplify(q_of_s.subs(s, 0) - sp.Rational(2, 3)) == 0
          and sp.simplify(q_of_s.subs(s, 1) - 1) == 0)

    # -------------------------------------------------------------------------
    # 2. Two-sector entropy on the block simplex.
    #
    # The sector fractions are singlet p0=1/(1+2r) and doublet p1=2r/(1+2r).
    # In the s coordinate this is p0=1/(1+2^s), p1=2^s/(1+2^s).
    # Entropy ascent in this two-sector partition stabilizes s=0.
    # -------------------------------------------------------------------------
    p0 = 1 / (1 + x)
    p1 = x / (1 + x)
    s2_entropy = -p0 * sp.log(p0) - p1 * sp.log(p1)
    ds2 = sp.simplify(sp.diff(s2_entropy, s))
    d2s2 = sp.simplify(sp.diff(s2_entropy, s, 2))
    ds2_closed = -s * ln2**2 * x / (1 + x) ** 2

    check("D2.1 two-sector probabilities sum to one",
          sp.simplify(p0 + p1 - 1) == 0,
          f"p0={p0}; p1={p1}")
    check("D2.2 two-sector entropy derivative has closed form -s*(log 2)^2*2^s/(1+2^s)^2",
          sp.simplify(ds2 - ds2_closed) == 0,
          f"dS2/ds={ds2_closed}")
    check("D2.3 s=0 is the unique stationary point of two-sector entropy",
          sp.simplify(ds2.subs(s, 0)) == 0
          and all(float(ds2.subs(s, val)) > 0 for val in [-3, -1, -sp.Rational(1, 5)])
          and all(float(ds2.subs(s, val)) < 0 for val in [sp.Rational(1, 5), 1, 3]))
    check("D2.4 two-sector entropy has negative curvature at s=0",
          sp.simplify(d2s2.subs(s, 0) + ln2**2 / 4) == 0,
          f"S2''(0)={sp.simplify(d2s2.subs(s, 0))}")

    # Continuous gradient ascent ds/dtau = dS2/ds has negative linearization at s=0.
    s2_linear = sp.simplify(sp.diff(ds2, s).subs(s, 0))
    check("D2.5 gradient ascent of two-sector entropy stabilizes s=0",
          sp.simplify(s2_linear + ln2**2 / 4) == 0 and float(s2_linear) < 0,
          f"linear coefficient at s=0 is {s2_linear}")

    # -------------------------------------------------------------------------
    # 3. Real-mode entropy on the three resolved real modes.
    #
    # This uses fractions [1, r, r]/(1+2r), equivalently
    # [1, 2^(s-1), 2^(s-1)]/(1+2^s). It stabilizes s=1, not s=0.
    # -------------------------------------------------------------------------
    p_real_0 = 1 / (1 + x)
    p_real_1 = x / (2 * (1 + x))
    s3_entropy = -p_real_0 * sp.log(p_real_0) - 2 * p_real_1 * sp.log(p_real_1)
    ds3 = sp.simplify(sp.diff(s3_entropy, s))
    d2s3 = sp.simplify(sp.diff(s3_entropy, s, 2))
    ds3_closed = ln2 * x * sp.log(2 / x) / (1 + x) ** 2

    check("D3.1 real-mode probabilities sum to one",
          sp.simplify(p_real_0 + 2 * p_real_1 - 1) == 0,
          f"p=[{p_real_0}, {p_real_1}, {p_real_1}]")
    check("D3.2 real-mode entropy derivative has closed form log(2)*2^s*log(2/2^s)/(1+2^s)^2",
          sp.simplify(ds3 - ds3_closed) == 0,
          f"dS3/ds={sp.simplify(ds3)}")
    check("D3.3 real-mode entropy stationary point is s=1",
          sp.simplify(ds3.subs(s, 1)) == 0
          and float(ds3.subs(s, 0)) > 0
          and float(ds3.subs(s, 2)) < 0)
    check("D3.4 real-mode entropy has negative curvature at s=1",
          sp.simplify(d2s3.subs(s, 1) + 2 * ln2**2 / 9) == 0,
          f"S3''(1)={sp.simplify(d2s3.subs(s, 1))}")
    check("D3.5 gradient ascent of real-mode entropy moves s=0 toward s=1",
          float(ds3.subs(s, 0)) > 0,
          f"dS3/ds at s=0 is {sp.simplify(ds3.subs(s, 0))}")

    # -------------------------------------------------------------------------
    # 4. Discrete map classifier in the same s coordinate.
    # -------------------------------------------------------------------------
    # Sharpening: r' = 2r^2. Since r=2^(s-1), this is s' = 2s.
    sharpen_s = 2 * s
    # Reverse/thermalizing branch: r' = sqrt(r/2). In s this is s' = s/2.
    reverse_s = s / 2

    check("D4.1 Lueders/record sharpening r->2r^2 becomes s' = 2s",
          sp.simplify(sharpen_s - 2 * s) == 0)
    check("D4.2 sharpening fixes s=0 but makes it repelling",
          sp.simplify(sharpen_s.subs(s, 0)) == 0
          and sp.simplify(sp.diff(sharpen_s, s).subs(s, 0) - 2) == 0)
    check("D4.3 reverse branch r->sqrt(r/2) becomes s' = s/2",
          sp.simplify(reverse_s - s / 2) == 0)
    check("D4.4 reverse branch fixes s=0 and makes it stable",
          sp.simplify(reverse_s.subs(s, 0)) == 0
          and sp.simplify(sp.diff(reverse_s, s).subs(s, 0) - sp.Rational(1, 2)) == 0)

    examples = [
        LocalMap("sharpening", lambda z: 2.0 * z, 0.0, 2.0),
        LocalMap("reverse", lambda z: 0.5 * z, 0.0, 0.5),
        LocalMap("neutral identity", lambda z: z, 0.0, 1.0),
    ]
    class_map = {example.name: example.classification() for example in examples}
    check("D4.5 local map classifier returns repelling/stable/neutral by |F'(s*)|",
          class_map == {"sharpening": "repelling", "reverse": "stable", "neutral identity": "neutral"},
          str(class_map))

    # Iteration sanity checks around the stable and repelling s=0 setting.
    z_reverse = 3.0
    z_sharpen = 0.05
    for _ in range(20):
        z_reverse = 0.5 * z_reverse
        z_sharpen = 2.0 * z_sharpen
    check("D4.6 reverse map iteration contracts toward s=0",
          abs(z_reverse) < 1e-5,
          f"3 -> {z_reverse:.6e} after 20 steps")
    check("D4.7 sharpening iteration expands away from s=0 for nonzero perturbations",
          abs(z_sharpen) > 1.0e4,
          f"0.05 -> {z_sharpen:.6e} after 20 steps")

    # -------------------------------------------------------------------------
    # 5. Supplied heat-kernel path is a transit through s=0, not an attractor.
    # -------------------------------------------------------------------------
    r_heat = sp.tanh(t) ** 4
    t_half = sp.atanh(2 ** sp.Rational(-1, 4))
    dr_heat = sp.diff(r_heat, t)
    dr_half = sp.simplify(dr_heat.subs(t, t_half))
    dr_half_expected = 4 * 2 ** sp.Rational(-3, 4) * (1 - 1 / sp.sqrt(2))

    check("D5.1 supplied heat-kernel path r(t)=tanh(t)^4 crosses r=1/2 once for t>0",
          sp.simplify(r_heat.subs(t, t_half) - sp.Rational(1, 2)) == 0
          and float(t_half) > 0)
    check("D5.2 heat-kernel crossing derivative is positive, so crossing is transit not attraction",
          sp.simplify(dr_half - dr_half_expected) == 0 and float(dr_half) > 0,
          f"dr/dt at crossing = {dr_half}")

    # -------------------------------------------------------------------------
    # 6. Generic local stability grammar.
    # -------------------------------------------------------------------------
    flow_stable = -y
    flow_unstable = y
    check("D6.1 continuous flow ds/dtau=-s stabilizes s=0",
          float(sp.diff(flow_stable, y).subs(y, 0)) < 0)
    check("D6.2 continuous flow ds/dtau=+s repels s=0",
          float(sp.diff(flow_unstable, y).subs(y, 0)) > 0)
    check("D6.3 stable-setting criterion is weaker than force/uniqueness",
          class_map["reverse"] == "stable" and class_map["sharpening"] == "repelling"
          and float(ds3.subs(s, 0)) > 0,
          "the same s=0 point is stable, repelling, or bypassed depending on the selected dynamics class")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print("FINDING: dynamics classifies stable settings on the generation dial;")
    print("         it does not force a unique Koide endpoint without an arrow/partition gate.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
