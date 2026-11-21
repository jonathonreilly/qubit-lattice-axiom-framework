# Check of row 1319 (gap-solve37-astra62.md) — FINISH row 1320

Checker: Claude Opus 5.5, line by line, by hand.
File checked: `library/gap-solve37-astra62.md` (row 1319, by gpt-6.2-astra).
Context read: rows 1315, 1317 and their checks, row 1215, and the thermal
criterion in `library/prior/gap-onebound-read-sol.md` (row 1218).
Clone revision at start: 199e7dc32.

Verdicts are added below as each section is finished.

Method. I derived each step by hand. I ran no numerics. Line numbers refer
to the checked file. The file has 37 PROVED blocks. Each gets one verdict
below. Precisions that change no claim are marked "Precision".

Credits. The transfer and reflection-positivity conventions are those of
Osterwalder and Seiler and of Lüscher, as used in rows 1215 and 1317. The
thermal criterion (A-B*, A-B**, Theorem F) is due to Deep Bhattacharjee,
Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo
John Sessford and Sanjeevan Singha Roy, as read in row 1218. The scope
remark on scalar reconstruction is from Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text.

## 1. The Wilson exclusions (9) and (17)

These rest on the one-link law (L21), the density bound (1), the slice
bound (2), the cell bound (11) and the bound (16). I check those first.

- L21. HOLDS. A spatial link lies in six plaquettes of the 4D torus (four
  spatial, two temporal). Each plaquette trace is Re(x g) or Re(x̄ g) for
  a unit quaternion g fixed by the other links. Each is linear in x. So
  the exponent is h·x with |h| <= 6 beta, and the trace of the chosen
  plaquette is s = v·x with |v| = 1. In the two-step bridge the middle
  link has four spatial and two temporal staples, which gives the same
  form. A bound uniform in the end frames survives frame averaging,
  because the averaged middle law is a positive mixture of the
  frame-fixed laws.

- L23-33, (1). HOLDS. Write x = s v + r(s) w with w uniform on the unit
  sphere of v-perp. The Haar density of s is (2/pi) r(s). By Archimedes the
  coordinate of w along the transverse part of h is uniform on [-1,1].
  The average of e^{b r u} is sinh(b r)/(b r). This gives the stated f.
  log f = alpha s + log sinh(b r(s)) + const. Here r is concave and
  log sinh is increasing and concave on (0, inf). So f is log-concave and
  unimodal. It is zero at s = ±1. Hence TV(f) = 2 max f. Next,
  max f <= (2/pi) e^{|h|}/Z. On the cap of radius (1+|h|)^{-1/2} about
  h/|h| one has h·x >= |h| - 1/2. The cap has Haar mass of order
  (1+|h|)^{-3/2}. So Z >= c e^{|h|}(1+|h|)^{-3/2}. The wrapped density is
  g(z) = sum_j f((j+z)/M)/M. On each cell [j/M,(j+1)/M] the sample
  differs from the integral by at most (1/M) times the variation there.
  Summing gives |g - 1| <= TV(f)/M <= C(1+beta)^{3/2}/M. This is valid
  for real M >= 1.

- L35-40, (2). HOLDS. Precision: for B > 1 the selection "all coordinates
  even" needs every side even. With an odd side n, the coordinates n-1 and
  0 are both even and adjacent. Then the 12-plaquette at a site with
  x_2 = n-1 contains a second marked link. "Even cube" must be read as
  "all sides even". With that reading, no plaquette holds two marked
  links. The parallel link of a 1-mu plaquette sits at a site with one odd
  coordinate. So the marked links are conditionally independent with laws
  of the form in L21, and the densities multiply. Then
  (1-eps)^B - 1 >= -delta and (1+eps)^B - 1 = delta give
  |prod g_k - 1| <= delta. Now (U M_i U)(x,y) = U^2(x,y) P_{x,y}(label i),
  and integrating the density over label i gives (2).

