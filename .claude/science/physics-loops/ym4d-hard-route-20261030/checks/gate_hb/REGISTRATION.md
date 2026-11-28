# Registered criteria, written before any run

Gate history-budget, commit 769697e8d. Script: `hb_checks.py`. Same-model
check, not independent and not an audit. These test abstract arithmetic and
finite probability. None of them is a statement about the Wilson law.

- **T1, GH.** Random finite reverse Markov chains, depth 1 to 4, at most 3
  vertices per level, recipes of form (G2), exact sup b_v and d_0, E random or
  B_root. PASS: no violation of (GH) above 1e-9 relative in 4000 chains at
  q = 1, 2, 4, and max LHS/RHS >= 0.5, so the test is not vacuous.
- **T1c, control, must fail.** Same chains with a copied bad bit, with the
  term P(D_p) replaced by the product of marginals. PASS if at least one
  violation is found, which shows T1 can see a wrong joint bound.
- **T2, source table.** Random hierarchy with random kernels and supplied
  a, I antisymmetric, beta. PASS: (G1), the total mark identity, the r^f
  identity for y_j(f), and each row of the table in section 2 of
  generated-observable-history.md (D, rho, r^f, Rem, H, h) hold to 1e-10.
- **T3, scalar sum.** For a grid of (N, B, b', c_G, l_0, l_1, Y, S/N, A), the
  direct sum E_J and the bottom and source sums at depth up to 4000 stay
  below E_*(X) and the right side of (HS-budget), whenever both denominators
  in (SUM) are below 1. PASS: no exceedance above 1e-9 relative. Also report
  the X needed for right side <= 1/2 at sample constants.
- **T3c, control, must fail.** Remove the half-path loss: use
  psi_J(a) with s_a = 1 and the GG term at offset 0 only, that is, a one-level
  bound. PASS if the direct sum diverges or exceeds 1 at some grid point,
  which shows why the joint form is read.
- **T4, radius.** Random (B, l_1, alpha, X, x_K in [X, 2X]) and random and
  extremal sequences obeying (FLOW-UL), under (END-R) and (FLOW-END). PASS:
  x^2 + 3 < floor(exp(lambda/5)), compared in logs, at every d up to 10^6,
  and (A-count) once X is past its stated bound.
- **T4c, control, must fail.** (a) x_(K-d) = x_K (5/4)^d with small l_1.
  (b) Fixed l_0 with large x_K. PASS if each violates the radius inequality.
- **T5, transport.** Finite model of (K-transport): random nu' on pairs
  (n, rest), kernel P, test G on two blocks. tau is the exact supremum of
  E|(E_W - E_W~)F| over |F| <= 1, by enumerating sign vectors on at most 8
  states. PASS: ell(PG) <= 2 ||G - G_n||_1 + 3 ||G||_2 sqrt(tau) in 2000 draws.
- **T6, bounded shell.** Evaluate the example of section 4 of
  history-budget-sum.md at explicit parameters. PASS: ell/(U B Phi(m)) > 1 at
  some x with all side conditions of that example checked.

What a pass can establish: no arithmetic slip of the tested form. What it
cannot: any hypothesis of Lemma HS, or any bound on Yang-Mills.

## Second registration, written after the first run

The first run's T3 had no exceedance, which meets the criterion above. The
script also carried a floor of more than 100 admissible grid points that was
not written above, and only 32 points were admissible, so the script printed
`pass: false`. That is recorded in `run.log` and is not edited.

- **T3'.** Wider grid: X up to 10^14 and c_G down to 10^-5, so that the
  denominators of (SUM) are below 1 at many points, including points with a
  denominator ratio above 0.5. PASS: no exceedance above 1e-9 relative, at
  least 500 admissible points, at least 20 of them with a ratio above 0.5.

## Third registration, written after the second run

T3' had no exceedance at 1872 points but `near_denominator_points` was 0, so
it FAILED its own floor and did not test the edge of the geometric series.
That is recorded in `run_t3prime.log` and is not edited.

- **T3''.** Solve for the parameters instead of using a grid: for each
  (N, B, b', c_G, l_1) and target ratio in {0.6, 0.8, 0.95}, set either the
  c_G ratio D exp(-mu_G) or the l_0 ratio D exp(-l_0/8) to the target. Depth
  20000. PASS: no exceedance above 1e-9 relative of E_* or of the right side
  of (HS-budget), and at least 200 solved points.
