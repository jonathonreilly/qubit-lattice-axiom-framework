# Independent review of the frozen residual lattice bridge

**Disposition: the finite charged-sector determinant identities and the free fixed-depth harmonic bridge are confirmed on their stated domains. This does not close the actual off-shell residual estimate, the periodic/neutral-sector bridge, any required interchange of limits, or the Yang–Mills existence and physical mass-gap theorem. No correction to this frozen unit is required.**

The target is all 245 lines of `checks/residual_det_lattice_bridge_working.md` at commit `9761471ab46e659ce856e2b9c7c10fef2b06cf5c`, SHA256 `bb67ad564747c4c9954ae93f88aa3f43a806c88b0aefedd5ef54a945e1512c6b`. Its manifest and all `residual_det_03.*` artifacts were read completely and checked against immutable Git objects. Source/evidence coverage is bound by [the source manifest](checks/review_residual_bridge_source_manifest.json), and the final report/evidence hashes by [the receipt](checks/review_residual_bridge_receipt.json).

This is a continued independent reviewer context, requested as Astra/max by the coordinator on the user's instructions. The visible model identity is GPT-6; a runtime configuration beyond that is not introspected. This is same-family review, not cross-family, whole-PR or audit certification. Current-main methodology is `ca2bc7ddf64790da96cd43d42017d000fbfe4808`, unchanged from the preceding review. The previously completed `REVIEW_RESIDUAL_DETERMINANT_ASTRA.md` remains unchanged. No active vertex artifact was read. No source, git, PR, audit-authority or shared-summary mutation was performed.

## Criteria, independence and complete coverage

[Criteria](checks/review_residual_bridge_criteria.md) were saved at 14:04:06 UTC on 2026-10-29 before the independent computations. They require reconstructing the actual null columns, every gauge/Gram/normalization factor, the failed point-lift route, the harmonic gap, all aliases, the full Hodge determinant, the all-mode bound and A7. Generic algebra tests are explicitly separated from identification of the actual action. The later Cholesky diagnostic was separately declared before running it; the original warning output is retained.

The complete target note was read before computation. The author's script was inspected after the independent implementations were written, and was not used as a helper or implementation template. The coordinator's exact 27/27 replay is reproduction, not independent mathematical verification. New controls use an actual d=4 contour map, a different mixed-twist Bloch point and Kronecker construction, and dense multidimensional noncommuting geometry. The proof below, rather than the number of numerical predicates, supports the quantified conclusions.

Newly read contextual source ranges at the target commit are `PROOF.md` 881–996 and 3349–3442, `UIR55.md` 114–201, `UIR2_55.md` 103–164, and `FLOW55.md` 341–393. These include the actual contour definition, normalized density, gauge conventions and normalized Phi. Prior consumed ranges and methodology were retained from the preceding review and their relevant bytes checked for change; the manifest distinguishes inherited coverage from new reading. These large source files are not certified in their entirety. In particular, an incidental historical PROVEN-HERE label is not an independent result of this review. The narrow BFT_A repair mentioned by the coordinator changes none of the previously consumed lines 20–38.

| Frozen claim | Disposition and exact scope |
| --- | --- |
| Charged Cartan twist/domain, real root-pair count | Confirmed, with the restrictions below. No full-colour or neutral conclusion follows. |
| Actual augmented null columns and A1–A3 | Confirmed at the actual fine/h saddle on the common invertible finite stratum. |
| A4, scaling and mean-zero exception | Confirmed. The periodic quotient correction is nonlocal. |
| Point-lift quartic Rayleigh quotient | Confirmed failure of the proposed simple-pole inference for that representation. |
| Harmonic lift, Schur complement and A5 | Confirmed with both the Dirichlet determinant and moving factors retained. |
| Dirichlet gap/locality | Confirmed, volume-independent at fixed depth; no depth-uniform constant. |
| Complete-alias S and its principal term | Confirmed with normalized root weight ell^-4. |
| Free Hodge determinant, A6, Phi(1,0)=0 | Confirmed with the one-form Gram and massive coarse block included. |
| Free all-mode simple-pole estimate | Confirmed by the full energy argument, not only a distinguished vector. |
| Actual free principal coefficient A7 | Confirmed after high-alias minimization; an explicit omitted-minimization control fails. |
| Off-shell vertices, generic backgrounds, neutral/periodic matching and infrared limits | Not proved by this unit; remain open. |

## 1. Domain and actual null-row reconstruction