- L94-99, (9). HOLDS. With sum_i p_i g(i) = 0,
  U M_g U = sum_i g(i)(U M_i U - p_i U^2). By (2) its kernel is at most
  delta (sum_i p_i |g(i)|) U^2 pointwise. Testing on |f|, |f'| and using
  ||U^2|| = 1 gives the operator bound. On ran Pi_r one has
  ||U^{-1} Pi_r|| <= 1/r. Then Pi_r M_g Pi_r = (U^{-1}Pi_r) U M_g U
  (U^{-1}Pi_r) gives r^{-2}. For r = e^{-aE} the factor r^{-2} <= e^{2E}
  is bounded. The bound is uniform in spatial volume because delta does
  not depend on it for fixed B. The inversion step is the method of row
  1192, (7). The estimate itself is new.

- L125. HOLDS. Maximality of an h/2-separated set puts each Voronoi cell
  within h/2 of its centre, so its diameter is at most h. Separation puts
  the ball of radius h/4 inside the cell. Its Haar mass is at least c h^3.

- L127-132, (11), setup. HOLDS. The two links at a vertex v are together
  only in the 12-plaquette at v. The four vertices differ by 5 in
  direction 1, so no plaquette meets two pairs. All six plaquettes at a
  private link have vertices in {3,...,21} in every coordinate. So they lie
  in the interior {1,...,31}^4 and count in S_u. The shared plaquette gives
  beta x·Oy with O orthogonal. The other five plaquettes at each link give
  linear terms with |a_i| <= 5. The binned normalizer is at least
  (c h^3)^2 e^{-11 beta}.

- L134, (11), proof. HOLDS. This uses the high-frequency bound
  C(1+|s|)^{-1/2} from the proof of row 1317, (5). There A and B are any
  measurable functions bounded by one, so bin indicators and the phases
  e^{if}, e^{ig} are allowed. The coupling expands as
  e^{beta x·Oy} = sum_n beta^n (sum_a x_a (Oy)_a)^n / n!. This splits into
  separated terms of modulus at most one, with total weight e^{4 beta}.
  The linear factors cost e^{10 beta}. Dividing by the normalizer gives
  C h^{-6} e^{25 beta}(1+|t|)^{-1/2} per pair. The fourth power gives
  (1+2 pi |l| M)^{-2}, and the sum over l != 0 is at most s_0. The pairs
  of different cells see disjoint plaquettes. So the cell densities
  multiply, and Delta_B = (1+s_0)^B - 1.

- L198-208, (16)-(17). HOLDS. For (16), H is measurable on the
  conditioning data. Then |E[G | data]| = |int G (g - 1) dz| <=
  Delta_k int |G| dz, which gives (16). For (17), the reflection through a
  plane between cells maps cell u to cell theta u, and it maps the reading
  to the identical reading because Re tr is invariant under orientation
  reversal. Under the product reference the integral of
  conj(G(z_-)) G(z_+) is |int G dz|^2, which is zero for centred G. Then
  (11) on the 2k cells gives the upper bound. The lower bound is Wilson
  site reflection positivity (Osterwalder-Seiler), since G depends only on
  links strictly inside the positive half. Precision: (17) needs the
  centring from (16). Without it the bound reads
  |E_W[(theta conj G) G] - |int G dz|^2| <= Delta_{2k} (int |G| dz)^2.
  The passage to periodic-state limits is sound. Continuous functions of
  z_u are continuous in the links, the density sandwich survives weak
  limits, and L^1(dz) approximation is uniform in volume.

Section verdict: (9) and (17) HOLD. They exclude the stated readings
from low-energy matrix elements (9) and from reflected norms (17), in
finite volume, uniformly in volume, and in periodic limits at fixed
cutoff.

## 2. The transfer comparison (4)-(6)

- L44-54, statement of (3)-(4). HOLDS. The labels are gauge-invariant
  functions of one slice, so V acts on L^2_inv. V = J*(A⊗U)J with
  A⊗U >= 0, so V >= 0. J is bounded on a finite partition and U is
  compact, so V is compact.

