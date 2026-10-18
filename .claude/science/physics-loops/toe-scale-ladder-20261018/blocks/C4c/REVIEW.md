# C4c — independent review

**Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), a subagent launched by the coordinating session.
It is a different invocation from the author but the same model family, so independence is
procedural only. **Date:** 2026-10-18. **Scope:** `NOTE.md`, `scripts/`, `logs/`, with C4b NOTE as
context. Every load-bearing step was re-derived by hand and re-checked with reviewer-written
code in `review_scripts/`. No author code was imported. No commits.

## Verdict summary

| claim | verdict | severity of issues |
|---|---|---|
| Lemma V (vertex lemma) and Cor. C | **correct** | none in the proof; one wording fix (XY gates) |
| Prop. S4 (4-segment diagonal) | **correct** (independently certified) | none |
| Lemma F | **correct** | the "why a layer must be commuting" remark is **incorrect** (medium) |
| Theorem N (scoped flat bands, all sectors frozen) | **correct with fix** | low/medium: scope wording; the 296/300 statistic depends on the sampling |
| Lemma K | correct | none |
| Observation M (6 face-diagonal channels under T, none under O) | **correct** | low: the glider/caterpillar T-covariance is unverified |
| "boundary-shell conflict" | presented as argued, not proved (honest) | low: one sentence needs a qualifier |

## (1) Lemma V and Corollary C — correct

