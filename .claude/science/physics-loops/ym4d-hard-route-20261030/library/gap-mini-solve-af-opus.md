lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T22:42Z

# gap-mini-solve-af-opus: the mass gap for four-dimensional SU(2) Yang-Mills (row 1256)

Started 2026-11-20T10:42Z (date -u), at commit 905d9a273 on branch claude/ym4d-hard-route.
Queue row 1256 of FINISH.md. Labels: PROVED, ARGUED, GUIDE, OPEN.

Status: in progress. Sections are appended step by step.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T11:02Z by date -u)

**1.1 What the record fixes (cited, not re-derived; these are pointers to evidence, not evidence).**
- Beside the account's premises (the T0 chain), the Jaffe-Witten gap on the account's tr F^2 sector reads one lattice
  estimate, (N-phys) (row 1161, `gap-solve9-astra62.md` L146-148; row 1179 Theorem BP; row 1225 Theorem E-N, check 1232).
- Row 1180: (N-phys) holds iff every fine coupling has a finite neutral seed and limsup a_j nu(beta_j) is finite.
  Row 1225 (ARGUED): modulo the ultraviolet carry, the crux is the seed of SU(2) Wilson at one fixed weak coupling,
  with seed side of order exp(c beta_0). Check 1242: a gap alone does not give that seed; the trace count matters
  (also row 1234, Proposition LS, check 1250).
- About 45 route families for the infrared seed are on file with a first failing step (`parts/gap.md` methods 19-36
  and route registry RA-RG; screening tables of rows 1189 (b-fable 2.1), 1194 (e-fable 2.1), 1199 (i-fable 1.2);
  rows 1237-1255). Row 998 9.5 asks for no further fresh-framing exercise by this model family.

**1.2 My own screen of the infrared seed (each idea grepped in `library/`, `library/prior/` and `parts/` before
any work; counts are files that name the tool).** Every idea is on file or dies at once.

| Idea | Status |
|---|---|
| Reflection coupling for the Wilson Langevin dynamics (Eberle) | needs convexity outside a ball; same wall as Bakry-Emery with the O'Neill term (b-fable 2.1 row 1) |
| Lattice bootstrap: positivity of Wilson-loop Gram matrices with loop equations (Kazakov and Zheng) | 105 files name bootstrap, 21 Kazakov; it bounds finitely many loop averages, not decay; its sharp form is a semidefinite program, a computed certificate |
| 't Hooft anomaly at theta = pi (Gaiotto, Kapustin, Komargodski, Seiberg) | 10 files; it forbids a trivial gapped phase at theta = pi only; it says nothing at theta = 0 |
| Deformed Yang-Mills on R^3 x S^1, adiabatic continuity (Unsal, Yaffe) | 21 files; Route T and rows 678-684; continuity to R^4 is a conjecture |
| Stability of a gap under perturbation (Bravyi, Hastings, Michalakis) | 12 files; needs a gapped frustration-free start and a small perturbation; at weak coupling the magnetic term is not small |
| Stochastic quantization (Chandra, Chevyrev, Hairer, Shen) | 15 files; local in time in 2D and 3D; 4D is critical |
| Ground-state Doob transform: the gap as the Poincare constant of psi_0^2 with the electric Dirichlet form | exact reformulation; Bakry-Emery needs Hess(-log psi_0^2) >= -Ric + kappa, and on a compact orbit space a convex function is constant, so this is the orbit-space curvature route (b-fable 2.1 row 1) |
| Finite subgroup (binary icosahedral 2I) at all couplings | 39 files; frozen Q_8, 2T rows of the test table; the confining window is the same band |

Verdict (ARGUED): no engine for the infrared seed off the record. The seed stays OPEN, as in rows 1219-1255.

