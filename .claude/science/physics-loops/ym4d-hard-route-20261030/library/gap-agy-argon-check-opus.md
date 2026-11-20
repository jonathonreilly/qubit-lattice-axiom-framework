lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T13:10Z

# gap-agy-argon-check-opus: cross-provider check of row 1205 (`library/gap-agy-solve-argon.md`)

Queue row 1206. Worker: Claude Opus 5.5, reasoning max, Mac mini Claude worker 2,
pinned at commit beea72f25. Lease start from `date -u` = 2026-11-20T01:10Z.
Checked file: `library/gap-agy-solve-argon.md` (row 1205, gemini-4-argon-high).
Provenance: this check is by a different provider from the author of the
checked file; it is one reader, not an independent derivation unless a
statement below says that a separate derivation was made.

## Plan (at most eight steps; each response does one step and appends)

1. Read the checked file in full, rows 1141, 1188-1190, 1196, 1205 and the
   FINISH rules (Build on published work, efficiency); list every PROVED
   statement with its line numbers.
2. Theorem 2.1, line by line.
3. Theorem 2.2, including the norm 1/256 and the Casimir gap 12.
4. Theorem 2.3 and Proposition 2.4 (volume bound on the Perron eigenvalue:
   correct? anything beyond normalization?).
5. Theorems 3.1-3.3; does 3.3 answer row 1141 as claimed?
6. Proposition 4.1.
7. Novelty: grep library/open-core.md and the FINISH rows for each
   statement, name the matching row; numeric guide only if memory allows.
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS), rating against the
   plain-brief rows 1188-1190 (checked in 1196), RESULT line.

## Step log

### Step 1. Inventory (done)

Read in full: `library/gap-agy-solve-argon.md` (343 lines at beea72f25), the
FINISH rows 1034, 1132, 1141, 1142, 1188-1190, 1196, 1205, and the FINISH
sections on building on published work, efficiency and rules. Memory was
42 percent free at the start (`memory_pressure`), below the 50 percent floor,
so no numeric job is started; every step below is by hand.

Statements labelled PROVED in the checked file, with lines:

| Id | Lines | Claim in one line |
|---|---|---|
| S1.1 | 19-25 | PROVED GIVEN rows 1161, 1179, 1183: gap clause splits into the continuum datum, (N-phys), and (BS) is needed for (W) only |
| T2.1 | 68-81 | A*A / AA* isospectrality of F_+ and the electric sandwich; identity (2.3) |
| T2.2 | 87-109 | Peter-Weyl selection rules; Casimir gap 12; C_E norm a_2^4; W_E norm 1/256 on the neutral complement |
| T2.3 | 115-127 | Courant-Fischer bounds (2.7)-(2.9) |
| P2.4 | 131-154 | lambda_0 <= ||M||_inf^2 exp(-c_0 n^3); ratio (2.10) >= 1 |
| T3.1 | 179-194 | integration by parts (3.1)-(3.3) from Identity STAR (3.4) |
| T3.2 | 208-232 | marginal equations (3.7); 2-link read sets; "6 raised to 9" |
| T3.3 | 242-269 | tree-transport frame: (3.10)-(3.14) |
| P4.1 | 284-302 | Le Cam chain (4.1)-(4.3); threshold (4.4) |
| S4.2 | 308-315 | comparison-model table, labelled PROVED |

Note on the FINISH summary of row 1205: it names "a magnetic-variance ratio
Theta_mag" and "OPEN: uniform-in-n bounds on Theta_mag". The file at
beea72f25 has no Theta_mag; the nearest object is the covariance term of
(2.7). This check reads the file as it stands.

### Step 2. Theorem 2.1 (lines 68-81): HOLDS; part (1) not new, part (2) one line

