# Original-source atoms and an exact level-zero return

## Contract recorded 2026-10-29 11:51 UTC

Status: open author construction; independent mathematical review pending.
Claim type: bounded theorem / direct support for the one-step obligation.
No audit status is asserted. The full non-free SU(N) theory on R4 satisfying
OS0–OS3 remains the parent target, not a consequence of a finite-volume check.

The coordinator supplied science baseline
`962f97c259d8c241df632a07e27f498f4ad33b09` and freshly fetched methodology
revision `6c269770273c3fe00de350d5a3c14cacb70c2833`. Methodology was read by
read-only `git show` at that exact revision; the installed physics-loop entry
point was inspected first and its current-main version supersedes it. This
worker makes no git mutations or edits to original sources/shared summaries.
All new files are this note and `checks/source_return_*`.

**Target and domain.** Construct connected-support atoms, with row, column,
and support-incidence majorants, for the identified level-zero operator in
PROOF's Setting N5-bg with local Wilson coefficient perturbations. Work on
finite four-dimensional tori and explicitly specified Dirichlet regions,
with fixed N, L, stiffness interval, and finite coarse R-boxes. Every atom
must read only its labelled original variables. Then derive the raw Haar
return identity, including its actual region/collar/history indicator and
reference normalization, before seeking a small-interaction specialization.
The source substitution U=b(V,epsilon) is a separate construction: treating
U as independent is not that bridge. E_cb is never identified with E_NA by
notation.

**Decisive criteria, before new checks.** (1) Direct inversion versus the
parametrix must agree in exact rational finite examples; the n-step remainder
must satisfy a proved norm bound. (2) A source at a local matrix entry must
remain in every atom that reads it, including compression inverses and their
collars. (3) A marked-atom argument must bound incidence, not merely endpoints.
(4) A determinant check by permutation expansion must match the independent
inverse/trace derivative and detect an omitted determinant. (5) A finite
nonabelian gauge check must preserve all plaquette traces and the normalized
kernel's contour transports under the stated tree gauge. (6) A retained
history indicator may not be set to one without proving its constancy on the
entire transformed support. These are author checks, not independent review.

**Prior exposure and novelty.** The known CX/source-locality and normalization
counterexamples in CODEX_REVIEW_STEP R9–R11 and CODEX_REVIEW_SRC2 F1/F2/F7 were
read before this declaration; reproducing them is not a new result. Complete
RECOVERY_CLUSTER_ASTRA was read. Necessary source arguments read include
STEP55 5.1–5.4/S8/S9, PROOF's Setting N5-bg/N5-an/CT/RW/N5-sf0/N5-sf_i and
NA-FP, SRC2 MB/E11, and B2's consumer caveat. A current-main statement search
for incidence+parametrix, original-coefficient+resolvent/parametrix, and
maximal-tree-gauge+denominator had no matching result; the matching lane
sources are RW (missing the weighted incidence construction) and the generic
CX-R proposal (missing its actual producer). This does not assert literature
novelty or complete repository coverage.

**Approach families.** A: retain the entire local compression collar in the
RW expansion; prove incidence by marking an atom. B: exact block maximal-tree
gauge followed by Lie coordinates, to avoid importing a nonlinear identity
from NA-FP's Gaussian-only statement. C: all-order connected-source implicit
construction for the background, if needed for a nontrivial source-dependent
center. Exponential matrix-entry decay or fixed-order derivative estimates
alone will not be promoted to C. No route-exhaustion or no-go is claimed.

## 1. Source-local level-zero parametrix (construction in progress)

The original independent variables in this section are the fine links U,
coarse links V, and relative Wilson coefficient field epsilon_p. U is **not**
the solved background b(V,epsilon) here. Every statement is uniform only on
the explicit local complex domain below. The fluctuation indices are fine
oriented links, each with the Hilbert–Schmidt su(N) block norm; support vertices
are R-boxes in a fixed product partition of the level-one block torus. Thus
one support vertex contains O((RL)^4) fine coordinates. All R-dependence is
retained in the constants. R is selected once for this one-step theorem; no
scale/history-uniform identification at higher levels is implied.

### 1.1 The operator and its complex domain

Put sigma^2=N/u, with u>0 real and t=κu. The kernels remain fixed when
epsilon varies. Write

    S_W,epsilon(U)=Σ_p(1+epsilon_p) Re tr(1-U_p),
    S_eff(U;V,epsilon)=(u/N)[S_W,epsilon(U)+κΣ_c φhat_c(V;Mbar_c(U))]
                         +Σ_c log Ntilde_t(Mbar_c(U)).                 (1)

At complex arguments, Re tr means its holomorphic continuation
tr(2I-U_p-U_p^{-1})/2, not complex conjugation. The centered normalization
Ntilde and φhat=Nψ are exactly STEP55's quantities. This is the conditional
action of the normalized soft kernel with its fine-field-dependent
normalizer included. No background minimization occurs in (1).

The identified full-space, gauge-fixed **Hessian operator** is

    K_epsilon=Π_U[Hess_A(S_W,epsilon+κΣφhat)|_0
                  +sigma^2 Hess_A Σ log Ntilde_t|_0
                  +D_U P_res^U D_U^T]Π_U+(I-Π_U).                    (2)

Without the sigma^2 term and at epsilon=0, this is exactly Setting N5-bg's
Õ. The sigma^2 term is the exact-normalizer correction from STEP55 NZ-R.
Equation (2) does not assert that the nonlinear Haar integral equals a
Gaussian integral in the NA-FP slice; NA-FP explicitly proves only a
Gaussian identity at a critical point. Section 3 uses an exact tree gauge
instead and identifies its different Hessian explicitly.

