---
claim_id: admissibility_dirac_kahler_temporal_link_extraction_bounded_theorem_note_2026-08-24
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md
claim_type: bounded_theorem
claim_scope: "on the certified Block 105 curved carrier exactly as landed by Block 128 and re-used by Blocks 181, 182 and 183 -- the 8x4 cover of dimension 32, the parameterized cover Hodge H[g] over the LANDED Block 105 overlap field, the chart differential d_00 and the completion convention Q(H,d) = m*H + i*(H d + d^H H) at SYMBOLIC POSITIVE MASS -- AND AT THE MINIMAL REFLECTION-CLOSED FRAME H_min = (H + U_x^T H U_x)/2, WHICH IS ONE ADMITTED MEMBER OF THE SIXTEEN-MEMBER FAMILY BLOCK 183 ENUMERATED AND IS TAKEN HERE FOR MINIMALITY ALONE: AT THAT FIXTURE FAMILY AND NO WIDER. THE dt=+-1 TEMPORAL LINK IS EXTRACTED, IT IS INVERTIBLE AT EVERY BOND, IT OBEYS AN EXACT PARITY THEOREM AGAINST THE DUAL FRAME, ITS SYMBOLIC FORM SPLITS EVEN AND ODD BONDS, AND THE SLICE DETERMINANTS ARE STRICTLY POSITIVE FOR EVERY REAL MASS. FIRST, THE CONTROLS: the parameterized Hodge at the landed field IS the landed curved_hodge_cover() at zero residual, R is real orthogonal at zero residual, the frame closes under Block 183's derived reflection at ZERO residual, and the frame is POSITIVE DEFINITE by 32 exact leading principal minors. SECOND, THE BAND STRUCTURE: the census of Q_min by time separation dt = (row//4 - col//4) mod 8 is EXACTLY {0: 80, +1: 72, +2: 16, -2: 16, -1: 72} -- 256 entries in five bands and nothing outside them -- and the dual-frame action carries the same census; THE LINK IS THE dt=+-1 PAIR AND IT IS IRREDUCIBLY A PAIR, since B_-1 is NOT the adjoint of B_+1 (40 entries), NOT minus its adjoint (32) and NOT its transpose (40). THIRD, THE TRANSPORTER IS INVERTIBLE: all EIGHT per-bond blocks L_t = Q_min[slice t+1, slice t] have RANK EXACTLY 4 and EMPTY KERNELS, with nonzero counts alternating 10 at even t and 8 at odd t, so the carrier's degeneracy is not in the link. FOURTH, THE PARITY THEOREM: R B_+1 R^-1 = the dt=-1 band of the DUAL-FRAME completion built with d_ref = R d_00 R^-1, at ZERO residual, against three failing neighbours measured in the same run -- the WRONG dual built with d_00 at EXACTLY 16 entries, the wrong band at 144, and the undualized frame at 96. FIFTH, THE SYMBOLIC SPLIT at a per-slice field (q_t, v_t) constant in x, with a_t = q_t v_t/(q_t^2 - 1): the ODD bond L_1 has EXACTLY 8 entries, exhibited entrywise as -3a_1/20 at (0,0) and (2,2), +3a_1/20 at (0,2) and (2,0) and m a_1/4 at (0,1), (1,2), (2,3) and (3,0), and VANISHES IDENTICALLY at q_1 = 0; the EVEN bond L_0 has 10 entries splitting EXACTLY 8 odd and 4 even under q -> -q with THE MASS ONLY IN THE ODD PART, and the even part is FOUR DIAGONAL ENTRIES with signs (-,+,-,+) and common magnitude E = (1/v_0 + v_1 - v_0/(q_0^2 - 1) - v_1/(q_1^2 - 1))/5, which is EVEN in the shears but GENUINELY SHEAR-DEPENDENT (dE/dq_0 = 2 q_0 v_0/(5(q_0^2 - 1)^2) and dE/dq_1 = 2 q_1 v_1/(5(q_1^2 - 1)^2), both nonzero and both odd) and which reduces EXACTLY to (v_1 + 1/v_1 + 2/v_0)/5 under the Pythagorean witness constraint q_t^2 + v_t^2 = 1. SIXTH, THE POLE LOCUS: the eight intra-slice determinants are EVEN QUARTICS in m with ALL THREE COEFFICIENTS STRICTLY POSITIVE, slices t and t+4 agreeing exactly so that four are distinct, and therefore det D_t > 0 FOR EVERY REAL m INCLUDING m = 0 -- the slice Schur factorization is globally regular on the physical mass axis AT THIS FRAME'S DECOMPOSITION, with the poles at m^2 < 0. SEVENTH, THE DESCENT: on Block 128's landed 16-dimensional antiperiodic quotient the census is EXACTLY {0: 40, +1: 36, +2: 16, -1: 36}, all four quotient bonds have rank 4 with the same 10/8 alternation, and the quotient seam bond is MINUS the cover bond 3 -> 4 exactly, at entrywise ratio -1 across all eight common nonzero positions. NOTHING HERE IS REGISTERED, nothing is adopted, no premise-class change is registered, and no axiom amendment is justified. This is NOT AN OS OR REFLECTION-POSITIVITY THEOREM (no pairing is shown positive at any scope), NOT A TWO-HISTORY GRAM (that is the successor, and this block supplies its inputs), NOT A GRAVITY RESULT, NOT A DERIVATION OF ANY ADM QUANTITY (the lapse/shift identification is a READING of the measured even/odd structure and is marked as one at every occurrence), NOT A UNIQUENESS CLAIM FOR THE FRAME (uniqueness was REFUTED by Block 183 and is not re-claimed here), NOT A STATEMENT ABOUT THE #7338 CHARTS' OWN VERTICAL SCHUR, not a continuum statement, not a Records result and not a derivation of the Born rule; no priority or originality claim is made or licensed at any scope; zero axiom retirement, ZERO OBLIGATION RETIREMENT, and no TOE percentage movement is established."
depends_on:
  - admissibility_dirac_kahler_derived_reflection_seam_dual_bounded_theorem_note_2026-08-24
  - admissibility_dirac_kahler_dual_patch_pullback_section_frame_bounded_theorem_note_2026-08-24
  - admissibility_dirac_kahler_curved_carrier_dependency_bounded_theorem_note_2026-08-17
  - admissibility_dirac_kahler_local_dual_patch_descent_bounded_theorem_note_2026-08-15
