# Finite boundary gluing primary

Continue at inherited configured model and reasoning effort. Base main is
f5af11cd0102cfd0b51aef0911f600130bf5beb1, parent branch head is
ba7790560e50afe712a68d42f550493e980cb19c. Use primary worktree only.
Allowed scientific reads: this spec, GOAL.md, the previous two-plaquette note,
docs/MINIMAL_AXIOMS_2026-06-29.md, docs/audit/data/axiom_premise_nodes.json.
Operating instructions may be read as required. Do not inspect the new checker
artifacts before delivering your derivation. Do not change shared status.

Raw model: each oriented link carries the Haar subspace R=span{1,2x1,2x2,2x3,2x4}
with g=x4 I+i x_j sigma_j, compressed multiplication U=P4 I+i P_j sigma_j,
P_mu=(|mu><0|+|0><mu|)/2 and E^2=3/4 on the nonconstant states. Observable
gauge transformation is U_xy -> h_y U_xy h_x^-1; reverse traversal uses
U dagger; closed holonomy is F_n ... F_1.

Derive, without presuming success:
1. For a link subdivided x->z->y, examine pullback f(g)->f(g2 g1).
   Find its exact finite matrix, metric/isometry, image and internal Gauss
   conditions. Check composition under a second subdivision. Determine whether
   the coarse compressed U is intertwined by U2 U1 and how E^2 is accounted
   for. Include full image invariance, not just projected matrix agreement.
2. For a graph partition with disjoint edge sets and shared boundary vertices,
   retain boundary group representations and derive the exact reconstruction
   of the global singlet space. Do not treat arbitrary overlapping links as
   independent copies. Explain when patch observables have one common action.
3. Distinguish algebraic observable/gluing consistency from compatibility of
   separately ordered patch gates, and from a native fixed-depth lattice law.

One deliverable is a source-backed PRIMARY.md with an exact standard-library
certificate runner and full raw output as supporting evidence. Write only:
.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/PRIMARY.md
scripts/gb1_cf_boundary_gluing_exact_2026_11_07.py
.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/outputs/primary_raw.txt

Use sparse/rational arithmetic; per numeric job <=90 s and <=300 MB, all math
threads one, lab_ops preflight --numeric and unique numeric lease. Declare
AUDIT_TIMEOUT_SEC and enforce resource bounds. No mutable workflow/spec reads
in the mathematical runner. Include meaningful mutation rejection for cut
normalization and one operator/accounting identity. No dense lattice matrix.
No commit, push, GitHub changes, external messages, or axiom/authority edits.
Targeted primary-source browsing is permitted if needed; record exact scope.
Deliver the derivation before comparing any checker results. No full-GB1-CF,
physical-law, continuum, vacuum or mass-gap conclusion is prescribed.
