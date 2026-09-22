# Bounded nonlinear-color and initial-drift review

**Disposition:** no actionable mathematical defect or consequential code/prose
discrepancy found in the two reviewed notes. This is independent scientific
scrutiny of the supplied construction, not an audit or retained-status
decision. The candidate nonlinear conservation law and the exact
initial-derivative theorem are correctly distinguished from a finite-time
microscopic hydrodynamic theorem.

The complete notes were read before any author checker or result. The actual
state, channel-rate and homogeneous-current premises of the unchanged routed
note were read at its verified identity; the earlier complete routed review
is a reused dependency. The independent proof reconstruction and controls
were sealed before requesting and accessing the author evidence. No primary
source or prior independent packet was modified.

## Mathematical conclusions

The fourteen-label axis/Walsh transform has rank fourteen; fixing total mass
gives exactly the thirteen stated coordinates. Its inverse and all thirteen
vector fluxes follow by summing

    F_g = gamma [<g e> cross Y + X cross <g b> - 2<g>X cross Y].

The population feedback and its order around the specified orbit-isotropic
rest background are correct. Keeping only the six vector fields at finite
amplitude would omit terms present in the actual homogeneous current.

For a direction n, the current Jacobian restricted to the simplex tangent
space is symmetrized by the positive entropy Hessian diag(1/p). This proves
real directional characteristic speeds and symmetrizability in the
interior; it does not prove strict hyperbolicity or a global solution
theorem. Direct tangent differentiation verifies the entropy flux, including
the essential -M/2 term. Removing that term produces an exact -4/35 defect
at an independently selected rational profile and tangent direction.

At a constant rest profile, the vector block is

    A6(n) = [[0,-gamma D[n cross]],[gamma B[n cross],0]].

Its positive energy, weighted divergence invariants and displayed
polarization formula are correct. For gamma!=0 and strictly positive
probabilities, coincident speeds on all three coordinate axes force
D_i=rhoA/3 and all off-diagonal B entries to vanish; these conditions also
give coincidence in every direction. They do not force full color-law
isotropy. The nonzero-w example preserves the vector optical block but
changes the full population response. A proper rotation can flip w.
Unweighted divergences generally fail to be conserved at anisotropic rest
profiles, as the source acknowledges. At gamma=0 all speeds vanish, and
the positive-speed statements correctly exclude that case.

The four-context expected current has the correct factor 1/4 multiplying
the drive and factor 1/2 multiplying the symmetric floor. Conditioning on
the endpoint colors gives E[h|a,b]=s_a-s_b; summing their indicator changes
then gives the exact displayed formula. It reduces to F_delta/2 at a
homogeneous law. Incoming and outgoing routes are counted once. With the
winding matching, even N>=8 ensures four distinct contexts for each
nonfixed channel; the fixed +e1 channel is omitted correctly.

For the initial product profile, the finite-stencil current J_h is a
polynomial in translated values of p. The integral formula

    (J_h-J_0)/h = integral_0^1 partial_h J_(theta h) d theta

has a uniformly bounded C1 norm for the given fixed C3 profile. Combining
one more spatial finite difference with
(1/2)sum a_delta tensor delta=I proves the uniform O(1/N) initial-drift
estimate. Independence is used only at time zero. The symmetric floor
remains in the finite-N correction: for gamma=0 its exact Fourier drift
is k0 sum[cos(Q.a_delta/N)-1], and the associated second displacement
tensor is diag(8,2,2). Thus it was not discarded silently.

The full reconstruction, hypotheses, countercontrols and derivations are
in `INDEPENDENT_DERIVATION.md`. The subsequently proposed smooth-time
extension was not read or used in this packet; it requires a separate check.

## Independent checks and author comparison

`independent_check.py` does not import author code. Before comparison it
verified the inverse transform, all 39 spatial moment-flux identities
symbolically, tangent entropy symmetry, an exact entropy-flux derivative,
generic anisotropic rest matrices, the source's optical examples and the
w/gamma/divergence countercontrols. It enumerated every one of the 14^4
four-context color assignments in each of the five nonfixed directions:
192080 exact integer-weight cases with four different rational laws. All
seventy current entries agree with the independently derived formula. An
exact local stencil derivative verifies
`d_h J|0 = DF_delta(p)z/4-k0 z/2`.

