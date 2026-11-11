lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-12T01:39Z

# gap-phys-seed: the continuum form of the seed, (PHYS-SEED), and the flow across scales

Row 720 of `FINISH.md`. Author run of Claude Fable 5.2 (model id claude-fable-5-2, max effort), Mac mini worker, one session, no subagents, pinned at commit 2a9dddb50. Started 2026-11-11T13:39Z. Research-stage working state. **No mass gap is claimed or proved here.** Nothing in this file is checked by another model.

**State of this file:** complete for this run (ended 2026-11-11). The final status, the RESULT line and the proof items for workers are in Section 5.

**What this run did not cover (full list in Section 5.2).** No proof of the account of Sussman and Alpoge was read, only statements at the lines named in Section 0. The primary papers on the small-volume spectrum were not read; the numbers come from van Baal's review. The statements about the comparison models and about the couplings of the step-scaling kind at large size are RECALLED or GUIDE. Nothing here is checked by another model. No tool for the flow across scales was found.

**Marks.** PROVED = proved by hand in this file from the named inputs, not checked. PROVED GIVEN = proved from a named input; the check state of the input is written. RECALLED = a known fact from memory or from a source named at the place, used in no proof. GUIDE = a belief from physics or numerics, used in no proof. OPEN = not proved.

## Status block (updated after each part)

- Section 0 (repo search, reading state, credits): done.
- Part 1 (what each end gives): done (Section 1). Result: the account controls log Z of its own tori up to an additive term C l^4 with l above a floor, at one time extent; this gives no bound for S near the threshold. On a small physical torus S is large (RECALLED physics), so no small torus can hold the seed. The large end needs a cube of at least 12.9 of its own correlation lengths.
- Part 2 (the flow; candidates and tests): done (Section 2). Fourteen candidates in three classes. Class I (S, the Casimir free energy, the doubling defect, the gap with the Casimir number, the thermal pressure) is sufficient for the seed, and its one-way step is false in every model without a seed, so the tests do not filter it. Class II (twist ratios, the Schrodinger functional coupling, the twisted Polyakov loop coupling, the force) holds the flux half at most and fails the test of a point with two confining phases. Two candidates are refuted in SU(2) itself as one-way statements. The account controls the base of no sufficient candidate.
- Part 3 (real attempts): done (Section 3). Proved (unchecked): Lemma Z, Corollary Z1, Lemma Z3, Theorems ZD and ZD-c ((PHYS-SEED) is equivalent to: the Casimir free energy of the symmetric torus is bounded, and the gap of the periodic cube in units of the inverse side is unbounded), Corollary Z2 (a converse of Theorem S), Lemma DIL, Proposition MB (monotony along the coupling and one weak-coupling number give the bound), Proposition NM. A guide run refutes monotony for the Ising model in its ordered phase.
- Part 4 (what must be extended): done (Section 4). The base of the best candidate needs the T0 chain below its torus floor, with exact cancellation of the bulk between two tori and the integral over the constant modes. This is weak-coupling work, not of the difficulty of the crux, and it gives the base only.
- Final section: done (Section 5): what the file adds, what it did not cover, six proof items, the RESULT line.

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
| Q5 (twist ratio) | pass: the Z_2 twist of U(1) costs a fixed action at every scale, zeta is constant below 1 | pass: zeta falls with L | **fail**, if both phases confine: zeta can rise to 1 while the seed fails (GUIDE). In the abstract class of Theorem S (a symmetric Z with positive transfer operators) the failure is PROVED GIVEN one factor without a gap in that class (RECALLED: the Ising model at its critical point): the product of a gauge model with such a factor has the twist ratios of the gauge model, and 1 + S is the product of the two factors, so the seed is lost | fail, the same | - |
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

## 3. Part 3: real attempts

Rule 0a, done before each attempt: `library/open-core.md` has no entry on a thermal sum, a Casimir free energy, a flux ratio or a monotone quantity. The FINISH rows that hold the neighbouring open statements are named in Section 0, and none of those statements is attacked here. Attempt 1 works on candidate Q3, Attempt 2 on candidate Q2. Both stay in Class I. Attempt 3 is the flux candidate Q5; it stops at the match with rows 697 and 708.

Notation for this part: D(a) := Delta(a, a, a, a). For an integer rho >= 2, Phi_rho(n) := rho^4 F(n^4) - F((rho n)^4) >= 0 (four uses of Lemma A (a)), and Phi := Phi_2.

### 3.1 Attempt 1: the seed from one gap and one Casimir number (candidate Q3)

**Aim.** The seed asks for a thermal sum below 6 x 10^(-4). A thermal sum has two parts: how high the first level is, and how many levels there are. I separate them. The count is carried by the Casimir free energy of a smaller symmetric torus. What is left is one number, the lowest gap of the cube in units of its side.

**Lemma Z (PROVED GIVEN Proposition Delta of row 708, checked row 709).** Let T_0 >= 3, b >= T_0 and T >= T_0 be integers. Then

S(T; b^3) <= (exp((b/T_0)^3 D(T_0)) - 1) exp(-(T - T_0) m(b^3)).

Proof. Put r_i = lambda_i/lambda_0 for the cube of side b; r_i <= r_1 = exp(-m(b^3)) for i >= 1. So S(T; b^3) = sum of r_i^(T - T_0) r_i^(T_0) <= r_1^(T - T_0) S(T_0; b^3). By Proposition Delta, g(T_0; b^3) <= (b/T_0)^3 D(T_0), and S = exp(g) - 1. QED

**Corollary Z1 (the gap form of the seed; PROVED GIVEN Lemma Z).** Let b >= 12 be divisible by 4. If

(C_b) b m(b^3) >= 256 D(b/4) + 29.64,

then S(b/2; b^3) <= 1/1650, which is the seed of Theorem SH at the shape r = 2.
Proof. Lemma Z with T_0 = b/4 and T = b/2: S(b/2; b^3) <= exp(64 D(b/4) - (b/4) m(b^3)). By (C_b), (b/4) m(b^3) >= 64 D(b/4) + 7.41, and log 1650 < 7.409. QED

Remark (other shapes; same proof). For a shape r with threshold t(r), a time b/r and T_0 = theta b/r, 0 < theta < 1: the seed S(b/r; b^3) <= t(r) follows from b m(b^3) >= (r/(1 - theta)) [(r/theta)^3 D(theta b/r) + log(1/t(r))]. At r = 2, theta = 2/3 this is 162 D(b/3) + 44.5; at r = 4, theta = 1/2 it is 4096 D(b/8) + 25.8.

