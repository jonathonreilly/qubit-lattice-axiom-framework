# Teleportation Native Record Apparatus Scope Split — Source Theorem Note

**Date:** 2026-05-16
**Claim type:** open_gate
**Status:** source theorem note (planning/conditional scope-split bridge);
explicit split between audited bounded apparatus/carrier consistency and
held-open native-derivation closure for the parent record apparatus note
**Parent note:** [teleportation_native_record_apparatus_note](TELEPORTATION_NATIVE_RECORD_APPARATUS_NOTE.md)
**Runner:** `scripts/frontier_teleportation_native_record_apparatus_scope_split_2026-05-16.py`
**Cache:** `logs/runner-cache/frontier_teleportation_native_record_apparatus_scope_split_2026-05-16.txt`

```yaml
actual_current_surface_status: bounded-apparatus-consistency-supported
conditional_surface_status: nature-grade-HOLD
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Bell-stabilizer transducer derivation, durable pointer irreversibility, and derived local record-field carrier remain held open per the parent note's own Nature-Grade Blockers; no promotion is asserted here"
independent_audit_required_before_effective_status: true
bare_retained_status_allowed: false
scope_split_target: teleportation_native_record_apparatus_note
```

## 1. Question

The parent note `TELEPORTATION_NATIVE_RECORD_APPARATUS_NOTE.md` constructs a
bounded model for a native Bell-record apparatus and a 3D+1 record carrier:
an ideal Bell-stabilizer transducer that writes a length-8 classical pointer
codeword (`z z z | x x x | p p`, `p = z xor x`, `min Hamming = 5`), local
3D+1 record-field pulses on `Z^3` along a Manhattan worldline
`(1,1,1)@t=4 -> (5,3,2)@t=11`, and a decoded Pauli correction
at Bob. The runner verifies the bounded model end-to-end on a 64-trial
random-qubit sweep at `seed = 20260426`, reaching numerical-zero
correctness on all bounded gates.

The conditional audit (`audited_conditional`, `claim_type=open_gate`,
`load_bearing_step_class=E`) records the verdict that:

- the bounded apparatus/carrier construction is internally consistent and
  the runner produces nontrivial bounded-model evidence (not just constant
  printing);
- the load-bearing apparatus and carrier components are introduced as
  ideal/projective and classical/discrete bounded model definitions rather
  than derived from the explicit framework baseline (physical `Cl(3)` local
  algebra on the `Z^3` spatial substrate);
- Nature-grade closure cannot propagate from the bounded model alone;
- a re-audit at Nature-grade requires either bridge theorems for the
  three named ideal-vs-derived gaps (Bell-stabilizer transducer derivation,
  durable pointer irreversibility, derived local record-field carrier) or an
  explicit structural split between the closed bounded consistency claim
  and the held-open native-derivation claim.

This note takes the second path. It does not introduce or promote new physics
axioms, does not derive any of the three missing bridges, and does not
modify the canonical harness index. It states and verifies a structural
scope split that the parent note already implies in its existing top-of-note
"Audit-conditional perimeter" and "Nature-Grade Blockers" sections.

## 2. Boundary Theorem (Scope-Split Theorem)

**Theorem (Scope Split).** The parent note's content factors into two
disjoint claim surfaces:

1. **Bounded apparatus/carrier consistency surface** `B`: on the audited
   bounded model (Bell stabilizer projectors, length-8 classical pointer
   codeword with `min Hamming = 5`, local 3D+1 pulse rule on `Z^3` along the
   Manhattan worldline `(1,1,1)@t=4 -> (5,3,2)@t=11`, decoded Pauli
   correction operator), the runner produces all of the following
   bounded-model identities at numerical zero on the recorded
   `trials=64 / seed=20260426` sweep:

   - the four Bell projectors `P_{zx} = 1/4 (I + (-1)^x Z_A Z_R)(I +
     (-1)^z X_A X_R)` form a complete projective resolution
     (`max Bell-transducer norm error ~ 4.4e-16`);
   - each branch emits the projector-labeled pointer codeword
     `(z, z, z, x, x, x, z xor x, z xor x)` with
     `min Hamming distance = 5` across the four outcomes; nearest-codeword
     decoding therefore corrects every one- and two-component bit flip
     (`one_bit_corrected = True`, `two_bit_corrected = True`);
   - record outcome probabilities equal `1/4` independent of the input qubit
     (`max record probability error from 1/4 ~ 1.1e-16`;
     `max pairwise record-distribution distance across inputs ~ 1.1e-16`);
   - Bob's pre-delivery reduced state equals `I/2` independent of the input
     (`max Bob trace distance to I/2 before carrier delivery ~ 3.1e-16`;
     `max pairwise pre-delivery Bob-state distance across inputs ~ 2.2e-16`);
   - the carrier payload is derived from the apparatus pointer
     (`carrier payloads derived from apparatus = True`), each pulse
     worldline moves at most one 3D step per tick
     (`carrier pulse worldlines local = True`), pulse count is conserved
     (`carrier pulse count conserved = True`);
   - the Manhattan delivery-tick identity `delivery_tick = alice_tick +
     L1` holds: `4 + 7 = 11`, the carrier is unavailable at
     `expected_delivery_tick - 1` (`early delivery blocked = True`) and
     available at `expected_delivery_tick`
     (`delivery at light-cone tick available = True`);
   - the decoded Pauli correction restores Bob's state at numerical zero
     (`minimum delivered-record corrected fidelity ~ 1 - 2.2e-16`;
     `max corrected-state trace distance to input ~ 1.9e-16`);
   - the wrong-record control is non-teleporting in the ensemble mean
     (`wrong-record mean fidelity control ~ 0.333333`, the Pauli-error
     value).

   Surface `B` is what the existing runner
   `frontier_teleportation_native_record_apparatus.py` audits, and what the
   parent note's existing closing prose calls
   "the first artifact in the lane where the Bell record is generated,
   encoded, carried, decoded, and used in one end-to-end model".

