# Block 01 section — R-N4-AUT (clause N4, steelman)

**Route id:** R-N4-AUT
**Clause:** N4 (axis-selection / axis-label of B-AXIS.2)
**Posture:** genuine fresh derivation attempt (steelman), not a no-go rehearsal.
**Runner:** `scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py`
**Cache:** `logs/runner-cache/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.txt`
**Runner result:** `TOTAL: PASS=17 FAIL=0`
**Outcome:** WALLED — steelman fails; no A_min enrichment is one-axis-selecting
(each joint stabilizer is full S₄ or trivial), so the S₄ automorphism orbit is
exhaustive over A_min-available surface enrichments. (No crack.)

---

## 1. The exact thing attempted

The headline N4 obstruction (s4-transportable branch,
`SINGLE_CLOCK_AXIS_DATUM_S4_TRANSPORTABLE_NATIVE_REDUCTION_NARROW_NO_GO_NOTE_2026-06-17.md`):
the bare staggered-Dirac surface on an **even cubic-symmetric** `Z^3+1` block is
exactly invariant under the signed axis-exchange
`W_{a,b} = P_{a<->b} · diag((-1)^{x_a x_b})`, and the adjacent transpositions
`(0,1),(1,2),(2,3)` generate **S₄ acting transitively on the four Euclidean
axes**. Transitive ⇒ no axis-selector is non-transportable ⇒ the time axis
cannot be derived, only declared (B-AXIS).

**Steelman attempted here:** a transitive orbit is only fatal if the surface is
"too poor". So **search for ANY additional retained structure on the staggered
block** — a coupling, a grading, a crossing-link invariant, a boundary
decoration, a richer lattice graph — whose **automorphism stabilizer is strictly
smaller than S₄ and fixes exactly one axis**, **without presupposing the
Hamiltonian/generator H**. Such an enrichment, if A_min-derivable, would CRACK
the wall by selecting the evolution axis from structure alone.

## 2. The A_min-only method

A_min = Lattice + Quantum + Record only (`docs/MINIMAL_AXIOMS_2026-06-05.md`).
The Lattice axiom supplies `Z^3` sites + nn cubic adjacency and *no* dynamics,
boundary condition, metric, or orientation. Quantum supplies one qubit
(`Cl(3,0)`) per site and *no* generator. Record supplies a durable, finitely
additive *scalar* readout and *no* time metric, decomposition, or axis weighting.

Method (all finite-dimensional **exact** linear algebra; no RNG):

1. **[G] Compute the full automorphism group of the bare surface, not just W.**
   Enumerate the entire candidate group = signed hyperoctahedral group `B₄`
   (24 axis-permutations × 16 per-axis reflections = 384 site relabelings).
   For each, solve numerically for the diagonal `Z₂` sign field (BFS over the
   hop graph) that makes the dressed relabeling `U_g` conjugate the bare
   staggered hop `M` to itself, and admit `g` into `G_bare` iff
   `‖U_g M U_g^T − M‖ < 1e-9`. Result: **|G_bare| = 384**, with axis-permutation
   image **all of S₄** (transitive; orbit of axis 0 = all four). This is a
   stronger recomputation of the wall than the single-W certificate: the *entire*
   automorphism group, not one exchange, projects onto S₄.

2. **Enumerate A_min-available enrichments** E1–E8 and, for each, compute its
   stabilizer inside `G_bare` (or, for graph enrichments, the plain-permutation
   symmetry group in its own right plus the joint stabilizer), and report the
   **axis-permutation image** as a subgroup of S₄.

3. **Crack criterion (corrected and load-bearing):** an enrichment SELECTS an
   axis iff its stabilizer **fixes exactly one axis as a common fixed point AND
   acts transitively on the other three** (the S₃-fixing-one signature). A
   *trivial* stabilizer (identity-only) fixes **all four** axes and therefore
   selects **none** — this is the subtle false-positive the corrected criterion
   `selects_exactly_one_axis()` rejects; the full S₄ fixes none. CRACK iff some
   enrichment selects exactly one axis **and** is A_min-derivable without H.

