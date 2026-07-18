---
claim_id: yt_ward_step3_contact_4fermion_vanishing_narrow_theorem_note_2026-05-17
claim_type_author_hint: bounded_theorem
runner_path: scripts/frontier_yt_ward_step3_contact_4fermion_vanishing.py
audit_authority: independent audit lane only
---

# YT_WARD Step 3 Contact Four-Fermion Vanishing Bounded Theorem

**Date:** 2026-05-17 (source-boundary repair 2026-07-18)
**Type:** bounded_theorem
**Claim scope:** under the explicit local bare-action hypothesis and standard
tree-level diagram bookkeeping, the absent scalar-singlet contact
four-fermion operator has zero bare coefficient, so single-gauge-boson
exchange is the complete leading contribution on the stated channel. Its
displayed `g_bare^2/q^2` form additionally uses the declared
continuum/small-lattice-momentum kernel convention. This
does not establish a Rep-B representation, a physical `H_unit` form factor,
or equality of Rep A and Rep B.
**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/frontier_yt_ward_step3_contact_4fermion_vanishing.py`](../scripts/frontier_yt_ward_step3_contact_4fermion_vanishing.py)

## Hypotheses

The theorem has the following ordinary explicit hypotheses:

1. The fermionic part of the bare action has the bilinear form
   `S_F = bar(psi) M[A] psi`; the remaining bare terms contain no fermion
   fields, and there is no independent fundamental scalar coupled to the
   fermions. In particular, no bare four-fermion monomial occurs. This is the
   action surface stated as a condition in
   [`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md),
   not a new framework premise supplied by this note.
2. Standard connected tree-level bookkeeping applies after integrating out
   the gauge field at tree level. With four external fermion legs and no other
   fermion-coupled carrier, the leading connected fermion-only kernel is
   single-gauge-boson exchange. That graph is one-particle reducible in the
   full gauge-plus-fermion theory; no full-theory 1PI claim is made.
3. In the declared direct/exchange color-tensor coordinates, SU(`N_c`)
   completeness has direct-singlet coordinate `-1/(2N_c)`. This is not the
   Hilbert--Schmidt projection of the full tensor onto `delta_ij delta_kl`.
   The Fierz-reordered Dirac pairing and scalar convention `c_S=+1` are fixed
   separately for the displayed specialization.
4. The notation `1/q^2` uses the continuum/small-lattice-momentum propagator
   convention. An exact Wilson-lattice expression would retain lattice
   momentum, gauge-projector, and vertex form factors.

The broader framework standing of the action condition is not re-proved
here. It remains an explicit condition rather than a premise-registry or
dependency-authority entry.

## Theorem

Because `S_F` is bilinear in the fermion fields and the other bare terms are
fermion-independent, its fourth fermionic functional derivative vanishes:

```text
delta^4 S_bare / (delta bar(psi) delta psi
                  delta bar(psi) delta psi) = 0.
```

Thus the bare four-fermion contact vertex vanishes. In particular, on the
scalar-singlet projection `O_S`,

```text
Gamma_contact,S^(4) = 0.                                      (T1)
```

Under hypotheses 2--4, the leading connected fermion-only kernel has the
one-gauge-boson-exchange coefficient

```text
Gamma_S^(4)(q^2;g_bare)
  = -c_S g_bare^2/(2N_c q^2) O_S + higher-order corrections.  (T2)
```

The displayed remainder is deliberately not assigned a universal
`g_bare^4/q^4` form: multi-boson exchange corrections require their own loop
and momentum analysis. This proves contact vanishing and leading-order
Rep-A completeness only.

## Rep-B boundary

Contact vanishing does not prove that a composite two-insertion diagram is a
second complete representation of the same projected fermion-only effective
kernel. Nor does it prove the normalization or physical interpretation of
such an operator.

For reference, if the local H-MATRIX hypothesis from the
[conditional Step-3 theorem](YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md)
is separately supplied, the
[abstract central-positive Hilbert--Schmidt theorem](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
gives only the conditional form factor

```text
F_RepB = 1/sqrt(N_c N_iso).
```

This use requires a physical construction to establish positivity,
full-matrix centrality, Hilbert--Schmidt unit norm, and the identification of
the physical form factor with a diagonal matrix expectation. The abstract
theorem supplies none of those physical statements. The separate
REP-B-RESIDUE condition must also establish unit residue/source
normalization, equal left/right insertions, and the kernel convention before
one may infer `C_B=F_RepB^2=1/(N_c N_iso)`.

Even after H-MATRIX and REP-B-RESIDUE are supplied, equality with `(T2)`
requires the separate SAME-1PI hypothesis in the fermion-only
effective-action convention. Under all three local hypotheses the coefficient
difference is

```text
c_S g_bare^2/(2N_c) - 1/(N_c N_iso),
```

and equality yields the familiar gate equation. H-MATRIX,
REP-B-RESIDUE, and SAME-1PI each remain separate and none follows from `(T1)`
or `(T2)`.

## What this theorem does not claim

- It does not derive a physical carrier or assign meanings to a
  factorization `n=N_iso N_c`.
- It does not derive a Wick state, free-field residue, Ward normalization,
  gauge-independent physical `H_unit`, `g_bare` selector, top-Yukawa datum,
  or observed quantity.
- It does not derive H-MATRIX, REP-B-RESIDUE, SAME-1PI, `g_bare=1`, or the
  physical equality of Rep A and Rep B.
- It introduces no new framework axiom, admission, primitive, physical
  input, carrier, or premise-registry entry.

## Declared dependencies

- [YT_WARD_IDENTITY_DERIVATION_THEOREM.md](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
  only for its explicitly stated Wilson-plaquette plus staggered-Dirac action
  condition and its SU(`N_c`) completeness/Fierz algebra. This note does not
  inherit that source's physical `H_unit` claims or premise readiness.
- [UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
  only for the optional abstract H-MATRIX corollary.
- [YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md](YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the explicit H-MATRIX/REP-B-RESIDUE/SAME-1PI boundary.

Non-load-bearing historical cross-references are
[G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md](G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md),
which now states only a conditional Rep-B corollary;
[G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md](G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md),
which names the unclosed pinning route. Neither supplies H-MATRIX,
REP-B-RESIDUE, or SAME-1PI here.

## Validation

The runner differentiates a generic fermion-bilinear action to verify the
zero four-fermion contact vertex, recomputes a quartic mutation to show that
the test fails when a contact term is inserted, reconstructs the SU(3) color
coordinates and an explicit Clifford-scalar coordinate, verifies the leading
exchange power, and recomputes both supplied- and missing-REP-B-RESIDUE
branches without treating any local bridge as derived. Expected output is
`PASS>0, FAIL=0`.
