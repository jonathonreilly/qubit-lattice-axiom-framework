# FS Rotation-Exchange Discrete-Insufficiency: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing finite-dimensional facts in
[`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`](FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md)
are invariant under the 2026-06-04 Record-axiom adoption. It is not a
new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and the
pipeline-derived `effective_status` remains downstream of that authority.
**Companion target:** `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28`
(parent note
`docs/FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`).
**Primary companion runner:**
[`scripts/audit_companion_fs_rotation_exchange_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_fs_rotation_exchange_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_fs_rotation_exchange_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_fs_rotation_exchange_record_axiom_invariance_2026_06_04.txt)

```yaml
actual_current_surface_status: companion-only
target_claim_type: meta
trace_class: axiom_premise_restoration_evidence
reachability_to_target: none
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Audit-friendly meta companion: the parent narrow no-go's load-bearing finite-dimensional facts (F1)-(F5) are purely exact symbolic linear-algebra statements about Pauli matrices, tensor products, the swap operator P, Jordan-Wigner dressing, and the dimension of M_4(C). None of them use the Record axiom (additive scalar record-readout functional I(.)); the parent's verdict that the rotation-exchange route does not close FS from the retained inputs is therefore invariant under the 2026-06-04 minimal_axioms premise hash change 1d36a556->b8848fc8. This companion records that invariance as machine-checkable evidence for the audit lane; it does NOT re-audit and does NOT promote status."
proposal_allowed: false
proposal_allowed_reason: "Meta audit-companion only: no new theorem claim, no status promotion, no edit to audit-lane-owned data. The parent narrow no-go's claim scope, claim type, deps list, and effective_status are untouched. The audit lane decides whether to honor the prior judicial verdict on the new premise hash; this companion supplies machine-checkable evidence on whether Record-axiom adoption disturbs the load-bearing step."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

---

## 0. Why this companion exists

The parent narrow no-go `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28`
records the following negative result on the one-qubit operator algebra over the
`Z^3` spatial substrate:

> The on-site spinor `2pi = -1` sign carried by the matter sector (an element of
> the on-site binary octahedral group `2O subset SU(2)`) is **necessary but not
> sufficient** to force fermionic anticommutation (CAR) over hard-core-boson
> (CCR-type) statistics via the rotation-exchange route. The bridge that the
> route would use to convert an on-site `2pi` rotation into a two-site exchange
> sign is the Finkelstein-Rubinstein construction, which is intrinsically
> continuous (it identifies exchange with a `2pi` rotation through a homotopy in
> a *continuous* configuration space `C_N(R^3)/S_N`, using
> `pi_1(SO(3)) = Z_2`); the bare discrete site set does not itself supply that
> continuous configuration-space homotopy. The discriminator between CAR and
> hard-core-boson statistics is therefore the **cross-site** (graded vs
> ungraded) relation, not the on-site rotation sign.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md` to
`MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6)
changed the stable `minimal_axioms` premise-node note-hash from `1d36a556` to
`b8848fc8`. The audit pipeline correctly invalidated the prior audit snapshot
for the parent via
`invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`,
returning the row to its `unaudited` effective status pending re-audit.

This companion records, for the audit lane, that the parent's load-bearing
finite-dimensional facts **(F1)-(F5)** are **independent of the Record axiom**:
they use only the Lattice and Quantum axiom content (the one-qubit local
algebra `M_2(C)` on the `Z^3` site set) plus standard finite-dimensional linear
algebra over `C` (tensor products on `C^2 (x) C^2 = C^4`, exact symbolic
matrix exponential, Pauli-algebra and Jordan-Wigner identities, and the
dimension `16 = dim End(C^4)` of `M_4(C)`). Adopting the Record axiom adds a
strictly additive scalar record-readout statement, which is neither used nor
invoked anywhere in the parent's finite-dimensional argument.

This companion is therefore audit-friendly evidence that the prior reading of
the parent's substantive content survives the axiom-set change. It is not a
re-audit and does not promote status; it documents the load-bearing-step
dependency surface in machine-checkable form so the audit lane can decide
whether to honor or re-test the prior treatment on the new premise hash.

---

