lead: anthropic/claude-opus-5-5/max laptop-agent
# Row 975, gap-ymcons-opus: ten approaches to the seed crux taken from the Yang-Mills construction

Author: Claude Opus 5.5 (max effort), brainstorm author, laptop agent. Date 2026-11-14.
Status: brainstorm. Nobody has checked it. Each mathematical statement carries PROVED (proof given here), ARGUED, or OPEN.
Credit: the construction is by Ethan Sussman and Levent Alpoge (text written with Claude and Codex). Their files are data.

## Target
The seed: S(a;B) = Tr(T_B^a)/lambda_0^a - 1 < 3/10 (Corollary O1(b)) on one fixed periodic box B,
SU(2) Wilson action, beta in [2.3, 2.6]. Lemma FL turns the seed into (SEED-FP) on cubes.
Acceptable end points: the seed at order one; or (LSI-traj-seed)_a of row 970; or a different input that reaches the seed by another route.

## Plan (one step per response; append after each)
1. Lane state: FINISH rows 960-974, gap-status-1113, gap-direction2-max, gap-avgcurv-max.
2. Construction part 1: block-spin steps, small/large field split, gauge fixing, class S, lem-correlation-decay.
3. Construction part 2: first passage (Lemma FL), hand-off, RP/OS, 3D work, monotone quantities.
4. Approaches 1-3 (items a-g each).
5. Approaches 4-6.
6. Approaches 7-8.
7. Approaches 9-10 and duplicate checks.
8. Ranking, top three, RESULT line.

## Working notes (appended step by step)

### Step 1 (done). Lane state, READ (pointers; no new claim)
Sources read: FINISH rows 960-975 (row text, `grep -nE '^\| (96|97)[0-9] \|'`); `library/gap-status-1113.md` sections 1, 5, 6;
`library/gap-direction2-max.md` sections 1, 2, 4, 7, 8; fact-test list in `library/gap-constraints-max.md` 1.4 (L60-75)
and FT-FK in `library/gap-pca-opus.md` L315-320.
- Objects (row 970, 1.2, quoting row 968). B periodic spatial box, L links, M = (S^3)^L. V(x) = -beta sum_p (1/2) tr x_p.
  T_0(x,w) = e^(-V(x)/2) e^(beta<x,w>) e^(-V(w)/2) (temporal gauge). Omega top eigenfunction. m(dw) = e^(-V/2) Omega dw is the
  boundary-slice law of the half-infinite cylinder. pi_theta = e^(<theta,w> - Lambda(theta)) m: tilted boundary law; the vacuum chain
  steps by pi_(beta x). J = two-slice vacuum law. nu_s = law of the bridge point.
- Consumer chain (row 970, 1.4): (TILT-COV-sup) -> (LSI-br)_s -> (HC-vac)_alpha -> X(2m+2;B) <= 72 beta |B| e^(-2 alpha m) -> seed on
  (a;(4a)^3) when alpha >= K_a, K_a = (C_beta + 3 log a)/(a - 2), K_30 = 0.811 (row 960) -> Theorem S. Needs m_G >= K_a (row 954).
- Row 970 verdicts: (TILT-COV-sup) NOT a port (CA-II 8.3 class S needs window (W), coercivity (Q) from the block constraint,
  smallness (P); all fail at seed scale, Lemma CLASS); supremum forms REFUTED at GUIDE level at beta 2.5-2.6 (Lemma SUB with frozen
  pi-flux slices, rows 950, 952). What stays: (LSI-traj-seed)_a (Lemma TRAJ: only bridge interpolations of P^k p_1(u,.)); Identity
  MM: D(mu_s|nu_s) = (1/2) int_0^c E_(J')|E_(J')[q~|phi_t] - E_J[q~|phi_t]|^2 dt (a mismatched-estimation identity). A3 = EXIT / HO.
- Status 1113: the seed splits (Lemma SPLIT, Corollary O1) into GLUE (S_ev <= 1/10) and (CORE) (Z^(v_12)/Z^0 >= 9/10 on (a,b,b,b),
  b >= 24a). Remark UNTW (row 895): every proved seed proves both halves or neither. Five walls W1-W5, shared assumptions SA1-SA6;
  SA1: the arena is the unit lattice at one order-one beta_W while the real object is first passage. Theorem HO: exact block steps past
  first passage landing in an explicit zone (EXIT) give the bare seed; normalised softening alone supplies none (row 861, check 877).
- Fact tests (gap-constraints-max 1.4). FT-U1: free photon and compact U(1) Coulomb must FAIL (glue log(1+S_ev) > 31 on the seed slab;
  flux p -> 1/2). FT-FROZEN: frozen Q_8, 2T must fail (S_ev >= 1/2). K7: mixed action exp(beta_F x + beta_A(4x^2-1)/3) with a
  first-order line, no seed at any size. SMALL-BOX: a fixed small box at large beta has no gap in units of its side. FT-FK: an argument
  acting only on the kinetic part fails FT-U1 and SMALL-BOX. FT-CEIL (worst-case forms): single-link 1/3, single-site Dobrushin 2/3,
  vertex blocks 0.775, background-uniform layer bounds false above 4 G_3 = 1.0109; averaged forms escape these.

### Step 2 (done). Construction part 1, READ (quotes are data; credit Sussman and Alpoge)
File abbreviations: O1400 = ~/ym4d-lead/sa1400/YM4_1400.tex (136,637 lines); CA-II = ~/ym4d-lead/sa/theorem_0_complete_account_raw_II.tex.
- F1. Hard-constraint block spin, exact image measure. O1400 L3641: "The transformation sends a complex Borel measure nu to its image
  T nu = M_* nu ... Wilson and Kadanoff introduced the block-spin transformations (T_t rho)(V) = int dU t(V,U) rho(U), with t >= 0,
  int dV t(V,U) = 1 ... the transformation here is the member of this family with a hard constraint." O1400 L4547: "The renormalisation
  transformations obey the semigroup law T^n nu = (M^n)_* nu ... Finite range does not survive ... Reflection positivity is required of the
  bare measure only". So every level carries the same total mass (the seed is one number at every level; row 837).
- F2. The block average exists only on a small-field domain. O1400 L3600-3620: M(U)(c) = exp(L^-4 sum log W_x) U[c] "on Dom(c) =
  {varpi_c < C^-1 L^-2}", "Off Dom(c) the map is given by ..." (a second rule). The approximate fluctuation test chi'_k (L3641) marks small fields.
- F3. No dilation, no fixed point. O1400 L4559: "a compact group admits no dilation. Hence x_k is the normalisation of the kinetic term ...
  there is no scaling transformation, no fixed point and no eigen-direction."
- F4. Coercivity from the constraint. O1400 L5445-5455 (flat precision gap): "With these operators the classical flat precision has a gap
  uniform in the torus volume and in the number of finer averaging levels." O1400 L122968ff: block Neumann form and "a uniform scalar
  Poincare inequality" for block means.
- F5. SU(2) quaternion structure. O1400 L4658: "In SU(2), a real combination of group elements close to one another is a positive number
  times a group element, and the map N is holomorphic." (U(1) in C has the same property, so it does not separate the two.)