runner: scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_derived_reflection_seam_dual_bounded_theorem_note_2026-08-24
target_blocker_text: "THE TEMPORAL-LINK BAND EXTRACTION: the dt=+-1 band of Q_s carries 72 entries and the thin dt=+-2 band carries 16 -- neither is extracted here, and the extraction should now be posed AGAINST THE DUAL FRAME, since the reflection carries the action to the dual-frame action at the reflected field rather than back to itself."
source_of_blocker_text: next_trace_action
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "THE LINK EXISTS AND IT IS INVERTIBLE; THE GRAM IS THE NEXT LEG AND IT IS NOT BUILT HERE. Four items, named. (i) THE TWO-HISTORY GRAM, Block 106 section 12 step 2, now with its two inputs supplied as measurements rather than assumptions: an INVERTIBLE per-bond transporter (rank 4, empty kernel, at every one of the eight bonds) and a slice Schur complement that is REGULAR AT EVERY REAL MASS (four even-quartic determinants, all coefficients strictly positive). Build the Gram on both spatial eigenlines and see whether the pairing is positive; NOTHING in this note is a positivity statement. (ii) OS / REFLECTION POSITIVITY ON THE SEAM PAIRING, which is where the parity theorem would have to be used rather than merely stated: the exact map R B_+1 R^-1 = B_-1[dual] is a covariance identity and a positivity statement is a different object. (iii) THE GRAVITY CONSTRAINT QUOTIENT downstream, which Block 106 section 12 step 4 puts last and which stays untouched here. (iv) THE ADM IDENTIFICATION, WHICH IS STILL A READING: the even/odd bond alternation is measured and the lapse/shift naming of it is not; deriving an ADM quantity from the split, rather than recognizing the split's shape, is open. TWO ITEMS ALSO STAY OPEN FROM THE PARENTS: the section-point family is still sixteen-member and no further principle picks inside it, and the uniformly-bounded finite-range clause of the 2026-08-15 blocker is still unmeasured on the curved section frame."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-183 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the block's load-bearing content is a set of EXACT SYMPY IDENTITIES on ONE landed fixture family at ONE frame, with every completion run at SYMBOLIC POSITIVE MASS so each identity is an operator identity in m and not a coincidence at MASS = 2/7, plus ONE per-slice symbolic field family for the split. The control leg is one exact zero landed-field Hodge residual, one exact zero orthogonality residual, one exact zero frame-closure residual and one positive-definiteness certificate of 32 exact leading principal minors. The band leg is one exact five-band census {0: 80, +-1: 72, +-2: 16} totalling 256 entries, the same census for the dual-frame action, and three exact nonzero non-identities at 40, 32 and 40. The transporter leg is eight exact rank-4 measurements with eight empty kernels and the exact nonzero counts (10, 8, 10, 8, 10, 8, 10, 8). The parity leg is one exact zero residual against three exact nonzero controls at 16, 144 and 96, with a fourth undressed control at 72. The symbolic leg is an exact 8-entry table for the odd bond with its identical vanishing at zero shear, an exact 8/4 odd/even split for the even bond with the mass exactly absent from the even part, four exact diagonal positions with signs (-1, 1, -1, 1) against one exact common magnitude, two exact nonzero shear derivatives, and one exact Pythagorean reduction. The pole leg is eight exact determinants with four exact coincidences, four exact degrees, twelve exactly positive coefficients and four exactly positive values at m = 0. The quotient leg is one exact four-band census {0: 40, +-1: 36, +2: 16}, four exact rank-4 bonds and one exact zero seam-negation residual against a nonzero seam-identity residual with eight entrywise ratios of exactly -1. NO FLOAT AND NO TOLERANCE ENTERS ANY CHECK. BUT THE STANDING IS BOUNDED AND THE BOUNDS ARE STRUCTURAL. First, IT IS ONE FIXTURE FAMILY -- the Block 128 8x4 cover over the certified Block 105 curved carrier -- with no width ladder, no second carrier rule and no second field for the numeric legs. Second, IT IS ONE FRAME, the minimal member of Block 183's sixteen-member closed family, chosen for MINIMALITY, with NO uniqueness claimed and none available. Third, NO POSITIVITY OF ANY PAIRING IS SHOWN, so no OS or reflection-positivity theorem follows from the parity theorem or from anything else here. Fourth, NO TWO-HISTORY GRAM IS BUILT and no gravity result exists here, so the block is KINEMATIC FRAME DATA. Fifth, THE ADM LAPSE/SHIFT IDENTIFICATION IS A READING AND NOT A THEOREM, as is the shift-squared remark about the even part's shear dependence. Sixth, THE POLE STATEMENT IS SCOPED TWICE: to REAL mass, and to THIS FRAME'S SLICE DECOMPOSITION -- it says nothing about the #7338 charts' metric-coupled vertical Schur, which is a different decomposition on different fixtures."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Temporal-Link Extraction — the invertible transporter, the exact parity theorem, the staggered ADM split, and the real-mass-regular pole locus

**Date:** 2026-08-24
**Runner:** `scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py`
**Stack parent:** Block 183, the derived reflection and the seam-dual frame
(`docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_THEOREM_NOTE_2026-08-24.md`),
whose reflection `R`, dual block `M H(q,v) M^T`, cell field reflection `theta`
and sixteen-member closed frame family this block uses and does not re-derive;
over Block 182's dual-patch pullback, Block 181's section frame and Block 128's
certified Block 105 curved carrier.
**Charter parent:** Block 106, the local dual patch descent
(`docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md`),
whose §12 step 1 — *"derive the reflection-odd ADM temporal link and seam overlap
from `Q_E(H_patch)` … rather than prescribing it"* — is the instruction this
block executes, and whose §12 step 2, the two-history Gram, is the successor this
block hands off to.
**Stack:** the gravity mainline, G4. Landing as block 184 on the b183 branch
after review.
**Standing:** bounded theorem, **PROPOSED**, branch-local. Scout measurement
only. Nothing here is registered and nothing is adopted; **no landed note is
edited and no landed number is touched.**

---

## N0 — THE BANNER, and it comes before any numeral

**EVERYTHING THIS BLOCK BUILDS IS AN IMPOSED MEASURED OBJECT, AND NOTHING HERE
IS REGISTERED.** The imposed objects are:

1. the certified **Block 105 curved carrier** exactly as landed by **Block 128**
   and re-used by **Blocks 181, 182 and 183** — the `8x4` cover of dimension 32,
   the parameterized cover Hodge `H[g]` over the landed Block 105 overlap field,
   the chart differential `d_00`, and the completion convention
   `Q(H,d) = m*H + i*(H d + d^H H)` at **symbolic positive mass**;
2. the **minimal reflection-closed frame** `H_min = (H + U_x^T H U_x)/2` —
   **one admitted member** of the sixteen-member equal-weight closed family
   Block 183 enumerated, taken here **because it is the minimal one**;
3. **Block 183's derived reflection** `R = P_edge * tpar` with its conjugate
   differential `d_ref = R d_00 R^-1`, its cell map
   `M = [[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]]`, the dual block
   `M H(q,v) M^T` and the cell field reflection `theta(t,x) = ((2-t)%4, x)`,
   all **rebuilt** here from the landed runners and imported from no scratchpad;
4. the **band decomposition** by time separation
   `dt = (row//4 - col//4) mod 8`, with the per-bond link blocks
   `L_t = Q_min[slice t+1, slice t]` and the intra-slice blocks
   `D_t = Q_min[slice t, slice t]`;
5. the **per-slice symbolic field** `(q_t, v_t)` constant in `x`, with the
   odd/even split of a link block under `q -> -q`;
6. **Block 128's landed antiperiodic quotient** `psi(t+4) = -psi(t)` applied to
   `Q_min`, with its four quotient bonds.

**ZERO are registered and ZERO are adopted.** They are MEASURED here and they
are **never registered**. No premise class is touched, no landed note is edited,
and **PROPOSALS STAY PROPOSALS**.

**AND THE SECOND THING THIS BANNER SAYS IS WHAT IS *NOT* CLAIMED.**

- **NO OS OR REFLECTION-POSITIVITY THEOREM IS CLAIMED.** Extracting a link is
  not showing a pairing positive. **No pairing is shown positive anywhere in
  this block**, and the runner gates the key as a declared constant.
- **NO TWO-HISTORY GRAM IS BUILT.** It is the next leg. What this block supplies
  are its two **inputs** — an invertible transporter and a regular Schur
  complement — as measurements.
- **NO GRAVITY RESULT IS CLAIMED.** The whole block is **kinematic frame data**.
- **NO ADM QUANTITY IS DERIVED.** The lapse/shift identification of the even/odd
  bond alternation is a **READING** of a measured structure, marked as one at
  every occurrence, and gated as not claimed.
