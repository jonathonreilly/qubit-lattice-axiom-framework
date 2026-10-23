---
claim_id: the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Three parts. (1) 3-4-5-0 far-wall term (the two forced 6-fermion terms l1 = (1,-2,1,2), l2 = (2,1,-2,1), one coupling g) placed on cells: on one site it vanishes (Pauli); on a two-site cell the ground state is 8-fold at -g/2; on the three-site complete-graph cell it is unique, neutral (Q_A = Q_B = 0 from half filling, zero variance), E0 = -g, first excitation -(sqrt3/2) g, so Delta_0 = (1 - sqrt3/2) g = 0.134 g; the four-site cell is unique with Delta_0 = 0.026 g. Bond terms on overlapping bonds do not commute (norm 0.25 g^2) and the uniform open three-site chain has E0 = -0.75 g > -g (frustrated, 2-fold), so a uniform rule is not a sum of commuting cells; a non-overlapping cell tiling is needed. With a naive hop of norm 2t per bond, Yarotsky's theorem (classical in the cell eigenbasis, unique product ground state, 1D Jordan-Wigner-local) gives a persistent gap for t/g < kappa_0 Delta_0/(z ||h_b||) = kappa_0 / 44.8 (kappa_0 the theorem's constant, not computed); one cell with its own hops keeps its unique state until t/g = 0.237. This is SMG of the doubled (vector-like) chain content. In the domain-wall slab the gapped far-layer product does not gap the mirror: the far-wall branch keeps E = sin k and moves one layer in (free slab with the far layer gapped). 3-4-5-1 contrast: odd cells carry Q51 in Z + 1/2 at the particle-hole point, so the three-site cell ground state is an exact Q51 = +-1/2 doublet; the four-site cell is a Q51 = +-2 doublet (dynamical); a one-site-translation chain at half filling has Q51 filling 13/2 (LSM obstruction). The lattice sees the anomaly only mod 2 (sum q = q^T K q mod 2). (2) Bosonization: l1, l2 K-null, mutually null, neutral under (3,4,5,0) and (2,1,2,-1), primitive; free-point dimension 5 for both; in the equal-velocity Luttinger family V(x) both have dimension 5 sqrt((1-x)/(1+x)), relevant iff 21/29 < x < 1. (3) One site carrying the 16 (one orbital, 2^16 states): exactly two Spin(10) singlets, |0> and |F>; the Casimir is (3/4) N (16 - N); the 10 channel psi^T C Gamma^a psi vanishes identically and the 120 channel is N(N-1)/2; so no Spin(10)-invariant, particle-hole-symmetric site term of degree below 16 has a unique ground state. Under SU(3) x SU(2) x U(1)_Y x U(1)_B-L the one-orbital 16 has singlets 1, 6, 8, 6, 1 at N = 0, 4, 8, 12, 16, and its six singlet 4-fermion terms (equal real couplings) give a unique particle-hole-symmetric singlet ground state with gap 0.442 g. 15 modes (no nu^c): every level of a particle-hole-symmetric site is doubly degenerate (exact). 8 modes (Q + L, or (4,2)): singlets only at N = 0, 8. Not covered: gauge fields, the continuum limit, a cell lattice beyond one cell, the two-orbital Spin(10) cell (register value cited, not recomputed)."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_fewest_change_symmetric_far_wall_term_is_forced_and_gaps_the_3450_mirror_in_a_wall_mode_chain_while_the_flux_pump_separates_anomalous_content_bounded_theorem_note_2026-10-23
runner: scripts/the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_2026_10_23.py
---

# The forced far-wall term has a unique gapped three-site cell state, but a strong-coupling cell only moves the mirror, and the one-orbital 16 site has only two Spin(10) singlets

