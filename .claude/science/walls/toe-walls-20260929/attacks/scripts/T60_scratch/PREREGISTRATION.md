# T60 pre-registration (written 2026-09-29 before any T60 script was run)

Wall: vacuum energy and the zero of energy (L13-W1 the 1e123 mismatch; L14-W18 which zero the
gravity member sees). Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor).

Working hypothesis (to be attacked): the walker sea's energy per site I ~ 1.19 (hop units) cannot be
removed by any fixed reading of the source; every reading of "what the member sees" moves the same
number I around (sea, sea removal, record birth cost) or leaves an m^2 residual. So T60 is priced at
a supplied source reading plus the realized state's record density, and the 1e-123 itself is T62's
R_Lambda/a in other units.

## Setting (all supplied, none adopted)
Free two-coin walker H = sum_j sigma_j sin k_j / ell (block 147's setting), staggered mass block for
the massive case (A = sigma.s tau_z, B = mu tau_x), hard-core one-record-per-site hopping (axiom
Record) on small bipartite tori for the many-body checks. Planck bridge a = l_P (scale primitive).

## Tests (numbers only; nothing here is a proof of a general statement)
 A1 reproduce the wall's own numbers: log-det per cell -0.667/-0.866/-1.068 (m = 0.3/0.7/1.0);
    I(inf) = <|s|> = 1.19380; I(4^3) = (3 + 3 sqrt2 + sqrt3)/8; T03's cost per record 2.387602 = 2 I.
    PASS = all reproduce to 3 digits (the wall is stated correctly); FAIL = any misstated.
 A2 equation of state by finite differences on exact spectra: free massless sea and exact hard-core
    ground state (4x4 torus, half filling): p/rho. Prediction 1/3 exactly (scale covariance H_ell =
    H_1/ell), so no state of massless hopping is Lambda-like. FAIL of prediction = any state with
    p/rho <= 0 at massless hopping.
 A3 dilution bounds. (a) stretch: ell_needed = (I/1.1e-123)^(1/4) l_P in metres. PASS-for-route
    (stretch dilutes the sea to the observed value harmlessly) iff ell_needed * l_P < 1e-19 m
    (collider reach). Prediction: FAIL by ~15 decades in length. (b) coarse lattice: floor on
    |rho_sea|/rho_P at a = 1e-19 m. PASS iff <= 1e-100. Prediction: FAIL (~1e-63).
    (c) empty-born growth: sea energy fixed, volume grows: needed volume ratio 1e123 vs sites in the
    Hubble volume ~4e183. Prediction: PASS arithmetically (this route's price is formation law, T01).
 A4 records-only (pinched) source: exact identity D(H_hop) = 0, so a massless packet keeps 0 of its
    gravitating weight; massive keeps m^2/E^2. Residual sea source r(m) = -(m^2/2) J(m), J = <1/E>.
    PASS-for-route iff residual/rho_P <= 1e-100 for the heaviest known fermion (top, 173 GeV) AND
    massless packet retains >= 0.5 of its weight. Prediction: FAIL both (residual ~1e-34, weight 0).
 A5 no fixed zero works across record density (hard-core torus, exact e(n) = E0(n)/N):
    Z_A = record-free zero, source e(n); Z_2 = sea-referenced zero, source e(n) - e_min;
    Z_3 = same-record-number ground state, source 0, leftover = formation term mu(n).
    PASS-for-route (a fixed zero suffices) iff max_n |leftover|/|e_min| <= 0.01 for Z_A or Z_2.
    Prediction: FAIL (max = 1 at n = 1/2 for Z_A, at n -> 0 for Z_2); mu(n) spans +/-band edge for Z_3.
 A6 no equilibrium (Volovik/Gibbs-Duhem route): dE/d ell for sea + rest mass, massless and massive.
    PASS-for-route iff dE/d ell changes sign at some finite ell. Prediction: FAIL (monotone, > 0).
 A7 shear lemma (only if time): hard-core 4x4 ground energy under volume-keeping shear t_x = e^s,
    t_y = e^-s satisfies E0(s) <= cosh(s) E0(0) (convexity + homogeneity + x<->y symmetry).

## What would change my reading
 - A1 mismatch: the wall is misstated (report it).
 - A2 finds p/rho != 1/3 for massless hopping: the "sea is never a Lambda" claim is wrong.
 - A3(a) passes: stretch route alive (lattice can dilute the sea harmlessly).
 - A4 residual small AND massless weight retained: a records-only source is a real route.
 - A5 finds a fixed zero with leftover <= 1% at all n: the zero of energy is fixed by the record
   ontology (a pass of L14-W18).
