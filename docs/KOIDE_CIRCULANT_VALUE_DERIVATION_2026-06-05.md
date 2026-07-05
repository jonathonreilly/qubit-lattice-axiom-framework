# Koide value of a C3-equivariant generation mass operator

**Date:** 2026-06-05
**Type:** bounded_theorem — derivation
**Claim type:** bounded_theorem — theorem (conditional on the supplied generation carrier and
readout context).
**Status authority:** independent audit lane only. This note does not set or
predict the ledger outcome.
**Runner:** `scripts/koide_circulant_value_derivation_2026_06_05.py`
(SUMMARY: PASS=14 FAIL=0; all checks exact in sympy).
**Cached log:** `logs/runner-cache/koide_circulant_value_derivation_2026_06_05.txt`

## Statement

Let the three-generation carrier be the hw=1 Brillouin-zone corner orbit
`{e1, e2, e3}` carrying the regular representation of `C3 = Z3` (taste-generation
provenance, cited below; supplied as the readout context). Let the generation
mass operator be `C3`-equivariant and `K/CPT`-real, i.e. the circulant

```
    Y = a*I + b*C + conj(b)*C^2,     a in R,  b in C,  C = the C3 cyclic shift,
```

whose eigenvalues `lambda_k` are identified with the singular/`sqrt(m)` data of
the generation. Then the Koide ratio

```
    Q := (sum_k m_k) / (sum_k sqrt(m_k))^2 = (sum_k lambda_k^2) / (sum_k lambda_k)^2
```

satisfies, **exactly and independently of `arg(b)`,**

```
    Q = 1/3 + (2/3) r,        r := |b|^2 / a^2 .
```

Writing the two real Wedderburn blocks (singlet = trivial character; doublet =
the two faithful characters fused by `K/CPT`), their powers are `a^2` and
`2|b|^2`; the singlet<->doublet power swap acts as `r -> 1/(4r)` with the unique
fixed point `r = 1/2` (equal block power), at which

```
    Q = 2/3 .
```

The other two distinguished settings are `r = 0 -> Q = 1/3` (degenerate) and
`r = 1 -> Q = 1` (Born / per-dimension).

## Proof (all steps verified exactly in the runner)

1. **Eigenvalues.** On Fourier mode `k` the circulant has eigenvalue
   `a + b*w^k + conj(b)*w^{2k} = a + 2|b| cos(theta + 2 pi k/3)` with
   `b = |b| e^{i theta}`, `w = e^{2 pi i/3}`. (Runner: re/im check, all `k`.)
   `K/CPT`-reality makes `a` real, so the spectrum is real.
2. **Power sums.** `sum_k lambda_k = 3a` (the `cos` sum vanishes) and
   `sum_k lambda_k^2 = 3a^2 + 6|b|^2` (the `cos^2` sum is `3/2`). Both exact.
3. **Koide ratio.** `Q = (3a^2 + 6|b|^2)/(9a^2) = 1/3 + (2/3)(|b|^2/a^2)`. The
   phase `theta` cancels identically: `dQ/dtheta = 0`.
4. **Blocks and swap.** Singlet power `a^2`, doublet power `2|b|^2`; equality
   `a^2 = 2|b|^2` is `r = 1/2`. The power-fraction swap is `r -> 1/(4r)`, an
   involution whose only fixed point is `r = 1/2`.
5. **Values.** Substituting `r = 1/2, 0, 1` gives `Q = 2/3, 1/3, 1`.

## Scope and honest boundary

This derives the Koide **structure** of any `C3`-equivariant `K/CPT`-real
generation mass operator: the one-parameter family `Q = 1/3 + (2/3) r`, and that
the swap-symmetric setting `r = 1/2` is `Q = 2/3`.

It does **not** derive that any particular sector (e.g. the charged leptons)
sits at `r = 1/2`. The dial position `r = |b|^2/a^2` is a free flavor input
(`a, b` are unconstrained Yukawa parameters); that is a separate boundary result
(`GENERATION_DIAL_OCCUPANCY_FREE_INPUT`). No measured mass is used here; the
statement is purely structural.

## Assumptions / provenance

- **Quantum** and the emergent three-generation carrier: the hw=1 BZ-corner orbit
  and its `C3` cyclic action (taste-generation provenance —
  [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md),
  [`CL3_TASTE_GENERATION_THEOREM.md`](CL3_TASTE_GENERATION_THEOREM.md)). Supplied as the readout context; not re-derived here.
- **Record:** with that supplied finite central-sector decomposition and fixed
  `K`/CPT conjugation, the record names the realized `K`/CPT orbit and the
  scalar readout is finitely additive over disjoint records. The adopted
  `K`/CPT-real readout condition fixes `a` real and fuses the two faithful
  characters into the real doublet, giving the two-block structure used above.
  (See [`RECORD_GENERATION_READOUT_TWO_SECTORS`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md).) Record itself supplies no
  carrier, decomposition, conjugation, weight, probability, or dynamics.
- The identification of `lambda_k` with the `sqrt(m_k)` (signed/Brannen readout)
  is the standard Koide readout; the value `Q = 1/3 + (2/3)r` is invariant under
  the doublet phase `theta`.

## What this does not assume

No measured masses; no Born weight; no chirality grading; no occupancy
selection; no continuum, scale, or dynamics. The result is an exact algebraic
identity for the circulant Koide ratio.
