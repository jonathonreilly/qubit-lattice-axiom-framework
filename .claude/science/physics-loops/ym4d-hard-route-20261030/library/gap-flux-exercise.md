lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-12T06:52Z

# Exercise (skill v2) on the flux half of the crux: does (GAP) need the flux sectors?

**Header.** Written by Claude Fable 5.2 (Anthropic), effort high, as author, Mac mini worker 1, one session, no subagents. Commit 84a72beb5, 2026-11-11. FINISH row 731 is the caller's brief. Skill: `docs/ai_methodology/skills/exercise/SKILL.md` at 1eb15ac428 (fetched to a scratch folder, read in full). **Nothing in this file is checked by another model.** Every statement below is `argued`, `refuted`, `guide`, `reading` or `open` in the sense of the skill; none is `checked`.

**Refresher replacement.** This target's `GOAL.md` reads no framework axiom or primitive (a standalone proof target). I read `GOAL.md` in full and the rules of `FINISH.md` (lines 1 to 84, 299 to 349, row 731) in place of the framework refresher list. No approved primitive enters.

**What this run did not cover** (kept current):

- (filled as the run goes)

## Status block

| Step | State | Main result |
|---|---|---|
| 0 Locate the record | started | |
| 1 State the wall twice | not started | |
| 2 Inventory | not started | |
| 3 Reason up | not started | |
| 4 Assumptions table | not started | |
| 5 Compare with earlier work | not started | |
| 6 Discard tests and set-aside methods | not started | |
| 7 Routes | not started | |
| 8 Real attempts | not started | |
| 9 Report | not started | |

## Step 0. Where the record is; what is open and what stays closed

**Rule 0a search (before any attack).** `grep -n -i "flux\|centre-even\|center-even\|even sector\|twist\|mass gap\|seed" library/open-core.md`: no line. `library/l17c.md`: two lines match "twist" or "flux"; read at step 5. FINISH rows with a `gap-` name: 655 to 731 (ids listed by grep only; rows 697 to 730 not read before step 5). No row id names the centre-even sector or a twist-averaged seed. The full search is step 5.

**Where the record of the wall is (file names found by grep for "flux sector", "even sector", "electric flux", "Z_odd", "Z_even"; arguments not read).** `library/gap-ac-lat.md`, `gap-crux-fp.md`, `gap-crux-restate.md`, `gap-mid-max.md`, `gap-phys-seed.md` and its check, `gap-seed-check.md`, `gap-seed-shape.md`, `gap-skeleton-final.md`, `gap-skeleton-max.md`, `gap-skeleton-max-b.md`, `gap-transfer.md`, `gap-zero-transport.md` and its check, `library/exercise-skill-v2.md`, `library/prior/gap-seed-lit.md`. The folder `library/prior/` holds 19 `gap-*` digests. No earlier exercise packet on this wall exists under `.claude/science/exercises/` (the folder is absent in this checkout).

**Open now (read before step 5).**

- `GOAL.md`, whole. `FINISH.md` lines 1 to 84, 299 to 349, and row 731.
- `library/gap-skeleton-final.md` Sections 0 to 3 and 13.15, whole.
- `library/gap-crux-restate.md`: Sections 0 to 2 whole; statements and proofs of 3.1, 3.2, 3.4, 4.1, 4.2. Not opened before step 5: 3.3, 4.3, 4.4, 5, 6 (failed ways and verdicts).
- `library/gap-seed-limit.md`: Sections 0 to 5 and 7. Not opened: Section 6.
- `library/gap-seed-shape.md`: header, Sections 0 and 1.1. The rest not opened before step 5.
- The account `YM4_1400.tex` of Sussman and Alpoge (with Claude and Codex) at 2bc0658f91d2, fetched by URL to a scratch folder: lines 140 to 175 (Theorem 0), 1680 to 1730 (continuum limit, volume-first limit, the frame), 1884 to 1910 (Theorem "Canonical components"). Statements only. The file has 136,637 lines; the rest is not read.

**Closed until step 5.** `library/gap-skeleton-final.md` Sections 4 to 13.14; every other `library/gap-*.md` file and its check file (this includes `gap-transfer.md`, `gap-phys-seed.md`, `gap-twist-chart.md`, `gap-twist-port.md`); `library/prior/gap-*.md`; `library/exercise-skill-v2.md`; FINISH rows 697 to 730.

