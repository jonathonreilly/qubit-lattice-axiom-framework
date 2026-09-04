# Carried relative extended Green-shape mode-existence hunt note (2026-07-17)

Authority: none
Audit: unset

## Question and answer

Can a broader finite-volume search of the actual carried update expose
Green-like profiles that are not almost wholly contact-supported?

Yes, in a deliberately limited constructive sense. A declared tournament over
bounded spectral windows returns simple search witnesses at nonzero total
momentum on training `L=3,4` and declared held-size `L=5,6`. Each witness has
contact fraction at most `0.60` and overlap at least `0.50` with the residual-matched
shifted-Green comparator after an explicitly adaptive projection within the
complete three-dimensional proper-cubic scalar projection space used here.
This is a search witness, not a continuing spectral branch, a predicted
kernel, or a long-distance law.

The executable is
`scripts/carried_relative_extended_green_branch_hunt_2026_07_17.py`.

## Actual update and lawful momentum sector

The finite update is the same one-matter `Q=N_e+N_f=1` carried update used by
the preceding stationary-mode probe:

1. the Cycle-219 common six-direction matter coin;
2. the Cycle-214 six-direction field coin;
3. the local `e <-> g+field` exchange at relative contact;
4. matter streaming and field streaming.

For torus length `L`, total momentum is supplied only as an integer vector
`n` with `K=2 pi n/L`. The relative stream therefore carries the matter
phase `exp(-i d_m.K)`. The lift into the full periodic one-matter sector
multiplies every body position by `exp(+i K.x)/sqrt(L^3)`. At `L=3` the
executable checks the lift on the full relative basis, rather than one sample:
it is an isometry and satisfies `G_full E_K = E_K G_K` to sparse numerical
precision. It also checks that the new `K=0` block is identical to the
predecessor carried-relative update. Undersized tori and fractional momentum
indices are rejected.

This validates the nonzero-`K` reduction of the actual carried update. It
does not turn `K`, an eigenphase, or the sector label into a new dynamical
resource. The lift spans the declared relative block inside one discrete
momentum sector of the already projected `Q=1` domain; it is not a leakage test
for other `Q` sectors or a claim to span the whole periodic Hilbert space with
one `K`.

## Proper-cubic scalar projections

An ordered matter-direction/field-direction pair has exactly three scalar
orbit types under simultaneous proper-cubic rotations:

- same direction, `d_m.d_f=+1`;
- opposite direction, `d_m.d_f=-1`;
- perpendicular directions, `d_m.d_f=0`.

The runner contracts the `6 x 6` pair amplitude separately on these three
orbits. It exhausts all 24 frames and verifies that these are exactly the
three simultaneous direction-pair orbits, of sizes `6+6+24=36`; hence they
span the invariant linear direction-pair contractions used here and introduce
no preferred axis. Each contraction is the orbit-amplitude sum divided by the
square root of that orbit's cardinality. This supplied normalization is
load-bearing for the Euclidean coefficient normalization and projection-weight
floor. The runner prints the
weight, contact fraction, Green overlap, and Green residual of all three
fixed profiles for every selected witness, before printing the adaptive
combination.

It also reports an adaptive projection. For each eigenpair, the three
zero-mean scalar profiles form a supplied matrix `A`. The rule projects the
comparator into `col(A)` and solves for the normalized three-component
coefficient vector. Thus the reported best overlap is the maximum available
inside this declared scalar span. The three complex coefficients are printed
for every selected witness. They are analysis-side selector structure, not
coefficients in the carried update, and their per-eigenpair adaptation means
the result is not a parameter-free prediction.

After coefficient normalization and removal of one irrelevant common phase,
this is up to four real profile-shape degrees of freedom per eigenpair
(`CP^2`, fewer if the three profiles are rank deficient). In addition, the
tournament adaptively selects the momentum shell, spectral window, and
eigenpair separately at each size. The comparator shift is also different for
each candidate, although it is deterministically residual-matched to that
candidate's eigenphase rather than independently fitted. None of these
analysis freedoms is a parameter of the physical update.

Tiny numerical scalar shadows of symmetry-dark eigenspaces are rejected by
the supplied projection-weight floor `10^-6`. Candidate eigenvalues must
also be locally simple at the returned-window resolution; degenerate ARPACK
basis choices are not promoted as stable witnesses.

## Residual-matched comparator and extension score

For an eigenvalue `z=exp(-i omega)` on the searched forward phase branch, the
shape comparator uses

`mu_carry = 6 (1-cos(omega))`

and

`H_mu = 3 (Delta_L-mu_carry I)^-1 (delta_0-1/L^3)`.

The coefficient `3`, Laplacian, and neutralized point source are supplied by
the separate fixed-reservoir/Cycle-216 comparison fixture. The actual
fixed-reservoir scalar state is not compared. The shift is required to stay
at least two percent of the first nonzero Laplacian eigenvalue below the first
pole. Only the phase-agnostic unit-shape overlap is scored; there is no scale
fit.

For a zero-mean projected profile `phi`, the extension diagnostic is

`f_contact = |phi(0)|^2 / ||phi||^2`.

The declared search gates include `f_contact <= 0.60` and Green-shape overlap
at least `0.50`. These are bounded operational definitions for the tournament,
not a theorem that the profile has an asymptotic tail. The executable also
prints the normalized Green residual
`sqrt(2-2 overlap)`, scalar projection weight, eigenpair residual, local
eigenvalue gap, pole margin, phase, and adaptive coefficients.

