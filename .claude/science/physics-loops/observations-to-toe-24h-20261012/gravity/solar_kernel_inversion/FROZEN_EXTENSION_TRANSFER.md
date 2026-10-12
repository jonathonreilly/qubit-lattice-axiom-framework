# Carry both frozen D responses to six out-of-fit sources

Direct parent protocol, 2026-10-12, fixed before either candidate's extension
fields. This implements FOLLOWUP_MARGIN_PROTOCOL.md without replacing its
original results or fitting any extension residual. These observations were
previously exposed through different response calculations; they are
out-of-fit development tests, not blind validation.

Carry the original D_galaxies_external_solar weights and the separate maximum
margin weights exactly. Require the former's three-source numerical gates and
the latter's full direct numerical/rectangle checks before execution. Any tiny
original direct rectangle allowance remains reported in the original result;
it does not change that candidate's weights or get rounded to zero.

Use all six previously source-selected galaxies in order: NGC3949, NGC3972,
UGC06667, UGC08837, DDO064, DDO168. No source replacement or selection by new
residual. Keep their64-ring baryonic profiles, stellar ratio, vertical height,
distance, inclination, isolated boundary, and processed score masks fixed.
Use the same direct full Poisson projection and the known source identity.

Stage1 constructs only the base Newtonian grids and evaluates the two frozen
responses for every galaxy, saving their actual forces. It verifies the
Newtonian projection against the midplane source field to .003 and the
previous response against its existing full-field receipt to1e-10. Stage1
has no observational scoring and is provisional. It reads no target array.

Stage2 evaluates the same two weights on the doubled radial/angular grid and
on the same boundary extension used for the three fitting sources. Require
finite positive radial forces and <=.005 refinement change, <=.003 boundary
change for each candidate/source. Do not borrow another response's convergence.
Keep failures and still complete the declared set; no refit or automatic
parameter change. Preserved caches/receipts may resume interrupted numerical
work only when source, protocol, candidate and data identities match.

After all stage2 receipts exist, open the processed targets and report each
candidate's base/refined/boundary circular velocities, RMS log10 velocity
residual, and the smallest original descriptive-rectangle relaxation
max(0,(force-H)/A,(L-force)/A). L=max(0,V-2err)^2/R and H=(V+2err)^2/R,
with A=V^2/R. No positive violation is rounded into exact compatibility.
Aggregate RMS with equal galaxy weight; aggregate rectangle t by maximum.
A nonpositive force has no real circular-speed score and remains a failure.
The comparison is numerically qualified only if every source gate passes.

No extension quantity is a fitted input to either response. The same solar
and external predictions remain unchanged because their weights and E remain
unchanged. These tests do not test an entire flexible response family, a
relativistic completion, pressure corrections or a statistical likelihood.
Any subsequent re-fit requires a new exposed-data development protocol and
retains this frozen transfer result.
