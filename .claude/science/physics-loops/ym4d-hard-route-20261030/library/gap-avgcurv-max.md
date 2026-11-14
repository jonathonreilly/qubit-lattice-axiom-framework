lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T01:57Z

# gap-avgcurv-max (row 968): averaged curvature against (LSI-J-seed)

Author: Claude Fable 5.2 (max), Mac mini worker, pinned at commit 4a2be4ba1. Started 2026-11-14T13:57Z.
Research-stage working state. Nothing here is a public claim. No statement below rests on a run; runs are labelled GUIDE.

## 0. Plan (at most eight steps; one step per response; each result is appended before the next step)

1. **Inputs and duplicate check.** Read rows 941, 947, 957, 958, 960 and `library/prior/gap-lit-bridge-lsi.md`.
   Grep `library/open-core.md` and the FINISH rows (rule 0a). Restate (LSI-J-seed) exactly, with the box and constants.
2. **Sources.** Bauerschmidt-Bodineau-Dagallier 2024 (Polchinski flow, Theorem 3.6), Chen-Eldan localization schemes.
   For each: the exact hypothesis, and whether it is an average or a supremum for J.
3. **Fact tests of the candidate criteria.** Compact U(1) Coulomb phase, frozen Q_8 / 2T, SMALL-BOX, K7, FT-FK.
4. **Attack 1.** Integrated or averaged Bakry-Emery criterion applied to J.
5. **Attack 2.** Ricci curvature of SU(2) against the averaged negative part of the Wilson Hessian
   (exponential-family form of log Omega, Brownian-bridge structure of Theorem BR).
6. **Attack 3.** Splitting: the large negative eigenvalues on a set of small J-measure (RARE-P).
7. **If not closed.** The smallest unproved averaged-curvature inequality and one GUIDE test that could refute it.
8. **Status table and RESULT line.**

Status log (UTC times read from `date -u`):

- 13:57 file created; reading inputs.
- 14:10 inputs read: FINISH rows 941, 947, 954, 957, 958, 960, 968; `gap-fc-max.md` L39-282, L487-586; `gap-lsivac-max.md` L84-222;
  `gap-ps-disint-max.md` L46-95, L163-180, L371-486; check 958 finding 5; `prior/gap-lit-bridge-lsi.md` in full;
  `prior/gap-fullread-2.md` Section 3 (BBD Theorem 3.6 digest). Duplicate check done (Section 1.3).

## 1. Inputs, target, duplicate check (READ; no new claim)

**1.1 Objects (rows 941, 947, 957; quoted in short).** B a periodic spatial box, L = 3|B| links, M = (S^3)^L in R^N,
N = 4L. V(x) = -beta sum_p (1/2) tr x_p. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2) (temporal gauge). Omega its top
eigenfunction, nu = Omega^2 dx, m(dw) = e^(-V(w)/2) Omega(w) dw. Lambda(theta) = log integral of e^(<theta, w>) m(dw) on R^N,
pi_theta(dw) = e^(<theta, w> - Lambda(theta)) m(dw); the one-step law is pi_(beta x); Hess Lambda(theta) = Cov_(pi_theta)(w)
(row 941 (A2)). J(dx, dw) = m(dx) e^(beta <x, w>) m(dw)/Z is the two-slice vacuum law. Elitzur (row 941 (A5)):
Cov_m(w) = Id/4. The bridge marginal (row 947 (B1)-(B4)): nu_s = law of y = (1 - lam) x + lam w + (lam (1 - lam)/beta)^(1/2) xi,
lam = beta s, s' = 1/beta - s, with density h_s h_(s')/Z on R^N, h_s = g_s * m.

**1.2 Target.** (LSI-J)_(alpha_J): Ent_J(Phi^2) <= (2/alpha_J) E_J[|grad_x Phi|^2 + |grad_w Phi|^2] for gauge-invariant Phi.
(LSI-J-seed)_a: alpha_J >= 2 beta K_a on one box, K_a = (C_beta + 3 log a)/(a - 2). Row 960 (unchecked): on the box
(a; (4a)^3), C_beta = 12.51 at beta 2.3 and 12.63 at 2.6, so K_30 = 0.811, K_40 = 0.621, K_60 = 0.427. Row 954
(Lemma GAP-R, conditional): the route needs m_G >= K_a. Theorem BR and Corollary BR-J (row 947; HOLD by check 949)
turn (LSI-J-seed)_a, or the weaker (LSI-br-seed)_a: (1/2) integral over (0, 1/beta) of alpha_s ds >= K_a (alpha_s the
gauge-invariant log-Sobolev constant of nu_s), into (HC-vac)_(K_a) and the seed. Row 957 (T1): any bound with
b alpha_J(b)/log b -> infinity along box sides b gives the seed for some a.

