# Cl(3) Taste-Cube Generation-Candidate Representation Theorem

**Date:** 2026-04-19 (originally); 2026-05-04 (audited_renaming
scope-narrow); 2026-06-11 (science-fix: current axiom-surface premise
edge; T₃(e₃) sign repair)
**Status:** representation-theory theorem on the admitted abstract
`C^8 = (C^2)^{\otimes 3}` taste cube. The hw=1 orbit gives **three
Z₃-related generation-candidate labels** with the listed Y/T₃ spectra;
identifying these candidates with a framework staggered-Dirac carrier or
with **physical SM generations** is outside this theorem's load-bearing
scope.
**Claim type:** bounded_theorem
**Claim boundary authority:** this note
**Script:** `scripts/verify_cl3_sm_embedding.py` (section G);
            `scripts/frontier_s3_action_taste_cube_decomposition.py` (independent crosscheck)

---

## Audit-driven scope narrowing (2026-05-04)

The 2026-05-04 audit verdict was `audited_renaming`: the
representation-theory checks (S₃ decomposition `4A₁ + 0A₂ + 2E`, hw=1 = A₁+E
with Z₃ orbit, restricted Y/T₃ spectra) were accepted as algebraic content, but the
load-bearing identification of these Z₃-orbit states with **three physical
SM generations** requires a separate retained bridge theorem this note
does not provide. The narrowed scope below keeps the verified algebraic
content and explicitly defers the physical generation identification.

The renaming criterion (from the audit): *"Re-check whether a separate
retained bridge theorem derives taste-orbit states as physical SM
generations rather than naming them generation candidates."* This note now
adopts the narrower "generation-candidate" framing throughout.

## Audit-driven science-fix (2026-06-11)

The 2026-06-11 conditional audit found that the finite S3 character
computation and the restricted hw=1 Y/T3 spectra close, while the source
still mixed that closed algebra with an unaudited carrier/generation
reading. This repair keeps only the closed representation-theory surface:

1. **Current retained dependencies.** The one-hop parents now used for this
   row are the current retained abstract S3 theorem and the retained-bounded
   three-generation local-structure row:
   [`S3_TASTE_CUBE_DECOMPOSITION_NOTE.md`](./S3_TASTE_CUBE_DECOMPOSITION_NOTE.md)
   and
   [`THREE_GENERATION_STRUCTURE_NOTE.md`](./THREE_GENERATION_STRUCTURE_NOTE.md).
   The theorem begins from the admitted abstract `C^8` carrier and does not
   cite a carrier-realization row as a load-bearing dependency.
2. **No carrier or physical-generation closure.** Any separate row that
   wants to identify this abstract `C^8` with a framework staggered-Dirac
   BZ-corner carrier, or identify the three labels with physical SM
   generations, must supply that bridge independently. This note proves only
   the finite S3/Z3 representation and restricted-spectrum facts.
3. **T₃(e₃) sign drift corrected.** Section D previously wrote
   `T₃ = +1/2` for `e₃ = |0,0,1⟩`. With `T₃` read on the `b₃` fiber
   (`σ₃|0⟩ = +|0⟩`, `σ₃|1⟩ = −|1⟩`), the state `e₃` has `b₃ = 1` and
   hence `T₃ = −1/2`, as both runners and every spectrum listing in
   this note (`{−1/2, +1/2, +1/2}`) already state. The per-state
   prose now matches the verified spectrum; no runner value changes.

## Audit-driven dependency-edge rigorization (2026-05-10; refreshed 2026-06-11)

The earlier dependency blocker was that this row cited non-retained
taste-cube and three-generation authority inputs while also using
generation-candidate language. The current source separates those concerns:
the retained S3 parent supplies the abstract representation theorem, the
retained-bounded three-generation parent supplies only its narrowed local
triplet support, and carrier/physical-generation identification is excluded
from the load-bearing statement.

This rigorize pass makes the one-hop dependency status explicit so the audit
graph can route directly to current ledger verdicts. It does not promote any
sibling claim or apply an audit status.

**Cited authorities (one-hop deps):**

- [`S3_TASTE_CUBE_DECOMPOSITION_NOTE.md`](./S3_TASTE_CUBE_DECOMPOSITION_NOTE.md)
  — current ledger `effective_status: retained` for the abstract finite
  theorem: under tensor-position permutations of S3 on
  `C^8 = (C^2)^{\otimes 3}`, the class character is `(8,4,2)` and
  `C^8 ~= 4 A_1 + 2 E` with no `A_2` summand. This note's sections A-C
  reuse that retained abstract theorem directly.
