# T74 pre-registration (written before any run)

Attacker: Claude Sonnet 5.5 (same family as supervisor). Date 2026-09-29.

## Question tested
W3's own "cheapest test": compute the area-law coefficient eta (nats per unit
Euclidean area, lattice units a=1) of the framework's own half-filled sea, with
no selector, and ask (a) does it land on 1/4 (or 1/6)? (b) is it a single
number, i.e. independent of cut orientation and of the free mass parameter?

Model (declared, not derived): the pi-flux cubic hopping sea of
docs/HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_...2026-09-02.md
(all face holonomies -1), infinite-volume dispersion E^2 = 4 sum cos^2 k + m^2
(m = staggered mass, m=0 is the repo's sea; eight Dirac points, no Fermi
surface). Gauge eta_x=1, eta_y=(-1)^x, eta_z=(-1)^(x+y). Ground state: all
E<0 levels filled.

## Method
M1 (100 cut, high accuracy): translation-invariant transverse momenta, periodic
   chain of Lx slices with 4 orbitals each, region = half the chain, two cuts.
M2 (100/110/111, torus): real-space L^3 torus with antiperiodic BC (no zero
   modes for L = 0 mod 4), region = {(h x + k y + l z) mod L in [0, L/2)}, two
   planar cuts, plane Euclidean area = L^2 sqrt(h^2+k^2+l^2).
eta = S_A / (2 * plane area). Also g_thermo = 1/(4 eta).

## Pre-registered readings
PASS (native sea supplies the quarter with no selector):
   eta_hkl(m=0) = 0.25 +- 2% for all three orientations in the L->infinity
   trend, AND max/min over orientations < 1.03.
FAIL (wall W3 stands as stated; entropy-side 1/4 is not native):
   any orientation differs from 0.25 by > 5%, OR orientation spread > 5%.
Additional readings (about the misframing claim, not pass/fail for W3):
   (i) ANISOTROPY: if max/min over (100),(110),(111) > 1.05 at m=0, then a
       single "entropy per Euclidean area" does not exist on the fixed cubic
       grid, so "1/4 vs 1/6" is ill-posed there.
   (ii) PARAMETER DEPENDENCE: if eta(100, m=1)/eta(100, m=0) differs from 1 by
       more than 10%, the coefficient moves by O(1) with an unfixed dimensionless
       parameter m/t, so hitting exactly 1/4 is a tuning (the same as W3 says
       of the April bands).
   (iii) g_thermo = 1/(4 eta) will be quoted for scale only: it is the Newton
       constant a Jacobson-type equation of state would need, not a derived G.
My prior (before running): eta in 0.10..0.30, spread among orientations
10-20% (from the gravity-exercise kill3 result on Wilson-Dirac: 16-18%),
mass dependence > 10% at m=1. Expect FAIL.

## Algebra check (separate, exact)
BP chain: c_cell = b * d / 2^d, G_lat = 1/(4 c_cell). Check: G_lat * b is
invariant under b -> lambda b (the coframe note's own remark, lines 326-385 of
PLANCK_PRIMITIVE_COFRAME_..._2026-04-25.md); G_lat = 1 iff b*d/2^d = 1/4
iff (d=4 and b=1) [or other (d,b) pairs on the curve]. Pass reading: the
number 1/4 carries no discriminating content beyond b (i.e. BP <=> b=1 <=> T70).
