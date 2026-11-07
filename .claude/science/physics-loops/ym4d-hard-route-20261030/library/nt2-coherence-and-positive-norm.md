# NT2: coherence is free, running needs negative norm, K_vert has no chart-free value

Author: anthropic/claude-opus-5-5/high mac-mini-worker, 2026-11-01, gate `gates/nt2-gate-2285befef.md`.
Source: 2285befef. Neutral: uses no proof of either hard-core attempt.
Status: Lemmas C, RM, X, K discharged at the stated scope. Proposition TD and Corollary RM are implications with their hypotheses named. Same-model author work, not an audit. No status.
Credit: the Stieltjes form of a positive-norm two-point function is Kallen-Lehmann. That asymptotic freedom sits badly with a positive-norm potential is an old observation (Oehme-Zimmermann, recalled from memory, not read and not used); the short proof below is complete in itself. The transport identity is `witness-running-tests.md`, section B.

## 1. Coherence

Let M be a deterministic measurable block map from links of level j + 1 to links of level j, the same at each level, on tori Lambda_j. If M has auxiliary variables, count them as part of the link data. Coherence means M_* mu_(j+1) = mu_j.

**Lemma C [discharged].**
(a) For any law mu_i at level i, mu_j := (M^(i-j))_* mu_i is coherent on 0 <= j <= i.
(b) Let mu_0 be any law and let kappa_j(V, dV') be any probability kernel carried by the fibre M^-1(V). This needs a non-empty fibre for mu_j-almost every V. Then mu_(j+1) := mu_j kappa_j is coherent, exactly, at every level, with no limit taken.

Proof. (a) is composition. (b): for bounded f, E_(mu_(j+1)) f(M V') = E_(mu_j) int kappa_j(V, dV') f(M V') = E_(mu_j) f(V). []

So the equation (B4) of `witness-running-tests.md`, called there the missing consistency equation, has solutions at no cost. What is not free is matching. A constant-amplitude fine law blocked by (a) has no reason to run, and (b) is the way to prescribe the running.

**The top-down law.** Let F_j be the classical action of level j: the Wilson action at the finest level of the tower, and at coarser levels the minimum over the fibre of M, which is the tropical action of `parts/witness.md` Lemma 5.2. Take a sequence gamma_j > 0, with j increasing to the ultraviolet here, gamma_(j+1)/gamma_j -> 1, gamma_j -> 0, and the fibre conditional law

    kappa_j(V, dV') = exp(-gamma_(j+1)^-2 F_(j+1)(V')) sigma_V(dV') / N_j(V),

with sigma_V the disintegration of Haar measure over M. The law mu^TD is gauge invariant when mu_0, F, M are. It keeps the conditional law of Wilson's hierarchy on each fibre and discards the factor N_j(V), which is what produces the true flow on the coarse marginal. It is coherent by Lemma C(b), with the volume and cutoff limit taken along a subsequence on windows by compactness of SU(2).

**Proposition TD [implication; hypotheses not verified].** Assume the one-step package of `parts/witness.md` Text 8.1 for mu^TD: (G0) with its lifted class, H-LIFT in the form (2)-(3) of `witness-moment-gap.md`, H-FIRST, H-TREE, H-MOM, each read with kappa_j as the fibre law. Then (NT2-M) holds for mu^TD with g_m/gamma_m -> 1, by the same recursion as `witness-moment-gap.md` (4)-(5) and (ERR-T). In particular:

- with gamma_m^-2 = c + b_W m log L, mu^TD satisfies all of NT2, (NT2-R) included;
- with gamma_m^-2 = c + b m log L, b != b_W, mu^TD satisfies (NT2-M) and fails (NT2-R) only through the chosen number b.

Proof. The recursion reads only one-step statements and H-FLOW. It nowhere reads that mu_j is the Gibbs marginal of mu_(j+1). H-FLOW holds by choice with d_j = 0, rho_j = 0. The first-order term of H-FIRST is computed from kappa_j, and the tree sum is Lemma 5.2 for the tropical F_j. []

Not claimed: reflection positivity, which I expect to fail, since the discarded N_j(V) is what a local action would supply; the one-step package itself, in particular H-MOM, whose chessboard source is not available without RP and would need a separate top-down argument; existence of the limit of F_j. A bottom-up version, a fine Gaussian with a slowly varying multiplier and the map of section B, is not claimed either. The weighted tree value in that version is `checks/gate_nt2` C2b, but power counting suggests that the quadratic map adds noise of relative size h^2 (r/a)^2 at scale r [unchecked], with no Ward identity to remove it. The top-down law has no such term, since the coarse marginal is unchanged by construction.

No clause that only matches moments can exclude mu^TD, because the running is an input to its construction. Only RP or locality can.

## 2. Running against positive norm

Let a be an R^3-valued vector potential on R^4 with independent colours, invariant under O(4), with a Kallen-Lehmann form: on conserved currents its covariance is the multiplier

    D(k^2) = int dnu(s) / (k^2 + s),   nu >= 0 on [0, infinity).

Proca fields, Maxwell, independent sums of those, and any RP vector field with O(4) invariance have this form for their transverse part. Let j be a closed current at unit scale, for instance a blocked loop current as in (B-4), and j_r(x) = r^-3 j(x / r).

**Lemma RM [discharged].** Var <j_r, a> = int dm(q) rho(q^2 / r^2), with dm(q) = |j^(q)|^2 / |q|^2 dq / (2 pi)^4 and rho(z) = z D(z) = int dnu(s) z / (z + s). rho is non-decreasing, so r -> Var <j_r, a> is non-increasing: the flux variance can only grow as r decreases.

Proof. The Fourier transform of j_r is r j^(r k). Substitute q = r k. Each z / (z + s) is non-decreasing. []

If a law depends on the cutoff i, with nu_i converging vaguely, each Var is monotone in r and so is the limit. No trajectory of amplitudes rescues it.

**Corollary RM [implication].** Let the leading blocked flux of a law be <J_m, a> with a of this form, Gaussian or a one-link local map of a Gaussian RP field (whose transverse two-point function again has this form), or a mixture of such laws. Then g_m cannot tend to zero, so (NT2-R) fails, whatever the amplitude. It needs only that the holonomy flux at level m is <J_m, a> up to errors vanishing when the flux is small. This covers the laws L1, L2 of `gates/witness-3b7fd4e57.md`, read coherently. No use of T.

Conversely a multiplier rho decreasing to zero, the running profile, forces a negative spectral density: for rho(z) = 1 / (c + b log(1 + z)), the density of D on z = -s, s > 1, is negative throughout. `checks/gate_nt2` C3d. So L3 at a running amplitude is not RP on functions of its links. The argument does not reach RP restricted to gauge-invariant functions, which is all T1 asks: Wilson itself has no positive-norm potential. Scope: O(4) invariance of the leading two-point function is used. With hypercubic invariance only, RP in each axis gives monotonicity of k_i^2 D in each k_i^2 separately, which does not give the dilation statement.

## 3. The energy excess of L1 is irrelevant under blocking

**Lemma X [discharged for the slope].** For X centred Gaussian, colour-isotropic, Phi_kappa = sum_b w_b X_b (1 + kappa |X_b|^2), L = sum_b w_b X_b, r_b = Cov(L^a, X_b^a), u = Var(L^a):

    d/dkappa at 0 { E|Phi_kappa|^4 - (5/3)(E|Phi_kappa|^2)^2 } = 120 sum_b w_b r_b^3.

Proof: as (C1) of `witness-running-tests.md`, with weights; the terms in u v_b r_b cancel for each b separately, also for unequal v_b. Exact check, two links with unequal variances and weights: C3c.

For the block (B-1), n = L^j, r_b is the fine-link value of E = G J, of order 1 / n, and sum |w_b| is of order n. So the slope normalized by u^2 is O(n^-2). Computed for Gamma_12, Feynman covariance: 3.75, 0.211, 0.0730, 0.0370 at n = 1, 3, 5, 7, which is 1.8 / n^2 at n >= 3. A fixed local map of the fine field therefore has no fixed excess at a blocked scale. The fixed-kappa family of section C of `witness-running-tests.md`, which puts the excess at the template scale at every m, is not a coherent family.

## 4. K_vert has no chart-free value

**Lemma K [discharged].** Let E_1, E_2, E_3 solve d^T d E_i = J_i with invertible P_ij = <J_i, E_j>. Let Pi_0 be a linear colour-diagonal projection onto a slice with Pi_0 d_0 = 0, and fix a site function theta. Let J' be the combination of J_1, J_2, J_3 with <J', E_1> = <J', E_2> = 0, <J', E_3> = 1. Then for each real t,

    Pi_t := Pi_0 + t (d_0 theta) tensor <J', . >

is again such a projection (Pi_t^2 = Pi_t, Pi_t d_0 = 0, using <J', d_0 . > = 0), hence a linear slice complementary to the gradients, colour diagonal, so with no term of order gamma in its Faddeev-Popov factor, since the colour trace of the adjoint vanishes. It sends E_3 to E_3 + t d_0 theta and fixes E_1, E_2. By Proposition 2.2 of `parts/witness.md`, K_T does not change and K_vert(t) = K_vert(0) + t delta(theta), with delta(theta) = -24 <J_1, theta_bar E_2> + 24 <J_2, theta_bar E_1>. If delta(theta) != 0, K_vert takes every real value on this family of charts, 0 included.

Computed on the box 3^4: K_T = 0.6260046897 in all charts, to 1e-14. K_vert = 0.2613 (Landau), 0.0368 and 0.1721 (two maximal trees), 0.0000 (Lemma K at t = 2.579).

The chart-free statement is the one for all charts at once: Theorem 3.16 says that no symmetric c has K_comp[c] = K_T on every triple in a box of side 23. So, at the lattice scale, every chart has some triple in that box with K_vert != 0. That is the correct form of "the vertex is present", and it needs a family of triples, not one.
