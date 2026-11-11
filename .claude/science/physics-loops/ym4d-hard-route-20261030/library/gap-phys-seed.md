lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-12T01:39Z

# gap-phys-seed: the continuum form of the seed, (PHYS-SEED), and the flow across scales

Row 720 of `FINISH.md`. Author run of Claude Fable 5.2 (model id claude-fable-5-2, max effort), Mac mini worker, one session, no subagents, pinned at commit 2a9dddb50. Started 2026-11-11T13:39Z. Research-stage working state. **No mass gap is claimed or proved here.** Nothing in this file is checked by another model.

**State of this file: IN PROGRESS.** The file is written part by part. The status block says where the run stands.

**Marks.** PROVED = proved by hand in this file from the named inputs, not checked. PROVED GIVEN = proved from a named input; the check state of the input is written. RECALLED = a known fact from memory or from a source named at the place, used in no proof. GUIDE = a belief from physics or numerics, used in no proof. OPEN = not proved.

## Status block (updated after each part)

- Section 0 (repo search, reading state, credits): done.
- Part 1 (what each end gives): done (Section 1). Result: the account controls log Z of its own tori up to an additive term C l^4 with l above a floor, at one time extent; this gives no bound for S near the threshold. On a small physical torus S is large (RECALLED physics), so no small torus can hold the seed. The large end needs a cube of at least 12.9 of its own correlation lengths.
- Part 2 (the flow; candidates and tests): not started.
- Part 3 (real attempts): not started.
- Part 4 (what must be extended): not started.

## 0. Repo search, reading state, credits

**Repo search (rule 0a and the repo-first rule), done before any derivation.** Searched `library/*.md`, `library/prior/*.md`, `parts/*.md`, `library/open-core.md` and FINISH rows 660 to 720 for: PHYS-SEED, step scaling, Schrodinger functional, Koller, van Baal, small volume, zero mode, toron, torus floor, twisted torus, twist eater, Creutz ratio, gradient flow, Casimir, monotone. `library/open-core.md` has no entry on the gap, the seed, a flux ratio or a finite-volume quantity. Matches that bind this file:

