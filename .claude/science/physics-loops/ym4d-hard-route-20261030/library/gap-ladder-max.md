lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T10:56Z

# gap-ladder-max (FINISH row 978): what carries a seed from one coupling to every finer cutoff

Research-stage working state. It grants no status. Nothing here is a public claim.
Pinned at commit 76c71df0c. Started 2026-11-14T22:56Z. Model: Claude Fable 5.2, max effort, Mac mini worker 3. No subagents.

Marks used: PROVED (every step written here), ARGUED (argument written, a step not written in full), OPEN.

## Plan (at most eight steps; one step per response; each result is appended before the next step starts)

1. **Goal and object, read narrowly.** Read only the statement of (SEED-phys) (`library/gap-seed-limit.md` Section 5) and of the seed S(a;B) with its chain (Proposition HC, E-to-HC, Theorem BR, Corollary BR-J, Lemma RATE). Write the goal and the object in my own words. No route file, no digest.
2. **Three or more approaches of my own**, written from the goal and the object only, each with its crux lemma.
3. **Fact tests**, before any proof attempt, one verdict per test: free photon, compact U(1), frozen Q_8 and 2T, SMALL-BOX, K7, FT-FK. The ceilings 2/3, 0.775 and 1.0109 bind worst-case forms only.
4. **Duplicate check** (rule 0a): grep `library/open-core.md` and the FINISH rows for the crux lemma of the best approach. If another row covers it, stop, name the match, pick the next approach.
5. **Attack the crux lemma** of the best approach (first route).
6. **Attack, second and third routes** if the first fails; stop at a proof, a counterexample, or three failed routes.
7. **Prior work, read after the attack**: `library/gap-phys-seed.md` and its check (row 720; Corollary MB1 needs (APR)), `library/gap-skeleton-final.md` Route Z, rows 931-977, and the lines of Sussman and Alpoge's account where its control ends. Say per approach whether it is already there. Credit what is used.
8. **Next step and RESULT line.**

## Log

- 22:56Z. File created. Memory free 64 percent (`memory_pressure`). No numeric job started.
- 23:08Z. Step 1 written (goal and object, read narrowly). Step 2 written (six approaches of my own).
- 23:12Z. Step 3 written (fact tests; definitions of K7 and FT-FK read first).
- 23:15Z. Step 4 (duplicate check) and Step 5 (Lemma IHC, Corollary CU, Lemma LAD, Lemma G) written.
- 23:19Z. Sections 5.6, Step 6, Step 7 (prior work read after the attack) written.
- 23:22Z. Step 8 and the RESULT line written. 23:24Z: section 5.7 and the (APR) form of Corollary CU added; times in this log are from `date -u`.
- No numeric job was started in this run; the numeric lock was never taken. No subagent was used. Two arithmetic evaluations quoted in 5.6 (b) and 5.7 are in `guide/lane978/arith978.py` (output `arith978.log`); they are hand-checkable, they are not GUIDE runs, and nothing rests on them.
- 23:26Z. Check state of row 720 corrected (it is checked, row 727); the defective form added to 5.7; file complete for this run.

## Step 1. Goal and object (read narrowly; no route file, no digest)

**Read for this step, statements only.** FINISH row 978. `gap-seed-limit.md` lines 1-53 and Section 5 to Section 7 (the goal). `gap-direction-max.md` lines 270-394 (S, X, (5.3), Theorem V, Proposition HC, (E-to-HC), SMALL-BOX). `gap-fc-max.md` lines 121-228 (Theorem BR and its corollaries). `gap-trajtest-opus.md` lines 1-135 (K_a, Lemma RATE). Not read yet: any route discussion, `gap-phys-seed.md`, `gap-skeleton-final.md`, rows 931-977, any digest.

**Object.** SU(2), Wilson action, coupling beta. B is a periodic spatial box, R = R_B(beta) its gauge-invariant transfer operator, with eigenvalues lambda_0 > lambda_1 >= ... > 0, r_i = lambda_i/lambda_0 = e^(-E_i).

- S(t; B) = sum over i >= 1 of r_i^t, and X(t; B) = log(1 + S(t; B)). 1 + S(t; B) = Z(B x t)/lambda_0^t.
- (SEED) at (beta, n): S_beta(n; (2n)^3) < 1/5041. Theorem S (row 697, checked): a seed at n gives a seed at 2^k n with value (5041 s)^(2^k)/5041, and a gap m_0 = log(1/(5041 s))/n on every cube of side 2^(k+1) n.
- nu is the vacuum law on a slice, P the vacuum chain (the ground-state transform of R/lambda_0), p_s(u, .) its s-step density with respect to nu. (5.3): 1 + S(2s; B) = E_(u ~ nu) ||p_s(u, .)||_2^2.
- (HC-vac)_alpha: ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-2 alpha m), all m >= 0, h gauge invariant.
- Proposition HC: (HC-vac)_alpha gives X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m) and E_1 >= alpha.
- Theorem BR: the log-Sobolev inequalities (LSI-br)_s for the bridge laws nu_s, 0 < s < 1/beta, with A = integral of alpha_s ds, give (HC-vac)_(A/2). Corollary BR-J and the size test: the seed on the seed box follows once A/2 >= K_a := (C_beta + 3 log a)/(a - 2), where a is the time extent of the seed box in lattice units and C_beta = log(72 beta 24^3/x_*) or the like (12.51 at beta 2.3).
- Lemma RATE (row 974): X(2m + 2; B) <= C e^(-2 alpha m) for all m forces E_1(B) >= alpha. So the size test needs m_0++ >= K_a on the seed box.

**Goal.** (SEED-phys), `gap-seed-limit.md` Section 5. A family of cutoffs iota, each with a coupling beta_iota and a spacing a_iota > 0. There are ell_* > 0 and s_* < 1/5041 such that for every iota there is an integer n_iota >= 3 with n_iota a_iota <= ell_* and S_(beta_iota)(n_iota; (2 n_iota)^3) <= s_*. The consumer is Proposition P there: every cube of side 2^(k+1) n_iota has lattice gap at least m_0(iota) = log(1/(5041 s_iota))/n_iota >= M_* a_iota, with M_* = log(1/(5041 s_*))/ell_*.

**The question of this row.** A seed proved at one coupling beta_0 (rows 968-977 aim at 2.3) is one inequality at one lattice size. What gives the inequality at every finer cutoff, at a size that stays bounded in physical units? Or what shows that nothing does?

**Three remarks from the statements alone (each PROVED in two lines).**

(R1) *The consumer reads only the rate.* Proposition P (a) uses m_0(iota) >= M_* a_iota and nothing else. So the hypothesis can be weakened to

(SEED-rate): there is M_* > 0 such that for every iota there is n_iota >= 3 with s_iota := S(n_iota; (2 n_iota)^3) < 1/5041 and log(1/(5041 s_iota)) >= M_* n_iota a_iota.

(SEED-phys) implies (SEED-rate) with the same M_*. (SEED-rate) allows n_iota a_iota to grow with the cutoff. Propositions P and P' hold under (SEED-rate) with the same proofs. (Compatibility of the sides, input (5) of that section, is unchanged.)