2. **Native-derivation closure surface** `N`: the three Nature-grade
   derivations named in the parent note's audit-conditional perimeter
   (verbatim `notes_for_re_audit_if_any`):

   - **N1.** Bell-stabilizer transducer derivation: derive the projective
     `Z_A Z_R -> x bit`, `X_A X_R -> z bit` apparatus coupling from the
     explicit framework baseline rather than supplying it as an ideal
     isometry / projective rule;
   - **N2.** Durable pointer irreversibility: replace the length-8 classical
     pointer codeword with a thermodynamic derivation of measurement-record
     irreversibility (bath, entropy production, second-law / fluctuation
     relations, no-erase) from the explicit framework baseline;
   - **N3.** Local record-field carrier from framework dynamics: replace the
     `Z^3` local pulse rule with a derived field equation whose
     finite-energy quanta carry the codeword bits and reproduce the
     Manhattan light-cone identity.

   Surface `N` remains HOLD until each of N1-N3 is resolved by a separate
   Nature-grade derivation. This note does not attempt any such
   resolution. The parent note's own "Nature-Grade Blockers" section
   already names each of these as an open blocker (Bell-stabilizer
   transducer "remains ideal/projective"; codeword "is a classical model of
   durable memory, not a thermodynamic derivation of irreversibility";
   record-field pulses "are local on a 3D+1 lattice but are not derived from
   a derived field equation").

**Disjointness.** The two surfaces are disjoint in claim grade: surface `B`
is supported only as a bounded-model consistency claim under the cited
runner certificate; surface `N` is unconditioned HOLD. The parent note's
strongest current statement — "A native record apparatus/carrier candidate
exists that generates a redundant Bell record from Alice's Bell branch,
propagates it locally in 3D+1, preserves Bob input-independence before
arrival, and restores the state after decoded delivery" — is a `B`-surface
statement only, as flagged by the parent note's own "Status: planning /
first native apparatus-carrier candidate" header and the existing
"audit-conditional perimeter" paragraph at the top of the note.

**Consequence.** A re-audit of the parent note that targets only surface
`B` has an explicit bounded-model boundary to inspect. A re-audit of the
parent note that targets surface `N` must remain HOLD until each of N1-N3
is independently closed by future bridge theorems. This source note does
not set or predict any audit verdict.

## 3. Proof Sketch

**(Surface `B` is closed on the cited bounded-model evidence.)** Each
bounded-model identity listed in surface `B` above is either an algebraic
fact about Bell projectors and the explicit length-8 codeword, or a
finite-trial certificate that the existing runner already produces at
numerical zero. The new runner companion does not re-run the full Bell
simulation; it re-verifies the algebraic / combinatorial identities that
the bounded-model gates rely on (Bell-projector completeness, codeword
Hamming distances, Manhattan delivery-tick identity, decoded Pauli
correction inverse) and re-parses the cited cache certificate to confirm
that the named bounded-model magnitudes are at the recorded numerical zero.

These are bookkeeping identities and runner-cache witnesses on a fixed
bounded model; they make no claim about derivation of the apparatus, the
record's thermodynamic irreversibility, or a derived field equation for
the carrier.

**(Surface `N` cannot be closed by the parent note alone.)** Surface `N`
requires Nature-grade derivations N1-N3. The parent note explicitly does
not contain any such derivation; the existing "Nature-Grade Blockers"
section enumerates each as an open blocker. No combination of the bounded
projector identities, the classical codeword, and the local pulse rule
constitutes such a derivation, because each of N1-N3 concerns a physical /
dynamical / thermodynamic fact that is not reachable from the bounded
model alone:

- N1 demands the projective rule emerge from the explicit framework baseline,
  not be
  postulated;
- N2 demands an irreversibility theorem (bath-coupled second law, no-erase
  argument, or equivalent), not a redundancy code;
- N3 demands a derived field equation with finite-energy carrier quanta,
  not a discrete pulse-shifting rule on `Z^3`.

Therefore surfaces `B` and `N` are independent claim grades, and the parent
note carries bounded-model content only on surface `B`.

## 4. Runner Witness

The paired runner
`scripts/frontier_teleportation_native_record_apparatus_scope_split_2026-05-16.py`
performs a structural verification of the split. It does not re-run the
underlying physics simulation; it audits the parent note's own boundary
claims against its own evidence map, re-verifies the algebraic identities
the bounded model relies on, and re-parses the cited runner-cache
certificate to confirm the bounded-model magnitudes are at numerical zero.

The runner checks:

- the parent note exists and is labeled
  "planning / first native apparatus-carrier candidate" (not a retained-grade
  promotion);
- the parent note's "Audit-conditional perimeter" paragraph cites the
  audit verdict, names the three load-bearing ideal-vs-derived gaps
  (Bell-stabilizer transducer, durable pointer irreversibility, local
  record-field carrier), and explicitly says the runner certificate
  covers only the bounded model "as an ideal apparatus-carrier candidate";
- the parent note's existing "Nature-Grade Blockers" section names each
  of N1-N3 as an open blocker;
- the parent note's existing "Citation chain and audit-stated repair path"
  table cites the parent runner under "bounded model only; not a
  derivation from the explicit framework baseline";
- the existing runner certificate at
  `scripts/frontier_teleportation_native_record_apparatus.py` exists and
  references the parent note;
- the canonical harness index already files this lane under
  "parked bounded planning lane; nature-grade closure HOLD; state
  teleportation only, no matter/FTL/mass/charge transfer" language (so no
  index update is asserted);
