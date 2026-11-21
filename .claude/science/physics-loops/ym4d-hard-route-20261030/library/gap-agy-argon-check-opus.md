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
1 - r^4. Since 1 - r^4 is about 6/beta at large beta (GUIDE: large-argument
Bessel asymptotics, not derived here), the exponent improves from order
beta^(-2) to order beta^(-1). It is a small real improvement of an
on-file statement, not a new statement.

### Step 5a. Theorem 3.1 (lines 179-194): HOLDS given (REG); not new (row 1034 STAR)

Re-derivation of (3.4). Write div_l(Y) := sum_a R_(l,a) Y^a. LINK (row 1034
L65): c_l = -e^(-A) div_l(e^A n_tail(l)). The gauge generator at z is
G_a = sum_out R_(l,a) - sum_in sum_b Ad(U_l)_(ba) R_(l,b) (the in-link
action U_l -> U_l e^(-eps e_a) = e^(-eps Ad(U_l) e_a) U_l). It is Haar
divergence free, G_a A = 0, and covariance gives G_a n_z = 2 e_a x n_z. Since
sum_b R_(l,b)(Ad(U_l) w)^b = sum_b (2 e_b x Ad(U_l) w)^b = 0 for fixed w,
sum_a G_a(e^A n_z^a) = 0 becomes
sum_out div_l(e^A n_z) = sum_in div_l(e^A Ad(U_l) n_z). With LINK on every
link at z this gives rho_z = -e^(-A) sum_in div_l(e^A D_l n), which is (3.4).
Then (3.1) is one integration by parts against e^A dU (left-invariant
derivatives are Haar skew-adjoint); the step across the frame's singular set
is exactly what (REG) supplies (row 1034, `gap-aligned-frame-check-opus.md`).
(3.2) drops the terms with R_(l_kappa) F_mu = 0. (3.3) is Riesz duality, with
C^1 dense in L^2(mu_b). First failing step: none.

Novelty. Row 1034 L70-75 states STAR and its reading: "(J) at z reads
sum_in sum_a R_(l,a)(e^A (D_l n)^a) = 0: the field Y_z = sum_in (D_l n) . R_l
preserves mu", with "this sum equals -e^A rho_z". Equation (3.1) is that
sentence in weak form (rho_z is minus the mu-divergence of Y_z). Verdict:
HOLDS; not new; trivial given STAR.

### Step 5b. Theorem 3.2 (lines 208-232)

**(1) HOLDS as an implication; "decouples" is wrong as an equivalence.**
Integrating rho_z e^A over the three other in-links kills their divergence
terms (Haar invariance of each integrated link), so rho_z = 0 on
Omega' x SU(2)^in(z) implies the four marginal equations (3.7). I checked the
plaquette bookkeeping: each in-link lies in 6 plaquettes, 6 backward
plaquettes p^-_(kappa lambda) carry two in-links, 12 forward plaquettes
p^+_(kappa nu) carry one (24 = 12 + 12), so A = Re(U_l_mu S^+_mu) +
A^0_(in,mu) + A_ext as written. The converse fails at the level of the
equations: a field Y = f(U_l2) g(U_l1) v . R_l1 with int f = 0 and
div_l1(g v) != 0 has every one-link marginal zero but div Y != 0. The file
gives no argument that the frame form restores the converse. So the four
equations are necessary conditions, not a decoupled form of conservation.
Section 5.2 item 2 (line 339) asks whether a frame "can satisfy (3.7) in all
four directions". That is not the conservation problem: a frame satisfying
(3.7) need not conserve its current.

