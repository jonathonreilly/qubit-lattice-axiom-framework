# Energy-resolved onsite perturbations with all physical heads retained

New ROOT author derivation, requiring a distinct check. This refines the uniform-in-energy finite-matching onsite interface bba11422. It is a conditional sufficient complete-certificate estimate, not a necessary onsite-precision theorem or native protection mechanism. No numerical operating point is evaluated.

## 1. Fixed nominal model and additional finite gate

Fix an admissible nominal mediated Q apparatus, or its exactly equivalent centered positive-P implementation, at the supplied mass-tuned microscopic tuple. Preserve the original capped background, shared B, old K/W, two physical windows, original product seed V, scalar packet, physical masses and actual scalar phase. Only add scalar occupation errors D_N on the finite set N of all10m-1 added heads, with ||D_N||<=xi. The background and receiver are unchanged; the actual preparation still lies on source0. Native occupation/block supply remains a premise.

Reuse the exact loaded/source/regularity/recovery premises and constants of5f909e1e,83530c67,9e4dffc5 and the newly checked residual f66b5636/check4f6784ef. In particular on each lip/window the PHYSICAL three-source inverse has full forcing-domain row bounds

 ||P S^-1||<=a_P/R, ||C S^-1||<=a_C/R+B_c,
 ||S^-1||<=u=A/R+B_c,
 R=sqrt(delta^2+lambda^2),
 a_P=f(1+x), a_C=fx(1+x), A=f(1+x)^2,
 f=6/[s(1-zeta)], x=b_mix/k_C, B_c=1/k_C.

The source P/C projections are constant within each window. These bounds are restored through the same physical mass congruence, not through an actually retuned one. They apply to arbitrary source forcing, not merely a prepared column.

Let r_*=min(a-rho,b)>0, where b=.185-(J_m+q), and let G_b=1/j+a0+b0*rho bound the full physical port kernel. Introduce the additional sufficient gate

 omega=gamma3^2*G_b/r_*<1,
 r_L=1/[r_*(1-omega)],
 c=sqrt(2)*gamma_*, h=1+c*r_L.                         (1)

This gate is explicit and must be checked; it is not silently deduced from the other inverse margins. The letter r_L here denotes an internal loaded-resolvent norm ceiling, not a reflection amplitude or packet normalization. All constants below are uniform over the two physical windows, lips and conserved sectors.

## 2. Reconstruct the entire new-head inverse

Split N into the three source endpoints and the disjoint union of internal mediator chains. Let C_s=Gamma E_s map source endpoints into internal chain endpoints, with ||C_s||<=c. The incidence E_s(s0,s1,s2)=((s0,s1),(s1,s2),(s2,0)) has norm sqrt(2). In this section C_s is a coupling operator, not the earlier scalar source-decay coefficient.

Let R_int=direct_sum_l(D+A_l)^-1 be the unloaded internal resolvent. Its full-fiber norm is at most1/r_*. Let J_R inject the old-port fiber into the rightmost internal head of cell3. Eliminating only the unchanged infinite background loads the internal block by gamma3^2 J_R G J_R*. Thus

 L=(R_int^-1-gamma3^2 J_R G J_R*)^-1,
 ||L||<=r_L.                                           (2)

The Neumann bound(1) proves(2) on each lip. No Hermitian or normal inverse is assumed on a continuum boundary. Eliminating this internal block produces exactly the same physical three-source Schur S as the checked elimination in the other order. This is finite block Gaussian elimination with invertible internal/port blocks, not a new effective Hamiltonian approximation.

The full outgoing new-region inverse is

 K_N=[[S^-1, -S^-1 C_s* L],
      [-L C_s S^-1, L+L C_s S^-1 C_s* L]].             (3)

Here C_s* is the fixed physical adjoint of the real coupling injection; L is NOT replaced by its adjoint on one lip. Factor the resonant term as [I;-L C_s] S^-1 [I,-C_s* L], plus diag(0,L). Triangle gives

 ||K_N||<=h^2*u+r_L=A_N/R+B_N,
 A_N=h^2*A, B_N=h^2*B_c+r_L.                          (4)

For the physical seed, which has no internal-chain input component,

 ||K_N V||<=h*u.                                      (5)

Thus no artificial r_L direct forcing is added to the prepared column. Formula(4) remains a full inverse bound needed for perturbations on ANY new head, including mediator interiors.