**1.3 Duplicate check (rule 0a).** `grep -n -i -E "LSI-J|polchinski|stochastic locali|localization scheme|chen-eldan|eldan|averaged curv|integrated bakry|DEF-ABS|entropic stab|bakry"`
on `library/open-core.md`, `library/l17c.md`, `library/open-registry.md`: no hit. FINISH rows: Polchinski 689, 690, 813,
915 (reading rows; 689: Bauerschmidt-Bodineau Theorem 1.2 "needs a lower bound at every scale ... no gauge
application"), 719 (BBD Theorem 3.6 read; digest `prior/gap-fullread-2.md` Section 3); Eldan 689, 690, 787 (reading);
"averaged curvature" 958 (the check that left the route open) and 968 (this row); (DEF-ABS) 957, 958. No row attacks
an averaged-curvature or Polchinski-flow criterion for J. Row 941 has the one-scale forms (Theorem MID, (COV)_kbar,
three ceilings at beta 1, 2, 3/2). I proceed, and I do not re-attack (SG-step), (SC), (FC), (MAC).

**1.4 What check 958 left open, in its words (finding 5).** Sampling the top eigenvalue of Hess H tests only the
pointwise tensor criterion. An averaged inequality may keep the term E[f |Hess log f|^2], which can compensate a
negative tensor term. So "no averaged form exists" was not established by row 957.

**Credit.** Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the transfer frame
and temporal-gauge setting of the account. Rows 941, 947 (Claude Fable 5.2): exponential family, Theorem BR.
Bauerschmidt, Bodineau, Dagallier; Chen, Eldan; Piazza, Shen: named where used below.
- 14:15 Sections 2 and 3 written (sources; the flow of the bridge marginal; Theorem POL-BR; zero-field values).

## 2. Sources: what each criterion needs, and whether the need is an average or a supremum

Read from open copies fetched to `/tmp/gap-avgcurv-968/` (not committed): Bauerschmidt, Bodineau, Dagallier,
arXiv:2307.07619 (BBD), Section 3.3 and the proof of Theorem 3.6 (printed pp. 19-21); Chen, Eldan, arXiv:2203.04163
(CE), Claim 22, Proposition 39, Lemma 40.

**2.1 BBD Theorem 3.6 (quoted in short).** nu_0 = e^(-V_0) x Gaussian(C_infinity), with a decomposition
C_t = integral of C-dot. V_t = -log(Gaussian(C_t) * e^(-V_0)), nu_t = e^(-V_t) x Gaussian(C_infinity - C_t). Hypothesis (3.32):
"for all phi in X, t > 0: C-dot_t Hess V_t(phi) C-dot_t - (1/2) C-ddot_t >= lambda-dot_t C-dot_t", with lambda-dot_t real, "allowed
to be negative". Conclusion (3.33)-(3.34): Ent_(nu_0)(F) <= (2/gamma) E_(nu_0)(grad F^(1/2))^2, 1/gamma = integral of e^(-2 lambda_t) dt.
- **Average or supremum.** An average over the scale t only. At each scale it is a SUPREMUM over the field phi.
- **Where the supremum is used (their proof, (3.43)-(3.48)).** Ent_(nu_0)(F) = 2 integral of E_(nu_t)(grad F_t^(1/2))^2 dt, F_t = P_(0,t) F
  ((3.44)). Lemma 3.10: (L_t - d/dt)(grad F_t^(1/2))^2 = 2 Hess V_t(grad F_t^(1/2), C-dot grad F_t^(1/2)) + (1/4) F_t |Hess log F_t|^2. The
  hypothesis is applied pointwise at the vector grad F_t^(1/2)(phi), and the last term (non-negative) is dropped.
- **Two consequences I use (READ from that proof; not rebuilt).** (a) If a compact group acts on X by orthogonal maps
  that preserve V_0 and C_t, then for invariant F the hypothesis is needed only on vectors orthogonal to the orbit
  of phi ("horizontal at phi"), because F_t is invariant. (b) Taking E_(nu_t) of Lemma 3.10 (C-dot = Id) gives an identity
  with no supremum, for I(t) := E_(nu_t)(grad F_t^(1/2))^2:
     I'(t) = -2 E_(nu_t)[ Hess V_t(grad F_t^(1/2), grad F_t^(1/2)) ] - (1/4) E_(nu_t)[ F_t |Hess log F_t|^2 ].      (ID-ent)
  The variance form (same computation with F in place of F^(1/2)): Var_(nu_0)(F) = integral of I_2(t) dt, I_2 = E_(nu_t)|grad F_t|^2,
     I_2'(t) = -2 E_(nu_t)[ Hess V_t(grad F_t, grad F_t) ] - E_(nu_t)|Hess F_t|^2.                               (ID-var)
- **What it needs for J.** J lives on M x M and is not of the form (3.10). The bridge marginals nu_s on R^N are of
  that form (Section 3), and Theorem BR reads only them. So the criterion applies to nu_s and J is bypassed.

**2.2 Chen-Eldan (quoted in short).** A localization process nu_t (a measure-valued martingale started at nu).
Proposition 39: "suppose that, almost surely for all t in [0, T], nu_t is alpha_t-entropically stable with respect to
psi(x, y) = (1/2)|C_t(x - y)|^2. Then E[Ent_(nu_T)[f]] >= e^(-integral of alpha_t) Ent_nu[f]." Lemma 40: entropic stability with
alpha = ||C A C|| holds if "for every v in R^n one has Cov(T_v nu) <= A", T_v the linear tilt. Variance (Claim 22 and its
continuous form): d Var_(nu_t)(phi) = -|C_t v_t|^2 dt + martingale, v_t = integral of (x - b(nu_t)) phi d nu_t, so
|C_t v_t|^2 <= ||C_t Cov(nu_t) C_t|| Var_(nu_t)(phi).
- **Average or supremum.** Entropy: a SUPREMUM over every tilt of every measure on the path. Variance: an almost-sure
  bound on ||Cov(nu_t)|| along the path. For the linear-tilt process nu_t = T_(h_t) nu with h_t = t X + B_t the path has
  full support, so "almost surely" is again a supremum over all tilts h in R^N. The average is over t only.
- **The typical-path form (RECALLED from Eldan's work on the KLS conjecture; not in CE in this form; not rebuilt).**
  For a bounded test function and a stopping time at the first exit of ||Cov(nu_t)|| from a bound, the same
  identity gives Var_nu(f) <= e^(alpha T) (E Var_(nu_T)(f) + osc(f)^2 P(exit before T)). This needs the covariance bound
  only with high probability. Its output is a weak Poincare inequality (a defect osc(f)^2 x probability), not a gap.
- **What it needs for J.** The linear-tilt localization of the one-step law pi_(beta x) is the exponential family of row
  941: nu_t = pi_(theta_t), d theta_t = grad Lambda(theta_t) dt + dB_t. The covariance on the path is Hess Lambda(theta) = Cov_(pi_theta)(w).
  The supremum form is (COV)_kbar of row 941 (A4), with kbar >= 1/4 (Elitzur).

**2.3 Verdict on input (1) of the row.** Both published criteria average over the scale and take a supremum over
the field or tilt. Neither is an average over the measure. The identities (ID-ent), (ID-var) are the averaged
statements behind them; they hold for every F and keep a Hessian term. Section 5 shows what an average over the
measure can and cannot mean.

## 3. The Polchinski flow of the bridge marginal is the reduction of one time-like coupling

Fix s in (0, 1/beta), s' = 1/beta - s, lam = beta s, and c := s s'/(s + s') = lam (1 - lam)/beta, so 1/c = 1/s + 1/s'.

**3.1 Proposition FLOW (PROVED, hand).** Put q~ := x/s + w/s' for (x, w) in M x M, and for 0 <= b <= beta, phi in R^N:
  J_(b,phi)(dx, dw) := e^(b <x, w> + <phi, q~>) m(dx) m(dw) / Z_b(phi).
(a) nu_s(dy) = Gaussian(c Id)(dy) e^(-V_0(y))/const with V_0(y) = -Lambda(y/s) - Lambda(y/s'). V_0 is concave.
(b) For 0 <= t <= c and C_t = t Id: V_t(phi) = -log Z_(b_t)(phi) - const_t, with b_t := t/(s s'). So b_t runs from 0 to beta.
(c) grad V_t(phi) = -E_(J_(b_t,phi)) q~ and Hess V_t(phi) = -Cov_(J_(b_t,phi))(q~). Every V_t is concave.
(d) nu_t is the law of (1 - t/c) q + (c - t)^(1/2) xi, with q = (1 - lam) x + lam w, (x, w) distributed by J, xi standard Gaussian,
    independent. Given this variable equal to phi, the law of (x, w) is J_(b_t,phi).
Proof. (a) On M, |x|^2 = L, so h_s(y) = (2 pi s)^(-N/2) e^(-L/(2s)) e^(-|y|^2/(2s)) e^(Lambda(y/s)); multiply the two factors (row 947 (B4)).
Hess V_0 = -Cov_(pi_(y/s))/s^2 - Cov_(pi_(y/s'))/s'^2 <= 0. (b) e^(-V_0(zeta)) = integral of e^(<zeta, q~>) m(dx) m(dw). For zeta Gaussian
with mean phi and covariance t Id: E e^(<zeta, q~>) = e^(<phi, q~> + (t/2)|q~|^2), and |q~|^2 = L/s^2 + L/s'^2 + 2 <x, w>/(s s') on M x M.
(c) Differentiate log Z_b(phi) in phi. (d) nu_t has density proportional to e^(-V_t(phi)) e^(-|phi|^2/(2(c - t))). Insert (b) and
complete the square: it is the mixture over (x, w), with weight e^((c/2)|q~|^2) m(dx) m(dw), of Gaussians with mean (c - t) q~ and
covariance (c - t) Id. The weight is proportional to e^(beta <x, w>) (since c/(s s') = beta), that is to J, and c q~ = q. The
posterior follows from the same display. QED
Reading. J_(b,phi) is the law of two consecutive slices of the vacuum chain when the ONE layer of time-like
plaquettes between them has coupling b in place of beta, and the two slices feel the linear fields phi/s and phi/s'.
Each factor m keeps the full coupling beta in its own half-space. So the multiscale curvature of the bridge
marginal is a link covariance of the two-slice system, along the flow that switches the middle layer on.
The fields phi/s, phi/s' are not gauge invariant: a linear term in the links is a gauge-fixing or Higgs-type term.

**3.2 Lemma Z (zero field; PROVED, Elitzur's argument of row 941 (A5) applied to the pair).** On a cubic periodic
box of side at least 3, for every b: Cov_(J_(b,0))(q~) = k0_(s,b) Id_N with
  k0_(s,b) = (1/4)(1/s^2 + 1/s'^2 + 2 tau_b/(s s')),   tau_b := E_(J_(b,0)) <x_l, w_l> in [0, 1],
so k0_(s,b) <= 1/(4 c^2). At phi = 0 every vector is horizontal.
Proof. J_(b,0) is invariant under gauge transformations acting on x and w at once. Two distinct links do not have
the same end sites, so the central element -1 at one site kills E[x_l (x) x_l'], E[x_l (x) w_l'], E[w_l (x) w_l'] for l != l'.
For l = l' the three matrices commute with q -> g q h^(-1) (independent g, h at the two ends), that is with SO(4), so
each is a multiple of Id_4: 1/4, tau_b/4, 1/4. E q~ = 0. tau_b is the same for all links by the lattice symmetries
of the cube. tau_b >= 0: L tau_b = (d/db) log Z_b(0) is non-decreasing in b and vanishes at b = 0. QED

**3.3 Theorem POL-BR (CONDITIONAL on BBD Theorem 3.6 with reading (a) of 2.1, cited, not rebuilt; and on Theorem BR,
row 947, checked by row 949).** For s in (0, 1/beta) and 0 <= t <= c_s let kbar_(s,t) be a piecewise continuous bound with
  (TILT-COV-sup):  Var_(J_(b_t,phi))(<z, q~>) <= kbar_(s,t) |z|^2  for every phi in R^N and every z orthogonal to the gauge orbit of phi.
Then nu_s has the gauge-invariant log-Sobolev inequality (LSI-br)_s with
  1/alpha_s <= integral over [0, c_s] of exp(2 integral over [0, t] of kbar_(s,u) du) dt,
and (HC-vac)_alpha holds with alpha = (1/2) integral over (0, 1/beta) of alpha_s ds.
Proof. By 3.1, nu_s has the form (3.10) of BBD with C_t = t Id on [0, c] (their Remark 3.8 allows the
reparametrisation of [0, c) to [0, infinity)); C-dot = Id, C-ddot = 0, and (3.32) on horizontal vectors holds with
lambda-dot_t = -kbar_(s,t). The continuity condition (3.31) holds: nu_t tends to the unit mass at 0 and P_(0,t) F(0) to E_(nu_s) F
(all functions here are smooth with bounded derivatives). The gauge group acts on R^N by orthogonal maps that
preserve m, hence V_0. Then Theorem BR. QED
Checks by hand. (i) One flat mode: on the line the factor e^(-x^2/(2s)) is not constant, so m is replaced by
e^(-x^2/(2s)) m there. With m of precision kappa: Hess V_t = -k/(1 - k t), k = (1/s^2)/(kappa + 1/s) + (1/s'^2)/(kappa + 1/s'), and
the integral is c/(1 - k c). So alpha_s = 1/c - k = kappa/(1 + kappa s) + kappa/(1 + kappa s'), the exact precision of nu_s (row 947, 5.4).
The criterion is exact in every Gaussian mode, as Theorem BR is. (ii) Units: for N(0, 1/A), alpha = A.

**3.4 What the zero field gives (PROVED arithmetic; it is NOT a bound for SU(2)).** If kbar_(s,t) could be taken
equal to its zero-field value k0 <= 1/(4 c^2), then alpha_s >= alpha0_s := 1/(2 c^2 (e^(1/(2c)) - 1)). At the mid-slice
(c = 1/(4 beta)): alpha0 = 8 beta^2/(e^(2 beta) - 1) = 0.43 at beta 2.3 and 0.30 at beta 2.6 (the Gaussian scale there is 4 beta).
With lam = 0.1, 0.2, 0.3, 0.4, 0.5 at beta 2.3: alpha0_s = 0.001, 0.078, 0.25, 0.38, 0.43, so
(1/2) integral of alpha0_s ds is about 0.04 (trapezoid by hand). K_a <= 0.04 on the box (a; (4a)^3) holds from a of about 830.
Two readings.
- The three one-scale ceilings of row 941 (beta 1, 2, 3/2) all come from the zero-field point. In the form
  integrated over scale that point costs a finite factor at every beta. So the integrated form is not capped by
  those ceilings. This is the precise sense in which an averaged form escapes them (PROVED for the zero-field
  point only).
- The zero-field value is the same for SU(2), compact U(1) (with 1/2 in place of 1/4) and the frozen groups. So
  the zero field cannot be the worst tilt for the rivals (Section 4), and the whole content of (TILT-COV-sup)
  is in the non-zero tilts.
- 14:18 Section 4 written (fact tests of the criterion of Section 3).

## 4. Fact tests of (TILT-COV-sup), before any proof attempt

Section 3 is exact and blind to the group and to V. So its hypothesis must fail for every rival, and it must
contain the box size. Each test below is a necessary condition. None is evidence for SU(2).

**4.1 Lemma NEC (PROVED given Theorem POL-BR and Proposition HC of row 931).** Let k* be the supremum of kbar_(s,t) over
s in [1/(4 beta), 3/(4 beta)] and t in [0, c_s]. Then E_1(B) >= e^(-k*/(2 beta)). So every model of the class obeys
  k* >= 2 beta log(1/E_1(B)).
Proof. On that range c_s lies in [3/(16 beta), 1/(4 beta)], so alpha_s >= (c_s e^(2 k* c_s))^(-1) >= 4 beta e^(-k*/(2 beta)). The range has length
1/(2 beta), so alpha >= e^(-k*/(2 beta)), and Proposition HC gives E_1 >= alpha. QED
Reading. A box-uniform bound on the tilted covariance gives a box-uniform gap. Where the gap closes with the box,
the tilted covariance must grow with the box, at least like 2 beta log(1/E_1).

**4.2 FT-U1.** (a) FP, the Gaussian mode model of row 929 (PROVED). The criterion is exact in every mode (3.3, check
(i)), so its output is the true rate of FP. On the box (a; (4a)^3) the lowest mode has omega_min = 2 asinh(sin(pi/(4a)))
< 1.58/a, against K_a > 12.5/a: FP fails the seed rate for every a, by a factor above 8 (above 59 on the slab, row 947
4.3). In the language of the flow: k = 1/c - (exact precision), and Var = k/(1 - k t) reaches 1/(precision) at t = c.
The soft modes are the photon modes, as the row asks. With the toron level of full FP (check 938: 1/(2 beta b)),
Lemma NEC gives k* >= 2 beta log(2 beta b).
(b) Compact Wilson U(1) in its Coulomb phase (ARGUED from Lemma NEC; the absence of a gap there is RECALLED, not
proved here). Section 3 holds for it word for word (M = (S^1)^L in R^(2L), zero-field value with 1/2 in place of 1/4).
The zero-field value is box-independent, so the supremum over non-zero tilts must grow with the box. The Ricci
curvature does not appear in Section 3 at all: the flat ambient space carries the argument. So "Ric = 0" is not
the place where U(1) fails. It fails in the tilted link covariance.
Verdict: the criterion passes FT-U1 only in the sense that it proves nothing for U(1). No step of Sections 2-3
separates SU(2) from U(1).

**4.3 FT-FROZEN (Q_8, 2T).** The proof of Theorem BR uses m as a finite measure on a closed subset of the product of
unit spheres, the kernel e^(beta <x, w>), and Gaussian convolutions in R^N. It does not use that M is a manifold
(ARGUED: I re-read steps (i)-(v) of row 947 5.2 for this; not checked by another reader). So for a finite group
the ambient inequality (LSI-br)_s is defined, Proposition FLOW and Lemma Z hold (the group contains -1 and
g q h^(-1) acts irreducibly on R^4 for Q_8 and 2T), and the test is no longer void. On a fixed box E_1 tends to 0 as
beta grows (row 941 FT-FROZEN, from check 938). By Lemma NEC, k*/(2 beta) tends to infinity there. The zero-field
value stays below (4/9)(4 beta)^2 on the range of 4.1. So for the frozen groups the failure sits in non-zero
tilts, as for U(1). Passes (nothing is claimed for them).

**4.4 SMALL-BOX (conditional on the premise of row 941: for SU(2) on a fixed lattice box E_1 tends to 0 as beta
grows).** Lemma NEC: k* >= 2 beta log(1/E_1) on that box. So no bound on kbar that is uniform in beta at fixed lattice
size exists. A proof of (TILT-COV-sup) must use the box size against the confinement scale. The box enters only
through m. Passes.

**4.5 K7.** Section 3 needs the time-like weight e^(beta <x, w>). With an adjoint term in the time-like plaquettes the
kernel is not a Gaussian of the ambient chord and Theorem BR does not apply. With the adjoint term in V only,
Section 3 holds, and at a coupling with no seed at any size Lemma NEC makes k* grow with the box. Passes.

**4.6 FT-FK (row 967).** The flow of Section 3 acts on the kinetic coupling of one layer only, and it is exact for
every rival. By FT-FK such an argument cannot decide anything, and it does not: the magnetic term and the rest
of the lattice enter only through m, in the hypothesis. The named step where SU(2) must differ from U(1) is a
bound on Var_(J_(b,phi))(<z, q~>) at non-zero phi. Check in the kinetic-only model (V = 0, m a product of Haar measures;
ARGUED): J_(b,phi) is a product over links, the covariance is one link's, and the theorem returns a positive
box-independent rate. This is correct there (independent rotor chains have a gap), and it shows the criterion
can only fail through correlations that m carries.

**4.7 The ceilings 1/3, 2/3, 0.775, 4 G_3 (FT-CEIL).** Each caps a one-scale criterion with a threshold
(`gap-status-1113.md` lines 68, 110, 112, 341). Theorem POL-BR has no threshold: any finite kbar gives a positive
alpha, and the loss is the factor exp(2 integral of kbar). So no cited ceiling applies to it (PROVED: there is no
smallness condition in 3.3). The price is the other one: it is a supremum over all linear tilts, and its
failure mode is growth with the box (Lemma NEC), not a critical coupling.

**4.8 Which tilts can be bad (ARGUED; physics reading, no proof weight).** A uniform tilt phi_l = kappa 1 on the
two slices is a fundamental Higgs term of frozen length on a three-dimensional layer, in unitary gauge. The
vector z = (1, ..., 1)/N^(1/2)-type (the real part on every link) is horizontal at such phi. If the layer has a phase
transition in kappa, the variance of the mean link along z grows with the box (like the volume at a first-order
point). So a box-uniform (TILT-COV-sup) says in particular: the Higgs-tilted layer has no transition, at any
kappa, in the confining bulk. For the full four-dimensional SU(2) Higgs model with frozen length a line of
transitions ends near beta 2.7 (RECALLED from lattice studies, not verified; the window 2.3 to 2.6 lies below it).
This family is the first place to test (Section 7).
- 14:24 Section 5 written (Attack 2: where the Ricci curvature sits; what an average over the measure can mean).

## 5. Attack 2: the Ricci curvature of SU(2) against the negative part, in the bridge picture

**5.1 The curvature of nu_s (PROVED; 3.1 (a), (c) at t = 0).** Put Phi := -log(d nu_s/dy). For y, z in R^N:
  K_s(y)(z, z) := Hess Phi(y)(z, z) = |z|^2/c - Var(<z, x> | y)/s^2 - Var(<z, w> | y)/s'^2,
where given y the slices x, w are independent with laws pi_(y/s), pi_(y/s'). The ambient space is flat, so K_s is the
whole Bakry-Emery tensor. No Ricci term appears. The curvature of the group must be found inside the covariances.

**5.2 One free link (m = Haar on S^(n-1); PROVED, hand).** Then Phi is radial, Phi(r) = r^2/(2c) - Lam(r/s) - Lam(r/s'),
Lam' = A (the mean resultant; A = I_2/I_1 for n = 4). The tangential curvature is Phi'(r)/r.
(a) Sign. At the mid-slice Phi'(r)/r = 4 beta (1 - A(2 beta r)/r). Since A(kappa) = kappa/n - O(kappa^3), it is negative near r = 0
exactly when 2 beta/n > 1: beta > 2 for SU(2) (n = 4), beta > 1 for U(1) (n = 2). This is ceiling (ii) of row 941. At
beta 2.3 the negative region is r below about 0.4, of small nu_s-probability; the value at r = 0 is 4 beta (1 - beta/2) = -1.4,
against about +3 at r = 1.
(b) Average. For p > 2 - n: E[ r^(p-1) Phi'(r) ] = (n + p - 2) E[ r^(p-2) ] (integrate by parts against r^(n-1) e^(-Phi) dr). So
  E[ Phi'(r)/r ] = (n - 2) E[ r^(-2) ]   for n >= 3:   the mean tangential curvature is Ric(S^(n-1)) x E|y|^(-2).
For n = 2 the same integral is the boundary term: E[Phi'(r)/r] = 2 pi x (density of y at the origin), which is tiny.
So for one link the Ricci curvature of the group is the average of the ambient tangential curvature over the
radial coordinate of the bridge. It is 2 E|y|^(-2) for SU(2) and essentially 0 for U(1). The negative part of (a) is the
inner side of the shell. The free rotor has a gap for both groups: for U(1) the gap does not come from this
average but from the Hessian term of 5.4 (b).

**5.3 Proposition ANG (fibre form; PROVED, hand).** Write y_l = r_l u_l, r_l = |y_l|. On the fibre of fixed radii, a product
of spheres of radii r_l, the conditional law of the angles has the Bakry-Emery tensor, for v tangent (v_l orthogonal
to y_l):
  BE_ang(y)(v, v) = sum_l [ 2/r_l^2 + (mu^x_l/s + mu^w_l/s')/r_l ] |v_l|^2 - Var(<v, x> | y)/s^2 - Var(<v, w> | y)/s'^2,
with mu^x_l := <u_l, E[x_l | y]>, mu^w_l := <u_l, E[w_l | y]> in [-1, 1]. For U(1) the term 2/r_l^2 is absent.
Proof. A geodesic of the sphere of radius r has acceleration -(|v|^2/r^2) y. So the fibre Hessian of Phi is
K_s(v, v) - sum_l <y_l, grad_l Phi> |v_l|^2/r_l^2, and the Ricci tensor of the fibre is 2|v_l|^2/r_l^2 on each factor. By 5.1,
grad Phi = y/c - E[x | y]/s - E[w | y]/s'. The terms |v|^2/c cancel. QED
Checks. One free link: Var(<v, x> | y) = (A/kappa)|v|^2 with kappa = r/s, and mu^x = A, so the bracket and the variance cancel
and BE_ang = 2/r^2, the round sphere. As s -> 0 (r -> 1) the display is the bridge form of row 941 (A6).
Readings.
- At the zero-field point y -> 0 (all links): mu^x_l = r_l/(4s) + o(r), Var(<v, x> | y) -> |v|^2/4 (Elitzur), so the mean
  term and the variance term cancel to leading order and BE_ang is 2/r_l^2 -> + infinity. The ceiling (ii) of row 941
  (mid-slice log-concavity dies at beta 2) is an artefact of Cartesian coordinates at a point where the fibre
  shrinks. In the fibre form the Ricci curvature of S^3, rescaled to 2/r^2, removes it. For U(1) the same
  computation leaves 0. This is the exact place where Ric = 0 shows for U(1), and it is a one-link effect.
- It does not make the fibre tensor positive (ARGUED, numbers by hand at beta 2.3, mid-slice). Take u_l opposite
  to the direction its staples prefer, at a typical radius: then mu^x_l, mu^w_l are near -0.7, the mean term is
  about -7, the variance term about -6, the Ricci term +2.5. So BE_ang < 0 at a frustrated link. This is the
  flipped link of Lemma SEP (row 957) and of ceiling (i) (row 941) again. It has small probability per link under
  nu_s and a positive density in the volume.
- The directions of 5.2 and of this proposition are local. The seed needs the collective directions at the box
  scale, where the Ricci term 2/r^2 is of order one and has nothing to say.

**5.4 Proposition AVG: what an average over the measure can mean (PROVED given Bochner's identity on R^N and the
slice theorem for compact group actions, both RECALLED).** Let mu = e^(-Phi) dy be nu_s, K = Hess Phi, L = Laplacian - grad Phi . grad.
For 0 <= th <= 1 consider, for all smooth gauge-invariant G with bounded derivatives:
  (AVG)_(th, rho):  E[ K(grad G, grad G) ] + th E|Hess G|^2 >= rho E|grad G|^2.
(a) (AVG)_(0, rho) holds if and only if K >= rho on horizontal vectors at every point of a principal orbit.
(b) (AVG)_(1, rho) holds if and only if the gauge-invariant Poincare constant gam_s of nu_s is at least rho.
(c) The linearisation at t = 0 of the flow criterion of Section 7 is (AVG)_(1/2, 1/c - kap_(s,0)).
Proof. (a) "If" is clear. "Only if": at a principal orbit every horizontal z is the gradient at y_0 of an invariant
smooth function (slice theorem). Multiply by an invariant cut-off supported in a small tube around the orbit;
both sides are continuous and the ratio tends to K(y_0)(z, z)/|z|^2. (b) E(L G)^2 = E|Hess G|^2 + E[K(grad G, grad G)] (Bochner), and
E(L G)^2 >= rho E[G (-L) G] for all G is the statement that -L has no spectrum in (0, rho) on invariant functions (spectral
theorem). (c) Section 7. QED
Reading. This is the answer to check 958's finding 5. With no Hessian term, an average over the measure for all
test functions is the pointwise criterion, which is dead (5.3, and rows 941, 957). With the full Hessian term it
is the Poincare inequality itself, so it is not a reduction. A statement strictly between the two needs th in
(0, 1), or a restricted class of test functions (smoothed by a flow), or both. The flow criterion of Section 3
is of this kind: th = 1/2 at each scale, with the renormalised measures nu_t and potentials V_t.

**5.5 Where attack 2 stops.** The negative part of the curvature is of three kinds. (K1) The inner side of each
link's shell: an artefact, removed by the fibre form, where the Ricci curvature of SU(2) is exactly the absorber
(5.2, 5.3). (K2) Frustrated links: rare under nu_s, with a positive density; absorbing them is the defect inequality
of Section 6. (K3) Collective directions at the box scale: this is the gap itself (5.4 (b)), and the Ricci
curvature does not act there. So the Ricci curvature of SU(2) pays for (K1) only. I found no way to make it pay
for (K2) or (K3).
