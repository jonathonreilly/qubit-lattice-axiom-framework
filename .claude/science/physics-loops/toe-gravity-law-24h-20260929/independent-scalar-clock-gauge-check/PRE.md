# Independent reconstruction before new proof exposure

I have read only the new CONTRACT and the complete provisional PR9398 canonical note at6515ffa8. I authored that parent milestone; this is not an independent re-review of it. Prior exposure is the root's scalar-time-gauge brief and the contract's displayed candidate, not the new proof, energy refinement, implementation or results. This PRE is frozen before opening those files. The current framework grants and selected7146 procedure boundary are reused only with the immediately preceding exact-main byte checks. No native result enters this argument.

Write S=sqrt(det g), t_g=tr(g pi), s=aK and let C_g be the actual continuum density, with its literal spectral/centered versions on the full six-pair finite carrier. Let w0(x)>0 be a supplied, time-independent scalar density. Set phi=t and N=S/w0. This is an internal coordinate gauge of the supplied continuous scalar comparator; it is not a framework Record clock or a derivation of the carrier.

## Canonical gradient and gauge restriction

The full scalar equations at spatially constant phi are phi_dot=Nw/S and w_dot=0. Thus w=w0 and this N preserve phi=t. The candidate is

    Hbar=mean[(S C_g)/w0+w0/2].

Its metric velocity is the fixed-lapse C_g velocity. Its momentum velocity contains the additional term -C_g N_g. Comparing to the fixed-lapse FULL scalar constraint gives

    p_dot_bar-p_dot_fixed_total=-chi N_g,
    chi=C_g+w0^2/(2S),   N_g[E]=(N/2)tr(g^-1 E).

Here independent off-diagonal coordinates vary both symmetric entries; tensor pi uses p_ij/2. On chi=0 the full scalar stress is exactly recovered. The extra term cannot be dropped off the surface.

Put W=sqrt(-2S C_g) on a real neighborhood where the radicand is positive. Direct functional differentiation, before integrations by parts, gives

    delta Hbar-delta Hred
       =mean[(1/w0-1/W)delta(S C_g)],
    Hred=-mean W.

Therefore all canonical gradients agree on the IDENTICALLY constrained field chi=0, since W=w0 as a function of x. Off the surface the coefficient difference is not in general a scalar factor multiplying an already integrated gradient: derivatives of it enter. Hbar=0 on that surface while Hred=-mean w0; equality of their values is neither needed nor asserted.

## Continuum constraint propagation derived independently

Use the parent's fixed-smearing brackets and retain the field dependence of N. The full scalar momentum contribution is zero at phi=t; its bracket contribution to the integrated generator is also zero because phi_dot=1 and the torus integral of div(w0 X) vanishes. For J_i=pi^jk partial_i g_jk-2partial_j(g_ik pi^jk), the reduced generator computation gives

    J_dot_i=partial_i(N chi)-N chi partial_i log w0.

A second way to obtain this is to note that F=S C_g is a density of weight two, while w0 is held fixed in the reduced Poisson calculation. Then {G[X],Hbar}=mean X^i w0 partial_i(F/w0^2); adding1/2 inside that derivative gives the displayed formula. Holding w0 fixed dynamically must not be confused with giving it scalar transformation weight under coordinate changes.

The fixed-smearing CC bracket and {C[f],N}=a N f t_g/(2S) give

    chi_dot=s g^ij J_i partial_j N
             +s partial_j(N g^ij J_i)+a N t_g chi/(2S),
    N_dot=-a N^2 t_g/(2S).

Thus the rescaled constraints

    u=N chi/w0=S chi/w0^2,   v_i=J_i/w0

obey the exact linear homogeneous system along the nonlinear metric solution

    u_dot=(s/w0)partial_j(N^2 w0 g^ij v_i),
    v_dot_i=partial_i u.

The positive energy

    E_c=(1/2)mean[w0 u^2+s w0 N^2 g^ij v_i v_j]

has derivative (s/2)mean[w0 partial_t(N^2 g^ij)v_i v_j]. The cross terms cancel by integration by parts, with no assumption that w0 is spatially constant. Smooth positive g,N and fixed positive w0 therefore give E_c'<=C(t)E_c. Initially zero constraints remain zero. This is a continuum statement; it does not manufacture a finite product rule or exact finite constraint ideal. The derivation will be checked against all signs and density conventions in the candidate.

## Literal finite augmentation

Define omega=1/w0 and Z^ij=N S g^ij=omega det(g)g^ij. The finite Hamiltonian is

    mean[a omega(tr(g pi g pi)-t_g^2/2)-K Z^ij R_ij+w0/2].

Set q_l,A=D_l g_A and r_l,ij=D_l Z^ij. Skew summation by parts rewrites curvature as the same local quadratic Christoffel expression as the parent, with B replaced by Z. With T=a omega(tr(g pi g pi)-t_g^2/2) and that potential V,

    g_dot=T_p,
    p_dot=-T_g-V_g+sum_l D_l V_q_l
                         +sum_(l,ij) Z^ij_g D_l V_r_l,ij,
    q_dot=D g_dot,
    r_dot=D(Z_g g_dot).

The coefficient Z_g belongs OUTSIDE D in the momentum equation. No spatial identity DZ=Z_g Dg may be used on either finite grid; omega also varies with x. Ordinary time differentiation preserves q=Dg,r=DZ exactly because omega_dot=0.

Treat omega as an extra frozen component in the analytic first-order system. Local maps are analytic near g=I; Z is even polynomial in g times omega, while Gamma still contains g^-1. Every vector-field component contains at most one D of a local map. The parent Wiener product/Cauchy estimates, shrinking-radius bootstrap and ordered Volterra argument should apply with new finite majorants depending on omega's analytic norm. A lower derivative-symbol bound is unnecessary. The actual all-alias spectral and centered sampling commutators remain the parent's ones. Comparison of the literal scalar and momentum densities needs another radius reserve.

Necessary hypotheses must include a strip on which omega is analytic with finite Wiener norm. Real positivity of a given analytic w0 implies this after possibly reducing the strip, not automatically at an arbitrarily preassigned radius. An explicit near-constant example can supply a quantitative inverse bound. Common time depends on this input and cannot be inferred from a tiny gradient diagnostic.

## Nonconstant compatible input

An explicit candidate is g0=I, pi0=lambda I+T(x), with T symmetric, traceless and divergence free, phi0=0. Then J0=0 and

    w0=sqrt(3a lambda^2-2a tr(T^2))

solves the scalar constraint wherever it is positive. For T=diag(0,f(x1),-f(x1)), f=eta cos x1, this becomes w0=sqrt(a)*sqrt(3lambda^2-4eta^2 cos^2 x1). Nonzero lambda and sufficiently small nonzero eta give a nonconstant positive analytic density, with a binomial-series inverse on a quantitative strip. All six metric/momentum coordinates remain part of the subsequent evolution. These sampled data also have zero initial literal finite constraints for both derivatives: g is constant and the divergence of T differentiates only its transverse directions. No claim of later exact finite propagation follows.

## Remaining comparison obligations

The algebra above makes the target plausible, not accepted. Check the candidate's exact variation, tensor multiplicities and signs; its fixed-density convention; the full off-constraint propagation; positivity/regularity for energy or analytic uniqueness; the finite r=DZ identity with nonconstant omega; actual full-mode consistency constants; initialization, domain and radius reserves; and the exact stated quantifiers. Read every new proof/refinement and control after this freeze. A full-gradient finite check can support the variation but cannot establish a PDE, a gauge-selected physical time, or exact finite closure. No computation is presently needed for this reconstruction.