**(2) HOLDS, with a stronger hypothesis than row 1034 PRIV and a weaker
conclusion.** I checked by the incidence list that P_(mu nu) = (z - e_mu +
e_nu, mu) and Q_(mu nu) = (z - e_mu, nu) lie, among all plaquettes that
contain an in-link of z, only in p^+_(mu nu). For P: the plaquettes
(y; mu, lambda), (y - e_lambda; mu, lambda), y = z - e_mu + e_nu, contain the
in-link l_mu only for lambda = nu. For Q: the plaquettes (w; nu, lambda),
(w - e_lambda; nu, lambda), w = z - e_mu, contain l_mu only for lambda = mu.
So A^0_(in,mu) does not read U_P or U_Q. If n_z and n_(z - e_mu) do not read
U_P, then W^0 and its divergence do not read U_P, and w . Im(X U_P^(-1) Y)
constant on an open set of U_P forces w = 0 (Im is a local diffeomorphism
where Re g != 0). Same for U_Q. First failing step: none.

Comparison with row 1034 PRIV (`gap-sym-reg.md` L214-229). PRIV assumes that
five frames (n_z and the four n_(z - e_kappa)) do not read U_P, which gives
the five-link set F_(mu nu), and concludes D_l n = 0 pointwise wherever
rho_z = 0 on a set of positive measure. Theorem 3.2 (2) assumes it of two
frames (n_z, n_(z - e_mu)), which gives the two-link set F^(2)_(mu nu) inside
F_(mu nu). It needs rho_z = 0 on a set that contains whole fibres
SU(2)^in(z), and it concludes only the marginal W^0 = 0. The transverse link
Q (sets G^(2)) is a second private link of the same forward plaquette, by the
same proof; this is a small new remark.

**(3) The implication HOLDS; the claim "the Lemma O1 threshold rises from 6
to 9" FAILS for general site frames (lines 168, 219, 331, 339, 342).** The
twelve sets F^(2)_(mu nu) are pairwise disjoint (direction mu; for fixed mu
the six base points -e_mu + e_nu, e_nu are distinct), so reading one link of
each F^(2)_(mu nu) for three directions mu and all nu needs 9 links. That
count is right. The failing step is the premise in the parenthesis at
line 219: Corollary P of row 1034 reaches a contradiction from D n = 0 on all
links of two directions (telescoping, row 1034 L236-240). Theorem 3.2 gives
only W^0 = 0, and W^0 = 0 implies D_(l_mu) n = 0 only when n_z and
n_(z - e_mu) do not read the other three in-links of z. Without that, a
frame can have W^0 = 0 with D_(l_mu) n != 0, and Corollary P does not start.
Correction: the 9-link bound holds for translation-invariant frames whose
read set avoids (-e_kappa, kappa) and (e_mu - e_kappa, kappa) for
kappa != mu, with conservation on sets that contain whole in-link fibres. For
general site frames the proved necessary condition stays row 1034's six
links (L252-255). No counterexample to "9" is possible at present: no site
frame with (J) is known (Lemma O1 is open).

### Step 5c. Theorem 3.3 (lines 242-269)

**(1) HOLDS, trivial.** For a tree edge l = (x -> y), P_x = U_l P_y in
either orientation, so n_x = Ad(U_l) n_y at the same U and D_l n = 0.

**(2) (3.10) HOLDS, and it is row 1141 (10). (3.11) HOLDS AFTER CORRECTION:
its sign is wrong.** Convention: rho_z = sum_in c - sum_out c, so
div Y(z) = sum_out Y_l - sum_in Y_l for every link field Y. In tree gauge
n = v at every site. Gauss identity G_a A = 0 gives sum_out N_l =
sum_in Ad(U_l)^(-1) N_l, so div j(z) = v . sum_in (Ad(U_l)^(-1) - I) N_l,
and tree in-links drop since U_l = 1; this is (3.10), identical to row 1141
L152-157. For div d, two independent derivations give the opposite sign to
(3.11):

- Direct. P_tail(l) depends on U_l at most by left multiplication, whose
  contribution is sum_a [e_a, n]^a = 0, so in tree gauge
  d_l = sum_a (R_(l,a) v)^a. The root axis v is invariant under the gauge
  generator at z != r (and at z = r, G_a v = 2 e_a x v, whose summed trace
  is zero), so sum_out sum_a (R_(l,a) v)^a = sum_in sum_b (Ad(U_l) R_(l,b) v)^b.
  Hence div d(z) = - sum over l in in(z) \ T of
  sum_a ((I - Ad(U_l)) R_(l,a) v)^a.