For the present construction choose a fixed entry radius α strictly inside
both the N5-an and NZ complex domains. On each compression collar require
a **real** gauge in which |log U|, |log V|<α; original variables are always
the ungauged links. Let |epsilon_p|<rho. Set

    P= sup N_0(|Π_U|),
    B_epsilon=24 exp(4α) P^2,
    delta=C_Delta α+B_epsilon rho+sigma^2 P^2 C_N.

Here C_Delta is N5-an's local bound and C_N is STEP55 NZ-R's corrected
row bound, including its su(N) dimension factor (S7). These constants exist
on a strictly smaller local polydisc. The Wilson factor 24 follows directly:
six plaquettes meet a fine link in d=4 and each Hessian row of one plaquette
has at most four insertion terms, each bounded by exp(4α). Multiplication
by the block-local Π costs P^2. The normalizer uses the same contour stencil.
No complex-coupling normalizer theorem is used: u and t stay real.

Take a proven flat-operator gap γ_0>0 from N5-coer, and choose α,rho,u^{-1}
so delta<γ_0/2. Choose m>0 sufficiently small that

    D_m(|Õ_0|)+(exp(m r_1)-1)delta ≤ (γ_0-delta)/2,  γ=γ_0-delta>0.    (3)

Use a common finite range r_1 enclosing (2)'s stencil, increasing the N5-bg
value if needed. Every entry of (2) reads only a fixed collar of at most
r_dep level-one blocks from its row block; one may take a conservative
r_dep=3. These claims follow by finite composition of the same local
functions in N5-an and the single-normalizer function. The coefficient
field is local at the Wilson plaquette where it is inserted. The constants
are uniform in volume. They are existence constants here, not numerical
estimates advertised as sharp.

In the local real gauge, a compression of (2) differs by at most delta from
the corresponding compression of Õ_0. Thus CT proves, on this **actual
operator**, for all a≥0,

    |(K_Omega+a)^{-1}(x,y)| ≤ 2 exp(-m d(x,y))/(γ+a),
    N_m(|K|) ≤ S_m < infinity.                                    (4)

Both are uniform for the selected domain and any compression I whose
coefficient-read collar has these local gauges. A global FILL satisfying
this domain is sufficient for a region with holes. Arbitrary twisted
collars have not been shown to satisfy it. This is a precise inherited
premise, not a hole-uniform conclusion without a domain. A gauge is used
only to prove (4); it never enters the definition of an atom.

### 1.2 The atoms and all three majorants

Fix R≥max(4,r_dep+1). Use the product R-box partition of RW. For a box q,
Omega_q is its R-block neighborhood, intersected with the integrated index
set I. Let D_q be the set of ambient R-boxes meeting the (R+r_dep+1)-block
neighborhood of q. D_q is connected and includes the full entry-read
collar, the rows and columns of each atom below. It may include fixed
collar/hole vertices; these are not integrated coordinates. On this product
partition, crude common geometric bounds are

    |D_q|≤s=9^4,  #{q:v in D_q}≤J=9^4,
    #{fine oriented links based in q}≤n_R=4(2RL)^4.                (5)

For example, in one direction D_q lies in an interval of length <6R when
r_dep≤3 and R≥4; a bound of nine intersecting intervals, each of length
at least R, is more than sufficient. The reverse incidence count has the
same bound. Periodic identifications reduce the count. The argument also
applies after deleting any integrated links while keeping the original
ambient partition/support graph.

For a≥0 define exactly RW's

    P_q(a)=(K_Omega_q+a)^{-1}1_q,
    R_q(a)=-1_{Omega_q^c} K (K_Omega_q+a)^{-1}1_q.                (6)

All matrices are restricted to I; complements in (6) are relative to I.
They are holomorphic functions of the original (U,V,epsilon) restricted
to D_q. This follows from the entries actually inverted, not from decay.
Finite range places the rows of R_q in the one-stencil outer boundary of
Omega_q, hence inside D_q. Give each atom the entire connected label D_q.

Let Q_m=4 coth^4(m/2), an upper bound for Σ_y exp(-m d(x,y)) over fine
oriented links on every four-torus (and its subsets). From (4), entrywise,

    Σ_q |P_q(a)|(x,y) ≤ 2 exp(-m d(x,y))/(γ+a),
    Σ_q |R_q(a)|(x,y) ≤ [2S_m/(γ+a)] exp(-m d(x,y))1_{d(x,y)>RL}.

The second bound follows by summing the intermediate index, using
d(x,y)≤d(x,z)+d(z,y), and the finite-range collar. Crucially the right sides
are symmetric in x,y. Consequently these inequalities give **both** row
and column sums, even though P_q and R_q themselves need not be symmetric.
Define

    a_0(a)=2Q_m/(γ+a),
    e_R(a)=8S_m coth^4(m/4) exp(-mRL/2)/(γ+a).

For β≥0 put w=exp(βs), p(a)=w a_0(a), r(a)=w e_R(a), r=r(0).
Increasing R makes r<1/2 for every fixed β; s is independent of R because
the supports are measured in **R-box units**, not fine-site units. This is
the point at which the fine-coordinate count n_R must remain visible.
For a family of matrix atoms A define

    M(A)=max(sup_x Σ_{y,S}e^{β|S|}|A_xy;S|,
             sup_y Σ_{x,S}e^{β|S|}|A_xy;S|),
    B(A)=sup_v Σ_{x,y,S containing v}e^{β|S|}|A_xy;S|.           (7)

The atom families in (6) obey

    M(P)≤p(a),    B(P)≤Jn_R p(a),
    M(R)≤r(a),    B(R)≤Jn_R r(a).                              (8)

To prove the incidence bounds, at most J labels D_q contain a specified
v. Each such atom has at most n_R nonzero **columns** (those in q), each
bounded in column sum by a_0(a) or e_R(a). This explicitly sums both
endpoints; no endpoint-local bound is substituted for incidence.

