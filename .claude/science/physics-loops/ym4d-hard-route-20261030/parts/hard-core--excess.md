lead: openai/gpt-6-astra/max macbook-codex
lease_until: 2026-11-02T12:00Z

# Excess: Lemma EX, Lemma EX2, (COMP)(ii)

Queue item 7 of `FINISH.md`, mapped side, frozen at commit `d9d4496f1`. Research-stage working state. Grants no status.

Started 2026-11-01T07:34Z. No read of `parts/hard-core--independent.md`, of any gate on it, or of the Sussman-Alpoge repository. Provenance: anthropic/claude-opus-5-5, effort max, Mac mini worker.

Repair session, 2026-11-01: source commit `0b13f39d269f19602ed3fee11fc146989029a8bb`, gate `gates/excess-codex-6c0d4e1c9.md`, mapped side. The lead lines identify the requested repair session; earlier numerical results retain their original provenance. This is an author repair, not an independent review or audit. No numerical computation was run in this session.

Weighted-comparison session, 2026-11-01: pinned source `216dcff7e69c1565c4a43d3cdb0a7ecc6341eb56`, mapped side, OpenAI Codex. Scope: H-W first, then only its dependent items if it closes. Stopped at item 1: a localized-weight obstruction to the unrestricted form, and the exact missing nonlinear comparison for the slow-weight form. Details: `library/excess-weighted-fibre-stop.md`. No Lemma EX proof is changed. This is a bounded author investigation, not an audit or independent gate. No numerical computation was run; earlier numerical results below belong to their original sessions.

Consumer-weight continuation, 2026-11-01: pinned source `8e7fd0a79b46f32924c1bd85574efa13c34a827b`, OpenAI Codex, mapped side. The live record is `library/excess-consumer-weight-continuation.md`; this part remains the recovery checkpoint. Bounded author work, no independent review, audit or numerical run. The user explicitly excludes other parts, gates on the independent attempt, commits, pushes and subagents. Lemma EX and its proofs are preserved.

## 0. Summary

**The lower-bound proofs retain the earlier support repair and are unchanged in the 216dcff7e and 8e7fd0a79 sessions.** The gate rates Lemma EX and its local ingredients ADVANCE. Section 1.7 uses the smaller coordinate rectangles in LE/TL and defines the fine-level W^+ by centred parent blocks, which repaired finding 3 without increasing its radius two. No proof rated ADVANCE was revised. A weight-bookkeeping correction is recorded separately below: compatible down-averages can have jumps that do not shrink with depth; EX-loc permits these, while FALL's shrinking rate belongs to sampled smooth weights.

**Finding 2 is repaired for LIFT and the trial upper bound.** `library/excess-finite-range-repair.md` proves the actual finite-range derivative estimate and its inverse with a kernel q^floor((d-a)_+/R) on squared flux, including the initial support enlargement. Normalised kernel moments, T1--T3 and the L gains survive. TOP-1 is conditional on item (o)'s class-minimality identification and the explicit threshold check (CLASS); the trial estimate itself is discharged. Constants are chosen in the order L, then flux/a_*, then x. No numerical L_0 is certified.

**H-W for the consumer weights stops at uniform endpoint coverage.** The arbitrary-weight obstruction in `library/excess-weighted-fibre-stop.md` remains: the minimizer has a linear far tail while the trial's K_q tail vanishes with flux. The consumers instead read slow exponential profiles, their enlargements and compatible descendants. The 8e7fd0a79 continuation constructs a genuine parent-fixed chart containing both endpoints near the trivial field on each fixed finite lattice, with the exact fibre derivative and a finite secant estimate. It does not establish a chart radius or relative-log bound free of depth and volume on the whole small-flux class. That is (END), the first stop. The subsequent uniform (SEC-unif) and inverse response (TRIAL-J) remain gaps. Theorem F's tangent inverse and AN3's parent-varying minimizing branch do not give these finite-displacement statements.

**Dependent claims remain conditional; the constant-order conflict is resolved.** HC-W and depth-free CJ/CR were not examined past the H-W stop. Rename the upper-excess coefficient C_TOP(L): the pre-L C_T in the closure list is Lemma TE's rough-cell counting constant, not the TOP coefficient, which `sector-values.md` calls C(L) or C_Y. A finite depth-uniform C_TOP(L) is enough for FALL and the active DS closure's constants graph, but no such estimate is proved here. COMP-ii-g remains a scalar implication of TOP-W and cubic decay on levels 1..k. Those are also exactly the argument levels of DS's source sum; its use of FALL does not ask for a bare-level-0 term.

**Finding 1 and the missing variance estimate have conditional repairs.** `library/excess-root-frame-repair.md` retains every constant root-rate term, bounds its weighted square by C(L)s^2 f^2 using A2, and proves the local box-Poincare bound (VP-W) needed to use A4. Lemma EX2-r follows under A1-r--A4-r in the specified one-level contour gauge, at output rate at most kappa/28 with the required growing response weights stated. It is a summability result; these hypotheses for the minimiser are not discharged. The pinned Prop DS now uses FALL/CRUDE/LAN rather than EX2; Section 5.4 states its exact conditional interpolation and the remaining inputs.

**Current checkpoint (8e7fd0a79 session, stopped).** See `library/excess-consumer-weight-continuation.md`. Step 1 identifies the weights, fixes their jump/sampling distinction and restates TOP only for that family. Step 2 supplies TRUE-CH/TRUE-J/SEC-fin on the finite local branch and stops at the exact uniform inequalities END, SEC-unif and TRIAL-J. EX-loc plus global minimality alone does not localize the upper budget: an exact two-site variational countermodel demonstrates the failed inference, not a Yang--Mills counterexample. A localized admissible competitor proving LOC-MIN remains a live alternative. Step 3 and dependent item 5 were not attempted across that stop. Independent step 4 separates C_TE from C_TOP(L) and checks the active closure's constant dependencies. The earlier support, trial, scalar-iteration and root-frame work retains its stated premises, including item (o). Prior failed routes remain on record: arbitrary-weight K_q comparison, tangent inverse used as a nonlinear comparison, fast squared tail, class-threshold omission, curvature-only root rates, gradients used as variances, the invalid q-bar choice, and extrapolation to DS. Shrinking flux cannot absorb a bare linear C(L), but the active consumer does not require that loss to be absolute. Source identities and mechanical checks are in `checks/excess-codex/`; no numerical computation, independent gate or audit was run.

## 1. Lemma EX: a proof with no symbol, no IMS and no toron term

*Label carried from the original author: discharged at the level of a written proof; the named research gate subsequently rated these lower-bound arguments ADVANCE, not an audit. Reads the definition of the block map and nothing else: not Theorem F-D, not Prop AN3, not the lift's minimality, not c_e.* Checks: `checks/excess/v1_identity.py`, log beside it, criteria T0 to T4 in `checks/excess/CRITERIA.md`, written first, all PASS at the first run on the comb map of `checks/gate_ex/ex_core.py`, SU(2), d = 4, L = 3 (T0 also L = 5).

### 1.1 Setting

Level-j lattice with unit spacing, torus of side n = L N', any N' >= 1, L odd; the parent lattice is (L Z / n Z)^4. *Every local step below is read on the universal cover of the torus*, where the field is periodic and a box has an axial gauge. So the size of the torus enters nowhere, and a holonomy around it plays no role: it only says two lifts of a site carry the same data up to a rotation. U is a level-j field, V' := M(U) its Balaban average (the deterministic map; class fields carry no rough label). theta_{mu nu}(z) := log of the plaquette at z, with theta_{nu mu} = -theta_{mu nu}. In the normalisation U = exp(i t . sigma), |Ad(e^theta) - 1| <= 2 |theta|. flux := max |theta|. E(U; W) := sum_{z, mu < nu} W(z) |theta_{mu nu}(z)|^2.

W > 0 with |log W(x) - log W(x')| <= nu |x - x'|_inf / L, nu <= 1/8. So nu is the rate in parent cells. S_e Phi(x) := Ad(V'_e(x)) Phi(x + e), with e a parent unit, is orthogonal on l^2, and grad_e := S_e - 1. I^grad(V'; W) := sum_{x, p, e} W(x) |grad_e theta'_p(x)|^2. Split it as P(W) + T(W): P the in-plane terms, e in {mu, nu} for p = (mu, nu); T the transverse ones.

**Kernels.** tau(t) := #{a in [-r, r] : a <= t <= a + L - 1}, r := (L - 1)/2: the discrete tent, with sum_t tau(t) = L^2, tau(t) + tau(t - L) = L on its range. For orientation (mu, nu) and a parent site y,

    chi_y(z) := L^-6 tau(z_mu - y_mu) tau(z_nu - y_nu) 1[|z_rho - y_rho| <= r] 1[|z_sigma - y_sigma| <= r].

**Lemma K.** (a) sum_z chi_y(z) = 1. (b) sum_y chi_y(z) = L^-4 for every z, and 0 <= L^4 chi_y <= 1. (c) Abelian, for any bond angles a with curl da: the Q-image of a has parent curl exactly L^2 <da>_{chi_y}. (d) For y' := y + L e_mu, min(chi_y, chi_{y'}) has mass eps_L := (1 - L^-2)/4 >= 2/9.

*Proof.* (a), (b): products of one-dimensional sums, using sum_{y_mu} tau(t - y_mu) = L. (c): Lemma 3.1 of the producer removes the contours from the curl, and the curl of Q_path over a parent plaquette is avg_{x in B(y)} of the sum of da over the L x L square at x. Counting x for each fine plaquette gives chi_y. (d): the two kernels differ only in the factor tau along mu, and sum_t min(tau(t), tau(t - L)) = (L^2 - 1)/4. QED. (T0 checks all four.)

### 1.2 The local expansion

Box(y) := y + [-2 L, 3 L]^4 on the cover, and n_y := sum over plaquettes in Box(y) of |theta|^2. On a small torus a plaquette occurs at most 6^4 times in Box(y), which only changes C(L).

**Lemma LE.** *There are a_0(L) := c/L and C(L) such that in any gauge on the paths of the parent plaquette at y with all fine links |log U_b| <= a <= a_0:*

    | theta'_{mu nu}(y) - L^2 <theta>_{chi_y} | <= C L^2 a^2,    theta := the plaquette angles in that gauge.

*In the axial gauge rooted at y, a^2 <= C L^3 n_y provided flux <= phi_0(L) := c L^-4.*

