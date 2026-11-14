lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T16:17Z

# gap-oddgap-max (FINISH row 930): the odd-gap form of the flux half

Worker: Claude Fable 5.2, max effort, Mac mini worker, pinned at commit edc2c18b3 on
`claude/ym4d-hard-route`. Author item. No commit, no push (relay copies this file).
Research-stage working state; nothing here is a public claim.

Status labels used below: PROVED, CONDITIONAL (on named inputs), GUIDE (numeric or heuristic,
carries no proof weight), OPEN.

## Plan (at most eight steps; one step per response; each appended before the next)

1. **Read the inputs in full**: row 922 `library/gap-fr-opus.md`, its check row 927
   `library/gap-fr-check-astra.md`, rows 899/901 (VAR-SLAB), and Step A of row 929
   `library/gap-seam-max.md` if present. Grep `library/open-core.md` and the FINISH rows for
   the lemma names before any attack. Record the exact statements used (p, R, FR, lambda_odd,
   ODD-0, the ceilings 2/3, 0.775, 4G_3 = 1.0109).
2. **STEP A, U(1) fact test, exact**: Gaussian U(1) (Villain or noncompact) on the same box and
   time extent, pi twist in place of the centre twist. Compute p, FR and lambda_odd in closed
   form and say which factor of `p <= FR/(2 lambda_odd)` carries the U(1) failure.
3. **STEP A, frozen groups**: the same three quantities for frozen Q_8 and 2T at the level of
   a sound estimate (a domain wall should cost nothing).
4. **Verdict of Step A**: either name the failing factor, or declare the odd-gap form the wrong
   target and give the form that does fail for U(1).
5. **STEP B, statement**: the exact SU(2) Wilson statement to attack (beta about 2.3-2.6, the
   size the flux half needs), with the property U(1) lacks written into the hypothesis.
6. **STEP B, attack 1** on the failing factor, as a real proof; mark the step where the photon
   breaks it.
7. **STEP B, attack 2 or repair**, and consistency with the ceilings 2/3, 0.775, 4G_3 = 1.0109.
8. **Result table and RESULT line**: every statement marked PROVED / CONDITIONAL / GUIDE / OPEN,
   what failed, what is left.

## Log

- 2026-11-14T04:17Z: file created; reading inputs (step 1).
- 2026-11-14T05:05Z: step 1 written (Section 1). Next: Section 2, the exact Gaussian U(1) values.

## 1. Inputs read, duplicate check, notation (step 1; READ = read at the pinned commit, not re-proved)

**Read in full:** `library/gap-fr-opus.md` (row 922, Claude Opus 5.5 max, 166 lines);
`library/gap-fr-check-astra.md` (row 927, Codex gpt-6-astra xhigh, 701 lines);
`library/gap-wall-assume-max.md:299-354` ((VAR-SLAB), row 899, Claude Fable 5.2 max) and
`library/gap-wall-assume-check-astra.md:19-71` (row 901). `library/gap-seam-max.md` (row 929) is
on the branch with its Section 1 only: **it has no Step A yet**, so there is no U(1) mechanism of
the glue half to compare with. I name the mechanism found here in Section 4 for row 931 to compare.

**Duplicate check (rule 0a).** `grep -n -i` for `lambda_odd`, `odd gap`, `ODD-0`, `VAR-SLAB`, `(FR)`
in `library/open-core.md`: no hit. In `FINISH.md`: rows 922, 927, 930 (this row), 931 (direction,
reads this file), 933 (check of this file). Row 928 is a reading row (no published precedent found
for the Fisher-information or odd-gap forms). No other row attacks the odd gap. I proceed.

**Credit.** The transfer-operator frame (gauge-averaged positive trace-class operator, Z = Tr L^s)
is from the account of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text (SA 2315-2335, as located by check 927). (VAR-SLAB) is row 899; the even-law identities, the
odd-Langevin criterion and ODD-0 are row 922 with the corrections of check 927. 't Hooft (1979) for
flux sectors as projected transfer traces; Tomboulis and Yaffe (1985) for twist and flux relations
(both as recorded by row 928, not re-read here).

