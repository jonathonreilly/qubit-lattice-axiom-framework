---
claim_id: candidate_law_cl2_a_records_qubit_leaves_the_flow_evidence_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Exact neutralized torus Green identities, finite Dirichlet obstacle and static pinning mathematics, and explicitly supplied finite scalar packet/trace diagnostics; no physical record-to-gravity bridge or universal dynamics classification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/candidate_law_cl2_a_records_qubit_leaves_the_flow_evidence_2026_10_18.py
---

# Supplied scalar flow rules: exact identities and finite diagnostics

Claim type: bounded_theorem.
Primary runner: `scripts/candidate_law_cl2_a_records_qubit_leaves_the_flow_evidence_2026_10_18.py`.

The [proposal register](CANDIDATE_LAWS.md) is provenance context with zero premise weight. Its reported approval quotations are unverified in this review, not declared false or globally absent. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the scalar fields, updates, weights or readouts below. This note derives consequences of those explicitly supplied choices. Numerical output must come from the corrected source's fresh capture; original cache numbers are historical and are not substituted here.

## Periodic Green functions and source projections

On an even cubic torus let A be the six-neighbor average and chi(x)=(-1)^(x+y+z). Fourier eigenvalues of A are (cos kx+cos ky+cos kz)/3. The pseudoinverses Rplus=(I-A)^+ and Rminus=(I+A)^+ use zero on their respective null spaces. For every source s,

    (I-A) Rplus s = s - mean(s),       mean(Rplus s)=0,
    (I+A) Rminus s = s - chi mean(chi s),
    mean(chi Rminus s)=0,
    Rminus s = chi Rplus(chi s).

The first equation follows mode by mode, with the constant mode deleted; the second deletes the checkerboard mode. Multiplication by chi conjugates A to -A, proving the third identity including its gauge. A nonzero total source on a torus therefore includes a compensating uniform background. The staggered analogue depends on the signed checkerboard total, not the ordinary total. The runner checks the full equations and gauges for an arbitrary seeded source as well as the three original symmetric finite source proxies. Agreement at one radius is not a theorem of shape independence for every far field, and the two sign choices do not exhaust admissible dynamics.

## Dirichlet floor and static identities

On the interior of the finite cube with boundary p=1, the supplied floor rule is

    p_i=max((A p)_i-q r_i,0).

Equivalently p>=0, w=(I-A)p+q r>=0 and p_i w_i=0 at every interior vertex. The fixed boundary is separate from the free obstacle sites. The Dirichlet matrix I-A is positive definite: its quadratic form is a positive multiple of the sum of edge differences squared, including edges to fixed boundary values. Every interior component reaches that boundary. Consequently the strictly convex obstacle energy has a unique minimizer, and its first-order optimality conditions are precisely the complementarity equations. The primary uses a primal-dual active set which can release sites; every linear solve checks GMRES status, finite entries and normalized equation residual. Acceptance additionally requires the full local fixed-point and complementarity residuals. Exhausting the iteration cap is failure.

At a nonsource interior vertex, a zero solution would have nonnegative neighbors of average zero, so all its neighbors would be zero. Along a source-free path to boundary1 this is impossible. Thus the connected source-free exterior is strictly positive. The former permanently unioned zero set was a different irreversible clamping construction; its enlarged zero region is not evidence for this floor equilibrium. The full original algorithm remains recoverable, with that interpretation explicitly superseded.

For the separate graph-hole problem, delete the hole vertices and edges incident on them. Constant one is harmonic on the live graph. If every live component reaches the fixed boundary1, positive-definiteness/maximum principle makes it the unique solution. This is a uniform-boundary identity, not a statement about holes under arbitrary nonconstant flow.

If p already solves a static Dirichlet problem, pinning additional vertices to their existing p values leaves p a solution. Uniqueness gives the same equilibrium. This says nothing about arbitrary nonequilibrium formation events. The primary's twelve pins test only this static statement.

For fixed Dirichlet data, the deficit's response to source amplitudes is linear. Exact superposition follows from the inverse matrix. A proxy sampled at one observation point is a linear combination with coefficients given by the corresponding Green row; those coefficients depend on source position. The one-versus33-source comparison is therefore approximate finite geometry, not exact equality of a physical mass per record. Absorber and multiplicative-drain numbers are freshly printed diagnostics, with no inherited rounded values asserted here.

## Scalar packet and delay experiments

The supplied wave update is v_next=v+dt Delta u/m, u_next=u+dt v_next, with m=(1+Phi)^(-4). In the smooth constant-coefficient limit its speed is 1/sqrt(m)=(1+Phi)^2, and inverse speed is 1-2Phi+O(Phi^2). This explains the chosen weak-well comparison conditional on this scalar equation, not universal equivalence for arbitrary species.

The 2D packet uses k=.6, dt=.4 and is sampled at T=260 in 140<X<280. The homogeneous discrete carrier velocity is cos(k/2)/sqrt(1-dt^2 sin^2(k/2)); its nominal first X-boundary crossing from X=-40 is later than this sample. The primary also reports the actual longitudinal peak, detected u^2 fraction and maximum u^2 fraction in ten-site boundary strips over the run, failing if the detection/contamination guards are not met. These are finite amplitude diagnostics; u^2 is a chosen weight, not the conserved wave energy. The old T500, X>200 statistic was after nominal wrapping and cannot certify outgoing bending.

The separate 1D delay comparison retains three packets, widths and windows. Its first two declared tolerances are respectively6% and8%; the short-wavelength comparison remains a finite dispersive observation. The 2D random-slab experiment reports excess crossing time divided by100 sites, using its fixed seed, fractions and window. This quantity is not fractional speed loss. If a unit reference speed and uniform100-site slab accounted for the entire delay d, speed loss would instead be d/(1+d). Two realizations establish no universal coefficient.

## Exact mean of the undamped torus update

For d_(t+1)=2d_t-d_(t-1)+s(Delta d_t+source_t), torus summation gives

    mean(d_(t+1))-2mean(d_t)+mean(d_(t-1))=s mean(source_t).

With both initial fields zero, s=1/4 and constant point source.3 on80^3 sites,

    mean(d_t)=.075 t(t+1)/(2*80^3).

With source12 only on step1, mean(d_t)=3t/80^3. For the separately imposed absorber pin, the mean recurrence includes the actual pin correction divided by80^3. The primary verifies each recurrence at every step. Nonzero undamped modes may oscillate and recur; four r10 samples at ticks56–68 remain finite traces, not stationarity or a spatial1/r proof. Changing to damping, neutralization or different boundaries would define another model requiring its own analysis.

## Evidence and deferred scope

The owning primary enforces a1500-second aggregate timer, rejects optimized Python, streams diagnostics, fails closed on uncertified solves, and prints five resolution statements plus actual check totals. All literal inputs, source and authority identities are bound. No fresh result is claimed until owner capture succeeds.

The useful conclusions are the exact projected Green, convex obstacle, static graph and mean-recurrence results, together with conditional finite diagnostics. Physical source/record identification, a conserved physical functional, universal attraction/equivalence, exhaustive dynamics selection and unrestricted screening/uniqueness claims remain deferred. The original generic route list is preserved only as history and is not represented as a qualifying no-go packet. Exact five-file recovery is in `archive/record_flow_review_2026_10_18/MANIFEST.json`.