- algebraic identities on the bounded model are recomputed:
    - the four Bell projectors `P_{zx} = 1/4 (I + (-1)^x Z_A Z_R)(I +
      (-1)^z X_A X_R)` sum to identity (`norm of completeness defect <
      1e-12`);
    - each pair of projectors is orthogonal at numerical zero;
    - the length-8 codeword has `min Hamming distance = 5` across the
      four Bell outcomes;
    - nearest-codeword decoding corrects all one- and two-bit flips;
    - the decoded Pauli correction operator `Z^z X^x` is its own
      inverse up to phase (`(Z^z X^x)^dagger (Z^z X^x) = I`);
    - the Manhattan delivery-tick identity `4 + 7 = 11` holds for the
      cited `(1,1,1) -> (5,3,2)` worldline at unit lattice speed;
- the existing runner-cache witness at
  `logs/runner-cache/frontier_teleportation_native_record_apparatus.txt`
  contains the bounded-model magnitudes the scope split relies on
  (Bell-transducer norm error, record-probability error, pairwise
  pre-delivery Bob distance, minimum corrected fidelity, wrong-record mean
  fidelity); each is checked to be at the recorded numerical-zero
  magnitude (or, for the wrong-record control, at the Pauli-error value of
  ~ 0.333).

Checks:

```bash
set -o pipefail; python3 scripts/frontier_teleportation_native_record_apparatus_scope_split_2026-05-16.py | tee logs/runner-cache/frontier_teleportation_native_record_apparatus_scope_split_2026-05-16.txt
python3 -m py_compile scripts/frontier_teleportation_native_record_apparatus_scope_split_2026-05-16.py
```

Expected runner result:

```text
SUMMARY: PASS=35 FAIL=0 TOTAL=35
```

(See cache file for the exact magnitudes parsed from the parent
runner cache.)

## 5. What This Closes And Does Not Close

**Closes (planning-grade only):**

- The structural scope-split between surface `B` (bounded apparatus/carrier
  consistency on the cited runner certificate) and surface `N`
  (native-derivation closure for N1-N3) is now an explicit, runner-verified
  property of the parent note rather than only prose language. A re-audit
  that targets only surface `B` has a clear, runner-supported boundary to
  work against.

**Does not close:**

- Nothing about surface `N` is closed here. The Bell-stabilizer transducer
  remains ideal/projective; the pointer codeword remains a classical model
  of durable memory rather than a thermodynamic irreversibility theorem;
  the record-field carrier remains a discrete local pulse rule rather than
  a derived field equation.
- The teleportation lane is not promoted. The canonical harness index
  entry "parked bounded planning lane; nature-grade closure HOLD; state
  teleportation only, no matter/FTL/mass/charge transfer" remains correct.
- No new physics axiom, no new retained-grade theorem, and no closure of any of
  N1-N3 is introduced or claimed.

## 6. Audit Position

This note is a bridge-discipline source theorem note, in the boundary /
no-go / scope-split family. It mirrors the structural pattern of
`TELEPORTATION_NATIVE_AXIOMS_SCOPE_SPLIT_SOURCE_THEOREM_NOTE_2026-05-16.md`
(the prior scope-split landing on the parent axiom theory note within this
same teleportation lane), adapted to the apparatus/carrier sub-claim
rather than the axiom-bundle sub-claim.

It supplies the lighter of the two repair paths recorded verbatim in the
parent note's "Citation chain and audit-stated repair path" section
(quoting the audit's `notes_for_re_audit_if_any`):

> "missing_bridge_theorem: derive the Bell-stabilizer transducer, durable
> pointer irreversibility, and local record-field carrier from the
> explicit framework baseline rather than introducing them as ideal bounded model
> components."

This note takes the structural-split path. Bridge theorems N1-N3 remain
open work and are not attempted here.
