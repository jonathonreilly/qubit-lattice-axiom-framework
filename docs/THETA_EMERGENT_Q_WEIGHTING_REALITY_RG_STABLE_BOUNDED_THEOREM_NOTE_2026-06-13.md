# The Emergent-Q Bridge's Weighting Half Closes: Reality of the Staggered Euclidean Measure Is an RG Invariant — No CP-Odd θ_gauge Weighting Can Emerge at Any Scale (θ Pinned to {0, π}) (Bounded Theorem)

**Date:** 2026-06-13
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome, does not retire or re-grade any Tier-A
admission, and does not edit any audit data file.
**Primary runner:**
[`scripts/frontier_theta_emergent_q_cp_rg_stability_2026_06_13.py`](../scripts/frontier_theta_emergent_q_cp_rg_stability_2026_06_13.py)
**Runner cache:**
[`logs/runner-cache/frontier_theta_emergent_q_cp_rg_stability_2026_06_13.txt`](../logs/runner-cache/frontier_theta_emergent_q_cp_rg_stability_2026_06_13.txt)
(SCORECARD: PASS=12, FAIL=0; deterministic, seeded)

> **Not claimed:** retirement of the θ admission, θ_gauge = 0 (the result
> gives the CP-even *set* {0, π}, not 0), exclusion of spontaneous CP
> violation, a proof that a sector functional Q exists in the scaling
> limit, or any audit status. **Claimed (bounded):** the *weighting* half
> of the emergent-Q bridge (block06) closes. The staggered substrate
> Euclidean measure is **real** and conjugation-invariant on the K-real
> site-diagonal section, and exact RG blocking under a conjugation-
> equivariant block map preserves reality (genuinely computed) — so
> reality is an **RG invariant**. A real Euclidean measure cannot carry
> the imaginary `iθQ` term, so no emergent CP-odd `θ_gauge` weighting can
> be generated at any scale (`Z_Q = Z_{−Q}`); reality pins the effective
> angle to the CP-even set **{0, π}**, refining the retained 06-07 no-go.

## A note on naming (reconciled with the framework's CPT convention)

The load-bearing symmetry is **reality of the Euclidean Boltzmann
measure**, equivalently its invariance under link complex conjugation
`U → U*`. In the framework's own CPT convention
([`AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`](AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md):
M→Mᵀ is C, M→M with x→−x is P, M→M* is the antiunitary T), `U → U*` is
**T / charge-conjugation of the real action — not genuine CP** (which is
M→Mᵀ). An earlier draft of this note called it "CP-symmetry"; that was a
mislabel. We therefore speak throughout of **reality / conjugation-
invariance**, and state the physics directly: a real measure has no
imaginary `iθQ` term, which is the only CP-odd source, so the CP-odd θ
weighting is absent — and reality is what is RG-stable.

## Role — closing the half block06 left open

