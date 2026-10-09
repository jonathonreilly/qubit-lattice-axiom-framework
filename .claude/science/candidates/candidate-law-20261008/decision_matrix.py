"""Decision matrix for candidate laws: rank every combination of fork settings.

Planning tool, not science. Every number below is a supervisor prior
(a judgement, stated with its one-line reason), not a computed result.
The ranking is what matters; the absolute products are not probabilities
of anything measurable.

Iteration rule: when a candidate is run against a check, record the outcome
in RESULTS (pass -> 1, fail -> 0) keyed by the check and the candidate's
settings on that check's dependency forks. A failure therefore removes every
combination that shares those settings, and the next-ranked survivor is the
next candidate. A diagnosis that blames fewer forks may record a narrower key.

Run: python3 decision_matrix.py [--top N] [--sensitivity] [--physics-only]
(--physics-only drops K0, the fit to the four axioms, from the product.)
"""

from itertools import product
import sys

# ---------------------------------------------------------------- forks

FORKS = {
    "motion": {
        "H": "continuous-time local Hamiltonian, time not a lattice direction (Lieb-Robinson cone)",
        "Q": "hypercubic tick: time is a lattice direction with the same step as space",
    },
    "turns": {
        "L": "turns act up to a site-local U(1) frame (main's kinetic-class reading; staggered signs)",
        "E": "turns act exactly: every site's possibilities turn rigidly with the grid (owner Q3)",
    },
    "room": {
        "P": "one qubit per site, sites given jobs by a pattern (2x2x2 or larger cell)",
        "M": "more room per site (several qubits or primitive fermion modes)",
        "U": "one qubit per site, uniform; everything emergent from the vacuum",
        "O": "continuous variables per site (oscillators) plus fermion modes: ordinary lattice fields",
    },
    "records": {
        "B": "Bell-type beables: occupations of matter sites, jump with the wave's flow",
        "F": "collapse flashes: rare permanent events, rate set by mass (GRW/CSL-like)",
        "D": "decoherence-defined: stable redundant pointer states, no new dynamics",
    },
    "gravity": {
        "G": "emergent helicity-2 collective mode of the same vacuum",
        "X": "explicit metric/shape field as an extra degree of freedom",
        "I": "induced/entanglement gravity (Sakharov, Jacobson), no separate mode",
        "R": "record-carried: records source and carry gravity",
    },
}
ORDER = ["motion", "turns", "room", "records", "gravity"]

CANDIDATE_1 = {"motion": "Q", "turns": "L", "room": "O", "records": "B", "gravity": "X"}

# ------------------------------------------------------- check factors
# Each check returns a prior pass factor from the settings on its dependency
# forks. Reasons are in DECISION_MATRIX.md, one line per number.


def k1_light(s):
    # 3D photon: gapless linear mode, Coulomb law.
    if s["motion"] == "Q" and s["turns"] == "E" and s["room"] == "U":
        return 0.0  # campaign 8 A42: nothing moves
    base = {"P": 0.45, "M": 0.50, "U": 0.10, "O": 0.85}[s["room"]]
    if s["motion"] == "Q":
        base *= 0.85
    if s["room"] == "U" and s["turns"] == "E":
        base *= 0.7
    return base


def k2_matter(s):
    # One-handed fermions with the Standard Model gauge structure.
    base = {
        ("L", "P"): 0.03, ("L", "M"): 0.15, ("L", "U"): 0.03, ("L", "O"): 0.20,
        ("E", "P"): 0.04, ("E", "M"): 0.08, ("E", "U"): 0.02, ("E", "O"): 0.10,
    }[(s["turns"], s["room"])]
    if s["motion"] == "Q":
        base *= 0.5  # K2a: the body-diagonal mirror selector exists only in continuous time
    return base


def k3_gravity(s):
    # Newton, light bending x2, equivalence to 1e-15, c_grav = c to 1e-15.
    base = {
        ("G", "P"): 0.02, ("G", "M"): 0.02, ("G", "U"): 0.015, ("G", "O"): 0.035,
        ("X", "P"): 0.008, ("X", "M"): 0.008, ("X", "U"): 0.004, ("X", "O"): 0.025,
        ("I", "P"): 0.02, ("I", "M"): 0.02, ("I", "U"): 0.02, ("I", "O"): 0.02,
        ("R", "P"): 0.01, ("R", "M"): 0.01, ("R", "U"): 0.01, ("R", "O"): 0.01,
    }[(s["gravity"], s["room"])]
    if s["turns"] == "E":
        base *= 0.8
    return base


def k4_quantum(s):
    # Born odds, one click per photon, CHSH 2.83.
    return {"B": 0.90, "F": 0.85, "D": 0.85}[s["records"]]


