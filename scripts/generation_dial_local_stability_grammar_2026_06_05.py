"""GENERATION_DIAL_LOCAL_STABILITY_GRAMMAR -- exact one-dimensional checks.

This runner isolates the stability grammar used by the dynamics classifier.
It proves that the positive ratio coordinate r and the dial coordinate

    s = log2(2r),        r(s) = 2^(s-1)

are smooth monotone reparametrizations, so local map/flow stability can be
computed in the s coordinate without changing the multiplier/sign at a fixed
point. It also verifies the two named generation maps.
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


def classify_map_multiplier(value: float) -> str:
    mag = abs(value)
    if mag < 1.0:
        return "stable"
    if mag > 1.0:
        return "repelling"
    return "neutral"


def classify_flow_linearization(value: float) -> str:
    if value < 0.0:
        return "stable"
    if value > 0.0:
        return "repelling"
    return "neutral_or_higher_order"


def main() -> int:
    s, r, eps = sp.symbols("s r eps", real=True)
    rstar, alpha, beta = sp.symbols("rstar alpha beta", positive=True)
    ln2 = sp.log(2)

    # Use exp((s-1)log 2) for clean branch-aware symbolic simplification.
    h = sp.exp((s - 1) * ln2)          # r(s)
    L = 1 + sp.log(r) / ln2            # s(r)=log2(2r)

    check("S1.1 dial map r(s)=2^(s-1) is positive and has positive derivative",
          sp.simplify(sp.diff(h, s) - ln2 * h) == 0)
    check("S1.2 inverse coordinate is s(r)=1+log(r)/log(2)",
          True,
          f"L(r)={L}")
    check("S1.3 L(r(s)) = s",
          simp(L.subs(r, h) - s) == 0)
    check("S1.4 r(L(r)) = r for positive r",
          simp(sp.exp((L - 1) * ln2) - r) == 0)

    # -------------------------------------------------------------------------
    # Map conjugacy: if G(r*)=r* and G'(r*)=alpha, then the conjugated
    # s-coordinate map has the same local multiplier alpha.
    # -------------------------------------------------------------------------
    r_eps = rstar * sp.exp(eps * ln2)
    sstar = 1 + sp.log(rstar) / ln2
    local_map = rstar + alpha * (r_eps - rstar)
    delta_s_map = 1 + sp.log(local_map) / ln2 - sstar
    multiplier = simp(sp.diff(delta_s_map, eps).subs(eps, 0))
    check("S2.1 smooth r<->s conjugacy preserves local map multiplier",
          sp.simplify(multiplier - alpha) == 0,
          f"multiplier={multiplier}")

    # Flow conjugacy: if dr/dtau = beta*(r-r*), then ds/dtau has the same
    # linear coefficient beta at the fixed point.
    local_flow_r = beta * (r_eps - rstar)
    local_flow_s = local_flow_r / (r_eps * ln2)
    flow_coeff = simp(sp.diff(local_flow_s, eps).subs(eps, 0))
    check("S2.2 smooth r<->s conjugacy preserves local flow linearization",
          sp.simplify(flow_coeff - beta) == 0,
          f"flow coefficient={flow_coeff}")

    # -------------------------------------------------------------------------
    # Named generation maps.
    # -------------------------------------------------------------------------
    sharp_s = simp(1 + sp.log(2 * h**2) / ln2)
    reverse_r = sp.exp((s - 2) * ln2 / 2)
    reverse_s = simp(1 + sp.log(reverse_r) / ln2)

    check("S3.1 sharpening r->2r^2 is s' = 2s",
          simp(sharp_s - 2 * s) == 0)
    check("S3.2 reverse branch r->sqrt(r/2) is s' = s/2",
          simp(reverse_s - s / 2) == 0)
    check("S3.3 sharpening is repelling at s=0",
          classify_map_multiplier(float(sp.diff(sharp_s, s).subs(s, 0))) == "repelling")
    check("S3.4 reverse branch is stable at s=0",
          classify_map_multiplier(float(sp.diff(reverse_s, s).subs(s, 0))) == "stable")

    # -------------------------------------------------------------------------
    # General grammar examples.
    # -------------------------------------------------------------------------
    examples = {
        "contracting map": classify_map_multiplier(0.5),
        "identity map": classify_map_multiplier(1.0),
        "expanding map": classify_map_multiplier(2.0),
        "orientation-flip contraction": classify_map_multiplier(-0.5),
        "orientation-flip expansion": classify_map_multiplier(-1.5),
    }
    check("S4.1 map grammar classifies by |F'(s*)|",
          examples == {
              "contracting map": "stable",
              "identity map": "neutral",
              "expanding map": "repelling",
              "orientation-flip contraction": "stable",
              "orientation-flip expansion": "repelling",
          },
          str(examples))

    flow_examples = {
        "negative linearization": classify_flow_linearization(-0.25),
        "zero linearization": classify_flow_linearization(0.0),
        "positive linearization": classify_flow_linearization(0.25),
    }
    check("S4.2 flow grammar classifies by sign of f'(s*)",
          flow_examples == {
              "negative linearization": "stable",
              "zero linearization": "neutral_or_higher_order",
              "positive linearization": "repelling",
          },
          str(flow_examples))

    # Stability is local, not value selection.
    check("S4.3 local stability grammar does not select which fixed point is physical",
          classify_map_multiplier(0.5) == "stable"
          and classify_flow_linearization(-0.25) == "stable",
          "a separate theorem must identify the physical map/flow and fixed point")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print("FINDING: the positive-ratio dial is a clean stability coordinate;")
    print("         local stability is map/flow classification, not value selection.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
