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

## Step 5. Compare with the earlier work

**What was opened and how.** Search by grep over `library/gap-*.md` (45 files), `library/prior/gap-*.md` (19), `library/exercise-skill-v2.md`, `library/l17c.md`, `gates/*.md`, `parts/*.md` and FINISH rows 697 to 730, for the objects and two or more wordings each: "even sector / even subspace / centre-even / zero-flux / zero flux"; "magnetic flux / magnetic twist / dyon / SO(3) / electric-magnetic / Pfaffian / Pontryagin"; "'t Hooft"; "extremal / ergodic / mixture / convex combination / dominated / Cesaro / 1/8"; "average over twists / sum over twists / all twists"; "contractible"; "same limit / periodic limit / zero-flux ... limit". Every matching line was read. Read in full: `gap-crux-fp.md` L108-126 and L176-184 (Remark 2.A, ranking), L222-246 and L270-288 (methods, tests); `gap-crux-fp-check.md` L28-42; `gap-mid-max.md` L218-238 (Identity FL, Remark Y); `gap-skeleton-max-b.md` L362-378 (zero-flux function, Corollary 5); `gap-zero-transport.md` L34-46 (Lemma 3, Lemma 1'); `gap-seed-check.md` L30-40, L177, L191-195; `gap-phys-seed.md` L190-216, L326-330, L386-390; `gap-skeleton.md` L104-106; `exercise-skill-v2.md` L1162-1172, L1204-1210. **Not read:** the bodies of the other gap files beyond the matching lines; `gap-skeleton-final.md` Sections 4 to 13.14 beyond the matching lines (L100, L410, L508, L539). **Not searched:** origin/main and the other YM4D pull-request branches; this checkout holds only `origin/claude/ym4d-hard-route`, and I did not fetch.

| Item | In the earlier work? | Where | Scope of a "new" mark |
|---|---|---|---|
| (F1), P_0, Z_{0,0} = (1/8) sum of the eight time-twisted Z | yes | run 2, `gap-skeleton-max-b.md` L254 (Lemma 1'), L368; `gap-zero-transport.md` L38-41 (Lemma 3); `gap-mid-max.md` L219 (Identity FL); `gap-crux-fp.md` L121 (Remark 2.A (a)) | - |
| (TM-tw): transfer operator for twisted spatial weights, several flips, all 64 twists, covariance under permutations of the axes | yes, checked by one model | `gap-seed-check.md` L177 (Remark F3 point, Claude Opus 5.5, row 698); `gap-crux-fp-check.md` L30-38 (row 716, Claude Opus 5.5: re-derived, HOLDS) | - |
| C1, single-slice form: functions of contractible spatial loops commute with the flips | yes | `gap-zero-transport.md` L38 Lemma 3 (d) | - |
| C1, slab form for the class 𝔄, with the gauge-transformation argument | partly (the slab form is not in the files I searched) | - | not found in the searched files |
| C2 (S1), (S2), (S3) | partly: Z^(0) <= Z and the even ground state are in Lemma 1' and Identity FL; lambda_m <= lambda_0 is used in Remark Y ("its top eigenvalue is that of the untwisted slice") without proof; (S1) for twisted boxes and (S2) for all 64 twists are not stated | `gap-zero-transport.md` L43-44; `gap-mid-max.md` L234 | not found in the searched files |
| C3 (b): Theorem L1 in the even sector | partly: run 2 asserts the consequence in one sentence, with no proof ("So every infinite-volume limit ... of these tori has exponential decay of the truncated functions of contractible-loop observables") | `gap-skeleton-max-b.md` L375 | - |
| C3 (c), (d): the periodic state equals the even state on 𝔄 (mixture argument, explicit bound); (G_ev) gives the gap of the periodic volume-first limit | **new** | - | all of the scope above; wordings searched: mixture, extremal, ergodic, convex combination, dominated, Cesaro, "1/8", "same limit", "periodic limit", "zero-flux ... limit". The nearest earlier lines: `gap-crux-fp.md` L115 (a3: "A gap for local observables in infinite volume is weaker ... no finite criterion is known for it in a gauge theory"), `gap-skeleton.md` L104 (cylinder limits are not by definition in the account's class of cubic tori), `exercise-skill-v2.md` L1206 (P' gives a gap only on the space its class generates). None states or proves C3 (c) |
| C4, first half: the even trace is not symmetric "by its form"; crossing turns the electric twists (1,3), (1,4) into magnetic ones | yes | `gap-crux-fp.md` L122 (Remark 2.A (b)); `gap-mid-max.md` L234 (Remark Y) | - |
| C4, identity (*) with the factor 1/4 and the projection (1 + C_1)/2; the sum rule (SR) | partly: Remark Y says "a sum over the two values of a magnetic twist of the slice" as a sketch, "not proved here"; the factor, the sixteen sectors and (SR) are not there | `gap-mid-max.md` L234 | (SR): not found in the searched files |
| C5, full set: the sum over all 64 twists is symmetric and is 8 Tr of the direct sum over magnetic twists of T^(m) P_0 | yes | `gap-crux-fp.md` L123 (Remark 2.A (c)), checked `gap-crux-fp-check.md` L34-38 | - |
| C5, kappa set (the sign (-1)^{Pf(k)}, sectors with electric flux equal to magnetic flux) | **new** | - | grep for dyon, Pfaffian, Pontryagin, SO(3), "electric-magnetic", "sign" near "twist": the only SO(3) lines are the Mack-Petkova splitting (`gap-crux-restate.md` L290-294) and literature notes; none is a twist sum with a sign |
| C5, classification: exactly three; four sectors for one pair; none is the even sector alone | **new** (the "none" part sharpens Remark 2.A (b), which says "I did not prove that this trace is not symmetric") | - | same scope |
| C6: Theorem S for the full set | partly: Remark 2.A (c), (d) sets up the full sum and reads it as having no seed in a confining phase; Theorem S for it is not stated | `gap-crux-fp.md` L123-124 | - |
| C6: Theorem S for the kappa set | **new** | - | same scope as C5 |
| C7: S_kappa <= S_full | **new** | - | same scope |
| C8 (belief): in a confining phase the magnetic sectors are light | yes, RECALLED there | `gap-crux-fp.md` L124; `gap-mid-max.md` L234 | - |
| Step 4, row c1 (the limit half needs the even sector only) | partly: named as an assumption (a2, a3), ranked sixth, not resolved | `gap-crux-fp.md` L114-115, L181 | - |
| Step 4, row d2 (Z_2 at large beta is not a model where the target fails) | partly: a2 says "Z_2 at large beta has a bulk gap and fails the seed (F9)"; the tests of L280-281 still use it with T = the whole-space seed | `gap-crux-fp.md` L114, L280-281 | - |
| Identity FL: 1 + S = (1 + S_0)/(1 - U); the two halves independent in the class | yes; I did not derive it; it is the stronger form of my split and I use it | `gap-mid-max.md` L219-232 (row 708) | - |
| (Z-UNB) splits into L m_0(L) unbounded and L E_e(L) unbounded | yes | `gap-phys-seed.md` L328 (row 720, unchecked) | - |
| (DS-tw), (W): a one-box criterion over boundary values for local observables | yes; it is the lane's one earlier candidate without flux sectors | `gap-ds-gauge.md` (row 691); `gap-crux-fp.md` L115, L245 | - |

**Corrections to my inventory.** Item 5/6: (TM-tw) is not an open input. It is the Remark F3 point of `gap-seed-check.md` with the extension in `gap-crux-fp-check.md` L30-38, checked by Claude Opus 5.5 (same provider as this run). I use it with that standing. Step 3.6: the range of 1 + V is corrected in 8.5.

**Where the earlier work is stronger.** Identity FL is an exact identity for the periodic box; my C2 is weaker on the periodic box and adds the twisted boxes. Run 2's Lemma 1' bounds S^(0) by the free-energy defect of the even function.

**Credit.** Run 2 of Claude Fable 5.2 max (rows 670, 681: Lemma 1', Lemma 3, the zero-flux function, Corollary 5). Row 708 author (Identity FL, Remark Y). Row 712 author (Remark 2.A, assumptions a2, a3). Rows 698 and 716, Claude Opus 5.5 (the twisted transfer operator and the 64-twist form). Row 697 author (Theorem S, Theorem F). Row 700 author (Theorem L). 't Hooft (twists, electric and magnetic flux, duality). Aharony, Seiberg and Tachikawa (the three global forms; recalled).

**What the fresh pass added.** C3 (c), (d); the kappa set and its Theorem S; the classification; (SR); C7; the slab form of C1.
**What it only found again.** (F1), the zero-flux function, the full 64-twist sum, the statement that the even trace has no symmetric form, the split of the seed into a glue half and a flux half.

## Step 6. The blockage: discard tests and set-aside methods

Here T, the statement a tool must give, changes. Rows 712 and 720 judged every method against T_0 = the periodic seed on the whole space. By C3 the consumer is T_1 = (G_ev). By C6 three seeds give T_1.

### 6a and 6d. Every method set aside, and its verdict re-judged for T_1

Sources read first-hand: `gap-crux-fp.md` L222-246 (22 methods, row 712); `gap-phys-seed.md` L190-216 (Q1 to Q14, row 720; lines read to 330 characters, so the long cells are read in part); `gap-crux-fp.md` L114-124 and `gap-mid-max.md` L234 for W1 to W3. "As reported" means: valid as reported, not re-derived here, and the reason does not read the flux sectors.

| # | Method (authors) | Reason given | Kind | Verdict for T_1 |
|---|---|---|---|---|
| W1 | A seed for the even sector by a sum over twists (row 712 Remark 2.A (d); row 708 Remark Y) | in a confining phase the magnetic twists cost little, so the sum has eight nearly equal top eigenvalues | fails a test; the test is RECALLED ('t Hooft) | **too strong.** It assumes equal weights. The sum with the sign (-1)^{Pf(k)} is symmetric and admissible (C5), and it holds no purely magnetic sector. What comes back: Theorem S for the kappa set (8.4). Range: wherever the dyonic sectors are heavy |
| W2 | A gap for local observables in infinite volume as the target (row 712, a3) | "no finite criterion is known for it in a gauge theory" beside (DS-tw) | open premise | **corrected.** C3 with C6 gives three finite criteria; the full and kappa seeds do not need a gap on the whole space |
| W3 | The zero-flux function of periodic tori in Route Z (run 2, `gap-skeleton-max-b.md` L450-452) | it holds pairs of winding flux tubes and winding sheets; the zero-free tube has measure a^2 | wrong quantity | as reported. It concerns zeros in complex beta, not this wall |
| 1 | Griffiths-type inequalities (Griffiths, Kelly, Sherman; Ginibre) | hold for Z_2 and U(1), where the seed fails | test | the U(1) half stands (T_1 fails for U(1) at large beta). The Z_2 half is valid for T_0 only: see 6c |
| 2 | Dual forms with positive weights | the same | test | the same |
| 3 | A monotone quantity along the scale | restates the seed | circular | as reported |
| 4 | Derivative in beta, (VIR_K), (DEF_K) | three ways failed | wrong quantity | as reported |
| 5 | Bakry and Emery (Shen, Zhu, Zhu) | small beta only | small number | as reported; range as in row 712 |
| 6 | Dobrushin on one link (Theorem DOB) | 18 beta < 1 | small number | as reported. It gives T_1 directly where it holds (all boundary values) |
| 7 | Cluster expansion (Osterwalder and Seiler) | beta < 1/12800 | small number | as reported |
| 8 | Zeros of Z along the coupling | radius shrinks with the gap | gap-dependent constant | as reported |
| 9 | Polchinski flow, two-scale log-Sobolev (Bauerschmidt and Bodineau; Otto and Reznikoff) | Hessian bound at every scale; blind to the group | test; unverified | as reported |
| 10 | Migdal-Kadanoff bounds (Tomboulis) | an unproved inequality (Ito and Seiler) | open premise | as reported |
| 11 | Simon and Lieb; Aizenman and Simon | spin systems; includes O(2) | other setting | as reported |
| 12 | Infrared bounds (Frohlich, Simon, Spencer) | order, not decay | wrong quantity | as reported |
| 13 | Durhuus and Frohlich | comparison across two dimensions open | open premise | as reported |
| 14 | Loop equations and bootstrap (Kazakov and Zheng) | numerical; local observables, not two volumes | rule f; wrong quantity | as reported. T_1 is still a statement on a box |
| 15 | Twist ratios (Tomboulis and Yaffe; Kanazawa); (TUBE'); the Z_2 splitting (Mack and Petkova) | premise open at the needed coupling | open premise | valid. **Its place changes:** these tools give the electric flux half. By C3 that half is not on the path of the limit; it is on the path only inside the periodic seed |
| 16 | Knabe; Lemm and Mozgunov | other setting; rate filter | other setting | as reported |
| 17 | Gopfert and Mack | abelian | other setting | as reported |
| 18 | Small-volume spectrum (Luscher; Koller and van Baal) | small volume only | other setting | as reported |
| 19 | Orbit-space curvature (Singer; Mondal) | heuristic | unverified | as reported |
| 20 | Random-cluster sharpness (Duncan and Schweinhart) | Potts gauge models | other setting | as reported |
| 21 | Mixing on a box, (W), (DS-tw) (row 691) | a hypothesis; not verified at order one | open premise | as reported. It is the lane's one earlier criterion that reads no flux sector |
| 22 | Large N (Kopper) | N large | small number | as reported |
| Q1-Q4 | Flow quantities that hold the whole thermal sum (row 720, class I) | none is easier than the seed | circular / open | as reported for T_0. For T_1 each has a kappa form and a full form (S_kappa, the defect of W_kappa). Whether one of them is easier is not known; C8 (belief) says no for SU(2) |
| Q5-Q8 | Twist ratios, Schrodinger functional, twisted Polyakov loop, force (class II) | they hold the flux half at most | wrong quantity | valid for T_0. For T_1: still wrong quantity (they do not hold S_ev) |
| Q9-Q12 | Gradient flow coupling, the account's coupling, plaquette shift, kappa(b) | local, or monotone in every model | wrong quantity | as reported |
| Q13 | The lowest zero-flux gap of a twisted box | (STEP) is false at weak coupling | fails in SU(2) itself (RECALLED one-loop number) | as reported. Note: the kappa set contains sectors of twisted boxes, so Q13's small-volume data bear on the kappa seed at small size |
| Q14 | Route T, the twisted thin torus | its crux is (AC') | open premise | as reported |

Where the corrected verdicts matter: W1 and W2 are on the path of (GAP), in the choice of the seed. The Z_2 half of rows 1 and 2 is off the path at present (no tool waits behind it).

### 6b. First principles on the blockage

A tool for this wall must give (G_ev): small even thermal sums on a sequence of cubes. Three kinds of statement can do it. (i) A seed on one size with a crossing step. Crossing exchanges electric and magnetic twists (C4), so the seed must be on a self-dual set of sectors, and there are three (C5). (ii) A bound over all boundary values of one cube ((DS-tw), row 691). (iii) An even step by another mechanism; none is known. The least a tool of kind (i) must use: which flux is heavy at the seed size. **The blockage in one sentence:** the step from one size to all sizes is a duality between the two time directions, the duality exchanges electric and magnetic flux, and so a one-size criterion that crosses must say which flux is heavy; for SU(2) that statement is confinement.

### 6c. The discard tests in their logical form

| Test (model M') | Class K | The exact T that fails in M' | How the failure is known | What a tool must use to pass | From which value it binds |
|---|---|---|---|---|---|
| U(1), four dimensions, weak coupling | groups that contain -1, Wilson-type weights | T_0, T_1, all three seeds, (GAP): the photon is centre-blind and lies in the even sector | THM recalled (Guth; Frohlich and Spencer), large beta only; no source read in this run | a property that U(1) does not have | from beta_U (row 712: GUIDE, about 1.01) |
| Z_2, four dimensions, large beta | the same | **T_0 only** (the eight electric sectors are degenerate). T_1 and (GAP) hold; the full and kappa seeds are expected to hold | failure of T_0 at fixed size: proved by hand in `gap-seed-check.md` L191-195 given the Z_2 form of Lemma 1.1 (not written). The gap of plaquette observables: recalled, no source read | for T_0: a property that Z_2 does not have. **For T_1: nothing.** A tool for T_1 may hold for Z_2 at large beta | for T_0: from about 0.44 (row 712, GUIDE). For T_1: at the transition point only, and above it only for a tool whose hypothesis is monotone in beta |
| Z_2 at its transition | the same | T_0 and T_1 (two phases: two nearly equal top eigenvalues in the even sector) | BELIEF (numerics; a first-order transition is not proved) | - | one coupling |
| Product of SU(2) at small beta with an Ising model at large J (row 708) | the abstract setting | T_1 for the product algebra (S_0 tends to 1); T_0 too | PROVED GIVEN two recalled Ising facts (`gap-seed-shape.md` lead note, point 1) | - | shows that U small does not give S_0 small |
| SU(2) on a small torus at weak coupling | SU(2) itself | all three seeds at small size (many low levels; in the twisted box m = (1,1,1) the sector e = (1,1,1) is degenerate with its vacuum, `gap-phys-seed.md` L110) | RECALLED small-volume physics | not a test of a tool: it bounds the seed size from below | - |

**The corrected filter.** "Z_2 at large beta: the seed is false, and it must be" (`gap-crux-restate.md` L227; the range bound "about 0.44" for tools blind to the group, `gap-crux-fp.md` L280-281; "in every comparison model the half that fails is (Z-UNB)", `gap-skeleton-final.md` L562). Valid form: these are statements about T_0. For T_1 the model Z_2 at large beta is a model where the target holds. So it refutes no tool for T_1, and it constrains only tools for the periodic seed. A pass is still no support.

**Are the tests enough?** For T_1 the lane has one test that rests on a theorem at large beta (U(1)) and none that separates the three seeds for SU(2). The statement "SU(2) is in the phase where electric flux is heavy" is a belief.

## Step 7. Routes: generate, try to kill, rank

`docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md` read in full before this step. No subagents: the passes below were made one after the other by the main agent, so they are not independent.

**Exact target contract.** Target: (Q1), (Q2) of Step 1. Quantifiers: Wilson SU(2), one real beta, tori with sides at least 3; "one size" means one cube and one time. Allowed premises: the checked statements of Step 2 and (TM-tw). Forbidden weakenings: a hypothesis at all sizes sold as one size; clustering assumed for the limit. Edge cases: non-simple top eigenvalue of a sector sum; observables that touch a flip plane; time extents below half the side. Completion witness: a written proof, or an explicit model. Not closure: a belief about confinement; a run.

**Routes.**

| Route | Family (object; mechanism; terminal obligation) | Assumption dropped | What one must believe | First artifact | Cost | What it changes |
|---|---|---|---|---|---|---|
| A | the even state as a mixture of eight twisted states; a clustering state is not a mixture; no terminal obligation | c1, c6 | nothing | Theorem EV-L (8.2) | done | the limit half reads the even sector only |
| B | the signed twist sum W_kappa; crossing; the kappa seed at one physical size | c3 | that the dyonic sectors are heavy at the seed size | Theorem S for W_kappa (8.4) | done; the seed is open | a second form of the crux, true in every phase where electric or magnetic flux is heavy |
| C | the full twist sum; crossing; the full seed | c3 | that magnetic flux is heavy | the same theorem | done | a form of the crux for a deconfined massive phase |
| D | the even trace and the sixteen crossed sectors; an even step with no flux sector; (EV-STEP) | c2 | that light flux at one size cannot make light even states at twice the size | (EV-LOSS), a test model (8.5, 8.6) | hours | confinement would leave the path |
| E | conditional laws on one cube; Dobrushin-Shlosman mixing; (DS-tw) | c2 | a mixing bound at order one | row 691 | not attacked: row 691 owns it (rule 0a) | the same as D |
| F (misframing pass) | "does (GAP) need the flux sectors" joins two questions. The limit does not (A). The step needs a choice of phase (C5). The question that replaces it: which of the three seeds can a tool reach, and can lattice data separate them at the seed size? | the framing | - | Step 6 | done | the name of the crux |

**Outside view (literature).** No source was fetched in this run. All entries are recalled, or read as lines of the lane's digests.

| Source | What it shows | Maps to the repo? | Reading state |
|---|---|---|---|
| 't Hooft, Nucl. Phys. B 153 (1979) 141 | twisted boundary conditions; electric flux sectors as a Z_N Fourier transform of twisted partition functions; duality between electric and magnetic flux free energies under the exchange of axes | yes: (F1), C4, (SR) re-derive the finite identities from items 5, 6 and (TM-tw) | recalled |
| Aharony, Seiberg, Tachikawa, JHEP 08 (2013) 115 | theories with algebra su(2): SU(2), SO(3)_+, SO(3)_-; the last differs by a sign (-1)^{P(w_2)/2} in the sum over bundles; which line operators exist in each | names the three sets of C5; the sign on the four-torus is Pf(k) mod 2. The identification is not used in a proof | recalled |
| Tomboulis and Yaffe (1985); Kanazawa; the Ito-Seiler criticism | inequalities between Wilson loops and twist ratios | already in the lane: `prior/gap-seed-lit.md` L69, row 697 Theorem F | digest line read |
| de Forcrand and von Smekal (2002); Kovacs and Tomboulis (2000) | lattice data on twist and electric-flux free energies of SU(2) | would test belief e2 (size of the flux weights at the seed size) | recalled; not read |
| Koller and van Baal; van Baal's review | small-volume spectra, twisted boxes | already in the lane: `prior/gap-small-volume-lit.md`, row 720 | digest lines read |

**Lenses used.** (1) Finite groups and bilinear forms: the twist group Z_2^6, the pairing of electric with magnetic twists, self-orthogonal subgroups (toy: the two-dimensional Ising model with its three sector sets; falsifier: a fourth invariant set; artifact: 8.3 and the enumeration of 8.6). (2) Ergodic theory: extremal invariant states (toy: a mixture of two product states; falsifier: a positive functional below a clustering state that differs from it; artifact: 8.2). (3) Outside the lane's vocabulary: global forms of a gauge theory and one-form symmetry (item 23). Considered and found empty for this wall: number theory, logic and independence, K-theory and index theory, optimization.

**Reframes tried.** Object against readout: the object (the transfer operator on the whole space) holds more than the readout (tr(F^2)) reads. Local pattern against global structure: flux is global, the target is local. Finite carrier against limiting family: (G_ev) is a family statement, the seeds are finite carriers. Obstruction against missing input: the even step is a missing input, not an obstruction.

**Kill pass (same agent, separate pass; not independent).**

| Route | Assumes the target? | Against a checked result? | Tried before? | Fails a valid test? | Rule broken? | Terminal obligation | Verdict |
|---|---|---|---|---|---|---|---|
| A | no | no; it agrees with Theorem L3 (b) where both apply | no (Step 5) | U(1): hypothesis (G_ev) false there, as it must be | no | none | survives |
| B | no | no | no | U(1): the kappa seed is false (photon). Z_2 at large beta: no failure needed | no | the kappa seed: unknown/comparable to the periodic seed; not shown weaker for SU(2) | wounded: no proof that it is easier than the periodic seed; by C8 (belief) it is confinement again |
| C | no | no | partly (Remark 2.A (c), (d)) | - | no | the full seed: believed false for SU(2) at large size | dead for SU(2) if item 16 holds (a belief, so not a refutation); survives for a deconfined massive model |
| D | no | no | named open in row 712 | the inequality form of the even step fails in a two-dimensional test model (8.6, guide) | no | (EV-STEP): weaker than every seed; its truth is open | wounded: no mechanism |
| E | - | - | row 691 | - | - | (DS-tw) | not attacked here |

**Rank** (change if it works, over cost).

| Rank | Route | Terminal obligation | Strength against (GAP) | Kill verdict | First artifact | What it changes | Stop or reopen |
|---|---|---|---|---|---|---|---|
| 1 | A | none | - | survives | 8.2 | consumer becomes (G_ev) | reopen only on a WRONG from the check |
| 2 | B | kappa seed | sufficient; not known necessary | wounded | 8.4 | a second form of the crux | stop unless lattice data or a tool separates the kappa seed from the periodic one |
| 3 | D | (EV-STEP) | sufficient with (G_ev); weaker than the seeds | wounded | 8.5, 8.6 | confinement off the path | reopen on a new mechanism that bounds the crossed flux weights |
| 4 | C | full seed | sufficient | dead for SU(2) under belief 16 | 8.4 | - | reopen if SU(2) data showed heavy magnetic flux |

**Approach registry (this wall).**

| Family | Object | Mechanism | Terminal obligation | Strength vs target | Status | Evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| limit by mixture | even state = mixture of twisted states | extremality of a clustering state | none | - | candidate-complete (not checked) | 8.2 | - |
| periodic seed | W = Z | crossing | (SEED-phys) | stronger than (GAP) needs | blocked: no tool | rows 697 to 720 | a tool at order one |
| kappa seed | W_kappa | crossing | kappa seed | unknown/comparable | provisional | 8.4 | a separation from the periodic seed |
| full seed | sum of all twists | crossing | full seed | believed false for SU(2) | retired for SU(2) (belief) | 8.4, Remark 2.A (d) | - |
| even step | sixteen crossed sectors | none known | (EV-STEP) | weaker | blocked-local | 8.5, 8.6 | a bound on crossed flux weights from even data |
| boundary values | conditional laws on a cube | Dobrushin-Shlosman | (DS-tw) | unknown | owned by row 691 | - | - |

<!-- END -->