- **NO UNIQUENESS IS CLAIMED FOR THE FRAME.** `{I, U_x}` is **one admitted
  member** of a sixteen-member family whose uniqueness Block 183 **refuted**.
  Minimality is a choice criterion; it is not a selection principle.

**AND THE THIRD THING IS THE STANDING OF EVERY PARENT.** **EVERY BLOCK 104, 105,
106, 128, 181, 182 AND 183 NUMBER STANDS EXACTLY AS LANDED.** What this block
corrects is **one of its own solve-side clauses**, refuted by the adversarial
check before landing and recorded in N7.

---

## W1 — the wall, the frame choice, and the charter

### What was open

Block 183 built the reflection and then said, in its own not-claimed list, that
it had **not** used it: *"NO TEMPORAL-LINK EXTRACTION IS PERFORMED"* — the
`dt=+-1` band was named, counted at 72 entries, and left to the successor. Its
`next_trace_action` item (i) went further and said **where** the extraction
should be posed: **against the dual frame**, because the reflection carries the
action to the dual-frame action at the reflected field rather than back to
itself.

Behind Block 183 stands the older instruction. **Block 106 §12 step 1** asked
for the reflection-odd ADM temporal link and the seam overlap to be **derived
from the action rather than prescribed**, and its step 2 named the two-history
Gram as what comes after. Both sentences are read by the runner from Block 106's
**primary body**, and gate `C` fails if either is absent.

### The frame choice, and what it is not

**THIS BLOCK WORKS AT ONE FRAME AND SAYS SO FIRST.** Block 183 enumerated the
complete equal-weight reflection-closed family: **sixteen** sets, **fifteen** of
them proper subsets of the full orbit, **all** positive definite, with
**`{I, U_x}` the minimal member** — and it **refuted** uniqueness rather than
leaving it unclaimed.

`H_min = (H + U_x^T H U_x)/2` is that minimal member. **THE CRITERION IS
MINIMALITY AND THE CRITERION IS NOT A SELECTION PRINCIPLE.** Nothing below shows
that the link structure is frame-independent, and nothing below is evidence that
another member of the family would give the same numbers. What the runner does
measure, before it bands anything, is that this frame is **usable**: it closes
under `R` at zero residual and it is positive definite by 32 exact leading
minors.

### The charter

**CUT THE ACTION INTO ITS TIME BANDS AND MEASURE WHAT THE LINK ACTUALLY IS.**
Take the census first; identify the link; ask whether the backward link is
recoverable from the forward one; ask whether each per-bond block is invertible;
ask what the reflection does to the link **against the dual frame**; put the
field into symbols and see what the even and odd bonds carry; take the
intra-slice determinants and find the pole locus; and push all of it through the
landed antiperiodic quotient. Measure the failing neighbour of every positive
statement **in the same run**. **THE AXIOMS ARE NOT TOUCHED**, no obligation is
retired, and **no axiom amendment is justified** by anything below.

---

## N1 — THE BAND STRUCTURE, AND THE LINK IS A PAIR

### The controls come first

- **`H[landed field]` equals the LANDED `b128.curved_hodge_cover()`** — zero
  residual. The object being banded is the landed object.
- **`R R^T = I`** — zero residual. `R` is real orthogonal, `R^-1 = R^T`, and
  **no operator inverse is ever formed** anywhere in this block.
- **`R H_min R^-1 = H_min_dual[theta g]`** — zero residual. The frame is
  genuinely one of Block 183's closed points, so the parity theorem below is
  asked at a point where the reflection **has somewhere to send** the action.
- **`H_min` is positive definite** by **32 exact leading principal minors** —
  exact rational determinants, no eigenvalue estimate, no tolerance.

**THE CONTROLS COME FIRST BECAUSE OTHERWISE THE STRUCTURE IS BOUGHT.**

### The census

With `Q_min = Q(H_min, d_00)` at symbolic positive mass, and time separation
`dt = (row//4 - col//4) mod 8`:

**`{dt=0: 80, dt=+1: 72, dt=+2: 16, dt=-2: 16, dt=-1: 72}` — 256 nonzero
entries in five bands and NOTHING outside them.**

**AND TWO OTHER POINTS CARRY THE SAME CENSUS, BOTH MEASURED HERE RATHER THAN
RECALLED**: the **dual-frame** action `Q_dual`, and **Block 181's equal-weight
four-origin point**, which the runner rebuilds with the same code from the same
landed field. The equal-weight point is a **genuinely different frame** — it
differs from `H_min` at **96** entries — so the agreement is a fact about the
band structure and not about the two points being the same object.

**THE LINK IS THE `dt=+-1` PAIR**: 72 entries forward and 72 back.

### The link is irreducibly a pair

**THE BACKWARD LINK IS NOT RECOVERABLE FROM THE FORWARD LINK.** Measured, in the
same run:

- `B_-1` is **not** the adjoint of `B_+1` — **40** nonzero entries;
- **not** minus its adjoint — **32**;
- **not** its transpose — **40**.

Three explicit non-identities. **THE TRANSPORTER DATA IS THE PAIR AND NOT ONE
BLOCK**, which is a fact about the completion convention `m*H + i(H d + d^H H)`:
the anti-Hermitian half is not a symmetry of the band decomposition.

**VERDICT N1: the action's support is exactly five time bands; the link is the
`dt=+-1` pair; and the pair carries two independent blocks, neither recoverable
from the other by adjoint, sign or transpose.**

---

## N2 — THE TRANSPORTER IS INVERTIBLE AT EVERY BOND

Slice the link into its eight `4x4` per-bond blocks
`L_t = Q_min[slice t+1, slice t]`, `t = 0..7`:

- **ALL EIGHT HAVE RANK EXACTLY 4;**
- **ALL EIGHT HAVE EMPTY KERNELS;**
- nonzero counts **`(10, 8, 10, 8, 10, 8, 10, 8)`** — **10** at even `t`, **8**
  at odd `t`.

**THE TEMPORAL TRANSPORTER IS INVERTIBLE BOND BY BOND**, at symbolic positive
mass, on this frame.

**AND IT LOCATES THE CARRIER'S DEGENERACY SOMEWHERE ELSE.** Block 128 found a
kernel on this carrier; it is **not in the link**. Whatever degeneracy the
carrier has must live in the **slice Schur complement** — which is exactly the
object N4 measures, and which N4 finds regular at every real mass. The two
statements are the two halves of one answer.

**THIS IS THE INPUT THE TWO-HISTORY GRAM NEEDS**, and it is supplied here as a
measurement rather than as an assumption. **The Gram itself is not built.**

**VERDICT N2: the link is invertible at every bond with an alternating 10/8
support, and the carrier's degeneracy is not in it.**

---

## N3 — THE PARITY THEOREM, AND ITS DIFFERENTIAL CONVENTION IS LOAD-BEARING

### The theorem

**`R B_+1 R^-1 = the dt=-1 band of Q_dual` — ZERO RESIDUAL**, where

`Q_dual = m*H_min_dual[theta g] + i(H_min_dual d_ref + d_ref^H H_min_dual)`

is the **dual-frame** completion built with the seam identity's own differential
`d_ref = R d_00 R^-1`.

**THE FORWARD LINK MAPS EXACTLY ONTO THE DUAL BACKWARD LINK.** This is Block
183's `next_trace_action` item (i) answered in its own terms: the extraction is
posed **against the dual frame**, and against the dual frame it closes exactly.

### Three failing neighbours, measured in the same run

- against the **WRONG dual** — the one built with `d_00` in place of `d_ref` —
  **16** nonzero entries;
- against the **`dt=+1`** band of the dual — **144**;
- against the **`dt=-1`** band of the **original** frame — **96**;
- and the **undressed** site reflection `P_edge` fails at **72**.