Write D for D_f, Delta=D*D, d for D_c, and Delta_c=d*d. All stars below are adjoints in the stated counting measures. The clean finite setting is a charged real root plane at a Cartan background, with the same Cartan twist around corresponding fine/coarse cycles. Restriction to roots and injection at roots then respect the boundary condition. For SU(2), conjugation by diag(i,-i) changes the sign of the two charged real components. A covariantly constant charged field at the trivial connection must be constant by transport along edges, and then vanish because of the nontrivial cycle holonomy. This gives injectivity of D and d. At each fixed finite volume, invertibility and the required positive/logarithm branches persist in a sufficiently small neighborhood. That neighborhood is not asserted uniform in volume.

The real two-dimensional charged plane is essential. A single complex-root matrix is useful notation but its determinant represents only one of the two conjugate factors when interpreted as a real operator. In the independent non-real cell, the complex scalar log determinant is 159.1705739048098 and the real-pair log determinant is 318.3411478096197. Omitting the second root is a demonstrable factor error.

At Cartan backgrounds, the Hessians and transports preserve root sectors. Derivatives confined to that Cartan background family preserve this decomposition. Generic non-Cartan background derivatives mix sectors and are not supplied by computing one root block. A nonlinear root plane is not being treated as a closed nonabelian gauge group. Rather, the full gauge-covariant action supplies the infinitesimal root-sector identity at the Cartan background. Neutral Cartan parameters retain a constant kernel under these twists; they have not disappeared from the full-colour theory.

For Q(U,V,h)=S_W(U)+Psi(U;V^h), the combined orbit holds V fixed and has tangent X_lambda=(D lambda,0,-ev lambda), after the declared h-chart sign choice. Differentiate dQ[X_lambda]=0 in any (U,V,h) direction v:

    Hess Q(X_lambda,v) = -dQ[(dX_lambda)v].

At (W*(V),V,1), Q_U=Q_h=0. X has no V component, so (dX)v has no V component either. Thus the right side vanishes even if Q_V is nonzero. This proves the entire Hessian null row, including its V cross row; it is stronger than checking only its U–U block. It uses actual fine/h stationarity and exact covariance, not a soft-distance replacement. PROOF's left-trivialized orbit sign and UIR's right-trivialized convention merely require the declared consistent chart sign; no determinant sign is lost.

This premise also defines the scope of A1–A5: they are identities at the fine/h saddle. They must not be silently differentiated as identities on independent off-family (U,rho) arguments. Away from stationarity the displayed right side contains gradient terms. A later off-shell extension or residual-vertex calculation has to retain or eliminate those terms by a proved argument.

## 2. Both eliminations and every finite determinant factor

Start from the same augmented Hessian of Q plus diag(DD*,dd*,0). Eliminating h first gives det(H_h) det(J_min), where J_min includes the fine/coarse gauge completions of the h-minimized Hessian. The point shear is

    (a,w,h)=(a'+D J eta,w',-eta),       ev J=1.

Its determinant has modulus one for every background. Its eta column is exactly the null column of the ungaugefixed Q Hessian. Only the fine gauge completion contributes to that column. Consequently its eta block is J*Delta^2 J=G_J and its a'–eta block is D Delta J. The Schur complement is precisely

    L_J=H_loc+diag(D Q_J D*,dd*),
    Q_J=1-Delta J G_J^-1 J*Delta.

Equating the two eliminations proves A1. No constancy of the shear as a function of background is needed: its determinant is identically one, while all differentiated operators still move.

The source Phi definition and the level-group Hodge identity give

    exp(2 Phi)= det(L_J) det(G_J) det(C) det(G_c)
                / [det(W) det(H_h) det(Delta_c)^2],
    G_c=d*C^-1d,    W=H_W+DD*.

This is exactly A2/A3, including the full coefficient -log det Delta_c. The level group uses C at U and d at V, on the common stated spaces. No incompatible primed determinant has entered this equality. C, H_loc and H_h still contain the actual normalized composite soft action and its local finite-depth jets; the equality does not erase BCH, intermediate-level or density-normalization terms.

For a harmonic lift, let I inject the nonroot scalar sites, with II*+JJ*=1. Positivity of Delta_int=I*Delta I follows because a covariantly constant field that vanishes at every root vanishes everywhere. Define

    L=J-I Delta_int^-1 I*Delta J,
    S=J*Delta J-J*Delta I Delta_int^-1 I*Delta J.

Direct multiplication gives ev L=1, I*Delta L=0, Delta L=JS, L*Delta L=S and L*Delta^2L=S^2. S is positive on the invertible charged stratum. The same shear with L instead of J therefore gives G_L=S^2 and

    Q_L=1-JJ*=II*,
    L_harm=H_loc+diag(D II* D*,dd*),
    det J_min=det(S)^2 det(L_harm)/det(H_h).

