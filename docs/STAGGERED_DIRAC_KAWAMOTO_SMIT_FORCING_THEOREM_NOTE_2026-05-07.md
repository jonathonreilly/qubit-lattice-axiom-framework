# Staggered-Dirac Substep 2 — Kawamoto-Smit Phase Forcing

**Date:** 2026-05-07; 2026-06-06 cocycle/gauge-class uniqueness repair;
2026-06-10 science-fix (iff + premise honesty + forcing certificate —
see §0 changelog); 2026-06-11 substep-1 boundary sync;
2026-06-13 source-boundary repair
**Type:** bounded_theorem
**Claim scope:** Abstract Clifford-link scalarization theorem on
nearest-neighbor simply connected regions of `Z³`. Given Hermitian
anticommuting `Cl(3)` link matrices `γ_μ` and a nearest-neighbor
`U(1)` phase system `η`, the site-local unitary scalarization equation
`T(x+μ) = η_μ(x) γ_μ T(x)` is solvable IF AND ONLY IF `η` satisfies the
Clifford `−1` plaquette cocycle, and on simply connected regions the
solutions form EXACTLY ONE local gauge class: the class of the
Kawamoto-Smit representative
`η_1 = 1, η_2(x) = (−1)^{x_1}, η_3(x) = (−1)^{x_1+x_2}`. This row does
not import the physical kinetic-class, P-SD, or statistics-selection
claims as load-bearing theorem premises; those are downstream
physical-use gates for the staggered-Dirac realization note.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome; audit verdict and effective status
are set only by the independent audit lane.
**Primary runner:** [`scripts/probe_kawamoto_smit_phase_forcing.py`](../scripts/probe_kawamoto_smit_phase_forcing.py)
**Authority role:** source note for the abstract Kawamoto-Smit
cocycle/gauge classification used by substep 2 (kinetic form, R2) of
the staggered-Dirac realization gate
(`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`, parent context
only, not a one-hop authority for this row),
which may consume this theorem only after its separate physical
kinetic-class/P-SD/statistics gates are supplied.

## 0. Changelog

- **2026-06-13 (source-boundary repair).** The auditable row is now the
  abstract Clifford-link scalarization theorem, not a physical
  derivation of the staggered kinetic class. P-KIN, P-SD, P-FLUX, and
  the substep-1 statistics-selection boundary are retained as
  downstream physical-use context only; they are not load-bearing
  theorem premises for Theorem 2 below. The local theorem still proves
  the same iff and one-gauge-class result, and still excludes torus
  holonomies from the simply connected scope. No audit status, ledger
  row, or realization-gate closure claim is changed here.
- **2026-06-10 (science-fix, this revision).** Four defects repaired:
  1. *(High — missing sufficiency.)* The 2026-06-06 revision proved
     only necessity (any scalarization forces the `−1` cocycle) plus
     gauge classification. The converse — that every cocycle solution
     actually admits a site-local unitary scalarization — was never
     proved, so "the cocycle characterizes admissibility" was an
     overclaim. Fixed: Lemma 3 (path-product transport construction;
     plaquettes generate loops on simply connected regions), giving the
     genuine iff in Theorem 2(i).
  2. *(High — out-of-packet authority.)* The prior revision cited a
     "retained no-rooting irreducibility" result NR via
     `scripts/frontier_generation_rooting_undefined.py`, a script
     outside the one-hop citation packet, and NR was load-bearing
     nowhere in the proof. NR is removed entirely; rooting/taste
     reduction is now listed under "What this does NOT close" (§7).
  3. *(Medium — overclaim inconsistency.)* The old Answer and Step 4
     said spin-diagonalization is "forced by single-mode Grassmann"
     while Theorem 2 was stated "under the spin-diagonalization
     premise." The 2026-06-10 revision made P-KIN/P-SD explicit
     assumptions to avoid silent physical overclaiming; the
     2026-06-13 revision supersedes that framing for this row by moving
     P-KIN/P-SD to downstream physical-use context and auditing only
     the abstract scalarization theorem.
  4. *(Medium — unjustified `η ∈ {±1}`.)* The old derivation assumed
     sign-valued phases without justification. Fixed: Remark R2 — the
     entire argument runs verbatim with `U(1)`-valued phases, giving
     uniqueness up to local `U(1)` gauge with the same real
     representative `η^0` (runner section E).
  5. *(Low — choice-language.)* Step 3's "natural identification"
     wording (a definition presented as if load-bearing) is demoted to
     Remark R1; the actual computable content is the bipartiteness
     corollary `{ε, D_staggered} = 0`. Remark R3 records that `−η^0`
     is the `ε`-gauge transform of `η^0` (same class; runner-verified),
     so the global-sign choice is gauge, not physics.
  The runner is rewritten from an instantiate-and-check script (which
  certified consistency of the canonical solution plus one gauge
  transform, not forcing) into a forcing certificate: exhaustive
  enumeration of all `2^12 = 4096` sign systems on the unit cube with
  scalarizability decided by explicit transport, a GF(2) cohomology
  certificate at scale, and falsification legs (§6).
