# Flavor - determinant-character finite-patch re-audit packet

**Date:** 2026-06-04; source repair 2026-06-06.
**Claim type:** bounded_theorem.
**Status authority:** independent audit lane only. This note sets no audit
status, assigns no effective grade, and does not retag any ledger row.
**Runner:**
[`scripts/flavor_det_character_selection_audit_ready_2026_06_04.py`](../scripts/flavor_det_character_selection_audit_ready_2026_06_04.py)
(scorecard PASS=12 FAIL=0).
**Runner cache:**
[`logs/runner-cache/flavor_det_character_selection_audit_ready_2026_06_04.txt`](../logs/runner-cache/flavor_det_character_selection_audit_ready_2026_06_04.txt).
**Depends:**
[`RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md`](RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md)
(exact Record object typing),
[`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md)
(`retained_bounded`, finite Berezin determinant identity),
[`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
(`retained_bounded`, abstract two-candidate Grassmann-vs-boson finite-site
packet),
[`FLAVOR_LOGDET_FACTOR_2_RECORD_READOUT_REALIZATION_NARROW_THEOREM_NOTE_2026-06-04.md`](FLAVOR_LOGDET_FACTOR_2_RECORD_READOUT_REALIZATION_NARROW_THEOREM_NOTE_2026-06-04.md)
(finite disconnected-block record-readout realization), and
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
(Record baseline statement; not a status source).

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Bounded Claim

On a finite source surface already supplied with Grassmann/CAR matter variables
and a declared partition into independent source patches,

```text
M = (D_1 + J_1) oplus ... oplus (D_k + J_k),
```

the determinant-character part of the log-det chain closes as a bounded finite
theorem:

1. the retained-bounded finite Berezin theorem gives
   `Z_i = Berezin exp(-bar chi_i M_i chi_i) = det(M_i)` on each patch;
2. block independence gives
   `Z = product_i Z_i = det(M)`;
3. the exact Record typing theorem supplies the object-type firewall: the
   finite record readout is a scalar/additive record surface, not a probability
   state over possible outcomes;
4. regular real-positive determinant branches are real analytic, so the
   regular additive readouts of positive multiplicative amplitudes are exactly
   `W = c log Z` on the connected branch;
5. regular algebraic composition characters of `GL_n(C)` factor through the
   determinant, so the composition-axis character family is `det^m` and the
   additive readout is `c log |det|` after the positive-amplitude modulus.

This is the repaired bounded surface for the audited conditional row: the
mathematics now separates finite-patch determinant realization, Record object
typing, composition-character selection, and regular logarithmic readout.

## What The Runner Verifies

The runner performs finite checks for the source packet:

- `det(A S)=det(A)det(S)`;
- `tr`, `tr(M^2)`, and elementary symmetric `e_2` fail composition
  multiplicativity;
- integer powers `det^m` obey composition multiplicativity, while a global
  fractional complex branch such as `det^(1/2)` fails;
- direct-sum trace additivity holds, so Record additivity alone cannot select
  determinant;
- a finite Berezin signed-permutation sum equals `det(M)` on two independent
  source patches;
- the block-diagonal patch amplitude factorizes as
  `det(M_1 oplus M_2)=det(M_1)det(M_2)`;
- `log|det|` is additive over that positive block branch, while raw powers are
  multiplicative rather than additive;
- finite derivative checks match
  `d/dt log det(M+tP)|_{t=0}=Tr(M^{-1}P)` on the positive branch.

The representation-theoretic statement that regular algebraic characters of
`GL_n(C)` are determinant powers is included in the proof sketch below; the
runner supplies sanity checks and hostile counterexamples, not the whole
classification theorem.

## Proof Sketch

Let `M_i = D_i + J_i` be the finite operator matrix on patch `i`, and assume
the patch variables are the supplied Grassmann/CAR variables. The
retained-bounded finite Berezin determinant theorem gives

```text
int dbar chi_i dchi_i exp(-bar chi_i M_i chi_i) = det(M_i).
```

For independent patches the variables are disjoint and the exponent is a direct
sum. The finite exterior algebra tensor product then factorizes the integral,
so

```text
Z(M_1 oplus ... oplus M_k)
  = product_i det(M_i)
  = det(M_1 oplus ... oplus M_k).
```

On a connected real-positive determinant branch, `log det` is real analytic and

```text
d log det(M+tP)/dt = Tr((M+tP)^-1 P).
```

Any regular additive scalar readout on the positive multiplicative amplitude
therefore has Cauchy form `W(Z_1 Z_2)=W(Z_1)+W(Z_2)`, hence
`W(Z)=c log Z` after fixing the additive baseline. This is the regularity
premise in finite form; no arbitrary pathological Cauchy solutions are in
scope.

For the composition axis, a regular algebraic character
`chi: GL_n(C) -> C^*` kills the commutator subgroup `SL_n(C)` and factors
through the abelianization carried by `det`. Thus the algebraic character
family is `chi(M)=det(M)^m` for `m in Z`. Non-determinant examples such as
trace, power-traces, and elementary symmetric coefficients fail the
composition-character law.

## Honest Boundary

This repair does **not** claim that the baseline Lattice + Quantum + Record
axioms force cross-site Grassmann/CAR statistics. The retained-bounded
Grassmann forcing bridge is narrow: it compares explicit finite candidates and
keeps the physical staggered-Dirac realization gate out of scope. The separate
`FLAVOR_ZDET_FERMIONIC_STATISTICS_ADMISSION_2026-06-04.md` still correctly
localizes full framework determinant-amplitude ownership to the FS
statistics/admission fork.

This repair also does **not** prove that a general coupled KS/Dirac surface
factorizes over arbitrary disjoint record subsets. The theorem here is for a
declared independent-patch/block-diagonal source surface. Off-block couplings
remain outside the bounded claim and are correctly treated by
`FLAVOR_LOGDET_FACTOR_2_RECORD_READOUT_REALIZATION_NARROW_THEOREM_NOTE_2026-06-04.md`
as a hostile counterexample.

## Net Effect

This source packet gives the reviewer and auditor a narrower re-audit target:

```text
supplied finite Grassmann/CAR independent patches
  -> retained-bounded Berezin determinant on each patch
  -> block determinant amplitude
  -> exact Record object type / additive readout target
  -> regular log readout
  -> determinant-character family on the composition axis.
```

The remaining open frontier is not the bounded determinant-character math. It
is the broader physical selection of the Grassmann/CAR statistics frame and
the full coupled source/action surface.