Scalar Schur elimination gives det Delta=det Delta_int det S. Hence

    Phi=1/2 log det L_harm-1/2 log det W
        +log det Delta-log det Delta_int-1/2 log det H_h
        +LG-1/2 log det Delta_c,

which proves A5. Delta_int is a genuine moving determinant. The harmonic lift also moves. In the independent dense family, det Delta_int(t)=5t^2-2t+11, its second log derivative at zero is 106/121, and L'(0) is nonzero. Neither can be set to its free value when taking jets. The exact multidimensional tests reject dropping Delta_int, replacing S^2 by S, and using the shear after destroying the null-column premise.

## 3. Point geometry, its failed pole route, and the periodic exception

On the unscaled four-dimensional nearest-neighbour graph, each diagonal entry of Delta is 8I and each of the eight off-diagonal entries is minus a unitary transport. The diagonal of Delta^2 is 64I+8I=72I, since each return path contributes transport times its adjoint. Delta^2 has graph range two. The stipulated root spacing ell>=3 and sufficiently long cycles exclude any two-step path between distinct roots and any short wrapping collision. This proves G_J=72I for arbitrary allowed unitary transports, not only at the free point. Scaling D by a_f^-1 scales this Gram by a_f^-4.

For periodic mean-zero coarse parameters, the inverse of G_J on its chosen domain is Pi_c/72. Thus

    Q_mean-Q_full=(Delta J 1)(Delta J 1)* /(72 N_c).

At distant distinct roots the entry is 64/(72 N_c), so global mean-zero projection destroys finite range. It is neither the charged-stratum identity nor an automatically negligible differentiated density. A small rank or entrywise inverse-volume coefficient alone proves no required infrared/volume interchange. For the periodic harmonic version the analogous identity is Q_L=1-J Pi_c J*, not 1-JJ*. Its extra root-constant term and the fine/coarse quotient Gram compatibility must still be handled. Root-fixing is a different domain and has not repaired this obligation.

At the free point the raw soft Hessian has blocks M*C^-1M, -M*C^-1, C^-1. Eliminating the massive coarse block C^-1+dd* gives

    O_J=H_W+D Q_J D*+M*d R d*M,
    R=(1+d*C d)^-1.

This follows by Woodbury with the displayed C, so no mass/gauge factor is suppressed. Exact root covariance is MD=d ev. For a=D J eta, H_W a=0 and Q_J Delta J=0, whereas M a=d eta. Therefore

    <a,O_J a>=<eta,Delta_c R Delta_c eta>,
    ||a||^2=<eta,J*Delta J eta>=8||eta||^2.

In a free scalar Bloch sector the quotient is lambda_c(K)^2/[8(1+g_n(K))], with g_n(K)=d*C d=O(|K|^2). It has order |K|^4. Positivity and Cauchy–Schwarz then force an inverse quadratic form of order at least |K|^-4 along that normalized vector. This refutes a volume-uniform simple-pole bound for O_J. Finite range of its entries does not prevent the quartic mode. The harmonic repair changes the representation and the norm; it does not retrospectively make the point-lift inference valid. Independent actual-contour samples recover the quotient coefficient approaching 1/8.

## 4. Fixed-depth Dirichlet gap and the complete-alias S

For a scalar field f vanishing at roots, transport f along a path from its block root. Unitarity and Cauchy–Schwarz bound |f(x)|^2 by the path length times the sum of squared edge differences on that path. A path has length at most 4(ell-1), and an edge is used by at most ell^4 chosen vertex paths. Summing yields

    ||f||^2 <= 4(ell-1)ell^4 ||Df||^2,
    Delta_int >= gamma_ell=1/[4(ell-1)ell^4].

This works also with noncommuting unitary transports and is volume independent at fixed ell. Since ||Delta_int||<=16, its inverse is the convergent finite-propagation Neumann series

    (1/16) sum_{r>=0} (1-Delta_int/16)^r.

Terms of degree r have range at most r, and their norms decrease geometrically. This gives exponential spatial decay with constants depending on ell. Fixed-order derivatives are products of these inverses and the local differentiated entries, yielding the stated fixed-depth local Taylor control. The constants deteriorate with ell; this is no depth-uniform hypothesis H1/H2/H3 or infrared mass-gap estimate.

