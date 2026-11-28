lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-15T12:45Z

# gap-det-fable: the determinant lemma (DET), FINISH row 987

Pinned at commit 708bcda9e, branch claude/ym4d-hard-route. Working file; each
step is appended when done. Marks: PROVED, ARGUED, OPEN.

## Plan (at most eight steps)

1. Read the statement of (DET) in `library/gap-detlemma-read-opus.md` (row 986)
   and the consumer (TH) of Corollary CU (rows 978, 981). Overlap check in
   `library/open-core.md` and the FINISH rows.
2. Read the 3D analogue: YM3_I Proposition II-44-37 (L60813-60846) and
   Proposition III-7-12. Record what is proved there and by what mechanism.
3. Read the 4D target form: YM4_1400 eq:flow-RF61 (L86260-86301) and the
   status the account declares for it.
4. Read the repository's frozen hma Theorem 5 (one-torus local expansion at
   P_0). Record statement, hypotheses, the object A_S.
5. Identification: hma's A_S against the account's step normaliser. Proved, or
   stated as an OPEN input.
6. Proof of (DET) in 4D: write G_m as a sum over K steps of a torus log
   determinant; local expansion per step; volume term cancels in the density;
   the remainder is bounded by c_det(L, p).
7. Check: quantifiers, order of constants, dependence on L and p only, the
   one-sided form m' >= m. A numeric sanity run only if memory allows.
8. Verdict and next step.

## Step log


## Repo search (rule "Repo first") and overlap check (00:55Z)

- grep `determinant lemma|c_det|(DET)|flow-RF61|gaussian normali[sz]er` over
  `library/open-core.md`: no hit. Over `FINISH.md`: rows 607 (map only), 981
  (found the gap), 986 (port reading), 987 (this row). Row 988 (`gap-unit-max`)
  is the unit-scale inequality (U1)/(U2), another object. No other row covers
  (DET). Row 320 (`library/ol.md`, OL-loc) is the field-dependent part
  log Z(U) - log Z(1), which subtracts the number (DET) is about (row 986,
  Step 4): not a duplicate.
- Prior work this row builds on: row 986 (`library/gap-detlemma-read-opus.md`,
  Claude Opus 5.5): statement (DET), the sources, and the two candidate routes
  (local expansion with common lifts; Riemann sum of the symbol). Row 981
  (`library/gap-ladder-check-opus.md`): the need. `library/hma.md` Theorem 5
  (Codex, frozen): the one-torus local expansion.
- Sources: Sussman and Alpoge with Claude and Codex,
  https://github.com/ethanwsussman/Yang--Mills-LLM-experiment, shallow clone at
  HEAD c7fef8b in `/tmp/gapdet987/sa` (scratch, not committed). `~/ym4d-papers`
  does not exist on this machine (checked again, 00:50Z): Balaban's papers are
  a skipped source in this row too.

## Step 1. The statement, and the route chosen (01:00Z)

**(DET), from row 986 Step 6.** N = 2, notation of CA-II Definition 8.22;
m, m' >= m_T(g_-(g)). G_m := sum_{j<K} G^(j)(T_m), with G^(j)(T_m) the logarithm
of the Gaussian integral of step j at the trivial background on T_m. Claim:
|G_m/(2L^m)^4 - G_m'/(2L^m')^4| <= c_det, c_det depending on L and p only.

**Route chosen: one abstract lemma on the infinite lattice, then an
identification.** hma Theorem 5 gives a one-torus expansion whose two-torus use
needs a common-lift identity for every local term and the whole premise list M.
At U = 1 the comparison needs much less. I split (DET) into:

- **Lemma A (two-torus determinant lemma, abstract).** A statement about one
  real symmetric kernel on the infinite lattice Z^4 with a gap, an upper bound
  and exponential decay, and its periodizations on two tori. Elementary:
  logarithm series, a tilted (Combes-Thomas) operator-norm bound, and the fact
  that periodization is an algebra homomorphism. No walk expansion, no Moebius
  inversion. Written and proved in Step 2.
- **Corollary B.** (DET) with an explicit c_det, from Lemma A and three
  structural inputs (S1)-(S3) on the step forms at U = 1: (S1) the step-j
  Gaussian integral on T_m is exp of [torus-free scalar times a lattice count]
  times det^{-1/2} of the periodization of ONE infinite-lattice kernel A_j,
  the same for all tori; (S2) A_j has gap, bound and decay uniform in j and K;
  (S3) sides: the level-j lattice of T_m has side 2 L^m L^(K-j) in its own
  units. Step 3.
- **Identification.** (S1)-(S3) against the sources: YM3_I II-44-37 /
  III-7-12, YM4_1400 RF61, hma D3/D5 at P_0, and the flat package. Steps 4-6.

Lemma A replaces, at U = 1 only, both the "local terms with common lifts"
(item (iii) of row 986 Step 6) and the decay rate above the entropy rate
(item (ii)): the comparison is made on closed-walk sums directly, where no
polymer entropy enters.

## Step 2. Lemma A, the abstract two-torus determinant lemma: PROVED (01:20Z)

