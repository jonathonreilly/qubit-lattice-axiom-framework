lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-01T19:34Z

# Excess: Lemma EX, Lemma EX2, (COMP)(ii)

Queue item 7 of `FINISH.md`, mapped side, frozen at commit `d9d4496f1`. Research-stage working state. Grants no status.

Started 2026-11-01T07:34Z. No read of `parts/hard-core--independent.md`, of any gate on it, or of the Sussman-Alpoge repository. Provenance: anthropic/claude-opus-5-5, effort max, Mac mini worker.

## 0. Summary

**Lemma EX is proved, in a stronger form and by a new route.** The coarse plaquette angle is L^2 times an average of fine plaquette angles against a tent-tent-box-box kernel, these kernels are a partition of unity on fine plaquettes, and so the excess of *any* field in the fibre is a sum of local variances up to second order (Theorem V). Overlapping tents bound the in-plane parent gradient, and a window at the block face with the Bianchi identities at both levels bounds the transverse one (Lemma TL). No symbol, no IMS, no gauge patch, no global gauge: so no sector and no toron term, and c_1 is free of L.

**An upper bound with no cut field.** An explicit one-level lift, in the fibre exactly, gains a power of L per level (Lemma LIFT). So Lemma TOP at W = 1 reads neither Prop AN3 nor Taylor at a cut field (TOP-1). The form with weights needs Theorem F (Prop TOP-W).

**(COMP)(ii) and Lemma EX2 are implications.** Hole-filling in the level gives (COMP)(ii) with a geometric rate q-bar^m in place of s^2, which is all any consumer reads; the printed s^2 follows given also (AD). Lemma EX2 is rewritten with its gauge fixed, by differentiating the variance identity twice in block-local gauges, and it closes given (COMP)(i), Prop AN3 and (COMP)(ii). Section 6 has every label. Nothing here is gated, and a same-model proof is not an audit.

## 1. Lemma EX: a proof with no symbol, no IMS and no toron term

*Label: discharged at the level of a written proof, same-model, not gated. Reads the definition of the block map and nothing else: not Theorem F-D, not Prop AN3, not the lift's minimality, not c_e.* Checks: `checks/excess/v1_identity.py`, log beside it, criteria T0 to T4 in `checks/excess/CRITERIA.md`, written first, all PASS at the first run on the comb map of `checks/gate_ex/ex_core.py`, SU(2), d = 4, L = 3 (T0 also L = 5).

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

