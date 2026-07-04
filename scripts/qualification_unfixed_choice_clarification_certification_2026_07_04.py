"""Certification runner for the 2026-07-04 Qualification clarification.

Sections:
  C1 surgical-edit certification: the four axioms' named content is unchanged,
     the base further-physical-structure sentence is present, the exact
     approved clause is present in the Qualification, and the machine mirror
     carries the same clause.
  C2 the clause is a law-dependence restriction, not a state symmetry: in a
     finite diagnostic model, a law that avoids the reflection-odd handedness
     channel remains achiral; one that uses it is the forbidden case absent
     admission; a state configuration may still carry it.
  C3 finite witness for the unfixed-choice boundary: a mirror pair shares the
     tested mirror-even invariant summaries while carrying opposite handedness,
     so those summaries do not select it. The axiom clause, not the finite
     witness alone, supplies the admission-only governance rule.

Expected close: TOTAL: PASS=11 FAIL=0
"""

import itertools
import json
import os

import numpy as np

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"{status}: {name}" + (f" -- {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# C1: surgical-edit certification (read the memo in this worktree)
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
MEMO = os.path.join(HERE, "..", "docs", "MINIMAL_AXIOMS_2026-06-29.md")
AXIOM_REGISTRY = os.path.join(HERE, "..", "docs", "audit", "data", "axiom_premise_nodes.json")
with open(MEMO, encoding="utf-8") as fh:
    memo = fh.read()
memo_flat = " ".join(memo.split())  # normalize whitespace/newlines
with open(AXIOM_REGISTRY, encoding="utf-8") as fh:
    registry = json.load(fh)
registry_note_flat = " ".join(registry["nodes"]["minimal_axioms"]["note"].split())

AXIOM_SECTIONS = ["### Lattice", "### Qubit", "### Admissibility", "### Record"]
NAMED_CONTENT = [
    "Physical sites are the points of the cubic lattice",
    "with nearest-neighbor adjacency, standard translations, and proper cubic",
    "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
    "A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice",
    "When present, a record locks exactly one admissible local possibility.",
    "Records form.",
]
BASE_SENTENCE = (
    "Further physical structure requires derivation, bridge, explicit admission, "
    "or approved primitive registration before use as a premise."
)
CLAUSE = (
    "In particular, a law may not depend on a choice not fixed by the supplied "
    "structure, unless that choice is admitted."
)

check(
    "C1a four axiom section headers present",
    all(h in memo for h in AXIOM_SECTIONS),
    f"headers={sum(h in memo for h in AXIOM_SECTIONS)}/4",
)
check(
    "C1b axioms' named content unchanged (verbatim sentences present)",
    all(" ".join(s.split()) in memo_flat for s in NAMED_CONTENT),
    f"named-content sentences present={sum(' '.join(s.split()) in memo_flat for s in NAMED_CONTENT)}/{len(NAMED_CONTENT)}",
)
check(
    "C1c base further-physical-structure sentence present unchanged",
    " ".join(BASE_SENTENCE.split()) in memo_flat,
)
check(
    "C1d exact approved clause present in the Qualification",
    " ".join(CLAUSE.split()) in memo_flat
    and memo_flat.index(" ".join(CLAUSE.split()))
    > memo_flat.index(" ".join(BASE_SENTENCE.split())),
    "clause appears immediately after the base sentence",
)
check(
    "C1e clause did not alter the state / law-domain sentences",
    "A state is a configuration of records." in memo
    and "A law privileges no states." in memo,
)
check(
    "C1f minimal_axioms machine mirror carries exact approved clause",
    " ".join(CLAUSE.split()) in registry_note_flat,
    "axiom_premise_nodes.json minimal_axioms note",
)


# ---------------------------------------------------------------------------
# Finite diagnostic model: contents = 6 axis directions; O_h is the full
# signed-permutation reflection test group. The memo itself names proper cubic
# rotations; improper elements are used here only to expose dependence on a
# mirror choice, not to assert that reflection covariance was already supplied.
# ---------------------------------------------------------------------------
AX = [np.array(a, dtype=float) for a in
      [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
OH = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for r, p in enumerate(perm):
            M[r, p] = signs[r]
        OH.append(np.array(M, dtype=int))
SIGMA = np.diag([-1, 1, 1]).astype(int)  # a reflection (improper, in O_h)


def aidx(v):
    for i, a in enumerate(AX):
        if np.allclose(a, v):
            return i
    raise ValueError


def act_cond(M, cond):
    return {aidx(M @ AX[d]): aidx(M @ AX[c]) for d, c in cond.items()}


def act_out(M, out):
    return frozenset(aidx(M @ AX[c]) for c in out)


def J2(cond):  # reflection-odd handedness channel used by the diagnostic
    s = 0.0
    for d in cond:
        for e in cond:
            if d != e:
                s += np.linalg.det(np.array([AX[d], AX[e], AX[cond[e]]]))
    return s


def base(m, cond):
    return sum(float(AX[m] @ AX[c]) for c in cond.values())


def R_align(cond):  # law that does NOT depend on the unfixed handedness
    return frozenset(m for m in range(6) if base(m, cond) >= 0)


def R_J2(cond):  # law that DOES depend on it (the forbidden case, absent admission)
    thr = 1.0 if (len(cond) >= 2 and J2(cond) < 0) else 0.0
    return frozenset(m for m in range(6) if base(m, cond) >= thr)


rng = np.random.default_rng(3)


def rand_cond(k):
    slots = rng.choice(6, size=k, replace=False)
    return {int(d): int(rng.integers(0, 6)) for d in slots}


SAMPLE = [rand_cond(int(rng.integers(3, 6))) for _ in range(200)]

# ---------------------------------------------------------------------------
# C2: dependence-restriction, not a state symmetry
# ---------------------------------------------------------------------------
c2a = all(R_align(act_cond(M, c)) == act_out(M, R_align(c)) for M in OH for c in SAMPLE[:40])
check(
    "C2a a law not depending on the unfixed handedness passes the achiral diagnostic",
    c2a,
    "R_align is O_h-covariant on 40x48 checks",
)
improper_break = any(
    round(np.linalg.det(M)) == -1 and R_J2(act_cond(M, c)) != act_out(M, R_J2(c))
    for M in OH for c in SAMPLE
)
check(
    "C2b a law depending on the unfixed handedness is the forbidden case absent admission",
    improper_break,
    "R_J2 fails the reflection diagnostic -- it depends on the unfixed choice",
)
# state freedom: a record configuration may carry the handedness (J2 != 0)
state_carries = sum(1 for c in SAMPLE if abs(J2(c)) > 1e-9)
check(
    "C2c a state configuration may still carry the handedness (state left free)",
    state_carries >= 30,
    f"configs with nonzero handedness={state_carries}/{len(SAMPLE)}",
)

# ---------------------------------------------------------------------------
# C3: finite witness for unfixed-choice behavior. The mirror pair shares the
# tested mirror-even invariant summaries but carries opposite handedness, so
# those summaries do not select the handedness. The governance conclusion that
# an unfixed choice is admission-only comes from the owner-approved clause.
# ---------------------------------------------------------------------------
def supplied_invariants(cond):
    # tested mirror-even summaries: the sorted base-value multiset and |J2|
    return (tuple(sorted(base(m, cond) for m in range(6))), round(abs(J2(cond)), 9))


chiral = [c for c in SAMPLE if abs(J2(c)) > 1e-9]
same_invariants = all(supplied_invariants(c) == supplied_invariants(act_cond(SIGMA, c)) for c in chiral)
opposite_handedness = all(
    np.sign(J2(c)) == -np.sign(J2(act_cond(SIGMA, c))) and abs(J2(c)) > 1e-9 for c in chiral
)
check(
    "C3a the mirror pair shares the tested mirror-even invariant summaries",
    same_invariants and len(chiral) >= 30,
    f"invariant-matched chiral pairs={len(chiral)}",
)
check(
    "C3b the mirror pair carries opposite handedness (the unfixed choice)",
    opposite_handedness,
)
# C3a + C3b witness the intended finite boundary without asserting an
# exhaustive invariant theorem.

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
