# T06 pre-registration (written before running hemi_test.py)

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks).

## What is tested
Route R1 (measure typing): the axioms type the Admissibility law as a probability MEASURE on the
possibility domain (AX:69-73), records lock a point, readout is a function of content (AX:82-84).
Take the domain to be the Bloch sphere S^2 (unit vectors of Cl(3,0)) and readouts to be covariant
hemisphere signs r_n(u)=sign(n.u). Then "menu independence" is automatic (each menu is a partition
of one measure). Claim L (lemma): with density f w.r.t. normalised Haar, the hemisphere readout is
H f(n) = int_{n.u>0} f dmu, diagonal on spherical harmonics with eigenvalue
c_l = (1/2) int_0^1 P_l(t) dt: c_0=1/2, c_1=1/4, c_l=0 for even l>=2, c_l != 0 for odd l.
Consequences claimed:
 (C1) Born-exactness for ALL hemisphere readouts <=> odd part of f is the pure dipole 2 r.u; the even
      part is unconstrained (any even function).
 (C2) A density that is affine in the state (1 + a.u) is positive iff |a|<=1, so it reaches Born
      purity r=|a|/2 <= 1/2 only ("factor-two", generalising the 2026-09-04 note from the round
      affine family to every density with a dipole-only odd part).
 (C3) The Kochen-Specker density 4 (q.u)_+ is Born-exact (cos^2(theta/2)) and has pure-dipole odd part.
 (C4) Zero forcing power: positivity + covariance + antipodal normalisation + endpoint certainty
      g(0)=1 do NOT force Born in measure typing (power kernels c_k (q.u)_+^k, k != 1, satisfy all).
 (C5) Preparation contextuality footprint: KS densities of I/2 from two decompositions differ while
      every hemisphere readout agrees.
Route R2 (outside, Wootters-type uniform distinguishability): among covariant antipodal-normalised
binary odds g(theta) that are C^1 on the sphere (g'(0)=g'(pi)=0) and monotone, constant Fisher
information I(theta)=g'^2/(g(1-g)) singles out Born with purity 1, g=cos^2(theta/2), and nothing else.
Side check F: the finite fixture law mu_A(1|n)=(n+1)/8 (L02-W5) is not a records-as-fields
(Heisenberg, thermal) law for any beta.

## Pass / fail readings (fixed now)
A. Funk-Hecke: numerical hemisphere transform of P_l(u.q) equals c_l P_l(cos theta) to <=1e-8 for l<=9,
   and even l>=2 give |value|<=1e-8. FAIL of A kills R1's lemma (then the classification is wrong).
B1. KS hemisphere prob = cos^2(theta/2) to <=1e-8; its Legendre odd part has only l=1.
B2. Adding random even perturbations leaves all hemisphere probabilities unchanged to <=1e-8.
    If they change, C1 (even part free) is false.
B3. Dipole-only density positivity boundary at |a|=1 => max Born purity 1/2.
B4. Gibbs kernels e^{beta t}: nonzero odd content at l>=3 and hemisphere prob non-affine for beta>0.
B5. Power kernels k!=1 satisfy positivity, covariance, antipodal normalisation, g(0)=1 but differ from
    Born. If instead k!=1 violates one of these, C4 is unsupported and R1 would have forcing power.
B6. Two KS decompositions of I/2: L1 density distance > 0.1 while max hemisphere-prob difference <=1e-8.
C.  R2 passes iff among {Born lambda in (0.5,0.8,0.95), Gibbs tanh, power k=0,2,3,4, T3-type, cone
    kappa=1/2} exactly Born lambda=1 (and its sign flip) has I(theta) constant to 1e-6 AND is C^1
    and monotone. Any other constant-I member that is smooth and monotone kills R2's uniqueness claim.
F.  For beta in a fine grid, max_n |P_thermal(1|n) - (n+1)/8| >= 0.02 at its minimum over beta.
    If some beta gives <0.02 the fixture would be a records-as-fields law.

## Verdict rules
- R1 "moves" the wall iff A, B1, B2, B3, B5 all pass: menu independence/abundance are not part of the price
  in the axioms' measure typing, and the residual clause is the dipole-only odd part.
- No test here can pass the wall: the dipole clause is not derived from any axiom. So the best possible
  outcome from this test is PRICED (or MISFRAMED for the menu/abundance formulation), never PASSED.
- If B5 shows Born is forced by positivity/endpoints, R1 would be stronger than I expect; report it.

## ADDENDUM (written after run 2 of hemi_test.py, before running hemi_test_E.py)
Part E was added after seeing that positivity might trim the space of hemisphere laws. Claims:
 (E1) A hemisphere law g (antipodal normalised, axisymmetric) is realised by a positive measure iff
      mean|f_odd| <= 1, where f_odd = H^{-1}(g - 1/2) via Funk-Hecke (f_odd = sum a_l P_l, a_l = coeff_l / c_l).
      Proof sketch: f = 1 + E + f_odd with E even, mean 0; f(u), f(-u) >= 0 iff 1+E >= |f_odd|.
      For Born g=(1+lam t)/2, mean|f_odd| = lam.
 (E2) Lane witness g=(1+t^3)/2 has f_odd = 6t - 8t^3 and mean|f_odd| = 1.25 > 1: NOT realisable.
 (E3) Lane witness g=(1+t)/2 + t(1-t^2)/8 has f_odd = t + 2t^3, mean|f_odd| = 1.0: realisable, and the
      density 2t+4t^3 on t>0 (zero on t<0) reproduces g by quadrature to <=1e-8.
 Fail readings: E2 value <= 1, or E3 density not reproducing g, or E1's Born value != lam.
Run history is kept in RUNLOG.md (run 1 had quadrature/threshold slips; they are reported, not hidden).