## 3. Worked steps — the enrichment table

| id | enrichment | A_min source | \|axis-img of joint Stab\| | class | selects axis? | A_min? |
|----|-----------|--------------|---------------------|-------|---------------|--------|
| E1 | reality/CPT parity grading ε=(−1)^Σx | Quantum (internal C² reality) | 24 (S₄) | S₄-isotropic | None | yes |
| E2 | cubic adjacency Laplacian | Lattice (nn cubic graph) | alone 24; **joint 1** | **trivial-joint (symmetric W-break)** | None | yes |
| E3 | staggered η hop-sector family {D₀…D₃} | the staggered structure itself | 24 (S₄) | S₄-isotropic | None | yes |
| E4 | STW crossing-link RP invariant P_a | crossing-link surface | 24 (S₄, P_a=+1 all axes) | S₄-isotropic | None | yes |
| E5 | η-curvature 2-cocycle on plaquettes | staggered phase curvature | 24 (S₄, cocycle=−1 all planes) | S₄-isotropic | None | yes |
| E6 | Record additive scalar readout | Record (additivity, I(∅)=0) | 24 (S₄, scalar identity) | S₄-isotropic | None | yes |
| E7 | per-axis Z₂ BC datum (A,P,P,P) | **boundary datum (NOT A_min)** | 6 (S₃) | **one-axis-selecting (S₃)** | **axis 0** | **NO** |
| E8 | face-diagonal-enriched cubic graph | richer isotropic Lattice graph | alone 24; **joint 1** | **trivial-joint (symmetric W-break)** | None | yes |

**Precise structural claim (corrected):** every A_min enrichment's joint
stabilizer with the staggered hop is **either all of S₄ (isotropic) or trivial
(a symmetric, non-axis-selecting W-break)**; **NO A_min enrichment has a
one-axis-selecting (S₃) stabilizer**. The only one-axis-selecting enrichment is
the per-axis Z₂ BC datum (E7), which is S₄-transportable and outside A_min. For
E2/E8 the joint stabilizer is **trivial (identity-only), NOT S₄-isotropic** — W
**is broken** by these A_min enrichments, but the break singles out no axis.

Key per-enrichment facts (all exact-zero / exact residuals in the cache):

- **E1** ε=(−1)^Σx is sum-symmetric and W-inert; its stabilizer image is full
  S₄ → no axis. (Reproduces the s3/s4 branches' grading W-inertness inside the
  full-group computation.)
- **E2** The cubic Laplacian **alone** is preserved by all 24 *plain*
  permutations (S₄-isotropic in its own right — the Lattice graph carries no
  direction). Its *joint* stabilizer **with the staggered hop is TRIVIAL**
  (identity-only, axis-image = 1, fixes all four axes): the plain swap preserves
  the Laplacian but **breaks the staggered hop** (resid ≈ 22.63); the dressed W
  preserves the hop but **breaks the Laplacian** (resid ≈ 45.25); **no
  non-identity B₄ element preserves both**. So **W IS broken** by this A_min
  enrichment — but the break is **axis-SYMMETRIC** (a trivial joint stabilizer
  fixes all four axes / acts freely, singling out none). This is **NOT
  S₄-isotropic**; it is a trivial-joint, symmetric, non-selecting W-break.
  Corrected criterion → selects None.
- **E3** The four staggered hop sectors `D_μ` form a single S₄ orbit (they
  permute among themselves up to sign under `G_bare`); no sector is singled out.
- **E4** STW crossing-link RP invariant `P_a(x)=η_a(x)η_a(θ_a x)=+1` on **every**
  axis (value-sets `[[1],[1],[1],[1]]`) → S_d-isotropic, no axis label.
