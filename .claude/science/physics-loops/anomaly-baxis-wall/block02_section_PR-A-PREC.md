# Block-02 / ROUTE PR-A — P-REC consumer reframe

**Type:** consumer-reframe audit (does the consumer NEED the walled identification?)
**Date:** 2026-06-20
**Branch:** physics-loop/anomaly-abj-bridge-block02-20260620
**Keystone under audit:** `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` (ledger=unaudited; fanout 1105)
**Parent:** `anomaly_forces_time_theorem` (ledger=unaudited)
**Runner:** `scripts/frontier_abj_prec_consumer_reframe_2026_06_20.py` — **TOTAL: PASS=35 FAIL=0**
**Cache:** `logs/runner-cache/frontier_abj_prec_consumer_reframe_2026_06_20.txt`

```yaml
Type: consumer_reframe
Status: P-REC REFRAMES TO UNNECESSARY for the 1105 consumer (B4/B5/B6 chirality+even-dim edge); PARTIAL UNLOCK; NO single-taste admission
outcome: reframes_unnecessary
cracked: partial
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
no_new_axiom_or_primitive: true
```

## 0. The question (audit, not campaign pivot)

WALL P-REC was the highest-value identification wall: the staggered ε carrier →
spacetime γ₅ identification was said to need a **single-taste selector** (the free
algebra has full `M₄(C)` taste symmetry, so picking one taste/Dirac factor is
selector-dependent = registered data unless derived; root authority
`NO_PER_SITE_CHIRALITY_THEOREM`). Block01 (R4) confirmed the SELECTOR wall and
sharpened it but did NOT crack it.

ROUTE PR-A asks the orthogonal **consumer** question, not the supplier question:
does the keystone (B4/B5) and its parent (EVEN parity law + P-REC declaration)
actually CONSUME a single-taste / de-tasted **irreducible** γ₅, or do they consume
only the **EXISTENCE of a taste-singlet γ₅** (γ₅²=+I ∧ ∀μ {γ₅,γμ}=0)? If only the
existence predicate is consumed and the consumed quantity is taste-dial-invariant,
then single-taste selection is a within-sector dial — not load-bearing — and P-REC
becomes UNNECESSARY for the 1105 consumer (without admitting single-taste chirality
as derived).

## 1. (a) B4/B5 restated as an existence predicate + the reused witness

B4 (keystone, verbatim): "a chirality operator γ₅ satisfying γ₅²=+I, {γ₅,γμ}=0
must exist on the spacetime representation that carries the gauge-theory anomaly
evaluation." B5: such a γ₅ exists iff `n = d_s + d_t` is even (retained EVEN).

Restated as the **existence predicate** on the carrying representation:

> E(rep) := ∃ X ∈ End(rep) : X² = +I ∧ ∀μ {X, γμ} = 0.

The block01 spin/taste core is **reused verbatim (NOT rebuilt)** from
`scripts/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py`: the blocked free
staggered `αμ` (Cl₄ on the 2⁴ carrier), the taste-singlet
`Γ₅^spin = α₀α₁α₂α₃`, and the `M₄(C)` taste commutant. Runner PART 0 reproduces the
residual-0 facts: `{Γ₅^spin, αμ}=0` (**residual 0.0**), `Γ₅^spin²=+I`, and
`Γ₅^spin` commutes with all of `M₄(C)` (taste-singlet, residual 1.1e-15).

**`Γ₅^spin` is an explicit witness for E on the FULL 4-tasted (reducible) carrier.**
So the predicate B4 consumes is already TRUE without selecting any single taste
(PART (a), residual 0.0). The EVEN parity law holds on the reducible carrier
identically (n=4 even ⇒ ω anticommutes every generator, residual 0.0).

## 2. (b) CRITICAL HONEST CHECK — does the parity law need an irreducible γ₅?

The parent phrases EVEN as the "anticommutant-nullity PARITY LAW … in irreducible
representations (nullity 1 for n even, 0 for n odd, for n=2..7)" (parent lines
61/222/361) and declares P-REC "on the irreducible Dirac factor" (~line 92, 219,
257, 305). The decisive test: is the even/odd nullity DICHOTOMY — the only thing B5
consumes (γ₅ exists ⟺ nullity > 0) — the SAME on a REDUCIBLE multiplicity-m carrier
as on the irreducible one?

PART (b) computes `anticommutant-nullity(rep) = dim{X : ∀μ {X,γμ}=0}` for n=2..6 on
(i) the irreducible Cl_n rep and (ii) reducible carriers `γμ ⊗ I_m`, m∈{2,4}:

| n | irrep nullity | reducible m=2 | reducible m=4 | verdict (γ₅ exists?) |
|---|---|---|---|---|
| 2 (even) | 1 | 4 | 16 | YES on all |
| 3 (odd)  | 0 | 0 | 0  | NO on all |
| 4 (even) | 1 | 4 | 16 | YES on all |
| 5 (odd)  | 0 | 0 | 0  | NO on all |
| 6 (even) | 1 | 4 | 16 | YES on all |

Reducibility scales the nullity (`m²` for even n, the tensored `M_m(C)` commutant)
but **never changes the nonzero-vs-zero verdict**. The DECISIVE-FAILURE PROBE
explicitly searched n=2..6, m∈{1,2,4} for ANY case where reducibility flips the
existence verdict (γ₅ on odd n, or no γ₅ on even n): **none found** (residual 0.0).
Had any flip existed, the reframe FAILS — the probe is non-vacuous and passed.