## Supplied-window inventory

The supplied-window inventory encoded in the artifact is:

- training sizes: `L=3,4`;
- held sizes: held `L=5,6`;
- `K=0` on all four sizes, with seven target fractions of the first-pole
  phase;
- axis momentum index `(1,0,0)` on all four sizes, with nine target
  fractions;
- face and body momentum indices `(1,1,0)` and `(1,1,1)` on `L=4,5`, with
  six target fractions each;
- eight sparse eigenpairs per target window;
- three fixed scalar orbit projections, their square-root-cardinality
  normalization, and the declared adaptive rule;
- contact maximum `0.60`, scalar weight minimum `10^-6`, pole-margin fraction
  `0.02`, Green-overlap minimum `0.50`, and local simple-eigenvalue gap
  `10^-7`.

That is 88 windows and 704 raw returned eigenpairs before phase, pole,
projection-weight, simplicity, extension, and overlap filters. Repeated eigenvalues
seen from overlapping target windows remain visible in the raw inventory and
are separately deduplicated for reporting.

The declared held-size result reruns that existence-search protocol on
`L=5,6`. This artifact is not a prospective preregistration and does not prove
that the partition or gates were fixed before those sizes were inspected, so “held” is a
supplied train/held partition and a held-size stress test, not an uncontaminated
statistical validation claim. It also does not track one eigenvalue or freeze
one adaptive coefficient vector from training, so it is not evidence for a
continuing spectral branch.

## Numerical disposition

The declared selector returned the following witnesses. `w_proj` is the
squared norm of the normalized-coefficient adaptive scalar projection; the
last column is the best of the three nonadaptive orbit contractions on the
same eigenstate.

| `L` | domain | `K` index | phase | `mu_carry` | `w_proj` | contact | adaptive overlap | best fixed overlap |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 3 | training | `(1,0,0)` | 0.960405 | 2.560872 | 1.351e-2 | 0.339197 | 0.913835 | 0.902978 |
| 4 | training | `(1,1,1)` | 0.764631 | 1.670171 | 4.533e-6 | 0.582735 | 0.701773 | 0.508536 |
| 5 | held | `(1,1,1)` | 0.314578 | 0.294437 | 6.156e-5 | 0.378211 | 0.796847 | 0.309625 |
| 6 | held | `(1,0,0)` | 0.181302 | 0.098341 | 4.406e-5 | 0.587707 | 0.682418 | 0.189253 |

The table exposes the central caveat rather than hiding it. `L=3` already has
a strong fixed perpendicular-orbit witness. The higher adaptive overlaps at
`L=4,5,6` depend on cancellations among scalar channels and have much smaller
projected weight, even though that weight remains above the declared floor and
is numerically selector-stable. The held fixed-orbit overlaps are weak. Thus
the held result supports existence in the declared adaptive scalar span, but
does not yet supply a preferred observable or robust fixed projection.

Across the selected witnesses, eigenpair residuals are below `1.5e-15` and
the smallest returned local eigenvalue gap is `3.56e-4`. The exact complex
adaptive coefficient vectors, fixed-channel metrics, pole margins, and
normalized Green residuals are emitted by the executable.

## Selector stability, covariance, and endpoint controls

For each selected witness, the eigenproblem is rerun with a different
deterministic start vector and with candidate counts `8` and `10`. The runner
compares eigenvalue, phase-agnostic state overlap, adaptive profile overlap,
Green score, and contact fraction. This selector stability control is needed
because a raw eigenvector inside a degenerate eigenspace would otherwise be
an arbitrary numerical basis choice.

For the selected `L=3` nonzero-`K` witness, every one of the all 24
proper-cubic frames is tested. A frame `R` maps the update at `K` to the update
at `R K`, maps the eigenstate into the corresponding momentum sector, and
rotates the adaptive profile spatially. The isotropic comparator and the
three orbit masks make the adaptive selector itself covariant; the runner
checks both profile and coefficient residuals after the one irrelevant common
phase is aligned.

At the `theta=0` parameter endpoint, the selected nonzero-coupling witness is
not retained as the same eigenpair. This is an exchange-dependence control,
not deletion of the update or evidence that the endpoint is physically
forbidden.

## What this does and does not establish

This hunt strengthens the earlier carried-mode evidence in one narrow way:
the carried update does contain bounded-volume, nonzero-momentum eigenstates
whose suitably declared scalar projections are materially less
contact-supported and more Green-like than the previously selected
source-bright contact branch. It also makes the selector freedom explicit and
tests it under the declared held sizes and frame covariance.

It does not establish a unique or continuing branch, asymptotic `1/r`
behavior, a source law, or a physical coupling constant. The adaptive
projection and finite
spectral window are supplied analysis structure. The eigenphase is not
physical energy; the eigenphase is not a rate. The conserved `Q` sector is
not a gravitational source. This is not gravity, makes no no-go claim, and
creates no axiom pressure.

## Prior-art and novelty boundary

Finite-volume momentum reduction, sparse eigenpair search, lattice resolvents,
group-orbit contractions, least-squares projection, and held-size numerical
checks are standard tools. The campaign-local contribution is their explicit
composition on this carried one-matter update, including the basis-spanning
nonzero-`K` lift, the complete three-orbit scalar selector inventory, the
residual-matched comparator score, and proper-cubic covariance of the adaptive
search witness. No external prior-art engine is extended here.