- L56-60, proof of (4). HOLDS. I checked each identity:
  (J* D J) has kernel U(x,y) A_{i(x)i(y)}/sqrt(p p), JJ* = diag(M_i/p_i),
  and (C_1)_{ij} = sum_l A_il A_lj U M_l U / p_l. By (2) and A_il A_lj >= 0
  the block kernel of C_1 - D^2 is at most delta (D^2)_{ij} pointwise.
  Testing on componentwise moduli and ||D^2|| = 1 gives
  ||C_1 - D^2|| <= delta. C_1 = XX* and B_1 = X*X for X = DJ, so their
  nonzero spectra agree, and ||B_1|| <= 1 + delta. V^2 - B_1 =
  J*(C_1 - D^2)J. J and J* act by nonnegative multipliers and sums, so its
  kernel is at most delta times the nonnegative kernel of B_1. Hence
  ||V^2 - B_1|| <= delta(1+delta). The min-max (Weyl) bound for ordered
  eigenvalues of compact positive operators, with zeros appended, gives
  |lambda_j(V)^2 - d_j^2| <= delta + delta(1+delta) = (2+delta) delta.
  For vacuum normalization, |lambda_j^2/lambda_0^2 - lambda_j^2| <=
  |1 - lambda_0^2| <= (2+delta) delta, because lambda_j <= lambda_0. This
  gives the factor 2. The list d_j contains 1·u_j for every Wilson
  eigenvalue u_j, so every Wilson level appears among the products. A
  rank-one A gives the one-slice multiplier of row 1317, (8), as L60 says.

- L62-68, (5). HOLDS. Tr V^T is a sum over label strings of
  prod_t A_{i_t i_{t+1}}/p_{i_t}, times Tr U^T times the Wilson path
  probability of the string. Each site carries two factors of p^{-1/2}.
  Given all slices but t, slice t has the two-end bridge law. The other
  indicators are measurable outside slice t. So each removal multiplies by
  a factor in [(1-delta)p_{i_t}, (1+delta)p_{i_t}]. The p's cancel, and the
  sum of prod_t A_{i_t i_{t+1}} over strings is Tr A^T. The same holds for
  any nonnegative function of the label path.

- L70-74, (6). HOLDS. Psi_F does not change when F is multiplied by a
  positive scalar. Both 2 log(ratio at T) and log(ratio at 2T) lie in
  [2T log(1-delta), 2T log(1+delta)]. So the difference is at most
  2T log((1+delta)/(1-delta)) = 4T artanh(delta) <= 4.4 T delta <= 8 T delta
  for delta <= 1/2. Next, Psi_A >= 0 because (sum a_k^T)^2 >= sum a_k^{2T}
  for a_k >= 0. Hence Psi_V >= Psi_U - 8 T delta. So a label interaction of
  this class cannot lower the Wilson defect by more than o(1) when
  T delta = o(1). For the gap: d_1 >= u_1, so v_1^2 >= u_1^2 - O(delta).
  With delta = o(a) and u_1 = e^{-aE}, E bounded, the modified first
  energy is at most E + o(1).

Section verdict: (4)-(6) HOLD. Every Wilson eigenvalue survives in the
modified product to error O(delta). The Wilson defect Psi_U enters (6)
additively, and the added term Psi_A is nonnegative.

## 3. The local construction: a low excitation and a massless reading

### The one-plaquette low excitation, (7)-(8)

- L78. HOLDS. Here A = (1/2)[[1+rho, 1-rho],[1-rho, 1+rho]]. Its
  eigenvalues are 1 and rho, its entries are nonnegative, it is PSD, and
  ||A|| = 1. With p = 1/2 the factor in (3) is 1 + rho sigma sigma', which
  is at least 1 - rho > 0. V is a positive operator with a real symmetric
  kernel. This gives link-plane positivity through V >= 0. It gives
  site-plane positivity as a squared modulus of real half-path amplitudes.
  The claim is time reflection only, as stated.

