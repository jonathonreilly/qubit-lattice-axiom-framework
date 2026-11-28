# Check of library/gap-mech-attack-astra62.md (FINISH row 1535)

Checker: Claude (Opus 5.5). Status: done.

## Plan
1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read library/gap-mech-attack-astra62.md in full.
3. Read the cited inputs: library/gap-crux2-astra62.md (2)-(7), row 1373, check 1527 parts (i),(vi), row 1386 Prop NEG.
4. Decisive outcome: (6) with probability -> 1 under 16 twisted laws; the two selectivity claims.
5. Parts in the order of the brief.
6. Equivalent-is-not-progress test; grep library/ and FINISH.md.
7. RESULT line.

## Step 1 (done). Sources read
GOAL.md; FINISH.md 'Working efficiently' and 'Rules'; library/gap-mech-attack-astra62.md in full (201 lines);
library/gap-crux2-astra62.md in full (row 1141); library/gap-agy-seed-approaches-neon-check-astra62.md in full
(check 1527); row 1526 Theorem 1 (library/gap-agy-seed-approaches-neon.md lines 190-218); row 1386 Proposition
NEG and Remark STAB (library/gap-mech-direction2-fable.md lines 190-240).

## Step 2 (in progress). Line-by-line notes
Working notes written as each part is checked; verdicts collected at the end.

Provenance: Claude (Opus 5.5), laptop subagent, check by reading at the lane checkout as found on 2026-11-25;
not an audit. Hand check only; no numerical run, no Lean. Verdicts per part: HOLDS, HOLDS AFTER CORRECTION, FAILS.

## Decisive outcome

**(6) HOLDS** under each of the sixteen twisted Wilson laws (v in {u, 2u}, z in Z_2^3), with probability
tending to one, for the bounded transported root curvatures and simultaneously for every choice of unit root
axes on the same trees. The law enters only through (7) and the one-link tilt bound |a| <= 6 beta; both hold
for every seam sign (checked below). The upper bound X_R <= C is deterministic (every connection). The lower
bound holds on one event for all dyadic R in [R_0, q/8] at once.

Two remarks on its scope (not defects of the statement):
- The lower-bound proof does not use (3) or the lower growth of beta_K. It needs only beta_K -> infinity,
  log(beta)/v and beta/n^2 bounded (for (7)), and q/v -> 0. The rate is slow: P(bad-cube fraction > 1/8) <=
  128 C_0 q^10/beta ~ beta^(-3/8) ~ (log n)^(-3/8).
- The range R_0 <= R <= q/8 is empty until floor(beta^(1/16)) >= 8 R_0, i.e. beta >= (8R_0)^16 >= 8^16 ~ 2.8e14
  even at R_0 = 1. With beta ~ log n that means n >= exp(10^14). The limit statement holds; at any reachable
  cutoff it has no instance.

**Selectivity claim 1 (compact U(1)) HOLDS, trivially.** For U(1) the adjoint action is trivial, ad h = 0,
so M_h = 0 and X = X_R = 0 for every connection. The vanishing is built into the observable (a commutator);
it is not a property of any Wilson estimate.