At the free Bloch point, normalize the fine Fourier basis in one ell^4-site cell. Root injection has coefficient ell^-2 in each scalar alias. Scalar Schur inversion consequently gives the full expression

    S(K)^-1=J*Delta(K)^-1J
           =ell^-4 sum_{r in aliases} 1/lambda_f((K+2pi r)/ell).

The main alias contributes ell^-2/|K|^2+O(1). Every other alias remains analytic and finite near zero. Reflection symmetry removes odd terms, so inversion yields S(K)=ell^2|K|^2+O(|K|^4). No alias may be dropped from the exact formula. In an independent 3^4 cell with Bloch phases (-1,-1,1,1), direct exact Kronecker elimination gives J*Delta^-1J=93/616 and S=616/93. Counting all 81 eigenvalues independently gives the same result and determinant/cofactor identity. This point differs from the author's four-antiperiodic cell (1047/7280). Omitting the nonprincipal aliases fails.

## 5. Free Hodge determinant and the genuine all-mode estimate

For nonzero invertible free Bloch momentum, let T be an orthonormal frame for ker D*. Write

    a=Tt+D(I xi+L eta).

The scalar change (I,L) has determinant modulus one, but the one-form change does not. Its squared-volume Gram is det Delta: the orthogonal gradient blocks have Grams Delta_int and S. Omitting this one-form Gram is a determinant error even though the scalar change is triangular.

Using H_W D=0 at the free point, I*Delta L=0, MD I=0 and MD L=d, the full harmonic energy is exactly

    t*H_T t+||Delta_int xi||^2
       +(d*M Tt+Delta_c eta)* R (d*M Tt+Delta_c eta).

The eta shift that removes d*M Tt has determinant one. It is used only for this finite determinant; its Delta_c^-1 is not advertised as a local field change. Dividing the resulting coordinate determinant by the one-form Gram gives

    det O_harm=det H_T (det Delta_int)^2 (det Delta_c)^2 det R / det Delta.

The eliminated coarse block contributes det(C^-1+dd*)=1/[det C det R]. Thus

    det L_harm=det H_T (det Delta_int)^2 (det Delta_c)^2
               / [det Delta det C],

which is A6. Also det W=det H_T det Delta and H_h=G_c at the free point. Substitution into A5 cancels every factor, giving Phi(1,0)=0. This is free normalization, not vanishing of the off-shell Hessian or of an interacting residue. In particular, H_W D=0 cannot be differentiated as an off-shell identity without its equation-of-motion correction.

For the all-mode estimate, write the energy above as E. At fixed ell and small nonzero K, the free transverse Wilson block bounds ||t||^2 by C_ell |K|^-2 E. The Dirichlet gap bounds ||D I xi||^2 by C_ell E. The complete-alias estimate S(K)<=C_ell |K|^2 gives

    ||D L eta||^2 <= C_ell |K|^2 |eta|^2
                  <= C_ell |K|^-2 |Delta_c eta|^2.

Set z=d*M a=d*M Tt+Delta_c eta. Positivity of R with fixed-depth constants bounds |z|^2 by C E. Boundedness of the actual fixed-depth M and d=O(K) gives |d*M Tt|<=C|K| ||t||. Hence the last display is bounded by C|K|^-2 E+C||t||^2, and therefore by C|K|^-2 E. The three one-form components are orthogonal. This proves the full quadratic-form estimate

    O_harm(K) >= c_{n,kappa}|K|^2 I.

This is genuinely an all-mode statement; the harmonic special-vector quotient alone would not prove it. At K=0, zero curl leaves a gradient plus four constant one-forms. The interior constraint forces Delta phi to be supported at the one root; its total sum is zero, so it vanishes. The gradient is then zero. Exactly four constant one-forms per scalar colour remain, and the finite high-alias block is positive. The charged finite regulator excludes K=0; here K=0 is the analytic free-symbol endpoint used to identify the limiting kernel, not an allowed finite logarithm at a singular matrix.

## 6. Actual free principal coefficient A7

In the normalized low-alias frame E(K), a constant field at K=0 has value ell^-2 v per fine link. Every contour has net displacement ell e_mu; its two root paths cancel on a constant field. Thus the actual contour average, and its fixed-depth composite, give M(0)E(0)=ell^-1 I_4. This is also obtained directly from the actual S4-prime path definition in PROOF 953–958. Linearizing either the normalized soft center or the stated contour average at the identity yields this same average of oriented path integrals. Their higher nonlinear vertices have not been equated by this observation.

