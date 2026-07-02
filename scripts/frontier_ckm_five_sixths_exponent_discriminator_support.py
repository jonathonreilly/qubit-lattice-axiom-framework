"""Paired runner for CKM_FIVE_SIXTHS_EXPONENT_DISCRIMINATOR_SUPPORT_NOTE_2026-07-02.md.

Exponent discriminator table + exact one-loop transport decomposition for the
bounded five-sixths CKM-to-mass-ratio bridge lane. All quantities are computed
from N=3 Casimir arithmetic and the stated atlas coupling; PDG numbers enter
comparator-only, on the comparison side of gates.
"""
from fractions import Fraction
from math import floor, log, log10, sqrt


PASS_COUNT = 0
FAIL_COUNT = 0


def fmt10(value):
    if value == 0:
        return "0.000000000"
    places = 10 - floor(log10(abs(value))) - 1
    if places < 0:
        return f"{value:.10g}"
    return f"{value:.{places}f}"


def pct3(value):
    return f"{value:+.3f}%"


def signed_fmt10(value):
    return f"{'+' if value >= 0 else '-'}{fmt10(abs(value))}"


def check(name, condition, detail):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL {name}: {detail}")


C_F = Fraction(4, 3)
T_F = Fraction(1, 2)
C_A = Fraction(3, 1)
N_F = 4

ALPHA_V = 0.103303816122
THRESHOLD_M_S_COMPARATOR_ONLY = 0.0934
THRESHOLD_M_B_COMPARATOR_ONLY = 4.180
ALPHA_S_2GEV_COMPARATOR_ONLY = 0.2965
ALPHA_S_MB_COMPARATOR_ONLY = 0.2265

FIVE_SIXTHS = C_F - T_F
GAMMA0 = 6 * C_F
BETA0 = Fraction(11, 1) - Fraction(2 * N_F, 3)
TRANSPORT_EXPONENT = GAMMA0 / (2 * BETA0)

VCB_ATLAS = ALPHA_V / sqrt(6)
THRESHOLD_COMPARATOR = (
    THRESHOLD_M_S_COMPARATOR_ONLY / THRESHOLD_M_B_COMPARATOR_ONLY
)

CANDIDATES = [
    ("C_F-T_F=5/6", FIVE_SIXTHS),
    ("6/7", Fraction(6, 7)),
    ("adjoint fraction 8/9", Fraction(8, 9)),
    ("3/4", Fraction(3, 4)),
    ("(C_F-T_F)/C_F=5/8", FIVE_SIXTHS / C_F),
    ("T_F=1/2", T_F),
    ("1", Fraction(1, 1)),
    ("C_F=4/3", C_F),
    ("C_A-C_F=5/3", C_A - C_F),
]


def ratio_for_exponent(exponent):
    return VCB_ATLAS ** float(Fraction(1, 1) / exponent)


def deviation_pct(ratio):
    return (ratio / THRESHOLD_COMPARATOR - 1) * 100


print(f"INPUT alpha_v={ALPHA_V}")
print(f"INPUT Vcb_atlas={fmt10(VCB_ATLAS)}")
print(
    "COMPARATOR_ONLY threshold="
    "(0.0934/4.180)"
    f"={fmt10(THRESHOLD_COMPARATOR)}"
)
print(
    "COMPARATOR_ONLY transport_alpha="
    f"({ALPHA_S_2GEV_COMPARATOR_ONLY}/{ALPHA_S_MB_COMPARATOR_ONLY})"
)
print("DISCRIMINATOR_TABLE")
print("candidate | exponent | ratio_pred | dev_pct")

rows = []
for label, exponent in CANDIDATES:
    ratio = ratio_for_exponent(exponent)
    dev = deviation_pct(ratio)
    rows.append((label, exponent, ratio, dev))
    print(f"{label} | {exponent} | {fmt10(ratio)} | {pct3(dev)}")