## 1. Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the FS rotation-exchange no-go's
load-bearing finite-dimensional facts.** The parent's load-bearing
finite-dimensional content — facts (F1) through (F5) in §1 of
`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`,
together with the route-enumeration walls in §5 — depends only on:

1. the one-qubit on-site Hilbert space `V ~= C^2` (Quantum axiom content);
2. the two-site tensor product `H = V (x) V ~= C^4` (Quantum + standard
   complex tensor products);
3. the on-site spinor `2pi` rotation `U_2pi = exp(2 pi i sigma_3 / 2) = -I_2`
   (granted-by-route premise, computed from the Pauli algebra);
4. the two-site tensor swap `P` (element of `S_2 subset U(4)`, fixed by
   the tensor-product structure);
5. cross-site (anti)commutators of bare ladders `sigma_+ (x) I`, `I (x) sigma_+`
   and Jordan-Wigner dressed ladders `c_0`, `c_1 = sigma_3 (x) sigma_+`
   (free linear algebra on `M_4(C)`);
6. the complex dimension `16 = dim End(C^4)` of the full matrix algebra
   `M_4(C)` (linear algebra fact about generated `*`-algebras).

None of items 1-6 use the Record axiom's additive scalar record-readout
content. They use only the Quantum axiom (one-qubit / `M_2(C)` / `Cl(3,0)`
local algebra; the Pauli matrices and `U_2pi`), the Lattice axiom (`Z^3` site
set; bare two-site product structure inherited from on-site `C^2`), and
standard finite-dimensional complex linear algebra and the Pauli /
Jordan-Wigner identities cited in `Admitted-context inputs` of the parent
(§4 of the parent).

**(C1) is the only auditable companion observation.** This companion does
**not** revisit the parent's open future-closure paths in §7 of the parent
(lattice-native discrete-homotopy / graph-braid `pi_1`; graded-locality /
fermion-parity-superselection); those remain open exactly as the parent
states them, on whatever axiom set is in force at the time they are
attacked.

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, deps list, or admitted-context
  inputs;
- assert anything about Record-axiom content or its scope;
- assert that the parent's prior treatment was clean or unclean — it merely
  records that the parent's load-bearing finite-dimensional facts do not
  consume Record content;