Use the analytic full fine Fourier frame and eliminate all high aliases by its Schur complement. The high block is positive at zero, while the low/high coupling vanishes there, so the high minimizer is analytic and O(|K|v). Wilson is exactly alias diagonal. The low Wilson energy has principal part ell^-2 v*(|K|^2 I-KK*)v. For any such high minimizer, d*M a_high=O(|K|^2|v|), while the low part gives the longitudinal principal energy ell^-2|K*v|^2. Nonnegative high Wilson and interior terms give the corresponding lower principal bound.

For a matching upper bound, choose a high-alias pure gradient D phi_H solving

    I*Delta(K) phi_H=-I*D*E(K)v.

At zero, this square map from the nonconstant scalar aliases to interior values is injective: if its image is zero, Delta phi_H is root-supported; the sum of a periodic Laplacian is zero, so the root value also vanishes; then phi_H is constant and, being a high alias, is zero. The inverse is analytic near zero. The right side is O(Kv), so phi_H and D phi_H are O(Kv). This trial field cancels the interior term exactly and has zero high Wilson energy. It supplies the matching upper principal coefficient. Therefore

    O_low(K)=ell^-2 |K|^2 I_4+O(|K|^3).

The field conversion v=ell w yields the stated coefficient in coarse link units, provided the same D/action conventions are retained. No background-derivative or physical mass-gap conclusion follows.

The independent implementation enumerates all 24 coordinate orders, all 81 starting sites and every oriented edge of each actual L=3 contour. The fine curl is built separately from plaquette edges. It verifies MD=d ev, the constant map, and the full high-alias Schur complement. At kappa=3/2, for the prescribed axis and mixed rays and t=.04,.02,.01, the principal errors at the last point are 1.94e-5 and 2.04e-5; the smallest full eigenvalue divided by t^2 is approximately 0.111111. Dropping high-alias minimization leaves a principal error about 0.10973. Analytically, the omitted interior correction adds ell^-2(1-ell^-4)|K*v|^2; for ell=3 the wrong longitudinal coefficient is 161/729 rather than 1/9. Thus the independent negative control detects exactly the potentially misleading shortcut.

## 7. Evidence, preserved diagnostics and remaining obligations

- [Independent actual-contour implementation](checks/review_residual_bridge_01.py), [complete stdout](checks/review_residual_bridge_01_out.json), [unaltered stderr](checks/review_residual_bridge_01_err.txt): **45/45 predicates**. Numerical samples control signs, aliases, units and the implementation, and do not replace the all-mode/A7 proofs.
- [Independent exact implementation](checks/review_residual_bridge_02.py), [complete stdout](checks/review_residual_bridge_02_out.json), [stderr](checks/review_residual_bridge_02_err.txt): **48/48 predicates**, empty stderr. It checks mixed-twist root Green data, every scalar/Hodge factor and a moving dense family with four fine gauge coordinates and two coarse gauge coordinates. Noncommutation is explicitly tested. These dense matrices verify finite algebra, not actual off-shell S4-prime vertices.
- [Independent numerical diagnostic](checks/review_residual_bridge_03.py), [complete stdout](checks/review_residual_bridge_03_out.json), [stderr](checks/review_residual_bridge_03_err.txt): **6/6 predicates**, empty stderr. The first run's NumPy `slogdet` issued divide/overflow/invalid warnings despite finite consistent results. An independently rebuilt Kronecker Laplacian is positive definite, and Cholesky logs reproduce both determinant values to the declared tolerance. Isolated `slogdet` repeats the warnings; these are captured in the diagnostic JSON. The original warnings are retained and their backend cause is not claimed resolved. No mathematical predicate was hidden or rerun until it passed.

Every pre-stated wrong-formula control rejects: omit conjugate multiplicity, high-alias minimization, nonprincipal aliases, Delta_int, one S power, the one-form Gram, or the null-column premise. The point-lift quartic route remains recorded as a failed analytic route rather than deleted. The independent exact mixed-twist and noncommuting tests are not the author's tests relabeled.

The smallest legitimate conclusion is the table above. No source correction is requested. A stronger conclusion would require new proofs: actual first/second background and residual vertices with all BCH/normalization and moving-frame terms; the applicable off-family gradient identities; grouped separate-pole bounds/continuity; preservation of the Ward/covariant-regulator hypotheses in the actual lattice matching; periodic neutral quotient and full-colour treatment; and the specified thermodynamic, external-momentum and depth limits. The fixed-depth Dirichlet gap and free |K|^2 coefficient do not supply an interacting physical spectral gap or the existence/OS theorem. The separate MASS_GAP_TARGET unit has not been used to justify any claim here.
