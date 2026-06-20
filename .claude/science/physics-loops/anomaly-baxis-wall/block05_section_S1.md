# Block05 / RAY S1 — P-REC SUPPLY-SIDE single-taste selector under the real Majorana reduction

**Type:** frontier supply-side attack (negative_route_pruning / sharper wall)
**Date:** 2026-06-20
**Branch:** physics-loop/anomaly-abj-bridge-block05-20260620
**Keystone under attack:** `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` (ledger=unaudited; fanout 1105) — **CONTEXT-ONLY**.
**Parent:** `anomaly_forces_time_theorem` (ledger=unaudited) — **CONTEXT-ONLY**.
**Runner:** `scripts/frontier_abj_prec_supply_side_majorana_J_real_selector_2026_06_20.py` — **TOTAL: PASS=40 FAIL=0**
**Cache:** `logs/runner-cache/frontier_abj_prec_supply_side_majorana_J_real_selector_2026_06_20.txt`

```yaml
Type: frontier_discovery + negative_route_pruning
Claim type: no_go (sharper supply-side wall)
outcome: sharper_no_go
cracked: no
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
independent_audit_lane_sole_authority: true
no_new_axiom_or_primitive: true
keystone_decoupled: true
```

## 0. The question (supply side, NOT the block02 consumer side)

Block02 PR-A (PASS=35) reframed P-REC's single-taste selector as **unnecessary for the
consumer**: the keystone consumer edge B4→B5/EVEN→B6 needs only γ₅-EXISTENCE, the
taste-singlet `Γ₅^spin = α₀α₁α₂α₃` supplies it, and the result is invariant over the
full `M₄(C)` taste family. Block01 R4 (PASS=43) established the **supply-side** status:
the single-taste selector is **registered data** because the COMPLEX carrier `C¹⁶` has a
full `M₄(C)` taste commutant of exact symmetries, so **≥2 distinct rank-4 single-taste
projectors** are both invariant — picking one is a selection.

**This ray attacks the supply side directly, with a move neither block01 nor block02
made.** Block01/02's `M₄(C)` taste freedom lived on the COMPLEX carrier. **No theorem
proves it survives the real reduction `Cl(3,1) = M₄(R)`.** The decisive question:

> Once the carrier is reduced to the real Majorana form and the antilinear `J` (Record
> K/CPT conjugation) is imposed, is the single-taste selector **DERIVED** — i.e. is
> exactly ONE `J`-real rank-4 projector onto a Dirac factor **forced**?

A crack here would be a **supply-side unlock of the 1105 cone P-REC edge — bigger than
the consumer reframe**. The honest result is the opposite: **the wall STANDS and is
SHARPER.** No crack.

## 1. Construction (all recomputed in-tree; retained authorities not cited blind)

**Carrier ground (PART 0, absorbs R4 / spin-taste-bank, residuals 0.0–1.2e-15).** Blocked
staggered `αμ` on the 2⁴ hypercube (`(αμ)_{b⊕eμ,b} = (−1)^{Σ_{ν<μ} bν}`); Cl₄
(`{αμ,αν}=2δ I`); taste-singlet `Γ₅^spin` (`(Γ₅^spin)²=+I`, `{Γ₅^spin,αμ}=0`); the
`M₄(C)` taste commutant (`dim_C = 16`); and the block01 fact reproduced on `C`: **≥2
distinct invariant rank-4 single-taste projectors** (residual 0.0).

**The antilinear `J` from CPT-EXACT (PART 1, residuals 0.0).** Recomputing the retained
`CPT_EXACT_REAL_ANTI_HERMITIAN_D` relation in-tree: the free massless `D_red(p) = i Σμ αμ
sin(pμ a)/a` is anti-Hermitian, `C = ε` (sublattice parity `(−1)^{Σ bk}`) gives **`ε D ε
= −D`** (CPT-EXACT), `T = K` complex conjugation. **The αμ are REAL in the lattice basis**
(staggered phases ±1), so `K αμ K = αμ`: bare `K` is already a Majorana real structure on
the SPIN Clifford factor (`J₀ = K`, `J₀² = +I`). The carrier-level Record K/CPT
conjugation is `J = U_J K` with `U_J` a unitary in the taste commutant (Record supplies
the SLOT — a K/CPT conjugation — never the content `U_J`; the αμ being K-fixed forces any
admissible `J` to act on the spectator TASTE index only).

## 2. The decisive computation: NO rank-4 single-taste object survives `J`

**Impose `J`-reality on the `M₄(C)` taste commutant and count the `J`-real rank-4
projectors onto Dirac factors.** For `J₀ = K`, `J`-real = real-entry. (PART 2)

- **dim_R of the `J`-real (K-real) taste commutant = 16** (residual 0.0): imposing
  reality HALVES `M₄(C)` (`dim_R 32`) to a full real form (`dim_R 16`).