dev_by_label = {label: dev for label, _, _, dev in rows}
ratio_by_label = {label: ratio for label, _, ratio, _ in rows}
five_dev = dev_by_label["C_F-T_F=5/6"]
competitor_devs = [
    abs(dev) for label, dev in dev_by_label.items() if label != "C_F-T_F=5/6"
]
margin = min(competitor_devs) / abs(five_dev)

E_FIT = log(VCB_ATLAS) / log(THRESHOLD_COMPARATOR)
E_FIT_REL_GAP = abs(E_FIT - float(FIVE_SIXTHS)) / float(FIVE_SIXTHS)

TRANSPORT_FACTOR = (
    ALPHA_S_2GEV_COMPARATOR_ONLY / ALPHA_S_MB_COMPARATOR_ONLY
) ** float(TRANSPORT_EXPONENT)
SAME_SCALE_DEV = (
    ratio_by_label["C_F-T_F=5/6"] * TRANSPORT_FACTOR / THRESHOLD_COMPARATOR - 1
) * 100

WRONG_DIRECTION_RATIO = VCB_ATLAS ** float(FIVE_SIXTHS)
WRONG_DIRECTION_DEV = deviation_pct(WRONG_DIRECTION_RATIO)

print(f"MARGIN nearest_competitor_over_five_sixths={fmt10(margin)}x")
print(
    "EMPIRICAL_EXPONENT "
    f"e_fit={fmt10(E_FIT)} rel_gap={fmt10(E_FIT_REL_GAP)}"
)
print(
    "TRANSPORT "
    f"factor={fmt10(TRANSPORT_FACTOR)} "
    f"same_scale_dev_pct={signed_fmt10(SAME_SCALE_DEV)}% "
    f"same_scale_dev_pct_table={pct3(SAME_SCALE_DEV)}"
)
print(
    "WRONG_DIRECTION "
    f"ratio={fmt10(WRONG_DIRECTION_RATIO)} dev_pct={pct3(WRONG_DIRECTION_DEV)}"
)

check("G1 C_F-T_F", FIVE_SIXTHS == Fraction(5, 6), f"value={FIVE_SIXTHS}")
check("G1 gamma0", GAMMA0 == 8, f"value={GAMMA0}")
check("G1 beta0", BETA0 == Fraction(25, 3), f"value={BETA0}")
check(
    "G1 transport exponent",
    TRANSPORT_EXPONENT == Fraction(12, 25),
    f"value={TRANSPORT_EXPONENT}",
)
check(
    "G2 Vcb_atlas chain",
    abs(VCB_ATLAS - 0.04217360633) < 1e-9,
    f"value={fmt10(VCB_ATLAS)}",
)
check(
    "G3 five-sixths discriminator window",
    0 < five_dev < 0.5,
    f"dev={pct3(five_dev)}",
)

for label, dev in dev_by_label.items():
    if label == "C_F-T_F=5/6":
        continue
    check(
        f"G3 competitor rejector {label}",
        abs(dev) > 5,
        f"dev={pct3(dev)}",
    )

check("G4 margin", margin > 50, f"margin={fmt10(margin)}x")
check(
    "G5 empirical exponent",
    E_FIT_REL_GAP < 0.001,
    f"e_fit={fmt10(E_FIT)} rel_gap={fmt10(E_FIT_REL_GAP)}",
)
check(
    "G6 transport factor",
    1.10 < TRANSPORT_FACTOR < 1.17,
    f"factor={fmt10(TRANSPORT_FACTOR)}",
)
check(
    "G6 same-scale deviation",
    10 < SAME_SCALE_DEV < 18,
    f"same_scale_dev={pct3(SAME_SCALE_DEV)}",
)
check(
    "G7 wrong-direction rejector",
    abs(WRONG_DIRECTION_DEV) > 5,
    f"dev={pct3(WRONG_DIRECTION_DEV)}",
)

total = PASS_COUNT + FAIL_COUNT
print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
if FAIL_COUNT:
    raise SystemExit(1)
