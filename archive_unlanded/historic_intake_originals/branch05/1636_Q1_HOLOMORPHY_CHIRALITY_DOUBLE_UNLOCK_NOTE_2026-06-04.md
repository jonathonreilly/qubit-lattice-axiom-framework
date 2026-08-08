---
claim_id: q1_holomorphy_chirality_double_unlock_note_2026-06-04
claim_type_author_hint: meta
---

# Q1 keystone, angle C: holomorphy (det_C) does NOT supply the generation chirality grading — the two are SEPARATE gates

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md).

**Date:** 2026-06-04
**Claim type:** meta (structural reconciliation / coverage-audit correction)
**Status authority:** independent audit lane only. This note sets, predicts, and
proposes no audit status; it adopts no axiom, primitive, or import. It records a
finite linear-algebra reconciliation on the generation factor `R^3`.
**Primary runner:** [`scripts/q1_holomorphy_chirality_double_unlock_2026_06_04.py`](../scripts/q1_holomorphy_chirality_double_unlock_2026_06_04.py)
(SCORECARD 38/38 PASS, 0 FAIL).
**Cached log:** [`logs/runner-cache/q1_holomorphy_chirality_double_unlock_2026_06_04.txt`](../logs/runner-cache/q1_holomorphy_chirality_double_unlock_2026_06_04.txt)

## Question

A coverage audit claimed the charged-lepton Koide `Q1` gate is a SINGLE binary —
"chiral/holomorphic vs vector/real on the generation Yukawa" — bundling (i) the
`r=1/2` VALUE bit (`det_C` → `Q=2/3` vs `det_R` → `Q=1`, the holomorphy fork)
with (ii) the CHIRALITY grading the retained anti-commuting `Q=2/3` derivation
needs. This note tests, with explicit computation, whether the HOLOMORPHIC
reading on the generation factor itself supplies a valid chirality grading,
making `Q1` a true double-unlock.

The chirality grading `Gamma_chi` has three requirements (from the retained
`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md` and the
`FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30.md`): it must be
**Hermitian** (involution, `Gamma^2=I`, spectrum `±1`), **off-block** (mix the
singlet ↔ doublet, i.e. NOT block-diagonal in `{P_s,P_d}`), and admit a mass
operator `H` with `{H,Gamma}=0` giving `Q=2/3`. The circulant no-go is exactly
the trap that block-diagonal (on-block) operators cannot escape; an off-block
grading is the open loophole.

## Verdict: HOLOMORPHY-AND-CHIRALITY-SEPARATE

The holomorphic reading does **not** supply a valid generation chirality
grading. Each holomorphy-derived object fails the off-block (or Hermitian/
involution) requirement, by direct computation:

| holomorphy object | Hermitian? | involution `Γ²=I`? | off-block? | `Q=2/3` anticommutant? | verdict |
|---|---|---|---|---|---|
| `J = (C−Cᵀ)/√3` (the `det_C` complex structure) | **no** (anti-Herm, `Jᵀ=−J`) | **no** (`J²=−P_d`) | **no** (commutes `P_s,P_d`) | n/a | fails all three |
| `K` (complex conjugation / anti-holomorphic CPT) | yes | yes | **no** (reflects WITHIN doublet, `P_s K P_d=0`) | **no** (anticommutant is traceless → `Q=∞`, and breaks `C₃`) | on-block |
| `sgn det_C` (signed vs singular-value readout) | — | — | — | — | a **scalar** Z₂, not an operator grading |

So `J` (which performs the `det_C` reading) is **on-block** and **anti-Hermitian**;
`K` (the only Hermitian involution holomorphy provides) is **on-block** — it
reflects the doublet's imaginary axis (`b_im → −b_im`, `det K = −1`, spectrum
`{+1,+1,−1}`) but never mixes singlet ↔ doublet; and the signed-`det_C` bit is a
sign/phase on a single complex number, **categorically** not a 3×3 Hermitian
grading. None is simultaneously Hermitian + involution + off-block + `Q=2/3`.

