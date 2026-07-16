# Staggered-Dirac Substep 3 — Species Reduction Bridge Narrow Theorem

**Legacy identity notice:** the stable path and title are retained for ledger
identity only.  This note does not establish a staggered-Dirac, species,
physical-carrier, or realization bridge.

**Date:** 2026-05-16
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or consume a mutable audit outcome.
**Primary runner:**
[`scripts/audit_companion_staggered_dirac_substep3_species_reduction_bridge_2026_05_16.py`](../scripts/audit_companion_staggered_dirac_substep3_species_reduction_bridge_2026_05_16.py)
**Authority role:** a narrow comparison of three independently stated exact
algebraic facts.  No identification among their carriers is proved.

## 1. Exact statement

Fix the comparison dimension `d=4`.

- **(R1) Naive-operator corner count.** For the operator in the cited
  naive-lattice theorem, the corner zero set is `{0,pi/a}^4`, hence has
  cardinality `2^4=16`.
- **(R2) Role-free arithmetic.** The integer identity
  `16=4*4=2^2*2^2` holds.  It assigns no physical or representation-theoretic
  role to either factor.
- **(R3) Independent Cl(3,0) complexification fact.** In the cited theorem,
  `Cl(3,0) tensor_R C` splits as `M_2(C) direct-sum M_2(C)`.  Its two
  irreducible summands have dimensions `(2,2)`, whose sum is `4`.
- **(R4) Defined-operator module fact.** For the finite periodic difference
  operator and sign coefficients *defined* in the cited four-bit theorem,
  exact blocking and rephasing produce four matrices `alpha_mu`.  That theorem
  constructs an explicit unitary `U` and explicit irreducible `4 by 4`
  Clifford generators `gamma_mu` satisfying

  ```text
  U^dagger alpha_mu U = gamma_mu tensor I_4,  mu=0,1,2,3.
  ```

  Therefore that defined 16-dimensional module is exactly four copies of the
  displayed 4-dimensional complex Clifford module.
- **(R5) No bridge theorem.** Facts (R1), (R3), and (R4) concern separately
  specified mathematical objects.  Equality of some dimensions does not
  identify their carriers.  In particular, (R4) does not turn either copy
  index into a taste, species, generation, field, or physical carrier.

The conclusion stated here is the conjunction of (R1)-(R5).  The legacy
words in the stable identity do not strengthen it.

## 2. One-hop authorities

- [`NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md`](NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies only (R1).
- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies only (R3).
- [`STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md`](STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md)
  supplies only the formal defined-operator statement (R4).  Its physical
  words are legacy identity terms, not theorem hypotheses or conclusions.

No authority is cited for an identification among these three objects,
because no such identification is claimed.

## 3. Mathematical inputs

- finite-set counting and integer arithmetic;
- exact finite-dimensional complex linear algebra;
- the explicitly defined matrices and maps in the cited theorems.

There is no supplied physical action among the hypotheses.  In (R4), the
finite periodic set, difference operator, sign coefficients, blocking map,
and rephasing are definitions of a mathematical object.  They are not
asserted to describe a fermion or any framework carrier.

## 4. Proof

### 4.1 Corner count and arithmetic

By (R1)'s cited theorem, the relevant corner set is the Cartesian product of
four two-element sets, so its cardinality is `2^4=16`.  Direct integer
arithmetic gives `16=4*4`.  This proves (R1) and (R2), but no factor role. ∎

### 4.2 Cl(3,0) comparison

The cited split is

```text
Cl(3,0) tensor_R C  ~=  M_2(C) direct-sum M_2(C).
```

Each matrix-algebra summand has a 2-dimensional irreducible left module.
Thus the ordered pair of module dimensions is `(2,2)` and its numerical sum
is `4`.  This is (R3); it does not identify that direct sum with either the
corner set in (R1) or the defined module in (R4). ∎

### 4.3 Exact defined-operator module decomposition

The cited four-bit theorem defines, on the bit basis `|b>`,

```text
alpha_mu |b> = (-1)^(sum_{nu<mu} b_nu) |b xor e_mu>.
```

It also defines commuting suffix-sign flips `beta_mu`, constructs four
orthogonal rank-4 joint eigenspace projectors from
`Q_01=i beta_0 beta_1` and `Q_23=i beta_2 beta_3`, and gives an exact unitary
`U` for which `U^dagger alpha_mu U=gamma_mu tensor I_4`.  The displayed
`gamma_mu` generate all of `M_4(C)`, so their 4-dimensional module is
irreducible.  The similarity, rather than the dimension identity
`16=4*4`, proves exactly four isomorphic summands.  This is (R4). ∎

### 4.4 Non-identification

The hypotheses contain no map from the naive-operator corner carrier or the
framework's local algebra to the finite periodic carrier of (R4).  They also
contain no physical action, reconstruction map, continuum limit, or carrier
selection.  Consequently the dimensional coincidences cannot supply such a
map or any physical role.  This proves the negative scope statement (R5). ∎

## 5. What this note does not claim

- It does not identify the framework substrate with the comparison lattice.
- It does not force a naive, staggered, or Kogut-Susskind regulator.
- It does not derive or assume a physical action or canonical physical phase.
- It does not identify the formal module's fourfold multiplicity as four
  tastes, species, generations, Dirac fields, or continuum modes.
- It does not identify a realized matter carrier or perform OS0
  reconstruction.
- It does not infer factor roles from Hamming counts or `16=4*4`.
- It does not consume PDG data, fitted constants, or mutable audit status.

## 6. Remaining bridge

Every physical bridge remains open.  A future result would separately have
to define a candidate physical carrier/action and prove that its exact
operator is unitarily equivalent to the defined finite periodic operator on
the claimed domain.  A continuum or reconstruction claim would additionally
need its own hypotheses and proof.  Only after such results could a physical
interpretation of the module multiplicity be considered.

## 7. Validation

The primary runner uses exact SymPy arithmetic and does not read source-note
prose or audit state.  It checks:

1. the 16-element corner enumeration and role-free factorization;
2. the exact Pauli realization of the two `Cl(3,0)` summands;
3. every Clifford relation for the defined `alpha_mu`;
4. the explicit exact unitary similarity
   `U^dagger alpha_mu U=gamma_mu tensor I_4`;
5. irreducibility by exact rank 16 of the `gamma`-word span;
6. a structural hypothesis firewall rejecting an illicit physical-carrier
   or taste inference; and
7. the `d=6` factorization as a second exact identity to which the runner
   assigns no physical or representation-theoretic factor roles.

Expected normal output is `FAIL=0` and a zero exit status.

## 8. Non-load-bearing context

The following are plain-text reader pointers, not dependency edges:

- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
- `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`
- `STAGGERED_DIRAC_PHYSICAL_SPECIES_DIRECT_THEOREM_NOTE_2026-05-07.md`
- `MINIMAL_AXIOMS_2026-06-29.md`

Their status and claims are unchanged by this formal narrowing.