- From the file's own (3.15). Its first sum is v . B_z = div j by (3.10), so
  its second sum, + sum sum_a R_(l,a)(D_l n)^a, equals div(j - d) - div j =
  - div d.

Corrected (3.11): div d^(T,v)(z) = - sum over l in in(z) \ T of
sum_a ((I - Ad(U_l)) R_(l,a) v)^a. The sign does not enter (3.12)-(3.14).
The statements "outgoing and incoming tree-link derivatives cancel" and
"both divergences vanish where in(z) is inside T" HOLD.

**(3) (3.12) HOLDS.** At most 4 chords x 3 components, each term at most
2 |R_(l,a) v|, Cauchy-Schwarz gives 12 x 4 = 48, and each chord has one head.

**(4) (3.13) and (3.14) HOLD, not sharp.** With |X|^2 <= 2|X - Y|^2 +
2|Y|^2 and (3.12), (1/V) sum |div(j - d)|^2 + (48/V) sum_chords |R v|^2 >=
(c/2) b^2; the file's 96 is weaker and true, and (3.14) holds with c/192 in
place of c/384. The use of row 1141 (9) pointwise for a field-chosen axis is
right: j_l reads only frame values, and row 1141 (9) is stated with "the tree
and the axis ... selected after seeing all links" (row 1141 L150; checked in
row 1142).

**Does Theorem 3.3 answer row 1141 as claimed (lines 169, 332, 342)? No.**

1. Row 1141's open leaf is "H with a general field-dependent frame: OPEN.
   The signed force and Jacobian can cancel" (row 1141 L224), recorded in
   `parts/gap.md` L190 as "Open: a general frame whose Jacobian cancels the
   signed defect". Theorem 3.3 treats only tree transports of a field-chosen
   root axis. Row 1141 already covers that class in (9) and (13), and already
   writes the Jacobian split: "If h_e is the Jacobian current of a smooth
   frame, replace the first norm in (13) by the sum of ||div(j - h)||_2 and
   ||div h||_2" (row 1141 L208-209). General frames, at positive distance
   from every tree transport, are not touched.
2. Inside the class, (3.14) is a necessary condition, not an obstruction. It
   asks for chord-gradient energy of order V, that is, order-one sensitivity
   of the axis to a positive fraction of the chords. Such axes exist. GUIDE
   example, by hand: v(U) = Im W_g(U) / |Im W_g(U)|, with W_g the holonomy
   of a loop g based at the root that runs through a positive fraction of
   the chords, is covariant at the root, smooth off the null set
   {W_g = +1 or -1}, square integrable in gradient there (|R v| ~ 1/r in
   three transverse dimensions), and has order-one derivatives along the
   chords of g. The file proves no cost attached to that energy in any
   consumer, and it does not show that cancellation is impossible.

What is new: the explicit Jacobian divergence (corrected sign) and the
chord bound (3.12) for this class, which make row 1141's ||div h|| explicit.
That is a small, correct addition. The question of row 1141 stays OPEN, also
for tree transports with a field-chosen axis.

### Step 6. Proposition 4.1 (lines 284-302), Section 1.1 (lines 19-25), table 4.2 (lines 308-315)

