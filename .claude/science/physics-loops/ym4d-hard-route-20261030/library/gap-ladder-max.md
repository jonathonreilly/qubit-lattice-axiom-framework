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
- 23:25Z. Step 1 written (goal and object, read narrowly). Step 2 written (six approaches of my own).

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