**Notation (fixed for the whole file).** Spatial box B = L_1 x L_2 x L_3, periodic; N = L_2 L_3;
time extent a even; t = a/2. T the gauge-invariant transfer operator, A^s(u, v) the kernel of T^s,
symmetric and strictly positive. J = centre flip of the direction-1 links of one cut x_1 = const of
a slice; C f = f o J; Theta(u, v) = (u, Jv). P_e, P_o = (1 +- C)/2. Z = Tr T^a,
p = Tr(T^a P_o)/Z, r = 1 - 2p. E_s = kernel of T^s P_e, O_s = kernel of T^s P_o, R_s = O_s/E_s,
so |R_s| < 1, R_s o Theta = -R_s. The seed box of rows 899/922: L_i = 20, a = 10, t = 5,
beta = 2.3, target p <= p_* with p_* between 1e-4 and 2e-4.

**Statements used (all HOLD in check 927).**

- (I1) Even two-slice law w_e = E_t^2/Z_e, Z_e = (1 - p) Z; w_e o Theta = w_e;
  p/(1 - p) = Var_(w_e)(R_t) = E_(w_e)[R_t^2].
- (I2) FR_u := sum over the 3|B| links b of slice u of E_w |grad_b log rho|^2, with
  rho = A^t o Theta/A^t = (1 - R_t)/(1 + R_t) and w = (A^t)^2/Z. Then
  FR_u = 4 (1 - p) E_(w_e)[ |grad_u R_t|^2 (1 + R_t^2)/(1 - R_t^2)^2 ] >= 4 (1 - p) D_u,
  D_u := E_(w_e)|grad_u R_t|^2. Trivial bound FR_u <= 12 beta^2 |B|.
- (I3) lambda_odd := the best constant in Var_(w_e)(F) <= lambda_odd^(-1) E_(w_e)|grad F|^2 over
  smooth F(u, v), gauge invariant in each slice, with F o Theta = -F (gradient over both slices,
  unit-S^3 metric per link). Then p/(1 - p) <= 2 D_u/lambda_odd, hence
  **p <= FR_u/(2 lambda_odd)** (check 927 Section 6).
- (I4) ODD-0: at beta = 0, lambda_odd = 3 L_1. One winding line chi_l has Rayleigh quotient
  L_1 (1 - q)/q, q = E_(w_e) chi_l^2, at every beta.
- (I5) grad_b R_t(u, v) = beta Cov_mix(f_b, sigma): mix = the mixture of the slab laws mu_(u,v),
  mu_(u,Jv) with weights (1 +- R_t)/2, sigma = +-1 the component label, f_b the first-layer force.
  M_s = E_mix[sigma | layers 0..s] = R_(t-s)(w_s, v) is a martingale (M_t := sigma).
- (I6) The odd transfer-chain gap is 1 - exp(-E_-); E_- is its decay rate (check 927 Section 5).
- (I7) Failed in check 927, to be redone here: the U(1) fact test (no cited theorem for p), the
  frozen-group domain-wall deduction, the flat-wall witness.

**The two chain steps, named for the fact tests.** (a) Poincare: E_(w_e)[R_t^2] <= 2 D_u/lambda_odd.
(b) Weight: D_u <= FR_u/(4 (1 - p)). The criterion (I3) is (a) then (b). A proof of the flux half
through this form supplies a pair (lambda_0, eps) with lambda_odd >= lambda_0 (the gap factor),
FR_u <= eps (the response factor) and eps <= 2 p_* lambda_0. By (I4), lambda_0 <= L_1 (1 - q)/q,
which is 3 L_1 = 60 at q = 1/4.

## 2. STEP A, U(1): the exact Gaussian values (step 2)

### 2.1 Model G (definition)

Model G is the Villain U(1) model with the monopole constraint dn = 0 and no spatial magnetic
flux: the spin-wave model with compact holonomies (torons). It is **not** the full Villain model;
nothing here is proved about monopoles.

- Slice space X_G = R^E/(2 pi Z^1_cl): E = the 3|B| spatial links, Z^1_cl = the closed integer
  1-cochains (integer gauge shifts dj and the windings). Flat metric of R^E, so each link is a
  unit-speed coordinate, as in the unit-S^3 convention for SU(2). Gauge group R^(sites),
  theta -> theta + dg.
