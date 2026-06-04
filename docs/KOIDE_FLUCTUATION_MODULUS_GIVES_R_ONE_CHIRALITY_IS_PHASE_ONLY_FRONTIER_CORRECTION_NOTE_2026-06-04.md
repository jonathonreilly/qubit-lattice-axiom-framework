# The Koide Fluctuation Modulus Gives r=1; Chirality Moves Only the Phase — Frontier Correction (Retracts the "Chiral → r=1/2" Mechanism)

**Date:** 2026-06-04
**Type:** correction
**Claim type:** correction — supersedes the mechanism of
`SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md` (#2614, block 4)
and `KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md`
(#2617, block 5). Both are on main; this note corrects them with real QFT.
**Claim scope:** the fermion-induced fluctuation-determinant **modulus** that sets the Koide
magnitude `r = |b|^2/a^2` is a function of `M^dag M` (i.e. `|b|^2`); the C3 doublet contributes
**two** genuine real fluctuation modes `(Re b, Im b)` (doublet Hessian rank 2), giving the `(1,2)`
weighting → `r = 1` (kappa=1), **robustly**. This holds for **chiral and Kähler-Dirac fermions
too**: a chiral fermion's effective action splits into `Re W = (1/2)·(Dirac modulus)` (still
`|b|^2`, two modes, r=1) plus `Im W =` the η-invariant (a **phase**). So **chirality changes only
the determinant phase** — it governs `delta = arg(b)` (the Koide phase ≈ 2/9), **not** the
magnitude `r`. Holomorphic counting (`b` once → r=1/2) requires a **SUSY superpotential**, which
the framework does not have.
**Consequence:** blocks 4/5's "chiral / holomorphic → r=1/2" is **refuted**. The framework's
`r = 1` (Q=1) prediction for a clean color-singlet lepton triplet is now backed by **real QFT**
(Coleman-Weinberg), not only the framework's internal measure — so the Koide partial falsification
is **robust**.
**actual_current_surface_status:** correction note; the modulus→r=1 result and the
non-holomorphy are reproven from the circulant primitive (sympy+numpy). Not retained.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_koide_modulus_gives_r_one_chirality_is_phase_only_exact.py`](./../scripts/audit_companion_koide_modulus_gives_r_one_chirality_is_phase_only_exact.py)

## Why this correction (frontier physics, external cross-check)

Blocks 4–5 proposed that the chirality-graded **supertrace / holomorphic** count weights the
complex doublet parameter `b` **once** → `(1,1)` → `r = 1/2`. Independent frontier-physics review
of the real QFT literature **refutes the mechanism**:

- The one-loop fermion effective potential is `V ~ Tr log(M^dag M)` (Coleman-Weinberg) — a function
  of `M^dag M ⊃ |b|^2`. Its dependence on `(Re b, Im b)` is **non-holomorphic** with a **rank-2**
  doublet Hessian → two genuine real modes → `(1,2)` → `r = 1`.
- For a **chiral (Weyl)** fermion the effective action splits exactly as `Re W = (1/2)·(vector
  Dirac result)` + `Im W = η`-invariant (Alvarez-Gaumé; lattice η-invariant literature). The
  **modulus** `Re W` still depends on `M^dag M` → `|b|^2` → two modes → r=1. Only the **phase**
  `Im W` (the η-invariant) is genuinely chiral.
- Holomorphy (`b` counted once) is a property of the **SUSY superpotential** only (Seiberg,
  *The Power of Holomorphy*); even in a SUSY theory the **Kähler potential** — which governs the
  fluctuation determinant — is non-holomorphic in `b, b̄`. The framework has no superpotential, so
  no holomorphic counting.
- For **Kähler-Dirac / staggered** fermions specifically (Catterall–Butt, *Anomalies and SMG for
  Kähler-Dirac fermions*), the chiral structure is a `Z_4` anomaly affecting the **phase** of the
  measure; the **modulus** is real. A holomorphic-in-`b` determinant is **not** established.

## Statement (reproven, sympy+numpy)

For `M = aI + bC + b̄C²` (Hermitian; eigenvalues `λ_k = a + 2|b|cos(arg b + 2πk/3)`):

1. `M` is Hermitian → a vector (Dirac) mass has **real** determinant (no chiral phase).
2. `V_mod = Tr log(M^dag M)` depends on **both** `Re b` and `Im b`; the doublet Hessian has
   **rank 2** → two real modes (non-holomorphic) → `(1,2)`.
3. The modulus extremum sits at `r = 1` (not 1/2) — reproducing block 1 (#2601) from the
   Coleman-Weinberg modulus.
4. The chiral **η-phase** exists only for a **non-Hermitian** (chiral) `M`; it is `arg(det)`,
   moving `delta = arg(b)` / CP — **not** the magnitude `r`.
5. `r = 1/2` would require a **rank-1** (holomorphic) doublet — i.e. a SUSY superpotential — which
   the framework lacks.

All five checks pass (sympy+numpy).

## What this means for the campaign (corrected verdict)

- **Blocks 1–3 stand and are strengthened.** They computed the modulus and got `r = 1` (fermion
  determinant, taste, multi-factor). Real QFT confirms the modulus is the right object and `r = 1`
  is **robust** — the framework genuinely predicts `Q = 1` (kappa=1) for a clean color-singlet
  C3-triplet. Probe 29's partial falsification (vs empirical `Q = 2/3`) is now **real-physics-backed,
  not a measure artifact.**
- **Blocks 4–5 are corrected.** The chiral structure does **not** rescue `r = 1/2`; it governs the
  **phase** `delta`, not the magnitude. The "gated bit" framing (chiral vs vector Yukawa → r) was
  mis-assigned: the magnitude `r` is set by the modulus (`= 1`) **regardless** of chirality.
- **`r = 1/2` (Q = 2/3) is a genuine 45-year open problem** — and external literature agrees the
  democratic balance `|b|/a = 1/√2` is "**not determined from first principles**" (Rivero-Gsponer).
  The real obstacle is the **pole-mass vs running-mass** problem (Koide 2018): the relation holds at
  pole masses but field theory derives running-mass relations. The only serious resolution
  (Sumino's family gauge boson) **protects** an assumed `2/3` via a TeV-scale family gauge
  symmetry; it does **not** derive it. **The framework does not solve Koide.**

## New direction this opens (honest, not yet established)

The genuinely chiral object is the **η-invariant / determinant phase**, whose natural home is
`delta = arg(b)` — the Koide **phase** (Brannen `δ ≈ 2/9 rad`), not the magnitude. So the framework's
chirality (`ε=(-1)^{x+y+z}`, `{ε,D}=0`; the chiral Kawamoto-Smit operator forcing the triplet) is a
candidate origin for the Koide **phase**, a distinct and untried direction. This is a **lead, not a
result**: whether the framework's η-invariant equals `arg(b) ≈ 2/9` is an open computation.

The magnitude `r = 1/2` would need, per the real literature, **either** a vacuum-alignment principle
that forces `|b|/a = 1/√2` (none exists) **or** a Sumino-type radiative-protection structure (new
TeV physics). The framework's lattice structure (masses defined at the lattice scale, no continuum
limit) may bear on the pole-vs-running problem — a separate frontier question.

## Trace gate

```yaml
trace_class: correction_and_reframe
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: refutes_prior_lead_and_reframes
artifact_role: correction
next_trace_action: "split the question: (magnitude r=1/2) is the genuine open problem requiring vacuum alignment + radiative protection (framework lacks both); (phase delta) is the new chiral/eta-invariant direction -- compute whether the framework's eta-invariant gives arg(b)~2/9."
```

## Forbidden imports / reprove-and-cite

- The modulus→r=1 result and the non-holomorphy (rank-2 doublet Hessian) are **reproven** from the
  circulant primitive `M = aI + bC + b̄C²` in the runner. The real-QFT facts (Coleman-Weinberg;
  Alvarez-Gaumé chiral split; Seiberg holomorphy; Catterall-Butt Kähler-Dirac `Z_4`; Koide 2018;
  Sumino; Rivero-Gsponer "not from first principles") are **comparators / cross-checks**, never
  derivation inputs. No PDG values as derivation inputs.

## Cross-references (corrected)

- `SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md` (#2614, block 4)
  — **superseded mechanism**: the supertrace/index governs the determinant **phase**, not the
  magnitude.
- `KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md` (#2617,
  block 5) — **corrected**: the FS math stands, but the bit governs `delta`, not `r`.
- `CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`
  (#2601, block 1) — the modulus → r=1, here re-derived from Coleman-Weinberg and **strengthened**.
- External comparators: Koide arXiv:1809.00425; Sumino arXiv:0812.2103; Rivero–Gsponer
  hep-ph/0505220; Seiberg hep-th/9408013; Catterall–Butt arXiv:2101.01026.
