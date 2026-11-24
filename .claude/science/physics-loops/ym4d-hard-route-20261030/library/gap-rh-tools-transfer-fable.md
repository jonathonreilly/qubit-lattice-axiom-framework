lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T03:54Z

# gap-rh-tools-transfer-fable (FINISH row 1481)

Worker: Claude Fable 5.2, high effort, Mac mini worker 3. Started 2026-11-24T15:54Z (date -u). Pinned commit b519804ce. No subagents. No numeric job started so far.

Question (owner, 2026-11-24): does any tool of the Alpoge-Claude proof of the Riemann hypothesis apply to the four-dimensional SU(2) mass-gap crux?

Credit: the RH argument is Levent Alpoge's (with Claude). The account read here is Michael Rubinstein's explainer `zeta-paper_v2.tex` (with Claude, Codex and Gemini). The continuum limit and its Lean development are Ethan Sussman's and Levent Alpoge's (with Claude and Codex).

Claim marks used below: **proved** (argument written here in full), **read** (taken from a source, with file and line), **sketched** (argument outlined, steps missing), **guessed** (no argument).

## 0. Plan (written first, per the save protocol)

1. Read FINISH.md head, GOAL.md, and the crux notes the row names. State the crux in one paragraph with file and line.
2. Read `~/ym4d-papers/alpoge-rh/`: the announcement `remark.pdf`, the verification pages, then the explainer `zeta-paper_v2.tex` in order, section by section. For each step record: proved, reduced or taken from the literature.
3. List the tools of the proof. For each tool write a candidate transfer lemma for the crux, then test it against the selectivity filter t1-t6 (rows 1386, 1442) and against closed rows (grep `library/open-core.md` and FINISH).
4. Decide outcome (A) or (B). End with the next two rows.

Status of each step is appended below as it finishes.

## 1. The crux, as read (step 1 done, 2026-11-24T16:0xZ)

All lines below are **read** from this checkout at b519804ce; nothing is re-proved here.

- Consumer. `library/gap-k2-tool-design-fable.md` 3.1 (lines 99-124): Z^z(v) = Tr(C_z T^v), Z_+(v) = (1/8) sum_z Z^z(v) = Tr(P_0 T^v), P_K = Z_+(2u)/Z_+(u)^2. Fact PUR: P_K >= 457/625 gives s_K(u) <= 4/21. (PUR-io): P_K >= 457/625 at infinitely many K for one l and one g_0 gives a gapped calibrated limit with rate at least (2/l) log(2^18/5041) (rows 1461, 1462, 1465).
- In eigenvalue form: with r_i in [0,1] the ratios of neutral eigenvalues of T to the vacuum eigenvalue, P_K = (1 + sum r_i^(2u)) / (1 + sum r_i^u)^2. So the crux is an upper bound on the positive sum s = sum_{i>0} r_i^u, a trace of a positive operator minus its top eigenvalue. Each Z^z is a positive number; the signs sit in the centre characters of the sixteen-fold sum and in the perturbative drift, not in the terms of s.
- The wall. Row 1468 4.3: (K2-STEP), with (DR) x_(k+1) <= x_k - delta_0 (a sign), (TR) a contraction of the tube radius, (WR) wrap error. Row 1468 4.4 Proposition GA: the Gaussian abelian readout of Q2 is x' = 2^(d-4) x, so in four dimensions every drift is non-Gaussian; the one-loop SU(2) drift is -(11/(3 pi^2)) log 2 = -0.2575 per side-2 step (sketched there).
- Sizes. Row 1470: the release's clauses force x above 2^3457; Balaban gives no number. Row 1472 with check 1478: the pointwise small-field step for Q2 fails below x about 1e4 (cubic term taken in supremum before integration). Row 1471 with check 1473: the end class is closed by hand only for beta below log(1 + 1/(42 e)) = 0.00872. Row 1474: no representation in which one order-one step is a finite statement of known cost; six candidates fail at named lines; Lemma NG (noise map, gradient decay e^(-2t) from Ricci curvature 2 of SU(2), factor 1 for U(1)) is proved by hand there and is not an end class. Row 1469: closed classes at order-one coupling exist on file (rows 1345, 1348, 1418) with the environment integration open (row 1475 running).
- Filter. Row 1386 (t1)-(t5), row 1442 (t6): a mechanism must give no gain for compact U(1) in d = 4 at weak coupling, none for Villain U(1), none for SU(2) in d = 5 at weak coupling. Remark PAIR (row 1386, credited to row 1128): a mechanism is a group-reading local gain times a dimension-reading exact carry; the lane has gains and lacks a carry with a sign at order-one coupling. Reopen triggers on file: R1-R3 (row 1442), R4-R6 (row 1474).
- Rule that binds this row. "Equivalent is not progress" (FINISH Rules) and (t5): a sufficient condition equivalent to the seed is no progress.

