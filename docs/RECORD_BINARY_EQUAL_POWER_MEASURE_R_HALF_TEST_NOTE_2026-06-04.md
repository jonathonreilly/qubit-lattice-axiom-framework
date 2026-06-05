---
claim_id: record_binary_equal_power_measure_r_half_test_note_2026-06-04
claim_type_author_hint: bounded_theorem
---

# Record-Binary Model — Does Record-Additivity FORCE the Equal-Power Measure (r = 1/2)? Decisive Test on the Internal-Carrier / Measure Layer

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the canonical
> source-of-truth doc.

**Date:** 2026-06-04
**Claim type:** bounded_theorem. This note reaches a clean **forced-or-not** result with a
single named residual: the record-binary model does **not** force the equal-power measure;
the equal-power weight `(1,1)` is reachable **only** by the added premise "a record = a
real-Wedderburn block (central idempotent)", which the Record axiom does not supply. The
bound is the `(1,1)`-vs-`(1,2)` isotype-weight choice — exactly the standing
`retained_no_go` ([`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)),
left **unweakened**.
**Status authority:** independent audit lane only. This note sets no audit status, promotes
no row, weakens no retained no-go, and edits no axiom. `r = 1/2` remains the Tier-A admitted
input `AC_φλ`; it is compared **structurally** only (no PDG value consumed).
**Primary runner:**
[`scripts/record_binary_equal_power_measure_r_half_test.py`](../scripts/record_binary_equal_power_measure_r_half_test.py)
(SUMMARY: PASS=42 FAIL=0).
**Cached log:**
[`logs/runner-cache/record_binary_equal_power_measure_r_half_test.txt`](../logs/runner-cache/record_binary_equal_power_measure_r_half_test.txt)

---

## §0 Why this test, and what is decisively different about it

The charged-lepton Brannen modulus `r = |b|²/a² = 1/2` (equivalently Koide `Q = 2/3` via the
retained biconditional
[`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)) is the single
Tier-A admitted input `AC_φλ` on the value chain
([`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)). Its
residual is sharply located: the **equal-power-per-block** (det_C / block-count) measure
selects `r = 1/2`; the **Born/dimension** (det_R) measure selects `r = 1`
([`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)).

**Three prior adjacency-geometry attacks all failed for one structural reason.** A single
face-diagonal, all diagonals (L2), and all-to-all distance-weighting with a Planck cutoff
each produced a **law-DEPENDENT** amplitude ratio (the singlet/doublet power swings by ~0.5
across decay laws), whereas the equal-power measure is **law-INVARIANT** (it weights the two
isotypes equally regardless of any continuous law). Geometry is therefore the wrong **kind**
of object: it cannot structurally realize a law-invariant measure
([`ALL_TO_ALL_PLANCK_R_HALF_FORCED_VS_NATURAL_TEST_NOTE_2026-06-04`](ALL_TO_ALL_PLANCK_R_HALF_FORCED_VS_NATURAL_TEST_NOTE_2026-06-04.md),
sister branch; parameter-free anchor `r ≈ 0.41`, Born side).

**This test attacks the right layer.** Not adjacency — the per-site **internal-carrier /
measure** layer. The user's record-binary model supplies, per site, a **discrete** Z₂
record/not-record label and a **discrete** 3-way qulink classification (both/one/none). These
are **law-invariant by construction**, so they pass the discriminator that every distance-law
failed. The decisive question is whether the **Record axiom's additivity** then **forces** the
equal-power (block-count) measure — closing `AC_φλ` with no import.

## §1 The model (Part A) — stated honestly, not tuned