Products use unions of supports. A nonzero product P_q0 R_q1 ... R_qn
has intersecting consecutive labels at each summed intermediate link,
so its union is connected and includes every original parameter read.
The elementary marked-product inequalities are

    M(AB)≤M(A)M(B),
    B(AB)≤B(A)M(B)+M(A)B(B).                                  (9)

For the first marked term use the row sum of B; for the second use the
column sum of A. Thus neither inequality is justified from row bounds alone.
Applying (9) to P R^n and summing proves the actual original-variable
expansions

    (K+a)^{-1}=Σ_{n≥0}Σ_{q0,...,qn} P_q0 R_q1...R_qn,
    M((K+a)^{-1})≤p(a)/(1-r(a)),
    B((K+a)^{-1})≤Jn_R p(a)/(1-r(a))^2.                       (10)

The inverse identity follows from (K+a)ΣP_q=I-ΣR_q. It uses no logarithm
or zero-free partition function. Absolute weighted convergence permits
grouping terms by their connected union. Holomorphy holds on the open
original product neighborhoods on which (3)–(4) hold uniformly, or locally
on their compact subdomains; a gauge-defined closed class is not called
an open polydisc.

Integrating each atom against a^{-1/2}/π gives the branch K^{-1/2} and

    M(K^{-1/2})≤2wQ_m/[sqrt(γ)(1-r)],
    B(K^{-1/2})≤2Jn_R wQ_m/[sqrt(γ)(1-r)^2].                   (11)

On the full space, or a Π_U-invariant integrated subspace, Setting N5-bg's
physical square root is obtained by subtracting the explicitly block-local
I-Π_U; add its own finite M and B bounds to (11). On arbitrary coordinate
compressions, (10)–(11) bound only the compressed augmented operator.
Subtracting the compressed I-Π_U does not in general give a physical
covariance; that interpretation requires a region-specific slice and gap.
For complex variables all transposes and quadratic forms are bilinear. The
augmented square root is positive on real data and is continued holomorphically;
the physical covariance on the stated invariant slice is positive there.

**Small tori and R dependence.** The local curvature-only derivation of
(4) requires nonwrapping collars, for example T≥4R+2r_dep+2. Reusing the old
epsilon_*(R_*) after increasing R is invalid. A sufficient curvature bound
is the N5 AX bound with the new collar diameter: epsilon_curv≤
α/[10p_L(4R+2r_dep+1)L], with a strictly smaller margin for the complex tube.
For smaller tori, (10)–(11) hold if (4) is separately proved, e.g. from a
global small-link gauge. If T<R use one box, Omega=I, R_q=0; n_R still
majorizes its coordinate count. No general flat-holonomy small-torus
positivity claim is made. Constants in (11) can be huge and depend on fixed
R,N,L,γ,m. They do not depend on volume or on the deletion pattern **within
the stated compression domain**. No level-uniform theorem follows until
the level-i producer supplies this same domain and original-source atoms.

### 1.3 The full determinant can also be localized

This construction does not require ||I-K||<1. Choose c≥γ_0 and put
K_theta=(1-theta)cI+theta K, 0≤theta≤1. The local compression proof (3)–(4)
applies uniformly to K_theta: the gauged reference is
(1-theta)cI+theta Õ_0, whose gap is at least γ_0, and its perturbation is
theta times the previous perturbation. Increase S_m to c+S_m and select R
once with that enlarged value. Thus (10) holds for K_theta, uniformly in
theta. Write Delta=K-cI=Σ_q 1_q Delta. These original-source-local atoms
can use D_q; with d=w(S_0+c),

    M(Delta)≤d,  B(Delta)≤Jn_R d.

Let g=2wQ_m/[γ(1-r)] and b=Jn_R g/(1-r). Jacobi's identity gives the exact
analytic logarithm

    log det K=dim(I) log c+∫_0^1 Tr(K_theta^{-1} Delta)dtheta.   (12)

Here dim(I)=(N^2-1)|I| counts real Lie-algebra coordinates. The branch is
fixed by this homotopy. The ODE for det K_theta proves exp of (12) equals
det K; invertibility along the homotopy was established first. For every
closed matrix product in the trace the inverse atom and Delta atom share
both endpoints, so their labelled union is connected. Marking the label
containing v gives, with D=N^2-1,

    ||log det K||_β ≤ D n_R exp(β)|log c|
                      +D[b d+g Jn_R d].                      (13)

The constant term is assigned per R-box. To check the trace estimate,
|tr A_xy B_yx|≤D|A_xy||B_yx|; the marked A sum is B(A) times a bound for
an individual B entry, at most M(B), and conversely. Formula (13) is a
separate, generally non-small budget. It is not multiplied by the cubic
interaction size. This closes a missing determinant-localization input
for (2) in independent original coordinates.

### 1.4 What has and has not been constructed

Equations (6)–(13) are actual-input atoms for the level-zero local operator,
including the Wilson coefficient field and the exact soft normalizer.
They improve RW's existing kernel/walk bounds by supplying the missing
original-coordinate support and incidence norms. They are not another
assumption that the integrated density already has the desired expansion.

They do not alone apply after U=b(V,epsilon): that map can read parameters
outside D_q. A source-local expansion for b must first be composed into
these atoms, or another source-independent center must be used. At
U=V=I, the center is independent of epsilon, and this particular bridge is
absent. The nontrivial-background construction and the exact return
specialization are developed below; they are not conclusions of (11).

## 2. Exact Haar return identity with the history retained

### 2.1 A nonlinear gauge identity that is actually exact

Take a finite link region E, fixed collar links eta, coarse V, and a fixed
history h. Write its actual integrand as

    Den_h(V,epsilon;eta)=Z_ref,h(V,epsilon;eta)^(-1)
        ∫ Π_{e in E} dHaar(U_e) Xi_h(U,V;eta)
           exp[-(u/N) S_W,epsilon(U)] Π_c k_t(V_c;Mbar_c(U)).   (14)