**1.3 Choice for this row.** Rule 0 asks what changes. The one-cutoff carry (row 1233 Proposition 3.7, as corrected
by check 1242 and by row 1255 for the normalisation term D) turns a seed at one cutoff into (N-phys). Its open inputs
(check 1242 L72-76): the 9.1 comparison's hypotheses, with `9.1:prop-blind-site-expansions` OUTSTANDING in the account
(a repeat of Balaban CMP 116 Section 2 at three sites, rows 1234 and 1255: a multi-row project); **(EDGE)**; (DET)'s
inputs; reading (R) or (V9) (row 1255). (EDGE) is attacked by no row (grep of `library/` for "(EDGE)": rows 1233,
1234, 1241, 1251, 1255 and check 1242 name it; none works on it). Check 1242 (L68-70) found that (EDGE) does not merely
restrict the base set: every datum above the base needs a real predecessor that is again a first-passage datum, the
analytic inverse of the matching map exists only on a smaller disc, equal terminal couplings do not control earlier
threshold crossings, and the account's window-inclusion corollary `9.8:cor-subsequential-limits` is OUTSTANDING.

Plan, one step per response:
- Step 2: the exact-pin chain. The account's matching map fixes 0, so along the exact pins beta = a_K every datum has
  an exact predecessor, and the one-cutoff base is a single datum. State and prove it from the account's proved
  statements, and say what it costs (which trajectory the gap consumer then reads).