def k5_record_data(s):
    # Heating, spontaneous X-rays, no anomalous record effects.
    return {"B": 0.95, "F": 0.10, "D": 0.95}[s["records"]]


def k6_numbers(s):
    # Three generations, alpha, mass ratios.
    return {
        ("L", "P"): 0.04, ("L", "M"): 0.04, ("L", "U"): 0.02, ("L", "O"): 0.04,
        ("E", "P"): 0.02, ("E", "M"): 0.02, ("E", "U"): 0.01, ("E", "O"): 0.02,
    }[(s["turns"], s["room"])]


def k7_one_cone(s):
    # Photon, matter and graviton speeds equal (GW170817, Lorentz tests).
    return {"H": 0.10, "Q": 0.30}[s["motion"]]  # K7a PASS: hypercubic forms exist; Q forbids
    # dimension-4 speed splits only if every sector's Euclidean form is hypercubic


AXIOM_FIT = {
    "motion": {"H": 1.0, "Q": 1.0},
    "turns": {"L": 0.95, "E": 1.0},
    "room": {"P": 0.6, "M": 0.5, "U": 1.0, "O": 0.2},
    "records": {"B": 0.6, "F": 0.95, "D": 0.4},
    "gravity": {"G": 1.0, "X": 0.6, "I": 0.9, "R": 1.0},
}


def k0_axiom_fit(s):
    out = 1.0
    for fork in ORDER:
        out *= AXIOM_FIT[fork][s[fork]]
    return out


CHECKS = [
    ("K1 light", ["motion", "turns", "room"], k1_light),
    ("K2 matter", ["motion", "turns", "room"], k2_matter),
    ("K3 gravity", ["turns", "room", "gravity"], k3_gravity),
    ("K4 quantum", ["records"], k4_quantum),
    ("K5 records", ["records"], k5_record_data),
    ("K6 numbers", ["turns", "room"], k6_numbers),
    ("K7 one-cone", ["motion", "gravity"], k7_one_cone),
    ("K0 axioms", ORDER, k0_axiom_fit),
]

# ------------------------------------------------------------- results
# Recorded outcomes: (check name, ((fork, option), ...)) -> 0 or 1.
# Empty until checks run. Example after a failure of Candidate 1 on K2:
#   ("K2 matter", (("motion", "H"), ("turns", "L"), ("room", "P"))): 0,
RESULTS = {}


def factor(check, deps, fn, s):
    for (name, key), value in RESULTS.items():
        if name == check and all(s[f] == o for f, o in key):
            return float(value)
    return fn(s)


PHYSICS_ONLY = False


def score(s):
    parts = [factor(name, deps, fn, s) for name, deps, fn in CHECKS]
    total = 1.0
    for (name, _, _), p in zip(CHECKS, parts):
        if PHYSICS_ONLY and name.startswith("K0"):
            continue
        total *= p
    return total, parts


def all_settings():
    for combo in product(*(FORKS[f].keys() for f in ORDER)):
        yield dict(zip(ORDER, combo))


def label(s):
    return "".join(s[f] for f in ORDER)


def main(argv):
    global PHYSICS_ONLY
    PHYSICS_ONLY = "--physics-only" in argv
    top = 15
    if "--top" in argv:
        top = int(argv[argv.index("--top") + 1])
    rows = sorted(((score(s), s) for s in all_settings()), key=lambda r: -r[0][0])
    best = rows[0][0][0]
    mode = "physics only (K0 dropped)" if PHYSICS_ONLY else "physics x axiom fit"
    print(f"{len(rows)} combinations; forks in order {ORDER}; score = {mode}")
    print("rank  code   rel.   " + "  ".join(n.split()[0] for n, _, _ in CHECKS))
    for i, ((total, parts), s) in enumerate(rows[:top], 1):
        mark = "  <- Candidate 1" if s == CANDIDATE_1 else ""
        cells = "  ".join(f"{p:.2f}" for p in parts)
        print(f"{i:>4}  {label(s)}  {total / best:5.3f}  {cells}{mark}")
    zero = sum(1 for (t, _), _ in rows if t == 0.0)
    print(f"combinations at zero (proved no-go or recorded failure): {zero}")
    if "--sensitivity" in argv:
        print("\nbest relative score with each option held fixed:")
        for fork in ORDER:
            for opt in FORKS[fork]:
                b = max(t for (t, _), s in rows if s[fork] == opt)
                print(f"  {fork:8} {opt}  {b / best:5.3f}  {FORKS[fork][opt]}")


if __name__ == "__main__":
    main(sys.argv[1:])