Only plaquette/kernel terms used by the region are included; fixed exterior
terms and any chosen reference factors stay in the explicitly named
Z_ref,h. This formula covers a specified denominator by inserting its
**actual** Xi_h and Z_ref,h. It does not define away those choices. At level
zero rho_0 is exactly the Wilson factor. If an inherited density occurs,
multiply it into (14) before applying any change of variables.

Let B contain every coarse anchor and both endpoints of every fixed collar
edge. Choose a rooted spanning forest T of the movable vertices using
integrated edges, with one root in B per component. A component without a
root may have one additionally fixed gauge root. The forest is chosen from
the geometry, not the fields or source coefficients. No fixed collar edge
belongs to T. For each U there is a unique gauge g_T, equal to I on the
roots, setting all tree edges to I: recurse along each rooted path. Let Z
be the remaining free link values after this gauge transformation.

The mapping U↔(U_T,Z_{E\T}) preserves product Haar measure exactly.
To prove it, eliminate leaves in a fixed order: at each step the change of
a remaining link is left/right multiplication by a previously exposed
group variable, and normalized Haar measure is invariant. Iterate Fubini.
Every tree variable has integral one. Equivalently the map is triangular
in these leaf coordinates with unit Haar Jacobian. The Wilson trace and
each kernel are invariant: its contour endpoints are fixed coarse anchors,
so Mbar_c is unchanged. The collar is unchanged because both endpoints of
its fixed edges lie in B.

If Xi_h is gauge invariant under this group, it becomes Xi_h(Z,V;eta).
Without that property the exact retained factor is instead

    Xi_h^T(Z,V;eta)=∫ Π_{e in T}dHaar(U_e)
                           Xi_h(U(U_T,Z),V;eta).               (15)

There is no unrecorded assumption of gauge invariance of a history sector.
The scalar Boltzmann/kernel part factors out of this tree integral. Thus
(14), with E replaced by E\T and Xi_h by Xi_h^T, is an **exact nonlinear**
gauge identity. Its gauge Jacobian is one, its gauge volume is one, and no
Gaussian NA-FP determinant has been promoted to a nonlinear formula.

For a full periodic lattice choose a tree within each L-block rooted at
its coarse anchor. Its maximal path length is ell_T≤4(L-1), independent
of volume. Regions with holes use the same proof whenever such rooted
trees preserve their collar; arbitrary regions need not admit the same
uniform depth bound. The algebraic identity itself needs no depth bound.

### 2.2 Chart, determinant, linear term and cutoff

Choose a tree-gauge center bar Z and restrict this sector to its injective
exponential chart Z_e=exp(a_e)bar Z_e. Include the chart restriction in
Xi_h^T if it was not already present. The omitted complement is an
additional integral in (14), not zero by convention. Write n=|E\T| and
n_d=D n, D=N^2-1. In an orthonormal Hilbert–Schmidt Lie basis,

    dHaar(exp(a)bar Z)=c_N j(a) da,
    j(a)=det_g[(1-exp(-ad_a))/ad_a],  j(0)=1.                  (16)

The removable singularity uses its entire series. For real a in the
small chart j(a)>0; it has a fixed holomorphic logarithm on a smaller
complex chart. c_N is the constant for **normalized** Haar measure in
this coordinate convention and must not be dropped. There is one such
constant per free link, not per original link before gauge reduction.

On this chart use exactly S_eff of (1), including every local kernel
normalizer. Let Q be any complex symmetric matrix, positive on the real
data under consideration, with the chosen holomorphic square root. It
need not be the Hessian. Set

    S_0=S_eff(bar Z;V,epsilon),  ell=∂_a S_eff|_0,
    R_Q(a)=S_eff(exp(a)bar Z;V,epsilon)-S_0-ell^T a
                                      -(1/(2sigma^2))a^TQ a. (17)

Hence a mismatch between Q and the exact Hessian remains in R_Q. In
particular stationarity of only the tree action does not set ell to zero.
With C=Q^(-1/2), a=sigma C W, ordinary real change of variables gives

    Den_h^chart = P_h exp(-S_0) det(Q)^(-1/2)
       × E_gamma[Xi_h^T(exp(sigma C W)bar Z,V;eta)
                     exp(-ell^T sigma C W-R_Q(sigma C W))
                     Π_e j((sigma C W)_e)],                    (18)
    P_h=Z_ref,h^(-1)c_N^n(2πsigma^2)^(n_d/2).

All chart/region/history restrictions, including holes, are inside the
displayed Xi_h^T. If the actual history has another inherited weight,
its pulled-back value belongs inside the expectation too. No determinant,
linear term, action at the center, Haar density, or reference normalization
has been absorbed into a supposed O(cubic interaction) error.

If and only if this sector's actual restriction can be written

    Xi_h^T(exp(sigma C W)bar Z,V;eta)=chi_p(W) Theta_h(W;V,eta),

where chi_p is the chosen fixed product cutoff, (18) becomes

    Den_h^sf=P_h exp(-S_0)det(Q)^(-1/2)N_chi
        × E_mu_p[Theta_h exp(-U)],
    U=ell^T sigma C W+R_Q(sigma C W)-Σ_e log j((sigma C W)_e),
    N_chi=gamma_D(|W|_infinity≤p)^n.                           (19)

The equality must be checked for the actual indicator, not asserted from
its name. For a general Xi_h, inserting 1=chi_p+(1-chi_p) splits (18) into
two exact terms, and the second remains a return obligation. The same
applies to the outside-chart contribution to (14).

For real parameters (18) is an ordinary measure identity. For complex
parameters (19) defines the analytic continuation only when the W-domain
is fixed, the integrand is holomorphic, and a uniform integrable bound
holds. An absolute-value indicator with a moving complex boundary does
not satisfy this condition. One must specify its continuation or prove a
contour identity. Analytic continuation of a fixed-domain integral is not
an equality to an unspecified complex cutoff operation.