**Lemma Z' (the count without the infinite lattice; PROVED GIVEN Lemma A, checked rows 698, 699).** Let T_0 >= 3 and rho >= 2 be integers, b = rho T_0, and T >= T_0. Then

g(T_0; b^3) <= (2/rho) Phi_rho(T_0), and S(T; b^3) <= (exp((2/rho) Phi_rho(T_0)) - 1) exp(-(T - T_0) m(b^3)).

Proof. By Lemma A (b), lambda_0^(T_0) >= Z(2 T_0, b^3)/Z(T_0, b^3), so g(T_0; b^3) <= 2 F(T_0, b, b, b) - F(2 T_0, b, b, b). F(n)/abs(n) does not increase in each side (the sign of F does not matter for this). So F(T_0, b, b, b) <= (b/T_0)^3 F(T_0^4), and, since 2 T_0 <= b, F(2 T_0, b, b, b) >= (2 T_0/b) F(b^4). Together: g(T_0; b^3) <= 2 rho^3 F(T_0^4) - (2/rho) F((rho T_0)^4) = (2/rho) Phi_rho(T_0). The bound for S(T; b^3) follows as in Lemma Z. QED

**Corollary Z1' (a seed from three finite objects; PROVED GIVEN Lemma Z').** Let b >= 12 be divisible by 4. If