**THE 16 IS THE SHARPEST OF THEM, AND IT IS THE ONE THAT MATTERS**: the theorem
is specific to the dual frame **and** to that frame's own differential. A reader
who substitutes `d_00` gets a **false statement**, off by exactly sixteen
entries.

### The convention catch, recorded as process

**THE FIRST COMPARISON RUN IN THE SOLVE USED `d_00`, AND IT FAILED — AT EXACTLY
THE 16 ENTRIES GATED ABOVE.** The seam identity's own differential `d_ref` was
substituted and the residual went to **zero**.

**THIS IS NOT A CORRECTION AND IT IS NOT RECORDED AS ONE.** Nothing wrong ever
left the solve: the failing comparison was caught by the control that was
measured alongside it, in the same run, before any claim was written down. It is
recorded here as **process**, in N7, because the mechanism is the useful part —
**the control-first rule found it, and the re-measure rule fixed it** — and
because the failing convention is now **gated**, at the count it failed by, so
that no successor can quietly reintroduce it.

**VERDICT N3: the derived reflection maps the forward temporal link exactly onto
the dual frame's backward link, and three neighbouring statements — including
the natural wrong one — fail in the same run.**

---

## N4 — THE SYMBOLIC ADM SPLIT AND THE POLE LOCUS

### The odd bonds are pure shear

Put the field into symbols: `(q_t, v_t)` per slice, constant in `x`, and write
`a_t = q_t v_t / (q_t^2 - 1)`. Then the **odd** bond `L_1` has **exactly 8
nonzero entries**, and the whole table is exhibited:

| position | entry |
| --- | --- |
| `(0,0)`, `(2,2)` | `-3 a_1 / 20` |
| `(0,2)`, `(2,0)` | `+3 a_1 / 20` |
| `(0,1)`, `(1,2)`, `(2,3)`, `(3,0)` | `m a_1 / 4` |

Every entry carries the factor `q_1 v_1`, so **`L_1` VANISHES IDENTICALLY AT
`q_1 = 0`**. **THE ODD BOND IS PURE SHEAR TRANSPORT AND THE MASS RIDES ON THE
SHEAR**: at zero shear there is no odd bond at all.

### The even bonds carry four more entries

The **even** bond `L_0` has **10** nonzero entries, splitting under `q -> -q`
into **exactly 8 odd and 4 even**. **THE MASS APPEARS ONLY IN THE ODD PART** —
`m` is absent from the even part entirely — and at `q_0 = 0` exactly the **4**
even entries survive.

**THE EVEN PART, IN CLOSED FORM.** It is **four diagonal entries** with signs
`(-, +, -, +)` and one common magnitude:

**`E = (1/v_0 + v_1 - v_0/(q_0^2 - 1) - v_1/(q_1^2 - 1)) / 5`.**

**AND `E` IS NOT FREE OF THE SHEAR.** Its two shear derivatives are

**`dE/dq_0 = 2 q_0 v_0 / (5(q_0^2 - 1)^2)`** and
**`dE/dq_1 = 2 q_1 v_1 / (5(q_1^2 - 1)^2)`**,

both **nonzero** — and both **odd**, which is exactly *why* `E` is even and why
the 8/4 parity split survives. The solve's compressed clause said the even part
had *"no q dependence"*; **that clause is refuted** and N7 records the
correction. What is true is the weaker and more interesting statement: the even
part depends on the shears **through even powers only**.

**AND THE WITNESS CONSTRAINT COLLAPSES IT.** The landed Block 105 field is
Pythagorean at every cell, `q_t^2 + v_t^2 = 1`. Under that constraint

**`E = (v_1 + 1/v_1 + 2/v_0) / 5` — exactly.**

The shear dependence is real, and on the witness locus it is carried entirely by
the volumes.

### The reading, marked as a reading

**(Reading R1, §READINGS.)** The even/odd alternation has the shape of the ADM
lapse/shift split: **odd bonds = pure shift/shear transport with the mass
coupled to it, even bonds = the same shear pattern plus lapse-and-volume data of
the two adjacent slices.** And the shear-**squared** corrections in the
lapse-transport weights are what an ADM decomposition would predict, since the
inverse metric's time components carry shift-squared terms. **IT IS A READING.
NO ADM QUANTITY IS DERIVED HERE, THE PHYSICAL REMARK IS UNTESTED, AND THE BANNER
KEY IS GATED AS A DECLARED CONSTANT.**

### The pole locus

Take the intra-slice blocks `D_t = Q_min[slice t, slice t]`. Their determinants:

- **slices `t` and `t+4` agree exactly**, so there are **four distinct**
  determinants;
- each is a polynomial in `m` of **degree 4 with only even powers** — an **even
  quartic**;
- and **every one of the twelve coefficients is strictly positive.**

An even polynomial with positive coefficients is strictly positive at every real
argument, and the `m = 0` end is **gated separately** so the massless point is
not taken on faith. Therefore:

**`det D_t > 0` FOR EVERY REAL `m`, INCLUDING `m = 0`.**

**THE SLICE SCHUR FACTORIZATION IS GLOBALLY REGULAR ON THE PHYSICAL MASS AXIS**
at this frame's decomposition; the poles sit at `m^2 < 0`, off the physical line.
Two of the four determinants factor as explicit products of positive linear
factors in `m^2`; all four are printed by the runner.

**THE SCOPE OF THAT SENTENCE IS NARROW AND IT IS STATED TWICE.** It discharges
the `#7338` no-pole-free-section warning **for real mass, at this frame's slice
decomposition, and nowhere else.** `#7338`'s poles are **metric-coupled vertical
Schur poles on two pre-registered stationary-section charts** — a **different
decomposition on different fixtures**. Nothing here touches those, nothing here
says a physical reduction exists, and the warning stands where it was raised.

### The descent

Push `Q_min` through **Block 128's landed antiperiodic quotient**
`psi(t+4) = -psi(t)`:

- the census becomes **`{0: 40, +1: 36, +2: 16, -1: 36}`** on the
  16-dimensional carrier;
- **all four quotient bonds have rank 4**, with the same **10/8** alternation.

**THE LINK SURVIVES THE DESCENT**, which is what makes the quotient a place the
successor can be posed at all.

**AND THE SEAM SIGN IS A CERTIFICATE.** At the **same field pair** on both
sides, the quotient's seam bond is **minus** the cover's bond `3 -> 4`, exactly:
the **sum is the zero matrix**, the **difference is not**, and the entrywise
ratio is **`-1` at all eight common nonzero positions** `(0,0)`, `(0,1)`,
`(0,2)`, `(1,2)`, `(2,0)`, `(2,2)`, `(2,3)`, `(3,0)`. The solve left this
comparison **queued** as a certificate it had not run cleanly — the seam-vs-bulk
comparison it *had* run confounded the twist with the field difference, since it
compared different slice pairs. **THE ADVERSARIAL CHECKER RAN THE CLEAN ONE, AND
THE CHECKER'S MEASUREMENT IS WHAT IS GATED.**

**VERDICT N4: the odd bonds are pure shear and vanish with it, the even bonds
add four diagonal entries free of the mass but not of the shear, the slice
determinants are strictly positive at every real mass, and the whole structure
descends to the antiperiodic quotient with an exactly negated seam bond.**

---

## READINGS — two of them, and each is a reading

**THE TWO-REGISTER RULE APPLIES: what follows is not measured and nothing below
is licensed by anything above.**

