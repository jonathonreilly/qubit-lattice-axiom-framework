# T42 pre-registration (written before any script was run)

Author: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check).

## Question
Which premise carries the load in T42 (strong CP, gauge side)?
- H_L: the locality licence (unit-neighbourhood link-support licence, packet P-FUND-1TICK,
  docs/PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md)
  protects theta_gauge on its own, at the marginal level and stably under effective-action generation.
- H_S: the protection is a symmetry / positivity class that is closed under effective-action
  generation (positive reflection-positive measure, or an improper symmetry). The licence only
  removes the *reviewed* carriers at tree level.
- H_R: the record-Gibbs range theorem (docs/ADMISSIBILITY_RULE_RECORDED_SET_GIBBS_THEOREM_...2026-09-15.md,
  T2/T5) supplies the licence from the Admissibility axiom, so P-FUND-1TICK is derivable.

## Tests (all exact, deterministic; scripts census.py and parity.py in this folder)
A. Licence census. Licence (V) = for every target link l=(a,b) and every endpoint p of every support
   link, min(d(p,a),d(p,b)) <= 1 (verbatim from the 06-09 / 06-11 notes). It is pairwise, so licensed
   supports are cliques of a compatibility graph. Enumerate all maximal licensed supports in Z^3 and Z^4.
   PREDICTION: exactly the vertex star (6 links in Z^3, 8 in Z^4) and the plaquette (4 links), up to symmetry.
   FALSIFIER: any other maximal licensed support (e.g. one holding a link perpendicular to a plaquette).
B. Marginal pseudoscalar carriers. Enumerate two-object supports over translation windows |t|_inf<=3:
   (link,plaquette) with the link normal to the plaquette (Hamiltonian E.B), (link,link) with distinct
   directions displaced along the third axis (E.curl E), and in Z^4 (plaquette,plaquette) in complementary
   planes (clover F Ftilde). Also all licensed two-object supports that span all axes.
   PREDICTION: 0 licensed.  FALSIFIER: >= 1 licensed.
C. Closure. Take licensed supports that share a vertex (vertex star with a plaquette through it).
   PREDICTION: the union is NOT licensed and contains the E.B support (so the licence is not closed under the
   supports an interacting theory generates at second order).  If the unions stay licensed, H_L is alive.
D. Record-Gibbs range (site language, fundamental Z^3): for all 24 orders of a plaquette's four sites,
   is the plaquette a clique of G_sigma (adjacent pairs plus pairs co-recorded by a later common neighbour)?
   PREDICTION: 0 of 24 (so a Wilson 4-body plaquette term is not a record potential).  FALSIFIER: >= 1.
   Then on the doubled lattice (edge sites = one odd coordinate): are the maximal licensed link supports
   exactly the maximal sets contained in a closed unit neighbourhood N(y)?  PREDICTION: yes.
E. Operator parity by orbit sums (abelian link variables E_l, sin/cos of plaquette angle, geometric action of
   the 24 proper rotations, translations quotiented). For each monomial m: OS_O(m)=sum over proper rotations,
   OS_sigma(m)=sum over the improper coset, D=OS_O-OS_sigma (nonzero D <=> a P-odd covariant operator exists).
   PREDICTIONS: (i) sin(plaquette) orbit sum is 0 (proper covariance alone kills the reviewed single-plaquette
   CP-odd slot); cos(plaquette) is nonzero and P-even. (ii) every monomial on a plaquette support has D=0.
   (iii) E_z sin(P_xy) and E_x E_z(displaced along y) have OS nonzero and D nonzero. (iv) on the six-arm abelian
   star the lowest degree with D != 0 is >= 3 (three field factors). (v) SU(2): epsilon^{abc} J1^a J2^b J3^c on
   three adjoint links is nonzero, Hermitian, cyclic-invariant and odd under an arm swap.

## Reading map
- A,B,C,D as predicted: the licence removes the marginal carriers but is not closed and cannot come from the
  nn Admissibility rule on the fundamental lattice. Then T42 is PRICED at a closed class (positive RP measure or an
  improper symmetry), not at the licence. W3 (no integer Q) is idle either way.
- C fails to fail (unions licensed): H_L is alive; price would be P-FUND-1TICK alone.
- B finds a licensed carrier: licence does not even protect at tree level; wall STANDS harder.
- D finds a clique: the Gibbs route derives the plaquette from Admissibility (would move the wall).

## Test F (added before running mc.py): price of the constraint-sector route (Luscher admissible fields)
Route 3 would give an integer sector functional Q only on fields whose plaquettes all satisfy
||1 - U_p|| < eps (Luscher, Commun. Math. Phys. 85 (1982) 39; the eps needed is small, of order 1/30 for SU(3)
in the locality literature; the number is quoted from memory and is not used: the test scans eps).
mc.py: SU(3) Wilson Metropolis at the repo's canonical beta = 6 on a 4^4 torus (seeded); anchor <P> near 0.5934.
PREDICTION: fraction of plaquettes with ||1-U_p|| < 1/30 is below 1e-3, and (fraction)^(number of plaquettes)
is below 1e-100.  FAIL READING (route not priced out): fraction above 0.5 for some eps <= 0.1.
