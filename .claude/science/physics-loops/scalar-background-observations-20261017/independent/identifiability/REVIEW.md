# Independent FLRW kinematic identifiability check

Scope: exact mathematical check of the proposed lift, no action assumptions, no empirical data, no theorem about general inhomogeneous spacetime.

Let D=L d, c=1, a0=1, L>0 and v=zdot/(1+z), with observer proper time calibrated. FLRW gives H=(1+z)(H0-v) and (H D_z)^2=1-kD^2. Dividing by L^2 gives A(H0-v)^2=L^-2-kd^2, A=(1+z)^2 d_z^2. Thus [A,-2Av,-1,d^2] dot (H0^2,H0,L^-2,k)=-Av^2. The signs and placement of curvature are correct.

Rank four is sufficient for uniqueness of the lifted tuple, but not sufficient for physical consistency. Require theta1=theta2^2, theta3>0, the selected expanding orientation H0-v>0, regularity and admissible radial branch. A finite point fit does not establish the identity between points; extra records are consistency tests. At z=0, regular normalized FLRW also has d(0)=0, v(0)=0 and L H0 d_z(0)=1. Squaring loses radial orientation, so at a closed-universe distance turning point use the appropriate branch, or restrict to d_z>0 and positive radicand.

Rank below four is not equivalent to nonidentifiability. Intersect the affine lifted solution set with theta1=theta2^2 and inequalities. A one-dimensional nullspace generically yields a quadratic with up to two physical candidates, possibly one; some deficient cases leave continua. For example constant H=H0 flat FLRW with d=z and H0=L=1 yields only quadratic row functions and rank at most three. Constant v makes columns one and two dependent.

A regular rank-four counterexample is flat FLRW, D=d=z+z^2, H=1/(1+2z), H0=L=1, k=0 on z>=0. Define t by dt/dz=-(1+2z)/(1+z), and a=1/(1+z); then a_dot/a=H exactly. Drift is v=1-1/[(1+z)(1+2z)]. Four nodes z=1,2,3,4 give matrix

    [ 36,   -60, -1,   4]
    [225,  -420, -1,  36]
    [784, -1512, -1, 144]
    [2025,-3960, -1, 400]

rhs=(-25,-196,-729,-1936). Determinant=23712 and tuple=(1,1,1,0). This is a constructed geometry, not a physically preferred matter solution or empirical fixture. Its decreasing H with increasing z is permitted by kinematics; no energy condition was assumed.

Unknown constant clock gain: for v_obs=g v_true, the data determine only g H0, g^2 L^-2, and g^2 k (and the squared first component). The exact transformation H0->sH0, L->L/s, k->s^2 k, g->g/s leaves the observed equation invariant up to s^2. Thus no absolute H/time, distance or curvature scale is recovered without clock calibration. Dimensionless H0 L and kL^2 are unchanged.

Unknown constant distance gain: d_obs=b d is absorbed by L_fit=L/b. H0,k and physical D=L_fit d_obs are unchanged if the clock is calibrated. The normalization L and b cannot be separately recovered, but this does not by itself obstruct recovery of physical D from the observed shape and clock. A redshift-dependent gain changes shape and is not covered by this cancellation.

The clock-calibrated drift and FLRW interpretation are retained premises. Source peculiar acceleration, redshift calibration, observer terms, finite-baseline drift error and distance derivative estimation are not derived by this lift.

Executable independent construction and two scaling checks: check.py; exact output: result.json.

## Root fixture and rank-deficient checks

Independently verified root's rescaled fixture d=(z+z²)/2 on nodes 1/4,1/2,3/4,1: determinant33/4096 and theta=(1,1,1/4,0). See followup.py and followup_result.json.

The flat constant H=1 fixture is a useful warning: rank3, with lifted nullspace span(1,1,1,1), but intersecting the physical parabola yields only (H0,L^-2,k)=(0,0,-1) and (1,1,0); the first is inadmissible, so the physical solution is unique.

For a genuine continuum degeneracy even with calibrated clock, take v=0 and d=log(1+z). Then A=1, the rows are [1,0,-1,log²(1+z)] of rank2, and all H0>0, L=1/H0,k=0 satisfy the records. This is regular flat FLRW H=H0(1+z), D=log(1+z)/H0. A zero drift contains no absolute clock-rate signal from which to establish the expansion scale.