**Proposition 4.1 (1) and (2): HOLD; not new.** p_t(x, .) is a probability
density for pi, and R preserves pi, so f = p_t(x, y) and g = p_t(x, Ry) are
probability densities on (X x X, pi x pi). P has a bounded positive density:
C_E P is the gauge average of C_E, whose kernel is continuous and positive.
min(f, g) <= sqrt(fg) gives tau <= B. 1 - tau = (1/2) int |f - g|, and
Cauchy-Schwarz on |sqrt f - sqrt g| (sqrt f + sqrt g) gives
(1 - tau)^2 <= (1 - B)(1 + B). sqrt(1 - x) <= 1 - x/2 gives tau >= B^2/2. Row
1161 (2) (`gap-solve9-astra62.md` L35-37) reads
1 - b^(2t) >= (1 - rho^(2t)) tau_R(t)/(2 - rho^(2t)), with b = e^(-E_q),
rho = e^(-m_+); with -log(1 - y) >= y this gives (4.2). (4.3) is row 1161 (1)
(L25-27) with tau <= B. The identity int (q_t - 1)^2 = s_+(2t) holds (P kills
the non-invariant part, so Tr(P_+ P^(2t)) = 1 + s_+(2t)). The inequalities in
(4.1) are the standard comparison of total variation and Hellinger affinity
(Le Cam); Hellinger contraction and d^2 <= 2 TV are already used in the lane
(rows 1163-1171, for instance `gap-solve12-check-opus.md` L261).

**Proposition 4.1 (3): the threshold (4.4) FAILS as printed (line 301);
HOLDS AFTER CORRECTION with 28 in place of 14.** Under (N-phys),
e^(-2 u m_+) <= s_+(2u) <= s_+(u)^2 <= 1/4, and (1 - x)/(2 - x) decreases in
x, so the factor is at least 3/7. Then (4.2) at t = u_j gives
E_q >= (3/7) B^2/(4 u_j) = 3 B^2/(28 u_j), so
n_j E_q >= K u_j E_q >= (3K/28) B^2, not (3K/14) B^2 as line 301 says. The
constant 3K/14 belongs to the overlap itself: from row 1161 (2) directly,
E_q >= (1/(2u)) (3/7) tau, so n_j E_q >= (3K/14) tau. Corrected statement:
Alternative I is selected at cutoff j if
B_R(u_j) > sqrt(28 b_-/(3K)), or, stronger and simpler, if
tau_R(u_j) > 14 b_-/(3K). By hand, at eps = 1/40329:
b_- = -log(1 - 2/40329) = 4.95933 x 10^(-5); with K = 512,
14 b_-/(3K) = 4.520 x 10^(-7), sqrt(28 b_-/(3K)) = 9.508 x 10^(-4). The
printed value 1.80 x 10^(-4) is sqrt(b_-/(3K)) = sqrt(3.2287 x 10^(-8)),
which matches neither the printed formula (6.723 x 10^(-4)) nor the corrected
one. For B between 6.723 x 10^(-4) and 9.508 x 10^(-4) the printed implication
is not proved. No counterexample is claimed; the failing step is the
arithmetic.

Two further remarks. (a) K = 512 belongs to row 1161's explicit-aspect
section (L213-216), which proves S_kappa < 2^(-18) under the transverse
frequency floor 1/10. Corollary FB (row 1179 L456-474) uses the existence
aspect K(eps) of row 1161 L146-148, which approximates all 64 sector weights
within eps. Pairing FB with K = 512 is not justified by either source, so
the numeric instance should be stated for the existence K. (b) The B-form adds
nothing. tau >= B^2/2 turns the corrected B-threshold into the tau-threshold,
and the tau-threshold follows from row 1161 (2) and Corollary FB in one line.
Neither threshold is proved for Wilson SU(2); (BS) stays OPEN. Verdict:
(1)-(2) HOLD, not new; (3) HOLDS AFTER CORRECTION (constant 28, value
9.51 x 10^(-4), existence K), a one-line corollary of rows 1161 and 1179.

**Section 1.1 (PROVED GIVEN): HOLDS as a summary; not new.** It restates row
1179 Theorem BP and Corollary FB (RESULT, row 1179) as checked in row 1183
(BP(i-iii) HOLDS; `gap-neutral-chain-check-astra.md` L40): (N-phys) and the
continuum datum give the gap clause in both flux alternatives, with
M_* = (2/L) log(1/(40328 eps)), and (BS) enters only (W). One looseness: item
2 quotes K = 512 for n_j >= 2^70 (row 1161 L213-216, conclusion
S_kappa < 2^(-18)), while item 3 quotes S_kappa <= 8 eps < 1/5041, which is
the existence-K version (L146-148). Both give S_kappa < 1/5041, so the
summary stands.