Block06
([`THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md))
relocated the gauge-side admission to the emergent-Q bridge: *"whether the
scaling limit forces an emergent integer sector functional with nonvacuous
weighting."* That has two halves — does a `Q` functional **exist** (a
magnitude question), and if so is its weighting **CP-odd** (the part that
would make θ a physical, fine-tunable parameter). This note closes the
second half.

## The chain (runner, 12/12)

**Step A — the substrate measure is real and conjugation-invariant.**
`W[U] = det(D(U)+A)·exp(−S_gauge[U])`. The matter determinant is real on
the K-real **site-diagonal** section for every gauge background (slogdet,
finite-guarded, U(1) and SU(2); via ε-chirality `ε(D+A)ε = (D+A)†`,
check 1); the per-plaquette action `S = −β Σ_P Re Tr U_P` is real and
conjugation-even (`Re Tr(U*) = Re Tr(U)`, check 2). The conjugation-
invariance of the determinant is the **corrected two-step** argument
(check 3): (a) since `D(U*) = conj(D(U))` entrywise (real staggered η)
and `A* = A`, we have `D(U*)+A = (D(U)+A)*`, so
`det(D(U*)+A) = conj det(D(U)+A)`; (b) reality (step a's RHS equals the
det, which is real by ε-chirality) gives `det(D(U*)+A) = det(D(U)+A)`.
*(There is no single similarity `K` with `K M K = D(U*)+A`; an earlier
one-line `det(KMK)=conj det M` gloss conflated two distinct arguments and
is corrected here and in the runner's check-3 description.)* Hence
`W[U*] = W[U]` (check 4).

**Step A′ — site-diagonality is load-bearing.** A K-real (`A* = A`) but
**non-site-diagonal** real coupling gives a complex, conjugation-non-
invariant determinant (violation class computed: |Im sign| ≈ 0.41; check
5). Site-diagonality of the matter coupling is therefore an independent
consumed premise, not a convenience.

**Step B — any emergent Q is conjugation-odd.** A topological sector
functional flips sign under `U → U*`: in the 2D U(1) testbed,
`Q[U*] = −Q[U]` exactly (check 6). (This is conjugation/C-oddness, not
genuine-CP-oddness — see the naming note.)

**Step C — `Z_Q = Z_{−Q}`.** Real conjugation-invariant measure + Q
conjugation-odd forces the sector weights to pair: on an explicit
ensemble (13 sectors, −6…+6), `Z_Q = Z_{−Q}` and `Σ_Q Q·Z_Q = 0`
(check 7).

**Step D — no CP-odd weighting; θ pinned to {0, π}.** `Z(θ) = Σ_Q e^{iθQ}
Z_Q` is real and even, `dZ/dθ|_0 = 0` (check 8): no CP-odd weighting.
Evenness means `Z(θ)` is invariant under `θ → −θ`, which pins the
effective angle to the CP-even **set {0, π}** — not to θ = 0. `θ = π` is
itself real/even (`e^{iπQ} = (−1)^Q`) and is **not excluded** here. This
refines the retained 06-07 no-go
([`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md):
reality does not force θ = 0): reality forces θ into {0, π} and does so
RG-stably; the 0-vs-π choice is part of the existence/dynamics half.

**Step E — reality is RG-stable (the new content, genuinely computed).**
The old version's checks here were tautologies; this version computes the
actual object. On an explicit finite Z₃ model with a real conjugation-
symmetric weight and the real-local block-spin map (verified conjugation-
**equivariant**, `block(σc) = σ′(block c)`), **exact marginalization** over
3⁶ fine configurations gives a blocked weight `W′[b]` that is real and
conjugation-symmetric (`W′[σ′b] = W′[b]`), with coarse sectors still
paired (check 9). The lemma is discriminating, not tautological (check
10): dropping reality (an imaginary `iθQ` CP-odd term) makes the blocked
weight complex, and dropping the fine conjugation-symmetry (a real but
conjugation-odd term) makes the marginal real but conjugation-asymmetric —
each preserved property is contingent on the corresponding fine-weight
hypothesis. Hence under a conjugation-equivariant block map, reality is
preserved by exact blocking; iterating, no CP-odd θ weighting is generated
at any scale in this blocking class (check 11).

## What this changes — θ is sandwiched (within {0, π})

Combining block06 and this note:

- **block06:** no θ carrier exists on the substrate (`π₀(G) = 0`; no
  per-plaquette topological density);
- **this note:** even if a sector functional `Q` emerges in the scaling
  limit, the real RG-invariant measure forces its weighting CP-even
  (`Z_Q = Z_{−Q}`), so it cannot carry a CP-odd θ; the effective angle is
  confined to the CP-even set {0, π}.

A generic CP-odd `θ_gauge` would require the scaling limit to generate
both a sector functional and a CP-odd weighting — the second is excluded
from a real RG-invariant substrate. The gauge-side strong-CP residual
reduces to: the **existence** of an emergent (necessarily CP-even) `Q`,
the **0-vs-π** choice within the CP-even set, and **spontaneous** CP
violation. The explicit/fine-tuning strong-CP problem — a continuous bare
θ to tune — does not arise on the gauge-weighting side of this surface.

## What this note does NOT claim

- **Not** θ_gauge = 0: reality gives the CP-even set {0, π}; θ = π (a
  CP-even nonzero angle) is not excluded here, and `Z(θ)` is even, not
  constant (the |θ|-dependent vacuum energy of 06-07 persists).