**Literature.** The lane's literature record is `library/prior/gap-*.md` (closed until step 5). Before step 5 this run uses statements of results only, each marked `recalled`. No paper was fetched before step 5.

## Step 1. The wall, stated twice

**Plain version.** We want to show that the lightest particle of the theory has a positive mass. The present plan reduces this to one inequality on a box of one size with wrap-around walls. A proved step then carries the inequality to every larger box. The inequality counts every state of the box. Some of these states carry a "flux": a line of force that winds once around the box. Flux states cannot be made or seen by any measurement inside a bounded region. The particle we want is seen by such measurements. So the question is whether the flux states have to be in the inequality at all. If they do not, the plan no longer needs "confinement" (flux is heavy), which is a second hard problem. If they do, the present form of the inequality is right. Getting past the wall means a proof one way or the other, or one exact statement that decides it. (Analogy: a census that must count ghosts.)

**Precise version.**

- Target (GAP), quoted, `library/gap-skeleton-final.md` Section 1 (not checked there): "Let sigma be a canonical component of a volume-first limit at reference coupling g, with Hilbert space H(sigma), vacuum Omega, Hamiltonian H >= 0 and ker H = C Omega. Then there is m > 0 with spec(H) contained in {0} union [m, infinity)." H(sigma) is the cyclic sector of the one field tr(F^2).
- Working crux, `library/gap-seed-limit.md` Section 5 and `gap-skeleton-final.md` 13.15: (SEED-phys). In lattice form (Theorem L, `gap-seed-limit.md` Section 7): s := S(n; (2n)^3) < 1/5041, where S(a; B) is the sum of (lambda_j/lambda_0)^a over all excited eigenvalues of the transfer operator of the periodic box B, **on the whole space, flux sectors included** (`gap-crux-restate.md` line 228).
- The question. (Q1) Does (GAP) follow from a statement about the centre-even sector alone? (Q2) Is there such a statement at one physical size, with a proved step from one size to all sizes? Answer yes or no with proof, or name the exact statement that decides it.
- Quantifiers and domain. Wilson SU(2), four dimensions, one real beta > 0 for the lattice statements; "physical size" means the scaling form of `gap-seed-limit.md` Proposition P. Tori with all sides at least 3.
- Allowed premises. The checked statements of the open list (Step 2), each with its mark. No numerics in a proof. Forbidden weakenings: a statement at all scales in place of one size (that is (G) itself); a statement that assumes clustering of the limit.
- Does not count as closure: a physical argument that flux is heavy; a numeric run.
- What currently fails: nothing fails; the present chain is consistent. It is not known whether its hypothesis is stronger than (GAP) needs.
- Progress: a proof that part of the chain reads the centre-even sector only; a seed with fewer or other sectors and a proved step; a model of the class with an even-sector seed and no gap.

**Blind check.** Not run (no subagents allowed). The plain version is corrected in step 9.

## Step 2. Inventory: what is known to be true

Sources are the open list only. "checked" names the check row as the open files report it; I did not re-read the check files before step 5.

