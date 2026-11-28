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

Where the steps are: step 1 = Section 1; step 2 = Section 2; step 4 (attack 1, the integrated criterion) = Section 3;
step 3 (fact tests) = Section 4; step 5 = Section 5; step 6 = Section 6; step 7 = Section 7; step 8 = Section 8.

Status log (UTC times read from `date -u`):

- 13:57 file created; reading inputs.
- 14:10 inputs read: FINISH rows 941, 947, 954, 957, 958, 960, 968; `gap-fc-max.md` L39-282, L487-586; `gap-lsivac-max.md` L84-222;
  `gap-ps-disint-max.md` L46-95, L163-180, L371-486; check 958 finding 5; `prior/gap-lit-bridge-lsi.md` in full;
  `prior/gap-fullread-2.md` Section 3 (BBD Theorem 3.6 digest). Duplicate check done (Section 1.3).
- 14:15 Sections 2 and 3 written (sources; the flow of the bridge marginal; Theorem POL-BR; zero-field values).
- 14:18 Section 4 written (fact tests of the criterion of Section 3).
- 14:24 Section 5 written (Attack 2: where the Ricci curvature sits; what an average over the measure can mean).
- 14:26 Sections 6 and 7 written (Attack 3; the smallest unproved inequality; the GUIDE test design, before any run).
- 14:30 7.3 and Section 8 written (test of 7.2 NOT run, with the reason; status table; RESULT). Numeric jobs of the row, all under lock holder
  gap-avgcurv-968, one at a time: the one-link quadrature (14:28:05Z, 2 s), the smoke test of 7.4 (about 14:31Z, 1 min), the batch of 7.4-7.5.
- 14:32 7.4 added: criteria for a run of the test of 7.2 at sides 8 to 24; batch launched in the background under the
  numeric lock (holder gap-avgcurv-968). Sections 7.3, 8 and the RESULT line were written BEFORE this run and say
  "NOT run"; they are corrected in 7.5 and 8 when the batch ends.
- 15:34 batch ended (lock 14:32:32Z to 15:31:57Z, 42 runs, no error output, 72 percent memory free at the start, one
  thread, nice). 7.5 written; 7.3, the table of 8.1, 8.2 and the RESULT line corrected for the run.

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
4.3). In the language of the flow: k = 1/c - (exact precision), and Var = k/(1 - k t) equals k/(c x precision) at t = c, large
for a soft mode. The soft modes are the photon modes, as the row asks. In any model of the class with a level at
1/(2 beta b) (the toron level of full FP, check 938), Lemma NEC gives k* >= 2 beta log(2 beta b).
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

## 5. Attack 2: the Ricci curvature of SU(2) against the negative part, in the bridge picture

**5.1 The curvature of nu_s (PROVED; 3.1 (a), (c) at t = 0).** Put Phi := -log(d nu_s/dy). For y, z in R^N:
  K_s(y)(z, z) := Hess Phi(y)(z, z) = |z|^2/c - Var(<z, x> | y)/s^2 - Var(<z, w> | y)/s'^2,
