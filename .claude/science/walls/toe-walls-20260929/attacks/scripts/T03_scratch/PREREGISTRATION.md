# T03 pre-registration (written before any of the scripts below was run)

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks, not referees).
Date: 2026-09-29.

Working hypothesis H*: T03 is not one wall but the two horns of one dilemma that appears
only once a quantum wave W is bought (to escape T08/Bell):
  horn 1 (update):  a sharp per-site lock of a wave costs the coherent-bond energy Tr rho(Phi*(h_x)-h_x);
  horn 2 (ride):    a unitary wave with Born count statistics cannot raise a never-falling count.
and the price of each horn is a supplied number or reading, not an axiom.

## Test 1  (t03_test1_cost.py) -- the cost horn, four variants, Heisenberg 2x2x2 cube (8 qubits, ED)
1a  semantics: energy change of "route-two" algebra refinement (state untouched, H -> E_P(H))
    vs the sharp Kraus update (state -> sum_a P_a rho P_a, H unchanged).
    PASS-for-escape: refinement costs < 10% of the update.   FAIL: they agree.
    Prediction: FAIL (identity Tr rho E_P(H) = Tr E_P(rho) H); both = 3.213393 J (probe 1 T3).
1b  order independence: mean TOTAL cost of locking all sites in one common basis, in 6 random
    orders (exact enumeration of all Born branches).
    PASS-for-escape: some order gives < 90% of the others.  FAIL: all equal (2/3)|E0|.
    Prediction: FAIL (all equal).  => the formation law (T01: order, rate) cannot lower the cost.
1c  growth front: cost of locking corner site x when m = 0..3 of its neighbours are already locked
    (static classical fields on the rest), lock axis = field axis.
    Prediction: monotone decreasing in m, exactly 0 at m = 3.  (cost = coherent bonds cut)
1d  temperature: cost(beta) for Gibbs states of the same cluster, beta in {0,0.05,0.2,1,5,20}.
    Prediction: cost >= 0 for every beta (passivity), -> 0 as beta -> 0 like beta*||h_x - Phi*(h_x)||^2,
    -> 3.213393 J at beta -> infinity.  FAIL of prediction (any cost < 0 for a Gibbs state) would
    refute the passivity argument.

## Test 2  (t03_test2_codex_law.py) -- the repository's OTHER formation model (on main, 2026-09-24):
finite-rate repeated record formation, GKLS creation-only jumps j (N -> N+2, W -> W-1), penalty W,
scripts/repeated_formation_check.py:tree_model, star_2, star_3, star_4, two_A_path.
Question: what does one birth do to the energy in that model's own Hamiltonian?
  H_orig = Delta*N_B + t*T   (Delta = delta/eps^2, t = delta/eps)  and
  H'     = Delta*W   + t*T   = H_orig - Delta*(N - M_A)  (the note's alternative offset).
Energy exchange with the bath = E(final) - E(0) per birth (unitary part conserves E exactly).
Pre-registered readings:
  H_orig: mean energy deposited per birth = Delta*(1 + O(eps)); "cost wall at the penalty scale".
  H'    : mean energy per birth -> O(delta) as eps -> 0, |Q|/delta >= 0.2 for eps <= 0.1
          (cost wall survives at the effective-hop scale, sign either way).  Cost is then linear in the
          supplied record rest energy mu: Q(mu) = Q(0) + mu.
  ESCAPE reading: |Q|/delta < 0.05 at eps=0.05 and shrinking with eps for H' in all four models.
Prediction: NOT escape (Q/delta of order 1), model-dependent sign.

## Test 3  (t03_test3_permanence.py) -- the count horn
3a  emission model (special initial state, reservoir n): atom (site 0, energy 0) + semi-infinite
    tight-binding chain (J=1) of length n, atom-chain coupling g, ONE excitation, exact unitary wave,
    Bell jump process for the excitation.  "Record formed" = excitation in chain; "count falls" =
    Bell jump chain->atom.
    PASS (escape 3 works with a source): g = 0.2, n = 400: P(count ever falls before t = 100) <= 0.05
      AND P(record formed by t = 60) >= 0.95 AND P(falls by t = 700 > t_rec ~ n) >= 0.3
      (T1 recovered at recurrence).   FAIL: P(fall by t = 100) >= 0.2.
    Control (inbound wave packet, same H, same n): P(fall) >= 0.5 -> monotone only for special psi.
3b  bulk formation term: hard-core ring, XX hopping 1, formation/annihilation term g*sigma^x = 0.4
    on every site, start empty, L = 6, 8, 10, 12, Bell process.  Per-record destruction rate r_d and
    per-empty-site creation rate r_c in the window t in [30, 80].
    PASS (statistical permanence in the bulk): r_d falls by >= 2x from L=6 to L=12.
    FAIL: r_d changes by < 30% over L=6..12 and r_c/r_d within 30% of rho/(1-rho).
    Prediction: FAIL (intensive, detailed balance) -> only transport from a source is permanent.

## Test 4  (t03_test4_inventory.py) -- arithmetic on probe 1 T4 numbers
Universe mass-energy ~1e70 J.  Sharp birth = 2.39*hbar*c/a.  Compute max births, sites, baryons.
Reading: sharp locks can be the constituents/ticks only if a >~ 1e-15 m (one per baryon) or
~3e-4 m (one per site).  Prediction: fails at a = l_P and a = 1e-19 m by many orders.

## Decision rule for the outcome
PRICED if 1a,1b FAIL-to-escape (cost model-independent, order-independent), Test 2 shows the cost
reappears in the second formation model as a supplied rest energy plus an O(hop) residual, and
3a PASS with 3b FAIL (permanence only by transport from a source into a large reservoir).
STANDS if 3a FAILS as well (no rising-count route inside a unitary wave).
PASSED only if Test 2 shows the escape reading AND 3a passes with creation from nothing (not run).
