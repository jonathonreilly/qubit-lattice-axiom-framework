# Z_N Spectral Asymmetry: Finite Operator Identification of L3(1,2)=2/9

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** finite `C_3`/circulant-operator identification of the
`L_3(1,2)=2/9` weight. This note does not prove a continuum APS eta invariant and does
not set or request any audit/status change.
**Primary runner:**
`scripts/frontier_z_n_spectral_asymmetry_physical_identification.py`
with cache
`logs/runner-cache/frontier_z_n_spectral_asymmetry_physical_identification.txt`.

## Result

For the finite generation operator

```
H = aI + bC + conj(b) C^2
```

on the `C_3` triplet, `[H,C]=0`, so `H` and the cyclic symmetry share an eigenbasis. The
singlet is the `C`-fixed vector and the doublet carries the two nontrivial characters
`omega^1` and `omega^2`. Therefore the weight tuple `(1,2)` in the finite cyclotomic sum
is the doublet character content of `H`, not an arbitrary repeated pattern.

The runner computes the same value two ways:

```
L_3(1,2) = (1/3) sum_{k=1}^{2} prod_j 1/(omega^{k a_j}-1)
         = (1/3) sum_{k=1}^{2} det[(C^k-I)^(-1) | H-doublet]
         = 2/9.
```

Thus `2/9` is a finite resolvent/Lefschetz weight attached to the `C_3` action on `H`'s
doublet sector. The doublet is also the signed sector of the same `H`: at `theta=0`, the
singlet remains positive while the doublet crosses zero at `r=1`, and the finite
equivariant character sum jumps there.

## Boundary

This supplies the finite operator-identification leg only. It does not prove the
continuum APS eta on a real lens space, does not build a curved-background Dirac
operator, and does not change the parent spectral-asymmetry note. The continuum bridge
remains separate source work.

## Load-Bearing Authorities

[AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
[THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
[NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md](NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md)
[THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