- **DECISIVE — number of `J`-real rank-4 taste projectors = ZERO** (residual 0.0;
  counts `[0,0,…]`). Not exactly 1 (no crack), and not ≥2 (the block01 picture). **None.**
- **Minimal real idempotent rank = 8, not 4** (residual 0.0). Every generic K-real
  symmetric taste element has eigenvalue multiplicities **`[8,8]` (Kramers doubling)** —
  verified across 12 random trials, pattern set `{(8,8)}` exactly. So the K-real taste
  form has **no real rank-4 idempotent**.

**Independent cross-check (separate method, in the section's supporting analysis, not the
PASS count):** minimizing `‖conj(P)−P‖` over 12000 candidate rank-4 commutant projectors
gives **0.277 > 0** — no real rank-4 taste projector exists, confirming the
eigenvalue-`[8,8]` result by a route that does not use it.

## 3. Which real form? — M2(H), the quaternionic one (PART 3)

The K-real taste commutant and the real spin Clifford algebra `⟨αμ⟩` are mutual
commutants in `M₁₆(R)`, both `dim_R = 16`. **Artin–Wedderburn over R is degenerate** here:
both `M₄(R)` (`4·4·1=16`) and `M₂(H)` (`2·2·4=16`) fit the dimension arithmetic
(`solutions = [('R',4,4),('H',2,2)]`). **The minimal-real-idempotent-rank breaks the tie:**
`M₄(R)` would have minimal idempotent rank 4 (rank-4 EXISTS); the carrier gives **rank 8 ⇒
the taste real form is `M₂(H)` (quaternionic)**, where rank-4 Dirac idempotents are
FORBIDDEN.

This is exactly the retained `CL3_TO_CL31` contrast made concrete **on the taste factor**
(recomputed in-tree, residuals 0.0): `Cl(3,1) = M₄(R)` (ε=−1, signature `(+,+,+,−)`) vs
`Cl(4,0) = M₂(H)` (ε=+1, `(+,+,+,+)`); **both complexify to `M₄(C)`**. The narrow theorem
proves only the abstract two-cell split and explicitly does NOT derive ε=−1 or reconstruct
the staggered carrier. The new finding is which real form the staggered carrier's TASTE
spectator actually carries under Record's K/CPT `J`: **the quaternionic one.**

## 4. Registered-data guard — the load-bearing honesty check (PART 4)