(R2) *The size test of the checked chain is not uniform in the cutoff.* K_a (a - 2) = C_beta + 3 log a, and C_beta contains log beta. By Lemma RATE the chain needs E_1 >= K_a on the seed box. If the gap is at most M_+ in physical units, E_1 <= M_+ a_iota, then with a = n_iota and n_iota a_iota <= ell_*: M_+ ell_* >= (C_beta + 3 log n_iota)(1 + o(1)), and the right side tends to infinity along any family with a_iota -> 0. So **Proposition HC as written cannot give (SEED-phys) with a bounded physical size.** The cause is its prefactor 72 beta |B|: it is the sup of the logarithm of the one-step density (Lemma HOT), a quantity that counts every lattice link of the box. The seed size that the chain gives grows like (3/M) log(1/a_iota) in physical units. By (R1) this growth is harmless for the consumer if the decay rate holds, but (SEED-phys) as stated is not reached. Approach A4 below removes the prefactor.

(R3) *Only the tail of the family matters.* Proposition P' reads sequences with a_iota -> 0. So (SEED-phys) is needed only for all but finitely many members of a sequence of cutoffs. A seed at one cutoff is neither necessary nor sufficient for it.

## Step 2. Approaches of my own (written before any route file or digest)

Notation: a_T0(beta) is the spacing that the existence chain attaches to beta (the asymptotic-freedom trajectory); c_AF = 3 pi^2/11 is the one-loop value of -d log a_T0/d beta for SU(2) with beta = 4/g^2 (RECALLED). n(beta) is the least seed size at beta, if there is one.

**A1. Exact RG transport.** A block map with a normalised kernel leaves every torus partition function unchanged. So S_beta(L n; (2 L n)^3), and the sufficient form 16 F(n^4) - F((2n)^4) of Theorem D (b), are the same numbers for the fine Wilson theory and for its blocked effective action on the coarse torus. Then (SEED-phys) says: the effective actions at one reference scale, for all cutoffs, have a seed at one bounded size. *Crux lemma (N):* a seed with margin for every limit point of the reference-scale effective actions, in a topology in which the seed functional is continuous. *First doubt:* Wilson at beta_0 is not one of these actions unless the reference coupling is beta_0 itself, and then the statement is the ladder of A2. The crude continuity bound (Step 5, Lemma G) asks for closeness of order 1/volume in the local sup norm.

**A2. Continuity ladder, the scale set by the seed.** S_beta(n; B) is continuous in beta, and Theorem S returns a strict margin after one doubling. So a seed at (beta_0, n_0) gives seeds at (beta, 2 n_0) for beta in a neighbourhood, then at 4 n_0 on a further neighbourhood, and so on. This defines beta_0 < beta_1 < beta_2 < ..., with seeds at size 2^(k+1) n_0 on [beta_k, beta_(k+1)]. *Crux lemma (NO-STALL):* beta_k -> infinity, and the climb is at least as fast as the asymptotic-freedom rate, beta_k >= beta_0 + k (log 2)/c_AF - C. *First doubt:* compact U(1) has a seed at small beta and a massless phase at large beta, so its ladder stalls. A proof has to use the group and the dimension.

**A3. A differential inequality in beta (lattice Callan-Symanzik form).** d X/d beta = -t sum_j r_j^t E_j'(beta)/(1 + S), and -E_j' is the action excess of state j over the vacuum (Hellmann-Feynman). *Crux lemma (SUM-RULE):* -E_j'(beta) <= c E_j + c' on seeded boxes, with c near c_AF. It would make the ladder steps of A2 of fixed length. *First doubt:* the bound I can prove is |E_j'| <= 2 x (number of plaquettes of a slab), too large by the volume. The statement is false wherever a gap closes at finite coupling.

**A4. Carry the rate, not the seed; make the chain cutoff-uniform.** By (R1) the consumer needs a rate. By (R2) the chain loses through its prefactor. *Crux lemma (IHC), interpolated hypercontractivity:* (HC-vac)_alpha gives X(2s + 2m; B) <= (1 - tanh(alpha m)) X(2s; B) for every start time 2s, so the prefactor 72 beta |B| can be replaced by X at a start time of fixed physical length. Then (SEED-phys) follows from two cutoff-uniform inputs: (TH) a bound on X(t_0; B) at one physical time t_0, of the kind ultraviolet stability gives, and (HC-phys) the rate alpha_iota >= M_H a_iota. *First doubt:* (HC-phys) contains the uniform physical gap; the lemma removes a loss, it does not produce the rate.

**A5. Two-scale log-Sobolev ladder.** A log-Sobolev constant for the fine vacuum law follows from one for the law of the fine field given its block averages (ultraviolet, where convexity is expected) and one for the law of the block averages (the coarse theory), by a two-scale criterion (Otto and Reznikoff; Grunewald, Otto, Villani and Westdickenberg; RECALLED). Iterate over scales. *Crux lemma (2S):* the loss per scale is summable. *First doubt:* in an asymptotically free theory the coupling between scales is of order g_k^2 of order 1/k, which is not summable. An inequality with a non-sharp one-loop coefficient loses a power of log(1/a). So the per-scale step has to be exact at one loop.

**A6. Continuum value.** By (R3), (SEED-phys) on the tail is: limsup over iota of S_iota(ell_*/a_iota; (2 ell_*/a_iota)^3) < 1/5041. This is the continuum value of a ratio of torus partition functions. *Crux lemma (C + N):* the limit exists, and it is below 1/5041 at one ell_*. *First doubt:* the existence chain controls the tr F^2 sector on a small physical torus; the thermal sum is a trace over all gauge-invariant states of a large box.

**Ranking before the fact tests.** A4 has a crux lemma that can be proved now and that changes what the lane's size test asks. A2 has a provable part (the ladder exists, with a dichotomy) and an open crux. A1, A5 and A6 name the inputs that any proof needs from the ultraviolet side. A3 is the weakest. The fact tests come next (Step 3).

## Step 3. Fact tests (before any proof attempt; one verdict per test)

Read for the definitions only: `gap-direction2-max.md` lines 229-270, `gap-assume-opus.md` line 139 (K7), `gap-pca-opus.md` line 319 (FT-FK). No run was made. Every verdict is by hand, with RECALLED facts marked.

The statement under test is (CARRY): *if the seed holds at (beta_0, n_0), then every beta >= beta_0 has a seed at some size n(beta)*, and its strong form (CARRY-AF): *with n(beta) a_T0(beta) bounded*. Each test asks: does (CARRY) hold in the model, and which crux lemma of Step 2 fails there?

