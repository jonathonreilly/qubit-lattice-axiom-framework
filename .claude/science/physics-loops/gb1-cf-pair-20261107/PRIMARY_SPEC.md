# Bounded primary computation

Use this worktree only. Keep the inherited model and reasoning effort.
Do not commit, push, contact external services, change axioms, or edit files
outside the three assigned deliverable paths below. Read applicable repository
instructions; source reads for the physics are capped to this specification,
GOAL.md, and GB1QL.md sections 1.1-1.3 at the pinned assembly revision.

## Question

Determine the finite-register magnetic algebra on two adjacent squares and
the exact gauge-invariant sector. Derive the result; no outcome is prescribed.

The link space has orthonormal basis |0>,|1>,|2>,|3>,|4>.
P_mu=(|mu><0|+|0><mu|)/2, mu=1,...,4.
U=P_4 I_2+i sum_{j=1}^3 P_j sigma_j.
L_mu,nu=-i(|mu><nu|-|nu><mu|).
E^2 is 0 on |0> and 3/4 on each |mu>.
Recover/verify the two endpoint SU(2) actions and their conventions directly.

Vertices are A=(0,0), B=(1,0), C=(2,0), D=(0,1), E=(1,1), F=(2,1).
Stored oriented links, in order: AB, BC, DE, EF, AD, BE, CF.
Left loop: AB+, BE+, DE-, AD-.
Right loop: BC+, CF+, EF-, BE-.
Outer loop: AB+, BC+, CF+, EF-, DE-, AD-.
A minus sign denotes reversed traversal and U dagger. For a traversal
F1,...,Fn use X=Fn...F1 and B=tr X+(tr X) dagger. Retain this order.
Gauge transformations act at all six vertices; there are no external links
or matter charges. State explicitly that this boundary sector is supplied.

## Required output

1. A small exact sparse/tensor computation of link identities, magnetic
   operators, physical vectors and their matrix elements. Avoid dense matrices
   on the full 5^7-dimensional space. Derive or justify sector completeness.
2. Determine whether the two operators commute, including on the physical
   sector. If not, return an explicit exact witness.
3. Analyze plaquette exchange for the ordered product, a symmetric product,
   and the joint exponential, using exact series/identities where possible.
   A failure at one order is a scoped witness, not an impossibility theorem.
4. State what a three-qubit encoding proves, and what native-lattice issues
   it leaves open. Do not claim that this model follows from the four axioms.

Assigned deliverables (write incrementally):
- scripts/gb1_cf_two_plaquette_s1_2026_11_07.py
- logs/runner-cache/gb1_cf_two_plaquette_s1_2026_11_07.txt
- .claude/science/physics-loops/gb1-cf-pair-20261107/PRIMARY.md

Use exact rational/Gaussian-rational arithmetic for decisive coefficients;
optional floating-point checks must be distinguished. Budget each numeric
job below 90 seconds and 250 MB. Before a numeric run, run lab_ops preflight
--numeric, acquire numeric-lock with a unique holder, pin math-library threads
to one, and release the lock when the job ends. If another job holds it,
continue analytic work and notify the supervisor. Do not relax a refused
resource check. Full logs go to the assigned cache; return a short summary.

Acceptance is a correct computation or a concrete counterexample/missing
obligation, never a predetermined coefficient or PASS count. The supervisor
will inspect all delivered source and perform a separate check.