What a transfer from the RH proof must therefore supply, in the words of the record: K-I (an exact carry with a sign for a typical-field stiffness) or K-II (a renormalisation step at order-one coupling), or a finite certificate of known cost for the stretch from readout about 2.3 to beta below 0.0087.

## 2. The sources, as read

Files read (read only, under `~/ym4d-papers/alpoge-rh/`): `remark.pdf` (4 pages, all), `lean-blog.html`, `rubinstein-index.html`, `drew-grh.html` (first 14,000 characters of text: the summary, the check table, the five theorems), `zeta-paper_v2.tex` (13,700 lines; progress is recorded below by line range).

### 2.1 Standing of the proof (read)

- The proof exists as a Lean library: 175,187 files, about 17 million lines (`rubinstein-index.html`). The Lean FRO and Mathlib Initiative statement (`lean-blog.html`, 2026-11-21) certifies statement and proof. Sutherland's page (`drew-grh.html`) records: all modules compile, the five theorems depend on `propext`, `Classical.choice`, `Quot.sound` only, the full export is accepted by Lean's kernel, nanoda, con-leche, con-ron, lean4lean. Five modules needed a raised step limit for `decide +kernel` computations in lean4lean. Scope: RH and GRH for Dirichlet L-functions; not Dedekind, Hecke or automorphic L-functions.
- No human-readable proof exists. The explainer says so of itself (lines 61-88, 112-138): it deduces RH from (M) and Estimates B and C; it proves B and C from cited theorems; it reduces (M) to thirteen numbered hypotheses, "none of them is proved outright here". So for this row every statement about the inside of (M) is **read from an explainer of a Lean development**, not checked here against the Lean files (which are not on this machine).
- Announcement (`remark.pdf` pages 3-4): twenty steps, found 2026-10-06 to 2026-11-16. Footnote 5 names Balaban's induction ("after gritting with Sussman through Bałaban's fantastic induction"), as a remark on difficulty, not as a tool of the RH proof.

### 2.2 The argument, Part I of the explainer (lines 1-1330, read in full)

Skeleton (line 230): (M), B, C => Estimate A => G(x) <= x^(1/2+eps) on long intervals => RH.

| # | Step | What it says | Status in the explainer |
|---|---|---|---|
| S1 | Zeros to primes (I.1; II.1) | G(x) = sum_{n<=x} Lambda(n)(x/n - 1) - x log x + (1+gamma)x. Mellin transform F(s) = -zeta'/zeta(s)/(s(s-1)) - 1/(s-1)^2 + (1+gamma)/(s-1). If G(x) <= x^theta on [Y, Y^(3/2)] for arbitrarily large Y, zeta has no zero in Re s > theta. One-sided: only an UPPER bound is needed. | proved (Landau's theorem on transforms of functions of one sign; on intervals by high derivatives of F, lines 1340-1361) |
| S2 | Chebyshev's principle (I.2) | Nonzero integer Delta with p^(e_p) dividing Delta gives sum e_p log p <= log abs(Delta). "It always points the same way: it bounds primes from above." Lattice form: for an injective map T: L -> M with T(L) inside p^e M, e log p <= log norm(T) + mu_max(M) - mu(L) (slope inequality, Bost; Stuhler, Grayson). | elementary case proved; lattice form proved in the form needed (III, Lemma M3) |
| S3 | Smooth divisibility (I.3-I.4) | Derivatives of order a of CM functions are divisible at inert primes by p^e, e >= a(1/p + 1/p^3 + ...) - 1 (lemniscate: Theorem Le18). Mechanism: the formal group has height two at inert primes; the logarithm is X + X^(p^2)/p + ...; a! gains a/(p-1), the inverse series loses a/(p^2-1). With a weight w: (a/p^h - w)_+ = w (x/p^h - 1)_+ at x = a/w: the ramp of G. b = exp(x^eps), a about x b. | lemniscate proved; for the theta kernels of the proof conditional on hypothesis (B), quoted from Lean |
| S4 | Size through the linear term (I.4.2, I.7) | Squared Gaussian norm: norm(z^a)^2 = a!. So log of squared size is a log a + O(a), and the O(a) term is computed exactly: log Omega = gamma + log(2 pi/sqrt d) - L'/L(1, chi_d) (Kronecker limit formula; Lerch, Chowla-Selberg), Siegel mass, Weyl dimension, Rallis inner product. The linear terms of size and of divisibility agree: "that the two sides produce the same linear term is the reason the method can work at all" (line 974). | quoted (eleven inputs) |
| S5 | Denominators (I.7) | The chain of lifts need not keep integral lattices. Lattices are glued prime by prime using twists by characters (seesaw: the final period does not depend on the twists). The cost is bounded by lengths of Galois cohomology groups ("a weakening of Vandiver"); bound sqrt b. | quoted |
| S6 | Rank (I.7) | One map controls only mu_max of the target. Many maps; a relative trace formula bounds a second moment, so sum of T* T is near a multiple of the identity; then the images fill the target and the MEAN slope is controlled. | linear algebra proved; trace-formula statements quoted |
| S7 | Balance (I.8) | Errors x/m (made once at the ends, divided by the m-fold gain) and m (accumulated over m lifts). Balance at m = sqrt x. With cost m^2 one gets only Re s > 2/3. | proved from the form of (M) |
| S8 | Inert primes to all primes (I.5-I.6) | The table: 2 rows (chi_q), n columns (classes mod N = 4n). (M) is an average over translates u, labels t, repetitions j of P - M <= error. Averaging over translates leaves (1 + chi_q)(1 - chi_d) = 1 + chi_q - chi_d - chi_q chi_d, so R_{q,d} = G + G_{chi_q} - G_{chi_d} - G_{chi_q chi_d}. Estimates B (the three twists are at most x^(1/2+eps) for well-chosen huge q, d: mean-square over moduli, zero-density) and C (other cells at scale exp(x^(eps/3)): zero-free region). | proved from cited theorems (III.1-III.3) |

