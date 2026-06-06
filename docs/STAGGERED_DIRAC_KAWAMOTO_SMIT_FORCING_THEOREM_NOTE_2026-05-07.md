# Staggered-Dirac Substep 2 — Kawamoto-Smit Phase Forcing (Block 03)

**Date:** 2026-05-07; 2026-06-06 cocycle/gauge-class uniqueness repair
**Type:** bounded support theorem
**Claim type:** bounded_theorem
**Status:** bounded source support for substep 2 (Kawamoto-Smit phase
forcing) of the staggered-Dirac realization gate. Conditional on the
current substep-1 Grassmann narrow theorem for the single-mode
Grassmann-vs-bosonic two-candidate surface, the per-site Pauli
realization (U2), Z³ bipartite-graph parity (A2 + admissible standard
math), and the Cl(3) chirality central pseudoscalar (U2). Derives the unique
Kawamoto-Smit phase gauge class η_1=1, η_2(n)=(−1)^{n_1},
η_3(n)=(−1)^{n_1+n_2} from spin-diagonalization forced by
single-mode Grassmann (Block 02) + Clifford anticommutation. The
2026-06-06 repair narrows "unique" to the exact local Z2 gauge class
on the simply connected Z³ nearest-neighbor graph; finite-boundary
holonomies/APBC phases remain boundary convention data. This note does
not assert an audit-ratified effective status.
**Authority role:** source note. Audit verdict and effective status are
set only by the independent audit lane.
**Primary runner:** [`scripts/probe_kawamoto_smit_phase_forcing.py`](../scripts/probe_kawamoto_smit_phase_forcing.py)

## Question

Given Block 02 (Grassmann partition forcing) — the matter measure is
the single-mode Grassmann partition with (χ_x, χ̄_x) per site — does
A1+A2 plus the cited support chain force the kinetic operator to take the
specific staggered form with Kawamoto-Smit phases?

## Answer

**Yes — the Kawamoto-Smit phase gauge class is forced** (up to local
Z2 gauge, coordinate permutation, and finite-boundary holonomy
conventions) by:

1. Substep-1 Grassmann narrow theorem: matter is single-mode
   Grassmann on the two-candidate finite-generator surface, hence the
   per-site Hilbert dim 2 carries a single fermion mode (not a
   2-component spinor)
2. A2 (Z³) + bipartite-graph parity: sublattice parity
   `ε(x) := (−1)^{x_1+x_2+x_3}` is forced
3. Cl(3) chirality central pseudoscalar `ω = γ_1 γ_2 γ_3` (per U2):
   per-site chirality grading
4. Chirality anticommutation `{ε, D_staggered} = 0` (forced by site-
   chirality assignment + retained no-rooting irreducibility)
5. Spin-diagonalization on Pauli per-site (forced by single-mode
   Grassmann)

Solving the resulting constraints gives:

```
η_1(n) = 1
η_2(n) = (−1)^{n_1}
η_3(n) = (−1)^{n_1 + n_2}
```

up to global gauge equivalence (overall sign + boundary-phase choices).

## Setup

### Premises (A_min for substep 2)

| ID | Statement | Class |
|---|---|---|
| A1 | Cl(3) local algebra, Pauli realization per-site | retained axiom |
| A2 | Z³ spatial substrate | retained axiom |
| BlockT1 | Matter measure is single-mode Grassmann (χ_x, χ̄_x) per site | Block 02 forcing theorem |
| U2 | Per-site faithful Cl(3) irrep dim 2; central pseudoscalar ω = γ₁γ₂γ₃ | retained per `AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29` (chirality repair) |
| F1 | Z₂ fermion-parity grading retained | per `FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02` |
| NR | No proper Cl(3)-preserving taste projection on irreducible C^8 | per `frontier_generation_rooting_undefined.py` |
| BPG | Bipartite-graph parity: Z³ has natural Z_2 sublattice structure | admissible standard math (graph theory) |

### Forbidden imports

- NO PDG values, NO lattice MC values, NO fitted coefficients
- NO new axioms (no-new-axiom rule)

## Derivation

### Step 1: Sublattice parity ε(x) is forced

Z³ as a graph (with edges = nearest-neighbor links) is **bipartite**.
The two sublattices A and B are defined by:

```
A = {x ∈ Z³ : x_1 + x_2 + x_3 ≡ 0 (mod 2)}
B = {x ∈ Z³ : x_1 + x_2 + x_3 ≡ 1 (mod 2)}
```

The bipartite-graph parity assigns a Z_2 charge to each vertex:

```
ε(x) := (−1)^{x_1 + x_2 + x_3}                                              (1)
```