- **2026-06-11 (substep-1 boundary sync).** The substep-1 source has
  since discharged the former U4/per-site-identification boundary via
  the Quantum/dim-two route while preserving the statistics-selection
  residual: the hard-core-boson frame remains outside the
  two-candidate comparison. The 2026-06-11 B1/P-KIN/P-SD boundary
  language is now superseded by the 2026-06-13 source-boundary repair:
  BlockT1/statistics selection and P-KIN/P-SD are downstream
  physical-use gates, not theorem premises for this row.
- **2026-06-12 (kinetic supply-line sync).** Current main now contains
  a sharper source-side supply line for this note's former B2/B3
  residuals. `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`
  proves a two-flux-class collapse on the licensed nearest-neighbor
  bilinear surface and discharges P-SD as an absorbing-frame theorem on
  the flux-`-1` branch; it leaves exactly the P-FLUX bit
  `phi = -1` as the P-KIN residual. `P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`
  then composes the retained `(Z)` geometry certificate with the FSB-K
  thermal row as a conditional selector for that bit. As of the
  2026-06-13 source-boundary repair, this supply line is downstream
  physical-use context only; it is not a premise for the abstract
  cocycle/gauge theorem audited here.
- **2026-06-06.** Cocycle/gauge-class uniqueness repair (necessity +
  classification; superseded in form by Lemmas 2 and 4 below).
- **2026-05-07.** Original substep-2 note.

## 1. Question

For the abstract nearest-neighbor Clifford-link scalarization problem
on a simply connected region of `Z³`, which phase systems admit a
site-local unitary scalarizing frame, and in exactly what sense is the
Kawamoto-Smit phase law "forced"?

## 2. Answer (bounded)

**For the abstract scalarization problem, yes — as an iff plus an
exhaustive classification.** A phase system on nearest-neighbor `Z³`
links admits a site-local unitary scalarization if and only if it
satisfies the Clifford `−1` plaquette cocycle (Theorem 2(i), Lemmas 2
+ 3), and on simply connected regions the cocycle solutions form
exactly one local gauge class — the class of

```
η_1(x) = 1
η_2(x) = (−1)^{x_1}
η_3(x) = (−1)^{x_1 + x_2}
```

(Theorem 2(ii), Lemma 4). What is NOT claimed in this row: that a
physical staggered kinetic class, the P-SD absorbing frame, the P-FLUX
selector, or the single-mode statistics-selection bridge has been
derived. Those are downstream physical-use gates, not load-bearing
premises of the theorem proved here.

## 3. Boundaries (the theorem surface, stated up front)

| ID | Boundary | Where it bites |
|---|---|---|
| B1 | Substep-1 single-mode/statistics selection is downstream physical-use context only. The abstract theorem below does not require the matter-measure row, and does not decide Grassmann-vs-hard-core-boson selection. | realization-gate closure, not Theorem 2 |
| B2 | P-KIN/nearest-neighbor physical kinetic-class selection is downstream physical-use context only. The theorem starts after an abstract nearest-neighbor Clifford-link scalarization problem has been supplied. | realization-gate closure, not Theorem 2 |
| B3 | P-SD/site-local absorbing-frame existence is downstream physical-use context only. The theorem classifies the phase systems satisfying the scalarization equation; it does not prove that a physical model must supply that equation. | realization-gate closure, not Theorem 2 |
| B4 | Finite tori carry extra holonomy data: signs around non-contractible cycles (PBC/APBC and wrap-sign conventions) are boundary convention data, not local phase law; likewise lattice-axis permutation is coordinate-label gauge. | Theorem 2(ii) is stated on simply connected regions |

