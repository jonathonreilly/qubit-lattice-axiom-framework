# DM-Neutrino V_sel Selected-Axis Commutator Transport — Bounded Support

**Date:** 2026-06-16
**Claim type:** bounded_theorem / bounded support
**Status authority:** independent audit lane only. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
ledger, queue, registry, or publication-status surfaces.
**Primary runner:**
[`scripts/frontier_dm_neutrino_vsel_selected_axis_commutator_transport_2026_06_16.py`](../scripts/frontier_dm_neutrino_vsel_selected_axis_commutator_transport_2026_06_16.py)
(`TOTAL: PASS=21 FAIL=0` after local execution).

## Purpose

This note attacks the ADM-3 blocker in
[`DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md`](DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md):
the Schur coefficient needs the transverse selector curvature
`m_perp = 32`, while the prior source surface says that the graph-shift
`V_sel` coefficient is not automatically transported to the Dirac Higgs family.

The existing no-go
[`DM_NEUTRINO_VSEL_CURVATURE_TASTE_TO_DIRAC_TRANSPORT_OBSTRUCTION_NO_GO_NOTE_2026-06-07.md`](DM_NEUTRINO_VSEL_CURVATURE_TASTE_TO_DIRAC_TRANSPORT_OBSTRUCTION_NO_GO_NOTE_2026-06-07.md)
is kept intact. It blocks the pure even-trace route: for
`M(phi)^2 = |phi|^2 I`, every `Tr f(M)` even invariant is radial and cannot
produce the taste-cube axis selector.

This note supplies a narrower, outside-the-no-go support bridge. If the weak
axis `Gamma_1` is already selected, the graph-trace-normalized Clifford
commutator norm

```text
V_axis(phi) = 8 * tau_D([Gamma_1, M(phi)]^dag [Gamma_1, M(phi)])
```

has transverse Hessian `diag(0,64,64)` at `e_1`, hence `m_perp=32`, exactly
matching the graph-shift selector curvature packet. Here `tau_D = Tr_D/d_D`
is the normalized Dirac trace and the factor `8` is the source graph/taste
trace dimension from the retained graph-shift selector surface.

This is curvature transport support only. It does not derive the selected-axis
physical functional, does not derive the full graph-shift potential on the
Dirac family, does not derive the physical readout `j = g/sqrt(2)`, and does
not derive the physical weak coupling `g`.

## Statement

Let `S_i = sigma_x^(i)` be the canonical axis bit-flips on the `2^3` taste
cube, and let

```text
H(phi) = sum_i phi_i S_i.
```

The retained graph-shift selector surface gives

```text
V_graph(phi) = Tr H^4 - (1/8)(Tr H^2)^2
             = 32 sum_{i<j} phi_i^2 phi_j^2,
Hess_{e1}(V_graph) = diag(0,64,64).
```

Let `Gamma_i` be the Dirac Higgs Clifford triple and

```text
M(phi) = sum_i phi_i Gamma_i,      M(phi)^2 = |phi|^2 I.
```

Pure even traces remain blocked:

```text
Tr M^4 - (1/8)(Tr M^2)^2 = d_D(1 - d_D/8)|phi|^4,
```

so the prior no-go still rules out a native even-trace axis selector.

However, with the selected weak axis `Gamma_1`,

```text
tau_D([Gamma_1,M]^dag [Gamma_1,M]) = 4(phi_2^2 + phi_3^2),
8 * tau_D([Gamma_1,M]^dag [Gamma_1,M]) = 32(phi_2^2 + phi_3^2),
Hess_{e1} = diag(0,64,64).
```

Thus the transverse curvature packet required by the Schur denominator is
carried by the selected-axis commutator norm. The result is not a global
potential equality: `V_axis(phi)` is quadratic and selected-axis-local, while
`V_graph(phi)` is a quartic taste-cube invariant. It only transports the
curvature data actually consumed by the Schur assembly.

## Boundaries

- **Does not reopen the pure-even-trace route.** The prior no-go remains valid:
  `Tr f(M)` even invariants of the Dirac family are radial.
- **Selected-axis premise is load-bearing.** Averaging the commutator norm over
  all three axes removes the selector and fails to match the graph Hessian.
- **Graph-trace normalization is load-bearing.** Without the source taste-cube
  trace factor `8`, the normalized Dirac commutator norm has the wrong
  curvature scale.
- **Curvature only.** This note matches `Hess_{e1}` and `m_perp=32`, not the
  full `V_graph(phi)` polynomial.
- **No physical readout closure.** ADM-1 (`j=g/sqrt(2)` as physical readout),
  ADM-2 (`g` as physical coupling), and the full graph-shift-to-Dirac-Higgs
  identification remain outside this note.
- **No new axiom or registry admission.** The bridge uses the already-declared
  Dirac weak-axis convention and the graph selector's trace dimension; it does
  not create a new primitive or status class.

## Relation To The Schur Row

This support note changes the useful re-audit surface for ADM-3:

- before: `m_perp=32` was derived on the retained graph-shift taste cube but
  had no reviewed Dirac-side curvature carrier beyond the blocked pure
  even-trace route;
- after: the selected-axis Clifford commutator norm gives an explicit
  Dirac-side curvature carrier with the same Hessian packet, outside the
  pure even-trace no-go class.

The Schur row can therefore cite this as bounded support for the curvature
coefficient transport, while still keeping its physical-status boundary:
the Schur suppression value remains conditional on ADM-1, ADM-2, and the
accepted use of this selected-axis commutator functional as the relevant
phi-space transport surface.

No retained-grade proposal or status promotion is made here.

## Dependencies

- [`GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md`](GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md)
  — retained graph-shift selector surface and source trace dimension `2^3=8`.
- [`DM_NEUTRINO_DIRAC_BRIDGE_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_DIRAC_BRIDGE_THEOREM_NOTE_2026-04-15.md)
  — Dirac Higgs family `M(phi)=sum_i phi_i Gamma_i`, branch convention, and
  `M(phi)^2=|phi|^2 I`.
- [`DM_NEUTRINO_VSEL_CURVATURE_TASTE_TO_DIRAC_TRANSPORT_OBSTRUCTION_NO_GO_NOTE_2026-06-07.md`](DM_NEUTRINO_VSEL_CURVATURE_TASTE_TO_DIRAC_TRANSPORT_OBSTRUCTION_NO_GO_NOTE_2026-06-07.md)
  — boundary: pure even trace invariants do not transport the selector.
- [`DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md`](DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md)
  — downstream consumer of `m_perp=32`; not promoted by this note.

## Runner Checks

The runner verifies:

- graph shifts are commuting involutions;
- `V_graph = 32 sum phi_i^2 phi_j^2`;
- `Hess_{e1}(V_graph)=diag(0,64,64)`;
- Dirac `Gamma_i` are Hermitian Clifford involutions on the `C^16` carrier;
- `M(phi)^2=|phi|^2I`;
- pure even trace route is radial and fails to match the graph Hessian;
- selected-axis normalized commutator norm is `4(phi_2^2+phi_3^2)`;
- graph-trace-normalized `V_axis` is `32(phi_2^2+phi_3^2)`;
- `Hess_{e1}(V_axis)=diag(0,64,64)`, hence `m_perp=32`;
- removing the graph factor, averaging over axes, or demanding full potential
  equality all fail, proving the stated boundaries have teeth;
- source firewalls leave status authority and ADM-1/ADM-2/full physical
  identification open.

```text
TOTAL: PASS=21 FAIL=0
```