Whenever the reduced expectation in (19) has a proved logarithm,

    Δlog Den_h^sf=Δlog P_h-ΔS_0-(1/2)Δlogdet Q
                      +Δlog N_chi+Δlog E_mu_p[Theta_h e^(-U)]. (20)

This is the full returned-denominator identity. Theta_h=1 is a special
case, not a consequence of Gaussian positivity. A history factor with
zero integral can invalidate zero-freeness without changing Q at all.
The source currently names Den_Y only as an integral “of the type” of CX;
it does not supply a concrete Xi_h/Z_ref,h/contour definition allowing a
universal match to (19). Formulae (14)–(20) preserve those data rather
than replacing them by a new unrestricted integral.

## 3. A concrete weak-coupling level-zero specialization

### 3.1 The actual tree-coordinate Hessian

On the full torus use the block trees above, set bar Z=I and V=I, and retain
the original Wilson coefficient field. This is an actual nonabelian SU(N)
integral, for any fixed N≥2. No minimizing/critical-branch consumer identity
is used. The center is independently critical for every epsilon: the
Wilson gradient is zero at I, ψ starts quadratically, and Ntilde has zero
first derivative since Mbar=I+QA+O(A^2), W_0=I+QA+O(A^2), so its centered
arguments change only at second order. The Haar logarithm also starts at
second order. Thus ell=0 here for the **exact** S_eff.

Let J_T embed the free-link Lie coordinates by zero on tree edges. Define

    Q_bare=J_T^T Hess[S_W+κΣ φhat]|_{U=V=I} J_T,
    Q_0(u)=Q_bare+sigma^2 J_T^T Hess Σ log Ntilde_t|_I J_T.      (21)

This is the exact scaled Hessian of the Haar-density action S_eff, before
putting j into the remainder. It is **different from** (2): it lives on
actual tree-gauge free coordinates and has no artificial residual fixing.
The difference is identified, not hidden by using the same symbol.

Here is a gap proof from the existing flat N5 operator. Let T_lin be the
linear operation that sets tree links to zero using the rooted path sums.
It fixes tree-gauge fields and annihilates DΛ. Each row has at most
1+2ell_T absolute weight; each input tree edge affects at most 8L^4 output
link rows, so

    ||T_lin||_2^2≤C_T^2=(1+8(L-1))(1+8L^4).                   (22)

For a tree-gauge A, the invertibility of χ_1D from NA-FP(ii) supplies a
representative A_chi in its orbit with hA_chi=0 and P_res D^T A_chi=0.
Flat criticality gives gauge invariance of its quadratic form. Hence

    A^T Q_bare A=H(A_chi,A_chi)
       ≥γ_0||A_chi||_2^2 ≥(γ_0/C_T^2)||A||_2^2.              (23)

The last step is T_lin A_chi=A. This argument uses NA-FP only for its
proved linear statement; the exact nonlinear integration was established
separately in section 2. The local normalizer Hessian has row/column norm
≤C_N, so

    Q_0(u)≥gamma_T I,  gamma_T=γ_0/C_T^2-sigma^2 C_N>0         (24)

for sufficiently large real u. All constants depend only on N,L,κ and
the supplied analytic neighborhoods. (21) is finite-range with bounded
row sums. CT and sections 1.2–1.3 therefore construct its fluctuation
atoms and determinant. For the uniform large-u family, take
sigma^2 C_N≤γ_0/(2C_T^2) and use the fixed lower bound
gamma_T=γ_0/(2C_T^2) in the estimates. Global trivial backgrounds need no
large-torus/local-gauge qualification. Dirichlet free-coordinate
compressions inherit (24).

### 3.2 Fix the cutoff before introducing the coefficient source

Choose the target rate μ_0≥0 and use β=μ_0+2 in all support bounds for
this specialization, with the corresponding R and covariance constants.
Use Q=Q_0(u), independent of epsilon, and C=Q_0(u)^(-1/2). Define the actual
small-field sector by its **fixed reference** tree coordinates
a=sigma C W and chi_p(W). This definition is made at epsilon=0 and kept
unchanged when the original coefficients vary. Thus the identity relates
the same sector of the same original Haar integral for every epsilon;
source-dependent cutoffs have not been substituted.

At V=I, bar Z=I, S_0=Σ_c log Ntilde_t(I), independent of epsilon, and
ell=0. The determinant, reference measure and cutoff probability are also
epsilon-independent. If Theta_h=1 and Z_ref,h is fixed, (19) is now a
completely identified integral. The original coefficient perturbation
appears exactly as

    U_source(W;epsilon)=(u/N)Σ_p epsilon_p
                          Re tr[1-U_p(sigma C W)].            (25)

The plaquette functions vanish to order two at A=0. The baseline R_Q is
cubic because Q_0 is its exact Hessian; the Haar logarithm is quadratic.
Let M_C and B_C be the finite row/incidence majorants of section 1 for C,
in a fixed support norm β. Let a_* be a common local analyticity radius.
Taylor/Cauchy estimates and connected-support substitution give computable
constants A_1,A_2,A_3 depending only on the local stencil, N,L,κ, the chosen
R, β, M_C,B_C,a_* and the uniform normalizer analytic bounds, such that

    ||U||_β ≤ A_1 sigma p^3+A_2 sigma^2 p^2
                                  +A_3 rho p^2,              (26)
    sigma p M_C < a_*/2,   |epsilon_p|≤rho.

One explicit way to calculate these constants, avoiding an inference from
low-order derivatives, is the all-order coefficient majorant as follows.
For each connected local stencil B, with at most q scalar coordinates,
let H be the supremum of its analytic vertex on |a_i|<a_*. If its Taylor
terms of degree <r vanish, use

    F_r(x)=H Σ_{n≥r} binom(n+q-1,q-1)(x/a_*)^n.

