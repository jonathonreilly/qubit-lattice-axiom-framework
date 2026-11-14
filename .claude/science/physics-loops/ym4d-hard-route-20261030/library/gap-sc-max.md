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
  slab). Its w_1-marginal has density proportional to e^(beta<u,w_1> - V(w_1)/2) (T_0^(n-1) e^(-V/2))(w_1), and
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