| # | Item | Mark | Source | Standing and reading state |
|---|---|---|---|---|
| 1 | (GAP): the target, on the cyclic sector of tr(F^2) in a canonical component of a volume-first limit | DEF | `gap-skeleton-final.md` L29-34 | not checked; statement read |
| 2 | A volume-first limit: each nu_j is a limit point of the periodically extended torus measures as l -> infinity at fixed spacing and coupling; the tori have four equal sides l = 2 L^m | DEF | account L1690, L1726 | statement read |
| 3 | The canonical decomposition of the centred functional into components sigma_xi, each with a unique vacuum; cluster rate \|v\|^(-2) only | THM (the account's, conditional on its packages) | account L1709-1720, L1884-1910 | statement read; proofs not read; the account is a conditional outline |
| 4 | tr(F^2) is a function of plaquette variables, gauge invariant, local | DEF | account L166-175, L2560 | read |
| 5 | (TM): Z(n) = Tr T^(n_mu) for a positive trace-class T; simple top eigenvalue with strictly positive eigenfunction; for every box with sides at least 3 | THM | `gap-crux-restate.md` L33 (from `gap-transfer.md`) | checked (rows 671, 698, 699 as reported); statement read, proof not read |
| 6 | (TM-c): the centre flip C_nu is a unitary involution commuting with T; Tr(T^(n_mu) C_nu) = Z^(mu nu)(n) > 0, the partition function with the sign of tr U_p flipped on one stack of (mu,nu)-plaquettes; symmetric in mu, nu | THM | `gap-crux-restate.md` L35 | checked (rows 698, 699 as reported); read |
| 7 | Lemma A: for S >= 0 trace class, (Tr S^k)^(1/k) is non-increasing in k | THM | L37 | checked as reported; read with proof source named |
| 8 | Lemmas K, X, E, E'; Theorem S; Corollary S3': one seed gives a uniform gap on all cubes of side at least 2N. The proofs use only the "setting for the lemmas": W(a,b) positive, symmetric, W(a,b) = Tr T_b^a, ell finite | THM | L174-219 | checked by two models (rows 698, 699 as reported); read in full with proofs |
| 9 | Theorem D (b), (e): 1 + S(n; (2n)^3) <= exp(Phi(n)); odd-flux weight u <= S(2n; B_2) | THM | L90-106 | checked as reported; read with proofs |
| 10 | Theorem F (a): Z_odd = Tr(T_1^a P_2) = Tr(T_2^b P_1), P_nu = (1 - C_nu)/2. So the one-plane twist sum is crossing symmetric | THM | L236-244 | checked as reported; read |
| 11 | Theorem L: (SEED) gives, for limit states of periodic tori and cylinders, exponential clustering in four directions and a gap of the transfer operator of the limit. Its torus errors are thermal sums S(d'; L^3) over the whole space (Theorem L1) | THM | `gap-seed-limit.md` Sections 2 to 4, 7 | checked (row 703 as reported); read with proofs |
| 12 | Lemma T, Proposition C: on the torus, <F H> (1 + S_T) = f h + u + u' + v with spectral sums; (K1) \|<phi, k_F psi>\| <= \|\|F\|\| \|\|phi\|\| \|\|psi\|\| | THM | `gap-seed-limit.md` L48-76 | checked (row 703); read |
| 13 | (PHYS-SEED) holds iff (BDD-Delta) and (Z-UNB); (Z-UNB): the gap of the periodic cube times its side is unbounded | THM | `gap-skeleton-final.md` L557-562 (from `gap-phys-seed.md`) | not checked (check = row 727); statement read as quoted |
| 14 | The seed boxes are periodic, the thermal sum is over the whole space, the time is half the side | SUPPLIED (a choice of the method: Theorem S needs W(a,b) = W(b,a)) | `gap-crux-restate.md` L172-176 | - |
| 15 | The volume-first limit uses periodic symmetric tori | SUPPLIED (the account's construction) | account L1690 | - |
| 16 | SU(2) confines: the energy of an electric flux grows like the side; twisted and periodic partition functions agree up to exp(-sigma area) | BELIEF | physics; used in no proof | - |
| 17 | Z_2 gauge theory in four dimensions at large beta: a gap on plaquette observables; eight flux sectors degenerate with the vacuum, S >= 7 - o(1) | THM, recalled | `gap-skeleton-final.md` L62; `gap-crux-restate.md` L62, L227 | recalled there and here; no source read; nearest model where the gap holds and the whole-space seed fails |
| 18 | U(1) in four dimensions at weak coupling: no gap (photon); S >= 12 exp(-pi) | THM, recalled | `gap-skeleton-final.md` L61; `gap-crux-restate.md` L62 | recalled (Guth; Frohlich and Spencer); nearest model where the target is false |
| 19 | SU(2) on a small torus at weak coupling: flux sectors nearly degenerate, many low levels | THM/BELIEF, recalled | `gap-skeleton-final.md` L553 | recalled small-volume physics |
| 20 | 't Hooft (1979): twisted boundary conditions k in Z_2^6 on the four-torus; a Z_2 Fourier transform over the three time-space twists gives the weights of the electric flux sectors; space-space twists are magnetic fluxes | THM, recalled | 't Hooft, Nucl. Phys. B 153 (1979) 141 | recalled; not re-read; I re-derive what I use from items 5, 6 |
| 21 | The two-dimensional Ising model: transfer matrix exactly solved (Onsager; Kaufman); at the critical point the scaling limit on the torus is the c = 1/2 conformal theory with characters of 1, epsilon, sigma | THM, recalled | Onsager 1944; Kaufman 1949 | recalled; used as a test model only |
| 22 | Local functions of tr U_p over contractible plaquette sets do not change under the centre flips C_nu (the flipped links of a slice enter each plaquette twice or not at all) | DEF (a computation from the definition in item 6) | this file, C1 | argued here |
| 23 | Theories with gauge algebra su(2) and different global form: SU(2), SO(3)_+, SO(3)_- (sum over twists, without or with the sign of the Pontryagin square) | THM, recalled | Aharony, Seiberg, Tachikawa, JHEP 08 (2013) 115 | recalled; used only to name objects |

Walls of this problem sit in items 14 and 15, both SUPPLIED. No framework axiom or primitive enters.

## Step 3. Reasoning up from the inventory

Written before any closed file was opened. Every statement here is `argued` (proved by Claude Fable 5.2, not yet checked) unless marked otherwise. Full proofs of C3, C5, C6 are in Step 8.

### 3.0 Notation (from items 5, 6, 20)

Directions 1 to 4. A **twist** is a k in K := Z_2^6, one entry k_{mu nu} for each coordinate plane. The stack of the plane (mu,nu) is the set of (mu,nu)-plaquettes with base point at x_mu = x_nu = 0. For k in K, s^k_p = -1 if p lies in an odd number of the stacks of the planes with k_{mu nu} = 1, and +1 otherwise. Z^k(n) is the integral of exp(-beta sum_p (1 - (1/2) s^k_p tr U_p)). Z^0 = Z. Each Z^k is positive.

Frame 1 (direction 1 is time, box B = (n_2, n_3, n_4)): E_1 = the twists in the planes (1,2), (1,3), (1,4) ("electric"), M_1 = the twists in the planes (3,4), (2,4), (2,3) ("magnetic"). K = E_1 + M_1. For e in E_1 write C^e for the product of the flips C_nu with e_{1 nu} = 1.

**(TM-tw), the twisted form of items 5 and 6 (an input; see 8.1 for its standing).** For every box B with sides at least 3 and every m in M_1 there is a positive trace-class operator T_{B,m} on the space of the box, with strictly positive kernel, commuting with C_2, C_3, C_4, such that Z^{e+m}(a, B) = Tr(T_{B,m}^a C^e) for all e in E_1 and a >= 3. The same holds in each frame. For m = 0 and one plane e this is items 5 and 6.

**Sector sums.** For chi in {+1,-1}^3 let P_chi be the projection on the joint eigenspace C_nu = chi_nu. Z_{chi,m}(a; B) := Tr(T_{B,m}^a P_chi) >= 0. Then

(F1) Z^{e+m} = sum over chi of chi(e) Z_{chi,m}, and Z_{chi,m} = (1/8) sum over e in E_1 of chi(e) Z^{e+m}.

The **centre-even sector** is (chi, m) = (0, 0) (all chi_nu = +1, no magnetic twist). S_ev(a; B) := Z_{0,0}(a; B)/lambda_0(B)^a - 1, and m_ev(B) := log(lambda_0 / the second eigenvalue of T_B on the even subspace). A pair (chi, m) other than (0,0) is a **flux sector**: electric if m = 0, magnetic if chi = 0.

### 3.1 What follows at once

**C1 (the target reads the even sector on the cylinder).** Let 𝔄 be the class of local functions F with F(g.U) = F(U) for every map g from sites to {+1,-1} (centre-valued gauge transformations). Every function of the numbers tr U_p, and so every lattice version of tr(F^2) (item 4), is in 𝔄. For F in 𝔄 whose width in direction nu is at most (side - 2), the slab operator k_F of item 12 commutes with C_nu. So on the cylinder, <F H> - <F><H> = <k_F^* Omega, Rx^d k_H Omega> runs over even eigenvectors only, and its modulus is at most ||F|| ||H|| exp(-m_ev(L^3) d).

Proof. C_nu flips the nu-links that cross one plane x_nu = c. Flip these links in every slice of the slab of F. On the support of F this equals the gauge transformation g = -1 on the sites with c < x_nu <= r, for r beyond the support; so F does not change. The slab weight does not change: a spatial plaquette holds two flipped links or none, and a time-like (1,nu)-plaquette at the plane holds the flipped link at both of its times. So K_F(C_nu u, C_nu v) = K_F(u, v). Omega is strictly positive and C_nu maps positive functions to positive functions, so Omega is even (as in Theorem D (e)). QED. Inputs: items 5, 6, 12, 22.

**C2 (three inequalities between sectors).** Given (TM-tw):

- (S1) Z_{chi,m} <= Z_{0,m}. Proof: by (F1), Z_{0,m} - Z_{chi,m} = (1/8) sum_e (1 - chi(e)) Z^{e+m} >= 0.
- (S2) Z^k <= Z^0 for every k in K. Proof: Tr(X C) <= Tr X for X >= 0 trace class and C a unitary involution commuting with X. So Z^{e+m} <= Z^m in every frame. Write k = e_1 + m_1 in frame 1; then m_1 = e_2 + m_2 in frame 2 with m_2 in the plane (3,4) only; that plane is electric in frame 3. Three steps give Z^k <= Z^0.
- (S3) The top eigenvalue lambda_m(B) of T_{B,m} is at most lambda_0(B), and its eigenvector is even. Proof: Z^m(a, B)^(1/a) tends to lambda_m(B), and (S2); positivity of the kernel.

**C3 (Theorem EV-L: the limit half reads the even sector only).** Let the torus be L^3 x T, m_ev = m_ev(L^3), and S_ev(.) = S_ev(. ; L^3). Write omega_per for the periodic torus state and omega_ev(F) := Tr(P_0 k_F Rn^(T-w)) / Tr(P_0 Rn^T) for F in 𝔄. Then:

- (a) omega_ev = sum over e in E_1 of q_e omega^e, with q_e = Z^e / sum_e' Z^e' and omega^e(F) = Tr(C^e k_F Rn^(T-w))/Tr(C^e Rn^T). Each omega^e is a positive normalised functional on the local functions of 𝔄, invariant under time translations. omega^0 = omega_per, and q_0 >= 1/8 by (S2).
- (b) (Theorem L1 in the even sector.) For F, H in 𝔄 as in Lemma T: |omega_ev(FH) - omega_ev(F) omega_ev(H)| <= ||F|| ||H|| (exp(-m_ev d) + 6 S_ev(d')). Also |omega_ev(F) - <F>_{L,inf}| <= 2 ||F|| S_ev(T - w).
- (c) (The periodic state is the even state on 𝔄.) For A in 𝔄 real with time width w, an integer delta >= w + 1 and an integer N >= 1 with N delta <= T - 2:

 |omega_per(A) - omega_ev(A)| <= ||A|| ( 8 [ (1/N)(1 + 2/(exp(m_ev) - 1)) + 6 S_ev(T - N delta) ] )^(1/2).

- (d) Let L_i -> infinity with m_ev(L_i^3) >= m_0 > 0 and S_ev(n_i; L_i^3) -> 0 for some n_i <= L_i/2 (hypothesis **(G_ev)**). Then on 𝔄 the periodic symmetric tori L_i^4, the even states and the cylinders have the same limit points, and every limit nu satisfies |nu(FH) - nu(F) nu(H)| <= ||F|| ||H|| exp(-m_0 d) for F, H in 𝔄 separated by d >= 1 in any of the four directions.

So the periodic volume-first limit (item 2) has the gap on the tr(F^2) sector as soon as the even sector alone is controlled at all sizes. No flux sector enters. Proof in 8.2. Inputs: items 5, 6, 11, 12, C1, (S2).

In words: (c) is the fact that a clustering state cannot be a mixture. The even state is a mixture of the periodic state and seven twisted states, and the periodic state has weight at least 1/8 in it.

**C4 (crossing exchanges electric and magnetic; the even sector alone is not crossing symmetric).** The exchange of the axes 1 and 2 maps the planes (1,3) to (2,3) and (1,4) to (2,4) and fixes (1,2) and (3,4). So Z^k(a, b, c, d) = Z^{tau k}(b, a, c, d) with tau k the image twist (the definition of Z^k is symmetric under relabelling the axes). The electric twists (1,3), (1,4) of frame 1 are magnetic twists of frame 2. Hence, with the sum over the four magnetic twists m' in the planes (1,3), (1,4) of the box (a, c, d):

(*) Z_{0,0}(a; (b,c,d)) = (1/4) sum over m' of Tr(T_{(a,c,d),m'}^b (1 + C_1)/2).

The right side is one quarter of a trace over sixteen sectors of the crossed box. It is not a trace with a simple top eigenvalue. Consequence on the symmetric pair a = b (and the same c, d): **the sum rule**

(SR) the fifteen flux sectors on the right of (*) carry exactly three times the weight of the even sector: sum over (chi', m') != (0,0) of Z_{chi',m'} = 3 Z_{0,0}.

So flux sectors are never all heavy. This is 't Hooft's duality (item 20) as an exact finite identity. It is why a seed on the even sector alone cannot be carried by the crossing step of Theorem S.

**C5 (which sector sets are crossing symmetric).** Let w be a real function on K and W_w := sum_k w(k) Z^k. In frame 1, W_w = sum over (chi, m) of what(chi, m) Z_{chi,m} with what(chi, m) = sum_e w(e + m) chi(e). Call w **admissible** if what takes values in {0} union [1, infinity) and what(0,0) = 1. Then W_w is the trace of T^a over a direct sum of sectors, with the vacuum simple. Proposition (8.3): w is admissible and invariant under all permutations of the axes if and only if it is one of three:

- **periodic**: w = the indicator of k = 0; sectors (chi, 0), all chi. This is the present form.
- **full**: w = 1/8 for all k; sectors (0, m), all m. Zero electric flux, all magnetic fluxes.
- **kappa**: w(k) = (1/8)(-1)^{Pf(k)}, Pf(k) = k_12 k_34 + k_13 k_24 + k_14 k_23; sectors with chi_nu = (-1)^{m_nu} (electric flux equal to magnetic flux, "dyonic").

For one pair of axes only, the sectors with chi_2 = m_2 = 0 in an admissible (1 2)-symmetric w form a group of exactly four, self-orthogonal for the pairing that couples chi_3 with m_4 and chi_4 with m_3. No admissible symmetric w has the even sector alone. (These are the theories SU(2), SO(3)_+, SO(3)_- of item 23; the names are not used in a proof.)

**C6 (Theorem S for the three sector sets).** Given (TM-tw): for each of the three w of C5 the function W_w satisfies the setting of the lemmas (item 8), with the top eigenvalue lambda_0(B) of the periodic box, by (S3). So Theorem S and Corollary S3' hold with S replaced by S_w(a; B) := W_w(a, B)/lambda_0(B)^a - 1. Since S_ev <= S_w, each seed S_w(N; (2N)^3) < 1/5041 gives (G_ev) on every cube of side at least 2N, and then C3 gives the gap of the periodic limit on 𝔄. Proof in 8.4.

**C7 (order of the three seeds).** S_kappa <= S_full on every box and time, by (S1) term by term. So the full seed implies the kappa seed. I have no exact inequality between S_kappa and S_per.

### 3.2 The least a solution must contain

Any proof of (GAP) must fail for U(1) at weak coupling (item 18) and must not fail for Z_2 at large beta (item 17). In Z_2 at large beta the electric flux sectors are degenerate with the vacuum and the plaquette observables have a gap. So no proof of (GAP) can need "electric flux is heavy" as a matter of logic in the class. By C3 the limit half needs no flux statement. By C4 and C5 the step from one size to all sizes, when done by crossing, needs seven flux sectors, of one of three kinds.

### 3.3 The smallest object

The smallest carrier of the information is the pair (even sector of the periodic cube; the sixteen-sector duality relation (*)). A toy in which the wall bites: the two-dimensional Ising model. Its sectors are (chi, m) in Z_2 x Z_2: chi = parity under the global flip, m = antiperiodic chain. Crossing exchanges chi and m. The three symmetric sector sets are {(0,0),(1,0)} (periodic), {(0,0),(0,1)} (even sectors of both chains), {(0,0),(1,1)} (the fermion form). In the ordered phase the periodic seed fails (the odd state is degenerate) and the other two can hold; in the disordered phase the full seed fails. The kappa seed can hold in both. Run in Step 8 (guide).

### 3.4 Where the result can come from; one problem or several

It is two problems. (i) The limit half: closed for the even sector by C3. (ii) The step: three forms by C6. Mechanisms: periodic seed = electric flux heavy (confinement); full seed = magnetic flux heavy (the Z_2 large-beta case); kappa seed = dyonic flux heavy. Under the belief of item 16, for SU(2) the magnetic sectors become degenerate with the vacuum at large size, so the full seed is false there, and the kappa sectors hold an electric flux, so the kappa seed is again a confinement statement (belief, not proved).

### 3.5 Make the requirement less wrong

The consumer (C3) needs (G_ev) only. (PHYS-SEED) on the whole space is stronger than needed in two ways: its limit half uses whole-space thermal sums where even ones suffice, and its seed is one of three admissible seeds. What cannot be weakened by this method: some seed with seven flux sectors.

### 3.6 Price

If the even-only seed is wanted, the missing input is exact: an **even step**, a bound of S_ev at size 2b by S_ev at size b alone. By (*) and Lemma A,

(EV-LOSS) 1 + S_ev(a; (2b,c,d)) <= (1 + S_ev(a; (b,c,d)))^2 exp(a (2 kappa(b) - kappa(2b))) (1 + V),

where kappa is the deficit of Lemma K for the periodic box and 1 + V = (sum_x y_x^2)/((1/4)(sum_x y_x)^2) in [1/4... ] is fixed by the sixteen crossed sector weights y_x (8.5 gives the exact form). The losses vanish when the light crossed sectors form one group of four, which is the statement that one of the admissible seeds holds.

### 3.7 Conclusions

- **C1.** tr(F^2) observables are centre-blind; the cylinder reads the even sector only. Rests on items 5, 6, 12, 22. argued.
- **C2.** (S1), (S2), (S3). Rest on (TM-tw). argued, given (TM-tw).
- **C3.** Theorem EV-L: (G_ev) gives the gap of the periodic limit on 𝔄; the periodic state equals the even state on 𝔄 up to an explicit error. Rests on items 5, 6, 11, 12, C1, (S2) for electric twists (which is item 6 with products of flips). argued.
- **C4.** Identity (*), the sum rule (SR). Rest on (TM-tw). argued, given (TM-tw).
- **C5.** Exactly three admissible symmetric sector sets; none is the even sector alone. Finite algebra. argued.
- **C6.** Theorem S for the three sets. argued, given (TM-tw) and item 8.
- **C7.** S_kappa <= S_full. argued, given (TM-tw).
- **C8.** For SU(2) the kappa and periodic seeds are both confinement statements and the full seed is false at large size. BELIEF (rests on item 16).
- **C9.** The even-only seed is not carried by crossing; the price is (EV-LOSS). argued for the identity; whether an even-only step exists by another method is open.

## Step 4. The assumptions table

Taken from the wall's statement and the open files, before step 5. "Method" = needed by the method, not by the target.

| ID | Assumption | Where used | Needed or habit | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| a1 | (GAP) is wanted for every canonical component of every volume-first limit | `gap-skeleton-final.md` L29 | target | with one component only, less is needed; C3 (c) shows the periodic limit already equals the even limit on 𝔄, so nothing is lost | no change | C3 |
| a2 | The observable class is the tr(F^2) sector | L33 | target | every contractible Wilson loop is in 𝔄 too, so C3 covers all local gauge-invariant observables; functions that are not centre-gauge invariant are not covered by C3 | no change for (GAP) | C1 |
| a3 | The consumer needs a rate uniform in the cutoff in physical units | `gap-seed-limit.md` Proposition P | target | - | - | none |
| b1 | The limit is built from periodic symmetric tori | account L1690 | supplied by the account | with twist-averaged tori (kappa or full) the limit is the same on 𝔄 under (G_ev) (C3), but the account's estimates are stated for periodic tori | no | C3 |
| b2 | Gauge group SU(2), centre Z_2, Wilson action | everywhere | target (first) | for SU(N) the twists are Z_N; the admissible sector sets must be classified again | unknown | inspect C5 for Z_N |
| b3 | The transfer operator with twisted spatial weights has the properties of (TM) | C2, C4, C6 | method | then C4 to C7 fall; C1 and C3 stand (they use electric twists only) | - | 8.1 |
| b4 | Local functions on a torus are placed in a simply connected region | C1 | method | - | - | none |
| c1 | The gap of the limit is obtained from a gap of the periodic cube on its whole space | Theorem L, Theorem L1 | **method** | C3: the even sector suffices for 𝔄 | yes, for the limit half | C3, proved |
| c2 | The step from one size to all sizes is the crossing step, which needs W(a,b) = W(b,a) | Theorem S | method | another step (boundary values of one cube, hypothesis (W) of `gap-crux-restate.md` L72; or an unknown even step) would remove the flux sectors | unknown | 8.5 |
| c3 | The seed is stated on periodic tori | (SEED), (PHYS-SEED) | **habit** | two more admissible forms (C5, C6): full and kappa | for SU(2): no gain is proved (C8 is a belief) | 8.3, 8.4 |
| c4 | The seed box is a cube at time half the side | Theorem S | habit (other shapes: `gap-seed-shape.md`) | - | constants only | not re-derived |
| c5 | The crux in two statements: (BDD-Delta) and (Z-UNB) on the whole space | `gap-skeleton-final.md` L557-562 | method | for the kappa form the analogue reads the kappa partition sums; not derived here | no | none; open |
| c6 | One quantity, the whole-space thermal sum, serves both the step and the limit | Theorems S and L | habit | the limit half needs S_ev only (C3) | yes | C3 |
| d1 | Test: U(1) at weak coupling has no gap | L61 | discard test | valid: T = gap is false there, on every sector (the photon is centre-blind) | - | recalled |
| d2 | Test: Z_2 at large beta: "the seed is false, and it must be" | `gap-crux-restate.md` L62, L227; `gap-skeleton-final.md` L562 | discard test | **too strong for the target (GAP)**: on the even sector the gap holds in Z_2 at large beta. The test shows that the whole-space seed is not necessary; it does not show that a tool must fail there. In the valid form it is a constraint on the periodic seed only | yes: it frees seeds that are true for Z_2 | step 6 |
| d3 | Tests: slab at 1/T_c, fundamental-adjoint end point, rate filter, upper bounds, two dimensions | L63-67 | discard tests | not touched by this wall | - | not re-derived |
| e1 | SU(2) confines at every coupling | item 16 | belief | if SU(2) had a deconfined massive phase, only the full or kappa seed could hold | - | none |
| e2 | At the seed size (about 17 correlation lengths or more) the flux sectors are far heavier than the lightest even state, so S_ev and S nearly agree | physics | belief | if flux were light at the seed size, the periodic seed would need a larger box than the kappa or even form | would matter for the size of the seed box | published lattice data on twist free energies; not read |
| e3 | No known tool reaches couplings of order one | L42-44, L566 | belief of both max runs | - | - | - |
| f1 | No computer-assisted step; Lean-formalizable proofs | `GOAL.md` | owner rule | obeyed; not questioned | - | - |
| f2 | No subagents, one output file, closed files until step 5 | row 731 | owner rule | obeyed | - | - |
| f3 | Port the account; work only on its open statements and on clauses it does not assert | `GOAL.md` | owner rule | the account asserts no gap; this lane is outside its statements | - | - |

Hidden assumptions added: (h1) "flux sector" always meant electric flux; magnetic and dyonic sectors were not in the vocabulary of the open files. (h2) The sectors were fixed in one frame; crossing mixes the frames (C4). (h3) Theorem L was stated for all local functions "gauge invariant or not", which hides that gauge-invariant functions need less.

**Ranking (by how much the problem changes).**

1. c1. The lane would state the consumer as (G_ev) and prove the limit half once, for the even sector. Changes the owner's reading of "confinement is on the path": it is on the path of the step only.
2. c3. The lane would carry three seeds, and ask of each tool which one it can reach.
3. d2. The lane would stop using Z_2 at large beta as a model where the target fails.
4. c2. The lane would look for a step that is not crossing (boundary values, or (EV-LOSS)).
5. e2. The lane would read lattice data on twist free energies to see whether any size gain exists.

Rows whose drop would change an owner decision: c1, c3 (whether "gap with confinement" is the right name of the crux).

<!-- END -->

