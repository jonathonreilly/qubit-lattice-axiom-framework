# Scope stress test for native SU(2) placement

**Type:** bounded_theorem
**Status:** scope record; no scientific grade.
**Primary runner:** `scripts/gb1_cf_native_placement_scope_check_2026_11_14.py`
**Cached output:** `logs/runner-cache/gb1_cf_native_placement_scope_check_2026_11_14.txt`

This is the N1–N8 scope record for the accompanying
[positive code theorem](SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md).
It grants no audit status. The negative evidence shipped is two explicit finite
capacity counterexamples under ordinary tensor composition. No general
impossibility of native gauge physics or need for an axiom change is proposed.

## N1 — Alternative approaches and submission limit

| Actual approach | Discriminating evidence | Disposition |
|---|---|---|
| Full-link exact tensor encoding | A five-state factor per edge gives dimension 5^E; the four-qubit link code explicitly realizes each factor | ATTEMPTED; feasible with extra native sites |
| Gauge-invariant spin-network reduction | Even occupied-edge patterns give at least 2^(E−V+1) orthogonal singlets; the open 27-vertex cube already exceeds 27 ordinary qubits | ATTEMPTED; exact finite capacity counterexample |
| Coarse geometric encoding with all origins | The explicit four-qubit code and local phase projectors realize every origin without selecting one in the total code | ATTEMPTED; positive result, defeats a blanket translation obstruction |
| Restricted low-energy or approximate observable reconstruction | A smaller sector or weaker fidelity target need not preserve the entire finite Hilbert space | NOT TESTED; a live different target |
| Enlarged local/joint possibility domain | More local degrees or global composition sectors change the capacity comparison | NOT ADOPTED; a different framework condition, not excluded |

Nonlocal compression, overlapping logical supports and gauge fixing are not
counted as extra mathematical approach families: at a fixed finite full-state
isometry target they still obey the same dimension comparison. No route is
labelled closed by retained authority. This inventory does not supply five
independently closed families for a general negative claim; **N1 does not
authorize a no-go packet PASS**. The negative proposal is restricted to the
displayed finite counterexamples, with broader routes explicitly live.

## N2 — Conditions are not counted as independent walls

The finite comparison specifies ordinary tensor composition, a fixed number
of native sites, and faithful isometry of the entire stated Gauss sector.
These jointly define the tested question. The unproved physical law, code
preparation and state identification are not asserted to be independent
obstructions, and no wall count is used. Altering the target or site count
escapes the finite comparison; the positive construction does so explicitly.

## N3 — Hidden-condition scan

The proof names the tensor product, SU(2) representation, graph, code basis,
fixed spectator states, spacing five, all-origin direct sum, and supplied
coarse Hamiltonian. The code's origin label is a genuine encoded degree of
freedom, not a convention silently quotiented away. The condition that the
coarse Hamiltonian is cubic invariant is proved for the stated equal-term
electric/plaquette family. No probability distribution, record preparation,
nearest-neighbor law, continuum identification or physical vacuum is imported.

## N4 — Match prior witnesses to the actual residual

| Source inspected | Actual content | Use here |
|---|---|---|
| Current minimal axioms and primitive registry | One-site M2; geometric covariance; probability/Record clauses; no supplied code state | Exact premise boundary, not a capacity theorem |
| Generated finite composition note, 2026-07-13 | Ordinary composition follows from faithful commuting generated local matrix algebras in the specified category | Warns against deriving global dimension from the one-site axiom alone |
| Finite edge-qubit cycle-space note, 2026-09-02 | Exact cycle/parity calculations on three named finite graphs | Prior mathematical method; no general physical obstruction inherited |
| MDTN outline, PR #10135 at 1f4d3173f28d41aa79f52ceb8e60d414a85f4ab1 | Resource counts and an expressly open fine-translation problem | Matching open interface; its gap and physical identifications are not used |

None is cited as an audited negative authority. The displayed finite bounds
are proved directly in the theorem and independently checked.

## N5 — Resolution of the actual statements

Per element: all five link states and operator products are encoded exactly.
Per site: native factors remain M2 under the stated composition condition.
Per mode: no spectral or momentum-mode reconstruction is tested.
Per block: spacing five and all 125 phase residues are explicit, with 12 active
and 113 spectator qubits per coarse cell.
Lattice wide: covariance and operator extension are proved on every 5n torus,
n >= 3; infinite-space claims are only local prescriptions. The two capacity
witnesses concern a fixed finite graph and the same number of native qubits.
The runner emits these resolutions without treating them as audit authority.

## N6 — Partial closure without changing axioms

The all-origin code supplies the kinematic placement on the same local M2
factors and adjacency. It does not select a physical origin, state, formation
mechanism or law. This constructive route is enough to reject the inference
that a chosen block origin necessarily requires a new lattice axiom. The
approved realized-state primitive supplies no missing preparation. No
registered primitive is relabelled as a missing or unapproved axiom.

## N7 — Strongest counterargument

An opponent of a broad negative would say: your dimension bound compares the
entire finite gauge Hilbert space with too few native sites. Physical gauge
observables may emerge on a larger scale or only in a smaller sector. Your
own all-origin code gives a local space-group-covariant encoding at a larger
scale, so the broad obstruction is already false. The actionable remaining
test is whether a uniform nearest-neighbor probability/record law can realize
the encoded observables and their preparation. This criticism is accepted;
that law is open, not ruled out or supplied by the encoding.

## N8 — Similar boundaries and what changed

The inspected corner-fermion block embedding on main uses selected blocks
and explicitly breaks fine translations. The staggered-block Dirac source
also uses a block subgroup and supplies neither a block origin nor the full
native rule. Their premises differ from the present pure geometric link code,
so neither is a no-go against it. The new local origin detectors address the
fixed-origin covariance issue at the code/operator level, while leaving the
physical-law question intact. The finite edge-parity results and earlier
two-plaquette/gluing work are retained as evidence, without promotion to a
framework verdict.

## Checks

The primary runner recomputes this note's finite statements by a path apart
from the theorem's runner. It checks the four-qubit code (isometry, `FJ = JK`,
`Q|0000> = 0`); the cycle rank `E - V + 1` of the open and periodic three-cubes
by GF(2) elimination of the incidence matrix (28 and 55) against the 27
site qubits; the singlet bound itself, by brute-force Gauss invariants on three
small graphs compared with the character count and with `2^(E-V+1)`; and the
per-cell counts (125 residues, 12 active, 113 spectators). Three controls must
fail and do: a code with `J3 = (1100 + 0011)/sqrt2` breaks `FJ = JK`; the
exponent `E - V + 2` exceeds the exact theta-graph count; and a 27-vertex tree
gives no capacity counterexample. The general lower bound remains the
theorem's proof; the runner checks its instances, in double precision for the
linear algebra.