- **(R1) THE ADM LAPSE/SHIFT READING OF THE EVEN/ODD ALTERNATION.** N4's split
  — odd bonds pure shear, even bonds shear plus adjacent-slice lapse/volume data
  — has the shape of an ADM decomposition, and the even part's shear-squared
  dependence is the shape a shift-squared term would take. **IT IS A READING.**
  No ADM quantity is derived anywhere in this note, no comparison to a continuum
  ADM decomposition is made, and the banner key is gated as a declared constant.
- **(R2) THE READING THAT THE PARITY THEOREM IS THE OS STATEMENT'S SKELETON.**
  N3's exact map from the forward link to the dual frame's backward link is what
  an OS reflection-positivity argument would need to *pose* its pairing across
  the bond. **IT IS A READING.** A covariance identity is not a positivity
  statement, **no pairing is shown positive anywhere in this block**, and the
  Gram where positivity would first be tested is not built.

---

## N5 — the fence

```text
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- the certified Block 105 curved carrier as landed by Block 128 and re-used by Blocks 181, 182 and 183 (the 8x4 cover of dimension 32, the parameterized cover Hodge over the LANDED Block 105 overlap field, the chart differential d_00, and the completion Q(H,d) = m*H + i*(H d + d^H H) at SYMBOLIC POSITIVE MASS), THE MINIMAL REFLECTION-CLOSED FRAME H_min = (H + U_x^T H U_x)/2 taken as ONE ADMITTED MEMBER of the sixteen-member family Block 183 enumerated and chosen for MINIMALITY ALONE, Block 183's derived reflection R = P_edge * tpar with d_ref = R d_00 R^-1, the cell map M and the dual block M H(q,v) M^T and the cell field reflection theta(t,x) = ((2-t)%4, x), the BAND DECOMPOSITION by dt = (row//4 - col//4) mod 8 with the per-bond link blocks L_t and the intra-slice blocks D_t, the PER-SLICE SYMBOLIC FIELD (q_t, v_t) constant in x with its odd/even split under q -> -q, and Block 128's LANDED antiperiodic quotient are IMPOSED MEASURED OBJECTS OF THIS BLOCK, rebuilt from the LANDED Block 128 runner and the Block 105 module it re-exports and from NOTHING in any scratchpad. NO OS OR REFLECTION-POSITIVITY THEOREM IS CLAIMED and no pairing is shown positive anywhere; NO TWO-HISTORY GRAM IS BUILT, it being the next leg; NO GRAVITY RESULT IS CLAIMED; THE ADM LAPSE/SHIFT IDENTIFICATION IS A READING OF THE MEASURED EVEN/ODD STRUCTURE AND IS NOT A THEOREM; AND NO UNIQUENESS IS CLAIMED FOR THE FRAME, which is one admitted member of a sixteen-member family whose uniqueness Block 183 REFUTED. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.
per_site: THE BAND STRUCTURE, AND THE LINK IS A PAIR. The band census of Q_min = Q(H_min, d_00) by time separation is EXACTLY {dt=0: 80, dt=+1: 72, dt=+2: 16, dt=-2: 16, dt=-1: 72} -- 256 nonzero entries in five bands and NOTHING outside them. THE SAME CENSUS IS CARRIED BY THE DUAL-FRAME ACTION AND BY THE BLOCK 181 EQUAL-WEIGHT POINT, both MEASURED HERE by the same code from the same landed field, the equal-weight point differing from this frame at 96 entries so that the agreement is a fact about the band structure and not about the two points being the same object. THE LINK IS THE dt=+-1 PAIR AND IT IS IRREDUCIBLY A PAIR: B_-1 is NOT the adjoint of B_+1 (40 nonzero entries), NOT minus its adjoint (32) and NOT its transpose (40). THE BACKWARD LINK IS NOT RECOVERABLE FROM THE FORWARD LINK BY ANY OF THE THREE, so the transporter data is the pair and not one block. THE CONTROLS COME FIRST: the parameterized Hodge at the landed field IS the LANDED curved_hodge_cover() at zero residual, R is real orthogonal at zero residual, the frame closes under the reflection at ZERO residual, and the frame is POSITIVE DEFINITE by 32 exact leading principal minors.
per_mode: THE TRANSPORTER IS INVERTIBLE AT EVERY BOND. The eight per-bond blocks L_t = Q_min[slice t+1, slice t] ALL HAVE RANK EXACTLY 4 and ALL HAVE EMPTY KERNELS, with nonzero counts alternating 10 at even t and 8 at odd t. THE BLOCK 128 KERNEL IS NOT IN THE LINK: the temporal transporter is invertible bond by bond on this frame, and whatever degeneracy the carrier carries lives in the slice Schur complement rather than in the link. THIS IS THE INPUT THE TWO-HISTORY GRAM NEEDS AND IT IS SUPPLIED HERE AS A MEASUREMENT, NOT AS AN ASSUMPTION.
per_block: THE PARITY THEOREM, EXACT, AND ITS DIFFERENTIAL CONVENTION IS LOAD-BEARING. R B_+1 R^-1 = the dt=-1 band of Q_dual EXACTLY, at ZERO residual, where Q_dual = m*H_min_dual[theta g] + i(H_min_dual d_ref + d_ref^H H_min_dual) is the DUAL-FRAME completion built with the SEAM IDENTITY'S OWN differential d_ref = R d_00 R^-1. THE FORWARD LINK MAPS EXACTLY ONTO THE DUAL BACKWARD LINK. AND THE CONVENTION IS MEASURED RATHER THAN ASSERTED: against the WRONG dual, the one built with d_00 in place of d_ref, the residual is EXACTLY 16 NONZERO ENTRIES; against the dt=+1 band of the dual it is 144; and against the dt=-1 band of the ORIGINAL frame it is 96. THREE FAILING NEIGHBOURS MEASURED IN THE SAME RUN, AND THE 16 IS THE SHARPEST OF THEM: the theorem is specific to the dual frame AND to its own differential, and a reader who substitutes d_00 gets a false statement.
lattice_wide: THE SYMBOLIC ADM SPLIT, AS THE ADVERSARIAL CHECK CORRECTED IT, AND THE READING THAT GOES WITH IT IS MARKED. At a per-slice symbolic field (q_t, v_t) constant in x, and with the shear variable a_t = q_t v_t / (q_t^2 - 1), THE ODD BONDS CARRY PURE SHEAR: L_1 has EXACTLY 8 nonzero entries and the whole table is exhibited -- -3 a_1/20 at (0,0) and (2,2), +3 a_1/20 at (0,2) and (2,0), and m a_1/4 at (0,1), (1,2), (2,3) and (3,0) -- so L_1 VANISHES IDENTICALLY AT q_1 = 0. THE EVEN BONDS CARRY THE SAME 8-ENTRY SHEAR PATTERN PLUS FOUR MORE: L_0 has 10 nonzero entries splitting EXACTLY 8 ODD and 4 EVEN under q -> -q, THE MASS APPEARS ONLY IN THE ODD PART, and at q_0 = 0 exactly the 4 even entries survive. THE EVEN PART IS FOUR DIAGONAL ENTRIES WITH SIGNS (-,+,-,+) AND COMMON MAGNITUDE E = (1/v_0 + v_1 - v_0/(q_0^2 - 1) - v_1/(q_1^2 - 1))/5, AND IT IS GENUINELY SHEAR-DEPENDENT: dE/dq_0 = 2 q_0 v_0/(5(q_0^2 - 1)^2) and dE/dq_1 = 2 q_1 v_1/(5(q_1^2 - 1)^2) are both NONZERO and both ODD, which is exactly why E is EVEN and why the 8/4 parity split stands. THE SOLVE'S 'no q dependence' CLAUSE IS REFUTED BY MEASUREMENT AND THE CHECKER'S VERSION IS WHAT SHIPS. UNDER THE PYTHAGOREAN WITNESS CONSTRAINT q_t^2 + v_t^2 = 1, WHICH THE LANDED FIELD SATISFIES AT EVERY CELL, E REDUCES EXACTLY TO (v_1 + 1/v_1 + 2/v_0)/5. THE READING, MARKED AS A READING: the even/odd bond alternation realizes the ADM lapse/shift split, even bonds carrying lapse-and-volume data of ADJACENT slices plus the shear and odd bonds carrying pure shear transport with the mass coupled to it, and the shear-SQUARED corrections in the lapse-transport weights are what an ADM decomposition would predict, the inverse metric's time components carrying shift-squared terms. NO ADM QUANTITY IS DERIVED, THE IDENTIFICATION IS NOT A THEOREM, THE PHYSICAL REMARK IS UNTESTED HERE, AND THE BANNER KEY IS GATED AS A DECLARED CONSTANT.
per_scope: THE POLE LOCUS, THE QUOTIENT, AND THE SEAM SIGN. The eight intra-slice blocks D_t have determinants that are EVEN QUARTICS IN m WITH ALL THREE COEFFICIENTS STRICTLY POSITIVE; slices t and t+4 agree exactly so there are FOUR distinct determinants; and therefore det D_t > 0 FOR EVERY REAL m INCLUDING m = 0, gated at the coefficient level and again at m = 0. THE SLICE SCHUR FACTORIZATION IS GLOBALLY REGULAR ON THE PHYSICAL MASS AXIS AT THIS FRAME'S DECOMPOSITION, with the poles at m^2 < 0 off the physical line. THE SCOPE IS EXACT AND IT IS NARROW: the #7338 no-pole-free-section warning is DISCHARGED FOR REAL MASS AT THIS DECOMPOSITION ONLY -- their metric-coupled vertical Schur poles are a DIFFERENT decomposition on DIFFERENT fixtures, and nothing here touches those. AND THE BLOCK DESCENDS: on Block 128's LANDED 16-dimensional antiperiodic quotient the band census is EXACTLY {0: 40, +1: 36, +2: 16, -1: 36} and all four quotient bonds have rank 4 with the same 10/8 alternation. AND THE TWIST CERTIFICATE IS A CERTIFICATE RATHER THAN AN EXPECTATION: the quotient seam bond equals MINUS the cover bond 3 -> 4 at the SAME field pair, EXACTLY -- the sum is the zero matrix, the difference is not, and the entrywise ratio is -1 at all EIGHT common nonzero positions (0,0), (0,1), (0,2), (1,2), (2,0), (2,2), (2,3) and (3,0). IT WAS QUEUED BY THE SOLVE, MEASURED BY THE ADVERSARIAL CHECKER, AND THE CHECKER'S MEASUREMENT IS WHAT IS GATED: the antiperiodic seam sign is a measured fact of the descent.
RESULT: THE TEMPORAL LINK IS EXTRACTED, IT IS INVERTIBLE AT EVERY BOND, IT OBEYS AN EXACT PARITY THEOREM AGAINST THE DUAL FRAME, ITS SYMBOLIC FORM SPLITS EVEN AND ODD BONDS, AND THE SLICE DETERMINANTS ARE STRICTLY POSITIVE FOR EVERY REAL MASS. The band census is {0: 80, +-1: 72, +-2: 16}; the eight per-bond blocks all have rank 4 and empty kernels at 10/8 nonzeros; R B_+1 R^-1 is the dual frame's dt=-1 band at ZERO residual against failing neighbours at 16, 144 and 96; the odd bonds are pure shear vanishing at zero shear while the even bonds carry four more diagonal entries, free of the mass and of common magnitude E, which is even in the shears but NOT free of them; the four distinct slice determinants are even quartics with every coefficient strictly positive; the quotient census is {0: 40, +-1: 36, +2: 16} with four full-rank bonds; and the quotient seam bond is MINUS the cover bond 3 -> 4 exactly. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.
DECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 128, 181, 182 and 183 STAND EXACTLY AS LANDED; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: it is a SINGLE FIXTURE FAMILY, the b128 8x4 cover over the certified Block 105 curved carrier, at ONE landed field for the numeric legs and ONE per-slice symbolic family for the split, with NO width ladder and NO second carrier rule; it works at ONE MEMBER of Block 183's sixteen-member closed frame family, chosen for MINIMALITY, with NO UNIQUENESS CLAIMED; THE ADM LAPSE/SHIFT IDENTIFICATION IS A READING AND NOT A THEOREM; THE POLE STATEMENT IS SCOPED TO REAL MASS AND TO THIS FRAME'S SLICE DECOMPOSITION and says nothing about the #7338 charts' own vertical Schur; NO OS OR REFLECTION-POSITIVITY THEOREM IS CLAIMED and no pairing is shown positive; NO TWO-HISTORY GRAM IS BUILT; and the whole block is KINEMATIC FRAME DATA. AND ONE SOLVE-SIDE CLAUSE WAS REFUTED BY THE ADVERSARIAL CHECK BEFORE LANDING AND THE CHECKER'S VERSION IS WHAT SHIPS: the even part of the even bond is NOT free of the shear -- it is four diagonal entries of common magnitude E, EVEN in the shears but genuinely q^2-dependent, both derivatives nonzero -- against the solve's compressed 'no q dependence' clause. THE ERROR WAS A SPEC COMPRESSION: the anchor's own displayed formula already carried the q^2 dependence and the summary clause outran it, and the rule reaffirmed is STATE FORMULAS, NOT SUMMARIES, IN CLAIM REGISTERS. THE d_ref CONVENTION CATCH IS A DIFFERENT THING AND IS RECORDED AS PROCESS AND NOT AS A CORRECTION: the first comparison in the solve used d_00 for the dual differential and failed at 16 entries, the seam identity's own differential d_ref was substituted and the residual went to ZERO, and the whole exchange happened INSIDE the solve and never left it. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE TEMPORAL-LINK EXTRACTION COMPLETE anchor, as corrected by the b184 adversarial check.
TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

The fence above appears BYTE-IDENTICALLY in the runner as a single-line literal
with `\n` separators, and gate H byte-checks it against this occurrence.

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

- **THE HOPE THAT THE LINK PAIR REDUCES TO ONE BLOCK — DEAD BY MEASUREMENT.**
  Three non-identities at 40, 32 and 40.
- **THE WORRY THAT THE LINK CARRIES THE CARRIER'S KERNEL — DEAD BY
  MEASUREMENT.** Eight bonds, rank 4, empty kernels.
- **THE PARITY THEOREM AGAINST THE SAME FRAME — DEAD AT 96.** The reflection
  does not send the link back into its own frame; it sends it to the dual.
- **THE PARITY THEOREM WITH `d_00` AS THE DUAL DIFFERENTIAL — DEAD AT 16.**
  Caught inside the solve, gated here.
- **THE READING THAT THE EVEN PART IS SHEAR-FREE — DEAD BY DERIVATIVE.**
  `dE/dq_0` and `dE/dq_1` are both nonzero.
- **THE WORRY THAT THE SLICE SCHUR HAS A REAL-MASS POLE — DEAD BY COEFFICIENT
  SIGN**, at this frame's decomposition and for real mass only.
- **THE SEAM-VS-BULK BOND COMPARISON AS A TWIST CERTIFICATE — DEAD AS POSED.**
  It confounded the twist with the field difference. The clean comparison, at the
  same field pair, is what replaced it.

### REOPEN IF

1. **THE TWO-HISTORY GRAM IS BUILT** — Block 106 §12 step 2, on both spatial
   eigenlines, now that its two inputs are measured. **Nothing in this note is a
   positivity statement**, and the Gram is where positivity would first be
   tested.
2. **AN OS / REFLECTION-POSITIVITY STATEMENT IS ATTEMPTED ON THE SEAM PAIRING**
   — the parity theorem is a covariance identity and would have to be *used*,
   not merely quoted.
3. **A SECOND FRAME IS MEASURED** — every number here is at the minimal member
   of Block 183's sixteen. Nothing here shows the link structure is
   frame-independent, and a second member would be the cheapest test of that.
4. **AN ADM QUANTITY IS ACTUALLY DERIVED** from the even/odd split, rather than
   the split's shape being recognized.
5. **A SECOND CARRIER, A SECOND FIELD OR A WIDTH LADDER IS BUILT** — one fixture
   family, and nothing here is evidence the pattern persists.
6. **THE `#7338` CHARTS' OWN VERTICAL SCHUR IS REVISITED** — the regularity
   proved here is about a different decomposition and does not transfer.

