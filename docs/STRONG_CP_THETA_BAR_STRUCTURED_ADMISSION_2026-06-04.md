# Strong-CP Theta-Bar Structured Open Gate

**Date:** 2026-06-04
**Type:** open_gate
**Claim type:** open_gate
**Claim scope:** runner-backed organization of the `strong_cp_theta_zero_note`
open problem into gauge-side and mass-side residuals. This note creates or
edits no premise registry.
**Status authority:** independent audit lane only. This note sets no audit
status and assigns no effective grade.
**Runner:** [scripts/strong_cp_theta_bar_structured_admission_2026_06_04.py](../scripts/strong_cp_theta_bar_structured_admission_2026_06_04.py)
**Runner cache:** [logs/runner-cache/strong_cp_theta_bar_structured_admission_2026_06_04.txt](../logs/runner-cache/strong_cp_theta_bar_structured_admission_2026_06_04.txt)

```yaml
target_claim_type: open_gate
proposed_claim_type: open_gate
trace_class: open_gate_structure
premise_registry_change: false
audit_status_authority: independent_audit_lane
```

## Governance Boundary

The existing [STRONG_CP_THETA_ZERO_NOTE.md](STRONG_CP_THETA_ZERO_NOTE.md)
remains an ordinary audit-lane-owned claim surface. The runner here gives finite checks that help organize
the residual. It does not prove `theta_bar = 0`, does not prove every route to
`theta_bar = 0` impossible, and does not establish that the framework has
closed the Strong-CP open problem.

The related bridge-specific result
[STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL_2026-06-04.md](STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL_2026-06-04.md)
prunes one joint-basis route. This note is broader in bookkeeping but weaker in
authority: it is an open-gate structure note.

## Runner-Backed Structure

The runner verifies six finite facts.

1. **Form-degree check.** A four-form writing has no components on a
   three-dimensional lattice slice (`C(3,4)=0`) while it has one component in
   four dimensions (`C(4,4)=1`). This only rules out a bare four-form slot at
   the fundamental three-space writing; it does not remove a canonical
   large-gauge-winding theta parameter.
2. **Cubic pseudoscalar character.** The Levi-Civita tensor obeys
   `R R R epsilon = det(R) epsilon` for all 48 signed-permutation elements of
   `O_h`. A fully `O_h`-even gauge action would forbid an odd pseudoscalar
   slot, but the full gauge-measure/action premise and slot identification are
   not derived here.
3. **K-real circulant determinant.** For the tested `C_3`
   conjugate-symmetric circulant `M = aI + bC + conj(b) C^2`, the determinant
   is real to numerical precision, so this mass-side model collapses
   `arg det M` to `{0, pi}`.
4. **Chiral-basis dependence.** An axial rotation shifts `arg det M` by
   `2 n alpha` for `n = 3` and breaks Hermiticity in the runner example.
   Therefore the mass-side value by itself is not the invariant Strong-CP
   angle; only `theta_bar = theta_QCD + arg det M` is invariant under the
   paired anomaly bookkeeping.
5. **AC_phi_lambda algebraic overlap.** The tested mass-side circulant is the
   same finite `C_3` conjugate-symmetric object used by the
   [AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md](AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md)
   surface.
6. **Open holomorphic gate.** Breaking the conjugate-symmetry condition with a
   genuinely complex second coefficient makes the determinant acquire a
   nonzero imaginary part in the runner. The AC_phi_lambda/holomorphic
   residual is therefore not free.

These facts support a structured residual map, not premise closure.

## Residual Map

- **Gauge-side residual:** the framework has a form-degree obstruction to a
  bare three-space four-form writing and an `O_h` pseudoscalar character lever,
  but it still lacks a derived full gauge-measure/action premise and a settled
  lattice large-gauge-winding account.
- **Mass-side residual:** the tested K-real circulant gives a discrete
  `{0, pi}` mass phase, but the invariant angle requires the gauge phase as
  well, the joint gauge/mass basis bridge is not supplied by this runner, and
  quark-sector transport remains separate.
- **AC_phi_lambda relation:** the mass-side algebra overlaps an existing
  AC_phi_lambda surface. That relation may guide future work, but it does not
  by itself close a theta obligation or promote the AC_phi_lambda parent.

## Negative Boundary Check

This note does not ship a terminal no-go, so the no-go discipline gate is not
claimed as `PASS`. The open routes are explicit:

- derive the full `O_h`-even gauge action/measure premise;
- settle whether the lattice model realizes the relevant large-gauge-winding
  sector;
- prove a joint gauge/mass antiunitary bridge rather than splicing sector
  operations;
- transport the mass-side construction to the physical quark-sector
  determinant;
- derive the holomorphic/chiral generation structure instead of importing it.

## What This Does Not Claim

- It does not solve Strong CP.
- It does not close or split `strong_cp_theta_zero_note` by premise policy.
- It does not introduce a new axiom, primitive, or premise class.
- It does not turn axioms or primitives into bounded-status sources.
- It does not apply an audit verdict.