### 3.1 2026-06-12/13 downstream physical-use supply line

The physical realization gate has a separate source-side supply line for
the B2/B3 downstream-use gates:

| former boundary | current source-side supplier | current honest status |
|---|---|---|
| P-SD site-local absorbing frame | `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`; runner cache `staggered_dirac_kinetic_class_forcing_check_2026_06_10.txt` (`TOTAL: PASS=27 FAIL=0`) | discharged as a theorem on the flux-`-1` branch, pending independent audit of that supplier |
| P-KIN broad kinetic-class declaration | same kinetic-class forcing note | reduced to exactly two licensed frame classes, `K0` with flux `+1` and `K1` with flux `-1`; the surviving residual is the one-bit P-FLUX selector |
| P-FLUX selector `phi = -1` | `P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`; runner cache `p_flux_selection_via_fsb_k_check_2026_06_11.txt` (`TOTAL: PASS=16 FAIL=0`) | conditional on FSB-K's audit grade, using the retained `(Z)` kernel-geometry certificate; no selection is performed at current grades |

When a downstream gate uses this row as physical staggered-Dirac
support, that downstream row must still supply the cascade:

```text
kinetic-class forcing
  -> P-SD discharged on K1
  -> P-KIN reduced to P-FLUX
  -> P-FLUX conditionally selected by FSB-K + retained Z
```

Source-only sync verifier:
`scripts/staggered_dirac_kinetic_supply_line_sync_2026_06_12.py`;
cache:
`logs/runner-cache/staggered_dirac_kinetic_supply_line_sync_2026_06_12.txt`.

This cascade is not a load-bearing premise for the theorem proved in
this row. It matters only when a downstream realization-gate argument
uses this abstract cocycle/gauge theorem as its R2 input.

## 4. Setup

### 4.1 Premises

| ID | Statement | Class |
|---|---|---|
| CL3 | Hermitian generators `γ_1, γ_2, γ_3` with `γ_μ² = I` and `γ_μγ_ν = −γ_νγ_μ` for `μ ≠ ν`; Pauli realization used for executable checks | native one-qubit/Cl(3) algebra, cross-referenced to [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md) |
| Lattice | Simply connected nearest-neighbor region of `Z³` with its square plaquettes | accepted lattice setting plus finite cell-complex algebra |
| Phase | A nearest-neighbor link phase system `η_μ(x) ∈ U(1)` | theorem variable, not an imported physical input |
| BPG | `Z³` nearest-neighbor graph is bipartite | admissible standard math (graph theory); used only for the parity corollary and global-sign gauge remark |

Not theorem premises: BlockT1, P-KIN, P-SD, P-FLUX, FSB-K, the
substep-1 statistics-selection row, rooting/taste reduction, PDG
values, lattice-MC values, or fitted coefficients. Those may matter for
physical realization-gate closure, but they are not load-bearing inputs
to the cocycle/gauge classification proved here.

### 4.2 Forbidden imports

- NO PDG values, NO lattice MC values, NO fitted coefficients
- NO new axioms (no-new-axiom rule)

### 4.3 The scalarization condition

For the abstract link problem, a scalarizing frame is a site-local
unitary map `T(x) ∈ U(2)` satisfying the **scalarization condition**

```
T†(x) γ_μ T(x + μ̂) = η_μ(x) · I_2                                       (4)
```

where the phases `η_μ(x)` are a priori `U(1)`-valued (Remark R2); the
sign-valued case `η_μ(x) ∈ {±1}` is the real representative. A physical
kinetic row may try to derive or supply this equation from its own
matter and kinetic assumptions; this row proves what follows once the
equation itself is the object under study.

## 5. Lemmas and theorem

### Lemma 1 (sublattice parity)

The `Z³` nearest-neighbor graph is bipartite (BPG), with parts
`A = {x : x_1+x_2+x_3 even}` and `B = {x : x_1+x_2+x_3 odd}`, and

```
ε(x) := (−1)^{x_1 + x_2 + x_3}                                          (1)
```

is the unique nontrivial `Z₂` vertex grading flipped by every
nearest-neighbor step. *Proof:* standard graph theory; each unit step
changes `x_1+x_2+x_3` by `±1`. ∎

### Lemma 2 (necessity: scalarization forces the `−1` cocycle)