| Test | Does (CARRY) hold there? | What fails in the seed | Crux lemmas that must fail there, and do | Crux lemmas that survive |
|---|---|---|---|---|
| **Free photon (FP)** | Vacuous. FP has no seed at any size or coupling: it is scale free, E_1 n stays near pi, and the continuum thermal sum of a photon gas in the box (2 ell)^3 at time ell is a fixed number of order e^(1.75) - 1 (Stefan-Boltzmann, RECALLED), far above 1/5041. | The rate: E_1 = omega_min tends to 0 like 1/side. | (HC-phys) of A4 and (N) of A1, A6 fail, as they must. | Lemma IHC of A4 holds in every mode (checked by hand below). (TH) holds. Exact RG invariance (A1) holds. So these three decide no rate, and say so. |
| **Compact U(1)** | **No.** A seed at small beta is expected (the strong-coupling expansion is group-blind; ARGUED, row 701 is for SU(2)). At large beta the theory has a massless phase (Guth 1980; Frohlich and Spencer 1982; RECALLED), and a seed implies a gap. | The gap. In the Coulomb phase E_1 is at most the lowest photon energy, of order 1/side. | (NO-STALL) of A2: the ladder exists (its proof is group-blind) and stops below the transition. (SUM-RULE) of A3. (HC-phys), (N). | Lemma IHC, the Ladder Lemma, the RG invariance: all group-blind and true. |
| **Frozen Q_8 and 2T** | **No.** At large beta a finite group freezes; the flat sectors of the periodic box are degenerate up to a splitting that tends to 0 (check 896 D6, ARGUED rate). The thermal sum counts them: S >= (number of flat sectors) - 1, roughly. 2T freezes near 2.15 to 2.2 (RECALLED), below the window point 2.3. | The count and the gap, both. | (NO-STALL), (SUM-RULE), (HC-phys), (N). | The group-blind lemmas. A finite group has no bridge gradient; Lemma IHC still holds (its proof uses only reversibility, (5.3) and Holder). |
| **SMALL-BOX** | Consistent. At fixed lattice size the seed must fail for large beta. (CARRY) lets n(beta) grow. | E_1 x side tends to 0 on a physically small box. | Any form of A2 or A3 with a step in beta that does not shrink the physical box. | The Ladder Lemma: its intervals [beta_k, beta_(k+1)] end where the seed at size 2^(k+1) n_0 ends. (HC-phys) is asked on a box of large physical size only. |
| **K7 (mixed weight, first-order line ending near (1.48, 0.90))** | **No, along a line of fixed beta_A above 0.9.** At the coexistence point two bulk phases tie; the box has two near-vacua and E_1 tends to 0 with the volume. On the line through the end point the gap closes continuously (GUIDE fact, RECALLED). Past the line a massive weak-coupling phase is expected again. | The gap at one finite coupling. | (NO-STALL) and (SUM-RULE): **any proof of them that also reads for the mixed weight is wrong.** The ladder of A2 stops at the line although seeds exist beyond it. | The tail forms A1, A4, A5, A6: K7 does not touch the limit beta_F -> infinity. This is (R3) seen in a model. |
| **FT-FK** | Not a model of (CARRY). | n/a | An A5 step that uses only the kinetic kernel of one layer decides nothing. | Lemma IHC claims no rate, so it passes by claiming nothing. A1, A2, A6 use the whole weight. |
| **Ceilings 2/3, 0.775, 1.0109** | Bind forms with a supremum over the conditioning slice. | n/a | A finite-size criterion with every boundary condition (Dobrushin-Shlosman type) as a robust form of the seed in A1. Lemma G of Step 5 uses a sup norm of the perturbation and is crude for this reason. | (HC-phys), (TH), IHC are averaged statements with no boundary slice. |

**Hand check of Lemma IHC in one Gaussian mode (PROVED).** For one photon mode of energy omega, X(t) = -log(1 - e^(-omega t)) and (HC-vac) holds with alpha = omega (Nelson). With x = e^(-2 omega s), y = e^(-2 omega m), the claim X(2s + 2m) <= (2y/(1 + y)) X(2s) reads f(x) := (2y/(1 + y))(-log(1 - x)) + log(1 - x y) >= 0. f(0) = 0 and f'(x) = y (1 - y)(1 + x)/((1 + y)(1 - x)(1 - x y)) >= 0. So it holds, and as x -> 0 the two sides differ by the factor 2/(1 + y) <= 2: the lemma is sharp up to that factor.

**What the tests decide.**

1. (CARRY) is false in three models that share every structural property of the object except the group or the weight: compact U(1), the frozen groups, and the mixed weight. So **no group-blind and no weight-blind argument carries a seed upward in beta.** The ladder from the window (A2, A3) has to cross every coupling between beta_0 and infinity, and at each one it needs a fact that is quantitative for the Wilson weight. I see no such fact. A2 keeps its provable part (the ladder and the dichotomy); its crux (NO-STALL) is marked as failing the K7 test in every structural form.
2. The tail forms pass all tests, because they claim nothing between beta_0 and the tail. By (R3) the tail is all the consumer needs.
3. **Best approach: A4.** Its crux lemma (IHC) is group-blind and claims no rate, so every test passes; it is provable; and it changes the lane's size test from K_a, which grows without bound in physical units (R2), to a number fixed in physical units. A2's Ladder Lemma is proved beside it, because it states exactly what one seed gives.

## Step 4. Duplicate check for the crux lemma (rule 0a; 23:14Z)

Searched `library/open-core.md`, the FINISH rows and `library/gap-*.md` for: interpolat, Riesz, "start time", "starting time", "tanh(alpha", SEED-rate, Stefan, "constant physics", NO-STALL, ladder, IHC, and the patterns "X(2s", "S(2s + 2m", "from any start", "from a later".

- `open-core.md`: no hit for any of these in the sense used here (4 hits of "interpolat" are block interpolation maps).
- FINISH rows: "ladder" occurs in rows 609, 610 (rim scale), 899 (finite-subgroup ladder) and 978 (this row). No row states a contraction of X from a later start time, a rate form of (SEED-phys), or the component of seeded couplings.
- Gap files: the only statements on X(2s) are (5.3) and I(U_0; U_s) <= X(2s) of row 931 (`gap-direction-max.md` L276, L344). Proposition HC starts at s = 1 only (L305-312). "seed-rate" in `gap-lsivac-check-astra.md` L102 is the size test K_a, a different thing.

No match. Lemma IHC, Corollary CU and Lemma LAD are not covered by another row. `gap-phys-seed.md` is read in Step 7, after the attack, as the row orders; if it holds any of them, Step 7 says so.

## Step 5. The attack: Lemma IHC and what follows from it

Setting of row 931 (`gap-direction-max.md` Step 5), any compact gauge group: nu is the vacuum law of a slice of the periodic box B, P the vacuum chain, self-adjoint on L^2(nu) (gauge-invariant functions), p_s(u, .) the density of P^s(u, .) with respect to nu, and (5.3): 1 + S(2s; B) = E_(u ~ nu) ||p_s(u, .)||_2^2 for integers s >= 1.

### 5.1 Lemma IHC (interpolated hypercontractivity). PROVED, group-blind, by hand; not checked by another model

**Statement.** Assume (HC-vac)_alpha on B: ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-2 alpha m), for every integer m >= 0 and every gauge-invariant h. Then for all integers s >= 1 and m >= 0:

  X(2s + 2m; B) <= theta_m X(2s; B),   theta_m := 1 - tanh(alpha m) = 2/(1 + e^(2 alpha m)) <= 2 e^(-2 alpha m).