A single-taste selector would be DERIVED only if exactly ONE `J`-real rank-4 projector
existed **for every admissible `J`**. Sampling the admissible family `J = U_J K` (`U_J`
unitary in the taste commutant — the law-admissible family Record's slot permits):

- **No admissible `J` yields exactly one** `J`-real rank-4 projector (distinct counts over
  the family `= [0]`; canonical `K` gives 0). The derivation leg FAILS.
- Even if some `J` had produced a unique projector, it would be **`J`-choice dependent ⇒
  registered data**, not a derivation, per `realized_state_primitive`'s counterfactual
  clause (a quoted object must be invariant over the law-admissible family). The guard is
  recorded explicitly so a future cherry-picked `J` cannot be laundered as a derivation.

## 5. Why — structural reason (PART 5)

The αμ are K-fixed (real), so the SPIN Clifford reality is the trivial `K` and any
admissible `J` acts on the **spectator taste index only**. The real form it imposes on the
`M₄(C)` taste algebra is the QUATERNIONIC `M₂(H)` (minimal real idempotent rank 8) — so
there is **no rank-4 single-taste object to select**. The spin chirality `Γ₅^spin` is
untouched: it is **K-fixed (residual 0.0)** and taste-singlet, hence invariant under every
admissible `J`. The carrier still factorizes spin⊗taste (`4×4=16`), `J`-equivariantly.

**Net:** the real Majorana reduction does not leave the single-taste selector *ambiguous*
(block01/02 picture on `C`, ≥2 rank-4 projectors); it **DELETES the rank-4 single-taste
object entirely** (M2(H), 0 rank-4 projectors). The single-taste rank-4 selector is
**intrinsically complex** and absent from the real form.

## 6. Verdict — sharper wall, NO crack

**The wall STANDS and is SHARPER.** The block02 CONSUMER unlock is **untouched and, if
anything, reinforced**: it routes through the K-fixed / `J`-invariant taste-singlet
`Γ₅^spin`, which is the *only* chirality object that survives the real reduction.

- **NOT a crack.** Single-taste is **not** derived from Record K/CPT + the real reduction.
  A crack needed exactly ONE `J`-real rank-4 projector for every admissible `J`; the count
  is **0**, never 1.
- **Sharper than block01/02.** On the complex carrier the single-taste selector was
  *ambiguous* (≥2 rank-4 projectors = registered data). Under the real reduction it is
  *deleted*: the K-real taste form is `M₂(H)`, with **zero** rank-4 single-taste
  idempotents. The supply-side obstruction is therefore not "an unforced choice among
  several" but "**no rank-4 single-taste object exists in the real form at all**" — a
  cleaner, more decisive no-go locus.
- **Registered-data guard intact.** Any unique projector (none appeared) would be
  `J`-choice/state dependent ⇒ supplied datum, not a derivation.

**Honest framing (do not soften, do not oversell).** A genuine crack would have been a
bigger unlock than the consumer reframe — it is **not** found. This is **honest frontier
negative_route_pruning**: a sharper, runner-verified statement of *why* the supply-side
single-taste selector is not derivable, which **prunes** the highest-value remaining
P-REC supply route (real-reduction-forces-single-taste) and **redirects** any future
supply attempt away from rank-4 Dirac-factor selection (structurally impossible in the
real form) toward the quaternionic-structure question itself. It does **not** crack the
keystone and is **not** a closure.

## 7. Discipline (B-AXIS lessons + scope)

- **Four primitives loaded.** `minimal_axioms` (which-symmetry-gauged / single-taste data
  stays withheld); `realized_state_primitive` read as the counterfactual `J`-family
  invariance test (PART 4); `scale_reference` / `kinetic_isotropy` non-load-bearing here.
- **Functional-calculus-correct algebra.** The taste commutant is the spectator `{α}″`
  computed as the actual commutant (not `span{I,G}`); `Γ₅^spin ∈ {α}″` (polynomial in the
  generators); the real form is computed as the K-fixed subalgebra and classified by
  Artin–Wedderburn + minimal-idempotent-rank, not assumed.
- **Realized-state guard load-bearing.** The decisive negative leg is "no admissible `J`
  derives a unique rank-4 projector"; the registered-data clause forecloses laundering a
  `J`-dependent object as a derivation.
- **Absorb-not-rebuild.** `frontier_abj_prec_r4_taste_reconstruction` (PASS=43),
  `frontier_abj_prec_consumer_reframe` (PASS=35),
  `frontier_abj_prec_spin_taste_clifford_core_bank` (PASS=40) absorbed by path+PASS
  (re-confirmed this block) and their residual-0 facts recomputed in PART 0; not rebuilt.
- **Retained authorities recomputed in-tree** (CONTEXT-ONLY, not cited blind):
  `CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27` (M₄(R) vs M₂(H), both →
  M₄(C)); `CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10` (`εDε=−D`, D
  real anti-Hermitian); `LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4` (αμ surface).
- **Keystone-decoupled.** No load-bearing fact routes through the unaudited keystone or
  parent; both kept CONTEXT-ONLY. **No new axiom or primitive.** No empirical/PDG/fitted
  inputs. No edits to `docs/audit/`, ledger, queue, or publication; `docs/audit/data/`
  parsed READ-ONLY. No git operations (orchestrator owns git). Independent audit lane is
  the sole status authority.

## 8. N1–N8 no-go discipline gate

- **N1 (routes ≥5):** (i) bare `K` real reduction; (ii) admissible `J = U_J K` family;
  (iii) Artin–Wedderburn + minimal-idempotent-rank real-form ID; (iv) `CL3_TO_CL31`
  ε-sign branch on the taste factor; (v) independent `‖conj(P)−P‖` projector search; plus
  the absorbed block01 R4 / block02 PR-A routes. **≥5 met.**
- **N2 (steelman):** "the real Majorana reduction forces a unique single-taste γ₅
  selector" — steelmanned (it is the highest-value supply route) and **defeated**: the
  K-real taste form is M₂(H) with ZERO rank-4 single-taste objects.
- **N3 (decisive-failure-first):** the counts (0 vs ≥2 vs exactly 1) and the
  `J`-family-dependence guard were computed BEFORE any crack claim; the crack leg
  (exactly 1 for every `J`) was tested and failed.
- **N4–N6:** functional-calculus-correct commutant; registered-data counterfactual leg
  load-bearing; carrier-conditional (even 2⁴) caveat inherited (odd-`L` extent breaks the
  blocked-grading; not in scope).
- **N7 (steelman settled):** the supply-side selector stays walled; the new content is a
  sharper structural reason (quaternionic real form), runner-verified.
- **N8:** non-bare; sharper no-go; consumer unlock explicitly preserved; no closure
  asserted.

---
*Block05 RAY S1 of the anomaly_forces_time ABJ bridge attack — P-REC SUPPLY-SIDE
single-taste selector under the real Majorana reduction. Sharper wall, NO crack: the
real `Cl(3,1)=M₄(R)` reduction + Record's antilinear K/CPT `J` puts the taste spectator
into the quaternionic real form `M₂(H)`, which has ZERO rank-4 single-taste idempotents —
the single-taste selector is not merely an unforced choice (block01/02) but is intrinsically
complex and deleted by the reduction. The block02 consumer reframe (taste-singlet
`Γ₅^spin`, K-fixed/`J`-invariant) is untouched. No keystone crack; no new axiom/primitive.*
