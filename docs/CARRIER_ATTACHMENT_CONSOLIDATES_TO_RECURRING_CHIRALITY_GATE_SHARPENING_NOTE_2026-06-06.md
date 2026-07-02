# The Half-Integer Matter-Field Carrier Escape Fails; Chirality Consolidation Is Boundary-Only

**Date:** 2026-06-06
**Claim type:** no_go (sharpening; refutes the spinor-module escape and
scopes the chirality-consolidation language to a source-boundary warning)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:** [`scripts/carrier_attachment_chirality_gate_consolidation_runner.py`](../scripts/carrier_attachment_chirality_gate_consolidation_runner.py)
**Cached output:** [`logs/runner-cache/carrier_attachment_chirality_gate_consolidation_runner.txt`](../logs/runner-cache/carrier_attachment_chirality_gate_consolidation_runner.txt)

**Claim scope (2026-06-18 repair):** The auditable source claim is the finite
rotation-level no-go: operator-frame/Clifford data do not force the per-site
`C^2` matter-state `j=1/2` law, and a spin-blind scalar kernel remains
compatible with the trivial scalar lift. The staggered/Kawamoto-Smit
`{epsilon,D}=0` route is identified only as the separate live route needed to
exclude that scalar lift. This row does not prove the KS/Grassmann
physical-state-law bridge, does not discharge the chirality import, and does
not identify the Dirac/staggered chirality gate with the Koide/generation
`r=1/2` gate.

## Audit context

After the carrier admission's signature/time residual is discharged and the massive-doubling core
has a structural/causal route, the live residual is the half-integer matter-field state-law carrier:
[`KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT`](KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md)
(`retained_bounded`): *the per-site C² qubit STATE carries the j=½ spinor rep of the PHYSICAL spatial
rotation as its transformation law* (vs the trivial scalar). A 13-agent find-the-escape panel
attacked the candidate escape *"the qubit's `Cl(3,0)→Cl(3,1)` IS the emergent spacetime Clifford, so
the spinor module supplies the j=½ state law by construction."* This note banks the verdict: the
escape is **refuted**. The older consolidation language is retained only as a
boundary statement: the remaining positive route is the separate
staggered/Kawamoto-Smit chirality route, not a closed theorem inside this row.

## Safe statement

**Part 1 — the escape is refuted (the rotation-level twin of the retained boost no-go).** The
operator-frame conjugation `U(R) σ_i U(R)† = R_{ij} σ_j` (the retained merger,
[`INTERNAL_EXTERNAL_SU2_MERGER`](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md),
`retained_bounded`) factors through `Aut(M₂(ℂ))=SO(3)` and is **blind to the SU(2) cover**: the STATE
`U(2π)=−I` (faithful j=½) but conjugation by `U` and by `−U` is identical and `R(2π)=+I` (the adjoint
kills the `Z₂` center). The **trivial scalar lift** `V(R)=I₂` satisfies **every** operator-frame
constraint and yields **identical measured numbers** (passive = active). So the j=½ state law is a
**separate datum** — the escape supplies it by assertion, exactly as the boost-covariance escape was
blind to `S(2π)=−1`. (The retained primary
[`CL3_TO_CL31_SPINOR_EXTENSION`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md) §8
confirms the `Cl(3,1)=M₄(ℝ)` action lives on the abstract algebra, **not** the per-site C² module —
so the e₄ extension never transports a state law onto the qubit.) The state-law residual therefore
still lives on the separate Kawamoto-Smit/physical-state-law route.