By A2 + admissible standard graph theory, ε(x) is the unique
non-trivial Z_2 grading on Z³ that's invariant under all lattice
translations modulo their parity.

### Step 2: Cl(3) chirality grading per site

By U2 (Cl(3) per-site uniqueness, chirality-aware repair 2026-05-03),
the central pseudoscalar `ω = γ_1 γ_2 γ_3` squares to `−I` (Euclidean
signature) and is central in Cl(3). On the Pauli realization
`γ_i = σ_i`:

```
ω = σ_1 σ_2 σ_3 = i · I (positive chirality) or -i · I (negative chirality)  (2)
```

So per-site chirality is `±i`, fixed by the choice of irrep (positive
vs negative). Either choice gives a per-site chirality eigenvalue.

### Step 3: Sublattice-parity / chirality identification

The framework assigns chirality to sites by combining:
- Sublattice parity ε(x) ∈ {+1, −1} (geometric, from Step 1)
- Per-site Cl(3) chirality eigenvalue (algebraic, from Step 2)

The natural identification: assign chirality `ω(x) = ε(x) · ω_global`
to each site, where `ω_global = +i` (canonical positive chirality).
Site x has chirality eigenvalue `+i` if x ∈ A, `−i` if x ∈ B.

This identification is the framework-internal staggered chirality
grading. It is consistent with F1 (Z_2 fermion-parity grading
retained) and is forced (up to global sign) by:
- The sublattice structure from A2 (Step 1)
- The per-site Cl(3) chirality (Step 2)
- Standard bipartite-graph + Z_2-grading assignment

### Step 4: Spin-diagonalization is forced

By BlockT1 (the substep-1 Grassmann narrow theorem on the
two-candidate finite-generator surface), the matter measure has a
single Grassmann mode per site, occupying the 2-dim per-site Hilbert
space. The Pauli realization `γ_i = σ_i` would, naively, give a
2-component spinor field per site. But by BlockT1, the per-site dim
2 must carry a single fermion mode (`a = σ_+, a^† = σ_-, n = (I − σ_3)/2`
per F1 / `FERMION_PARITY_Z2_GRADING_THEOREM`), not a 2-component
spinor.

Therefore the spin-1/2 structure must be ABSORBED — diagonalized away
into local phases — via a unitary spin-rotation `T(x)` at each site:

```
χ(x) := T(x) ψ(x)                                                          (3)
```

where ψ is the formal 2-component spinor on Pauli per-site, and χ is
the resulting single-mode Grassmann field after diagonalization.

The diagonalization condition is that the kinetic operator
`D = Σ_μ γ_μ ⊗ ∂_μ` (where ∂_μ is the symmetric lattice difference
on Z³) becomes spin-diagonal under T. Specifically:

```
T^†(x) γ_μ T(x + μ̂) = η_μ(x) · I_2                                         (4)
```

where η_μ(x) ∈ {+1, −1} are the Kawamoto-Smit phases.

### Step 5: Solving for T(x) and η_μ(x)

The constraint (4) is a finite linear-algebra problem. A canonical
representative is

```
T(x) = γ_1^{x_1} · γ_2^{x_2} · γ_3^{x_3}                                    (5)
```

For the Pauli realization `γ_i = σ_i`, this is:

```
T(x) = σ_1^{x_1} · σ_2^{x_2} · σ_3^{x_3}                                    (5')
```

Substituting (5) into (4) and using `σ_μ σ_ν = δ_{μν} I + i ε_{μνρ} σ_ρ`
(Pauli algebra) gives:

```
η_1(x) = 1
η_2(x) = (−1)^{x_1}
η_3(x) = (−1)^{x_1 + x_2}                                                    (6)
```

These ARE the Kawamoto-Smit phases.

### Step 6: Cocycle uniqueness up to gauge

This repair supplies the missing uniqueness argument. Suppose another
spin diagonalization `(T', η')` satisfies the scalarization condition
(4), with `γ_μ^2 = I` and `γ_μ γ_ν = -γ_ν γ_μ` for `μ != ν`. From (4),

```text
    T'(x + μ̂) = η'_μ(x) γ_μ T'(x).                                      (7)
```

Going from `x` to `x+μ̂+ν̂` along the two elementary paths gives

```text
    η'_ν(x + μ̂) η'_μ(x) γ_ν γ_μ T'(x)
      = η'_μ(x + ν̂) η'_ν(x) γ_μ γ_ν T'(x).
```

Since `γ_ν γ_μ = -γ_μ γ_ν`, every admissible phase system must obey the
Clifford `-1` plaquette cocycle

```text
    η'_ν(x + μ̂) η'_μ(x)
      = - η'_μ(x + ν̂) η'_ν(x).                                       (8)
```