**Selectivity claim 2 (five dimensions) HOLDS.** D_R <= 3R^-2 (H+R^-2)^-2, so D_R^2 <= 9R^-4 (H+R^-2)^-4.
Heat-walk domination (checked below) gives Tr D_R^2 <= 27 R^-4 V F_{5,4}(R^-2), and F_{5,4}(s) <= C s^(-3/2)
(ball C s^(5/2-4); annuli C r^(5-8) summed from sqrt s; zero mode R^8/V <= R^3 since V >= c n^5 and R <= n).
So X_R <= (4/V) Tr D_R^2 <= C/R for every connection and every |h| <= 1. The same proof as (6) gives the
matching 5D lower bound c R^(4-d) = c/R on good cubes (count: X_R >= c R^4 V^-1 #bumps, #bumps >= cV/R^d).
So the 4D/5D difference is exactly the free mode count R^(4-d): the textbook marginality of the two-propagator
spin bubble in four dimensions. The Wilson law contributes only "the background is near pure gauge on most
q-cubes".

## Upper bounds (2)-(5)

**(1) and the set-up — HOLDS.** J and ad h are skew, so M_h = -2J (x) ad h is symmetric; ||M_h|| = 2 max|h_x|
<= 2. For a ~ N(0,Gamma), Var(a^t M a/2) = Tr(Gamma M Gamma M)/2, so V X is that variance. Gauge
transformations conjugate D_U, H and M_h; a seam move U_e -> -U_e keeps sigma_p U_p and Ad U_e. So X(U) is a
function of the twisted sample. HOLDS.

**Use of row 1141 (2)-(7) under seam signs — HOLDS.** Row 1141's proof of (2) uses (i) the one-link
conditional law e^{a.q}dq with |a| <= 6b, (ii) for (4), the conditional law of a plaquette holonomy given its
other three links (orthogonal image of (i)), (iii) the cross product |u x n|, (iv) conditional iteration (7),
and (v) deterministic steps (5), (6), the amplitude bound. With seam signs each of the six normalized terms
sigma_p tr(U_p)/2 is still linear in q with coefficient vector of norm one, so (i) holds with |a| <= 6 beta.
Multiplication by -1 is orthogonal on S^3 and maps u -> -u, so |u x n| and Ad h_i are unchanged; (ii)-(iv) hold.
(v) does not see the law. The Neumann v-cubes: v divides n (512 | n, u = n/512), (n/v)^3 in {512^3, 256^3}
cubes, all periods >= 3; dropping the temporal wrap when the cube fills the period leaves an open coordinate
cube with distinct sites, and dropped bonds only lower the energy. Union bound: fixed factor times
(2+v)^-k <= C_k n^-k. First inequality of (3) HOLDS. The second (gamma = c'/(1+beta)) uses
sqrt(log n) <= C beta, i.e. the lower growth beta_K >= c log n; as a premise from the trajectory. Without it the
bound reads c/(1+beta+sqrt(log n)) and (2) becomes C(1+log(1+beta+log n)); nothing downstream in (6) changes.

**Heat-walk domination by three times the scalar trace — HOLDS.** ||D_U f||^2 = sum_{x,i}(|f_x|^2 +
|f_{x+i}|^2 - 2 f_x . Ad U_{x,i} f_{x+i}), so H = 2d I - A_U with A_U the adjoint-transport adjacency.
e^{-tH} = e^{-2dt} sum_k t^k A_U^k/k!; Tr A_U^k = sum over closed walks of tr(Ad hol) <= 3 per walk; all
weights nonnegative, so Tr e^{-tH} <= 3 Tr e^{-tH_0}. (H+s)^-j = int t^{j-1}e^{-st}e^{-tH}dt/(j-1)! transfers it.
The gap step: H >= gamma implies H + m^2 >= (H + m^2 + gamma)/2, so (H+m^2)^-j <= 2^j (H+m^2+gamma)^-j as
functions of one operator. HOLDS. (Adjoint transports are periodic for every twist, so H_0 is the periodic
Laplacian of the same rectangle.)

**(4) — HOLDS.** Count: per coordinate (n_i r/pi + 1)/n_i <= r/pi + 512/n, so count/V <= C(r + 1/n)^d.
4 sin^2(p/2) >= 4p^2/pi^2 on [-pi,pi]. Ball: C(sqrt s + 1/n)^d s^-j <= C s^{d/2-j} for s >= n^-2. Annuli:
C r^{d-2j}. Hence F_{4,2} <= C(1+log 1/s), F_{4,4} <= C s^-2, F_{5,2} <= C, and F_{5,4} <= C s^{-3/2}.

**(2) — HOLDS.** Tr(Gamma M Gamma M) <= ||Gamma M||_HS ||M Gamma||_HS = Tr(Gamma M^2 Gamma) <= ||M||^2 Tr Gamma^2,
Tr Gamma^2 = 2 Tr G^2. So X <= (4/V) Tr G^2 <= 48 F_{4,2}(m^2+gamma) <= C_k(1+log(1+beta)) on (3).
Off (3), 12 F_{4,2}(n^-2) <= C(1+log n), times C_k n^-k. Field-dependent h: the bound is uniform in |h_x| <= 1.

**(5) — HOLDS.** D_R = 3a(H+a)^-1(H+4a)^-1 <= 3a(H+a)^-2, a = R^-2. X_R <= (4/V) Tr D_R^2 <= 36 R^-4 V^-1
Tr(H+a)^-4 <= 36.16.3 R^-4 F_{4,4}(a+gamma) <= C(1+beta)^2 R^-4. Off (3): D_R <= (H+n^-2)^-1 for R <= n gives
C(1+log n) (the deterministic 4D bound C, from F_{4,4}(R^-2) <= CR^4, is even better). The mixed trace:
|Tr(Gamma M D M)| <= ||Gamma M||_HS ||D M||_HS <= 4 ||Gamma||_HS ||D||_HS, nonnegative as
||D^{1/2} M Gamma^{1/2}||_HS^2; the stated bound follows. Bessel remark HOLDS.

**5D bound X <= C for every connection — HOLDS** (F_{5,2}(m^2) <= C, no gap used).

## (7) and its two free-energy bounds — HOLDS

Upper bound on f(beta): a tree leaves dV - (V-1) = (d-1)V+1 links; Haar cap of chord radius beta^-1/2 has
mass >= c beta^-3/2 (density (2/pi) sin^2 theta). 1 - tr U/2 = |U-1|^2/2, four links within beta^-1/2 give
|U_p - 1| <= 4 beta^-1/2, deficit <= 8/beta, so beta x (positive part) <= 48V. Negative plaquettes: a 0i twist is
one stack of n^2 = n^{d-2} faces at fixed time and fixed x_i, at most 3 stacks, each face costs <= 2 beta. HOLDS.
Lower bound on f(beta/2): all terms are >= 0, so dropping all but the non-wrapping temporal plaquettes raises
the integrand. Spatial links at time v-1 lie in exactly one kept plaquette each; integrating them gives I(t)
each, independent of the rest by Haar invariance (also for sigma = -1, g -> -g); proceed down to layer 1.
Count (d-1) n^{d-1}(v-1) = (d-1)(V - n^{d-1}). I(t) <= C t^{-3/2} from 1-cos theta >= 2theta^2/pi^2 on [0,pi].
HOLDS. Difference: (3/2)[(d-1)n^{d-1}+1] log beta + CV + C beta n^{d-2}, and n^{d-1}/V = 1/v, n^{d-2}/V =
1/(nv); bounded per site given log(beta)/v and beta/n^2 bounded. log E e^{beta A/2} = f(beta) - f(beta/2) is
the right identity for the normalized law e^{-beta A}/Z. Jensen and exponential Markov give (7). HOLDS.

## Good-cube fraction — HOLDS

||I - Ad U||^2 = 4 sin^2 theta = 4(1-w^2) <= 8(1 - sigma w) (both factors 1 +- w <= 2, and
(1-w)(1+w) <= 2 min(1-w,1+w)). A bad cube has a face with 1 - sigma w > q^-6/8; internal faces of distinct
cubes are disjoint; so #bad <= 8 q^6 A and the bad-site fraction <= 8 q^{d+6} A/V. Expectation <= 16 C_0 q^10/beta
-> 0 since q^10 <= beta^{10/16}. Strips: gaps fraction <= d/(q+1), remainders <= d(q+1)/v; both -> 0. Markov
gives >= 3/4 of sites in good cubes w.p. -> 1. HOLDS.

## Root-vector estimate and its conditioning — HOLDS

Given all links but a private link of p_r, sigma_{p_r} U_{p_r} is an orthogonal image of that link, so its law
is a tilt with |a| <= 6 beta; row 1141 (3) gives P(|w_r x n| <= t) <= 4(1+6beta)t^2, and |w_r| >= |w_r x n|.
At t = tau/sqrt(1+beta), tau = 1/16: <= 24/256 < 1/8. Root plaquettes of distinct cubes are disjoint, so the
earlier indicators are measurable without the private link of p_r; the tower property gives
E[2^{J_r} | F_{r-1}] <= 9/8 and E 2^J <= (9/8)^N, P(J > N/2) <= (9/(8 sqrt 2))^N, 9/(8 sqrt 2) ~ 0.795.
N >= c V/q^4 -> infinity. Counting: #good cubes >= (3/4)V/q^d and N <= V/q^d, so good cubes with good roots
>= V/(4q^d). The two events are intersected, not conditioned. |h_r| = min(sqrt(1+beta)|w_r|, 1) >= tau exactly
on the complement of the failure event. Compatibility with goodness: good gives |w_r| <= q^-3/2 ~ beta^(-3/16)/2,
which is much larger than tau beta^(-1/2). HOLDS.

## Root-tree gauge error — HOLDS

In the tree gauge the transport on bond (x, x+e_i) is Ad of the holonomy of root -> x -> x+e_i -> root. The
coordinate-ordered paths differ by one e_i step moved past the segments j > i: sum_{j>i} x_j <= (d-1)(q-1)
elementary moves, each across one internal ij face (all four corners in the cube since x + e_i is). Lasso
decomposition gives a product of conjugated face rotations; ||prod R_k - I|| <= sum ||R_k - I|| for orthogonal
R_k; total <= (d-1) q^-2. h_x = T(x) h_r is constant in this gauge. HOLDS. (The citation to PX42-PX43 is not
load-bearing; the proof given is complete.)

## Bump test spaces and (8) — HOLDS

Subcubes: floor(q/R)^d >= (q/2R)^d for R <= q/8; #bumps >= (V/(4q^d))(q/2R)^d = V/(2^{d+2} R^d). Sampled bump:
norm^2 ~ R^d (Riemann sum, R >= R_0), ||H_0 phi|| <= C R^-2 (second differences, Taylor remainder, zero
extension). On phi (x) T(.)c the operator H - H_0 (x) I is a sum of 2d shifted link errors (A~ - I), each of
norm <= C q^-2 <= C R^-2, all bonds internal since the one-bond enlargement is in the subcube. Disjoint
enlarged supports give ||H psi|| <= C R^-2 ||psi|| on all of S_R. Then <psi, D_R^{-1} psi> =
(3a)^{-1}(||H psi||^2 + 5a<psi,H psi> + 4a^2||psi||^2) <= C R^-2 ||psi||^2. Variational formula for D > 0,
restricted to S_R: <f,D f> >= sup_{psi in S_R}(2<P f,psi> - C R^-2 ||psi||^2) = c R^2 ||P f||^2. (8) HOLDS.

## Monotonicity of the quadratic trace and the finish of (6) — HOLDS

Tr(B M C M) = ||C^{1/2} M B^{1/2}||_HS^2 >= 0 for B, C >= 0, M symmetric. So
Tr((G+Delta)M(G+Delta)M) - Tr(GMGM) = 2Tr(G M Delta M) + Tr(Delta M Delta M) >= 0: increasing in the form
order on psd operators. Insert I_2 (x) D_R >= cR^2 I_2 (x) P_R. Tr(PMPM) = Tr((PMP)^2); M is sitewise and the
bump supports are disjoint, so PMP is block diagonal with blocks <phi_b T c, M phi_b T c'> =
-2J (x) <c, ad h_r c'> (Ad is a Lie automorphism, sum phi^2 = 1). Block trace of the square:
4 Tr(J^2) Tr((ad h_r)^2) = 4(-2)(-2|h_r|^2) = 16|h_r|^2 >= 16 tau^2. X_R >= (c^2 R^4/2V) 16 tau^2 #bumps >= c'.
Telescoping: sum of D_R over R_1..R_2 = (H+R_2^-2)^-1 - (H+4R_1^-2)^-1 <= G for R_2 <= n; monotonicity and
nonnegative cross terms give X >= sum_R X_R >= c (1/16) log_2 beta - C. With (2): X ~ log(1+beta) ~ log log n;
expectation: X >= 0 and the event has probability -> 1. HOLDS.

## Sitewise-insertion paragraph — HOLDS

|h_x|^2 = (1+beta)(1-w^2) <= 2(1+beta)(1-sigma w), summed over the 12 plaquettes <= 2(1+beta)A.
Tr(Gamma M Gamma M) <= Tr(Gamma^2 M^2), M^2 = 4 I_2 (x) (-(ad h)^2) sitewise, tr of the 6x6 block 16|h_x|^2.
Diagonal blocks: psd order passes to diagonal blocks, so (H+m^2)^-2(x,x) <= 4 (H+m^2+gamma)^-2(x,x); the
heat walk with ||walk transport|| = 1 bounds the block norm by the scalar diagonal (H_0+s)^-2(x,x) = F_{4,2}(s)
(translation invariance). Same for D_R^2 with F_{4,4}. On (3) and (7)'s event A/V <= 2(C_0+1)/beta, so (2) and
(5) hold. Off-event: ||M|| <= C sqrt(1+beta) gives the stated expectation cost. HOLDS.

## (9)-(10) — HOLDS

P = S_1 S_2 S_1^* S_2^* acts at x by Ad(U_{x,1}U_{x+1,2}U_{x+2,1}^-1 U_{x,2}^-1) (computed). For U = w + u,
Ad U - Ad U^t = 4w ad u, so (P - P^*)/4 = w ad u; invariant under U -> -U. [S_1 - I, S_2 - I] = [S_1, S_2]
and [S_1,S_2] S_1^* S_2^* = P - I (S_i unitary). ||(S_i - I)s|| = ||(D_U s)_{.,i}|| <= ||D_U s||, the same for
S_i^* - I. ||(W - I)t|| <= 2||D_U t||; ||(S_i - I)W t|| <= ||D_U t|| + 2.2||D_U t|| = 5||D_U t||. Two terms give
10. (9) HOLDS. The form of ad h with h = sqrt(1+beta) w u is bounded by 5 sqrt(1+beta)||D s|| ||D t||, so
M_h = H^{1/2} L H^{1/2} with ||L|| <= 10 sqrt(1+beta), zero on ker H. Cyclicity: Tr(D M D M) = Tr(B L B L),
B = H^{1/2} D_R H^{1/2} = H D_R >= 0, <= ||L||^2 Tr B^2. H D_R <= 3a (H+a)^-1, so Tr (H D_R)^2 <=
27 a^2 V F_{4,2}(a) <= C V R^-4 (1 + log R). (10) HOLDS, for every connection, R <= n. The closing caveat
(the Wilson Hessian has other coefficients; (9) does not estimate it) is correct.

## Exact second-derivative identity and the two-level example — HOLDS

det(I + theta K)^{-1/2}, K = Gamma^{1/2} M Gamma^{1/2}, ||K|| <= 2/m^2, so |theta| < m^2/2 keeps I + theta K > 0
and the Gaussian formula holds. (log L)'(0) = -Tr(Gamma M)/2 = 0 since Tr J = 0; (log L)''(0) = Tr K^2/2 = V X.
Pointwise L(0) = 1, L'(0) = 0, L''(0) = V X; so d^2 log Zhat^z = V E^{z,v} X and, with positive twist weights
Z^z(v)/sum Z^{z'}(v) (all Z^z > 0) and zero first derivatives, d^2 log(Zhat_+(2u)/Zhat_+(u)^2) =
2n^3u(E^{+,2u}X - E^{+,u}X). HOLDS. Two-level: with eigenvalues 1, r and diagonal insertion (B, B+1) the mean
is B + r^v/(1+r^v), decreasing in v; with (B+1, B) it is B + 1/(1+r^v), increasing. Sign reverses. HOLDS (an
illustration that positivity fixes no sign; it is not a statement about Wilson theory).

## Implication (11) -> seed — HOLDS; (11) is on file in equivalent form

u = n/512 is even since 1024 | l. Row 1526 (2.1), (2.2), (2.3) HOLD by check 1527 (i), with the neutral
projection on both half periods as here (check 1527 (i) correction satisfied). b_A = int w_A dW with the centre
sum and endpoint gauge averages in dW (all weights > 0) gives d_s log b_A = E_Q S, so J = Var_p(E_Q S).
Total variance: Var_{pQ} S = Var_p(E_Q S) + E_p Var_Q S, and Var_Q S >= (E_Q[SY])^2/E_Q[Y^2] when E_Q Y = 0.
So the integrand of (11) is >= J; then E d_Hel^2 <= threshold and (2.2) gives P_K >= (sqrt 457/25)^2 = 457/625.
HOLDS (with measurable paths ending at a gauge-and-centre representative, as stated).

Not equivalent to the seed: check 1527 (vi)'s kernels 1 + cos(Na)cos(Nc)/2 have purity 257/289 > 457/625 and
mean minimum path energy >= cN^2, and (11)'s left side is >= E int J; so (11) fails there while the seed's
inequality holds. HOLDS. But (11) is not new: Y = S - E_Q S is admissible and gives equality (fraction =
Var_Q S), so inf over Y of the integrand is exactly J. Hence "(11) for some measurable paths and tests" is
equivalent to "E int J ds <= 2(1 - sqrt 457/25) for some measurable paths", which is the direct test of check
1527 (vi) (STIFF-TO-HELL at the original aspect, line 114 there). The note does not claim (11) is new; it should
say it is that test.

## Zero-overlap claim for the auxiliary Gaussian test — HOLDS (tautologically)

S is a function of the first half; the Gaussian is drawn independently given both bridges, with
E[a^t M a/2 | bridges] = Tr(Gamma M)/2 = 0. So E[S Y | bridges] = S . 0 = 0, for any bridge-measurable
multiplier. An auxiliary noise independent of the Wilson field given the field has zero covariance with every
Wilson score. The integration-by-parts remark E_Q[S div_Q V] = -E_Q<grad S, V> (sign convention aside) is
standard. Polarization example: covariance (1-eta^2)G + eta^2 G = G, cross covariance E[eps] = 0, each marginal
N(0,G), density positive for eta > 0; a^t (ad h) a = 0 sitewise, so the spin term is eta a^t(ad h)c and its
variance is eta^2 V X. HOLDS.

## Stopping statement — HOLDS

R_K = 2^{floor(log2(u/8))} >= u/16 ~ n/8192, so (5) gives sup_h X_{R_K} <= C(1+beta)^2 R_K^-4 -> 0 on (3), and
the deterministic bound C times C_k n^-k off it: the physical-radius statement fails on all sixteen tori.
HOLDS. beta = 0: Haar transfer, rank one, purity one; (3) with b = 0 gives gamma = c_k/(1+sqrt(log(2+n))), and
(5) gives C log n R^-4 -> 0: the response is not necessary for the seed. HOLDS. Spectator: eigenvalues
1 +- n^-2, (1 +- n^-2)^u -> 1, purity factor -> 1/2; normalized Wilson measurements unchanged. HOLDS (as in
check 1527 (vi)). "(6) is genuinely selective": HOLDS in the two stated tests, with the scope below.

## Equivalent is not progress; is (6) beyond one site; is it on file

- (6) is not a sufficient condition for anything on file: the note proves no consumer, and its own zero-overlap
  section shows its Gaussian test supplies no subtraction in (11). The rule therefore applies only to (11),
  which is equivalent to check 1527 (vi)'s direct test (above): no progress on that side.
- Content beyond one site: in lattice units yes (R up to q/8 -> infinity, about (1/16) log_2 beta dyadic
  shells). In physical units no: R a_K <= beta_K^{1/16} a_K -> 0. Proposition NEG (a) asks for content at
  physical side L > L_gamma at all late cutoffs. (6) has none, so it does not escape NEG. It is a new
  ultraviolet, small-field member of the selective class, not a member with content in the band.
- Remark STAB of row 1386: (6) comes from plaquette concentration (7) on q-cubes and its range grows with beta.
  That is the kind of hypothesis STAB says cannot alone imply the seed test.
- On file: the flat-background form with the same two selectivity tests is on file: row 1244, Lemma 2.2 and
  Proposition 2.3 (library/gap-mini-solve-aa-opus.md lines 144-196, the spin bubble ~ (1/(8 pi^2)) log L on the
  flat torus) and row 1526 Theorem 5(a) as checked in check 1527 (iv) ("the Abelian spin is zero and in five
  dimensions the shell integral is infrared finite"). Grep of library/ and FINISH.md for heat-walk/Kato
  domination of an adjoint resolvent trace, good cubes at scale beta^(1/16), transported root curvatures and
  D_R shell traces on Wilson backgrounds found no earlier statement of (2), (5), (6) or (10) on typical Wilson
  samples. So (6) is new as a typical-Wilson-sample statement; its selectivity is the flat one, carried to
  scales where most q-cubes are near pure gauge.

## Verdicts

| Part | Verdict |
|---|---|
| (6), two-sided shell bound, w.p. -> 1 under all sixteen twisted laws | HOLDS (range nonempty only for beta >= (8R_0)^16) |
| Selectivity: compact U(1) | HOLDS (trivially: ad h = 0) |
| Selectivity: 5D shells <= C/R for every connection | HOLDS (matching 5D lower bound c/R: the difference is the free count R^(4-d)) |
| (2) | HOLDS |
| (3), row 1141 (2)-(7) under seam signs | HOLDS (second inequality uses beta_K >= c log n) |
| Heat-walk domination by 3 x scalar trace; gap doubling | HOLDS |
| (4) | HOLDS |
| (5) and the mixed trace | HOLDS |
| (7) and both free-energy bounds | HOLDS |
| Good-cube fraction | HOLDS |
| Root-vector probability and its conditioning | HOLDS |
| Root-tree gauge error (d-1)q^-2 | HOLDS |
| Bump test spaces and (8) | HOLDS |
| Monotonicity of the quadratic trace; finish of (6); X ~ log(1+beta) | HOLDS |
| Sitewise-insertion paragraph | HOLDS |
| (9) | HOLDS |
| (10) | HOLDS |
| Exact second-derivative identity | HOLDS |
| Two-level example | HOLDS (illustration only) |
| (11) -> seed, with row 1526/1373 (2.1)-(2.3) and check 1527 (i) | HOLDS |
| (11) strictly stronger than the purity test (check 1527 (vi)) | HOLDS |
| (11) as a new statement | Not new: inf over Y gives exactly J, so (11) is equivalent to check 1527 (vi)'s direct test. Wording correction: name it as that test |
| Zero overlap of the auxiliary Gaussian test | HOLDS (tautological: independent noise) |
| Polarization example | HOLDS |
| Stopping statement (physical-radius disproof, beta = 0, spectator) | HOLDS |
| (6) beyond one lattice site, under NEG and STAB | In lattice units yes; in physical units no (R a_K -> 0). Does not escape Prop NEG (a); a small-field statement of the STAB kind. Flat version on file (row 1244 Lemma 2.2/Prop 2.3; row 1526 Thm 5(a) per check 1527 (iv)); the typical-Wilson-sample version is new |

RESULT Check 1535 of row 1530: every mathematical statement checked HOLDS; (6) holds w.p. -> 1 under all sixteen twisted Wilson laws, and both selectivity claims hold, but (6) is a small-field ultraviolet statement (scales R <= beta^(1/16)/8, physical size -> 0, nonempty only for beta >= 8^16) whose 4D/5D split is the free mode count R^(4-d); it has no consumer, does not escape Proposition NEG (a) or Remark STAB, and (11) is equivalent to check 1527 (vi)'s direct test; no progress toward PUR-io.

Checked line by line by Claude (Opus 5.5).
