# Cl(3) Abstract Taste-Cube S3/Z3 Representation Theorem

**Date:** 2026-04-19 (originally); 2026-05-04 (audited_renaming
scope-narrow); 2026-06-11 (science-fix: current axiom-surface premise
edge; T₃(e₃) sign repair); 2026-06-12 (science-fix: abstract `C^8`
scope and no carrier/family load)
**Status:** representation-theory theorem on the admitted abstract
`C^8 = (C^2)^{\otimes 3}` carrier. The theorem proves only the S3
decomposition, the hw=1 Z3 orbit, and the restricted Y/T3 spectra. It is
not a framework carrier theorem and not a physical-family theorem.
**Claim type:** bounded_theorem
**Claim boundary authority:** this note
**Primary runner:** `scripts/audit_companion_cl3_taste_abstract_c8_orbit_scope_2026_06_12.py`
**Crosschecks:** `scripts/verify_cl3_sm_embedding.py` (section G);
                `scripts/frontier_s3_action_taste_cube_decomposition.py`

---

## Audit-driven scope narrowing (2026-06-12)

The latest conditional audit accepted the finite S3 character computation and
the restricted hw=1 Y/T3 spectra, but kept the row conditional because the
source still carried a non-retained framework-carrier/family reading. The
repair target allowed a direct source fix: narrow the row to a purely abstract
`C^8` representation theorem with no carrier or family load.

This pass makes that boundary the live theorem:

1. **Current retained dependencies.** The one-hop parents used for this row are
   the current retained abstract S3 theorem
   [`S3_TASTE_CUBE_DECOMPOSITION_NOTE.md`](./S3_TASTE_CUBE_DECOMPOSITION_NOTE.md)
   and the current axiom-surface metadata
   [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md). The theorem
   begins from the admitted abstract `C^8` carrier and no longer cites a
   carrier-realization or local-structure row as load-bearing input.
2. **No carrier or physical-family closure.** Any separate row that wants to
   identify this abstract `C^8` with a framework matter carrier, or identify
   the three orbit labels with physical families, must supply that bridge
   independently. This note proves only the finite S3/Z3 representation and
   restricted-spectrum facts.
3. **T3(e3) sign drift already corrected.** With `T3` read on the `b3` fiber
   (`sigma3|0> = +|0>`, `sigma3|1> = -|1>`), the state `e3` has `b3 = 1` and
   hence `T3 = -1/2`, matching the verified spectrum `{−1/2, +1/2, +1/2}`.

**Admitted-context mathematics input.** Standard finite-group character theory
for S3 (permutation-character formula `chi(sigma) = |Fix(sigma)|`,
decomposition of the 3-point permutation representation as `A_1 + E`) is
universal mathematics input, applied here directly to the retained abstract
S3 tensor-position action.

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

5. **No naming upgrade.** The combined hw=1 content is exactly a three-label
   abstract orbit with the listed restricted spectra. The theorem does not
   name those labels as physical families.

## Non-claim Boundary

This note **does not derive**:

- a framework matter-carrier realization of the abstract `C^8`;
- a physical-family identification of the three Z3 orbit labels;
- mass ordering, hierarchy, CKM, Yukawa, chirality, or full matter-content
  consequences.

Related current surfaces are
[`S3_TASTE_CUBE_DECOMPOSITION_NOTE.md`](S3_TASTE_CUBE_DECOMPOSITION_NOTE.md)
and [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md). They are
not treated here as supplying any carrier or physical-family bridge.

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

### C. hw=1 Triplet = Abstract Z3 Orbit

The hw=1 sector `{e₁, e₂, e₃}` has characters:
- `χ(e) = 3`, `χ(2-cycle) = 1`, `χ(3-cycle) = 0`

This matches `A₁ + E` exactly — the standard 3-point permutation representation.
The Z₃ element `(123)` sends `e₁ → e₂ → e₃ → e₁` (cyclic, verified numerically).

### D. Restricted Operator Spectra of the hw=1 Sector

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
restricted spectra above. It does not establish any carrier or physical-family
reading.

---

## Interpretation Boundary

The closed content is the abstract chain

```text
S3 tensor-position action on C^8 -> hw=1 A1+E sector -> Z3 three-state orbit
```

together with the restricted Y/T3 spectra. This is an abstract representation
result only; it is not a carrier theorem and not a physical-family theorem.

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

Primary verifier:

```bash
PYTHONPATH=scripts python3 scripts/audit_companion_cl3_taste_abstract_c8_orbit_scope_2026_06_12.py
```

Independent crosscheck: `scripts/frontier_s3_action_taste_cube_decomposition.py`
produces identical decomposition (`TOTAL: PASS=57, FAIL=0` per its
runner cache; the older "63/63" count referred to a superseded runner
revision).

---

## What This Theorem Sharpens

- Exact abstract support for a three-state Z3 orbit in the hw=1 sector.
- Exact restricted spectra `{+1/3,+1/3,-1}` and `{-1/2,+1/2,+1/2}` on that
  sector.
- A retained-dependency route for re-auditing this narrowed abstract support
  claim without importing an open carrier or physical-family bridge.

## What Remains Bounded

- framework-native derivation of a matter carrier;
- physical-family identification of the three labels;
- mass splitting, CKM, Yukawa hierarchy, chirality, and flavor dynamics;
- any claim that the Z3 orbit fixes physical ordering.

## Reading Rule

This note is the claim boundary for the narrowed representation-theory support
result. It does not retag audit status and does not apply carrier or
physical-family authority to downstream rows.
