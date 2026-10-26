# Supplied phase and historical ratio comparison

**Claim type:** bounded_theorem
**Date:** 2026-10-24
**Status:** conditional matrix/readout identities and finite bracketed comparisons
**Primary runner:** `scripts/frontier_koide_as_pin_replaces_h_star_witness.py`

This is the ordinary owner of an existing previously unowned computation. Its
historical AS-named filename does not grant an AS/APS physical theorem. The old
source/cache are preserved; their physical/retained/unique-point claims are
withdrawn. No new phase law or absence theorem is asserted.

## Explicit supplied chart and positive diagonal readout

Supply real m, γ=1/2, E1=sqrt(8/3), E2=sqrt8/3, s=sqrt6/3 and
H(m)=H_BASE+m T_M+s T_D+s T_Q, where
H_BASE=[[0,E1,−E1−iγ],[E1,0,−E2],[−E1+iγ,−E2,0]],
T_M=[[1,0,0],[0,0,1],[0,1,0]],
T_D=[[0,−1,1],[−1,1,0],[1,0,−1]],
T_Q=[[0,1,1],[1,0,1],[1,1,0]].
Each summand is Hermitian, hence H is Hermitian. Spectral decomposition gives
exp(H)=U diag(exp(λ_i)) U*, positive definite. Thus its supplied diagonal
readouts v=X33,w=X22 are strictly positive (one-based indices). The fixed unit
clock and diagonal readout are assumptions, not inferred physical observables.

Supply u=2(v+w)−sqrt(3(v²+4vw+w²)). Substitution, or solving the quadratic in u,
gives u²+v²+w²=4(uv+uw+vw). For r=w/v>0, u/v=2(1+r)−sqrt(3(1+4r+r²)).
Squaring the positive comparison shows u>=0 iff r²−4r+1>=0, equivalently
r outside(2−sqrt3,2+sqrt3). The signed quadratic identity still holds outside
that domain, but it is not the positive-mass Q identity there. No positivity
claim for every bracket point is made or used by the four comparisons.

## Independent phase convention

Let ω=exp(2pi i/3). Define b=(w+conj(ω)u+ωv)/3. Since u,v,w are real,
Re b=[w−(u+v)/2]/3 and Im b=sqrt3(v−u)/6; the conjugate Fourier coordinate
is conj(b). In this fixed ordering δ(m)=atan2(Im b,Re b), on its principal
branch when b is nonzero. This particular Fourier orientation is part of the
prescription. It is not silently equated to the differently ordered Fourier
coordinate of another runner or to gauge-invariant Berry holonomy.
On the supplied cone, b cannot vanish: its imaginary part would give v=u and
its real part w=u, while the cone then forces3u²=12u², hence u=v=w=0,
contradicting v,w>0. atan2 nevertheless has a branch cut, so a bracket search
alone is not a global continuous inverse or uniqueness proof.

## Exact input and finite execution scope

The runner independently brackets r(m)=4.100904169382 and δ(m)=2/9 in
[-1.3,−.8], using brentq xtol=1e-12. The ratio is a hardcoded historical
calibration comparator, not recalibrated in this script;2/9 is a supplied
radian target, not derived from an AS index, APS invariant or physical bridge.
Failure to bracket raises an error; no fallback or global existence claim is made.
The four unchanged predicates check:

1. ratio-comparator candidate m lies in(−1.17,−1.15);
2. phase-target candidate residual is less than1e-10;
3. relative difference between the two m candidates is below0.01%;
4. relative ratio difference at the phase-target candidate is below0.01%.

The latter percentages are computed by multiplying relative differences by100.
They do not assert equality or the former stronger0.003% claim. The ratio value
at its candidate is printed; there is no additional scored ratio-residual test.
These are finite checks, not proofs of exhaustive roots, unique physical m,
physical generation labels or observational independence. The old literal-True
D1 narrative is unscored. The complete actual source is self-contained apart
from NumPy/SciPy and the standard library, with this own note declared as input.
The proposed120s cap bounds two small-matrix bracket searches; no measured runtime
or new cache freshness is claimed. Original reviewer source confirmation and
subsequent authorized capture remain pending.
