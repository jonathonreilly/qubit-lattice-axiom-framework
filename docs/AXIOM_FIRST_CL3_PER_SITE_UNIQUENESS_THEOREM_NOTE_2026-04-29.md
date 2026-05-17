# Axiom-First Per-Site Uniqueness of the Cl(3) Spinor Module

**Date:** 2026-04-29 (originally); 2026-05-03 (review-loop repair); 2026-05-08 (narrowed to physical-Cl(3)-only U1–U3 to break cycle)
**Status:** support — branch-local theorem note on the physical `Cl(3)` local algebra alone. Runner passing on all six exhibits. Queued for independent audit at the narrowed physical-Cl(3)-only scope.
**Claim type:** bounded_theorem
**Loop:** `axiom-first-foundations`
**Cycle:** 6 (Route R6)
**Runner:** `scripts/axiom_first_cl3_per_site_uniqueness_check.py`
**Log:** `outputs/axiom_first_cl3_per_site_uniqueness_check_2026-04-29.txt`

## Audit scope (2026-05-08 narrowing)

This note is now restricted to the **physical-Cl(3)-only** content
(U1, U2, U3) — the abstract real-algebra classification of `Cl(3,0)`
and its complex chirality irreps. The earlier U4 statement ("per-site
Hilbert space has dimension exactly 2 on the explicit framework
baseline") has been **moved out of scope of this note** because its
bridge from the abstract 2-dim Cl(3) chirality module to the physical
per-site Hilbert space depends on the staggered-Dirac/Grassmann
realization input. That realization bridge is carried by the
staggered-Dirac realization gate,
specifically substep 1
(`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`).

The 2026-05-08 review separated the U1–U3 physical-Cl(3)-only
classification from the staggered-Dirac/Grassmann-dependent U4
realization step. Narrowing to U1–U3 makes this row auditable without
the staggered-Dirac gate cycle and lets the substep 1 note carry the
realization-dependent U4 conclusion separately.

The narrowed claim_scope is therefore:

> **Per-site uniqueness of the Cl(3) spinor module (physical `Cl(3)`
> local algebra only):** the
> abstract real Clifford algebra `Cl(3,0)` admits exactly two
> non-isomorphic faithful complex irreducible representations
> (positive- and negative-chirality), each 2-dim, distinguished by
> the central pseudoscalar eigenvalue `ω → ±i`; every finite-dim
> complex representation decomposes as a direct sum of these two
> irreps.

## Review-loop repair (2026-05-03)

The original Step 1 misidentified `Cl(3) ⊗_R C` as `M_2(C)` by halving
the tensor-product dimension and ignoring the odd-complex-Clifford
split. The 2026-05-03 review follow-up identified this as the
load-bearing error: U2 and U3 relied on simplicity and unique
irreducibility of `M_2(C)`, but the correct complexification is
`M_2(C) ⊕ M_2(C)` (two simple summands distinguished by the central
pseudoscalar `ω = γ_1 γ_2 γ_3` taking eigenvalue `+i` or `-i`), so
there are **two** non-isomorphic 2-dim faithful complex irreps, not
one.

This repair:

- Replaces Step 1 with the correct identification: `Cl(3,0) ≅ M_2(C)`
  as a **real** algebra (real-dim 8 = real-dim of `M_2(C)`).
- Adds an explicit Step 2 on the central pseudoscalar `ω`,
  showing `ω² = -1` and `ω central` in `Cl(3)`.
- Adds an explicit Step 3 deriving the complexification
  `Cl(3) ⊗_R C ≅ M_2(C) ⊕ M_2(C)`, with the two summands indexed
  by the central character `ω = ±i`.
- Restates U2 as uniqueness-within-chirality: any faithful irreducible
  complex representation of `Cl(3)` has dimension exactly 2 and is
  unitarily equivalent **either** to the canonical positive-chirality
  Pauli irrep `ρ_+(γ_i) = σ_i` (`ω → +i`) **or** to its
  parity-conjugate negative-chirality irrep
  `ρ_-(γ_i) = -σ_i` (`ω → -i`). The two are not unitarily equivalent.
- Restates U3 to allow either chirality in the decomposition:
  every finite-dim complex Cl(3) representation is a direct sum
  of `n_+` copies of `ρ_+` and `n_-` copies of `ρ_-`, with total
  dim `2(n_+ + n_-)`.
- Preserves U4 (per-site Hilbert dim = 2): the dimensional
  conclusion holds in both chirality summands, so per-site Hilbert
  dim = 2 is independent of the chirality choice.
- Acknowledges that U4 uses the staggered-Dirac/Grassmann realization
  input (one Grassmann pair per site →
  2-dim Fock space) for the Cl(3)-irrep-to-Hilbert-space bridge,
  not the physical `Cl(3)` local algebra alone. The hypothesis set is
  updated accordingly.

The canonical convention adopted in the rest of the package
(`γ_i = σ_i`, `ω = +i`) corresponds to the positive-chirality
summand. Downstream consumers that depend only on per-site Hilbert
dim = 2 (notably the spin-statistics chain) are unaffected; consumers
that assume "the unique 2-dim Cl(3) irrep" need to be aware of the
chirality choice.

## Historical context (2026-05-03 second pass — staggered-Dirac/Grassmann bridge gate; superseded by 2026-05-08 narrowing)

> **Status note (2026-05-17 audited_conditional repair):** This subsection
> is retained for historical context only. It describes a U4 closure path
> via the staggered-Dirac realization gate that was *moved out of this
> note's scope* by the 2026-05-08 narrowing to U1–U3
> (physical-Cl(3)-only). The
> staggered-Dirac gate is therefore **not** a one-hop cited authority of
> the present physical-Cl(3)-only audit packet. All references to
> `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` and
> `STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md` below
> appear backticked-only as non-load-bearing metadata; see the explicit
> citation-graph statement in §"Audit dependency scoping (2026-05-17)".

The 2026-05-03 review follow-up identified a remaining scope gate:
U4's "one-Grassmann-pair staggered-fermion normalization" used to
identify the abstract 2-dim Cl(3) chirality module with the physical
per-site Hilbert space chains through the staggered-Dirac/Grassmann
realization input, but the current canonical
minimal-input surface
[`MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md)
places the staggered/Grassmann realization outside the physical `Cl(3)`
local algebra plus `Z^3` spatial substrate primitive kernel.

The historical repair (now superseded): cite the open-gate authority
for the staggered-Dirac realization rather than treat the
staggered-Dirac/Grassmann realization input as primitive. The
historical citation target was
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (backticked here
as non-load-bearing metadata under the 2026-05-08 narrowed scope).

**Status of U4 under the 2026-05-08 narrowing:**
- **U2, U3** (the abstract Cl(3) representation classification with
  chirality split) load-bear on the physical `Cl(3)` local algebra only
  and remain unconditional.
- **U4** (per-site Hilbert dim = 2 on the **physical** lattice) has been
  moved out of this note's audited scope as of the 2026-05-08 narrowing;
  the staggered-Dirac/Grassmann bridge content is now carried by substep
  1 of the staggered-Dirac realization gate
  (`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`)
  rather than by this note. That citation appears backticked-only here as
  non-load-bearing metadata.

The runner still PASS=6/6 on the physical-Cl(3)-only U1–U3 algebraic content; the
out-of-scope U4 references do not affect runner-level verification of
the audited claim or the publication-facing retention status of this
physical-Cl(3)-only packet.

## Scope

Cycle 1's spin-statistics theorem load-bears on the *finite-
dimensionality* of the per-site Cl(3) module: the minimal complex
spinor irrep of Cl(3) is dim 2, hence per-site Hilbert space is dim
2, hence bosonic CCR `[a, a^†] = I` is impossible per site. This
note discharges the "minimal complex spinor irrep is dim 2" step
into an explicit Stone–von Neumann–style uniqueness theorem for
Cl(3) representations: any faithful irreducible representation of
Cl(3) on a finite-dimensional complex vector space has dimension
exactly 2 and is unitarily equivalent to the canonical Pauli
representation `γ_i = σ_i`.

After this note, Cycle 1's Step 2 argument is closed at the
representation-theoretic level: per-site Hilbert dim = 2 is a
theorem, not a stipulation.

## Explicit framework object in use

- **Physical `Cl(3)` local algebra.** Used as the canonical real
  Clifford algebra with three generators `γ_1, γ_2, γ_3` satisfying

  ```text
      { γ_i ,  γ_j }   :=   γ_i γ_j  +  γ_j γ_i   =   2 δ_{ij} · I.    (1)
  ```

  No other explicit-framework-baseline ingredient is used in this note.

## Statement

Let `Cl(3)` be the real Clifford algebra defined by (1).

**(U1) Existence.** The Pauli matrices `σ_1, σ_2, σ_3` satisfy
(1) on `C²`. Hence there is at least one faithful irreducible
representation of Cl(3) on a 2-dim complex vector space.

**(U2) Uniqueness within chirality.** Any faithful irreducible
representation `ρ : Cl(3) → End(V)` on a finite-dim complex vector
space `V` satisfies `dim_C V = 2`, and the central pseudoscalar
`ω = γ_1 γ_2 γ_3` acts as a scalar `ω(ρ) = ε i` on `V` with
`ε ∈ {+1, -1}` fixed by `ρ`. Up to unitary equivalence there are
exactly two such irreps:

- the positive-chirality irrep `ρ_+(γ_i) = σ_i` (so `ω → +i`);
- the negative-chirality irrep `ρ_-(γ_i) = -σ_i` (so `ω → -i`).

Within each chirality summand, there is a unitary `U ∈ U(2)` such
that `U^{-1} ρ(γ_i) U = ε σ_i` for all `i`. The two chiralities are
**not** unitarily equivalent (they have different `ω`-eigenvalues).
The canonical convention adopted in the package is the
positive-chirality summand `ρ_+`.

**(U3) Decomposition.** Any finite-dim complex representation of
Cl(3) decomposes as a direct sum of copies of the two chirality
irreps:

```text
    V   =   ρ_+^{n_+}  ⊕  ρ_-^{n_-}                                  (2)
```

with `dim_C V = 2(n_+ + n_-)`. There is no faithful representation
of Cl(3) on a complex vector space of odd dimension. Under the
canonical positive-chirality convention only the `ρ_+` summand is
populated and the decomposition reduces to `n_+` copies of the
Pauli irrep.

**(U4 — out of scope of this note as of 2026-05-08.)** The
per-site Hilbert dimension conclusion on the explicit framework
baseline (combining (U2) with the one-Grassmann-pair-per-site
canonical normalisation supplied by the staggered-Dirac/Grassmann
realization input) is NOT a theorem of this note. It is downstream
content carried by the staggered-Dirac realization gate's substep 1
(`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`).
Downstream cycles (spin-statistics, RP, cluster, CPT) that need
the per-site dim = 2 conclusion should cite that substep, not
this note.

## Proof

The proof is the standard real-algebra classification of `Cl(3,0)`,
together with the explicit complexification splitting and Schur's
lemma in each chirality summand.

### Step 1 — `Cl(3,0) ≅ M_2(C)` as a real algebra

The relations (1) generate `Cl(3,0)` as a real algebra of dimension
`2³ = 8` (basis: `1, γ_1, γ_2, γ_3, γ_1γ_2, γ_1γ_3, γ_2γ_3, γ_1γ_2γ_3`).
The map

```text
    γ_1  ↦  σ_1,    γ_2  ↦  σ_2,    γ_3  ↦  σ_3                     (3)
```

extends to a real-algebra homomorphism `Cl(3,0) → M_2(C)`. The
image contains `σ_i, σ_iσ_j = i ε_{ijk} σ_k, σ_1σ_2σ_3 = i I, I`,
which span `M_2(C)` over `R` (`M_2(C)` has real-dim 8 = `dim_R Cl(3,0)`),
so the map is a real-algebra isomorphism. **Note that the codomain
is treated as a real algebra here**; the natural complex structure
on `M_2(C)` corresponds to multiplication by `ω = γ_1γ_2γ_3` (which
acts as `i I` under (3); see Step 2).

### Step 2 — central pseudoscalar `ω` with `ω² = -1`

Define `ω := γ_1 γ_2 γ_3 ∈ Cl(3)`. Direct calculation using (1):

```text
    ω²  =  γ_1 γ_2 γ_3 γ_1 γ_2 γ_3
        =  γ_1 γ_2 (-γ_1 γ_3) γ_2 γ_3        (γ_3γ_1 = -γ_1γ_3)
        =  -γ_1 (-γ_1 γ_2) γ_3 γ_2 γ_3       (γ_2γ_1 = -γ_1γ_2)
        =  γ_1² γ_2 γ_3 γ_2 γ_3
        =  γ_2 (-γ_2 γ_3) γ_3                (γ_3γ_2 = -γ_2γ_3)
        =  -γ_2² γ_3²
        =  -1.                                                       (4)
```

Centrality: `ω γ_i = γ_i ω` for `i = 1,2,3`. Direct computation:
e.g. `ω γ_1 = γ_1 γ_2 γ_3 γ_1 = γ_1 γ_2 (-γ_1 γ_3) = -γ_1 (-γ_1 γ_2) γ_3
= γ_1² γ_2 γ_3 = γ_2 γ_3`, and `γ_1 ω = γ_1 (γ_1 γ_2 γ_3) = γ_2 γ_3`.
The other directions are analogous. Hence `ω ∈ Z(Cl(3))`.

### Step 3 — complexification: `Cl(3) ⊗_R C ≅ M_2(C) ⊕ M_2(C)`

Tensor (3) with `C` over `R`. As a real algebra, `Cl(3) ⊗_R C` has
real-dim 16 and complex-dim 8 (NOT 4 — a real algebra of real-dim
`n` has complex-dim `n` after tensoring with `C`).

The central pseudoscalar `ω` extends to `ω ⊗ 1 ∈ Cl(3) ⊗_R C`,
still satisfying `(ω ⊗ 1)² = -(1 ⊗ 1)`. In the complexified algebra
`ω` and `i ⊗ 1 := 1 ⊗ i` both square to `-(1 ⊗ 1)`, so the
combinations

```text
    e_+  :=  (1 - i ω)/2,        e_-  :=  (1 + i ω)/2,                (5)
```

(with `i ω := (1⊗i)(ω⊗1)`) satisfy `e_+ + e_- = 1`, `e_+ e_- = 0`,
`e_+² = e_+`, `e_-² = e_-`. These are central orthogonal idempotents.
On `e_+ Cl(3)⊗_R C`, `ω` acts as `+i`; on `e_- Cl(3)⊗_R C`, `ω`
acts as `-i`. Hence

```text
    Cl(3) ⊗_R C   =   ( e_+  Cl(3)⊗_R C )   ⊕   ( e_-  Cl(3)⊗_R C ),  (6)
```

with each summand a complex algebra of complex-dim 4 (totals to
complex-dim 8, consistent with the count above). Each summand is
generated by the images `ε σ_i` of `γ_i` (with `ε = +1` on `e_+`,
`ε = -1` on `e_-`) and is isomorphic to `M_2(C)`. Hence
**`Cl(3) ⊗_R C ≅ M_2(C) ⊕ M_2(C)`**, with the two summands indexed
by the central character `ω = ±i`.

### Step 4 — uniqueness within each chirality summand (U2)

Each summand `e_ε Cl(3) ⊗_R C ≅ M_2(C)` is simple (`M_2(C)` has no
non-trivial two-sided ideals). By Artin–Wedderburn, each summand
has, up to isomorphism, a unique irreducible representation: the
natural action of `M_2(C)` on `C²`. Concretely:

- `ρ_+ : Cl(3) ⊗_R C → End(C²)`, `γ_i → σ_i`, `ω → +i I`;
- `ρ_- : Cl(3) ⊗_R C → End(C²)`, `γ_i → -σ_i`, `ω → -i I`.

Any faithful irreducible complex representation of `Cl(3)` factors
through one and only one of the two summands (since the central
pseudoscalar `ω` acts as a scalar on any irrep by Schur, and that
scalar is `+i` or `-i`). Within the chosen chirality summand,
uniqueness up to unitary equivalence follows from Schur as before:
choose any intertwiner `U : V_1 → V_2` between two faithful irreps
of the same chirality, and adjust `U` to intertwine the Hermitian
inner products (which exist uniquely up to positive scalar by the
Hermiticity of `γ_i`).

### Step 5 — decomposition (U3)

Apply Maschke / Wedderburn to the semisimple algebra
`M_2(C) ⊕ M_2(C)`. Any finite-dim complex `Cl(3)`-representation
decomposes uniquely into chirality components: a `+`-component
that factors through the `e_+` summand and a `-`-component that
factors through `e_-`. Each component further decomposes into
copies of its single irrep. Hence (2) holds with multiplicities
`(n_+, n_-)` and `dim_C V = 2(n_+ + n_-)`. No odd-dim faithful
complex rep exists.

### Step 6 — moved to substep 1 (2026-05-08)

The per-site Hilbert dimension argument that was Step 6 of the
original proof is no longer in scope of this note. It depended on
the staggered-Dirac/Grassmann realization input (staggered-fermion
canonical normalisation, one Grassmann pair per site) in addition to
the physical `Cl(3)` local algebra, so it cannot be derived from the
local-algebra content here. The argument now lives in the
staggered-Dirac realization gate's substep 1
(`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`),
which forces the Grassmann partition from the physical `Cl(3)` local
algebra plus admissible mathematical infrastructure plus the
spin-statistics S2 dimension match. ∎

## Hypothesis set used

**Physical `Cl(3)` local algebra alone** for U1–U3, the in-scope
content of this note. The proof uses the standard real-algebra
classification of `Cl(3,0)`, explicit complexification via the
central pseudoscalar `ω`, and Schur's lemma in each chirality
summand. All elementary finite-dim representation theory; no
imports from the forbidden list. **No staggered-Dirac/Grassmann
realization dependency** — the former U4 step that brought in that
input has been moved to substep 1 of the staggered-Dirac realization
gate.

## Corollaries (downstream tools)

C1. *Spin-statistics chain — see substep 1 instead.* The "per-site
Hilbert dim = 2" step in
`docs/AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md` is now
discharged by substep 1 of the staggered-Dirac realization gate
(`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`)
rather than by U4 of this note. The dimensional conclusion is
independent of the chirality choice — both `ρ_+` and `ρ_-` are 2-dim
— so the spin-statistics chain is unaffected by the chirality
structure.

C2. *Universality of the spin-1/2 representation under the
canonical chirality choice.* Any half-integer spin lattice fermion
content on the explicit framework baseline (with the package convention `γ_i = σ_i`,
`ω = +i`) lives in a direct sum of the positive-chirality Pauli
irrep `ρ_+`. Higher-spin matter content, if needed, requires
*extending* the local algebra beyond `Cl(3)`, which would change
the explicit framework baseline. This is a structural rigidity result
modulo the chirality convention.

C3. *No-go for "alternative" Cl(3) site algebras within the chosen
chirality.* Anyone proposing an alternative spinor representation
on the explicit framework baseline must produce one that is unitarily equivalent to
`ρ_+ = (σ_1, σ_2, σ_3)` or, with an explicit parity flip, to
`ρ_- = (-σ_1, -σ_2, -σ_3)`. There are exactly two non-isomorphic
finite-dim faithful Cl(3) irreps and no others.

C4. *Compatibility with downstream cycles.* All downstream
cycles (spin-statistics, reflection positivity, cluster
decomposition, CPT) that need a per-site Hilbert dim = 2 input
should cite the staggered-Dirac substep 1
(`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`)
plus this note's chirality content (U2). The chirality choice is
fixed by the package convention and does not change the dimensional
content of any downstream cycle.

## Honest status

**Branch-local theorem.** (U1)–(U3) are proved on the physical `Cl(3)`
local algebra alone by
standard real-algebra classification, explicit complexification
via the central pseudoscalar, and Schur's lemma in each chirality
summand. The runner exhibits the load-bearing facts:
anticommutation relations of Pauli; central-pseudoscalar identity
`ω² = -1` and centrality; chirality eigenvalue assignments
`ω → ±i` on `ρ_±`; non-existence of an odd-dim faithful complex
rep; and unitarity of intertwiners within each chirality summand.
The 2026-05-08 narrowing dropped U4 (per-site Hilbert dim = 2 on
the explicit framework baseline) from this note's scope; that
staggered-Dirac/Grassmann bridge content is now carried by substep 1
of the staggered-Dirac realization gate.

**Not in scope.**

- Real / quaternionic uniqueness statements. The note works over
  the complex field, matching the package's complex-amplitude
  structure (derived in `docs/AXIOM_REDUCTION_NOTE.md` from the
  unitarity axiom).
- Derivation of the chirality convention from physical input. The
  package convention `γ_i = σ_i` (positive chirality) is adopted as
  a normalisation choice consistent with the standard Pauli sign
  conventions; the parity-conjugate negative-chirality irrep `ρ_-`
  is equally valid abstractly but is not the package convention.

## Load-bearing Dependencies

- Explicit framework baseline: [MINIMAL_AXIOMS_2026-04-11.md](MINIMAL_AXIOMS_2026-04-11.md)

## Audit dependency scoping (2026-05-17)

Per the 2026-05-08 narrowing of this note to physical-Cl(3)-only U1–U3 content, and
the 2026-05-10 `audited_conditional` repair instruction
(*"remove the out-of-scope staggered-Dirac gate citation from this
physical-Cl(3)-only audit packet or mark it as non-load-bearing metadata outside
the one-hop cited-authority set"*), the following notes appear in
this file as **non-load-bearing metadata only**, backticked rather
than markdown-linked so the citation graph parser does not register
them as one-hop dependencies of the physical-Cl(3)-only U1–U3 audit packet:

- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — historical
  context for the now-out-of-scope U4 closure path.
- `STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md` —
  carrier of the out-of-scope U4 / staggered-Dirac/Grassmann bridge
  content; consumed by downstream notes (spin-statistics, RP, cluster
  decomposition, CPT) directly, not via this note.

The single load-bearing one-hop dependency of the U1–U3 physical-Cl(3)-only packet
is `MINIMAL_AXIOMS_2026-04-11.md` (and its successor surface
`MINIMAL_AXIOMS_2026-05-03.md` cited above in the historical-context
section).

## Citations

- downstream consumer in this loop:
  `docs/AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md`
  (uses (U4) as a load-bearing input)
- standard external references for the technique (cited as theorem-
  grade representation theory; we do not import any numerical
  input): Artin–Wedderburn 1908/1927; Schur 1905.