- L80-84, (7). HOLDS. B = 1 gives delta = eps =
  C(1+beta)^{3/2}/M. With M = ceil(exp(log^2(1/a))) and beta = O(log 1/a),
  delta = o(a^k) for every k. Since d_1 >= rho·1, (4) gives
  v_1^2 >= rho^2 - o(a^k), so -log v_1 <= a^2 + o(a^k). Simplicity: the
  kernel is bounded and bounded below by a positive constant. A real top
  eigenfunction can be replaced by its modulus without lowering the
  Rayleigh quotient, with strict gain if the sign changes on positive
  measure. A nonnegative top eigenfunction is positive a.e. by the
  eigenvalue equation. So two orthogonal top eigenfunctions cannot exist,
  v_0 = 1 is simple, and v_1 < 1 is an excited level.

- L86-92, (8). HOLDS. Psi_A(T) = log((1+rho^T)^2/(1+rho^{2T})). For
  T <= t0/a, rho^T >= e^{-a t0} -> 1 uniformly, so the term tends to log 2,
  and O(T delta) -> 0. Since Psi_U >= 0, Psi_V >= log 2 - o(1). The A-B**
  threshold on the window is gamma V(s) <= y0 48^3/(2·96^3) = y0/16
  <= 1/320 < log 2. For A-B*, log Tr(V/||V||)^T >= log(1 + v_1^T) and
  v_1^T -> 1 for T <= t0/a. So A-B* fails as well. B = 1 makes delta
  independent of the spatial size.

- L119, time-correlation test. HOLDS. Marked links at consecutive times
  share a temporal plaquette, so they are not conditionally independent.
  The argument does not need that. In the chain rule, each conditional
  bit probability is an average of probabilities given all other links.
  Each of these lies in (1 ± e_0)/2 by (1). The reference chain has
  transition A, and A^d_{ij} = (1+rho^d ij)/2. The bridge marginal on an
  inner interval has density, relative to the stationary chain, equal to
  (1+rho^{t1} sigma_0 s)(1+rho^{L-t2} s' sigma_L)/(1+rho^L sigma_0 sigma_L).
  With rho = e^{-am} and q = ceil(a^{-1} log^2(1/a)), rho^q -> 0. The
  number l of interior sites is of order a^{-1} log^2(1/a), so
  l e_0 -> 0. Means tend to 0, and the correlation tends to
  rho^{floor(tau/a)} -> e^{-m tau}. The bound is uniform in the exterior,
  so it survives the volume limit.

### The massless local reading, (12)-(15) and (23)

- L145-155, (12) and its reflection positivity. HOLDS. Y_u is a
  gauge-invariant function of the links of one cell interior. A
  reflection plane at a multiple of b is a site plane. It maps cell u to
  cell theta u, and Y_{theta u} = theta Y_u. On a periodic even array the
  far plane pairs cells in the same way. Every crossing factor joins a
  pair (u, theta u). The Gaussian identity writes the product of crossing
  factors as an average, with positive weight, of G_t · theta conj(G_t),
  where G_t = prod e^{i t_u Y_u}. The terms inside each half are a real
  factor times its reflection. With Wilson site positivity
  (Osterwalder-Seiler), this gives positivity for every axis.

- L157. HOLDS. Under the uniform z the Y_u are iid N(0, eta^{-2}). With
  (12) the precision is -Delta_cell + eta^2. The relative density error
  2 Delta_B/(1-Delta_B) follows from the sandwich in L136.

- L166-177, (13). HOLDS. I recomputed the covariance:
  d^6 sum_{u,v} Q^{-1}(u,v) conj f(x_u) g(x_v), with
  Q^{-1}(u,v) = N^{-4} sum_k e^{ik(u-v)}/(eta^2 + 4 sum sin^2(k_mu/2)).
  Put p = k/d and N^4 = L^4/d^4. This gives (13) with denominator
  eta^2/d^2 + 4 d^{-2} sum sin^2(d p_mu/2), and eta^2/d^2 = d^2.

- L179-185, (14). HOLDS. The zero mode is O(L^{-4} d^{-2}) = O(n^{-6}).
  The bound sin(x/2) >= x/pi on [0, pi] gives a denominator of at least
  4|p|^2/pi^2. A max-norm shell has at most C j^3 points, and summing gives
  C(eps^2 + L^{-2}) near 0. Summation by parts gives
  |f_d^(p)| (2 d |p_mu|/pi)^k <= C d^k, so the UV tail decays. Riemann
  sums converge on annuli. Gaussian characteristic functions and moments
  converge. B = N^4 = n^12 is polynomial and s_0 is superpolynomially
  small, so the transfer to the gauge model through (11)-(12) holds.

- L187-194, (15). HOLDS. The p_0 integral of e^{i p_0 t}/(p_0^2 + r^2)
  over 2 pi is e^{-r|t|}/(2r). For theta f and f shifted by tau, the
  time distance is t + t' + tau. With f real this gives the squared
  modulus. The energy image E = |p| has density of order E·|int f|^2 near
  0. So there is no atom at zero and there is weight in every (0, m).
  Cutting at |p| < m/2 gives the lower bound c e^{-tau m/2}, and this
  excludes a gap m. The means are zero, so the vector is orthogonal to the
  vacuum.

- L257-262, (22). HOLDS. Given all raw links except the eight private
  links of u, the other readings are fixed. Only the eight edge factors
  at u vary. Completing the square in
  -eta^2 Y^2/2 - (1/2) sum_{v~u} (Y_v - Y)^2 gives the normal in (22).
  The Wilson density of z_u is in [1-s, 1+s], so the ratio is in
  [(1-s)/(1+s), (1+s)/(1-s)]. Mixing over raw exteriors with the same
  readings keeps the bounds.

- L264-269, (23), one coordinate. HOLDS. The common part is
  min(dnu/dgamma, 1) gamma. Each residual is at most C s gamma pointwise.
  Independent pairing and |y-y'|^p <= 2^{p-1}(|y-h*|^p + |y'-h*|^p) give
  cost C_p s int |y-h*|^p dgamma. This is independent of h*.