The canonical phases (6) obey (8): for `μ < ν`, shifting by `μ`
flips `η_ν` and shifting by `ν` does not flip `η_μ`; the other order is
the same equation with `μ,ν` exchanged.

Now let `η^0` denote the canonical representative (6), and set
`r_μ(x)=η'_μ(x)η^0_μ(x)`. Because both `η'` and `η^0` obey the same
`-1` cocycle, `r` has trivial plaquette cocycle:

```text
    r_ν(x + μ̂) r_μ(x) = r_μ(x + ν̂) r_ν(x).                            (9)
```

On the simply connected `Z³` nearest-neighbor graph, every such closed
Z2 one-cochain is exact. Choose `g(0)=1` and define `g(x)` by the path
product of `r` from `0` to `x`; (9) gives path independence. Then

```text
    η'_μ(x) = g(x) η^0_μ(x) g(x + μ̂).                                  (10)
```

So any admissible local phase system is a Z2 gauge transform of the
canonical Kawamoto-Smit phases. Conversely, if `η'` has the form (10)
and `T'(x)=g(x)T(x)`, then (4) holds with `η'`. Thus the local
Kawamoto-Smit phase law is unique as a gauge class.

Finite tori can also carry global holonomy signs around non-contractible
cycles. Those are the boundary-phase/APBC choices named in this note,
not additional local phase laws. Lattice-axis permutations give the
same statement after relabeling the coordinate order.

The retained no-rooting irreducibility result NR (per
`frontier_generation_rooting_undefined.py`) confirms that no further
projection / rooting / reduction of the Kawamoto-Smit gamma realization
on C^8 (the full taste-cube space) is consistent with Cl(3)-preserving
Hamiltonian dynamics on Z³. So the irreducibility on C^8 of the
Kawamoto-Smit construction is retained; the new content of this
Block 03 is the forcing of the gauge class (6) from A1+A2 plus the
substep-1 single-mode Grassmann surface under the spin-diagonalization
premise.

QED.

## Theorem 2 (Kawamoto-Smit phase forcing)

**Bounded theorem.** On A1+A2 + substep-1 single-mode Grassmann
support + U2, F1, NR plus admissible standard graph theory:

```
The staggered-Dirac kinetic operator on Z³ has the unique local
phase gauge class

    D_staggered = (1/2) Σ_{x, μ} η_μ(x) · (χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂})

with Kawamoto-Smit phases

    η_1(x) = 1, η_2(x) = (−1)^{x_1}, η_3(x) = (−1)^{x_1+x_2}.

Up to local Z2 gauge + finite-boundary holonomy/APBC choices +
lattice-axis permutation gauge, this is the unique phase structure
consistent with the cited framework primitive stack and the
spin-diagonalization premise.
```

**Proof.** Steps 1-6 above. ∎

## Audit boundary

This note should seed as `bounded_theorem`. It does not write an audit
verdict, an effective status, or a retained-grade closure claim. Any later
retained-grade use must wait for independent audit of this note and its
dependency chain.

## What this supports

- Substep 2 of staggered-Dirac realization gate (Kawamoto-Smit phase
  forcing) as bounded theorem support
- Explicit forcing chain from A1+A2 + Grassmann support + cited primitives
- Unique η_μ(x) gauge class derived by the Z2 cocycle argument, not
  just consistency-checked

## What this does NOT close

- The gate itself
- Physical species-label identification (`AC_φλ`)
- Boundary-phase / APBC holonomy selection
- Lattice-axis ordering as anything more than coordinate-label gauge

## Cross-references

- Parent open-gate: [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- Substep-1 Grassmann narrow theorem:
  [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
- Historical Block 02 source packet:
  `STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`
- Per-site uniqueness: [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
- Fermion parity Z_2 grading: [`FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md`](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md)
- No-rooting irreducibility: `scripts/frontier_generation_rooting_undefined.py`
- Standard methodology: Kawamoto, N. & Smit, J. (1981). "Effective Lagrangian and dynamical symmetry breaking in strongly coupled lattice QCD." Nucl. Phys. B192, 100. — admissible standard staggered-fermion construction in narrow non-derivation role.

## Command

```bash
python3 scripts/probe_kawamoto_smit_phase_forcing.py
```

Expected output: explicit verification that
`T(x) = σ_1^{x_1} σ_2^{x_2} σ_3^{x_3}` applied via (4) gives
Kawamoto-Smit phases (6), that the phases obey the Clifford `-1`
plaquette cocycle, that gauge-transformed phases recover to the
canonical representative on simply connected finite boxes, and that
the invalid all-plus sign law is rejected.
