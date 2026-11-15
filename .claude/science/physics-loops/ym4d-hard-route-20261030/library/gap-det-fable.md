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