**Table 4.2 (labelled PROVED): HOLDS AFTER CORRECTION in one cell; the other
cells are citations.** U(1) cell: on L^2_0(H) the electric step has norm
I_1(beta)/I_0(beta), from a single link of charge 1; the fourth power holds
on the gauge-invariant mean-zero space (a nonzero divergence-free flow has a
cycle of at least four edges). The Q_8 and 2T commutator claim is right:
characters of the abelianizations Q_8/{+1, -1} and 2T/Q_8 are trivial on
commutators. The product cell, (1 + s^SU2)(1 + s^spec) - 1 >= s^spec, is
right. The photon and frozen-count cells cite rows 988, 1186, 884 and 1130
and were not re-derived here. Comparison lines of this kind are on file in
row 1141 (Phase 2 table) and row 1132.

### Step 7. Novelty, against `library/open-core.md` and the FINISH rows

Greps run on `library/open-core.md` (564 lines) and FINISH.md for: Jacobian,
chord, PRIV / private link, transverse link, McDiarmid, R4, Hellinger /
Bhattacharyya, overlap, electric sandwich, Casimir, 1/256, Lemma O1, tree
transport. open-core.md has no match on any of these topics; its two hits, R4
and overlap, are in unrelated formulas (L135, L130). FINISH and library
matches:

| Statement | On file | Match |
|---|---|---|
| T2.1 (1) sandwich swap | yes | rows 875, 914, 934, 1155 (lines in Step 2) |
| T2.1 (2) identity (2.3) | yes, as the ground-state transform | row 1161 L22-23 |
| T2.2 selection rules, four-edge support, a^4 bound | yes | row 1132 L98 |
| T2.2 commutator multiplier, 4^(-4) on plaquette traces | yes | row 1132 L37, L64 |
| T2.2 exact norms, Casimir 12, cut parity | no; one-line consequences | none |
| T2.3 min-max against the electric operator | yes, in kind | row 1180 R4 (L167-169) |
| P2.4 | yes, same statement | row 1180 Lemma R4 (L208-227); new: McDiarmid-free proof, exponent linear in 1 - r^4 |
| T3.1 | yes | row 1034 STAR (L70-75) |
| T3.2 (2) private link P | yes, stronger hypothesis there | row 1034 PRIV (L214-229) |
| T3.2 (2) transverse private link Q | no match for this use | FINISH "transverse link" hits are rows 936, 1081, 1177, other contexts |
| T3.2 (3) 9 links | 6 links on file | row 1034 L252-255; the general 9 is not proved (Step 5b) |
| T3.3 (10) | yes | row 1141 (10), L152-157 |
| T3.3 Jacobian split | yes, abstractly | row 1141 L208-209 |
| T3.3 explicit Jacobian divergence for a field-chosen axis, bound (3.12) | no match | rows 1051, 1141 treat fixed axes (zero Jacobian, Corollary RM-TREE of row 1051) |
| P4.1 (1) | standard; tools used in the lane | rows 1163-1171 (e.g. `gap-solve12-check-opus.md` L261) |
| P4.1 (2)-(3) | corollaries | row 1161 (1)-(2), row 1179 Corollary FB |

So the only items not on file are small: the transverse private link Q, the
explicit Jacobian divergence of a tree transport with a field-chosen axis
(corrected sign) with its chord bound, the McDiarmid-free proof of row 1180
Lemma R4, and the exact norm values of Theorem 2.2. None of them closes or
kills an item on the critical path: (N-phys), the continuum datum, (BS), (W)
and Lemma O1 are unchanged.

### Step 8. Verdicts, rating, RESULT

