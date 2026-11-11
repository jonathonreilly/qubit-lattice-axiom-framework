lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-12T06:52Z

# Exercise (skill v2) on the flux half of the crux: does (GAP) need the flux sectors?

**Header.** Written by Claude Fable 5.2 (Anthropic), effort high, as author, Mac mini worker 1, one session, no subagents. Commit 84a72beb5, 2026-11-11. FINISH row 731 is the caller's brief. Skill: `docs/ai_methodology/skills/exercise/SKILL.md` at 1eb15ac428 (fetched to a scratch folder, read in full). **Nothing in this file is checked by another model.** Every statement below is `argued`, `refuted`, `guide`, `reading` or `open` in the sense of the skill; none is `checked`.

**Refresher replacement.** This target's `GOAL.md` reads no framework axiom or primitive (a standalone proof target). I read `GOAL.md` in full and the rules of `FINISH.md` (lines 1 to 84, 299 to 349, row 731) in place of the framework refresher list. No approved primitive enters.

**What this run did not cover** (kept current):

- No check by another model. No blind check of the plain version and no independent kill pass (no subagents allowed).
- origin/main and the other YM4D pull-request branches were not searched (this checkout holds only `origin/claude/ym4d-hard-route`; nothing was fetched). Every "new" mark means "not found in this branch's record", with the scope of Step 5.
- No primary paper was read. 't Hooft (1979), Aharony, Seiberg and Tachikawa (2013), Kaufman, Schultz-Mattis-Lieb, and the facts on Z_2 and U(1) are recalled.
- The account `YM4_1400.tex`: lines 140-175, 1680-1730, 1884-1910 only.
- (TM-tw), the transfer operator for twisted spatial weights with all 64 twists, was not re-derived; it is taken from two check files (8.1).
- `gap-transfer.md`: Section 8, 9.3 and Lemma A0 read; Sections 1 to 7 not read. The 36 verdicts of rows 712 and 720 are listed in Step 6; 33 are "as reported, not re-derived". The cells of row 720's table were read to 330 characters.
- The passage from Theorem EV-L to the transfer operator of the limit and to the continuum (Theorem L3 (e), Propositions P, P' of row 700, with 𝔄 in place of all local functions) was not rewritten.
- (EV-STEP) and (KP) for SU(2) are open. No statement here is about SU(N), N >= 3.
- No four-dimensional gauge theory was run; the runs are a two-dimensional toy and a finite enumeration.

## Status block

| Step | State | Main result |
|---|---|---|
| 0 Locate the record | done | open and closed lists; `open-core.md` has no line on this wall |
| 1 State the wall twice | done | (Q1), (Q2); no blind check |
| 2 Inventory | done | 23 items with marks; the wall sits in two SUPPLIED items (periodic seed, periodic limit) |
| 3 Reason up | done | C1 to C9: the limit half reads the even sector only; crossing exchanges electric and magnetic twists; three self-dual sector sets |
| 4 Assumptions table | done | 21 rows; first: c1 (whole space in the limit half, needed by the method only), c3 (periodic seed, a habit) |
| 5 Compare with earlier work | done | found again: Remark 2.A, Remark Y, Identity FL, run 2's zero-flux function; new in this branch: Theorem EV-L, the kappa set, the classification, S_kappa <= S_full |
| 6 Discard tests and set-aside methods | done | 3 corrected (W1, W2, the Z_2 test); 33 as reported |
| 7 Routes | done | A (limit by mixture) survives; B (kappa seed) wounded; C (full seed) dead for SU(2) under a belief; D (even step) wounded |
| 8 Real attempts | done | 8.2 Theorem EV-L; 8.3 Proposition CL; 8.4 Theorem S-w, Corollary EV; 8.5 (*), sum rule, loss, Proposition AS, (EV-STEP) open; 8.6 runs; 8.7 Lemma GS, (KP) proved for Z_2, open for SU(2) |
| 9 Report | done | answer: (GAP) needs (G_ev) only; the known step needs one of three seeds with seven flux sectors |

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

where kappa is the deficit of Lemma K for the periodic box and 1 + V := Theta = 4 (sum_x y_x^2)/(sum_x y_x)^2, a number in [1/4, 4] fixed by the sixteen crossed sector weights y_x (8.5 gives the exact form; corrected at step 5). Theta is 1 when four crossed sectors carry equal weight and the other twelve none, which is the case of a seed on a group of four.

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

## Step 8. Real attempts

Rule 0a before each attempt: `library/open-core.md` has no line for the even sector, a twist sum or a seed (Step 0). The FINISH rows 697 to 730 name "a step from one size to all sizes for the centre-even sector alone" as open (row 712) and assign it to this row (row 721, proposal 1). (TUBE'), (MF), (VORT) and (DS-tw) belong to rows 697, 708, 670 and 691; I do not attack them.

All proofs below are by Claude Fable 5.2 and are not checked by another model.

### 8.1 Inputs and their standing

- **(TR)**: `library/gap-transfer.md` statements (1) to (4), (8), Lemma A0, and 9.3 (the flips Z_k, the sectors). Checked by Claude Opus 5.5 (row 671), for every box by rows 698, 699 (Lemma 1.1 of `gap-seed-check.md`). Read here: Section 8 and 9.3 in full, Lemma A0 (statement).
- **(L)**: `library/gap-seed-limit.md` Lemma T, Proposition C, Theorem L1, Theorem L3 (a). Checked by Claude Opus 5.5 (row 703). Read in full.
- **(S)**: `library/gap-crux-restate.md` Lemmas A, K, X, E, E', Theorem S, Corollary S3', Theorem D (b). Checked by Claude Opus 5.5 and Codex gpt-6-astra (rows 698, 699). Read in full.
- **(TM-tw)**: for every box B and every magnetic twist m, the operator T_{B,m} = M' C_E M' with the twisted spatial potential is positive, trace class, with a simple top eigenvalue and a strictly positive eigenfunction; the flips commute with it; Tr(T_{B,m}^a C^e) = Z^{e+m}(a, B); a permutation of the axes maps the twist k to its image and keeps Z^k. Source: `gap-seed-check.md` L177 (Remark F3 point) and `gap-crux-fp-check.md` L30-38, both by Claude Opus 5.5 in check files. They state the extension "word for word" from `gap-transfer.md` and re-derive it in a few lines. I did not re-derive it. Standing: argued in two check files by one model; no separate check of it exists. 8.2 does not use (TM-tw). 8.4 and 8.5 do.

### 8.2 Theorem EV-L (the limit half reads the even sector only). On the path of (GAP).

**Setting.** Torus Lambda x Z_T with Lambda = (Z/L)^3, L >= 3, time direction 1, T_P the transfer operator of (TR), Rn = T_P/lambda_0. For nu = 2, 3, 4, C_nu f = f o Z_nu, where Z_nu flips the links (x, nu) with x_nu = 0. For e in {0,1}^3, C^e is the product of the C_nu with e_nu = 1. P_0 = (1/8) sum_e C^e. By 9.3 of (TR) the C_nu are commuting unitary involutions that commute with T_P, and Omega is in the range of P_0.

**The class 𝔄.** A slab function F on [a, b] (Section 8 of (TR)) is in 𝔄_L if (i) F(g.U) = F(U) for every g from the sites of the slab to {+1, -1}, where (g.U)(x, mu) = g(x) g(x + mu) U(x, mu) for spatial and time-like links; (ii) for each nu the nu-range of F has width at most L - 2. Functions of the numbers tr U_p of finitely many plaquettes, and of traces of contractible closed loops, satisfy (i).

**Lemma CB (centre-blind).** For F in 𝔄_L on [a, b]: K_F(Z_nu u, Z_nu v) = K_F(u, v). So the operator k_F := lambda_0^(-(b-a)) S_{K_F} (for b = a: k_F = M_F) commutes with each C_nu and with P_0.

Proof. In the integral that defines K_F substitute U(t) -> Z_nu U(t) for a < t < b. Haar measure is invariant. By 9.3, T_0(Z_nu u, g.Z_nu v) = T_0(Z_nu u, Z_nu(g.v)) = T_0(u, g.v). It remains to show F(Z_nu U(a), ..., Z_nu U(b); g) = F(U; g). By (ii) there is r != 0 such that no link (x, nu) with x_nu = r is in the support of F: the nu-range [alpha, beta'] holds the beta' - alpha <= L - 2 link positions alpha, ..., beta' - 1, so at least two of the L positions are free, and one of them is not 0. Put g(x) = -1 on the sites of all slices with x_nu in {1, ..., r} (cyclic order) and +1 elsewhere. Then g.U differs from U exactly on the links (x, nu) with x_nu = 0 and with x_nu = r: a link in another spatial direction or in the time direction joins two sites with the same x_nu. F does not read the links at x_nu = r. So F(Z_nu U) = F(g.U) = F(U) by (i). For b = a the statement is F(Z_nu u) = F(u), the same argument. QED

**Definitions.** For F in 𝔄_L on a slab of width w <= T - 2 and e in {0,1}^3:

omega^e(F) := Tr(C^e k_F Rn^(T-w)) / Tr(C^e Rn^T), omega_ev(F) := Tr(P_0 k_F Rn^(T-w)) / Tr(P_0 Rn^T), q_e := Tr(C^e Rn^T) / sum over e' of Tr(C^e' Rn^T).

omega^0 = omega_per, the periodic torus state (8.1 of (TR)). S_ev(t) := Tr(P_0 Rn^t) - 1 >= 0 (the sum over the excited eigenvalues of T_P in the range of P_0, an invariant subspace that contains Omega). m_ev := log(lambda_0/lambda_1^ev), lambda_1^ev the second eigenvalue of T_P on the range of P_0.

**Lemma MX (mixture).** (a) Tr(C^e Rn^T) > 0 and q_0 >= 1/8. (b) Each omega^e is linear on the slab functions of 𝔄_L of a given slab, does not depend on the slab chosen for F, is invariant under time translations, and satisfies omega^e(F) >= 0 for F >= 0 and omega^e(1) = 1. (c) omega_ev = sum_e q_e omega^e. (d) For real X in 𝔄_L: omega_per(X)^2 <= omega_per(X^2) <= 8 omega_ev(X^2).

Proof. (a) C^e T_P^T has the kernel a_T(Z^e u, v), a_T the kernel of T_P^T. By A0(e) of (TR), Tr(C^e T_P^T) is the integral of a_T(Z^e u, u). a_T is strictly positive ((4) of (TR)), so the trace is positive. C^e is a unitary involution that commutes with T_P^T >= 0, so Tr(C^e T_P^T) <= Tr T_P^T. Hence q_0 >= 1/8.
(b) Linearity: K_F is linear in F. Positivity: for F >= 0, K_F >= 0, and Tr(C^e S_{K_F} T_P^s) is the integral of K_F(Z^e u, v) a_s(v, u) >= 0 (A0(e); s = T - w >= 2). Normalisation: K_1 = a_w (8.3 of (TR)), so k_1 = Rn^w. Slab: if [a', b'] contains [a, b], integrating the extra slices and time-like links gives K'_F = a_{a-a'} * K_F * a_{b'-b} (the computation of 8.5 of (TR)), so k'_F = Rn^(a-a') k_F Rn^(b'-b); C^e commutes with Rn and the trace is cyclic, so the value does not change. Time translation: K_F depends on F only through its position relative to the slab.
(c) P_0 = (1/8) sum_e C^e in numerator and denominator.
(d) omega_per is positive and normalised on the algebra of slab functions of 𝔄_L of one slab (which is closed under products), so omega_per((X - t)^2) >= 0 for all real t gives the first inequality. By (c), omega_ev - q_0 omega_per = sum over e != 0 of q_e omega^e >= 0 on positive functions; apply it to X^2 and use (a). QED

**Lemma L1-ev (Theorem L1 in the even sector).** Let F, H in 𝔄_L be as in Lemma T of (L): time ranges [0, b] and [a', b'], d = a' - b >= 1, d' = T - b' >= 1, T - w(F) >= 2, T - w(H) >= 2, and the product FH in 𝔄_L. Then

|omega_ev(FH) - omega_ev(F) omega_ev(H)| <= ||F|| ||H|| (exp(-m_ev d) + 6 S_ev(d')), and |omega_ev(F) - <F>_{L,inf}| <= 2 ||F|| S_ev(T - w(F)).

Proof. Choose the orthonormal eigenvectors phi_j of T_P as eigenvectors of the C_nu (each eigenspace of a positive eigenvalue is finite-dimensional and invariant; `gap-seed-check.md` L69). Let J be the set of j with P_0 phi_j = phi_j; 0 is in J. By Lemma CB, k_F and k_H commute with P_0. So Tr(P_0 k_F Rn^d k_H Rn^(d')) = sum over i, j in J of rho_i^d rho_j^(d') <phi_j, k_F phi_i><phi_i, k_H phi_j>, by the proof of Lemma T with P_0 Rn^t = sum over j in J of rho_j^t |phi_j><phi_j|. Split into (0,0); i != 0, j = 0; i = 0, j != 0; i, j != 0, as in Proposition C. With (K1), (K2) of (L): the first term is f h; |u| <= ||F|| ||H|| exp(-m_ev d); |u'| <= ||F|| ||H|| exp(-m_ev d'); |v| <= ||F|| ||H|| exp(-m_ev d) S_ev(d'). The one-point functions are (f + alpha)/(1 + S_ev(T)) with |alpha| <= ||F|| S_ev(T - w(F)), and the same for H. Also |omega_ev(FH)| <= ||F|| ||H|| by Lemma MX (b), (c). The algebra of Theorem L1 of (L) is then unchanged, with S_ev in place of S; S_ev(t) is non-increasing in t and exp(-m_ev t) <= S_ev(t). The second claim is the Remark after Theorem L2 of (L). QED

**Theorem EV-L.** (c) Let A in 𝔄_L be real with time width w, delta >= w + 1 and N >= 1 integers with N delta <= T - 2. Then

|omega_per(A) - omega_ev(A)| <= ||A|| ( 8 [ (1/N)(1 + 2/(exp(m_ev) - 1)) + 6 S_ev(T - N delta) ] )^(1/2).

(d) Let L_i -> infinity, n_i <= L_i/2, with sigma_i := S_ev(n_i; L_i^3) -> 0 and m_ev(L_i^3) >= m_0 > 0 for all i, and L_i - n_i -> infinity. Then for every local function F of Z^4 that satisfies (i): omega_per on L_i^4, omega_ev on L_i^4 and the cylinder state on L_i^3 x Z differ by amounts that tend to 0. Every limit point nu of the periodic states on L_i^4 (they exist along subsequences, Theorem L3 (a) of (L)) satisfies, for F, H with (i), separated by d >= 1 in one of the four directions,

|nu(FH) - nu(F) nu(H)| <= ||F|| ||H|| exp(-m_0 d).

Proof of (c). Let c = omega_ev(A), tau the time translation, X := (1/N) sum over j = 0..N-1 of (tau_{j delta} A - c). X is a slab function of width (N-1) delta + w <= N delta - 1 <= T - 3, real, in 𝔄_L. By Lemma MX (b), omega_per(X) = omega_per(A) - c. By Lemma MX (d), |omega_per(X)|^2 <= 8 omega_ev(X^2), and

omega_ev(X^2) = (1/N^2) sum over j, l of [omega_ev(tau_{j delta} A tau_{l delta} A) - c^2].

For j = l the term is at most ||A||^2. For j < l apply Lemma L1-ev to F = tau_{j delta} A and H = tau_{l delta} A (after a translation by -j delta): d = (l - j) delta - w >= l - j, because delta >= w + 1; d' = T - (l - j) delta - w >= T - N delta + 1. The term is at most ||A||^2 (exp(-m_ev (l - j)) + 6 S_ev(T - N delta)). Sum: N diagonal terms, and for each r >= 1 at most 2N ordered pairs with |l - j| = r, and sum over r >= 1 of exp(-m_ev r) = 1/(exp(m_ev) - 1). QED

Proof of (d). Let F have time width w and satisfy (i); for large i it is in 𝔄_{L_i} and T = L_i. Real and imaginary parts are treated one at a time. Take delta = w + 1 and N_i = floor((L_i - n_i - 2)/delta), which tends to infinity. Then S_ev(L_i - N_i delta) <= S_ev(n_i) = sigma_i, and (c) gives |omega_per(F) - omega_ev(F)| -> 0. By Lemma L1-ev, |omega_ev(F) - <F>_{L_i,inf}| <= 2 ||F|| S_ev(L_i - w) <= 2 ||F|| sigma_i for large i. So the three sequences have the same limit points. Time direction: on the cylinder, by C1 (Lemma CB and 8.5 of (TR) with the even eigenvectors), |<FH>_inf - <F>_inf <H>_inf| <= ||F|| ||H|| exp(-m_ev(L_i^3) d) <= ||F|| ||H|| exp(-m_0 d); F, H and FH all satisfy (i), so the three expectations converge along the subsequence that defines nu. Space directions: the periodic state on L_i^4 is invariant under the exchange g of the axis mu with the time axis (Theorem L3 (c) of (L)); g maps functions with (i) to functions with (i); so nu(FH) = nu((gF)(gH)), and the time case applies. QED

**What 8.2 gives and does not give.** It gives: the lattice form of (GAP) on the algebra generated by 𝔄, for every limit of periodic symmetric tori, from (G_ev) alone. The passage to the transfer operator of nu and to the scaling form is Theorem L3 (e) and Propositions P, P' of (L), read with the functions of 𝔄 in place of all local functions; I did not rewrite those proofs (argued, given (L)). It does not give (G_ev): that is the step (8.4, 8.5). It covers no function that fails (i).

### 8.3 Proposition CL: the crossing-symmetric sector sets. Finite algebra; on the path as the list of admissible seeds.

**Coordinates.** A twist k in K = Z_2^6 is written in frame 1 as (e; m), e = (e_2, e_3, e_4) = (k_12, k_13, k_14), m = (m_2, m_3, m_4) = (k_34, k_24, k_23). A sector is (chi; m) with chi in Z_2^3, and chi(e) = (-1)^{chi.e}. For w: K -> R,

what(chi; m) := sum over e of w(e; m) (-1)^{chi.e}, w(e; m) = (1/8) sum over chi of what(chi; m) (-1)^{chi.e}.

A permutation of {2, 3, 4} permutes the indices of e, of m and of chi alike. The exchange tau of the axes 1 and 2 fixes k_12 and k_34 and exchanges k_13 with k_23 and k_14 with k_24: tau(e_2, e_3, e_4; m_2, m_3, m_4) = (e_2, m_4, m_3; m_2, e_4, e_3). w is **admissible** if what has values in {0} union [1, infinity) and what(0; 0) = 1.

On Z_2^4 with x = (chi_3, chi_4, m_3, m_4) put B(x, y) = x_1 y_4 + x_2 y_3 + x_3 y_2 + x_4 y_1 (mod 2). B is bilinear, symmetric, and B(x, x) = 0.

**Lemma CL1.** w o tau = w if and only if, for each (chi_2, m_2), the slice G(x) := what(chi_2, x_1, x_2; m_2, x_3, x_4) satisfies G(x) = (1/4) sum over y in Z_2^4 of (-1)^{B(x,y)} G(y) for all x.

Proof. tau does not move e_2 and m_2. Put h(e_3, e_4, m_3, m_4) := sum over e_2 of w(e; m) (-1)^{chi_2 e_2}, for fixed (chi_2, m_2). The map w -> (h for all chi_2, m_2) is a bijection, so w o tau = w if and only if every h satisfies h(e_3, e_4, m_3, m_4) = h(m_4, m_3, e_4, e_3). Now G(chi_3, chi_4, m_3, m_4) = sum over e_3, e_4 of h(e_3, e_4, m_3, m_4) (-1)^{chi_3 e_3 + chi_4 e_4} and h(e_3, e_4, m_3, m_4) = (1/4) sum over psi_3, psi_4 of G(psi_3, psi_4, m_3, m_4) (-1)^{psi_3 e_3 + psi_4 e_4}. Let h'(e_3, e_4, m_3, m_4) := h(m_4, m_3, e_4, e_3) and G' its transform. Then G'(chi_3, chi_4, m_3, m_4) = sum over e_3, e_4 of (1/4) sum over psi of G(psi_3, psi_4, e_4, e_3) (-1)^{psi_3 m_4 + psi_4 m_3 + chi_3 e_3 + chi_4 e_4}. Rename mu_3 = e_4, mu_4 = e_3: G'(x) = (1/4) sum over y = (psi_3, psi_4, mu_3, mu_4) of (-1)^{B(x,y)} G(y). And h' = h if and only if G' = G. QED

**Proposition CL.** Let w be admissible.
(a) If w o tau = w, then the set L of x in Z_2^4 with what(0, x_1, x_2; 0, x_3, x_4) > 0 is a subgroup with exactly four elements, what = 1 on it, and B(x, y) = 0 for all x, y in L. In particular L is not {0}: **the even sector alone is not the sector set of any admissible w with w o tau = w.**
(b) If w is invariant under every permutation of the four axes, then what is the indicator of one of the three sets
 Sigma_per = {(chi; 0)}, Sigma_full = {(0; m)}, Sigma_kappa = {(chi; m): chi = m},
and w is, in this order, the indicator of k = 0, the constant 1/8, and (1/8)(-1)^{Pf(k)} with Pf(k) = k_12 k_34 + k_13 k_24 + k_14 k_23. Each of the three is admissible and invariant.

Proof. (a) Let G be the slice at (chi_2, m_2) = (0, 0). G >= 0 and G(0) = 1. Lemma CL1 at x = 0: sum_y G(y) = 4. At any x: G(x) <= (1/4) sum_y G(y) = 1. A value in {0} union [1, infinity) that is at most 1 is 0 or 1. So G is the indicator of a set L with four elements. For x in L: 1 = (1/4) sum over y in L of (-1)^{B(x,y)}, so every sign is +. For x, x' in L: G(x + x') = (1/4) sum over y in L of (-1)^{B(x,y) + B(x',y)} = 1, so x + x' is in L.
(b) Step 1. For any (chi_2, m_2), the slice G is non-negative and G(0) = (1/4) sum_y G(y); so if G(0) = 0 then G = 0. Let A be the set of (c, n) in Z_2^2 with what(0, 0, c; 0, 0, n) > 0. By the invariance under the permutations of {2, 3, 4}, what(c, 0, 0; n, 0, 0) > 0 if and only if (c, n) is in A. So what(chi; m) > 0 implies (chi_2, m_2) in A, and by the same invariance (chi_nu, m_nu) in A for nu = 3, 4. Hence the support Sigma of what lies in A^3 := {(chi; m): (chi_nu, m_nu) in A for nu = 2, 3, 4}.
Step 2. By (a), L has four elements and lies in {x: (x_1, x_3) in A and (x_2, x_4) in A}, which has |A|^2 elements. So |A| >= 2. L contains {(0, c, 0, n): (c, n) in A} and {(c, 0, n, 0): (c, n) in A}. If |A| = 4, each of these two sets has four elements, so both equal L; they are different sets. So |A| is 2 or 3. A is a subgroup, because {(0, c, 0, n): (c, n) in A} is the intersection of the subgroup L with a subgroup. So |A| = 2, A = {0, alpha}, and L = {x: (x_1, x_3) in A, (x_2, x_4) in A}.
Step 3. The slice at (chi_2, m_2) = alpha has G(0) = what(alpha_1, 0, 0; alpha_2, 0, 0) = what(0, 0, alpha_1; 0, 0, alpha_2) = 1, since (0, alpha_1, 0, alpha_2) is in L. The argument of (a) applies to it: it is the indicator of a set of four elements, inside A x A by Step 1, so equal to A x A. So what is the indicator of A^3. For alpha = (1, 0), (0, 1), (1, 1) this is Sigma_per, Sigma_full, Sigma_kappa.
Step 4. The inverse transform: for Sigma_per, w(e; m) = (1/8) sum_chi (-1)^{chi.e} for m = 0 and 0 otherwise, the indicator of k = 0. For Sigma_full, w = 1/8. For Sigma_kappa, w(e; m) = (1/8)(-1)^{m.e} = (1/8)(-1)^{k_34 k_12 + k_24 k_13 + k_23 k_14}. The first two are invariant. Pf(k) is the sum over the three ways to split {1,2,3,4} into two pairs of the product of the two entries; a permutation of the axes permutes these three splittings. QED

Cross-check (guide; `scripts/classify.py`, 8.6): an enumeration over all unions of orbits finds exactly these three sets.

### 8.4 Theorem S for the three sector sets, and the gap of the periodic limit. On the path of (GAP).

**Setting.** Given (TM-tw). Let w be one of the three functions of Proposition CL (b), Sigma its sector set, and

W_w(n) := sum over k of w(k) Z^k(n), for tori n with all sides at least 3.

So W_per = Z; W_full = (1/8) sum over all 64 twists of Z^k; W_kappa = (1/8) sum over all 64 twists of (-1)^{Pf(k)} Z^k.

**Lemma W.** (a) W_w is invariant under permutations of the sides. (b) For a box B, let P_{Sigma,m} be the sum of the projections P_chi with (chi; m) in Sigma, and T_B^w the direct sum over m of T_{B,m} P_{Sigma,m}, on the direct sum of eight copies of the space of the box. T_B^w is positive and trace class, and W_w(a, B) = Tr (T_B^w)^a = sum over (chi; m) in Sigma of Z_{chi,m}(a; B). (c) The largest eigenvalue of T_B^w is lambda_0(B), the top eigenvalue of the periodic box, and W_w(a, B) >= lambda_0(B)^a > 0. (d) inf over a, b of log W_w(a, b, c, d)/(ab) >= -12 beta c d.

Proof. (a) Z^{sigma k}(sigma n) = Z^k(n) by (TM-tw), and w o sigma = w. (b) Z^{e+m}(a, B) = Tr(T_{B,m}^a C^e) and C^e = sum_chi (-1)^{chi.e} P_chi, so sum_e w(e; m) C^e = sum_chi what(chi; m) P_chi = P_{Sigma,m}. P_{Sigma,m} is an orthogonal projection that commutes with T_{B,m}, so T_{B,m} P_{Sigma,m} is positive, trace class, and its a-th power is T_{B,m}^a P_{Sigma,m}. (c) (0; 0) is in Sigma and Omega is in the range of P_0, so lambda_0(B) is an eigenvalue. Every eigenvalue of T_{B,m} is at most lambda_m(B) <= lambda_0(B) by (S3). (S3) is proved in 3.1 from (S2): Z^m(a, B)^(1/a) -> lambda_m(B) (Lemma A (a)) and Z^m <= Z^0. (d) Each plaquette weight is at least exp(-2 beta), a torus has 6 |n| plaquettes and the Haar measure has mass one, so Z(n) >= exp(-12 beta |n|) and lambda_0(b, c, d) = lim Z(a, b, c, d)^(1/a) >= exp(-12 beta b c d). Use (c). QED

**Theorem S-w.** Given (TM-tw) and (S). Let w be one of the three, S_w(a; B) := W_w(a, B)/lambda_0(B)^a - 1 >= 0. Then Lemmas K, X, E, E', Theorem S and Corollary S3' of (S) hold with W_w in place of Z and S_w in place of S. In particular, if N >= 3 and s := S_w(N; (2N)^3) < 1/5041, q := 5041 s, then for every integer L >= 2N, with k >= 0 such that D := 2^(k+1) N <= L < 2D:

S_w(D/2; L^3) <= q^(2^k)/71, and every eigenvalue of T^w_{L^3} other than the simple eigenvalue lambda_0 is at most lambda_0 exp(-m_0), m_0 = log(1/q)/N.

Also 1 + S_w(n; (2n)^3) <= exp(Phi_w(n)) with Phi_w(n) := 16 log W_w(n^4) - log W_w((2n)^4) >= 0. So the seed holds if Phi_w(N) <= 1.9 x 10^(-4).

Proof. For fixed c, d >= 3 put W(a, b) := W_w(a, b, c, d) and T_b := T^w_{(b,c,d)}. By Lemma W: W is positive, W(a, b) = W(b, a), W(a, b) = Tr T_b^a with T_b positive and trace class, and ell is finite. This is the setting of the lemmas (`gap-crux-restate.md` L174), with lambda(b) = lambda_0(b, c, d). The same holds for each pair of directions. The proofs of Lemmas K, X, E, E' use nothing else. The proofs of Theorem S and Corollary S3' use these lemmas, the inequality S(k + k') <= S(k) S(k') for sums of powers of numbers in [0, 1], and, to pass from a bound on S to the gap, that the top eigenvalue is simple. Here: if S_w(t; B) < 1 for some t, then lambda_0(B) has multiplicity one in T_B^w (a second copy would add 1 to S_w), and the second eigenvalue lambda' satisfies (lambda'/lambda_0)^t <= S_w(t; B). The bounds on S_w in the recursion do not use simplicity, and each of them is below 1, so this applies at every size reached. Theorem D (b) of (S) uses Lemma A (a), (b) for the traces Tr T^n and Tr T^(2n) and the symmetry; it holds for W_w word for word. QED

**Corollary EV (three seeds, one conclusion).** Given (TM-tw), (S), (L). If for one of the three w there is N >= 3 with S_w(N; (2N)^3) < 1/5041, then (G_ev) holds along every sequence of integer sides L_i -> infinity, with n_i = D_i/2 <= L_i/2 and m_0 = log(1/(5041 s))/N. By Theorem EV-L (d) every limit point of the periodic symmetric tori clusters exponentially at rate m_0 on the functions with (i), in all four directions.

Proof. S_ev <= S_w because (0; 0) is in Sigma and all terms are non-negative; m_ev >= the gap of T^w. D_i/2 tends to infinity with L_i, S_ev(D_i/2; L_i^3) <= q^(2^k)/71 -> 0, and L_i - D_i/2 >= L_i/2. QED

**Reading (not a proof).** The three seeds say: besides the even sector, seven flux sectors are heavy at the size N. Periodic: the seven electric sectors of the periodic box. Full: the even sectors of the seven magnetically twisted boxes. Kappa: in each twisted box m the sector with electric flux m. Which of these can hold is the phase of the model. For Z_2 at large beta the periodic seed fails (proved at fixed size in `gap-seed-check.md` L191-195, given the Z_2 form of the transfer operator); I expect the full and kappa seeds to hold there (recalled gap; not proved). For SU(2), under belief 16, the full seed fails at large size and the kappa seed holds where the periodic one does.

**Order of the seeds.** S_kappa <= S_full for every box and time: Z_{m,m} <= Z_{0,m} by (S1). argued, given (TM-tw). The statement **(KP): W_kappa <= W_per**, that is, sum over chi != 0 of (Z_{chi,0} - Z_{chi,chi}) >= 0, is open. If true, the kappa seed is implied by each of the other two and is the weakest of the three. In the two-dimensional Ising model no violation was found at 900 points (8.6; guide).

### 8.5 The even sector alone: what crossing gives, and what it does not. On the path of the question (Q2).

Given (TM-tw). Box sides (b, c, d), time a, all at least 3. Write Z_{chi,m}(t; B) for the sector sums of the box B at time t.

**Proposition X16 (crossing of the even sector).** Let X be the set of the sixteen sectors (chi; m) of the box (a, c, d) with chi = (0, chi_3, chi_4) and m = (0, m_3, m_4). (The box (a, c, d) has the old time direction as its first direction; chi_3, chi_4 are the parities under the flips in the directions of the sides c, d; m_3, m_4 are the twists of the planes spanned by the first side and d, respectively the first side and c.) Then

(*) Z_{0,0}(a; (b, c, d)) = (1/4) sum over x in X of Z_x(b; (a, c, d)).

Proof. Z_{0,0}(a; (b,c,d)) = (1/8) sum over e in E_1 of Z^e(a, b, c, d) by (F1). The exchange tau of the axes 1, 2 gives Z^e(a, b, c, d) = Z^{tau e}(b, a, c, d), and tau maps E_1 onto the twists in the planes (1,2), (2,3), (2,4). For the torus (b, a, c, d) in frame 1 these are: the electric twist (1,2), and the magnetic twists m_4 = k_23, m_3 = k_24, with m_2 = k_34 = 0. So the sum is sum over m' with m'_2 = 0 of [Tr(T_{(a,c,d),m'}^b) + Tr(T_{(a,c,d),m'}^b C_2)] = 2 sum over m' of Tr(T_{(a,c,d),m'}^b (1 + C_2)/2), and (1 + C_2)/2 is the sum of the P_chi with chi_2 = 0. QED

**Corollary SR (sum rule).** On a torus with a = b: the fifteen sectors of X other than (0; 0) satisfy sum of Z_x(a; (a, c, d)) = 3 Z_{0,0}(a; (a, c, d)). So on such a torus the flux sectors of X are never all light or all heavy relative to the even sector: their total weight is exactly three times its weight.

**Proposition EVL (the loss of an even step).** Put y_x := Z_x(b; (a, c, d)) for x in X, Theta := 4 (sum_x y_x^2)/(sum_x y_x)^2, and kappa(b) := log lambda_0(b, c, d) - ell b as in Lemma K for W = Z. Then 1/4 <= Theta <= 4,

1 + S_ev(a; (2b, c, d)) <= Theta (1 + S_ev(a; (b, c, d)))^2 exp(a (2 kappa(b) - kappa(2b))), and (b - a) kappa(b) <= log(1 + S_ev(a; (b, c, d))) + log 4 for a < b.

Proof. By (*) at the sides b and 2b, and Lemma A (a) in each sector (Z_x(2b; .) = Tr((T P)^(2b)) <= Z_x(b; .)^2): Z_{0,0}(a; (2b, c, d)) <= (1/4) sum_x y_x^2 = Theta ((1/4) sum_x y_x)^2 = Theta Z_{0,0}(a; (b, c, d))^2. Divide by lambda_0(2b, c, d)^a; the terms ell a b cancel. Theta <= 4 because sum y^2 <= (sum y)^2; Theta >= 1/4 by the Schwarz inequality for sixteen terms. For the last claim: by (*), Z_{0,0}(a; (b,c,d)) >= (1/4) Z_{0,0}(b; (a,c,d)) >= (1/4) lambda_0(a, c, d)^b. Take logarithms: a kappa(b) + log(1 + S_ev(a; (b,c,d))) >= b kappa(a) - log 4 >= b kappa(b) - log 4, by Lemma K (d). QED

So crossing gives, for the even sector alone, 1 + S_ev(a; 2b) <= 64 (1 + S_ev(a; b))^4 at a = b/2 at best. This is true and useless: the constants 4 and 16 are the price of the twelve crossed sectors that the even data do not see. In the periodic proof the same two steps have Theta = 1 and no log 4.

**Proposition AS (the even trace is not symmetric; an explicit model of the class).** For the Z_2 Wilson theory (link variables +1, -1, normalised counting measure, weight exp(-beta (1 - s^k_p sigma_p))), let a < b < c and E := 4 a b c^2 (the number of links of the torus (a, b, c, c)). If 2 beta (b - a) c > E log 2 + log 7, then

(1/8) sum over e in E_1 of Z^e(b, a, c, c) > (1/8) sum over e in E_1 of Z^e(a, b, c, c).

So the function (a, b) -> Z_{0,0}(a; (b, c, c)), defined by the twist average, is not symmetric. This settles, for the class, the point that row 712 left unproved (Remark 2.A (b)). It is not shown for SU(2).

Proof. A plane twist in the plane (mu, nu) puts one twisted plaquette in each two-dimensional (mu,nu)-slice of the torus; the number of slices is N_{mu nu}, the product of the other two sides. In a slice the product of sigma_p over all plaquettes is 1 (each link is in two of them), so the product of s_p sigma_p over the slice is -1 if the slice holds one twisted plaquette: at least one plaquette of the slice has weight exp(-2 beta). Stacks of other planes hold no plaquette of this plane. So Z^k <= exp(-2 beta N_{mu nu}) for every k with k_{mu nu} = 1. From below: the configuration sigma = 1 has weight exp(-2 beta N_{mu nu}) for the twist in the plane (mu,nu) alone, so Z^{(mu nu)} >= 2^(-E) exp(-2 beta N_{mu nu}). On (a, b, c, c): N_12 = c^2, N_13 = N_14 = b c. Every e != 0 in E_1 has a plane with N >= b c, so sum over e != 0 of Z^e(a, b, c, c) <= 7 exp(-2 beta b c). On (b, a, c, c): N_13 = a c, so sum over e != 0 of Z^e(b, a, c, c) >= 2^(-E) exp(-2 beta a c). Z^0 is the same on both tori. The hypothesis gives 2^(-E) exp(-2 beta a c) > 7 exp(-2 beta b c). QED

**The statement that decides (Q2) for the even sector alone.**

**(EV-STEP).** For Wilson SU(2) at the couplings of the scaling form there are t_0 > 0 and N_0 such that S_ev(N; (2N)^3) <= t_0 for one N >= N_0 implies: S_ev(n_i; L_i^3) -> 0 and m_ev(L_i^3) >= m_0 > 0 along a sequence L_i -> infinity with n_i <= L_i/2.

With (EV-STEP), Theorem EV-L gives the gap of the periodic limit from a seed on the even sector of one periodic cube, and confinement leaves the path. I could not prove or refute (EV-STEP). What is established:

- It does not follow from crossing: Proposition CL (a), Proposition EVL. argued.
- Its two-dimensional analogue cannot have the recursion of Corollary S2: in the Ising model the even form of Lemma E fails at every coupling tried, and the even form of the doubling inequality fails at the critical coupling for n >= 12 (8.6). guide.
- No model of the class is known to me in which the even seed holds at one size and the even gap closes later. In the two-dimensional test the critical model stays just above the threshold: S_ev(n; 2n) decreases to about 0.0511 > 1/20. guide.
- It follows from: "an even seed at N forces one of the three seeds of 8.4 at a comparable size". This is a statement about the fifteen crossed weights y_x: by (SR) their sum is fixed, and a seed needs them to be concentrated on three sectors that form a group with (0; 0). In a massive phase 't Hooft's argument says that they are (recalled; not proved).

### 8.6 Runs (guides; a run can refute or guide, it proves nothing)

Scripts and outputs: `/tmp/gfx-work/scripts/` on the Mac mini (`classify.py`, `ising2d.py`, `ising_ff.py`, `ising_val.py` and their `.out` files); not in the repository. The numeric lock was held (holder gap-flux-exercise-731) and released; memory free was 53 percent before the first run. Readings R1 to R7 were written in the script headers before the runs.

**Run 1, `classify.py` (finite enumeration).** Class searched: all 2^19 unions of orbits, under the permutations of the axes 2, 3, 4, of the 64 sectors, that contain (0; 0); test: w invariant under the three transpositions (12), (23), (34). Result: exactly three sets, each with 8 sectors: periodic, full, kappa; for kappa, 8 w(k) = (-1)^{Pf(k)} for all 64 k. This agrees with Proposition CL (b) for indicator weights. It does not cover weights above 1 (the proof does).

**Run 2, `ising2d.py`.** Two-dimensional Ising model, couplings K = 0.2, 0.3, 0.38, 0.42, K_c, 0.46, 0.5, 0.6, 0.8; chains of length 3 to 12 with periodic and antiperiodic closing, symmetric transfer matrix, sectors by parity. Results against the readings:

- R1 pass. The three sets {(0,0),(1,0)}, {(0,0),(0,1)}, {(0,0),(1,1)} give W(a, b) = W(b, a) for 3 <= a, b <= 12: the largest difference of logarithms is 4.3 x 10^(-13). The even set alone is not symmetric: differences of logarithms up to 0.62.
- R2 pass. No violation of Lemma E or of the doubling inequality at n = 3 for the three sets.
- R3 pass. The two-dimensional sum rule Z_10 + Z_01 + Z_11 = Z_00 at a = b holds to 5 x 10^(-14).
- R4. **The even form of Lemma E is violated in 36 of the cases tried**, at every coupling. Example: K = 0.2, a = 3, b = 6: 1 + S_ev(3; 12) = 1.005647 against (1 + S_ev(3; 6))^4 = 1.004751. The even form of the doubling inequality is not violated at n = 3.
- R5 pass. S_kappa <= S_full at all points. Recorded: S_kappa <= S_per at all 900 points (a, b, K).
- The seeds at K = 0.2 (disordered): S_per(6; 12) = 1.8 x 10^(-3), S_full = 1.0, S_kappa = 1.8 x 10^(-3). At K = 0.8 (ordered): S_per = 1.0, S_full = 2.2 x 10^(-3), S_kappa = 2.2 x 10^(-3). So the kappa seed can hold in both phases, and each of the other two fails in one. At K_c all three are above 0.5.

**Run 3, `ising_ff.py`, with the follow-up `ising_val.py`.** The even sector of the periodic chain by the free-fermion formula (recalled: Kaufman; Schultz, Mattis, Lieb). R7's validation, as pre-registered, compared with values printed to seven digits and asked for 10^(-8); the difference was 3 x 10^(-7), so by its own reading that validation is void. Follow-up test R7b (dated 2026-11-11, reading fixed before its run): agreement with the brute-force sums in double precision to 10^(-9) at nine points; result 1.2 x 10^(-13), pass. Results at K_c:

| n | S_ev(n; 2n) | S_ev(2n; 4n) | ((1 + S_ev(n; 2n))^4 - 1)^2 | even doubling inequality |
|---|---|---|---|---|
| 6 | 0.054657 | 0.051923 | 0.056270 | holds |
| 8 | 0.052993 | 0.051567 | 0.052635 | holds |
| 12 | 0.051923 | 0.051317 | 0.050371 | **violated** |
| 24 | 0.051317 | 0.051170 | 0.049114 | violated |
| 64 | 0.051148 | 0.051128 | 0.048767 | violated |

S_ev(n; 2n) at K_c stays above 1/20 for every n tried (it decreases towards about 0.0511; the leading terms of the scaling value are q + 4 q^2 = 0.0507 with q = exp(-pi), recalled conformal data). At K = 0.43 and 0.45 the even sum falls below 1/20 at n = 8 and n = 12 and the inequality holds at all n tried.

**What the runs moved.** They did not move the wall. They support 8.3 and 8.4 in a toy, and they show that an even step, if it exists, is not the inequality of Theorem S.

**Fresh adversarial check of the negative readings.** Not available as an independent check (no subagents). A separate pass by the same session re-read the readings: the violations of the even Lemma E are violations of one inequality in one model, not a no-go for (EV-STEP); the text above says only that.

### 8.7 The three sums by surface class; (KP) in exact form. Written after 8.6, on the open statement (KP) of 8.4.

Rule 0a: (KP) is named in no other row (grep of the scope of Step 5 for "kappa", "Pfaffian": no hit outside this file).

**Definition.** For h in K = Z_2^6 put <k, h> := sum over the six planes of k_{mu nu} h_{mu nu} (mod 2), and

Y_h(n) := (1/64) sum over k in K of (-1)^{<k,h>} Z^k(n). Then Z^k = sum over h of (-1)^{<k,h>} Y_h (Fourier inversion on Z_2^6).

**Lemma GS (exact, for every model with twisted partition functions Z^k; no transfer operator is used).**

W_per = sum over h of Y_h, W_kappa = sum over h of (-1)^{Pf(h)} Y_h, W_full = 8 Y_0.

So W_per - W_kappa = 2 sum over the 28 classes h with Pf(h) = 1 of Y_h, and **(KP) is the statement that this sum is non-negative.**

Proof. The first and third lines are the definitions. For the second: W_kappa = (1/8) sum_k (-1)^{Pf(k)} sum_h (-1)^{<k,h>} Y_h, so it is enough that (1/8) sum_k (-1)^{Pf(k) + <k,h>} = (-1)^{Pf(h)}. Let (*u)_{12} = u_34, (*u)_{34} = u_12, and the same for the pairs (13, 24) and (14, 23). Then Pf(k + u) = Pf(k) + <k, *u> + Pf(u), Pf(*u) = Pf(u) and **u = u. With u = *h: Pf(k) + <k, h> = Pf(k + *h) + Pf(h) (mod 2). So sum_k (-1)^{Pf(k)+<k,h>} = (-1)^{Pf(h)} sum_k (-1)^{Pf(k)}, and sum_k (-1)^{Pf(k)} is the cube of sum over x, y in Z_2 of (-1)^{xy} = 2, that is 8. The count: Pf(h) = 0 has 36 solutions and Pf(h) = 1 has 28, because 36 - 28 = 8 and 36 + 28 = 64. QED

**Proposition KP-Z2 ((KP) holds for the Z_2 Wilson theory).** For the Z_2 theory of Proposition AS, Y_h >= 0 for every h. So W_kappa <= W_per on every torus, and also W_kappa >= -W_per.

Proof. exp(-beta (1 - s_p sigma_p)) = e^(-beta) (cosh beta + s_p sigma_p sinh beta). Expand the product over the plaquettes and average over sigma: the average of the product of sigma_p over a set S of plaquettes is 1 if every link lies in an even number of plaquettes of S (S closed), and 0 otherwise. So Z^k = e^(-beta |P|) sum over closed S of (cosh beta)^(|P| - |S|) (sinh beta)^(|S|) prod over p in S of s^k_p. The last product is (-1)^{<k, h(S)>}, where h(S)_{mu nu} is the parity of the number of plaquettes of S in the stack of the plane (mu, nu). Hence Y_h = e^(-beta |P|) sum over closed S with h(S) = h of (cosh beta)^(|P|-|S|) (sinh beta)^(|S|) >= 0. QED

**What this gives.** In every model whose class weights Y_h are non-negative, the kappa seed is implied by the periodic seed (W_kappa <= W_per gives S_kappa <= S_per) and by the full seed (C7): it is the weakest of the three. The two-dimensional analogue (classes of closed graphs by their winding parities) explains the 900 points of run 2. For SU(2) the character expansion has the same form with weights that are integrals of products of characters; I did not show that they are non-negative. For SU(2), given (TM-tw), Y_h >= 0 holds for each h whose planes share one axis (in the frame of that axis Y_h is (1/8) of a sum of sector sums), and all these h have Pf(h) = 0. **(KP) for SU(2) is open**; it is the exact statement "the classes with Pf(h) = 1 carry non-negative total weight". Reading, not proved: at the lowest order of the character expansion at small beta a class with Pf(h) = 1 is carried by two flat sheets of spin-1/2 plaquettes that meet in one site and share no link, and the weight of such a pair is positive; so I expect (KP) for SU(2) at small beta.

## Step 9. Report

Every claim carries a mark. "argued" = proved in this file by Claude Fable 5.2, not checked by another model.

### 9.1 The wall, in plain words (corrected)

We want to show that the lightest particle has a positive mass. The plan reduces this to one inequality on a box of one size with wrap-around walls, and a proved step carries the inequality to every larger box. The inequality counts all states of the box, and some of them carry a line of force that winds around the box ("flux"). Measurements inside a bounded region cannot see flux. The question was whether the flux states must be counted. The answer has two parts. For passing from large boxes to infinite space they need not be counted: only the flux-free states matter (argued). For the step from one box to all larger boxes some flux states must be counted, because the step exchanges a space direction with the time direction, and that exchange turns one kind of flux into another. There are exactly three consistent ways to choose which flux states to count (argued). No way is known that counts none.

### 9.2 What the exercise found

1. **The limit half reads the even sector only** (Theorem EV-L, 8.2; argued; inputs checked by other models). On gauge-invariant local observables the periodic torus state equals the flux-free state up to an explicit error that tends to zero, because the flux-free state clusters and a clustering state is not a mixture. So small flux-free thermal sums on all cubes, (G_ev), give the gap of the account's periodic volume-first limit on the tr(F^2) sector. No hypothesis on a flux sector enters. I did not find this in the branch's record (search scope in Step 5).
2. **The step needs a self-dual set of sectors, and there are exactly three** (Proposition CL, Theorem S-w, 8.3, 8.4; argued, given (TM-tw)). Periodic (the present form: seven electric flux sectors), full (seven magnetic sectors), kappa (seven sectors with electric flux equal to magnetic flux; the twist sum with the sign (-1)^{Pf(k)}). Each seed at one size gives (G_ev) at all sizes, and with item 1 the gap. The kappa form and the classification were not found in the branch's record. "Exactly three" is proved for weights that are invariant under all permutations of the axes and admissible in the sense of 8.3; it is a statement about the crossing step of Theorem S, not about every possible step. The flux-free sector alone is not self-dual (Proposition CL (a)); in an explicit Z_2 model its trace is not symmetric (Proposition AS; argued).
3. **A sum rule** (Corollary SR; argued, given (TM-tw)): on a torus with two equal sides, fifteen flux sectors carry exactly three times the weight of the flux-free sector. This is why a seed on the flux-free sector alone cannot be crossed.
4. **What changed since the start.** The crux was named "the gap with confinement on the whole space". It is now: (G_ev) is what (GAP) needs; a seed with seven flux sectors of one of three kinds is what the known step needs. For SU(2) I have no proof that the kappa seed is easier than the periodic one; under the belief that SU(2) confines, both are confinement statements and the full seed is false (belief).
5. **Attempts.** Proofs: 8.2, 8.3, 8.4, 8.5. Runs (guides): the three sets are symmetric in the two-dimensional Ising model, the kappa seed holds there in both phases, the even form of Lemma E fails there, and the even form of the doubling inequality fails at the critical point for n >= 12.
6. **Answer to the row.** (Q1) No: (GAP) does not need the seed on the whole space; it needs (G_ev) (argued). (Q2) A statement on tori of one physical size that gives (GAP) with a proved step exists in three forms, each with seven flux sectors; none is about the even sector alone, and for SU(2) confinement stays on the path of the step unless (EV-STEP) of 8.5 is proved (open) or the kappa seed is reached by a tool that does not need heavy electric flux (not known).

### 9.3 Filters corrected

- **W1** (row 712 Remark 2.A (d), row 708 Remark Y): "a seed for the centre-even sector cannot be obtained by symmetrizing over twists". Too strong. Valid form: the sum over all twists with equal weights has no seed where magnetic flux is light (belief for SU(2)). The sum with the sign (-1)^{Pf(k)} is symmetric and holds no purely magnetic sector. What comes back: Theorem S for W_kappa. Range: where the sectors with equal electric and magnetic flux are heavy.
- **W2** (row 712, a3): "no finite criterion is known for a gap of local observables in a gauge theory" beside (DS-tw). Corrected: Corollary EV gives three, and two of them do not need a gap on the whole space.
- **The Z_2 test** (`gap-crux-restate.md` L227; `gap-crux-fp.md` L280-281; `gap-skeleton-final.md` L562). Valid for the periodic seed. For (G_ev) and (GAP), Z_2 at large beta is a model where the target holds (recalled), so it refutes no tool for them. It binds such a tool only at the Z_2 transition point, and above it only if the tool's hypothesis is monotone in beta.
- Not corrected: the U(1) test, and the 22 + 14 verdicts of rows 712 and 720 apart from the above ("as reported; not re-derived").

### 9.4 Routes worth doing (at most three)

1. **Restate the consumer.** Believe: nothing. Cost: one check (work item 1) and a short edit by the lead. First test: the check of 8.2. Change: `gap-seed-limit.md` Theorem L and the skeleton's crux read (G_ev); the flux half ((TUBE'), (MF), (VORT), Route T) is off the path of the limit.
2. **Price the three seeds against data.** Believe: published lattice numbers on twist free energies at sizes of some tens of correlation lengths exist. Cost: one reading lane. First test: is the electric (or dyonic) flux weight at the seed size below the even thermal sum? Change: whether the choice of seed matters for the size of the seed box (belief e2).
3. **(KP) for SU(2): W_kappa <= W_per.** Believe: that the surface classes with Pf(h) = 1 carry non-negative total weight (8.7). It is proved for Z_2 (Proposition KP-Z2; argued). Cost: one short author run. First test: the sign of the class weights in the character expansion at second order in beta on a small torus. Change: if true, the kappa seed is implied by the periodic seed and by the full seed; it is then the weakest of the three and the natural form of the crux.

### 9.5 What not to do next

- No author run on the full seed for SU(2): under belief 16 it is false at large size.
- No author run on (EV-STEP) now: no mechanism is in sight, crossing is excluded (8.5), and the two-dimensional test shows the known inequality fails.
- No further work on the flux half as a prerequisite of the limit: 8.2 removes it there.
- Do not use Z_2 at large beta as a model where the target fails.

### 9.6 The exact price

For the even sector alone the wall is equivalent to nothing I can prove. The exact open statement is **(EV-STEP)** (8.5). The exact proved alternative is: **one of the three seeds** S_w(N; (2N)^3) < 1/5041, w in {periodic, full, kappa}, at one physical size, uniformly in the cutoff; in free-energy form 16 log W_w(N^4) - log W_w((2N)^4) <= 1.9 x 10^(-4).

### 9.7 Work items

**Item 1 (first): check of this file.** A model that did not write it (Claude Opus 5.5 high, or Codex gpt-6-astra) reads `library/gap-flux-exercise.md` Steps 3, 5, 8 line by line. Statements, in order: Lemma CB, Lemma MX, Lemma L1-ev, Theorem EV-L (c), (d); Lemma CL1, Proposition CL (a), (b); Lemma W, Theorem S-w, Corollary EV; Proposition X16, Corollary SR, Proposition EVL, Proposition AS; (S1), (S2), (S3) of 3.1. Read with them: `gap-transfer.md` Section 8 and 9.3; `gap-seed-limit.md` Sections 1 to 4; `gap-crux-restate.md` L174-219; `gap-seed-check.md` L30-40, L177; `gap-crux-fp-check.md` L30-38. Points to test first: (1) Lemma CB, the gauge transformation on a slab with time-like links, and the choice of r; (2) Lemma MX (b), positivity with C^e and independence of the slab; (3) the count of d and d' in Theorem EV-L (c); (4) Proposition CL (b), Steps 2 and 3; (5) (TM-tw) for twists with Pf(k) = 1, where an electric and a magnetic stack meet; (6) Theorem S-w where the top eigenvalue could be degenerate; (7) the three "new" marks of Step 5, by a search of its own that includes origin/main and the other pull-request branches. Verdict per statement: HOLDS, HOLDS AFTER CORRECTION, FAILS. Output: `library/gap-flux-exercise-check.md`. Stop at the first statement that breaks Theorem EV-L, and report it.

**Item 2: (TM-tw) as a lemma of its own.** Write `library/gap-transfer-twisted.md`: for every box with sides at least 3 and every k in Z_2^6, the operator T_{B,m}, its positivity, trace class, simple top eigenvalue, commutation with the flips, Tr(T_{B,m}^a C^e) = Z^{e+m}, and Z^{sigma k}(sigma n) = Z^k(n), each step written from `gap-transfer.md` Sections 1 to 4 and 9.3 (not "word for word"). Sources: `gap-seed-check.md` L30-40, L177; `gap-crux-fp-check.md` L30-38. Then one check. Reason: 8.4 and 8.5 rest on it, and today it lives in two check files.

**Item 3: reading lane on twist free energies.** Read the published lattice results on twisted partition functions and electric flux free energies of SU(2) in four dimensions (de Forcrand and von Smekal; Kovacs and Tomboulis; later work), open copies only. Question: at a torus of L/xi between 10 and 40, what are Z^k/Z for one-plane twists and for the two-plane twist with Pf = 1, and what do they give for S_per - S_ev and S_kappa - S_ev at time L/2? Mark every number GUIDE. Output: `library/prior/gap-twist-data.md`. Stop if no source gives a size above 5 correlation lengths.

**Item 4: (KP) for SU(2).** Prove or refute: for Wilson SU(2) on every torus with sides at least 3, the sum of Y_h over the 28 classes h with Pf(h) = 1 is non-negative (Lemma GS, 8.7; Y_h = (1/64) sum_k (-1)^{<k,h>} Z^k). Proved here for Z_2 (Proposition KP-Z2). Points to test first: the character expansion of the SU(2) weight (are the class weights sums of non-negative terms?); the Z_2 splitting of Mack and Petkova (`gap-crux-restate.md` L290-294), where the Z_2 couplings beta J_p(V) can be negative; a small torus by hand at small beta (second order in beta is enough to see a sign). Stop after three distinct ways. Output: `library/gap-kappa-order.md`.

**Not proposed:** an author run on (EV-STEP) (no mechanism); the full seed for SU(2) (believed false); an attack on (DS-tw) (row 691 owns it); the extension to SU(N) (the sector sets must be classified again for Z_N; not needed for T0, SU(2) first); edits of `gap-skeleton-final.md`, `t0-tree.md` or the registry (the lead's files).

### 9.8 Appendix

The tables are in Steps 2 (inventory), 4 (assumptions), 5 (compare), 6 (methods and tests), 7 (routes, kill pass, rank, registry), 8.6 (runs).

- **Assumptions most likely to be wrong:** e2 (flux is far heavier than the lightest even state at the seed size); the reading that the kappa seed is "confinement again" (C8, a belief).
- **Assumptions most expensive to be wrong:** (TM-tw), because 8.3 to 8.5 rest on it; item 16 (confinement), because every seed for SU(2) rests on it in one form.
- **Literature proofs worth translating:** 't Hooft's duality argument for flux free energies in a massive phase (it would turn "the light crossed sectors form a group of four" from a recalled reading into a statement with hypotheses); the Peierls or duality proof of the gap of Z_2 gauge theory at large beta (it would turn the corrected Z_2 test from recalled to proved).

## Measure of the skill (row 721, Section 4.6)

- **Discard tests or verdicts corrected: 3.** W1 (too strong), W2 (corrected), the Z_2 test (valid for the periodic seed only). All three are on the path of the choice of the seed. 34 other verdicts were listed and left "as reported".
- **Statements of this run and their status.** argued, not checked: Lemma CB, Lemma MX, Lemma L1-ev, Theorem EV-L, Lemma CL1, Proposition CL, Lemma W, Theorem S-w, Corollary EV, Proposition X16, Corollary SR, Proposition EVL, Proposition AS, (S1) to (S3), Lemma GS, Proposition KP-Z2 (18 items; (S1) to (S3) and those of 8.4 and 8.5 except Proposition AS are "argued, given (TM-tw)"; 8.2, 8.3, Proposition AS and 8.7 do not use (TM-tw)). open: (EV-STEP); (KP) for SU(2). belief: C8. guide: the three runs. A check has not been made, so the counts "right / right after correction / wrong" are not known.
- **"New" marks and their support (4).** Theorem EV-L (c), (d); the kappa set with its Theorem S; the classification (exactly three, none the even sector alone); S_kappa <= S_full. Search: grep of all `library/gap-*.md`, `library/prior/gap-*.md`, `exercise-skill-v2.md`, `l17c.md`, `gates/`, `parts/` and FINISH rows 697 to 730, with the wordings listed in Step 5; every hit read. Not searched: origin/main and the other pull-request branches (not in this checkout). So the marks mean "new in this branch's record".
- **The compare step found by its own search:** (SEED-phys) of row 700 (open list), Identity FL of row 708, Remark 2.A of row 712, Remark Y of row 708, run 2's zero-flux function and Corollary 5, (DS-tw) of row 691, and the (TM-tw) re-derivation in the check of row 716.
- **Cost.** About 11 dollars on this session's budget meter and about 45 minutes of wall time to the end of step 8; one session, no subagents; three small numeric runs under the lock.
- **Did the pre-registration rule bind?** Once: R7's validation failed its own tolerance for a trivial reason (printed digits); a dated follow-up R7b was added and the original reading was not changed.
- **Should a next long run change?** Yes. (1) Before any further author run on the seed or on the flux half, run work item 1; if Theorem EV-L holds, brief every later run with (G_ev) as the consumer and with the three seeds. (2) A long run on (TUBE'), (MF) or Route T as a prerequisite of (GAP) is no longer justified by the limit half. (3) The step-5 search should be given the other branches; this run could not search them.

**Did the exercise succeed, by the skill's own list?** A corrected filter: yes (three, argued, not checked). A route with its first test run: yes (routes A and B, proofs written; runs as guides). An exact price for the even-only form: only a named open statement, (EV-STEP); no equivalence is proved. The wall is not solved: no seed is proved for SU(2) at any coupling of order one, and no mass gap is proved.

**Credits.** Sussman and Alpoge, with Claude and Codex (the account; the notions of volume-first limit and canonical component; no statement of theirs is used in a proof here). Balaban (the ultraviolet basis of the account). Osterwalder and Seiler, Luscher (transfer operator, through rows 667, 671). 't Hooft (twists, electric and magnetic flux, duality). Aharony, Seiberg and Tachikawa (the three global forms). Kaufman; Schultz, Mattis and Lieb; Onsager (the Ising spectrum, in a guide run). Mack and Petkova (the Z_2 splitting, named in a work item). Rows 667 to 720 of this lane: the authors and checkers named in Step 5.

RESULT: argued, not checked by another model: (1) Theorem EV-L: on centre-blind local observables the periodic torus state equals the flux-free (centre-even) state up to an explicit error, so small even-sector thermal sums on all cubes, (G_ev), give exponential clustering of every periodic volume-first limit in four directions; (GAP) does not need the flux sectors in its limit half. (2) Proposition CL and Theorem S-w (given the twisted transfer operator of rows 698, 716): the crossing step works for exactly three sector sets, periodic (the present seed), full, and kappa (twist sum with sign (-1)^{Pf(k)}, new in this branch); each seed at one size gives (G_ev) and the gap; none is the even sector alone; S_kappa <= S_full; W_kappa <= W_per for Z_2 (Lemma GS, Proposition KP-Z2). (3) Sum rule, loss identity, and an explicit Z_2 model where the even trace is not symmetric. Corrected: three filters (Remark 2.A (d) and Remark Y too strong; row 712 a3; the Z_2 test valid for the periodic seed only). Open: (EV-STEP), a step for the even sector alone, neither proved nor refuted (guide: the even form of the known inequality fails in the two-dimensional Ising model); (KP) for SU(2); every seed at a coupling of order one; so for SU(2) confinement stays on the path of the step, as a belief about which seed can hold, and no mass gap is proved.

