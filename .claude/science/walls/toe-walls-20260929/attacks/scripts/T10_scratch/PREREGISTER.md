# T10 pre-registration (written before any T10 script was run)

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks, not referees).

## What the wall says (working statement)
"From Lattice, Qubit, Admissibility, Record, show a pointer observable is preferred and a determined
record value is recoverable from >= 3 disjoint local fragments." Evidence so far: 1D rings of 10-14
sites with a free-fermion SEA and one impurity gave R = 1.7-2.4 ("never 3"); a 4x4 Heisenberg patch
at infinite temperature gave R = 1.88. The lane's own named next test (viability map, 09-28; L01-W5
"cheapest test", L03-W7 "cheapest known test") is: pointer + many independent scatterers, redundancy
against their number. That test has not been run. It is the main test here.

## Hypotheses under test (mine, stated so they can fail)
H1 (state, not law). Redundancy of a pointer-conserving coupling depends on the ENVIRONMENT STATE, not
   on the lattice law: same law, same coupling, same size, an equilibrium sea gives R <= 2 at every
   size, a non-equilibrium beam of N_b independent carriers gives R that grows with N_b.
H2 (coordination ceiling). In 1D a sea/pointer contact has 2 neighbours, so the ring result
   "R about 2" is a geometric ceiling of that design, not evidence about scrambling. Size trend: the
   sea R does NOT grow with L (screening).
H3 (coupling form). A pointer that only shifts the phase of the scatterers (V = +-g) leaves far
   fragments with far less information than a pointer that switches a scatterer on/off (V = g or 0).
H4 (June quantification is definitional). The 2026-06-08 "299/300 non-redundant" statistic counts
   single-qubit fragments with N = 2, threshold 0.9; in the same star family with N = 12 and Zurek
   fragments (any size), R >= 3 in most samples.
H5 (covariance lemma). If Admissibility is covariant under the automorphisms of M_2(C) (reading of
   "no possibility is privileged"), no rule-level bit-valued pointer exists: invariant partitions of
   the Bloch sphere are only {points}, {antipodal pairs}, {whole}. Under cubic-only covariance, no
   bit-valued partition of the six axis directions exists, but the free 24-orbit has A4-coset bits.

## Tests and pass/fail readings

### Test A: beam vs sea (the main test). Script: `beam_vs_sea.py`
Model: free spinless fermions on an open chain, hopping -1 (band -2..2, max speed 2). Pointer S = qubit
in |+>, coupling H_s = H_hop + V_s n_{j0} with s = up/down (so [H, sigma_z] = 0: pointer-non-demolition).
Branch states are Slater determinants; fragment F = contiguous window of m <= 8 sites (a "local
observer"); recoverable pointer information = Holevo chi_F = S(avg rho_F) - avg S(rho_F^s), exact from
the branch correlation matrices (natural-orbital minors). H_S = 1 bit. delta = 0.1: a window "carries
the record" iff chi_F >= 0.9 bit. R = maximum number of pairwise-disjoint windows (<= 8 sites) that
carry the record (interval scheduling; a lower bound on Zurek's R because windows are capped at 8).
 Environment states: (i) half-filled ground state (sea), L = 60, 120, 240, at t = L/8 (cone stays
 inside the chain); (ii) N_b = 1, 2, 4, 6 Gaussian packets (sigma = 1.5, k0 = pi/2, spacing 10),
 L = 300, run to the time when all have scattered.
 Couplings: 'proj' V_up = g, V_down = 0 (presence/absence); 'sym' V = +-g. g = 3 and g = 20.
Readings:
 - H1 PASS: sea R <= 2 for all L, both g, both couplings AND beam (proj, g = 20) R(N_b = 4) >= 3
   with R non-decreasing in N_b (R(6) >= R(4) >= R(2) >= R(1)).
 - H1 FAIL (wall stands harder than I think): beam R(N_b = 4) <= 2 for all (g, coupling), i.e. many
   independent carriers do not give redundancy on this lattice. Then the last named test of the lane
   fails too, and the wall is a no-go for this class.
 - H1 also FAILS if the sea gives R >= 3 at some L (then screening is not the story).
 - H2 PASS: sea R(L=240) <= sea R(L=60) (+0), and the windows that carry the record sit within
   a few sites of the pointer.
 - H3 PASS: at equal g, beam 'sym' has max chi over windows (excluding the contact window) strictly less
   than 'proj', with R(sym, N_b = 4) < R(proj, N_b = 4).
 Also recorded: decoherence |<E_up|E_down>| (pointer preferred: sigma_z stays pure by construction, sigma_x
 coherence decays), and how many windows reach 0.5 bit.

### Test B: June star family, larger N. Script: `star_family.py`
H = sum_k c_k Z_S X_k, c_k ~ N(0,1), environment |0>^N, exact closed form chi_F = h((1+prod_k |cos 2 c_k t|)/2).
 - H4 PASS: at N = 12, fraction of samples (t uniform in [0,pi]) with Zurek R_0.1 >= 3 exceeds 0.5,
   while for N = 2 single-qubit fragments it reproduces the lane's rarity (below 10%).
 - H4 FAIL: fraction <= 0.5 at N = 12.

### Test C: covariance / block systems. Script: `blocks.py`
Enumerate all G-invariant partitions (block systems of imprimitivity) for G = octahedral rotation group
(24) on: the 6 axis directions, the 8 vertex directions, the 12 edge directions, the free 24-orbit.
 - H5 PASS: no 2-block partition on the 6/8/12 orbits; exactly one 2-block partition (A4 cosets) on the
   free orbit. The SO(3)-on-S^2 statement is by the subgroup lattice (SO(2) < O(2) < SO(3)), argued, not run.
 - H5 FAIL: any 2-block invariant partition on the 6, 8 or 12 orbits.

## What each outcome means for the verdict (fixed in advance)
 - H1 and H3 pass, H2 passes: PRICED. Price: (a) a pointer-conserving coupling that switches
   scatterers (law-level, dynamics = T02), (b) an incident many-carrier flux (realized-state data, T16),
   plus (c) covariance lemma: the pointer AXIS is state-level, never rule-level.
 - H1 fails (beam R <= 2): STANDS, and the last named lane test is a no-go for this free-fermion class.
 - Test A cannot be made to run: report what blocked it.