A separately chosen positive trigonometric profile was checked at four
fixed black anchors over N=8 through 256. Its maximum residual decreases
from 1.57624 to 0.0586614, while N times the residual lies between 12.61
and 15.02. This floating-point sequence is corroboration; the uniform bound
comes from the smooth-stencil argument. It is not a fit or trajectory test.

After the pre-comparison seal, the complete author checker and result file
were read. Their four source bindings, final receipt/logs and preserved
failure evidence were authenticated. The author's exact moment and
symmetrizer checks, numerical complex-step entropy check, optical controls
and initial-current computation match the declared purposes. They are
finite controls supporting the arguments, not substitutes for them.

`compare_author.py` imports only the independent helper. It reconstructs
the author's selected profile's analytic derivative by differentiating
the species cross-product flux, rather than using the author's Jacobian
implementation. The N=8,128,1024,8192 maximum drift errors agree within
2.23e-16. All eleven N-times-error rows, nine exact optical speed pairs and
the two symbolic harmonic fluxes were checked. The author checker itself
was not executed in this review, and the unchanged four-group suite was
not rerun solely to reproduce its completion count.

The author's first execution failed its finite-grid 0.003 threshold at
N<=1024. The preserved original source, traceback, diagnostic table and
explanation were inspected. The complete final delta only removes a dead
false conditional from the tangent-basis definition and adds
N=2048,4096,8192. All eight original row values are exactly retained, and
the profile, formulas and threshold are unchanged. This transparent
resolution does not strengthen the theorem or provide an independent rate
fit. Both independent check scripts succeeded on their first executions;
their full stdout, empty stderr and command/source receipts are preserved.

## Source identities and reproduction

All paths below are under the campaign's `campaign12h_second` directory.
Full absolute paths, sizes and hashes are recorded in the seals.

| Source | SHA-256 |
|---|---|
| DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md | d6a3689bb2ab6bf627886a77f4f197bb6a2478da59264b0dde91d3bf1f131e69 |
| DIMER_NONLINEAR_INITIAL_DRIFT.md | a67bc5a0b8f9a85e0eccba11fc56870e7861410044ff5d6e28d1ddd05d384c78 |
| DIMER_ROUTED_RECORD_TRANSPORT.md | dc7bac51a1ffb273e11e9356713778aeb645acbfb280973f927c1f1de007d873 |
| dimer_nonlinear_flux_check.py | 45f732b01260e3bd9e8651aefe42acb346a7a2f8bd30190f9f1b33313de57cc4 |
| dimer_nonlinear_flux_checks/RESULTS.json | 756b19b0ebcdacdda23510173e63f2b16627d6ba6cc1d6a2998d0a145fe6f138 |
| independent_check.py | 495f49c4c651f7f53737a116d7ffcefda8f9ff99234b23e35ee9879c539a4e70 |
| compare_author.py | a81ac8e56cc4f31398d0fcc64ebd6cb1892756f94f2156b2f6b3c4c0e40f7b84 |
| PRE_COMPARISON_SEAL.json | 976d7aaa5dccf6e65e5662ba76fffc225ded9f0b62d178eebcd70160ad2065e0 |

Reproduction uses Python 3.13.5, SymPy 1.14.0 and NumPy 2.4.4. Run a copy
of each script in a fresh reproduction directory to preserve the sealed
outputs; outputs deliberately use exclusive creation. The post-comparison
helper requires the source paths and sealed pre-comparison packet recorded
in its manifest. `FINAL_SEAL.json` reauthenticates all pre-seal bindings and
binds the complete new report, comparison and logs.

The result concerns the specified fixed matching, independent supplied
initial profile, fixed rates and smoothness/interiority hypotheses. It
does not establish preparation by the birth law, later product evolution,
nonlinear hydrodynamics, shocks, a microscopic quantum dynamics or a physical
field identification. Those limits are stated accurately in the sources.