- **Geometry.** The three generations are the `hw = 1` BZ-corner orbit
  `{e₁, e₂, e₃}` of `(Z₂)³` on `Z³`
  ([`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)),
  pairwise face-diagonal (squared distance 2). Each `Z³` site has 6 nearest neighbors
  (3 dims × 2); the three generation corners are **not** mutual nearest-neighbors (runner
  A5/A5b), so they are related here by **record-classification**, not by NN adjacency.
- **Per-site carrier.** one qubit **plus** a binary record-status `s_i ∈ {0,1}`
  (record / no-record), a per-site Z₂.
- **Qulink.** each ordered pair `(i,j)` carries a connection classified by the joint
  record-status `(s_i, s_j)`: both-record `(1,1)`, one-record (mixed), or no-record `(0,0)`
  — a **discrete, distance-free** 3-way classification.
- **Brannen circulant.** the generation mass operator is `Y = a I + b C + b̄ C²` (`C` the
  forward 3-cycle), with `r = |b|²/a²` and the **exact** signed-Brannen Koide readout
  `Q = Σλ²/(Σλ)² = 1/3 + (2/3) r` (runner A3; `Q = 2/3 ⟺ r = 1/2`). Here `a` is the
  on-site/diagonal ("stay") amplitude and `b` the forward-shift ("hop") amplitude.

**The honest convention (runner A4).** On the **homogeneous** (all-record), C₃-symmetric
triangle — the physical "all three generations carry a record" reading — the 3-way qulink
classification **collapses**: all three diagonal self-links are one class (`→ a`), all six
off-diagonal pairs are one class (`→ b`). So the classification yields the **circulant `(a,b)`
split**, and the numbers `a, b` are **free until a weight rule is supplied**. The convention is
stated, not hand-picked to land at `1/2`.

## §2 Part B — THE DECISIVE TEST: does record-additivity realize the equal-power measure?

The two measures on the two isotypes of `R[Z₃] = R ⊕ C` (singlet, 1 real-dim; doublet,
2 real-dim), via the block-total Frobenius split `E₊ = ‖aI‖² = 3a²` (identity-orbit `{e}`),
`E_⊥ = ‖bC + b̄C²‖² = 6|b|²` (shift-orbit `{C, C²}`):

| measure | isotype weights | balance condition | `r` | `Q` |
|---|---|---|---|---|
| equal-power / **block-count** (det_C) | `(1,1)` | `E₊ = E_⊥` ⇒ `3a² = 6|b|²` | **1/2** | **2/3** |
| **dimension** / Born (det_R) | `(1,2)` | `E_⊥ = 2E₊` | 1 | 1 |

Both are verified end-to-end on the explicit `r = 1/2` and `r = 1` Brannen circulants (runner
B2/B2b/B3/B3b): at `r = 1/2` the block energies are **equal** and the spectrum gives `Q = 2/3`;
at `r = 1` the doublet energy is **twice** the singlet (the dimension/Born balance) and `Q = 1`.

**The law-invariance discriminator (reused from the all-to-all worker).** A measure is
law-invariant iff its doublet/singlet weight ratio is **independent of any continuous
parameter**. The record count is **discrete**, so it is **trivially law-invariant for EITHER
choice** (runner B4a/B4b: ratio spread `= 0` across a fictitious continuous law for both `(1,1)`
and `(1,2)`). The positive control confirms a distance-weighting **is** law-dependent (runner
B6: geometry doublet/singlet spread `= 0.882`).

**Part-B finding — NECESSARY-BUT-NOT-SUFFICIENT (runner B5/B8).** The record model **passes**
the law-invariance test that geometry **failed** — a genuine qualitative improvement: the
discrete record-count lands on a **clean rational with no continuous knob** (block-count `r = 1/2`
exactly), whereas the parameter-free all-to-all geometry anchor lands at `r ≈ 0.41` on the Born
side, missing both idealized values (runner B7). **But law-invariance no longer
DISCRIMINATES:** because **both** `(1,1)` and `(1,2)` are discrete and law-invariant, the test
that killed geometry cannot separate the two measures here. **Record-additivity does not realize
the equal-power measure in a discriminating way.** Passing law-invariance is necessary, not
sufficient.

## §3 Part C — FORCED or RESTATEMENT? (the ruthlessly-honest line)

**The load-bearing hypothesis was: "additive counting IS block-counting; block-counting IS the
equal-power measure (→ r = 1/2)." This hypothesis is FALSE as stated.**

The decisive point is the **Pattern-L** precedent
([`FLAVOR_DET_CHARACTER_SELECTION_AUDIT_READY_2026-06-04`](FLAVOR_DET_CHARACTER_SELECTION_AUDIT_READY_2026-06-04.md)):
**`Tr` is additive over direct sums**, so additivity **cannot exclude `tr`**. Specialized to the
generation isotypes (runner C5/C6): the **dimension count** `I(e_k) = rank(e_k) = Tr(e_k)` is
**also additive** over the orthogonal central idempotents, because `Tr(e₀) + Tr(e₁) = Tr(e₀ + e₁)`.
So additive record-counting is satisfied by **both** `(1,1)` and `(1,2)`. **Additivity fixes the
LINEAR law (the functional is linear over disjoint record collections); it does not fix the
WEIGHT per piece (1 vs rank).** The `(1,1)`-vs-`(1,2)` choice survives untouched.

Why the record structure does **not** supply the block-count specifically:

- **The record binary is per-SITE (runner C1/C2/C8).** Its native "disjoint record collection"
  is the **site** decomposition `{e₁, e₂, e₃}`, which carries the **regular** character `(3,0,0)`
  — **not** the isotype split. Reaching the block-count requires regrouping the 3 site-records
  into 2 isotype blocks via the **Fourier/Wedderburn** transform, which is C₃ representation
  theory applied **on top**: the record binary is **blind** to the `ω`-phase that distinguishes
  singlet from doublet. The isotype dimensions `(1,2)` come from `Tr E₀, Tr E₁`, not from any
  record/site datum.
- **Site-record additivity does not fix `r` (runner C3).** Equal site-records fix only the three
  **equal diagonal entries** `= a` — i.e. trace-equipartition, already the retained AC_φ content
  ([`STAGGERED_DIRAC_SUBSTEP4_AC_PHI_TRACE_EQUIPARTITION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17`](STAGGERED_DIRAC_SUBSTEP4_AC_PHI_TRACE_EQUIPARTITION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md))
  — and say **nothing** about the hop `b` relative to `a`. A continuum of `r` is consistent with
  equal diagonals.
- **The naive uniform-token reading gives Born, not 1/2 (runner C4).** Giving each qulink
  (including the diagonal) one record-token (uniform `a = b`) yields `r = 1` (`Q = 1`), the Born
  endpoint — the **opposite** of `r = 1/2`.
- **The 3-way classification is only non-trivial on a heterogeneous record pattern, which breaks
  C₃ (runner C9).** Any pattern that makes both/one/none genuinely distinct (e.g. `s = (1,0,0)`)
  induces a **non-uniform diagonal**, so the operator is **not circulant** and the Brannen
  `Q = 1/3 + (2/3)r` structure — which the Koide value requires — no longer applies. Conflict,
  not derivation.
- **The freedom is QUADRATIC; additivity is LINEAR (runner C7).** The isotype-weight measure is
  a quadratic form `B_{α,β}(A,A) = α Tr(AB) + β tr(A)tr(B)` on `Herm(3)`; record additivity is a
  linear law. A linear law cannot constrain a quadratic ratio, so the entire positive-definite
  cone `{α > 0, α + 3β > 0}` of
  [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  remains additive-compatible: the `retained_no_go` is **unweakened**.

**Verdict: RESTATEMENT.** Equal-power `(1,1)` **is** reachable in this model (runner B2) — but
only by the **added premise** "a record = a real-Wedderburn block / minimal central idempotent".
That premise is the choice; choosing it **relabels** `AC_φλ` rather than deriving it. The
competing premise "a record = a basis outcome / pointer mode" is equally a record reading and
gives the dimension count `(1,2) → r = 1`. Indeed the **decoherence/pointer** reading of "record"
— the physically loaded one — points toward Born (`r = 1`), not `1/2`. Representation theory
ranks neither block-count nor dimension-count canonical; the Record axiom adds additivity, which
both satisfy, so it adds no canonicity.

## §4 Part D — the other two gates (corroboration; both negative)

**Chirality (D1).** The record Z₂ does **not** supply the `Γ_χ = (2/3)J − I` grading:

- `Γ_χ = diag(+1,−1,−1)` in the **Fourier** basis (runner D1a), but in the **site** basis it is a
  **full circulant** with off-diagonal `2/3` (runner D1b). A per-site record Z₂ is **site-diagonal**,
  so it lives in the **wrong basis** and cannot equal `Γ_χ`.
- The **homogeneous** record grading is uniform `= ±I` (scalar): `{±I, H} = ±2H = 0` only at
  `H = 0` — **no chiral grading** (runner D1c).
- A **heterogeneous** site-diagonal grading `diag(+1,−1,+1)` (the diagonal worker's candidate)
  **breaks C₃** and forces a **traceless, one-massless** spectrum (runner D1d) — not a
  charged-lepton Koide spectrum, not `Q = 2/3`.
- This is **consistent** with the retained chirality no-go
  ([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
  `retained_bounded`): `comm(C) ∩ anticomm(Γ_χ) = {0}` (runner D1e). The record Z₂ does **not**
  supply the missing on-site chiral term in a form compatible with the Koide circulant.

**Color (D2).** The 3-way qulink classification does **not** carry the color character:

- The generation orbit gives the regular character `(3,0,0)`; the color-center (Z₃ center of
  `SU(3)`) gives `(3, 3ω, 3ω²)`. These **differ** (runner D2a) — worker-1's mismatch confirmed.
- The 3-way classes `{none, mixed, both}` are `Sym²(Z₂)` — **3 classes but no order-3 element**,
  i.e. **not a Z₃ group** (runner D2b). They carry Z₂ characters, not the Z₃ color-center
  character. The numerical "3 classes = 3 colors" is a count coincidence with the **wrong group**
  (same error class as "√2 = sector count" flagged by the diagonal workers).

## §5 Part E — no-import / posit discipline (decisive for the classification)

The Record axiom ([`MINIMAL_AXIOMS_2026-06-04`](MINIMAL_AXIOMS_2026-06-04.md), Record) supplies
**only** additive scalar record readout, `I(R₁ ⊔ R₂) = I(R₁) + I(R₂)`, `I(∅) = 0`. Its own scope
sentence states it does **not** supply `AC_φλ`, Born weights, P2/modulus, or any observable
bridge; `AC_φλ` is listed as an **open gate outside axiom content**. Therefore:

- **The per-site record/not-record BINARY is NOT axiom-native — it is a posit/extension**
  (runner E2). Additivity is over **abstract** disjoint record collections; a per-site Z₂
  presence label is an added structural model, not axiom content.
- **The 3-way qulink classification is NOT axiom-native — a posit/extension** (runner E3).
- **The identification "record = central idempotent / block" — the ONLY route to `(1,1)` — is an
  ADDED premise, not axiom-native** (runner E5), and is not more canonical than "record = mode /
  outcome" (which gives `(1,2)`).

So even **if** one adopted the block-identification, the result would be **posit-conditional**,
not a no-import derivation. Combined with Part C (the identification is also not **forced** — it
is one of several additive-compatible readings), the honest standing is **RESTATEMENT**, the
strongest of the negative outcomes still short of any closure.

## §6 Honest verdict — RESTATEMENT (record-additivity does not force equal-power)

Of the four possible outcomes, the result is **RESTATEMENT**:

- **NOT FORCED-AND-AXIOM-NATIVE**, **NOT FORCED-BUT-POSIT.** Record additivity does **not** force
  equal isotype weight: by Pattern-L, the dimension/Born count `(1,2)` is **equally additive**, so
  additivity does not exclude it (runner C5/C6, VERDICT.forced = False).
- **RESTATEMENT (the verdict).** Equal-power `(1,1) → r = 1/2` is reachable **only** by the added
  premise "record = real-Wedderburn block / central idempotent". That choice **relabels** `AC_φλ`
  rather than deriving it; the `(1,1)`-vs-`(1,2)` line is the admission.
- **NOT (purely) BORN/WRONG-MEASURE.** The model does reach `r = 1/2` under the block reading; it
  is not that record-counting forces `r = 1`. (Though the **physically loaded** pointer/decoherence
  reading of "record" leans Born `r = 1`.)

This **converges** with the all-to-all worker (TUNED-LAW), the diagonal workers
(NATURAL-not-FORCED), and the memory ("block-counting is just `AC_φλ` restated"), now sharpened on
the **measure layer** rather than the adjacency layer: the law-invariance discriminator that
defeats geometry is **passed** by the discrete record-count but is **necessary-not-sufficient** —
it does not pick block-count over dimension-count.

**The genuine positive residual this opens (not a closing claim).** The record model **does**
clear the obstruction that defeated all three geometry attacks: it supplies a **law-invariant,
knob-free** discrete weight that lands **exactly** on a clean rational. What it does **not** supply
is the **single bit** selecting **block-count over dimension-count** — i.e. "a record is counted by
**presence** (one token per irreducible block) rather than by **dimension** (one token per real
mode)". The next path this opens is therefore sharply posed and **independent of geometry**: a
principle that fixes the **record-counting granularity** (block vs mode) — a measurement /
record-individuation principle on the carrier, not an adjacency or a decay law. If a future source
result derives that one bit from the framework's record/measurement structure, the
`retained_no_go` would close on the block side; this note neither supplies nor forecloses it.

## §7 What this note does NOT do

- Does **not** find record-additivity to force the equal-power measure, and does **not** claim
  `r = 1/2`/`Q = 2/3` is derived. The verdict is RESTATEMENT; `r = 1/2` remains the Tier-A admitted
  input `AC_φλ`.
- Does **not** edit any axiom. `MINIMAL_AXIOMS_2026-06-04` (Lattice / Quantum / Record) is
  untouched; the record-binary carrier and the 3-way qulink are an exploratory model surface,
  **not** adopted as primitives.
- Does **not** set audit status, promote any row, or weaken any retained no-go. The isotype-split
  no-go (`retained_no_go`) and the chirality no-go (`retained_bounded`) remain correct on their
  scope; this note's RESTATEMENT verdict is **consistent** with both (the "free singlet:doublet
  ratio" is precisely the block-vs-dimension freedom found here).
- Does **not** import external comparators or PDG values. `√2`, `r = 1/2`, and `Q = 2/3` are
  lattice/algebra structural data; the runner uses **no** measured mass.
- Does **not** claim the record model is useless: it is the **first** of the four `r = 1/2` attacks
  to clear the law-invariance obstruction with a knob-free discrete weight. It simply does not rise
  to a forcing — the block-vs-dimension bit remains unsupplied.

## §8 Audit-lane handoff

- **Claim type:** bounded_theorem. Clean forced-or-not result; single named residual (the
  `(1,1)`-vs-`(1,2)` / "record = block" bit), no value discharged. Honest tier matches the sister
  `retained_bounded` block-weight frontier
  ([`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md);
  [`KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29`](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md)).
