# Independent boundary-flux and gluing check

Use this worktree at main f5af11cd0102cfd0b51aef0911f600130bf5beb1. Retain
the inherited configured model and effort. This is a fresh-context same-family
check, not an audit. Do not inspect any primary worktree, prior/new primary
results, or other checker artifacts before completing your own derivation.
The worktree contains unrelated frozen files; leave them untouched.

Allowed scientific sources: this spec; docs/MINIMAL_AXIOMS_2026-06-29.md;
docs/audit/data/axiom_premise_nodes.json. Required operating instructions may
be read. Targeted primary-source browsing is allowed; record exact scope.

Raw finite model: an oriented link has SU(2) Haar subspace
R=span{1,2x1,2x2,2x3,2x4}, g=x4 I+i x_j sigma_j, sum x_mu^2=1.
Compressed multiplication is U=P4 I+i P_j sigma_j with
P_mu=(|mu><0|+|0><mu|)/2. Its endpoint representation is the constant plus
the fundamental matrix-coefficient space. E^2 is zero on the constant and
3/4 on the other four states. Gauge action is U_xy -> h_y U_xy h_x^-1;
path products are reverse traversal order; reversal means dagger.

Derive two related checks, without assuming expected dimensions or a positive
gluing verdict:
1. With a link cut into x->z->y, analyze f(g)->f(g2 g1) using normalized
   representation coefficients/Haar integration. Determine its image and
   normalization, boundary representation matching, subdivision associativity,
   the action of compressed U2 U1, and electric-energy accounting. Prefer
   index/fusion reasoning independent of a direct five-state matrix runner.
2. Use the 2x2 plaquette graph on vertices (x,y), x,y=0,1,2; all 12 edges point
   along positive coordinate directions. For a vertical regional split,
   A owns vertical edges at x=0 and x=1 (four total), and the three horizontal
   edges from x=0 to x=1. B owns the two vertical edges at x=2 and the three
   horizontal edges from x=1 to x=2. Their common boundary is x=1, y=0,1,2.
   Enforce Gauss constraints only at each region's non-interface vertices and
   retain the full representation/multiplicity data at the three interface
   vertices. Compute each regional decomposition and its gluing count, and
   independently count the full all-vertex singlet space. Preserve all
   multiplicities at vertices with four occupied ends.
   Also count the open-boundary square with Gauss law only at (1,1), keeping
   the eight outer boundary vertices unprojected; do not build a dense matrix.
   Examine grouping into three edge sets: left vertical edges plus left
   horizontals; middle vertical edges alone; right vertical edges plus right
   horizontals. Explain which constraints may be applied before the final
   region is attached. Do not assume shared boundary vertices can always be
   projected to singlets at an intermediate grouping.

One deliverable is CHECKER.md, with a self-contained exact certificate and
full raw execution output as supporting evidence. Write only:
.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/CHECKER.md
scripts/gb1_cf_boundary_fusion_check_2026_11_07.py
.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/outputs/checker_raw.txt

Resource cap per numeric job: 90 seconds and 300 MB, exact rational/integer
arithmetic, one math thread, successful lab_ops numeric preflight and unique
numeric lease, released afterward. Declare AUDIT_TIMEOUT_SEC and enforce
bounds. No workflow/spec runtime inputs in the certificate. Include meaningful
fault probes for prematurely deleting flux sectors and discarding invariant
multiplicity. No commit, push, GitHub changes, external messages, or edits
outside the assigned paths. Deliver analytic results before seeing comparison
artifacts. Distinguish finite gauge mathematics from native qubit allocation,
Admissibility/Record law, continuum, vacuum and mass gap.