- re-audit `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field;
- promote, demote, or accept the parent's open future-closure paths;
- read on the parent retained no-go
  `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25`
  beyond noting that the parent narrows it via the rotation-exchange route.

The audit lane decides whether (C1) is sufficient evidence to honor the
parent's prior treatment on the new premise hash or whether a fresh
per-fact audit is warranted.

---

## 2. The Record axiom is not used by the load-bearing facts

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing facts (F1)-(F5) define no record surface, ask no
question about scalar record additivity, and write no record functional
`I(.)`. They compute:

- (F1) the on-site value of `U_2pi = exp(2 pi i sigma_3 / 2)`, the two-site
  lifts `U_2pi (x) I = I (x) U_2pi = -I_4`, the action of the swap `P` on
  the symmetric / antisymmetric sectors of `C^2 (x) C^2`, and the spectrum
  `{+1 (mult 3), -1 (mult 1)}` of `P`;
- (F2) the complex dimension `1` of the unital `*`-algebra generated by the
  on-site `2pi` rotations on the two-site space, and the fact that the
  non-scalar `P` is not in that algebra;
- (F3) a literature-context statement (Finkelstein-Rubinstein,
  Jabs/Peshkin, Streater-Wightman all require continuous `SO(3)`/Poincaré
  symmetry, broken to `2O subset SU(2)` by the `Z^3` substrate);
- (F4) the bare ladder commutator `[sigma_+ (x) I, I (x) sigma_+] = 0`
  (ungraded / bosonic-type cross-site locality);
- (F5) the Jordan-Wigner dressed CAR `{c_0, c_1} = 0`,
  `{c_0, c_1^dag} = 0`, `{c_0, c_0^dag} = I_4`, `c_0^2 = c_1^2 = 0`, and
  the equal algebra dimension `16 = dim M_4(C)` of both the
  hard-core-boson generators and the JW-fermion generators.

The operator content (Pauli `sigma_3`, `sigma_+`, `sigma_-`, exact matrix
exponential of `(2 pi i) sigma_3 / 2`, tensor-swap `P`, JW string
`sigma_3 (x) sigma_+`), the unital `*`-algebra closure, and the
equal-algebra-dimension statement are fixed by:

- the one-qubit on-site `M_2(C)` algebra (Quantum axiom content);
- the `Z^3` site set with the bare two-site product structure
  (Lattice axiom content);
- standard finite-dimensional complex linear algebra, tensor products, the
  Pauli algebra, and the Jordan-Wigner construction (admitted-context
  mathematical infrastructure listed in §4 of the parent).

The Record axiom adds an additive scalar record functional. It does **not**
modify (and is not modified by) the Quantum local algebra, the Lattice
two-site product, the Pauli matrices, the swap operator, the bare ladders,
the Jordan-Wigner dressing, or the dimension of `M_4(C)`. So the values of
all of (F1)-(F5) are invariant under the axiom-set change. The route walls
R1-R6 in the parent's §5.1 N1 table are likewise invariant: each rules out
a candidate forcing argument purely from those finite-dimensional facts.

In particular, the Record-axiom scope statement (`MINIMAL_AXIOMS_2026-06-04.md`
§"Record" closing paragraph) explicitly excludes from the Record axiom's
content: "rule for record production, persistence, measurement/decoherence,
Born weights, P2/modulus/phase-blindness, log-det structure, time arrow,
system composition, normalization/scale, source/action identification,
`AC_phi_lambda`, theta, or arbitrary observable identification." None of
those bridges enter the parent note's finite-dimensional load-bearing
content either; the route walls are about the absence of a *continuous-`pi_1`
exchange-rotation bridge* and the *ungraded* character of the retained
tensor-locality, neither of which is provided or revoked by the additive
scalar Record functional.

This invariance is what the companion runner verifies block-by-block:
every load-bearing finite-dimensional check in (F1)-(F5) passes using only
Quantum + Lattice content and standard finite-dimensional linear algebra,
and a "Record-axiom counterfactual" block confirms that all numeric outputs
are unchanged whether or not a Record-axiom statement is appended.

---

## 3. Companion runner block plan

`scripts/audit_companion_fs_rotation_exchange_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the FS rotation-exchange no-go's
load-bearing finite-dimensional facts. Each block runs as an independent
symbolic / numeric check; nothing is hard-coded against an expected target
value beyond standard finite-dimensional linear algebra. The runner reports
`PASS` / `FAIL` per check; the cached output records the run.

Block 1 — On-site `2pi` rotation. Verifies `U_2pi = exp(2 pi i sigma_3 / 2)
= -I_2` and `U_4pi = +I_2` (double-cover signature) using exact sympy matrix
exponentials. Uses only Pauli-algebra content; no Record axiom enters.

Block 2 — Two-site lifts of `U_2pi`. Verifies `U_2pi (x) I = I (x) U_2pi
= -I_4` (the same global scalar), confirming that the on-site spinor sign
is a global scalar on the two-site space and carries no
two-site-exchange information. Uses only the tensor-product structure of
`C^2 (x) C^2`.

Block 3 — Tensor swap `P` and its spectrum. Constructs the swap operator
`P` explicitly, verifies `P^2 = I_4`, computes its action on the four
basis vectors of `C^2 (x) C^2`, and verifies the spectrum
`{+1 (mult 3), -1 (mult 1)}`. Uses only the tensor-product structure.

Block 4 — On-site rotations act as `-1` on both symmetric and
antisymmetric sectors. Verifies that `(U_2pi (x) I) * v = -v` for both the
symmetric basis vector `|01> + |10>` and the antisymmetric basis vector
`|01> - |10>`. Confirms that the on-site `2pi` rotations cannot
distinguish the two sectors and therefore cannot equal the non-scalar `P`.

Block 5 — Algebra-dimension wall. Computes the complex dimension of the
unital `*`-algebra generated by `{U_2pi (x) I, I (x) U_2pi}` inside
`M_4(C)`; verifies it equals `1` (scalars only). Confirms that no
product/linear combination of the on-site `2pi` rotations equals the
non-scalar `P`. This is the algebraic shadow of the absent
continuous-`pi_1` exchange-rotation bridge.