- **No status to set.** This note proposes no promotion. `r = 1/2` remains Tier-A `AC_φλ`.
- **Runner:** PASS=42, FAIL=0; every PASS keyed to a substantive computed assertion (no
  hard-coded `True`).
- **Dependency posture:** depends only on the framework baseline (Brannen circulant structure, the
  `hw = 1` orbit geometry, `R[Z₃] = R ⊕ C`) and the Record axiom for the additive-record target. It
  **load-bears on none** of the cited retained rows and **weakens none**. It does not load-bear on
  `closure_c_staggered_dirac_gate` or any open-gate output.

## §9 Cross-references

- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) — the Lattice / Quantum / Record
  axioms; the Record-axiom additivity tested here, and its own statement that `AC_φλ` is outside
  axiom content.
- [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  — `retained_no_go`: the singlet:doublet (equal-power vs Born) ratio is free; this note shows
  record-additivity does not force `β = 0`, leaving the no-go unweakened.
- [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
  — `r = 1/2 ⟺ Q = 2/3` and `κ = a²/|b|²`.
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  — `AC_φλ`; the equal-power-vs-dimension measure fork (structure/value split); the memory that
  block-counting "is just `AC_φλ` restated".
- [`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)
  — equal real-Wedderburn-block → `Q = 2/3`, complex-dimension/trace → `Q = 1`; "neither measure is
  forced" (the frontier this note re-attacks on the record layer).
- [`FLAVOR_DET_CHARACTER_SELECTION_AUDIT_READY_2026-06-04.md`](FLAVOR_DET_CHARACTER_SELECTION_AUDIT_READY_2026-06-04.md)
  — the **Pattern-L** precedent (`tr` is additive over direct sums, so additivity cannot exclude
  `tr`), the decisive Part-C lever here.
- [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  — the `hw = 1` generation orbit `{e₁,e₂,e₃}` and the `(Z₂)³` charge-conjugation involution.
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  — the chirality no-go `comm(C) ∩ anticomm(Γ_χ) = {0}` (the on-site / `Γ_χ` structure), with
  which Part D is consistent.
- [`STAGGERED_DIRAC_SUBSTEP4_AC_PHI_TRACE_EQUIPARTITION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP4_AC_PHI_TRACE_EQUIPARTITION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — trace-equipartition (equal diagonals `= a`), the only thing site-record additivity fixes.
- Sister branch `codex/all2all-planck-r-half-forced-test-2026-06-04`:
  `ALL_TO_ALL_PLANCK_R_HALF_FORCED_VS_NATURAL_TEST_NOTE_2026-06-04.md` — the law-invariance
  discriminator (Part B) this note reuses, and the parameter-free `r ≈ 0.41` Born-side anchor.
