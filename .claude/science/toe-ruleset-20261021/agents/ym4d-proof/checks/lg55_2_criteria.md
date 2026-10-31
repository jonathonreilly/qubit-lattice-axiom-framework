# lg55_2 — criteria (written BEFORE the script; LARGE55.md §3 "soft-specific phenomenon", §6 tower/dilution item)

Author: claude-opus-5-5. Written 2026-10-29 (UTC), before lg55_2_s4p.py exists.

## Object (exact; PROOF.md `S4' [S3] Order-averaged averaging` and `Decision 4: the RG kernel`)
Fine lattice Z^d, L odd, m = (L-1)/2. Coarse site X has block B(X) = {LX + z : z in {-m..m}^d}, centre c_X = LX.
Coarse link c = (X, mu): for every coordinate order sigma (d! of them) and every y in B(X):
T^sigma_y = P^sigma(c_X -> y) . S_y . P^sigma(c_Y -> y + L e_mu)^(-1), c_Y = c_X + L e_mu, where P^sigma moves the coordinates
in the order sigma (complete-axial), S_y is the straight leg of L steps in +e_mu.
**Abelian linearisation** (the first-order response of the S4' mean to small link perturbations): link angle a_b; the angle of
a path is the signed sum of its link angles (+ for a step +e_nu along link (s, nu), - for a step -e_nu along link (s - e_nu, nu));
the linearised angle of M̄_c is theta(c) = sum_b w^c_b a_b with w^c_b := (d! L^d)^(-1) * (signed incidence count over all
(sigma, y)). Coarse plaquette (X; mu<nu): Theta = theta(X,mu) + theta(X+e_mu,nu) - theta(X+e_nu,mu) - theta(X,nu).

## Computations, for (d, L) in {(2,3), (2,5), (3,3), (3,5), (4,3), (4,5)}
- w^c for the 2d coarse links c incident to coarse site 0.
- For every fine link b with both endpoints in B(0): the response Theta_P(delta_b) for all coarse plaquettes P containing
  coarse site 0 (these are the only coarse plaquettes such b can affect; asserted and checked: every coarse link with
  w^c_b != 0 for such b is incident to coarse site 0 — gate G0).
- R1 := max over such b and P of |Theta_P(delta_b)|; R1c := the same max restricted to the 2d fine links incident to c_0.

## Gates (PASS/FAIL pre-registered)
- G0: every coarse link (within the coarse ball of radius 2 around 0) whose weight map reads a link with both ends in B(0) is
  incident to coarse site 0.  PASS iff true for every (d, L).
- G1 (control, exact): for a pseudo-random integer gauge function omega on fine sites (fixed seed), a_b = omega(head) - omega(tail)
  gives Theta_P = 0 for all P containing coarse site 0; AND for a pseudo-random non-gauge a (fixed seed) at least one Theta_P != 0
  (shows the gate can fail).  PASS iff both hold for every (d, L).
- G2 (first-link formula derived in LARGE55): for c = (0, mu) and every signed direction +-e_nu (nu any coordinate, mu included),
  the fraction of (sigma, y) whose first segment P^sigma(c_0 -> y) starts with that step equals (L^d - 1)/(2 d L^d), and the
  fraction with an empty first segment (y = c_0) is 1/L^d.  PASS iff exact equality for every (d, L, mu, nu, sign).
- H3 (hypothesis): max_{c incident to 0, b} |w^c_b| < 1/2 for every (d, L).  PASS iff true.
- H4 (hypothesis, dilution at the linear level incl. the block-centre hub): for d = 4: R1 <= 1/4 for L = 3 and L = 5, and
  R1(L=5) < R1(L=3).  PASS iff all three hold.
- H5 (hypothesis, two levels at a deep centre): perturb the single fine link b_0 = (c_0, e_1). Its level-1 response theta^(1) is
  supported on the 2d coarse links incident to coarse site 0 (checked). Treat level 1 as the fine lattice of the next step: coarse
  site 0 is the centre of its level-2 block. Level-2 plaquette response Theta^(2)_P = sum over level-1 links of theta^(1) times the
  level-2 weights (same construction one level up). R2 := max_P |Theta^(2)_P| over level-2 plaquettes containing level-2 site 0,
  R1(b_0) := max_P |Theta^(1)_P| for the same perturbation. H5: R2 <= R1(b_0)/2 for d = 4, L = 3 and L = 5.  PASS iff true.
A FAIL of H4 or H5 is a first-class result (the dilution argument of LARGE55 §6 fails at the linear level) and is reported as such.

## Report-only
R1, R1c, R1(b_0), R2 for every (d, L); the decomposition of theta^(1)(b_0) on the 2d links at coarse site 0 into the pure-gauge
pattern (omega(0) = -1/(2d) * (L^d - 1)/L^d) and a remainder (max |remainder| reported).

## Limits
Pure python, fractions only; wall-clock < 10 min, memory < 2 GB; exit 0 and empty stderr for any PASS to count.