where given y the slices x, w are independent with laws pi_(y/s), pi_(y/s'). The ambient space is flat, so K_s is the
whole Bakry-Emery tensor. No Ricci term appears. The curvature of the group must be found inside the covariances.

**5.2 One free link (m = Haar on S^(n-1); PROVED, hand).** Then Phi is radial, Phi(r) = r^2/(2c) - Lam(r/s) - Lam(r/s'),
Lam' = A (the mean resultant; A = I_2/I_1 for n = 4). The tangential curvature is Phi'(r)/r.
(a) Sign. At the mid-slice Phi'(r)/r = 4 beta (1 - A(2 beta r)/r). Since A(kappa) = kappa/n - O(kappa^3), it is negative near r = 0
exactly when 2 beta/n > 1: beta > 2 for SU(2) (n = 4), beta > 1 for U(1) (n = 2). This is ceiling (ii) of row 941. At
beta 2.3 the negative region is r < 0.43, of nu_s-probability 0.02; the value at r = 0 is 4 beta (1 - beta/2) = -1.38, against
+2.8 at r = 1. At beta 2.6: r < 0.56, probability 0.05, values -3.1 and +2.8. (Numbers: GUIDE quadrature for one free
link, `/tmp/gap-avgcurv-968/scripts/onelink.py`, 2 s under the numeric lock at 14:28Z, not committed; the sign
statement is PROVED.)
(b) Average. For p > 2 - n: E[ r^(p-1) Phi'(r) ] = (n + p - 2) E[ r^(p-2) ] (integrate by parts against r^(n-1) e^(-Phi) dr). So
  E[ Phi'(r)/r ] = (n - 2) E[ r^(-2) ]   for n >= 3:   the mean tangential curvature is Ric(S^(n-1)) x E|y|^(-2).
For n = 2 the same integral is the boundary term: E[Phi'(r)/r] = 2 pi x (density of y at the origin), which is tiny.
(GUIDE check of the identity at n = 4: both sides 2.770 at beta 2.3 and 2.731 at beta 2.6.)
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
and BE_ang = 2/r^2, the round sphere. The display is the bridge analogue of row 941 (A6); I did not verify the
limit s -> 0 term by term.
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

## 6. Attack 3: the negative part on a set of small measure

**6.1 Proposition SCHR (scalar domination; PROVED given Bochner's identity, RECALLED).** Let k_s(y) be the lowest
eigenvalue of K_s(y) on horizontal vectors. Then the gauge-invariant Poincare constant of nu_s obeys
  gam_s >= sig_s := inf over invariant Lipschitz h of ( E|grad h|^2 + E[k_s h^2] ) / E[h^2].
Proof. For invariant G put om = grad G and h = |om|. Pointwise |grad h| <= |Hess G| (Cauchy-Schwarz; Kato's inequality), and
K_s(om, om) >= k_s h^2. So E(L G)^2 = E|Hess G|^2 + E K_s(om, om) >= sig_s E|grad G|^2, and 5.4 (b) applies. QED
This is an averaged-curvature criterion in the exact sense: the curvature enters as a potential of a scalar
Schrodinger form, and a negative well of small measure costs nothing if leaving it is cheap.

**6.2 It dies by the volume (PROVED given one premise).** Premise (DENS): there are D > 0 and p > 0 such that each link
is frustrated (5.3: K_s <= -D in a direction on that link) with nu_s-probability at least p, with enough
independence that some link of the box is frustrated with probability tending to 1 as the box grows. Then
k_s <= -D with probability tending to 1, and the trial function h = 1 gives sig_s <= E k_s < 0 on large boxes. So
Proposition SCHR is empty on the seed box. The scalar h forgets the direction: one bad link anywhere lowers k_s
for the whole lattice. (DENS) is not proved here; the hand numbers of 5.3 suggest p of the order of one per cent.

**6.3 The direction-resolved form and its three needs (PROVED implication).** Suppose
  (LOC-COV): K_s(y) >= diag_l( k_l(y) ) as forms on horizontal vectors, with k_l >= rho off a set Bad_l and k_l >= -D on it;
  (CAP)_l: E[h^2 1_(Bad_l)] <= A E|grad h|^2 + del E[h^2] for all invariant Lipschitz h, with (rho + D) A <= 1.
Then gam_s >= rho - (rho + D) del.
Proof. With h_l = |grad_l G|: E|Hess G|^2 >= sum_l E|grad h_l|^2 and E K_s(om, om) >= sum_l E[k_l h_l^2] >= sum_l ( rho E h_l^2 - (rho + D) E[h_l^2 1_(Bad_l)] ).
Insert (CAP)_l and sum. QED
Where each need stands.
- (CAP)_l from a Poincare constant lam of nu_s (the computation of Proposition RARE-P, row 936, 4.3): A = (1 + eta)/(eta lam),
  del = (1 + eta) P(Bad_l). The condition (rho + D) A <= 1 asks lam >= (rho + D)(1 + eta)/eta > D. With the global constant lam = gam_s this is
  circular with a loss: the premise gam_s > D is stronger than the conclusion gam_s >= rho - ... . So RARE-P does
  not transfer: there, an even gap pays for an odd one; here the same gap would have to pay for itself.
- (CAP)_l from local conditional laws, uniformly in the conditioning: FALSE in the worst case (Lemma WC, PROVED).
  Given x_l = -w_l, the mid-slice variable y_l is Gaussian with mean 0 and covariance c Id_4, so
  P(|y_l| < 0.4 | x, w) = P(chi^2_4 < 0.64 beta) = 0.17 at beta 2.3, against 0.016 unconditionally for one free link (GUIDE quadrature). A defect
  is not rare under a bad conditioning. A scheme with typical conditionings needs a hierarchy of bad
  environments. That is the large-field problem of the renormalisation group, here at intermediate coupling
  with no small parameter. I did not attempt it.
- (LOC-COV) is the deepest need. It asks that the conditional covariance of a slice of the half-space lattice
  with a boundary field be bounded by a local diagonal form, at typical fields with rare exceptions. For the
  collective directions this is a mass-gap statement for the tilted system ((K3) of 5.5). No method gives it.
Stop of attack 3: (LOC-COV). The rarity of the frustrated links is not the obstruction; the locality of the
conditional covariance is.

## 7. The smallest unproved averaged-curvature inequality, and one GUIDE test

**7.1 The inequality (OPEN).** For s in (0, 1/beta), with nu_t, F_t = P_(0,t) F, b_t, J_(b,phi) of Sections 2-3:
  (ABS-flow)_s: there is a piecewise continuous kap_(s,t), 0 <= t <= c_s, such that for every smooth gauge-invariant F
  with values in a compact subset of (0, infinity) and almost every t:
     2 E_(nu_t)[ Var_(J_(b_t,phi))( <grad F_t^(1/2)(phi), q~> ) ] <= 2 kap_(s,t) E_(nu_t)|grad F_t^(1/2)|^2 + (1/4) E_(nu_t)[ F_t |Hess log F_t|^2 ].
Proposition (PROVED given (ID-ent) of 2.1, READ from BBD's Lemma 3.10 and (3.44), and Theorem BR). (ABS-flow)_s gives
(LSI-br)_s with 1/alpha_s <= integral over [0, c_s] of exp(2 integral over [0, t] of kap_(s,u) du) dt. Proof: by (ID-ent) and 3.1 (c),
I' <= 2 kap I, so I(t) <= exp(2 integral of kap) I(0), and Ent_(nu_s)(F) = 2 integral of I. QED
  (ABS-flow-seed)_a: (ABS-flow)_s on the box (a; (4a)^3), with (1/2) integral over (0, 1/beta) of alpha_s ds >= K_a.
Strength, in decreasing order: (TILT-COV-sup) with a box-uniform kbar; (ABS-flow-seed)_a for one a; (LSI-br-seed)_a;
(HC-vac)_(K_a); the seed. The first arrow is trivial (drop the Hessian term and take the supremum), the second is
the Proposition, the rest is rows 947 and 931. The variance form, from (ID-var), with F_t in place of F_t^(1/2) and
E|Hess F_t|^2 in place of the last term, gives gam_s and E_1 >= K_a only.
What it is. An average over typical tilts phi (the law nu_t of 3.1 (d)), weighted by the test function, with the
Hessian term kept, at every scale of the flow. By 5.4 it lies strictly between the pointwise criterion and the
inequality itself. What it is not: it is not smaller than (LSI-br-seed) in any proved sense. It is another
sufficient form, whose input is a link covariance of the two-slice system in a linear field.
Why I cannot prove it. Its content at non-zero phi is (K2) and (K3) of 5.5, and Section 6 stops at (LOC-COV).
The only tilt where the covariance is known is phi = 0 (Lemma Z).

**7.2 One GUIDE test that could refute the supremum form (design and criteria written before any run).**
Object. At t = 0 the law J_(0,phi) is a product, and for the uniform tilt phi_l = kap0 1 (the unit quaternion on every
link) it is a pair of boundary slices of half-space lattices with the Higgs-type boundary term kap sum_l (1/2) tr w_l,
kap = kap0/s. For a link direction i, a momentum k orthogonal to i and an imaginary unit e_a, the vector
z = e^(i k x) e_a on the links of direction i is horizontal at phi (it is orthogonal to lattice gradients). Put
  chi(kap; k) := E|sum over links l of direction i of e^(i k x_l) w_l^a|^2 / (number of those links)
(connected; averaged over i, a and the directions of k). (TILT-COV-sup) at t = 0 gives kbar_(s,0) >= chi(|phi|/s; k)/s^2 for all
kap, k. So if chi* := max over kap of chi(kap; k_min) grows with the box side, no box-uniform kbar exists.
Control and expectation. At kap = 0: chi = 1/4 exactly for SU(2) and 1/2 for U(1), every box (Elitzur). For compact
U(1) in the Coulomb phase I expect (ARGUED in the lane log, not proved) growth of chi* with the side, at the tilt
where the boundary layer orders: there the photon is exposed with a surface stiffness of order beta |k|.
Verdict rules. On boxes of side 4, 6, 8 at beta 2.3 (half-space of 6 slices, open far end, tilt on slice 0):
REFUTES a box-uniform (TILT-COV-sup) for SU(2) on these boxes (GUIDE) if chi* at k_min rises by more than a factor
1.25 per step of the side, outside three standard errors. NOT REFUTED otherwise, which proves nothing. The
run is valid only if the kap = 0 control returns 1/4 within three standard errors.
What it cannot show. It tests one family of tilts and one scale t = 0. The averaged form 7.1 would need the
typical tilts of 3.1 (d) and nested sampling (the conditional covariance of (x, w) given the bridge point), and
by 5.4 no finite set of test functions can confirm it.

**7.3 First decision, superseded by 7.4-7.5: not to run the test on sides 4, 6, 8. Reason (ARGUED, hand estimate).** A test is worth its run only if the control
can fail. For compact U(1) in the Coulomb phase, at a tilt kap just above the ordering of the boundary layer, the
transverse mode of momentum k on the boundary has a restoring coefficient of about kap rho + beta (|k| + k^2): rho is the
order of the gauge-orbit field (small near the ordering), beta |k| is the surface stiffness of the massless bulk,
beta k^2 the magnetic term of the layer. So chi is about 1/(beta (|k| + k^2)) there. It exceeds its own kap = 0 value 1/2 only
when beta (|k_min| + k_min^2) < 2, that is for box sides above about 12 at beta 1.3, and it reaches twice that value near
side 24. On sides 4, 6, 8 the U(1) control would stay at or below 1/2 and the run could not tell U(1) from SU(2).
A valid run therefore needs U(1) boxes of side 12 to 24 and SU(2) boxes above the confinement length at the same
sides (about 10^5 sites and several thousand sweeps per point): hours on this machine in plain numpy, or the
compiled code of row 954. (This cost estimate was too high by a factor of about 3: see 7.4.) The design, the control
and the verdict rules of 7.2 stand, with larger sides; the rules actually used are those of 7.4. Scope: the estimate above is not a
proof that U(1) fails in this family; Lemma NEC only proves that it fails in some family.
The second test, for the averaged form (proposed, not run): sample (x, w) from J and the bridge point y; sample
the two conditional slices given y (two half-space lattices with boundary field y/s, y/s'); estimate
E[Var(<grad G(y), q~> | y)] / E|grad G|^2 against 1/c and E|Hess G|^2 / E|grad G|^2 for the slow modes G of rows 947 and 954 (time-like
plaquette sum, winding lines). By 5.4 (c) this gives a lower bound on kap_(s,0), and by (ID-var) the initial slope of
I_2. It can show that a claimed kap_(s,0) is too small. It cannot confirm (ABS-flow).

**7.4 Run of the first test at larger sides (criteria written at 14:32Z, BEFORE the run; added after 7.3 when a smoke
test showed the plain-numpy code is fast enough: 28 ms per sweep for SU(2) at side 16, 13 ms for U(1)).**
Script `/tmp/gap-avgcurv-968/scripts/tilt.py` (not committed): full lattice with time-like links, 6 slices, open
time, hot start, heat bath (Creutz sampler for SU(2), von Mises for U(1)), checkerboard by direction and parity,
tilt kap Re(U) on the spatial links of slice 0. Measured on slice 0: chi1 = chi(kap; k_min) of 7.2 (imaginary link
components, k transverse to the link direction), chi0 (the same at k = 0), the mean real part, and the middle
spatial plaquette. 400 thermalisation sweeps, 2000 measurements 2 sweeps apart, errors from 20 blocks.
Runs: SU(2) at beta 2.3, sides 8, 12, 16, kap in (0, 0.6, 1.0, 1.4, 1.9, 2.6, 4.0); compact U(1) at beta 1.3 (Coulomb phase,
RECALLED: the transition is near 1.01), sides 8, 16, 24, kap in (0, 0.3, 0.5, 0.7, 1.0, 1.5, 2.5).
Smoke test (about 14:31Z, lock holder gap-avgcurv-968): kap = 0 on side 4, 300 measurements: SU(2) chi1 = 0.247 +- 0.004 (exact
1/4), U(1) chi1 = 0.517 +- 0.029 (exact 1/2); SU(2) plaquette 0.609 after 100 sweeps (recalled 0.60).
Verdict rules.
- (V0) Validity: at kap = 0, chi1 within three standard errors of 1/4 (SU(2)) and 1/2 (U(1)) on every box.
- (V1) The control is informative only if, for U(1), chi* := max over kap > 0 of chi1 exceeds 1/2 by three standard
  errors at side 24 and rises from side 8 to 16 to 24. If (V1) fails, the family does not expose the photon at
  these sides, my estimate of 7.3 is wrong or too optimistic, and the SU(2) numbers decide nothing.
- (V2) REFUTES a box-uniform (TILT-COV-sup) for SU(2) at beta 2.3 on these boxes (GUIDE) if chi* rises by more than a
  factor 1.25 per step 8 -> 12 -> 16, outside three standard errors. NOT REFUTED otherwise, which proves nothing.
Limits: one tilt family, the scale t = 0 only, 6 slices with an open far end in place of the vacuum factor, no
autocorrelation analysis beyond the blocks.

**7.5 Results of the run (GUIDE; logs `/tmp/gap-avgcurv-968/logs/tilt_results.jsonl`, `batch.log`, not committed).**
Entries are chi1 = chi(kap; k_min) with the block error on the last digits; the last column is chi0 (k = 0) at the
three sides. Peak resident memory was not recorded; the script stops itself above 2 GB and did not stop.

| compact U(1), beta 1.3, kap | side 8 | side 16 | side 24 | chi0 at 8, 16, 24 | mean Re U (side 24) |
|---|---|---|---|---|---|
| 0 | 0.513(9) | 0.503(9) | 0.506(6) | 0.50, 0.52, 0.52 | 0.00 |
| 0.3 | 0.529(10) | 0.527(11) | 0.547(12) | 0.51, 0.54, 0.54 | 0.16 |
| 0.5 | 0.588(15) | 0.627(15) | 0.624(16) | 0.70, 0.66, 0.66 | 0.33 |
| 0.7 | 0.324(3) | 0.506(19) | 0.929(34) | 1.01, 0.86, 0.83 | 0.63 |
| 1.0 | 0.316(3) | 0.494(12) | 0.575(8) | 0.79, 0.76, 0.80 | 0.76 |
| 1.5 | 0.295(4) | 0.402(4) | 0.454(7) | 0.54, 0.58, 0.55 | 0.83 |
| 2.5 | 0.238(3) | 0.301(2) | 0.314(4) | 0.35, 0.35, 0.36 | 0.89 |

| SU(2), beta 2.3, kap | side 8 | side 12 | side 16 | chi0 at 8, 12, 16 | mean Re U (side 16) |
|---|---|---|---|---|---|
| 0 | 0.2501(12) | 0.2491(15) | 0.2516(21) | 0.248, 0.254, 0.243 | 0.00 |
| 0.6 | 0.2556(22) | 0.2579(14) | 0.2620(16) | 0.259, 0.257, 0.259 | 0.16 |
| 1.0 | 0.2747(21) | 0.2759(14) | 0.2768(19) | 0.284, 0.275, 0.283 | 0.28 |
| 1.4 | 0.2732(24) | 0.2997(22) | 0.3091(29) | 0.336, 0.326, 0.338 | 0.46 |
| 1.9 | 0.2318(19) | 0.2698(25) | 0.2901(27) | 0.327, 0.323, 0.318 | 0.61 |
| 2.6 | 0.1964(12) | 0.2281(16) | 0.2469(18) | 0.264, 0.271, 0.270 | 0.71 |
| 4.0 | 0.1542(10) | 0.1713(12) | 0.1818(12) | 0.196, 0.196, 0.202 | 0.80 |

Sanity: SU(2) middle plaquette 0.600 to 0.604 in all 21 runs (recalled 0.60 at beta 2.3); U(1) 0.776.
Verdicts, by the rules of 7.4.
- (V0) PASS. At kap = 0 all six chi1 values are within 1.5 standard errors of 1/4 and 1/2 (Elitzur), and the six
  chi0 values within 2.
- (V1) MET as written: chi* = 0.588(15), 0.627(15), 0.929(34) at sides 8, 16, 24; at side 24 it is 12 standard errors
  above 1/2. Two cautions. The step from 8 to 16 is inside two standard errors. And the k = 0 value does not grow
  (1.01, 0.86, 0.83 at kap 0.7), so the rise of chi1 looks like an approach to a finite chi0 of about 0.8 to 1.0, not like
  a divergence. The grid has no point between kap 0.5 and 0.7, where the layer orders (mean Re U from 0.33 to 0.63),
  so the maximum over kap is not resolved. The run does not show that this family diverges for U(1).
- (V2) NOT REFUTED for SU(2) at beta 2.3 on sides 8, 12, 16: chi* = 0.2747(21), 0.2997(22), 0.3091(29), ratios 1.09 and 1.03
  per step, below 1.25 and falling. This proves nothing about the seed box.
Readings (GUIDE, no proof weight).
- The photon shows as a dependence on k, not as a size: chi1/chi0 at the tilt of the maximum is 0.32, 0.59, 1.1 for
  U(1) (kap 0.7; sides 8, 16, 24) against 0.81, 0.92, 0.91 for SU(2) (kap 1.4; sides 8, 12, 16). The SU(2) boundary
  mode has reached its k = 0 value by side 12; the U(1) mode has not by side 16.
- Zero field is not the worst tilt, even in this simplest family: for SU(2), chi0 = 0.338(6) at kap 1.4 on side 16,
  1.35 times the Elitzur value; for U(1) about twice. So the arithmetic of 3.4 is an optimistic end, also
  empirically. The excess is stable in the side for SU(2) (0.336, 0.326, 0.338).
- The SU(2) layer orders through a smooth crossover (mean Re U and its variance show no growth with the side
  beyond 8 percent), in line with the expectation of 4.8.
What the run teaches about the test itself (arithmetic from Lemma NEC; the value of E_1 is an estimate). Lemma NEC
forces s^2 k* >= (1/(2 beta)) log(1/E_1) at the mid-slice, a logarithm. At side 24 and beta 1.3, with the free-photon value
E_1 of about 0.26, that is 0.52, below the zero-field value (at least 1 in these units). So the growth that kills a box-uniform (TILT-COV-sup) for U(1) can be slow, and no run at sides up to 24
can show it unless some tilt family has a true divergence; this family did not show one. The criterion is
exponentially lossy in kbar, so a logarithmic growth of the tilted covariance is enough to destroy it. This is
the practical weakness of the supremum form: SU(2) needs boundedness at all tilts and all sizes, and a small-box
test can refute it only by luck.

## 8. Status, answers, and the result

**8.1 Status table.** "PROVED" means proved by hand here, by Claude Fable 5.2, not yet checked by another model.

| Statement | Where | Status |
|---|---|---|
| BBD Theorem 3.6 and Chen-Eldan Proposition 39, Lemma 40 average over the scale and take a supremum over the field or tilt; the identities (ID-ent), (ID-var) are the averaged statements behind BBD | 2.1-2.3 | READ (sources quoted; not rebuilt) |
| Proposition FLOW: nu_s is Gaussian(c) x e^(-V_0) with V_0 concave; its renormalised potentials are the free energies of the two-slice law with middle coupling b_t = t/(s s') in linear fields; Hess V_t = -Cov_(J_(b_t,phi))(q~); law of the typical tilt | 3.1 | PROVED |
| Lemma Z: at zero field the covariance is k0 Id with k0 <= 1/(4 c^2), every box, every group containing -1 that acts irreducibly | 3.2 | PROVED |
| Theorem POL-BR: (TILT-COV-sup) gives (LSI-br)_s and (HC-vac) with explicit constants; exact in every Gaussian mode | 3.3 | CONDITIONAL on BBD Theorem 3.6 (cited, with the horizontal reading of its proof) and Theorem BR (row 947, check 949) |
| The integrated form has no threshold; the zero-field point, which gives the three ceilings of row 941, costs a finite factor at every beta (alpha0 = 8 beta^2/(e^(2 beta) - 1) at the mid-slice) | 3.4, 4.7 | PROVED (arithmetic at one point; not a bound for SU(2)) |
| Lemma NEC: k* >= 2 beta log(1/E_1(B)) in every model of the class | 4.1 | PROVED given 3.3 and Proposition HC |
| Fact tests: FP exact and fails the rate through the photon modes; compact U(1), Q_8/2T, SMALL-BOX, K7: the hypothesis must grow with the box or with beta; FT-FK: the flow is kinetic-only and decides nothing, the model enters only through m | 4.2-4.7 | PROVED for FP and for the Lemma NEC consequences; ARGUED for compact U(1) (no gap RECALLED) and for the extension of Theorem BR to finite groups |
| One free link: sign of the tangential curvature (negative near r = 0 iff beta > n/2 at the mid-slice); E[Phi'/r] = (n - 2) E r^(-2) | 5.2 | PROVED; numbers GUIDE |
| Proposition ANG: fibre tensor with the Ricci term 2/r_l^2; the Elitzur point is an artefact for SU(2) and stays marginal for U(1); frustrated links stay negative | 5.3 | PROVED (formula, zero-field reading); ARGUED (frustrated-link numbers) |
| Proposition AVG: an average over the measure without the Hessian term is the pointwise criterion; with it, the Poincare inequality itself | 5.4 | PROVED given Bochner's identity and the slice theorem (RECALLED) |
| Proposition SCHR and its death by volume; the direction-resolved form; RARE-P does not transfer; Lemma WC | 6.1-6.3 | PROVED (6.2 given the premise (DENS), not proved) |
| (TILT-COV-sup) with a box-uniform bound; (ABS-flow-seed)_a; (LOC-COV); (LSI-br-seed)_a; (LSI-J-seed)_a; the seed | 3.3, 6.3, 7.1 | OPEN |
| GUIDE test of the supremum form (uniform Higgs-type tilt, transverse boundary susceptibility), sides 8 to 24 | 7.2-7.5 | GUIDE, RUN: controls pass; SU(2) at beta 2.3 NOT REFUTED on sides 8-16 (chi* 0.275, 0.300, 0.309); the U(1) control rises (0.59, 0.63, 0.93) but shows no divergence; zero field is not the worst tilt (factor 1.35 for SU(2)) |

**8.2 Answers to the row.**
- Input (1), integrated or averaged criteria. Both named criteria need a supremum over the field or tilt at each
  scale; only the scale is averaged (Section 2). Applied to the bridge marginals they give Theorem POL-BR. Its
  hypothesis is a bound on a link covariance of the two-slice system in every linear field, uniform in the box.
  That is not proved, and by Lemma NEC it is false wherever the gap closes with the box.
- Input (2), Ricci against the averaged negative part. In the bridge picture the Ricci curvature of S^3 is the
  radial average of the ambient curvature of one link (5.2), and in the fibre form it is the term 2/r^2 (5.3). It
  removes the zero-field ceiling of row 941, which U(1) keeps. It does not act on frustrated links or on the
  collective directions.
- Input (3), a rare set. The scalar form dies by the volume; the direction-resolved form needs a local bound on
  the conditional covariance, (LOC-COV), which is a mass-gap statement for the tilted system. RARE-P does not
  transfer (the same gap would pay for itself), and rarity uniform in the conditioning is false (Lemma WC).
- The averaged route left open by check 958. It is real but it is not a reduction: at the Poincare level the
  averaged inequality with the Hessian term is the inequality itself (5.4 (b)). The form with content is the
  flow form (ABS-flow) of 7.1. No inequality smaller than (LSI-br-seed)_a came out of this row.
- What changes. For the lead: (i) the three one-scale ceilings of row 941 are not ceilings of the route through
  Theorem BR, so "curvature criteria die below the window" should read "one-scale curvature criteria"; (ii) the
  open input of the lane can now be written as a second-moment statement, (TILT-COV-sup), in place of a
  functional inequality for all test functions, at the price of a supremum over linear fields; (iii) an
  averaged-curvature lane should not be queued again without a route to (LOC-COV); (iv) small-box runs cannot
  decide the supremum form (7.5): its failure for a massless rival may be a logarithmic growth.

**8.3 For the checker, in this order.** (1) Proposition FLOW (b), (d): the completion of the square and b_c = beta.
(2) The use of BBD Theorem 3.6 on a finite scale interval (their Remark 3.8) and the horizontal reading (a) of
2.1; if the horizontal reading fails, Theorem POL-BR holds with the supremum over all z, and Lemma NEC is
unchanged. (3) Lemma Z. (4) Proposition ANG: the fibre Hessian and the cancellation of |v|^2/c. (5) Proposition AVG
(a): the use of the slice theorem at principal orbits. (6) 6.3: E|Hess G|^2 >= sum_l E|grad h_l|^2. The physics readings
(4.8, 7.3) carry no proof weight.

**Reading order.** Sections 3 and 4 (the criterion and its fact tests), then 5.4 and 7.1 (what "averaged" can
mean), then 5.2-5.3 (Ricci), then 6.

RESULT: Row 968 (Claude Fable 5.2 max, author, checked by no one): the averaged-curvature route does NOT close; (LSI-J-seed) and the seed stay OPEN, and no inequality smaller than (LSI-br-seed)_a was found. PROVED by hand: Proposition FLOW (the Polchinski flow of each bridge marginal nu_s is the switching-on of the one time-like coupling between two slices, and its curvature is minus a link covariance of the two-slice law in a linear field); Lemma Z (zero-field covariance, every box); Lemma NEC (the tilted covariance must grow at least like 2 beta log(1/E_1)); Proposition ANG (the Ricci curvature of S^3 is the term 2/r^2 of the fibre tensor and removes the Elitzur ceiling of row 941, which U(1) keeps); Proposition AVG (an average over the measure is the pointwise criterion without the Hessian term and the Poincare inequality itself with it); Proposition SCHR with its death by volume, and the failure of RARE-P and of uniform conditional rarity to transfer. CONDITIONAL on BBD Theorem 3.6 (cited) and Theorem BR: Theorem POL-BR, a box-uniform bound on that covariance over all linear tilts gives (HC-vac) and the seed for some a, with no threshold in beta. READ: Bauerschmidt-Bodineau-Dagallier and Chen-Eldan both need a supremum over the field or tilt; only the scale is averaged. FACT TESTS: the criterion is exact for the free photon and fails only its rate; for compact U(1), Q_8/2T, SMALL-BOX and K7 its hypothesis must fail (Lemma NEC); FT-FK holds (the flow is kinetic-only, the model enters only through m). SMALLEST UNPROVED AVERAGED-CURVATURE INEQUALITY: (ABS-flow-seed)_a of 7.1 (typical tilts, Hessian term kept, every test function), implied by the supremum form (TILT-COV-sup); its obstruction is (LOC-COV), a local bound on the conditional covariance of a tilted half-space slice, which is a mass-gap statement. GUIDE (7.4-7.5, criteria written before the run): uniform Higgs-type tilt on the boundary slice, transverse boundary susceptibility, 42 runs; Elitzur controls pass; SU(2) at beta 2.3 on sides 8, 12, 16: 0.275, 0.300, 0.309, NOT REFUTED (proves nothing); compact U(1) at beta 1.3 on sides 8, 16, 24: 0.59, 0.63, 0.93, a rise toward a finite k = 0 value, no divergence shown; zero field is not the worst tilt (factor 1.35 for SU(2)); by Lemma NEC the growth that kills the supremum form may be logarithmic, so small-box runs cannot decide it.
