# H-W: a localized-weight obstruction and the nonlinear estimate still needed

Pinned source: `216dcff7e69c1565c4a43d3cdb0a7ecc6341eb56`, 2026-11-01, OpenAI Codex, mapped side. Author investigation; no independent gate or audit, and no numerical calculation. The source of the trial is `excess-finite-range-repair.md`, Sections 1--4, including its initial support enlargement. Lemma EX is neither re-proved nor changed. The checkpoint and obligations live in `../parts/hard-core--excess.md`.

Constant convention: “absolute” may depend on d=4, SU(2), the fixed comb and spline profiles, and a fixed weight-rate ceiling, but not on x, L, depth, volume or position. C(L) additionally permits L. Constants in the falsifier explicitly labelled (L,M,B) need not be uniform; one fixed choice suffices. The slow-weight target has nu<=min(nu_0,delta_#/8); if the added J_kappa tail is used, also take nu<=kappa/2 with kappa fixed below the absolute linear inverse rate. None of the missing nonlinear constants is claimed to have these uniformities already.

**Disposition.** The arbitrary-weight reading of H-W with the displayed, field-dependent `W^+` fails on the analytic minimizing branch already used by the consumer. A slow log-Lipschitz-weight reading is not refuted. For that reading, the genuine nonlinear fibre comparison below remains a gap. This is the first stop; HC-W, CJ/CR at general depth, and the dependent upper bounds are not established here.

## 1. What the localized test asks

**Discharged formulation of the test.** Fix one level, one odd L >= 5, and one sufficiently large finite periodic four-dimensional lattice. Put a small commuting parent perturbation on a slab far from a chosen top block B, and put W=1_B. All fields below tend to the trivial connection; “far roughness” means a spatially varying small field, not a violation of the class threshold. Let its amplitude be t, taken to zero with L, the separation and the volume fixed.

The repaired trial weight uses

    q=B'_L f=O(t),   K_q(z) proportional to q^floor((|z|_infinity-a)_+/R),
    W^+=max(P_a W, K_q*P_a W),   a=232, R=68.

Its limit as q tends to zero has **finite support**, including the whole plateau |z|<a+R, not just |z|<=a. Any fixed finite number of the permitted enlargements and convolutions still has this property. Choose the separation beyond this entire support and the trial's local construction radius. On a fixed finite torus, W^+ is then O(q) on the trial's source support. Periodisation does not change this: the sum of all the farther shells is O(q), with the usual polynomial shell count. This uses the corrected kernel on squared flux; it makes no use of the withdrawn squared-kernel estimate.

A falsifier is therefore a nonzero **linear** curvature response at B of the minimizing lift, when the trial is flat there. H-W would require its squared relative-field norm, of order t^2, to be at most O(t^3)+O(t^4). The next section constructs that response exactly.

## 2. An exact one-level linear calculation in d=4

**Discharged algebraic lemma (author proof).** Work in one fixed su(2) direction. Let the only nonzero coarse potential be v_2(j)=delta_{j,0}, depending on the first coordinate j and constant in the other three. There are M coarse cells in each direction, with M even and large; indices j are modulo M. The coarse curvature is

    b_j=v_2(j+1)-v_2(j)=delta_{j,-1}-delta_{j,0}.

At the trivial connection the contour part of Q is a coarse gradient, by the displayed definition in the mapped part, Lemma 3.1. It has zero curvature. For a fine potential A_2(x_1), independent of the other coordinates, set F(x)=A_2(x+1)-A_2(x). With r=(L-1)/2, the coarse 2-link is

    (Q_path A)_2(j)=sum_{x=jL-r}^{jL+r} A_2(x).

Taking a coarse difference gives the curvature constraint C F=b, where

    (C F)_j=sum_x t_j(x) F(x),
    t_j(x)=#{(a,s): -r<=a<=r, 0<=s<L, x=jL+a+s}.

Thus each row has the triangular coefficients 1,2,...,L,...,2,1. Adjacent rows alone overlap. Its Gram matrix on the coarse ring is

    G=C C^*=a_L I+b_L(S+S^-1),
    a_L=L^2+2 sum_{h=1}^{L-1} h^2=(2L^3+L)/3,
    b_L=sum_{h=1}^{L-1} h(L-h)=(L^3-L)/6>0.

In particular a_L>2b_L. Put

    D_L=sqrt(a_L^2-4b_L^2),
    rho_L=(a_L-D_L)/(2b_L),   0<rho_L<1.

The inverse on the infinite coarse line is g_j=(-rho_L)^|j|/D_L. To check this, away from zero use b_L rho_L^2-a_L rho_L+b_L=0; at zero use a_L-2b_L rho_L=D_L. Periodising gives, for 0<=j<M and even M,

    g_j^(M)=(-1)^j (rho_L^j+rho_L^(M-j))/[D_L(1-rho_L^M)].

Each summand has the same sign because M is even. For w=G^-1 b,

    w_j=g_(j+1)^(M)-g_j^(M),

which is nonzero at every j (including the periodic seam), since consecutive g's have opposite signs. The unique least-norm curvature with C F=b is

    F_*=C^* w.

Indeed C F_*=b and F_* is orthogonal to ker C, so every other solution has squared norm ||F_*||^2+||F-F_*||^2. At x_j=jL+r only t_j is nonzero, and F_*(x_j)=L w_j !=0. There is also a nonzero curvature strictly inside that coarse block: at x_j-1 and x_j-2 the two values are

    (L-1)w_j+w_(j-1),   (L-2)w_j+2w_(j-1).

They cannot both vanish, since the determinant is L. For L>=5 both corresponding plaquettes can be chosen inside the block, including their bond stencils.

**Why this is a sector of the four-dimensional constrained Maxwell problem.** First the true-Q and Q_path minimizations have the same curvature problem. Their difference is D'Phi; Q D omega=D'ev(omega), while Q_path D omega=D'R^0(omega). Both ev and the block average R^0 are onto coarse site functions, so either gradient discrepancy can be corrected by a fine gauge without changing curvature or torus periods. Now average a Q_path competitor over all fine translations in directions 2,3,4, and project its colour onto the specified direction. The fine translation average intertwines with the corresponding coarse average: the R^0 tiles partition that circle, and the sum of the translated R^1 rows has constant multiplicity L. Thus it preserves these transversely constant coarse data and does not increase the quadratic action. This is an averaging identity, not covariance under an individual one-site fine translation of the blocked lattice. The remaining components decouple from A_2(x_1); they cannot lower its curvature cost. Since sum_j t_j(x)=L and sum_j b_j=0, C F=b already implies sum_x F(x)=0. Hence every such F is a periodic derivative of an A_2. Its additive constant is chosen so Q_path A_2=v_2; their coarse difference is already b. Consequently F_* is exactly the curvature of the linear minimizing lift for these parent data, not a scalar analogy to it. The other three directions merely repeat this calculation and multiply the energy by a fixed positive multiplicity.

## 3. Transfer to the trial and to the nonlinear claim

**Discharged local-branch argument; class-infimum identification remains the existing premise.** On this fixed finite lattice the block map and Wilson action are analytic near the identity. The derivative of the block map is surjective (the displayed tensor right inverse, with its contour correction, is a right inverse). On the tangent fibre, the Wilson Hessian is the Maxwell energy. Its null vectors are exactly the residual fine gauges. Indeed, for a curl-free periodic field subtract the constant recording its four cycle periods; the remainder has zero sum around every closed path, by plaquette deformations and the vanishing periods, so path integration defines a periodic gauge potential. Thus the field is a constant plus a gradient. Q=0 kills that constant by its coarse periods and forces the potential's values at coarse centres to agree. Subtracting the common value gives a gauge parameter vanishing at the centres. Fix those residual gauges by block trees. The constrained Hessian is then positive definite in finite dimensions. The implicit function theorem gives an analytic local minimizing branch U(t) and

    theta_p(U(t))=t F_*(p)+O(t^2).

This is only a fixed-volume, fixed-L local argument; it claims no uniform implicit-function radius. It is enough for the falsifier. If “the class minimum” denotes the global class infimum instead of this local branch, its identification with U(t) is precisely the pre-existing item (o)/branch premise. The obstruction applies to the analytic branch that Theorem F/AN3 and the consumer use, without proving item (o).

For V(t)=exp(t v) the trial construction remains entirely in the same commuting subgroup. With t small all logs are on their principal branch. Products, exponentials, combs and contour corrections then reduce exactly to their abelian expressions, the residual m is zero, and the Picard correction Y is zero. Its curvature is the compactly supported tensor lift t T_2 b. Thus it is flat near B when the separation in Section 1 is chosen. The trial variance Yhat_tr has finite support, independent of t, and is O(t^2) on that support. Any local trial flux envelope f_B is O(t); even a global maximum in this fourth-power term would be O(t^4).

For any proposed relative representative Utilde(t)^g=exp(eta H(t))U(t), with eta=1/L, flatness of Utilde at an interior plaquette p of B is gauge invariant. Telescoping the four link products and using |exp X-1|<=C|X| near zero bounds the change in its plaquette holonomy by the sum of |eta H| on these four bonds. At fixed L this sum is bounded by C(L)||H||_Eps(B). The nonzero t F_*(p) therefore forces

    sum_B W(B)||H(t)||_Eps(B)^2 >= c(L,M,B) t^2,
    Yhat_tr(W^+) + sum_B W(B) f_B^4 = O_(L,M,B)(t^3+t^4).

Here c(L,M,B)>0 may be extremely small. All these parameters are fixed before t goes to zero. If H-W held, its right side would itself force H to be small, so a different large gauge cannot evade the local product estimate. No finite C_H works, even one depending on L, M and B but independent of t. All thresholds hold for sufficiently small t, the sector is trivial, depth is one, and the classical statement contains no coupling x. Strict positivity without a rate restriction does not help: on this fixed torus replace W by 1_B+t^2 outside B; the added right-hand contribution is O(t^4).

**Implication: failure of the unrestricted reading.** H-W with the field-dependent K_q enlargement and arbitrary nonnegative W is incompatible with this analytic minimizing branch. Shrinking a_* or increasing x cannot repair a linear tail by a higher-order error. This is not a counterexample to H-W for slow weights, or a no-go theorem for weighted minimizer comparisons.

**Gap: admissible repair.** Either restrict the comparison to the consumer's positive scalar weights with |log W(B)-log W(B')|<=nu d(B,B'), or add a tail independent of the flux. For example, with a fixed kappa>0 below the linear inverse rate, enlarge W by J_kappa*W, where J_kappa(z) is the normalized exp(-kappa |z|) kernel, in addition to the full repaired trial enlargement. A fixed K_qbar can serve the same purpose only if its decay rate is chosen slow enough; replacing q by qbar is a change of the comparison's weight, not a conclusion about the displayed K_q. For nu<kappa, the exponential moment gives J_kappa*W<=C(kappa,nu)W. Such changes remove this particular obstruction; they do not prove the nonlinear estimate.

## 4. The actual nonlinear map and the precise remaining inequality

**Discharged definition, not a finite-displacement estimate.** At the true minimizing U, use the contour-free map N_U^(n) of the energy package, Theorem 7 Step 1, with its gauges fixed at that base point. In top-scale units define

    C_U(Z)=log(N_U^(n)(exp(eta Z)U) V^-1),
    R_U(Z)=C_U(Z)-Q_U^o Z,   eta=L^-n.

C_U(0)=0 and D C_U(0)=Q_U^o. On a genuine N-fibre displacement, the **exact** equation is Q_U^o Z=-R_U(Z), not Q_U^o Z=0. Even a representative of a point on the true M-fibre must first be aligned with this contour-free fibre; N differs from M by a field-dependent coarse gauge.

Given Theorem F at U, let B_U be the H component of Sad#_U^-1(0,z). It is a right inverse of Q_U^o in the gauge P_r D_U^*H=0. A candidate nonlinear local fibre chart, in this slice, is

    Z(h)=h+B_U z(h),   Q_U^o h=0,   P_r D_U^*h=0,
    z(h)=-R_U(h+B_U z(h)).                                      (CH)

These equations specify the nonlinear map that would have to be used. They are not the trial equation Psi_V(Y)=0 of the finite-range repair: that equation adjusts parent input to produce a trial, not a secant between trial and minimizer. A local implicit-function construction of (CH) is possible at any fixed n and volume. Uniformity, its domain containing the specified trial, and the controlled gauge converting it back to the true parent-fixed fibre are additional requirements.

Theorem F can be read **at U**, conditional on its own inputs and (R3)'s box L^4 curvature bound. It does not assert a pointwise curvature bound at U. Its item (iv) maps tangent representatives to linear chart coordinates; it supplies no nonlinear endpoint coverage. In particular its hostile point (6') explicitly says that an Eps ball by itself does not give the summable contour control of (R3). No application of F at every point of an unconstructed interpolation is made here.