| Earlier work | Where | What it already holds |
|---|---|---|
| (PHYS-SEED), Corollary C | row 712, `gap-crux-fp.md` 4.3 | the statement of this row; P1 (14.8 correlation lengths); P2 (the seed contains the twist criterion) |
| The seed in scaling form | row 697, `gap-crux-restate.md` Section 5, verdict item 4 | "at one physical size the doubling defect is below 1.9 x 10^(-4), uniformly in the cutoff" |
| Step scaling as a heuristic | run 2, `gap-skeleton-max-b.md` A5 with crux (STEP); high draft `gap-skeleton.md` B6 | "strict monotonicity is not enough; u can converge to a finite limit below u_*"; K6: a slab has a fixed point at 1/T_c |
| Excess free energy of symmetric tori | run 2, A1 with crux (FE); Proposition 3 (a count of states from (ST5) and (V-ext)) | Delta(l) = kappa log(1/g(l)) + O(1) at small l (heuristic there) |
| Casimir free energy step | row 708, `gap-mid-max.md` C-B, (CAS), Proposition Delta | verdict: (CAS) restates the seed in steps |
| Transport in the coupling | row 708 C-A, (VIR_K), Theorem TR; row 710 Theorem U | open; a mixing statement |
| Flux half | row 697 Theorem F and (TUBE'); row 708 C-C, Identity FL, (MF); run 2 A6 (VORT); row 712 Identity L, Proposition TW | open at a coupling of order one |
| Thin torus with a twist | Route T: rows 678, 679, 684, 691; crux (AC') | open; (CH) proved and checked |
| Dilation identity | run 2, A10 with crux (SHIFT) | "the constant of integration is the whole question" |
| Literature: step scaling | `prior/gap-vir-lit.md` Section 6; `prior/gap-fullread-1.md` (Luscher, Narayanan, Weisz, Wolff read in full); `prior/gap-seed-lit.md` S4 | no rigorous inequality between two box sizes was found |

By rule 0a this file does not attack (CAS), (VIR_K), (VIR-log), (TUBE'), (MF), (VORT), (AC'), (W), (DS-tw), (BOOT_eps), (NOCRIT), (vMF-Lip) or (AS-bg). Where a candidate of Part 2 reduces to one of them, the match is named and the candidate stops there.

**Read in full for this file.** FINISH.md header, rules and row 720; GOAL.md; `gap-crux-fp.md` Sections 1, 3b, 4.1, 4.3, 5; `gap-crux-restate.md` Sections 0 to 3.2, 3.4, 5; `gap-seed-shape.md` lead note and Sections 1.1 to 1.6; `gap-skeleton-final.md` Sections 1 to 5 and 13.10 to 13.14; `prior/gap-seed-size.md` whole; `gap-mid-max.md` Section 2 and the statements of Proposition Delta, Theorem CRIT, Identity FL; `gap-skeleton-max-b.md` Parts 0, 1.1 to 1.3 (A1 to A10); `sa-index/README.md`; `assembly-status.md` Section 1.1.

**Sources fetched by URL into /tmp/gap-phys-seed-scratch (not kept in the repository).**
- The outline of Sussman and Alpoge, `YM4_sketch_500.tex`, commit 31a47c543775 (32,992 lines). Read: lines 46-222 (main theorem and plan), 4086-4250 (packages D and E), 6836-7038 (objects, Theorem 0 clause by clause, Theorem 0'), 8733-8775 and 9536-9582 (flat holonomies, finite tori), 21454-21534 (statement 3.4, the torus floor), 22249-22345 (vacuum constants), 23767-23833 (the torus hypothesis (ST5), (ST6)). Cited below as SA L<line>.
- The complete account, parts I and II, same commit. Read: CA-I 4209-4262 (Balaban's ultraviolet stability theorem as cited there), CA-I 157028-157075 (integrated stability), CA-II 140995-141030 (trace sub-additivity), CA-II 141276-141392 (torus-independence of the vacuum-energy density). Statements only; no proof was read.
- P. van Baal, "QCD in a finite volume", arXiv:hep-ph/0008206 (79 pages). Read: pages 1-2, 10-12 (the effective Hamiltonian of the constant modes, the flux energy), 31-34 (twisted boundary conditions, Table 1). Used for RECALLED numbers only.

**Not covered by this run** is listed at the end of the file.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the account and the outline (the ultraviolet end; every statement quoted in Section 1.1). Tadeusz Balaban: the block renormalization method and the ultraviolet stability theorem that the account builds on (CMP 95 to 122). M. Luscher; M. Luscher and G. Munster; J. Koller and P. van Baal; P. van Baal: the small-volume spectrum (RECALLED, through van Baal's review). G. 't Hooft: twists and flux sectors. Earlier rows of this target: Claude Fable 5.2 (rows 669, 670, 697, 705, 708, 712: Lemmas A, K, X, E, Theorem S, Theorem SH, Proposition Delta, Identity FL, Corollary C, Propositions T1 to T3, V); Codex gpt-6-astra (row 699: Lemma E', Corollary S3'); Claude Opus 5.5 (checks). Osterwalder and Seiler, Luscher: the transfer operator (through rows 667, 671).

## 1. Part 1: what each end gives

Notation as in `gap-crux-restate.md` Section 1 and `gap-seed-shape.md` 1.1. Torus with sides n = (n_1, ..., n_4); Z(n), F = log Z; f = inf F(n)/abs(n); Delta(n) = F(n) - f abs(n) >= 0. Box B, transfer operator T_B, eigenvalues lambda_0 > lambda_1 >= ..., m(B) = log(lambda_0/lambda_1), S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k, g(k; B) = log(1 + S(k; B)). t(r) is the threshold of Theorem SH at the shape r = b/a: t(2) = 1/1650, t(3) = 1/100, t(4) = 1/25, t(6) = 1/10.

### 1.1 The small end: what the account controls on a torus

Everything in 1.1.1 to 1.1.3 is a quotation or a restatement of the text of Sussman and Alpoge (with Claude and Codex). Their text states these as conditional on its packages; the T0 chain of this target is the work of closing them. I read the statements, not the proofs.

**1.1.1 The tori of the account (RECALLED from the source; lines read in this run).**

- Lattice and unit. Wilson SU(2), torus T_l with all four sides equal to l, spacing a_K = L^(-K), L odd and large (SA L6844). The unit of length is the scale at which the running inverse coupling x_k first enters the window g^(-2) <= x <= g^(-2) + B_sharp; a pair (K, beta) with this property is a first-passage datum (SA L6854-6861). So the running coupling at distance 1 is about g, and g is small.
- Allowed sides. l = 2 L^m (SA L6913), and above a floor: "it suffices that l >= l_*(g) := 2 L^11 M R(g^(-2) + B_sharp)"; "Write L(g) for the compatible torus sides above this floor ... The side is selected after g; the cutoff K remains unrestricted" (SA L21521-21532, (RF35)). The complete account uses the same floor, L^(m_T(g')) = L^11 M R(g') (CA-II L141279-141281).
- Why the floor is there: "Wrapping domains have d_j(X) >= c l L^(K-j)/M. Their exponential decay is used directly and does not define an additional renormalized coefficient" (SA L21518-21520). So the construction treats the torus as large against the localization cubes at every one of its K steps. It ends at the unit lattice, which has l >= l_*(g) sites on a side. No step of the account integrates the scales between 1 and l.
- The same torus in other units. By the exact dilation identity (SA L6863-6869), a datum beyond first passage is a first-passage datum on a dilated torus. So "a torus where the coupling is small" means, for the account: a torus whose side is at least l_*(g') times the length at which the running coupling is g', for one g' below the ceilings of Theorem 0. The account defines no running coupling at the scale of the torus side itself.

**1.1.2 The partition function (RECALLED from the source).** The torus hypothesis, which is Obligation D1 ("We must prove the precise torus conditions (ST5)-(ST6)", SA L4088-4098), reads at zero source (SA L23778-23787):

Z_(a,l)(0) >= exp(V_(a,l) - C_- l^4), and abs(Z_(a,l)(W)) <= exp[V_(a,l) + Re U(W) + Re sum over s, D of e_(a,l,s,D)(W) + C_+ l^4],

"uniformly over the selected cutoff-coupling data (a, beta) and allowed tori", with "the source-independent vacuum number V_(a,l)" real. At W = 0 the local terms vanish. So

(UV-Z) V_(a,l) - C_- l^4 <= log Z_(a,l) <= V_(a,l) + C_+ l^4.

In the complete account the same content is Balaban's ultraviolet stability theorem, cited as CMP 122b Theorem 1 with the hypothesis that all effective couplings lie in (0, gamma] (CA-I 4209-4240), and the integrated stability theorem with the bound abs(E_k(U_k)) + abs(R_k(U_k)) <= C_E N_k, N_k the number of sites of the level-k lattice (CA-I 157028-157036). The vacuum number is not given to this precision: the outline's explicit requirement is abs(E_(K,l,beta) + (3/2)(N^2 - 1)(L^4 - 1) sum over j < K of (log x_j) N_(j+1)) <= C N_0, with N_0 the number of fine sites (SA (RF62), L22292-22298). Its density is independent of the torus up to a small constant: abs(E_m/(2 L^m)^4 - E_(m')/(2 L^(m'))^4) <= delta_vac-bar, a number that depends on L and the constants only (CA-II 141374-141386; declared proved there under its hypotheses (a) to (c)).

**1.1.3 Correlations (RECALLED from the source).** Theorem 0 (c) (SA L6937-6960): for Lipschitz tests with supports at pairwise distance at least d, (1) abs(S^T_n) <= C_n(d) exp(n c_V l^4) times the product of the norms, on every allowed torus; (2) a bound with no volume factor when l >= C n (R + 1); (3) for bumps of size and separation of order d <= d_0 < 1: the two-point function is zeta_K(d)^2 (3 (N^2 - 1)/pi^4) g(d)^4 K_free(f, h) (1 + eps), with abs((11 N^2/(12 pi^2)) g(d)^2 log(1/d) - 1) <= eta-bar(d). Clause (d) (SA L6972-6977): "On each torus, the renormalised coupling by itself determines the limit theory."

**1.1.4 The packages behind each statement (the outline's catalogue, SA L3757-4650; packages D and E read in full, the others by their titles).** A: background fields and propagators. B: cluster expansion and power counting. C: large-field histories and the closed induction. D: sources and local correlation bounds (D1 the torus conditions and the partition floor; D2 graded all-state bounds; D3 rarity; D4 one-point transfer). E: flow, tuning and comparison of cutoffs (E1 a consistent flow; E2 tuning; E3 matched cutoffs; E4 calibrations). F: short-distance normalization and nontriviality. G: symmetries, rotations and phases. H: test spaces and reconstruction. (UV-Z) is D1, which rests on A, B, C and E1. The bounds (c)(1) and (c)(2) are D1 with D2 and G1. The law (c)(3) is F. Clause (d) is E2 to E4. Packages G and H concern R^4 and are not used for a statement on one torus.

**1.1.5 The same control as a statement on the transfer operator (PROVED GIVEN (UV-Z) and (TM); (TM) is checked, rows 671, 698, 699).** Let B be the cube with l/a sites on a side and n = l/a. By (TM), Z_(a,l) = Tr T_B^n. So (UV-Z) is a two-sided bound on one number, Tr T_B^n, at the one time extent n equal to the side:

V - C_- l^4 <= log Tr T_B^(l/a) <= V + C_+ l^4.

It contains no statement on a second time extent, so none on lambda_0(B) or lambda_1(B) alone. Three consequences can be drawn with the lemmas of this target.

(i) Upper side, other shapes. By Lemma A (a), F(n)/abs(n) does not increase in each side. So for every torus n' whose sides are multiples of l/a: F(n') <= (abs(n')/n^4) (V + C_+ l^4).

(ii) Lower side. F(n') >= f abs(n') for every torus, by (LB).

(iii) A count of states (run 2, Proposition 3; restated). Let v := V_(a,l)/l^4, and assume that the densities v at the allowed sides l' >= l differ by at most delta (the statement of CA-II quoted in 1.1.2, with delta = delta_vac-bar). Then f >= v - delta - C_- (let l' grow in the lower bound of (UV-Z)), so Delta(n^4) = F(n^4) - f n^4 <= (C_+ + C_- + delta) l^4, and by Proposition Delta (checked, row 709), for every integer b >= n: g(n; b^3) <= (b/n)^3 (C_+ + C_- + delta) l^4.

**Proposition 1.1 (the account gives no bound for S near the threshold; PROVED as a statement about the size of the error terms).** The only bound for a thermal sum that follows from (UV-Z) by the lemmas above is S(n; b^3) <= exp((b/n)^3 C l^4) - 1 with C = C_+ + C_- + delta and l >= l_*(g). The seed needs g(n; b^3) <= log(1 + t(r)) <= log(1.1) < 0.1. So the control of the account is short of the seed by the factor C l^4/0.1 at least, with l^4 >= 16 L^44. No choice of the constants repairs this: C_+ and C_- are bounds on the logarithm of the unit-scale integral per unit cell, and they are of order one by their construction (the bound C_E N_k of CA-I 157033). QED

In words: the account controls the free energy of the torus to an error of order one for each unit cell. The seed is a statement about the free energy of the torus to an absolute error of 6 x 10^(-4). On the tori of the account the two are apart by the number of unit cells, at least 16 L^44.

### 1.2 The small end: what is true there (RECALLED physics; no proof step uses it)

The account stops at the unit lattice. What the torus does at its own scale is the subject of the small-volume expansion. I quote van Baal's review (arXiv:hep-ph/0008206; pages read in this run).

- Periodic boundary conditions, zero electric flux. The low levels are those of the Hamiltonian of the nine constant modes; their energies are of order g^(2/3)(L)/L. "The constant eps_1 = 4.116719735 determines to lowest order the mass of the scalar glueball, m_0 = L^(-1) eps_1 g^(2/3)(L), which was already computed by Luscher and Munster" (page 11).
- Periodic boundary conditions, electric flux. The eight flux sectors are degenerate to all orders of perturbation theory. The splitting is a tunnelling effect: "Delta E = 2 L^(-1) lambda B^2 g^(5/3)(L) exp[-S/g(L) + eps_1 T/g^(2/3)(L)] {1 + f(g(L))}", with "S = 12.4637", "T = 3.9186", lambda = 0.6997, B = 0.206, f(g) = O(g) (page 11, formula (12)).
- "The influence of the boundary conditions on the low-lying glueball states is felt as soon as z = m_0 L > 0.9" (page 12).
- Twisted boundary conditions m = (1, 1, 1). There are no constant modes. "z_r = m_r L = 2 sqrt(2) pi + g^2(L) gamma_r/(16 pi^2), z_(e_n) = E_(e_n) L = sqrt(2) pi + g^2(L) gamma_(e_n)/(16 pi^2) (n not 3)", with gamma = -92.08 for the lowest scalar (formula (44) and Table 1, page 33). "z_0 is here a decreasing function of the volume, which has to turn around at some point, when the mass stabilizes and z_0 becomes linear in L" (page 33). The flux e = (1, 1, 1) has an energy that "is entirely due to instanton effects", of order exp(-4 pi^2/g^2) (page 32).

**What this says about S (GUIDE).** Take the seed shape, time L/2 and box L^3, and let g(L) tend to 0.

1. Periodic box. The seven excited flux sectors have ground states within exp(-12.46/g(L)) of the vacuum, so they add 7 (1 - o(1)) to S. Each level of the constant-mode Hamiltonian with eps_i g^(2/3) <= 1 adds about 1, in each of the eight sectors, and the number of such levels grows without bound as g(L) falls. So S(L/2; L^3) tends to infinity as L tends to 0, like a power of 1/g(L). The quantity log(1 + S), and the Casimir free energy Delta(L^4), grow like a multiple of log(1/g(L)), which is a multiple of log log(1/(L Lambda)). (Run 2 has Delta = kappa log(1/g) + O(1). My count on a fixed lattice at large beta gives kappa = 3: the twelve constant modes scale like beta^(-1/4) and not like beta^(-1/2). This count is not a proof.)
2. Twisted box m = (1, 1, 1). The zero-flux gap starts at z = 2 sqrt(2) pi, about 8.9, and falls at first. One flux sector, e = (1, 1, 1), is degenerate with the vacuum up to exp(-4 pi^2/g^2). So the thermal sum of the twisted box is at least 1 - o(1).
3. In both cases the lowest gap of the whole space of the box, in units of 1/L, starts at zero: z_full(L) = L m(L^3) is of order g^(5/3) exp(-12.46/g(L)) for the periodic box.

**A proved fragment (PROVED GIVEN (TM-c), checked rows 698, 699).** P2 of row 712 says 0 <= 1 - Z^(1 nu)/Z <= 2 S/(1 + S). Solved for S: S(n_1; B) >= (1 - zeta)/(1 + zeta), with zeta = Z^(1 nu)(n)/Z(n). So every upper bound zeta <= zeta_0 < 1 on a twist ratio is a lower bound on the thermal sum, and the seed at the threshold t forces zeta >= (1 - t)/(1 + t). A proof that the seed fails on small physical tori would be a proof that zeta stays away from 1 there, uniformly in the spacing. That is a weak-coupling statement about the torus at its own scale. It is not in the account (1.1.1), and I did not prove it.

### 1.3 The large end: what the seed requires

**P1 for every shape (PROVED; the proof is P1 of row 712 with the thresholds of Theorem SH, checked row 707).** If S(a; b^3) <= t(r), r = b/a, then a m(b^3) >= log(1/t(r)), so the side of the cube is at least r log(1/t(r)) correlation lengths of the cube itself:

| r = b/a | threshold t(r) | time side a m >= | space side b m >= |
|---|---|---|---|
| 2 | 1/1650 | 7.41 | 14.8 |
| 3 | 1/100 | 4.61 | 13.8 |
| 4 | 1/25 | 3.22 | 12.9 |
| 6 | 1/10 | 2.30 | 13.8 |
| >= 24 | 3/10 | 1.20 | 28.9 |

(log 1650 = 7.409, log 100 = 4.605, log 25 = 3.219, log 10 = 2.303, log(10/3) = 1.204.) So with the present thresholds no cube of side below 12.9 of its own correlation lengths can carry a seed. With the multiplicities of the levels the published masses give about 20 to 24 correlation lengths of the lightest glueball at r = 2 (GUIDE: `prior/gap-seed-size.md`; `gap-seed-shape.md` Section 5).

**The flux half at the large end (PROVED GIVEN (TM-c)).** By P2, the seed at the threshold t forces every twist ratio in a plane that contains the time direction to satisfy Z^(1 nu)/Z >= 1 - 2 t/(1 + t).

**A form of (PHYS-SEED) on symmetric tori only (PROVED GIVEN Proposition Delta, checked row 709, and Theorem SH, checked row 707).** The seed torus (N, 2N, 2N, 2N) is not a torus of the account, whose tori have four equal sides. Proposition Delta gives a form in that family: if along the sequence

(PHYS-SEED-Delta) limsup over j of Delta(n_j^4; beta_j) <= 6.1 x 10^(-4), with n_j a_j = l_1 fixed,

then for all large j, S(n_j; (4 n_j)^3) <= exp(64 x 6.1 x 10^(-4)) - 1 < 0.0399 < 1/25, and by Theorem SH (line r = 4, K = 22.2) every cube of side at least 4 n_j has m >= log(1/(22.2 x 0.0399))/n_j >= 0.12/n_j. In physical units the gap is at least 0.12/l_1, uniformly in j. Delta contains f, the free energy density of the infinite lattice at the same spacing; by Delta(n^4) = sum over k >= 0 of 16^(-(k+1)) Phi(2^k n) it is a sum of doubling defects of symmetric tori.

### 1.4 The distance between the two ends (GUIDE)

Lengths in units of the correlation length xi of the lightest glueball. From the numbers of 1.2 and of `prior/gap-seed-size.md` (sqrt(sigma) xi about 0.28, xi about 0.12 fm with sqrt(sigma) = 440 MeV):

| Regime | Box side L | What holds there |
|---|---|---|
| Perturbative constant modes | z = L m_0(L) below about 0.9; L below about 0.2 fm | the small-volume expansion; S is large |
| Constant modes with boundary conditions in field space (Koller and van Baal) | L up to about 5 to 6 xi, about 0.7 fm | a truncated Hamiltonian, compared with Monte Carlo data; not a controlled expansion; S is of order one (three flux states at L E_e of about 1.4 alone give about 1.5 at time L/2) |
| The seed | L of about 20 xi, about 2.5 fm | S(L/2; L^3) < 1/1650 |

So in physical units the distance from the largest box with a semi-analytic description to the seed box is a factor of about 4, two doublings. The distance from a box in which the coupling at the box scale is small (alpha below 0.1; L below about 0.05 fm) is a factor of about 50, between five and six doublings. On the whole way S falls from infinity to 6 x 10^(-4). The step of Theorem S, s -> 5041 s^2 or the map phi of Theorem SH, contracts only below the threshold. Above it the lemmas allow growth, and the class contains models where S does not fall (the ceiling models of `gap-seed-shape.md` Section 4).

**Summary of Part 1.** (a) The account controls, on tori of four equal sides above the floor l_*(g) and under its packages A to F: the logarithm of the partition function up to C l^4 at the one time extent equal to the side; connected correlations of the action density on separated supports; the two-point law at distances below the unit. It gives no value and no useful bound for S. The true S on a small torus is large. (b) The seed needs a cube of at least 12.9 of its own correlation lengths (14.8 at the shape of Theorem S) and twist ratios above 1 - 2t/(1 + t). Between the two ends S must fall from a power of 1/g(L) to 6 x 10^(-4), over five to six doublings of the physical size.

## 2. Part 2: the flow. Candidates, step inequalities, tests

### 2.1 What a flow candidate is, and what a test can show

Along the trajectory (a_j, beta_j) write Q_j(L) for a lattice quantity on the torus of physical side L (n_j a_j = L), and Q(L) for its limit, or its upper or lower limit, as j grows. A flow candidate is a quantity Q with three statements.

- (BASE_Q) At one small size L_0, where the coupling is small, Q(L_0) lies in a known set. The weak-coupling analysis must give this.
- (STEP_Q) There is a continuous function sigma on a compact interval I, with sigma(u) > u on I (or sigma(u) < u for a quantity that must fall), such that Q(2L) >= sigma(Q(L)) whenever Q(L) is in I, for every L >= L_0, uniformly in j. I reaches from the base value to the target value. This is "the flow goes one way, for every value of Q".
- (SUF_Q) A value of Q beyond the target implies the seed on a torus of a fixed multiple of that size.

**Lemma FLOW (PROVED; elementary).** Let sigma be continuous on I = [u_0, u_1] with sigma(u) > u there, and delta := min over I of (sigma(u) - u) > 0. Let q_0 >= u_0 and q_(k+1) >= sigma(q_k) whenever q_k is in I. Then q_k > u_1 for some k <= (u_1 - u_0)/delta + 1.
Proof. While q_k is in I, q_(k+1) - q_k >= delta. QED

So (BASE_Q), (STEP_Q) and (SUF_Q) give (PHYS-SEED) at the size 2^k L_0 times the factor of (SUF_Q), with k bounded as in the lemma. A strict inequality alone is not enough (run 2, A5): the minimum delta over the whole interval is what carries the flow, so (STEP_Q) is a statement at every value between the two ends.

**What a test can show (Proposition T1 of row 712, applied).** Let M' be a comparison model in which the seed fails at every size. Then (BASE), (STEP) and (SUF) cannot all hold in M'. There are two outcomes.

- *Pass.* (STEP_Q) is false in M' (the quantity stalls or flows back). The candidate is not refuted. The test says what a proof of (STEP_Q) must use.
- *Fail.* (BASE_Q) and (STEP_Q) hold in M', or can hold. Then (SUF_Q) is false in M': the quantity does not see what stops the gap there. The candidate cannot be the whole tool.

**The comparison models, in the form that fits a flow.**

| Model | Where the seed fails | Mark | What the flow does there |
|---|---|---|---|
| (M1) U(1) in four dimensions, weak coupling | every size | THM, RECALLED, at large beta (Guth; Frohlich and Spencer); the statement on all torus quantities is GUIDE | scale invariance at large scales: every dimensionless quantity of the torus tends to a constant in L |
| (M2) SU(2) Wilson in five dimensions, weak coupling | every size | GUIDE (numerics; row 718 reads the sources) | the dimensionless coupling g_5^2/L falls as L grows: the flow runs toward the free end |
| (M3) the weights w_p = exp(beta ((1 + x)/2)^p), p large, at the coupling beta_t(p) | every size, at beta_t | THM GIVEN van Enter and Shlosman in the reading of row 712 (Proposition V; row 717 reads the paper) | two phases coexist at one lattice spacing |
| (M4) SU(N) Wilson, N >= 5, at its bulk transition | every size, at that coupling | GUIDE (numerics) | two phases coexist at one lattice spacing; at N infinite the dependence on L has jumps (finite-volume transitions; RECALLED: Kiskis, Narayanan and Neuberger) |
| (K6) SU(2) Wilson itself on a slab of width 1/T_c (run 2) | no gap along the long directions | GUIDE (numerics) | a fixed point of the flow in the long directions at one shape |

A remark on (M3) and (M4) in the continuum form. The transition of w_p sits at one finite coupling beta_t(p). The continuum trajectory of w_p passes it once and is then, by the usual belief (GUIDE), in the class of the Wilson weight. So (M3) does not give a continuum theory without a gap. It gives this: in the variable beta_W = p beta/2, the coupling of the quadratic form of w_p at the identity, the point beta_t(p) lies at larger and larger beta_W as p grows (GUIDE: beta_t grows with p). So there is no number beta_0 such that every weight of the family is "in the scaling region" for beta_W > beta_0. **A proof of a step that works for every lattice action with the Wilson quadratic form, once the quadratic coupling is large, is refuted by (M3).** The proof must use a bound on the distance of the weight from the Wilson weight, or the Wilson weight itself. The same holds for the effective actions that a renormalization step produces: at an effective coupling of order one they are not the Wilson weight, and nothing known bounds their distance from it.

### 2.2 The candidates

Three classes, by what (SUF_Q) can be.

**Class I: quantities that hold the whole thermal sum.** For these (SUF) is a theorem of this target.

| Q | Definition | (BASE): value at small L | (SUF) | (STEP), the one-way statement |
|---|---|---|---|---|
| Q1 | s_r(L) = S(L/r; L^3), g = log(1 + s) | tends to infinity like a power of 1/g(L) (GUIDE, 1.2); not controlled by the account (Proposition 1.1) | it is the seed: s_r(L) <= t(r) (Theorem SH) | (STEP-S): s(2L) <= sigma(s(L)), sigma(s) < s, for s in [t(r), s(L_0)] |
| Q2 | D(L) = Delta(L^4), the Casimir free energy of the symmetric torus | about 3 log(1/g(L)) + O(1) (GUIDE) | D <= 6.1 x 10^(-4) (Proposition Delta) | (CAS) of row 708: D(2L) <= theta D(L) while D > 6.1 x 10^(-4) |
| Q2' | Phi(L) = 16 F(L^4) - F((2L)^4), the doubling defect | about 15 D(L) (GUIDE) | Phi <= 1.9 x 10^(-4) (Theorem D) | Phi(2L) <= sigma(Phi(L)); for small Phi this is (Phi-step) of row 697 |
| Q3 | the pair (z(L), D(L/4)), z = L m(L^3) the lowest gap of the cube in units of 1/L | z tends to 0 like g^(5/3) exp(-12.46/g) (RECALLED, 1.2); D as above | z >= 256 D(L/4) + 29.64 (Lemma Z, Part 3; new) | (Z-GROW): z(L) passes 256 D(L/4) + 29.64 at one size |
| Q4 | pi(a) = a^4 p(1/a), the dimensionless thermal pressure in infinite space, with the cube b >= 24 a | the Stefan-Boltzmann value of six gluon modes, pi^2/15, with corrections in g (RECALLED) | g(a; b^3) <= 0.26 at b >= 24 a (Theorem SH, r >= 24); it follows from Delta(a, b^3) <= 0.26 | pi(2a) <= sigma(pi(a)); the non-strict form "p/T^4 does not fall as T rises" is the positivity of the interaction measure, eps - 3p >= 0 |

**Class II: quantities that hold the flux half only.**

| Q | Definition | (BASE) | What it can give | (STEP) |
|---|---|---|---|---|
| Q5 | zeta(L) = Z^(mu nu)(L^4)/Z(L^4), a twist ratio of the symmetric torus; U(L) of Identity FL; the flux free energies of 't Hooft | zeta tends to 0, U to 7/8 (GUIDE: the flux sectors are degenerate, 1.2) | (MF) of row 708, the flux half; not the seed (Identity FL: the zero-flux sum S_0 is a second, independent number) | zeta(2L) >= sigma(zeta(L)), sigma(u) > u on (0, 1). The proved part is Theorem F of row 697 (the two directions of the sheet); the open part is (TUBE') |
| Q6 | the Schrodinger functional coupling gbar^2(L) (Luscher, Narayanan, Weisz, Wolff): the response of log <C'| T_B^(L/a) |C> to a constant abelian boundary field; B is the periodic cube, the same transfer operator as in the seed | perturbative: gbar^2 = g^2 + c_1 g^4 + ... (read in `prior/gap-fullread-1.md`); the unique minimum of the action is a theorem of that paper on the lattice; fixed boundary values are not in the account | not known; at large L the boundary fields enter through their spatial holonomies only (they are flat), so this is a flux quantity (GUIDE, not derived) | the step-scaling function: gbar^2(2L) = sigma(gbar^2(L)) with sigma(u) > u. Seen in simulations on the measured range (RECALLED: Luscher, Sommer, Weisz, Wolff); no inequality is proved (`prior/gap-vir-lit.md`) |
| Q7 | the twisted Polyakov loop coupling (de Divitiis, Frezzotti, Guagnelli, Petronzio): a ratio of Polyakov loop correlations in a twisted and an untwisted direction | perturbative, no constant modes (RECALLED, not read) | the ratio tends to 1 when the centre symmetry holds in every direction, so the coupling tends to a finite constant (RECALLED, not read). A flux quantity | one-way up to a finite end value |
| Q8 | r^2 times the force between static charges; Creutz ratios at the scale L | perturbative | the area law, with the inequality of Tomboulis and Yaffe as in row 697 | r^2 F(r) grows; no inequality known |

**Class III: local quantities and others.**

| Q | Definition | (BASE) | Why it is not the tool |
|---|---|---|---|
| Q9 | the gradient flow coupling: t^2 <E(t)> at sqrt(8t) = c L | perturbative; with periodic sides the constant modes enter (RECALLED) | a local density at the scale L. It grows like L^4 times a condensate in every theory with a non-zero condensate, gap or no gap |
| Q10 | the coupling of the account: the two-point function of the action density at distance d, divided by the free kernel; it is zeta_K(d)^2 (3 (N^2 - 1)/pi^4) g(d)^4 (1 + eps) | **controlled by the account as it stands** for d <= d_0 (Theorem 0 (c)(3)) | it rises with d at small d and falls at large d if there is a gap: not one-way. Its exponential fall would give the gap on the one-field vectors only (run 2, (W5)) |
| Q11 | the finite-size shift of the plaquette, n^4 (abar_inf - abar_n): the derivative of Q2 along the coupling (Lemma DIL, Part 3) | positive at weak coupling (GUIDE) | it is the derivative of a Class I quantity, not a quantity that flows; its sign is the monotony (MONO-Delta) of Part 3 |
| Q12 | the deficit kappa(b) of Lemma K | - | monotone in every model of the class (Lemma K (d)); it is thermodynamic stability (the pressure is convex in the temperature) and cannot be strict by itself (row 708) |
| Q13 | the lowest zero-flux gap of a twisted box, z_0 = L m_0 | 2 sqrt(2) pi + g^2(L) gamma/(16 pi^2), gamma = -92.08 (RECALLED, 1.2) | (STEP) is false for SU(2) itself at weak coupling: z_0 falls as L grows, by the published one-loop coefficient. It must turn later. A one-way statement for every value does not exist for this quantity |
| Q14 | Route T: the gap of the thin torus R^2 x T^2_s with a twist, in units of 1/s | of order one at small s (tree level; the chart (CH), rows 679, 695) | its crux is (AC'), rows 678 and 691; not attacked here |

### 2.3 The tests, candidate by candidate

"Pass" and "fail" as defined in 2.1. Every entry on a comparison model is RECALLED or GUIDE, as marked in the table of 2.1.

| Candidate | (M1) U(1), d = 4 | (M2) SU(2), d = 5 | (M3) w_p at beta_t | (M4) SU(N) at the bulk point | In SU(2) itself |
|---|---|---|---|---|---|
| Q1, Q2, Q2', Q3 (Class I) | pass: the quantity is constant in L, (STEP) is false | pass: the quantity moves the other way | pass: no size has a seed, so the quantity never crosses the target | pass, the same | the step function depends on the shape; at the slab shape (K6) it has a fixed point |
| Q4 (pressure) | pass: p/T^4 is the constant of two photon modes | pass: p/T^5 rises toward the free value as T falls in lattice units | pass | pass | the non-strict form is the sign of the interaction measure |
| Q5 (twist ratio) | pass: the Z_2 twist of U(1) costs a fixed action at every scale, zeta is constant below 1 | pass: zeta falls with L | **fail**, if both phases confine: zeta can rise to 1 while the seed fails (GUIDE). In the abstract class of Theorem S the failure is PROVED: a product with a decoupled factor without a gap keeps every twist ratio and loses the seed | fail, the same | - |
| Q6 (Schrodinger functional) | pass: the coupling tends to the renormalized charge | pass | fail, as Q5 (GUIDE) | fail | - |
| Q7 (twisted Polyakov loop) | pass | pass | fail, as Q5 | fail | the coupling stops at a finite value: no step beyond it |
| Q8 (force) | pass: r^2 F tends to a constant | pass | fail, as Q5 | fail | - |
| Q9 (gradient flow) | pass | pass | fail: a condensate, no gap | fail | - |
| Q10 (two-point coupling) | pass | pass | not one-way | not one-way | **(STEP) is false**: the quantity rises, then falls |
| Q13 (twisted box gap) | - | - | - | - | **(STEP) is false** at weak coupling (RECALLED one-loop sign) |

**Reading of the table.**

1. No candidate is refuted by (M1) or (M2). Both tests say the same thing about every candidate: the proof of the step must use the sign of the one-loop coefficient in four dimensions for a non-abelian group, at every value of Q and not only at the weak end.
2. Every quantity of Class II and Q9 fail (M3) and (M4): they can flow to their strong end at a point with two phases. They see confinement, not the glue half. This is the statement of row 708 (C-C) for (MF), now for every coupling of the step-scaling kind. A proof that such a coupling grows without bound, if it existed, would give the flux half at most.
3. The quantities of Class I pass every test, and for a reason that has no content: their (SUF) is a theorem, so their (STEP) holds in no model without a seed. For them the test is not a filter. The content is in (STEP) itself, and row 708 says of its form (CAS) that it restates the seed in steps.
4. Two candidates are refuted in SU(2) itself as one-way statements: Q10 (the only one whose base the account controls as it stands) and Q13.
5. The account controls the base of no Class I quantity. Part 4 says what must be added.

**What Part 2 does not find.** No quantity that is at once (a) controlled at small L by weak-coupling analysis, (b) sufficient for the seed, and (c) carried by a step whose proof at one value of Q is easier than the seed itself. The step for a Class I quantity at a value of order one is a statement about one pair of tori at a coupling of order one. It has the same form and the same difficulty as the seed. What the continuum form adds is the list of what the step may use that the fixed-beta problem could not: the trajectory is asymptotically free, so the base is at infinity for Class I, and the question is only whether the flow stalls.
