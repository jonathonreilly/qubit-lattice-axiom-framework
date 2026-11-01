lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-01T19:34Z

# Excess: Lemma EX, Lemma EX2, (COMP)(ii)

Queue item 7 of `FINISH.md`, mapped side, frozen at commit `d9d4496f1`. Research-stage working state. Grants no status.

Status: started 2026-11-01T07:34Z. Sections appear below as they are written.

## 0. Working summary (updated as sections land)

**Frozen statements.** Lemma EX, Lemma EX2, (COMP) as printed in `library/sector-values.md` at `d9d4496f1`, read with `gates/lemma-ex-7c12c6981.md` and `gates/closure-bad958abb.md`.

**New route for Lemma EX (under test in this file): no symbol, no IMS, no gauge patch.** The one-level excess is, up to second-order remainders, an exact sum of local variances:

    E_j(U) - E_{j+1}(M U) = sum_{y, p} L^4 Var_{chi_y^p}(F^{(y)}_p) - remainders,

because the coarse plaquette angle is L^2 times an average of fine plaquette angles against a tent-tent-box-box kernel chi_y^p, and these kernels are a partition of unity on fine plaquettes. Overlapping tents control the in-plane coarse gradient, and a discrete Bianchi identity bounds the transverse gradient by exactly twice the in-plane one (sharp at p = (1,1,1,0), a = e_4, which is the gate's minimiser of c_e). Nothing global is read, so sectors and torons do not enter.

## 1. Lemma EX: a proof with no symbol, no IMS and no toron term

*Label: discharged at the level of a written proof, same-model, not gated. Reads the definition of the block map and nothing else: not Theorem F-D, not Prop AN3, not the lift's minimality, not c_e.* Checks: `checks/excess/v1_identity.py`, log beside it, criteria T0 to T4 in `checks/excess/CRITERIA.md`, written first, all PASS at the first run on the comb map of `checks/gate_ex/ex_core.py`, SU(2), d = 4, L = 3 (T0 also L = 5).

### 1.1 Setting

Level-j lattice with unit spacing, torus of side n = L N', N' >= 3, L odd; the parent lattice is (L Z / n Z)^4. U is a level-j field, V' := M(U) its Balaban average (the deterministic map; class fields carry no rough label). theta_{mu nu}(z) := log of the plaquette at z, with theta_{nu mu} = -theta_{mu nu}. In the normalisation U = exp(i t . sigma), |Ad(e^theta) - 1| <= 2 |theta|. flux := max |theta|. E(U; W) := sum_{z, mu < nu} W(z) |theta_{mu nu}(z)|^2.

W > 0 with |log W(x) - log W(x')| <= nu |x - x'|_inf / L, nu <= 1/8. So nu is the rate in parent cells. S_e Phi(x) := Ad(V'_e(x)) Phi(x + e), with e a parent unit, is orthogonal on l^2, and grad_e := S_e - 1. I^grad(V'; W) := sum_{x, p, e} W(x) |grad_e theta'_p(x)|^2. Split it as P(W) + T(W): P the in-plane terms, e in {mu, nu} for p = (mu, nu); T the transverse ones.

**Kernels.** tau(t) := #{a in [-r, r] : a <= t <= a + L - 1}, r := (L - 1)/2: the discrete tent, with sum_t tau(t) = L^2, tau(t) + tau(t - L) = L on its range. For orientation (mu, nu) and a parent site y,

    chi_y(z) := L^-6 tau(z_mu - y_mu) tau(z_nu - y_nu) 1[|z_rho - y_rho| <= r] 1[|z_sigma - y_sigma| <= r].

**Lemma K.** (a) sum_z chi_y(z) = 1. (b) sum_y chi_y(z) = L^-4 for every z, and 0 <= L^4 chi_y <= 1. (c) Abelian, for any bond angles a with curl da: the Q-image of a has parent curl exactly L^2 <da>_{chi_y}. (d) For y' := y + L e_mu, min(chi_y, chi_{y'}) has mass eps_L := (1 - L^-2)/4 >= 2/9.

*Proof.* (a), (b): products of one-dimensional sums, using sum_{y_mu} tau(t - y_mu) = L. (c): Lemma 3.1 of the producer removes the contours from the curl, and the curl of Q_path over a parent plaquette is avg_{x in B(y)} of the sum of da over the L x L square at x. Counting x for each fine plaquette gives chi_y. (d): the two kernels differ only in the factor tau along mu, and sum_t min(tau(t), tau(t - L)) = (L^2 - 1)/4. QED. (T0 checks all four.)

### 1.2 The local expansion

Box(y) := y + [-2 L, 3 L]^4 and n_y := sum over plaquettes in Box(y) of |theta|^2, with Box read on the torus when it wraps (N' <= 5): the paths used below stay in a slab of width at most 3 L, so they embed for N' >= 3, and n_y only needs to dominate what they read.

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
