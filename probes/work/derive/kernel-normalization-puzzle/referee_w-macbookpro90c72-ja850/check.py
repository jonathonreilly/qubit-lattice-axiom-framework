#!/usr/bin/env python3
"""Independent referee for kernel-normalization-puzzle a1.

The Gaussian lab-frame ratio is recomputed. The attempt's script is not
imported. The formation runs were not repeated.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


source = Path("probes/lib/formation_levelplane.py").read_text()
loop = source.split("for t in range(1, T + 1):", 1)
check(
    "N1 frame",
    len(loop) == 2
    and "t1 = ref - (ref @ e0) * e0" in loop[0]
    and "fx, fy = s @ t1, s @ t2" in loop[1]
    and "0.5 * (np.abs(np.fft.fftn(fx)) ** 2 + np.abs(np.fft.fftn(fy)) ** 2)" in loop[1]
    and "sigma2 = A(n * beta) / (n * beta)" in source
    and "n = (2 * dim + 1) if sym else (dim + 1)" in source,
    "axes are fixed from the initial direction, the spectrum averages the two lab-frame components, and n = dim + 1",
)

variance, angle, total = sp.symbols("v theta T", positive=True)
horizontal, vertical = sp.symbols("x y", real=True)
density = sp.exp(-(horizontal ** 2 + vertical ** 2) / (2 * variance)) / (2 * sp.pi * variance)
moments_ok = True
for order in (1, 2, 3, 4):
    moment = sp.integrate(
        sp.integrate((horizontal ** 2 + vertical ** 2) ** order * density, (horizontal, -sp.oo, sp.oo)),
        (vertical, -sp.oo, sp.oo),
    )
    moments_ok = moments_ok and sp.simplify(moment - (2 * variance) ** order * sp.factorial(order)) == 0
check("N2 moments", moments_ok, "<(theta^2)^m> = (2v)^m m! for m = 1, 2, 3, 4")

taylor = sp.series(sp.sin(angle) ** 2, angle, 0, 10).removeO()
check(
    "N2 series",
    sp.expand(taylor - (angle ** 2 - angle ** 4 / 3 + 2 * angle ** 6 / 45 - angle ** 8 / 315)) == 0,
    "sin^2 theta = theta^2 - theta^4/3 + 2 theta^6/45 - theta^8/315 + O(theta^10)",
)

radius = sp.symbols("r", positive=True)
rate = 1 / (2 * variance)
exact = sp.integrate(rate * radius * sp.exp(-rate * radius ** 2) * (1 - sp.cos(2 * radius)), (radius, 0, sp.oo))
ratio = sp.series(sp.simplify(exact / (2 * variance)), variance, 0, 4).removeO()
in_total = sp.expand(ratio.subs(variance, total / 2))
expected = 1 - sp.Rational(2, 3) * total + sp.Rational(4, 15) * total ** 2 - sp.Rational(8, 105) * total ** 3
check(
    "N2 ratio",
    sp.expand(in_total - expected) == 0,
    "E[sin^2 theta]/T = 1 - (2/3)T + (4/15)T^2 - (8/105)T^3 + O(T^4)",
)

slope = sp.symbols("beta", positive=True)
def gain(field):
    return 1 - 1 / field + 2 / (sp.exp(2 * field) - 1)
def noise(count, coupling):
    return gain(count * coupling) / (count * coupling)
limit_gap = sp.simplify(sp.Rational(2, 9) * gain(3 * slope) - slope * sp.Rational(2, 3) * noise(3, slope))
check(
    "N3 limit",
    sp.simplify((sp.coth(slope) - 1 / slope - gain(slope)).rewrite(sp.exp)) == 0 and limit_gap == 0,
    "A = 1 - 1/kappa + 2/(e^{2 kappa}-1), so beta*(2/3)*A(3 beta)/(3 beta) = (2/9) A(3 beta) -> 2/9",
)

def values(count, coupling):
    sigma2 = noise(count, coupling)
    deficit = sp.Rational(2, 3) * sigma2
    quadratic = 1 - deficit + sp.Rational(4, 15) * sigma2 ** 2
    return sp.N(sigma2, 30), sp.N(deficit, 30), sp.N(quadratic, 30)

rows = {coupling: values(3, coupling) for coupling in (1, 2, 4, 6, 24)}
deficits = [rows[coupling][1] for coupling in (1, 2, 4, 6, 24)]
beta2 = rows[2][1]
beta24 = rows[24][1]
ratio2 = rows[2][2]
ratio24 = rows[24][2]
check(
    "N3 size",
    all(deficits[i] > deficits[i + 1] for i in range(4))
    and abs(beta2 - sp.Float("0.0925939579815")) < sp.Float("1e-12")
    and abs(beta24 - sp.Float("0.00913065843621")) < sp.Float("1e-12")
    and abs(ratio2 - sp.Float("0.912550226651")) < sp.Float("1e-12")
    and abs(ratio24 - sp.Float("0.990919362918")) < sp.Float("1e-12")
    and beta2 > sp.Rational(9, 100)
    and beta24 > sp.Rational(9, 1000)
    and ratio2 < sp.Rational(95, 100),
    "at n=3 and T=sigma^2 the deficit is 0.09259 at beta=2 and 0.00913 at beta=24; the quadratic ratio 0.9126 lies below the quoted 0.95",
)

four = values(4, 2)[1]
seven = values(7, 2)[1]
check(
    "N3 stencil count",
    four > sp.Rational(7, 100) and seven > sp.Rational(4, 100) and four < beta2 and seven < four,
    "the same linear deficit at beta=2 is still above 0.07 for n=4 and above 0.04 for n=7",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. The estimator projects onto axes fixed by the initial direction and averages the two "
    "lab-frame components. For an isotropic Gaussian of total variance T, E[sin^2 theta]/T = 1 - (2/3)T + (4/15)T^2 "
    "- (8/105)T^3 + O(T^4). With T = A(3 beta)/(3 beta) the linear deficit is 0.09259 at beta = 2 and 0.00913 at "
    "beta = 24, and beta times that deficit tends to 2/9. The attempt's summary states 0.0300 and 0.00309 instead. "
    "The corrected quadratic ratio at beta = 2 is 0.9126, below the quoted table 0.95-0.99, so this factor at T = sigma^2 "
    "is too large to be the whole measured ratio. It remains below 1, so it does not produce the values above 1. "
    "The formation runs were not repeated, and the Gaussian hypothesis was not proved.",
    flush=True,
)
print(
    "HIT: confirmed - the lab-frame Gaussian ratio is 1 - (2/3)T + (4/15)T^2 - (8/105)T^3 + O(T^4), "
    "and at T = A(3 beta)/(3 beta) the deficit is 0.09259 at beta = 2 and 0.00913 at beta = 24, "
    "not the stated 0.030 and 0.0031",
    flush=True,
)