After inserting the covariance atoms, the rooted bound is at most

    d_B exp(β|B|)[F_r(sigma p M_C)
                                 +sigma p B_C F_r'(sigma p M_C)]. (27)

All scalar choices are counted by the binomial coefficient; no q factor
is omitted. Use r=3 and H proportional to u/N=sigma^(-2) for baseline
action remainders, r=2 and bounded H for -log j, and r=2 with H proportional
to rho sigma^(-2) for (25). Terms from log Ntilde are uniformly bounded
on a fixed complex field neighborhood for real u>0 only after subtracting
the field-independent vacuum value: the uniformly bounded objects are
log Ntilde_t(M)−log Ntilde_t(I) and its field derivatives/remainders.
The vacuum logarithm itself grows with log t and stays in S_0, not the
fluctuation interaction. The field-dependent remainders only improve the
large-u powers. On x/a_*≤1/2 the three coefficient series explicitly
bound (27) by (26). The locality includes the original epsilon_p in B;
the support of A alone is not used as the coefficient support.

For any fixed p and sufficiently small fixed rho and sufficiently large
u, require the right side of (26) to be at most 1/4 at the chosen
β=μ_0+2. This is the generic CX-R product-measure threshold. Thus, subject
to the independently checked CX-R combinatorial lemma, (19) is zero-free
and its **epsilon-dependent** logarithm has connected original-source
activities. For p(u) growing logarithmically, the sufficient condition is
sigma p(u)^3→0 and rho(u)p(u)^2→0; a fixed relative coefficient radius is
not asserted for that growing cutoff. The physically smeared source has
epsilon=O(u^{-1}) on a fixed source disc, so this particular level-zero
source regime meets the latter condition. No marginal-flow conclusion
is inferred from it.

This is a genuine instantiation at level zero, trivial coarse data,
empty retained history, with a fixed reference white-noise sector. It is
not the full return: the outside-chart/cut-failure integrals, nontrivial
Theta_h, nontrivial coarse background, and all higher-level induction
remain separate. Their absence is a scope limitation, not a proof that
the full Yang–Mills program is impossible.

## 4. Constructing the original-source background on the global chart

This section supplies the substitution missing from section 1 on a
**specified global neighborhood of the trivial tree-gauge field**. It does
not claim the curvature-only class with arbitrary holonomy or arbitrary
hole histories. The variables are the original coarse-link coordinates
B, V=exp B, and original epsilon_p, all in a fixed product polydisc. The
finite-volume construction below is uniform in volume and real u≥u_*.

### 4.1 A support-norm implicit construction from the actual local action

Use the same geometrically fixed block tree gauge. In its global free-link
coordinates a, set

    F(a;z)=sigma^2[S_eff(exp a;exp B,epsilon)-Σ_e log j(a_e)],
    z=(B,epsilon),  K_*=∂_a^2 F(0;0).                         (28)

This time the Haar density is part of the Lebesgue action. Its determinant
has no zeros on a fixed small chart, so its local derivatives are bounded.
For sufficiently large u, (24) with C_N+C_j in place of C_N gives a
uniform positive gap for K_*. It is a finite-range, real symmetric matrix
in the fixed tree coordinates. Its inverse G has the atoms of section 1.
Here all source variables of G are fixed at zero; only the global real
coupling u and the geometry are spectators. All bounds can be chosen
uniformly for u≥u_*.

Let f(a,z)=K_*a-∂_a F(a,z). Every component f_i reads a fixed connected
stencil B_i of original fine/coarse/coefficient coordinates. It satisfies

    f(0,0)=0,  ∂_a f(0,0)=0.                                 (29)

These are identities of (28), not an assumption of an unknown minimizer.
For a common radius a_*>0, the local functions f_i are holomorphic and
bounded by H on their scalar-coordinate polydiscs. This follows from the
explicit finite products/exponentials, the local polar map, the proved
real-t single-normalizer domain, and the local Haar determinant. The
factor sigma^2 cancels the u factor in the Wilson/soft part and suppresses
the other terms, so H and a_* are uniform for u≥u_*. Let q_a,q_z bound the
numbers of scalar a,z variables in each stencil; let s_* bound its R-box
cardinality and d_* the number of force-component stencils meeting a
given R-box. These are finite constants for fixed R,N,L.

For vector atoms A_i;S require S connected, containing the box of i, and
depending only on original z_S. Define

    ||A||_v=max{sup_i Σ_S exp(β|S|)||A_i;S||,
                sup_v Σ_{i,S containing v}exp(β|S|)||A_i;S||}. (30)

This uses scalar coordinates; the finite color-coordinate factors are
included when converting section 1's Hilbert–Schmidt block bounds. In
particular the scalar inverse has finite M_G and B_G. Each original source
coordinate is a singleton atom; its combined norm is at most
z_*=n_z exp(β) eta if |z_j|≤eta, where n_z bounds the scalar source count
in one R-box. The coefficient indices have not been replaced by a solved
background field.

Taylor-expand each **actual** f_i and retain its original local stencil
in every monomial. Substitute A atoms into its a factors and the singleton
source atoms into its z factors. All labels meet B_i, so the union is
connected and contains the complete original source dependence. A degree
(n+m) monomial has at most n+m+1 ways for a specified support vertex to
belong to the root stencil or a marked factor. The inequalities
n+m+1≤2^(n+m) for n+m≥1, followed by Cauchy's coefficient estimate, give

    ||f(A,z)||_v ≤ d_*exp(βs_*) H
       [(1-2t/a_*)^(-q_a)(1-2z_*/a_*)^(-q_z)
                                    -1-2q_a t/a_*],          (31)
    t=||A||_v,  2t,2z_*<a_*.

The subtractions are permitted by (29); all remaining majorant coefficients
are nonnegative. The same marked-factor proof for a difference gives the
derivative of the right side with respect to t as a Lipschitz majorant.
Indeed a degree n in A supplies n telescoping difference terms, and the
factor n2^(n+m) already bounds n(n+m+1). This is an all-order coefficient
argument, not a finite-derivative locality inference.

Multiplication by G obeys

    ||G h||_v≤(M_G+B_G)||h||_v.                               (32)

This follows from the same row/column/marked-incidence multiplication as
(9). Let Psi(t,z_*) be (31)'s right side times M_G+B_G. It is an explicit
analytic nonnegative power series, Psi(0,0)=0 and ∂_tPsi(0,0)=0. Therefore
one can select positive tau,eta, in this order, by the **computable** tests

    tau<a_*/8,  z_*<a_*/8,
    ∂_tPsi(tau,z_*)≤1/2,  Psi(0,z_*)≤tau/2.                   (33)

They imply Psi(tau,z_*)≤tau. Picard iteration

    A_0=0,  A_{n+1}=G f(A_n,z)                               (34)

converges in (30), with geometric ratio ≤1/2, to b(z). Thus

    ∂_a F(b(z);z)=0,  ||b||_v≤tau.                           (35)

Each iterate and its limit have connected **original-z** support atoms.
The weighted norm is complete after taking absolutely summable coefficient
families; uniform convergence of the holomorphic iterates proves
holomorphy. Evaluation gives the unique critical point in the corresponding
small ball, also by the ordinary pointwise contraction. It is real for
real sources, since the local action, G and iteration are real there.
No minimum-action identification or new physical axiom enters.

The hypotheses of this fixed-point theorem have been checked from the
actual level-zero local action and the existing flat gap. The constants
are existence/computable-majorant constants, not numerically optimized.
This produces the missing all-order source-local map on this global chart.
It is stronger than merely assuming that the map has such a norm, and
its output is explicitly used below.

### 4.2 The actual Hessian and determinant after substitution

Let K(z)=∂_a^2 F(b(z);z), and Delta(z)=K(z)-K_*. Each pre-substitution
Hessian entry is local in a and z and has a finite coordinate stencil.
Taylor substitution using b's atoms and (27)/(31), including the row,
column and marked incidence counts for its two matrix endpoints, gives

    M(Delta)≤d_M(tau,eta),  B(Delta)≤d_B(tau,eta),
    d_M(tau,eta),d_B(tau,eta)→0 as tau,eta→0.                  (36)

These majorants are obtained by deleting the constant Taylor coefficient
of the local Hessian entry, using the same Cauchy radius and finite stencil
counts. More explicitly, on a smaller radius a_h let H_h bound each local
Hessian entry, q_ha,q_hz bound its input coordinate counts, s_h its stencil
size, and d_h bound the number of ordered-entry stencils meeting a support
vertex (and both row and column entry counts). Both d_M and d_B may be
chosen as the following single majorant:

    d_h exp(βs_h) H_h
       [(1-2tau/a_h)^(-q_ha)(1-2z_*/a_h)^(-q_hz)-1].           (36a)

Reduce tau,z_* to less than a_h/4. The marked-term proof is exactly the
degree-plus-one counting of (31); it includes both matrix endpoints in the
root stencil. Thus (36) consists of explicit convergent coefficient sums
of the actual functions. The complex Hessian is symmetric; its transpose-paired atoms
may be grouped so the column count is paid as well. There is no decay-only
shortcut in (36).

For G_a=(K_*+a)^(-1), the already constructed atoms obey
M(G_a)≤M_0 γ/(γ+a), B(G_a)≤B_0 γ/(γ+a), with constants M_0,B_0 from
(10). Reduce (33)'s source radius until r=M_0 d_M<1/2. The actual inverse
then has the original-source atoms

    (K(z)+a)^(-1)=G_a Σ_{n≥0}(-Delta G_a)^n,                  (37)
    M≤M(G_a)/(1-r_a),
    B≤B(G_a)/(1-r_a)
       +M(G_a)[d_B M(G_a)+d_M B(G_a)]/(1-r_a)^2,
    r_a=d_M M(G_a)≤r.

Every product is connected because matrix endpoints are in their labels.
The same bounds with denominators 1-r dominate the square-root integral;
all numerator products decay at least as (γ+a)^(-1). This proves finite
row/column/incidence bounds for K(z)^(-1/2), uniformly on the chosen
original source polydisc. The complex branch agrees with the positive
square root on real sources. Real positivity also follows from the small
operator perturbation of K_*.

The source-dependent determinant has the exact expansion

    logdet K(z)-logdet K_*=
        ∫_0^1 Tr[(K_*+s Delta(z))^(-1)Delta(z)]ds,             (38)

localized by the same marked-product proof as (12)–(13). The baseline
logdet K_* is independent of all original spatial sources. The action at
the solved center, S_eff(exp b;exp B,epsilon)-Σ logj(b), is also localized
by the Taylor composition. Its norm may grow like u times the squared
coarse-field size. It stays in the explicit main term and is **not** charged
to the cubic fluctuation budget. This closes the original-source
substitution bridge for these level-zero global-chart quantities.

### 4.3 The cut does not disappear under this construction

The solved center and covariance define an analytic **moving-contour**
integral over a=b(z)+sigma K(z)^(-1/2)[-p,p]^(n_d). For real data its
interpretation is a chosen small-field sector of the raw Haar integral.
To compare it with a denominator whose sector was fixed at reference
sources, a boundary term remains. Here is the exact finite-dimensional
formula, before any estimate.

Let D=[-p,p]^(n_d). Let A_0(w) be the actual reference affine chart and
A_z(w)=b(z)+sigma K(z)^(-1/2)w. Assume the straight homotopy H(s,w) from
A_0 to A_z stays within the holomorphic chart of the **target** integrand
f_z(a) da_1...da_{n_d}. Orient the side chain so Stokes gives

    ∫_{A_z(D)} f_z(a)da - ∫_{A_0(D)} f_z(a)da
        = ∫_{H([0,1]×∂D)} f_z(a)da.                          (39)

The n_d-form is closed because it is holomorphic; the boundary-of-a-product
identity proves (39), including at complex z. The side is a sum of 2n_d
explicit face integrals with the corresponding Jacobian minors. Thus the
reference denominator equals the moving-contour expression **minus** that
side integral. A hard history indicator is not a holomorphic f_z; it must
be kept as a real-domain restriction or decomposed before (39). It cannot
be swept through the homotopy under this argument.

There is a useful size fact for the intended weak-coupling window.
For this estimate fix B and take the reference specifically to be

    A_0^(B)(w)=b(B,0)+sigma K(B,0)^(-1/2)w,

varying only epsilon in A_z. The general Stokes identity (39) allows any
stated reference satisfying its homotopy hypothesis; the estimate here uses
this same-B, zero-epsilon reference.
b(0,epsilon)=0 for every small epsilon, by the exact trivial-field
stationarity and uniqueness. Hence the analytic difference
b(B,epsilon)-b(B,0), which vanishes both at B=0 and at epsilon=0, has a
bilinear Cauchy bound O(|B| |epsilon|) on smaller polydiscs. Similarly the
covariance changes by O(|epsilon|). For |B|≤c sigma p and |epsilon|≤rho,
the shift in reference W coordinates is O(rho p), and the linear-map
change is O(rho). Choosing rho small keeps swept faces a fixed fraction
of p away from the new Gaussian center. The constants here are uniform
on the constructed chart and follow from the convergent analytic atoms.

This last geometric fact is **not** a proved history-uniform bound for
the normalized side integrals in (39). Absolute estimates that replace
all remaining complex Gaussian directions by their suprema can lose an
exponential in volume. A valid return estimate must cancel the common
bulk factors or prove a local face expansion; the present calculation
has not yet supplied it. Keeping the exact side term is essential. In
particular sections 4.1–4.2 solve a source-locality producer on this chart;
they do not establish the full denominator of every return history.

## 5. Checkpoint, executed checks, and exact scope

Frozen author checkpoint: **2026-10-29 12:26 UTC**. The coordinator requested
an Astra/max worker; this note does not independently attest runtime model
metadata. Same-vendor author calculations are not a fresh referee.

Executed, with exit code zero and no stderr observed:

    python3 checks/source_return_exact.py > checks/source_return_results.json

The script uses only exact rational arithmetic. All **21** named predicates
passed. No positive scientific status is inferred from that count.

| Calculation | Result and discrimination | Scope |
|---|---|---|
| 12-site coefficient-dependent cyclic matrix | Direct Gaussian elimination, local compression identity, and Neumann remainder agree exactly through order 3; 60 nonzero support atoms | Finite algebra check of the parametrix; scalar test matrix, not the Yang–Mills operator |
| Weighted row/column/incidence sums | Both endpoint sums and the marked-incidence bound hold; every nonzero atom has connected support containing both endpoints | Checks the finite support accounting independently of the closed-form analytic bound |
| Original coefficient dependence | Changing a coefficient outside an atom's collar leaves it identical; changing an interior coefficient changes the local inverse | Tests retention of the original coefficient field |
| Row-only diagnostic | A separate matrix has row norm 1/4 and column norm 3/4 | Detects an illicit row-to-column inference |
| Determinant | Permutation/cofactor calculation and inverse trace both give d[-logdet K/2]/dz=-377285/2720727 | Omitting the determinant predicts zero and fails |
| Noncommuting SU(2) links on a 3^4 lattice | 324 unit quaternion links, 80 tree links become I; all 486 plaquette traces and 648 anchored contours remain exactly equal | Actual nonabelian gauge/contour identities; no nonlinear Hessian or Haar integral was numerically evaluated |
| Corrupted free SU(2) link | At least one plaquette trace changes | The gauge identity check is capable of failing |
| Fixed versus moving interval | Independent endpoint and oriented-face integrations give side term 44/45 | Dropping the side term fails; this is a polynomial differential-form check, not a Gaussian tail bound |
| Retained history indicator | Exact integral is 3/2 versus 2 after discarding the indicator | Detects the unjustified Theta_h=1 replacement |

Script SHA-256:
`a41aec8a773fbd2f00f9cf675186f5aa4d62395602fe55b687f88656d44b03aa`.
Output SHA-256:
`7da955603c753fcefc16e938c33ab2f8d47ad8c480f437cace3010eda7a611a5`.
The companion `checks/source_return_receipt.json` binds the note, script,
output and actually inspected source identities. Hash agreement is only
provenance, not mathematical review.

**Author result ready for fresh review.** (i) A level-zero original-variable
parametrix and determinant expansion with all three support norms, on its
explicit complex compression domain. (ii) An exact nonlinear tree-gauge
Haar identity retaining chart, history, collar, cutoff, Jacobian, reference
and linear terms. (iii) An actual trivial-coarse-field, fixed-sector source
instantiation. (iv) A global-chart all-order original-source critical-map
construction and its Hessian/determinant substitution, using the actual
level-zero action. These are author proofs with computational checks of
selected finite steps; independent review is pending.

**The next scientific task is precise.** On the source-dependent background
just constructed, prove a connected, normalized expansion for the face
terms in (39), with the actual retained history indicator and its collar
data. The level-zero chart gives a concrete starting operator and source
domain; it does not supply the all-history uniform norm by itself. Then
the one-step output must be shown to preserve the same source norm and
operator identity at higher levels. No claim is made for the minimum
tower E_NA from a critical-value theorem, for all V, or for OS0–OS3 on R4.
The work remains inside the user-authorized full-proof effort; this frozen
checkpoint is not a declaration that that target is complete.
