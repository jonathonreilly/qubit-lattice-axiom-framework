# Staggered-Dirac Substep 2 — Kawamoto-Smit Phase Forcing

**Date:** 2026-05-07; 2026-06-06 cocycle/gauge-class uniqueness repair;
2026-06-10 science-fix (iff + premise honesty + forcing certificate —
see §0 changelog); 2026-06-11 substep-1 boundary sync; 2026-06-15
bounded-surface hygiene repair
**Type:** bounded_theorem
**Claim scope:** On the supplied local kinetic-scalarization surface —
the naive-Dirac kinetic form on nearest-neighbor `Z³` links (premise
P-KIN) together with a site-local unitary scalarization hypothesis
(premise P-SD) — a nearest-neighbor phase system `η` admits a
site-local unitary scalarization IF AND ONLY IF it satisfies the
Clifford `−1` plaquette cocycle, and on simply connected regions of
`Z³` the solutions form EXACTLY ONE local gauge class: the class of the
Kawamoto-Smit representative `η_1 = 1, η_2(x) = (−1)^{x_1}, η_3(x) =
(−1)^{x_1+x_2}`. This is bounded forcing of the Kawamoto-Smit gauge
class under the declared local premises (boundaries B2–B4 below), not
an unconditional derivation of the kinetic class itself from Lattice +
Quantum alone. The substep-1 single-mode/statistics surface is
downstream realization context, not a premise of this local theorem.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome; audit verdict and effective status
are set only by the independent audit lane.
**Primary runner:** [`scripts/probe_kawamoto_smit_phase_forcing.py`](../scripts/probe_kawamoto_smit_phase_forcing.py)
**Authority role:** source note for substep 2 (kinetic form, R2) of the
staggered-Dirac realization gate
(`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`, parent context
only, not a one-hop authority for this row),
which consumes exactly the bounded statement above ("unique as a local
Z2 gauge class … bounded on the declared kinetic class … the P-SD
surface").

## 0. Changelog

- **2026-06-15 (bounded-surface hygiene repair).** The theorem surface
  is made proof-exact: Lemmas 2--4 use the supplied local
  `P-KIN/P-SD` scalarization surface, the Pauli/Clifford input, and
  the `Z³` box topology. The substep-1 Grassmann/statistics packet is
  retained as downstream realization context for gate consumers, but
  it is no longer listed as a theorem premise or a load-bearing
  dependency for the local Kawamoto-Smit gauge-class result. No
  kinetic-class derivation or status promotion is claimed.
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
     premise." That prose is withdrawn: the naive-Dirac kinetic form
     (P-KIN) and the site-local unitary diagonalization (P-SD) are now
     declared, named premises (boundaries B2, B3). The single-mode
     surface motivates P-SD (one Grassmann mode per dim-2 site module
     leaves no room for a 2-component spinor) but the precise exclusion
     bridge is open and is carried by the gate note's residual list,
     not silently assumed here.
  4. *(Medium — unjustified `η ∈ {±1}`.)* The old derivation assumed
     sign-valued phases without justification. Fixed: Remark R2 — the
     entire argument runs verbatim with `U(1)`-valued phases, giving
     uniqueness up to local `U(1)` gauge with the same real
     representative `η^0` (runner check 47).
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
  two-candidate comparison. This note's B1 language is synchronized to
  that current boundary. No kinetic-class derivation is added here:
  P-KIN and P-SD remain declared premises. The 2026-06-15 hygiene
  repair below further narrows B1 from theorem premise to downstream
  realization context.
- **2026-06-12 (kinetic supply-line sync).** Current main now contains
  a sharper source-side supply line for this note's former B2/B3
  residuals. `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`
  proves a two-flux-class collapse on the licensed nearest-neighbor
  bilinear surface and discharges P-SD as an absorbing-frame theorem on
  the flux-`-1` branch; it leaves exactly the P-FLUX bit
  `phi = -1` as the P-KIN residual. `P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`
  then composes the retained `(Z)` geometry certificate with the FSB-K
  thermal row as a conditional selector for that bit. This sync does
  not change this row's current audit status and does not claim
  retained closure: the kinetic-class and P-FLUX supplier rows are
  still audit-owned, and the P-FLUX selection is conditional on FSB-K's
  audit grade.
- **2026-06-06.** Cocycle/gauge-class uniqueness repair (necessity +
  classification; superseded in form by Lemmas 2 and 4 below).
- **2026-05-07.** Original substep-2 note.

## 1. Question

On the supplied local kinetic-scalarization surface (P-KIN + P-SD), is
the staggered kinetic operator's phase structure forced to be the
Kawamoto-Smit law, and in exactly what sense "forced"?

## 2. Answer (bounded)

**Within the declared kinetic class, yes — as an iff plus an exhaustive
classification.** A phase system on nearest-neighbor `Z³` links admits
a site-local unitary scalarization if and only if it satisfies the
Clifford `−1` plaquette cocycle (Theorem 2(i), Lemmas 2 + 3), and on
simply connected regions the cocycle solutions form exactly one local
gauge class — the class of

```
η_1(x) = 1
η_2(x) = (−1)^{x_1}
η_3(x) = (−1)^{x_1 + x_2}
```

(Theorem 2(ii), Lemma 4). What is NOT claimed: that the kinetic class
itself (P-KIN, P-SD) is forced by Lattice + Quantum alone — those are declared premises
with named boundaries below. This is exactly the bounded statement the
realization-gate note consumes as its R2 authority.

## 3. Boundaries (the bounded surface, stated up front)

| ID | Boundary | Where it bites |
|---|---|---|
| B1 | Downstream realization context: the substep-1 single-mode/statistics surface motivates why gate consumers want P-SD, but it is not a premise of Lemmas 2--4 or Theorem 2 in this row | does not bite inside the local Kawamoto-Smit proof; remains a downstream gate-residual context |
| B2 | P-KIN: the naive-Dirac kinetic form `D = Σ_μ γ_μ ⊗ ∂_μ` on nearest-neighbor `Z³` links is a declared premise; non-nearest-neighbor or non-Dirac kinetic operators are not excluded here | Theorem 2 quantifies over phase systems *within* this class only |
| B3 | P-SD: a *site-local unitary* scalarization `T(x)` is supplied; alternatives that bypass spin diagonalization (for example a 2-component naive operator) are outside this local theorem unless separately mapped into P-SD | the scalarization condition (4) is the P-SD premise in equation form |
| B4 | Finite tori carry extra holonomy data: signs around non-contractible cycles (PBC/APBC and wrap-sign conventions) are boundary convention data, not local phase law; likewise lattice-axis permutation is coordinate-label gauge | Theorem 2(ii) is stated on simply connected regions |

### 3.1 2026-06-12 kinetic supply-line status

The B2/B3 boundary is now sharper than the original declared-premise
wording. This subsection is **not** a load-bearing dependency edge for
the theorem in this row: it is a source-side roadmap for future premise
retirement. The claim audited here remains only the local iff/gauge-class
theorem under the supplied `P-KIN` and `P-SD` hypotheses stated in B2/B3.
Independent audit of the supplier rows is not required to audit this
bounded local theorem on its supplied kinetic surface.

| former boundary | current source-side supplier | current honest status |
|---|---|---|
| P-SD site-local absorbing frame | `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`; runner cache `staggered_dirac_kinetic_class_forcing_check_2026_06_10.txt` (`TOTAL: PASS=27 FAIL=0`) | discharged as a theorem on the flux-`-1` branch, pending independent audit of that supplier |
| P-KIN broad kinetic-class declaration | same kinetic-class forcing note | reduced to exactly two licensed frame classes, `K0` with flux `+1` and `K1` with flux `-1`; the surviving residual is the one-bit P-FLUX selector |
| P-FLUX selector `phi = -1` | `P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`; runner cache `p_flux_selection_via_fsb_k_check_2026_06_11.txt` (`TOTAL: PASS=16 FAIL=0`) | conditional on FSB-K's audit grade, using the retained `(Z)` kernel-geometry certificate; no selection is performed at current grades |

Future stronger re-audit that wants to retire `P-KIN/P-SD` should treat
this row's B2/B3 residual as a source-side cascade:

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

This row remains a bounded theorem on supplied `P-KIN/P-SD` unless that
cascade is accepted by the independent audit lane. The local
Kawamoto-Smit phase-forcing proof below still states its theorem under
the `P-KIN/P-SD` class because that is the exact local hypothesis. The
supply-line section records the current route for retiring those
hypotheses, not a branch-local status promotion and not a dependency
required for this row's bounded local closure.

## 4. Setup

### 4.1 Premises

| ID | Statement | Class |
|---|---|---|
| Quantum | one-qubit local algebra, equivalently `M_2(C) ~= Cl(3,0)`, with Pauli realization per site | accepted axiom premise |
| Lattice | `Z³` nearest-neighbor lattice | accepted axiom premise |
| U2 | Per-site faithful Cl(3) irrep of dim 2; central pseudoscalar `ω = γ₁γ₂γ₃` | per [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md) |
| F1 | Z₂ fermion-parity grading | per [`FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md`](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md) |
| BPG | `Z³` nearest-neighbor graph is bipartite | admissible standard math (graph theory) |
| P-KIN | Naive-Dirac kinetic form on nearest-neighbor links | DECLARED premise (B2) |
| P-SD | Site-local unitary spin diagonalization | DECLARED premise (B3) |

P-KIN + P-SD together are what the realization-gate note calls "the
declared kinetic class (the P-SD surface)". The 2026-06-06 revision's
NR premise ("retained no-rooting irreducibility") is removed: it was
cited via a script outside the one-hop packet and was load-bearing
nowhere in the derivation.

The substep-1 single-mode/statistics packet is downstream context for
staggered-realization consumers. It is not used in Lemmas 2--4: once
P-SD is supplied, the proof is the local Pauli/lattice transport
calculation below.

### 4.2 Forbidden imports

- NO PDG values, NO lattice MC values, NO fitted coefficients
- NO new axioms (no-new-axiom rule)

### 4.3 The scalarization condition

Under P-KIN the kinetic operator is `D = Σ_μ γ_μ ⊗ ∂_μ` with `∂_μ` the
symmetric lattice difference. P-SD supplies the site-local unitary
scalarization map `T(x)` per site, `χ(x) := T(x) ψ(x)`, with the
**scalarization condition**

```
T†(x) γ_μ T(x + μ̂) = η_μ(x) · I_2                                       (4)
```

where the phases `η_μ(x)` are a priori `U(1)`-valued (Remark R2); the
sign-valued case `η_μ(x) ∈ {±1}` is the real representative.

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

**On Quantum + Lattice + U2 + F1 + BPG, within the declared kinetic
class P-KIN (B2) + P-SD (B3):**

**(i)** A nearest-neighbor phase system `η` (`Z₂`- or `U(1)`-valued)
admits a site-local unitary scalarization (4) **if and only if** it
satisfies the Clifford `−1` plaquette cocycle (8). [Lemmas 2 + 3]

**(ii)** On simply connected regions of `Z³`, the solution set of (8)
is **exactly one** local gauge class, the class of the Kawamoto-Smit
representative `η^0` of (6); a canonical solution of (4) is
`T(x) = γ_1^{x_1} γ_2^{x_2} γ_3^{x_3}` (on the Pauli realization,
`T(x) = σ_1^{x_1} σ_2^{x_2} σ_3^{x_3}`). [Lemma 4]

Hence the staggered kinetic operator

```
D_staggered = (1/2) Σ_{x, μ} η_μ(x) · (χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂})
```

carries the Kawamoto-Smit phase law uniquely as a local gauge class, up
to finite-boundary holonomy/APBC convention data and lattice-axis
permutation gauge (B4). ∎

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
  representative** `η^0`. Runner check 47 verifies this exactly
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
second. 47 checks in five sections; this is a *forcing certificate*,
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
- **E (checks 46–47):** a nontrivial `Z₂` gauge transform of `η^0`
  scalarizes and its gauge function is recovered exactly by path
  products (Lemma 4); the `U(1)` leg of Remark R2 (complex local phase
  transform scalarizes; recovery returns the same real representative
  `η^0`), exact sympy.

The runner prints the declared-open P-KIN/P-SD and B4 residuals, plus a
`CONTEXT (not theorem premise): ...` line for the substep-1
single-mode/statistics surface, so the bounded local theorem is not
mistaken for an unconditional realization-gate closure.

## 7. What this does NOT close

- The realization gate itself (carried by the gate note's bounded
  synthesis and its residual list).
- Derivation of the kinetic class from Lattice + Quantum alone: the
  2026-06-12 supply line narrows this residual but does not remove it
  at this row's current grade. P-SD is discharged as a source theorem
  on the `K1` branch, and P-KIN is reduced to the P-FLUX bit
  `phi = -1`; the bit-selection route is conditional on FSB-K plus the
  retained `(Z)` certificate and remains audit-owned.
- The substep-1 statistics-selection/exhaustiveness residual (B1) for
  downstream gate consumers. It is not part of this local theorem's
  proof, but it still blocks any claim that the full staggered
  realization gate is unconditionally closed.
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
  gate, at exactly the strength the gate note cites: forcing of the
  Kawamoto-Smit phase law, unique as a local `Z₂` gauge class by the
  Clifford `−1` plaquette-cocycle argument, bounded on the declared
  kinetic class (P-KIN + P-SD), with boundary holonomies/APBC and axis
  ordering as convention data.
- The gauge class is derived by a genuine iff plus exhaustive
  classification (Theorem 2(i)–(ii)), not consistency-checked on a
  single representative.

## 9. Cross-references

- Parent gate (consumes this note as R2; file-path context only, not a
  one-hop authority for this row):
  `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
- Substep-1 Grassmann/statistics packet (downstream context only, not a
  theorem premise for this row): the retained two-candidate
  single-mode note from 2026-05-16
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

Expected output (deterministic): 47 numbered `[PASS]` lines in
sections A–E as described in §6, including
`exactly 128 = 2^7 admit a site-local unitary scalarization`,
`scalarizable set == Clifford -1 plaquette cocycle solution set`,
`scalarizable set == Z2 gauge orbit of eta^0`,
three GF(2) certificates with `nullity(d1) = |V|-1`,
14 falsification rejections, the Z2 gauge recovery, and the U(1)
generalization check; two `RESIDUAL (declared-open): ...` lines
(B2/B3 kinetic-class premises and B4 holonomy) plus one
`CONTEXT (not theorem premise): ...` line for B1; then exactly:

```text
TOTAL: PASS=47 FAIL=0
```

Exit code 0 iff FAIL=0.