If `(T, η)` satisfies (4) with `γ_μ² = I`, `γ_μ γ_ν = −γ_ν γ_μ`
(`μ ≠ ν`), then `η` satisfies the **Clifford `−1` plaquette cocycle**

```
η_ν(x + μ̂) η_μ(x) = − η_μ(x + ν̂) η_ν(x)        (μ ≠ ν).               (8)
```

*Proof.* From (4), `T(x + μ̂) = η_μ(x) γ_μ T(x)` (using `γ_μ† = γ_μ`,
`γ_μ² = I`; for `U(1)` phases replace `η_μ(x)` by its value, the
computation is identical). Transporting from `x` to `x + μ̂ + ν̂` along
the two elementary paths gives

```
η_ν(x + μ̂) η_μ(x) γ_ν γ_μ T(x) = η_μ(x + ν̂) η_ν(x) γ_μ γ_ν T(x),
```

and `γ_ν γ_μ = −γ_μ γ_ν` with `T(x)` invertible forces (8). ∎

### Lemma 3 (sufficiency: every cocycle solution scalarizes)

Let `R ⊆ Z³` be simply connected (e.g. any box, or all of `Z³`) and let
`η` satisfy (8) on every plaquette of `R`. Then there exist site-local
unitaries `T(x)`, `x ∈ R`, satisfying (4) with exactly these `η`.

*Proof (path-product transport).* Fix a base point `x_0` and set
`T(x_0) := I`. For an edge `(x, μ)` define the transport factor
`U_{x,μ} := η_μ(x) γ_μ`, a unitary (product of a unimodular scalar and
a Hermitian unitary) with `U_{x,μ}^{-1} = η̄_μ(x) γ_μ`. Define `T(x)`
as the ordered product of transport factors along any lattice path from
`x_0` to `x`. This is well-defined iff the transport around every
closed loop is the identity. On a simply connected region every loop is
generated by elementary plaquette loops (the plaquettes generate the
loop group of the cell complex), and the transport around the
plaquette `x → x+μ̂ → x+μ̂+ν̂ → x+ν̂ → x` is

```
U_{x,ν}^{-1} U_{x+ν̂,μ}^{-1} U_{x+μ̂,ν} U_{x,μ}
  = η̄_ν(x) η̄_μ(x + ν̂) η_ν(x + μ̂) η_μ(x) · γ_ν γ_μ γ_ν γ_μ
  = − η̄_ν(x) η̄_μ(x + ν̂) η_ν(x + μ̂) η_μ(x) · I,
```

since `γ_ν γ_μ γ_ν γ_μ = −I`. By (8) the scalar prefactor is `−1`, so
the loop transport is `+I`. Hence `T` is well-defined, each `T(x)` is
unitary, and by construction `T(x + μ̂) = η_μ(x) γ_μ T(x)`, which is
(4). Right-multiplying all `T(x)` by a fixed unitary shows the choice
`T(x_0) = I` is no loss of generality. ∎

### Lemma 4 (exactly one gauge class on simply connected regions)

The canonical Kawamoto-Smit phases

```
η^0_1(x) = 1,  η^0_2(x) = (−1)^{x_1},  η^0_3(x) = (−1)^{x_1+x_2}        (6)
```

satisfy (8) (for `μ < ν`, shifting by `μ` flips `η^0_ν` while shifting
by `ν` does not flip `η^0_μ`). Let `η'` be any other solution of (8) on
a simply connected region and set `r_μ(x) := η'_μ(x) η̄^0_μ(x)`. Both
solutions carry the same `−1`, so `r` has trivial plaquette cocycle:

```
r_ν(x + μ̂) r_μ(x) = r_μ(x + ν̂) r_ν(x).                                 (9)
```

On a simply connected region every such closed one-cochain is exact:
set `g(x_0) := 1` and define `g(x)` as the path product of `r` from
`x_0` to `x` ((9) gives path independence, plaquettes generating
loops as in Lemma 3). Then

```
η'_μ(x) = ḡ(x) η^0_μ(x) g(x + μ̂)                                       (10)
```

(in the `Z₂` case `ḡ = g`). Conversely every gauge transform (10) of a
solution is a solution, with `T'(x) = g(x) T(x)` satisfying (4) for
`η'`. Hence the solutions of (8) form exactly one local gauge class,
containing the Kawamoto-Smit representative `η^0`. ∎

### Theorem 2 (Kawamoto-Smit phase forcing — bounded)