- Step 3: the general chain (EDGE'), a corrected (EDGE) for first-passage data: predecessors need only be tuned data,
  and the backward drift of the window coordinate is controlled by the summable matching errors. Prove it.
- Step 4: the window inclusion of first-passage data (part (a) of the account's outstanding corollary), attempted
  from the account's flow bounds; first failing input if it fails.
- Step 5: state after this row, RESULT.
Moves: (EDGE) of the one-cutoff carry, an open input of the gap chain's ultraviolet half. Success: (EDGE) leaves the
input list, or is replaced by named account statements. Failure: the first account statement the replacement needs.

Source for Steps 2-4: Sussman and Alpoge's complete account at commit 31a47c543775 (`theorem_0_complete_account_raw_III.tex`,
fetched by URL into a scratch folder outside the repository; credit Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their text; the construction is Balaban's renormalisation group). Line numbers below are of that
file (written III:n).

## Step 2. The exact-pin chain needs no (EDGE) (written 2026-11-20T11:05Z by date -u)

**2.1 What the account states (READ).**
- Tuned runs (III:1264-1300, Definition `9.1:def-tuned-family`): on the canonical scaffold Theta_X a run of length n
  started at zeta is zeta_(n) := zeta, zeta_(r) := zeta_(r+1) + b_(r) - c_0, with couplings x_(r) := theta_r - zeta_(r).
  (J3) (III:1331-1337): for |t| <= r_J there is exactly one real zeta_*^n(t) whose run of length n is alive and has
  zeta_(0) = t. The pin run is zeta_*^n := zeta_*^n(0); its depth-zero coupling is x_(0) = theta_0 = X = g^-2.
- `9.8:thm-uniqueness-theorem` (III:53784-53900; index status PROVED, an implication from its hypotheses (i)-(iv)):
  (a) the run of length n started from a_n has x_(0) = X exactly, "and it is the only real alive run of length n with
  this property" (III:53844-53846); (b) the matching map n_n is holomorphic on |w| < r_J, real on the reals,
  **n_n(0) = 0**, the runs of lengths n+1 from a_(n+1) - n_n(w) and n from a_n - w have equal depth-zero coupling, and
  |n_n(w) - w| <= Upsilon_n |w| with Upsilon_n <= C n^(-3/2) (log n)^(p_0+1) (III:53859-53868); (e) the a_n, n_n,
  N_n, Upsilon_n do not depend on the torus (III:54140-54153; also the statement, III:53836-53838: the a_n depend on
  (L, p, g, n) "and on no torus").
- The pair compared at the last lattice (III:11806-11830, `9.1:not-centre-normalisation`): for n with
  Upsilon_n <= 1/4 and u = Re w, run A has length n and centre zeta_*^n + u, run B has length n+1 and centre
  zeta_*^(n+1) + n_n(u); the zero residual source is w = u real, z = 0. Since a run of length n started from the bare
  number a has zeta = theta_n - a, the centre zeta_*^n + u is the run started from a_n - u.

Notation (as in row 1233, check 1242 and row 1255). Fix the two tori T = T_(m_0) and T' = T_(m_0+1) of tuned units
(side 2L^(m_0) and 2L^(m_0+1) depth-zero blocks). A datum (n, beta) is the bare lattice Lambda_(n+m_0) (resp.
Lambda_(n+m_0+1)) at bare inverse coupling beta. Phi(n, beta) := L^4 log Z^bare_T(n, beta) - log Z^bare_T'(n, beta).
The **pin datum** is p_n := (n, a_n).

**Proposition PIN (PROVED GIVEN the uniqueness theorem's hypotheses (i)-(iv) on T and on T').** Let n_U be the least
integer with Upsilon_n <= 1/4 for all n >= n_U. For every n >= n_U:
(a) *Exact predecessor.* The only real number u in (-r_J/2, r_J/2) with n_n(u) = 0 is u = 0. So the predecessor of
    p_(n+1) under the matching map, pi(p_(n+1)) := (n, a_n - n_n^(-1)(0)), exists, is unique, and equals p_n.
(b) *Each edge is a 9.1 pair at the zero residual source with u = 0.* The pair (A, B) of `9.1:not-centre-normalisation`
    at w = 0 is (the pin run of length n, the pin run of length n+1), that is, the runs of p_n and of p_(n+1).
(c) *Consistency.* The run of p_n is one and the same run when p_n is the B-run of the edge (p_(n-1), p_n) and the
    A-run of the edge (p_n, p_(n+1)), and the bare number a_n is the same on T and on T'.
(d) *Carry along pins.* Let b_n be the edge bound of row 1233 Lemma 3.5 (from `9.1:cor-sourced-integrals` at the
    zero residual source; it holds under hypotheses (a)-(e) of `9.1:thm-last-lattice-comparison`, of which (e) is the
    OUTSTANDING `9.1:prop-blind-site-expansions`), and let E9(p_n; T) be the additive bare constant of the run of p_n
    (row 1255 Lemma D0). Then for every K_0 >= n_U and every n >= K_0,
        Phi(p_n) <= Phi(p_(K_0)) + sum_(j >= K_0) b_j + 2 sup_(j >= K_0) |Delta E9(p_j)|.
    No inverse of the matching map off 0, no window of w, no first-passage condition on intermediate data and no
    base datum other than p_(K_0) enters.

*Proof.* (a) Upsilon_n <= 1/4 gives |n_n(z) - z| <= |z|/4 on |z| < r_J. On the circle |z| = r_J/2,
|n_n(z) - z| <= r_J/8 < r_J/2 = |z - 0|. By Rouche's theorem n_n and the identity have the same number of zeros in
|z| < r_J/2, namely one, counted with multiplicity. n_n(0) = 0 by (b) of the uniqueness theorem, so 0 is that zero
and it is simple; a real u in (-r_J/2, r_J/2) with n_n(u) = 0 would be a second zero unless u = 0. Hence
n_n^(-1)(0) = 0 on that disc and pi(p_(n+1)) = (n, a_n). Independently of the inverse: by (a) of the uniqueness
theorem the run of length n from a_n is the only real alive run of length n with x_(0) = X, and the run of length
n+1 from a_(n+1) has x_(0) = X; so p_n is also the unique real alive datum of length n with the depth-zero coupling of
p_(n+1).
(b) Put w = 0 in `9.1:not-centre-normalisation`: u = 0, so A has centre zeta_*^n and B has centre
zeta_*^(n+1) + n_n(0) = zeta_*^(n+1). By the identity zeta = theta_n - a these are the runs started from a_n and
a_(n+1). The residual sources are W^A(0) = 0 and W^B(0) = n_n(0) - n_n(0) = 0 (III:11826-11830).
(c) Both readings of the run of p_n are "the run of length n with centre zeta_*^n", which (J3) defines uniquely; the
scaffold Theta_X and the step data do not depend on the torus by (J1), and a_n does not by (e).
(d) By (b) and (c) the chain p_n -> p_(n-1) -> ... -> p_(K_0) satisfies the hypotheses of row 1255 Corollary D1 with
consistent representatives (one run per pin, one constant E9 per run), and each edge satisfies the hypotheses of row
1233 Lemma 3.5 at u = 0 on each torus. Corollary D1 gives the display. QED

**Remarks on Proposition PIN.**
1. (PROVED, elementary.) Along pins the edge comparison sits at the centre of the account's comparison window
   (u = 0), so the outward drift that check 1242 L68-70 found for the inverse matching map (its example
   n(z) = (1 - eps) z) does not arise: n_n^(-1)(0) = 0 for every n.
2. (READ.) Check 1242's requirement that an intermediate datum use "the same mass on its two adjacent edges" (L60) is
   met by (c) with no extra choice.
3. (PROVED from (d).) The base requirement of the one-cutoff carry becomes one inequality at one datum per torus
   pair: Phi(p_(K_0)) <= phi_* - sum_(j >= K_0) b_j - 2 eta_9, where eta_9 := sup_j |Delta E9(p_j)| (row 1255's (V9),
   needed only at pins). Under row 1255's reading (R), eta_9 <= eta_vac(m_0) + eta_det(m_0) (row 1255 Proposition
   D2(b), from row 1233 Lemma 3.6).
4. (READ; credit.) The observation that at v = 0 the matched pair is the pair of tuned runs of lengths n and n+1 is
   the account's own: it uses it for the convergence of the depth-s couplings (III:56740-56745, coupling convergence
   in 9.9; III:69358-69362, `9.13:lem-depth-convergence`). New here is only its use as the chain of the gap lane's
   one-cutoff carry, in place of (EDGE), and the reduction of the base set to one datum.