- V(theta) = (beta/2) |d theta|^2. One-step kernel A_G(u, v) = e^(-(V(u)+V(v))/2) I(u, v),
  I(u, v) = sum over w in Z^3 of the integral over g in R^(sites)/R of
  exp(-(beta/2) |u - v + dg - 2 pi sum_i w_i c_i|^2), c_i = the indicator of the direction-i links
  crossing one fixed cut. I is the Villain time-like weight, gauge averaged, with the winding sum.
- The pi twist: J adds pi c_1 (it adds pi to the direction-1 links of one cut). J is an isometric
  involution of X_G, V o J = V and A_G(Ju, Jv) = A_G(u, v).
- beta is the Villain coupling. Matching exp(beta cos) to SU(2)'s exp(beta x_p) at quadratic order
  gives the same symbol; all formulas below keep beta general.

Every identity (I1)-(I5) of Section 1 holds in Model G: their proofs use only a symmetric strictly
positive kernel with finite traces and a measure-preserving isometric involution J commuting with
T. (The transverse directions of X_G are not compact; they carry Gaussian weights.)

### 2.2 Lemma G1 (factorization; PROVED)

Split R^E = exact + coexact + harmonic (orthogonal). The harmonic part of theta is constant on the
links of each direction; put Phi_i(theta) = L_i times the mean of theta over the direction-i links.
Phi_i is defined modulo 2 pi on X_G (2 pi c_i shifts it by 2 pi; dj does not move it). Write u_T
for the coexact part. Then, for every s >= 1,

  A_G^s(u, v) = P_s(u_T, v_T) prod_i K_(s E_i)(Phi_i(u) - Phi_i(v)),
  K_tau(psi) = sum over e in Z of exp(-tau e^2 + i e psi) = sqrt(pi/tau) sum_n exp(-(psi - 2 pi n)^2/(4 tau)),
  E_i = L_i^2/(2 beta |B|),  so  E_1 = kappa/(2 beta),  kappa := L_1/N,

with P_s a strictly positive symmetric kernel on the coexact space (trace class on it: d is
injective there, so every transverse mode has a positive frequency).