**On the abstract nearest-neighbor `Cl(3)` scalarization problem over a
simply connected region of `Z³`:**

**(i)** A nearest-neighbor phase system `η` (`Z₂`- or `U(1)`-valued)
admits a site-local unitary scalarization (4) **if and only if** it
satisfies the Clifford `−1` plaquette cocycle (8). [Lemmas 2 + 3]

**(ii)** On simply connected regions of `Z³`, the solution set of (8)
is **exactly one** local gauge class, the class of the Kawamoto-Smit
representative `η^0` of (6); a canonical solution of (4) is
`T(x) = γ_1^{x_1} γ_2^{x_2} γ_3^{x_3}` (on the Pauli realization,
`T(x) = σ_1^{x_1} σ_2^{x_2} σ_3^{x_3}`). [Lemma 4]

Hence any downstream staggered kinetic construction that separately
supplies this scalarization problem has its local link phases forced to
the Kawamoto-Smit class, up to finite-boundary holonomy/APBC convention
data and lattice-axis permutation gauge (B4). The physical operator,
measure, and kinetic-class selection are not part of this theorem. ∎

### Remarks

- **R1 (bipartiteness corollary).** Each hopping term of `D_staggered`
  connects opposite-parity sites (Lemma 1), so
  `{ε, D_staggered} = 0`. This replaces the former Step 3's "natural
  identification" of site chirality with sublattice parity, which was
  a labeling convention, not a load-bearing step; only the computed
  anticommutation is used downstream.
- **R2 (`U(1)` generalization; why `η ∈ {±1}` is not assumed).** Lemmas
  2–4 nowhere use reality of the phases: with `U(1)`-valued `η`, the
  same two-path computation gives (8), the same transport gives
  sufficiency, and the same path-product gives (10) with `ḡ(x)` —
  uniqueness up to local `U(1)` gauge with the **same real
  representative** `η^0`. Runner section E verifies this exactly
  (sympy): a genuinely complex local phase transform scalarizes and
  path-product recovery returns `η^0`.
- **R3 (global sign is gauge).** `−η^0` is the `ε`-gauge transform of
  `η^0`: `ε(x) η^0_μ(x) ε(x + μ̂) = −η^0_μ(x)` since `ε` flips across
  every edge (Lemma 1). So the overall-sign choice lies inside the
  single gauge class (runner check 28).
- **R4 (holonomy and axis order, B4).** Finite tori have
  non-contractible cycles; transport around them yields holonomy signs
  not fixed by the local cocycle. These are the PBC/APBC wrap-sign
  conventions, recorded as boundary data by the gate note, not
  additional local phase laws. Lattice-axis permutations relabel
  coordinates and permute the representative (6) accordingly —
  coordinate-label gauge.

## 6. What the runner computes

[`scripts/probe_kawamoto_smit_phase_forcing.py`](../scripts/probe_kawamoto_smit_phase_forcing.py)
— deterministic, no network, no randomness, runtime well under one
second. Checks are grouped in six sections; this is a *forcing certificate*,
not an instantiate-and-check script:

- **A (checks 1–25):** exact-sympy canonical construction —
  `T(x) = σ_1^{x_1} σ_2^{x_2} σ_3^{x_3}` scalarizes to the
  Kawamoto-Smit phases (6) on all 8 unit-cell sites × 3 directions;
  `ω = σ_1σ_2σ_3 = i I_2` (U2 cross-check).
- **B (checks 26–28):** exhaustive forcing certificate — ALL
  `2^12 = 4096` sign systems on the 12 edges of the `{0,1}³` box are
  enumerated and scalarizability is *decided* for each by the explicit
  Lemma-3 transport construction (exact Gaussian-integer arithmetic).
  Exactly `128 = 2^7` are scalarizable; the scalarizable set equals
  the cocycle solution set (the iff of Theorem 2(i)) and equals the
  computed `Z₂` gauge orbit of `η^0` (exactly one gauge class,
  Theorem 2(ii)); `−η^0` is verified to be the `ε`-gauge transform
  (Remark R3).
- **C (checks 29–31):** GF(2) cohomology certificate at scale — on the
  `3³`, `4³`, `5³` boxes, the cocycle solutions form the affine space
  `e^0 + ker(d₁)` over GF(2) and gauge orbits are cosets of `im(d₀)`;
  the runner computes `rank(d₁)` by GF(2) elimination and certifies
  `nullity(d₁) = |V| − 1 = rank(d₀)`, hence exactly one gauge class,
  and that `η^0` satisfies every plaquette condition at scale.