**Conclusion (b):** the EVEN parity law's load-bearing content is **parity-of-n
only**, and it is irrep-INDEPENDENT. "In irreducible representations" is the
parent runner's computational convenience (the irrep is the minimal faithful
matrix realization), not a load-bearing requirement that the consumed γ₅ be
irreducible. The taste-singlet `Γ₅^spin` discharges B5/EVEN directly.

## 3. (c) R-DIAL — taste-dial invariance of the consumed quantity

PART (c) varies the single-taste projector across the `M₄(C)` taste commutant
(12 random rank-4 sectors) and checks the two consumed quantities:

- **(c1) γ₅-existence:** on EVERY single-taste sector a γ₅ exists — `Γ₅^spin`
  restricts to a γ₅ of that single irreducible Dirac factor and the restricted
  anticommutation `P({Γ₅^spin, αμ})P = 0` holds (dial-invariant existence,
  residual 3.9e-15).
- **(c2) anomaly trace:** with 4 orthogonal rank-4 taste projectors summing to I,
  the per-sector trace of a representative taste-singlet chirality-graded anomaly
  insertion is **IDENTICAL across all 4 sectors** (spread 6.4e-16), equal to ¼ the
  full taste-summed trace (residual 8.9e-16), with `Σ sector = full` (residual
  1.0e-15). The four tastes are degenerate replicas, so the consumed anomaly
  quantity is a taste-dial CONSTANT (up to the overall replica factor).

Both consumed quantities are taste-dial-INVARIANT ⇒ **single-taste selection is a
within-sector dial, not load-bearing** for B4/B5/B6 or the B1/B3 anomaly trace.

## 4. (d) Downstream-need audit (grep-backed)

Read-only grep of keystone and parent for `irreducible | single-taste | de-tast`:

- **Keystone:** ZERO occurrences. B4/B5/B6 consume only γ₅-existence, even-`n`, and
  `d_s=3` — never irreducibility or a taste selection.
- **Parent:** every occurrence is either (i) the **P-REC declared premise itself**
  (lines 92, 219, 257, 305) — the claim being reframed, not a downstream consumer —
  or (ii) the **EVEN parity-law parenthetical** "in irreducible representations"
  (lines 61, 222, 361), which §2 above shows is computational convenience, not a
  consumed requirement.

No downstream step (B5 existence, B6 parity, SC clock count) consumes a property a
taste-singlet γ₅ lacks. The d_t pin (SC) consumes the clock count, not chirality
irreducibility.

## 5. Verdict

**P-REC REFRAMES TO UNNECESSARY for the 1105 consumer.** The chirality+even-dimension
edge (B4 → B5/EVEN → B6) routes through the taste-singlet `Γ₅^spin` witness, which
already satisfies the existence predicate B4/B5 actually consume; the EVEN parity law
needs only parity-of-`n` (irrep-independent); and the consumed quantities are
taste-dial-invariant. The single-taste / irreducible-Dirac-factor selection that
P-REC was admitting is a **within-sector dial**, not load-bearing for the consumer.

This is a **PARTIAL UNLOCK** of the 1105 cone: the B4/B5/B6 chirality+even-dimension
premise edge is discharged from A_min + the taste-singlet core WITHOUT a new axiom,
new primitive, or any single-taste admission. The block01 SELECTOR wall is not
cracked as a supplier statement — it is rendered UNNECESSARY by reframing what the
consumer needs.

**Scope fence (honest):** this unlock is the B4/B5/B6 chirality+even-dim edge ONLY.
It does NOT touch P-ABJ (B2 external admission), P-COMP (B3 RH-completion existence),
or P-HY (the "is-gauged" predicate). The d_t=1 pin still needs SC/(B-AXIS). No
single-taste chirality is admitted as derived; the result holds invariantly over the
entire `M₄(C)` law-admissible taste family, so it is a derivation of UNNECESSITY, not
realized-state-dependent registered data.

## 6. Authorities and discipline

- **Reused (NOT rebuilt):** block01 P-REC core
  `scripts/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py`
  (Γ₅^spin residual 0.0, M₄(C) taste commutant) — PART 0 reproduces its residual-0
  facts in-tree.
- **Retained authority recomputed in-tree (CONTEXT-ONLY, not cited blind):**
  `CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10`
  (retained positive_theorem) — its anticommutant-nullity law recomputed on irrep
  AND reducible carriers in PART (b); the keystone/parent EVEN dependency is the
  recomputed object, never imported as an A_min derivation.
  `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` (retained_no_go) — root M₂(C) wall
  that block01's reused core already encodes; not collided here (taste-singlet γ₅
  lives in the doubled carrier, not per-site).
- **Primitives loaded:** the four approved primitives are legitimate premises; this
  route uses `minimal_axioms` (which-symmetry-gauged stays withheld, untouched here)
  and reads the realized-state-independence requirement as the `M₄(C)` dial-invariance
  test (c). No new axiom/primitive; keystone/parent kept CONTEXT-ONLY and unaudited;
  no edits to docs/audit/data, ledger, queue, or publication.
- **Exercise lessons applied:** functional-calculus-correct membership (the taste
  commutant `{α}″` is the spectator `M₄(C)`, reused from block01); a result holding
  over the full law-admissible family (every taste dial) is a derivation of
  unnecessity, not registered data; the imported EVEN theorem is recomputed, never
  presented as a bare A_min derivation.