**2.2 What the pin chain costs: which trajectory the gap consumer reads.** The (ONE-K) consumer and the gap consumer
(row 1225 Theorem E-N through (N-phys)) are stated on first-passage data: K(beta, g) = min{k : x_k <= g^-2 + B_sharp}
for the running couplings x_k of clause (0) of the account's Theorem 0 (III:68763-68767; CA-I L1666-1667, read by
row 924). A pin p_n is a tuned datum. Two ways connect them.

**Lemma OFF (PROVED GIVEN (FI) and clause (0) at the datum a_n).** Assume
(FI) the clause-(0) couplings of the bare datum (Lambda_(n+m_0), a_n) agree with the couplings of the pin run of
    length n: x_k = x_(n-k) for 0 <= k <= n;
and that clause (0) attaches to that datum the flow bound of III:68709-68712,
    lambda_sharp (j - i) - c_5 <= x_i - x_j <= B_sharp (j - i)   (0 <= i <= j).
Then the first-passage depth K_0(n) := K(a_n, g) satisfies n - D_* <= K_0(n) <= n with
D_* := ceil((B_sharp + c_5)/lambda_sharp).
*Proof.* By (FI) and (J3), x_n = x_(0) = X < X + B_sharp, so K_0(n) <= n. For k <= n - D_* - 1 the lower flow
bound with (i, j) = (k, n) gives x_k >= x_n + lambda_sharp (n - k) - c_5 >= X + lambda_sharp (D_* + 1) - c_5
> X + B_sharp, since lambda_sharp D_* >= B_sharp + c_5. So no k <= n - D_* - 1 is a passage, and K_0(n) >= n - D_*. QED