## 3. Preserve the small resonant factor in the physical port row

The physical background forcing for arbitrary new-region input is Z_N=-gamma3 J_R* K_N, with J_R* here acting on the internal part of(3). By the exact block identity,

 Z_N=gamma3 J_R* L C_s S^-1 [I,-C_s* L]
                                  -gamma3 J_R* L [0,I].     (6)

Only the last cell couples directly to J_R. The loaded internal resolvent identity yields

 gamma3 J_R* L C_s=K_p t3(D) J2,
 K_p=(I-s_3R(D)G)^-1.                                (7)

Indeed the right-end compression of the identity L=R_int+R_int gamma3^2 J_R G J_R* L gives the left factor (I-s_3R G)^-1; the unloaded right-to-left endpoint product is t3=gamma3^2 C_R*R_3 C_L in the fixed physical sign convention. J2 selects source2. Other internal paths do not couple directly to J_R. This retains exact noncommuting order and agrees with the checked physical forcing z=K_p t3 J2 U. A fixed sign gauge conjugates these identities consistently without altering any norm.

Let k=1/(1-eta), selected physical hopping t_P=sqrt(Z2)*kappa*(1+theta3), and complementary hopping ceiling tau=gamma3^2/b. Define the existing full-row forcing coefficients

 D_w=t_P*a_P+tau*a_C, e_w=tau*B_c.

Since t3 preserves P/C before multiplication by K_p,

 ||t3 J2 S^-1||<=D_w/R+e_w.

Use (6)--(7), ||[I,-C_s*L]||<=h and ||J_R*L||<=r_L to obtain the FULL port row bound

 ||Z_N||<=A_z/R+B_z,
 A_z=k*h*D_w, B_z=k*h*e_w+gamma3*r_L.                  (8)

The direct internal-forcing term gamma3*r_L is essential; it represents perturbations injected within a mediator. This estimate does not replace the entire row by its prepared-source column. Conversely replacing t_P by the full complementary tau would unnecessarily remove its resonance scaling. Physical sqrt(Z2) and the direct complementary e_w remain.

## 4. Exact onsite subtraction and energy-resolved expressions

The finite new-region pencil changes from K_N^-1 to K_N^-1-D_N. Require the uniform sufficient gate

 theta=xi*(A_N/lambda+B_N)<1.                          (9)

Then the full perturbed inverse K_d exists on the windows, and

 K_d-K_N=K_N D_N K_d,
 ||K_d V||<=h*u/(1-theta).

This second bound uses (I-K_N D_N)^-1 K_N V, preserving the actual prepared-column factor in(5). Define

 e_N(delta)=xi*h/(1-theta)*(A_N/R+B_N)*(A/R+B_c),
 e_z(delta)=xi*h/(1-theta)*(A_z/R+B_z)*(A/R+B_c).        (10)

They bound the actual prepared new-head and port-forcing differences, respectively. The second uses the NOMINAL full row Z_N in the ordered identity -gamma3 J_R*(K_d-K_N)=Z_N D_N K_d. It does not require a small perturbed physical row or discard direct internal forcing. D_N can affect every new source and mediator head, not just source0, and need not commute with the inverse.

With J_Rint=2asinh(rho/lambda) and J_R2=2atan(rho/lambda)/lambda, define for any nonnegative pair(p,q)

 I(p,q)=p*A*J_R2+(p*B_c+q*A)*J_Rint+2rho*q*B_c,
 L2(p,q)=p*A*sqrt(pi/(2lambda^3))
       +(p*B_c+q*A)*sqrt(pi/lambda)+q*B_c*sqrt(2rho).

These are exact integrals of the positive product envelope or safe L2 triangle ceilings using the convergent rational moments; no derivative of an envelope is invoked. Set alpha=xi*h/(1-theta). The full retained-evolution discrepancy obeys

 B_d,ER=(2/pi)*alpha*[I(A_N,B_N)+14000*I(A_z,B_z)]
           +4*461*sqrt(j/pi)*alpha*L2(A_z,B_z).        (11)

The local term includes ALL new heads plus the unchanged full finite/closed background; two lips and two windows give2/pi. The ray term covers two windows and both incoming/outgoing coefficients with exact physical j/pi flux conversion. Fixed real matching identifies incoming at the same positive physical time. Halfline restrictions are contractions, not omitted outputs. Every bound extends to arbitrary passive references.

