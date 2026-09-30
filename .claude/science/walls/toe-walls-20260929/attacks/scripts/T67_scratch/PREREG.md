# T67 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor; same-family check only).
Date: 2026-09-29. Repository: main_wt at 7146fe17a7 (read only).

## Question the tests decide

W7 says every working gravity piece starts from a supplied geometric carrier.
The most natural "Record-to-geometry map" that stays inside the axioms'
adjacency is: one length per nearest-neighbour bond (Lattice supplies
adjacency only; the kinetic-isotropy primitive adds the tick edge).
The repository's own landed action (Regge second variation on the 4D
cubic-Coxeter complex; R4 = scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py)
uses 15 edge classes, of which only 4 (3 space + tick) join nearest-neighbour
sites; 11 join sites at sqrt2, sqrt3, 2 (face, triple, body diagonals).

Test A (edge-carrier test, decides route R2): with R4's own Hessian Q(k)
(15x15), gauge map G(k) (15x4), metric map M(k) (15x10):

- A1  "axis-only, diagonals frozen at flat": Q_aa = Q[axes, axes] (4x4).
- A2  "axis-only, diagonals relaxed (Schur complement)": Q_eff = Q_aa - Q_ad pinv(Q_dd) Q_da.
- A3  control "axes + 6 face diagonals (10 edges), rest relaxed".
- A4  which supplementary edge sets S (containing the axes) give a gauge-closed
      carrier whose Schur-complement Hessian has rank 6 (= 10 metric comps - 4 gauge) at generic k.

Readings fixed in advance (route "NN bond lengths are a sufficient carrier" = R2):

- R2 PASSES (survives) iff BOTH
  (i) A1 has gauge leakage ||Q_aa G_A xi|| / (||Q_aa|| ||G_A xi||) < 1e-3 at k->0 AND
      Q_aa(0) = 0 (no mass-type term), and
  (ii) A2 has rank >= 2 at generic k with eigenvalues scaling as |k|^2.
- R2 FAILS iff A1 has O(1) gauge leakage / nonzero Q_aa(0) (mass-type term at the cutoff)
  OR A2 has Q_eff = 0 (norm < 1e-10 * ||Q||) at generic k (axis lengths pure gauge).
- Control passes iff A3 shows 4 exact gauge zero modes and rank 6 at generic k
  (this is the landed R4 result seen through a 10-edge chart, so it must work
  or the harness is wrong).
- A4 is descriptive: the smallest supplementary set that closes gauge
  gives the adjacency the carrier needs beyond NN.

Generic k: random real 4-vectors with all four components nonzero, scaled by
lambda in {0.02, 0.05, 0.1, 0.2}; degenerate k with k_mu = 0 for one or more mu
reported separately.

## Test B (event-cardinality test, decides route R1 = order + number)

Route R1 (Sorkin "order + number = geometry", Cycle 46 note):
records are the events; causal order gives the conformal class; count gives the
conformal factor, provided (Cycle 46 hypothesis 2) record number in every suitable region converges to a
uniform density rho times 4-volume.

Lemma V (elementary counting, to be checked): by AX:79-80 the map
{records} -> Z^3 is injective, so the number of record events in any region D
is at most the number of sites in D's spatial projection. Uniform density
rho on a causal diamond of time extent T and radius R (rho * c_4 * T * R^3 events)
therefore forces T <= const/rho (lattice units): no macroscopic uniform-density region.

B1: simulate the minimal covariant clause (iid Exp(1) formation time per site,
    Z^3 torus, L=48). Measure events per unit coordinate time per site vs t.
    PASS for R1 iff density is constant (within 10%) over a window of >= 5 mean formation times.
    FAIL if it decays as exp(-t).
B2: causal futures under the dependency order "x < y iff exists nearest-neighbour
    path with strictly increasing formation times". Measure the size and extent of
    the future of random events. PASS for R1 iff futures reach the torus scale
    (extent grows with L); FAIL iff futures are bounded (extent <~ e*mu, mu = 4.68).
B3: same for a nucleation clause (a site forms at rate proportional to its number of recorded
    neighbours = Richardson growth from one seed): measure cone extent along 100/110/111 and the
    fraction of all later events that are in the future (sharp cone vs total order).
    PASS for R1 iff a cone with speed spread across 100/110/111 < 3% and future fraction < 0.5 of later events;
    FAIL otherwise.

Overall outcome mapping:
- If Test A fails R2 and Test B fails R1: no cheap route passes; report best route and price.
- Nothing here can show the wall is solved: a pass would only make a route "survives" pending its own artifact.