- L271, coupling iteration. HOLDS. The heat-bath update keeps both
  equilibrium laws. Coupling Y_u to Z ~ N(m_Y, sigma^2), then setting
  X_u = Z + (m_X - m_Y), gives by Minkowski the bound
  C_p s^{1/p} + alpha max_v ||Y_v - X_v||_p with alpha = 8/(8+eta^2).
  If D >= D_* the bound never increases. After one sweep
  D <= D_* + alpha(D - D_*). Finite starting moments hold at fixed volume
  by the product sandwich.

- L273. HOLDS. d^3 sum |f(x_u)| <= C_f/d, and (8+eta^2) eta^{-2} is of
  order n^4. s^{1/p} is superpolynomially small at fixed p, so the
  smeared L^p error -> 0 in the order "volume first". The identity
  e^{2 pi i M S_u} = e^{2 pi i Phi_eta(Y_u)} passes to joint limits.

Section verdict: the construction HOLDS. The modified theory has a level
with energy at most a + o(a) by (7), a time correlation e^{-m tau} for any
chosen m by L119, and a massless Gaussian local reading (14)-(15) in both
orders of limits by (23).

## 4. Does the conclusion follow?

Claim (L279, L281): giving these readings their own dynamics cannot
supply the missing Wilson thermal estimate (20).

Verdict: it follows, in this precise sense. The logical direction
matters. A bound on Psi_V would imply the Wilson bound, since
Psi_U <= Psi_V + 8 T delta by (6) and Psi_A >= 0. So the modification is a
valid route, but it is no easier. Its defect is the Wilson defect plus a
nonnegative term fixed by A alone. Knowing the gap of A controls only
Psi_A. It gives nothing on Psi_U. If A has a slow mode, Psi_A is near
log 2 and the modified model fails A-B** (8). If A has a large gap,
Psi_A is near 0 and Psi_V is near Psi_U. The same holds for the local 4D
weight (12), by L159: Psi_mod = Psi_W + Psi_Gauss + O(Delta) with
Psi_Gauss >= 0 and divergent.