Claim type: bounded_theorem (exact statements; finite diagnostics labelled [F]; the stability theorems and the
Haldane criterion are supplied, not rederived). Runner: runner.py, TOTAL: PASS=21 FAIL=0, 2.5 s, 241 MB peak, 4.7 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120;
run under a unique filename (scratch/smg_strong_coupling_test_run.py).
Axioms unchanged. No rule adopted.

## Question

far-wall-smg found that the two forced 6-fermion terms gap the 3-4-5-0 mirror in a wall-mode chain at L = 12, but no
size trend could be extracted. The owner asked for a cheaper route: a strong-coupling derivation, a bosonization check, and the
same site test for the 16 in 3+1D.
- (1) Is there a smallest cell on which the forced term has a unique symmetric gapped ground state, and does a
  stability theorem then give a size-independent gap?
- (2) Do the forced vectors pass Haldane's criterion, and when are they relevant?
- (3) Does one site carrying the 16 admit a local symmetric interaction with a unique symmetric ground state?

Repo first. This builds on:
- far-wall-smg (the forced terms, the Chern pump, the regulator-blind 3451 result);
- block-quartic-smg (Spin(10) on the one-orbital 16 admits no singlet charge-4 term, two orbitals admit one; the block
  mirror term releases light partners);
- the register's candidate unification law (one 32-mode cell under the Spin(10) pair square has a unique singlet
  ground state, gap 19.1 g, with survival under inter-cell hopping "estimated only");
- gk-nogo-check (Golterman-Shamir obstruction for mirror schemes);
- smg-literature.
New here:
- the cell search;
- the commuting/frustration analysis;
- the stability-theorem application and its failure mode in the slab (mirror relocation);
- the LSM mod-2 reading of the 3451 contrast;
- the bosonization threshold;
- the exact one-orbital Spin(10) singlet theorem;
- the SM-group site result.

## Pass criteria (written before the runner's first run; scratch exploration in scratch/ preceded them, so the A, B
## and D values were seen in scratch and the thresholds are diagnostics, not blind tests)

A1 one site: the forced-term operator on one site has norm 0.
A2 two-site cell: ground state degeneracy > 1.
A3 three-site complete-graph cell (pairs 01, 02, 12): unique ground state, |E0 + 1| < 1e-9, |E1 + sqrt3/2| < 1e-9;
   <Q_A>, <Q_A^2>, <Q_B>, <Q_B^2> all < 1e-9 (charges measured from half filling).
A4 four-site complete-graph cell: unique ground state with gap > 1e-2.
A5 overlapping bond terms: ||[h01, h12]|| > 0.1; open three-site chain E0 > -1 + 0.1 and ground state degenerate.
A6 naive hop norm per bond = 2 (to 1e-9); one cell with its two intra-cell hops keeps a unique ground state with gap
   >= Delta_0/2 for t/g <= 0.1, and the first crossing t_c/g lies in (0.1, 0.5).
A7 free slab Ls = 12, far layer gapped by m sz with m = 20: the far-wall branch at k = pi/8 has |E - sin k| < 1e-6,
   weight on the far layer < 0.01 and on the next layer > 0.9.
B1 arithmetic: Q51 per site at half filling = 13/2 (non-integer); Q_A, Q_B per site = 6, 2; sum q = q^T K q mod 2.
B2 3451 three-site cell: lowest energies in Q51 = +1/2 and -1/2 equal (to 1e-9) and lower than all other sectors.
B3 3451 two- and four-site cells: ground state degenerate (two-site: > 2 states; four-site: Q51 = +-2 doublet, the
   Q51 = 0 sector strictly higher).
C1 l1, l2: K-null, mutually null, neutral under both charges, gcd of 2x2 minors 1.
C2 free-point dimension 1/2 |l|^2 = 5 for both.
C3 sympy: V(x) eta V(x) = eta, Delta(x) = 5 sqrt((1-x)/(1+x)) for both, threshold Delta = 2 at x = 21/29; numerical
   O(2,2) diagonalisation at x = 0.3, 0.8 agrees to 1e-9.