**Is holomorphy's involution Hermitian-and-off-block? NO.**

## Why the off-block requirement is real (non-vacuous) and unmet by holomorphy

Off-block Hermitian involutions DO exist: the explicit reflection `G_off`
swapping the singlet `v0` with a doublet vector `u` is Hermitian, `G_off²=I`,
spectrum `{+1,+1,−1}`, and genuinely off-block (`P_s G_off P_d ≠ 0`). But
`[J, G_off] ≠ 0`: it is **not** holomorphic, and no product of `J`, `K`, or the
`det_C` sign generates it. The object that could escape the circulant no-go
exists in `Sym(R³)`; holomorphy simply does not produce it.

This is consistent with `KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`
(every retained antilinear/`CPT` map is a `det=−1` reflection within the doublet
plane — on-block) and with `FLAVOR_SPLIT_THE_BRICK_DOUBLET_COMPLEX_STRUCTURE_2026-06-04.md`
(the doublet `J` COMMUTES with every circulant `H` — on-block, a holomorphic
READOUT object, not an anticommuting grading).

## Reconciliation with the prior chirality-factor pressure test (PT-C)

PT-C found the chirality-FACTOR Dirac structure reduces to on-block (`Q=1`). This
note finds the GENERATION-factor holomorphy ALSO reduces to on-block. The runner
reproduces the Connes-Lott check: `γ_CL = I₃ ⊗ σ₃` anticommutes with `G ⊗ σ₁`
for **every** generation `G` (only `{σ₁,σ₃}=0` is used) — so the doubling-factor
chirality is INERT on the generation index. Both the chirality factor (PT-C) and
the generation holomorphy (here) leave the generation operator on-block. The two
pressure tests converge.

## Consequence — the coverage-audit "same binary" claim is CORRECTED

`Q1` is **two** gates, not one:

- the `r=1/2` VALUE bit IS the holomorphy fork (`det_C` → `Q=2/3` vs `det_R` →
  `Q=1`), carried by the commuting `J`/`det_C` object and the scalar `sgn det_C`
  readout — this is the half a holomorphy choice closes;
- the CHIRALITY grading (a Hermitian off-block `Γ_χ` anticommuting to `Q=2/3`)
  is a **separate** open handle that holomorphy does not supply.

So choosing holomorphy on the generation Yukawa closes only the `r=1/2` half of
`Q1`. The off-block chirality grading remains a distinct open question — the same
`C₃`-orbit-splitting handle the no-transport and generation-identification lanes
isolate.

## The next path this opens (not a closing framing)

The off-block grading that escapes the circulant no-go **exists** in `Sym(R³)`
(witnessed by `G_off`) but is not holomorphic. The live question is whether any
native structure — distinct from the complex structure `J`, the conjugation `K`,
or the `det_C` sign — produces a `C₃`-orbit-splitting Hermitian involution. This
is the same off-block target named by `FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30`'s
sharpest path (the equivariant spectral-asymmetry / non-circulant endpoint),
now sharpened by the present result: holomorphy is not a source for it, so the
search should not route through the polarization/`det_C` choice.

## What this note does NOT claim

- It does not derive `r=1/2`, `Q=2/3`, or any charged-lepton mass; it consumes no
  PDG value, fitted parameter, or literature comparator.
- It does not adopt holomorphic polarization, the `det_C` reading, or a chirality
  grading as an axiom, primitive, or import.
- It does not assert that NO native off-block grading can ever be derived; it
  shows only that the holomorphy-derived objects (`J`, `K`, `sgn det_C`) are not
  such a grading.
- It does not weaken or retire any retained row, and it sets no audit status.

## No-Go Discipline Disposition

The reconciliation half (holomorphy ≠ chirality) is a bounded structural fact,
not a global no-go. The open half (find an off-block grading) is preserved as an
explicitly open, non-enumerated search.

