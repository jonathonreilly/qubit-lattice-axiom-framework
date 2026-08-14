from __future__ import annotations
NOTE_NAME = "TWO_CUBE_L1_TICK3_BOUNDED_THEOREM_NOTE_2026-08-14.md"

from fractions import Fraction
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / "docs" / NOTE_NAME
AUDIT_INPUT_PATHS = ("docs/TWO_CUBE_L1_TICK3_BOUNDED_THEOREM_NOTE_2026-08-14.md", "docs/MINIMAL_AXIOMS_2026-06-29.md")
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "exhausted", "only route", "we adopt", "Codex", "L_phys")
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SEED = (0, 0, 0)

def verts():
    return tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))

def in_A(v):
    return v[0] in (0, 1)

def in_B(v):
    return v[0] in (1, 2)

def occ(v, locks):
    return 1 if v in locks else 0

def nvec(site, locks):
    V = set(verts())
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        op = occ(plus, locks) if plus in V else 0
        om = occ(minus, locks) if minus in V else 0
        out.append(Fraction(op - om, 3))
    return tuple(out)

def k_of(n):
    return int(sum((3 * c) ** 2 for c in n))

def step(locks):
    new = set(locks)
    formed = set()
    for v in verts():
        if v not in locks and any(c != 0 for c in nvec(v, locks)):
            new.add(v)
            formed.add(v)
    return frozenset(new), frozenset(formed)

def evolve(ticks):
    locks = frozenset({SEED})
    hist = [locks]
    formed = [frozenset()]
    for _ in range(ticks):
        locks, fr = step(locks)
        hist.append(locks)
        formed.append(fr)
    return hist, formed

def rho(locks):
    a = sum(1 for v in locks if in_A(v))
    b = sum(1 for v in locks if in_B(v))
    return a, b

class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0
    def check(self, label, statement, cond):
        self.passed += int(bool(cond))
        self.failed += int(not cond)
        print(f"{'PASS' if cond else 'FAIL'}: {label} {statement}")
    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed

def hygiene(checks):
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    checks.check("thm0", "Lattice quote present", "proper cubic rotations" in axiom)
    for s in FORBIDDEN:
        checks.check("hygiene", f"avoids {s!r}", s not in note)


def main():
    checks = Checks()
    hygiene(checks)
    hist, formed = evolve(3)
    fr = formed[3]
    checks.check("thm1", "tick3 forms three sites", fr == frozenset({(1,1,1),(2,1,0),(2,0,1)}))
    checks.check("thm1", "(2,1,1) unread at t=3", (2,1,1) not in hist[3])
    checks.check("thm2", "k at (1,1,1) is 3", k_of(nvec((1,1,1), hist[2])) == 3)
    checks.check("thm2", "k at (2,1,0) is 2", k_of(nvec((2,1,0), hist[2])) == 2)
    checks.check("thm2", "k at (2,0,1) is 2", k_of(nvec((2,0,1), hist[2])) == 2)
    checks.check("thm2", "n at (2,1,1) is 0", nvec((2,1,1), hist[2]) == (0,0,0))
    print("per_mode: tick-3 k table")
    print("per_block: d=3 layer")
    print("lattice_wide: checked and not executed")
    return checks.finish()
if __name__ == "__main__":
    raise SystemExit(main())