**Proof.** Fix u. (i) p_(s+m)(u, .) = P^m p_s(u, .), by the Chapman-Kolmogorov equation and the symmetry of the densities (P is self-adjoint on L^2(nu)). The function p_s(u, .) is gauge invariant, so (HC-vac) applies: ||p_(s+m)(u, .)||_2 <= ||p_s(u, .)||_(q').
(ii) g := p_s(u, .) is non-negative with ||g||_1 = 1. Holder's inequality between L^1 and L^2: for 1 <= q' <= 2 and 1/q' = (1 - theta) + theta/2, ||g||_(q') <= ||g||_1^(1 - theta) ||g||_2^theta = ||g||_2^theta. Here theta = 2 (q' - 1)/q' = 2 e^(-2 alpha m)/(1 + e^(-2 alpha m)) = theta_m, and 0 < theta_m <= 1.
(iii) So ||p_(s+m)(u, .)||_2^2 <= (||p_s(u, .)||_2^2)^(theta_m). Average over u ~ nu. The map x -> x^theta is concave for 0 < theta <= 1, so by Jensen E_u ||p_(s+m)(u, .)||_2^2 <= (E_u ||p_s(u, .)||_2^2)^(theta_m).
(iv) By (5.3) this is 1 + S(2s + 2m) <= (1 + S(2s))^(theta_m). Take logarithms. QED

**Remarks (each PROVED in a line).**
- s = 1 returns Proposition HC with a slightly better constant: X(2) <= log sup p_1 <= 36 beta |B| (Lemma HOT), so X(2m + 2) <= 72 beta |B|/(1 + e^(2 alpha m)).
- Odd times: S is non-increasing in t, so X(t) <= X(2 floor(t/2)).
- Necessity of the rate, as in Lemma RATE (c): if X(2s + 2m) <= C e^(-2 alpha m) for all m then E_1(B) >= alpha. So Lemma IHC changes the constant in front and never the rate.
- Sharpness: in one Gaussian mode the two sides differ by at most the factor 2/(1 + e^(-2 alpha m)) (Step 3).
- A finer start value (ARGUED, not used): as q' -> 1 the Renyi divergence of order q' of p_s(u, .) tends to its relative entropy, so for large m the factor X(2s) can be replaced by about the mutual information I(U_0; U_s) <= X(2s).

### 5.2 Corollary CU (the chain, uniform in the cutoff). PROVED implication

Let iota range over a family of cutoffs (beta_iota, a_iota). Fix a physical length ell and a physical time tau_0 < ell. Put n = n_iota with n a_iota = ell (or the nearest integer above), B = (2n)^3. Assume:

- **(TH)** there is Theta < infinity, independent of iota, and for each iota an even integer t_0 <= tau_0/a_iota with X_iota(t_0; B) <= Theta;
- **(HC-phys)** there is M_H > 0, independent of iota, such that (HC-vac)_alpha holds on B at beta_iota with alpha >= M_H a_iota.

Then X_iota(n; B) <= 2 Theta e^(-M_H (ell - tau_0 - a_iota)) for every iota. So (SEED-phys) holds with s_* and ell_* = ell (ell_* = ell + sup a_iota if n is rounded up) as soon as

  (SIZE-phys)   M_H (ell - tau_0 - a_iota) >= log(2 Theta/log(1 + s_*)).

Proof. Lemma IHC with 2s = t_0 and 2s + 2m = 2 floor(n/2) >= n - 1, then monotonicity in t. QED

**Where (TH) comes from (PROVED implication).** Suppose two-sided stability holds with one bulk constant: there are e_iota and c_F with |log Z_iota(B x t) - e_iota |B| t| <= c_F |B| t (a_iota/a_*)^4 for all t >= t_0, the volume |B| t counted in lattice sites. Then X(t_0; B) = log Z(B x t_0) - t_0 lim_(t') (1/t') log Z(B x t') <= 2 c_F |B| t_0 (a_iota/a_*)^4, which is 16 c_F ell^3 tau_0/a_*^4 in physical units: (TH) with Theta polynomial in ell. With such a Theta, (SIZE-phys) holds for every large ell, since its left side is linear in ell and its right side is logarithmic.

**What changes for the lane.** The size test "m_0++ >= K_a" of row 974, K_a = (C_beta + 3 log a)/(a - 2), becomes: gap >= M_H >= K_phys(ell) := log(2 Theta(ell)/x_*)/(ell - tau_0), in physical units. K_phys does not depend on the cutoff. K_a times the physical seed size grows like 3 log(1/a_iota) + log beta_iota (R2). The price is the input (TH): at a fixed coupling it needs a bound on the thermal sum at one earlier time that is better than Lemma HOT, and I have none at beta 2.3 (OPEN there). In the limit it is the two-sided form of ultraviolet stability, an interface statement of the existence chain (CT4 of GOAL.md is its lower half).

### 5.3 Lemma LAD (what one seed gives, exactly). PROVED GIVEN Theorem S, group-blind

Let G := { beta > 0 : S_beta(n; (2n)^3) < 1/5041 for some integer n >= 3 }. For s_* < 1/5041 let n(beta; s_*) be the least n >= 3 with S_beta(n; (2n)^3) <= s_*.

(a) beta -> S_beta(t; B) is continuous for each box. (Z_beta(B x t) is an integral of a continuous bounded weight; lambda_0(beta) is the operator norm of the positive self-adjoint R_beta, and R_beta is norm continuous in beta because its kernel is uniformly continuous in beta on a compact space.)
(b) G is open. (A strict inequality and (a).)
(c) n(beta; s_*) is finite on G and locally bounded there. (Let beta in G with a seed of value s at n. Take r with (5041 s)^(2^r)/5041 < s_*. Theorem S gives S_beta(2^r n) < s_*, strictly; by (a) this holds near beta.)
(d) Let (beta_-, beta_+) be the component of G that contains beta_0. If beta_+ < infinity, then S_(beta_+)(n; (2n)^3) >= 1/5041 for every n >= 3, and n(beta; s_*) -> infinity as beta increases to beta_+. (The first claim is beta_+ not in G. For the second: if n(beta_j; s_*) = n along a sequence beta_j -> beta_+, then by (a) S_(beta_+)(n) <= s_* < 1/5041, so beta_+ is in G.)
(e) With the unit a_seed(beta) := 1/n(beta; s_*), (SEED-phys) holds on every family inside (beta_-, beta_+), with ell_* = 1, by definition. For another unit a(beta): (SEED-phys) holds on a family inside the component if sup over iota of n(beta_iota; s_*) a(beta_iota) is finite; and if (SEED-phys) holds with (ell_*, s_*) then n(beta_iota; s_*) a(beta_iota) <= ell_*.

So: **(CARRY) is the statement beta_+ = infinity, and (CARRY-AF) is sup over beta >= beta_0 of n(beta; s_*) a_T0(beta) < infinity.** One seed gives the open set (b) and nothing on its size. The ladder of A2 is the proof of (c). In compact U(1), in the frozen groups and on K7 lines the lemma holds and beta_+ is finite (Step 3).

### 5.4 Lemma G (how far continuity alone reaches). PROVED GIVEN the trace formula and (K1), (K2) of `gap-seed-limit.md` Section 1

For the Wilson weight exp(beta sum_p P_p), |P_p| <= 1: d X_beta(t; B)/d beta = sum over the 6 |B| t plaquettes of B x t of [<P_p>_(B x t) - <P_p>_(B x infinity)], and each bracket is at most 2 S(t - 1; B)/(1 + S(t; B)) in absolute value. So |d X/d beta| <= 12 |B| t S(t - 1; B).

Proof. log Z is differentiable with derivative the sum of <P_p>; lambda_0 is a simple isolated eigenvalue of an analytic family, and the derivative of (1/t') log Z(B x t') converges to that of log lambda_0 (convex functions with a differentiable limit). For one plaquette F = P_p of time width w <= 1: <F>_(B x t) = [<Omega, k_F Omega> + Tr(Rx^(t - w) k_F)]/(1 + S(t)), |Tr(Rx^(t - w) k_F)| <= S(t - w) by (K1), and <Omega, k_F Omega> = <F>_(B x infinity) by (K2). QED

Reading. On the seed box |B| t = 8 n^4. A seed with margin survives a change of beta of order (margin)/(96 n^4 S), where the truth, if masses scale, is a change of order one (a factor in the scale). The bound loses the volume because it charges every plaquette the full thermal weight, where a state of a few particles has an action excess of order one in total (A3's sum rule). With this bound the steps of the ladder are summable, like 16^(-k). So **continuity alone climbs a finite distance in beta.** This is the exact place where A2 and A3 stop.

### 5.5 Where the attack stands

- Crux lemma of A4, Lemma IHC: **PROVED.** Corollary CU: PROVED implication. Lemma LAD, Lemma G: PROVED GIVEN the named inputs.
- (SEED-phys) is **not** proved. After Corollary CU it rests on (TH) (ultraviolet, an interface statement of the existence chain, OPEN there) and on (HC-phys), which by Theorem BR is: the bridge inequalities (LSI-br)_s on the box of physical side 2 ell hold with (1/2) integral of alpha_s ds >= M_H a_iota, uniformly in the cutoff. (HC-phys) contains the uniform gap. It is OPEN, and a result at beta 2.3 is one member of the family, not on its tail.
- (HC-phys) is the right shape in the one case I can do by hand: a free field of mass M on the lattice satisfies it with M_H equal to the lowest mode energy over a_iota, which tends to M (Nelson's bound mode by mode; the modes are independent). PROVED for that model; it says nothing on SU(2).

### 5.6 Two more consequences of Lemma IHC ((a) PROVED, (b) ARGUED; added 23:19Z)

**(a) The lemma needs the inequality on trajectories from the start time only.** The proof applies (HC-vac) to the functions p_s(u, .), u in the slice space, and to nothing else. So with

(HC-traj)_(alpha, s): ||P^m p_s(u, .)||_2 <= ||p_s(u, .)||_(1 + e^(-2 alpha m)) for nu-almost every u and every m >= 0,

the conclusion X(2s + 2m) <= theta_m X(2s) holds. Proposition HC is the case s = 1 (row 970, 7.1, noted that it reads only p_1(u, .)). For s at a fixed physical time the functions p_s(u, .) are the kernels after that time: the roughness at the lattice scale is gone. So (HC-phys) can be asked in this weaker form.

**(b) A necessary condition in infinite space (thermodynamic form; ARGUED).** Let pi(t) := lim over cubes B of X(t; B)/|B|, the thermal pressure over the temperature at time extent t in lattice units (the limit exists by sub-additivity of the kind of Proposition Delta; not rebuilt). If (HC-vac)_alpha holds on all large cubes with one alpha, then pi(t + 2m) <= (1 - tanh(alpha m)) pi(t) for even t. So a rate alpha is refuted by any two time extents with pi(t + 2m)/pi(t) > 1 - tanh(alpha m).

- Local form (small steps, read in the continuum): alpha <= -2 d log pi/dt = 2 T eps/p at T = 1/t, with eps the energy density and p the pressure (from d(p/T)/dT = eps/T^2). Where eps >= 3p and T >= T_c (RECALLED: the interaction measure is positive), the right side is at least 6 T_c. In the confined range it is about 2 m_0++. So a rate up to the gap passes the local form if m_0++/T_c <= 6 (RECALLED value: about 5.2).
- Finite steps with the idealised law pi ~ t^(-3) up to the critical extent N_c, alpha = r/N_c, 2m = x N_c, t + 2m = N_c: the test reads g(x) := log(2/(1 + e^(r x))) - 3 log(1 - x) >= 0. At r = 5.2 the interior minimum is +0.012 (near x = 0.3); it is negative from r = 5.25 on (`guide/lane978/arith978.log`; hand check at r = 5.2, x = 0.3: -1.058 + 1.070). The true pressure near N_c is far below the idealised one (ARGUED), and that gives room.

Reading: thermodynamics does not refute a hypercontractive rate up to the gap, but with the idealised law it is close. A comparison with published SU(2) pressure data would give an upper bound on M_H/m_0++; it is a GUIDE item, proposed and not run.

### 5.7 Corollary CU in the lane's letters, and a fact test for any proof of (HC-phys) (added 23:24Z)

**Corollary CU with (APR) (PROVED implication GIVEN Proposition Delta, checked row 709).** Proposition Delta: g(a; b^3) <= (b/a)^3 Delta(a^4) for integers b >= a >= 3. (APR) of row 720, Proposition MB: D(L_0/a_iota; beta_iota) <= A for the symmetric torus of physical side L_0, for every member of the family. So X(L_0/a_iota; (2n)^3) <= (2 ell/L_0)^3 A: this is (TH) with tau_0 = L_0 and Theta = (2 ell/L_0)^3 A (L_0/a_iota even). Hence

  **(APR) and (HC-phys) give (PHYS-SEED)**, at every half side ell with M_H (ell - L_0 - a_iota) >= log(2 (2 ell/L_0)^3 A/log(1 + s_*)).

Compare Corollary MB1 of row 720: (BASE-Phi), (MONO-Delta) and (Z-UNB) give (PHYS-SEED), with (APR) as a side input. Here (APR) is the only input from the ultraviolet side, and it is the one that row 720 derives from the account (1.1.5 (iii); a conditional, checked in row 727, with assumptions (a), (b) named in Step 7).

**The square-root test (PROVED for one Gaussian mode; a test, not a step).** Take one photon mode of energy omega, in the flat model of rows 931 and 941. Its slice law nu has precision 2 beta sinh(omega) (row 931, Step 5: gamma = 2 beta sigma with sigma = sinh omega). The four-dimensional Gibbs law of the same mode has the quadratic form beta (2 - 2 cos p + 2 cosh omega - 2) at time frequency p, so its smallest Hessian eigenvalue is 4 beta sinh^2(omega/2). A log-Sobolev or Poincare inequality of the four-dimensional law, restricted to functions of one slice, therefore gives the slice constant 4 beta sinh^2(omega/2) at best, where the truth is 2 beta sinh(omega). Put into Theorem BR as a constant lower bound for alpha_s on (0, 1/beta), it returns the rate A/2 = 2 sinh^2(omega/2), about omega^2/2, where the exact rate is omega (`gap-fc-max.md` 5.4). (That the bridge laws nu_s inherit no better constant from a space-time law is ARGUED: the constant test vector has Rayleigh quotient of order beta (2 cosh omega - 2) in the space-time form with one refined step.) With omega = M a_iota this is the physical rate M^2 a_iota/2, which tends to 0 with the spacing. So **any proof of (HC-phys) that passes through an inequality for the four-dimensional measure in the link metric (stochastic quantisation, a Bakry-Emery or Polchinski bound for the full lattice law) and then restricts to a slice gives rate zero in physical units.** The square root has to come from the transfer structure, as it does in Theorem BR (bridge laws between two slices) and in Nelson's bound. At beta 2.3 the loss is invisible (2 sinh^2(omega/2) = 0.97 against K_30 = 0.81 for omega = 1.3), so a method can pass in the window and fail on the tail for this reason alone. Route Z met the same power on periodic tori ("a lattice mass of order a^2", `gap-skeleton-final.md` 4.2).

**The defective form (PROVED; three lines), and why it is not a shortcut.** Assume only hyperboundedness with a defect: ||P^m h||_2 <= e^D ||h||_(1 + e^(-2 alpha m)) on the kernels p_s(u, .). The proof of Lemma IHC gives X(2s + 2m) <= 2D + theta_m X(2s). Then, for T >= t_1 := 2s + 2m, S(T) <= e^(-E_1 (T - t_1)) S(t_1) (each r_i <= r_1; this is the step of Lemma Z, row 720). So with m such that theta_m Theta <= 1, the seed at time n follows from E_1 (n - t_1) >= 2D + 1 + log(1/s_*). In words: a defect D that does not grow with the box turns the extensive start value into a bounded thermal sum, which is the half (BDD-Delta) of row 720's Theorem ZD, and the gap half (Z-UNB) does the rest. This is the exact link between B11's crux (HC) and Theorem ZD. It is not a shortcut: a defect that comes from a lower bound on a local energy is additive over the sites of the box, and with D of the order of the volume the condition asks E_1 n above the volume. So the defect has to be free of the volume, and that is again a statement at the scale of the correlation length.

## Step 6. Second and third routes: not needed

The crux lemma of the best approach was proved at the first route (5.1). The stop rule of the row is met. No second or third route was run.

## Step 7. Prior work, read after the attack: what is already there, per approach

**Read in this step.** `gap-phys-seed.md` (row 720): header, Sections 0, 1, 2, 3.2, 3.4, 4, 5.1, 5.2 (lines 1-250, 340-437); its check `gap-phys-seed-check.md` (row 727, Claude Opus 5.5 high; lines 1-22, 42-54, 84-94): no statement fails; 1.1.5 (iii) HOLDS as a conditional, with two assumptions that stay unchecked there, (a) the vacuum number V of (ST5) is the vacuum energy E_m of CA-II 141374-141386 with the same normalisation of Z, (b) delta_vac-bar is uniform in the cutoff, and with the remark that the unit of the account (first passage) must be the unit of the trajectory; Corollary MB1 HOLDS AFTER CORRECTION, it needs (APR); Proposition 1.1 holds as a comparison of sizes only ("that no other argument from (UV-Z) gives the seed is not proved"). `gap-mid-max.md` (rows 708, 709): lines 48-60 and Section 5.1. `gap-skeleton-final.md` Section 4.2 (Route Z) and lines 125-127. `gap-ymcons-opus.md` (row 975) Approach 10. The RESULT lines of FINISH rows 931-977. The account of Sussman and Alpoge only through the lane's index (`sa-index/chunk-04.md`, `chunk-06.md`) and the quotations in rows 720 and 975; **the tex itself was not opened in this run**, and no proof of the account was read.

**Where the account's control ends (from those quotations).** The unit of length is the first-passage scale: the scale at which the running inverse coupling first enters the window [g^(-2), g^(-2) + B_sharp] (outline lines 6854-6861, index `chunk-06.md` row 6854). The existence of the recursion "through first passage" is itself a named open requirement, E1 (outline 4197-4205, index `chunk-04.md`). The tori have four equal sides l = 2 L^m above the floor l_*(g) (outline 21521-21532); "No step of the account integrates the scales between 1 and l" (row 720, 1.1.1). The partition function is controlled as (UV-Z): V - C_- l^4 <= log Z <= V + C_+ l^4 (outline 23778-23787; Balaban's stability theorem as cited at CA-I 4209-4240, with all effective couplings in (0, gamma]). The account applies only for beta >= g^(-2) + B_sharp (row 975, quoting outline 23378). It claims no gap and no exponential decay (row 700, Section 0). So the window point 2.3 is not a lattice of the account's family, and every lattice of the family is at weak bare coupling.

| My approach | Already in the lane? | Where | What is new here, if anything |
|---|---|---|---|
| A1 exact RG transport, and A6 continuum value | **Yes.** | Row 697 Section 5 (scaling form); row 720 (PHYS-SEED), its Class I candidates and Part 4; (UNIV-K) and Lemma ONE-K (rows 904, 913, 916, 924); CUTOFF-COMPARE with (CC) (row 975, Approach 10: "a bridge that fails", on precision) | Nothing. Named as a match; not attacked. |
| A2 continuity ladder; Lemma LAD; (NO-STALL) | **Yes.** Lemma LAD (a), (b), (d) is **Theorem CRIT** of row 709 (`gap-mid-max.md` 5.1) at the shape r = 2; (NO-STALL) is **(NOCRIT)**. | rows 708, 709; Proposition NM of row 720 | Only (c) and (e): local boundedness of the seed size, and the form (CARRY-AF) = sup n(beta; s_*) a_T0(beta) < infinity. By rule 0a, (NOCRIT) is not attacked here. Lemma LAD is kept in 5.3 as a restatement with this credit. |
| A3 differential inequality; (SUM-RULE); Lemma G | **Yes.** (SUM-RULE) is **(VIR_K)** with Theorem TR (row 708, C-A: "the missing line is the bound of the action deficit of an excited state by its energy"); idea 46 of `gap-brainstorm-max.md`. Lemma G is its Lemma 4.2 with the trivial bound. | row 708; row 710 Theorem U | Nothing. Named as a match; not attacked. |
| A4 rate, not seed; Lemma IHC; Corollary CU | **Partly.** Proposition HC (row 931) is the case s = 1. The start-time idea with the gap in place of hypercontractivity is **Lemma Z** of row 720: S(T; b^3) <= (e^((b/T_0)^3 D(T_0)) - 1) e^(-(T - T_0) m). (TH) is **1.1.5 (iii)** of row 720: g(n; b^3) <= (b/n)^3 (C_+ + C_- + delta) l^4, from (UV-Z), the torus-independence of the vacuum density (CA-II 141374-141386) and Proposition Delta. | rows 931, 720 | **New:** Lemma IHC (a contraction of X, not of S, from any start time), Corollary CU, (SEED-rate), remark (R2), and the two items of 5.6. See below for why this changes row 720's Proposition 1.1. |
| A5 two-scale log-Sobolev ladder | **Named, not developed.** | `gap-crux-fp.md` L233 and `gap-crux-exercise-astra.md` L532 (Polchinski flow and two-scale criteria: "a Hessian bound at every scale is needed; it would not tell U(1) from SU(2)"); row 968 Proposition FLOW (the Polchinski flow of each bridge marginal) | The remark that an iterated two-scale step loses a factor 1 - c g_k^2 per scale, which is not summable in an asymptotically free theory (ARGUED). Not attacked. |
| Carry by decimation inequalities (Migdal-Kadanoff bond moving; considered, not listed in Step 2) | **Yes.** | WALL G of `gap-brainstorm-max.md` L257 and item 16 of `gap-brainstorm2-max.md` (Tomboulis; the objection of Ito and Seiler, recalled there): bond moving bounds Z, not the ratio that the seed reads | Nothing. |
| Route Z (the lane's own carrier in beta) | n/a | `gap-skeleton-final.md` 4.2: a zero-free domain in complex beta carries a gap from the strong-coupling disc; on periodic tori it gives a lattice mass of order a^2, zero in physical units; crux (ZF_B), open | It is a carry from strong coupling to a fixed beta. It is not a carry to finer cutoffs at a physical rate, by its own correction. |
| Rows 931-977 | n/a | All of them work at a fixed coupling 2.3 to 2.6 on the seed box: (LSI-vac), (HC-vac), (E-to-HC), (FC), (SC), (SG-step), (LSI-J-seed), (LSI-br-seed), (LSI-traj-seed), tilt covariances. None states a cutoff-uniform form. Row 974 finds that the needed a rises with beta (refuted for a up to 44 at 2.6), which is (R2) seen in the data. | (R2) says why, and that it does not stop. |

**What the new part changes in row 720.** Proposition 1.1 there: the account's bound is "short of the seed by the number of unit cells". (Its check, row 727, already notes that this is a comparison of sizes and that "no other argument from (UV-Z) gives the seed is not proved".) Lemma Z needs (gap) x (time) above that extensive number, so Theorem ZD asks for a bounded Casimir free energy, (BDD-Delta), an infrared statement. With Lemma IHC the same extensive bound is enough as a start value, because hypercontractivity contracts X = log(1 + S) and not S: the number of unit cells enters through its logarithm. In formulas, with the account's torus side l as the start time, tau_0 = l, and Theta = 8 C ell^3 l from 1.1.5 (iii) (C = C_+ + C_- + delta, lengths in the account's unit):

  (PHYS-SEED) holds at the half side ell as soon as M_H (ell - l - a_iota) >= log(16 C ell^3 l/log(1 + s_*)).

So: **(SEED-phys) follows from the account's own stability statements (under its packages; unchecked here) and (HC-phys). No bounded Casimir free energy, no monotony and no base value is asked.** The whole open content is (HC-phys), in the trajectory form of 5.6 (a) if wished. It is stronger than a uniform gap; whether the seed implies it back is not known to me.

Credits for this section: Sussman and Alpoge, with Claude and Codex as authors of their text (the account, (UV-Z), the first-passage unit, the density statement); Balaban (the stability theorem behind (UV-Z)); row 720 (Claude Fable 5.2: 1.1.5, Proposition 1.1, Lemma Z, the comparison models) and its check, row 727 (Claude Opus 5.5); rows 708, 709 (Theorem CRIT, (NOCRIT), (VIR_K), Theorem TR); row 931 (Proposition HC, (5.3)); rows 947, 949 (Theorem BR and its check); row 974 (Lemma RATE); row 975 (CUTOFF-COMPARE); Gross and Nelson (hypercontractivity; the interpolation step is Holder's inequality).

**One more match, found on a last duplicate check for (HC-phys) (23:21Z).** `gap-skeleton-max.md` L190-195, item B11 with crux (HC): "a defective logarithmic Sobolev inequality for the lattice Hamiltonian on T^3_l in its ground-state representation, with constants uniform in the lattice spacing, and a uniform positivity-improving bound", proposed there for the gap of a *small* torus, and judged: "the time-zero fields of a four-dimensional gauge theory are too singular for a time-zero measure in the continuum; the inequality must be formulated on slabs, and its uniformity is a problem of the size of the existence proof." (HC-phys) is the tight form of that crux, with a rate, on the large box. It is not in `open-core.md` and no FINISH row attacks it (grep: HC-phys, "hypercontractiv" with "cutoff"; one literature row, 747). I name the match and do not attack it. The caution of B11 stands for (HC-phys): it is a family of inequalities at finite cutoff with one constant, and no limit of the slice laws nu_iota is used or claimed.

## Step 8. Verdicts, what stays open, and the next step

### 8.1 Verdicts on the question of the row

1. **What carries a seed proved at one coupling to every finer cutoff? Nothing that I found, and nothing in the lane.** The carry is the statement beta_+ = infinity of Lemma LAD, which is (NOCRIT) of row 709, together with a climb at the asymptotic-freedom rate. Its two exact forms are already named open: (NOCRIT) and (VIR_K) (rows 708, 709); on the account's side (UNIV-K) and (CC) (rows 904, 916, 924, 975). By rule 0a none of them was attacked here.
2. **What shows that it cannot? Not a theorem; three tests and one fact of scope.** (CARRY) is false for compact U(1), for the frozen finite groups and on the mixed-weight lines of K7, where every group-blind and weight-blind lemma of the object holds. So an argument that carries the seed must use a quantitative property of the Wilson weight at every coupling above beta_0. And by (R3) with Step 7: the lattices of the existence chain all lie at weak bare coupling, beta >= g^(-2) + B_sharp; the point 2.3 is not one of them. A seed at 2.3 is a theorem about one lattice theory. It enters the continuum statement only through the carry.
3. **What the continuum statement needs in place of a carried seed (new, PROVED as an implication).** Lemma IHC and Corollary CU: (SEED-phys) follows from the stability bounds that the account states for its own tori, used as a start value at the time l, and from (HC-phys), hypercontractivity of the vacuum chain at a rate M_H a_iota on the box of physical side 2 ell, in the trajectory form (HC-traj). The size test becomes (SIZE-phys), fixed in physical units. The lane's present size test K_a is not: it grows like 3 log(1/a_iota) + log beta_iota in physical units (R2).
4. **The consumer can be served by less.** (SEED-rate) of (R1) is enough for Propositions P and P'.

**Kind of result.** A proof of new implications inside this target's gap lane (Lemma IHC, Corollary CU), and a direction verdict. It is not a check of the account's proofs and not a correction of its text. The account asserts no gap; it is used only as the source of the start value (TH).

### 8.2 Marks

| Statement | Mark |
|---|---|
| (R1) (SEED-rate) suffices for Proposition P, P' | PROVED (two lines, from the proof of Proposition P as written) |
| (R2) the size test K_a is not uniform in the cutoff | PROVED GIVEN Lemma RATE and a bound E_1 <= M_+ a_iota on the gap from above (not proved here; an upper bound on a gap is a variational statement) |
| (R3) only the tail of the family is read | PROVED (from the statement of Proposition P') |
| Lemma IHC, with remark 5.6 (a) | PROVED, group-blind, by hand; not checked by another model |
| Corollary CU; (TH) from two-sided stability with one bulk constant | PROVED implications |
| (TH) from the account, as in row 720, 1.1.5 (iii) | PROVED GIVEN (UV-Z), the density statement and Proposition Delta; checked as a conditional by Claude Opus 5.5 (row 727), with its assumptions (a) V = E_m in one normalisation, (b) delta_vac-bar uniform in the cutoff, both unchecked; the account's statements are conditional on its packages |
| Lemma LAD | PROVED GIVEN Theorem S; its parts (a), (b), (d) are Theorem CRIT of row 709 |
| Lemma G | PROVED GIVEN the trace formula, (K1), (K2); it is Lemma 4.2 of row 708 with the trivial bound |
| 5.7: the defective form X(2s + 2m) <= 2D + theta_m X(2s) and its link to Theorem ZD | PROVED implication (unchecked) |
| 5.7: Corollary CU with (APR); the square-root test in one Gaussian mode | PROVED implication GIVEN Proposition Delta (checked, row 709); PROVED for the Gaussian mode, its reading for SU(2) ARGUED |
| 5.6 (b), the thermodynamic necessary condition | implication ARGUED (the limit pi(t) is not rebuilt); the numbers are RECALLED |
| Fact-test entries on U(1), the frozen groups, K7 | RECALLED or GUIDE, as marked in Step 3 |
| (HC-phys); (NOCRIT); (VIR_K); (UNIV-K); (SEED-phys) | OPEN |

### 8.3 What this run did not cover

(1) The tex of the account was not opened; its lines are cited through the lane's index and through rows 720 and 975. No proof of the account was read. (2) No numeric run was made; the numeric lock was never taken. (3) Nothing here is checked by another model. (4) (TH) rests on row 720, 1.1.5 (iii): checked as a conditional (row 727); its assumptions (a), (b) and the account's packages are not checked. (5) Whether (HC-phys) is true for SU(2) is not known to me; the only models where I verified it by hand are free fields (Nelson, mode by mode). (6) Whether the seed implies (HC-phys) back is open. (7) The compatibility of the seed sides with the account's tori (input (5) of `gap-seed-limit.md` Section 5) is untouched. (8) A5 was not attacked.

### 8.4 Next step (each item is a complete brief)

**N1, check (another model, high effort).** Check line by line `library/gap-ladder-max.md` 5.1 (Lemma IHC), 5.2 (Corollary CU and the derivation of (TH)), 5.6 (a) and 5.7. `gap-phys-seed.md` 1.1.5 (iii), which supplies (TH), is already checked as a conditional (row 727); what is left there is its two assumptions, (a) V = E_m in one normalisation of Z and (b) delta_vac-bar uniform in the cutoff, to be read in the account. Verdict per statement. Moves: the reduction "(SEED-phys) from the account plus (HC-phys)".

**N2, direction then proof (Claude Fable 5.2, max): (HC-phys) on the lattices of the account.** Statement: for first-passage data of the account, on the cube of physical side 2 ell, (HC-traj)_(alpha, s) holds with 2 s a_iota = l and alpha >= M_H a_iota. By Theorem BR it is enough to have the bridge inequalities (LSI-br) on the bridge interpolations of P^k p_s(u, .). First, a port question (rule 9): which convexity of the fluctuation action at each scale below the unit do the account's small-field statements give, and in which norm. Second, write the inequality that is left at the unit scale, where the coupling is g, on the box of e^(c/g^2) unit cells; this is the order-one input. Fact tests to pass before any proof: FP and compact U(1) must fail it through the rate only; the weights w_p of row 720 (M3) show that the unit-scale inequality must use the distance of the effective weight from the Wilson weight; a per-scale loss of order g_k^2 must be exact at one loop or it costs a power of log(1/a) (A5); the square-root test of 5.7 (no step through an inequality of the four-dimensional law in the link metric). Stop rule as in this row.

**N3, for the rows at fixed coupling (968 to 977).** Lemma IHC lets Proposition HC start at any even time 2s: the prefactor 72 beta |B| becomes 2 X(2s; B), and (HC-vac) is needed on the kernels p_s(u, .) only. It helps at a fixed coupling only with a bound on X(2s; B), s >= 2, better than Lemma HOT. One candidate is row 720's Lemma Z': g(T_0; (rho T_0)^3) <= (2/rho) Phi_rho(T_0). No such bound is known at beta 2.3; this is a small open item, not attacked here.

**N4, for the lead (I may not edit other files).** `gap-seed-limit.md` Section 5 can state (SEED-rate) beside (SEED-phys); evidence is (R1). `gap-phys-seed.md` Proposition 1.1 can point to Corollary CU: the account's bound is short of the seed by the number of unit cells for the gap route (Lemma Z), and by its logarithm for the hypercontractive route.

**N5, GUIDE, optional (reading, no simulation).** From published SU(2) thermodynamics (pressure and energy density against T/T_c), evaluate the test of 5.6 (b): the largest alpha/m_0++ with pi(t + 2m) <= (1 - tanh(alpha m)) pi(t) on the measured range. Criteria before reading: REFUTES a rate M_H if one pair of temperatures violates the inequality by more than twice the quoted error; otherwise it gives an upper bound on M_H/m_0++ and decides nothing else. It can only lower the M_H that N2 may aim at.

RESULT: Row 978 (Claude Fable 5.2 max, Mac mini worker 3; author, checked by no one; no numeric run). No carrier of a seed from one coupling to finer cutoffs was found: the carry is (NOCRIT) of row 709 plus an asymptotic-freedom climb, it is false for compact U(1), the frozen groups and K7 lines, and beta 2.3 is not a lattice of the account's family (all at weak bare coupling), so a seed there reaches the continuum statement only through that open carry. PROVED by hand (group-blind, unchecked): Lemma IHC, (HC-vac)_alpha gives X(2s + 2m; B) <= (1 - tanh(alpha m)) X(2s; B) from every start time 2s, needing the inequality only on the kernels p_s(u, .); Corollary CU, (SEED-phys) follows from the account's stability bounds as a start value at its torus time (row 720, 1.1.5 (iii), a conditional checked in row 727, under the account's packages) and (HC-phys), a hypercontractive rate M_H a_iota uniform in the cutoff, with the size test (SIZE-phys) fixed in physical units; (R1) the consumer needs only (SEED-rate); (R2) the lane's size test K_a grows like 3 log(1/a) + log beta in physical units, so Proposition HC as written cannot give (SEED-phys) at a bounded physical size. Already in the lane, named and not attacked: Lemma LAD = Theorem CRIT, (SUM-RULE) = (VIR_K), RG transport = (UNIV-K)/(CC), (HC-phys) near B11's crux (HC). OPEN: (HC-phys) (the one statement the new reduction rests on), (NOCRIT), (VIR_K), (UNIV-K), (SEED-phys). Next: N1 check of IHC and CU; N2 direction on (HC-phys) for the account's lattices.
