lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T08:47Z

# Joint induction: two-step kill test (mapped side)

Pinned at commit f27f268c4. Status: **FINAL** for this item.

Provenance: anthropic/claude-opus-5-5, effort max, Mac mini worker, fresh session. Side: mapped. Same-model work: not independent and not an audit. Labels are this repo's (gap, unchecked, implication, discharged); nothing here grants status. Firewall kept: `parts/hard-core--independent*.md`, gates on that attempt, `library/shelling-by-hand.md`, `library/adapted-domains.md`, `gates/history-budget-*`, `gates/compute-inventory-*` not opened. `gates/strategy-codex-b5251ab07.md` was not opened either: it reads both attempts, so I treated it as a gate on the independent attempt and worked from the queue row alone. If that gate gives "flat, commuting quadratic limit" a narrower meaning than section 2 here, the lead should say so.

## Verdict

| Registered criterion | Result, on the actual recipe of Lemma 14.16 |
|---|---|
| (N) nondecaying term in law, far difference or second moment | **Not found.** In the flat quadratic limit the current vanishes identically on every chart (Theorem G0). At first order it is an exact, chart-free current, quadratic in the flux and decaying in n (Theorem F1) |
| (C) coercivity lost with depth | **Not found.** Chart gap monotone in the constraints, exact (Prop W1). Inf-sup constant in the d = 2 model flat in depth, 0.2147 to four depths (run) |
| (S) source K3 assuming output K3 | **Not found.** Every K3 row reads level j, Pass H, or a deterministic bound (section 1) |
| Same-level input with no prior supplier | **Yes. STOP at D1:** Theorem F-D is written for one jump only; two jumps are first read at the second step |

**So the kill test does not kill the invariant, and the induction does not close.** No inequality failed. The stop is an unsupplied statement, not a counterexample. I wrote no new induction around it. The flat limit is weak evidence for the full theory: section 7 lists what it cannot see, and the two highest-risk items there are out of its reach.

The "joint" induction is not joint. By grep and by reading, H(k) reads nothing from the K-class; every reference runs consumer-ward. So it is two passes in sequence, and the K-class at level j reads the hard core up to K, since LL_j has tops up to K.

## 1. Dependency diagram, ordered by (level, stage)

Status: **E** exact or elementary. **A** gated ADVANCE. **P** proof text, ungated. **D** supplier with a gated defect, or a named gap. **U** no supplier at all.

**Pass H, the hard core, level k. Reads nothing from Pass C.**

