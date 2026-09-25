---
claim_id: dynamics_clause_non_abelian_gauge_links_need_several_qubits_one_qubit_carries_no_su_n_link_su2_needs_two_su3_three_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: For continuous finite-dimensional unitary SU(N) representations, N>=2, a link with commuting nontrivial actions at both ends requires at least 2N states. The direct sum (N,1)+(1,N) attains this with explicit covariant matrix-unit operators. SU(2) needs two qubits and SU(3) three under this supplied link definition. Independent tensor-factor U(1), SU(2), SU(3) fields require 48 states; a joint (3,2)_Y direct-sum construction has 12 states without a joint minimum claim. No gauge-group selection or physical phase is derived.
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_non_abelian_links_need_several_qubits_2026_09_24.py
---

# State counts for supplied SU(N) quantum links

**Type:** bounded_theorem

**Date:** 2026-09-24
**Status:** conditional-support; bounded representation theory, unaudited.

## Assumptions and dimension bound

A link is a finite-dimensional Hilbert space with continuous unitary
representations of SU(N)_L and SU(N)_R, N≥2, which commute and are each
nontrivial. These are supplied mathematical requirements; the
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select a gauge group
or a link encoding. Results do not cover arbitrary non-Abelian groups.

Decompose the joint representation into irreducibles (rho,sigma).
Every nontrivial SU(N) irrep has dimension at least N. If a component
has both factors nontrivial, its dimension is at least N²≥2N.
Otherwise distinct components carrying the two nontrivial end actions
have dimensions at least N each. Thus the total dimension is at least 2N.

For a qubit, the nontrivial SU(2) representation is irreducible, so its
commutant consists of scalars; a continuous SU(2) action in that commutant
is trivial. For N≥3, a nonzero Lie algebra map su(N)→u(2) would be
injective by simplicity, contradicting N²-1>4. Connectedness then makes
the group action trivial. A qubit therefore cannot carry the specified
SU(N) link. U(1) is different: E=sigma_z/2 has unit-spaced eigenvalues
and a covariant raising operator. This half-integer generator gives a
projective 2-pi-periodic action on states and an ordinary periodic action
on observables; shifting it by I/2 gives integer eigenvalues 0,1 and a
strict U(1) representation with the same conjugation law. One-dimensional Hilbert space cannot
carry a nonzero operator of nonzero raising charge, so two states are
minimal for this nontrivial Abelian link requirement.

## Explicit attainment and covariance convention

On H=C^N_L ⊕ C^N_R take V=diag(Omega_L,Omega_R) and define

    U^{ab}=|R_b><L_a|.

Then direct multiplication, for all group elements, gives

    V† U^{ab} V
      =sum_(c,d) (Omega_L)_(a,c) U^{cd} (Omega_R†)_(d,b).

This is the chosen covariance convention. A different picture requires
correspondingly transformed transformation rules; it is not intrinsically
inconsistent. The construction attains 2N for every N≥2. Random
null-space calculations for N=2,3 are supplementary diagnostics:
the reported covariant spaces have dimensions two and one, respectively.

For the SU(3) mixed space (3,1)⊕(1,bar3), the required centre character is
omega_L omega_R^-1. Diagonal operator blocks have trivial centre
character; the cross blocks have omega_L omega_R and its inverse.
None matches under the two independently variable centres, so the
covariant space vanishes. For the four-state (2,2), End(2)=1⊕3 at
each end contains no fundamental 2, so it likewise lacks such a link
operator. Reaching a state-count bound does not make every representation
at that dimension suitable.

## Encodings and their limits

| Supplied link | States | Qubits sufficient to encode |
|---|---:|---:|
| Nonzero U(1) raising operator | 2 | 1 |
| SU(2) with both end actions nontrivial | 4 | 2 |
| SU(3) with both end actions nontrivial | 6 | 3 |
| Three independent tensor-factor U(1), SU(2), SU(3) links | 48 | 6 |
| One joint direct-sum link for R=(3,2)_Y, Y≠0 | 12 | 4 |

The 48-state result assumes independent tensor factors for the fields.
For the joint construction use (R,1)⊕(1,R) and the same matrix-unit formula
with dim R=6. Choose a nonzero allowed U(1) weight in the declared group
normalization. All factors then act at both ends. Twelve is a construction,
not a claimed minimum over all joint encodings. Unused computational
states require an encoding/constraint prescription of their own.

These counts do not select a superlattice, a continuum limit, confinement,
a Hamiltonian, the Standard Model gauge group or a physical phase. Auxiliary
Kitaev bond variables are not silently identified with physical gauge links.
The earlier unprovided independent-check narrative is preserved on the
original PR branch; the analytic arguments above carry the live claims.

## Evidence and negative-claim discipline

The [primary](../scripts/dynamics_clause_non_abelian_links_need_several_qubits_2026_09_24.py)
and [receipt](../logs/runner-cache/dynamics_clause_non_abelian_links_need_several_qubits_2026_09_24.txt)
check the qubit commutant, numerical intertwiner dimensions, explicit
matrix-unit constructions and encoding counts. Current source review
does not confer an audit verdict.

### N1
Examined routes are the qubit representation, direct-sum attainment,
mixed SU(3) pairing, tensor-product SU(2) pairing and a joint link.

### N2
A lower bound for two commuting end actions and existence of a covariant
operator are distinct requirements; dimension alone is not sufficient.

### N3
The gauge group, two-end representation and link transformation law are
supplied. Their physical realization is not an axiom consequence here.

### N4
The minimal-axiom context supplies no gauge-group selector.
Historical checker descriptions are not independent execution receipts.

### N5
Five resolutions are explicit: prove the representation floor; construct
the matrix units for all N; use centre charges for the mixed-pair
obstruction; distinguish independent fields from a joint link; and fix
the convention without declaring another picture inconsistent.
The runner prints these resolutions separately.

### N6
Native composite-link dynamics, physical group selection, a joint minimum
and controlled phases remain open.

### N7
Other groups can evade this SU(N) statement. For example U(2) can act
through its determinant at one end of a qubit, so nontrivial actions at
both ends alone are not a universal non-Abelian no-go.

### N8
This is bounded representation theory of truncated links, not a derivation
of the Standard Model or a claim of literature priority.
