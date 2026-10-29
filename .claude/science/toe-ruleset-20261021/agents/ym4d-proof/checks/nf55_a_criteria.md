# nf55_a — criteria (written before nf55_a.py exists)

Owner: NONFREE55 (claude-opus-5-5). Exact rational arithmetic only (sympy Rational / python Fraction); no floats in any verdict.

Objects. G~(z) := 1/|z|^2 (= 4 pi^2 G_0; all propagators below are in units with the factor 1/(4 pi^2) removed).
Feynman-gauge potential correlator <A_a(x) A_b(y)> = delta_ab G~(x - y). F_{mu nu} = d_mu A_nu - d_nu A_mu.
The script must BUILD the field-strength correlator D~_{mu nu, rho sigma}(z) = <F_{mu nu}(x) F_{rho sigma}(y)>, z = x - y,
by applying the antisymmetrised derivatives to the potential correlator (d^y = -d^z), not by typing the final formula.
Ordered index pairs I = (mu, nu), mu != nu (12 of them; F_{mu mu} = 0).

Points: P1=(1,0,0,0) P2=(0,0,0,2) P3=(1,1,0,0) P4=(1,2,3,4) P5=(2,-1,3,5) P6=(3,3,3,1).
Configurations: Q1 = {(0,0,0,0),(1,0,0,0),(0,2,0,0)}; Q2 = {(0,0,0,0),(1,2,0,1),(-1,1,3,0)};
Q3 = {(1,0,0,0),(0,1,1,0),(2,3,-1,1)}; R1 = {(0,0,0,0),(1,0,0,0),(0,2,0,0),(0,0,1,3)}.

Gates (registered PASS conditions):
- A1 (gauge independence of the F correlator). Add the pure-gauge term d_a d_b H(z), H = log|z|^2, to the potential
  correlator. PASS iff all 144 components of the resulting F correlator equal D~ exactly at P3, P4, P5, P6.
  Control A1-F: with the symmetrised (wrong) F^s_{mu nu} = d_mu A_nu + d_nu A_mu the same pure-gauge term must change at least
  one component at P3. The control FIRES if the difference is nonzero. If it does not fire, A1 is not evidence.
- A2 (free-gluon composite two-point coefficient). |z|^8 * sum_{I,J} D~_{IJ}(z)^2 = 384 exactly at P1..P6.
  PASS iff all six values equal 384. (Meaning: sum D^2 = 384/(16 pi^4 |z|^8) = 24/(pi^4 |z|^8), hence
  <:F^aF^a:(x) :F^bF^b:(0)> = 2 (N^2-1) * 24/(pi^4|x|^8) = 48 (N^2-1)/(pi^4 |x|^8).)
  Control A2-F: the same sum with the fourth term (delta_{mu rho} d_nu d_sigma) of the correlator omitted must differ from 384 at
  P3. FIRES if it differs.
- A3 (three-point function of the one-colour composite :F_I F_I:, electric-magnetic duality prediction). T3 computed by
  brute-force enumeration of all perfect matchings of the six fields with no same-point pair. Registered prediction:
  T3 = 0 exactly at Q1, Q2, Q3 (Euclidean F.F continues to a multiple of B^2 - E^2, odd under the unitary duality rotation of
  free Maxwell theory [m]). PASS iff all three values are exactly 0. A nonzero value is recorded as FAIL and the text must follow
  the computed value.
  Control A3-F: the same enumeration code applied to the scalar composite :phi^2: (propagator G~) must return a NONZERO value equal
  to 8 G~(x-y) G~(y-z) G~(z-x) at Q1. FIRES if nonzero and equal.
- A4 (four-point truncated function of the one-colour composite is nonzero). T4 := sum over perfect matchings of the eight fields
  with no same-point pair whose pair-graph on the four points is connected (brute force), at R1. Independently, the cycle formula
  16 * sum over the 3 Hamiltonian 4-cycles of the index contraction of four D~ factors. PASS iff the two agree exactly AND
  T4 != 0.
  Control A4-F: adding the disconnected (2+2) matchings must change the value at R1 (FIRES if the disconnected part is nonzero),
  showing that the truncation is not vacuous.

Verdict: PASS iff A1, A2, A3, A4 all PASS and all four controls fire; otherwise FAIL (recorded as such).
Resources: plain python3 + sympy (pure Python). Expected < 2 min, < 200 MB.