Proof. c_i = (1/L_i) 1_i + (exact), so |u - v + dg - 2 pi sum w_i c_i|^2 =
|(u - v)_T|^2 + |d(g + ...)|^2 + sum_i (|B|/L_i^2)(Phi_i(u) - Phi_i(v) - 2 pi w_i)^2. The g-integral
is a constant. The w_i-sum is a periodized Gaussian of variance L_i^2/(beta |B|) = 2 E_i, which is
K_(E_i) up to a constant (Poisson summation). V depends on u_T only. Powers: K_tau * K_tau' =
2 pi K_(tau+tau'). QED

Consequences. (i) J shifts Phi_1(v) by pi and moves nothing else. (ii) For F = f(Phi_1(u)):
|grad_u F|^2 = |B| (f'/N)^2 = kappa f'^2. (iii) E_s, O_s are P_s prod_(i>1) K times the even and odd
parts of K_(s E_1), so **R_s depends on (u, v) only through psi = Phi_1(u) - Phi_1(v)**:
R_s = (K_tau(psi) - K_tau(psi + pi))/(K_tau(psi) + K_tau(psi + pi)) at tau = s E_1.
(iv) w and w_e are product laws: (transverse part) x (Phi_2, Phi_3 part) x (law of the pair
(Phi_1(u), Phi_1(v)), with density prop. to K_tau(psi)^2, resp. (K_tau(psi) + K_tau(psi + pi))^2).

From here tau := t E_1 = t kappa/(2 beta) and y := exp(-pi^2/(8 tau)). Seed box: kappa = 1/20,
tau = 5/92, pi^2/(8 tau) = 2.3 pi^2 in (22.6, 22.8), so y < 2e-10 (GUIDE value 1.385e-10). In a cube
with a = L: tau = 1/(4 beta), independent of L.

### 2.3 Proposition G2 (p; PROVED)

p = sum_(e odd) exp(-2 tau e^2)/sum_(e in Z) exp(-2 tau e^2), and
1 - 2p = 2 sum_(m>=0) y^((2m+1)^2) / (1 + 2 sum_(m>=1) y^(4 m^2)). For y <= 1/2:

  y/(1 + 4 y^4) <= 1/2 - p <= y (1 + 2 y^8).

Proof. The traces factor by G1; the Phi_1 factor of Tr(T^a C)/Tr(T^a) is
sum (-1)^e e^(-a E_1 e^2)/sum e^(-a E_1 e^2), a E_1 = 2 tau. Poisson summation gives the second
form. The bounds are geometric series. QED

So **Model G fails the flux half at its maximum**: p = 1/2 - 1.4e-10 at the seed box, and
p >= 1/2 - 1.2e-5 in every cube a = L at beta = 2.3 (y = e^(-pi^2 beta/2)). The electric flux e in
direction 1 is a rotor with levels E_1 e^2, E_1 = L_1/(2 beta N): Coulomb flux spreads over the
cross-section. This replaces the citation that check 927 failed (row 922 line 125).

### 2.4 Proposition G3 (the response factor FR; PROVED)

FR_u = kappa J(tau), J(tau) := E_w[X'(psi)^2], X = log(K_tau(psi + pi)/K_tau(psi)), w(d psi) prop.
to K_tau(psi)^2. With m(psi) := the mean of n under the weights exp(-(psi - 2 pi n)^2/(4 tau)):

  X'(psi) = (pi/(2 tau)) (1 - 2 m(psi) - 2 m(pi - psi))   (exact).

Bounds: |X'| <= pi/(2 tau) for all psi and all tau, hence

  J(tau) <= pi^2/(4 tau^2),  i.e.  **FR_u <= pi^2 beta^2 N/(t^2 L_1)**  (every size, every beta);

and for tau <= 1/16: J(tau) >= pi^2/(8 tau^2), i.e. FR_u >= pi^2 beta^2 N/(2 t^2 L_1).

Proof. FR_u = E_w|grad_u X|^2 and X is a function of psi, so G1(ii) gives kappa E_w[X'^2].
(log K_tau)'(psi) = -(psi - 2 pi m(psi))/(2 tau). m is odd, m(psi + 2 pi) = m(psi) + 1, so
m(psi + pi) = 1 - m(pi - psi); subtracting gives the formula. The weights are an exponential
family in psi, so m' = (pi/tau) Var(n) >= 0; with m(0) = 0 and m(pi) = 1/2, both m(psi) and
m(pi - psi) lie in [0, 1/2] on [0, pi]; X' is odd. So |X'| <= pi/(2 tau).
Lower bound. For x in [0, pi] and tau <= 1: m(x) <= e^(-pi(pi - x)/tau) + 3 e^(-2 pi^2/tau)
<= 2 e^(-pi(pi - x)/tau) (the n = 1 weight relative to n = 0, plus the rest). For psi in
[tau, pi/2]: m(pi - psi) <= 2 e^(-pi) < 0.0865 and m(psi) <= 2 e^(-pi^2/(2 tau)) < 0.001, so
X' >= 0.82 pi/(2 tau). The w-mass of {tau <= |psi| <= pi/2} is at least 1 - 0.81 sqrt(tau) - 1e-6
>= 0.79: on |psi| <= tau the density is at most 1.003/sqrt(2 pi tau), and
the integral of K^2 over [pi/2, pi] is at most 1.01 (2 tau/pi) y times the peak scale (Mills
ratio; the n = 1 image adds less than one percent). 0.82^2 x 0.79 > 1/2. QED

Reading. X' = (pi/(2 tau)) tanh(pi psi/(2 tau)) up to exponentially small terms (row 922's
formula, now with an exact bound). The response is the pull of the two nearest images of the
toron; each direction-1 link feels pi beta/(t L_1).

### 2.5 Proposition G4 (the gap factor lambda_odd; PROVED)

**lambda_odd(G) = kappa mu_odd(tau)**, where mu_odd(tau) is the odd Poincare constant of the law of
(phi, phi') = (Phi_1(u), Phi_1(v)) on the 2-torus, density prop. to
(K_tau(psi) + K_tau(psi + pi))^2, psi = phi - phi', for the form |d_phi F|^2 + |d_phi' F|^2 and
F(phi, phi' + pi) = -F(phi, phi'). Bounds:

  (i) mu_odd(tau) <= 1 for every tau: **lambda_odd(G) <= L_1/N at every size and every beta**;
  (ii) for tau <= 1/16: mu_odd(tau) <= 2D/V <= 10.3 tau^(-3/2) y, with D := E_e[R_t'(psi)^2]
       <= 5.1 tau^(-3/2) y and V := p/(1 - p) >= 1 - 4.1 y.

Proof. Product reduction: w_e is a product law (G1(iv)) and the Dirichlet form is a sum over the
factors. For F odd, F(x, .) is odd in the pair (phi, phi') for each value x of the other
coordinates, so E|grad F|^2 >= E_x E|grad_(phi,phi') F|^2 >= kappa mu_odd E[F^2] (G1(ii));
equality is approached by F independent of x.
(i) F = cos(Phi_1(v)) is odd. w_e is invariant under the simultaneous rotation of phi and phi', so
phi' is uniform: E[F^2] = 1/2 = E[sin^2], Rayleigh quotient 1 (times kappa).
(ii) F = R_t is odd, depends on psi only; its quotient is 2D/V (two slices). Put A = K_tau(psi),
A_J = K_tau(psi + pi). Then R' = -2 A A_J X'/(A + A_J)^2, so
((A + A_J)/2)^2 R'^2 = (A A_J/(A + A_J))^2 X'^2 <= (pi^2/(4 tau^2)) min(A, A_J)^2 by G3. The
integral of min(A, A_J)^2 over the circle is at most 4 times the integral of A^2 over [pi/2, pi],
which is at most 4 x 1.01 (2 tau/pi) y in the units where the peak of A is 1; the integral of
((A + A_J)/2)^2 is at least half the integral of A^2, at least 0.4995 sqrt(2 pi tau). The quotient
is (4.045 pi/sqrt(2 pi)) tau^(-3/2) y <= 5.1 tau^(-3/2) y. V = (1 - r)/(1 + r) >= 1 - 2r. QED

What mu_odd is (PROVED structure, ARGUED asymptotics). Fourier modes e^(i(n phi + n' phi')) are odd
iff n' is odd; n + n' is conserved. Sector n + n' = 0 (functions of psi, odd under psi -> psi + pi)
is a double-well problem: the wells are psi = 0 and psi = pi, the barrier weight is y; its bottom
is mu_0 = 16 C (1 + o(1)) = 2 sqrt(2 pi) tau^(-3/2) y (1 + o(1)) (C the conductance of one
barrier). In the sectors n + n' = +-1 the form is 2|f'|^2 + (1/2)|f|^2, so the bottom is at least
1/2. So mu_odd = mu_0 once mu_0 < 1/2, and R_t itself is the slow mode: step (a) is nearly an
equality. For large tau, mu_odd -> 1 (the mode cos(Phi_1(v))).

### 2.6 Values (hand bounds PROVED from G2-G4; decimals in the GUIDE column are a double-precision
quadrature, `/tmp/oddgap-fable-scratch/u1_guide.py`, 0.6 GB, run under the numeric lock at 71
percent memory free; they carry no proof weight)

| Model G | hand bound | GUIDE |
|---|---|---|
| seed box, 1/2 - p | < 3e-10 | 1.385e-10 |
| seed box, FR_u = kappa J | in [20.8, 41.8] ((1058/500) pi^2 and (1058/250) pi^2) | 36.87 (J = 737.3 = 0.8826 pi^2/(4 tau^2)) |
| seed box, lambda_odd | < 8.2e-9 (0.05 x 10.3 x 79 x 2e-10) | 2.636e-9 (mu_0 = 5.273e-8; 2D/V = 5.296e-8) |
| seed box, FR_u/(2 lambda_odd) | > 1.2e9 | 7.0e9 |
| cube a = L, beta 2.3 (tau = 0.1087) | FR_u <= 4 pi^2 beta^2/L = 209/L; lambda_odd <= 1/L | 1/2 - p = 1.18e-5; FR_u = 174.5/L; lambda_odd = 1.51e-3/L |
| cube a = L, beta 2.6 (tau = 0.0962) | FR_u <= 267/L; lambda_odd <= 1/L | 1/2 - p = 2.7e-6; FR_u = 225.5/L; lambda_odd = 4.19e-4/L |

The two chain steps in Model G at the seed box (GUIDE): step (a) is saturated within 0.5 percent
(2D/V against mu_0); step (b) loses the factor FR_u/(4 (1 - p) D_u) = 1.4e10. So the criterion
p <= FR_u/(2 lambda_odd) is true and empty there: it overshoots p = 1/2 by 7e9.

## 3. STEP A, frozen Q_8 and 2T (step 3)

### 3.1 Proposition F1 (p at beta = infinity; PROVED, finite counting)

Let G be a finite subgroup of SU(2) containing -1, on a 4-torus of any sides. As beta -> infinity,
r = Tr(T^a C)/Tr(T^a) -> N_tw/N_0, where N_0 = the number of commuting quadruples (h_0, ..., h_3) in
G, and N_tw = the number of quadruples with h_0 h_1 = -h_1 h_0 and all other pairs commuting.

Proof. r = Z^tw/Z ((T2) of row 899), Z^tw having the sign of beta reversed on one sheet of (0,1)
plaquettes. On a finite lattice and group, e^(-beta #plaq) Z -> the number of configurations with
all U_p = 1, and e^(-beta #plaq) Z^tw -> the number with U_p = -1 on the sheet and 1 elsewhere (this
needs -1 in G). Fix a maximal tree: each such configuration is given by its values on the tree
(|G|^(#sites - 1) choices in both cases) and by the holonomies of the four generators at the base
point. Those commute, except that the (0,1) pair encloses one sheet plaquette, so its commutator
is -1. QED

Counting. A commuting tuple that is not central lies in exactly one maximal abelian subgroup
(two of them meet in the centre). An anticommuting pair (a, b) has Tr a = Tr b = 0, so both have
order 4 and lie in Q_8, not in one cyclic subgroup: 6 x 4 = 24 pairs; h_2, h_3 commute with both,
hence with Q_8, hence are central: N_tw = 24 x 4 = 96 for Q_8 and for 2T.

| G | maximal abelian subgroups | N_0 | N_tw | r(infinity) | p(infinity) | p/(1 - p) |
|---|---|---|---|---|---|---|
| Q_8 | three Z_4 | 16 + 3 (4^4 - 16) = 736 | 96 | 3/23 | **10/23** | 10/13 |
| 2T | three Z_4, four Z_6 | 16 + 720 + 4 (6^4 - 16) = 5856 | 96 | 1/61 | **30/61** | 30/31 |
| Z_2 (for comparison) | itself | 16 | 0 | 0 | 1/2 | 1 |

(Check of the method on pairs: 4 + 3 x 12 = 40 = 8 x 5 for Q_8; 4 + 36 + 4 x 32 = 168 = 24 x 7 for
2T: the group order times the number of classes.)

So the frozen groups fail the flux half at every size: p = 0.435 and 0.492. And r > 0: the twist is
absorbed at **zero action** by the twist-eating pair (h_0, h_1) = (i, j). "A domain wall costs
nothing" is exact here; the twisted sector is rare only by counting (3/23, 1/61). This corrects
row 922 Section 7.2 (failed by check 927): no unabsorbed wall is forced, and the size of p is a
ratio of numbers of flat connections, not a wall free energy.

Finite beta (ARGUED, a sound estimate, not proved). A local excitation costs e^(-6 beta) per link
for Q_8 (the nearest plaquette value is 0) and e^(-3 beta) for 2T (nearest value 1/2): 1e-6 and
1e-3 at beta = 2.3. The local corrections are the same around every flat background until a
cluster wraps the torus, so r(beta) = r(infinity)(1 + O(e^(-c beta L_min))) in the frozen phase.
The lane's window for "frozen" is GUIDE (row 838); 2T freezes near beta = 2.2 (recalled from the
1980 Monte Carlo literature, not re-read).

### 3.2 The two factors for a finite group

There is no gradient. The exact analogue (check 927 Section 8.1): the heat-bath form
D_hb(F) = sum over boundary links b of E_(w_e)[Var(F | the other boundary links)], the odd constant
lambda_odd^hb = inf over odd F of D_hb(F)/Var(F), and p/(1 - p) = Var_(w_e)(R_t) <=
D_hb(R_t)/lambda_odd^hb.

**Proposition F2 (PROVED at beta = infinity, sides at least 3).** D_hb is identically zero. So the
response factor D_hb(R_t) is 0, the gap factor lambda_odd^hb is 0, and p/(1 - p) is 10/13 or 30/31.
Proof. Under w_e at beta = infinity both slices are flat. A boundary link lies in a spatial
plaquette of its slice whose other three links are conditioned; flatness fixes it. QED

Finite beta (ARGUED). D_hb(F) is O(e^(-4 beta delta_G)) per link for a local F. For an odd F that
is stable under local excitations (the sign of the transverse average of the winding-line
characters) a change needs a positive fraction of the N parallel lines altered, so
lambda_odd^hb <= exp(-c beta N): tunnelling-small. A Peierls estimate for the two-slice marginal
would prove it; I have not written one. R_t is locked to the holonomy sectors in the same way, so
D_hb(R_t) is tunnelling-small too.

Verdict for the frozen groups: **the response factor cannot carry the failure** (it tends to 0, so
it meets every smallness target), and the gap factor carries all of it.

## 4. Verdict of Step A (step 4)

A proof through the odd-gap form supplies lambda_odd >= lambda_0 and FR_u <= eps <= 2 p_* lambda_0.
At the seed box lambda_0 <= 60 (if q >= 1/4) and so eps <= 0.024 at p_* = 2e-4.

| rival | p | response factor against eps = 0.024 | gap factor against lambda_0 |
|---|---|---|---|
| U(1), Model G, seed box | 1/2 - 1.4e-10 (PROVED < 3e-10 below 1/2) | FAILS: FR_u >= 20.8 (PROVED), a factor 870 or more | FAILS: lambda_odd <= 8.2e-9 (PROVED); a factor 7e9 at lambda_0 = 60; fails for every lambda_0 > L_1/N = 0.05 at every beta |
| U(1), Model G, cube a = L | at least 1/2 - 1.2e-5 at beta 2.3 | fails only for L below about 420 (FR_u <= 4 pi^2 beta^2/L against 2 p_* 3L, PROVED); PASSES above | FAILS at every size: lambda_odd <= 1/L against 3L |
| frozen Q_8, 2T, beta = infinity | 10/23, 30/61 (PROVED) | PASSES (D_hb = 0, PROVED) | FAILS (lambda_odd^hb = 0, PROVED) |

**Answers to the row's questions.**

1. *Which factor carries the U(1) failure?* At the seed box both do. The gap factor is the one
   that carries it at every size and every coupling (Proposition G4(i): lambda_odd(G) <= L_1/N
   always). The response factor fails for U(1) only in boxes below a size, and it does not fail at
   all for the frozen groups. So **the gap factor lambda_odd is the carrier in all three rivals**,
   and it is the factor Step B attacks.
2. *Does some factor fail for U(1)?* Yes. The odd-gap form passes the fact test; it is not the
   wrong target on this ground.
3. *Two warnings for the form.* (W-a) (FR) alone is not a valid crux: frozen groups and large U(1)
   boxes meet any (FR) target. A lane that proves "(FR) is small" has proved nothing a rival
   lacks. (W-b) Step (b) is where the form is empty for U(1) (it loses 1.4e10 there), while row 922
   showed that for SU(2) (FR) at the needed size is the flux half again. Both say: remove (FR) from
   the criterion. Section 5 does that.
4. *The mechanism (U(1)).* One collective coordinate: the toron Phi_1, the transverse average of
   the winding-line phase. It exists as a smooth coordinate because parallel winding lines differ
   by the magnetic flux between them, a single-valued real number when the group is abelian and
   there are no monopoles. Its gradient is small, |grad Phi_1|^2 = L_1/N, and J moves it by pi. The
   even law is a double well in psi (wells psi = 0 and pi, barrier weight y = e^(-pi^2/(8 tau)));
   R_t is the well indicator, a tanh across the barrier. Hence p -> 1/2, the gap is the tunnelling
   rate kappa mu_0, and the response is the pull pi/(2 tau) of the two nearest images.
5. *Shared mechanism with the glue half.* Row 929's file has no Step A at this commit. The carrier
   here is the k = 0 mode alone; the photons with k != 0 drop out of p, R_t, FR and lambda_odd
   exactly (Lemma G1). The glue half's U(1) failure is expected from the k != 0 thermal photons
   (ARGUED). So the two halves probably have different U(1) carriers; row 931 should check this
   against row 929's result.
6. *Frozen groups against U(1).* Different mechanisms, same factor: U(1) has a soft collective
   coordinate with a double well; the frozen groups have no dynamics between holonomy sectors.
   Both make the odd Poincare constant collapse. An SU(2) proof of the gap factor has to exclude
   both: no soft collective odd coordinate, and no frozen odd sector label.