Scope. The conclusion is proved for two classes: (a) label interactions
of form (3) across one time step, with A PSD and with nonnegative
entries, and T delta = o(1); (b) the weight (12). In fact L136 gives the
additive split for every nonnegative weight W(z) of cell readings:
log Z_mod = log Z_W + log int W dz + O(Delta). So the split extends to
every such W. The sign of the extra term needs a positive transfer for W
(it holds for every T when all its eigenvalues are nonnegative). The file
does not claim more than these classes, and the RESULT wording ("show
why") fits. The thermal estimate (20) for the actual Wilson action stays
open. The file says so at L228-233 and L279.

## 5. Everything else

- L103-113, statement of (10). HOLDS (proof below).

- L115, proof of (10). HOLDS. Put phi(s) = D(s,w) F(x(s,w)). Then
  |dx/ds| = 1/r and int |r'| ds = 2. The derivative terms r h·dx/ds and
  r dF/ds cost at most |h| ||F|| + L_F. With e^{|h|}/Z <= C(1+beta)^{3/2}
  this gives TV(phi) <= C(1+beta)^{5/2} H_F. phi vanishes at s = ±1, so
  extension by zero adds no jump. For an interval I, the shifted Riemann
  sum gives |int phi 1_I(Ms mod 1) ds - |I| int phi| <= |I| TV(phi)/M.
  Then telescope prod N_k - 1 = sum_k N_{<k}(N_k - 1). Each marked link
  lies in no other reading's plaquette, including readings at other times,
  so N_{<k} is measurable given the other links. The bound
  E N_{<k} <= (1+e_0)^{k-1} then gives (10). Coupling of marked links at
  adjacent times through temporal plaquettes only enters h, and
  |h| <= 6 beta still holds.

- L117. HOLDS. Applying (10) with F = 1 gives P(path)/p in
  [(1-e_0)^P, (1+e_0)^P]. The quotient of the two errors gives the stated
  bound on conditional expectations. Under (3) the density relative to
  Wilson depends only on labels, so the conditional laws given a label
  path agree. A product of normalized SU(2) traces is bounded by 1. Its
  Lipschitz constant is at most the number of uses of the link, by
  telescoping a unitary product. The sign field has Lipschitz constant of
  order M, so it lies outside the class.

- L136-141. HOLDS. The normalizer int P(dD) int g_D W dz lies in
  (1 ± Delta) int W. Dividing gives the sandwich with no factor
  1/int W. Moving each of the 8B private links to its bin representative
  costs at most 8 B h L_F. With h = e^{-(log n)^{3/2}},
  M = e^{(log n)^2} and beta = O(log n), s_0 is at most
  C e^{24 (log n)^{3/2} + O(log n) - 2 (log n)^2}, which is
  superpolynomially small.

- L159-164. HOLDS. Z_mod/Z_W = E_W W lies in (1 ± Delta) int W dz, and
  int W dz is the Gaussian ratio. The per-cell factors eta/sqrt(2 pi)
  cancel on doubling. The log errors are at most 2 Delta each, so the
  total is at most 6 max(Delta_B, Delta_2B). The time determinant
  e^{T omega}(1-e^{-T omega})^2 gives the momentum term
  log((1+e^{-T omega})/(1-e^{-T omega})) >= 0. At zero momentum,
  T omega ~ T d^2 = (dT) d -> 0, so the term diverges.

- L210. HOLDS. Under the product reference, d^4 sum f Y_u has covariance
  d^8 eta^{-2} sum conj(f) g = d^4 sum conj(f) g -> int conj(f) g. The
  characteristic functions transfer by (11) on the cells in the support.
  Precision: for two different tests f and f_tau, the "separated
  reflected covariance" uses the two-function form of (11) (G_1 on the
  positive cells, G_2 on the negative cells, with reference integral
  int G_1 · int G_2 = 0). This is not (17) as written, but it is the same
  one-line argument. The moment factor int |G| is of order d^{-3},
  polynomial, so the bound -> 0.

- L212-219, (18). HOLDS. Replacing private links of p costs at most
  4 beta h. The replaced X is D-measurable and bounded by 2 beta. Bayes
  and (11) put the density of D given z, relative to the law of D, in
  [(1-Delta)/(1+Delta), (1+Delta)/(1-Delta)]. Var_W X >= c follows from
  row 1317's unwrapped variance (from its (6)), conditional on all links
  off the slice of p.

