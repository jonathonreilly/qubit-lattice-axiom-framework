# Mermin-Wagner / Hohenberg / Coleman + Bogoliubov Inequality — Named Non-Derivation Imports

**Date:** 2026-05-18
**Claim type:** bounded_theorem
**Status:** bounded named-import wrapper bundling three classical
results from statistical mechanics / quantum field theory: the
Bogoliubov inequality on the thermal commutator-symmetrized inner
product, and the Mermin-Wagner / Hohenberg / Coleman theorems
forbidding spontaneous breaking of continuous global symmetries in
`d <= 2` spatial dimensions at finite temperature, with the Coleman
theorem giving the relativistic `1 + 1`-dimensional zero-temperature
analogue.
**Status authority:** independent audit lane only.

## Purpose

This wrapper note documents the Bogoliubov inequality plus the
Mermin-Wagner / Hohenberg / Coleman dimension-restriction theorems as
named non-derivation imports so downstream rows (notably
`AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md`)
can register one-hop dependencies for the textbook technique inputs.

## Imports covered

### 1. Bogoliubov inequality (1962)

Statement: for two operators `A, B` on a Gibbs thermal state
`ρ = Z^{-1} e^{-βH}` with `Z = tr e^{-βH}`, the thermal commutator
inner product satisfies

```
| ⟨ [A, B] ⟩_β |^2  ≤  β · ⟨ {A, A^†} ⟩_β · ⟨ [B, [H, B^†]] ⟩_β / 2.
```

This is the **Bogoliubov inequality**, a Schwartz-style inequality
on the thermal commutator inner product. Standard derivation uses
the spectral decomposition of `ρ` plus the Schwartz inequality on
the matrix element representation. It is the central technique input
in the Mermin-Wagner proof.

Reference: N. N. Bogoliubov, *Phys. Abhandl. Sowjetunion* **6**, 1
(1962); textbook treatments in J. M. Ziman, *Models of Disorder*
(Cambridge 1979), §6; G. D. Mahan, *Many-Particle Physics*, 3rd ed.
(Plenum 2000), Ch. 3.

### 2. Mermin-Wagner theorem (1966)

Statement: in `d ≤ 2` spatial dimensions at any finite temperature
`T > 0`, no continuous global symmetry of a Hamiltonian with
sufficiently short-range interactions can be spontaneously broken; the
order parameter `⟨q_x⟩_β` of any local generator `q_x` of the symmetry
vanishes identically.

The proof combines Bogoliubov's inequality applied to the
Goldstone-mode-projected fields with the lattice infrared integral
`I_d = (1/V) Σ_{k ≠ 0} 1/E_k`. For `d = 1, 2` the integral diverges
logarithmically (`d = 2`) or as a power (`d = 1`) in the
infrared, forcing the order parameter to zero.

Reference: N. D. Mermin & H. Wagner, "Absence of Ferromagnetism or
Antiferromagnetism in One- or Two-Dimensional Isotropic Heisenberg
Models," *Phys. Rev. Lett.* **17**, 1133 (1966).

### 3. Hohenberg theorem (1967)

Statement: extends Mermin-Wagner to crystalline ordering and
Bose-Einstein condensation in `d ≤ 2`. The argument structure is
identical to Mermin-Wagner via Bogoliubov's inequality applied to the
relevant order-parameter operator.

Reference: P. C. Hohenberg, "Existence of Long-Range Order in One and
Two Dimensions," *Phys. Rev.* **158**, 383 (1967).

### 4. Coleman theorem (1973)

Statement: in `d = 2` (relativistic `d_s = 1` plus one time direction)
spontaneous breaking of continuous global symmetries is forbidden in
relativistic quantum field theory by the infrared divergence of the
massless Goldstone propagator.

Reference: S. Coleman, "There are no Goldstone bosons in two
dimensions," *Comm. Math. Phys.* **31**, 259 (1973).

## What this note does NOT claim

- This is NOT a re-derivation of any of the cited theorems.
- This is NOT a framework-level derivation of the dimension restriction
  from `Cl(3)` on `Z^3` alone; the `d = 3` substrate choice is recorded
  separately, with the textbook Mermin-Wagner restriction providing
  the structural necessity that `d >= 3` for SSB of continuous global
  symmetries.
- The D9 long-range-force/kernel condition cited in the consumer note
  is a separate framework-internal axiom-reduction artifact (from
  `AXIOM_REDUCTION_NOTE.md`) and is not covered by this textbook
  import.
- The bounded scope is the named non-derivation import only.

## Downstream usage

This wrapper is consumed by:

- `AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md` — uses Bogoliubov's inequality (Step 1) and the lattice IR-integral analysis (Step 3-4) on `Z^d`, both of which are textbook moves classified by the Mermin-Wagner / Hohenberg / Coleman literature. The consumer note's framework contribution is the explicit `Cl(3) ⊗ Z^d` substrate adaptation and the `d_s = 3` minimality conclusion combining Mermin-Wagner with the framework's D9 long-range-force/kernel condition.

## Boundary

This wrapper note is a named-import-only bounded theorem. It does not
claim:

- a framework derivation of any of the imported textbook theorems;
- closure of any downstream `d = 3` minimality theorem;
- a tighter audit-tier status for the consumers.

Its only function is to pin the Bogoliubov inequality and the
Mermin-Wagner / Hohenberg / Coleman dimension-restriction theorems as
accepted mathematical inputs so downstream notes can cite them cleanly
via one-hop edges in the audit citation graph.