- [`THREE_GENERATION_STRUCTURE_NOTE.md`](./THREE_GENERATION_STRUCTURE_NOTE.md)
  — current ledger `effective_status: retained_bounded` for the narrowed
  local spectral/orbit structure on its admitted surface, with physical
  species and SM-generation identification out of scope. This note uses
  only its retained-bounded local `hw=1` triplet/no-quotient support, not
  any physical-generation conclusion.
- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md) — current
  axiom-surface metadata for the finite tensor local algebra context. This
  theorem does not add an axiom.

**What the cite-chain does NOT close.** The source now satisfies the earlier
"dependency_not_retained" repair target for the scoped representation claim:
the direct S3 parent is retained and the local triplet parent is
retained_bounded. The chain still does **not** close a framework-carrier
derivation or physical SM-generation identification, because those statements
are deliberately outside the load-bearing theorem. The word
"generation-candidate" below is only a three-state-orbit label.

**Admitted-context literature input.** Standard finite-group character
theory for S₃ (permutation-character formula `chi(sigma) = |Fix(sigma)|`,
decomposition of the 3-point permutation representation as `A_1 + E`) is
universal mathematics input; not framework-derived.

## Statement (scope-narrowed)

**Theorem (representation-theory, scope-narrowed).** Let
`C^8 = (C^2)^{\otimes 3}` be the admitted abstract taste-cube carrier with
the tensor-position S3 action and the Y/T3 operators defined in the runner.
Then the following are exact representation-theory facts:

1. The axis-permutation group S₃ acts by tensor-position permutation, giving the
   decomposition `C^8 = 4A₁ + 0A₂ + 2E` (no A₂ component).

2. The Hamming-weight-1 sector (hw=1), spanned by
   `{e₁=(1,0,0), e₂=(0,1,0), e₃=(0,0,1)}`, transforms as the 3-dimensional
   permutation representation `A₁ + E` of S₃.

3. The three hw=1 states are related by the Z₃ cyclic subgroup:
   `e₁ → e₂ → e₃ → e₁`.

4. The hw=1 sector has Y eigenvalues {+1/3, +1/3, −1} and T₃ eigenvalues
   {−1/2, +1/2, +1/2} within the 3D subspace. The Z₃ cyclic symmetry relates all
   three states.

5. **Generation-candidate terminology.** The combined hw=1 content — two
   `Y=+1/3` eigenvectors and one `Y=-1` eigenvector — is compatible with
   the charge pattern usually sought for one left-handed generation block,
   so this note calls the three Z3-related labels "generation candidates."
   This is terminology for the abstract orbit only; it is not a physical
   generation-identification theorem.

## Physical-generation identification (deferred to a separate bridge)

This note **does not derive** the physical identification

> "the three Z₃-related taste states **are** the three physical SM
> generations (e/μ/τ together with d/s/b and u/c/t partner blocks)."

That identification is the load-bearing bridge gap flagged by the
2026-05-04 audit. To close this lane to retained-grade, a separate
retained-grade theorem must derive:

- The map between the Z₃-cyclic taste-orbit indexing and the physical
  generation index;
- Why the residual block degeneracy lifts in the physical mass spectrum
  in the Yukawa hierarchy direction (light/heavy generation split), not
  the taste-cycle direction;
- Why the Z₃-orbit ordering matches the observed e/μ/τ mass ordering or,
  equivalently, why the Yukawa hierarchy respects the cyclic structure.

Until that bridge is on the retained-grade surface, the corollary "the three
hw=1 Z₃ states **are** the three physical SM generations" is **conditional
on the bridge**, not a direct consequence of this note's
representation-theory.

Related current surfaces are
[`S3_TASTE_CUBE_DECOMPOSITION_NOTE.md`](S3_TASTE_CUBE_DECOMPOSITION_NOTE.md),
[`THREE_GENERATION_STRUCTURE_NOTE.md`](THREE_GENERATION_STRUCTURE_NOTE.md),
and [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md). They are
not treated here as supplying the deferred physical-generation bridge.

---

## Proof

### A. S₃ Action on C^8

S₃ acts on `(ℂ²)^{⊗3}` by permuting tensor positions. For permutation `σ ∈ S₃`,
the unitary operator `U(σ)` satisfies:

```
U(σ)|b₁,b₂,b₃⟩ = |b_{σ⁻¹(1)}, b_{σ⁻¹(2)}, b_{σ⁻¹(3)}⟩
```

This action:
- Preserves Hamming weight (commutes with `P_hw` for each `hw = 0,1,2,3`)
- Respects the group structure: `U(σ)U(τ) = U(στ)`