**Gap (NF-W), exact sufficient comparison still missing.** Let Phi be a genuine chart of the parent-fixed fibre on a domain containing the segment {s h:0<=s<=1}, with Phi(0)=U and Phi(h) gauge equivalent to the specified trial by a gauge fixing its parent. Normalize its tangent coordinate by the class representatives of F. Let S(h)=A(Phi(h)), A_U=D^2 S(0) (the constrained class Hessian bH), and J_h=D S(h). In an admissible slow weight, or using the augmented tail just described, one must prove endpoint coverage and the following estimates with constants free of n, volume, x and position:

    ||H||_(Eps,W) <= C_ch ||h||_(Eps,W),
    ||A_U^-1 [J_h-A_U h]||_(Eps,W) <= epsilon ||h||_(Eps,W),
    ||A_U^-1 J_h||_(Eps,W)^2
        <= C_0 Yhat_tr(W_dagger) + C_1(L) sum_B W_dagger(B) f_B^4,
    epsilon<1, uniformly (for example <=1/2).                    (NF-W)

H is the requested parent-fixed relative logarithm, not an arbitrary tangent vector; W_dagger contains all trial enlargements and any additional inverse tail. The inverse acts on class tangent functionals with the gauge normalization of F. No bound on extending arbitrary weighted functionals to that space is silently assumed: the displayed inequalities are for the inverse response itself.

