lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T20:20Z

# gap-sc-max (queue row 950): is (SC) an order-one input, and can it be proved?

Provenance: Claude Fable 5.2, max effort, Mac mini worker, pinned at commit `0d2530101`. Author item. Not an audit,
no status. Nothing here is checked by another model yet (row 951 is the check).

Moves: the second order-one input of the hypercontractivity chain, (SC) of row 944
(`library/gap-sgstep-opus.md`): Hess(log Omega + V/2) at most C_F, a box-free first-step electric susceptibility,
uniform in the boundary slice.

## 0. Plan (one step per response; each step is appended before the next)

1. Repo search and inputs: read row 944's note in full, row 941's exponential-family form of log Omega, the checks
   942/943, and grep `library/open-core.md` and the FINISH rows for (SC). Record the exact statements used.
2. (a) The one-step conditional law in temporal gauge, written exactly; what the Omega factor does to locality.
3. (b) Is (SC) implied by (FC) or (LSI-vac), or independent?
4. (c) Fact tests: photon, ordered phase (Example DW), frozen groups, SMALL-BOX.
5. Attack (SC), or the weakest projected form Theorem SC needs, for SU(2) Wilson at beta 2.3-2.6.
6. If open: the smallest unproved inequality and one test that could refute it (a run is GUIDE only).
7. Result table and RESULT line.

Status marks: PROVED, CONDITIONAL (on named inputs), GUIDE, OPEN.

## 1. Repo search and inputs (step 1; READ at 0d2530101)

**Read.** FINISH.md (opening, How we work, Joining, Working efficiently, Rules; rows 946, 947, 950), GOAL.md is the
target file (not re-read beyond the rules above). `library/gap-sgstep-opus.md` in full (row 944, Claude Opus 5.5,
unchecked; its check, row 945, is not on disk). `library/gap-lsivac-max.md` Steps 0-6 (row 941, Claude Fable 5.2):
(A1)-(A7), the ceilings of Step 2, Theorem C, Theorem C0, 5.3 Gaussian domination, Step 6. READ means read at the
pinned commit, not re-proved.

**Duplicate check (rule 0a).** `grep -n -i -E "\(SC\)|SC-Omega|semiconcav|susceptib|electric|first-step"` on
`library/open-core.md`: no hit. FINISH rows that name (SC): 944 (states it, leaves it OPEN), 950 (this row), 951
(its check). Row 947 attacks (FC), row 946 tests (FC); neither touches (SC). Row 941's (C2) and (COV) are the same
kind of object ((C2) for all tangent z is (SC) at the sub-Gaussian level, Section 3 below); row 941 "did not
attempt them" (its Step 6). So (SC) is this row's. I stay off (FC), (C1-av), (LSI-vac), (CUT-TYP), (VAC-SUB).

**Repo search.** This clone holds only `claude/ym4d-hard-route`; origin/main and the PR branches are not on it.
Inside the lane folder: `grep -l -i -E "Dirichlet|half-space|boundary slice" library/gap-*.md` gives the gap lane's
own files only; no note bounds a conditional covariance uniformly in a boundary slice.

**Notation (row 944 Section 1, kept).** B a periodic spatial box, N = 3|B| links, M = (S^3)^N, <.,.> the R^4 inner
product. V(u) = beta sum_p (1 - (1/2) tr U_p(u)). T_0(u, w) = e^(-V(u)/2) e^(beta <u, w>) e^(-V(w)/2), T = T_0 Pi_G,
Omega its ground state, lambda_0 its top eigenvalue, nu = Omega^2 dw.
F := log Omega + V/2. Temporal-gauge one-step law pi~_u, gauge-invariant one-step law pi_u (law of the orbit).
(SC): Hess_M F(v) <= C_F g for every v in M, C_F box-free. Row 944, Theorem SC: (SC) gives (SG-step) with
sigma^2 = C_F + beta. Row 944, Identity HV: beta^2 Var_(pi~_u)(<z, w'>) = Hess_M F(u)(z, z) + beta sum_l E<u_l, w'_l> |z_l|^2.
Row 941 (A2): F = Lambda(beta .) - log lambda_0 on M, Lambda convex on R^(4N), Hess Lambda = covariance of the tilted law.
(Row 941 drops the constant of V; this only rescales lambda_0.)

## 2. The one-step law in temporal gauge, and what Omega does to locality (step 2; question (a))

All statements of this section are PROVED by hand (Claude Fable 5.2), not yet checked, unless marked.

**2.1 The exact law.** For u in M,
  pi~_u(dw) = exp( beta <u, w> - V(w) + F(w) - F(u) - log lambda_0 ) dw.                                   (2.1)
Proof. Row 944 Lemma TG: pi~_u(dw) = e^(-V(u)/2) e^(beta <u, w>) e^(-V(w)/2) Omega(w) dw/(lambda_0 Omega(u)). Insert
Omega = e^(F - V/2). QED
Three factors. (i) Temporal plaquettes: beta <u, w> = sum_l beta <u_l, w_l>, a product over links; it pins each link
to u_l with the same strength beta, and it is the ONLY place where u occurs. (ii) Spatial plaquettes of the new
slice: e^(-V(w)), local. (iii) The future: e^(F(w)).

**2.2 Omega is the integrated future of a local measure (Lemma UNROLL).** For n >= 1, the law of the first n slices
of the temporal-gauge chain started at w_0 = u is
  P_u^n(dw_1 .. dw_n) = exp( sum_(t=0..n-1) beta <w_t, w_(t+1)> - sum_(t=1..n) V(w_t) + F(w_n) - F(u) - n log lambda_0 ) prod_t dw_t.   (2.2)
Its w_1-marginal is pi~_u for every n.
Proof. Multiply (2.1) for the steps w_t -> w_(t+1); the factors e^(F(w_t)) telescope. QED
Reading. (2.2) is the Wilson measure of the slab [0, n] x B in temporal gauge, with Dirichlet data u on the slice
t = 0 and the weight e^(F(w_n)) on the last slice. Every factor except the last is a plaquette term. So:
- pi~_u is not a local Gibbs measure on one slice, but it is the first-layer marginal of a local 4D measure on the
  half space. The Omega factor adds nothing else. log Omega is as non-local as the half-space measure is correlated:
  by row 941 (A2), the mixed second derivatives of F at w are beta^2 times the covariances of the next slice given w.
- Omega can be removed from (SC) altogether. Let P_u^(n,free) be (2.2) with F(w_n) replaced by -V(w_n)/2 (row 944's
  slab). Its w_1-marginal has density proportional to e^(beta<u,w_1> - V(w_1)/2) (T_0^(n-1) 1)(w_1), and
  T_0^(n-1) h/lambda_0^(n-1) tends to <Omega, h> Omega uniformly as n grows (positive kernel on a finite box). So
    Hess_M F(u)(z, z) + beta sum_l E<u_l, w_l> |z_l|^2 = beta^2 lim_n Var_(P_u^(n,free))(<z, w_1>).                 (2.3)
  (SC) is a statement about the local half-space Wilson measure only.

**2.3 Gauge-invariant form.** Restore the temporal links g_x of the first step (row 944: w' = g.w). Then
w'_l u_l^* = g_x w_l g_(x+l)^* u_l^* = P_l, the holonomy of the temporal plaquette over the link l, based at (x, 0). With
z_l = xi_l u_l (xi_l an imaginary quaternion), <z_l, w'_l> = <xi_l, E_l>, E_l := Im P_l. So
  (SC)  <=>  sup over u of || Cov_u(E) ||_op <= (C_F + O(beta))/beta^2,
where Cov_u is the covariance of the 3N numbers E_l^a = (Im P_l)^a under the half-space Wilson measure whose spatial
links at t = 0 are frozen at u (all other links Haar; gauge transformations are frozen at the sites of t = 0 only).
E_l transforms in the adjoint representation at the base site of l. In words: (SC) says that the colour-electric
field on a Dirichlet boundary has a box-free susceptibility, for every Dirichlet datum u. Sufficient (Schur test):
sum over l' of |Cov_u(E_l^a, E_l'^b)| <= C for all l, u. This is a strong-mixing statement for the boundary layer.
(SC) depends on u only through its gauge orbit (pi~_(g.u) is the image of pi~_u under g).

**2.4 Total variance (Identity TV).** For u in M and z in T_u M, with mu_(u,w)(dg) = k(u, g.w) dg/K(u, w) and phi_(u,z)
the projected score of row 944:
  Hess_M F(u)(z, z) = Var_(pi_u)(phi_(u,z)) + E_(pi_u)[ Var_(mu_(u,w))(beta <z, g.w>) ] - beta sum_l E_(pi~_u)<u_l, w'_l> |z_l|^2.     (2.4)
Proof. Identity HV, and the law of total variance for psi = beta<z, w'> - mean under rho_u (row 944 Lemma TG:
phi = E[psi | w]). QED
So (SC) = a variance bound for the projected score (the gauge-invariant content, what (SG-step) needs at second
order) + a bound on the gauge-frame fluctuation of the linear statistic. Row 944's Theorem SC drops the second
term from the benefit side; it is the whole difference between (SC) and (SG-step) at the variance level.