D1 16 of Spin(10) from five oscillators: 45 Hermitian generators, Casimir 45/4 on the 16 (to 1e-12).
D2 Weyl-character count of Spin(10) singlets in Lambda^n(16): exactly [1 at n = 0, 1 at n = 16, 0 else].
D3 on random Fock vectors, || C2 v - (3/4) N (16 - N) v || < 1e-9.
D4 multiplicity of the 10 in Lambda^2(16) = 0, in Sym^2(16) = 1; Lambda^2(16) = 120 irreducible (multiplicity 1, dim 120).
D5 H = N(16 - N) - (Psi16 + h.c.) with Psi16 the product of all 16 annihilators: unique ground state at -1, gap 2,
   ground state (|0> + |F>)/sqrt2 up to sign.
D6 15 modes: the particle-hole operator prod_i (c_i + c_i^+) anticommutes with fermion parity (exact), so every level of a
   particle-hole-symmetric, parity-conserving site is at least 2-fold.
D7 Q + L (8 modes) under SU(3) x SU(2) x U(1)_Y x U(1)_B-L and (4,2) under SU(4) x SU(2): singlets only at n = 0, 8.
D8 16 under SU(3) x SU(2) x U(1)_Y x U(1)_B-L: singlet counts [1,6,8,6,1] at n = 0,4,8,12,16 (0 elsewhere); six
   singlet charge-4 terms; with equal real couplings H = -g sum_i (O_i + O_i^+) has a unique ground state, gap > 0.05 g,
   and the ground state is killed by all simple raising and lowering operators (< 1e-8) with weight zero.
   (Prediction written before the runner; the equal-coupling value was seen in scratch.)

## A. Strong coupling for the forced 3450 term (part 1)

- A1 [T]. Both forced terms need two modes of one flavour (|l_f| = 2), so on one site they vanish: H_site = 0, and all
  16 states are degenerate.
- A2 [F]. Two-site cell: the terms connect only pairs of configurations, so the ground state is 8-fold at -g/2.
- A3 [F]. Three-site complete-graph cell (all three pairs; the pair terms are symmetric under exchange of the two sites
  because each term holds two pair factors, so the cell is S3-symmetric and no ordering is chosen):
  - the ground state is unique, E0 = -g, and the first excited level is -(sqrt3/2) g (4-fold), so Delta_0 = (1 - sqrt3/2) g = 0.134 g;
  - Q_A = Q_B = 0 from half filling, with zero variance;
  - a unique ground state carries a one-dimensional representation of every symmetry of the cell, so it is symmetric
    automatically.
  This is the smallest such cell.
- A4 [F]. The four-site cell is also unique, but with Delta_0 = 0.026 g.
- A5 [T]/[F]. The bond terms on (01) and (12) do not commute (||[h01, h12]|| = 0.25 g^2). The open three-site chain has
  E0 = -0.75 g, above 2 e_bond = -g, and is 2-fold.
  - So the uniform rule (one coupling on every bond) is NOT a sum of commuting or frustration-free blocks, and
    Bravyi-Hastings-Michalakis does not apply to it.
  - The block form the rule would need is a non-overlapping tiling by complete-graph cells of three sites, with the
    hops (and any inter-cell term) treated as the perturbation. That tiling breaks one-site translation to three-site
    translation: a lopsided choice that needs a reason (three equivalent tilings).