*Proof.* Square Lemma TL, with (A + B)^2 <= 2 A^2 + 2 B^2 and six terms: |grad_e theta'_q(y)|^2 <= 108 L^4 (sum of six sigma^2) + errors. There are 96 slots per site, 16 per orientation after the sum over y, so I^grad(V'; W^-) <= 1728 V(W) + C(L) sum W^- (n_y^+ + Theta_y (n_y^+)^{1/2} + Theta_y^2)^2. The last is at most C(L) (cub(V'; W^+) + cub(U; W^+)), since |theta| <= 1 and Young. In (V_W), |r_{y,q}| <= C(L) n_y, and |theta'| n_y <= C(L) sum_{Box(y)} (|theta'|^3 + |theta_p|^3). QED

*Reading.* The right side has the *fine* cubic energy, which is the natural form on a chain, where it is geometric in the level. For W = 1 and flux(U) <= C f this gives Theorem EX back in the printed form, with a worse c_1.

## 2. A one-level lift with a gain, and Lemma TOP at W = 1

*Label: the abelian kernels are discharged; the non-abelian lift is written step by step with soft constants C(L), same-model, not gated. It reads the map, and class minimality (item (o) of `library/relative-density-bound.md`) only to say A_k(V) <= E_0 of a class chain in the fibre. No Prop AN3, no Theorem F, no cut field.* Needed because an upper bound on Y_k is the input of the sum over levels, and the printed Lemma TOP reads Prop AN3 and Taylor at cut fields, which is where the toron term came from. Numerics: T8, T9 and follow-up, `checks/excess/v8_lift1d.py`, `v9_lift4d.py`, `v9b_follow.py`.

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

**Exact fibre.** Psi(Y) := log( M T_0'(e^Y V') V'^-1 ) on parent bonds is analytic and of finite range, and D Psi(0) = id + O(C(L) Theta), as at V' = 1 the first order of M T_0' is the identity. So Psi(Y) = 0 has a solution: the map Y -> Y - Psi(Y) contracts in sup norm, and |Y(c)| <= C(L) Theta-tilde_c^2, Theta-tilde_c := sum_{c''} (C(L) f)^{d(c, c'')} Theta_{c''}. **Define T(V') := T_0'(e^Y V'). Then M(T(V')) = V' exactly.** Its curvature obeys (C) with Theta replaced by Theta-tilde, as the parent curvature of e^Y V' is theta' + O(C(L) Theta-tilde^2).

**Lemma LIFT.** *There are absolute C_1, C_2, C_6, and L_0, f_0(L), C(L), such that for L >= L_0 and flux(V') <= f_0(L), U := T(V') has M(U) = V', is parent-gauge covariant, and for all W >= 0, with W^+ := W smeared over parent distance at most 6 blocks with the tail of Theta-tilde:*

    (T1)  |theta_p| <= L^-2 ( |theta'(y)| + C max_near |grad' theta'| ) + C(L) Theta-tilde_y^2,   |grad theta_p| <= C_6 L^-3 max_near |grad' theta'| + C(L) Theta-tilde_y^2;
    (T2)  e(U; W) <= C_1 I^grad(V'; W^+) + C(L) cub(V'; W^+);
    (T3)  I^grad(U; W^down) <= C_2 L^-2 I^grad(V'; W^+) + C(L) f cub(V'; W^+),    cub(U; W^down) <= C L^-2 cub(V'; W^+).

*Proof.* (T1): (C), (K), and the flat difference of theta'^{G_y} against grad' up to C Theta^2. In (C) the frame is close to the axial gauge at y; the gauges differ by a rotation of size C(L) Theta, which changes theta by second order. (T2): in (V_W), sigma_{y,q}^2 <= <|theta^{(y)} - L^-2 theta'_q(y)|^2>_{chi_y}, so L^4 sigma^2 <= C max_near |grad' theta'|^2 + C(L) Theta-tilde^4 by (T1), and |r| <= C(L) n_y <= C(L) Theta-tilde^2. (T3): (T1), L^4 fine plaquettes per block, and a fine link in frame y has angle at most C(L) Theta, so the covariant and flat fine differences differ by second order. QED

*Numerics, T10 (`checks/excess/v10_lift_su2.py`, criteria written first): the construction above, coded literally, SU(2), L = 3, comb map, d = 2, 3 on N' = 8, and d = 4 on N' = 4 read on the cover of the torus.* m := log(M T_0' V' V'^-1).

| d, f | max|m| / f^2 | (C) defect / f^2 | Picard to 1e-12 | e / I^grad | I^grad(U) / I^grad(V') |
|---|---|---|---|---|---|
| 2: 0.49, 0.19, 0.083 | 0.0125, 0.0107, 0.0075 | 0.0015, 0.0011, 0.0010 | 6, 4, 4 | 0.35, 0.31, 0.29 | 0.068, 0.060, 0.054 |
| 3: 1.07, 0.47, 0.24 | 0.0175, 0.0169, 0.0121 | 0.036, 0.039, 0.034 | 9, 6, 5 | 0.31, 0.26, 0.23 | 0.25, 0.18, 0.14 |
| 4: 1.53, 0.83, 0.42 | 0.0238, 0.0150, 0.0147 | 0.063, 0.044, 0.042 | **no (40 steps, 1.8e-3)**, 9, 7 | 0.34, 0.28, 0.28 | 1.42, 0.84, 0.74 |

Constant flux: |m| below 6e-17. So there is no first-order term, the fibre is reached exactly, and e/I agrees with the abelian lift's 0.27 to 0.33 at L = 3. *Against the registered rule:* (a), (c), (e) PASS. (b) fails at f = 1.53 in d = 4, the amplitude having overshot the intended range, which is far above any class flux. (d) as first written was void in d < 4 (the fine sum needs L^{4-d}); corrected before the second run, PASS. Limits: L = 3 only, smooth parents, one seed per dimension, d = 4 on a small torus. Nothing here tests L large.

### 2.3 Lemma TOP at W = 1, with no toron term

Let V be a level-k field of flux f <= f_1(L), Vtilde_k := V, Vtilde_i := T(Vtilde_{i+1}), Utilde := Vtilde_0.

*Uniform flux.* Put f^_i := L^{2(k-i)} sup |theta(Vtilde_i)|, d^_i the same for sup |grad theta|. By (T1), d^_{i-1} <= (C_6/L) d^_i + C(L) L^{-2(k-i)} f^_i^2 and f^_{i-1} <= f^_i + C d^_i + C(L) L^{-2(k-i)} f^_i^2. For L >= 2 C_6, the d^_i sum geometrically, so sup_i f^_i <= C_7 f, by a bootstrap from f <= f_1(L). **So the trial chain has flux at most C_7 f L^{-2(k-i)}, with no factor per level, and it is a class chain.**

**Theorem TOP-1.** *For L >= L_0 and flux(V) <= f_1(L), in every sector and on every torus:*

    A_k(V) - E_k(V) <= E_0(Utilde) - E_k(V) <= 2 C_1 I^grad_k(V) + C(L) cub(V),    both with W = 1.

*With compatible weights W_i, the same bound holds for E_0(Utilde; W_0) - E_k(V; W_k), with W_k^+ on the right.*

*Proof.* Let a_i := I^grad(Vtilde_i; W_i), c_i := cub(Vtilde_i; W_i). (T3), with W^+ <= e^{C nu_i} W on a log-Lipschitz weight, gives a_{i-1} <= (C_2 L^-2 e^{C nu_i}) a_i + C(L) f_i c_i and c_{i-1} <= C L^-2 e^{C nu_i} c_i. For L >= L_0 both contract, and the product of e^{C nu_i} is bounded, as nu_i is geometric. Sum (T2) over i. The first inequality is class minimality. QED

*What this replaces.* Lemma TOP as printed: it read Prop AN3 uniformly in k and a Taylor expansion at a cut field. TOP-1 reads neither, and it has no tail. It costs L >= L_0 with C_2 L_0^-2 < 1, which Section 3A wanted to avoid and which the program allows anyway. Section 3 below gets the local form.

## 3. Lemma TOP with weights

*Label: implication, level of each term. Reads Theorem F of `library/fibre-propagator.md` at the true lift, (R3), item (o). Unlike TOP-1 it is not self-contained: locality of the minimiser is an elliptic fact, and Theorem F is where it lives. It reads no cut field and no Prop AN3.*

Fix n <= k, V := V_n, U the class minimal lift, and write W := W_n with its down-averages. Y_n(W) := E_0(U; W_0) - E_n(V; W_n). Let Utilde be the trial of Section 2.3 from V.

**Hierarchical frames (Lemma CJ, exact).** Sample y_{n-1} ~ chi_B on level-(n-1) plaquettes, then y_{n-2} ~ chi_{y_{n-1}}, ..., down to a fine plaquette z, with the orientation of B. Call the path omega, and let F(omega) be theta(z) transported to B through the axial gauges of y_1, ..., y_{n-1}, B in turn. Then |F(omega)| = |theta(z)|, and by Lemma K(b) at each level, E_0(U; W_0) = sum_B W(B) L^{4 n} E_omega |F(omega)|^2. The tower property gives L^{2 n} E_omega F(omega) = theta(B) - r^{(n)}(B), with

    r^{(n)}(B) = sum_{i <= n} L^{2 (n - i)} E_{y_i} [ transported r_{y_i} ],    |r^{(n)}(B)| <= C(L) sum_{i < n} L^{-2 (n - 1 - i)} E_i(B^+),        (CR)

as the law of y_i has mass at most L^{-4 (n - i)} on each plaquette and |r_{y_i}| <= C(L) n_{y_i}. **(CR) is the composite second-order bound, free of n, in the sharp scale-invariant form, read from one-level remainders with no Lemma AN1 and no Uhlenbeck gauge.** This is the repair of D4 of `gates/closure-bad958abb.md`: the frame moves with the block at every level, so no gauge at the top box is needed.

And exactly, with c := L^{-2 n} theta(B),

    L^{4 n} E_omega |F|^2 - |theta(B)|^2 = L^{4 n} E_omega |F - c|^2 - 2 <theta(B), r^{(n)}(B)>.

Let Yhat_n(W) := sum_B W(B) L^{4 n} E_omega |F - c|^2 >= 0. So Y_n(W) = Yhat_n(W) - 2 sum_B W(B) <theta(B), r^{(n)}(B)>. The same holds for Utilde's chain, with its own frames and Yhat_tr.

**Prop TOP-W.** *Let W be log-Lipschitz at rate nu <= delta_#/8 in level-n cells. Then for V in D_n, in every sector,*

    Y_n(W) <= C_T ( I^grad_n(V; W) + cub(V; W) ) + C(L) Cub_n(W),    Cub_n(W) := sum_{i <= n} L^{-(n - i)/2} cub(V_i; W_i^+).

*Proof.* (1) *Trial.* By the tower property Yhat_tr(W) is the sum over levels of the trial's variances, plus the mean's term, and by (T2) and Section 2.3 it is at most C (I^grad_n(V; W^+) + cub(V; W^+)).

(2) *Elliptic step.* U and Utilde are class chains in one fibre, so in a box both have small angle in tree gauge, and Utilde = e^H U with sup_B ||H||_{Eps(B)} small, by item (o). Let J(G) := D A(Utilde)[G] for G in ker Q^o at U. Since D A(U) vanishes on ker Q^o, Taylor at U gives bH[H, G] = J(G) + N(H)[G], with ||N(H)||_{Eps^*(B)} <= C(L) sup ||H||_{Eps} ||H||_{Eps(B^+)}. Theorem F at U, (i), (ii), with a weight e^g, g Lipschitz at rate delta_#/4 (real, by item (iii) the gauge part vanishes): sum_B W(B) ||H||^2_{Eps(B)} <= C sum_B W(B) ||J||^2_{Eps^*(B)}. In level-n units, for G on B of norm 1, split F(Utilde) into its constant part F-bar_B in the frame of B and the rest. The constant part pairs with d_{Utilde} G to at most the commutator, of size f_B^2. The rest is at most ||F(Utilde) - F-bar_B||_{L^2(B)} ||d G||_{L^2}. So

    sum_B W(B) ||H||^2_{Eps(B)} <= C ( Yhat_tr(W^+) + sum_B W(B) f_B^4 ).        (H)

(3) *Comparison.* On omega-space, F_U(omega) - F-tilde(omega) =: Omega-hat(omega) obeys |Omega-hat| <= |d_U H + [H, H]|(z) + 2 |tau_omega| |theta-tilde(z)|, with tau_omega the sum of the link differences along the path omega. Level by level, with (1) of `library/analytic-lift.md` and the Sobolev step of that note, E_omega |tau_omega|^2 <= C(L) ||H||^2_{Eps(B^+)}, as avg_b e_i(b)^2 <= C L^{-2 (n - i)} e_n^2. So with |theta-tilde| <= C_7 f_B L^{-2 n} from Section 2.3, O-hat := sum_B W(B) L^{4 n} E_omega |Omega-hat|^2 <= C(L)^2 times (H) for f small. Then L^{4 n} E_omega |F_U - c|^2 <= 2 L^{4 n} E_omega |F-tilde - c|^2 + 2 L^{4 n} E_omega |Omega-hat|^2, and

    Yhat_n(W) <= 2 Yhat_tr(W) + 2 O-hat.

(4) *Back to Y.* The (CR) term is at most C(L) sum_B W(B) |theta(B)| sum_{i<n} L^{-2 (n - 1 - i)} E_i(B^+). Young on each pair, |theta(B)| |theta_p|^2 <= eps |theta(B)|^3 + eps^{-1/2} |theta_p|^3 with eps := L^{-3 (n - i)} against the L^{4 (n - i)} plaquettes of B^+ at level i, makes this at most C(L) Cub_n(W). QED

*Why no toron term here either.* The trial needs no trivialisation, and Theorem F does not read the sector.

## 4. (COMP)(ii)

### 4.1 Geometric form, by hole-filling in the level

*Label: implication of Theorem EX-loc, Prop TOP-W and one clause of (COMP)(i). Own derivation; the idea T_{m+1} <= q T_m is the route named in D7 of `gates/closure-bad958abb.md`.*

Fix W_k with log W_k Lipschitz at a rate nu <= delta_#/8 in top cells, and W_j := down-averages. a_j := I^grad(V_j; W_j). By (TS) with compatible weights, Y_j(W_j) = Y_{j+1}(W_{j+1}) - e_j(W_{j+1}). Theorem EX-loc gives e_j(W_{j+1}) >= c_1 e^{-C nu_{j+1}} a_{j+1} - C(L) c_{j+1}, with c_{j+1} := cub(V_{j+1}; W^+) + cub(V_j; W^+). Prop TOP-W at level j + 1, with W^+ <= C_w W, gives a_{j+1} >= (Y_{j+1}(W_{j+1}) - C(L) Cub_{j+1}(W)) / (C_T C_w) - C cub(V_{j+1}; W). Hence, for either sign of Y,

    Y_j(W_j) <= q_h Y_{j+1}(W_{j+1}) + C(L) ( c_{j+1} + Cub_{j+1}(W) ),    q_h := 1 - c_1 e^{-C nu} / (C_T C_w) < 1, free of j and k.        (HF)

**Theorem COMP-ii-g.** *Let I_k(V; W) := I^grad_k(V; W) + cub(V; W), and suppose (COMP)(i), first clause, or any bound cub(V_{k-m}; W_{k-m}^+) <= C rho^m cub-bar, with rho < 1. Let q-bar := max(q_h, 2 rho). Then for all m <= k:*

    sum_{c at level k - m} W_{k-m}(c) |grad theta_c|^2 <= C(L) q-bar^m ( I_k(V; W_k^+) + cub-bar ).

*From (COMP)(i), rho = L^-2 and cub-bar = f_loc^3: by Hoelder sum_c |theta_c|^3 <= (sum_c |theta_c|^4)^{3/4} (s^-4)^{1/4} <= C s^2 f_loc^3. So for W_k := w_{c_k} of rate at most delta_#/8, this is (COMP)(ii) with s^2 replaced by q-bar^m.*

*Proof.* Iterate (HF) from the top: Y_{k-m} <= q_h^m Y_k + C(L) sum_{l < m} q_h^{m-1-l} rho^l cub-bar. Y_k <= C_T I_k + C(L) Cub_k by TOP-W. And c_1 a_{j+1} <= e_j + C(L) c_{j+1} = Y_{j+1} - Y_j + C(L) c_{j+1}, with -Y_j <= C(L) Cub_j, as each e_i >= -C(L) c_{i+1} by Theorem EX-loc. QED

**Corollary GS (Prop GS, W = 1).** Sum Theorem EX-loc over the chain and use (TS) and TOP-1: c_1 sum_{j<k} I^grad_{j+1}(V_{j+1}) <= 2 C_1 I^grad_k(V) + C(L) ( cub(V) + sum_{j<k} cub(V_j) ). With (COMP)(i) clause 1 the last sum is at most C(L) N_k^4 f^3 in the worst case, and on each top cell at most C f_loc^3; or with sup flux falls, at most C f_k E_k(V). With weights, the same with Prop TOP-W. No toron term from this step.

**Is the weaker rate enough?** Yes for every reader. Prop DS and Lemma EX2 write "geometric" and sum a_m^{1/2} over m, and that sum converges with q-bar^{m/2}. (i)'s clause 1 and the clauses at variations carry their own s. Prop GS at W = 1 needs only the sum. No consumer reads s^2 as a number: the only places are the words "C(L) s" and "C s" in EX2 and DS, which become q-bar^{m/2}.

**(COMP)(i), clause 1, from the fine level (implication of (R3), by Lemma CJ).** Jensen on omega-space gives |L^{2 j} E_omega F|^4 <= L^{8 j} E_omega |theta^0(z)|^4, and the partition of unity gives sum_c |L^{2 j} E_omega F|^4 <= L^{4 j} sum_z |theta^0(z)|^4 = s^4 ||F||^4_{L^4}, with constant 1. By (CR), and E_i(c^+) <= 2 E_0(c^{++}) from (V_W) with an indicator weight, |r^{(j)}(c)| <= C(L) ||F||^2_{L^2(c^{++})} <= C(L) s^2 ||F||^2_{L^4(c^{++})}, so sum_c |r^{(j)}(c)|^4 <= C(L) s^8 f^8. So sum_c |theta_c|^4 <= C s^4 f_loc^4, for f small in L. *So "(R3) by scale counting" is now a proof, given (R3) at the fine level.*

### 4.2 The form with s^2

*Label: implication, given (AD) of `library/composite-adjoint.md` and (R3). Repairs D4 of the closure gate. Not needed by any consumer.*

**Lemma W (lattice Weitzenboeck, any field of flux at most 1/6).** ||D^* theta||^2 + ||B||^2 = I^grad + X, with |X| <= C cub(U), where D^* is the backward covariant divergence and B the Bianchi defect. *Proof.* Expand both squares. The diagonal of ||D^* theta||^2 is P, the diagonal of ||B||^2 is T, and the cross terms cancel by the swap of Lemma BT, up to its commutators. QED

With a cut-off eta at top scale, in level-k units, this gives ||eta grad F||^2 <= 2 ||eta D_U^* F||^2 + C Yhat_k(loc) + C ||F||^3_{L^3} + lattice term, by applying it to eta (theta - theta-bar) in the frame of the top box, with F-bar the mean: the term in grad eta reads only the variance, so no energy appears. D_U^* F = Q^* lambda on the Wilson form up to a quartic correction, the contour part vanishes as D'^* lambda = 0 (Step 1 of (LIFT-I)), and (AD) bounds the rest by C |lambda|_loc. *The multiplier needs no Taylor expansion:* for a bump G with Q^o G = b on one parent bond, supported in its block, of norm C, lambda(b) = D A(U)[G] = <F - F-bar, d_U G> + commutator. So |lambda|_loc^2 <= C Yhat_k(loc) + C f^4. With Prop TOP-W and (R3): ||grad F||^2_{L^2(W)} <= C(L) I_k(V; W^+).

*Down to level j.* Lemma CJ with block side ell := L^j at the fine level: E_omega |F - c|^2 is at most C ell^2 avg_{B^+} |grad theta^0|^2 by the box Poincare inequality, plus the frame term, the holonomy of a loop of area ell^2, which by Hoelder in L^4 contributes at most C ell^4 avg_{B^+} |theta^0|^4. In lattice sums, Yhat_j(W) <= C s^2 ||grad F||^2_{L^2(W)} + C s^4 ||F||^4_{L^4(W)}. So with Theorem EX-loc, a_j <= C(L) s^2 I_k(V; W^+) + C s^4 f^4 + C(L) cub-sum <= C(L) s^2 I_k(V; W^+). That is (COMP)(ii) as printed.

*What this repairs.* D4 asked for AN1 per block in a lattice Uhlenbeck gauge. (CR) replaces both, and the Poincare step replaces the convolution of Step 5.

## 5. Lemma EX2, rewritten

*Label: implication, level of each term, given (A1) to (A4) below. Answers D1, D2, D3 of `gates/lemma-ex-7c12c6981.md`.*

**The change of method.** The printed proof ran Lemma EX's Steps 3, 4 on delta F, with IMS balls of radius f^{-1/2}. There a transport across a ball costs r |delta F|, and that is D1. Here no ball appears. The identity (V_W) is differentiated twice in time at block scale, where a transport costs C(L), which is allowed.

### 5.1 Statement

*Gauge (D3).* V_j(t) := N^{(j)}(U_0 e^{H(t b)}), with H(.) the solution of Prop AN3 for V e^{t b}, and N^{(j)} the contour-free chain. So V_j(t) is the minimal chain of V e^{t b} up to a level-j gauge. delta F, h_j := d/dt log (V_j(t) V_j^-1), h_j^{(2)} and delta^2 theta are read in this gauge. b_m(b; W) := sum_{c at level k-m} W(c) sum_e |grad_e delta_b theta_c|^2, grad_e the covariant difference at t = 0.

*Inputs.*
- (A1) (COMP)(i), with weight: sum_c W |theta_c|^4 <= C s^4 f^4, sum_c W |delta theta_c|^2 + sum_c W |delta^2 theta_c|^2 <= C(L), for W = e^g with g centred at b of rate at most a quarter of the kernel's.
- (A2) sum_c W ( |h_j(c)|^4 + |h_j^{(2)}(c)|^4 ) <= C(L), same W. *Reading:* (2) of Prop AN3 for H, H_2 in Eps(B), the box Sobolev bound, and Lemma AN1's linear bound |h_j(b)| <= C_1 e_j(b) with (1) of `library/analytic-lift.md`, plus its quadratic term for h^{(2)}.
- (A3) |d^2/dt^2 ( E_0(U(t); W_0) - E_k(V(t); W_k) )| <= C(L): (A1) at m = 0, m = k.
- (A4) Theorem COMP-ii-g.

**Lemma EX2'.** *Let W := e^g as in (A1). With F^j_y the level-j plaquette angles in the axial gauge rooted at y, at each t, and root frame the chain's frame at y,*

    sum_{j<k} sum_{y, q} W(y) L^4 Var_{chi_y}( d/dt F^j_{y,q} ) <= C(L),        (V-dot)
    sum_m b_m(b; W) <= C(L).        (EX2')

*(EX2') is Lemma EX2 as printed, with b_m defined. The fine level m = k is one term, bounded by 4 ||delta theta^0||^2.*

### 5.2 Proof of (V-dot)

*Differentiate (V_W).* Fix j, write F := F^j_{y,q}. The variance is quadratic, so for any frame,

    d^2/dt^2 Var_y(F(t)) = 2 Var_y(F-dot) + 2 Cov_y(F, F-ddot).

With e_j(t; W) of (V_W), and R_{y,q}(t) := 2 <theta'_q(y), r_{y,q}> - |r_{y,q}|^2, summing over j and using the exact chain sum:

    2 sum_j sum_{y,q} W L^4 Var_y(F-dot) = Y-ddot - 2 sum_j sum_{y,q} W L^4 Cov_y(F, F-ddot) + sum_j sum_{y,q} W R-ddot_{y,q}.        (D)

**This has all the terms D2 asks for.** F-ddot is the full second variation with the transports:

    F-dot = Ad(T) ( delta theta + [tau-dot, theta] ),    F-ddot = Ad(T) ( delta^2 theta + 2 [tau-dot, delta theta] + [tau-ddot, theta] + [tau-dot, [tau-dot, theta]] ),

with tau-dot the variation of the transport from y to z in the gauge of 5.1, including the root rotation from N^{(j+1)} to the axial frame, of size the contour average of h_j. *Both live in a block.* So with B-tilde(y) a finite region, N_1(y) := sum_{B-tilde(y)} |h_j|, N_2(y) := sum_{B-tilde(y)} (|h_j^{(2)}| + |h_j|^2), we have |tau-dot| <= C(L) N_1(y), |tau-ddot| <= C(L) N_2(y).

*Size of F-ddot.* Hoelder with (A1), (A2), using l^2 inside l^4: sum_y W N_1^2 sum_{Box(y)} |delta theta|^2 <= (sum W N_1^4)^{1/2} (sum W |delta theta|^2) <= C(L), and sum_y W N_2^2 n_y <= (sum W N_2^4)^{1/2} (sum W n_y^2)^{1/2} <= C(L) s^2 f^2, and N_1^4 n_y the same. So G_j := sum_{y,q} W L^4 <|F-ddot|^2>_{chi_y} <= C(L), uniformly in j. **That is the place where D1's l^4 repair is used, and it is at block scale.**

*Cov.* For W = e^g take W-tilde := e^{2 g + g'}, with g' a decaying profile of the same rate. Cauchy-Schwarz:

    |sum W L^4 Cov_y(F, F-ddot)| <= ( sum e^{-g'} L^4 sigma_y^2(F) )^{1/2} ( sum W-tilde L^4 <|F-ddot|^2>_y )^{1/2} <= C(L) q-bar^{(k-j)/2}.

The first factor is the *local* variance near b. By (V_W) and Theorem EX-loc, sum_{y,q} W' L^4 sigma_y^2 <= e_j(W') + C(L) c_{j+1} <= Y_{j+1}(W') + C(L) Cub_{j+1}(W'), so (A4) applies. This is the one place that reads (COMP)(ii), and it reads only that the sum of square roots converges.

*Remainder.* In the t-dependent axial gauge at y, r_{y,q} = Phi(a(t)), with Phi analytic on a polydisc of radius c/L, Phi(0) = 0, D Phi(0) = 0, by Lemma LE. Links in that gauge: |a|^2 <= C(L) n_y, and, by Stokes on the strips, |a-dot|^2 <= C(L) N_d(y) := C(L) sum_{Box(y)} |F-dot|^2, |a-ddot|^2 <= C(L) (N_dd(y) + N_d(y)^2), N_dd(y) := sum_{Box(y)} |F-ddot|^2. So |r-dot| <= C(L) (n_y N_d)^{1/2} and |r-ddot| <= C(L) (N_d + (n_y N_dd)^{1/2} + n_y^{1/2} N_d). In R-ddot = 2 <theta'-ddot, r> + 4 <theta'-dot, r-dot> + 2 <theta', r-ddot> - 2 |r-dot|^2 - 2 <r, r-ddot>, with Hoelder and l^p nesting, each sum has a factor ||theta||_{l^4}-type at level j or j + 1:

    sum W |theta'-ddot| n_y <= C(L) s^2 f^2,   sum W |theta'-dot| (n_y N_d)^{1/2} <= C(L) s f,   sum W |theta'| N_d <= C(L) s f,

and the rest are smaller. Weights as for Cov. So sum_j |sum W R-ddot| <= C(L) sum_j s_{j+1} f <= C(L), a geometric sum with ratio 1/L and *no flux falling input*: only (A1). QED of (V-dot), with (A3).

### 5.3 From the variance to the gradient

**Lemma TL at a variation.** Lemma TL's proof is a list of linear identities in the angles, for fixed t, plus second-order errors. Differentiate them at t = 0 in the t-dependent axial gauge at y. The linear functionals of F become the same functionals of F-dot, bounded by Var(F-dot). The errors are analytic and vanish to second order, so their t-derivatives are at most C(L) (n_y^+ + Theta_y^2)^{1/2} (N_d^+)^{1/2}. In that gauge the links read by the fine and the coarse Bianchi defects vary by at most C(L) (N_d^+)^{1/2}, by Stokes on strips of length C L, so **the term [h, theta] is at most C(L) (N_d^+)^{1/2} Theta_y, read at block scale**: in a gauge fixed far away the same term is what D1 measured growing. So, with xdot_{q,e}(y) the t-derivative of the flat difference of theta'_q by L e in that gauge,

    sum_{q, e} |xdot_{q,e}(y)|^2 <= C sum_{y'' in Y_1(y), q'} L^4 Var_{chi_{y''}}( F-dot in gauge at y ) + C(L) (n_y^+ + Theta_y^2) N_d^+(y).

A variance in the gauge at y against the gauge at y'': they differ by Ad(g) with g constant up to C(L) (a + a''), and by a rotation rate phi(z) with |phi| <= C(L) (N_d^+)^{1/2}. So the difference of the two sigmas is at most C(L) ( (n^+ N_d^+)^{1/2} ) in L^2 units.

*To the gauge of 5.1.* grad_e delta theta'(y) = xdot(y) + O( C L a |delta theta'| ) + O( N_1(y) |theta'(y + L e)| ). So, summing over y with W, the errors are at most C(L) (sum W (n^+)^2)^{1/2} ||delta theta'||^2 + C(L) (sum W N_1^4)^{1/2} ||theta'||_{l^4}^2 <= C(L) s^2 f^2, geometric. With (V-dot) this gives (EX2'). QED

### 5.4 What Prop DS reads

*Order 1.* |D(Z o Lambda_m)[b]| <= C(L) a_m^{1/2} ||delta F||_{l^2}, by (SRC)'s first-derivative bound, so the sum over m converges by Theorem COMP-ii-g with no use of EX2.

*Order 2.* <Delta delta F, K Delta delta' F> <= (b_m b'_m)^{1/2}, summed by (EX2') and Cauchy-Schwarz. <Delta F, K Delta delta^2 F> <= a_m^{1/2} ||delta^2 F||_{l^2} <= C(L) q-bar^{m/2}. The transport terms that gate D1 of the closure lists, |h| |F| |Delta delta' F|, are at most (sum W |h|^4)^{1/4} (sum W |F|^4)^{1/4} b'_m^{1/2} <= C(L) s f b'_m^{1/2}, geometric. In the axial gauge at x of Prop DS, "link size |delta F|" should read: link size C(r) times the l^2 norm of delta F on the ball, with polynomial growth in r taken by the tree decay. Since zeta is gauge invariant at each order, the frame at x may be chosen for each of delta, delta' separately. So Prop DS stands as an implication, with "C s" replaced by q-bar^{m/2}. (Not rewritten here: its owner has it. The repair of its own D1 in the closure gate is this paragraph.)

## 6. Status of each statement

| Statement | State here | Reads |
|---|---|---|
| Lemma EX, weighted, as printed | **Proved** (Theorem EX), with the toron term deleted and c_1 = 1/810 free of L | The map only; flux(U) <= phi_0(L) |
| Lemma EX, local form | **Proved** (Theorem EX-loc), no E term, W >= 0 arbitrary | The map only |
| Lemma BT, T <= 2 P + 8 f E + C f^2 E | **Proved**, the 2 is sharp | Nothing |
| c_e > 0 over all P | **Proved**: c_e >= (1 - L^-2)/96 for all P and L, from Theorem V and Lemma BT at r = 0, against 0.0988 measured. No longer read by Lemma EX | Nothing |
| Lemma LIFT, TOP-1 (W = 1) | Implication | Item (o) for A_k <= E_0 of a class chain; L >= L_0 |
| Prop GS at W = 1 | Implication: Theorem EX, TOP-1, and the sum of cub | (COMP)(i) clause 1, or sup flux falls |
| Prop TOP-W | Implication, level of each term | Theorem F at the true lift, (R3), item (o), Lemma AN1's linear bound |
| (COMP)(ii) | Implication, **with q-bar^m in place of s^2** (Theorem COMP-ii-g) | Prop TOP-W, (COMP)(i) clause 1 |
| (COMP)(ii) as printed, with s^2 | Implication (4.2) | Also (AD), (R3); Lemma W is proved |
| Lemma EX2 | Implication, rewritten (Lemma EX2'), gauge fixed | (A1) to (A4) |
| Prop DS | Not rewritten; 5.4 says what changes | Its owner |

**The gate's list.** `gates/lemma-ex-7c12c6981.md`: D1 dissolved (5.2, 5.3: transports at block scale, l^4 only where it costs nothing). D2 repaired (the full F-ddot is in (D)). D3 repaired (5.1). D4 gone for Lemma EX and for Lemma TOP; the tail in Lemma O3 and (SRC) is untouched. D5: not read here. D6, D7: moot, no Plancherel and no IMS. *No field with topological charge at small flux had been tested:* the proofs above read no sector; T6 is the test (Section 7). `gates/closure-bad958abb.md` D4 repaired by (CR) and Lemma CJ, with no Lemma AN1 and no Uhlenbeck gauge, in 4.2.

## Obligations

- discharged: Lemma K, Theorem V, Lemma LE, Lemma IP, Lemma NN, Lemma BT, Theorem EX: the excess of any field in the fibre is a sum of local variances up to second order, so Lemma EX holds with no toron term, no symbol, no IMS, in every sector, on every torus; own proof, same-model, not gated; T0 to T4 PASS
- discharged: Lemma TL, Theorem EX-loc: pointwise bound of the parent gradient by local variances, compatible weights, no term in E; own proof, same-model, not gated; T7 PASS
- discharged: c_e >= (1 - L^-2)/96 over all P, abelian, from Theorem V and Lemma BT; own proof, not gated
- implication: Lemma LIFT, one-level exact lift with gain, tensor chain map plus block frames plus Picard, constants soft; TOP-1 given item (o); T8 to T10 as reported, with L_0 not computed -> Prop GS at W = 1
- implication: Lemma CJ, (CR), Prop TOP-W, composite remainder free of the level from one-level remainders; given Theorem F at the true lift, (R3), Lemma AN1's linear bound -> Theorem COMP-ii-g
- implication: Theorem COMP-ii-g, (COMP)(ii) with q-bar^m, by hole-filling in the level; given Prop TOP-W and (COMP)(i) clause 1 -> Lemma EX2', Prop DS
- implication: (COMP)(ii) with s^2, Section 4.2; given also (AD) and (R3); no consumer needs it
- implication: Lemma EX2', second variation of the variance identity in block-local gauges; given (A1) to (A4) -> Prop DS, so low orders of R_k
- unchecked: C_T and q_h are not computed; L_0 of Lemma LIFT is about 11 at the abelian level by T12, for this beta
- gap: the upper bound with boundary data, for (VAL^d): Theorem EX-loc applies as it stands on free parents, since (V_W) reads only the region of each parent in supp W, but Lemma LIFT next to a frozen layer and Prop TOP-W with Theorem F-D are not written
- unchecked: Lemma TL's and Lemma LIFT's non-abelian steps at the level of every BCH term: written as second-order remainders of finite-dimensional analytic maps with C(L), checked numerically at L = 3 only

## 7. Numerics, summary

Criteria: `checks/excess/CRITERIA.md`, written before each run; additions dated and marked. All numerics under the lock. A search that finds nothing does not prove a bound; here each run tests a step of a written proof.

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
| T6a lift of a charged parent | PASS on field a: second Chern number 2, constant abelian flux plus smooth non-abelian modes, N' = 8, L = 3, d = 4, f = 0.129. Residual 1.9e-12 after 5 Picard steps, rate 0.01 per step. Charge estimate 1.989 on V', 1.994 on U. e_tr/I^grad = 0.219. Field b: see below |
| T6 true minimiser, charged | Running, see below |

## Requests

**TO THE OWNER OF `library/sector-values.md`.** (1) Section 3A: Lemma EX can be replaced by Theorem EX or Theorem EX-loc; Steps 1 to 4, c_e, IMS and "(toron term)" are not read, and R1 is not needed. (2) Lemma TOP: TOP-1 at W = 1, and Prop TOP-W with weights, in place of the Taylor proof. If weights are kept in Prop GS, use down-averaged weights, which remove the quadrature error of a fixed W. (3) (COMP)(ii): read q-bar^m where a consumer reads s^2, or keep s^2 and read (AD). (4) Lemma EX2: Lemma EX2'. (5) Prop DS: 5.4. (6) The remark in Section 8 (14) that the lift "lies in the fibre, so it is at least the one-level Wilson minimum, at second order at flat data" can go: positivity is now Theorem V, for every field in the fibre.

**TO THE LEAD.** Lemma O3's tail, and so (SRC) and Theorem VAL's term N_k^4 Phi(e^-8 N_k/4), are untouched: that tail comes from Taylor of the source at a cut field, not from the excess. Whether a block-frame comparison could remove it there too was not tried; it is outside this item.

## Read and not read

Read: `FINISH.md`, `GOAL.md`; `library/sector-values.md` Sections 0 to 3B and 7, 8 in part; `library/analytic-lift.md` in full; `library/critical-class-and-excess.md`; `library/block-poincare-energy-package.md` to Theorem 6; `library/composite-adjoint.md` head and Lemma AD1; `library/fibre-propagator.md` Setting and Theorem F; (R1) to (R3), Text 1, Text 3.1 to 3.3 of `parts/hard-core--mapped.md`; Prop 10' and items (f), (f') of `library/relative-density-bound.md`; `gates/lemma-ex-7c12c6981.md`, `gates/closure-bad958abb.md`; `checks/gate_ex/ex_core.py`.

Not read: `parts/hard-core--independent.md`, any gate on it, the Sussman-Alpoge repository, Theorem F-D, HS-P, HS-T, `library/lattice_sobolev_box_gauge.md`, `library/lattice-uhlenbeck.md`, `library/one-step-closure.md` beyond grep lines, Sections 4 to 6 of `library/sector-values.md` beyond the statements. Inputs of Sections 3 to 5 are taken at their labels: none of them was checked here.
