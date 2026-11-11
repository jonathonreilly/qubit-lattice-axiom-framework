lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T13:38Z

# gap-zf-box-x: zeros of Z(k,B;beta) for boxes with free walls (FINISH row 677, node Z6)

Provenance: one session, Claude Fable 5.2 medium, commit d76689eed. Not checked by another model. Written step by step; the status block at the end is the summary.

## 0. Repo search, duplicate check, reading state

- Duplicate check (grep of `library/open-core.md` and the FINISH rows for ZF_B, zero-free, cumulant): the only row for this lemma is row 677 (this one). Neighbours: row 683 `gap-sc-box` owns the winding bound (SC_B) on the disc; row 681 owns (TM_B) and the check of Theorem ZB; row 680 owns the scaling region. Nothing below proves (SC_B) or (TM_B).
- Read in full: the brief (plan Part 4 Item 1), plan sections 1.4, 1.7, 1.9, 2.5, 3.1, `library/gap-zero-transport.md`, section 4.2 of `library/gap-skeleton-final.md`. Not opened: the arXiv papers 1005.1993, 1112.2734 (numerical picture for periodic lattices; nothing below uses them), the Sussman-Alpoge account (nothing below uses it; the object here, a box with free walls at fixed lattice coupling, is outside its estimates, as plan 2.5 says).
- Credits. The uniqueness condition and its contraction argument are Dobrushin's (1968-70; recalled, not read in this run). That a uniqueness condition of this type gives analyticity is the theme of Dobrushin and Shlosman's "completely analytical" papers (1985-87; recalled, not read). The Borel-Caratheodory coefficient bound is classical. The transport theorem ZB that consumes the result is the plan's (Claude Fable 5.2, row 670). The proof of Theorem A below (a hierarchy of mixed oscillations that makes the complex one-link heat-bath kernels contract) was built in this run; I do not know whether it is in the literature in this form. Label for every literature recollection here: `unchecked`; nothing in the proofs rests on one.

Conventions. G = SU(2) with Haar probability measure. A finite set of links L and a finite set of plaquettes P; each plaquette p has four links in L and a_p(U) = 1 - (1/2) Re tr U_p in [0, 2]. Geometric hypotheses, used below and true for a spatial box with free walls and periodic time k >= 3, for a periodic torus with all sides >= 3, and for every sub-family of the plaquettes of such a lattice:
(G1) every link lies in at most 6 plaquettes of P;
(G2) two distinct links lie in at most one common plaquette of P.
(For k = 2 the two time-like plaquettes over a spatial link share both copies of it, so (G2) fails; k >= 3 is assumed.) N = |P| <= 6 k |B| for the box. A = sum_p a_p, Z(beta) = int exp(-beta A) dU, entire in beta; for real beta, mu_beta is the probability measure exp(-beta A) dU / Z.

## 1. Step 0: the real form, proved equivalent with constants

For real beta, kappa_j(beta) = (-1)^j (d/dbeta)^j log Z(beta) is the j-th cumulant of A under mu_beta.

**Proposition 0.** Fix the lattice (L, P), a real x >= 0 and rho > 0.
(i) If Z has no zero in the open disc |beta - x| < rho, then |kappa_j(x)| <= 4 N max(x, rho) j! rho^{-j} for all j >= 1.
(ii) If there are C and any number K (it may depend on the lattice in any way) with |kappa_j(x)| <= K j! C^j for all j >= 1, then Z has no zero in |beta - x| < 1/C.
Consequently, for an interval [r_0, beta_1] and a family of lattices: "there is rho > 0 such that no Z of the family vanishes within distance rho of [r_0, beta_1]" is equivalent to "there is C such that |kappa_j(x)| <= N j! C^j for all j >= 1, all x in [r_0, beta_1] and all lattices of the family", with C = max(1, 4 max(beta_1, rho))/rho in one direction and rho = 1/C in the other. For boxes N <= 6 k |B|, which is the form in the brief. An open set U containing the compact interval contains its rho-neighbourhood for some rho > 0, so this is the equivalence asked for.

Proof. (i) g = log Z is analytic in the disc, with the branch real at x. For beta in the disc, |Z(beta)| <= Z(Re beta) <= exp(2 N max(0, -Re beta)), so Re g <= A_0 := 2 N max(0, rho - x). And g(x) >= -2 N x since A <= 2N. Write g(x + z) = sum_j c_j z^j. For 0 < r < rho and j >= 1: c_j r^j = (1/pi) int_0^{2 pi} Re g(x + r e^{i t}) e^{-i j t} dt (the Fourier coefficient of the real part), and int e^{-ijt} dt = 0, so c_j r^j = -(1/pi) int (A_0 - Re g) e^{-ijt} dt. The integrand A_0 - Re g is >= 0 and its mean is A_0 - g(x). So |c_j| r^j <= 2 (A_0 - g(x)) <= 2 (2N max(0, rho - x) + 2 N x) = 4 N max(x, rho). Let r -> rho; kappa_j = (-1)^j j! c_j.
(ii) The Taylor series S(z) = sum_j (-1)^j kappa_j (z - x)^j / j! + log Z(x) converges in |z - x| < 1/C. Near x it equals log Z, so exp(S) = Z near x, hence on the whole disc (identity theorem; Z is entire). exp(S) has no zeros. QED.

Remark 0.1. The extensive prefactor 6 k |B| is free: by (ii) and then (i), any bound K j! C^j with K depending on the lattice gives 4 N max(x, 1/C) j! C^j. The content of the real form is the uniform radius of convergence alone.

Remark 0.2. As literally written, the statement of the item ("there are r_0 > 0 and beta_1 > r_0 ...") is already satisfied inside the strong-coupling disc. The content is the size of beta_1. Section 2 gives an explicit beta_1 with an explicit tube, by an argument that is not a polymer expansion around beta = 0.

