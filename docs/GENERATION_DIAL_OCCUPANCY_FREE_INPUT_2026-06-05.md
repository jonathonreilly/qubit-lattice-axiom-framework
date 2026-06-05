# Generation Dial Occupancy Is Free Flavor Input

**Result name:** `GENERATION_DIAL_OCCUPANCY_FREE_INPUT`
**Date:** 2026-06-05
**Claim type:** theorem (no-go boundary)
**Status:** finite no-go boundary. A1 (Lattice), A2 (Quantum), and A3 (Record)
do not fix the per-sector dial occupancy `r = |b|^2 / a^2`. It is a free flavor
(Yukawa-texture) input — exactly one real parameter per fermion sector on the
derived dial axis.
**Runner:** [`scripts/generation_dial_occupancy_free_input_2026_06_05.py`](../scripts/generation_dial_occupancy_free_input_2026_06_05.py)
(target ≥ 15 PASS / 0 FAIL)

## Adopted axioms

- **A1 Lattice.** `Z^3` with nearest-neighbour structure; the generation factor
  carries the cyclic `Z_3 = C_3` regular representation with generator `C`,
  `C^3 = I`.
- **A2 Quantum.** Per-site qubit algebra `M_2(C) ~= Cl(3,0)`; physical mass
  operators are Hermitian.
- **A3 Record.** Durable `K` / CPT-orbit registration with a finitely-additive
  scalar readout. **A3 explicitly supplies no weighting, normalization,
  probability, or occupancy rule.**

## Setup: the dial

The most general `C_3`-equivariant (circulant) mass operator on the generation
factor `R^3` is

```text
Y = a I + b C + conj(b) C^2,     a > 0 real,   b in C free.
```

`(a, b)` are the Yukawa parameters. The runner verifies that the circulant
family is *exactly* the `C_3`-commutant (any matrix commuting with `C` is a
polynomial in `C`), and that the Hermitian slice is exactly "`a` real, `b`
free" — so `Y` is parametrised by **two real degrees of freedom** beyond an
overall scale: `a > 0` and one complex `b` (modulus `|b|`, phase `arg b`).

The **dial position** is the Brannen modulus

```text
r = |b|^2 / a^2  in  [0, infinity).
```

The framework's **dial axis** (sibling structure result) reads off the Koide
ratio as

```text
Q(r) = 1/3 + (2/3) r,
```

so the two distinguished settings are

```text
r = 1/2  ->  Q = 2/3   (equal-block / det_C counting),
r = 1    ->  Q = 1     (per-DOF / Born / det_R default).
```

## No-Go Statement

> The map `(a, |b|) |-> r = |b|^2 / a^2` is **onto** `[0, infinity)`, and no
> clause of A1, A2, or A3 constrains `(a, b)`. Therefore the dial occupancy
> `r` — which value the dial takes for a given fermion sector — is **not fixed
> by the axioms**. It is a free per-sector flavor input: exactly one real
> parameter per sector on the derived axis.

### Proof

**(1) Onto-ness.** For any target `r0 >= 0`, set `|b| = a sqrt(r0)` for any
`a > 0`. Then

```text
r = |b|^2 / a^2 = (a^2 r0) / a^2 = r0.
```

The endpoint `r = 0` is attained at `b = 0`; every `r0 > 0` is attained by the
above preimage. Since `r = (Re b)^2 + (Im b)^2) / a^2` is a ratio of squares,
the image is contained in `[0, infinity)`. Hence the map is onto `[0, infinity)`.
The runner constructs the preimage explicitly for
`r0 in {0, 1/2, 1, 2, 4, 7/13, 1000, r0}` (the last a generic nonnegative
symbol).

**(2) Axiom independence.** Encode each axiom's structural content as a
predicate on `Y`:

- **A1** demands only `C_3`-equivariance: `[Y, C] = 0`. This holds for *all*
  `(a, b)`; it pins the operator *form* (circulant), not the coefficient
  magnitudes.