The second line is a **secant** estimate. The exact expression whose norm must be controlled is

    J_h-A_U h = integral_0^1 [D^2 S(s h)-D^2 S(0)] h ds.          (SEC)

The last line controls the trial's **fibre derivative**, J_h(v)=D A(Phi(h))[D Phi(h)v]. Replacing D Phi(h)v by a vector tangent only at U drops precisely the nonlinear constraint and gauge errors. Lemma AN1's local quadratic remainder and AN2's multilinear claims suggest an epsilon of size C(L) r for r=sup_B ||h||_Eps(B), but this session does not derive (NF-W), its endpoint coverage, or the last line from them. Item (o)'s qualitative chart sketch does not supply those estimates for this trial at arbitrary depth.

**Implication, proved.** If (NF-W) holds, the identity h=A_U^-1 J_h-A_U^-1[J_h-A_U h] gives

    ||H||_(Eps,W)^2 <= C_ch^2/(1-epsilon)^2
        [C_0 Yhat_tr(W_dagger)+C_1(L) sum_B W_dagger(B) f_B^4].   (H-W-dagger)

This is a corrected sufficient H-W form; no existence premise has been discharged by writing it. Its leading coefficient is absolute only if C_ch, (1-epsilon)^-1 and C_0 are absolute. A C(L) coefficient confined to the fourth-power error is harmless for the intended C(L) cubic remainder. A bare C(L) in C_0 is a linear loss and cannot be absorbed by taking the flux smaller. When genuinely multiplied by a small r or f, C(L) can be paid by choosing the smallness threshold after L. This distinction is necessary before asserting an absolute C_T.