*Proof.* Write U_b = e^{a_b}. For a path of at most C L bonds, |log(prod e^{a_b}) - sum +- a_b| <= C (L a)^2. Applied to Omega_x := Gamma_{y,x} . line_x . (Gamma'_{y',x'})^-1 and to Omega_0: v_x = log(Omega_x Omega_0^-1) = omega_x - omega_0 + O(L^2 a^2), with omega_x the abelian sum along the path. With A := avg_x v_x and V'(c) = e^A Omega_0: log V'(c) = avg_x omega_x + O(L^2 a^2), of size at most C L a. The same BCH step over the four sides gives theta' = curl of the Q-image of a + O(L^2 a^2), and the curl is L^2 <da>_{chi_y} by Lemma K(c). On a fine plaquette da = theta + O(a^2), and chi_y has mass 1, so this changes the right side by O(L^2 a^2). If the contour is an average over orders, as in Lemma 3.1, the same holds, as each step is an average of bounds. Axial gauge: a link's angle is the holonomy of a loop on a strip S(b) of at most C L^3 plaquettes, and it is at most sum_{S(b)} |theta_p| by the geodesic triangle inequality and conjugation invariance. Cauchy-Schwarz. QED

*Numerics, T2.* max |r_y| scales as t^2 (2.38e1, 2.38e1, 2.44e1 at white-noise amplitude t = 0.04, 0.02, 0.01; 4.4, 4.3 at smooth t = 0.2, 0.1), and max |r_y| / n_y is 0.0093 (white), 0.117 (smooth), stable. So no missed linear term.

### 1.3 The variance identity

Fix y and an orientation, and let theta^{(y)} be the plaquette angles transported to y in the axial gauge at y; |theta^{(y)}_p| = |theta_p|, as the axial transport is an isometry. m_{y,p} := <theta^{(y)}_p>_{chi_y}, sigma_{y,p}^2 := Var_{chi_y}(theta^{(y)}_p), r_{y,p} := theta'_p(y) - L^2 m_{y,p}.

**Theorem V (exact).** *For W = 1,*

    E(U) - E(V') = sum_{y, p} L^4 sigma_{y,p}^2 - sum_{y, p} ( 2 <theta'_p(y), r_{y,p}> - |r_{y,p}|^2 ).

*Proof.* By Lemma K(b), sum_z |theta(z)|^2 = sum_y L^4 <|theta^{(y)}|^2>_{chi_y} = sum_y (L^4 |m_y|^2 + L^4 sigma_y^2). And L^4 |m_y|^2 = |theta' - r|^2. QED

In the abelian case r = 0, so **the excess is exactly a sum of local variances, for every field in the fibre**. This is the positivity behind (TS), and it needs no minimality: T1 holds to 1.4e-15 relative, T2's identity to 1e-12 on non-abelian fields.

### 1.4 The in-plane gradient

Let V(W) := sum_{y, p} W(y) L^4 sigma_{y,p}^2. Let n_y^+ := the sum of n_{y''} over parents y'' with |y'' - y|_inf <= L.

**Lemma IP.** *If flux(U) <= phi_0(L) (shrunk below), then P(W) <= (64 e^{nu} / (1 - L^-2)) V(W) + C(L) sum_y W(y) n_y^+ (f^2 + n_y^+), with f the flux of V'.*

*Proof.* Let y' := y + L e_mu with mu in the plane, G the axial gauge at y on the union of the two regions, a its link bound, and G' the axial gauge at y'. In G: V'_mu(y) = exp(O(L a)), and Lemma LE at y and at y' gives

    grad_mu theta'(y) = L^2 (m'_G - m_G) + (r' - r) + (Ad(V'_mu(y)) - 1) theta'(y'),

with m_G = m_{y}, m'_G the chi_{y'}-mean of theta in gauge G. For two laws mu_1, mu_2 on the same points with common part nu of mass eps, and any vector function F, |<F>_1 - <F>_nu/eps|^2 <= Var_1(F)/eps. So by Lemma K(d),

    |m_G - m'_G| <= eps_L^{-1/2} ( sigma_y + sigma'_G ),    sigma'_G^2 := Var_{chi_{y'}}(theta in gauge G).

G and G' differ by g(z) with g(z) = g_0 (1 + O(L (a + a'))), g_0 constant, and a constant rotation does not change a variance. So sigma'_G <= sigma_{y'} + C L (a + a') <|theta|^2>_{chi_{y'}}^{1/2}. With L^4 chi <= 1 and a^2 + a'^2 <= C L^3 n_y^+:

    |grad_mu theta'(y)| <= L^2 eps_L^{-1/2} (sigma_y + sigma_{y'}) + E_y,    E_y^2 <= C(L) n_y^+ (f^2 + n_y^+).

Square, using (s + t)^2 <= 2 s^2 + 2 t^2 and (sigma + sigma')^2 <= 2 sigma^2 + 2 sigma'^2. Each sigma_{y,p}^2 occurs for two in-plane directions, at y and at y'; and W(y) <= e^nu W(y'). QED

**Lemma NN (no flux bound on the lift is needed).** *With flux(U) <= phi_0(L): sum_y W(y) (n_y^+)^2 <= C(L) ( f^2 sum_y W(y) n_y^+ + phi_0^2 V(W) ).*