- **E5** η-curvature 2-cocycle = **−1 in all six planes including the three
  temporal (0,i)** (`temporal=[-1,-1,-1]`, `spatial=[-1,-1,-1]`) → no
  time-singling.
- **E6** The only A_min-canonical additive readout is the uniform scalar
  identity weighting (Record gives a scalar, not an axis-weighted readout);
  S₄-fixed.
- **E7** The per-axis Z₂ BC datum (A,P,P,P) **does** have a sub-S₄ stabilizer
  that selects exactly axis 0 and acts as S₃ on the spatial axes — a genuine
  selector. **But** it FAILS the A_min test on two counts: (i) it is a
  **supplied boundary input**, and A_min's Lattice axiom explicitly withholds
  any boundary condition (an EXPLICIT OPEN GATE); (ii) it is **S₄-transportable**
  — a `G_bare` element maps (A,P,P,P) exactly onto (P,A,P,P)
  (`‖W₀₁ M_appp W₀₁^T − M_pappp‖ = 0`), so the datum selects an axis only
  relative to an already-privileged axis. This is exactly the standing pin from
  the s4-transportable branch, recovered as the unique sub-S₄ enrichment.
- **E8** Adding face-diagonal cubic links keeps the graph S₄-isotropic in its own
  right (all 24 plain perms preserve it); but its *joint* stabilizer **with the
  staggered hop is again TRIVIAL** (identity-only) — **W IS broken** by this A_min
  enrichment, axis-symmetrically (not S₄-isotropic; a trivial-joint, non-selecting
  break). Any *isotropic* graph enrichment respects cubic symmetry by
  construction, so no richer A_min graph yields a one-axis-selecting (S₃)
  stabilizer.

## 4. EVEN-extent scope boundary (tested, recorded)

The S₄-transitivity exact-zeros hold on **even** cubic-symmetric blocks only.
`[SCOPE]` leg: on the **odd** block L=(3,3,3,3) the signed exchange does NOT
preserve the hop, `‖W M W^T − M‖ = 6.000` (matches the s4-branch odd-L
falsifier resid 6 exactly); on even L=(4,4,4,4) the residual is 0. The
even-extent condition is the standard staggered-fermion requirement (the
periodic η-phase closes consistently across the boundary wrap iff the extent is
even). The whole steelman is therefore scoped to **even cubic-symmetric**
blocks; on odd blocks W is not even a symmetry, so the "richer surface breaks W"
question does not arise the same way (and odd extent is a declared regulator
choice, not an A_min datum).

## 5. Honest outcome

**WALLED. The steelman fails; no crack.** **Every A_min enrichment's joint
stabilizer with the staggered hop is either all of S₄ (isotropic) or trivial (a
symmetric, non-axis-selecting W-break); NO A_min enrichment has a one-axis-
selecting (S₃) stabilizer. The only one-axis-selecting enrichment is the per-axis
Z₂ BC datum (E7), which is S₄-transportable and outside A_min.** Concretely:
E1, E3–E6 are S₄-isotropic; E2 and E8 have a **trivial joint stabilizer** —
**W is genuinely broken** by them (plain swap keeps the Laplacian/diagonal graph
but breaks the hop; dressed W keeps the hop but breaks the graph; no non-identity
B₄ element keeps both), but the break is **axis-symmetric** and selects no axis.
The **only** enrichment with a genuine one-axis-selecting (S₃ fixing axis 0)
stabilizer (E7) is a **supplied boundary datum outside A_min and is itself
S₄-transportable**. Therefore no A_min enrichment is non-transportable, and the
conclusion is **not an artifact of a too-poor surface** — it survives against the
richest A_min-derivable enrichments enumerated. (Note: this is **stronger** than
"every A_min enrichment is S₄-isotropic" — some A_min enrichments DO break W;
they just break it symmetrically, with no axis singled out.)