Re-derivation (reviewer's own):
1. Fix s with S ∩ (S+t) = {s}. Write h = Σ A_i ⊗ P_i and h_t = Σ Q_j ⊗ B_j, with the A_i and B_j
   linearly independent. Then the A_i ⊗ B_j are independent, so [h, h_t] = 0 gives [P_i, Q_j] = 0
   for all i, j. So V = span{P_i} (h's local space at s) and V' = span{Q_j} (h's local space at
   s − t, translated) commute elementwise.
2. V is the image of h under the partial slices φ ⊗ id. U(1) invariance of h, together with
   φ ↦ φ∘Ad(e^{iθQ_rest}), shows V is invariant under on-site Ad(e^{iθσ^z}). So V is graded
   into span{1,σ^z} ⊕ Cσ⁺ ⊕ Cσ⁻. Checked numerically in rv1 (B).
3. Hermitian case: V is †-closed. If V has a charged part, it contains σ⁺ and σ⁻, so V' ⊂ C1. That
   contradicts h being nontrivial at s − t. Hence V ⊂ diag. Since V is not scalar, V' ⊂ comm(σ^z)
   = diag.
4. Unitary case: the "σ^z coefficient of h†h = ±G₊†G₊/2" step is right, so G₊ = 0. The
   alternative route, h = −i log g, is also valid: log g is a function of g, has the same support,
   and conserves U(1).
5. Vertex claim: take ℓ with unique maximiser v and unique minimiser w, and set t = v − w. Then
   x = y + t with x, y ∈ S forces ℓ(x) ≥ ℓ(v), so x = v and y = w. Hence S ∩ (S+t) = {v}, and both
   v and w are forced. Correct.
6. Cor. C: the intersection of the subspaces diag_s ⊗ M(rest) over the forced s is
   diag^{⊗forced} ⊗ M(s₀). Charge conservation then kills σ^± at s₀. Correct.

Numerical tests (rv1, own code):
- (C) 200 random U(1) unitaries on each of the bond e1, the face bond, the collinear triple, the
  L-triple and a skew triple all fail translate-commutation, while random diagonal gates commute.
- (D) Levenberg–Marquardt minimisation of Σ_t‖[h,h_t]‖² with the hop part normalised to 1. Results
  are in the log; see the evidence section.
- (D0) Positive control without U(1): the collinear triple reaches ≈ 0, as ZXZ-type families do.
  This shows the optimiser does find solutions when they exist.

Coverage classification (rv3, own forced-site code):
- every one of the 247 cube subsets with |S| ≥ 2 is fully forced;
- every bond up to range 3 is fully forced;
- the star has exactly its centre unforced;
- the 3×3 square has 5 unforced sites and the 27-cell has 19;
- among collinear 4-sets {0 < a < b < c ≤ 12}, only the equally spaced ones have 2 unforced
  sites. So Prop. S4 plus rescaling covers "collinear 4-site segments" exactly as claimed. Unequal
  spacings are covered by Cor. C.

**Wording fix (low).** The result-up-front list says covered two-site supports include "XY/exchange-type
gates". Covered means *forced diagonal*, so XY gates are excluded from 𝓕, not members of it.
Suggested text: "two-site gates at any separation (which are then forced to be |11⟩-phase
type; XY/exchange gates are excluded)".

**Statistic fix (low).** The "296/300 sampled supports covered" figure holds for |S| uniform in
[2,12], the author's `randint(2,12)`. rv3 reproduces it exactly: 283/13/4. For |S| uniform in
[2,27], only 142/300 are covered. The NOTE already says it is a sample, but it must state the
size distribution. Without that, the figure reads as "almost all supports are covered", which is
false for large supports.

## (2) Prop. S4 — correct, independently certified

The reviewer's construction (rv2) builds integer structure tensors from kron-embedded matrices.
- Exact row reduction gives 128 distinct coefficient rows and 101 independent homogeneous
  quadratic equations in the 24 unknowns.
- For each κ, sympy Gröbner with the f5b algorithm (not the author's default Buchberger) of
  ideal + ⟨a_κ b_κ − 1⟩ is [1].
- Control: diagonal assignments solve the system.

The homogeneity normalisation argument is valid over C: rescaling by λ multiplies a b by λ². The
24-unknown ansatz relies on Lemma V, which (1) verified. As a further check, rv1 (D) minimises
over the *full* 70-parameter U(1) Hermitian 4-site ansatz with no Lemma V reduction; see the
evidence section.

## (3) Lemma F and Theorem N — correct with fixes

**Lemma F.** Correct. The cancellation argument gives supp L^n(A) ⊂ supp A + S − S uniformly in n,
for any gates, any charge and any range. rv5 checks a commuting non-diagonal layer, V^⊗ (CZ-phase
chain) V^†⊗: |supp α^n(X)| = 3 for n = 1..8. "Flat bands" follows: a uniformly bounded light cone
gives zero group velocity.

**"Why a layer must be commuting" is incorrect (medium).** The argument "any Z^3-invariant
ordering function is constant" confuses an ordering *function* with an ordering *relation*. The
lexicographic order is translation-invariant as a relation, and ordered staircase products of
non-commuting translates can define TI QCAs. Standard example: the staircase of SWAPs along each
line is the shift, which is TI, well defined and U(1)-conserving. rv5 checks that SWAP translates
do not commute and that the staircase product maps σ^z_0 to a single other site. Generic staircases
are not locality preserving, but some are. The NOTE should therefore:
- delete or replace this paragraph and the sentence in Answer 1, "Exchange-type 2-site gates
  cannot be put in a TI layer";
- say instead that 𝓕 is *defined* to use commuting layers, and that sequential (staircase)
  circuits form an open class.

The "What is still open" list already includes "QCAs that are not circuits of commuting TI
layers", so the scope is honest. Only the justification is wrong. Theorem N is unaffected.

**Theorem N.** The quantifiers check out:
- Each gate commutes with its own translates, because the whole layer is a commuting family.
- Being covered is an O-invariant property, so the whole orbit is covered.
- Lemma V and Cor. C/S4 make every gate diagonal. Ad σ_n^⊗ is a diagonal conjugation.
- So α is a diagonal automorphism of the form Ad(σ_n^⊗)^ε ∘ (a single commuting diagonal layer).
- Full action: SU(2) invariance plus fixing σ_z^x gives α(σ_m^x) = σ_m^x for all m, hence α = id.
  This is elementary, so the citation is not even needed.

**"Every density frozen" is justified, in the strongest sense.**
- α(n_x) = n_x for every site x, so ⟨n_x⟩ is time-independent in *every* state: any k-magnon
  sector, finite density, any vacuum.
- Configuration states are invariant: on the diagonal algebra they are point measures, and such a
  state extends uniquely.
- Light cones are bounded by Lemma F applied to the composite diagonal layer.

The explicit instance was recomputed from the Ising-phase formula on a 5³ torus (rv4): the phases
3.0623 (axis, ×3), −2.1809 (face, ×6) and 2.7423 (body, ×4) match.

Scope caveats to state explicitly (low):
- 𝓕 requires *each gate* to be U(1)-conserving. Layers whose product conserves Q_n while their
  individual gates do not are outside 𝓕.
- 𝓕 requires each layer to be orbit-closed.

The NOTE says the second; it should also say the first.

## (4) Observation M — correct; the glider claims are flagged appropriately

rv4 uses its own group construction: |O| = 24 and T = the even-permutation subgroup, |T| = 12.
It enumerates space-group stabilisers.
- Under T at r = 1, the exceptions are exactly the 6 face-diagonal relative positions. Each has
  |Stab| = 2: the C2 about the face normal combined with a translation.
- The example {0, e1+e2} → {e3, (1,1,1)} is a Stab-fixed, ~-related image with a different COM.
  The COM moves only along the face normal, with ΔCOM = ±e3 per tick. Allowed images also include
  the crossed diagonal, e.g. {(0,1,1),(1,0,1)}.
- Under O there are 0 exceptions. The edge C2′ (x,y,z) → (y,x,−z), which lies in O∖T, fixes the
  pair and moves the image.
- At r = 2 there are 56 exceptions under T and 36 under O. Lemma K's counts are 89 related pairs,
  88 with a different COM.

All of these reproduce exactly.

Minor points:
- "v = 1 site/tick" is consistent with ΔCOM = ±e3 per tick.
- "The two-layer form is T-covariant, which I checked by hand" has no script and an ambiguous
  definition ("P(z) ↔ Q(z+1)"). **Unverified.**
- The boundary-shell conflict is labelled "argued, not proved impossible", both in the text and in
  the claim-type table. That is presented honestly.
- The follow-on sentence, "by Lemma V they must lie in the unforced interior of a larger gate
  support", holds only if a *single* commuting-layer gate performs the whole move. A multi-gate
  or multi-layer realisation is not constrained this way. Add that qualifier.

## Evidence (reviewer logs in `review_scripts/`)

- `rv1_vertex_numeric.log` — commutants, charge grading, random U(1) gates, optimisation (see TOTAL line)
- `rv2_seg4_groebner.log` — TOTAL: PASS=7 FAIL=0 (≈ 1 min)
- `rv3_forcing.log` — TOTAL: PASS=10 FAIL=0
- `rv4_pair_symmetry.log` — TOTAL: PASS=12 FAIL=0
- `rv5_layers.log` — TOTAL: PASS=3 FAIL=0
- `rv_SUMMARY.log` — combined