- F6. Class S and its decay. CA-II L83837-83866 (items (i)-(vi): convex window K_x, density 1_K e^-Phi, Phi = (1/2)<y,Qy> + <h,y> - P(y),
  q_- 1 <= Q, ||P''|| <= varpi, coupling bound c(x,x'), (vi) "The conditional law ... is carried by the fixed set K_(S^c)"); Lemma 8.3
  lem-correlation-decay CA-II L83869-83900: under the Helffer-Sjostrand representation, |Cov(F,G)| <= (2/m) sum e^(-nu dist) ||d_x F|| ||d_x' G||,
  with the rate condition nu <= e nu_0 m/(4 K) (CA-II item (v)). Mechanism: coercivity m of the Helffer-Sjostrand operator divided by the
  weighted coupling sum K (a Combes-Thomas type bound). Row 970 Lemma CLASS: the seed-scale laws fail (W), (Q), (P).

### Step 3 (done). Construction part 2, READ (quotes are data; credit Sussman and Alpoge)
Further abbreviations: S500 = ~/ym4d-lead/sa/YM4_sketch_500.tex; Y3S = ~/ym4d-lead/sa/ym3/YM3_supplement.tex.
- F7. Positive history sums, averaged removal. O1400 L106666-106677: "estimate the error from exceptional runs without a uniform lower bound
  on the clean probability at every exterior field"; "One first sums the positive histories that represent the same physical event, and then
  normalizes their total mass. Conditioning each history separately generally gives different weights." L106821-106835: "The number p can be
  exponentially small although q(e) is zero on a set of exterior fields of positive measure ... the exceptional exteriors must be retained in
  the error estimate". Prop. "Averaged clean resampling" (L106875-106882): ||rho - nu_G||_TV <= p + lambda(G^c), with lambda(G_eta^c) <= p/(1-eta).
- F8. Scale forgetting. O1400 L80912-80916: "Geometric forgetting of old interactions is stronger still ... A small probability of retaining an
  old region can appear as a small factor in the bound on an analytic function. It does not in general permit the analytic input radius to grow".
- F9. One large-field zone, partial. O1400 L81179-81182: "The one-zone estimate must bound a complexly perturbed integral; rarity at a real
  centre alone does not suffice ... The result is partial."
- F10. Plateau and all-mirror RP. O1400 L125586-125590: "a consequence of translation invariance and reflection positivity in coordinate and
  diagonal directions. No infrared bound, mass gap, or differentiability of a pressure is assumed." Prop. "Uniform plateau bound" (L125630-125641):
  |nu(A* tau_y B) - Pl(A,B)| <= C[(r/n)^2 + (r/n)^3] N(A)^(1/2) N(B)^(1/2), "independent of the measure ... and any coupling".
  Prop. "All-mirror positivity of periodic states" L125126 (lane already has diagonal RP: row 963, CA-III L108556).
- F11. Marginal-flow first passage. O1400 L82552-82575: x_j = x_(j-1) - b_j, "An individual increment of the recursion is allowed to be
  negative", only |sum_(l=i+1)^j (b_l^0 - c_0)| <= C_0 is assumed.
- F12. Even-coupling symmetry. O1400 L56592-56601: "changing the sign of the fluctuation coupling can be compensated by changing the sign of every
  Gaussian variable. We use that exact symmetry ... It improves their intrinsic smallness by one power of the coupling."
- F13. Regulators by rank. O1400 L89036-89042: "The few averaging directions are controlled by rank, rather than by pretending that the averaging
  regulator is a scalar mass."
- F14. Dilation beyond first passage. S500 L23373-23383: "Cutoffs beyond first passage. The dilation identity ... S^T_(n;K,l,beta) = S^T_(n;K-q,L^q l,beta)".
  S500 L588-595: "A polynomial cluster estimate likewise gives no positive mass gap" (spectral measure E e^-E dE gives (1+t)^-2).
- F15. 3D box criterion. Y3S L35235-35300: e(l) = 2 log Z(l,2l,2l) - log Z(2l,2l,2l) <= x_0 <= 0.069 at one physical size implies a gap and
  area law; "e(2l) <= 12.9 e(l)^2 ... a small initial defect becomes exponentially small"; "Establishing the displayed box inequality at a
  physical scale is still the outstanding confinement step. The source's small-torus estimates can exclude it at small sides. A test at one
  cutoff proves a uniform criterion only when its explicit cutoff-comparison error fits inside the margin below the threshold." (Same engine
  shape as the lane's Theorem S; not new as a consumer.)
- F16. 3D latent heat and infrared bounds by two incommensurable frames. Y3S L27480-27483: J(beta) = O(beta^(-4-c)) from "a reflection-positive
  lower bound, comparison with finite tori and an oscillation estimate for two incommensurable blocking factors". Y3S L28481-28486: "Chessboard
  estimates turn control of the source pressure into bounds on correlations of distinct cube means ... at most linear spectral mass near zero.
  They exclude an atom at zero without giving a positive gap." Partner frame: log L/log L^ irrational (Y3S Def. C-365-2 (3)).
- F17. 3D RG chain as a coarse-to-fine Markov chain with log-concave kernels. Y3S Lemma C-367-7 (L32124-32150): "under sigma^K the sequence
  V_t,...,V_0 is a Markov chain from coarse to fine whose kernel at every W ... is the image under V_W of p_W"; (iv) p_W = e^(-Psi_W) dB with
  (1/4)gamma_r <= D^2 Psi_W <= Lambda_+, so Var, (1/2)Ent of p_W <= C_P (a_d^2/b) int Gamma_d, "not on K, k, W, l or b". Top law (iii):
  sup g <= e^(o_n) inf g. Mixing (Y3S L31856-31870): "the connected part of the coarse regular region gives a Poincare inequality, while its
  complement contributes a defect": Var(F) <= C_n E(F) + r_n osc(F)^2, r_n -> 0; "This proves the stated mixing without supplying a spectral
  gap uniform in volume."
- F18. 3D uniform gauge on a box. Y3S L32474-32482: cells "of side comparable to the inverse square root of the plaquette bound ... For SU(2), the
  required extensions can be constructed quantitatively on the unit sphere in the quaternions."
- F19. Background by Lagrange multipliers; Gribov-free small fields. O1400 L4547-4560 ("The minimiser HB is the one given by the method of
  Lagrange multipliers"; L4658 "Uniqueness holds among small A, so no Gribov ambiguity arises").
Reading of where the account stops (READ by row 970 and re-used, not re-read): CA-I L2556-2560 "No statement about the laws of the block
variables is a clause of the present theorem". At beta 2.3-2.6 on the unit lattice the bare theory is outside the account (S500 L23373: the
dilation identity needs beta >= g^-2 + B_sharp), so the model arena has no RG chain of the account's kind.
One exact identity used below (PROVED here, one line). On M, |x|^2 = |w|^2 = L, so e^(beta<x,w>) = e^(-beta L) E_(phi ~ N(0, beta Id))[e^(<phi,x> + <phi,w>)].
Hence J(dx,dw) = int nu(dphi) pi_phi(dx) pi_phi(dw), with nu(dphi) proportional to gamma_beta(dphi) e^(2 Lambda(phi)): J is a positive mixture of
PRODUCT laws (a positive history sum in the sense of F7, history = phi). Proof: for phi ~ N(0, beta Id), E[e^(<phi,y>)] = e^(beta|y|^2/2);
take y = x + w, so |y|^2 = 2L + 2<x,w>; insert into J = m(dx) e^(beta<x,w>) m(dw)/Z and use Fubini. QED. (This is the b = beta end of row 968's family J_(b,phi), RECALLED from row 970, 1.2.)

## The ten approaches
Conventions. P is the vacuum chain on gauge-invariant functions of one slice, reversible for pi = Omega^2 dx; its eigenvalues
are lambda_n/lambda_0 in [0,1] (T_B >= 0 by reflection positivity, RECALLED from the lane). S(a;B) = sum_(n>=1) (lambda_n/lambda_0)^a.
"Duplicate check" greps the five prior brainstorm files named in the brief (gap-brainstorm-max, gap-brainstorm2-max, gap-next3-max,
gap-constraints-max, gap-status-1113) and, where useful, other lane notes.

### Approach 1. ESC: the trace counts every metastable set once, so averaged methods need fast escape
(a) Feature. F7 and F8. O1400 L106826-106835: "The number p can be exponentially small although q(e) is zero on a set of exterior
fields of positive measure ... the exceptional exteriors must be retained in the error estimate; they do not disappear from a
conditional statement." O1400 L80913-80915: "Geometric forgetting of old interactions is stronger still ... A small probability of
retaining an old region ... does not in general permit the analytic input radius to grow". The account keeps rare exteriors in the
budget and pays for old regions by forgetting them.
(b) Statement.
Lemma META (PROVED here). For a gauge-invariant set A with pi(A) = p in (0,1) let r_A(a) = P_(pi(.|A))(x_a in A). Then
  S(a;B) >= (lambda_1/lambda_0)^a >= (r_A(a) - p)/(1 - p).
Proof. f = 1_A - p has pi(f) = 0, ||f||^2 = p(1-p), <f, P^a f> = p r_A(a) - p^2. P^a is self-adjoint and >= 0 on L^2(pi), with eigenvalue 1
on constants and top eigenvalue (lambda_1/lambda_0)^a on constants-perp. The variational principle gives (lambda_1/lambda_0)^a >= <f,P^a f>/||f||^2.
The sum over n >= 1 dominates its first term. QED.
Corollary ESC-nec (PROVED). If S(a;B) < 3/10 then r_A(a) < 3/10 + 7p/10 for every A. So every gauge-invariant set of probability at most
1/2 is left by time a with probability above 0.35 from its own conditional law. A metastable set of ANY probability adds about 1 to S.
Reading (ARGUED). The account's averaged estimate ||rho - nu_G||_TV <= p + lambda(G^c) controls expectations of bounded functions. The
seed is a trace, not such an expectation. So an averaged route must add a transience input for the sets it discards:
  (ESC)_a: for each set A in a named class of bad sets (for example an eps-neighbourhood of the gauge orbit of the layered pi-flux slice
  u_xy of rows 950, 952 on a block of side R), r_A(a/4) <= 1/2.
Route to the seed (OPEN): a Harris-type theorem with a local drift for the number of bad blocks, E[N_bad(x_1) | x_0] <= theta N_bad(x_0) + b,
theta < 1, plus local mixing on good configurations, plus the count of the hypercontractive chain (Proposition HC). ESC is necessary;
it is not sufficient: Cheeger's bound turns it into lambda_1 only, and the seed needs the count of all states.
(c) SU(2) property. Escape from a frozen high-action slice is driven by the spatial plaquettes against the temporal pinning beta<x,w>.
The configuration space is connected for every compact connected group, so continuity alone does not separate SU(2); the drift must
come from the spatial weight at order one. U(1) splits in two. (i) Nonzero-momentum photon modes do NOT violate ESC: for one Gaussian mode of
frequency w on (a;(4a)^3), w a >= pi/2, and A = {mode > 0} has r_A = 1/2 + arcsin(e^(-wa))/pi <= 0.567 < 0.65 (Sheppard's formula, RECALLED;
arithmetic here). (ii) The winding holonomy DOES: in the Coulomb phase the electric-flux sector n costs about n^2 e^2/(2b) (RECALLED
continuum formula; with e^2 = 1/beta of order 1 and b = 120 this is near 0.002 per unit time), so the set {winding holonomy angle in
(0, pi)} keeps r_A(a) near 1 and ESC fails. So ESC is U(1)-sensitive only through the flux sector (the lane's flux half); the U(1) failure
of the glue half is by the count of modes. ESC is a filter, not a route.
(d) Fact tests. Free photon, compact U(1): ESC fails through the winding holonomy (c)(ii) and holds for one-mode sets (c)(i):
consistent; ESC claims no sufficiency. Frozen Q_8, 2T: discrete degenerate vacua give r_A near 1, ESC fails, the seed fails: pass.
SMALL-BOX: the flat-connection valley of a small box at large beta is metastable, ESC fails: pass. K7: two coexisting phases are
metastable, ESC fails: pass. FT-FK: not a kinetic-only argument: pass. Ceilings: ESC is a supremum over SETS (forced by Lemma META),
not over tilts or boundary data; the tilt ceilings do not apply, but no form of the seed escapes the supremum over sets.
(e) Cheapest refutation test (GUIDE, for someone else; criteria fixed here). Half-infinite slab with the bottom slice frozen at u_xy
(rows 950, 952 code, `guide/lane952/`), long enough in time (at least 32 slices plus a buffer), beta 2.5 and 2.6, sides 8 to 12. Measure
the colour order parameter of the first-step electric field and the xy-plaquette action at steps k = 1, 2, 4, 8, 16, 30. Call a slice
"in A" if its xy-plaquette action is within 10 percent of the frozen value and its colour order is above half the step-1 value.
Criterion (Lemma META with p negligible): if at least 30 percent of runs are still in A at k = 30 = a, the seed on (30; 120^3) is refuted
at GUIDE level at that beta, and the box must grow. If at least 95 percent of runs leave A by k = 3, the ties of row 970 are transient
and harmless for the trace (support for Approaches 2 and the trajectory form). Control: start from a vacuum slice, same observables.
(f) Where it dies. Sufficiency: no box-local drift-plus-minorization theorem is known at order one (the local mixing on good sets is A3).
The test can kill the box choice; it cannot prove the seed.
(g) Duplicate check. `metastab|escape time|residence|transien`: no hit. `Lyapunov`: gap-status-1113 L311 (W2, "Does not block: ...
Lyapunov weights (row 899)"); gap-brainstorm-max L298, L368 (Furstenberg, unrelated). Partial match with the named W2 door "Lyapunov
weights", which had no supplier. New: Lemma META (each metastable set counts about once, whatever its probability), which names
transience as the exact extra input of every averaged route, and the escape test at u_xy.

### Approach 2. HIST-AVG: defective entropy contraction with an averaged discard of bad tilts
(a) Feature. F7, used on the exact mixture of Step 3 (J = int nu(dphi) pi_phi x pi_phi, histories = tilts). O1400 L106668-106671: "One
first sums the positive histories that represent the same physical event, and then normalizes their total mass. Conditioning each
history separately generally gives different weights." Prop. "Averaged clean resampling", O1400 L106875-106882: ||rho - nu_G||_TV <= p + lambda(G^c).
(b) Statement.
Lemma DEF (PROVED here, given Identity MM of row 970 7.2 as stated there). Let G_l be any measurable set of tilts for each link l, and
Delta_(t,l) = E_(J')[q~_l | phi_t] - E_J[q~_l | phi_t]. Then
  D(mu_s | nu_s) <= (1/2) int_0^c E_(J')[ sum_l 1{phi_t in G_l} |Delta_(t,l)|^2 ] dt + 2c (1/s + 1/s')^2 sup_t E_(J')[ #{l : phi_t not in G_l} ].
Proof. Split each link's term of Identity MM by 1_(G_l) + 1_(G_l^c). Since |x_l| = |w_l| = 1, |q~_l| <= 1/s + 1/s', so |Delta_(t,l)|^2 <= 4(1/s + 1/s')^2.
Integrate over t in [0,c]. QED. At the mid-slice s = s' = 1/(2 beta): c = 1/(4 beta), 1/s + 1/s' = 4 beta, so the defect is 8 beta per bad link
(18.4 at beta 2.3; my arithmetic).
Target (OPEN). (LSI-traj-def)_a: (LSI-traj)_s of row 970 7.1 on the good links only, with rate (1/2) int alpha_s ds >= K_a, plus an additive
defect 8 beta E[N_bad] per step. Iterated over the m steps of Proposition HC, the defect sums to 8 beta sum_k E_(u,k)[N_bad]. With ESC
(Approach 1) the sum is 8 beta x (expected bad-link residence of the started chain). For the seed it must stay O(1).
Budget (my arithmetic, ARGUED). Over the m = 14 steps of Proposition HC (2m + 2 near a = 30) the vacuum share of bad links must be at
most about 1/(8 beta |B| m) = 7.5e-10 on (30; 120^3) at beta 2.3 (|B| = 3 x 120^3 = 5.18e6 links; 18.4 x 5.18e6 x 14 = 1.34e9). So "bad" can
only mean large rare structures (frozen-flux blocks of side R whose energy cost grows with R; a chessboard bound is the natural tool),
and every typical order-one fluctuation must sit in the good set.
(c) SU(2) property. None in the bookkeeping (group-blind). SU(2) enters through the good-tilt local covariance and through the rarity and
transience of bad structures. U(1) breaks at the good tilts: the photon's soft modes are present at typical tilts, so the good-set
covariance fails with rho of order 1/b (row 970 A3 fact test).
(d) Fact tests. Free photon, compact U(1): no bad tilts, the good-set rate fails: pass. Frozen Q_8, 2T: no gradient form; nothing
claimed. SMALL-BOX: at large beta on a small box the typical tilts lie on the flat valley; the good-set bound must fail there; pass
only if stated above the confinement length. K7: the other phase is not rare (probability 1/2), so the defect is of order |B|: the route
fails, as it must: pass. FT-FK: acts on the full two-slice law: pass. Ceilings: an averaged form with an additive defect; it escapes
2/3, 0.775, 1.0109, but a worst-case proof inside the good set would meet them again.
(e) Cheapest refutation test (GUIDE). Sample typical bridge tilts phi_t under J (and under the chain started at u_xy, k = 1..8). In each
block of side 2, compute the top horizontal eigenvalue of Cov(x|y)/s^2 + Cov(w|y)/s'^2 against 1/c (row 968 7.3, second test, not yet run).
Criterion: call a block bad if it exceeds the threshold. If the bad-block fraction at vacuum-typical tilts is above 0.05 on sides 8 to 16 at
beta 2.3, bad is not rare, the additive defect cannot absorb it, and the route reduces entirely to A3. If it is below 1e-3 and falls with the
side, the bookkeeping is worth a proof.
(f) Where it dies. At the good-tilt local covariance (A3) and at the locality of the defect: a posterior mean at a good link depends on
bad tilts nearby, so the clean split of Lemma DEF needs a local recovery estimate that nobody has.
(g) Duplicate check. `typical tilt|bad tilt` and `weak Poincar|Rothaus|defective`: no hit. Lane: row 970 7.3 (the ARGUED "small share"),
row 970 A2 and A3, row 968 (ABS-flow); status L311 with check 852 ("conditions only on surviving path sums") matches the spirit (sum,
then normalise). New: Lemma DEF, a proved additive form that replaces the unproved "small share", with the explicit price 8 beta per bad
link and the rarity budget near 7.5e-10 per link.

### Approach 3. MOS-EXIT: weak mixing at the block scale makes the soft block image local (a supplier for PIN-MIX)
(a) Feature. F1, O1400 L3641: "Wilson and Kadanoff introduced the block-spin transformations (T_t rho)(V) = int dU t(V,U) rho(U), with
t >= 0, int dV t(V,U) = 1 and t(V^(u|coarse), U^u) = t(V,U); the transformation here is the member of this family with a hard
constraint." CA-II class S item (vi), L83866: the conditional law "is carried by the fixed set K_(S^c)" (the class is closed under
conditioning). Y3S Lemma C-367-7: the chain V_t,...,V_0 "is a Markov chain from coarse to fine". Lane: row 861 (gap-exit-max): a soft
exact step lands the per-link size for free (Proposition FREE); the crux is locality of the landed action, PIN-MIX.
(b) Statement. Let t_a be a soft gauge-covariant Wilson-Kadanoff kernel at block side l with noise a, and nu_l = T_(t_a) mu the image.
  (WM)_(l,w): for every gauge-invariant F of the links of a block Q of side l and two exterior data eta, eta' outside the collar of width w,
  |mu(F | eta) - mu(F | eta')| <= C e^(-w/xi) ||F||_inf, with xi below w/4.
  Target (OPEN): (WM)_(l,w) with l >= 4w and the soft kernel imply PIN-MIX of row 861 at noise a, hence the explicit zone of Theorem HO,
  hence the bare seed (Theorem HO, check 850 after correction).
Mechanism (RECALLED: Martinelli, Olivieri, Schonmann, CMP 165 (1994) 33): in d = 2, weak mixing in squares implies that the block image
satisfies a Dobrushin-Shlosman finite-volume condition, hence strong mixing. The proof uses planarity. In d >= 3 the implication is not
available in general because boundary layers can order while the bulk does not (RECALLED). The lane's GUIDE has exactly this: the
boundary layer at a frozen slice orders at beta 2.5-2.6 (rows 950, 952, 970 7a). So the uniform-in-eta form of (WM) is at risk in the
upper window, and a typical-eta form (Cesi-Maes-Martinelli, Griffiths regime; row 936 explored typical cuts) is the version to aim at.
(c) SU(2) property. (WM) with exponential collar decay is the confinement input; it must fail for U(1). It does: the Coulomb photon gives
boundary influence decaying as a power of w, so C e^(-w/xi) fails as w grows. Note: at ONE fixed (l, w) a power law can be small, so the
statement must carry the exponential form or a numerical threshold tied to the zone; a fixed-size "influence below eps_0" alone could
pass U(1).
(d) Fact tests. Free photon, compact U(1): exponential form fails: pass. Frozen Q_8, 2T: ordered, boundary selects the vacuum, (WM)
fails: pass. SMALL-BOX: stated at l of several correlation lengths: pass. K7: boundary selects the phase at coexistence: pass. FT-FK:
full measure: pass. Ceilings: the uniform-in-eta form is worst-case; by W1-t (row 899, check 901) a background-uniform slab bound of
thickness w is false where the flat Dirichlet slab orders, so w must exceed that critical thickness (GUIDE: near the deconfinement length).
The typical-eta form is averaged and escapes the ceilings.
(e) Cheapest refutation test. Hand: read the MOS proof for the planarity step and decide whether a 4D multiscale substitute
(bad-box percolation with typical boundaries) exists in the literature (one Opus high reading row). GUIDE: boxes of side l = 2w + 4 with
collar data flat, vacuum-typical, and u_xy; measure the central plaquette and a central small Wilson loop. Criterion: at beta 2.3, w = 8,
the spread over the three boundary types must be below 0.01; at beta 2.6 the u_xy boundary is expected to fail (row 952); a failure at a
vacuum-typical boundary refutes the typical form at that w.
(f) Where it dies. (WM) at order one is itself an unproved mixing statement; the order-one input moves there. The d = 4 version of
"weak implies strong" is missing, and the block image may fail to be Gibbsian (van Enter-Fernandez-Sokal, RECALLED).
(g) Duplicate check. `weak mixing|Martinelli|Olivieri`: no hit in the five files. `EXIT`: gap-constraints-max L250, L477, L528 (EXIT
as an open node). Lane: gap-exit-max (row 861, PIN-MIX is the crux), gap-ds-gauge (row 691, Theorem W: weak mixing FROM a Hamming
condition, the opposite direction), gap-blockcrit-opus (vertex blocks, 0.775 cap), gap-cuttyp-max (row 936, typical cuts, cites
Cesi-Maes-Martinelli). MATCH with EXIT/PIN-MIX as the target. New: the MOS mechanism as the supplier of PIN-MIX, and the identification
of its d >= 3 obstruction with the lane's frozen-slice boundary ordering.

### Approach 4. LANGEVIN-CHAIN: the 4D Langevin log-Sobolev inequality on the cylinder gives (LSI-J) by projection; the 3D chain reduces it to a top law
(a) Feature. F17. Y3S Lemma C-367-7 (ii), (iv) (L32124-32150): "under sigma^K the sequence V_t,...,V_0 is a Markov chain from coarse to
fine whose kernel at every W ... is the image under V_W of p_W"; "p_W = e^(-Psi_W) dB with ... (1/4) gamma_r <= D^2 Psi_W <= Lambda_+", so Var and
(1/2)Ent of p_W are at most C_P (a_d^2/b) int Gamma_d, with C_P "not on K, k, W, l or b". Y3S L31856-31870: "the connected part of the coarse
regular region gives a Poincare inequality, while its complement contributes a defect"; "This proves the stated mixing without supplying
a spectral gap uniform in volume." Bounded grep (this step): CA-I, CA-II, CA-III contain no "Langevin" and no coarse-to-fine chain
statement; O1400 has one Langevin passage (L97170-97177, a synchronous coupling: "No convexity of H_1 is needed for this comparison").
So the 3D machinery has no 4D counterpart in the account.
(b) Statement.
Lemma PUSH (PROVED here). If a law mu satisfies Ent_mu(f^2) <= (2/rho) int |grad f|^2 dmu and T is 1-Lipschitz, then T_* mu satisfies the same
inequality with the same rho. Proof: apply it to f = g o T; |grad(g o T)| <= |grad g| o T. QED.
Corollary (PROVED given the lane's definitions). Let (CYL-LSI)_rho be the log-Sobolev inequality, on gauge-invariant functions, of the
Wilson measure on the cylinder B x Z in temporal gauge (the slice chain (x_t) as a one-dimensional Gibbs measure of spins x_t in M), with
the product round metric, uniformly in the time length. The two-slice law J is the law of (x_0, x_1), a coordinate projection, which is
1-Lipschitz and commutes with the residual gauge action. Apply Lemma PUSH on the time-periodic box of length T and let T grow: on a fixed
box the two-slice marginal converges to J because T_B has a simple top eigenvalue (Jentzsch, RECALLED), and the inequality passes to the
weak limit for smooth f. So (CYL-LSI)_rho gives alpha_J >= rho, and rho >= 2 beta K_a gives (LSI-J-seed)_a and,
through Theorem BR and Corollary BR-J, the seed.
Template (ARGUED). At first-passage data a 4D port of Y3S C-367-7/8 would split (CYL-LSI) by the chain rule of entropy into uniform
conditional inequalities (fine given coarse, by convexity) and the inequality of the top law. So (SEED-FP) in this form needs
(TOP-LSI): the top block law on the seed box satisfies LSI at the needed rate in the transported Dirichlet form. Y3S (iii) gives only
sup g <= e^(o_n) inf g with o_n of the order of the volume, so Holley-Stroock gives a volume-dependent constant, as SA say.
(TOP-LSI) is implied by EXIT (a strong-coupling top law mixes by Dobrushin-type arguments), so it is no stronger than EXIT (ARGUED).
(c) SU(2) property. Only in (TOP-LSI) or, in the model arena, in (CYL-LSI) itself. U(1): no first passage (the coupling falls in the
infrared), and (CYL-LSI) fails through the photon and the winding holonomy.
(d) Fact tests. Free photon, compact U(1): (CYL-LSI) fails (soft modes): pass. Frozen Q_8, 2T: no gradient; nothing claimed. SMALL-BOX:
on a small box at large beta the flat valley is slow, (CYL-LSI) fails at the needed rate: pass. K7: coexistence kills any LSI: pass.
FT-FK: full measure: pass. Ceilings: the one-dimensional Otto-Reznikoff criterion (RECALLED) needs the conditional slice LSI constant
rho_0 to exceed 2 beta at EVERY tilt h_l = beta|x_(t-1,l) + x_(t+1,l)|. Hand bound (PROVED): for the one-link law e^(h<mu,y>) on S^3 and
f = <e,y> with e orthogonal to mu, L f = -(3 + h<mu,y>) f, so the gap is at most 3 + h. At tilts with h_l near 0 (x_(t+1,l) near -x_(t-1,l)),
and without staples, this is 3 < 2 beta = 4.6. With staples the bound changes, so the worst-case failure is ARGUED, not PROVED. The worst-case
form meets a ceiling of the same kind as 2/3; averaged forms escape it.
(e) Cheapest refutation test. Hand (an hour): the staple-included worst case of the conditional slice LSI against 2 beta; if it fails,
the worst-case (CYL-LSI) route is dead. GUIDE: on long periodic cylinders (time 64, sides 4 to 8) at beta 2.3, the Langevin (or heat-bath)
integrated autocorrelation of the slowest gauge-invariant observable (smeared plaquette, smallest Polyakov-type winding loop); the
criterion is a relaxation rate below 2 beta K_a in the same time normalisation, stable under a doubling of the side: then (CYL-LSI) at
that rate is refuted. Calibrate the normalisation on the free photon first.
(f) Where it dies. (CYL-LSI) is stronger than (LSI-J); in the model arena it is a new order-one statement. At first passage the account has
no 4D chain statement to port from, and (TOP-LSI) is the rest of the flow.
(g) Duplicate check. `Langevin`: gap-brainstorm2-max L223 (orbit-space curvature, Bochner), L257, L382 (Witten Laplacian G2), L47
(row 845, annealed block heat-bath). `push-forward|Lipschitz map|Otto-Reznikoff|Zegarlinski`: no hit. Match: the Langevin gap appears in
the lane only as a curvature target (G2, idea 18). New: Lemma PUSH, which makes the 4D cylinder inequality a sufficient input for
(LSI-J), and the identification of SA's 3D chain (Y3S C-367-7/8) as the template, with the bounded finding that the 4D account has none.

### Approach 5. SVD-CVAR: the seed is the trace of a channel; the gap is a lower bound on posterior variance
(a) Feature. F7 (positive history sums) and F17 (coarse-to-fine Markov kernels). Y3S Lemma C-367-7 (ii): "the images of the p_W under the
V_W form a regular conditional law"; the account handles a law through its conditional kernels. Here the latent variable is the HS tilt
phi of Step 3, and x and w are conditionally independent given phi.
(b) Statement.
Lemma SVD (PROVED here). Let Gamma(dx,dphi) = nu(dphi) pi_phi(dx), and P* : L^2(pi) -> L^2(nu), (P* f)(phi) = E_(pi_phi) f, with adjoint P. Then the
vacuum chain operator is P P* on L^2(pi), pi = Omega^2 dx. So lambda_n/lambda_0 = sigma_n^2, the squared canonical correlations of (x, phi), and
  S(a;B) = sum_(n>=1) sigma_n^(2a),   1 - lambda_1/lambda_0 = inf_(f perp 1) E_nu[Var_(pi_phi) f] / Var_pi f.
Proof. From J = int nu pi_phi x pi_phi: E_J[f(x) g(w)] = E_nu[(P* f)(P* g)] = <f, P P* g>_pi, and E_J[g(w) | x] is the kernel of P P*. The x-marginal
of Gamma is pi. For f perp 1, <f, P P* f> = ||P* f||^2 = Var_nu(P* f) = Var_pi f - E_nu Var_(pi_phi) f (total variance). QED.
Lemma VOL (PROVED). S(a;B) <= (lambda_1/lambda_0)^(a-1) S(1;B), and S(1;B) = sum_(n>=1) sigma_n^2 = Tr T_B/lambda_0 - 1. Proof: each term
sigma_n^(2a) <= sigma_1^(2(a-1)) sigma_n^2. QED. Reading (ARGUED): log S(1;B) is extensive (the time-1 periodic box is a high-temperature
system), so a gap bound alone reaches the seed only if (a-1) m_G is of order |B|. The count needs hypercontractivity; this is the exact
reason behind row 954 (m_G >= K_a is necessary, not sufficient).
Target (OPEN). (CVAR)_gamma: E_nu[Var_(pi_phi) f] >= gamma Var_pi f for all gauge-invariant f perp 1 ("the tilt never pins the slice"); it is
equivalent to m_G >= -log(1 - gamma). It is a LOWER bound on posterior variance, the opposite direction to (TILT-COV-sup).
Bridge (ARGUED; the van Trees inequality is RECALLED). For an eigenfunction psi of the pi-Langevin generator with eigenvalue kappa, van Trees
with v = grad psi gives Bayes risk >= kappa Var psi/(c_I + kappa), c_I a bound on the channel Fisher information. So (CVAR) follows from the
Poincare constant of the vacuum slice law Omega^2, the Hamiltonian-limit gap (ideas 26, G9 of the prior brainstorms).
(c) SU(2) property. Only through the slice Poincare constant. U(1): the photon's low modes are pinned by the tilt (sigma_1 near 1).
(d) Fact tests. All pass trivially for the identities (they hold for every model). For (CVAR): photon, U(1), Q_8, 2T, SMALL-BOX, K7 all
fail it, as they must, since it is the gap. FT-FK: the channel uses m, which carries the magnetic weight: pass. Ceilings: none apply
to the identity; any worst-case proof of the slice Poincare constant meets them.
(e) Cheapest refutation test. Hand: the free photon, where van Trees is tight for linear psi, calibrates c_I. GUIDE: on sides 4 to 8 at beta
2.3, sample (x, w) from J, phi = beta(x + w) + sqrt(beta) xi, then resample x from pi_phi (slab with a tilted boundary); estimate
E_nu Var_(pi_phi)(plaquette)/Var(plaquette). It must be at least 1 - e^(-m_G) for the slowest mode; a value below 1 - e^(-K_a) = 0.556 at
a = 30 (my arithmetic) refutes the box choice at GUIDE level.
(f) Where it dies. At once as a route to the seed, by Lemma VOL, unless joined to hypercontractivity; as a route to the gap it is the
slice Poincare constant, already a lane target.
(g) Duplicate check. `canonical correlation|maximal correlation|total variance|van Trees|Cramer`: no hit in the five files. Lane-wide
14 files mention maximal correlation (not read here). Match in substance: ideas 3, 26 and G9 (the gap as the Dirichlet form of Omega^2).
New: Lemma SVD (exact channel form of the seed), Lemma VOL (the volume obstruction for any route that uses the gap alone), and the anti-concentration
direction.

### Approach 6. ANALYTIC-TILT: a zero-free complex polydisc around typical tilts gives local covariance bounds by Cauchy
(a) Feature. CA-II class S, item (iii) note (L83851-83853): "In the application, P is holomorphic on a complex tube containing K^+, by the
localisation and nesting properties established for it. Cauchy's estimates on the remaining margin then bound every derivative of P".
F9, O1400 L81180: "The one-zone estimate must bound a complexly perturbed integral; rarity at a real centre alone does not suffice."
The account gets derivative bounds from analyticity on complex tubes, not from convexity.
(b) Statement. Z(phi) = int e^(<phi,x>) m(dx) is entire on C^N, so Lambda = log Z is analytic off its zero set.
  (LY-loc)_(r,C): for vacuum-typical real phi_0 and every psi supported on a block Q with |psi_l| <= r, Z(phi_0 + i psi) != 0 and
  |Lambda(phi_0 + i psi) - Lambda(phi_0) - i<psi, grad Lambda(phi_0)>| <= C|Q|.
  Then by Cauchy (one complex variable along z, PROVED given (LY-loc)): Var_(pi_(phi_0))(<z,x>) <= 2C|Q| |z|_inf^2 / r^2 for z supported on Q.
  That is a local (TILT-COV) at typical tilts. Decay between blocks needs a cluster form of the zero-free region (Dobrushin-Shlosman
  complete analyticity, RECALLED: equivalent to strong mixing).
One-link computation (PROVED, given the RECALLED formula int_(S^3) e^(<phi,y>) dsigma(y) = 2 I_1(r)/r with r^2 = phi.phi, and that the zeros of
I_1(r)/r are at r = +- i j_(1,k)). For phi = phi_0 + i psi, phi.phi = |phi_0|^2 - |psi|^2 + 2i<phi_0,psi>; a zero needs <phi_0,psi> = 0 and
|psi|^2 = |phi_0|^2 + j_(1,k)^2. So one link is zero-free on |psi| < (|phi_0|^2 + j_(1,1)^2)^(1/2), j_(1,1) = 3.8317: radius at least 3.83 at
every real tilt. The mean tilt beta(x_l + w_l) has norm near 1.8 beta = 4.1 (from <x,w> near 0.6, row 968's GUIDE plaquette); with the noise of
variance beta per coordinate a typical |phi_l| is near (4.1^2 + 4 beta)^(1/2) = 5.1. The radius is then about 5.6 to 6.4 (my arithmetic). The interacting law m
shrinks it; by how much at beta 2.3 is OPEN.
(c) SU(2) property. The one-link radius uses the S^3 measure (Bessel I_1); the U(1) analogue has I_0 with radius j_(0,1) = 2.405 (RECALLED),
so the one-link step does not separate the groups. Separation must come from the interacting law: for the U(1) photon the low-mode
covariance at typical tilts grows like b^2, so by Cauchy the radius in that direction shrinks like 1/b: (LY-loc) fails for U(1), as needed.
(d) Fact tests. Photon, U(1): fails through the low modes: pass. Frozen Q_8, 2T: no continuous tilt; nothing claimed. SMALL-BOX: at
large beta the flat valley gives large covariance in valley directions, so the radius shrinks: pass if stated above the confinement
length. K7: at coexistence Lee-Yang zeros pinch the real axis: pass. FT-FK: m carries the magnetic weight: pass. Ceilings: a cluster
expansion that proves (LY-loc) uniformly over tilts is worst-case and meets the ceilings (single-plaquette zero-freeness reached only
1.0136 in row 870's setting, gap-brainstorm2-max L130); the typical-tilt form is averaged.
(e) Cheapest refutation test. The Cauchy bound turns any measured covariance into an upper bound on the radius: r^2 <= 2C|Q| |z|^2/Var. So
the GUIDE of Approach 2(e) (covariances at typical tilts, block side 2) refutes (LY-loc) with r >= 1 if it finds a block variance above
2C|Q| at typical tilts with C the measured free-energy oscillation. Hand: the two-link and one-plaquette zero-free radius at beta 2.3,
to see how fast the interacting radius falls below 1.
(f) Where it dies. No Lee-Yang theorem is known for the SU(2) boundary law: the plaquette weight is a four-linear form in quaternions,
not of Lieb-Sokal ferromagnetic type (RECALLED), so the zero-free region must be proved by expansion, which is worst-case.
(g) Duplicate check. `Lee-Yang|zero-free|complete analyticity|Cauchy estimate`: gap-brainstorm2-max L81, L130, L151, L193, L209 (ideas 7
and 40: zeros of the centre marker polynomial and of the edge polynomial; HA). Different object: those are zeros in a twist or spin
weight; here the zeros are in the linear tilt of the boundary law, which is the variable of Identity MM. New: the tilt-plane form, the
one-link radius (|phi_0|^2 + j_(1,1)^2)^(1/2), and the Cauchy link to the GUIDE covariances.

### Approach 7. PLATEAU-BOOT: bootstrap the coupling-free plateau bound to exponential decay (recorded as a fast death)
(a) Feature. F10. O1400 L125586-125590: the plateau estimate "is a consequence of translation invariance and reflection positivity in
coordinate and diagonal directions. No infrared bound, mass gap, or differentiability of a pressure is assumed." Prop. "Uniform plateau
bound", O1400 L125630-125641: |nu(A* tau_y B) - Pl_nu(A,B)| <= C[(r/n)^2 + (r/n)^3] N(A)^(1/2) N(B)^(1/2), "independent of the measure, the
support size, and any coupling". S500 L588-595: "A polynomial cluster estimate likewise gives no positive mass gap" (spectral measure
E e^(-E) dE gives (1 + t)^(-2)).
(b) Statement. A bootstrap (SL-gauge): if for ONE box Q_n the boundary sum of a gauge-invariant correlation is below 1, exponential decay
follows at all distances (a Simon-Lieb inequality for SU(2) Wilson). OPEN, and no such inequality is known for non-abelian gauge theories
(RECALLED: Simon-Lieb uses Griffiths-Lebowitz-type correlation inequalities).
Lemma U1-PASS (PROVED, given the RECALLED decay |y|^(-4) of the free photon's field-strength two-point function in 4D). (i) Every clustering
input of power p <= 4 for local gauge-invariant observables holds for the free photon, which fails the seed. So no bootstrap whose only
model input is such clustering reaches the seed; the bootstrap inequality itself must be SU(2)-specific. (ii) With the plateau's power
p = 2, the 4D boundary sum over |dQ_n|, of order n^3 sites, of (r/n)^2 is of order r^2 n, which grows: the Simon-Lieb step fails even on the
input as given. Proof of (ii): arithmetic. QED.
(c) SU(2) property. None in the input (coupling-free and group-blind by construction); it would have to be in (SL-gauge). U(1) passes the
input; that is the death.
(d) Fact tests. Free photon, compact U(1): satisfy the input, so the route fails FT-U1 unless (SL-gauge) carries the group: recorded.
Frozen Q_8, 2T and K7: the plateau holds for ordered and coexisting states too (Pl_nu is not a product there): the input is blind. SMALL-BOX:
not applicable. FT-FK: not applicable. Ceilings: none (coupling-free), and no content either.
(e) Cheapest refutation test. Done above by arithmetic: (ii) kills the bootstrap at p = 2; (i) kills any p <= 4.
(f) Where it dies. Immediately, as a route. Its use is as a filter: a lane statement that follows from RP and translation invariance
alone cannot be the order-one input (consistent with row 910's finding that RP, chessboard and axis exchange survive direct sums).
(g) Duplicate check. `Simon.Lieb` (any hyphen): gap-brainstorm-max L323 (idea 38, Simon-Lieb given SO(3)), L340 (idea 52, Nishimori
line), L560, L574 (scores "thin"); gap-next3-max L319 (GKS-C). Match. New: SA's coupling-free plateau as the input and the two PROVED
arithmetic facts that kill it.

### Approach 8. TWO-FRAME: incommensurable blocking factors against the first-order alternative of Theorem CRIT
(a) Feature. F16. Y3S L27480-27483: the 3D latent heat J(beta) = O(beta^(-4-c)) from "a reflection-positive lower bound, comparison with finite
tori and an oscillation estimate for two incommensurable blocking factors". Y3S L28481-28486: "Comparing two blocking factors with
incommensurable logarithms excludes concentration of the pressure response ... They exclude an atom at zero without giving a positive gap."
Y3S Def. C-365-2 (3): a partner frame has log L/log L^ irrational.
(b) Statement. Theorem CRIT of row 708 (gap-mid-max 5.1, READ): if beta*(1/25) is finite, every cube of ratio 4 has S >= 1/25 at beta*, and
the seed box diverges as beta rises to beta*; so beta* is a first-order point or a point of infinite correlation length.
  (NOLH): the infinite-volume plaquette mean of 4D SU(2) Wilson is continuous in beta on (0, infinity).
(NOLH) removes the first-order alternative at beta*. The 3D proof runs the two frames along the account's flow, so it reaches only
couplings above the first-passage threshold (ARGUED from the quoted setup; the frames are built from first-passage data, Y3S Def.
C-365-2 (2)). At an order-one beta* there is no frame. And (NOLH) leaves the continuous alternative of Theorem CRIT (e).
(c) SU(2) property. The frames exist only where asymptotic freedom drives the flow; U(1) has no first passage. As a statement, (NOLH) is
false for 4D compact U(1), whose Coulomb transition near beta 1.01 is weakly first order (RECALLED): good separation in the statement,
but the method is not available where it is needed.
(d) Fact tests. Compact U(1): (NOLH) false (first order): pass for the statement. Frozen Q_8, 2T: finite groups have first-order
transitions: pass. K7: the mixed action has a first-order line: pass. SMALL-BOX, FT-FK: not applicable (an infinite-volume statement).
Ceilings: not a worst-case method.
(e) Cheapest refutation test. Reading (one hour): Y3S L27480-28400, to confirm that the oscillation estimate needs the frames only at
beta above the first-passage threshold. If so, the route cannot reach an order-one beta*; stop.
(f) Where it dies. At order-one beta* (no frames), and because (NOLH) alone does not exclude a continuous transition.
(g) Duplicate check. `incommensur`: no hit in the lane library (0 files). `latent heat`: no hit in the five files (lane: gap-vacsub-max,
prior/gap-tests-lit). `first-order|first order`: K7 and its uses (gap-brainstorm2-max L463, L465; gap-next3-max L514). New: SA's
two-frame oscillation mechanism, mapped onto the dichotomy of Theorem CRIT.

### Approach 9. ENTROPY-DRIFT: the seed is a Renyi-2 entropy; seek first passage of it along doublings with a drift on average
(a) Feature. F11, O1400 L82552-82575: for the coupling recursion x_j = x_(j-1) - b_j, "An individual increment of the recursion is allowed to be
negative", with only |sum_(l=i+1)^j (b_l^0 - c_0)| <= C_0 assumed. F15, Y3S L35238-35240 and L35276-35281: e(l) = 2 log Z(l,2l,2l) - log Z(2l,2l,2l)
and "e(2l) <= 12.9 e(l)^2 ... a small initial defect becomes exponentially small in the linear size".
(b) Statement.
Lemma RENYI (PROVED here). Let rho_t = T^t/Tr T^t on a fixed spatial box. Then -log Tr rho_t^2 = 2 log Tr T^t - log Tr T^(2t) = S_2(rho_t), the
Renyi-2 entropy. So SA's 3D defect is e(l) = S_2(rho_l) for the section (2l, 2l); and in 4D, S_2(rho_a) = 2 log(1 + S(a;B)) - log(1 + S(2a;B)).
With x_n = (lambda_n/lambda_0)^a in [0,1], S(2a) = sum x_n^2 <= min(S(a), S(a)^2). If S(a) >= 1 then S_2 >= log(1 + S(a)) >= log 2 = 0.693.
If S(a) <= 1 then S_2 >= f(S(a)) with f(S) = 2 log(1+S) - log(1+S^2), and f' = 2(1 - S)/((1+S)(1+S^2)) > 0 on [0,1). Also S_2 <= 2 log(1 + S(a)).
So S_2(rho_a) < f(3/10) = 0.439 implies S(a;B) < 3/10 (my arithmetic: 0.5247 - 0.0862 = 0.4386). QED.
Target (OPEN). (DRIFT)_c: along dyadic boxes B_k = (2^k a_0; (4 2^k a_0)^3), S_2 at level k+1 is at most S_2 at level k minus c whenever it is at least
0.439, uniformly in the cutoff, allowing negative increments with cumulative error at most C_0 (the marginal-flow form). Then first passage
below 0.439 happens within (S_2^(0) + C_0)/c doublings, and the seed holds at a box of bounded size.
Calibration (PROVED, free photon). A harmonic mode of frequency w at inverse temperature a has Tr rho^2 = (1-q)/(1+q), q = e^(-wa), so
S_2 = log((1+q)/(1-q)). On (a;(4a)^3) the first shell has wa = pi/2 (q = 0.208) and 12 modes (6 momenta, 2 polarisations): S_2 >= 12 x 0.422 = 5.06,
more than 11 times the threshold 0.439, at every large a (scale invariance). So the photon fails (DRIFT) by staying constant.
(c) SU(2) property. Asymptotic freedom at the small boxes and the absence of an infrared fixed point. U(1) breaks: its infrared limit is the
free photon, a fixed point with S_2 constant near 5 or more on this shape.
(d) Fact tests. Free photon, compact U(1): constant S_2 >= 5.06: (DRIFT) false: pass. Frozen Q_8, 2T: S_2 tends to log(number of vacua) > 0:
pass. SMALL-BOX: the sequence starts in the ultraviolet where S_2 is large (free gluons and the flat valley): consistent. K7: S_2 tends to
log 2 at coexistence: pass. FT-FK: not applicable. Ceilings: not a worst-case method.
(e) Cheapest refutation test. Hand: done for the photon (above). GUIDE: S_2 = log Z(t)^2/Z(2t) on dyadic boxes at beta 2.3 (time 2, 4, 8; side
8, 16, 32) by thermodynamic integration or the snake method; criterion: a rise, or a plateau above 0.439 over two doublings, refutes (DRIFT)
at that beta at GUIDE level. Expected (ARGUED): SU(2) passes, since its spectrum is gapped; the test mostly calibrates c.
(f) Where it dies. There is no mechanism for the drift. The entropic monotones of continuum QFT (the 4D a-theorem of Komargodski-Schwimmer,
and the strong-subadditivity proofs of Casini-Teste-Torroba, RECALLED) concern vacuum entanglement of regions of one state, not thermal
Renyi entropies of different boxes; and a monotone that is constant at fixed points gives no drift by itself. (DRIFT) is the confinement
statement in entropy units.
(g) Duplicate check. `Renyi` (any accent): gap-status-1113 L69 (row 839, "Lemma Z'' (Renyi telescoping)", a different use). `monoton`:
gap-brainstorm-max L325 (idea 40, "induction on scales in which each step holds for a structural reason (a monotone quantity)") and
L402 (idea 29, "a monotone in the box size"). Match with idea 40. New: Lemma RENYI (SA's 3D defect and the 4D seed are Renyi-2 entropies,
with the exact threshold 0.439), the marginal-flow (average) form of the drift, and the photon calibration 5.06.

### Approach 10. CUTOFF-COMPARE: a seed at one cutoff, transported by SA's comparison of consecutive cutoffs (recorded as a bridge that fails)
(a) Feature. Y3S L305-312: "The new estimate concerns the relation between the measures at K and K+1. Bounds on each measure separately
would only provide compactness. The comparison instead evaluates their insertions over one block field at a common depth. This introduces
three errors: replacing each insertion by its value at a background, comparing the two background values, and comparing the two laws of
the block field." Y3S L35298-35301: "A test at one cutoff proves a uniform criterion only when its explicit cutoff-comparison error fits
inside the margin below the threshold." S500 L23373-23383 (dilation identity beyond first passage).
(b) Statement. (ONE-CUT)_eta: (SEED-L) holds at one cutoff K_1 with margin eta. (CC): sum over K >= K_1 of |Phi_L(K+1) - Phi_L(K)| < eta, with
Phi_L = L^4 log Z(l) - log Z(L l). Then (SEED-L) holds at every K >= K_1, and Lemma FL gives (SEED-FP). PROVED (telescoping), given both.
Why it fails (ARGUED from the quoted text). SA's comparison controls normalised insertions over one block field. Phi_L is a difference of
unnormalised log partition functions of two tori; it is not an insertion, and it needs precision o(1) in quantities of size l^4. The
account controls the last integral only up to e^(O(l^4)) (row 837), and Y3S's "Stability at a fixed label" (L26610-26625) bounds
|E_1 l_1^(-3) - E_2 l_2^(-3)|, an O(1) error per unit volume, not per torus. Also, the account applies only for beta >= g^(-2) + B_sharp
(S500 L23378), so (ONE-CUT) is a seed on a fine lattice at weak bare coupling, not the model arena at beta 2.3-2.6; it is not hand-checkable,
and a computer check would not be a proof.
(c) SU(2) property. None in the bridge; all of it sits in (ONE-CUT). U(1): the bridge statement is group-blind; (ONE-CUT) fails.
(d) Fact tests. U(1), Q_8, 2T, K7: (ONE-CUT) false, so nothing is claimed: pass. SMALL-BOX, FT-FK, ceilings: not applicable.
(e) Cheapest refutation test. Reading: search CA-I to CA-III and Y3S for a comparison of unnormalised free energies of consecutive cutoffs
with error o(1) per torus (grep "vacuum constant", "E_(K)", "consecutive cutoffs"). If none, (CC) is a new estimate at the precision of
the hand-off, and the route stops.
(f) Where it dies. At once, on precision (normalised against unnormalised), and because (ONE-CUT) is not in the model arena.
(g) Duplicate check. `two cutoffs|cutoff comparison|consecutive cutoff|UNIV`: gap-constraints-max L102, L103 (row 904), L250, L254
("(UNIV-K) (rows 916, 924; OPEN)"), L299. Match with (UNIV-K) and row 904. New: the exact reason SA's 3D two-cutoff comparison does not
carry it (it compares insertions, the seed is a free-energy difference), with the quoted 3D caveat.

### Step 7 close: duplicate summary (greps of the five prior brainstorm files; lane notes where named)
| # | Short name | Closest prior item | Verdict | What is new here |
|---|---|---|---|---|
| 1 | ESC | W2 door "Lyapunov weights" (status L311) | partial match | Lemma META; transience as the exact extra input of averaged routes; u_xy escape test |
| 2 | HIST-AVG | row 970 7.3 "small share", A2, A3; check 852 repair | partial match | Lemma DEF (proved additive defect, 8 beta per bad link); rarity budget 7.5e-10 |
| 3 | MOS-EXIT | EXIT / PIN-MIX (row 861); rows 691, 936 | match on target | MOS mechanism as PIN-MIX supplier; its d >= 3 obstruction = frozen-slice ordering |
| 4 | LANGEVIN-CHAIN | G2, idea 18 (Langevin gap via curvature) | partial match | Lemma PUSH: (CYL-LSI) gives (LSI-J); SA's 3D chain as template; no 4D chain in CA |
| 5 | SVD-CVAR | ideas 3, 26, G9 | match in substance | Lemma SVD, Lemma VOL (routes that use the gap alone fail by a volume factor) |
| 6 | ANALYTIC-TILT | ideas 7, 40 (other zeros) | different object | zero-free tilt polydisc; one-link radius (|phi_0|^2 + j_(1,1)^2)^(1/2) |
| 7 | PLATEAU-BOOT | ideas 38, 52, GKS-C | match | SA's coupling-free plateau as input; two arithmetic kills |
| 8 | TWO-FRAME | K7 only | no prior item | SA's two-frame oscillation vs Theorem CRIT's first-order alternative |
| 9 | ENTROPY-DRIFT | idea 40 (monotone induction) | match | Lemma RENYI (threshold 0.439), average-drift form, photon calibration 5.06 |
| 10 | CUTOFF-COMPARE | (UNIV-K), row 904 | match | why SA's 3D two-cutoff comparison cannot carry a free-energy difference |

## Step 8. Ranking, top three, status
### 8.1 Ranking by (chance the proof could die there early) x (value if it survives)
E = how early and cheaply a test can decide (5 = an hour of hand work or one existing-code GUIDE run). V = value if it survives
(5 = it would give the seed or the hand-off). Scores are my judgement (ARGUED), not measurements.
| Rank | Approach | E | V | E x V | One-line reason |
|---|---|---|---|---|---|
| 1 | ESC | 5 | 4 | 20 | One run with row 952's code decides whether the u_xy ties are metastable; either answer redirects every averaged route |
| 2 | HIST-AVG | 4 | 4 | 16 | Lemma DEF is proved; one GUIDE run of the bad-block fraction decides whether the additive bookkeeping is worth a proof |
| 3 | MOS-EXIT | 3 | 5 | 15 | A reading decides whether a d = 4 "weak implies local image" exists; survival supplies PIN-MIX, hence EXIT and the bare seed |
| 4 | LANGEVIN-CHAIN | 4 | 3 | 12 | An hour of hand work settles the worst-case margin; survival gives a port target from SA's 3D chain |
| 5 | SVD-CVAR | 5 | 2 | 10 | Already decided by Lemma VOL as a seed route; its identities stay as tools |
| 6 | ENTROPY-DRIFT | 2 | 5 | 10 | It would be the seed, but no mechanism is in sight and the test costs free-energy runs |
| 7 | CUTOFF-COMPARE | 5 | 2 | 10 | One grep decides; it is a bridge, not the order-one input |
| 8 | ANALYTIC-TILT | 3 | 3 | 9 | Shares the GUIDE of 2; no Lee-Yang theorem for the SU(2) boundary law |
| 9 | TWO-FRAME | 4 | 2 | 8 | One reading decides; (NOLH) alone leaves the continuous alternative |
| 10 | PLATEAU-BOOT | 5 | 1 | 5 | Dead by arithmetic (Lemma U1-PASS) |

### 8.2 Top three and the first concrete step of each
1. ESC. First step: a GUIDE row (Opus high, Mac mini, one numeric job under the lock) with the criteria of 1(e) fixed in the file
   before the run: slab of at least 32 slices, bottom slice frozen at u_xy, beta 2.5 and 2.6, sides 8 to 12, observables at k = 1, 2, 4, 8,
   16, 30, with the vacuum-start control. Outcome A (still in A at k = 30 in at least 30 percent of runs): by Lemma META the seed on
   (30; 120^3) fails at GUIDE level at that beta; the box must grow, and rows 960, 954 need their K_a revisited. Outcome B (95 percent leave
   A by k = 3): the ties of rows 950, 952, 970 are transient, and the trajectory form (LSI-traj-seed)_a and Approach 2 lose their main GUIDE
   objection.
2. HIST-AVG. First step: the second test of row 968 7.3, at typical tilts, block side 2, beta 2.3, sides 8 to 16, reusing row 974's
   trajectory sampler; criteria of 2(e) (bad-block fraction above 0.05 refutes the bookkeeping; below 1e-3 and falling with the side
   supports it). In parallel, ask the checker of row 970 (row 972) to read Lemma DEF, which uses Identity MM exactly as stated there.
3. MOS-EXIT. First step: a reading row (Opus high) on Martinelli-Olivieri-Schonmann 1994 and Cesi-Maes-Martinelli 1997: locate the
   planarity step; record whether any d >= 3 result gives locality of a block image from weak mixing at typical boundaries; then write
   the exact hypotheses of PIN-MIX from `library/gap-exit-max.md` (row 861) next to (WM)_(l,w) and state the missing implication.

### 8.3 Status of every statement in this file
| Statement | Where | Mark |
|---|---|---|
| J = int nu(dphi) pi_phi x pi_phi with nu proportional to gamma_beta e^(2 Lambda) (Gaussian mixture of products) | Step 3 | PROVED |
| Lemma META: S(a;B) >= (r_A(a) - p)/(1 - p); Corollary ESC-nec | 1(b) | PROVED (T_B >= 0 RECALLED from the lane) |
| Nonzero-momentum photon modes satisfy ESC (r_A <= 0.567) | 1(c) | PROVED given Sheppard's formula (RECALLED) |
| The U(1) winding holonomy violates ESC | 1(c) | ARGUED (continuum flux energy RECALLED) |
| (ESC)_a with a local drift reaches the seed | 1(b) | OPEN |
| Lemma DEF (additive defect 8 beta per bad link at the mid-slice) | 2(b) | PROVED given Identity MM (row 970, unchecked) |
| Rarity budget 7.5e-10 per link on (30; 120^3) | 2(b) | ARGUED (arithmetic on a heuristic accounting) |
| (LSI-traj-def)_a, and the good-tilt local covariance | 2(b), 2(f) | OPEN |
| (WM)_(l,w) implies PIN-MIX, hence EXIT | 3(b) | OPEN; the d = 2 mechanism RECALLED |
| Lemma PUSH and (CYL-LSI) implies (LSI-J) | 4(b) | PROVED |
| One-link gap at most 3 + h for e^(h<mu,y>) on S^3 | 4(d) | PROVED |
| Worst-case Otto-Reznikoff fails for the slice chain | 4(d) | ARGUED (staples not included) |
| (TOP-LSI) is implied by EXIT; the 4D account has no Langevin chain statement | 4(b), 4(a) | ARGUED; bounded grep |
| Lemma SVD (seed = sum sigma_n^(2a); gap = posterior-variance ratio) | 5(b) | PROVED |
| Lemma VOL (S(a) <= (lambda_1/lambda_0)^(a-1) S(1)); extensivity of log S(1) | 5(b) | PROVED; extensivity ARGUED |
| (CVAR) from the slice Poincare constant via van Trees | 5(b) | ARGUED (van Trees RECALLED; eigenfunctions only) |
| One-link zero-free tilt radius (|phi_0|^2 + j_(1,1)^2)^(1/2); Cauchy step from (LY-loc) | 6(b) | PROVED given RECALLED Bessel facts; (LY-loc) OPEN |
| Lemma U1-PASS (i), (ii) | 7(b) | PROVED given the RECALLED photon decay |
| Two-frame mechanism reaches only couplings above first passage | 8(b) | ARGUED from the quoted setup |
| Lemma RENYI (S_2 < 0.439 implies S < 3/10); photon S_2 >= 5.06 on (a;(4a)^3) | 9(b) | PROVED |
| (DRIFT)_c | 9(b) | OPEN |
| Telescoping bridge (ONE-CUT) + (CC) gives (SEED-FP); why SA's comparison cannot carry it | 10(b) | PROVED; ARGUED |
| The seed; (LSI-traj-seed)_a; any order-one bound for SU(2) | all | OPEN; none proved here |

### 8.4 What this file does not show
No order-one bound for SU(2) is proved. Every GUIDE test above is a proposal with criteria; none was run (no numerics on this laptop).
Readings are bounded: CA-III was only grepped; the MOS, Cesi-Maes-Martinelli, van Trees, Otto-Reznikoff, Sheppard and Bessel facts are
RECALLED, not re-read. Identity MM and Lemma TRAJ are used as stated in row 970, which nobody has checked yet (check row 972 is held).
Quotes of Sussman and Alpoge are data; line numbers refer to the local copies named in Steps 2 and 3.

RESULT: Row 975 (Claude Opus 5.5 max, laptop agent; checked by no one): ten approaches drawn from Sussman and Alpoge's construction - ESC, HIST-AVG, MOS-EXIT, LANGEVIN-CHAIN, SVD-CVAR, ANALYTIC-TILT, PLATEAU-BOOT, TWO-FRAME, ENTROPY-DRIFT, CUTOFF-COMPARE; PROVED here: the two-slice law is a Gaussian mixture of products, Lemma META (each metastable set adds about 1 to S whatever its probability, so averaged routes need transience), Lemma DEF (an additive 8 beta per bad link defect in Identity MM), Lemma PUSH ((CYL-LSI) gives (LSI-J)), Lemmas SVD and VOL (a gap alone misses the seed by a volume factor), Lemma RENYI (S_2 < 0.439 gives S < 3/10; photon S_2 >= 5.06), Lemma U1-PASS; OPEN: the seed, (LSI-traj-seed)_a and every order-one SU(2) input; top three: (1) ESC, first step the u_xy escape GUIDE run with criteria fixed in 1(e); (2) HIST-AVG, first step the bad-block fraction at typical tilts (row 968 7.3 second test) plus a check of Lemma DEF; (3) MOS-EXIT, first step a reading row on whether weak mixing gives a local soft block image in d = 4, set against PIN-MIX of row 861.