As in the checked onsite interface, the analytic background matching and strict gate(9) supply local continuation of the actual finite inverse. This is required to identify the represented evolution with the Stone synthesis. Outside singular mass is not assumed absent.

## 5. Actual outside allowance and complete scope

Use the SAME original first-cell normalized trial X. Its residual after onsite perturbation grows by at most xi since ||D_N X||<=xi. Therefore use the actual o_d in onsite bba11422 equation(3). The complete bound is

 ||exp(-itH_P(w,d))V-exp(-itC(w))T0(t)||
                           <=o_d+B_d,ER+b0(t),         (12)

when the fixed w is nominal and b0 is its explicit retained-to-target allowance. For an already separately certified bond-perturbed w, its retained bond allowance can also be added, but then all constants(1)--(11) require corresponding valid full-row/source bounds for that tuple; nominal critical bounds must not be silently reused. No joint numerical box is claimed here.

The actual outside vector is paid once. For nominal w, relative to its original witness ceiling, o_d increases by at most sqrt(2)*xi/rho; the min with1 cannot increase that increment. Thus the new interface is a perturbation of the existing complete OUTPUT CERTIFICATE. It does not bound the difference of full unitary evolutions on all outside eigenvectors. The fixed nominal packet, raw mass, global phase, old aging, record and all blank outputs remain. No time, cut or receiver has been selected here.

## 6. Conditional linewidth scaling

Fix microscopic suppliers and background with the additional gate omega and all inherited inverse/gap margins uniformly bounded away from closure. Take eventual rho=sqrt(a lambda) in the checked geometric family, and restrict xi/lambda so theta stays uniformly below1. Then r_L,h,A_N,B_N,A,B_c,k are bounded. From the checked row structure, a_C=O(sqrt(lambda)*(a0+b0rho)), t_P=O(sqrt(lambda)), and hence

 A_z=O(sqrt(lambda)), B_z=O(1).

The local new-head integral in(11) is O(xi/lambda)+O(xi log(1/lambda)). The background local integral is O(xi/sqrt(lambda))+O(xi log(1/lambda)). In the ray term A_z*lambda^(-3/2)=O(lambda^-1), while B_z*lambda^-1/2 is smaller. Thus

 B_d,ER=O(xi/lambda),
 o_d-o_nominal <=sqrt(2)*xi/rho=O(xi/sqrt(lambda)).

The complete sufficient certificate increment is therefore O(xi/lambda) on the nominal valid time domain. This is a sufficient law with supplier-dependent constants and explicit gates, not a universal necessary precision or proof of an output failure at larger xi. The old uniform-in-energy bound has an avoidable inverse-linewidth loss; integrating the actual pole structure removes that loss but does not derive symmetry protection. No fixed nonzero xi at unbounded length, varying g limit or arbitrary old-background error is covered.

## Sources, exposure and remaining checks

ROOT authored this new argument after independently checking the onsite interface bba11422 and residual row reconstruction f66b5636. The use of a full internal loaded inverse and its arbitrary-input port row is new author work; the earlier checks are not a check of this proposal. A distinct reviewer should especially reconstruct(3),(6)--(8), the prepared Dyson subtraction and physical integration factors. No numerical scientific program or parameter selection was performed.

Exact primary sources: onsite bba11422e5b425fa003ba4ba4890e2cdf70b717389d4b6ada4136ee19154dc50/check972406c9ba8c40658ba3465f09a3110b270938a7b7df229472c1e5b2c18211c7; residual f66b5636cca5cc6ef8e71b40746beb97b831527028738a6ccef7f17bca2b28ea/check4f6784efb2f68f36b5598ac764cc3ae33ee7785048ad440acf16016305cadc5c. Unchanged full source/loaded/recovery/regularity premises retain the exact ten identities in f66b's table and the full finite-Schur adapter594461/check462c76, already read completely within this coherent task.

Native centered-chiral/common-carrier constraints, occupation and block supply, actual phase knowledge, initialization and physical Record identification remain separate premises. No autonomous capture, finite permanent halt, reset/reuse, repeated monitoring, retained audit or broad impossibility is established. Only this proposal was written; no W/Git/PR/checkpoint/model or editable prompt changed.