Provenance: Claude Opus 5.5, max effort, Mac mini Claude worker 2, commit
beea72f25. One cross-provider reading by hand, not an audit. No numeric run:
memory was below the 50 percent floor. Grants no status.

| Id | Verdict | New? | Defect (line) |
|---|---|---|---|
| T2.1 | HOLDS | no: rows 875, 914, 934, 1155; trivial | wording at 54: psi_0 is moved into the vector, not removed |
| T2.2 | HOLDS AFTER CORRECTION | no in substance: row 1132 L37, L64, L98 | 90: "iff plaquette" fails at n = 4 (adjoint winding line); bounds unaffected |
| T2.3 | HOLDS, vacuous | no in kind: row 1180 R4 | (2.8) right side equals a_2^4 ||M||^2/lambda_0 >= a_2^4 e^(c_0 n^3) |
| P2.4 | HOLDS | same statement as row 1180 Lemma R4; better proof and constant | says nothing beyond normalization (free energy below 3 beta per site); holds for gapless U(1) |
| T3.1 | HOLDS given (REG) | no: row 1034 STAR | none |
| T3.2 (1) | HOLDS as an implication | variant of row 1034 | "decouples" (168, 200, 331) is wrong as an equivalence; (3.7) is necessary only |
| T3.2 (2) | HOLDS | P: variant of PRIV (stronger hypothesis, weaker conclusion); Q: small new remark | needs conservation on whole in-link fibres |
| T3.2 (3) | implication HOLDS; claim "Lemma O1 threshold 6 -> 9" FAILS | no | 219: W^0 = 0 does not give D n = 0 for frames that read other in-links; 9 holds only for a subclass; 6 (row 1034) stands |
| T3.3 | HOLDS AFTER CORRECTION | (3.10) = row 1141 (10); (3.11)-(3.12) small new | 246: sign of (3.11) wrong; (3.13)-(3.14) true, not sharp (48, c/192) |
| T3.3 vs row 1141 | does NOT answer it | - | covers only tree transports of a field-chosen axis (already row 1141 (9), (13)); (3.14) is a satisfiable necessary condition with no cost attached |
| P4.1 (1)-(2) | HOLDS | no: Le Cam; rows 1161, 1163-1171 | none |
| P4.1 (3) | FAILS as printed; HOLDS AFTER CORRECTION | no: rows 1161 (2) + 1179 FB | 301: 3K/14 should be 3K/28; threshold sqrt(28 b_-/(3K)) = 9.51e-4, not 1.80e-4; K = 512 not justified for FB |
| S1.1 | HOLDS as a summary | no: rows 1179, 1183 | K = 512 and 8 eps come from two different versions of row 1161 |
| S4.2 | HOLDS AFTER CORRECTION in one cell | no: rows 1132, 1141 tables | U(1) electric norm on L^2_0(H) is I_1/I_0; the fourth power is on the gauge-invariant space |

**Answers to the questions of the queue row.**
- The norm 1/256 and the Casimir gap 12 are correct and sharp, attained by
  one plaquette trace. They add nothing a consumer reads: row 1132 already
  has the four-edge support and the multipliers, and statement (A) is what
  reads W_E, and it fails at one step (row 1132 L61-64).
- Proposition 2.4's volume bound on the Perron eigenvalue is correct. It says
  nothing beyond normalization: it is a free-energy bound, true for gapless
  U(1) as well. It shows only that every one-step bound normalized by
  ||M||_inf^2, including Theorem 2.3's, loses exp(c_0 n^3).
- Theorem 3.3 does not answer row 1141. Row 1141's open question is about
  general field-dependent frames, and it stays OPEN, also for tree transports
  with a field-chosen axis.

**Rating against the plain-brief rows 1188-1190 (Claude Fable 5.2 max),
as checked in row 1196 (gpt-6.2-astra max).** This is one reader's
judgement.
- Correctness is comparable. Here: 7 statements hold as stated (T2.1, T2.3,
  P2.4, T3.1, T3.2 (2), P4.1 (1)-(2), S1.1), 4 need a correction, and 3
  claims fail (6 -> 9, "decouples", "answers row 1141"). In row 1196: 7 hold,
  3 hold after correction, 3 fail.