Block 6 — Hard-core-boson cross-site commutation. Verifies
`[sigma_+ (x) I, I (x) sigma_+] = 0`, `[sigma_+ (x) I, I (x) sigma_-] = 0`,
and `{sigma_+ (x) I, I (x) sigma_+} != 0`. Confirms that the bare ladders
on disjoint sites commute (ungraded / bosonic-type locality), matching the
retained Lieb-Robinson tensor-locality narrow.

Block 7 — On-site nilpotency. Verifies `(sigma_+)^2 = 0` on a single site
(per-site Fock dim `2`, spin-`1/2`). Confirms that the hard-core-boson
shares the on-site `2pi = -1` sign, the per-site dim, and the on-site
nilpotency premise with the JW-fermion frame.

Block 8 — Jordan-Wigner dressed CAR. Verifies the JW relations
`{c_0, c_1} = 0`, `{c_0, c_1^dag} = 0`, `{c_1, c_0^dag} = 0`,
`{c_0, c_0^dag} = I_4`, `c_0^2 = 0`, `c_1^2 = 0` for
`c_0 = sigma_+ (x) I`, `c_1 = sigma_3 (x) sigma_+`. Confirms that JW
dressing produces cross-site anticommutation (graded / fermionic locality).

Block 9 — Equal full-algebra dimension. Computes the complex dimension of
both the hard-core-boson algebra
`<sigma_+ (x) I, sigma_3 (x) I, I (x) sigma_+, I (x) sigma_3>` and the
JW-fermion algebra `<c_0, c_1>` inside `M_4(C)`; verifies both equal
`16 = dim End(C^4)`. Confirms that the fermion/boson distinction is the
cross-site (anti)commutator (graded locality), not the on-site sign or
the ungraded algebra.

Block 10 — Static-source scan of parent note. Reads the parent note's
load-bearing structural section and confirms zero occurrences of
Record-axiom usage tokens. The token set scans for
`{"I(R_1", "I(R)", "scalar record", "record functional",
"record-readout", "additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04"}` over the §1 "Claim scope" and §5 "Proof"
sections of the parent. Confirms zero matches inside the load-bearing
core.

Block 11 — Record-axiom counterfactual. Re-runs the symbolic core of
Blocks 1-9 inside an explicit "Record axiom is asserted" outer scope and
an explicit "Record axiom is not asserted" outer scope; verifies that
every load-bearing value (the `-I_2` scalar of `U_2pi`, the `-I_4` scalar
of `U_2pi (x) I`, the spectrum of `P`, the algebra dimension `1` for the
on-site rotations, the `0` cross-site commutator for bare ladders, the
`0` cross-site anticommutators for the JW dressing, and the dimension
`16` of the full `M_4(C)` algebra) is identical in both runs. The
counterfactual is a tautology at the calculation level (no Record-axiom
content enters the symbolic linear algebra), which is precisely the
substantive content of (C1).

Block 12 — Quantum / Lattice content preservation. Reads
`MINIMAL_AXIOMS_2026-05-20.md` and `MINIMAL_AXIOMS_2026-06-04.md` and
confirms that (a) the one-qubit local-algebra content used by the parent is
present in both memos under the historical wording and the new "Quantum"
name; (b) the `Z^3` site set is present in both; (c) the Record axiom in
the new memo asserts only additive scalar record-readout and explicitly
excludes "log-det structure", "source/action identification", "rule for
record production", "P2/modulus/phase-blindness", "Born weights", and
related bridges from its scope; (d) none of those excluded bridges are
load-bearing in the parent note's finite-dimensional argument.