Re-derivation. C_E is the tensor product of convolutions by the class function
h_beta, so it commutes with left and right translations, hence with gauge
transformations and with the centre flips (multiplication of cut links by -I).
M is a gauge-invariant, flip-invariant multiplier. On H_00 = P_+ P L^2(H) the
operators P, P_+ act as the identity, so A := C_E^(1/2) P_+ P M equals
C_E^(1/2) M there, its adjoint inside H_00 is M C_E^(1/2), A*A = M C_E M =
F_+ on H_00, and AA* = C_E^(1/2) M^2 C_E^(1/2) = Ftilde_+. Trace class: c_beta
has eigenvalue a_d = I_d(beta)/I_1(beta) with multiplicity d^2 on the spin
(d-1)/2 block (character expansion of e^(beta cos theta)), the sum of d^2 a_d
is finite, and C_E is a finite tensor product. Nonzero spectra of A*A and AA*
agree with multiplicity, so (2.2) holds for every u >= 1, and
||A psi_0||^2 = <psi_0, F_+ psi_0> = lambda_0 normalizes phi_(1/2). For (2.3):
<f, P_0 f>_pi = lambda_0^(-1) <psi_0 f, M C_E M psi_0 f>_H, and f = 1 gives
lambda_0 = <M psi_0, C_E M psi_0>_H. Here psi_0 is bounded above and below
(C_E has a continuous kernel bounded above and below; M is bounded above and
below), so L^2(pi) and L^2(H) are the same set. First failing step: none.

Inputs taken, not re-derived: simplicity of lambda_0 and positivity of psi_0
(Perron-Frobenius for the positive kernel, row 1161 lines 22-23).

Remark (wording, line 54). "No unknown ground-state density in the inner
product" is true of the inner product only: psi_0 sits in the vector
xi_f = M psi_0 f. The unknown is moved, not removed.

Novelty. Part (1) is the swap of the magnetic sandwich M^(1/2) K M^(1/2) for
the electric sandwich K^(1/2) M K^(1/2), on file in row 875
(`gap-exc-astra.md` L367, "use the isospectral transfer"), row 914
(`gap-target-check-astra.md` L261-264), row 934 (`gap-vacsub-max.md` L491)
and row 1155 (`gap-solve7-astra62.md` L222, "half-electric sandwich").
Part (2) is row 1161's ground-state transform P = psi^(-1) U psi written in
Haar coordinates. Verdict: HOLDS; not new; trivial.

### Step 3. Theorem 2.2 (lines 87-109): HOLDS AFTER CORRECTION (the "iff" at n = 4); bounds (2.4)-(2.6) HOLD; not new in substance

Re-derivation of the selection rules. In the block V_j = tensor over e of
V_(j_e) (x) V_(j_e)^*, the vertex gauge average projects onto invariants of
the tensor product of the incident factors. An invariant vector needs an
integer spin sum at x (-I acts by (-1)^(sum 2 j_e)) and no vertex with exactly
one nonzero incident spin. The cut flip C_mu acts on V_j by
(-1)^(sum over cut_mu of 2 j_e). So S(j) has minimum degree 2 and contains a
simple cycle; the torus (Z/nZ)^3 with n even and n >= 4 is bipartite and
simple, so every cycle has length at least 4. All this HOLDS.

Correction (line 90, the "iff"). At n = 4, which the setting allows
(4 | n, n >= 4), a straight line winding once around the torus is a simple
4-cycle that is not a plaquette boundary. Counterexample: the adjoint
Polyakov line chi_1(U_e1 U_e2 U_e3 U_e4) along such a line. It is gauge
invariant, has mean zero, has spin 1 on four edges (vertex sums 2, integer),
and crosses cut_mu once with spin 1 (integer), so it lies in H_00^perp with
|S(j)| = 4 and S(j) not a plaquette. Repair: the "iff" holds for n >= 5
(with 4 | n: n >= 8); at n = 4 add the winding lines. The bounds are not
affected: on that block the Casimir sum is 4 x 8 = 32, the electric
multiplier is a_3^4 < a_2^4, and the commutator multiplier is 9^(-4).