*Proof.* By Lemma K(b), n_y^+ <= sum_{y'' near y, q} L^4 <|theta_q|^2>_{chi_{y''}} = sum (L^4 sigma_{y'',q}^2 + |theta'_q(y'') - r_{y'',q}|^2) <= t_y + C f^2 + C(L) sum_{y'' near y} n_{y''}^2, with t_y := the variance sum near y, and C(L) n_{y''} <= C(L) phi_0^2. Multiply by W(y) n_y^+ and sum, using n_y^+ <= C(L) phi_0^2 on the t_y term and 2 n n'' <= n^2 + n''^2 on the last. For phi_0(L) small, that last term is at most half the left side. QED

### 1.5 The transverse gradient: a lattice Bianchi inequality

**Lemma BT (any lattice gauge field, sharp).** *Let V be a field of flux f <= 1/6. Then with absolute C*

    T(W) <= (2 + 8 kappa) P(W) + C (f + kappa) E(V; W),    kappa := sup |w(x + e)/w(x) - 1|,  w := W^{1/2}.

*At W = 1 this is T <= 2 P + 8 f E + C f^2 E, and the constant 2 is sharp: T4 gives T/P = 2.0 for the plane wave p = (1,1,1,0), a = e_4.*

*Proof.* W = 1 first. Fix distinct mu, nu, rho and put a := theta_{mu nu}, b := theta_{nu rho}, c := theta_{rho mu}.

*Bianchi.* B := grad_rho a + grad_mu b + grad_nu c obeys |B(x)| <= C sum_{faces} |theta|^2. In the tree gauge of the 3-cube at x, rooted at x, with the three bonds at x in the tree, the five non-tree bonds have angle at most sum_faces |theta|. So every Ad in B is 1, and each face angle is the signed sum of its bond angles up to O(|a|^2), and the linear parts cancel by d^2 = 0.

*Expansion.* ||grad_rho a||^2 + ||grad_mu b||^2 + ||grad_nu c||^2 = ||B||^2 - 2 <grad_rho a, grad_mu b> - 2 <grad_mu b, grad_nu c> - 2 <grad_nu c, grad_rho a>.

*Swap.* Let grad-bar_e := 1 - S_e^-1, so ||grad-bar_e X|| = ||grad_e X||. Since (S_e)^* = S_e^-1,

    <grad_rho a, grad_mu b> = <grad-bar_mu a, grad-bar_rho b> + <a, [S_rho^-1, S_mu] b>.

[S_rho^-1, S_mu] b(x) = (Ad(P_1) - Ad(P_2)) b(x + e_mu - e_rho), and P_1 P_2^-1 is the plaquette at x - e_rho in the plane (mu, rho), conjugated. So its norm is at most 2 |theta_{mu rho}(x - e_rho)| |b(x + e_mu - e_rho)|, and the last term is at most 2 f ||a|| ||b||.

*Count.* The first term is a product of in-plane derivatives: mu lies in the plane of a, rho in the plane of b. So 2 |<grad_rho a, grad_mu b>| <= ||grad_mu a||^2 + ||grad_rho b||^2 + 2 f (||a||^2 + ||b||^2), and the same for the other two pairs, with (grad_nu b, grad_mu c) and (grad_rho c, grad_nu a). So

    T_{mu nu rho} <= P_{mu nu rho} + ||B||^2 + 4 f (||a||^2 + ||b||^2 + ||c||^2).

Each of the 12 transverse terms lies in one triple; each of the 12 in-plane terms in two; each orientation in two. Sum over the four triples.

*Weight.* Apply the same to (w a, w b, w c). The derivation reads only that S is orthogonal, the commutator bound, and the size of B^w := grad_rho(w a) + grad_mu(w b) + grad_nu(w c), and grad_e(w a) = w grad_e a + (w(x + e) - w(x)) S_e a gives ||B^w||^2 <= 2 ||w B||^2 + C kappa^2 E(W), and the comparison of ||w grad_e a||^2 with ||grad_e (w a)||^2 up to factor 1 + kappa and error 4 kappa ||w a||^2. QED

T3: B^2 / (f^2 E) = 0.31 (white), 0.38 (smooth), stable, and T - 2 P < 0 on every field run.

### 1.6 Theorem EX

**Theorem EX.** *There are an absolute c_1 > 0 (c_1 = 1/810 is allowed for all odd L >= 3 and nu <= 1/8) and phi_0(L), C(L) such that for every level-j field U with flux at most phi_0(L), V' := M(U), f := flux(V'), and W as in 1.1:*

    E(U; W) - E(V'; W) >= c_1 I^grad(V'; W) - C(L) (f + nu) E(V'; W).

*There is no toron term, no condition on the sector, and U need not be minimal. In particular this is Lemma EX of `library/sector-values.md`, with U := V^*(V'), at every level, in the stronger form with the toron term deleted, once T_2 <= phi_0(L). The Wilson form follows, as E - A^W is quartic.*

*Proof.* X := E(U; W), Y := E(V'; W). By Lemma K(b) and W(z) >= e^{-2 nu} W(y) on supp chi_y,

    X >= e^{-2 nu} sum_{y, p} W(y) L^4 <|theta_p|^2>_{chi_y} = e^{-2 nu} ( Y'' + V(W) ),    Y'' := sum W(y) L^4 |m|^2.

By Lemma LE, Y - Y'' = sum W(y) (2 <theta', r> - |r|^2) <= 2 f C(L) sum W(y) n_y <= C_3(L) f X. So X (1 + C_3 f) >= e^{-2 nu} (Y + V(W)). With kappa' := 2 nu + C_3 f <= 1/2: X >= (1 - kappa') (Y + V(W)), that is

    e := X - Y >= (1 - kappa') V(W) - kappa' Y,    so V(W) <= 2 e + 2 kappa' Y.

Lemmas IP and NN, with phi_0 small, give P(W) <= 100 V(W) + C_4(L) f^2 X. Put X = Y + e and C_4 f^2 <= 1: e >= P(W)/201 - C(L) (f + nu) Y, in both signs of e. Lemma BT, with kappa <= nu: I^grad = P + T <= (3 + 8 nu) P(W) + C (f + nu) Y. So e >= (1/(603 + 1608 nu)) I^grad - C(L) (f + nu) Y, and 603 + 1608/8 = 804. QED

**What this settles from the gate.** D4: there is no toron term to define at this lemma. D6, D7, X1 to X5: moot, no Plancherel or hypercubic average is used. R1 is no longer needed. "c_e > 0 over all P": no longer read by Lemma EX. An identification, by hand, not needed below: for a plane wave F of small momentum the kernel variance is (1 - L^-2)/12 times (|P|^2 + P_mu^2 + P_nu^2) on the component F_{mu nu}, the box directions giving the first term and the extra width of the tents the second. Summing over components gives **the gate's limit formula (g - 1)/|P-hat|^2 = 2 c (1 + sum p^4 + sum a^2 p^2), so that formula is the variance of the kernel**.

**"Not a defect, but worth knowing", revisited.** The lemma still says little where I is of the order of f E, as for an instanton of any radius. That is a fact about the sizes, not about the proof. The sum over levels there is carried by the fall of f.

### 1.7 A pointwise form, with compatible weights

Lemma BT needs a global integration by parts, and its weighted form carries an energy term. That term cannot be removed from Lemma BT: F := x_3 dx_1 dx_2 - x_1 dx_2 dx_3 is closed with zero in-plane gradient and non-zero transverse gradient. So a local bound has to use the fine field. It does, and then it is pointwise.

**Compatible weights.** Let W^q >= 0 on parent sites, one function for each orientation q. Define the down-average W^{q,down}(z) := sum_y L^4 chi_y^q(z) W^q(y) and

    e(W) := sum_{z, q} W^{q,down}(z) |theta_q(z)|^2 - sum_{y, q} W^q(y) |theta'_q(y)|^2.

Lemma K(b) gives, with no Lipschitz condition and no error,

    e(W) = sum_{y, q} W^q(y) ( L^4 sigma_{y,q}^2 - 2 <theta'_q(y), r_{y,q}> + |r_{y,q}|^2 ).        (V_W)

Starting from W_k on top sites and defining W_j := (W_{j+1})^down, the chain sum is exact: sum_{j<k} e_j(W_{j+1}) = E_0(U; W_0) - E_k(V; W_k), with no quadrature error. If W_k is log-Lipschitz at rate nu in top cells, then W_j / W_k stays in [e^{-3 nu}, e^{3 nu}] on the cell below, and over a bounded number of level-j cells W_j changes by a factor e^{C nu L^{j-k}}: a jump at a block face of a box direction is allowed, and it is all that is read.

**Lemma TL (pointwise bound on the parent gradient).** *Let Y_1(y) := {y, y + L e_a : a = 1..4}, flux(U) <= phi_0(L), D(y) the union of the regions of the parents in Y_1(y), n_y^+ the fine energy on D(y), and Theta_y the largest |theta'| on the plaquettes at the sites of Y_1(y) and on the faces of the parent cubes at y. For every orientation q and direction e,*

    |grad_e theta'_q(y)| <= 3 L^2 sum_{six terms} sigma_{y'',q'} + C(L) ( n_y^+ + Theta_y (n_y^+)^{1/2} + Theta_y^2 ),

*the six terms having y'' in Y_1(y): for e in the plane q they are sigma_{y,q}, sigma_{y+Le,q}; for e = rho transverse to q = (mu, nu) they are sigma^{mu nu} at y, y + L e_rho, sigma^{nu rho} at y, y + L e_mu, and sigma^{rho mu} at y, y + L e_nu.*

*Proof, abelian.* In-plane: Lemma IP's two lines. Transverse: put w := ceil(L/4), so w/L <= 2/5 and L/w <= 4. Write b_y(t) := L^-1 1[|t - y| <= r], tau_y := L^-2 tau(. - y), so tau_y = b_y * c with c := L^-1 1_{[0, L-1]}, and tau_y(t - 1) - tau_y(t) = L^-1 (b_{y+L}(t) - b_y(t)). Let t_0 := y_rho + r, the top of the tent tau_{y_rho}. Let phi(t) be the chi^{mu nu}_y-mean of F_{mu nu} given z_rho = t, so m^{mu nu}(y) is the b_{y_rho}-mean of phi and m^{mu nu}(y + L e_rho) the b_{y_rho + L}-mean. Compare with the two windows of w layers on either side of t_0: A_0, A_1 the means of phi over [t_0 - w + 1, t_0] and [t_0 + 1, t_0 + w]. Conditioning on a window has density at most L/w against chi, so

    |A_0 - m^{mu nu}(y)| <= (L/w)^{1/2} sigma^{mu nu}_y,    |A_1 - m^{mu nu}(y + L e_rho)| <= (L/w)^{1/2} sigma^{mu nu}_{y + L e_rho}.

Next A_1 - A_0 = sum_t kappa(t) (phi(t + 1) - phi(t)), kappa the tent of height 1 and mass w at t_0. Closedness of F at each fine cube and summation by parts in z_mu and in z_nu give

    phi(t + 1) - phi(t) = -L^-1 ( psi^{nu rho}_{y + L e_mu}(t) - psi^{nu rho}_y(t) ) - L^-1 ( psi^{rho mu}_{y + L e_nu}(t) - psi^{rho mu}_y(t) ),

where psi^{nu rho}_y(t) is the chi^{nu rho}_y-mean of F_{nu rho} given z_rho = t, and likewise psi^{rho mu}. Under both chi^{nu rho}_y and chi^{rho mu}_y the law of z_rho is tau_{y_rho}, with tau_{y_rho}(t) = (L - |t - t_0|)/L^2 on the support of kappa. So kappa/w has density at most (4/3) L/w against it, and with Delta_a the flat difference by L e_a,

    A_1 - A_0 = -(w/L) ( Delta_mu m^{nu rho}(y) + Delta_nu m^{rho mu}(y) ) + O( (4 w/(3 L))^{1/2} (four sigmas) ).

This alone would be the coarse Bianchi identity with a factor. The gain is that the coarse Bianchi identity also holds, Delta_rho m^{mu nu} + Delta_mu m^{nu rho} + Delta_nu m^{rho mu} = 0. Substituting,

    (1 - w/L) Delta_rho m^{mu nu}(y) = O( (L/w)^{1/2} (two sigmas) ) + O( (4 w/(3 L))^{1/2} (four sigmas) ).

Multiply by L^2. The coefficients are at most 3 for all odd L: (1 - w/L)^-1 (L/w)^{1/2} <= 2.7, (1 - w/L)^-1 (4 w/(3 L))^{1/2} <= 1.3, eps_L^{-1/2} <= 2.2.

*Proof, non-abelian.* Work in the axial gauge G at y on D(y), links at most a, a^2 <= C L^3 n_y^+. (1) Fine Bianchi: the flat sum of the three differences at a fine cube is E(z), |E(z)| <= C a N(z)^{1/2} + C N(z), N(z) the energy of the cube, as Ad(U_e) - 1 has norm at most 2 a. This adds at most C(L) n_y^+ to L^2 (A_1 - A_0). (2) Coarse Bianchi in G: the flat sum x_1 + x_2 + x_3 of parent differences is at most C L a Theta_y + C Theta_y^2, by the Bianchi step of Lemma BT, as the parent links in G have angle at most C L a. (3) Lemma LE at the parents involved replaces L^2 m by theta' up to C L^2 a^2. (4) Each sigma in G against the same sigma in its own axial gauge, and grad_e against the flat difference in G: as in Lemma IP, at most C L (a + a'') (n_y^+)^{1/2} and C L a Theta_y. QED

*Numerics, T7* (criteria written first; `checks/excess/v7_local.py`). Every y, every triple, L = 3, 5, abelian and SU(2), white noise and smooth: no violation; largest left/right ratio 0.21 (transverse), 0.43 (in-plane), level in the amplitude.

**Theorem EX-loc.** *Put W^-(y) := min of W^{q'}(y'') over q' and y'' in Y_1(y), W^+ := the largest value of W at parent distance at most 2 blocks, and cub(V; W) := sum W |theta|^3. For flux(U) <= phi_0(L), every W >= 0, and V' = M(U):*

    e(W) >= c_1 I^grad(V'; W^-) - C(L) ( cub(V'; W^+) + cub(U; W^+) ),    c_1 := 1/3500, absolute.

*There is no Lipschitz condition on W, no term in E, no toron term.*

*Support convention (gate finding 3, discharged).* For this local theorem use, in place of the oversized Box(y), the coordinate rectangle with in-plane coordinates [-r,L+r] and transverse coordinates [-r,r], translated by y. The contour paths, straight lines and coordinate-comb fillings used in LE stay in this rectangle: successively filling a coordinate strip never leaves the coordinate intervals of its boundary. Hence the same finite-dimensional LE estimate holds with its energy and another C(L). For TL take the union of the six such rectangles at the parents specified there, together with the intervening cube faces. Every fine plaquette in this union has its centred parent block within two blocks of y. On fine plaquettes W^+ means the maximum over all parent orientations and parents within two blocks of that centred parent block. This is a support statement, requiring no comparison of distinct values of W.

*Proof.* Square Lemma TL, with (A + B)^2 <= 2 A^2 + 2 B^2 and six terms: |grad_e theta'_q(y)|^2 <= 108 L^4 (sum of six sigma^2) + errors. There are 96 slots per site, 16 per orientation after the sum over y, so I^grad(V'; W^-) <= 1728 V(W) + C(L) sum W^- (n_y^+ + Theta_y (n_y^+)^{1/2} + Theta_y^2)^2, using the restricted energies just defined. Finite overlap, |theta| <= 1 and Young bound the last sum by C(L) (cub(V'; W^+) + cub(U; W^+)). In (V_W), |r_{y,q}| <= C(L) n_y with the restricted rectangle, and |theta'| n_y <= C(L) sum over that rectangle of (|theta'|^3 + |theta_p|^3). Every weight is dominated by the stated W^+ at the plaquette charged. QED

*Reading.* The right side has the *fine* cubic energy, which is the natural form on a chain, where it is geometric in the level. For W = 1 and flux(U) <= C f this gives Theorem EX back in the printed form, with a worse c_1.

## 2. A one-level lift with a gain, and Lemma TOP at W = 1

*Label: the abelian kernels are carried as discharged; the non-abelian inverse and its corrected tail are proved below with soft nonlinear constants C(L), as a new author repair not independently checked. It reads the map, and class minimality (item (o) of `library/relative-density-bound.md`) only to say A_k(V) <= E_0 of a class chain in the fibre. No Prop AN3, no Theorem F, no cut field.* Needed because an upper bound on Y_k is the input of the sum over levels, and the printed Lemma TOP reads Prop AN3 and Taylor at cut fields, which is where the toron term came from. Numerics: T8, T9 and follow-up, `checks/excess/v8_lift1d.py`, `v9_lift4d.py`, `v9b_follow.py`.

### 2.1 The abelian lift is a tensor product

The abelian block map is a tensor of two one-dimensional maps. On functions, R^0 g(y) := avg_{x in I(y)} g(x), I(y) := [y - r, y + r], y in L Z. On bonds, R^1 a(y) := avg_{x in I(y)} sum_{s < L} a(x + s). Then R^1 d = d' R^0, and Q_path on component mu is R^1 in direction mu and R^0 in the others. On the component F_{mu nu}, L^2 <.>_{chi_y} is R^1 R^1 R^0 R^0.

**A right inverse that is a chain map.** Let xi(x) := N(x/L), N the cubic B-spline, so sum_y xi(x - y) = 1 and sum_y y xi(x - y) = x. Let beta(x) := c_L (1 - (2 x/(L + 1))^2)^2 on I(0), zero elsewhere, with R^0 beta(0) = 1. Put

    T^0 omega' := Xi omega' + sum_y beta(. - y) ( omega'(y) - R^0 Xi omega'(y) ),    Xi omega' := sum_y omega'(y) xi(. - y).

So T^0 omega'(x) = sum_y zeta_y(x) omega'(y), with range at most 4 L. *Properties.* R^0 T^0 = id, by construction. T^0 reproduces affine functions: Xi does, and R^0 of an affine function is itself on a centred block, so the correction vanishes. |grad zeta_y| <= C/L and |grad^2 zeta_y| <= C/L^2, C absolute: zeta_y is a bounded combination of a finite number of samples of fixed C^{1,1} profiles at scale L. Define T^1 by T^1 d' = d T^0: its kernel is eta_c(x) := sum_{y'' >= y + L} (zeta_{y''}(x + 1) - zeta_{y''}(x)) for c = (y, y + L), compactly supported as sum_y zeta_y = 1, with sum_c eta_c(x) = 1/L, |eta_c| <= C/L, |grad eta_c| <= C/L^2. And R^1 T^1 d' = R^1 d T^0 = d' R^0 T^0 = d', so R^1 T^1 = id.

**d = 4.** T_0 := T^0 in all axes. T_1 on component mu: T^1 in mu, T^0 in the others. T_2 on the component (mu, nu): T^1 in mu, nu, T^0 in the others. Then d T_1 = T_2 d', Q_path T_1 = id, and L^2 <T_2 theta'>_{chi_y} = theta'(y). Constants lift to L^-2 times themselves. Since T_2 reproduces constants, for z near y,

    |T_2 theta'(z) - L^-2 theta'(y)| <= C L^-2 max_near |Delta' theta'|,    |grad T_2 theta'(z)| <= C L^-3 max_near |Delta' theta'|.        (K)

*Numerics.* T8 identities to 1e-14 at L = 3 to 21, and T9: chain map to 1e-15, constant flux to 12 digits. **Two clauses of mine failed as registered:** L^2 |grad eta| rose 39 percent from L = 9 to 21, and C_2 := I^grad(fine) L^2 / I^grad(parent) rose by a factor 1.8 from L = 3 to 5. The rule was a guess at when these level off. Follow-up, declared after that result: L^2 |grad^2 zeta| = 15.7, 20.1, 21.8 at L = 41, 101, 201, so it levels off, as the proof says it must. C_2 = 9.5, 16.9, 23.0, 27.9, 36.4 at L = 3, 5, 7, 9, 13 on random parents, with C_2/L = 3.2, 3.4, 3.3, 3.1, 2.8 falling and local power 0.72 at the end. So C_2 was still rising at L = 13 on these parents. T12 settles it, by the tensor structure, all aliases, sup over P, closedness not used, so an upper bound: C_2 = 16.5, 27.3, 35.3, 42.8, 56.5, 77.5, 105.5, 126.1 at L = 3, 5, 7, 9, 13, 21, 41, 81, with falling increments, and C_1 = 0.63 to 1.62. So **C_2 L^-2 is below 1 from L = 7 and below 1/2 from L = 11 or so, for this choice of beta**, up to the non-abelian terms, which come after L. (`checks/excess/v12_symbol.py`.)

### 2.2 The non-abelian lift, in block frames

Let V' be a level-(i+1) field of flux at most f_0(L). For a parent site y let G_y be the comb axial gauge rooted at y on Pi(y) := y + 5 L [-1, 1]^4 (on parent sites), v^{(y)} := log V'^{G_y} on parent bonds, and A^{(y)} := T_1 v^{(y)}, read on fine bonds near B(y). Let gamma(y'') := G_y(y'') G_{y'}(y'')^-1 for y' next to y, and lambda(y'') := log( gamma(y'') gamma(y')^-1 ), small, and g_{y y'}(z) := exp( T_0 lambda (z) ) G_y(y').

**The field.** On a fine bond inside B(y): exp A^{(y)}(b). On a bond from z in B(y) to z' in B(y'): exp(A^{(y)}(b)) g_{y y'}(z'). Under a parent gauge h, v^{(y)} rotates by h(y), lambda by h(y), and the anchor G_y(y') goes to h(y) G_y(y') h(y')^-1. So this U^flat is parent-gauge covariant, with a fine gauge constant on each block. It is local, and analytic in the parent links for flux small.

**Curvature.** Near B(y), gauge transform B(y') by g_{y y'}. Abelian: v^{(y')} = v^{(y)} + d' lambda up to the anchor rotation, and T_1 d' = d T_0, so A^{(y')} = A^{(y)} + d T_0 lambda, and the field is A^{(y)} on B(y') too. Non-abelian the two differ by C(L) Theta^2, by BCH on finitely many small elements. So with Theta_y the largest flux on Pi(y),

    theta_p = T_2 (theta'^{G_y})_p + O(C(L) Theta_y^2)    for p near B(y), in frame y.        (C)

**The constraint.** By Lemma LE's BCH steps, log M(U^flat)(c) in frame y is Q A^{(y)}(c) + O(C(L) Theta^2) = v^{(y)}(c) + D' phi^{(y)}(c) + O(C(L) Theta^2), with phi^{(y)} := the contour average of A^{(y)}, by Lemma 3.1 and Q_path T_1 = id. With phi(y) := phi^{(y)}(y), this says M(U^flat)(c) = e^{phi(y)} V'(c) e^{-phi(y')} up to second order. Let T_0'(V') be U^flat gauge transformed by e^{-phi(y)} on each block, which is a gauge constant on blocks, so M changes by exactly that parent gauge. Then M T_0'(V') = e^{m} V', |m(c)| <= C(L) Theta_c^2.

**Exact fibre (finding 2 repaired; discharged for this construction).** The full proof is in `library/excess-finite-range-repair.md`, Sections 1--3. In the row-sum operator norm the actual derivative satisfies

    D Psi(Y)=I+E(Y),   E(c,c')=0 for d(c,c')>R,   sup_c sum_c' ||E(c,c')||<=q=B_L f<q_*,

on the Picard ball ||Y||<=C(L)f^2. A conservative support count gives initial flux radius a_0=32 and derivative range R=68 in parent cells, independent of L. Local products, combs, tensor kernels and contours are all included. The Neumann series gives an inverse entry bounded by q^ceil(d/R)/(1-q). After the initial source enlargement and the further local curvature operations,

    |Y(c)| <= C(L) B_c,    B_y := (K_q*F^2)(y),
    K_q(z) proportional to q^floor((|z|_infinity-a)_+/R),    sum_z K_q(z)=1,

where F(y)=max_q |theta'_q(y)| and a is a fixed enlarged radius. This is a kernel on squared flux, not the square of a fast convolution on flux. At f=0 take Y=0. Define T(V')=T_0'(e^Y V'); then M T(V')=V' exactly, and uniqueness in the Picard ball gives parent-gauge covariance. The scalar diagnostic (I-qS_R)^-1 gives q^m at distance mR and refutes the old tail inference. No numeric run is needed for that identity.

**Lemma LIFT (corrected).** *There are absolute C_1,C_2,C_3,C_6,L_0 and a positive f_0(L), such that for odd L>=L_0 and flux(V')<=f_0(L), the exact lift above obeys, for every nonnegative orientation weight W,*

    (T1) |theta_p| <= L^-2 (|theta'(y)|+C max_near |grad' theta'|)+C(L)B_y,
         |grad theta_p| <= C_6 L^-3 max_near |grad' theta'|+C(L)B_y;
    (T2) e(U;W) <= C_1 I^grad(V';W^+)+C(L)cub(V';W^+);
    (T3) I^grad(U;W^down) <= C_2 L^-2 I^grad(V';W^+)+C(L)f cub(V';W^+),
         cub(U;W^down) <= C_3 L^-2 cub(V';W^+).

*Here W^+=max(P_a W,K_q*P_a W), with P_a the maximum over a fixed enlarged parent neighbourhood and all orientations. Further finitely many convolutions/enlargements may be included once. In particular 1^+=1. All fixed polynomial moments and a fixed exponential moment of K_q are uniform in f,L,depth and volume, after q_* exp(nu_0 R)<1 is imposed by shrinking f_0(L). Thus W^+<=exp(C nu)W for scalar log-Lipschitz W of rate nu<=nu_0, or the orientation weights obtained by compatible down-averaging of a scalar top profile; unrelated orientation weights require the actual maximum/convolution.*

*Proof.* The finite-range derivative, inverse and support count are proved in the new note. The tensor bounds (K) give T1. Jensen gives B^(3/2)<=K_q*F^3, B^2<=f K_q*F^3 and B^3<=f^3 K_q*F^3. Transposing the kernel charges precisely W^+. The variance identity and Young's inequality F B<=F^3/3+2B^(3/2)/3 give T2. Squaring the gradient bound and counting L^4 fine sites gives C_2 L^-2 in T3; its squared error is f cub. Cubing T1 gives C L^-2 cub+C(L)f^3 cub, and f_0(L) is reduced so the latter coefficient is at most L^-2. C_1,C_2,C_3,C_6 are absolute upper bounds; C(L) occurs only in nonlinear terms. QED. The old numerical estimates do not certify these enlarged constants or L_0.

*Numerics, T10 (`checks/excess/v10_lift_su2.py`, criteria written first): the construction above, coded literally, SU(2), L = 3, comb map, d = 2, 3 on N' = 8, and d = 4 on N' = 4 read on the cover of the torus.* m := log(M T_0' V' V'^-1).

| d, f | max|m| / f^2 | (C) defect / f^2 | Picard to 1e-12 | e / I^grad | I^grad(U) / I^grad(V') |
|---|---|---|---|---|---|
| 2: 0.49, 0.19, 0.083 | 0.0125, 0.0107, 0.0075 | 0.0015, 0.0011, 0.0010 | 6, 4, 4 | 0.35, 0.31, 0.29 | 0.068, 0.060, 0.054 |
| 3: 1.07, 0.47, 0.24 | 0.0175, 0.0169, 0.0121 | 0.036, 0.039, 0.034 | 9, 6, 5 | 0.31, 0.26, 0.23 | 0.25, 0.18, 0.14 |
| 4: 1.53, 0.83, 0.42 | 0.0238, 0.0150, 0.0147 | 0.063, 0.044, 0.042 | **no (40 steps, 1.8e-3)**, 9, 7 | 0.34, 0.28, 0.28 | 1.42, 0.84, 0.74 |

Constant flux: |m| below 6e-17. So there is no first-order term, the fibre is reached exactly, and e/I agrees with the abelian lift's 0.27 to 0.33 at L = 3. *Against the registered rule:* (a), (c), (e) PASS. (b) fails at f = 1.53 in d = 4, the amplitude having overshot the intended range, which is far above any class flux. (d) as first written was void in d < 4 (the fine sum needs L^{4-d}); corrected before the second run, PASS. Limits: L = 3 only, smooth parents, one seed per dimension, d = 4 on a small torus. Nothing here tests L large.

### 2.3 Lemma TOP at W = 1, with no toron term

**Trial estimate: discharged. Class minimality: implication of item (o).** Let Vtilde_k=V and Vtilde_i=T(Vtilde_(i+1)). Section 4 of `library/excess-finite-range-repair.md` proves

    flux(Vtilde_(k-m)) <= C_7 L^-2m flux(V),
    E_0(Utilde)-E_k(V) <= 2 C_1 I^grad_k(V)+C(L)cub(V).             (TOP-tr)

The proof retains the rescaled gradient recurrence, whose coefficient is C_6/L, and the gradient-energy recurrence, whose coefficient is C_2/L^2. Thus both the gain of a power of L for the rescaled gradient and the L^-2 energy gain survive the corrected tail. There is no constant raised to the depth in the flux bound.

**Class membership is a threshold check.** The kernel's unlabelled children require flux<=T; the terminal formula domain is D_k={flux<=T_2}, T_2=C_p C_a T. For all inputs in D_k, all strict descendants are class provided

    T_2<=f_1(L),    C_7 C_p C_a/L^2<=1.                           (CLASS)

Use <=1/4 for the consumer's stronger margin. For a top already below T, L^2>=C_7 suffices. A terminal value in D_k need not itself be below the rough threshold T. It is prescribed parent data, not a child being labelled in this preimage. If C_p,C_a are the fixed geometric constants stipulated in the consumer's threshold convention, (CLASS) is part of choosing L. If they depend on L, the displayed inequality must be checked; shrinking a_* cannot repair that ratio.

**Theorem TOP-1 (corrected scope).** *Choose L so C_6/L<=1/2, C_2/L^2<=1/2, C_3/L^2<=1/2 and (CLASS) holds. Then shrink a_* so T_2<=f_1(L) and the chart thresholds. Given item (o)'s identification of the branch value with the infimum over class chains, in every sector and volume,*

    A_k(V)-E_k(V) <= E_0(Utilde)-E_k(V) <= 2C_1 I^grad_k(V)+C(L)cub(V).

The first inequality also uses the matching Wilson energy <= squared-angle energy. The rest is (TOP-tr). With a_i,c_i the trial's gradient and cubic energies, T3 gives sum_i a_i<=2a_k+C(L)c_k and sum_i c_i<=2c_k; sum T2 and telescope. Compatible log-Lipschitz weights give the same **trial** estimate with an absolute weight factor, since the product of exp(C nu L^-m) is bounded. All constants are free of x,depth,volume and position; only the nonlinear coefficients and smallness thresholds depend on L. Item (o) is an imported sketch and is not discharged here. No Prop AN3 or cut field is read by this trial construction.

## 3. Lemma TOP with weights

*Label: gap for the actual minimiser; conditional implication with (H-W) and (HC-W) below. The repaired tail establishes the weighted trial bound, but Theorem F at the true lift, (R3) and item (o) have not been shown here to supply the required nonlinear comparison. The live target below is restricted to the slow weights used by its consumer; the former unqualified arbitrary-weight reading with the field-dependent K_q fails as described in Section 3.1.*

Fix n <= k, V := V_n, U the class minimal lift, and write W := W_n with its down-averages. The live family consists of positive scalar top profiles with log W Lipschitz at fixed rate nu<=min(nu_0,delta_#/8,1/8) and the consumer's delta/4 ceiling, their compatible descendants, and fixed local or summable-kernel enlargements. If an additional J_kappa inverse tail is used, also take nu<=kappa/2. At partial-chain tops, compatible descendants have the bounded comparison (W-COMP) of `library/excess-consumer-weight-continuation.md`, not necessarily a shrinking fine-edge Lipschitz rate. Sampled smooth weights have that rate and their excesses convert with the explicit energy error there. Section 2's trial bounds retain their own stated scope and premises. Y_n(W) := E_0(U; W_0) - E_n(V; W_n). Let Utilde be the trial of Section 2.3 from V.

**Hierarchical frames (Lemma CJ, carried exact claim; unchecked in the 216dcff7e and 8e7fd0a79 continuations).** Sample y_{n-1} ~ chi_B on level-(n-1) plaquettes, then y_{n-2} ~ chi_{y_{n-1}}, ..., down to a fine plaquette z, with the orientation of B. Call the path omega, and let F(omega) be theta(z) transported to B through the axial gauges of y_1, ..., y_{n-1}, B in turn. Then |F(omega)| = |theta(z)|, and by Lemma K(b) at each level, E_0(U; W_0) = sum_B W(B) L^{4 n} E_omega |F(omega)|^2. The tower property gives L^{2 n} E_omega F(omega) = theta(B) - r^{(n)}(B), with

    r^{(n)}(B) = sum_{i <= n} L^{2 (n - i)} E_{y_i} [ transported r_{y_i} ],    |r^{(n)}(B)| <= C(L) sum_{i < n} L^{-2 (n - 1 - i)} E_i(B^+),        (CR)

as the law of y_i has mass at most L^{-4 (n - i)} on each plaquette and |r_{y_i}| <= C(L) n_{y_i}. **(CR) is the composite second-order bound, free of n, in the sharp scale-invariant form, read from one-level remainders with no Lemma AN1 and no Uhlenbeck gauge.** This addresses the kernel-density count in D4 of `gates/closure-bad958abb.md`: the frame moves with the block at every level. It does not supply the weighted minimiser comparison or the further estimates in Section 4.2.

And exactly, with c := L^{-2 n} theta(B),

    L^{4 n} E_omega |F|^2 - |theta(B)|^2 = L^{4 n} E_omega |F - c|^2 - 2 <theta(B), r^{(n)}(B)>.

Let Yhat_n(W) := sum_B W(B) L^{4 n} E_omega |F - c|^2 >= 0. So Y_n(W) = Yhat_n(W) - 2 sum_B W(B) <theta(B), r^{(n)}(B)>. The same holds for Utilde's chain, with its own frames and Yhat_tr.

**Prop TOP-W (restricted conditional form; the application is a gap).** *Only for the consumer family just specified, besides the corrected LIFT, (CLASS), CJ/(CR) and the named inputs of this section, assume the following weighted comparison, uniformly in n,volume,x and sector. In a gauge fixing the parent data, a relative field H between U and Utilde exists in the top-scale Eps chart and satisfies*

    sum_B W(B)||H||_Eps(B)^2
        <= C_H(L) [Yhat_tr(W^dagger)+sum_B W^dagger(B) f_B^4],     (H-W)
    O-hat(W) := sum_B W(B)L^(4n) E_omega |F_U-F_trial|^2
        <= C_O(L) sum_B W^dagger(B)||H||_Eps(B)^2.               (HC-W)

*Here W^dagger contains all trial and inverse enlargements, including their fixed compositions when the estimates are combined; its ratio to the admissible profile is bounded uniformly. The fourth-power term is bounded by C(L)cub(V;W^dagger) for the same local flux envelope of the trial. The comparison must include the hierarchical transport paths, not only the endpoint curvatures. Then*

    Y_n(W) <= C_TOP(L) I^grad_n(V;W^dagger) + C(L) Cub_n(W),
    Cub_n(W) := sum_(i<=n) L^(-(n-i)/2) cub(V_i;W_i^dagger).

C_TOP(L) depends on C_H(L),C_O(L), the trial constants and the fixed weight margins; it must be free of x,depth,volume and position. It is absolute only if its leading inputs are absolute (or their L-dependent nonlinear errors have been absorbed). The active consumer needs only the finite C_TOP(L) form. Its pre-L C_T is the separate rough-cell constant C_TE; Section 3.2 resolves the former symbol identification. No estimate for C_TOP(L) is established by this correction of order.

*What is proved and where this stops.* (1) The corrected trial estimate, its kernel moments and the tower variance identity give Yhat_tr(W)<=C I^grad(V;W^+)+C(L)cub(V;W^+). (2) Given H-W and HC-W, |F_U-c|^2<=2|F_trial-c|^2+2|F_U-F_trial|^2 gives the claimed bound for Yhat_n. (3) The CR cross term is bounded by C(L)Cub_n: at distance m=n-i, Young with eps=L^-3m gives a top cubic coefficient L^-m after the L^4m occurrence count and a lower cubic coefficient L^-m/2; both have summable top coefficients. This part is algebraic.

**Honest stop: (H-W) is not derived.** Here H is in top-scale units: eta=L^-n and Utilde^g_b=exp(eta H_b)U_b, with H in su(2). Equal nonlinear coarse data imply Q^o H=O(H^2), not Q^o H=0 (with the scaling absorbed in the chart coefficients). A vector tangent at U need not be tangent at Utilde. Theorem F supplies a linear inverse at U; before using it in the former Step (2), one needs a uniform nonlinear fibre chart controlling these constraint and tangent errors in the weighted Eps norm. Item (o) is a qualitative sketch, not that inequality. The former Step (3)'s hierarchical transport estimate is also only a condition (HC-W), with its constant unresolved. The precise missing comparison is recorded in `library/excess-finite-range-repair.md`, Section 5. Minimality at W=1 alone cannot replace it: even the scalar constraint u_1+u_2=a has energy minimiser (a/2,a/2), while the trial (a,0) has smaller energy for the weight (0,1). This diagnostic concerns that inference, not the Yang--Mills conclusion. No counterexample to TOP-W is asserted.

### 3.1 Pinned H-W investigation: the first stop

**Discharged algebraic diagnostic; nonlinear transfer on the local minimizing branch.** `library/excess-weighted-fibre-stop.md`, Sections 1--3, uses d=4 fields in one commuting colour direction, with coarse v_2(j)=t delta_(j,0) and no dependence on the other three coordinates. The fine curvature constraint has triangular rows. Its Gram matrix is a_L I+b_L(S+S^-1), with a_L=(2L^3+L)/3 and b_L=(L^3-L)/6. Its inverse has a nonzero alternating geometric tail, explicitly periodised on an even torus. The constrained linear minimiser therefore has nonzero curvature at arbitrarily distant blocks. The commuting trial is exactly the compact tensor lift, with zero Picard correction. At a fixed distant block, W=1_B and q=B'_L flux(V)=O(t) give a relative-field norm at least c(L,volume,B)t^2, but H-W's proposed right side is O(t^3+t^4). The separation is chosen beyond the **entire** initial support, zero-q plateau and all fixed finite enlargements. The argument works at fixed L and depth one, for any finite C_H(L) independent of t. No numerical run is behind it. Identifying the analytic branch with the global class infimum retains item (o)'s premise.

**Gap for the consumer's slow weights.** The preceding W is not log-Lipschitz and is not a counterexample to the restricted target now stated here. A flux-independent exponential convolution of W can also remove this obstruction for arbitrary weights. Neither repair supplies a nonlinear chart. The actual constraint in such a chart is C_U(Z)=log(N_U^(n)(exp(eta Z)U)V^-1)=0, with Q_U^o Z=-(C_U(Z)-Q_U^o Z). Section 4 of the new note writes its implicit chart equation (CH), distinguishes it from the trial's finite-range Picard equation, and records the required controlled conversion back to the true parent-fixed fibre.

**Exact missing estimate (NF-W).** In a genuine chart Phi with Phi(0)=U and Phi(h) the trial up to a parent-fixing gauge, put S=A o Phi, A_U=D^2 S(0), J_h=D S(h). Endpoint coverage and relative-log control must be uniform, and one needs

    ||A_U^-1 [J_h-A_U h]||_(Eps,W) <= epsilon ||h||_(Eps,W),   epsilon<=1/2,
    ||A_U^-1 J_h||_(Eps,W)^2 <= C_0 Yhat_tr(W_dagger)+C_1(L) sum_B W_dagger(B)f_B^4.

Here J_h(v)=D A(Phi(h))[D Phi(h)v], and J_h-A_U h is the integral of [D^2 S(s h)-D^2 S(0)]h over 0<=s<=1. W_dagger includes the full trial enlargement and any inverse tail. Theorem F may be used at the true lift under its (R3) L^4 hypothesis; it is not used at every point of an unconstructed path. Its tangent chart does not prove the endpoint coverage or these inequalities. If they and ||H||_W<=C_ch||h||_W hold, H-W follows with leading coefficient C_ch^2 C_0/(1-epsilon)^2. This implication is proved in the note; its premises remain gaps, not a renamed discharge of H-W.

**Historical constant boundary, superseded in part by Section 3.2.** The 216dcff7e session left the pre-L C_T identification unresolved. The 8e7fd0a79 source check distinguishes C_TE from C_TOP(L): no absolute TOP coefficient is required by the active consumer. All constants in a successful NF-W and HC-W must still be free of x, depth, volume and position. FALL allows finite depth-independent C_Y(L), giving q_h=1-c_1/C_Y(L)<1. This scalar mechanism does not prove its other inputs. The nonlinear comparison and transport estimates remain gaps.

### 3.2 Consumer-weight continuation at 8e7fd0a79

**Discharged scope identification; comparison still a gap.** FALL uses positive scalar weights log-Lipschitz in top cells. Prop DS uses W_y(x)=exp(-nu d(x,y))/C_nu, their fixed local enlargements and summable convolutions, and mixed-bond tree profiles for derivatives. Algebraic (TS) works for any consistently chosen level weights; EX-loc's no-quadrature-error version uses orientation-dependent compatible down-averages. These can have persistent jumps, so do not use the shrinking sampled rate for them. The exact conversions in Section 1 of `library/excess-consumer-weight-continuation.md` retain the O(nu_l)E_l error FALL budgets. No consumer here needs the refuted arbitrary-indicator H-W. This weight restriction is sufficient only if the uniform comparison, transport, cubic/energy and spatial-rate premises are supplied. DS's actual source sum needs only levels 1..k; it does not need the stronger bare fine-endpoint claim.

**Discharged local construction; uniform application gap.** Sections 2--3 of the continuation give a true parent-fixed local chart for the specified trial and the analytic local minimizing branch on each fixed finite torus near 1. TRUE-J differentiates the correction, and SEC-fin is its finite Taylor estimate. The first missing uniform inequality is END, with r_ch(L)>0 and C_ch(L) free of depth and volume on the whole class; the corresponding SEC-unif and TRIAL-J are also open. Theorem F's linear chart and item (o)'s sketch do not prove this. The EX-loc/global-minimality shortcut fails as an inference even for a positive slow weight: the note gives an exact variational countermodel and retains LOC-MIN from a localized admissible replacement as an unproved alternative. No counterexample to Yang--Mills TOP-slow is claimed.

**Discharged constant-order reading.** Section 4 separates C_TE (Lemma TE, printed value 32, before L) from C_TOP(L) and C_Y(L). FALL and closure Section 10 permit finite C_Y(L) at fixed L, with the strict rate choice q_bar>max(q_h,forcing rates); its cost enters C_low(L) and is paid at the final x_* choice. The high-order singleton contraction still needs its independent absolute C_1. No proof of those inputs, HC-W or all-depth CJ/CR is supplied here. Stop at END; the independent constant question is settled, and the downstream estimates remain conditional.

## 4. (COMP)(ii)

### 4.1 Geometric form, by hole-filling in the level

*Label: implication conditional on TOP-W, hence on its unresolved (H-W), (HC-W), and on the cubic decay stated below. This section proves the scalar iteration only; it does not cross that stop.*

Fix W_k with log W_k Lipschitz at a rate nu <= delta_#/8 in top cells, and W_j := down-averages. a_j := I^grad(V_j; W_j). By (TS) with compatible weights, Y_j(W_j) = Y_{j+1}(W_{j+1}) - e_j(W_{j+1}). Theorem EX-loc gives e_j(W_{j+1}) >= c_1 e^{-C nu} a_{j+1} - C(L) c_{j+1}, with c_{j+1} := cub(V_{j+1}; W^+) + cub(V_j; W^+). The fixed nu covers the compatible weights' persistent jumps by (W-COMP). Prop TOP-W at level j + 1, with all fixed enlargements absorbed in W^dagger <= C_w W, gives a_{j+1} >= (Y_{j+1}(W_{j+1}) - C(L) Cub_{j+1}(W)) / (C_TOP(L) C_w). Hence, for either sign of Y,

    Y_j(W_j) <= q_h Y_{j+1}(W_{j+1}) + C(L) ( c_{j+1} + Cub_{j+1}(W) ),    q_h := 1 - c_1 e^{-C nu} / (C_TOP(L) C_w) < 1, free of j and k.        (HF)

**Theorem COMP-ii-g (corrected conditional form).** *Put I_k(V;W)=I^grad_k(V;W)+cub(V;W). Assume TOP-W with a finite C_TOP(L) for the restricted weight family, EX-loc, and cub(V_(k-m);W_(k-m)^+)<=C rho^m cub-bar for some 0<rho<1. Increase C_TOP(L) if necessary so 0<q_h<1. Choose any*

    max(q_h,rho)<q-bar<1,    e.g. q-bar=(1+max(q_h,rho))/2.

*Then for 0<=m<=k-1,*

    I^grad_(k-m)(V_(k-m);W_(k-m))
        <= C(L,rho,q-bar) q-bar^m (I_k(V;W_k^+)+cub-bar).          (COMP-g)

*This is uniform in position,x,depth and volume; neither q-bar nor the prefactor is claimed free of L. The old choice max(q_h,2rho) was not <1 for every rho<1. The present choice also handles resonance without a depth-dependent prefactor. The fine endpoint m=k needs a separate bound; EX-loc controls the parent gradient, so the chain-sum argument alone supplies only levels 1 through k.*

*Proof.* Cub_j<=C(L)rho^(k-j)cub-bar by summing its defining geometric convolution. The error in HF is therefore <=C(L)rho^(k-j-1)cub-bar. Iteration gives Y_(k-m)<=q_h^m Y_k+C(L)cub-bar sum_(ell<m) q_h^(m-1-ell)rho^ell. If r=max(q_h,rho), that sum is <=m r^(m-1)<=C(r,q-bar)q-bar^m, including q_h=rho. TOP-W bounds Y_k. Independently, summing EX-loc from level 0 gives -Y_j<=C(L)sum_(i<j)c_(i+1)<=C(L)rho^(k-j)cub-bar. For j>=1, EX-loc on j-1 gives c a_j<=Y_j-Y_(j-1)+C(L)c_j. Insert these two bounds. There is no corresponding j=-1 step for a_0. QED.

From the first clause of COMP(i), rho=L^-2 requires a local top-cell weight with controlled mass: Holder gives sum W |theta|^3 <= (sum W |theta|^4)^(3/4)(sum W)^(1/4) <= C s^2 f_loc^3 when sum W<=C s^-4. A gradient bound alone does not supply this mass condition. All local enlargements use the repaired kernel moments.

**Corollary GS (Prop GS, W = 1).** Sum Theorem EX-loc over the chain and use (TS) and TOP-1: c_1 sum_{j<k} I^grad_{j+1}(V_{j+1}) <= 2 C_1 I^grad_k(V) + C(L) ( cub(V) + sum_{j<k} cub(V_j) ). With (COMP)(i) clause 1 the last sum is at most C(L) N_k^4 f^3 in the worst case, and on each top cell at most C f_loc^3; or with sup flux falls, at most C f_k E_k(V). With weights, the same with Prop TOP-W. No toron term from this step.

**What the rate supplies.** A geometric bound is sufficient for a sum of square roots, provided it holds for the required weights and the fine endpoint is handled. Section 5 supplies the previously missing passage from gradients to local variances. The pinned `library/sector-values.md`, Section 3B, now uses FALL and Landau interpolation for Prop DS and explicitly parks EX2 and COMP(ii) as a second route; Section 5.4 below distinguishes these consumers.

**(COMP)(i), clause 1, from the fine level (implication of (R3), by Lemma CJ).** Jensen on omega-space gives |L^{2 j} E_omega F|^4 <= L^{8 j} E_omega |theta^0(z)|^4, and the partition of unity gives sum_c |L^{2 j} E_omega F|^4 <= L^{4 j} sum_z |theta^0(z)|^4 = s^4 ||F||^4_{L^4}, with constant 1. By (CR), and E_i(c^+) <= 2 E_0(c^{++}) from (V_W) with an indicator weight, |r^{(j)}(c)| <= C(L) ||F||^2_{L^2(c^{++})} <= C(L) s^2 ||F||^2_{L^4(c^{++})}, so sum_c |r^{(j)}(c)|^4 <= C(L) s^8 f^8. So sum_c |theta_c|^4 <= C s^4 f_loc^4, for f small in L. *So "(R3) by scale counting" is now a proof, given (R3) at the fine level.*

### 4.2 The form with s^2

*Label: gap in the application, conditional on TOP-W and the further (AD), (R3) and covariant mean-subtraction estimates written below. This route was not pursued across the TOP-W stop. Its earlier assertion that closure D4 was repaired is withdrawn; Lemma W itself is unchanged.*

**Lemma W (lattice Weitzenboeck, any field of flux at most 1/6).** ||D^* theta||^2 + ||B||^2 = I^grad + X, with |X| <= C cub(U), where D^* is the backward covariant divergence and B the Bianchi defect. *Proof.* Expand both squares. The diagonal of ||D^* theta||^2 is P, the diagonal of ||B||^2 is T, and the cross terms cancel by the swap of Lemma BT, up to its commutators. QED

With a cut-off eta at top scale, in level-k units, this gives ||eta grad F||^2 <= 2 ||eta D_U^* F||^2 + C Yhat_k(loc) + C ||F||^3_{L^3} + lattice term, by applying it to eta (theta - theta-bar) in the frame of the top box, with F-bar the mean: the term in grad eta reads only the variance, so no energy appears. D_U^* F = Q^* lambda on the Wilson form up to a quartic correction, the contour part vanishes as D'^* lambda = 0 (Step 1 of (LIFT-I)), and (AD) bounds the rest by C |lambda|_loc. *The multiplier needs no Taylor expansion:* for a bump G with Q^o G = b on one parent bond, supported in its block, of norm C, lambda(b) = D A(U)[G] = <F - F-bar, d_U G> + commutator. So |lambda|_loc^2 <= C Yhat_k(loc) + C f^4. With Prop TOP-W and (R3): ||grad F||^2_{L^2(W)} <= C(L) I_k(V; W^+).

*Down to level j.* Lemma CJ with block side ell := L^j at the fine level: E_omega |F - c|^2 is at most C ell^2 avg_{B^+} |grad theta^0|^2 by the box Poincare inequality, plus the frame term, the holonomy of a loop of area ell^2, which by Hoelder in L^4 contributes at most C ell^4 avg_{B^+} |theta^0|^4. In lattice sums, Yhat_j(W) <= C s^2 ||grad F||^2_{L^2(W)} + C s^4 ||F||^4_{L^4(W)}. So with Theorem EX-loc, a_j <= C(L) s^2 I_k(V; W^+) + C s^4 f^4 + C(L) cub-sum <= C(L) s^2 I_k(V; W^+). That is (COMP)(ii) as printed.

*Earlier proposed repair, now conditional.* The claims about covariant mean subtraction and the gradient estimate above have not been re-established in this repair. They do not resolve closure D4 while TOP-W and those estimates remain open.

## 5. Lemma EX2, repaired with its root rates

**Label: implication under the precise weighted inputs below.** The local frame repair and the local variance inequality are discharged in `library/excess-root-frame-repair.md`. This establishes a conditional second-variation sum, not the response estimates of Prop AN3. In particular A4 still depends on the unresolved weighted TOP comparison. The original output-weight range is narrowed explicitly.

### 5.1 Gauge, profiles and inputs

V_j(t)=N^(j)(U_0 exp H(t b)) is the contour-free chain in its fixed matrix coordinates. F^j_y(z,t)=Ad(T_yz(t))theta_j(z,t), with T_yy(t)=1 identically, is the comb-rooted axial field. Its root is the chain's frame at y; there is no additional chosen time-dependent root rotation. Use the explicit choice in `library/block-poincare-energy-package.md`, Theorem 7 Step 1: N_j(V)=g^[j](V).M_j(V), with g_y^[j](V)=exp(-Phi_y^[j] X), X=log(V V_j(0)^-1), and Phi frozen at the base chain. Then C_j=g^[j](V_j(t))^-1 and theta'=Ad(C_j(y,t))theta_(j+1) are the deterministic parent in V_W. This is an exact **one-level** relation. Phi is the finite contour functional, so derivatives of C_j are bounded by C(L) times local sums of |h_j| and |h_j^(2)|+|h_j|^2. No rotation accumulated from the top is suppressed. The response inputs below must hold for this specified chain gauge.

Write s_j=L^(j-k), and d_j for distance to b in top cells. Fix nu>0 with 7nu<=kappa/4, where kappa is the available response-kernel rate. Set P_j=exp(-nu d_j), V_j^wt=exp(3nu d_j), J_j=exp(7nu d_j). All input bounds include fixed local enlargements and compatible down-averages. The target W=exp(g), g(b)=0, has |grad_top g|<=nu. Thus W^2/P<=C V^wt and W<=C(P V^wt)^(1/2). The shell count sum P_j<=C_nu s_j^-4 is uniform in volume.

- (A1-r) sum P_j |theta_j|^4<=C s_j^4 f^4; sum V_j^wt (|delta theta_j|^2+|delta^2 theta_j|^2)<=C_A(L); all fields remain in the small chart.
- (A2-r) sum J_j (|h_j|^4+|h_j^(2)|^4)<=C_A(L).
- (A3-r) |d^2/dt^2(E_0(W_0)-E_k(W_k))|<=C_A(L), weights fixed in time.
- (A4-r) I^grad_j(V_j;P_j^+)<=C_A(L) q-bar^(k-j) B for 1<=j<=k, with q-bar<1 and B independent of volume. Corrected COMP-g supplies this conditionally, with B bounded by the local top input. No fine-level gradient estimate is assumed.

These are explicit uses of the former A1--A4, with profile slack: their claimed family at rates <=kappa/4 contains all these profiles if both signs are indeed available. If only one decaying profile is known, the growing response bounds are additional open conditions. Weighted l^p nesting on a decaying measure does not prove them. The output rate here is at most kappa/28, not the former kappa/4.

**Lemma EX2-r (corrected EX2').** *Under these inputs and the one-level contour relation, with b_m(b;W)=sum_(c at k-m) W(c)sum_e |grad_e delta_b theta_c|^2 in the chain gauge at t=0,*

    sum_(j<k) sum_(y,q) W(y)L^4 Var_(chi_y)(Fdot^j_y) <= C(L),    (V-dot-r)
    sum_(m=0)^k b_m(b;W) <= C(L).                              (EX2-r)

C(L) may depend on the fixed nu, the input constants and sqrt(B)/(1-sqrt(q-bar)); it is free of x,position,depth and volume. This proves summability, not a pointwise geometric bound on b_m.

### 5.2 Variance from gradients, including the fine endpoint

The required inequality, proved by coordinate paths in `library/excess-root-frame-repair.md`, Section 2, is

    sum_y P(y)L^4 Var_(chi_y)(F^j_y)
        <= C(L)[I^grad_j(V_j;P_j^+)+sum P_j^+ |theta_j|^4].       (VP-W)

For adjacent plaquettes, the two comb paths differ by a loop with a coordinate-strip filling in a C L box. Its holonomy error is <=C(L)n_y^(1/2), so |Delta F_y|<=|grad theta|+C(L)n_y^(1/2)|theta|. The exact pairwise formula for a variance, telescoping on coordinate paths, and squaring give a gradient sum plus C(L)n_y^2. Finite overlap yields VP-W. No reversal of EX-loc, or unproved identification of a variance with A4's gradient, is used.

For j>=1 the right side is <=C(L)(q-bar^(k-j)B+s_j^4 f^4). For j=0, use Var<=second moment and Holder with sum P_0<=C_nu s_0^-4 to obtain V_0(P)<=C(L,nu)f^2. Thus sum_(j<k) sqrt(V_j(P)) is bounded uniformly in depth. This is the missing estimate at the former line 375.

### 5.3 Root rates and the differentiated identity

For neighbouring roots y,z write T_y(w)T_z(w)^-1=R_yz exp(lambda(w)), R_yz=T_y(z), lambda(z)=0. Put Omega=R_yz^-1 Rdot_yz. Finite product differentiation gives |Omega|<=C(L)sum_path |h_j|. Strip reconstruction in z's rooted gauge gives |lambda|<=C(L)n^(1/2) and |d exp(lambda)/dt|<=C(L)N_d^(1/2), with N_d the local sum of |Fdot_z|^2. Consequently

    Ad(R_yz^-1)Fdot_y = Fdot_z+[Omega,F_z]+error,
    ||error||_(L^2(chi)) <= C(L)[(n N_d)^(1/2)+|Omega|n].

The constant-root term remains. Its weighted square is

    sum W L^4 |Omega|^2 <|F_z|^2>
        <= C(L)(sum V^wt H_1^4)^(1/2)(sum P n^2)^(1/2)
        <= C(L)s_j^2 f^2,                                     (ROOT-W)

where H_1 is a finite local path sum of |h_j|. This uses A2-r and A1-r, with W<=C(P V^wt)^(1/2). The same estimate pays every coarse contour/root conversion with s_(j+1). Both scale sums are geometric. A spatially constant relative rotation cannot be set to zero after differentiation; for Fdot_z=0 the displayed commutator can have nonzero variance.

The complete identity and its estimates are derived in Sections 4--5 of the new note. In particular

    Fdot=Ad(T)(delta theta+[alpha,theta]),
    Fddot=Ad(T)(delta^2 theta+2[alpha,delta theta]+[alpha-dot,theta]+[alpha,[alpha,theta]]),
    2 sum_j W L^4 Var(Fdot)=Yddot-2 sum_j W L^4 Cov(F,Fddot)+sum_j W Rddot,

with alpha=T^-1 Tdot and R=2<theta',r>-|r|^2. A1-r,A2-r give sum V^wt L^4 <|Fddot|^2><=C(L); the h^(2)theta product uses (V^wt)^2/P=J. Cauchy--Schwarz and VP-W bound the covariance sum. The full five terms in Rddot, including theta'ddot r and theta' rddot, have a factor s_j f or s_(j+1) f by the explicitly weighted Holder estimates in the note. They sum geometrically. A3-r therefore gives V-dot-r.

Differentiate TL in a common rooted box; change each variance frame using ROOT-W; then return to the fixed chain gauge. The squared errors from n N_d and from transport rates times theta are <=C(L)s_(j+1)^2 f^2 in sum. This gives b_(k-j-1)<=C(L)Vdot_j+C(L)s_(j+1)^2f^2. The single fine b_k is bounded by the weighted l^2 norm of delta theta_0. Summing proves EX2-r. This closes the two local defects **as a conditional theorem with the stated profiles**; it does not discharge A1-r--A4-r for the minimiser.

### 5.4 What Prop DS now reads

**Pinned-source distinction.** At `0b13f39d2`, `library/sector-values.md`, Section 3B, explicitly parks EX2 and COMP(ii). Its current Prop DS uses FALL, CRUDE and LAN. The former assertion here that “Prop DS stands” from EX2 alone is withdrawn. Only this part and new notes have been edited; the consumer has not been rewritten.

**Older second-variation route: conditional summability only.** Given the source's full differentiated representation, mixed response estimates and a common gauge for both variations, the new EX2-r controls sum_m (b_m(b)b_m(b'))^(1/2) by Cauchy--Schwarz. COMP-g controls sum_m a_m^(1/2); root and transport terms have a factor s_m f and are summable. This would give a summed order-two estimate. The additional source estimate that must be supplied, with its mixed-bond tree weights, is of the form

    |D^2(Z_(k-m-1) o Lambda_m)[b,b']|
      <= C(L)S [sqrt(b_m(b)b_m(b')) + sqrt(a_m) c_m(b,b')
                    + s_m f (1+sqrt(b_m(b))+sqrt(b_m(b')))],       (DS-H)

where c_m is the uniformly bounded full mixed second variation of the transported curvature, and every term has the spatial weights required by the norm. SRC's first-derivative display alone is not DS-H. Separate time-dependent gauges for the two directions do not prove a mixed derivative estimate. EX2-r also supplies no per-m geometric rate for its first term. DS-H and that stronger per-level conclusion are not established here.

**Current Prop DS: exact conditional interpolation.** On its common interval |t|<=t_1=c_0 T_2 inside D^+, let z_m^y be the local composed source. Suppose its named FALL/SRC/CRUDE inputs give, with the same tail control and uniform constants,

    sup_t |partial_(b') z_m^y(V exp(t b))|
        <= C(L)S q^(m/2) T_2 exp(-delta d(y,b')),
    sup_t |partial_b^2 partial_(b') z_m^y(V exp(t b))|
        <= C(L)S exp(-delta St(y,b,b')).                          (DS-input)

Choose b' farther from y, so St<=2d(y,b'). Taylor at plus/minus tau gives |g'(0)|<=A/tau+tau G/2 for g=partial_(b')z_m^y. If sqrt(A/G)<=t_1 choose that tau; otherwise choose t_1 and use G<A/t_1^2. It follows that |partial_b partial_(b')z_m^y|<=C(L)S q^(m/4)exp(-(delta/2)St), since T_2 is bounded and T_2/t_1=c_0^-1. Summing in a norm with a strictly positive spatial-rate margin gives the corresponding geometric series. This is an implication of DS-input, not its derivation.

The present repair supplies the corrected trial in FALL's upper-bound input, but FALL for local weights still lacks TOP-W's (H-W)/(HC-W). The required CRUDE mixed derivatives, SRC tail/domain control and matching norm rates were not checked in this session. The current Prop DS therefore remains conditional on exactly those inputs; EX2's repair neither replaces them nor certifies DS.

## 6. Status of each statement

| Statement | State here | Exact dependency / limit |
|---|---|---|
| Lemma EX, weighted, c_1=1/810 | discharged, carried proof; gate ADVANCE | Map, small flux phi_0(L); proof unchanged |
| Lemma EX-loc, c_1=1/3500 | discharged, gate's local support repair written in | Coordinate rectangles and fine W^+ convention in 1.7 |
| Lemma BT and c_e>=(1-L^-2)/96 | discharged, carried proofs; gate ADVANCE | Not revised or newly numerically checked |
| Actual finite-range inverse, kernel moments, LIFT T1--T3 | discharged, new written author proof | Fixed comb/tensor construction; f<=f_0(L); no independent check |
| TOP-tr and class membership; signed weighted TR-SLOW | discharged trial inputs; implication for TR-SLOW | (CLASS), T2-r/T3-r; choose L so C_w C_2/L^2 and C_w C_3/L^2 <=1/2, then f_1(L), a_*; hierarchical Yhat_tr still retains CJ/CR |
| TOP-1 for A_k | implication | Also item (o)'s branch/class-minimality identification and matching Wilson normalisation |
| Prop GS at W=1 | implication | TOP-1 and cubic sum; weighted version additionally needs TOP-W |
| Localized linear-tail diagnostic | discharged algebraic calculation, author proof | One-level d=4 commuting sector; nonlinear branch transfer at fixed L and volume; no independent check |
| H-W with arbitrary W and the field-dependent K_q | implication: failure on the analytic minimizing branch | Global class-infimum identification still reads item (o); no finite C_H(L) fixes the amplitude mismatch |
| Consumer weights and sampled/compatible conversion | discharged, author proof | Slow exponential profiles, fixed enlargements, compatible descendants; persistent box-direction jumps; retain the sampled-weight energy error |
| TRUE-CH, TRUE-J and SEC-fin | discharged, local branch only | Fixed L, depth and volume, sufficiently small link-coordinate neighborhood of 1; constants/radius not uniform |
| EX-loc plus global minimality as a weighted shortcut | discharged failed inference | Exact two-site countermodel, not a Yang--Mills counterexample; localized admissible replacement LOC-MIN still open |
| H-W for the consumer weights | gap, first stop | END with depth/volume-free radius and gauge control, then SEC-unif and TRIAL-J; no C_H(L) established |
| CJ/CR and HC-W at general depth | unchecked CJ/CR; gap HC-W | Carried claims, not newly checked after the H-W stop; no certification of level-free transport constants |
| Prop TOP-W, restricted family | gap | (NF-W)/(H-W), (HC-W), CJ/CR and the trial/cubic premises; C_TOP(L) allowed |
| C_TE versus C_TOP(L); active closure's order | discharged source/dependency reading | Pre-L C_T is TE's count; finite depth-uniform C_Y(L) suffices for FALL/DS, conditional on their other inputs |
| COMP-ii-g, levels 1 through k | implication | TOP-W and cub decay rho<1; choose max(q_h,rho)<q-bar<1 |
| COMP(ii) at the fine endpoint | gap in the stronger hole-filling claim | No level -1 EX-loc step; DS's actual sources read only levels 1..k |
| COMP(ii) with s^2, Section 4.2 | gap in application | Also (AD), (R3), covariant mean-subtraction and TOP-W; not pursued across the stop |
| Root-rate square (ROOT-W), local variance (VP-W) | discharged local estimates | A2/A1 respectively for their weighted summed consequences |
| Lemma EX2-r | implication | A1-r--A4-r, small charts, one-level contour relation; output rate <=kappa/28 |
| Older DS second-variation route | gap for the full consumer | Needs DS-H and mixed tree norm; EX2 gives summability, not per-level geometric decay |
| Pinned current Prop DS | implication only from DS-input | FALL still needs TOP-W; CRUDE/SRC/domain/tail/norm inputs not certified here |

**Disposition of the gate findings.** Finding 3 is written in locally. Finding 2's tail inference is replaced by an inverse on squared flux, with all initial support and moments explicit. Finding 1's constant root-rate term is retained and paid using A2 at every change of frame; A4's gradient-to-variance passage is supplied by VP-W. Neither of the latter repairs establishes the independent minimiser/response premises. The former blanket statements “D1 dissolved”, “TOP proved”, “DS stands” and “closure D4 repaired” are superseded by the rows above. Historical numerics below do not establish any of those missing premises.

## Obligations

- discharged: retain Lemma K, Theorem V, LE, IP, NN, BT, EX and TL at the named gate's research standing; no new check of their proofs in this repair, except EX-loc's support convention.
- discharged: finite-range derivative row norm, Neumann inverse on squared flux, initial support enlargement, normalised moments, weighted T1--T3; `library/excess-finite-range-repair.md`, Sections 1--3.
- discharged: TOP-tr and rescaled-gradient bootstrap; class descendants require T_2<=f_1(L) and C_7 C_p C_a/L^2<=1 (<=1/4 for the stronger margin). If C_p,C_a are not fixed geometric constants, check this ratio explicitly.
- implication: TOP-1 and W=1 GS still read item (o); it is a sketch, not discharged here.
- discharged: the localized linear-tail calculation in `library/excess-weighted-fibre-stop.md`; with the analytic minimizing branch it contradicts the arbitrary-weight H-W using the field-dependent K_q. Do not reuse that unrestricted comparison. Its global class-infimum identification remains conditional on item (o).
- discharged: identify the consumer weight family and distinguish sampled smooth profiles from compatible descendants with persistent jumps; the exact conversions are in the continuation note. Do not invoke a shrinking fine-edge rate for the latter. DS uses FALL only on levels 1..k.
- implication: TR-SLOW repairs the signed weighted trial bound from T2-r/T3-r, paying the fixed descendant-weight ratio C_w against L^-2. Its threshold may require increasing L_0 before choosing a_*. It does not discharge the hierarchical Yhat_tr or minimizer comparison.
- discharged: TRUE-CH covers the specified trial and the local minimizing branch near 1 on each fixed finite lattice; TRUE-J retains the derivative of the constraint correction; SEC-fin is its finite Taylor bound. These do not establish the consumer's uniform chart.
- gap: first prove END on the whole consumer class, with r_ch(L)>0 and C_ch(L) independent of depth, volume, x and position, then SEC-unif and TRIAL-J for the actual fibre derivative. Item (o), AN3 and F(iv) do not supply that endpoint estimate. A localized admissible comparison proving LOC-MIN is an alternative; EX-loc plus global minimality alone is insufficient.
- gap: only after H-W closes, derive HC-W and check the level-free CJ/CR transport/remainder bounds, then establish a finite C_TOP(L) uniform in the class, depth and volume. No such bound is proved here. Shrinking a_* can absorb C(L) times a small factor, never a bare linear C(L).
- discharged: the constant-order issue is a symbol collision, not a need for an absolute TOP coefficient. C_TE belongs before L; C_TOP(L), C_Y(L), q_bar(L), C_F(L) may follow L. Closure Section 10 pays the resulting C_low(L) at x_*, while its independent high-order C_1 must remain absolute.
- implication: COMP-g on levels 1..k given TOP-W and cubic decay, with a rate strictly between max(q_h,rho) and 1. The fine endpoint needs a separate bound, not another iteration of EX-loc.
- discharged: VP-W, retaining its quartic curvature error, and ROOT-W, retaining the root rate bounded by link variations; `library/excess-root-frame-repair.md`, Sections 2--3.
- implication: EX2-r under the exact profiles and A1-r--A4-r. Verify these response and curvature estimates for the AN3 curve in the specified one-level contour gauge before using the result for that curve. The output-rate loss and growing response weights cannot be omitted.
- gap: DS-H and mixed spatial norms for the older second-variation route; current Prop DS instead needs its FALL/CRUDE/SRC inputs in DS-input. No consumer file was changed.
- gap: upper bounds with frozen boundary data, including LIFT next to a frozen layer and TOP-W with Theorem F-D, remain outside this repair.
- unchecked: numerical sizes of C_1,C_2,C_3,C_6,L_0,C_TOP(L),q_h and all new non-abelian estimates by an independent reader. Prior T8--T12 values are not a certificate for the repaired constants. No new numerical job was run.

## 7. Numerics, summary

**Historical original-author record; not rerun or independently reproduced in this repair.** Criteria: `checks/excess/CRITERIA.md`, written before each run; additions dated and marked. The original author reports all numerics under the lock. A search that finds nothing does not prove a bound; here each run tests a step of a written proof.

| Test | Outcome |
|---|---|
| T0 kernels | PASS, 1e-16 |
| T1 abelian identity | PASS, 1.4e-15 relative |
| T2 remainder order, identity | PASS. Identity to 1e-12 on SU(2), remainder t^2 |
| T3 Bianchi | PASS. B^2/(f^2 E) 0.31 to 0.46, T - 2 P < 0 on all fields run |
| T4 sharpness | PASS. T/P = 2.0 at p = (1,1,1,0), a = e_4 |
| T5 | PASS on the fields of `v1_identity.log`: e/I = 0.46 (smooth), about 120 (white), no adversarial search here; the gate's own searches stand, with lowest in-domain e/I = 0.1125 |
| T7 pointwise bounds | PASS, largest ratio 0.43 |
| T8 kernels | Identities PASS. Constant clause **FAIL** as registered; follow-up levels off at 22 |
| T9 abelian lift | Identities PASS. C_2 clause **FAIL** as registered; C_2/L falls, bounded by (K), constant not computed |
| T10 lift, SU(2) | (a), (c), (e) PASS; (b) fails at f = 1.53 only, outside any class flux; (d) void as first written, corrected, PASS |
| T11 Lemma TL at a variation | Ratio clause PASS: 0.147 to 0.167 transverse, 0.36 to 0.38 in-plane, level from a = 0.2 to a = 0. Second clause, block gauge against a global gauge, **not run** |
| T12 sup over P, abelian lift | Report only: C_2 levels off, see 2.1 |
| T6a lift of a charged parent | PASS on both fields, see below |
| T6 true minimiser, charged | PASS on fields a, b, see below |

**The charged field (T6, T6a): the test the gate asked for.** Constant abelian flux with n_12 = n_34 = 1 on a fine torus of 24^4, so second Chern number 2 and f near 0.1, plus smooth non-abelian modes; field b adds a localised bump. N' = 8, L = 3, d = 4, SU(2), comb map. The charge estimate is a clover sum, exact at zero perturbation (2.0000).

| | f | Q(V'), Q(U) | E(V') | e | I^grad(V') | e / I^grad | C_eff at c_1 = 1/810 |
|---|---|---|---|---|---|---|---|
| field a, lift (residual 1.9e-12) | 0.129 | 1.989, 1.994 | 85.842 | 4.366 | 19.911 | 0.219 | -0.39 |
| field a, true minimiser | 0.129 | 1.989, 1.993 | 85.842 | 3.141 | 19.911 | **0.158** | **-0.28** |
| field b, lift | 0.125 | 1.998, 1.999 | 84.170 | 3.627 | 15.556 | 0.233 | -0.34 |
| field b, true minimiser | 0.125 | 1.998, 1.998 | 84.170 | 2.534 | 15.556 | **0.163** | **-0.24** |

C_eff := (c_1 I - e)/(f E); negative means the inequality holds with no error term. Field a: |r| = 3.4e-7 and stationarity 1.3e-5, 13 outer loops. Field b: |r| = 4.4e-7 and stationarity 4.8e-6, 10 outer loops. Both are inside the tolerances fixed in advance (1e-6, 2e-4). So **in a charged sector at small flux the true minimisers have e/I = 0.158, 0.163**, above the abelian c_e = 0.0988, and the lift is within a factor 1.39, 1.43 of the minimum. The lower and upper bounds of this file bracket them, in fields no earlier test reached. These are two fields at one flux, one level, L = 3: a test of the proofs, not a bound. *How it was run.* Three runs stopped: twice at the 2 GB guard, once at the harness's 2 hour limit, with no checkpoint. Newton stalled on this background, as the solver's flat preconditioner is wrong at the gauge seam. The result is from an augmented Lagrangian with L-BFGS started at the lift, at rho = 10 then rho = 100. All logs are kept in `checks/excess/`, and the steps are in `CRITERIA.md`.

## Requests

**TO THE OWNER OF `library/sector-values.md` (local handoff only; nothing sent).** The lower EX replacement is unchanged except support. Read the corrected LIFT/TOP-1 with (CLASS), and the unresolved (H-W)/(HC-W) before using weighted TOP or FALL. COMP-g is conditional and controls levels 1..k. EX2-r is a second route with explicit response profiles and output-rate loss; it is not needed by your pinned current DS proof. Section 5.4 distinguishes DS-H for the old route from DS-input for the current FALL/CRUDE/LAN route. These notes supply no certificate of SRC, its tail, the mixed derivatives of CRUDE, or the boundary version.

**216dcff7e follow-up (historical local record, constant question now resolved).** The field-dependent trial tail cannot support the arbitrary-weight minimiser comparison: see Section 3.1 and `library/excess-weighted-fibre-stop.md`. FALL's slow weights avoid that particular falsifier, but still need NF-W and then HC-W. The 8e7fd0a79 continuation below supersedes the earlier identification of its TOP coefficient with the closure list's C_T.

**8e7fd0a79 handoff (local record only; nothing sent).** Use `library/excess-consumer-weight-continuation.md` for the exact weights, persistent-jump correction, true finite chart and the END/SEC-unif/TRIAL-J gaps. A compatible no-energy-error EX-loc statement and a sampled-weight FALL statement have different weights; the conversion retains the expected nu_l E_l term. DS needs only levels 1..k. The pre-L constant is C_TE, while a depth-uniform C_TOP(L) suffices for the active scalar/DS constants chain. Neither that bound nor HC-W/CJ/CR is newly certified. Lemma EX proofs, all consumers, gates, axioms and ledgers were left unchanged. No commit, push, PR, message, audit or subagent was used.

**TO THE LEAD.** Lemma O3's tail, and so (SRC) and Theorem VAL's term N_k^4 Phi(e^-8 N_k/4), are untouched: that tail comes from Taylor of the source at a cut field, not from the excess. Whether a block-frame comparison could remove it there too was not tried; it is outside this item.

## Read and not read

**Original author record (preceding this repair).**

Read: `FINISH.md`, `GOAL.md`; `library/sector-values.md` Sections 0 to 3B and 7, 8 in part; `library/analytic-lift.md` in full; `library/critical-class-and-excess.md`; `library/block-poincare-energy-package.md` to Theorem 6; `library/composite-adjoint.md` head and Lemma AD1; `library/fibre-propagator.md` Setting and Theorem F; (R1) to (R3), Text 1, Text 3.1 to 3.3 of `parts/hard-core--mapped.md`; Prop 10' and items (f), (f') of `library/relative-density-bound.md`; `gates/lemma-ex-7c12c6981.md`, `gates/closure-bad958abb.md`; `checks/gate_ex/ex_core.py`.

Not read: `parts/hard-core--independent.md`, any gate on it, the Sussman-Alpoge repository, Theorem F-D, HS-P, HS-T, `library/lattice_sobolev_box_gauge.md`, `library/lattice-uhlenbeck.md`, `library/one-step-closure.md` beyond grep lines, Sections 4 to 6 of `library/sector-values.md` beyond the statements. Inputs of Sections 3 to 5 are taken at their labels: none of them was checked here.

**Repair-session reading boundary and verification.** Read GOAL and FINISH first, then the full specified excess gate. Read the relevant bounded arguments in this part, the map definition in `parts/hard-core--mapped.md` 3.1 and its current threshold paragraph (near original line 1027), the contour-free definition in `library/block-poincare-energy-package.md` Theorem 7 Step 1 and `library/analytic-lift.md` near its definition of N_j, item (o) of `library/relative-density-bound.md`, the constant order of `library/one-step-closure.md`, Theorem F's statement, and the current SRC/COMP/FALL/CRUDE/LAN/DS statements and relevant proofs in `library/sector-values.md` Section 3B. Repository workflow and the applicable procedure were inspected from pinned HEAD because the workflow file is absent from this sparse checkout; no campaign, review or audit was started. Some initial multi-read/search outputs were truncated; the consequential mathematical ranges were reread separately. No truncated search is claimed as completed verification.

**Weighted-comparison session reading boundary (216dcff7e).** Read GOAL/FINISH first; this part's Sections 0, 2, 3, 6 and Obligations; the complete finite-range repair; the setting, true-lift condition, statement and relevant proof portions of Theorem F; analytic-lift Sections 1--AN3; the energy package's setting, Theorem 6, and Theorem 7's nonlinear contour-free map; mapped 3.1 and (R1)--(R3); item (o); sector-values (TS), TOP and FALL; and the closure constants list. Large search outputs were only locators; consequential mathematical ranges were reread in bounded calls. Theorem F, (R3), AN1/AN2, item (o), HC-W and general-depth CJ/CR were not independently validated. No other side's part, good file or gates, no external account, and no gate report were opened in this session. No numerical scripts were run. Mechanical checks and source identities are saved in `checks/excess-codex/`; they verify file scope and preservation, not the mathematical argument. The explicit bounded task overrides campaign, delegation, commit and PR procedures.

**Consumer-weight continuation reading boundary (8e7fd0a79).** Read GOAL and FINISH first, the Summary and complete earlier fibre-stop note, the current part's affected arguments/status/obligations and EX-loc statement/proof for its weight convention; the finite-range repair; sector-values (TS), TOP, FALL, COMP-B, CRUDE, DS and their stated uses; closure Sections 1--4 and 10, plus its C_T/rate/constant references; fibre-propagator's setting, F and (6'); analytic-lift's setting, AN1--AN3 and hostile points; the energy package's setting and Theorem 7; relative-density-bound item (o) and TE's statement/Step 4; mapped C_T locators. The source workflow and relevant physics-loop instructions were read from HEAD where absent in this sparse checkout; broader campaign/PR procedures are outside this explicit bounded task. Search output was used as a locator, not proof verification. No independent-side part, good file, gates on that side, history-budget gates, external account or any gate file was opened. No numerical computation, independent check or audit was run. New results are author proofs/implications at exactly the scopes stated. The editable files are this part, the new continuation lemma, and mechanical evidence under checks/excess-codex/.

**Earlier repair's verification record (historical).** No independent-attempt part, its good file, or any gate on that attempt was opened. No external literature, original numerical script or numerical log was used in the repair; historical numbers above are left as their author's record. The scalar shift diagnostic, shell bound, scalar iteration and root-rate tests were derived algebraically, not run as numerical computations. No numeric-lock was acquired because no numerical job was launched. No subagents, commit, push, PR, message to another party, axiom/ledger edit or audit. Only this part, the two new library notes and the mechanical verification receipt in `checks/excess-codex/verification.txt` were written. Verification checked the pinned HEAD, permitted write set, unchanged protected proof text and historical numeric tables, and whitespace; it was not an independent mathematical review. The current session's write set and receipt are recorded separately above and under `checks/excess-codex/`.
