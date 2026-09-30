# T02 pre-registration (written before any script was run)

Provenance: Claude Sonnet 5.5, same vendor family as the supervisor; checks are same-family.

## Question the test answers
Wall T02 (no dynamics, nothing selects one). Best route on my reading: the wall is
priced as the dynamics clause (D-dyn + D-perm + D-tr, landed as "supplied, not adopted"
in docs/DYNAMICS_CLAUSE_*_2026-09-24.md). Two sub-questions decide how big the price is:

 Q1 (range). The landed clause SUPPLIES "sum of two-site terms on nearest-neighbour bonds".
    Claim R (mine, untested): that range is not a separate premise. If the odds at an
    isolated forming site are read from the compressed generator (the landed interface),
    and Admissibility says those odds are determined by the six nearest-neighbour records,
    then every generator term must have support on a clique of Z^3 (a site or a bond).
 Q2 (freedom left). How many independent real couplings do the axioms' own symmetries
    leave (a) at bond range, (b) at star range (a site with its six neighbours), under
    (i) possibility covariance SU(2) x proper cubic rotations acting on positions only
    ("unsoldered") and (ii) proper cubic rotations acting on positions and Pauli labels
    together ("full soldering")?

## Script A: T02_scratch/count_covariant_generators.py
Counts translation-invariant Hermitian generators supported inside a translate of the star,
covariant under the stated group, by shape size n, by two independent methods
(character formula; direct nullspace for n <= 4). Then applies the range test: the subspace
whose compressed one-site field h_x(q) depends only on the six NN records (polynomial
reading, injective monomial map).

Pre-registered readings
 - Cross-check: bond-range dimension must be 1 (unsoldered) and 3 (soldered), matching
   the landed note DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_...
   (docs/, 2026-09-24). Any other value = my code or my reading is wrong; report as such.
 - Route survives (PASS for claim R): NN-local subspace dimension == bond-range dimension
   while the star-range dimension is strictly larger (so range genuinely cuts something).
 - Route dies (FAIL): NN-local subspace strictly larger than bond range, or star range
   equal to bond range (then claim R is vacuous).
 - Method disagreement between character and nullspace counts at n<=4: stop, debug, report.

## Script B: T02_scratch/thermal_time_check.py  (outside route: Connes-Rovelli thermal time)
Two adjacent unrecorded qubits with fixed fields from records. Compare the modular
Hamiltonian K = -log(rho) of (a) the product of the one-site odds-marginals, (b) the joint
Gibbs state of the compressed Heisenberg generator.
 - Route would be alive (PASS) if (a) generates entanglement (operator Schmidt rank of
   exp(-iKt) > 1 at generic t). Prediction: FAIL, rank 1, because K is a sum of one-site terms.
 - Also report whether (b) returns the coupling J unchanged (expected: yes, K = beta H).

## Script C: T02_scratch/j_invisibility_check.py
In the compressed-field model with ground-state odds, record-level odds depend on the
scale |J| not at all and on sign(J) only through c = lam*sgn(J). Prediction: exact
invariance under J -> lam*J (lam>0) for the unsoldered branch; for the soldered branch the
odds depend on the ratios K/J and D/J only.

Everything else in the report (Bell necessity, Skolem-Noether, prior-art) is argument, labelled.