- Novelty and record search are weaker. The file calls T2.1, T2.2, T2.3,
  P2.4 and T3.1 new (lines 326-330), and all five are on file (rows 875,
  914, 934, 1155, 1132, 1180, 1034). Rows 1188-1190 named their own on-file
  matches: row 1188 named rows 712-1179; row 1189 found all twelve route
  families on file; row 1190 found 12 of 17 attacks on file.
- Value is smaller. None of the four rows moves (N-phys), the continuum
  datum, (BS), (W) or Lemma O1. The new pieces here (transverse private
  link, an explicit Jacobian divergence, a McDiarmid-free R4) are smaller
  than row 1189's A8 (a power-law bound on mixed rectangles, held in 1196)
  and similar in size to row 1188's Lemma PC.
- Labels of open items are honest: no mass gap is claimed, and (N-phys),
  (BS), (W) and the continuum datum are stated OPEN, as in rows 1188-1190.
- Speed: 16 minutes and 116k output tokens, against 51-59 minutes for rows
  1188-1190. The summary lines (168-169, 326-333, 342) overstate the
  results; rows 1188-1190 did not overstate them in that way.
- On Astra (reading only): the Astra crux rows this file builds on held
  under their checks (row 1141: all 34 statements HOLD in row 1142; row 1161
  HOLDS AFTER CORRECTION in row 1162), and they carry the quantitative
  inputs (row 1141 (9), (13); row 1161 (1), (2)) that Sections 3.4 and 4 reuse.

Overall: below rows 1188-1190. Correctness is similar; there is less new
content and more overclaiming.

RESULT: Row 1206 (Claude Opus 5.5 max, Mac mini worker 2, cross-provider check by hand of row 1205, gemini-4-argon-high; no numeric run, memory below floor; grants no status): HOLD: Theorem 2.1, Theorem 2.3 (but (2.8)-(2.9) are vacuous: the right side of (2.8) equals a_2^4 ||M||^2/lambda_0 >= a_2^4 e^(c_0 n^3)), Proposition 2.4 (correct; only a free-energy normalization bound, true for gapless U(1); same statement as row 1180 Lemma R4 with a McDiarmid-free proof and a better constant), Theorem 3.1 (= row 1034 STAR in weak form), Theorem 3.2 (2), Proposition 4.1 (1)-(2), Section 1.1; HOLD AFTER CORRECTION: Theorem 2.2 (norm 1/256 and Casimir gap 12 correct and sharp; the "iff plaquette" fails at n = 4, adjoint winding line), Theorem 3.3 ((3.11) has the wrong sign; (3.12)-(3.14) true), Proposition 4.1 (3) (3K/14 should be 3K/28, threshold 9.51e-4 not 1.80e-4, K = 512 not justified for Corollary FB), table 4.2 (U(1) cell); FAIL: "Lemma O1 threshold raised from 6 to 9" (line 219: W^0 = 0 does not give D n = 0 for frames that read other in-links; row 1034's 6 stands), "decouples" as an equivalence (line 168), and Theorem 3.3 does NOT answer row 1141 (tree transports only; (3.14) is a satisfiable necessary condition). New but small: the transverse private link Q, an explicit Jacobian divergence for field-chosen tree axes, a McDiarmid-free R4; everything else is on file (rows 875, 914, 934, 1034, 1132, 1141, 1155, 1161, 1179, 1180). Rating against plain-brief rows 1188-1190 (checked in 1196): similar correctness (here 7 hold, 4 corrected, 3 fail; there 7, 3, 3), weaker record search and more overclaiming, smaller value; none of the four moves the crux. OPEN: (N-phys), the continuum datum, (BS), (W), Lemma O1, row 1141's general-frame question, the mass gap. Output library/gap-agy-argon-check-opus.md.