## 5. Stopping boundary and consumer consequences

**Gap.** H-W for the slow weights actually used by FALL is not closed. Therefore HC-W, the uniform-depth transport/CR comparison, and an absolute C_T are not decided in this session. The source's existing CJ/CR claims are carried at their previous status, not newly verified. COMP-ii-g remains an implication of a valid TOP-W and its cubic decay premise; no later step is used to rescue H-W.

**Discharged constant-order observation, not a proof of FALL.** The identity (TS) uses compatible weighted telescoping, with no C_T. In the pinned `sector-values.md`, Lemma FALL expressly allows C_Y(L), C_F(L) and q(L)<1, free of depth. Its displayed contraction q_h=1-c_1/C_Y requires only a finite depth-independent C_Y, enlarged if necessary so C_Y>c_1. A final rate must be strictly above the contraction and forcing rates to cover resonances. Thus C_T(L) alone would not break (TS) or this fixed-L scalar mechanism. The constants list in `one-step-closure.md`, Section 1, nevertheless places C_T before L; that order is not established by a C_T(L) proof. No other use of that symbol or the full closure argument has been certified here, and no consumer file was edited.

For the unrestricted K_q-weight claim, neither an absolute C_H nor C_H(L) exists on the branch above. For the slow-weight claim, even a uniform C_H(L) is still open. It would be incorrect to announce C_T(L) as the proved truth. The current result is the localized obstruction, the exact nonlinear map to be controlled, and the named inequality (NF-W), with the stop at item 1.