- **A2** demands only that `Y` be a valid observable: `Y = Y^dagger`,
  i.e. `a` real and `coeff(C^2) = conj(coeff(C))`. This holds for *all*
  `(a, b)`; the qubit algebra fixes the *form*, not `|b|/a`.
- **A3** supplies a finitely-additive scalar readout over CPT/`K`-orbit
  sectors. Finite additivity constrains how sector readouts *combine*
  (`f(s + d) = f(s) + f(d)`); it does **not** fix the relative weight
  `phi_doublet / phi_scalar` of the two isotype blocks. So A3 leaves the
  scalar-vs-traceless (i.e. `a`-vs-`|b|`) split free.

None of the three predicates contains `|b|` or `a` in a way that forces a
value. Their conjunction `A1 & A2 & A3` is satisfied by the entire
two-real-parameter family. The runner exhibits axiom-satisfying members at
`r in {0, 1/2, 1, 2}` on equal footing, confirming the family is flavor-blind.

**(3) Conclusion.** A surjection onto `[0, infinity)` with no axiom clause
selecting a fibre means the occupancy `r` is undetermined by A1/A2/A3. It is
the irreducible per-sector input. ∎

## Independent confirmation (framework-internal)

This boundary coincides exactly with the freedom that two retained no-gos
already record:

- `koide_frobenius_isotype_split_uniqueness` (**retained_no_go**): on the
  `C_3`-invariant cone, positive-definiteness, Ad-invariance, and
  scalar/traceless orthogonality do **not** force the singlet:doublet
  isotype-weight ratio. The free isotype weight is the same degree of freedom
  as the free `r` here.
- `action_normalization` (**retained_no_go**): the framework declines to rank
  the `(1,1)` (block) versus `(1,2)` (per-DOF) sector weightings — i.e. it does
  not select `r = 1/2` over `r = 1`.

These are independent confirmations that the per-sector ratio is unconstrained.
The present result states the same fact directly at the level of the dial
occupancy `r`, via an onto-ness certificate.

## What IS derived vs what is the input

- **Derived (sibling results):** the dial *structure* — three chiral
  generations on the `C_3` channels, the affine axis `Q = 1/3 + (2/3) r`, and
  its distinguished settings `r = 1/2` (block-count) and `r = 1` (Born). The
  axis is strictly monotone in `r`, so distinct `r` give distinct `Q`.
- **The input (this result):** the *occupancy* — which `r` a given sector
  takes. That is the lone irreducible flavor parameter, one real number per
  sector on the derived axis.

A per-sector ladder framing `r(s) = 2^(s-1)` is merely an indexing convention
for these free occupancies; this note does **not** derive the ladder, only
records that each `r(s)` is an independently free choice.

## Honest floor (not a wall)

This is the standard flavor-input floor, stated honestly. The Standard Model
leaves the full Yukawa matrices free; here the irreducible freedom is reduced
to **one real parameter per sector on a derived one-dimensional axis** — far
less free than the SM, but not zero. The literature is consistent with this:
Koide's `Z_3` phenomenology likewise leaves the per-sector ratio a free fit.

This note makes **no** attempt to force `r = 1/2` or any occupancy; the content
is precisely that the occupancy is free. The next paths this opens include
operator-level sector-factorization on the framework's own `M_2(C)`-per-site +
`R[C_3]` algebra, and the signed-vs-singular-value readout dimension
(`koide_signed_eigenvalue_vs_singular_value_readout`) — both attempts to
supply an *additional* principle that would pin a fibre of the onto map.

## Boundary

This result does **not** claim:

- a derivation of `Q = 2/3`, `Q = 1`, or any specific occupancy;
- a derivation of the physical charged-lepton or quark mass spectrum;
- a new axiom, import, or audit verdict;
- uniqueness of any isotype-weight normalization.

It claims only the onto-ness of the occupancy map and the consequent freedom of
`r` under A1/A2/A3.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/generation_dial_occupancy_free_input_2026_06_05.py
```

Expected: `PASS=N FAIL=0` with `N >= 15`.