**2.5 Only horizontal directions matter (Lemma HG, Theorem SC-hor).** G = SU(2)^|B| acts on M by isometries. For v
in M let Vert_v be the tangent space of the gauge orbit and Hor_v its orthogonal complement.
Lemma HG. A geodesic c of M with c'(0) in Hor_(c(0)) has c'(s) in Hor_(c(s)) for all s.
Proof. For X in Lie(G) the field X^*(v) = d/ds (e^(sX).v) is a Killing field, so v -> nabla_v X^* is skew. Hence
d/ds <c', X^*(c)> = <nabla_(c') c', X^*> + <c', nabla_(c') X^*> = 0. So <c'(s), X^*(c(s))> = 0 for all s and X. QED
**Theorem SC-hor.** Assume
  (SC-hor)  Hess_M F(v)(z, z) <= C_h |z|^2  for every v in M and every z in Hor_v.
Then (SG-step)_sigma holds for every u and every unit z in T_u M, with sigma^2 = C_h + beta.
Proof. p(u, w) is gauge invariant in u, so the score vanishes on Vert_u: phi_(u,z) = phi_(u,z^h), z^h the horizontal
part, |z^h| <= 1. If z^h = 0 there is nothing to prove. Else put e = z^h/|z^h| and u(s) = exp_u(s e). By Lemma HG,
u'(s) is horizontal and of unit length. Row 944 (4.1): Hess_u log p(u(s), w)(u', u') = Hess_u log K(u(s), w)(u', u')
- Hess_M F(u(s))(u', u') >= -beta - C_h. Row 944 Lemma HSS (its proof uses the Hessian only along this geodesic) gives
E_(pi_u) e^(t phi_(u,e)) <= e^((C_h + beta) t^2/2) for all real t. Put t = lambda |z^h|. QED
So the hypothesis of Theorem SC can be cut down to horizontal vectors. In the form of 2.3: only the horizontal block
of the first-step electric covariance has to be bounded. At a central slice (all u_l = +-1) the vertical vectors are
the lattice gradients xi_l = X_x - X_(x+l) and the horizontal ones are the divergence-free fields xi.
(SC) => (SC-hor) => (SG-step). Neither converse holds in general: row 944 Lemma CEN gives phi = 0 at central slices
whatever Hess F is; Section 5 gives a candidate slice where the horizontal block itself would grow.

**2.6 The average over the vacuum is free (Proposition AV; uses that the adjoint representation has no invariant).**
For a field xi of imaginary quaternions put z^xi(u) := (xi_l u_l)_l in T_u M. Then, on every box of side >= 3,
  E_nu(du) [ Var_(pi~_u)(<z^xi(u), w'>) ] <= E_J[ <xi, E>^2 ] <= |xi|^2,    E_l = Im(w'_l u_l^*).
Proof. J(du, dw') = nu(du) pi~_u(dw') = e^(beta<u,w'>) m(du) m(dw')/lambda_0 (row 941 (A1)) is invariant under the
simultaneous gauge transformations (u, w') -> (g.u, g.w'), and E_l -> g_x E_l g_x^* (x the base site of l). Take g = c
at one site x and 1 elsewhere, and average over c in SU(2): E_J[E_l^a E_l'^b] = 0 unless l and l' have the same base
site. For the three links based at x, E_J[E_l^a E_l'^b] = delta_ab c_(ll') (average over c again), and the 3 x 3 matrix
c has norm at most its trace, sum_l E|E_l|^2/3 <= 1. Last, Var(X | u) <= E[X^2 | u]. QED
Reading. In the body frame the vacuum average of the first-step electric covariance is at most the identity:
E_nu[Cov_u(E)] <= 1, on every box, with no input. Row 941's 5.3 (Gaussian domination) is the ambient-frame analogue
with the constant 1/beta, and is group-blind; this one is false for U(1) (E is gauge invariant there).
So the whole content of (SC) is the SUPREMUM over the boundary slice. Neither average bounds the top eigenvalue of
Cov_u(E) at a typical u (the bad direction may depend on u).

## 5. Attack, part 1: try to kill (SC) first (step 5; the criteria below were written before the run)

(Sections 3 and 4 are written while the run is going; they follow below in the file.)

**5.1 The most dangerous slice found: the layered pi-flux slice u_xy (ARGUED; this is a design, not a proof).**
Mechanism to look for (row 944 Section 4): a slice at which two classical half-space extensions tie and differ on
a number of links growing with the box. A tie is forced by symmetry when the stabilizer of u moves the extension.
For a central slice the stabilizer is the global SU(2) (constant gauge transformations), acting on the first-step
field by a global colour rotation E_l -> Ad_c E_l. If the first step has a preferred pattern E_l = eps_l s n with a
colour direction n in S^2, the extensions form an SO(3) orbit, and Cov_u(E) has an eigenvalue of order |pattern|^2
as soon as n is ordered across the box.
Row 944 tested u_pi (every spatial plaquette -1) and found a short-range staggered pattern. u_pi is FRUSTRATED:
write w_l = h_l u_l, h_l = exp(sigma_l theta n). A plaquette of u with flux -1 becomes +1 at theta = pi/4 iff the four
signs circulate, sigma_1 + sigma_2 - sigma_3 - sigma_4 = +-4. For the xy, yz and zx planes together this forces
sigma_x = -sigma_y = sigma_z = -sigma_x at each site: impossible. With flux -1 through the xy plaquettes ONLY,
  u_xy:  u_y(x, y, z) = (-1)^x,  u_x = u_z = 1   (L even),
the pattern sigma_x = (-1)^(x+y), sigma_y = -(-1)^(x+y), sigma_z = 0 circulates on every xy plaquette, leaves the xz and
yz plaquettes at +1, and is not frustrated. It has zero lattice divergence, so it is HORIZONTAL at u_xy (2.5): it
tests (SC-hor) as well as (SC). Its momentum is (pi, pi, 0) and its polarization is (1, -1, 0)/sqrt 2 in directions.
One-step classical estimate: energy per site 2 beta (1 - cos theta) + beta (1 + cos 4 theta), least near theta = 0.70, so the
pattern is large (sin theta about 0.65), and a twist gamma of n between neighbours costs about 0.14 beta gamma^2 per xy
plaquette and 0.2 beta gamma^2 per xz or yz plaquette: a 3D Heisenberg-type stiffness of order 0.3 beta to 0.4 beta per bond,
against a critical coupling 0.69 for the 3D classical Heisenberg model (RECALLED). At beta 2.3 this is borderline,
so the outcome is not predictable by hand. Thermal fluctuations are as large as the pattern (row 944: E|E_l|^2
about 0.6), which argues against order.
What an ordered n would and would not mean. It would refute (SC), (SC-hor) and the pointwise form (HS) of row 944
at u_xy (GUIDE). It would not touch (SG-step): for SU(2) the two staggered patterns +-n are gauge equivalent (a
global rotation), the tie is pure gauge frame, and Lemma CEN gives phi = 0 at u_xy. For compact U(1) the same slice
has only the charge-conjugation tie s = +-1; the two patterns are gauge INEQUIVALENT there (staggered flux), so for
U(1) an ordered sign would break (SG-step) itself (ARGUED).

**5.2 Kill test (GUIDE; criteria fixed here, before the run).** Model and observable as in row 944 Section 6
(half-space slab in temporal gauge, slices t = 0..T, T = 6, last slice with weight 1/2 on its plaquettes, heat
bath; Lambda(k) = (1/(3 L^3)) sum_a E[Ehat^a(k) Ehat^a(k)^dagger], lambda(L) = max_k of its top eigenvalue), but with my
own code (`/tmp/gap-sc-950/scripts/slab_xy.py`, written without reading row 944's script; quaternion links,
Creutz sampler, checkerboard by direction and parity of x + y + z + t). Also lambda_*(L) := the value of Lambda at
k = (pi, pi, 0) on the polarization (1, -1, 0)/sqrt 2 (the predicted mode).
Criterion. G := lambda(10)/lambda(4) at u_xy, beta 2.3, cold start, 20000 measured sweeps (12000 at L = 10).
- G >= 4 with lambda increasing in L: GUIDE says (SC) and (SC-hor) FAIL at u_xy.
- G <= 1.3: no growth; (SC) survives this slice (establishes nothing).
- otherwise inconclusive.
Controls. (i) Code: u = 1 and u_pi at L = 4, beta 2.3 must reproduce row 944's 0.2991 and 0.4503 within 3 percent.
(ii) Power: at beta 6.0 the classical picture should hold; at u_xy, lambda(6)/lambda(4) should then be well above 1.3
(fully ordered: (6/4)^3 = 3.4), with the maximum at (pi, pi, 0). If not, the design has no power and I say so.
(iii) Hot and cold starts at L = 6 must agree within 15 percent. (iv) Same slice at beta 2.6.
Sampler checks done before the run: mean of the von Mises-Fisher draw against I_2/I_1 at k = 0.5, 2.3, 6, 15
(agreement 4e-4); quaternion product associative to 2e-16; plaquettes of the slices as designed; smoke run at u = 1
gives the per-component variance 0.1602 (row 944: 0.1600).

## 3. Is (SC) implied by (FC) or (LSI-vac)? (step 3; question (b))

**Answer.** No implication in either direction is available, and (SC) is a separate input. (SC) is a REGULARITY
statement (a lower curvature bound for the vacuum chain); (LSI-vac) and (FC) are ERGODICITY statements. In convex
classes (SC) is automatic with C_F = beta and no gap; in the compact non-convex chain it is a genuine order-one
statement (no first-layer order for any Dirichlet datum). Details:

**3.1 Dictionary with row 941 (PROVED).** Row 941's (C2)_sigma taken for all unit tangent z is sup_u sigma~(u)^2 <= sigma^2,
and row 944's converse gives C_F - beta <= sup_u sigma~(u)^2 <= C_F + beta. Taken for horizontal z, as row 941 states it,
(C2) is (SC-hor) in the same sense (Lemma HSS for the temporal-gauge kernel along horizontal geodesics, Lemma HG).
Row 941's (COV)_kbar (a supremum over all ambient fields theta in R^(4N)) gives (SC) with C_F = beta^2 kbar + beta, by
Identity HV; (COV) is stronger in form than (SC), which needs only theta in beta M and tangent directions.

**3.2 (SG-step) is a reverse log-Sobolev inequality for P (PROVED, given the standard duality; Bobkov and Goetze
1999, RECALLED; the forward half is row 940's Lemma SGC, HOLDS in check 938).** (SG-step)_sigma holds iff for all
positive gauge-invariant g and all u,
  |grad P g|^2 / P g  <=  2 sigma^2 [ P(g log g) - (P g) log (P g) ]      pointwise.                          (3.1)
At second order (g = 1 + eps f): Var_(pi_u)(phi_(u,z)) <= sigma^2 for all u, z iff |grad P f|^2 <= sigma^2 [P(f^2) - (P f)^2].
Proof of the second-order line. z . grad P f(u) = Cov_(pi_u)(phi_(u,z), f) (row 941 (A3) in projected form), so Cauchy-
Schwarz gives the inequality; f = phi_(u,z) gives the converse. QED
Reading. Reverse Poincare and reverse log-Sobolev inequalities are what a LOWER curvature bound gives for a
diffusion semigroup (Bakry-Emery CD(-K, infinity); Wang's Harnack inequality, RECALLED). For the ground-state
diffusion with invariant law Omega^2 dU, CD(-K, infinity) is Ric - 2 Hess log Omega >= -K, an UPPER bound on Hess log Omega:
this is (SC-Omega). So the pair of the chain is the classical pair "log-Sobolev + curvature bounded below", in
discrete time. Row 941's Attack A asked for positive curvature and died; (SC) asks only for a box-free negative
bound. A lower curvature bound holds for Brownian motion on every compact manifold and implies no gap.

**3.3 (SC) with (C1-av) gives (FC) (PROVED; averaged form of row 941's Theorem C).** Integrate (3.1) in nu and use
stationarity: I(P g) <= 2 sigma^2 [Ent_nu(g) - Ent_nu(P g)]. With (C1-av)_(alpha_c) of row 941 (5.1):
  (SG-step)_sigma + (C1-av)_(alpha_c)  =>  (FC)_theta with theta = sigma^2/alpha_c,
and then Theorem C0 gives (LSI-vac) with alpha = alpha_c - sigma^2. So (SC) would also feed (FC), but only below the
threshold C_h + beta < alpha_c, which nothing here supports at beta 2.3 (GUIDE values of row 944 give sigma~^2 about
beta^2 0.45 = 2.4 at u_pi; alpha_c is unknown). One Gaussian mode: sigma^2/alpha_c = e^(-2 omega), exact.

**3.4 (SC) does not imply (LSI-vac) or (FC) at a box-free rate (PROVED, given row 929's mode list, READ).** The
photon has Hess F = beta e^(-omega) <= beta on every mode (row 944), while alpha = 2 beta sinh(omega_min) -> 0 and
theta = e^(-2 omega_min) -> 1 with the box (row 941 FT-U1, 5.1).

**3.5 Convex classes: (SC) follows from the structure, with C_F = beta.**
(i) Gaussian class (PROVED). Flat chain with R(w) = exp(-<w, A w>/2), A > 0 (Lemma RS of row 944 in flat space):
pi_u = N(beta A^(-1) u, A^(-1)), Hess F = beta^2 A^(-1), and nu = R kR is proportional to exp(-<w, (A - beta^2 A^(-1)) w>/2).
A stationary law exists iff A > beta, and then Hess F < beta. For the photon Hess F = beta e^(-omega(K)), whatever the
spectrum of K >= 0. So in the Gaussian class (SC) with C_F = beta is implied by stationarity alone.
(ii) Log-concave class (CONDITIONAL on two cited theorems, RECALLED: Prekopa-Leindler, and the Brascamp-Lieb
variance inequality, J. Funct. Anal. 22 (1976)). Flat chain T(q, q') = e^(-U(q)/2) e^(-(beta/2)|q - q'|^2) e^(-U(q')/2), U
convex. T preserves log-concavity (Prekopa), so Omega is log-concave. Then m(dq') = e^(-(beta/2)|q'|^2 - U(q')/2) Omega(q') dq'
has -Hess log (density) >= beta, every tilt e^(beta<q,q'>) m(dq') too, so Cov <= 1/beta (Brascamp-Lieb) and
Hess F = beta^2 Cov <= beta. No gap is used.
Reading. This answers the row's first question for the classes where it can be answered by structure: convexity
is the structure that gives (SC). The compact Wilson slice law at beta > 1 has none (row 941 Step 2 (i)), and
row 944's Example DW shows that without it the constant can be of order beta^2 N.

**3.6 (LSI-vac), (FC) do not imply (SC) (ARGUED, not proved).** (a) Form: (LSI-vac) and (FC) are nu-averages over
gauge-invariant functions; (SC) is a supremum over all slices, nu-null families included, and it bounds the gauge
frame part of (2.4) as well. Proposition AV shows that the nu-average of the object of (SC) is bounded with no
input at all. (b) Mechanism for a counterexample in the class of Lemma RS: R = e^(-beta<h_0, w>) R_0 with h_0 in M and
R_0 a symmetric weight that orders at zero field. At u = h_0 the tilt cancels the hidden field and pi_u = R_0 orders,
so C_F grows with N; nu = R kR sits in a field of strength at least beta per link and has one phase. That nu then
has a box-free log-Sobolev constant is the known behaviour of spin systems in a strong field (Stroock-Zegarlinski
type results, RECALLED); I did not prove it for an explicit R_0. So this direction is ARGUED.
(c) For the Wilson chain itself the question is the kill test of Section 5: an ordered first layer at a
symmetric slice would be exactly "(SC) false while the vacuum is massive".

## 4. Fact tests of (SC) (step 4; question (c))

- **Photon (PROVED).** Hess F = beta e^(-omega) on each mode: (SC) with C_F = beta e^(-omega_min) <= beta, box-free, for a
  gapless model. So (SC) implies no gap and costs U(1)'s Gaussian part nothing. Same for every convex class (3.5).
- **Free links, V = 0 (PROVED).** Omega = 1, F = const, Hess_M F = 0. Identity HV then reads beta^2 Var = beta A(beta) |z|^2,
  the von Mises-Fisher tangential variance A(beta)/beta of row 941 (A6). (SC) holds with C_F = 0.
- **Ordered phase (PROVED for the abstract chain, row 944 Example DW).** C_F >= 0.15 beta^2 N - beta at beta 2.3.
  (SC) is violated exactly by a first-layer coexistence. The gauge-theory candidate is 5.1.
- **Frozen Q_8, 2T.** M is finite; no Hessian, no tangent vector. (SC), (SC-hor) and Theorem SC-hor are not
  defined. Domain exclusion, as in row 944 and check 942. Nothing here carries a rival's failure.
- **Compact U(1) (PROVED where marked).** Sections 2.1-2.5 hold verbatim on S^1 (Lemma HG is general). Proposition
  AV fails: E is gauge invariant for U(1), so the vacuum average of Cov_u(E) is the true electric two-point
  function. At a real slice (all u_l = +-1) charge conjugation w -> w^* fixes u and maps E to -E, so E has mean 0 and
  a sign tie. At u_xy the two staggered patterns are gauge inequivalent (ARGUED, 5.1). So in U(1) an ordered
  sign breaks (SG-step) itself, while in SU(2) the same order is pure frame. This is the one place where the
  group enters; it is ARGUED, and it is a prediction for a U(1) control run, not a result.
- **SMALL-BOX (conditional on its premise, as in check 938).** On a fixed box, as beta grows, the tie at a
  flux -1 slice becomes exact (the first step of a classical extension from a maximum of V is of order one,
  5.1), so C_F is of order beta^2 times the number of links of the pattern, not of order beta (ARGUED). Then
  alpha/sigma^2 falls like 1/beta or faster, as SMALL-BOX demands of every route. No conflict. It also shows
  that (SC) cannot be proved uniformly in beta: a proof at beta 2.3 to 2.6 must use the size of the fluctuations.
- **FT-CEIL.** (SC) is a sup form. The three time-direction ceilings of row 941 Step 2 cap POSITIVE curvature
  criteria; (SC) is a negative lower bound and none of them applies. Check 870's refutation conditions on all
  links (row 944 Section 5) and does not apply as stated. No cited ceiling refutes (SC). None supports it.
- **Small beta (RECALLED, not rebuilt).** A uniform Dobrushin condition on the half-space measure gives 2.3's
  Schur bound; it needs beta of order 1/13 (one link has 13 neighbours through plaquettes, each with influence at
  most about beta). Far below the window.

## 5 (continued). Attack, part 2: what a proof would have to do (step 5; by hand, while the run waits for the lock)

**5.3 Bellman recursion for the Hessian (Identity REC; PROVED by hand, not yet checked).** For a field eta of
imaginary quaternions let Z = Z_eta be the left-invariant vector field Z(w) = (w_l eta_l)_l on M (the generator of the
right translations w_l -> w_l e^(s eta_l); these are not gauge transformations). Then for every u in M:
  (Z F)(u) = E_(pi~_u)[ (Z(F - V))(w) ],
  Hess_M F(u)(Z, Z) = E_(pi~_u)[ Hess_M(F - V)(w)(Z, Z) ] + Var_(pi~_u)( (Z(F - V))(w) ).                         (REC)
Every tangent vector z at u is Z_eta(u) for one eta (eta_l = u_l^* z_l), so (REC) covers all directions.
Proof. e^(F(u)) lambda_0 = integral of e^(beta<u,w>) e^((F - V)(w)) dw by (2.1). The kernel is invariant under simultaneous right
translations, <u_l c, w_l c> = <u_l, w_l>, and dw is Haar. So e^(F(u e^(s eta))) lambda_0 = integral of e^(beta<u,w>) e^((F - V)(w e^(s eta))) dw.
Differentiate the logarithm once and twice at s = 0. The curves s -> u e^(s eta) and s -> w e^(s eta) are geodesics of M
(one-parameter subgroups of a bi-invariant metric), so the second derivatives are the Riemannian Hessians. QED
Iterated over n steps of the temporal-gauge chain (the conditional variances add up to the variance of the
martingale M_t = (Z F)(w_t) - sum_(s<=t) (Z V)(w_s)):
  Hess_M F(u)(Z, Z) = E_u[ Hess_M F(w_n)(Z, Z) ] - sum_(t=1..n) E_u[ Hess_M V(w_t)(Z, Z) ] + Var_u( (Z F)(w_n) - sum_(t=1..n) (Z V)(w_t) ).
Reading. (REC) is the second variation of the half-space free energy under a common right translation of all
slices: the electric susceptibility of the first step equals the susceptibility of the time-summed magnetic
force. In flat space it is the Riccati equation of the photon (check: one Gaussian mode, with F~ = F - (beta/2) q^2
and U = beta (m^2/2) q^2: (F~ - U)'' = beta (1 - e^omega), Var = beta (1 - e^omega)^2 e^(-omega), sum beta (e^(-omega) - 1) = F~''. Exact.)
What it does not give. Taking suprema, C_F <= C_F + 16 beta + sup Var: the first term returns C_F with coefficient
one, so (REC) is not a contraction. In the convex classes the recursion closes because the variance term is
controlled by Brascamp-Lieb with the precision beta + Hess(V - F) (3.5). Without convexity the variance term needs
a Poincare constant of pi~_u for ALL functions (frames included) and a sign that is not there. So the recursion
restates (SC); it does not prove it. First failing step of this attack: no bound on Var_(pi~_u)(Z(F - V)) uniform in u.

**5.4 Where each known tool stops (summary; ARGUED unless marked).**
- Convexity (Prekopa, Brascamp-Lieb): gives C_F = beta in flat convex classes (3.5); the compact chain is not
  convex for beta > 1 (row 941 Step 2 (i), PROVED there).
- Symmetry: gives the vacuum average (Proposition AV, PROVED) and phi = 0 at central slices (row 944 Lemma CEN), never a
  supremum.
- Reflection positivity, Gaussian domination: annealed and group-blind (row 941 5.3, PROVED there).
- Dobrushin, cluster expansion: beta of order 1/13 (Section 4).
- Bellman recursion: no contraction (5.3).
So (SC) for SU(2) at beta 2.3 to 2.6 is a uniform strong-mixing statement for the Dirichlet boundary layer at
intermediate coupling. I know no method that proves such a statement there. It stays OPEN (Section 6).

## 6. The smallest unproved inequality, and the test that could refute it (step 6)

**6.1 The inequality.** For SU(2) Wilson at beta in [2.3, 2.6] on the seed box (24a)^3:
  (SC-hor)  for every slice u and every field xi of imaginary quaternions with zero covariant divergence at u,
            sum over links l out of x of xi_l  -  sum over links l into x of u_l^* xi_l u_l  =  0  at every site x,
            Var_u( sum_l <xi_l, E_l> ) <= c_E |xi|^2,   c_E box-free,
where E_l = Im P_l is the first-step electric field of 2.3 and Var_u is taken in the half-space Wilson measure with
Dirichlet datum u. (The divergence condition is horizontality of z = (xi_l u_l)_l: z is orthogonal to
X_x u_l - u_l X_(x+l) for all X.) By Identity HV this is (SC-hor) of 2.5 with C_h <= beta^2 c_E + beta, and Theorem SC-hor then
gives (SG-step) with sigma^2 <= beta^2 c_E + 2 beta. It is weaker than row 944's (SC) (all xi) and stronger than
(SG-step). A sufficient form: |Cov_u(E_l^a, E_l'^b)| <= C e^(-m dist(l, l')) for all u (uniform decay on the boundary layer).
Size: any box-free c_E serves the seed (it enters through alpha/sigma^2 and a may grow). GUIDE values at beta 2.3:
c_E = 0.30 at u = 1, 0.45 at u_pi (row 944, reproduced in 5.5), 2.5 at u_xy; about 8 at u_xy at beta 2.4.
**After the runs (5.5-5.8): at beta 2.5 and 2.6 no box-free c_E exists at u_xy on boxes up to 20 (GUIDE). So (SC-hor)
is a candidate only in the lower part of the window; the inequality that remains for the whole window is
(SG-step) in the gauge-invariant form of 7.3, with first instance (SG2).**
Fact tests of (SC-hor): photon c_E = e^(-omega)/beta <= 1/beta (the transverse field; PROVED); free links c_E = A(beta)/beta;
Example DW has no gauge group (all vectors horizontal) and violates it; frozen groups not defined; SMALL-BOX no
conflict (Section 4). It is group-blind in form; nothing in it is expected to fail for U(1) at weak coupling
except at real slices with a sign tie (Section 4).

**6.2 The test.** The kill test of 5.2 at the layered pi-flux slice u_xy: a first-step electric susceptibility that
grows with L at the mode (pi, pi, 0), (1, -1, 0) refutes (SC-hor) and (SC) for SU(2) at that coupling (GUIDE), and
leaves only (SG-step) itself. Results: Sections 5.5 to 5.8 (growth found at beta 2.5 and 2.6, none at 2.3 and 2.4).

**6.3 Compact U(1) control of the same test (GUIDE; queued after the SU(2) batch).** Script
`/tmp/gap-sc-950/scripts/slab_u1.py` (angles, von Mises heat bath, same slab, E_l = sin(theta_l(1) - u_l), Lambda(k) with no
colour sum). Prediction of Section 4: at u_xy the sign of the staggered pattern orders in the Coulomb phase, so
lambda grows like L^3; at u = 1 it does not; in the confined phase (beta 0.9) it does not.
Criteria: G_U1 := lambda(8)/lambda(4) at u_xy, beta 2.3. G_U1 >= 4: compact U(1) FAILS (SC-hor) at beta 2.3 (GUIDE).
G_U1 <= 1.3: no order. Control u = 1: lambda(8)/lambda(4) <= 1.3 and lambda below 1.
Honest note on order of events: a 250-sweep smoke run of this script (L = 4, outside the lock, under one second)
was seen BEFORE these criteria were written. It gave lambda = 41.2 at (pi, pi, 0) for u_xy (staggered order parameter
1.13, the fully ordered value 2 L^3 sin^2 theta with sin theta = 0.57) against 0.72 for u = 1. So the L = 4 value was
known; the L dependence and the controls were not. The smoke runs of both scripts (about 12 s in all) ran outside
the lock; every reported number comes from the batches under the lock.

## 5.5 GUIDE results of the kill test, batch 1 (run 08:43-08:55Z under the numeric lock, 71 percent memory free)

Log `/tmp/gap-sc-950/logs/batch.log` (not committed). One thread, nice; arrays below 10 MB. Entries are lambda(L), the
top eigenvalue of the one-colour first-step electric covariance; "blocks" are the four quarter-run values.

| slice | beta | start | L = 4 | L = 6 | L = 8 | L = 10 | k of the max | per-component variance |
|---|---|---|---|---|---|---|---|---|
| u = 1 (code control) | 2.3 | cold | 0.2984 | | | | flat top | 0.1600 |
| u_pi (code control) | 2.3 | cold | 0.4558 | | | | (pi, pi, pi) | 0.2251 |
| u_xy (power control) | 6.0 | cold | 11.91 | 38.65 | | | (pi, pi, 0), (1, -1, 0) | 0.1404 |
| **u_xy** | **2.3** | cold | **2.03** | **2.55** | **2.51** | **2.46** | (pi, pi, 0), (1, -1, 0) | 0.2028 |
| u_xy | 2.3 | hot | | 2.52 | | | (pi, pi, 0), (1, -1, 0) | 0.2024 |
| **u_xy** | **2.6** | cold | **4.19** | | **22.62** | | (pi, pi, 0), (1, -1, 0) | 0.1901 |

Block spreads: u_xy at beta 2.3: 1.82-2.24 (L = 4), 2.16-3.08 (L = 6), 2.32-2.80 (L = 8), 2.15-2.87 (L = 10); at beta 2.6:
4.04-4.35 (L = 4), 21.97-23.71 (L = 8); at beta 6.0 within 1 percent.
Controls. (i) Code: 0.2984 and 0.4558 against row 944's 0.2991 and 0.4503 (0.3 and 1.2 percent): PASS, with an
independent implementation. (ii) Power: at beta 6.0, lambda(6)/lambda(4) = 3.25 against 3.375 for full order, at the
predicted momentum and polarization: PASS. The colour direction of the first step IS ordered at beta 6.0, as 5.1
predicted. (iii) Hot against cold at L = 6: 1.2 percent: PASS.
**Verdicts against the criteria of 5.2.**
- beta 2.3: G = lambda(10)/lambda(4) = 1.21 <= 1.3, and lambda is flat from L = 6 to 10 (2.55, 2.51, 2.46). No growth:
  (SC) and (SC-hor) survive u_xy at beta 2.3. But the level is 2.5, against 0.45 at u_pi and 0.30 at u = 1: the
  predicted mode is strongly enhanced, with a finite correlation length. In the units of (SC):
  beta^2 lambda - beta c = 13.2 - 1.2 = 12, so C_h is at least about 12 at beta 2.3 (GUIDE), and sigma^2 = C_h + beta about 14.
- **beta 2.6: lambda(8)/lambda(4) = 5.4 (full order would give 8), far above the criterion value 4, at the predicted
  mode. GUIDE: at beta 2.6 the first-step colour direction is ordered, or correlated over more than 8 lattice
  units, at u_xy; (SC) and (SC-hor) FAIL there with any constant of order one.** At L = 8, beta^2 lambda = 153.
- beta 6.0: full order. (SC) and (SC-hor) fail (GUIDE), C_h of order beta^2 (2/3) sin^2 theta L^3.
Reading (GUIDE). The window 2.3 to 2.6 contains, or borders, an ordering transition of the Dirichlet boundary
layer at the layered pi-flux slice. So (SC) is not only a genuine order-one statement: by this run it is FALSE in
the upper part of the window, at a slice that is as symmetric as a slice can be. What the run cannot show: whether
lambda at beta 2.6 saturates at some L above 8 (a long but finite correlation length), the half-space limit (T = 6
only), any other slice, and (SG-step) itself, which is 0 at u_xy by Lemma CEN.
Next (batch 3, criteria fixed here before it runs): u_xy at beta 2.6 with L = 6, 10, 12, a hot start at L = 8 and
T = 10 at L = 8; beta 2.4 and 2.5 with L = 4, 8, 12. At each beta: lambda(12)/lambda(8) >= 2 means growth persists (full
order: 3.375); <= 1.3 means saturation; otherwise inconclusive. Hot and cold, and T = 6 and T = 10, must agree
within 15 percent at L = 8, else I say "not equilibrated" or "slab thickness matters".

## 5.6 GUIDE results, compact U(1) control (batch 2; run 08:55-08:59Z under the numeric lock, 71 percent free)

Log `/tmp/gap-sc-950/logs/batch2.log`. Entries are lambda(L) for the scalar field E_l = sin(theta_l(1) - u_l); m_st is the
mean absolute staggered order parameter of the predicted mode.

| slice | beta | start | L = 4 | L = 6 | L = 8 | k of the max | m_st |
|---|---|---|---|---|---|---|---|
| u = 1 | 2.3 (Coulomb phase) | cold | 0.413 | | 0.430 | k near 0 | 0.03, 0.01 |
| u_xy | 2.3 | cold | 41.3 | 139.6 | 331.6 | (pi, pi, 0), (1, -1, 0) | 1.135, 1.137, 1.138 |
| u_xy | 2.3 | hot | | 139.8 | | (pi, pi, 0), (1, -1, 0) | 1.137 |
| u_xy | 0.9 (confined phase) | cold | 1.25 | | 1.11 | (pi, pi, 0), (1, -1, 0) | 0.16, 0.05 |

Against the criteria of 6.3. G_U1 = lambda(8)/lambda(4) = 8.03 at u_xy, beta 2.3, the exact volume ratio: the sign of the
staggered pattern is fully ordered (sin theta = 0.57), hot and cold starts agree. **GUIDE: compact U(1) in its Coulomb
phase FAILS (SC-hor), hence (SC), at the layered pi-flux slice**, with C_h of order 2 beta^2 sin^2 theta L^3. Control u = 1:
lambda = 0.41 to 0.43, flat, at the photon value 1/beta = 0.435 (PASS). In the confined phase (beta 0.9) there is no
growth (1.25, 1.11), as predicted.
Reading (GUIDE, with the ARGUED part marked). (a) The photon satisfies (SC) with C_F <= beta, but compact U(1)
does not: the failure is a compact, large-field effect that the Gaussian model FP of row 929 cannot see. So (SC)
is NOT group-blind in fact: it is an input that compact U(1) fails at weak coupling. (b) ARGUED (5.1): for U(1)
the two patterns are gauge inequivalent, so this order should also break (SG-step) itself near u_xy; for SU(2)
the same order is a gauge frame and does not. This run does not test (b).

## 5.7 GUIDE results, batch 3: where the layered pi-flux slice orders (run 08:59-09:17Z under the lock, 70 percent free)

Log `/tmp/gap-sc-950/logs/batch3.log`. SU(2), slice u_xy, T = 6, cold start unless noted. All maxima sit at
k = (pi, pi, 0) on the polarization (1, -1, 0), the predicted mode. (L = 4 and 8 at beta 2.3 and 2.6 are from batch 1.)

| beta | L = 4 | L = 6 | L = 8 | L = 10 | L = 12 | lambda(12)/lambda(8) | verdict (criteria of 5.5) |
|---|---|---|---|---|---|---|---|
| 2.3 | 2.03 | 2.55 | 2.51 | 2.46 | | (flat from 6 to 10) | saturation, level 2.5 |
| 2.4 | 2.74 | | 8.00 | | 7.57 | 0.95 | saturation, level about 8 (blocks 5.9 to 9.9) |
| 2.5 | 3.56 | | 16.42 | | 42.73 | 2.60 | growth persists |
| 2.6 | 4.19 | 11.34 | 22.62 | 41.59 | 64.87 | 2.87 | growth persists |

Controls at beta 2.6, L = 8: hot start 22.39 against cold 22.62 (1 percent, PASS); T = 10 gives 23.31 against 22.62 at
T = 6 (3 percent, PASS: the slab thickness does not matter at this precision).
Shape of the growth. lambda/L^3 at beta 2.6 is 0.0655, 0.0525, 0.0442, 0.0416, 0.0375 for L = 4 to 12. It fits
m2 + c/L with m2 = 0.024, c = 0.16 to within 3 percent at all five sizes: the form of a squared order parameter with
a Goldstone finite-size correction. At beta 2.5 the three sizes give m2 = 0.010, c = 0.18. (At beta 6.0, lambda/L^3 = 0.19.)
**Reading (GUIDE).** At the layered pi-flux slice the colour direction of the first-step electric field orders
between beta 2.4 and 2.5. Below, the susceptibility saturates (2.5 at beta 2.3, about 8 at beta 2.4: C_h at least about
12 and 45). From beta 2.5 up it grows with the box, on every box tried, in the way long-range order does.
So the window 2.3 to 2.6 is cut by a boundary-ordering transition near beta 2.45, and above it (SC) and (SC-hor)
have no box-free constant on the boxes tried.
**Caveat that the run cannot remove (small boxes).** At beta 2.5 to 2.6 a periodic box of side 8 to 12 is near or
below the deconfinement extent of the bulk theory (RECALLED lattice values: critical extent about 8 at beta 2.51 and
12 at beta 2.64). So part of the growth may be a small-volume effect, and the order may stop at a finite length on
the seed box, which is 500 lattice units and more. Batch 4 tests this at beta 2.5 and 2.45 on boxes up to 20.
Batch 4 criteria (fixed here, before it runs). beta 2.5: the fit above predicts lambda(16) = 86 and lambda(20) = 150 for
long-range order. Growth persists if lambda(20)/lambda(12) >= 2.5; saturation if <= 1.5; otherwise inconclusive.
beta 2.45, L = 8, 12, 16: growth if lambda(16)/lambda(8) >= 4; saturation if lambda(16)/lambda(12) <= 1.3.

## 7. What the kill test means, and what replaces (SC) (step 6, continued; by hand)

**7.1 At a central slice all of Hess F is gauge-frame fluctuation (Proposition FR; PROVED).** If every u_l is +-1, then
for every z in T_u M:
  Hess_M F(u)(z, z) = E_(pi_u)[ Var_(mu_(u,w))(beta <z, g.w>) ] - beta sum_l E_(pi~_u)<u_l, w'_l> |z_l|^2,    and phi_(u,z) = 0.
Proof. Identity TV (2.4) and row 944 Lemma CEN. QED
So the kill test measures only the fluctuation of the first-step temporal links given both slices. What orders at
u_xy is the gauge frame of the first step relative to the frozen slice. (SG-step) holds trivially AT u_xy.
Pointwise form: with row 944 (4.1), at a central slice
  Hess_u log p(u, w)(z, z) = [ Var_(mu_(u,w))(psi) - E_(pi_u) Var_(mu)(psi) ] - beta sum_l ( E_(mu_(u,w))<u_l, (g.w)_l> - E_(pi~_u)<u_l, w'_l> ) |z_l|^2,
psi = beta <z, g.w>. At w = u the frame law mu_(u,u) is the 3D O(4) ferromagnet exp(beta sum <g_x, g_(x+l)>), the same for
every central u, and for a divergence-free xi the statistic has no first-order spin-wave term, so its variance is
of order one (ARGUED). Then Hess_u log p(u_xy, u_xy)(z, z) is about -beta^2 lambda: row 944's pointwise form (HS) fails with
the same growth as (SC) (GUIDE + ARGUED).

**7.2 The group enters here (PROVED where marked).** At u_xy the two staggered patterns w_+-, with first-step angles
+-theta eps_l, are exchanged by charge conjugation.
- SU(2): w_- = c.w_+ for a constant c (a rotation by pi about an axis orthogonal to n). Charge conjugation is inner.
  The tie is a gauge frame; every gauge-invariant function takes the same value on both (PROVED).
- Compact U(1): the xy plaquette of w_+- has the phase pi +- 4 theta e_p, e_p = (-1)^(x+y), and Im U_p = -+ sin(4 theta) e_p is gauge
  invariant. So the two patterns are gauge INEQUIVALENT unless sin 4 theta = 0 (PROVED). The score is odd under
  charge conjugation, phi_(u,z)(w^*) = -phi_(u,z)(w) at a real slice (PROVED: p(u, w) = p(u, w^*), and z -> -z), and it
  does not vanish on an ordered pattern (ARGUED: the abelian frame is pinned near a constant by the temporal
  plaquettes, so the frame average keeps a fraction of beta sqrt(N') sin theta).
  With the sign order of 5.6 this gives Var_(pi_u)(phi_(u,z)) of order beta^2 sin^2 theta L^3 at u_xy: **compact U(1) in its
  Coulomb phase fails (SG-step) itself (GUIDE for the order, ARGUED for the frame factor), and the SU(2) chain
  cannot fail it this way.** The property U(1) lacks at this step: charge conjugation is a gauge transformation.
  In the confined phase of U(1) (beta 0.9) no order is seen.

**7.3 Consequence for the chain.** Row 944 reduced (SG-step) to (SC). By 5.5-5.7 (GUIDE) that reduction cannot be
used for beta >= 2.5: (SC), its horizontal form (SC-hor) of this note, and the pointwise form (HS) all grow with
the box at u_xy. For beta 2.3 and 2.4 they survive the slices tried, with large constants (C_h at least about 12 and
45), and a proof would have to be a statement about the absence of frame order, coupling by coupling. None of
this touches (SG-step), which never sees a gauge frame. So the input of the hypercontractivity chain should be
(SG-step) itself, in gauge-invariant form:
  (SG-step), gauge-invariant form: for every slice u and every unit horizontal z = (xi_l u_l)_l,
     phi_(u,z)(w) = beta sum_l <xi_l, Ebar_l(u, w)> - mean,   Ebar_l(u, w) := E_(mu_(u,w))[ Im P_l ],
     is sub-Gaussian under pi_u with a box-free proxy sigma^2.
Ebar is the first-step electric field averaged over the first-step temporal links, given BOTH slices. Its first
instance is the variance bound
  (SG2)  sup over u of || Cov_(pi_u)( Ebar ) ||_op <= sigma_2^2/beta^2   (box-free),
which by 3.2 is the reverse Poincare inequality |grad P f|^2 <= sigma_2^2 [P(f^2) - (P f)^2]. (Row 941's Proposition W
holds with beta^2 kbar_h replaced by sigma_2^2, by the same line: frames drop out of Cov_(pi~_u)(<z, w'>, f) when f is gauge
invariant. PROVED.) What can violate (SG2) or (SG-step): a tie between gauge-INEQUIVALENT next slices. At a
central slice phi = 0. So a violation needs a non-symmetric slice at a first-order transition of the gauge-invariant
data of the boundary layer (ARGUED). Whether one exists at beta 2.3 to 2.6 is not known; the frame order found
here shows that the boundary layer is close to ordering in this window, so it cannot be dismissed.

**7.4 The test for (SG2) (design only; not run).** Lagged covariance under frame-only dynamics. In the slab, a
time-independent gauge transformation g applied to all slices t >= 1 changes the weight only through
exp(beta <u, g.w_1>). Heat bath on g_x (von Mises-Fisher on S^3 with parameter
beta sum_i [ u_i(x) g_(x+i) w_i(x)^* + u_i(x-i)^* g_(x-i) w_i(x-i) ]), started at g = 1 for each sample. Put E^(n) := Im((g^(n).w_1) u^*).
Then C_n := Cov(E^(0), E^(n)) starts at the temporal-gauge covariance C_0 = Cov_u(E) and tends to Cov_(pi_u)(Ebar) as n
grows (PROVED: (1, w_1) is an exact draw of the frame given the orbit, the frame chain is ergodic on a compact
space, and E[E^(0) x E^(n)] = E[ E[E^(0) | orbit] x E[E^(n) | orbit, g^(0)] ]). (SG2) says the top eigenvalue of the limit is
box-free for every u. Slices to try first: non-central ones near a possible tie of invariant data, for instance
anisotropic deformations of u_pi and tilted copies of u_xy. For compact U(1) the same measurement at u_xy should
show a limit growing like L^3 (7.2).

**7.5 A first run of the test of 7.4 (GUIDE; batch 5; criteria fixed here before the batch).** Scripts
`/tmp/gap-sc-950/scripts/slab_proj.py` (SU(2)) and `slab_u1p.py` (U(1)). They follow only the tie-mode amplitudes
X_a = sum over x and y links of eps_l E_l^a/sqrt(2 L^3) (a = colour; the mean over a of E[X_a^2] is lambda_* of 5.2) and a control
Y_a (uniform mode on z links), at frame lags n = 0, 1, 2, 4, 8, 16, 32, 64. Slices: u_xy, and u_xy tilted by an angle
delta per link along the pattern in colour 3 (non-central; stabilizer U(1); X_3 is then the radial, horizontal mode
and X_1, X_2 are almost vertical).
- Validation (V): at u_xy, beta 2.3, L = 6, the raw lagged moment (1/3) sum_a <X_a^(0) X_a^(n)> must start near 2.5 and fall
  below 10 percent of that by lag 64 (Lemma CEN: the limit is exactly 0). If it does not, the frame chain is too
  slow or wrong, and I say so.
- SU(2), tilted slices at beta 2.6 (delta = 0.3 at L = 4 and 8; delta = 0.1 at L = 8) and beta 2.3 (delta = 0.3, L = 8): report
  lag 0 (temporal gauge) and lag 64 (projected). (SG2) survives these modes if the projected variances at L = 8
  are at most 1.3 times those at L = 4 and of order one; a ratio of 4 or more would refute (SG2) there.
- U(1) at u_xy, beta 2.3, L = 4 and 6: compact U(1) fails (SG2), hence (SG-step), if <X^(0) X^(64)> is at least half of
  <X^(0) X^(0)> and grows by a factor of 3 or more from L = 4 to 6.
Order of events: 8-sample smoke runs (outside the lock, a few seconds) were seen before these lines were written:
U(1) at L = 4 gave 41.5 at every lag; SU(2) at u_xy decayed from 6.1 to about 0 by lag 32 on one colour. So the
direction of the U(1) result was known; the SU(2) tilted-slice values and all L dependence were not.

## 5.8 GUIDE results, batch 4: boxes up to 20 (run 09:18-09:43Z under the lock, 71 percent free)

Log `/tmp/gap-sc-950/logs/batch4.log`. SU(2), u_xy, T = 6, cold start. Maxima at (pi, pi, 0), (1, -1, 0) in every run.
(This section and 5.5-5.7 belong to Section 5; they were appended in the order of the runs.)

| beta | L = 4 | L = 8 | L = 12 | L = 16 | L = 20 | lambda/L^3 | against the criteria of 5.7 |
|---|---|---|---|---|---|---|---|
| 2.5 | 3.56 | 16.42 | 42.73 | 81.79 | 144.0 | 0.056, 0.032, 0.025, 0.020, 0.018 | lambda(20)/lambda(12) = 3.37 >= 2.5: growth persists |
| 2.45 | | 11.86 | 24.89 | 39.96 | | 0.023, 0.014, 0.0098 | lambda(16)/lambda(8) = 3.37, lambda(16)/lambda(12) = 1.61: inconclusive |

Blocks: beta 2.5, L = 16: 76.9 to 87.0; L = 20: 99.7, 158.6, 156.3, 161.5 (the first quarter is still ordering after 1500
thermalization sweeps; the last three quarters give 159). beta 2.45, L = 16: 29.2, 30.8, 47.2, 52.6 (slow, critical-like).
The fit of 5.7 to L = 4, 8, 12 at beta 2.5 predicted 86 and 150; found 81.8 and 144 (159 without the first quarter).
**Reading (GUIDE).** At beta 2.5 the growth continues to L = 20, two and a half times the recalled deconfinement
extent, and it follows the long-range-order form m2 + c/L with m2 about 0.010. So the small-volume caveat of 5.7
does not explain it on the boxes that can be run here. At beta 2.45 the susceptibility grows like L^1.6 to L^1.8,
between saturation and volume growth: this is what a critical point of a three-dimensional O(3)-type order
looks like (lambda proportional to L^(2 - eta)). So the ordering coupling of this slice is beta_c(u_xy) = 2.45 to 2.5.
What stays unshown: boxes of the seed size (hundreds of lattice units), other slices, and any proof. A
correlation length far above 20 at beta 2.5 is not excluded by a run.
**Verdict on (SC) from 5.5-5.8 (GUIDE).** For SU(2) Wilson: at beta 2.3 and 2.4 (SC) and (SC-hor) survive the most
dangerous slice found, with C_h at least about 12 and 45. At beta 2.5 and 2.6 they fail at that slice on every box
from 4 to 20 (to 12 at beta 2.6), with lambda growing like the volume. The upper part of the window 2.3 to 2.6 is
therefore closed to the route "(SC) gives (SG-step)" of row 944, unless the growth stops beyond L = 20.