### B. Character Computation and Decomposition

The characters for each conjugacy class of S₃:

| Class | `χ(g)` on C^8 | `χ(g)` expected |
|-------|--------------|-----------------|
| identity | 8 | 8 |
| 2-cycles {(12),(13),(23)} | 4 | 4 |
| 3-cycles {(123),(132)} | 2 | 2 |

Multiplicities via inner product with irrep characters:
- `n(A₁) = (8 + 3·4 + 2·2)/6 = (8+12+4)/6 = 4`
- `n(A₂) = (8 - 3·4 + 2·2)/6 = (8-12+4)/6 = 0`
- `n(E) = (2·8 - 2·2)/6 = (16-4)/6 = 2`

Result: **C^8 = 4A₁ + 2E** — no A₂ appears.

### C. hw=1 Triplet = Generation-Candidate Orbit

The hw=1 sector `{e₁, e₂, e₃}` has characters:
- `χ(e) = 3`, `χ(2-cycle) = 1`, `χ(3-cycle) = 0`

This matches `A₁ + E` exactly — the standard 3-point permutation representation.
The Z₃ element `(123)` sends `e₁ → e₂ → e₃ → e₁` (cyclic, verified numerically).

### D. Quantum Number Content of the hw=1 Sector

Z₃ cycles all three tensor factors: e₁→e₂→e₃→e₁. Because Z₃ maps b₃ (fiber)
to b₁ (base) and back, it does NOT preserve the base/fiber decomposition on which
Y and T₃ are defined. Individual hw=1 states are NOT Y eigenstates:
- e₃ = |0,0,1⟩ (b₃=1): Y eigenstate with Y = +1/3, T₃ = −1/2 (σ₃|1⟩ = −|1⟩;
  sign corrected 2026-06-11 — the earlier `+1/2` contradicted the verified
  spectrum below and both runners)
- e₁ = |1,0,0⟩ and e₂ = |0,1,0⟩ (b₃=0, mixed base): T₃ = +1/2 each (σ₃|0⟩ = +|0⟩);
  symmetric combination (e₁+e₂)/√2 has Y = +1/3, antisymmetric (e₁−e₂)/√2 has Y = −1.

The Y eigenvalue spectrum of the full 3D hw=1 subspace is {+1/3, +1/3, −1}.
The T₃ spectrum is {−1/2, +1/2, +1/2}.

The Z3 symmetry establishes only a three-state abstract orbit carrying the
restricted spectra above. It does not establish three physical families,
mass ordering, or a framework carrier.

---

## Interpretation Boundary

The closed content is the abstract chain

```text
S3 tensor-position action on C^8 -> hw=1 A1+E sector -> Z3 three-state orbit
```

together with the restricted Y/T3 spectra. This is useful generation-lane
support, but it is not a "taste = physical generation" theorem and it does
not derive a staggered-Dirac carrier from the framework.

---

## Numerical Verification

| Check | Result |
|-------|--------|
| `U(σ)` unitary for all σ ∈ S₃ | exact |
| `[U(σ), P_hw]= 0` for all hw | exact |
| χ(e)=8, χ(2-cycle)=4, χ(3-cycle)=2 | exact |
| C^8 = 4A₁ + 0A₂ + 2E | exact |
| hw=1: A₁+E permutation rep | exact |
| Z₃ cycles {e₁→e₂→e₃→e₁} | exact |
| hw=1 Y spectrum: {−1, +1/3, +1/3} | exact |
| hw=1 T₃ spectrum: {−1/2, +1/2, +1/2} | exact |

Independent crosscheck: `scripts/frontier_s3_action_taste_cube_decomposition.py`
produces identical decomposition (`TOTAL: PASS=57, FAIL=0` per its
runner cache; the older "63/63" count referred to a superseded runner
revision).

---

## What This Theorem Sharpens

- Exact abstract support for a three-state Z3 orbit in the hw=1 sector.
- Exact restricted spectra `{+1/3,+1/3,-1}` and `{-1/2,+1/2,+1/2}` on that
  sector.
- A retained-dependency route for re-auditing this narrowed support claim
  without importing the open carrier or physical-generation bridge.

## What Remains Bounded

- framework-native derivation of a staggered-Dirac carrier;
- physical identification of the three labels with SM generations;
- generation mass splitting, CKM, Yukawa hierarchy, and flavor dynamics;
- any claim that the Z3 orbit fixes physical ordering.

## Reading Rule

This note is the claim boundary for the narrowed representation-theory support
result. It does not retag audit status and does not apply physical-generation
authority to downstream rows.
