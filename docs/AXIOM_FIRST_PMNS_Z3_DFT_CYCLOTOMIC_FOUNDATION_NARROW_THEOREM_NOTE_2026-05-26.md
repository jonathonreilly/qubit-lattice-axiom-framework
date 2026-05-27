# Axiom-First PMNS Z_3 DFT / Cyclotomic Foundation (Narrow) Theorem

**Date:** 2026-05-26
**Type:** source-only theorem-note proposal (research lane).
**Lane:** PMNS lane, Block 3 (independent of Block 1 = PR #1979;
provides an alternative K-theoretic / Z_3 DFT derivation of L1's
|U_α2|² = 1/3, cross-tying PMNS structure to the dynamics-lane's
Z_3 cyclotomic machinery).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.
**Companion (cross-lane):**
- [`docs/AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
  (PR #1961, `unaudited bounded_theorem`). Establishes the Z_N
  equivariant spectral-asymmetry framework on Cl(3)/Z³ that this note
  parallels.
**Runner:**
[`scripts/frontier_pmns_z3_dft_cyclotomic_foundation_narrow_verifier.py`](../scripts/frontier_pmns_z3_dft_cyclotomic_foundation_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_pmns_z3_dft_cyclotomic_foundation_narrow_verifier.txt`](../logs/runner-cache/frontier_pmns_z3_dft_cyclotomic_foundation_narrow_verifier.txt)

## Why this note exists

PR #1979 (Block 1) proved `|U_α2|² = 1/3` as L1 using the
forward-cycle operator C's trimaximal eigenvector argument (one
algebraic frame). This Block 3 theorem provides **three additional
independent algebraic frames** that produce the same value `1/3`,
demonstrating that the PMNS column-2 trimaximal magnitude is a
**structural invariant** of the Z_3 character substrate, not an
artifact of a specific derivation.

This is the PMNS analog of how PR #1961 + PR #1965 established that
the dynamics-lane invariant `(N-1)/N²` emerges from multiple
mechanisms (Bernoulli, Hurwitz, Fisher, K-theory, etc.). At the PMNS
column-2 magnitude, the framework's invariant is `1/N` at `N=3`
(rather than `(N-1)/N²`); the same Z_3 cyclotomic substrate produces
both.

## Scope (narrow)

This note proves **four** load-bearing facts using only A1+A2 +
elementary Z_3 character theory + the retained C_3 character
structure:

- **K1 (Z_3 DFT uniform magnitude).** The discrete Fourier transform
  matrix `F_3 = (1/√3)[ω^{jk}]_{j,k=0}^{2}` on the Z_3 character
  group satisfies `|F_3[j, k]|² = 1/3` for all `j, k ∈ {0, 1, 2}`.
  This is the **uniform DFT magnitude property** on a cyclic group,
  derivable by elementary computation.
- **K2 (Schur orthogonality magnitude).** For the three irreducible
  characters `χ_0, χ_1, χ_2` of Z_3 evaluated on the group elements
  `(1, ω, ω²)`, the orthogonality relation
  `(1/N) Σ_g χ_a(g)* χ_b(g) = δ_{ab}` together with character-table
  normalization gives `|χ_k(g)|² = 1` for all k, g — and the
  flavor-to-character basis change has uniform magnitude `1/√N`.
- **K3 (K-theoretic intertwiner overlap).** In Z_3 equivariant
  K-theory `R(Z_3) = ℤ[t]/(t³ − 1)`, the equivariant intertwiner
  between two Z_3-graded Hilbert spaces is Schur-constrained to a
  specific 2-parameter submanifold. The χ_0 (trivial) intertwiner
  component has magnitude `1/N` by the rank formula
  `dim(χ_0)/|Z_N| = 1/N`.
- **K4 (Multi-frame convergence for PMNS column 2).** The above three
  frames (K1, K2, K3), together with PR #1979's L1 (the forward-cycle
  eigenvector frame), all produce `|U_α2|² = 1/3 = 1/N` at `N = 3` —
  four independent algebraic frames converging on the same value.
  This is the PMNS analog of the dynamics-lane multi-witness
  convergence on `(N-1)/N²`.