Self-contained; uses only finite sums, absolutely convergent series, the Schur
test, and eigenvalues of a real symmetric matrix.

**Setting.** d >= 1 and l >= 1 integers. X = Z^4 x {1,...,d}; for x = (s,a),
y = (t,b) write |x-y| = |s-t|_1 (the l^1 norm on Z^4) and x+v = (s+v,a) for
v in Z^4. A *kernel* is a real function on X x X. For n a positive multiple of
l, Gamma_n = nZ^4, T_n = X/Gamma_n (a finite set with d n^4 points), and for a
kernel K with K(x+v,y+v) = K(x,y) for v in Gamma_n and sup_x sum_y |K(x,y)|
finite,

  Per_n(K)(xbar,ybar) := sum_{v in Gamma_n} K(x,y+v).

**Hypotheses on the kernel A.** Constants mu_0 > 0, C_A >= gamma > 0, B >= gamma.
- (A0) A(x,y) = A(y,x).
- (A1) A(x+v,y+v) = A(x,y) for all v in lZ^4.
- (A2) sum_y |A(x,y)| e^{mu_0 |x-y|} <= C_A for every x.
- (A3) gamma |f|^2 <= <f,Af> <= B |f|^2 for every finitely supported real f on X
  (|f| the l^2 norm; <f,Af> = sum_{x,y} f(x)A(x,y)f(y)).

**Constants.** nu := mu_0 gamma/(2 C_A) (so nu <= mu_0/2), q' := 1 - gamma/(2B),
c_eps := e^{nu} [coth(nu/2)^4 - 1].

**Lemma A.** Under (A0)-(A3) there is a real number a(A), defined in (A.5)
below from the kernel A alone, such that for every positive multiple n of l:
1. A_n := Per_n(A) is a real symmetric matrix on T_n with all eigenvalues in
   [gamma/2, 2B];
2. | (d n^4)^{-1} log det A_n - a(A) | <= log(2B/gamma) c_eps e^{-nu n}.

*Proof.*

(a) *Operators.* By (A0), (A2) and the Schur test, A is a bounded symmetric
operator on l^2(X) with norm at most C_A; (A3) extends to all of l^2(X). Put
T := 1 - A/B. Then 0 <= <f,Tf> <= (1-gamma/B)|f|^2, so the operator norm of T
is at most q := 1 - gamma/B.

(b) *Tilt.* For theta in R^4 with |theta|_infty <= mu_0 put
A_theta(x,y) := e^{theta.(s-t)} A(x,y) (x = (s,a), y = (t,b)). Since
|theta.(s-t)| <= |theta|_infty |x-y| and e^{rt}-1 <= (r/mu_0)(e^{mu_0 t}-1) for
0 <= r <= mu_0, t >= 0 (convexity in r),

  |A_theta(x,y) - A(x,y)| <= (|theta|_infty/mu_0) |A(x,y)| e^{mu_0|x-y|}.

Rows sum to at most (|theta|_infty/mu_0) C_A by (A2), columns too by (A0). By
the Schur test |A_theta - A|_op <= (|theta|_infty/mu_0) C_A. For
|theta|_infty = nu this is gamma/2, so T_theta := 1 - A_theta/B has

  |T_theta|_op <= q + gamma/(2B) = q'.                                (A.1)