- **D (checks 32–45):** falsification legs — the all-plus sign system
  and all 12 single-edge perturbations of `η^0` are *rejected* by the
  transport decision procedure on the unit cube; a flipped interior
  edge on the `4³` box violates the cocycle at scale.
- **E:** a nontrivial `Z₂` gauge transform of `η^0`
  scalarizes and its gauge function is recovered exactly by path
  products (Lemma 4); the `U(1)` leg of Remark R2 (complex local phase
  transform scalarizes; recovery returns the same real representative
  `η^0`), exact sympy.
- **F:** source-boundary firewall — the companion note is checked for
  the 2026-06-13 abstract theorem target and for the absence of
  superseded declared-physical-premise wording.

The runner prints source-boundary lines separating downstream
physical-use gates (B1/B2/B3) from the actual theorem boundary (B4) so
the stdout reflects this row's revised audit target.

## 7. What this does NOT close

- The realization gate itself (carried by the gate note's bounded
  synthesis and its residual list).
- Derivation of the kinetic class from Lattice + Quantum alone: the
  2026-06-12 supply line narrows this downstream physical-use gate, but
  it is not a premise of Theorem 2. P-SD is discharged as a source
  theorem on the `K1` branch, and P-KIN is reduced to the P-FLUX bit
  `phi = -1`; the bit-selection route is conditional on FSB-K plus the
  retained `(Z)` certificate and remains audit-owned for rows that need
  physical realization closure.
- The substep-1 statistics-selection/exhaustiveness residual (B1): this
  remains relevant to realization-gate closure, not to the abstract
  cocycle/gauge classification in this row.
- Rooting / taste reduction: the previous revision's NR claim
  ("retained no-rooting irreducibility" of the Kawamoto-Smit
  realization on `C^8`) is withdrawn from this note's premise set and
  conclusions; any such statement needs its own audited authority and
  is not used or asserted here.
- Boundary-phase / APBC holonomy selection (B4).
- Physical species-label identification (`AC_φλ`).
- Lattice-axis ordering as anything more than coordinate-label gauge.

## 8. What this supports

- Substep 2 (kinetic form, R2) of the staggered-Dirac realization
  gate, once that downstream gate separately supplies the physical
  kinetic-class/scalarization hypotheses: forcing of the Kawamoto-Smit
  phase law, unique as a local `Z₂` gauge class by the Clifford `−1`
  plaquette-cocycle argument, with boundary holonomies/APBC and axis
  ordering as convention data.
- The gauge class is derived by a genuine iff plus exhaustive
  classification (Theorem 2(i)–(ii)), not consistency-checked on a
  single representative.

## 9. Cross-references

- Parent gate (consumes this note as R2; file-path context only, not a
  one-hop authority for this row):
  `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
- Downstream single-mode/statistics context, not a theorem premise:
  [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
- Downstream physical-use context, not theorem premises:
  `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`
  and
  `P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`
- Historical substep-1 source packet:
  `STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`
- Per-site uniqueness (U2):
  [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
- Fermion parity Z₂ grading (F1):
  [`FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md`](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md)
- Standard methodology: Kawamoto, N. & Smit, J. (1981). "Effective
  Lagrangian and dynamical symmetry breaking in strongly coupled
  lattice QCD." Nucl. Phys. B192, 100. — admissible standard
  staggered-fermion construction in narrow non-derivation role.

## 10. Command

```bash
python3 scripts/probe_kawamoto_smit_phase_forcing.py
```

Expected output (deterministic): numbered `[PASS]` lines in sections
A–F as described in §6, including
`exactly 128 = 2^7 admit a site-local unitary scalarization`,
`scalarizable set == Clifford -1 plaquette cocycle solution set`,
`scalarizable set == Z2 gauge orbit of eta^0`,
three GF(2) certificates with `nullity(d1) = |V|-1`,
14 falsification rejections, the Z2 gauge recovery, and the U(1)
generalization check; source-boundary lines recording B1/B2/B3 as
downstream physical-use gates rather than theorem premises, plus B4 as
the simply connected theorem boundary;
then exactly:

```text
TOTAL: PASS=58 FAIL=0
```

Exit code 0 iff FAIL=0.