- L221-226, (19). HOLDS. inf_g E|X - g|^2 = Var X - Var E[X|z], and
  Var E[X|z] <= ||E[X|z] - EX||_inf^2 = o(1) for beta = O(log n).

- L239-249, statement of (21). HOLDS (proof below).

- L251, proof of (21). HOLDS. The restricted polynomial space is
  SO(4)-invariant, so its reproducing kernel is constant on the diagonal.
  It equals the dimension, at most binom(D+4,4). On a great circle q is a
  trigonometric polynomial of degree at most D. So
  sup|q'| <= D(D+1) sup|q|, and the Lipschitz constant of |q|^2 is at most
  2D(D+1) sup|q|^2. The one-link law has density at least e^{-2|h|} >=
  e^{-12 beta} relative to Haar. This converts Haar L^2 into conditional
  L^2 and gives zeta. Each removal multiplies by (1 ± zeta), since
  |F|^2 stays a polynomial of degree at most D in each remaining link.

- L253. HOLDS. Numerator and denominator are sandwiched separately. If
  -eps Q <= Q' - Q <= eps Q on a Hermitian form, Cauchy-Schwarz gives the
  inner-product bound by polarization.

- L275. HOLDS. Fix the raw exterior. The incident factors of (12) are a
  positive integrable function of the k interior readings. The
  four-pair proof of (11) holds at a fixed exterior. The sandwich of L136
  then gives the conditional comparison, for any exterior.

- GUIDE and OPEN blocks (L3, L5, L9, L11, L13, L15, L17, L123, L228-233,
  L237, L279). Accurate. Row 1175, (29), adds independent signs and keeps
  every Wilson path marginal. Row 1192, (44)-(50), uses the single weight
  W_y = w_b + y w_B. Row 1192, (6)-(7), is the half-weighted polynomial
  subspace. Row 1317, (5), (6), (8), (11) and (16), are used as cited.
  (20) is A-B** of row 1218, with gamma = y0/(2(96T)^3). Its quantifiers
  match row 1218: for all p >= p0 and N >= N0(p) there is T0 with
  3 <= T0 <= t0/a. Precision for L233: Theorem F also needs hypothesis
  (W). The file's phrase "the matching continuum construction" covers
  this.

## Does any main step only restate an earlier row?

No main step is only a restatement. Details:
- (4) extends row 1317, (8), from a rank-one A to any PSD A with
  nonnegative entries. It uses the same XX*/X*X method and pointwise
  kernel sandwich. The file says so (L60).
- (5) is a simpler, one-slice-at-a-time version of row 1317's all-period
  argument. The new part is the factor Tr A^T.
- (6) has the same derivation and constant 8 T delta as row 1317, (11).
  The new content is the additive term Psi_A >= 0.
- L159-164 repeats row 1317's free-field determinant. The file cites it.
  The new step is the additive coupling to Wilson through (11).
- (11) reuses row 1317's high-frequency Haar bound, as cited. The cell
  reading, the bins and the four-pair product are new.
- (9) uses the spectral inversion of row 1192, (7). Its equidistribution
  input (1)-(2) is new. It differs from row 1315, (8), which bounds rare
  events by marking.
- (18)-(19) use row 1317's unwrapped variance as an input. The
  predictor bound is new.

## Summary

37 PROVED blocks: 37 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL. Precisions
only: L35 ("even cube" must mean all sides even when B > 1), L208 ((17)
needs the centring of (16)), L210 (two-test version of (11), not (17)
itself), L233 (Theorem F also needs (W)).

RESULT: 37 of 37 PROVED statements of row 1319 HOLD, 0 need correction, 0 FAIL; main finding: for Wilson, (9) and (17) remove the rapidly oscillating plaquette and cell readings from low-energy matrix elements and reflected norms uniformly in volume, and for any label interaction of form (3) the modified defect is Psi_U + Psi_A + O(T delta) with Psi_A >= 0 (6), while the local weight (12) adds a divergent Gaussian defect and a massless reading (14)-(15); so these modifications are valid but no easier routes, and they leave the Wilson thermal bound (20) and the mass gap OPEN.