| Stage | Output | Same-level inputs | Supplier | Status |
|---|---|---|---|---|
| C_k | CA_k, R3_k, non-concentration | level k - 1 | `relative-density-bound.md` (f') | P |
| BC1_k | Theorem F, one-jump F-D, (NC) | R3_k at class fields | `fibre-propagator.md` | P |
| **BC2_k** | **F-D on two or more jumps** | (NC), level-by-level inf-sup, commutators | **none** | **U, read from k = 1** |
| Dat_k | Lemma ST, (Resp+), (J+), (QD) | BC1; BC2 once lower data sit on a patch | `energy-by-stages.md` 7, induction on bricks | P, inherits U |
| En_k | AE-T, AE-R, AE-S, W2, W1 | Dat_k, (LIFT-1) | `energy-by-stages.md` | P |
| Z_(k+1) | Theorem Z | I_k, Z_k, DM_k, En_k, (LNC) | `quiet-boundary-rarity.md` | D, (LNC) gap |
| Base_k | chart, (H1)-(H3), HS-T | BC1, BC2, R_k | closure 3, `preconditioned-covariance.md` | P, inherits U |
| Gas_k | (A1'), (A2), gas | Z_(k+1), DM_k | Text 5.4, polymer note | P |
| I_(k+1) | R_(k+1), VAL, low orders, flow | Base_k, Gas_k, DS, EX | closure 10, sector-values | D |
| Loc_(k+1) | (Loc^f_(k+1)) | Base_k, Gas_k far difference, Lemma CL | `far-difference-two-rate.md` | D; not in H(k) as printed |
| MD_k | (MD*_k), hence (SCR_k) | I_k^D, Gas_k, BC2 | Prop MD*, Prop 20.4 | D, inherits U from k = 1 |
| RC_k | RC-size; RC-far | Loc_k, Lemma CL, Lemma FAR | same note | size A; far D |
| DM_(k+1) | (DM), so (RAR) below regular tops | I_(k+1), Z_(k+1), DM_k | Theorem DM | D |

**Pass C, the K-class, level j + 1 from j. Reads Pass H at all levels up to K.**

| Stage | Output | Inputs at this stage | Supplier | Status |
|---|---|---|---|---|
| R | recipes a', I and their extensions | MC' for I; **nothing for a'** at n_0 - 1 >= T/4 | rc-far (MC'); none for a' | A for I; **U for a'**, D2 |
| V | reference numbers v^e | K2 at j under P_j(1, .) in LL_j | HS section 1 | E |
| X | beta_j, K1 of Rem | K1 to K3 at j, GS_j, LE_j, REG_j, rho covariant | Lemma 14.15(a), (b) | P; covariance D, D4 |
| I1 | **K1 of I and of h** | (C2_j)(a), (b), (c) on the actual polynomials | RC explicitly does not; (C2) is a sketch | **U as printed**, D3 |
| K3 | locality rows | K2, K3 at j, SCR_j; L_a from CF; L_J from RC, MC' | K-transport, Lemma EXT' | P; EXT' A |
| K3' | pullback in the mean | K3 at j + 1 under (nu' + pi_# nu')/2, in LL | 21.1 | E |
| GG | good sets | K1, K3' at j + 1 | (20.3) | E |
| K2 | moments | GG up to j + 1, RAR^ch, budgets | Lemma HS | P |

**Mixture laws.** LL closure is E: nu' P_j is in LL_j for each generator. K3 is proved for a fixed arbitrary mixture by conditionally independent copies at level j + 1; no component-to-mixture step is used. K3' needs only that mixtures with regular point masses stay in LL. Same-level regular point masses need no rarity. RAR^ch under mu has a supplier at implication level, by (Z) and Lemma TE. **No gap on this edge.**

**Criterion (S).** The rows read: K-transport, level j; L_a, a deterministic classical bound; L_J, RC_j, which reads Pass H; K3', K3 at the same level but a prior stage. GG comes after K3 and HS after GG. **No loop.**

## 2. The flat commuting model

d any, abelian, fine curvature theta in the exact 2-forms E in l^2(plaquettes). Let K_l := {dU : Q^(l) U is pure gauge}, so 0 = K_0 in K_1 in K_2 ..., because the block maps compose. H_l := E minus K_l, the curvature of minimal fields. Pi_l := the orthogonal projector on K_(l+1) minus K_l, and P_j := Pi_0 + ... + Pi_j, the projector on K_(j+1). So the curvature space is an orthogonal sum over levels. In d = 2 at U = 1 these are the linear-spline spaces of `library/upper-chain-by-hand.md`, identity (I1).

Over a parent W: theta = theta^*(W) + eta, with theta^* in H_(j+1), eta in range Pi_j. a_(j,c)(V) = sum_p w_c(p) s(theta_p(U_j(V))), with w_c(p) := (corners of p in c)/4, so a block has weight w := sum over c in B(c') of w_c.

**"Flat, commuting quadratic limit"** is read in two ways, since the recipe is empty in the first: s(t) = t^2/2 (section 3), and first order in the nonlinearity of s at small flux, x large (section 4).

## 3. The exact quadratic limit [discharged]

**Theorem G0.** Let s(t) = t^2/2, g^2 = 1/x. For every chart and every j:

1. The law of eta given W is N(0, g^2 Pi_j). It does not depend on W, on any frozen data, or on the cut, which is W-free.
2. E_W^r G_W = E_1^r G_1, so **I_j = 0 identically**, for all c', c'', and also **h_j = 0, rho_j = 0, beta_j = 0, z_j = 1, D_j = a_j**.
3. r^f_j(V) = sum_c sum_(x in c) (f(x) - f(c)) a_(0,x)(U_j(V)).

*Proof.* The constraint is linear, so the chart is linear and W-free: Q_c does not depend on W, and grad_c is linear in W. By criticality the action has no linear term, so E xi = 0 and E[xi_b (Q_c xi)_b] = (Q_c C)_bb, free of W. That is 1 and the first claim of 2. Next, E[x a^w] = x a^w(theta^*) + (1/2) Tr(w Pi_j), so H_j(a) = a' and h = 0; the rest follows from the recipes. Item 3 is the recursion for r^f with C_j acting as composition with the lift. []

**So at the strict limit the current has no far difference and no K3 to fail.** Arbitrary K1 fields do not enter. G^cur itself is a nonzero random polynomial; only its mean is read.

**Second moment, two steps [discharged].** Var_W(x a^w) = x ||Pi_j (w theta^*)||^2 + (1/2) ||Pi_j w Pi_j||_HS^2. Since Pi_j theta^* = 0, Pi_j (w theta^*) = [Pi_j, w] theta^*, which lives at the block's boundary. Through two steps eta_j and eta_(j+1) are independent, so the same formula holds with Pi_j replaced by Pi_j + Pi_(j+1). It adds; it does not compound. The far difference of the variance is at most x ||Pi_j w (theta - theta~)|| ||Pi_j w (theta + theta~)||, so it decays at the rate of the kernel of Pi_j.

## 4. First order: the current is known exactly [implication; kill-tested]

Let s(t) = 1 - cos t. Let f_w^(j)(theta) := [E_W^r x a^w - x a^w(theta^*)] at W, minus the same at W = 1, with the law carrying R_j. Let theta in H_(j+1).

**Theorem F1.** f_w^(j)(theta) = Phi_w[P_j](theta) - Phi_w[P_(j-1)](theta), up to O(theta^4) and O(g^2 theta^2), with

    Phi_w[P](theta) := sum_(p,r) (w_p - w_r) [ (1/2) P_pr P_rr theta_p theta_r + (1/4) P_pr^2 theta_r^2 ].

*Derivation.* Write theta = theta^* + g eta + zeta, zeta the lower modes. Minimise over zeta to first order in the quartic term. Collect at order x^0: the linear term of the current against the mean of eta, which has two sources, the cubic vertex and D R_j; the Hessian's change with theta; the change of covariance; and two lift terms, one linear in eta. Then use three facts: P theta = 0, P_rr = sum_p P_pr^2, and Pi_j Pi_i = 0. Each of the five terms carries (w_p - w_r). []

Consequences, each read off the display:

- **It is a current.** Every term carries w_p - w_r. Splitting 1 = sum over c'' gives an explicit antisymmetric, gauge-invariant pair form. The block sum J is chart-free at this order. On this model the exact virial cancels the chart dependence: Tr(pi C_W Q(W)) = N' for the coordinate weight pi.
- **It telescopes.** The sum over i <= j of f^(i) is Phi_w[P_j]. Two steps add to one functional, with no accumulation.
- **No constant and no linear term.** It is homogeneous of degree 2 in theta. So K1 holds in its energy form.
- **Far difference.** If theta, theta~ agree within n coarse cells of the block, a term needs w_p != w_r with one of p, r at distance >= n, so it carries one kernel factor across that distance: bounded by C e^(-delta n) times the product of the two local fields. This is the energy-weighted form K1 asks for.

**Scope warning.** With abelian fluctuations this current is a lattice artefact, suppressed like L^(-dj) at level j; in the d = 2 run the level-1 piece is about a tenth of the level-0 piece. The scale-invariant current at level j comes from charged fluctuations, which this model does not have.

## 5. Nested flat walls

**The current has no consumer on walls.** Nothing in Theorem Z, DM or MD* reads a current under frozen data. Walls reach it only through (SCR_j) in K-transport. So the test is on the normalized law and on Z^*.

**Prop W1, no depth loss in the chart [discharged at the flat limit].** For any nested family, M^D >= M restricted to the free coordinates, at any depth. *Proof.* A_j^D is a minimum over a subset, and the Hessian of a quadratic minimum is the homogeneous problem's, free of the data. Restriction to xi_Omega = 0 keeps the lower bound. [] So gamma(L) cannot degrade with depth here. This is not (NC), which is a fine-scale weighted statement: Theorem N shows the sharp weight does lose, and at small clearance compounds. For s^#, note s^# >= s~, so the values of c~ in Text 23.5 bound it from below: flat in depth to 8 levels at clearance >= 2, normal modes only. Evidence only.

**Prop W2, normalized law [discharged at the flat limit].** Z_k^D(V) = exp(-x F^D(V) + B^D), G = 1, with B^D a function of the shapes alone. So Delta R^D = 0 and b_k = 0 in (BD3). At equal shapes the cross-ratio has no scalar term, and log CR(Z^*) is exactly the bilinear form of the classical mixed difference. Against a torus reference there is an O(1) constant per wall cell, but no consumer forms that difference: (S) compares two parents under the same layers.

**Prop W3, cross-ratio [discharged at the flat limit].** With rho the canonical correlation of inner and outer data given W,

    |log CR(Z^*)| <= (2 rho / (1 - rho^2)) x ( E_I(da) E_O(db) )^(1/2),

E_I, E_O the marginal energies of the data differences. *Proof.* Block inverse of the Gaussian covariance of the data, R := S_II^(-1/2) S_IO S_OO^(-1/2), ||R|| = rho, and |log CR| <= x (rho/(1 - rho^2)) ||S_II^(-1/2) da|| ||S_OO^(-1/2) db||. [] Data processing across the middle slabs, which carry no frozen rows, makes rho free of depth. The energies are not: fine data count about L^3 per level. So W3 alone has a factor of the brick count. The run below shows it is absent: fine data couple more weakly than the count. Prop MD*'s recursion is what must pay this at the full scope.

**Runs, d = 2 [evidence].** Part A of `flat2d.py`: A1, A2, A3 PASS; rates 1.22 to 1.34 per coarse cell for all level pairs at depths 2 to 4, no slower channel; amplitude with the count 2.26, 2.53, 2.56 x 10^-3 at depths 2, 3, 4. **A1 passed with an unexplained trend**, lam = .381, .308, .238, with the wall period tied to the depth, so I did not accept it. `nest_gram.py`, registered after, with the redundant parents dropped as in F-D and the period separated: **lam = 0.2147 at every depth, to four depths, at three scales**; the trend came from the period and the redundant rows. G1 to G3 PASS. **Its control shows a limit:** with the clearance removed lam barely moves, 0.2145. So this test cannot see compounding at small clearance. It tests inf-sup, not (NC).

## 6. Mixture of two regular tops agreeing on the read cube

Let nu' = (delta_(W_1) + delta_(W_2))/2 and nu = nu' P_(j+1). In the Gaussian limit the two components of nu are N(V^*(W_i), g^2 C). On a read cube with means m_i and covariance S the posterior odds are

    pi_1(v) / pi_2(v) = exp[ x < v - (m_1 + m_2)/2, S^-1 (m_1 - m_2) > ],

and the conditional mean is recomputed with these weights. **K3 does not read them**: conditional Jensen bounds ell_(nu,m)(F) by the sup of |F(V) - F(V')| over V, V' agreeing on the cube, for every law, so no nondecaying term can enter through the weights. At the point-mass law, ell = |T(W_1) - T(W_2)|/2 exactly, for T the transported current. Through two steps T is the bilinear form of Theorem F1 on theta^*(W), and its far difference is the bound of section 4. The K-transport bound 2 U B Phi + 3 U tau^(1/2) sits far above this, so that row has room here. In the d = 2 run the far difference decays at 1.318 per coarse cell at j = 0, matching log(2 + 3^(1/2)) = 1.317, and 1.158 at j = 1 on a shorter, noisier fit, against rho_f >= 2 kappa.

## 7. What this test cannot see

Each of these is outside the flat limit, so a pass here says nothing about it: the first-order colour cancellation of section 8, D3; different sectors, and lumps of charge at small flux; the gas, rough cells, the cut; the running of x; charged fluctuations; d = 4 beyond normal modes. Part B of the run is d = 2, levels 0 and 1. Theorem F1 is a leading-order expansion, not a bound on the full law.

## 8. Defects, ranked by what each breaks

Repairs are unproved unless marked.

1. **D1, STOP. Theorem F-D with two or more jumps has no statement and no proof.** `library/fibre-propagator.md` sets Y and Omega at one pair of levels (k, n). (NC) is written, but `library/quiet-boundary-rarity.md`, The bulk step near a layer, cites "Theorem F-D with layers", and no such theorem exists. First read at level 1: (MD*_1) has data at levels 0 and 1 under W at level 2, so three scales. It feeds (I_2^D), (SCR_1), and K-transport from the second step on. *Proposed statement:* Sad#_N invertible on G x Lam^*, uniformly in the number of jumps, stable under e^f, with Lam-norm squared := sum_l s_l^-2 ||Y_l||_(N_l)^2. *Why it may hold, a count only:* [Q^o,(l), e^f] costs delta s_l from L^2 to N_l, so delta in Lam; the block means give C delta ||H||_G at each scale; (NC) replaces Lemma D-coer; the run above supports inf-sup. The one step I have not checked at all is the extension in Lemma D-coer with two jumps inside one patch, which clearance should exclude.
2. **D2. (CF_j) has no regular completion at n_0 - 1 >= T/4, so a_(j+1,c') and hence h are undefined there.** First in strict order, at (level 1, stage R), but a one-line repair: the same cap as (MC'), with Lemma EXT' at d = 0. So it does not stop the item. The interface still prints (MC), which is false. Rg_c of Lemma 14.15 has the same hole.
3. **D3. K1 of the current and of h has no supplier, and RC cannot be one.** RC-far is first order in the far field with amplitude U, about x^(1/2). K1 asks for g^2 tau^2, so at tau about 1 it misses by about x^(3/2) exp(-(rho - kappa) n) for n below about log x. Lemma FAR does not close this, contrary to rc-far defect 4: it bounds |Cov| in absolute value and cannot see a colour cancellation. In the abelian model it does suffice, since D is already second order and x^(1/2) theta^3 = g^2 tau^3; the loss is purely non-abelian. And (C2_j)(a), the energy-weighted size, rests on the patch path of (RG2), which is false across sectors. A pullback does not fix that: it keeps any lump inside the cube, so it does not have zero charge. *Repair.* (i) Size, by a dichotomy from Lemma U: small energy on a cube gives a small gauge and a local path; otherwise Ebar is bounded below and the bound |x'I| <= C(L) suffices. This needs the odd gain for E xi in far-difference form, which removes x^(1/2). (ii) Then interpolate, as Lemma 14.15(b) already does: min(A, B) <= A^(1-s) B^s with s = 2 kappa/rho <= 1/3, using rho_f >= 6 kappa. [Arithmetic discharged, premises not.] This gives eta = C_I g for I and b = C(L) g^3 for h, using FAR on G^hi with amplitude g. Both suffice: Theorem 14.13 needs iota_* bounded and the sum of b_j small, and the sum of g_j^3 converges by (FLOW-UL). The sharper g^2, g^4 are not needed.
4. **D4. rho is not hypercubic covariant on this chart,** contrary to the proof of Theorem 14.13(i), which Lemma 14.15(b) reads. Trees, designated bonds and the one-sided assignment of crossing bonds are not symmetric, so J is not, and h inherits this at order b^new. J vanishes at constant flux, so no marginal term arises, but (b) as written reads covariance. *Repair:* average I over the hypercubic orbit of charts, as Section 2 of `library/sector-values.md` does for g_i. RC, MC' and antisymmetry pass to the average, and h stays defined by the identity.
5. **D5. (Loc^f_k) is not in H(k) as printed,** though RC_k reads it. The queue's two steps are exactly where this first matters: RC_0 reads R_0 = 0, and RC_1 is the first to read R_1, hence the gas. Prop LF's gas clause and Lemma CL's hybrid stay as gated.
6. **D6. Evidence for gate rc-far D1, the slow Hessian amplitude: the square root is an artefact of the split point.** y_* in `library/one-step-closure.md` is the crossing of the tiers of Phi_k(t), but the norm reads Phi_k(tau/2), whose crossing is 2 y_*. On (y_*, 2 y_*) the kernel is first-tier, and it was charged to the slow weight at amplitude zeta^(1/2). Split at 2 y_* instead. Then V_f still obeys (A), since mu/2 >= rho_f/L, and V_s has amplitude zeta_k, so zeta_V <= C(L) g^2 B_2 zeta_k, given L mu_s/2 > rho_s. No reader needs the smaller y_*, since Sections 5, 6 are no longer read. This matters beyond the gate: taken literally, zeta -> g^2 zeta^(1/2) per level has fixed point g^4, a slow tail with power amplitude, which the rate test excludes. With the split at 2 y_* that recursion is gone. [Repair, elementary, not read by anyone else.]
7. **D7. Radii.** K1, K3' and the good set use pi_n up to M_j, undefined at n >= T_j/4, and on a torus of fixed physical size M_j exceeds that near the top. Cap at min(M_j, n_T), the last increment going to V by far difference. Local.

## 9. Runs

All under `checks/joint_induction/`, under the numeric lock, memory free 62 to 63 percent at each start, BLAS threads 1, RSS guard. Peak RSS 1.73 GB. Criteria in each header, written first.

| Script | Criteria | Result |
|---|---|---|
| `toy_formula.py`, exact nested quadrature of Theorem F1 | T1 to T3, controls | **All PASS, first run.** Relative error at most 8.0e-4 on 8 seeds at flux 0.05, falling about 4-fold from flux 0.1; total response at most 2.9e-5; all three controls fail as they must |
| `flat2d.py` Part B, d = 2, N = 243, levels 0, 1 | B1 to B4 | **All PASS.** Sum over blocks at most 2.3e-13; quadratic to 6.4e-13; rates 1.318, 1.158; K1 ratio falls with n |
| `flat2d.py` Part A | A1 to A3 | **All PASS**, A1 with a trend, explained by the next row. **Amended before it ran:** the first geometry would have exceeded 2 GB; each layer now has its own width, depth 4 has period s_n only, and the header records this. A1 to A3 unchanged |
| `nest_gram.py` | G1 to G3 | **All PASS**; its control has no power against clearance |

These can refute or guide. None discharges anything here. Theorem G0, Props W1 to W3 and the algebra of section 4 are written arguments; Theorem F1 is a leading-order derivation, kill-tested once.

## 10. Read and not read

Read: FINISH, GOAL; `parts/upper-chain.md` The interface, Text 14, 20, 21.1 to 21.4, 21.7 by grep, 22.3, 23; `parts/hard-core--mapped.md` State of attack, Obligations, Text 3.1, 5 to 5.1, 5.4, 5.8, 5.10, 5.11; `parts/hard-core--rc-far.md`; `gates/rc-far-codex-be14215b8.md`; `library/` current-locality-reduced-law, induction-with-boundary-data, generated-observable-history 1 to 5, history-budget-sum 1, 2, 4, 5, far-difference-two-rate 0 to 5, fibre-propagator, preconditioned-covariance, one-step-closure 1 to 3, 8, 10, quiet-boundary-rarity Setting and induction, energy-by-stages 7, upper-chain-by-hand 3, sector-values 2, 6, polymer-covariance by grep. Text 18 of the upper chain not read, as it sits on the other attempt's chart. Not read: the Sussman-Alpoge repository, proofs of Theorem Z, DM, EX. Nothing committed or pushed. No subagents.