- A6 [F] Stability. Write H = g sum_cells h_c + t sum_bonds h_b, with naive hop h_b = sum_f s_f (i/2)(c^+_x c_x+1 - h.c.),
  where ||h_b|| = 2.
  - In each cell's eigenbasis, g sum h_c is classical with a unique product ground state and local gap Delta_0.
  - The hops are nearest-neighbour and bounded, and in 1D every hop is local after Jordan-Wigner.
  - So the hypotheses of Yarotsky 2006 hold: the ground state stays unique with gap >= Delta_0 - O(t) for
    t z ||h_b|| / Delta_0 < kappa_0, where z = 3 bonds touch each cell and kappa_0 is the theorem's constant (not
    computed). That is, t/g < kappa_0 / 44.8.
  - Kennedy-Tasaki 1992 is the cluster-expansion precedent; for fermions in d > 1 the analogue is De Roeck-Salmhofer
    2019 (CMP 365, 773; not on the supplied list).
  - Finite check: one cell with its own two hops stays unique until t_c/g = 0.237, which bounds the true constant from
    above at this cell.
  What this proves is SMG of the chain's full content, in which the naive hop gives each flavour both chiralities
  (3450 plus its mirror at k = pi): a vector-like statement.
- A7 [F] Relocation. In the domain-wall slab, the far layer in a unique cell product is gapped and decoupled, and the
  rest is a free Chern-1 slab per flavour. Its open face is now the next layer, so the mirror branch reappears there.
  - Free check: with the far layer gapped by m sz (m = 20), the far-wall branch keeps E = sin k exactly. Its weight on
    the far layer is 0.0025 and on the next layer 0.99.
  - Induced corrections are a bilinear self-energy O(T^2/g), which cannot gap a one-handed branch, and multi-fermion
    terms of order T^6/g^5 with free-point dimension 5 (part 2), which are irrelevant.
  So the g -> infinity limit of a far-layer term does NOT gap the mirror. The stability theorem's hypotheses fail for the
  coupled slab, because its unperturbed part (the free slab with the moved edge) is gapless.
  This is a route no-go for "strong coupling on the far layer" in this form. Escapes:
  - an intermediate-coupling phase (Zeng et al.'s regime), which no product-state theorem reaches;
  - a term acting on enough layers that the mirror modes themselves are cell-local, which turns it into the vector-like
    case, where the light copy must be protected by something the term does not see (momentum- or taste-selective
    forms: ax7, momentum-selective-mirror).

## B. 3451 contrast (part 1)

- B1 [T].
  - At the particle-hole point, Q51 per site is 13/2. A one-site-translation chain therefore has fractional Q51 filling,
    and LSM (Oshikawa form) forbids a unique gapped symmetric ground state.
  - For 3450, Q_A and Q_B per site are 6 and 2 (integers): no obstruction.
  - Since q^2 = q mod 2, sum q = q^T K q mod 2. The lattice remnant of the anomaly is its parity only: 3451 has q^T K q = -1 (odd).
- B2 [T]+[F]. On odd cells, Q51 lies in Z + 1/2, so particle-hole pairs Q51 with -Q51. The three-site cell ground state
  is an exact doublet at Q51 = +-1/2.
- B3 [F] (recorded result). The two-site cell is many-fold. The four-site cell is a Q51 = +-2 doublet with the Q51 = 0
  sector higher. Even cells carry no kinematic obstruction, so this doublet is dynamical.
  So no cell up to four sites has a unique state for 3451, and only the odd-cell part is a theorem. The anomaly enters
  the cell test only mod 2.

## C. Bosonization (part 2)

K = diag(1,1,-1,-1) (flavours 3, 4 one way, 5, 0 the other), t = (3,4,5,0), and the second charge (2,1,2,-1).
- C1 [T]. l1, l2 are K-null and mutually null, neutral under both charges, and primitive (the 2x2 minors have gcd 1).
  Haldane's criterion (supplied) then says cos(l1.phi) + cos(l2.phi) can gap all four modes. Primitivity gives a
  unique pinned minimum, so no discrete symmetry breaks.
- C2 [T]. At the free point, Delta(l) = 1/2 |l|^2 = 5 for both (> 2): both are irrelevant.
- C3 [T]. Write l = (a; b) with b = O a, where O = [[-3/5, -4/5], [4/5, -3/5]] is a rotation (possible because the
  Gram matrices of the a's and b's agree: both are null and mutually null).
  - The equal-velocity family V(x) = (1 - x^2)^(-1/2) [[1, x O^T], [x O, 1]] obeys V eta V = eta and
    Delta = 1/2 l^T V^-1 l = 5 sqrt((1-x)/(1+x)) for both.
  - Both are relevant iff 21/29 < x < 1: a strong forward-scattering helper, 0.72 of the velocity.
  - Unequal velocities and the general 10-parameter V are not scanned.
- Consistency with (1). Both routes say the forced terms gap only far from the free point: either at a large helper,
  or at g comparable to the bandwidth (far-wall-smg's level crossing near g ~ 40 in wall-mode units, and the cell regime
  g >> t here). Bosonization does not see A7's relocation, because it treats the mirror's own low-energy fields. The
  cell argument does not reach the bosonization regime.

## D. The 16 on one site (part 3)

Modes: the 16 of Spin(10) as the even Fock space of five oscillators, one complex mode per weight (one orbital). The
Lorentz spin index is dropped.
- D1 [T]. There are 45 generators, with Casimir 45/4 on the 16.
- D2 [T] (Weyl character formula, |W(D5)| = 1920). Lambda^*(16) holds exactly two Spin(10) singlets: |0> (n = 0) and
  |F> (n = 16).
- D3 [T]. C2 = (3/4) N (16 - N) on the whole Fock space. Reason: Lambda^2(16) = 120 is irreducible, so the only
  invariant 2-in-2-out operator is sum_{i<j} n_i n_j, and C2 is fixed by n = 1 and n = 16.
  - Every number-conserving 4-fermion invariant is a function of N.
  - The 120-channel Phi^+ Phi is N(N-1)/2, a pure Hubbard term.
- D4 [T]. The 10 lies in Sym^2(16), not Lambda^2(16), so psi^T C Gamma^a psi = 0 identically on one orbital. The suggested
  H = g sum_a |psi C Gamma^a psi|^2 is zero.
- D5 [T]. A unique ground state of a Spin(10)-invariant site lies in span{|0>, |F>} (there is no nontrivial 1D
  representation).
  - Particle-hole symmetry C (with the outer automorphism) swaps |0> and |F>, and only the 16-fermion term mixes them.
  - So a C-symmetric Spin(10)-invariant site term of degree < 16 never has a unique ground state, and the fewest-change
    unique site term is Psi16 + h.c. (gap 2w with N(16-N) supplied).
  - Without C, the empty site (chemical potential, a bilinear) is trivially unique: no SMG content.
  - Two orbitals change this: the register's 32-mode pair square is unique, gap 19.1 g (cited, not recomputed).
- D6 [T]. 15 modes: prod_i (c_i + c_i^+) is fermion-odd, so a C-symmetric parity-conserving site has every level at least
  2-fold for ANY interaction. Exact failure.
- D7 [T]. 8 modes (Q + L under the SM group, or (4,2) under SU(4) x SU(2)): singlets only at n = 0, 8. So no term of
  degree < 8 is unique. This is the same pattern as the Spin(10) 16: at fixed symmetry the site test does not separate
  8 from 16.
- D8 [F]. Under SU(3) x SU(2) x U(1)_Y x U(1)_B-L, the one-orbital 16 has singlets 1, 6, 8, 6, 1 at n = 0, 4, 8, 12, 16.
  - Its six singlet charge-4 terms are the B-L-conserving four-fermion types: QQQL-type, u d d nu, u u d e,
    Q L d nu, Q L u e and Q Q u d contractions.
  - With equal real couplings they give a unique, C-symmetric, singlet ground state with gap 0.442 g.
  - Three seeded random coupling vectors (scratch) also gave unique states, with gaps 0.003, 0.65 and 0.30 g.
  - Spin(10) kills all six (D2), so this needs the Spin(10)-breaking pattern and six supplied couplings.

Answer to (3): for the Spin(10) one-orbital 16, NO at fewest change. Only the degree-16 cat term gives a unique
symmetric site state. The SM-group one-orbital 16 gives YES at degree 4. The 15 fails exactly (parity). The 8 fails
below degree 8. A unique symmetric site state with a gap would, by the fermionic stability theorem, give a gapped
symmetric product phase of a lattice of such sites in any dimension. But the site test sees only the 0+1D anomaly
(mode-count parity under C, and the degree thresholds), not Z16: 8 and 16 behave alike, and an on-site symmetry lattice
carries no 4D 't Hooft anomaly. And in a domain-wall geometry, A7's relocation applies unchanged. So this is NOT "the
Z16 statement made local". It is the vector-like (Butt-Catterall-Hasenfratz-type) strong-coupling statement, and a
necessary site condition for a strong-coupling route.

## Answers

1. Strong coupling (3450): the smallest unique, symmetric, gapped cell is the three-site complete-graph cell,
   Delta_0 = (1 - sqrt3/2) g. The uniform rule is frustrated and non-commuting, so a cell tiling is required. Yarotsky
   gives a persistent gap for t/g < kappa_0/44.8 (ingredients: Delta_0 = 0.134 g, ||h_b|| = 2, z = 3), but for the
   vector-like content only. In the slab the mirror relocates (A7), so the far-wall strong-coupling route is a route
   no-go in this form. 3451: odd cells are exact doublets (LSM, mod 2), and the four-site cell is a dynamical doublet.
2. Bosonization: Haldane's criterion is met (null, mutually null, neutral, primitive). Delta = 5 at the free point.
   Both become relevant in the equal-velocity Luttinger family for x > 21/29.
3. The 16 site: Spin(10) one orbital: two singlets only. The 10 channel is identically zero and the 120 channel is
   Hubbard, so there is no unique state below degree 16. SM group: unique at degree 4 (gap 0.442 g). 15: exact
   doublets. 8: no unique state below degree 8. Not Z16.

## Mapping to the rules (no rule adopted)

A cell clause would be: "the far-wall term acts on non-overlapping complete-graph three-site cells".
- It is forced by A3 as the smallest unique cell, but its job (gapping the mirror) fails by A7, so it is not proposed.
- For the 16, an SM-group site clause would pass D8 but inserts SU(3) x SU(2) x U(1) x U(1) by name and six couplings,
  so it FAILS gate 2 unless the group is read off the light wall.

Gate for the cell clause:
1. no number is chosen;
2. no structure is inserted (3450 charges are the light wall's);
3. its purpose fails (A7), and it makes no new prediction: UNTESTED;
4. it bends no axiom, but breaks one-site translation, a lopsided tiling choice with no reason given.
Gate result: not adopted.

## Smuggling review

Supplied:
- the charges (textbook 3450 and 3451);
- the bond-average and pair forms (from far-wall-smg);
- the complete-graph cell;
- the naive hop;
- the m sz stand-in for a gapped layer;
- the Luttinger family;
- the one-orbital site (spin dropped);
- the SM-group couplings;
- the stability theorems and the Haldane and LSM criteria (cited, not rederived).

Forced:
- A1, A3, the A5 non-commutation;
- B1, B2;
- C1-C3;
- D2-D7.

Not shown:
- the gap of a lattice of cells (only the theorem's existence of kappa_0, plus one cell);
- intermediate coupling;
- gauging;
- the continuum limit;
- the two-orbital Spin(10) cell recomputation.

Literature (supplied, cited not computed): Wang-Wen 2013/2018, Tong 2021, Razamat-Tong 2020,
Butt-Catterall-Hasenfratz 2024, You-He-Xu-Vishwanath 2018, Kennedy-Tasaki 1992, Yarotsky 2006,
Bravyi-Hastings-Michalakis 2010, Haldane 1995, Zeng-Zhu-Wang-You 2022.