**Corollary OFF-1 (PROVED GIVEN Lemma OFF's hypotheses for every n >= K_0).** Put delta_n := n - K_0(n) in
{0, ..., D_*}. Some value delta occurs for infinitely many n; along that subsequence the pin p_n is the first-passage
datum (K_0(n), a_n) of clause (0) on the tori of first-passage units with sides 2L^(m_0 + delta) and 2L^(m_0+delta+1),
fixed along the subsequence (systems of units, Definition `9.13:def-systems-of-units`, III:68074-68097: Lambda_(n+m_0) read with reference
length L^(K_0(n)) has torus exponent n + m_0 - K_0(n) = m_0 + delta). So Proposition PIN (d) gives the (ONE-K)
inequality Phi <= phi_* at first-passage data on two fixed physical tori, along an infinite subsequence of cutoffs.
*Proof.* Pigeonhole on the finite set {0, ..., D_*}; the rest is the change-of-units identity. QED

What the subsequence buys (ARGUED from row 1180, which states that for one continuum datum a liminf suffices, with row
1179 Proposition P'-ev): a continuum datum built along a further subsequence of these first-passage data (the account's
first-passage subsequence construction, `t0-tree.md` node AII-T-b) is a T0 datum, and (N-phys) along that subsequence
is what its gap clause reads. So under (FI) the pin chain feeds the gap consumer with no (EDGE) at all.

**Standing of (FI) and of the offset (READ).** The account itself assumes the offset as a hypothesis in its clause (v)
lemmas: "(b) The first-passage depth of tuned data. For every w in W and every n, the bare datum x_0 = a_n - w is a
first-passage datum of clause (0) ... at a depth K_0 with |K_0 - n| <= j_U - 1" (III:54429-54434), and in the same form
at w = 0 (III:54832-54835). Its corollary on the coupling shift between two readings assumes as hypothesis (b) that x_k
"is a function of (Lambda_n, x_0) and of k only" (III:68713-68716), which is (FI)'s kind of statement. I found no
account line proving (FI). Lemma OFF needs (FI) only at w = 0, with D_* = ceil((B_sharp + c_5)/lambda_sharp) in place of
the account's j_U - 1. So the pin chain moves (EDGE) onto (FI) at pins, a statement the account's own clause (v)
lemmas already assume in a stronger form.

**2.3 Status after Step 2.**
- PROVED GIVEN the uniqueness theorem's hypotheses: Proposition PIN (a)-(c). PROVED GIVEN in addition the 9.1
  comparison's hypotheses (a)-(e) and the normalisation hypothesis (V9) at pins: Proposition PIN (d).
- PROVED GIVEN (FI) at pins and clause (0): Lemma OFF and Corollary OFF-1.
- ARGUED: the consumer remark after Corollary OFF-1 (it rests on row 1180's liminf remark and the T0 subsequence).
- OPEN: (FI) at pins; the 9.1 comparison's hypothesis (e); the base inequality at p_(K_0) (the infrared seed).
- New against the record, as far as my grep shows: grep of `library/` for "exact pin", "pin trajectory",
  "n_n(0) = 0" finds only `t0-tree.md` L84 (node name "exact pin" for clause (v-a)) and unrelated uses; no row uses the
  pins as the chain of the one-cutoff carry. The pin pair itself is the account's (Remark 4 above).

## Step 3. First-passage tops: the backward drift, a corrected (EDGE'), and the window inclusion (written 2026-11-20T11:10Z by date -u)

**3.1 More account statements used (READ).**
- `9.6:prop-depth-zero-match` (III:52290-52330; index PROVED): with h_n(v) := zeta^n_(0)(zeta_*^n + v) on D(0, R),
  R = 4 r_J, for |w| <= r_J there is exactly one n_n(w) in D(0, 8 r_J/3) with h_(n+1)(n_n(w)) = h_n(w), and
  |n_n(w)| <= 2|w|, |n_n(w) - w| <= Upsilon_n |w|.
- `9.12:lem-bi-lipschitz` (III:67295-67330), hypothesis (A), "the running-shift statement of the correlation theorem
  ... read on the scaffold Theta_X about the tuned centre with radius r_J": with beta^(n)_r(eta) := b^(n)_(r)(zeta_*^n + eta),
  (R1) beta^(n)_r is holomorphic on D(0, 2 r_J) and real on the reals; (R2) for rho in [r_J, 2 r_J],
  |beta^(n)_r(eta) - beta^(n)_r(0)| <= d^(n)_r(rho) |eta| on D(0, rho) with sum_(r<n) d^(n)_r(rho) <= 1/3. This is the
  same budget as (J2)'s sum_u a_u <= 1/3 (III:1319-1328).
- The account's outstanding corollary `9.8:cor-subsequential-limits` (III:54156-54198): under "the supplementary run
  hypothesis" and r_J >= 6(B_sharp + 1), varpi(r_J, g) <= 1, every bare x with first passage at K has
  |x - a_K| <= (3/2)(B_sharp + varpi(r_J, g)) <= (1/2) varrho_2. As printed, varpi is defined only as "the correction
  term ... that enters the first-passage offset bound" (III:54160-54161), the bound it is used to state, and the phrase
  "supplementary run hypothesis" occurs nowhere else in CA-III (grep: one hit, III:54159). So the printed statement has
  no checkable hypotheses; 3.4 below gives a precise form.

**3.2 Lemma DRIFT (PROVED GIVEN (b) of the uniqueness theorem).** Let n_* >= n_U, so that Upsilon_j <= 1/4 for
j >= n_*, and put Psi(n_*) := prod_(j >= n_*) (1 - Upsilon_j)^(-1). Then Psi(n_*) is finite and
log Psi(n_*) <= (4/3) sum_(j >= n_*) Upsilon_j, which tends to 0 as n_* grows. Let K > K_0 >= n_* and let w_K be real
with |w_K| <= r_J/(4 Psi(n_*)). For j = K-1, ..., K_0 let w_j be the solution in D(0, r_J/2) of n_j(w_j) = w_(j+1).
Then each w_j exists, is unique in that disc, is real, and
    |w_j| <= |w_K| prod_(i=j)^(K-1) (1 - Upsilon_i)^(-1) <= r_J/4 = varrho_2/2.
*Proof.* Finiteness: sum_j Upsilon_j < infinity (Upsilon_j <= C j^(-3/2) (log j)^(p_0+1)) and -log(1 - y) <= (4/3) y for
0 <= y <= 1/4. Induction downward on j, with the claim |w_(j+1)| <= r_J/4 (true at j+1 = K because Psi >= 1). On the
circle |z| = r_J/2: |n_j(z) - z| <= Upsilon_j r_J/2 <= r_J/8 < r_J/4 <= |z - w_(j+1)|. By Rouche's theorem
n_j(z) - w_(j+1) has exactly one zero w_j in |z| < r_J/2. Since n_j is real on the reals, n_j(conj z) = conj n_j(z)
(Schwarz reflection), so conj w_j is also a zero in the disc; uniqueness gives w_j real. Next
|w_(j+1)| = |n_j(w_j)| >= (1 - Upsilon_j)|w_j|, so |w_j| <= |w_(j+1)|/(1 - Upsilon_j); iterating from K gives the display,
and the product is at most Psi(n_*), so |w_j| <= r_J/4, which closes the induction. QED

**3.3 Proposition EDGE' (PROVED GIVEN (WI-theta), Lemma DRIFT's hypotheses and those of Proposition PIN (d) on the
window).** Fix theta in (0, 1) and n_* >= n_U with Psi(n_*) <= 1/theta. Assume
(WI-theta) every first-passage datum (K, beta) with K >= K_1 has beta = a_K - w with w real and |w| <= theta r_J/4.
Let K_0 >= n_*. For every first-passage datum d = (K, beta) with K >= max(K_0 + 1, K_1), put w_K := a_K - beta and let
w_(K-1), ..., w_(K_0) be the points of Lemma DRIFT. Then:
(a) every chain datum d_j := (j, a_j - w_j), K_0 <= j <= K, is a tuned datum in the comparison window |w_j| <= varrho_2/2,
    and d_K = d;
(b) each edge (d_j, d_(j+1)) is the pair of `9.1:not-centre-normalisation` at the zero residual source with u = w_j
    (run A of length j and centre zeta_*^j + w_j, run B of length j+1 and centre zeta_*^(j+1) + n_j(w_j)
    = zeta_*^(j+1) + w_(j+1));
(c) representatives are consistent: d_j is the B-run of (d_(j-1), d_j) and the A-run of (d_j, d_(j+1)), both with
    centre zeta_*^j + w_j;
(d) Phi(d) <= sup_(|w| <= varrho_2/2) Phi(K_0, a_(K_0) - w) + sum_(j >= K_0) b_j + 2 eta_9^W, where eta_9^W is the sup
    of |Delta E9| over tuned data in the window (row 1255's (V9) on the window), and b_j is row 1233's edge bound,
    uniform over u in the window because `9.1:cor-sourced-integrals` holds at every w in N'_w (III:18136-18157).
No intermediate or base datum needs to be a first-passage datum.
*Proof.* (a) (WI-theta) and Psi(n_*) <= 1/theta give |w_K| <= r_J/(4 Psi(n_*)), so Lemma DRIFT applies. (b) The
centre of the A-run at u = w_j is zeta_*^j + w_j, the run started from a_j - w_j (Step 2.1); the B-run has centre
zeta_*^(j+1) + n_j(w_j) = zeta_*^(j+1) + w_(j+1), the run of d_(j+1). (c) By (b) at j-1 and at j. (d) Row 1255
Corollary D1 along the chain, with row 1233 Lemma 3.5 on each edge at u = w_j. QED

What changes against check 1242 (L68-70) (PROVED by the proposition): the predecessor of a first-passage datum need not
be a first-passage datum; the inverse of the matching map is needed only on |w| <= r_J/4, where Rouche gives it; the
outward drift is bounded by Psi(n_*), which tends to 1. The base requirement becomes the window at one cutoff,
Phi(K_0, a_(K_0) - w) <= phi_* - sum_(j >= K_0) b_j - 2 eta_9^W for every real |w| <= varrho_2/2. By (WI-theta) this
window contains every first-passage datum of cutoff K_0 (when K_0 >= K_1), so the base set grows from those data to the
whole window at the same cutoff.

**3.4 Proposition WI: a precise form of part (a) of `9.8:cor-subsequential-limits` (PROVED GIVEN (FI-W), (MON) and
(R2)).** Let K >= 1 and assume r_J >= 6(B_sharp + 1). Write x_K(y) for the clause-(0) coupling after K steps of the bare
datum y (on the given torus), and assume:
(FI-W) for every real w with |w| < 2 r_J, x_K(a_K - w) equals the depth-zero coupling of the tuned run of length K
    started from a_K - w, that is x_K(a_K - w) = X - h_K(w);
(MON) y -> x_K(y) is non-decreasing on the bare data to which clause (0) applies;
(R2) as in 3.1, at rho = 2 r_J.
Then every first-passage datum y at K satisfies a_K < y <= a_K + (3/2) B_sharp. In particular
|y - a_K| <= (3/2) B_sharp <= (B_sharp/(B_sharp + 1)) varrho_2/2, so (WI-theta) holds with theta = B_sharp/(B_sharp + 1) < 1.
*Proof.* Step (i), the passage window. If y has first passage at K >= 1, then x_K(y) <= X + B_sharp < x_(K-1)(y), and
the upper flow bound x_(K-1) - x_K <= B_sharp (III:68709-68712 with j - i = 1) gives x_K(y) > X. So
X < x_K(y) <= X + B_sharp.
Step (ii), inside the disc. For real w with |w| < 2 r_J, h_K(0) = 0 (the pin, (J3)) and the recursion of
`9.1:def-tuned-family` give h_K(w) = w + sum_(r<K) (beta^(K)_r(w) - beta^(K)_r(0)), so by (R2)
|h_K(w) - w| <= |w|/3 and h_K(w)/w lies in [2/3, 4/3] for w != 0. By (FI-W), x_K(a_K - w) - X = -h_K(w). If y = a_K - w
with |w| < 2 r_J is a first-passage datum at K, step (i) gives 0 < -h_K(w) <= B_sharp; so w < 0 and (2/3)|w| <= B_sharp,
that is a_K < y <= a_K + (3/2) B_sharp.
Step (iii), outside the disc. Let y >= a_K + 2 r_J. For real w in (-2 r_J, -3 r_J/2], (FI-W) and (ii) give
x_K(a_K - w) >= X + (2/3)|w| >= X + r_J > X + B_sharp, and (MON) gives x_K(y) >= x_K(a_K - w) > X + B_sharp, so y is not
a first-passage datum at K. Let y <= a_K - 2 r_J. For w in [3 r_J/2, 2 r_J), x_K(a_K - w) <= X - (2/3) w < X, and (MON)
gives x_K(y) < X, which step (i) excludes.
Step (iv), arithmetic. varrho_2/2 = r_J/4 >= (3/2)(B_sharp + 1) by the floor on r_J, so
(3/2) B_sharp <= (B_sharp/(B_sharp + 1)) varrho_2/2. QED

Remarks (PROVED unless marked).
1. Under (FI-W) the pin a_K is not itself a first-passage datum at K: x_K(a_K) = X and the upper flow bound give
   x_(K-1)(a_K) <= X + B_sharp, so a_K passes at a depth at most K - 1. This matches the account's own form of the
   offset hypothesis, which places x_(K_0) in (X, X + B_sharp] (III:54832-54835), and sharpens Lemma OFF to
   1 <= delta_n <= D_*.
2. The account's varpi(r_J, g) can be read as the defect of (FI-W): if |x_K(a_K - w) - (X - h_K(w))| <= varpi for those
   w, the same proof gives |y - a_K| <= (3/2)(B_sharp + varpi) when varpi < r_J/3 (step (iii) then needs
   X + (2/3)|w| - varpi > X + B_sharp at |w| close to 2 r_J). So (FI-W) with defect varpi <= 1 and (MON) are a
   checkable version of the "supplementary run hypothesis". ARGUED: this is the reading the corollary's route intends
   (III:54190-54198: "a_n is the reference inverse coupling X plus the accumulated step shifts ... to be compared with the
   first-passage condition on x at K").
3. Part (b) of the corollary (identification of subsequential limits) is not attempted here.

**3.5 Status after Step 3.**
- PROVED GIVEN (b) of the uniqueness theorem: Lemma DRIFT.
- PROVED GIVEN (WI-theta) and the window form of Proposition PIN (d)'s hypotheses: Proposition EDGE'.
- PROVED GIVEN (FI-W), (MON), (R2) and the clause-(0) flow bound: Proposition WI, hence (WI-theta) with
  theta = B_sharp/(B_sharp + 1).
- So (EDGE) of row 1233, in check 1242's corrected reading, leaves the input list. In its place: (FI-W) on the window
  and (MON) for first-passage tops (Proposition EDGE' with WI), or (FI) at pins only (Proposition PIN with Lemma OFF).
- OPEN: (FI) (in either form) and (MON); the 9.1 hypothesis (e); the base inequality (the infrared seed).