- **N1 alternative routes:** at least five distinct off-block-grading routes
  remain open and untouched: (1) equivariant APS/`Z_N` spectral-asymmetry
  endpoints; (2) multi-factor Connes-Lott with `γ` on a factor distinct from the
  generation `R³`; (3) `C₃`-breaking (non-circulant) Hermitian involutions such
  as `G_off`; (4) twisted/modular spectral triples; (5) larger Hilbert-space
  extensions. This note rules out only the holomorphy-derived objects as the
  grading.
- **N2 wall independence:** the value bit (`r=1/2`) and the chirality bit
  (off-block grading) are shown to be SEPARATE handles; the note does not claim
  independence beyond exhibiting that no holomorphy object meets the off-block
  requirement.
- **N3 hidden-wall scan:** all inputs (`C`, `P_s`, `P_d`, `J`, `K`, `γ_CL`) are
  explicit; no physical species, PMNS, mass, or scale reading is consumed.
- **N4 residual matching:** cited rows are used only where their residual
  matches — the anti-commuting no-go and the no-transport note supply the three
  `Γ_χ` requirements; the block-count and split-the-brick notes supply the
  on-block facts for `K` and `J`. None is cited as a positive derivation.
- **N5 rhetoric audit:** "separate gates" means the holomorphy fork closes only
  the `r=1/2` value bit; it does NOT mean chirality is impossible or that the
  search space is finite or closeable.
- **N6 partial-closure scan:** a future off-block grading (native or
  convention/readout-factorized) could still close the chirality half without a
  new axiom; this note leaves that open.
- **N7 steelman:** a reviewer could argue the physical Koide readout factors
  through the doublet complex-slot quotient (the value bit) and that "chirality"
  has no charged-lepton lab referent (e/μ/τ are not L/R partners), so the second
  gate may be dissolvable rather than derivable. This note does not close that
  reframe; it only shows holomorphy does not supply the grading-as-operator.
- **N8 cross-cycle echo:** downstream Koide/spectral-triple claims must cite this
  only as a local reconciliation (holomorphy ≠ chirality grading), not as route
  closure for the off-block search.

## Authorities (load-bearing structure, non-load-bearing values)

| Authority | Role |
|---|---|
| [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) | one-qubit operator algebra and `Z³` substrate baseline |
| [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) | the circulant trap + `Γ_χ=(2/3)J_allones−I` (the on-block obstruction) |
| [`FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30.md`](FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30.md) | the off-block requirement + Connes-Lott inertness (PT-C) |
| [`FLAVOR_SPLIT_THE_BRICK_DOUBLET_COMPLEX_STRUCTURE_2026-06-04.md`](FLAVOR_SPLIT_THE_BRICK_DOUBLET_COMPLEX_STRUCTURE_2026-06-04.md) | `J` is the commuting holomorphic-readout object, distinct from a grading |
| [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md) | the `det_C` (`r=1/2`) vs `det_R` (`r=1`) value fork |
| [`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`](KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md) | antilinear `CPT`/conjugation maps are on-block `det=−1` reflections |
| [`KOIDE_ANTICOMMUTING_EIGENVECTOR_VS_EIGENVALUE_READOUT_RECONCILIATION_NOTE_2026-06-01.md`](KOIDE_ANTICOMMUTING_EIGENVECTOR_VS_EIGENVALUE_READOUT_RECONCILIATION_NOTE_2026-06-01.md) | traceless anticommutant → eigenvalue `Q=∞` |

## Verification

```bash
python3 scripts/q1_holomorphy_chirality_double_unlock_2026_06_04.py
```

The runner checks the isotype split, each holomorphy candidate against the three
`Γ_χ` requirements, the existence of an off-block Hermitian involution and its
non-holomorphy, the Connes-Lott separate-factor inertness, the independent value
fork, and the explicit verdict. 38/38 PASS.