(C'_b) b m(b^3) >= 2 Phi_4(b/4) + 29.64, where Phi_4(b/4) = 256 F((b/4)^4) - F(b^4),

then S(b/2; b^3) <= 1/1650.
Proof. Lemma Z' with rho = 4, T_0 = b/4, T = b/2: S(b/2; b^3) <= exp(Phi_4(b/4)/2 - (b/4) m(b^3)). QED

(C'_b) contains three finite objects: the gap of the cube of side b and the partition functions of the two symmetric tori of sides b/4 and b. It does not contain f, so it needs no limit of infinite volume at fixed spacing. The two counts are tied by Phi_4(n) = 256 D(n) - D(4n), so Phi_4(n) <= 256 D(n) and D(n) = the sum over k >= 0 of 256^(-(k+1)) Phi_4(4^k n). A run in the two-dimensional Ising model did not refute the two-dimensional form of Lemma Z' (704 cases, script lemzp_check.py in the same scratch folder; GUIDE).

**Lemma Z3 (a seed forces the Casimir free energy to zero; PROVED GIVEN Theorem S, Lemma E', Corollary S3' of row 697/699, checked).** Let N >= 3, s = S(N; (2N)^3) < 1/5041, q = 5041 s. For an integer L >= 2N let k >= 0 be such that D_k := 2^(k+1) N <= L < 2 D_k, and put s_k := q^(2^k)/5041. Then

Phi(L) <= 15360 s_k and D(L) <= 1024 s_k. For L = D_k: Phi(L) <= 1920 s_k and D(L) <= 128 s_k.

Proof. Step 1 (the doubling defect as four thermal terms). For a box B and a time n: F(n, B) = n e(B) + g(n; B), so 2 F(n, B) - F(2n, B) = 2 g(n; B) - g(2n; B) <= 2 g(n; B). Double the four sides of the torus n^4 one after the other and use the symmetry of Z to call the doubled side the time:

Phi(n) = 8 d_1 + 4 d_2 + 2 d_3 + d_4, d_i = 2 F(n, B_i) - F(2n, B_i), B_1 = (n, n, n), B_2 = (2n, n, n), B_3 = (2n, 2n, n), B_4 = (2n, 2n, 2n).

(Check: 16 F(n^4) = 8 d_1 + 8 F(2n, n, n, n) = 8 d_1 + 4 d_2 + 4 F(2n, 2n, n, n) = ... = 8 d_1 + 4 d_2 + 2 d_3 + d_4 + F((2n)^4).) So Phi(n) <= 16 g(n; B_1) + 8 g(n; B_2) + 4 g(n; B_3) + 2 g(n; B_4).
Step 2 (the thermal terms). By Theorem S, S(D_k/2; D_k^3) <= s_k. Let H be a box with sides h_i in [D_k, 4 D_k). Lemma E' with a = D_k/2 and b = D_k, once in each direction, has the exponents h_i/(D_k - D_k/2) = 2 h_i/D_k < 8. So g(D_k/2; H) <= 512 log(1 + s_k) <= 512 s_k. If all h_i <= 2 D_k the exponents are at most 4 and the factor is 64.
Step 3. Take n = L. The boxes B_i have sides L or 2L, all in [D_k, 4 D_k), and the time L is at least D_k/2; g does not increase with the time. So each g(L; B_i) <= 512 s_k and Phi(L) <= 30 x 512 s_k. For L = D_k the factor is 64 and Phi(L) <= 1920 s_k.
Step 4. D(L) = sum over i >= 0 of 16^(-(i+1)) Phi(2^i L) (the telescoping sum of row 697, Proposition R). The size 2^i L lies in [D_(k+i), 2 D_(k+i)) and s_(k+i) <= s_k. So D(L) <= 15360 s_k/15. QED

**Theorem ZD (five forms of the seed at one coupling; PROVED GIVEN Theorem SH, Proposition Delta, Lemmas Z, Z', Z3).** For a model of the class at one coupling the following are equivalent.

- (A) There is N >= 3 with S(N; (2N)^3) < 1/5041.
- (B) There is a >= 3 with D(a) <= 6.1 x 10^(-4).
- (C) There is b >= 12, divisible by 4, with b m(b^3) >= 256 D(b/4) + 29.64.
- (C') There is b >= 12, divisible by 4, with b m(b^3) >= 2 Phi_4(b/4) + 29.64.
- (D) The Casimir free energy is bounded and the gap is not of the order of 1/b: there are a_0 and D_0 with D(a) <= D_0 for all a >= a_0, and the supremum of b m(b^3) over the multiples b of 4 is infinite.

Proof, in the order (A) to (B) to (A), (A) to (D), (D) to (C) and (C'), (C) and (C') to (A). (A) gives (B): Lemma Z3 at L = D_k with k so large that 128 s_k <= 6.1 x 10^(-4). (B) gives (A): by Proposition Delta, S(a; (4a)^3) <= exp(64 x 6.1 x 10^(-4)) - 1 < 1/25. By Theorem SH (i) at the line r = 4, the numbers s'_k := S(2^k a; (2^(k+2) a)^3) satisfy 22.2 s'_k <= (22.2 s'_0)^(2^k), so they tend to 0. With N = 2^(k+1) a: S(N; (2N)^3) <= (s'_k)^2 by (T). (A) gives (D): Lemma Z3 gives D(L) <= 1024/5041 for every L >= 2N, and Corollary S3' gives m(L^3) >= log(1/q)/N for every L >= 2N. (D) gives (C): take a multiple b >= 4 a_0 of 4 with b m(b^3) >= 256 D_0 + 29.64. (C) gives (A): by Corollary Z1, S(b/2; b^3) <= 1/1650; by the line "r = 2, two stages" of `gap-seed-shape.md` 1.5, S(b/2; (2b)^3) < 1/25, which is the seed at r = 4 with a = b/2; then as in "(B) gives (A)". (D) gives (C'): Phi_4(b/4) <= 256 D(b/4) <= 256 D_0, so take a multiple b >= 4 a_0 of 4 with b m(b^3) >= 512 D_0 + 29.64. (C') gives (A): as (C) does, with Corollary Z1' in place of Corollary Z1. QED

**Corollary Z2 (a converse of Theorem S; PROVED GIVEN Theorem ZD).** Let the periodic cubes have a uniform gap: m(b^3) >= m_0 > 0 for all b >= b_0. If the lower limit of D(a)/a, as a grows, is below m_0/64, then the model has a seed. So a model of the class with a uniform gap on its periodic cubes and no seed must have D(a) >= (m_0/64) a - 0.12 for all large a: its Casimir free energy grows at least linearly with the side.
Proof. Choose a >= b_0/4 with D(a)/a <= m_0/64 - 0.116/a and put b = 4a. Then b m(b^3) >= 4 a m_0 >= 256 D(a) + 29.64, which is (C). QED

Row 697 left open whether a uniform gap forces a seed ("it needs a bound on the number of states"). Corollary Z2 names the bound: sublinear growth of D. I do not know a model of the class with a uniform gap and linear growth of D. OPEN, not on the path.

**Theorem ZD-c (the continuum form; PROVED GIVEN Theorem ZD and its inputs).** Let (a_j, beta_j) be a trajectory, and let P = {2^i l_1 : i >= 0} for one physical size l_1 such that l_1/(4 a_j) is an integer at least 3 for all large j. Put D^+(L) := the upper limit over j of D_j(L/a_j), and z^-(L) := the lower limit over j of (L/a_j) m_j((L/a_j)^3). In (Z-UNB) below, "unbounded" means: for every number C and every size L' there is L >= L' in P with z^-(L) > C. The following are equivalent.

- (PHYS-SEED): there is l in P such that the upper limit over j of S_j(l/(2 a_j); (l/a_j)^3) is below the threshold of Theorem SH (1/5041, or 1/1650 with the two-stage line).
- (PHYS-SEED-Delta): there is l' in P with D^+(l') < 6.1 x 10^(-4).
- (Z-SEED): there is L in P with z^-(L) > 2 psi^+(L) + 30, where psi^+(L) := the upper limit over j of Phi_4(L/(4 a_j); beta_j). This is one inequality between two functions of one physical size: the gap of the cube of side L in units of 1/L, and the doubling defect of the tori of sides L/4 and L.
- (BDD-Delta) and (Z-UNB) together:
 (BDD-Delta) there are L_0 in P and D_0 with D^+(L) <= D_0 for every L >= L_0 in P;
 (Z-UNB) z^- is unbounded on P.

Proof. The proof of Theorem ZD, with every constant uniform in j. From (PHYS-SEED): fix q' < 1 with 5041 S_j <= q' for all large j (if the threshold 1/1650 was used, first pass to a larger size of P by the two-stage line and the recursion of Theorem SH, as in "(C) gives (A)", and call it l again); Lemma Z3 gives D_j <= 1024 q'^(2^k)/5041 at every size from 2^k l on, and Corollary S3' gives (L/a_j) m_j >= 2 (L/l) log(1/q'). From (BDD-Delta) and (Z-UNB): choose L_1 >= 4 L_0 in P with z^-(L_1) > 256 D_0 + 30; for all large j, (C_b) holds at b = L_1/a_j, with D_j(L_1/(4 a_j)) <= D_0 + 10^(-3), so S_j(L_1/(2 a_j); (L_1/a_j)^3) <= 1/1650. The step between the first two forms is "(A) gives (B)" and "(B) gives (A)" with uniform constants. (Z-SEED) gives (PHYS-SEED) by Corollary Z1' for all large j. (PHYS-SEED) gives (Z-SEED): psi^+(L) <= 256 D^+(L/4) tends to 0 and z^-(L) tends to infinity along P. QED

**Corollary Z4 (a dichotomy in the plain gap variable; PROVED GIVEN Theorem ZD).** Let D(a) <= D_0 for all a >= a_0. Then either b m(b^3) < 256 D_0 + 29.64 for every multiple b >= 4 a_0 of 4, or there are N and c > 0 with m(L^3) >= c/N for every L >= 2N, so that L m(L^3) grows at least linearly. The gap of the cube in units of its inverse side cannot stay above 256 D_0 + 29.64 without growing for ever. In particular, at a coupling with no seed and bounded D (the critical coupling beta* of Theorem CRIT of row 708, if D is bounded there), every periodic cube of side b has a level within (256 D_0 + 29.64)/b of its ground state.
Proof. If (C_b) holds for one such b, Theorem ZD gives (A), and Corollary S3' gives the gap. QED

**What Attempt 1 gives.** The crux in continuum form is equivalent to two statements with no small number in them:

- (BDD-Delta): the Casimir free energy of the symmetric torus stays bounded as the torus grows.
- (Z-UNB): the lowest gap of the periodic cube, in units of the inverse side, is unbounded. By (TM-c) the space of the cube splits into the eight flux sectors, so (Z-UNB) says two things along one sequence of sizes: L m_0(L) is unbounded (m_0 the gap of the zero-flux sector), and L E_e(L) is unbounded for every flux e (E_e the lowest level of the sector e above the vacuum). The flux part is far weaker than an area law: it asks that the flux energy is not of the order of 1/L. With a bound D_0 on the Casimir free energy, one size with L m(L^3) above 256 D_0 + 29.64 is enough.

The numbers 6 x 10^(-4) and "20 correlation lengths" are then consequences, through Theorem SH, and not hypotheses.

The same content as one inequality at one size is (Z-SEED): the gap of the cube of side L, times L, exceeds twice the doubling defect of the tori of sides L/4 and L, plus 30. At small L the left side is near 0 and the doubling defect is large (about 765 log(1/g(L)), GUIDE). At large L, in a theory with a gap and confinement, the left side grows like L and the right side tends to 30. The crux is that the two cross. In a scale-invariant theory both sides are constant in L, and by Theorem ZD the left side is then below the right side: for the free photon z is at most 2 pi.

Where the two cross (GUIDE; a crude estimate with the numbers of `prior/gap-seed-size.md`: lightest glueball of mass 1/xi, sqrt(sigma) xi = 0.28, one-particle and one-flux-tube terms only). The doubling defect Phi_4(L/4) is about 16 Phi_2(L/4), and Phi_2(n) is about twice the weighted sum of the thermal terms of Step 1 of Lemma Z3. At n = 8 xi the three flux tubes of energy sigma n - pi/(3n) give about 0.06 for the thermal term of the cube, so Phi_4 is between 20 and 30 and (Z-SEED) fails at L = 32 xi (32 against 70 to 90). At n = 10 xi they give about 0.004, Phi_4 is about 1.5, and (Z-SEED) holds at L = 40 xi (40 against 33). So the box of (Z-SEED) has about 40 correlation lengths on a side, twice the box of the direct seed. The form (Z-SEED) pays a factor of two in the size for the absence of a small number.

**The tests in this form.** U(1) at weak coupling: (BDD-Delta) holds (GUIDE: scale invariance), (Z-UNB) fails: z stays bounded (the photon; the compact constant modes). Z_2 at large beta, and a point with two phases: (BDD-Delta) holds (D tends to the logarithm of the number of sectors or phases; RECALLED), (Z-UNB) fails: z tends to 0. SU(2) in five dimensions at weak coupling: (Z-UNB) fails, z falls with L (GUIDE). So in every comparison model the failing half is (Z-UNB), and (BDD-Delta) holds. I know one kind of model where (BDD-Delta) fails: a broken continuous symmetry, where the torus partition function carries a power of L from the zero modes (RECALLED; not a gauge model of the class).

**A run that tried to refute Lemma Z (GUIDE; a run can refute, not prove).** Two-dimensional Ising model, exact transfer matrices on rings of 3 to 10 sites, six couplings from 0.15 to 0.6, free energy density from Onsager's formula. Tested: the two-dimensional forms of Proposition Delta (g(T_0; b) <= (b/T_0) D(T_0)), of Lemma Z (all T_0 <= b, all T from T_0 to 3b) and of Step 1 of Lemma Z3 (Phi(n) <= 4 g(n; n) + 2 g(n; 2n)). 4050 cases, no violation; smallest margin 2.3 x 10^(-7) in Proposition Delta. Script /tmp/gap-phys-seed-scratch/scripts/lemz_check.py on the Mac mini, not kept in the repository. The numeric lock was taken and released; memory free was 58 percent.

### 3.2 Attempt 2: monotony along the coupling carries the bound on the Casimir free energy (candidate Q2)

**Aim.** (BDD-Delta) is a statement at every large size. I look for a one-way statement that would carry it from one small size. The dilation identity gives the exact form of such a statement: a sign of a finite-size shift.

**Lemma DIL (the Casimir free energy along the coupling; PROVED GIVEN Lemma 2 of run 2, quoted as Theorem D (f) in row 697, checked rows 698, 699).** f is convex in beta and f(0) = 0. Put abar_inf(s) := -f'(s)/6 where f is differentiable (all but countably many s). Then for every torus n:

Delta(n; beta) = 6 abs(n) times the integral over [0, beta] of (abar_inf(s) - abar_n(s)).

So Delta(n; .) is non-decreasing on an interval J if and only if abar_n <= abar_inf almost everywhere on J.
Proof. F(n; beta) = -6 abs(n) times the integral of abar_n over [0, beta] (dF/dbeta = -6 abs(n) abar_n, F(n; 0) = 0). f is the limit of F/abs(n) along the cubes 2^k n_0, a limit of convex functions, so it is convex, and f(beta) is the integral of f' over [0, beta]. QED

**(MONO-Delta)** on [beta_min, infinity): for every integer n >= 3, D(n; beta) is non-decreasing in beta there. In words: at every coupling above beta_min the mean plaquette action of a finite symmetric torus is at most that of the infinite lattice. On a trajectory the spacing falls as beta rises, so (MONO-Delta) says that the Casimir free energy of a torus of n sites does not rise when its physical size grows. It is the statement for the symmetric torus that the positivity of the interaction measure, eps - 3p >= 0, is for the thermal geometry.

**Proposition MB (monotony and one weak-coupling number give (BDD-Delta); PROVED).** Let rho >= 2 be an integer, nu_0 > 0, and N := {nu_0 rho^i : i >= 0} a set of inverse spacings. Let beta be a non-decreasing function on N (the trajectory). Let L_0 be a size with n_0 := L_0 nu_0 an integer at least 3. Assume:

- (MONO-Delta) on [beta(nu_0), infinity);
- (BASE-Phi): Phi_rho(L_0 nu; beta(nu)) <= P_0 for every nu in N. This is a bound on the doubling defect of the two tori of sides L_0 and rho L_0, uniform in the spacing;
- (APR): D(L_0 nu; beta(nu)) <= A for every nu in N, for some finite A.

Then for every nu in N and every k >= 0: D(rho^k L_0 nu; beta(nu)) <= P_0/(rho^4 - 1). So (BDD-Delta) holds on the sizes rho^k L_0, with D_0 = P_0/(rho^4 - 1), uniformly in the spacing.

Proof. Put M(nu) := D(L_0 nu; beta(nu)). The identity F(n^4)/n^4 - F((rho n)^4)/(rho n)^4 = Phi_rho(n)/(rho^4 n^4) gives D(n) = rho^(-4) (Phi_rho(n) + D(rho n)) at every coupling. At n = L_0 nu and the coupling beta(nu): M(nu) <= rho^(-4) (P_0 + D(rho L_0 nu; beta(nu))). The torus of rho L_0 nu sites is also the torus of the size L_0 at the finer spacing 1/(rho nu), where the coupling is beta(rho nu) >= beta(nu). By (MONO-Delta), D(rho L_0 nu; beta(nu)) <= D(L_0 rho nu; beta(rho nu)) = M(rho nu). So M(nu) <= rho^(-4) (P_0 + M(rho nu)). After i steps: M(nu) <= P_0 (rho^(-4) + ... + rho^(-4i)) + rho^(-4i) M(rho^i nu) <= P_0/(rho^4 - 1) + rho^(-4i) A. Let i grow. Last, by (MONO-Delta) again, D(rho^k L_0 nu; beta(nu)) <= M(rho^k nu). QED

Remarks. (i) No scaling hypothesis is used: the torus of n sites at two couplings of the trajectory is one lattice object at two physical sizes. (ii) (APR) follows from the account as in 1.1.5 (iii) when L_0 is one of its tori. (iii) (BASE-Phi) contains only the two tori L_0 and rho L_0. If both are small it is a weak-coupling statement. It is not in the account (Proposition 1.1); Part 4 says what is missing. Its expected size is about 45 log(1/g(L_0)) at rho = 2 (GUIDE). (iv) Since the trajectory can start at any fine spacing, beta_min can be taken as large as one likes. (MONO-Delta) is then a statement at weak bare coupling only, but for every lattice size n, also for tori that are large in physical units.

**Corollary MB1 (PROVED GIVEN Proposition MB, Theorem ZD-c).** (BASE-Phi), (MONO-Delta) and (Z-UNB) on the sizes 4 rho^k L_0 give (PHYS-SEED): it is enough that z^-(L_1) > 256 P_0/(rho^4 - 1) + 30 at one size L_1 = 4 rho^k L_0.

**Is (MONO-Delta) true? Three known answers.**

1. Two dimensions, Wilson SU(2) (RECALLED: the character expansion; not re-derived). The torus of A plaquettes has Z = sum over j of c_j(beta)^A up to the bulk factor, with c_j = I_(2j+1)(beta)/I_1(beta) increasing in beta. So D = log(1 + sum over j > 0 of c_j^A) is increasing: (MONO-Delta) holds.
2. Wilson SU(2) in four dimensions, the two ends. For small beta, D(n) = sum of 16^(-(k+1)) Phi(2^k n) with Phi(n) = 192 n^3 (beta/4)^(4n) (1 + O(beta)) for n >= 5 (`gap-seed-sc.md` Theorem 2, checked row 704): the values rise with beta; the derivative is not bounded there, so the sign of the shift is not proved by this. For fixed n and large beta, D is about (3/2) log beta (GUIDE, 1.2): rising. The middle is open.
3. **The Ising model: (MONO-Delta) is false in the ordered phase (GUIDE run, with the leading term by hand).** Exact transfer matrices of the two-dimensional Ising model, tori n^2 with n = 3 to 8 and (4, 8), (3, 9), couplings K = 0.02 to 1.20: D rises to a maximum above log 2 and then falls to log 2. Values: D(3^2) = 0.6971 at K = 0.56 and 0.6965 at K = 0.60, against log 2 = 0.6931; D(8^2) = 0.69384 at K = 0.50 and 0.69318 at K = 0.60. For the torus (4, 8): 0.7255 at K = 0.44, 0.7000 at K = 0.60. The reason, at leading order of the low-temperature expansion: on the torus a band of flipped rows between two walls that wrap costs 2n broken bonds, whatever its width, and a cluster of as many flipped spins that does not wrap costs more. For each ground state there are n(n - 1) such bands (two directions, and the pairs of n wall positions, each pair counted once for the two ground states). So D(n^2; K) = log 2 + n(n - 1) exp(-4nK) (1 + o(1)) as K grows: it tends to log 2 from above. A second run with 40 digits gives for the quotient (D - log 2)/(n(n - 1) exp(-4nK)) the values 1.038, 1.040, 1.022, 1.007 at n = 3 and 1.517, 1.246, 1.111, 1.033 at n = 4, for K = 0.8, 1.0, 1.2, 1.5. (The leading term is by hand; the remainder is not bounded here, so this is not a proof.) Scripts /tmp/gap-phys-seed-scratch/scripts/mono_check.py and lowT_check.py; lock taken and released each time; memory free 58 percent.

So (MONO-Delta) is not a property of the class. It fails where a larger coupling means a larger box in units of the correlation length. Before the run I expected (MONO-Delta) to follow, for the abelian models, from the inequalities of Griffiths and Ginibre by identifying the links of the infinite lattice modulo the torus. That argument is wrong: the identification multiplies the coupling by the number of copies. The run refutes the conclusion for the Ising model. I record this because row 697 names an inequality of Griffiths type as one of the three tools that could prove the seed: for the Casimir free energy it would not give the sign.

**Proposition NM (where monotony must fail; PROVED GIVEN Proposition Delta and Lemma Z3).** In a model of the class let beta_t < beta_1 be two couplings such that no size has a seed at beta_t and some size N has a seed at beta_1. Then for every large k, with n = 2^(k+1) N: D(n; beta_1) <= 6.1 x 10^(-4) < D(n; beta_t). So D(n; .) is not non-decreasing on [beta_t, beta_1], and abar_n > abar_inf on a set of positive measure there.
Proof. At beta_t, (B) of Theorem ZD fails, so D(a; beta_t) > 6.1 x 10^(-4) for every a >= 3. At beta_1, Lemma Z3 gives D(2^(k+1) N; beta_1) <= 128 q^(2^k)/5041, which is below 6.1 x 10^(-4) for large k. QED

Use. If the weights w_p of Proposition V, or SU(N) for N >= 5, have a seed on the weak side of their transition (GUIDE: both phases confine with a gap), then (MONO-Delta) is false for them. So a proof of (MONO-Delta) for the Wilson SU(2) weight must use what separates it from w_p, as for the seed itself. In the other direction: in a model where (MONO-Delta) holds on [beta_min, infinity), a seed that is lost at one coupling above beta_min is lost at every larger coupling.

**What Attempt 2 gives.** A second reduction, by implication only:

(BASE-Phi) and (MONO-Delta) and (Z-UNB) give (PHYS-SEED).

(BASE-Phi) is one weak-coupling number. (MONO-Delta) is a sign with no small number in it; it is true at both ends of the Wilson axis (item 2, GUIDE at the weak end), true in two dimensions, false in ordered phases of other models, and open in the middle. (Z-UNB) is the crux in its plain form. This is not an equivalence: (PHYS-SEED) gives (BDD-Delta) but I do not know that it gives (MONO-Delta). The exact open statements are (MONO-Delta) on [beta_min, infinity) for Wilson SU(2), and (Z-UNB).

### 3.3 Attempt 3: the flux candidate (Q5) stops at earlier rows

In the continuum form the twist ratio of the symmetric torus, zeta(L), runs from 0 at small L (GUIDE) to 1 at large L, and the seed forces zeta >= 1 - 2t/(1 + t) (P2). The step from L to 2L splits into the two directions of the twisted plane and the two transverse directions. The first is Theorem F of row 697 (proved). The second is (TUBE') of row 697, the same open step as (MF) of row 708 and (VORT) of run 2. By rule 0a I stop here and name the match. The continuum form adds one remark, from Theorem ZD-c: for the seed the flux half is needed only in the weak form "L E_e(L) is unbounded", and not as an area law.

### 3.4 Result of Part 3

| Statement | Mark |
|---|---|
| Lemma Z: S(T; b^3) <= (exp((b/T_0)^3 D(T_0)) - 1) exp(-(T - T_0) m(b^3)) | PROVED GIVEN Proposition Delta (checked) |
| Corollary Z1: b m(b^3) >= 256 D(b/4) + 29.64 gives the seed at r = 2 | PROVED GIVEN Lemma Z |
| Lemma Z' and Corollary Z1': g(T_0; (rho T_0)^3) <= (2/rho) Phi_rho(T_0); b m(b^3) >= 2 Phi_4(b/4) + 29.64 gives the seed at r = 2, with no reference to the infinite lattice | PROVED GIVEN Lemma A (checked) |
| Lemma Z3: a seed gives D(L) <= 1024 q^(2^k)/5041 at every size L >= 2N | PROVED GIVEN Theorem S, Lemma E' (checked) |
| Theorem ZD and ZD-c: the seed is equivalent to "D bounded and b m(b^3) unbounded"; (PHYS-SEED) is equivalent to (BDD-Delta) with (Z-UNB), and to the one inequality (Z-SEED) | PROVED GIVEN the above and Theorem SH (checked) |
| Corollary Z2: a uniform gap with sublinear D gives a seed | PROVED GIVEN Theorem ZD |
| Corollary Z4: with D bounded, the gap of the cube times its side stays below 256 D_0 + 29.64 or grows linearly | PROVED GIVEN Theorem ZD |
| Lemma DIL, Proposition MB, Corollary MB1: (BASE-Phi), (MONO-Delta), (Z-UNB) give (PHYS-SEED) | PROVED (the hypotheses are open) |
| Proposition NM: monotony fails between a coupling with no seed and a larger coupling with a seed | PROVED GIVEN Proposition Delta, Lemma Z3 |
| (MONO-Delta) is false for the Ising model in its ordered phase | GUIDE (exact transfer matrices; leading term by hand) |
| (Z-UNB); (MONO-Delta) for Wilson SU(2); (BASE-Phi) | OPEN |

## 4. Part 4: what in the T0 chain must be extended

**The best candidate.** It is Class I in the form of Corollary MB1: (BASE-Phi), (MONO-Delta), (Z-UNB). In the form of Theorem ZD-c, (BDD-Delta) with (Z-UNB), no base is needed at all, but then both statements live at large sizes. Only (BASE-Phi) is a statement that the T0 chain could supply.

**What the T0 chain gives now, at this place.** (UV-Z) of 1.1.2 on tori of four equal sides above the floor l_*(g), with the additive error C l^4. It gives (APR) of Proposition MB (1.1.5 (iii)). It does not give (BASE-Phi): the doubling defect is a difference of two free energies, each known up to C l^4.

**What (BASE-Phi) asks.** One number P_0 with Phi_rho(L_0/a; beta(a)) <= P_0 for all fine spacings a, where the two tori have the sides L_0 and rho L_0 (rho = L fits the tori of the account). P_0 enters the final threshold as 256 P_0/(rho^4 - 1), so an additive error of order one is enough; no small number is needed. The expected value is 15 x 3 log(1/g(L_0)) at rho = 2 (GUIDE). Three extensions are needed.

- **E1, exact cancellation of the bulk between two tori.** In rho^4 F(n^4) - F((rho n)^4) every local term that does not wrap must cancel exactly, at every scale and for every kind of term (small-field terms, large-field terms, boundary terms, vacuum numbers). The complete account declares the needed statements for its localized terms: "Torus-independence of the localized terms" (CA-I 4.38, line 58187) and the torus-independence of the vacuum-energy density up to delta_vac-bar (CA-II 8.22, line 141276). I read only the second statement. What is left after the cancellation: the terms that wrap, and the difference of the two last integrals. Constants: the density bound delta_vac-bar is multiplied by the number of unit cells, so it is of order one only when the tori have at most about 1/delta_vac-bar unit cells; an exact cancellation, not a bound on a density, is what (BASE-Phi) needs.
- **E2, below the torus floor.** The last integrals are those of the unit lattice with l^4 sites, l >= l_*(g), at the coupling g. The account bounds each by exp(C l^4) and does not evaluate it. To evaluate their difference the block steps must go on until the block lattice has a bounded number of sites on a side. That removes (RF35): the domains that wrap are then not exponentially rare, and their leading terms must be computed, not bounded. The backgrounds are flat connections with holonomies; the outline has the classical gap with holonomies of any size (SA L8733-8760, L9552-9565) and says that the interacting comparison "still need[s] their own quantitative comparison" (SA L8765-8771). Physical size: any L_0 such that the coupling at the scale L_0/(C_0 M) is below the ceilings of the account, C_0 a fixed number of blocks.
- **E3, the constant modes.** The last integral, over the fields on a lattice of a bounded number of sites at small coupling, is not Gaussian. Near each of the sixteen flat connections with central holonomies the twelve constant modes have a quartic action, and along the valley of commuting holonomies the transverse modes have a frequency that vanishes at those points. This is Luscher's small-volume problem (1.2). For the partition function it is one finite-dimensional integral. For SU(2) in four dimensions the quartic integral is at the border of convergence (GUIDE: my count gives a logarithm of beta from the valley, the integral of d^4x/abs(x)^4 between the scales beta^(-1/4) and 1), so the compactness of the holonomies must be used. Output: Phi_rho(L_0) = (rho^4 - 1)(3/2) log beta_eff(L_0) up to lower terms, with an error of order one.

**Is this extension of the same difficulty as the crux? No.** E1 to E3 are statements at small coupling. They are of the kind of the T0 chain itself: block renormalization on a torus, with one new finite-dimensional integral at the end. They are long. E2 changes the geometry of every step near the end (domains that wrap), and E3 is new work with no counterpart in the account. But no step needs a coupling of order one.

**What the extension would not do.** It gives (BASE-Phi) only. It does not touch (MONO-Delta) or (Z-UNB). With the base alone nothing follows about the gap: the comparison models have a base too (2.3). So the extension has no value for (GAP) before a tool for (Z-UNB) exists. Its value by itself is a theorem short of the gap: the low spectrum of the continuum theory on a small periodic torus (run 2's (W3), and the statement of 1.2 that S is large there, which is RECALLED physics at present).

**The extension that would be the crux.** To carry the T0 chain past first passage, to effective couplings of order one, is run 2's (EXIT) and is the crux itself. By the reading of (M3) in 2.1 it needs a bound on the distance of the effective actions from the Wilson weight at a coupling of order one. Nothing in the account, in this target or in the literature read gives such a bound.

## 5. Final status, RESULT, and proof items for workers

**No mass gap is proved. (PHYS-SEED) is open, and no tool for the flow across scales was found.**

### 5.1 What this file adds

1. *Part 1.* The exact place where the account stops: tori of four equal sides above the floor l_*(g), the logarithm of the partition function up to C l^4, at one time extent. Proposition 1.1: this is short of the seed by the number of unit cells. The small end is the wrong end for the seed: S is large on a small torus (RECALLED physics), and the seed needs a cube of at least 12.9 of its own correlation lengths (P1 for the shapes of Theorem SH).
2. *Part 2.* A classification of the flow candidates by what they can imply. Only quantities that hold the whole thermal sum (Class I) can give the seed, and for them the tests in the valid form are no filter. Every coupling of the step-scaling kind (Schrodinger functional, twisted Polyakov loop, force, gradient flow) and every twist ratio holds the flux half at most or a local density, and fails at a point with two confining phases. Two candidates fail as one-way statements in SU(2) itself (the two-point coupling of the account; the gap of a twisted box). The reading of Proposition V for a flow: no step can be proved for all lattice actions with the Wilson quadratic form at large quadratic coupling.
3. *Part 3.* (PHYS-SEED) is equivalent to two statements with no small number: (BDD-Delta), the Casimir free energy of the symmetric torus is bounded at large sizes; (Z-UNB), the gap of the periodic cube in units of its inverse side is unbounded (Theorems ZD, ZD-c; Lemmas Z, Z3). It is also equivalent to one inequality between three finite objects at one physical size, (Z-SEED): L m(L^3) > 2 Phi_4(L/4) + 30, the gap of the cube against the doubling defect of the tori of sides L/4 and L (Lemma Z', Corollary Z1'). GUIDE: this holds from about 40 correlation lengths. A converse of Theorem S given sublinear growth of the Casimir free energy (Corollary Z2). A dichotomy for the plain gap variable (Corollary Z4). An implication with one weak-coupling number and one sign: (BASE-Phi), (MONO-Delta), (Z-UNB) give (PHYS-SEED) (Proposition MB). (MONO-Delta) is not a property of the class (Proposition NM; the Ising run).
4. *Part 4.* The extension of the T0 chain that the base needs (E1 to E3) is weak-coupling work, not of the difficulty of the crux, and has no value for (GAP) before a tool for (Z-UNB) exists.

### 5.2 What this run did not cover

(1) No proof of the account was read; its statements are quoted from the lines named in Section 0, and CA-III was not fetched. (2) The primary papers on the small-volume spectrum (Luscher; Luscher and Munster; Koller and van Baal) were not read; the numbers are from van Baal's review, pages 10-12 and 31-34. (3) The statements on the Schrodinger functional coupling at large size, on the twisted Polyakov loop coupling, on the gradient flow coupling and on the phases of the large-N torus are from memory. (4) Every entry of the tables of 2.3 about a comparison model is RECALLED or GUIDE. (5) The count kappa = 3 and the logarithm in E3 are my own counts on a fixed lattice, not proofs. (6) The low-temperature statement on the Ising model has its leading term by hand and its remainder from a run. (7) Lemmas Z, Z3, DIL, Theorems ZD, ZD-c, Corollaries Z1, Z2, Z4, MB1 and Propositions MB, NM, 1.1 are not checked by another model. (8) Boxes that are not cubes, and sides that are not multiples of 4, are not treated in Theorem ZD. (9) Whether a model of the class can have a uniform gap on its periodic cubes and no seed is left open (Corollary Z2).

### 5.3 Proof items for workers (each is a complete brief)

**Item 1, check (another model; high effort).** Check line by line `library/gap-phys-seed.md` Sections 1.1.5 (with Proposition 1.1), 1.3, 2.1 (Lemma FLOW), 3.1 (Lemma Z, Corollary Z1, Lemma Z', Corollary Z1', Lemma Z3, Theorem ZD, Corollaries Z2 and Z4, Theorem ZD-c) and 3.2 (Lemma DIL, Proposition MB, Corollary MB1, Proposition NM). Inputs to open: `library/gap-crux-restate.md` Sections 1 and 3.4 (Lemma A, (LB), Theorem S, Lemma E', Corollary S3'); `library/gap-seed-shape.md` 1.4 and 1.5 (Theorem SH, the lines r = 2 and r = 4); `library/gap-mid-max.md` Section 4.3 (Proposition Delta) with `library/gap-mid-check.md`. Points to test first: in Lemma Z', the two uses of the monotony of F(n)/abs(n) (an upper bound for the torus (T_0, b^3) and a lower bound for (2 T_0, b^3)); in Lemma Z3, the decomposition Phi = 8 d_1 + 4 d_2 + 2 d_3 + d_4 and the range of the sides in Step 2 (exponents below 8); in Theorem ZD, the step "(B) gives (A)" (the use of (T) to pass from the shape r = 4 to r = 2) and the step "(C) gives (A)"; in Theorem ZD-c, the uniformity in j; in Proposition MB, the use of (MONO-Delta) at the torus of rho L_0 nu sites and the limit of rho^(-4i) A; in Lemma DIL, the convexity of f. Report the first failing step, or none. Output `library/gap-phys-seed-check.md`.

**Item 2, lead note (no proof).** Record in `library/gap-skeleton-final.md`, next to (PHYS-SEED) in Section 13.14: (PHYS-SEED) is equivalent to (BDD-Delta) with (Z-UNB) (Theorem ZD-c of `library/gap-phys-seed.md`, unchecked until Item 1), and the classification of Section 2.2 (only quantities that hold the whole thermal sum can give the seed; the step-scaling couplings hold the flux half at most). State that the open statements on the path of (GAP) are now (Z-UNB) and (BDD-Delta), or (Z-UNB), (MONO-Delta) and (BASE-Phi).

**Item 3, reading (Codex runner; downloads allowed; guide only).** Find published Monte Carlo values of the mean plaquette of four-dimensional Wilson SU(2) on symmetric periodic lattices n^4, n = 4, 6, 8, 12, 16, at the same couplings in the range beta = 1.5 to 3.0 (standard convention beta = 4/g^2), with their errors, and the infinite-volume or largest-lattice value at each coupling. Answer one question with a table: does the mean plaquette action 1 - (1/2) tr U_p on the smaller lattice exceed that of the larger lattice at any coupling, outside the errors? This tests (MONO-Delta) of `library/gap-phys-seed.md` 3.2 (the Casimir free energy of a symmetric torus does not fall as the coupling rises). Also quote, from the thermodynamics literature for SU(2), the sign of the interaction measure eps - 3p at all temperatures (the same statement for the thermal geometry). Output `library/prior/gap-mono-lit.md`. No proof step may use these numbers.

**Item 4, reading (Codex runner; downloads allowed).** Read in full: M. Luscher, Nucl. Phys. B219 (1983) 233; M. Luscher and G. Munster, Nucl. Phys. B232 (1984) 445; J. Koller and P. van Baal, Nucl. Phys. B302 (1988) 1; P. van Baal, arXiv:hep-ph/0008206, Sections 2 to 4. Answer with quotes and page numbers: (a) which statements about the low levels of the periodic box are proved and which are computed (the effective Hamiltonian, the value eps_1, the flux splitting formula (12) of the review); (b) the range of z = m L in which each description is claimed to hold; (c) the published one-loop coefficients of the twisted box (Table 1 of the review) and the statement that z_0 falls with the volume there; (d) for the twisted Polyakov loop coupling (de Divitiis, Frezzotti, Guagnelli, Petronzio, Nucl. Phys. B422 (1994) 382) and the Schrodinger functional coupling: what is stated about their behaviour at large box size. This replaces the RECALLED marks of `library/gap-phys-seed.md` 1.2 and 2.2 by quotations. Output `library/prior/gap-small-volume-lit.md`.

**Item 5, proof (author; medium effort; off the path of (GAP), a test of a statement).** Prove or refute by hand: for the two-dimensional Ising model on the torus n^2, n >= 3, D(n^2; K) = log 2 + n(n - 1) exp(-4nK) (1 + o(1)) as K tends to infinity, with a bound for the remainder (a convergent low-temperature expansion of log Z on the torus and of Onsager's f; the terms that do not wrap cancel). Then state the consequence: (MONO-Delta) of `library/gap-phys-seed.md` 3.2 fails for every n at large K. Known: a run with exact transfer matrices gives the quotient 1.007 at n = 3, K = 1.5 and 1.033 at n = 4, K = 1.5. Output `library/gap-mono-ising.md`. Say at the top that this is a statement about a comparison model.

**Item 6, proof (author; only if the lead wants the base; long).** The fixed-lattice form of (BASE-Phi): for Wilson SU(2) on the tori n^4 and (2n)^4 with n fixed, prove Phi(n; beta) = (45/2) log beta + O(log log beta) as beta tends to infinity, by Laplace asymptotics at the flat connections (the sixteen central points with their twelve quartic constant modes, the valley of commuting holonomies, the gauge directions). Inputs: the chart of row 679 (`library/gap-twist-chart.md`) for the technique of a chart at a minimal orbit; Section 4, E3, of `library/gap-phys-seed.md` for the count. Stop rule: a proof, or the exact place where the valley integral is not controlled. This is a statement at one lattice size and is not uniform in the spacing; it does not give (BASE-Phi) on a trajectory. Output `library/gap-base-fixed-lattice.md`.

**Not proposed.** A proof lane on E1 to E3 of Section 4 (the base on a trajectory): it is long weak-coupling work and has no value for (GAP) before a tool for (Z-UNB) exists. Another author run on a step inequality: Part 2 finds no candidate whose step at one value is easier than the seed.

RESULT: no mass gap is proved and no tool for the flow across scales was found; stated exactly: the account controls log Z on its own tori (four equal sides above a floor) up to C l^4 at one time extent, which gives no bound for S near the threshold, and S is large on small tori (recalled physics), while the seed needs a cube of at least 12.9 of its own correlation lengths; fourteen candidate quantities classed and tested in the valid form: only those that hold the whole thermal sum can give the seed, the step-scaling couplings and twist ratios hold the flux half at most and fail at a point with two confining phases, and two candidates fail in SU(2) itself; proved here (unchecked): (PHYS-SEED) is equivalent to "the Casimir free energy of the symmetric torus is bounded and the gap of the periodic cube times its side is unbounded", and to the one inequality L m(L^3) > 2 Phi_4(L/4) + 30 between the gap of one cube and the doubling defect of two symmetric tori (Lemmas Z, Z', Z3, Theorems ZD, ZD-c), a converse of Theorem S under sublinear Casimir growth, and the implication "(BASE-Phi), (MONO-Delta), (Z-UNB) give (PHYS-SEED)" with Proposition NM; a guide run refutes monotony along the coupling for the Ising model; open: (Z-UNB) (the crux in plain form), (BDD-Delta) or (MONO-Delta) for Wilson SU(2), and the weak-coupling base (BASE-Phi), whose proof needs the T0 chain below its torus floor with the constant modes and is not of the difficulty of the crux.