This CONFIRMS (does not crack) the N4 wall and strengthens it: the prior
branches tested the single exchange W and a handful of invariants; this route
computes the **entire 384-element automorphism group** of the bare surface and
shows that **no A_min enrichment's joint stabilizer fixes exactly one axis** —
each is either full S₄ or trivial (a symmetric break). The wall is not "W happens
to be a symmetry" but "the full hyperoctahedral group acts transitively and no
A_min enrichment singles out an axis under it."

## 6. Named load-bearing wall + authority

**Load-bearing wall:** the Lattice axiom's withholding of any **boundary
condition** (and of dynamics/orientation), which is an EXPLICIT OPEN GATE. The
only enrichment with a **one-axis-selecting (S₃) stabilizer** (E7) is precisely a
per-axis Z₂ boundary-condition datum — exactly the structure A_min refuses to
supply. Everything A_min *does* supply has a joint stabilizer that is **either
full S₄ (isotropic) or trivial (a symmetric, non-axis-selecting W-break)**: the
cubic graph (E2) and the face-diagonal graph (E8) actually **break W** (trivial
joint stabilizer) but axis-symmetrically; the qubit reality grading, staggered η
sectors and their curvature, and the additive scalar record readout are
S₄-isotropic. **No** A_min enrichment singles out an axis.

**Retained authority the wall rests on:**
- `SINGLE_CLOCK_AXIS_DATUM_S4_TRANSPORTABLE_NATIVE_REDUCTION_NARROW_NO_GO_NOTE_2026-06-17.md`
  (retained_no_go) — S₄ acts transitively on all four axes; the per-axis Z₂ BC
  datum is itself S₄-transportable (block [T], self-resid 16 there; recovered
  here as E7 transport resid 0).
- `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`
  (retained_no_go) — the sharpened pin: the minimal axis-selecting input is one
  per-axis Z₂ BC-asymmetry datum (recovered here as E7).
- `docs/MINIMAL_AXIOMS_2026-06-05.md` — Lattice supplies no boundary condition,
  no dynamics, no metric/orientation; Record supplies no time metric and no
  axis-weighted readout (boundary condition and dynamics are EXPLICIT OPEN
  GATES).

## 7. What the consolidated no-go should carry from this route (for N1/N7)

- **N1 (≥5 routes):** R-N4-AUT adds the **automorphism-stabilizer enumeration**
  as a distinct route: not "does W transport X?" but "is there ANY A_min
  enrichment whose *full automorphism group* drops below S₄ and fixes one axis?"
  Answer computed over E1–E8: no. This closes the "richer surface" escape that
  every transport-only no-go left implicitly open.
- **N7 (steelman honesty):** the strongest pro-derivation move (enrich the
  surface) was genuinely built and falsified by computing the actual stabilizer,
  including the corrected selector criterion that rejects the
  trivial-stabilizer-fixes-all false positive (E2/E8). The one sub-S₄ enrichment
  (E7) is explicitly the supplied, transportable BC datum — i.e. the steelman
  collapses back onto the already-named boundary-condition OPEN GATE, not onto a
  new A_min selector.
- **Reusable artifact:** the 384-element `G_bare` computation (full
  hyperoctahedral automorphism group with solved sign fields) is the canonical
  "the orbit is S₄ and it is exhaustive" certificate; the enrichment table is
  the canonical "every A_min enrichment's joint stabilizer is full-S₄ or trivial
  (symmetric W-break); only a supplied BC datum is one-axis-selecting, and it is
  transportable" list.

**Residual relocation:** unchanged from the campaign consensus — the only axis
selector is a boundary-condition / record-production-direction datum, which lands
on the **emergent-dynamics / boundary-condition OPEN GATE** of the minimal
axioms. B-AXIS.2 (N4 axis-label) remains a declared premise; A_min does not
supply it.

## 8. Status discipline

This is branch-local stretch-note work. No audit/publication/effective-status
surfaces touched; no bare "retained"/"promoted" status asserted; the independent
audit lane remains sole status authority. The runner derives nothing into A_min
and adds no axiom or primitive.