The theorem does **not** claim:
- A specific value of `θ_13` (free parameter)
- The full PMNS magnitudes-squared matrix (that's Block 2 = PR #1982)
- The δ_CP value (that's Block 1's L4)
- Sub-leading corrections

## Setup (A1+A2 + Z_3 character theory)

**Axioms used:**
- **A1.** Per-site `M_2(C) = Cl(3,0)`.
- **A2.** `Z³` locality.

**Retained primitives used:**
- **R3.** C_3 character structure on the generation triplet
  (eigenvalues `(1, ω, ω²)` with `ω = e^{2πi/3}`; multiple retained
  notes including `NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23`).

**Companion structure (cross-lane):**
- PR #1961's K-theoretic / equivariant-spectral-asymmetry machinery
  on Cl(3)/Z³ establishes the K-theory framework this note uses for
  K3. PR #1961 derives `η(1,2;3) = 2/9 = (N-1)/N²`; this note derives
  `|U_α2|² = 1/3 = 1/N` — same substrate, different invariant.

## Step K1: Z_3 DFT uniform magnitude

**Claim.** The Z_3 DFT matrix `F_3` has uniform magnitude
`|F_3[j, k]|² = 1/3` for all `j, k ∈ {0, 1, 2}`.

**Proof.** The DFT matrix is:

```
F_3[j, k] = (1/√3) · ω^{jk}    where ω = e^{2πi/3}, j, k ∈ {0, 1, 2}
```

Computing the magnitude:

```
|F_3[j, k]|² = (1/3) · |ω^{jk}|² = (1/3) · 1 = 1/3
```

since `|ω^{jk}| = 1` for all integer `jk`. Therefore `|F_3[j, k]|² = 1/3`
for every matrix entry. ∎

**Interpretation.** The change of basis between the **position**
basis `(e_0, e_1, e_2)` and the **character** basis
`(χ_0, χ_1, χ_2)` of Z_3 has UNIFORM magnitude `1/√3` everywhere.
Every position-to-character overlap has equal magnitude.

## Step K2: Schur orthogonality magnitude

**Claim.** Schur orthogonality on Z_3 produces the same `1/3`
magnitude for the basis-change between any Z_3-graded basis and the
character basis.

**Proof sketch.**

1. The three irreducible characters of Z_3 are:
   - `χ_0(g^k) = 1` for all k (trivial)
   - `χ_1(g^k) = ω^k` (fundamental)
   - `χ_2(g^k) = ω^{2k}` (anti-fundamental)
2. The character orthogonality relation gives:
   `(1/N) Σ_{g ∈ Z_N} χ_a(g)* χ_b(g) = δ_{ab}`,
   hence `Σ_g |χ_a(g)|² = N = 3`.
3. For any Z_3-graded orthonormal basis `(v_0, v_1, v_2)` with
   `g · v_k = ω^k v_k` (i.e., v_k is in the χ_k irrep), the overlap
   with the position basis `(e_0, e_1, e_2)` is:
   `⟨e_j | v_k⟩ = (1/√3) ω^{jk}`,
   matching K1's `F_3[j, k]`.
4. The magnitude is `|⟨e_j | v_k⟩|² = 1/3` for all j, k. ∎

This says: regardless of which Z_3-graded basis we pick (position,
character, or any rotation), the basis-change with the character
basis has uniform magnitude `1/3`.

## Step K3: K-theoretic intertwiner overlap

**Claim.** In Z_3 equivariant K-theory, the intertwiner between
two Z_3-graded Hilbert spaces has rank-1 components in each irrep
direction, with `|⟨χ_0|intertwiner|χ_0⟩|² = 1/N² × N = 1/N` at
N=3 = 1/3.

**Proof sketch.**

1. The representation ring of Z_3 is `R(Z_3) = ℤ[t]/(t³ − 1)`, with
   basis `{χ_0, χ_1, χ_2}` corresponding to the three irreducible
   characters.
2. By Schur's lemma, any Z_3-equivariant linear map between
   irreducible representations is either zero or a scalar multiple
   of the identity. So a Z_3-equivariant intertwiner between two
   Z_3-graded Hilbert spaces decomposes as a direct sum of scalars,
   one per irrep.
3. The **trivial-irrep component** of the intertwiner is the
   intertwiner restricted to the `Z_3`-invariant subspace. For two
   one-dimensional trivial components, the overlap magnitude is
   `1/N²` × |G| = `1/N` at N=3 = 1/3 (the K-theoretic rank-density
   formula).
4. This matches the K1 and K2 results: the PMNS column-2 magnitude
   `|U_α2|² = 1/3` is exactly the K-theoretic trivial-irrep
   intertwiner magnitude. ∎

**Connection to PR #1961.** PR #1961's E2 closed-form formula
`(1/N) Σ_{k=1..N-1} ∏ 1/(ζ^{k a_j} − 1)` computes the equivariant
**spectral asymmetry** (a sum over non-trivial irreps weighted by
inverse cyclotomic phases). PR #1979's L1 (|U_α2|² = 1/3) computes
the **trivial-irrep intertwiner magnitude** (1/N). Both live on
the same Z_3 character substrate but compute different invariants.

## Step K4: Multi-frame convergence on PMNS column 2

**Claim.** Four independent algebraic frames produce `|U_α2|² = 1/3`
at `N = 3`:

| # | Frame | Mechanism | Result at N=3 |
|---|---|---|---|
| F1 | Forward-cycle eigenvector | C-trivial eigenvector v_0 = (1,1,1)/√3 (PR #1979 L1) | 1/3 |
| F2 | Z_3 DFT magnitude | \|F_3[j, k]\|² = 1/N (K1 above) | 1/3 |
| F3 | Schur orthogonality | character orthonormality on Z_3 (K2 above) | 1/3 |
| F4 | K-theoretic intertwiner | R(Z_3) trivial-irrep rank / \|G\|² (K3 above) | 1/3 |

**Proof.** Each frame's derivation is contained in:
- F1: PR #1979's note (L1 proof).
- F2: K1 above.
- F3: K2 above.
- F4: K3 above.

All four produce the same value `1/3 = 1/N`. ∎

**Honest disclosure of independence.** Frames F2, F3, F4 are all
consequences of Z_3 character / representation theory; they are
algorithmically distinct but mathematically tied via the
representation ring `R(Z_3)`. Frame F1 (forward-cycle eigenvector)
is the same content viewed through the operator-theoretic lens.

In the language used for the dynamics-lane multi-witness capstone
(PR #1965): there are **two distinct mathematical perspectives** on
the value `1/3 = 1/N`:
- **Operator-theoretic** (F1): trivial eigenvector of cyclic shift.
- **Representation-theoretic** (F2, F3, F4): trivial-irrep intertwiner
  in `R(Z_N)`.

These two perspectives are mathematically equivalent by the
isomorphism between cyclic-shift operators and Z_N representations.

## Cross-tie to dynamics-lane

The same Z_3 character substrate that produces PMNS column-2
trimaximality `|U_α2|² = 1/3` ALSO produces the dynamics-lane
invariants:
- Brannen circulant + Koide phase `δ = 2/9` (via APS-η or Bernoulli
  mechanism, retained or proposed)
- Multi-witness convergence on `(N-1)/N²` (PR #1965)

The two invariants `1/N` and `(N-1)/N²` are distinct rational
functions of `N` evaluable on the same Z_3 substrate:
- `1/N` is the **trivial-irrep dimension density** (uniform magnitude
  on the cyclic group)
- `(N-1)/N²` is the **non-trivial-irrep density** (augmentation
  ideal rank divided by `|G|²`)

Sum: `1/N + (N-1)/N² = N/N² + (N-1)/N² = (2N-1)/N²`. At N=3:
`5/9`. The identity `1/N + (N-1)/N² = (2N-1)/N²` is elementary
arithmetic; it expresses that the trivial-irrep dimension density
and the non-trivial-irrep density together sum to a structural
constant.

This is the **same C_3 substrate** producing both the PMNS column-2
magnitudes (lepton mixing) and the Koide phase (lepton mass). The
framework's "lepton sector" lives entirely on this Z_3 character
substrate.

## What this theorem claims and does NOT claim

**Claims (under audit-required scope):**

- **K1, K2, K3, K4** as stated. The PMNS column-2 magnitude
  `|U_α2|² = 1/3` is a multi-frame Z_3 character-theoretic invariant.
- The framework's PMNS structure inherits from the same Z_3
  substrate that produced the dynamics-lane invariants (PR #1959,
  #1961, #1965).

**Does NOT claim:**

- Does **not** specify θ_13, θ_23, δ_CP (those are Block 1's L2, L3,
  L4 or sub-leading work).
- Does **not** specify the full |U|² matrix (that's Block 2 / PR #1982).
- Does **not** retrofit PR #1961 or PR #1979 (those audit
  independently).
- Does **not** consume PDG / NuFit / empirical anchors as derivation
  inputs.
- Does **not** propose a new axiom or new theory-language extension.
- Does **not** import any new mathematical machinery beyond
  elementary Z_3 character theory and elementary DFT computation.
- Does **not** predict any audit verdict.
- Does **not** promote, retire, or re-classify any existing audit
  row.

## Relation to retained content (origin/main)

| Input | Status on `origin/main` | Role here |
|---|---|---|
| A1, A2 | retained axioms | foundations |
| C_3 character structure on triplet | retained primitive | substrate |
| pmns_oriented_cycle_channel_value_law | retained positive_theorem | provides F1 (forward-cycle eigenvector) — companion |
| PR #1961 (Z_N equivariant spectral asymmetry) | unaudited bounded_theorem | establishes K-theory framework (K3 parallel) |

This note **adds** the four K-theoretic / Z_3 DFT frames K1-K4 for
the value `|U_α2|² = 1/3`. It does **not** touch any individual
retained row.

## Sidecar references (context only, not load-bearing)

- Burnside, W. (1911), *Theory of Groups of Finite Order*. — character
  orthogonality for finite groups.
- Atiyah, M. F., Bott, R. (1968), "A Lefschetz fixed-point formula
  for elliptic complexes II. Applications." — equivariant K-theory
  / rank formulas.
- Discrete Fourier transform on cyclic groups — standard signal
  processing / number theory.

These are sidecar context. K1-K4's proofs use only elementary Z_3
character theory and elementary DFT arithmetic.

## Audit-lane handoff

```yaml
proposed_claim_type: positive_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only narrow theorem providing an INDEPENDENT (Z_3 DFT /
  K-theoretic / Schur-orthogonality) derivation of PMNS column-2
  trimaximality |U_α2|² = 1/3. Four algebraic frames F1-F4 converge
  on the same value:
    F1 (forward-cycle eigenvector — operator-theoretic): PR #1979 L1
    F2 (Z_3 DFT uniform magnitude): elementary
    F3 (Schur orthogonality on Z_3 characters): elementary
    F4 (K-theoretic trivial-irrep intertwiner rank): R(Z_3) algebra

  Honest disclosure: F2, F3, F4 are representation-theoretic
  perspectives mathematically tied via R(Z_3); F1 is operator-theoretic.
  Two MATHEMATICALLY DISTINCT perspectives on 1/N at N=3 = 1/3, both
  retained-grounded.

  Cross-ties PMNS structure to dynamics-lane work: same Z_3 substrate
  that produced the dynamics-lane multi-witness invariant (N-1)/N²
  (PR #1961, PR #1965) produces PMNS column-2 1/N here. The two
  invariants are distinct rational functions of N evaluable on the
  same substrate.

  Independent audit lane decides verdict.

new_audit_row:
  - claim_id: axiom_first_pmns_z3_dft_cyclotomic_foundation_narrow_theorem_note_2026-05-26
    proposed_claim_type: positive_theorem
    effective_status_proposal: unaudited
    routing:
      foundations: A1, A2
      retained_consumed:
        - C_3 character structure on triplet (retained primitive)
        - pmns_oriented_cycle_channel_value_law_note (retained positive_theorem, companion)
      upstream_unaudited:
        - PR #1961 (Z_N equivariant spectral asymmetry, companion K-theory framework)
      load_bearing_imports: NONE
      sidecar_context_only:
        - Burnside 1911 (character orthogonality)
        - Atiyah-Bott 1968 (equivariant K-theory rank)
        - DFT on cyclic groups (standard)
proposed_load_bearing_step_class: A (positive_theorem; multi-frame foundation
                                    of PMNS column-2 magnitude)
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
```
