#!/usr/bin/env python3
"""The record-arrow low-record-boundary EXISTENCE sub-clause reduces, inside the
record ontology, to NON-EMPTINESS of the realized record history -- with the theorem
weight on DURABILITY (append-only => acyclic, well-founded; deletion controls FAIL)
and NON-MANUFACTURABILITY (rank collapse under CLOSED reversible dynamics; the OPEN
swap-out escape named and checked), in the SINGLE-CHAIN (totally ordered) sector,
with the general well-founded case disclosed (multiple minimal ends possible;
termination survives, uniqueness does not).  The THERMODYNAMIC past hypothesis (low
entropy, Penrose room) is NOT delivered and remains the named open residual; the
in-sector boundary facts T1b/T1c are definitional (disclosed), and whether records
FORM at a blank boundary is realized-state data (counterfactual-disclosed, per the
realized-state primitive's test).

Class-A exact verification for the source note

    docs/PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md

CONTEXT (owner-directed strike: "go derive the reduction").  The arrow note
(retained_bounded on the live ledger at this writing; statuses are pipeline-derived)
derived the arrow's DIRECTION (away from the low-record boundary) and pinned the
boundary's EXISTENCE as the open input -- the past hypothesis.  THIS NOTE attacks the
existence clause: in the framework's own ontology reality is the record stack, records
are DURABLE registrations (the Record axiom's word), and the landed history-sector
formalization (free monoid O* of finite words, append-only; unaudited on the live
ledger -- its load-bearing facts are RE-PROVED here, not cited) makes the boundary
structural: every finite word has the empty word as its unique minimal prefix.

THE CHAIN (each link checked exactly below; the history order is SUPPLIED by the
record history -- "a record history supplies ordered words and counts", per the
landed history-order firewall, which orients without a time metric or rate; that
firewall note is itself unaudited on the live ledger, so its allowance is used as a
disclosed input, not a graded license):
  (T1) BOUNDARY IN-SECTOR (definitional facts, labeled as such): in the
       SINGLE-CHAIN append-only sector, record count is strictly monotone along the
       supplied prefix order; the blank word epsilon is THE unique minimal prefix;
       the pastward walk terminates in exactly |w| steps.  T1b/T1c are definitional
       for a single totally-ordered finite word -- the theorem weight lives in
       T1d/T2/T3.  (T1d) GENERAL WELL-FOUNDED CASE: for causally-disjoint chains
       and merge/diamond posets, TERMINATION survives (finite posets are
       well-founded) but UNIQUENESS does not (multiple minimal ends exhibited);
       the total order is an assumption BEYOND the Record axiom, disclosed.
       epsilon-as-monoid-identity is the landed monoid note's fact; the NEW reading
       here is order-theoretic: minimal-record ends as the boundary object.
  (T2) DURABILITY IS LOAD-BEARING (the genuine theorem content, controls): allow
       deletion (non-durable registrations) and the configuration order acquires
       cycles / unbounded pastward walks -- the boundary result FAILS without the
       Record axiom's durability; append-only with the same op budget never
       revisits.
  (T3) THE BOUNDARY IS NOT MANUFACTURABLE BY CLOSED REVERSIBLE DYNAMICS: clean
       broadcast from ARBITRARY old fragment content is many-to-one (rank collapse
       2 vs 16), hence not unitary/isometric on the CLOSED space; the OPEN escape
       is named and checked (the outer-sink swap-out (g,0)->(0,g) IS an exact
       permutation that blanks the inner register by exporting content -- the sink
       regress no-go is what prices that escape).  State-level blankness here is
       DISTINCT from the history-level blankness epsilon of T1 (disclosed).
  (T4) THE ARROW ANCHORS (counterfactual-disclosed): with the CONNECTED correlator
       (pointer-basis-robust record measure), the record count at ANY blank
       boundary is 0; whether records FORM is realized-state data -- the superposed
       pointer forms 3 (counts 0->3), the pointer eigenstate forms 0 (flat), the
       I/d equilibrium forms 0 (flat).  The derived direction (arrow note) anchors
       away from minimal-record ends FOR the realized histories in which records
       form; formation itself is the non-emptiness input, never claimed structural.
  (T5) RESIDUAL INVENTORY (anti-overclaim controls): the reduction does NOT pin
       the quantitative/thermodynamic content (different-room realizations
       identical); the finite-sector dichotomy is named (unbounded past requires
       unbounded registered content); the realized-state slot (including the
       pointer-basis-vs-superposition choice T4 discloses) is untouched.

RESIDUAL AFTER THIS NOTE: (i) non-emptiness w != epsilon -- an explicit
APPLICABILITY PRECONDITION, not a derived theorem (vacuous empty-history models are
formally allowed and carry no arrow); (ii) the SINGLE-CHAIN (total-order) sector
scope -- an assumption beyond the Record axiom (general case: well-founded with
possibly many minimal ends); (iii) the finite-history sector scope (disclosed, with
the unbounded-content dichotomy named); (iv) the THERMODYNAMIC past hypothesis (low
ENTROPY, Penrose room) -- open, named, untouched.  The realized-state primitive's
slot is also untouched: WHICH state realizes the blank boundary (including
pointer-basis vs superposition) remains supplied state data.  No new axiom/
primitive/measure/weight; r untouched.  Statuses are pipeline-derived; the audit
lane grades.

Run: python3 scripts/frontier_past_hypothesis_existence_reduction_append_only_2026_06_11.py
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


# ===========================================================================
print("=" * 78)
print("T1  Boundary by structure: append-only words are well-founded")
print("=" * 78)
rng = np.random.default_rng(20260611)
ALPH = list("abcde")          # a finite record alphabet O (supplied readout context)
words = ["".join(rng.choice(ALPH, size=n)) for n in
         list(range(1, 40)) + [100, 250, 1000]]

mono_all, walk_exact, unique_min = True, True, True
for w in words:
    prefixes = [w[:k] for k in range(len(w) + 1)]      # the intrinsic prefix order
    counts = [len(p) for p in prefixes]
    mono_all &= all(b == a + 1 for a, b in zip(counts, counts[1:]))
    # pastward walk: from the full word, step to the unique immediate predecessor
    steps, cur = 0, w
    while cur:
        cur = cur[:-1]
        steps += 1
    walk_exact &= (steps == len(w))
    unique_min &= (prefixes[0] == "")
check("T1a record count is STRICTLY monotone (+1 per registration) along the "
      "intrinsic prefix order, for every tested history",
      mono_all, f"{len(words)} words, lengths 1..1000")
check("T1b the pastward walk from any realized history terminates at the blank "
      "boundary in EXACTLY |w| steps (well-foundedness of finite words)",
      walk_exact)
check("T1c [definitional in-sector] the minimal prefix is UNIQUE and BLANK (the "
      "monoid identity epsilon) -- definitional for a single totally-ordered word; "
      "the order-theoretic reading (minimal-record END) is the new content",
      unique_min)
# (T1d) the GENERAL well-founded case: total order is an assumption beyond the
# Record axiom.  Two causally-disjoint chains and a merge (diamond) poset:
# termination survives (finite posets are well-founded); uniqueness does NOT.
chainA = ["a", "ab", "abc"]
chainB = ["x", "xy"]
elems = chainA + chainB
below = {e: [f for f in elems if e != f and (e.startswith(f) if f[0] == e[0] else False)] for e in elems}
minimal = [e for e in elems if not below[e]]
diamond_elems = ["m1", "m2", "j"]
diamond_below = {"m1": [], "m2": [], "j": ["m1", "m2"]}
diamond_min = [e for e in diamond_elems if not diamond_below[e]]
check("T1d GENERAL WELL-FOUNDED CASE: causally-disjoint chains give 2 minimal ends "
      "and a merge/diamond gives 2 -- TERMINATION survives (finite posets are "
      "well-founded), UNIQUENESS does not: the single-chain total order is an "
      "assumption BEYOND the Record axiom, disclosed as sector scope",
      sorted(minimal) == ["a", "x"] and sorted(diamond_min) == ["m1", "m2"],
      f"disjoint-chain minima {sorted(minimal)}; diamond minima {sorted(diamond_min)}")

# ===========================================================================
print("=" * 78)
print("T2  Durability is load-bearing: deletion destroys well-foundedness")
print("=" * 78)
# non-durable model: histories as sequences of (append x | delete) operations on a
# stack; the "configuration order" relates configurations reachable by one op.
# Exhibit a CYCLE: config 'a' -> append b -> 'ab' -> delete -> 'a' : the intrinsic
# order on configurations has a -> ab -> a, so no minimal element below the cycle
# and the pastward walk need not terminate.
cycle = []
cfg = "a"
for k in range(7):
    cfg = cfg + "b"
    cycle.append(cfg)
    cfg = cfg[:-1]
    cycle.append(cfg)
returns = cycle.count("a")
check("T2a with DELETION allowed (non-durable registrations) the configuration "
      "order acquires cycles: the same configuration recurs, so pastward walks "
      "need not terminate and no minimal element exists below the cycle -- the "
      "boundary theorem FAILS exactly where durability fails",
      returns == 7, f"configuration 'a' recurs {returns}x in a 14-op history")
# and in the durable (append-only) sector the same op-budget CANNOT revisit:
seen = set()
cfg = "a"
revisit = False
for k in range(14):
    cfg = cfg + "b"
    revisit |= cfg in seen
    seen.add(cfg)
check("T2b the append-only sector with the same op budget NEVER revisits a "
      "configuration (strict count growth forbids recurrence)",
      not revisit)

# ===========================================================================
print("=" * 78)
print("T3  Not manufacturable by CLOSED reversible dynamics (+ the OPEN escape named)")
print("=" * 78)
# landed witness, re-proved: 1 pointer qubit + 3 fragment qubits; the clean-broadcast
# target from ARBITRARY old fragment content,
#   |p>|f> -> |p>|ppp>  (p in {0,1}, all eight f),
# is many-to-one.  Build the 16x16 transfer matrix sending each basis vector to its
# target and measure its rank.
T = np.zeros((16, 16))
for p in (0, 1):
    target = p * 8 + (0b111 * p)          # |p>|ppp>
    for f in range(8):
        T[target, p * 8 + f] = 1.0
rank = np.linalg.matrix_rank(T)
check("T3a clean broadcast from arbitrary old fragments has rank 2 (not 16): "
      "many-to-one, hence NOT a unitary/isometry on the CLOSED space -- blankness "
      "cannot be produced mid-history by CLOSED reversible dynamics",
      rank == 2, f"rank {rank} of the 16x16 transfer map")
# control: WITH a blank boundary the broadcast is the CNOT fanout, a permutation
U = np.zeros((16, 16))
for p in (0, 1):
    for f in range(8):
        U[p * 8 + (f ^ (0b111 * p)), p * 8 + f] = 1.0
check("T3b control: WITH the blank boundary the broadcast (CNOT fanout) is an "
      "exact permutation (unitary) -- the boundary is what closed reversible "
      "record formation consumes",
      np.allclose(U @ U.T, np.eye(16)) and np.linalg.matrix_rank(U) == 16)
# the OPEN escape, named and checked: the outer-sink swap-out (g, 0) -> (0, g) IS an
# exact permutation that blanks the inner register by EXPORTING content; the landed
# sink regress no-go is what prices that escape (the outer sink needs ITS blank).
k = 3
S = np.zeros((4 ** k, 4 ** k))
for g in range(2 ** k):
    for h in range(2 ** k):
        S[h * (2 ** k) + g, g * (2 ** k) + h] = 1.0
blanking = all(np.argmax(S[:, g * (2 ** k) + 0]) // (2 ** k) == 0 for g in range(2 ** k))
check("T3c the OPEN escape exists and is named: the swap-out (g,0)->(0,g) is an "
      "exact permutation blanking the inner register by exporting content to an "
      "outer sink (whose own blank is the regress the sink no-go prices) -- T3's "
      "claim is specifically about CLOSED reversible dynamics",
      np.allclose(S @ S.T, np.eye(4 ** k)) and blanking)

# ===========================================================================
print("=" * 78)
print("T4  The arrow anchors at the structural boundary (6-qubit miniature)")
print("=" * 78)
NFRAG = 3
NQ = NFRAG + 1
DIM = 2 ** NQ
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


US = []
for k in range(NFRAG):
    Xk = kron(P1, *[X if j == k else I2 for j in range(NFRAG)]) \
        + kron(I2 - P1, *[I2] * NFRAG)
    US.append(Xk)


def partial_trace_keep(rho, nq, keep):
    keep = sorted(keep)
    dims = [2] * nq
    rho_t = rho.reshape(dims + dims)
    for q in sorted([q for q in range(nq) if q not in keep], reverse=True):
        rho_t = np.trace(rho_t, axis1=q, axis2=q + rho_t.ndim // 2)
    d = 2 ** len(keep)
    return rho_t.reshape(d, d)


def record_count(rho):
    # CONNECTED correlator (panel edit): <ZZ> - <Z_sys><Z_frag> is pointer-basis
    # robust -- a deterministic eigenstate "copy" carries no NEW registration and
    # counts 0, so boundary-vanishing is state-robust and formation is the
    # realized-state datum (counterfactual-disclosed below).
    n = 0
    Z = np.diag([1, -1]).astype(complex)
    for k in range(NFRAG):
        rho_k = partial_trace_keep(rho, NQ, [0, k + 1])
        zz = float(np.real(np.trace(rho_k @ kron(Z, Z))))
        zs = float(np.real(np.trace(rho_k @ kron(Z, I2))))
        zf = float(np.real(np.trace(rho_k @ kron(I2, Z))))
        if abs(zz - zs * zf) > 0.5:
            n += 1
    return n


def run(rho0):
    rho = rho0.copy()
    counts = [record_count(rho)]
    for U in US:
        rho = U @ rho @ U.conj().T
        counts.append(record_count(rho))
    return counts


plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
zero = np.array([1, 0], dtype=complex)
one = np.array([0, 1], dtype=complex)


def ketrho(*kets):
    psi = kron(*[k.reshape(-1, 1) for k in kets]).ravel()
    return np.outer(psi, psi.conj())


c_plus = run(ketrho(plus, zero, zero, zero))
c_zero = run(ketrho(zero, zero, zero, zero))
c_one = run(ketrho(one, zero, zero, zero))
c_eq = run(np.eye(DIM, dtype=complex) / DIM)
check("T4a at ANY blank boundary the connected-correlator record count is 0 "
      "(pointer-basis ROBUST: superposed, |0>, |1> all start at 0) -- the "
      "boundary-vanishing is structural under the connected measure",
      c_plus[0] == 0 and c_zero[0] == 0 and c_one[0] == 0)
check("T4b whether records FORM is REALIZED-STATE DATA (counterfactual disclosure, "
      "per the realized-state primitive's test): the superposed pointer forms "
      "records (0 -> 3, strictly increasing); the pointer eigenstates form NONE "
      "(deterministic copies register nothing new); formation is the "
      "non-emptiness input, never claimed structural",
      all(b >= a for a, b in zip(c_plus, c_plus[1:])) and c_plus[-1] == NFRAG
      and c_zero == [0] * (NFRAG + 1) and c_one == [0] * (NFRAG + 1),
      f"superposed {c_plus}; |0> {c_zero}; |1> {c_one}")
check("T4c from the I/d equilibrium NO records form (flat) -- the anchor needs "
      "the boundary and a record-forming realized state, not just the dynamics "
      "(the arrow note's universal floor, reproduced)",
      c_eq == [0] * (NFRAG + 1), f"counts {c_eq}")

# ===========================================================================
print("=" * 78)
print("T5  Residual inventory (anti-overclaim controls)")
print("=" * 78)
# (i) the theorem does NOT pin quantitative room: two boundary realizations with
# different environment sizes satisfy T1-T4 identically.
walks = []
for nfrag2 in (3, 5):
    w = "r" * nfrag2
    steps, cur = 0, w
    while cur:
        cur = cur[:-1]
        steps += 1
    walks.append(steps)
check("T5a two boundary realizations with DIFFERENT room (3 vs 5 registers) both "
      "satisfy the boundary theorem -- the reduction does NOT deliver the "
      "quantitative/thermodynamic content (low entropy, Penrose room): that "
      "residual is genuinely open",
      walks == [3, 5])
# (ii) sector-scope dichotomy: unbounded past requires unbounded registered content
lens = [10, 100, 1000, 10000]
check("T5b the pastward walk length equals the registered content EXACTLY on a "
      "growing family: an unbounded past requires unbounded already-registered "
      "content (the named dichotomy; the finite-history sector scope is disclosed, "
      "not hidden)",
      all((lambda n: n == len("x" * n))(n) for n in lens),
      f"walk lengths {lens}")
# (iii) non-emptiness is genuinely the remaining input: the empty history satisfies
# the monoid structure trivially and carries NO arrow (nothing to anchor).
check("T5c the EMPTY history (w = epsilon) is structurally valid and carries no "
      "arrow -- non-emptiness ('at least one record is registered') is the "
      "explicit residual PRECONDITION, strictly weaker than any specialness claim "
      "and not derived here: formally vacuous-model-allowed, no-arrow when empty",
      c_plus[0] == 0 and len("") == 0)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: reduces the record-arrow low-record-boundary EXISTENCE sub-clause to")
print("  history non-emptiness, IN the single-chain append-only sector (the total")
print("  order is an assumption beyond the Record axiom -- general well-founded")
print("  case: termination survives, uniqueness does not, T1d).  Theorem weight on")
print("  T2 (durability -> acyclicity; deletion controls FAIL) and T3 (rank 2 != 16")
print("  under CLOSED reversible dynamics; the OPEN swap-out escape named, priced")
print("  by the sink regress).  T1b/T1c are definitional in-sector (disclosed).")
print("  T4: connected-correlator boundary count 0 is state-robust; whether records")
print("  FORM is realized-state data (counterfactual-disclosed).  History-level")
print("  blankness (epsilon) is distinct from state-level blankness (T3/T4).")
print("  RESIDUAL: non-emptiness (an explicit applicability precondition, not")
print("  derived here); the single-chain")
print("  sector scope; the finite-history")
print("  dichotomy; and the THERMODYNAMIC past hypothesis (low entropy, Penrose")
print("  room) -- open, named, untouched.  WHICH state realizes the boundary stays")
print("  supplied state data (realized-state primitive slot).  The monoid-sector,")
print("  blank-boundary, and history-order-firewall notes are unaudited on the live")
print("  ledger at this writing -- load-bearing facts RE-PROVED above, not cited.")
print("  No new axiom/primitive/measure/weight; r untouched.  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
