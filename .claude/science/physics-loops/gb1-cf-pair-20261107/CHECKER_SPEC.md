# Independent two-plaquette check

Use this worktree only and retain the inherited configured model and effort.
You have a fresh context, but the same model family as the primary; record
that limitation. Do not inspect the primary worker's worktree, program,
numerical results, or conclusions before completing your own derivation.
No commit, push, external messages, axioms or authority edits.

## Raw model

Consider two coplanar squares on vertices A=(0,0), B=(1,0), C=(2,0),
D=(0,1), E=(1,1), F=(2,1). The seven links are AB,BC,DE,EF,AD,BE,CF,
oriented as written. Left loop is AB+,BE+,DE-,AD-. Right loop is
BC+,CF+,EF-,BE-. Outer loop is AB+,BC+,CF+,EF-,DE-,AD-.

Each link is the SU(2) Haar-space subspace R=span{1,2x_1,2x_2,2x_3,2x_4},
where g=x_4 I+i sum x_j sigma_j, sum x_mu^2=1. The listed basis is
orthonormal. Project multiplication by each entry of g onto R. This is
equivalently the five-state model with P_mu=(|mu><0|+|0><mu|)/2 and
U=P_4 I+i sum P_j sigma_j. It is a specified mathematical model, not
assumed to follow from the physical axioms.

For a traversal F1,...,Fn, holonomy is Fn...F1; a negative traversal uses
U dagger. Magnetic operator is the holonomy trace plus its adjoint, with
no extra normalization. Gauge transformations are independent SU(2) at all
six vertices, with U_(x,y) -> h_y U_(x,y) h_x^-1. There are no matter charges
or external links. Electric E^2=0 on the constant and 3/4 on the four
nonconstant functions.

## Independent machinery

Prefer Haar integrations / representation fusion and tensor-index contractions,
not a copy of the primary's local-matrix sparse-action implementation. Derive:
1. the complete gauge-invariant patch Hilbert space;
2. the exact two magnetic operators and electric sum in a declared basis;
3. the commutator and the square-exchange action;
4. exchange symmetry for the ordered product, Strang product, and joint
   exponential, including any counterexamples or qualifications.

Write the derivation before any comparison. Treat exact trace normalizations,
inverse orientations, the shared link, and boundary Gauss laws as candidate
failure points. A basis-dependent sign must be reconciled explicitly, not
declared a discrepancy by appearance. Do not presume a sector dimension or
matrix coefficient. Derive and report them.

Write incrementally only:
- .claude/science/physics-loops/gb1-cf-pair-20261107/CHECKER.md
- scripts/gb1_cf_two_plaquette_haar_check_2026_11_07.py
- logs/runner-cache/gb1_cf_two_plaquette_haar_check_2026_11_07.txt

Use exact arithmetic for decisive checks. Each numeric job must remain under
90 seconds and 250 MB. Run lab_ops preflight --numeric, acquire a unique
numeric-lock, set math-library threads to one, and release after the job.
If the lease is held, continue analytic work and report; do not run concurrently.
The same-model independent context is authorized by AGENTS and workhorse;
distinct machinery and exposed assumptions, not model count, support the check.

After deriving independently, send the supervisor a compact report and source
hashes. A later comparison can test emitted primary values. Include two
mutation probes that a checker demonstrably rejects (e.g. altered link
normalization and a shared-link contraction error); do not encode an expected
scientific outcome merely as a PASS assertion.

Do not claim a homogeneous three-dimensional update, physical law selection,
vacuum, continuum theory or mass gap. This is a bounded finite-patch check.