---

## N7 — THE RECORD

### Corrections carried

**THIS BLOCK CORRECTS NO LANDED NUMBER AND EDITS NO LANDED NOTE.** What it
corrects is **one of its own solve-side clauses**, caught **before landing** by
the check lane.

1. **THE SUPERVISOR'S THIRTEENTH CORRECTION — THE SPEC-COMPRESSION ERROR.** The
   solve recorded the even bond's even part as having **"no q dependence"**.
   **That is false.** The even part is four diagonal entries with signs
   `(-,+,-,+)` and common magnitude
   `E = (1/v_0 + v_1 - v_0/(q_0^2 - 1) - v_1/(q_1^2 - 1))/5`, which is **even**
   in the shears — the parity split stands, and `dE/dq_0` and `dE/dq_1` are odd,
   which is why — but **genuinely `q^2`-dependent**, both derivatives nonzero.
   **THE MECHANISM OF THE ERROR IS RECORDED BECAUSE IT IS THE USEFUL PART:** the
   campaign anchor's own displayed formula already carried the `q^2` dependence,
   and the **compressed summary clause outran the formula it was summarizing**.
   **THE RULE REAFFIRMED: STATE FORMULAS, NOT SUMMARIES, IN CLAIM REGISTERS.**
   The runner enforces it on itself — gate `F` gates the closed form, both
   derivatives and the Pythagorean reduction, and `break_even_part` restores the
   refuted clause and must fail.