Bounds. Each nonzero block in H_00 has at least 4 edges with d_e >= 2, so
the Casimir sum is at least 4 x 3 = 12, the electric multiplier
prod a_(d_e) is at most a_2^4, and the commutator multiplier prod d_e^(-2) is
at most 4^(-4). All three are attained by w_q = (1/2) Tr U_q, which is gauge
invariant, centre neutral (a spatial plaquette has 0 or 2 links on each cut)
and of mean zero. The eigenvalue d^2 - 1 = 4j(j+1) of the unit-S^3 Laplacian
and the Frobenius multiplier d^(-2) of the Haar commutator law are correct, so
W_e = (1 - Delta_e)^(-1). Monotonicity a_d strictly decreasing in d >= 1:
on file, row 1192 L122 (I_(j+1)/I_j < 1 as the mean of u under a positive
weight, from GL3 of Sussman and Alpoge, with Claude and Codex as authors of
their text); the file cites "Section 6 of row 1192", but the proof is at
L122. First failing step for (2.4)-(2.6): none.

Novelty. The cycle-support argument, the four-edge minimum, and the bound of
the electric multiplier by its largest one-link value to the fourth power are
in row 1132 (`gap-council-op-astra.md` L98, "any nonempty support contains a
cycle, with at least four edges on these cubes ... their product is at most
(13/20)^4"). The commutator multiplier (2j+1)^(-2) and ||W_E|| = 1/4 on
L^2_0(H) are row 1132 L37, and 4^(-4) on plaquette traces is row 1132 L64. New
here are only the exact norm values (attainment by w_q), the Laplacian form
of the same count (Casimir 12) and the cut-parity rule. These are one-line
consequences. The improvement from 1/4 to 1/256 moves no consumer: statement
(A) of row 1132, which is what reads W_E, fails at one step (row 1132 L61-64)
and stays open. Verdict: HOLDS AFTER CORRECTION (the "iff" at n = 4);
(2.4)-(2.6) HOLD; not new in substance.

### Step 4. Theorem 2.3 (lines 115-127) and Proposition 2.4 (lines 131-154)

**Theorem 2.3: HOLDS; the bounds (2.8) and (2.9) are vacuous on large cubes at every beta.**

Re-derivation. For f in V_0, int M psi_0 f dH = 0, so xi_f lies in
H_00^perp, and (2.3) with (2.5) gives (2.7); the split into mean and
covariance is an identity, with int M^2 dpi = ||M psi_0||_H^2. On H_00 seen
inside L^2(pi), P_0 is self-adjoint and unitarily equivalent (f -> psi_0 f) to
F_+/lambda_0, so its eigenvalues are lambda_i/lambda_0. Min-max: for any
subspace of codimension c <= k, the k-th eigenvalue (counted from 0) is at most
the supremum of the Rayleigh quotient on that subspace. V_0 = W_12 has
codimension 1, since every nonzero block of H_00 has Casimir sum at least 12;
W_Lambda has codimension at most N(Lambda), which counts the j = 0 block.
First failing step: none.

What it says. Claim: for every closed subspace W of H_00 of finite codimension
k, sup over W of int M^2 f^2 dpi / int f^2 dpi = ||M||_inf^2 = e^(3 beta n^3).
Proof: for delta in (0, 1), the k + 1 sets
A_i = {(1 - delta(i+1)/(k+1)) ||M||^2 < M^2 <= (1 - delta i/(k+1)) ||M||^2}
are disjoint, gauge and flip invariant (M is), and of positive Haar measure
(M^2 is continuous on a connected space and takes every value in
[(1 - delta) ||M||^2, ||M||^2], the top one at U = 1). Some nonzero
combination of their indicators lies in W, and its quotient is at least
(1 - delta) ||M||^2. QED. So the right side of (2.8) equals
a_2^4 ||M||_inf^2 / lambda_0, which is at least a_2^4 exp(c_0 n^3) by (2.11).
It exceeds 1, the trivial bound, as soon as c_0 n^3 > 4 log(1/a_2). The same
holds for (2.9) unless alpha(beta, Lambda) < exp(-c_0 n^3). Products of w_q
over k edge-disjoint plaquettes lie in H_00^perp with Casimir sum 12k and
multiplier a_2^(4k), so alpha(beta, Lambda) >= a_2^(4 ceil(Lambda/12)). Hence
(2.9) can be below 1 only for Lambda of order n^3. At such Lambda, N(Lambda)
counts all products over fewer than Lambda/12 of the n^3/2 plaquettes of one
edge-disjoint family, a number exponential in n^3. An eigenvalue of that index
does not bound s_+. The file says the volume factor is the obstruction
(line 129, line 338). The new point here is the size: equality, not only
growth. Novelty: min-max against the electric operator is row 1180
(`gap-mini-neutral-fable.md` L167-169, R4: "the bound exceeds lambda_0^u by a
factor exp(c u n^3)"). Verdict: HOLDS; vacuous for the gap; not new in kind.

**Proposition 2.4: HOLDS. It is correct, and it says nothing beyond
normalization. Same statement as row 1180 Lemma R4, with a proof that needs
no McDiarmid inequality and a better constant at large beta.**

Re-derivation, line by line. (2.10): 0 < C_E <= 1 and lambda_0 =
<M psi_0, C_E M psi_0>. (2.11): M C_E P M = M C_E^(1/2) P C_E^(1/2) M <=
M C_E M in form order; the kernel M(U) C_E(U,V) M(V) is symmetric and
nonnegative, so the Schur test with the constant test function bounds the
norm by ||M||_inf sup_U (C_E M)(U). (c_beta phi)(g) = E phi(g xi), with xi of
density h_beta, by the substitution u = g xi and centrality of h_beta. For
even n, the plaquettes of one orientation split by the parity of the two
in-plane coordinates into two classes of n^3/2 pairwise edge-disjoint
plaquettes (plaquettes of one orientation share an edge only with in-plane
nearest neighbours, which have the other parity), so the six families are
correct. Hoelder with six exponents 6 turns (beta/2) into 3 beta. Within a
family the w_q(U xi) are independent. E xi = a_2 I and E xi^(-1) = a_2 I, so
by multilinearity E w_q(U xi) = a_2^4 w_q(U). The chord bound
e^(3 beta x) <= cosh 3 beta + x sinh 3 beta on [-1, 1] and the algebra
cosh 3b + r^4 sinh 3b = e^(3b) [1 - (1 - r^4)(1 - e^(-6b))/2] are right. The
six geometric means multiply back to e^(3 beta n^3/2) B^(n^3/2), and
1 - y <= e^(-y) gives c_0 = (1 - r^4)(1 - e^(-6 beta))/4. First failing
step: none.

Beyond normalization? No. log lambda_0 is the vacuum free energy of one time
step (in units where the electric kernel is a probability kernel), and
||M||_inf^2 = e^(3 beta n^3) is the largest value of the spatial weight. So
(2.11) says only that the free energy per site is at most 3 beta - c_0(beta):
the vacuum does not freeze the spatial plaquettes at w_q = 1. It carries no
spectral information above lambda_0. The same proof holds verbatim for
compact U(1) at large beta, which is gapless (the file's own table, line 312,
says Proposition 2.4 holds there). Its only use is the one above: a one-step
bound normalized by ||M||_inf^2 loses exp(c_0 n^3).

Novelty. Row 1180 Lemma R4 (`gap-mini-neutral-fable.md` L208-227, PROVED,
"uses the bounded-difference inequality of McDiarmid, cited, not rebuilt")
proves lambda_0(F) <= 4 ||D||^2 exp(-2 c_4 n^3) with
c_4 = min{(3/256)(1 - r^4)^2, (3/4) beta (1 - r^4)}, from the same mean
identity E w_p(x xi) = r^4 w_p(x) and the same Schur test, for the same
purpose. Proposition 2.4 is that lemma with a self-contained proof (no cited
concentration inequality) and an exponent linear rather than quadratic in
1 - r^4. Since 1 - r^4 is about 6/beta at large beta, the exponent improves
from order beta^(-2) to order beta^(-1). It is a small real improvement of an
on-file statement, not a new statement.