Block 13 — Route-wall preservation. Confirms that each of the parent's
N1 route-enumeration walls R1-R6 remains valid using only the finite-
dimensional facts verified above:
  - R1 (on-site `2pi` sign as exchange sign) fails because Block 4 shows
    it acts as `-1` on both sectors.
  - R2 (algebraic generation of `P` from on-site rotations) fails because
    Block 5 shows the on-site algebra has dimension `1` while `P` is
    non-scalar.
  - R3 (Finkelstein-Rubinstein homotopy) fails because the discrete site
    set has no continuous configuration-space `pi_1` (literature-context
    statement; not numerically tested here, only re-cited).
  - R4 (non-relativistic / relativistic spin-statistics route) fails for
    the same reason as R3 (continuous `SO(3)`/Poincaré symmetry needed).
  - R5 (retained Lieb-Robinson locality as CAR selector) fails because
    Block 6 shows that ungraded locality is the bosonic signal, not the
    CAR signal.
  - R6 (spin-`1/2` + nilpotency + `2pi = -1` as fermion test) fails
    because Blocks 6-9 show the hard-core boson passes all three premises
    yet is bosonic.

Total: 13 blocks. The exact PASS/FAIL count is recorded in the cached
runner output.

---

## 4. Cited authorities (one hop)

Load-bearing (markdown-linked):

- **Parent narrow no-go.**
  [`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`](FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md):
  the rotation-exchange route does not close FS from the retained inputs on
  the discrete substrate.
- **New framework axioms.**
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md): Quantum
  one-qubit local algebra, `Z^3` Lattice, and Record additive scalar
  readout (the third explicitly approved premise; the only premise this
  companion addresses).
- **Predecessor framework axioms (still authoritative for local-algebra
  and `Z^3` content):**
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md).
- **Axiom-minimality policy and explicit-owner-approval ledger:**
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md).
- **Audit lane authority statement:**
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md).
- **Audit pipeline ground rules:**
  [`docs/audit/README.md`](audit/README.md).

Plain-text / backtick reader pointers (non-load-bearing):
`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`
(the parent's parent retained no-go, narrowed by the parent via the
rotation-exchange route),
`scripts/audit_companion_fs_rotation_exchange_discrete_insufficiency_2026_05_28.py`
(the parent's own paired runner, whose 30 PASS the present companion does
not consume as load-bearing),
`BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md`
(the sibling source for the on-site `2pi = -1` ingredient granted by the
route),
`lieb_robinson_equal_time_tensor_locality_narrow_theorem_note_2026-05-10`
(retained ungraded tensor-locality, cited by the parent as the bosonic-
type, not CAR, sign).

No PDG values, fitted selectors, scale, mass input, `g_bare`, lattice-
action carrier, or literature comparator load-bearing consumption. The
Finkelstein-Rubinstein / Jordan-Wigner / spin-statistics references are
literature **context** only (as in the parent §4).

---

## 5. Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence. Per
[`docs/audit/README.md`](audit/README.md) (the auditor sets `claim_type`,
the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.

The audit lane decides whether to honor the prior treatment of the parent
no-go on the new premise hash; this companion only supplies machine-
checkable evidence on whether the new Record axiom disturbs the
load-bearing finite-dimensional facts. The Record-axiom-invariance
observation here is structurally narrow: it does not extend to any
downstream claim that consumes the parent's output, and it does not
re-open or pre-close the parent's open future-closure paths in §7 of the
parent.

Other rows recently axiom-invalidated under the same hash change remain
out of scope of this companion; they are listed in the audit queue's
`axiom_premise_changed` cohort and should be examined separately as the
audit lane reaches them.

---

## 6. Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citations to `MINIMAL_AXIOMS_2026-06-04.md`.
Both are valid framework axiom memos; the 2026-06-04 memo cites the
2026-05-20 memo as the predecessor explicit-owner-approved axiom set. A
separate citation-migration PR (if desired) can refresh the parent note's
`Source` column; this companion is independent of that text update and is
content-only.

This companion's load-bearing-step invariance observation depends only on
the Quantum and Lattice content being preserved across the two memos —
verified in Block 12 — and on the Record axiom adding a strictly additive
non-overlapping statement — confirmed by direct reading of
`MINIMAL_AXIOMS_2026-06-04.md` §"Record" and its scope-exclusion list.

---

## References

- Parent note:
  [`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`](FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md)
- Parent runner:
  `scripts/audit_companion_fs_rotation_exchange_discrete_insufficiency_2026_05_28.py`
- Prior treatment snapshot:
  `docs/audit/data/audit_ledger.json` row
  `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28`,
  `previous_audits[-1]` with
  `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms:
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