(c) *Decay of powers.* Kernels with sup_x sum_y |K(x,y)| e^{mu_0|x-y|} finite
are closed under kernel product (triangle inequality for |.|), all sums
absolutely convergent, and K -> K_theta is multiplicative on them:
(KK')_theta = K_theta K'_theta, because e^{theta.(s-t)} = e^{theta.(s-r)}
e^{theta.(r-t)}. So (T^k)_theta = (T_theta)^k for k >= 0, i.e.
T^k(x,y) = e^{-theta.(s-t)} (T_theta)^k(x,y). A matrix element between two
unit vectors is at most the operator norm, so |(T_theta)^k(x,y)| <= q'^k by
(A.1). Choosing theta = nu sign(s-t) (componentwise) gives

  |T^k(x,y)| <= q'^k e^{-nu |x-y|}   for all x, y, k >= 0.            (A.2)

(d) *Periodization is multiplicative.* Let K, K' be Gamma_n-covariant with
finite sup_x sum_y |.|. Then, all sums absolutely convergent,

  Per_n(KK')(xbar,ybar) = sum_v sum_z K(x,z) K'(z,y+v)
   = sum_{zbar} sum_{w in Gamma_n} K(x,z+w) sum_v K'(z+w,y+v)
   = sum_{zbar} sum_w K(x,z+w) sum_v K'(z,y+v-w)
   = sum_{zbar} Per_n(K)(xbar,zbar) Per_n(K')(zbar,ybar),

(z runs over one representative of each class; covariance of K' in the third
line; v -> v+w in the fourth). Per_n is linear and Per_n(1) = 1. Hence, with
S := Per_n(T) = 1 - A_n/B,

  S^k = Per_n(T^k),   k >= 0.                                         (A.3)

S is symmetric: Per_n(A)(ybar,xbar) = sum_v A(y,x+v) = sum_v A(x+v,y)
= sum_v A(x,y-v) = Per_n(A)(xbar,ybar), by (A0), (A1).

(e) *Spectrum of S.* By (A.2), (A.3), for every xbar, ybar,
|S^k(xbar,ybar)| <= q'^k sum_{v in Gamma_n} e^{-nu|x-y-v|} <= q'^k c_0, with
c_0 := (2/(1-e^{-nu n}))^4 (the sum factorizes over the four coordinates; in
one coordinate, for an integer a and each i >= 0, at most two w in Z have
|a-nw| in [in,(i+1)n), so sum_w e^{-nu|a-nw|} <= 2 sum_{i>=0} e^{-nu n i}). If
S f = lambda f, f != 0, then |lambda|^k |f|_infty <= d n^4 c_0 q'^k |f|_infty
for all k, so |lambda| <= q'. S is real symmetric, so its eigenvalues
lambda_1,...,lambda_{d n^4} are real and lie in [-q', q']. The eigenvalues of
A_n = B(1-S) are B(1-lambda_i), in [B(1-q'), B(1+q')], which is inside
[gamma/2, 2B]. This is assertion 1.

(f) *Logarithm.* For real |lambda| <= q' < 1, log(1-lambda) = -sum_{k>=1}
lambda^k/k, absolutely convergent. Summing over the eigenvalues,

  log det A_n = d n^4 log B - sum_{k>=1} (1/k) tr S^k,                (A.4)

absolutely convergent since |tr S^k| <= d n^4 q'^k.

(g) *Split of the trace.* By (A.3),
tr S^k = sum_{xbar in T_n} T^k(x,x) + sum_{xbar} sum_{v in Gamma_n, v != 0}
T^k(x,x+v). By (A1), T^k(x+v,x+v) = T^k(x,x) for v in lZ^4, and T_n is the
disjoint union of (n/l)^4 translates of the cell C := {0,...,l-1}^4 x {1,...,d};
so the first sum is d n^4 tau_k with

  tau_k := (d l^4)^{-1} sum_{x in C} T^k(x,x),  |tau_k| <= q'^k,
  a(A) := log B - sum_{k>=1} tau_k/k.                                 (A.5)

a(A) is defined by A, B, l, d only; n does not enter. By (A.2) the second sum
is at most d n^4 q'^k eps(n) in modulus, where, with r = e^{-nu n},

  eps(n) := sum_{w in Z^4, w != 0} e^{-nu n |w|_1} = ((1+r)/(1-r))^4 - 1.

((1+r)/(1-r))^4 - 1 is a power series in r with non-negative coefficients and
zero constant term, so eps(n)/r is non-decreasing in r; n >= 1 gives
r <= e^{-nu}, hence eps(n) <= c_eps e^{-nu n}. Dividing (A.4) by d n^4:

  |(d n^4)^{-1} log det A_n - a(A)| <= sum_{k>=1} (q'^k/k) eps(n)
     = log(1/(1-q')) eps(n) = log(2B/gamma) eps(n) <= log(2B/gamma) c_eps e^{-nu n}.

This is assertion 2. QED

**Remarks.**
1. a(A) does not depend on the choice Lambda = B (it is the limit of the left
   side of 2 as n grows); not used.
2. No polymer, no entropy factor, no Moebius inversion: the comparison is on
   closed walks, and the wrapping walks are bounded through (A.2). The decay
   rate nu may be arbitrarily small; only nu > 0 is used.
3. The lemma needs the gap on the INFINITE lattice (A3) and gets the torus gap
   as a conclusion (assertion 1). If instead a gap is known on tori only, the
   same proof runs between two tori n | n' with Per from T_n' to T_n (the
   one-sided form), provided the kernel on T_n' has (A2) with the torus
   distance; then the error is taken relative to T_n'. Not written out.
4. Complex extension is not needed: the kernel is real at U = 1.

Stopped here: Lemma A is complete. Next: Corollary B (Step 3), then the
identification against the sources.

## Step 3. Lemma A' (torus to torus) and Corollary B: PROVED as implications (01:45Z)

The frozen statements of this repository (hm (4), import R) are on finite tori,
uniform in the volume, not on Z^4. So the form used below is the nested-torus
form of Lemma A; its proof is the same and is finite-dimensional throughout.

**Setting.** d, l as in Step 2; n | n', both positive multiples of l.
X_n := (Z/n)^4 x {1,...,d}; |x-y|_n the l^1 distance on the torus (minimum of
|v|_1 over lifts v of the difference of base points). pi: X_n' -> X_n the
quotient map, Gamma := nZ^4/n'Z^4 (acting freely on X_n', X_n = X_n'/Gamma),
pi^* f := f o pi. For a real matrix K on X_n' with K(x+g,y+g) = K(x,y) for
g in Gamma, Per(K)(xbar,ybar) := sum_{g in Gamma} K(x,y+g).

**Lemma P (periodization is restriction to periodic vectors).** For K, K' as
above: (i) K pi^* = pi^* Per(K), and Per(K) is the only matrix with this
property; (ii) Per(KK') = Per(K)Per(K'), Per(1) = 1, Per(K^T) = Per(K)^T, Per
linear; (iii) if K is invertible then K^{-1} is Gamma-covariant, Per(K) is
invertible and Per(K^{-1}) = Per(K)^{-1}; (iv) <f,Per(K)f> = (n/n')^4
<pi^*f, K pi^*f>, so gamma <= K <= B (K symmetric) implies
gamma <= Per(K) <= B. The same holds for rectangular Gamma-covariant matrices
between two index sets with free Gamma-actions (several lattice levels).
*Proof.* (i) (K pi^* f)(x) = sum_{y in X_n'} K(x,y) f(pi y) = sum_{ybar}
sum_g K(x,y+g) f(ybar); the right side depends on x through xbar only, by
covariance. pi^* is injective, so the matrix is unique. (ii) from (i) and
injectivity of pi^*: K K' pi^* = K pi^* Per(K') = pi^* Per(K)Per(K'); the
transpose by the substitution g -> -g and covariance. (iii) K^{-1} commutes
with the translations since K does; apply (ii) to K K^{-1} = 1. (iv)
|pi^* f|^2 = (n'/n)^4 |f|^2 and <pi^*f, pi^* h> = (n'/n)^4 <f,h>. QED

**Lemma A'.** Let A' be a real symmetric matrix on X_n' with
- (A1') A'(x+v,y+v) = A'(x,y) for v in lZ^4;
- (A2') sum_y |A'(x,y)| e^{mu_0 |x-y|_n'} <= C_A for every x;
- (A3') gamma <= A' <= B as quadratic forms, 0 < gamma <= B.
Put A := Per(A') on X_n, nu := mu_0 gamma/(2 C_A), q' := 1 - gamma/(2B),
eps(n) := coth(nu n/2)^4 - 1 <= c_eps e^{-nu n}, c_eps := e^{nu}[coth(nu/2)^4-1].
Then gamma <= A <= B and

  | (d n^4)^{-1} log det A - (d n'^4)^{-1} log det A' | <= log(2B/gamma) eps(n).

*Proof.* gamma <= A <= B is Lemma P (iv). T' := 1 - A'/B has 0 <= T' <= q
:= 1 - gamma/B; S := Per(T') = 1 - A/B has 0 <= S <= q by Lemma P; S^k =
Per(T'^k) by Lemma P (ii).
*Decay.* Fix x in X_n' and put rho(z) := |z-x|_n', so |rho(z)-rho(w)| <=
|z-w|_n'. Let E := diag(e^{-nu rho}). The entries of E A' E^{-1} - A' are
A'(z,w)(e^{-nu(rho(z)-rho(w))}-1), of modulus at most |A'(z,w)|
(e^{nu|z-w|}-1) <= (nu/mu_0)|A'(z,w)| e^{mu_0|z-w|} (convexity, as in Step 2
(b)). Rows and columns sum to at most (nu/mu_0)C_A = gamma/2 by (A2') and
symmetry; Schur gives |E T' E^{-1} - T'|_op <= gamma/(2B), so
|E T' E^{-1}|_op <= q'. Now T'^k = E^{-1}(E T' E^{-1})^k E, hence
T'^k(x,y) = e^{nu rho(x)} (E T' E^{-1})^k(x,y) e^{-nu rho(y)}, and rho(x) = 0:

  |T'^k(x,y)| <= q'^k e^{-nu |x-y|_n'}   (all x, y, k >= 0).          (A'.1)

*Trace.* tr S^k = sum_{xbar in X_n} sum_{g in Gamma} T'^k(x,x+g). The g = 0
part is sum_{xbar in X_n} T'^k(x,x) = (n/n')^4 tr T'^k, because T'^k(x,x) is
invariant under lZ^4 (A1'), hence under Gamma, and each class has (n'/n)^4
points. For g != 0 the difference x+g-x has a lift v in nZ^4, v != 0, of
minimal l^1 norm, distinct g giving distinct v; with (A'.1),

  | (d n^4)^{-1} tr S^k - (d n'^4)^{-1} tr T'^k | <= q'^k sum_{v in nZ^4, v != 0}
     e^{-nu |v|_1} = q'^k eps(n).

*Logarithm.* The eigenvalues of S and of T' lie in [0,q], so log det A =
d n^4 log B - sum_{k>=1} tr S^k/k and the same for A', both absolutely
convergent. Subtract the densities: the difference is at most
sum_k q'^k eps(n)/k = log(2B/gamma) eps(n). The bound eps(n) <= c_eps e^{-nu n}
is Step 2 (g). QED

**Corollary B ((DET) from three structural inputs).** Fix L and the range of m.
Suppose that for every K >= 1, every j < K and every m in the range:
- (S3) the coordinates of step j on T_m are indexed by X_n with
  n = n_{j,m} := 2 L^{m+K-j} and a fixed d (so n_{j,m}^4/(2L^m)^4 = L^{4(K-j)});
- (S1) G^(j)(T_m) = c_{j,K} n_{j,m}^4 - (1/2) log det A_{j,K,m}, where c_{j,K}
  is a real number that does not depend on m, A_{j,K,m} is a real symmetric
  matrix on X_n covariant under LZ^4, and for m <= m' in the range
  A_{j,K,m} = Per(A_{j,K,m'});
- (S2) A_{j,K,m} satisfies (A2'), (A3') with constants mu_0, C_A, gamma, B that
  do not depend on j, K, m.
Then for m <= m' in the range and every K,

  | G_m/(2L^m)^4 - G_m'/(2L^m')^4 |
     <= (d/2) log(2B/gamma) sum_{u=1}^{K} L^{4u} eps(2 L^{m+u})
     <= c_det := (d/2) log(2B/gamma) c_eps (15/(4 nu^5)) L^{-5m}/(L-1).

c_det depends on d, mu_0, C_A, gamma, B, L (and decreases with m); not on K,
m'. No bound on the numbers c_{j,K} is used: they cancel exactly.
*Proof.* By (S1), (S3), G^(j)(T_m)/(2L^m)^4 = L^{4(K-j)} [c_{j,K} - (d/2)
(d n^4)^{-1} log det A_{j,K,m}]. Subtract the same at m'; c_{j,K} cancels;
Lemma A' (l = L, n = n_{j,m}, n' = n_{j,m'}, n | n') bounds the rest by
(d/2) L^{4(K-j)} log(2B/gamma) eps(2L^{m+K-j}). Sum over j, u = K-j. For the
last bound, e^{-t} <= 120/t^5 (t > 0) gives L^{4u} c_eps e^{-2 nu L^{m+u}} <=
c_eps (120/(32 nu^5)) L^{-5m} L^{-u}, and sum_{u>=1} L^{-u} = 1/(L-1). QED

**What is left after Step 3.** (DET) is now exactly (S1)-(S3) for the
account's step. (S3) is bookkeeping. (S2) is a gap, an upper bound and kernel
decay of the step's quadratic form at U = 1 on a torus, uniform in level and
volume. (S1) has two parts: the scalar factors are per-coordinate with
torus-free coefficients, and the form on the smaller torus is the
periodization of the form on the larger. By Lemma P the second part follows
whenever the form is built from stencil operators (the same local rule on
every torus) by sums, products, transposes and inverses: a stencil operator R
satisfies R pi^* = pi^* R by definition, and Lemma P (ii), (iii) carries this
through the algebra. Steps 4-6 check these against the sources.

## Step 4. The ports: what the three named sources give, and what Step 2-3 change (02:10Z)

Sussman and Alpoge (with Claude and Codex), repository at HEAD c7fef8b; read at
the lines row 986 located.

1. **YM3_I Proposition II-44-37 and L60813-60846 (3D, proved there).** The
   trivial-background value is expanded by the logarithm series of a gapped
   positive form: "f_b(Y;P) = 3 log c_N - sum_{n>=1} (1/n) tr T_Y^n(b,b)",
   T_Y = 1 - c_N^{-1} A_{Y,N}, |T_Y| <= q_N < 1 (L40737-40755), then Moebius
   inversion over coarse regions gives local terms n^(j)(X,b) = -(1/2)
   E^N(X;P_0,b) with |n^(j)(X,z)| <= E_N e^{-delta_N M d_j(X)} (II-45-8,
   II-45-65, L60818-60835), and "The same change of coordinates used for the
   normalizer transports these constants between local lattice charts. In
   particular, their definition does not introduce a choice of a larger torus"
   (L60843-60846). Proposition III-7-12 then compares two tori term by term.
   **Ported here:** the logarithm series of 1 - A/Lambda (Step 2 (f), Step 3).
   **Changed:** no Moebius inversion and no local family at U = 1; the series
   is compared on closed walks through Lemma P, so the 4D case needs no
   analogue of the local-chart identity and no decay rate above the polymer
   entropy. Credit for the mechanism (log series of the gapped form; the
   torus-free extensive coefficients II-192-10) is theirs.
2. **YM4_1400 eq:flow-RF61 (L86260-86301; 4D, a target there).** "n_k^tot =
   36 N_{k+1} log L - (1/2) log det(C^T Delta^(k) C)|_1", "C is the actual
   linear embedding of nonpivot coordinates into full constrained
   fluctuations; this determinant is on the free color coordinates", count
   N^(k) "with -3 log theta_k/2 per free bond", and "The determinant estimates
   and first-step sign in (RF61) remain actual Gaussian targets". This has the
   shape of (S1): scalars times counts, plus -(1/2) log det of one form on the
   free coordinates. Of the three targets in RF61, Corollary B addresses the
   two-torus comparison that (TH) needs, and (S2) gives |log det| <= d n^4
   max(|log gamma|, |log B|), which is the form of |n_k^tot| <= C N_{k+1}
   (ARGUED, on (S2)). The local family n^(k+1)(X,z) with common lifts and the
   first-step sign n_0^tot < 0 are NOT addressed here; (DET) does not need them.
3. **Repository, frozen `library/hma.md` Theorem 5 and D3, D5 (4D).** D3 (3):
   A^Y(P) = C_V^T [iota^T {(Q G_1 Q^T)^{-1} - a} iota + G^Y_V - E_amb[...J]]
   C_V; D5: full Gaussian S = I; Theorem 5 (16): -(1/2) log det A_S =
   -(1/2)|S| log Lambda + sum_X N_S(X;P), valid at P_0; and after (21): "A
   ratio tau adds -|S|_scalar Log tau/2, assigned per integrated coordinate;
   u -> b adds the corresponding fixed theta_j scalar factor". **Ported
   here:** the form (the operator whose determinant is the step's Gaussian
   value on the free coordinates, and the per-coordinate scalars). **Not used
   here:** the local family N_S and its bound (19); Lemma A' replaces them at
   U = 1. So this row does not depend on hma's premise list M beyond the two
   statements quoted in Step 5.

## Step 5. (S1)-(S3) for the repository's step form at U = 1 (02:25Z)

The form is `library/pr-lay.md` (6)-(7) (frozen; "This is SA 10200-10208 and
14091-14107 with active injections explicit", pr-lay L83), equal at a real
axial V to hma's A^Y (hma D2, L30: "At a real axial V it is SA 7181-7182").
Take U = 1 on a torus with no large-field region (Omega_0 = ... = Omega_{k+1}
= the torus, so the separation condition pr-lay (1) is empty), depth k = j,
P_0 = (1,0,0). Then J = 0, so in pr-lay (6) G = G_0 = G_1, and

  A_j := A(P_0) = C^T [ iota^T {(Q G_0 Q^T)^{-1} - a} iota + K_GF ] C,
  G_0 = (Delta^W + D R D^T + Q^T a Q)^{-1},
  R = 1 - G' Q'^T (Q' G'^2 Q'^T)^{-1} Q' G',  G' = (D^T D + Q'^T a Q')^{-1}.

**(S3): ARGUED (bookkeeping).** With T_m of side 2L^m in level-K units (CA-II
Definition 8.22 (b): the volume (2L^m)^4), the level-j lattice has side
2L^{m+K-j}; free coordinates are the positively stored non-pivot level-j
bonds with three colours, "at most twelve coordinates per site" (pr-lay L24).
The number of coordinates per site is not constant (pivots are removed), so
X_n is to be read as: a set with a free action of the translations of the
torus by L Z^4 and a fixed number d_L of coordinates per L-block. Lemma P and
Lemma A' use only a free action of Gamma on a finite index set and a distance
with |x+g-x| >= |v|_1 for the minimal lift v; with "d n^4" replaced by the
number of coordinates, d_L (n/L)^4, the proofs are unchanged.

**(S1), periodization part: ARGUED from Lemma P, on a reading of the imported
definitions.** Each primitive in the display (D, D^T: covariant difference at
U = 1; Q, Q': the straightened averages at U = 1; a: the row weights;
Delta^W: the Wilson Hessian at 1; K_GF: the Hessian of the soft gauge
functional at V = 1; C: the derivative of the pivot graph at V = 1; iota) is
defined by a finite stencil rule that reads the lattice near a point, the same
rule on every torus. For such an operator R, R_{n'} pi^* = pi^* R_n holds by
definition (apply the rule to a periodic field). Lemma P (ii), (iii), in its
rectangular form across the bare lattice and the level-j lattice, carries this
through the sums, products, transposes and the four inverses of the display,
provided the inverses exist on the larger torus (pr-lay W, L103: "all inverses
in (6)-(7) exist"). Hence A_j on T_m is Per of A_j on T_m' (m <= m').
What is read and not proved here: that every primitive is such a stencil rule
at U = 1, and that the pivot choice and the gauge-fixing choice on T_m' are
the pull-back of those on T_m (YM4_1400 L102650-102654 asserts "fixed choice
of gauges give the same two scalars for the two tori"). pr-lay L74: "These
maps, their branches and boundary conventions are imported". This is the
first input to check against the definitions (I-loc).

**(S1), scalar part: ARGUED.** By hma (21) with S = I the Gaussian integral
over the free coordinates is (2 pi)^{|I|/2} (det A_j)^{-1/2}; the ratio tau,
the change of variable u -> b (theta_j) and the pivot Jacobian (YM4_1400:
36 log L per coarse site) are scalars per coordinate or per coarse site
(hma L275; RF61). On a torus without large-field region every count is an
exact multiple of the number of L-blocks, with torus-free coefficients
provided the coupling sequence is the same on both tori (CA-II lemma,
hypothesis of a common sequence; YM4_1400 L102576). So G^(j)(T_m) =
c_{j,K} n^4 - (1/2) log det A_j with c_{j,K} free of m.

**(S2): PORTED, conditional on the frozen imports R and W of hm/pr-lay.**
- Gap: pr-lay R (L99): "A(P_0) exists, is real symmetric, and A(P_0) >= c_L I
  whenever the longer sequence satisfies those floors and U has real bound
  < a_R in the stated axial representative". U = 1 has real bound 0 and is
  axial (all contours are I). So gamma = c_L.
- Decay and upper bound: hm Lemma 1 (4): the precision is a sum of labelled
  terms with max of row and column sums of e^{mu_W t_omega} m_omega(x,y) at
  most W, t_omega >= d(x,y), d the periodic l^infty distance of base points
  (hm L13), and "At global pairs the resulting fixed-region expansion sums to
  the actual symmetric precision (7) of pr-lay" (hm L42). Since |.|_1 <=
  4|.|_infty: (A2') with mu_0 = mu_W/4, C_A = W; and B = W by Schur.
- Uniformity: hm L49: "All imported constants/floors are uniform in depth,
  volume, region shape and larger admitted layer gaps." c_L, W, mu_W are
  early constants depending on L and the fixed parameters.
- Conditions: the torus room of pr-lay L26 on the LARGER torus only (Lemma A'
  uses (S2) for A' only; the smaller torus gets gamma <= A <= B from Lemma P).
  R and W are themselves conditional in the library (pr-lay L101, L112: flat
  c0-loc inputs, a2-curved inputs, h-walk gate repairs). At U = 1 the curved
  inputs are evaluated at the flat background; whether they then reduce to
  the checked flat package (row 95, `library/flat-port.md`) was not traced in
  this row.

**Result of Step 5.** For the repository's step form (pr-lay (7) = hma D3 at
U = 1, full torus), (DET) holds with

  c_det = (d_L/(2L^4)) log(2W/c_L) c_eps (15/(4 nu^5)) L^{-5m}/(L-1),
  nu = mu_W c_L/(8W),  c_eps = e^{nu}[coth(nu/2)^4 - 1],

m = min(m, m'), given (I-loc) and the imports R, W. The constant depends on L
and the fixed parameters only; not on K, g_0, g, m'. Status: PROVED as an
implication from (I-loc), R, W; each of those is ARGUED or imported, as marked.

## Step 6. Identification with the account's step normaliser: OPEN input (02:35Z)

The account does not define its Gaussian integral; it cites it. CA-I
Definition 4.2 (a) (L3769-3775): "Z^(j-1) is the Gaussian integral that
normalises the fluctuation measure of step j, as in [(3.28)]{B-CMP119} and
{B-CMP116}." CA-II hypothesis (a) (L141289-141290): "the logarithm of the
Gaussian integral of step j at the trivial background". Balaban's papers are
not on this machine (`~/ym4d-papers` absent), so CMP 119 (3.28) and CMP 116
Sections 1-2 were not read, and nothing below is quoted from them.

**(ID), the identification, stated as an OPEN input.** For every j < K and
every torus T_m in the range, Balaban's Z^(j)(1) on T_m (CMP 119 (3.28)) is

  Z^(j)(1) = exp[c_{j,K} #(T_m at level j)] det(A_j)^{-1/2},

with c_{j,K} torus-free and A_j a real symmetric positive form on the free
(constraint- and gauge-reduced) coordinates that is (i) built from stencil
operators at U = 1 by sums, products, transposes and inverses, and (ii)
satisfies (A2'), (A3') uniformly in j and the volume.

What supports (ID) without settling it: `library/ol.md` L52 (row 320, on CMP
109 (1.22)): "The Gaussian includes the constraint and gauge Jacobians of
Balaban's step"; `library/b109.md` L131-132: the Haar/coarea factors, pivot
and Gaussian normalization are CMP 109 (0.11)-(0.16), (1.4)-(1.5),
(2.4)-(2.13), and "this alone does not identify every Haar or determinant
factor of the physical integral"; YM4_1400 RF61 writes the 4D number as
-(1/2) log det(C^T Delta^(k) C)|_1 plus counts; hma L277: "SA 17528-17545
uses the compressed determinant in (21), together with elimination factors
z^(j)" and "this determinant theorem does not prove the z^(j) bounds". On a
torus with no large-field region and U = 1 there is no conditional step and
no elimination factor, so only the full determinant S = I occurs (ARGUED).

Corollary B does not care which form it is: any definition of the step's
Gaussian integral at U = 1 that satisfies (S1)-(S3) gives (DET). So (ID) (i)
is a reading task (the definition in CMP 119 (3.28) / CMP 116 against Lemma
P), and (ID) (ii) is Balaban's flat propagator estimates (CMP 95, 96; row 95)
for his Delta^(k) at U = 1 reduced to the free coordinates. Neither needs a
new estimate if the definitions are as RF61 and pr-lay (7) write them.

## Step 7. Check of the argument (02:45Z)

1. *Quantifiers and order of constants.* L and the fixed parameters; then the
   early constants c_L, W, mu_W of hm (before kappa, hm L49); then nu, c_eps,
   c_det. K, j, m' arbitrary afterwards. c_det is non-increasing in m; at the
   bottom of the range it is a number depending on L and p only. No cycle.
2. *Hypothesis (A1') is not needed in full.* The proof of Lemma A' uses only
   covariance under Gamma = nZ^4/n'Z^4 (for Per to exist and for
   sum_{xbar} T'^k(x,x) = (n/n')^4 tr T'^k). Covariance under LZ^4 is not
   used. So the pivot pattern need not be block-periodic, only pulled back
   from the smaller torus.
3. *Where the gap is used.* Only in q' < 1 and nu > 0. If the form had a zero
   mode on a torus (constant fields), (A3') would fail and the lemma with it;
   in pr-lay (7) the averaging constraint and the axial gauge remove them
   (import R). A form with a torus-dependent zero-mode treatment would break
   (S1); none appears in pr-lay (6)-(7).
4. *One-sided or two-sided.* Two tori of the family are always nested
   (2L^m | 2L^m'), so the bound is two-sided for every pair, with
   m = min(m, m'). (TH) needs only one side.
5. *Uniformity in K.* The sum over levels is sum_{u>=1} L^{4u} eps(2L^{m+u}),
   convergent with a bound free of K; this is the point where a torus-wide
   number of order one per level would have cost K (2L^m)^{-4} (CA-II
   L141426-141432). Here the per-level error is exponentially small in the
   side of that level's lattice.
6. *No computer-assisted step.* None. The toy run prepared as a refutation
   test (`/tmp/gapdet987/scripts/check_Aprime.py`, two-dimensional tori, pass
   and fail criteria written first) was NOT run: the numeric lock was held by
   `lane980-pinsheet-guide-w2` until 10:44Z (memory free 70 percent, so memory
   was not the obstacle). Lemma A' was checked by hand only.
7. *Lean-formalizable.* Lemma P is linear algebra over a finite quotient;
   Lemma A' uses the Schur test, similarity by a diagonal matrix, eigenvalues
   of a real symmetric matrix, and log(1-x) = -sum x^k/k on [0,q].
   Lemma A (infinite lattice) additionally uses bounded operators on l^2(X);
   it is not needed for Corollary B.
8. *Not independently checked.* Written by one model in one session; by the
   model rule an Opus line-by-line check is owed before any use.

## Step 8. Verdict and next step (02:50Z)

| Statement | Mark |
|---|---|
| Lemma A (infinite lattice to torus) | PROVED |
| Lemma P (periodization = restriction to periodic vectors) | PROVED |
| Lemma A' (nested tori) | PROVED |
| Corollary B: (S1)-(S3) imply (DET), explicit c_det, K-free, two-sided | PROVED |
| (S3) sides and counts | ARGUED |
| (S1) for pr-lay (7)/hma D3 at U = 1 (periodization via Lemma P; per-coordinate scalars) | ARGUED, on reading (I-loc) |
| (S2) for the same form: gap c_L, decay mu_W, bound W, uniform | PORTED from frozen hm (4), pr-lay R; conditional on imports R, W |
| (DET) for the repository's step form | PROVED as an implication from (I-loc), R, W |
| (ID): the account's Z^(j)(1) (Balaban CMP 119 (3.28)) has the form (S1)-(S2) | OPEN input (papers absent here) |
| RF61's local family with common lifts, and the first-step sign | not addressed; not needed by (DET) |

**Next step (for the lead; not done here).**
1. A reading row on the machine that has the scans: CMP 119 (3.28) and CMP 116
   Sections 1-2 (and CMP 109 (1.4)-(1.7), (2.4)-(2.13)), to settle (ID) (i):
   write Balaban's Z^(k)(1) as scalars per coordinate times det^{-1/2} of a
   form in stencil operators; and (ID) (ii) from the flat package of row 95.
2. An Opus line-by-line check of Lemma P, Lemma A', Corollary B and of the
   reading (I-loc) of pr-lay (6)-(8) at U = 1.
3. The toy run, when the numeric lock is free (a guide; it can only refute).
4. Row 981's open input can then read: "(DET) follows from Corollary B of
   `library/gap-det-fable.md` given (ID); delta = delta-bar_vac + c_det".

RESULT: Row 987 (Claude Fable 5.2 medium, Mac mini worker 3; one session, checked by no one, no numeric run: the lock was held by lane 980). PROVED: Lemma A' (for a real symmetric matrix on a torus with gap gamma, bound B and kernel decay (mu_0, C_A), and its periodization on any sub-torus of side n, the log-determinant densities differ by at most log(2B/gamma)[coth(nu n/2)^4 - 1], nu = mu_0 gamma/(2 C_A)), with Lemma P (periodization is restriction to periodic vectors, so it passes through sums, products, transposes and inverses) and the infinite-lattice Lemma A; and Corollary B: if the step-j Gaussian integral at U = 1 is exp(torus-free scalar times count) times det^{-1/2} of one such form with constants uniform in level and volume, then |G_m/(2L^m)^4 - G_m'/(2L^m')^4| <= c_det = (d/2) log(2B/gamma) c_eps (15/(4 nu^5)) L^{-5 min(m,m')}/(L-1), two-sided, free of K, g_0, g. For the repository's step form (pr-lay (7) = hma D3 at U = 1) the inputs are PORTED from frozen hm (4) and pr-lay R (gap c_L, decay mu_W, bound W; conditional on their imports R, W) and ARGUED by Lemma P on a reading of the imported definitions as stencil operators (I-loc). The mechanism (log series of the gapped form, torus-free counting coefficients) is Sussman and Alpoge's YM3_I II-44-37 / III-7-12; the 4D change is that closed walks are compared through periodization, so no local family, common-lift identity or entropy rate is needed. OPEN: (ID), that the account's step normaliser (Balaban CMP 119 (3.28), cited and not defined in CA) is of that form, since Balaban's papers are absent on this machine; (I-loc); the Opus check; RF61's local family and first-step sign are not addressed.