- **Not** an exclusion of spontaneous CP violation (about the
  action/measure, not the realized vacuum).
- **Not** a proof that a `Q` functional exists (existence half open from
  block06); this note forces its weighting CP-even regardless.
- **Not** unconditional: consumes (i) K-reality (`A* = A`, equivalently
  `arg det M_matter = 0` — the matter-sector reality the θ̄ mass side also
  consumes); (ii) **site-diagonality** of the matter coupling (Step A′);
  (iii) a real per-plaquette gauge action, supplied by the real-positive
  Wilson selector
  ([`WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md`](WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md)),
  itself an admitted path-integral convention (unaudited), not a
  framework-derived fact; (iv) conjugation-equivariance of the block map
  (the real-local class).
- The fermion-measure (Fujikawa/anomaly) **Jacobian under coarse-
  graining** — the canonical radiative-θ route — is covered only insofar
  as the matter weight stays real under blocking (a marginal of reals);
  that rests on the determinant reality of Step A being preserved under
  RG, a premised not separately RG-verified fact for the dressed fermion
  sector.
- Substrate checks run on a 3D lattice; the `iθF·F̃` term is 4D. The
  reality/conjugation mechanism is dimension-independent (it uses neither
  d=3 nor the determinant's dimension), so 4D staggered-flavor determinant
  reality is argued by that dimension-independence, not computed in 4D.
- **Not** a retirement or re-grade of the θ admission; the registry is
  untouched. **No** PDG value or fitted selector anywhere.

## Honesty gate (negative-flavored sub-claim discipline)

The negative sub-claim — "no CP-odd θ_gauge weighting at any scale" — is
scoped exactly: the measure is real *given* K-reality + site-diagonal `A`
+ a real per-plaquette action (consumed premises); RG-stability holds for
conjugation-equivariant blocking kernels (the real-local class) and is
genuinely computed (not asserted) on the finite model with both
discriminators; the claim is about *explicit/radiative* θ, with
spontaneous CPV and the 0-vs-π choice explicitly out of scope. The 2D and
Z₃ models are concrete instantiations of dimension-independent mechanisms
(Q conjugation-odd; marginalization of a real equivariant weight is
real-equivariant), not the 4D claim itself; the 4D content rests on Steps
A and E.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  (block06; the emergent-Q bridge whose weighting half this closes)
- [`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md)
  (the retained no-go this refines: reality → {0, π}, RG-stably)
- [`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md)
  (the θ̄ split)
- [`WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md`](WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md)
  (the real-positive per-plaquette action premise — admitted convention)
- [`AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`](AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md)
  (the C/P/T convention used for the naming reconciliation)
- Context, not load-bearing (plain text, in-flight): the 06-11 mass-side
  bridge note (matter-determinant reality re-verified here in check 1) and
  the Tier-A minimum-statement refinement carrying θ(a)/θ(b).

## Reprove-and-cite ledger

- **Reproven here (runner):** matter-determinant reality (slogdet,
  finite-guarded, via ε-chirality); gauge-action reality and conjugation-
  evenness; the corrected two-step conjugation-invariance of the
  determinant; the site-diagonality violation class; conjugation-oddness
  of the 2D charge; `Z_Q = Z_{−Q}` and `Σ Q Z_Q = 0`; reality, evenness,
  and {0, π}-pinning of `Z(θ)`; the genuine finite-model marginalization
  with both discriminators (reality-drop and symmetry-drop); the block06
  and 06-07 interface pins.
- **Cited at declared grade:** the K-reality, site-diagonal, and real-
  Wilson-action premises; block06's relocation; 06-07's no-go.

## Verification

```bash
python3 scripts/frontier_theta_emergent_q_cp_rg_stability_2026_06_13.py
```

Expected: 12 `[PASS]` lines, six `RESIDUAL (declared-open)` lines, then
`TOTAL: PASS=12 FAIL=0` and the verdict paragraph. Exit code 0 iff
FAIL=0. Deterministic (seeded).

**Independent audit required.** This note asserts no effective-status
change.