**Part 2 — the kernel route is a boundary, not a closed consolidation.** Via the
kernel-covariance route, the spin-blind scalar mass-shell kernel `H·I₂`
**commutes** with `σ_i`, so the trivial scalar attachment is
kernel-compatible; the **only** displayed kernel excluding the scalar is the
**spinful `σ·p`** (non-central, co-rotating). The staggered/Kawamoto-Smit
route supplies the live place where such a spinful selector can enter:
Kähler-Dirac spin-diagonalization
([`STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC`](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md),
`retained_bounded`) and the Kawamoto-Smit phase surface
([`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md),
`retained_bounded`) carry a staggered Dirac operator `D` with chiral structure
**`{ε, D}=0`** (`ε(x)=(−1)^{x+y+z}`, verified on a `Z³` torus). But those
sources are bounded local/route authorities; they do not by themselves close
the physical matter-state-law bridge, the Grassmann/statistics residual, or a
generation/r=1/2 selector.

**So the half-integer state-law carrier residual remains exactly the named
KS/physical-state-law route residual.** This row refutes the spinor-module
escape and locates the required positive selector; it does not prove that the
selector is already paid, and it is not the Koide/generation `r=1/2` gate.

## What this means for the carrier admission

After this repair, the staggered-Dirac carrier admission is scoped as:

- **signature/time** — discharged (time axis / arrow / (3,1) signature);
- **massive doubling** — structural+causal core delivered (the emergent time realizes the e₄
  doubling); positive-energy via R + rung C;
- **half-integer state-law carrier** — not supplied by the operator-frame or by
  the `Cl(3,0)→Cl(3,1)` extension; the live route is the separate
  Kawamoto-Smit/physical-state-law bridge;
- **Dirac/staggered `{ε,D}=0` chirality** — a bounded local chirality surface
  on the staggered route, not the Koide/generation `r=1/2` selector.

The source-side conclusion is therefore a clean no-go plus a route boundary:
operator-frame data cannot remove the state-law residual, and the spinful
selector must be supplied on the staggered/Kawamoto-Smit route before any
downstream carrier-cost consolidation is load-bearing.

## No-go gate (N1–N8)

- **N1 (alternatives).** (1) **ATTEMPTED:** identify the qubit spinor module with the physical
  rotation state law; it fails because operator conjugation factors through `SO(3)` and loses the
  `SU(2)` center. (2) **ATTEMPTED:** use the `Cl(3,0)→Cl(3,1)` extension to transport a state law
  onto the per-site C² module; §8 of the retained extension confines the action to the abstract
  algebra, not the site module. (3) **ATTEMPTED:** use the operator-frame covariance constraints
  alone; the trivial scalar lift satisfies them with identical measured numbers. (4) **ATTEMPTED:**
  use kernel covariance; the scalar kernel is compatible, and only a spinful `σ·p` kernel excludes
  it. (5) **OPEN:** force that spinful kernel from the staggered/Kawamoto-Smit route and bridge it
  to the physical matter-state law.
- **N2 (wall-independence).** The `Spin→SO` cover blindness, trivial-lift compatibility, and
  spinful-kernel/chirality requirement are independent: closing the kernel route does not make
  operator-frame conjugation faithful, and faithful operator-frame data would not derive the
  staggered chirality gate.
- **N3 (hidden-wall scan).** The load-bearing wall is the operator-frame→state-law lift
  (faithful-vs-trivial selector). No "by construction" or "the framework provides" step supplies
  the state law; the chirality gate is named explicitly when used.
- **N4 (residual matching).** The residual matches
  `KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT`: the unresolved object is the state-law carrier,
  not the already-retained operator-frame merger. It also matches the boost-action faith no-go's
  residual: algebra action does not force state-module faithfulness.
- **N5 (rhetoric).** The claim is scoped to the spinor-module escape and the
  source-boundary location of the live staggered route. It does not say the
  half-integer state law is forced, does not close the Kawamoto-Smit route,
  and does not force or identify the Koide `r=1/2` dial value.
- **N6 (partial-closure).** The partial closure is the finite no-go:
  operator-frame data and the `Cl(3,1)` extension do not supply the state law,
  while scalar-kernel covariance leaves the scalar lift alive. Any
  consolidation beyond that requires a separate retained KS/physical-state-law
  bridge.
- **N7 (steelman).** The strongest objection is that the qubit is already a spinor module, so the
  physical state law should be inherited. The reply is that this grants only an abstract module
  label; the physically tested rotation law still has a faithful-vs-trivial choice, and the trivial
  lift preserves all operator-frame observables unless the spinful/chiral kernel is supplied.
- **N8 (cross-cycle echo).** Consistent with the `retained_no_go`
  [`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
  (the boost-level twin) — this is its rotation-level analog.

## Boundary (honest)

- A **negative/source-boundary** result: it refutes the spinor-module escape
  and shows why a spinful staggered selector is still required; it does
  **not** force the state law or discharge the chirality import.
- The single highest-leverage next object (named, not done here): supply a
  retained KS/Grassmann-to-physical-matter-state-law bridge. The current
  Kawamoto-Smit and Grassmann rows are retained-bounded route authorities, not
  this row's proof that a physical matter-state law has been selected.
- `CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08`
  is retained-bounded and blocks the old wording that `{ε,D}=0` is the same
  gate as Koide/generation chirality or `r=1/2`. The latter remains untouched.

## Forbidden imports check

No new axiom. The minimal axioms plus retained Clifford/merger/staggered facts are used
(with the finite checks reproduced self-contained). Exact
finite-dimensional. The boost-no-go analogy is to an existing `retained_no_go`.

## Runner check breakdown

Class A: (1) operator-frame conjugation blind to the SU(2) cover; (2) trivial scalar lift satisfies
all operator-frame constraints + identical measured numbers; (3) only the spinful `σ·p` excludes the
scalar; (4) the displayed staggered `D` has `{ε,D}=0`; (5) the source-boundary guardrails forbid
reading this row as closed KS/Grassmann physical-state-law or Koide/generation `r=1/2` consolidation.
Expected `runner_check_breakdown = {A: 5, B: 0, C: 0, D: 0, total_pass: 5}`.

## Honest auditor read

The operator-frame conjugation is the adjoint `SO(3)` (blind to the `SU(2)` cover; `R(2π)=+I` while
the state `U(2π)=−I`), and the trivial scalar lift `V(R)=I₂` satisfies every operator-frame constraint
with identical measured numbers — so the j=½ state law is a separate datum and the spinor-module
escape is refuted (the rotation twin of the retained boost no-go). The spin-blind scalar kernel admits
the scalar; a spinful `σ·p`/staggered route is the next required selector, but this row does not
derive the KS/Grassmann physical-state-law bridge and does not identify the Dirac/staggered chirality
gate with Koide/generation chirality or `r=1/2`. Effective status is audit-owned.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/carrier_attachment_chirality_gate_consolidation_runner.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
- [staggered_dirac_grassmann_forcing_theorem_note_2026-05-07](STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md)