2. **WHAT IS NOT A CORRECTION IS SAID JUST AS PLAINLY.** The **`d_ref`
   convention catch** of N3 is **process, not a correction**: the first
   comparison used `d_00`, failed at exactly 16 entries, and the seam identity's
   own differential took the residual to zero — **all inside the solve, caught
   by the control measured alongside it, and never written down as a claim.**
   The **control-first rule** found it and the **re-measure rule** fixed it; both
   are Block 183's own process rules applied inline. The failing convention is
   now gated at the count it failed by.
3. **AND WHAT ELSE IS NOT CORRECTED.** Every Block 104, 105, 106, 128, 181, 182
   and 183 number — Block 183's `R^2 = -I`, its 16/16 census, its 96 / 256
   equal-weight failures, its sixteen closed sets, Block 128's kernel — **STANDS
   AS LANDED**. This block touches none of them.

### The adversarial check

**ADVERSARIAL CHECK: RUN AND FOLDED. codex 5.6-sol xhigh, cross-model,
independent exact-SymPy reconstruction from the bounded public sources only.
OVERALL VERDICT: REFUTED-LOCALIZED-TO-C4-THEN-FOLDED — seven of eight checks
CONFIRMED exactly, ONE clause refuted and replaced by the checker's version.**
The findings file is preserved at
`.claude/science/physics-loops/generator-program-20260821/b184_check_findings.md`.

**Confirmed exactly (C1–C3, C5–C8):** the band census `80 / 72 / 16`; all eight
per-bond link blocks at rank 4; the parity theorem at **zero** against the
wrong-convention **16**; the four distinct determinants with **independently
verified positive constant terms**; the quotient census `40 / 36 / 16 / 36`; the
twist ratio of **`-1` at eight positions**; and Block 183's seam identity holding
at **zero** on the minimal frame.

**The one refutation, folded throughout this note (C4):** the even part's
**"no q dependence"** clause. The checker supplied the replacement in closed
form — four diagonal entries, signs `(-,+,-,+)`, common magnitude `E`, both
shear derivatives nonzero and odd — together with the **bonus identity** now
gated as content: under the Pythagorean witness constraint `q_t^2 + v_t^2 = 1`,
`E` reduces exactly to `(v_1 + 1/v_1 + 2/v_0)/5`.

**The checker's gift, recorded and attributed:** the **twist certificate**, which
the solve left **queued** rather than claimed. The checker ran the clean
comparison — quotient seam bond against cover bond `3 -> 4` at the **same field
pair** — and measured **exact negation**, entrywise ratio `-1` at all eight
common nonzero positions. It is gated in this block's runner as a certificate,
not as an expectation, and the runner's `break_twist_negation` mutation guards
it.

**THE CHECKER'S FINDINGS OVERRIDE THE SOLVE EVERYWHERE THEY COLLIDE**; in this
block they collided **once**, and in that collision **the checker's version is
what ships**.

### Worker profile, and the cross-model disclosure

**THE WORKER PROFILE IS DISCLOSED IN FULL.** All solve-side science and the
synthesis were done by the supervising frontier model **INLINE**, per the
owner's standing directive. **THE ADVERSARIAL CHECK IS RUN BY A cross-model
WORKER**, machinery-disjoint, and its findings override the solve — which in this
block is not a formality, since it changed one claim and supplied one
certificate. **OPUS DID MECHANICAL DRAFTING ONLY** — this note and the runner to
a fixed contract — and the supervisor reviews and lands. **COMMON-MODE RISK IS
REDUCED AND NOT ELIMINATED:** every worker shares the landed Block 128 and Block
105 fixture code, which is the single point through which an error in the
fixtures would propagate to every gate at once.

---

## N8 — the verdict, at its exact scope

### THE RESULT

**THE TEMPORAL LINK IS EXTRACTED, IT IS INVERTIBLE AT EVERY BOND, IT OBEYS AN
EXACT PARITY THEOREM AGAINST THE DUAL FRAME, ITS SYMBOLIC FORM SPLITS EVEN AND
ODD BONDS, AND THE SLICE DETERMINANTS ARE STRICTLY POSITIVE FOR EVERY REAL
MASS:**

1. **THE CONTROLS.** Landed-field Hodge control **exact**; `R R^T = I`
   **exact**; the frame's closure **exact**; `H_min` positive definite by **32**
   exact leading minors.
2. **THE CENSUS.** `{0: 80, +-1: 72, +-2: 16}` — **256** entries in five bands,
   the same for the dual-frame action and for Block 181's equal-weight point,
   which is **96** entries away from this frame.
3. **THE LINK IS A PAIR.** `B_-1` is not the adjoint (**40**), not minus the
   adjoint (**32**) and not the transpose (**40**) of `B_+1`.
4. **THE TRANSPORTER IS INVERTIBLE.** Eight bonds, **rank 4**, **empty
   kernels**, nonzero counts `(10, 8, 10, 8, 10, 8, 10, 8)`.
5. **THE PARITY THEOREM.** `R B_+1 R^-1 = B_-1[dual]` **exact**, against **16**
   (wrong dual differential), **144** (wrong band), **96** (no dual frame) and
   **72** (undressed).
6. **THE ODD BOND.** 8 entries, exhibited entrywise in `a_1`, **vanishing
   identically at `q_1 = 0`**.