The announcement's steps 4 and 6 (positivity W(f) >= 0 in Weil's explicit formula from a determinant) are "an earlier form of our first step" (line 1085); the final argument uses the Landau-type lemma S1 instead. The announcement's "sign-only proof of Weil and Deligne" (q N = M^k + R) is "largely absent from the final proof" (line 1102).

What is new, in the explainer's words (line 1218): "iterated theta lifts as a source of multiplicity, the comparison of divisibility with size through slopes of lattices carried to the term linear in the order, and the resulting one-sided bound for G(x)".

### 2.3 Part II of the explainer (lines 1328-1976, read in full)

- II.1 (lines 1340-1361), **read, proof complete there**. The one-sided criterion on intervals. A_j(s) = (-1)^j F^(j)(s)/j! = integral of g(u) e^(-itu) u^j e^(-sigma u)/j! du. The kernel u^j e^(-(sigma-2)u) concentrates on the window [U, 3U/2] when j is nearest to (5/4)(sigma - 2)U. Then abs(A_j(sigma+it)) + A_j(sigma) <= 2 integral of max(g,0) K_j, by abs(g) + g = 2 max(g,0). A pole to the right of theta forces abs(A_j) >= c d^(-j) at a point with a unique nearest pole. Contradiction. So: a one-sided bound on a window, plus an a priori two-sided bound outside (Chebyshev), excludes singularities of a transform.
- II.2, **read**. Stepanov's count: zeros of multiplicity m of a function of degree D number at most D/m. Integer form: sum e_p log p <= log abs(Delta). Local model of the odd powers of p.
- II.3-II.5, **read, proofs complete there**. Exact identity P - M = sum_i w_i R_i(a/w_i) (II.24); translation average (II.29)-(II.30) gives (delta b/2) R_{q,d}; Estimate C discards the non-distinguished cells; result (II.36): (1/n) sum (P - M) = B R_{q,d}(x) + O(B(1 + log x)). "Only an upper bound follows" (line 1660).
- II.6, **read; elementary parts proved there, arithmetic inputs quoted**. (6.2) chain integrality; (6.4) Hasse product rule: a determinant absorbs one derivative per direction, so the gain at scale p^h is (a/p^h - w_h)_+; factorial count (II.48) by Legendre's formula. (6.5) Cauchy-Schwarz in the Fock norm. (6.6)-(6.7) the linear term: the size bound gives log a - 1 - log Omega_E, the count of forms (mass times Weyl dimension, with the factorials cancelling, (II.57)) gives -<log w> - log v + log pi, and the Chowla-Selberg identity (II.54) turns the sum into log a - 1 - gamma + c_{chi_d} - <log w>, which is the main term M of the prime sum. "An uncancelled constant per derivative ... would leave an error at least of order x" (line 1875). (6.8) slope inequalities mu(L) + (1/r) log[M : T(L)] <= mu(M) + log norm(T); gluing of local lattices (CRT over Q; over E with twists, quoted); the denominator bound sum_l log l sum_a h_{l,a} <= sqrt b (II.shabound, quoted). (6.9) Lemma (FrameLA): if sum norm(K_i - I)_HS^2 <= e S and tr(Q^2) <= (1 + eta)(tr Q)^2/D then codim(sum B_i U_i) <= (eta + 4 alpha + 4 sqrt e) D; proved there in ten lines from rank Q >= (tr Q)^2/tr(Q^2). (6.10) layer-cake formula (II.69) turns the count of slopes below a level into a bound for the MEAN slope.