7. **THE EVEN BOND.** 10 entries splitting **8 odd / 4 even**, the **mass only
   in the odd part**, the even part four diagonal entries with signs
   `(-,+,-,+)` and magnitude `E` — **even in the shears, not free of them**,
   reducing to `(v_1 + 1/v_1 + 2/v_0)/5` on the Pythagorean witness locus.
8. **THE POLE LOCUS.** Four distinct **even quartics**, **twelve strictly
   positive coefficients**, four strictly positive values at `m = 0`: **`det D_t
   > 0` at every real mass.**
9. **THE DESCENT.** Quotient census `{0: 40, +-1: 36, +2: 16}`, four bonds at
   **rank 4** with the same 10/8 alternation.
10. **THE SEAM SIGN.** The quotient seam bond is **minus** the cover bond
    `3 -> 4`, at entrywise ratio **`-1`** across all **eight** common nonzero
    positions.

### LIMITS

- **ONE FIXTURE FAMILY.** The Block 128 `8x4` cover of dimension 32 over the
  certified Block 105 curved carrier, at the landed overlap field for the
  numeric legs and one per-slice symbolic family for the split. **No width
  ladder. No second carrier rule. No second field.**
- **ONE FRAME, CHOSEN FOR MINIMALITY.** `{I, U_x}` is **one admitted member** of
  Block 183's sixteen-member closed family. **No uniqueness is claimed**, none
  is available, and **nothing here shows the link structure is
  frame-independent.**
- **THE TWO READINGS ARE READINGS.** The ADM lapse/shift reading of the even/odd
  alternation and the reading of the parity theorem as an OS skeleton are marked
  as readings at every occurrence, and **neither is a theorem.**
- **THE POLE STATEMENT IS SCOPED TWICE.** To **real mass**, and to **this
  frame's slice decomposition**. It says **nothing** about `#7338`'s
  metric-coupled vertical Schur poles, which live on different charts with
  different fixtures, and it is **not** a claim that a physical reduction exists.
- **NO OS OR REFLECTION-POSITIVITY THEOREM, NO TWO-HISTORY GRAM, NO GRAVITY, NO
  DERIVED ADM QUANTITY.** No pairing is shown positive at any scope; the block
  is **kinematic frame data**.
- **NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NOTHING IS PROPOSED AS AN
  AXIOM CHANGE.** No premise-class change is registered, no landed note is
  edited, no landed number is touched.

### What that is, and what it is not

It is a set of exact SymPy identities on **ONE FIXTURE FAMILY** at **ONE FRAME**,
with every action identity at symbolic positive mass. **It is NOT an OS or
reflection-positivity theorem.** **It is NOT a two-history Gram.** **It is NOT a
gravity result.** **It is NOT a derivation of any ADM quantity — the lapse/shift
identification is a reading.** **It is NOT a uniqueness claim for the frame.**
**It is NOT a statement about the `#7338` charts.** It is not a continuum
statement, not a Records result and not a derivation of the Born rule. **It is
not re-verified** against any independent implementation of the lattice fixtures
beyond the exact routes run here and the cross-model adversarial check. **No
priority or originality claim is made or licensed at any scope.**

### The successor question

**THE SUCCESSOR IS THE TWO-HISTORY GRAM, AND ITS INPUTS ARE NOW MEASURED.**
Block 106 §12 step 2 asked for the unnormalized two-history Gram on both spatial
eigenlines; it could not be posed without a transporter, and the transporter now
exists, is **invertible at every bond**, and sits on a slice decomposition whose
Schur complement is **regular at every real mass**. Build the Gram; then, and
only then, ask whether any pairing is positive — that is the first place an OS
statement could even be posed. The `#7338` Schur join and the gravity constraint
quotient stay downstream of both, and the section-point family is still
sixteen-member with no principle picking inside it.

### TOE

**Zero axiom retirement. ZERO OBLIGATION RETIREMENT. Zero TOE movement. No TOE
percentage moves. The retained-positive end-to-end theory count remains zero.
No axiom amendment is justified.**

---

## The runner

Every number in this note is produced by
`scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py`,
which imports the **LANDED** Block 128 runner
`scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py`
(and the Block 105 module it re-exports) and rebuilds every object from it —
including Block 183's reflection, cell map, dual block and field reflection,
which are **rebuilt and not imported from any scratchpad**. The note is read at
its **final path only**, with no draft fallback anywhere in the runner. The
checks are grouped into **eight families, `A` through `H`**:

- **`A` — AUTHORITY.** The five-pin authority block, Block 183's note and runner
  content-bound at the parent commit and in the worktree, the nine audit inputs
  readable — including the **primary body** the charter is read from, Block
  106's note — and the stale pin verified to be a real ancestor of `HEAD` that
  carries **neither** Block 183 artifact.
- **`B` — THE IMPOSED-OBJECT BANNER.** Six imposed objects, zero registered and
  zero adopted, with the OS/reflection-positivity theorem, the two-history Gram,
  any gravity result, the ADM identification and any frame uniqueness all
  declared **NOT CLAIMED** as measured constants.
- **`C` — THE CONTROLS AND THE BAND STRUCTURE.** The four citation pins read
  from two primary bodies — Block 106 §12 steps 1 and 2, Block 183's minimal
  member and its "no temporal-link extraction" sentence — the landed-field
  Hodge control, `R`'s orthogonality, the frame's exact closure and its 32
  positive leading minors, the five-band census at 256 entries for this frame,
  the dual frame and the re-measured Block 181 equal-weight point 96 entries
  away, and the three non-identities at 40 / 32 / 40.
- **`D` — THE INVERTIBLE TRANSPORTER.** Eight per-bond blocks, all rank 4, all
  with empty kernels, nonzero counts `(10, 8, 10, 8, 10, 8, 10, 8)`.
- **`E` — THE PARITY THEOREM.** Exact at zero residual, with the wrong-dual
  contrast at 16 and three further controls at 144, 96 and 72.
- **`F` — THE SYMBOLIC ADM SPLIT.** The odd bond's whole 8-entry table compared
  entrywise, its vanishing at zero shear, the even bond's 8/4 split with the
  mass confined to the odd part, the even part's four diagonal positions and
  `(-,+,-,+)` signs against the exact magnitude `E`, both nonzero shear
  derivatives, and the Pythagorean reduction.
- **`G` — THE POLE LOCUS, THE QUOTIENT AND THE SEAM SIGN.** Four distinct
  even-quartic determinants with every coefficient strictly positive and every
  `m = 0` value positive, the quotient census, the four full-rank quotient
  bonds, and the seam negation at eight positions with both halves asserted.
- **`H` — THE NOTE.** This note at its final path, with the N5 fence as a raw
  byte-identical substring.

**Every check is exact SymPy Rational, Integer and Symbol arithmetic; no float
and no tolerance enters any measured object**, and positive definiteness is
decided by exact leading principal minors rather than by any eigenvalue estimate.
The runner carries a **sixteen-mutation battery** — `--list-mutations`,
`--mutation <name>` — in which each mutation rewrites exactly **one claim** and
must flip **exactly one family** to `FAIL`; every measurement is taken once,
before any mutation flag is consulted, so no family can cascade into another.
Two of the sixteen guard what the adversarial check supplied: `break_even_part`
restores the refuted "no q dependence" clause and `break_twist_negation` denies
the seam negation, and both must fail. The runner **fails closed**: it prints one
`PASS`/`FAIL` line per check, a per-family summary, and exits nonzero on any
failure.

Provenance for every claim above:
`.claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its
**THE TEMPORAL-LINK EXTRACTION COMPLETE** anchor, as corrected by the b184
adversarial check.
