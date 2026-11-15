# RD — the actual returned denominator and a complete-factor completion criterion

**Theorem RD at the requested history/scale/volume-uniform scope: OPEN.**
Pass 2 constructs an exact effective-density return, with an explicit
history recursion, a joint replacement operator, and a finite connected
expansion of its actual denominator (§3.1–§3.6). Earlier integrations are
opened back into their original Haar variables; inherited terms are not
replaced by a Wilson action. Every failed return and every real chart
complement remains in the identity. This is an exact finite expansion,
not a convergent small-activity logarithm. The common zero-free domain,
uniform norm estimates and quantitative RG induction remain OPEN.

Pass-2 author source: `295b508bea2c65bf548172f3190e32f7f7eaf6cf`.
[RD_LOG.md](RD_LOG.md) records source hashes, reads, review and recovery state.
No commits, audit verdicts, ledger changes or axiom changes belong to this lane.
PROVEN below means an ordinary mathematical proof at the displayed scope;
ARGUED means a proposed construction; OPEN identifies an undischarged step.

The small/large-field method is due to Tadeusz Balaban; Jonathan Dimock's
[small-field](https://arxiv.org/abs/1108.1335),
[large-field](https://arxiv.org/abs/1212.5562) and
[convergence](https://arxiv.org/abs/1304.0705) expositions provide attribution.
These expositions concern the scalar model in three dimensions. No literature
theorem or claimed nonabelian analogue supplies a proof step here. The cluster
argument used below is rebuilt; LIB1's reviewed R10 is consumed as explicitly
permitted by the brief.

## 1. Theorem RD: target and exact scope

Fix N≥2, odd L≥3, real u>0 and κ in a fixed compact subinterval of (0,∞).
The block graph Γ is a finite four-dimensional torus (T≥2) or a box with
fixed exterior links. All Haar measures are normalized. Γ includes the
collars and hole vertices needed to label every original field/source read.
The analytic variables ε_p are the **original Wilson coefficient sources**;
the Decision-4 kernel parameter κu stays real and fixed. Real exterior fine
links and real coarse V are parameters. An extension to complex V is a
separate requirement of STEP55 and is not implied by ε-holomorphy.

**OPEN — target estimate.** For every admissible one-step return region Y,
history h, and fixed hole/collar geometry, use the denominator D_{k,h,Y}
constructed in (R6), with the reference in (R9). On a common product domain in the
original sources (and the coarse fields where the consumer requires them),
prove

    D_{k,h,Y}(z) = N^{ref}_{k,h,Y} exp(Σ_X K_{k,h,Y}(X;z_X)),       (RD)

with an explicitly bounded nonzero reference, holomorphic original-data-local
connected activities, and a rooted norm bounded independently of k, h, Y,
holes and volume. A source-independent choice is N^{ref}=D(0), when that
actual denominator is positive. Alternatively all source-dependent main,
determinant, cut and reference factors must be displayed and bounded
separately. Zero-mass history **numerators** must not be used as references.

The requested conclusion includes the actual effective density at level k,
its inherited interactions and every failed-return contribution. Section 3
now supplies an exact identity for these objects. Its finite expansion has
no smallness guarantee. The coarse history convention is fixed explicitly
there; a different supplied joint history is retained as a joint insertion,
not identified with this convention without checking its indicator.

For μ≥0 write

    ||K||_μ = sup_{v∈Γ} Σ_{X∋v} e^{μ|X|} sup_D |K_X|.             (1)

Supports are connected in the ambient face graph and include all original
parameters read, even when some of their vertices are not integrated. This
is the CX-R full support norm. LIB1's active norm after saturating holes is
different; §6 states both without equating them.

## 2. The actual bare denominator, with no chart substitutions

**PROVEN — identification.** Let I(Y) be all fine links whose endpoints lie
in one block of Y. Every link joining different blocks is frozen. P(Y)
contains all plaquettes reading I(Y); C(Y) contains the coarse links with an
endpoint block in Y. The complete frozen data η include the fine links in
N₁(Y) outside I(Y), and V on C(Y). Define

    s(U)=1−Re tr(U)/N,
    M_c(U)=(4!L⁴)⁻¹ Σ_σ Σ_{y∈B(X)} T_y^σ(U),
    k_t(V;M)= exp{−t[1−Re tr(V⁻¹M)/N]}/N_t(M),
    N_t(M)=∫ exp{−t[1−Re tr(W⁻¹M)/N]} dHaar(W),   t=κu,
    χ_Q=Π_{p wholly interior to Q}1{||I−U_p||op<ε_cut},
    χ_Y=Π_{Q∈Y}χ_Q,          ζ_Y=Π_{Q∈Y}(1−χ_Q),
    w_Y^ε=exp{−uΣ_{p∈P(Y)}(1+ε_p)s(U_p)} Π_{c∈C(Y)}k_t(V_c;M_c),
    D_Y^ε(η,V)=∫ χ_Y w_Y^ε dHaar(U_{I(Y)}),
    N_Y^ε(η,V)=∫ ζ_Y w_Y^ε dHaar(U_{I(Y)}).                    (2)

Here 0<ε_cut≤2 is fixed, independent of the coefficient sources. All matrices
inside these integrals are real group variables; no nonholomorphic operation
is applied to ε. The denominator in RLARGE §3's bare frozen quotient is
**exactly D_Y^ε**, and the quotient is N_Y^ε/D_Y^ε where the denominator is
nonzero. Every factor reading an integrated link is present. A factor in
C(Y) which happens not to read I(Y) stays in both integrals.

This reconstructs H2–H4 of [the history return](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md).
It specifies the object that STEP55 §5.4 leaves as an integral “of the type”
of CX. It does not assert that an effective-level or multilevel history
denominator equals (2). For those levels the actual conditional density and
indicator must replace w_Y and χ_Y before applying any argument.

**PROVEN — exact positive reference with explicit bounds.** Put

    m=|Y|,  n_l=4L³(L−1),  n_P=6n_l,
    δ=min(ε_cut/8,1/2),
    M_N(δ)=(1+4√2 N/δ)^{2N²},
    A(u)=n_l log M_N(δ)+2u n_P+16κu.

For every real frozen datum, including arbitrary fixed holes and coarse
fields, the denominator (2) obeys

    exp{−A(u)m} ≤ D_Y^0 ≤ exp{16κu m}.                       (3)

These bounds are deliberately coarse. They are uniform in the data and
geometry for this **bare block-interior** operation, with the displayed
coupling dependence; they are not small-action or mixing bounds.

Proof, step 1 — PROVEN. A unitary matrix has s∈[0,2]. M is an average of
unitary matrices, so ||M||op≤1 and 1−Re tr(V⁻¹M)/N∈[0,2]. Therefore

    e^{−2t}≤N_t(M)≤1,             e^{−2t}≤k_t(V;M)≤e^{2t}.   (4)

No single-kernel zero-free theorem is used for a complex integral here.

Proof, step 2 — PROVEN. A lower bound for the Haar mass of the operator-norm
δ-cap can be obtained without a supplied Haar-ball constant. Embed SU(N) in
the 2N² real entry coordinates of [−1,1]^{2N²}; subdivide each coordinate
interval into at most ceil(4√2 N/δ) intervals of length ≤δ/(2√2 N).
The Frobenius diameter of a cell is at most δ/2. Choose a group representative
in each nonempty cell. Left translates of the open identity δ-cap about
these representatives cover SU(N). There are at most M_N(δ) cells. Haar
invariance and the union bound give cap mass ≥M_N(δ)⁻¹.

Proof, step 3 — PROVEN. Restrict every I(Y) link to that cap. An interior
plaquette is a product of four unitary links or inverses; telescoping gives
||I−U_p||op<4δ<ε_cut. Thus χ_Y=1 on this cap product, regardless of the
exterior. There are n_l m integrated links, at most n_P m affected plaquettes
(six per fine link), and at most 8m coarse factors. Use (4), the cap mass,
and s≤2 for the lower bound. The upper bound uses χ≤1, exp(−uΣs)≤1 and
normalized Haar measure. Empty Y has D_∅^0=1. ∎

If a different history indicator is inserted, a positive lower bound requires
a positive-mass subset where that indicator survives. Formula (3) does not
cover arbitrary retained indicators merely because the unconditioned cut is
nonempty. The reference in (2) never divides by such a history probability.

### 2.1 A complete-integral source estimate, with its size dependence visible

**PROVEN — finite-domain result, not uniform RD.** Set

    dν_Y^0 = χ_Y w_Y^0 dHaar / D_Y^0,
    D_Y^ε/D_Y^0 = E_{ν_Y^0} exp{−uΣ_{p∈P(Y)}ε_p s(U_p)}.     (5)

This is the exact denominator, including its cut, kernel normalization and
all configurations allowed by that cut. It is entire in ε at finite volume.
For any 0<r<π/2 it is nonzero on

    u Σ_{p∈P(Y)} |ε_p| < r.                                 (6)

On this domain the analytic logarithm normalized to zero at ε=0 satisfies

    |log(D_Y^ε/D_Y^0)| ≤ 3r−log cos r,
    e^{−2r} cos r ≤ |D_Y^ε/D_Y^0| ≤ e^{2r}.                  (7)

Proof — PROVEN. Extract exp(−uΣε_p) and put
F(ε)=E exp{−uΣε_p(s_p−1)}. Since |s_p−1|≤1, the exponent of each
integrand has real part in [−r,r] and imaginary part in [−r,r]. Hence
Re F≥e^{−r}cos r>0, |F|≤e^r, and |arg F|≤r (the sector of angle 2r is
convex). The right-half-plane logarithm of F is holomorphic; its modulus
is bounded by 2r−log cos r. Add −uΣε_p to obtain (7). This proof includes
all of the measure in (5), without using a Gaussian sector or a cancellation
of omitted factors. ∎

A product disc |ε_p|<ρ follows only when u n_P m ρ≤r. Thus this argument
supplies ρ=O((um)⁻¹), not the requested radius independent of m. Assigning
the whole logarithm to A(Y)=N₁(Y) would be exact but would cost
e^{μ|A(Y)|} in (1); it does not give uniform connected activities. Equations
(3)–(7) verify normalization and a limited domain, not spatial clustering.

## 3. Correct replacement quotient and the complete failure/reference identity

**PROVEN — exact level-zero alternative.** On the full finite lattice use
the same bare density w_ε and cuts. Write δS=uΣε_p s(U_p) and
δS_Y=uΣ_{p∈P(Y)}ε_p s(U_p). Define

    Z_cut^0(V)=∫Π_Qχ_Q w_0 dHaar>0,
    dν_cut^0=Π_Qχ_Q w_0 dHaar/Z_cut^0,
    t_Y^ε(U,V)=e^{δS_Y(U)} N_Y^ε(η_Y,V)/D_Y^0(η_Y,V).         (8)

The division is by a **source-independent real** positive number. t_Y is
entire in ε on fixed real data. Where the old quotient exists,

    t_Y^ε=e^{δS_Y(U)} (D_Y^ε/D_Y^0)(N_Y^ε/D_Y^ε).             (9)

Both first factors are essential. This is a changed normalization with an
exact compensator, not a proof of zero-freeness of the old quotient.

For completeness Z_cut^0 also has explicit bare prefactor bounds. For a
periodic lattice let E be the number of integrated fine links, P the number
of Wilson plaquettes and C the number of coarse links. The same cap proof
gives

    M_N(δ)^{−E} e^{−2uP−2κuC} ≤ Z_cut^0 ≤ e^{2κuC}.          (10)

On a full torus E=4L⁴|Γ|, P=6L⁴|Γ|, C=4|Γ|, with the usual labelled
positive orientations. On a region use actual counts and require a cap
that satisfies its fixed cuts. No lower bound for an incompatible external
cut is asserted.

Join blocks at periodic sup-distance ≤2 (graph G₂). Distinct bad components
Y have disjoint face-connected collars A(Y)=N₁(Y), |A(Y)|≤81|Y|. Their
I(Y), P(Y) and C(Y) are disjoint and no density factor reads two interiors.
Let h_Y(η_Y,V) be the actual source-independent completion/size selector
(H11–H12), fixed by the frozen collar and unchanged when a component interior
is replaced. Put a_Y=h_Yt_Y and f_Y=(1−h_Y)t_Y. A compatible failure list F
has disjoint collars. G_{ret,F} is the hard-core gas of the a_Y whose collars
avoid A_F=∪_{Y∈F}A(Y). Let Xi_F select exactly that failure list in the original
configuration. Then

    Z_ε[Xi_F]/Z_cut^0
      = E_{ν_cut^0}[e^{−δS} (Π_{Y∈F}f_Y^ε) G_{ret,F}^ε],
    Z_ε/Z_cut^0
      = E_{ν_cut^0}[e^{−δS} Σ_{F compatible}(Π_{Y∈F}f_Y^ε)
                                                G_{ret,F}^ε].     (11)

Proof — PROVEN. Expand Π_Q(χ_Q+ζ_Q)=1. For each fixed bad set B use its
G₂-components. In the all-cut expectation multiply by Π_Yt_Y. The factors
e^{δS_Y} cancel those source terms from e^{−δS}; all remaining source/action
factors read no replaced interior. Fubini on the original good interiors
produces Π_YD_Y^0 and cancels exactly the denominators in (8). The new bad
interior integrals give the original χ/ζ term. Split t=a+f and collect the
failures. Because every selector reads only the unchanged collar, the
classification agrees before and after replacement. This proves (11) for
complex ε on compact Haar domains without taking any logarithm. An arbitrary
additional joint history insertion must stay inside the joint bad-interior
integral of H8; it cannot be factored into local h_Y without a separate proof.
Zero-mass histories contribute zero, with no division by their mass. ∎

The prior history note already proves this identity. Its reconstruction here
is denominator matching, not a new history theorem. Its supported estimate
is G_{ret,F}=exp(Σ_X V_X^F), ||V^F||_μ≤d_q under H20–H24's hypotheses.
It estimates neither f_Y nor the interacting expectation in (11). In
particular the **complete** current unresolved expression is

    E_{ν_cut^0}[ e^{−δS} Σ_F (Π_{Y∈F} f_Y^ε) exp(Σ_X V_X^F) ].    (12)

The sum and expectation remain outside the exponent. Replacing (12) by one
of its pointwise exponential factors would change the denominator.

### 3.1 The effective density and a specified legal history family

**PROVEN — exact construction at every finite depth.** Let E_j be the
level-j link set and Γ_j its L-block graph. Fix a finite chain of such
lattices, the positive numbers u_j, and the Decision-4 kernels K_j with
t_j=κu_j. No assertion about a running-coupling flow is needed for this
identity. Only the original level-zero Wilson coefficients have sources:

    ρ_0^ε(U_0)=exp{−u_0 Σ_{p∈P_0}(1+ε_p)s(U_{0,p})},
    ρ_{j+1}^ε(U_{j+1})=∫ρ_j^ε(U_j)K_j(U_{j+1},U_j)dU_j.     (R1)

Here dU_j is normalized product Haar. Thus (R1) is exactly LARGE55's
effective-density recursion, with its original sources retained. It is
unnormalized: no vacuum factor or partition function has been divided out.

To remove an ambiguity left by the earlier effective-level statements,
fix the following *explicit* iteration of H11–H13. Fix cut thresholds
ε_cut,j, completion thresholds ε_loc,j and integer size thresholds n_j.
These are construction parameters; their useful quantitative values are
not supplied here. Set H_0=∅. A history h through stage j−1 determines
H_j and the active blocks A_j=Γ_j\H_j. Form the bad set
B_j={Q∈A_j:χ_{j,Q}(U_j)=0}, with exactly the interior-plaquette cut of
(2). Form its G₂-components Y. Evaluate the actual completion minimum
e_flat,j on N₁(Y), using the frozen U_j links outside I_j(Y), the straight
anchor paths and U_{j+1} on C_j(Y), as in H11. Set

    a_j(Y)=1{|Y|≤n_j}1{e_flat,j≤ε_loc,j},
    F_j={Y component of B_j:a_j(Y)=0},
    H_{j+1}=N₁(π_j(H_j ∪ ⋃_{Y∈F_j}Y)).                      (R2)

π_j maps block labels to their containing next-level block; N₁ is the
periodic sup-distance collar, intersected with the graph for a box. This
recursion fixes masks from the *recorded* F_j before the next integration.
No cut is imposed on H_j. The masks label holes; their fields are still
integrated or explicitly frozen as boundary variables. We do not use COL
to integrate them to 1 in the presence of readers.

Legal histories are all finite records h=(F_0,…,F_{k−1}) allowed by this
finite decision tree, including records with zero measure. One completely
explicit formula for its transition indicator is

    I_{j,F|h}(U_j,U_{j+1})
      = Σ_{B⊆A_j: F⊆C₂(B)}
          [Π_{Q∈B}ζ_{j,Q} Π_{Q∈A_j\B}χ_{j,Q}]
          [Π_{Y∈F}(1−a_j(Y)) Π_{Y∈C₂(B)\F}a_j(Y)],
    Ξ_h(U_0,…,U_k)=Π_{j<k}I_{j,F_j|h_{<j}}.                 (R3)

The tests use real fields, are measurable, and do not depend on ε. At a
fixed pair of fields exactly one B term and exactly one F survive. Hence
Σ_F I_{j,F|h}=1, even on cut boundaries (equality belongs to ζ for χ's
strict cut, and to success for the completion's weak inequality).
Compatibility and the “no other failures” condition are both enforced by
(R3). Failure reasons are size or completion failure; any additional
selected-chart failure is a further partition in §3.6, never a deletion.

This is a concrete history convention for an exact Decision-4 step, not a
claim that RLARGE's sample-wise σ^J or every earlier unspecified history
rule equals H12. For another specified finite hard history, the identities
below use its actual joint indicator in place of Ξ_h. Its match to (R3)
must be checked before identifying individual history summands. The sum
over histories in either partition is the same density (R1).

Define, rather than assume an effective-action ansatz,

    ρ_{k,h}^ε(U_k)=∫[Π_{j<k}dU_j] Ξ_h ρ_0^ε(U_0)
                                      Π_{j<k}K_j(U_{j+1},U_j). (R4)

Then Σ_hρ_{k,h}^ε=ρ_k^ε, and
ρ_{k+1,(h,F)}^ε=∫ρ_{k,h}^ε(U_k)K_k(V,U_k)I_{k,F|h}(U_k,V)dU_k.
Proof: substitute (R4), append the last indicator and kernel, and apply
Fubini. Summing the partition (R3) recovers (R1). Finite Haar domains,
bounded selectors and bounded kernels justify Fubini on every compact
source set. This proves the algebraic induction for every finite k;
it does not prove LARGE55 (R_m)'s estimates. It also shows exactly where
past failed returns survive: in Ξ_h and its still-integrated chain fields.

### 3.2 The actual local and joint quotient denominators

**PROVEN — matching with an explicit normalization convention.** Define
the bare bookkeeping factor b_k^ε and the entire inherited insertion J by

    b_0^ε=ρ_0^ε,                 b_k^ε=exp(−u_kΣ_p s(U_{k,p})) (k>0),
    J_{k,h}^ε=ρ_{k,h}^ε/b_k^ε.                               (R5)

At k=0 the only h is empty and J=1. At k>0 this equation introduces no
Wilson approximation: b_k^ε J_{k,h}^ε is the actual density (R4).
No logarithm of J is taken. Its zeros, inherited interactions, vacuum
terms, determinants from any earlier exact computation, and joint history
dependence remain in J. If a previously computed representation for ρ
is substituted, it replaces (R4); it is never multiplied by (R4) again.

For B⊆A_k let P_k(B), C_k(B), I_k(B) be exactly (2)'s reader sets. Freeze
η=U_k|_{E_k\I_k(B)} and V=U_{k+1}. Write

    w_{k,B}^ε=b_{k,P_k(B)}^ε Π_{c∈C_k(B)}k_{t_k}(V_c;M_c(U_k)),
    O_{k,B}^ε=b_{k,P_k\P_k(B)}^ε Π_{c∉C_k(B)}k_{t_k}(V_c;M_c(U_k)),
    D_{k,h,B}^ε=∫χ_B w_{k,B}^ε J_{k,h}^ε dU_{k,I_k(B)},
    N_{k,h,B}^ε[Ξ]=∫ζ_B w_{k,B}^ε J_{k,h}^ε Ξ dU_{k,I_k(B)}. (R6)

Here b_{k,P} denotes the plaquette factors of b_k indexed by P. The full
frozen datum is **all η**, not merely N₁(B): J can read arbitrarily far
outside the bare collar. The bare w reads only N₁(B), and each completion
test uses that collar, but no locality of J has been assumed. Holes and
collars are frozen in these local integrals. All lower-level fields in
(R4) remain integrated. Additional joint insertions depending on those
fields go inside (R4) before doing (R6), not at their averaged values.

The full conditional integrand is O_{k,B}^ε w_{k,B}^ε J_{k,h}^ε. O is
independent of the integrated current links: every Wilson and S4′ reader
of such a link was included in P_k(B),C_k(B). Thus the quotient of its
bad and good integrals is exactly N/D wherever D≠0; its full denominator
is O D. Our convention keeps even the occasional independent kernel in
C(B) in both integrals, as (2) does. At k=0 (R6) is precisely (2), not
just a proportional integral. This states every factor by which one
denominator convention differs from the other.

For several separated bad components B=⋃Y, w_{k,B}^ε=Π_Yw_{k,Y}^ε,
but J is still a **single joint insertion**. Consequently D_{k,h,B}
need not equal Π_YD_{k,h,Y}. Neither a product of individual ratios nor a
success-only gas is an identity for an inherited interacting density.
The joint version of (R6) is used when more than one interior is replaced.

### 3.3 Exact replacement of the complete effective-density step

**PROVEN — no history probability is inverted.** Let w_k^0=b_k^0K_k
and use cuts only on the fixed active set A=A_k(h). Define

    C_{k,Y}(η,V)=∫χ_Y w_{k,Y}^0 dU_{I(Y)}>0,
    Z_{k,A}^{cut,0}(V)=∫χ_A w_k^0dU_k>0,
    dν_{k,A}^{cut,0}=χ_A w_k^0dU_k/Z_{k,A}^{cut,0},
    L_{k,h}^ε=ρ_{k,h}^ε/b_k^0,
    (R_{k,B}L)(U_k,V)
      =[Π_{Y∈C₂(B)}C_{k,Y}]⁻¹
         ∫ζ_B(Uhat) [Π_{Y∈C₂(B)}w_{k,Y}^0(Uhat;η,V)]
                  L(Uhat_{I(B)},U_{outside I(B)},V)dUhat_{I(B)}. (R7)

R_{k,∅}L=L. The same cap proof as (3)/(10) bounds the displayed bare
references, with u=u_k, |Y| as shown there, and the actual global counts
for Z. These references contain no inherited indicator. The notation L
may include a current selector or an additional joint insertion; when it
does, retain every lower-level argument inside its original joint integral.

For each h and each current failure record F, the complete identity is

    ρ_{k+1,(h,F)}^ε(V)/Z_{k,A}^{cut,0}(V)
       =E_{ν_{k,A}^{cut,0}} Σ_{B⊆A}
                 R_{k,B}[L_{k,h}^ε I_{k,F|h}],
    ρ_{k+1}^ε(V)=Σ_h Z_{k,A_k(h)}^{cut,0}(V)
                   E_{ν_{k,A_k(h)}^{cut,0}} Σ_{B⊆A_k(h)}R_{k,B}L_{k,h}^ε.
                                                                  (R8)

Proof: fix B, expand χ/ζ on A, and factor w_k^0 into its B readers and
its remaining factors. No remaining factor reads I(B). G₂ separation
makes the C_{k,Y} product the good-interior integral of those readers.
The expression R_{k,B}L no longer depends on the old sea coordinates in
I(B). Their integration against χ_Aw_k^0 therefore produces exactly
Π_YC_{k,Y}, cancelling (R7)'s denominator. The new Uhat integrals give
the original B-bad term with its **joint** inherited density and current
selector. Sum B, then F and h, using (R3)/(R4). This is an actual Fubini
calculation on the effective step, without a clustering assumption. ∎

All zero-mass histories remain zero summands. The real reference in (R7)
is not being equated to D_{k,h,B}. Where the latter is nonzero,

    N_{k,h,B}^ε/(Π_YC_{k,Y})
      =[D_{k,h,B}^ε/(Π_YC_{k,Y})] [N_{k,h,B}^ε/D_{k,h,B}^ε].

For k=0, L=e^{−δS}; extracting its unchanged exterior source factor from
R_B reproduces both compensators in (8)/(9). At higher levels it stays
joint. Equations (R7)/(R8) cannot license dropping D/(ΠC) when studying
STEP55's quotient. The sum over all F is performed in (R8); no f_Y or
sea expectation is replaced by a successful exponential.

For the target reference take

    N^{ref}_{k,h,B}=D_{k,h,B}^0(η,Vbar)                       (R9)

at fixed real η,Vbar **only when it is positive**. The admissible real
fibres and its precise finite bounds are specified in §3.5. The positive
C references make (R8) meaningful even on excluded zero-reference fibres;
they do not prove that (R9) is nonzero there.

### 3.4 A constructed product-Haar connected identity for this denominator

**PROVEN — finite identity, with no input of the form (17).** Open (R4)
inside (R6). Let μ be normalized product Haar in the variables

    x=(U_0,…,U_{k−1}, U_k|_{I_k(B)}),
    W_k^ε=ρ_0^ε(U_0) Π_{j=0}^k K_j(U_{j+1},U_j),
    D_{k,h,B}^ε=(O_{k,B}^ε)⁻¹ E_μ[χ_B Ξ_h W_k^ε].          (R10)

For k=0 the first list is empty except for U_0|_{I(B)}. Frozen η and V
are parameters. Every earlier normalizer N_{t_j}(M) is still in W.
In particular this is the original chain, not an assumed interacting
effective action or a single-background integral.

Here is a finite algorithm producing its connected coefficients. Assign
each free link coordinate and each original external/source coordinate
to a fixed containing current block (choose the lexicographically first
one when necessary). Group free coordinates by owner v, so μ=⊗_vμ_v.
Include all blocks physically touched by a reader, not merely its chosen
owner. For every factor choose a deterministic connected hull of these
blocks in Γ_k; never contract an inactive component. Frozen vertices may
carry point-mass measures. Disconnected reader sets are connected by the
first spanning-tree connector in a fixed finite ordering. Such connectors
are bookkeeping, not decay estimates.

Use the following actual finite factor list:

* e^{−u_0(1+ε_p)s(U_{0,p})}, one per original plaquette;
* k_{t_j}(U_{j+1,c};M_c(U_j)), one per j≤k and coarse link c;
* χ_{k,Q}, one per Q∈B;
* I_{j,F_j|h_{<j}}, one per j<k, with the explicit finite formula (R3).

For an additional joint history, include its actual indicator as an
additional factor with its full read support. Factors that are constant
in the free coordinates still retain their external/source supports.
A purely numerical factor can be assigned any fixed vertex. Empty
lattices/integrations use the scalar formula directly. Set b_i=F_i−1
and denote the nonempty connected support of F_i by S_i. For each
nonempty connected *set of distinct factor labels* C in the overlap graph
(i∼j iff S_i∩S_j≠∅), define

    w_{k,h,B}(X)=Σ_{C connected: ⋃_{i∈C}S_i=X}
                         ∫Π_{i∈C} b_i dμ_X,
    D_{k,h,B}^ε=(O_{k,B}^ε)⁻¹
          Σ_{G a family of disjoint nonempty X} Π_{X∈G}w_{k,h,B}(X).
                                                                  (R11)

The empty G contributes 1. Every sum in (R11) is finite. To prove it,
expand Π_iF_i=Σ_{C⊆labels}Π_{i∈C}b_i. Split each selected set into the
connected components of its support-overlap graph. Distinct components
read disjoint free coordinates, so their integrals factor under μ.
Conversely a disjoint collection of such components uniquely determines
the selected set. Group by support X. This proves (R11), including all
signs, multiplicities and overlapping-history correlations. It applies
to the actual numerator by replacing χ_Q with ζ_Q and retaining its
additional insertion. It applies to each summand of (R8) as well. ∎

This gives a product-reference identity and explicit connected activities
for the entire denominator, without assuming an exponential or taking a
logarithm. All original source labels survive. A history indicator may
have graph-wide support: (R11) charges that support in full. Its atoms
and reference may be large, and the finite gas can vanish. Therefore
(R11) is **not** the smallness hypothesis of CX-R and cannot be used as
if (19) had already been proved for it. It removes an identity ambiguity;
it does not remove the needed analytic estimates.

### 3.5 What can actually be bounded on this identity

**PROVEN — finite-depth references and holomorphy.** On real frozen data
write

    γ_{k,h,B}(η)=E_μ[χ_B Ξ_h],
    T_k=Σ_{j≤k}t_j|E_{j+1}|,    P_0=number of original plaquettes.

Ξ_h reads U_0,…,U_k, but not the new V=U_{k+1}. Thus γ is independent
of V. Positivity of the actual elementary factors and (4) give exactly

    γ e^{−2u_0P_0−2T_k}/O_{k,B}^0
        ≤ D_{k,h,B}^0 ≤ γ e^{2T_k}/O_{k,B}^0.               (R12)

In particular the admissible real fibres for (R9) are precisely γ>0;
when γ=0 the whole selected integral is identically zero in ε. A legal
history need not have positive mass on every frozen fibre. Such fibres
cannot be included in a theorem claiming a nonzero history denominator.
(R8) still includes them without division. No uniform lower bound on γ
over the useful history/collar class has been proved here.

For fixed real η and a fixed history label, D is entire in all original
ε. It is also holomorphic in the *new* coarse V∈SL(N,C)^{E_{k+1}}:
replace each last kernel numerator by

    exp{−t_k[1−(tr(V_c⁻¹M_c)+tr(M_c*V_c))/(2N)]}.

M_c is a function of real integrated/frozen U_k, so M_c* is fixed when
V varies. N_{t_k}(M_c)>0 is unchanged; matrix inversion is polynomial
on SL(N,C). All these factors are bounded uniformly in x on compact
complex parameter sets, and the hard indicators are independent of these
parameters. Termwise power-series integration proves holomorphy. O has
a specified nowhere-zero continuation by the same formula and the
exponential plaquette factors. This also proves holomorphy of (R11)'s
coefficients on that domain. It does not continue η or a coarse field
*through* a hard selector depending on it. In particular the selected
output ρ_{k+1,(h,F)} need not be holomorphic in V across its own F cuts.

There is an explicit but nonuniform zero-free germ on a positive fibre.
Set Dhat=O D and V_c=Vbar_c exp Z_c, Z_c∈sl(N,C). Relative to the
positive probability proportional to χ_B Ξ_h W_k^0 at Vbar,

    Dhat(ε,V)/Dhat(0,Vbar)=E exp H,
    |H|≤r:=2u_0Σ_p|ε_p|+t_kΣ_c(e^{||Z_c||op}−1).           (R13)

For the last inequality use ||M_c||≤1,
||e^{±Z_c}−1||≤e^{||Z_c||}−1 and |tr A|≤N||A||. If r<π/2,
Re E exp H≥e^{−r}cos r>0 and |E exp H|≤e^r. Divide by the explicit
nonzero O ratio to obtain the bound for D. The half-plane logarithm has
|Log E exp H|≤2r−log cos r. This proves an actual all-finite-depth germ,
with every history retained. The source count, top-link count and γ in
(R12) are visible; none provides the uniform product-domain norm requested
in B2. Entire integrals may have zeros outside this germ.

### 3.6 Charts and contours: a complete disjoint sector identity

**PROVEN — no selected sector is substituted for the full integral.**
Fix any ordered finite list Ω_1,…,Ω_m of measurable real chart/white-cut
tests on the lifted variables of (R10), including tests for earlier
levels if those coordinates are changed. A test that cannot be evaluated
outside its prerequisite chart is defined to fail there. Set

    q_0=Π_{i=1}^m1_{Ω_i},
    q_l=(Π_{i<l}1_{Ω_i})(1−1_{Ω_l})  (1≤l≤m),
    D_l=O⁻¹ E_μ[q_l χ_B Ξ_h W_k^ε].
    D=D_0+Σ_{l=1}^m D_l.                                   (R14)

Indeed the first failed test is unique, or all tests pass. This proves
Σq_l=1 pointwise, including intersections of several failures. Each D_l
has (R11)'s finite construction with the additional displayed indicator
factors. Thus all outside-chart and white-cut failures are assigned a
term, even if their support is the whole graph and no estimate is known.
For the Haar construction (R10) there is no contour deformation at all.

On a selected real chart the tree/Haar calculation of §4 applies, with
J from (R5) retained inside the exact pulled-back insertion; any earlier
field integrations remain inside it. A complex contour change must be
justified on that sector with its actual insertion and fixed-domain
continuation. If it is valid and D_0^{new} is its new-contour integral,
retain the oriented term E_side=D_0−D_0^{new}; then
D=D_0^{new}+E_side+Σ_lD_l. This is the complete matching identity, not
a bound or a claim that a nonholomorphic hard history can be deformed.
The uncharted proof of (R10)/(R11) needs no such deformation hypothesis.

## 4. All Gaussian, gauge and reference factors, and the exact remainder

**PROVEN at the specified bare real chart — change of variables.** This
section identifies precisely what a CX-R calculation would have to match.
Use a field-independent rooted forest preserving all coarse anchors and
fixed collar endpoints. Leaf-by-leaf Haar invariance gives unit nonlinear
gauge Jacobian and unit gauge volume. A non-gauge-invariant history is
averaged over the tree variables; retain the resulting Θ_h rather than
setting it to one. Let n be the number of remaining free links, d=(N²−1)n.
In an injective real exponential chart Z=e^a b,

    dHaar(Z_e)=c_N j(a_e) da_e,
    j(a)=det_su(N)[(1−e^{−ad_a})/ad_a],   j(0)=1.

c_N is the normalized Haar density at zero in an orthonormal Lie basis,
one factor per free link. To obtain j, differentiate the exponential series:
left translation of its differential to the identity sends b to
∫₀¹e^{−s ad_a}b ds. Taking its determinant gives the displayed j; Haar
volume is left invariant and fixes the remaining constant c_N. In the
chosen small real chart this determinant is positive, with j(0)=1.
First fix one exact action/insertion allocation: the actual integrand is
e^{−S_eff} times its retained insertion and cut. S_eff is smooth and
invariant under the allowed tree transformations. For (R6) one valid
choice is S_eff=−log w_{k,B}^ε, with **all** J_{k,h}^ε in the insertion.
The logarithm of each kernel is its explicit exponent minus log N_t.
If a smooth inherited factor is instead allocated to S_eff, remove that
same factor from the insertion. Nothing is counted twice; a zero or
non-invariant history factor is not logged and remains in the tree
average. The actual kernel normalizers always occur exactly once.
Choose a real symmetric positive definite Q, set
σ²=N/u, C=Q^{−1/2}, and define **without deleting a term**

    S_0=S_eff(b),   ell=∂_aS_eff(e^a b)|_0,
    R_Q(a)=S_eff(e^a b)−S_0−ell^T a−a^TQa/(2σ²),
    U(W)=ell^TσCW+R_Q(σCW)−Σ_e log j((σCW)_e).              (13)

A quadratic mismatch stays in R_Q. ell vanishes only at a critical point
of the **exact** action. Put a=σCW and take a fixed product Gaussian cut
χ_p(W) whose entire image lies in the injective chart with j>0. Θ_h retains
the pulled-back original cut and the full remaining insertion, including
J when using the choice just specified. The selected real sector
has exactly

    D_h^sel = P_h e^{−S_0} det(Q)^{−1/2} N_χ
                                  E_{μ_p}[Θ_h e^{−U}],
    P_h=Z_ref,h^{−1} c_N^n(2πσ²)^{d/2},
    N_χ=γ_d(χ_p),      μ_p=χ_p γ_d/N_χ.                     (14)

The determinant follows from the real Jacobian σ^d det C. Multiplying
the normalized Gaussian by (2π)^{d/2} proves all constants and signs in
(14). For a product of link cuts μ_p is a product over links, not necessarily
over individual colour coordinates. A nonlocal slice map needs its actual
Jacobian instead; (14) uses the exact tree coordinates just described.

**PROVEN — additive remainder identity.** If the intended denominator is
D_h, let Ω be precisely this selected real sector. With its actual original
history indicator in both terms,

    D_h=D_h^sel+E_h^comp,     E_h^comp=Z_ref,h^{−1}∫_{Ω^c}Xi_h w.  (15)

If contour deformation replaces D_h^sel by another contour integral
D_h^new, retain its oriented side E_h^side=D_h^sel−D_h^new. Then
D_h=D_h^new+E_h^side+E_h^comp. This is an exact accounting identity; no
bound for either error is asserted. A moving hard cutoff has no automatic
holomorphic continuation in complex coarse fields. Fixed-source sectors of
the continuation note are supported examples, but not identities for all h.

**PROVEN conditional identity, OPEN instantiation.** Once an actual
exponential representation for the reduced expectation is independently
proved, the full logarithmic variation is

    Δlog D_h^sel = Δlog P_h−ΔS_0−½Δlogdet Q
                          +Δlog N_χ+Δlog E_{μ_p}[Θ_h e^{−U}]. (16)

Only a small reduced cluster term can have an O(h) budget. At U=0 the
main-term and determinant variations remain. Moreover (16) says nothing
about D_h until (15)'s complements are controlled. Even a scalar bound
|E_comp/D_sel|<1 would not by itself give spatially local logarithmic
activities. A total-volume small-error estimate is not presumed here.

### 4.1 Direct product-cut Haar route: exact identity, insufficient weak-coupling bound

**PROVEN — another exact bare identity.** A product reference for (2) can
also be obtained without a Gaussian change of variables. Since χ_Q reads
only I(Q), let

    c_Q=∫χ_Q dHaar(U_{I(Q)}),
    dμ_Q^cut=χ_Q dHaar(U_{I(Q)})/c_Q,
    P_Y^cut=Π_{Q∈Y}c_Q,
    U_Y^Haar=uΣ_{p∈P(Y)}(1+ε_p)s(U_p)
                                  −Σ_{c∈C(Y)}log k_t(V_c;M_c).

For real external data k_t>0; the logarithm here is its real logarithm,
independent of ε. The exact identity is

    D_Y^ε=P_Y^cut E_{⊗_{Q∈Y}μ_Q^cut} exp(−U_Y^Haar),
    M_N(δ)^{−n_l|Y|}≤P_Y^cut≤1.                             (17a)

This includes the entire original cut-good domain, hence every configuration
that would be outside an additional Gaussian/chart sector. No contour side,
Haar density or determinant is missing: no such change of variables has
been made. With frozen vertices as point masses, this is a product reference
on the ambient block graph and is a genuine bare instance of the *identity*
part of (17), with no defect insertions. It does not identify an inherited
history-conditioned effective density.

Proof and attempted estimate — PROVEN. The cut product factors across
disjoint I(Q), giving (17a) directly. The cap argument proves the prefactor
bound. Label each plaquette term by its at most four touched blocks, a
face-connected set; label a soft kernel by its adjacent endpoint blocks.
Every source and link read is retained. At most 24L⁴ plaquettes have a
vertex in a given block (four vertices per plaquette, six positive planes
per site). At most eight coarse kernels meet a block. By (4), on
|ε_p|≤ρ and with β≥0 these local vertices obey the sufficient estimate

    ||U_Y^Haar||_β
       ≤48u(1+ρ)L⁴ e^{4β}+16κu e^{2β}.                      (17b)

Thus the exact product identity alone does not produce CX-R's smallness
in the intended weak-coupling regime u=1/g² large: the bound supplied by
this direct route grows with u. This is a failure of this sufficient
estimate, not a lower bound or an impossibility theorem. A background,
Gaussian or more adapted interacting reference is needed to improve the
estimate within this route. No small-u result is substituted for STEP55's
weak-coupling consumer, and no active fixed-radius or tail calculation is
undertaken here.

## 5. Library entry: local failed-return insertions inside CX-R

This gives a non-circular sufficient *input* criterion for a complete
denominator. It does not assume its logarithm or zero-freeness. It extends
CX-R's elementary argument to an explicitly retained defect gas.

**PROVEN — conditional mixed expansion.** Let μ=⊗_{v∈Γ}μ_v be a fixed
product probability measure, allowing point masses at frozen vertices.
Let U_S(W_S,z_S) and d_a(W_{S_a},z_{S_a}) be bounded measurable functions of
W, holomorphic in the original z on a product domain D containing 0. All labels S,S_a
are nonempty connected sets carrying every coordinate read. Families are
finite at fixed Γ; absolutely summable grouped families follow by limits.
Different defect labels may share a support but are then incompatible.
Defect compatibility is disjointness of S_a. Suppose the **actual** integral
has independently been put in the form

    D(z)=P(z) Z(z),
    Z(z)=E_μ[ exp(−Σ_S U_S) Σ_{F compatible}Π_{a∈F} d_a ],   (17)

including F=∅ and all failures. P has a specified holomorphic logarithm.
Set β=μ_0+2, μ_0≥0, f_S=e^{−U_S}−1, and assume

    q = sup_v [Σ_{S∋v}e^{β|S|}||f_S||∞
                   +Σ_{a:S_a∋v}e^{β|S_a|}||d_a||∞] ≤ 1/4. (18)

Then explicitly constructed connected original-source-local F_X satisfy

    Z=exp(Σ_XF_X),             ||F||_{μ_0}≤q,
    e^{−q|Γ|}≤|Z|≤e^{q|Γ|}.                                 (19)

All are holomorphic on D, with the bounds uniform over any family with
the **same** input constants. A sufficient (18) is e^h h+δ_f≤1/4, where
||U||_β≤h and the defect contribution in (18) is ≤δ_f.

Proof, step 1 — PROVEN, exact first regrouping. Expand Π_S(1+f_S), keeping
the finite compatible-defect sum. In a selected mixed collection, join two
atoms when their full supports intersect. Its connected components have
disjoint coordinate sets; product measure makes their integrals factor.
Consequently Z is exactly a hard-core gas of connected unions X. Its activity
w(X) is the sum of integrals of connected mixed collections with union X,
respecting defect compatibility internally. Nothing is discarded. Let
v_i=e^{(μ_0+1)|S_i|}||b_i||∞ for each atom b_i=f_S or d_a. Dropping the
internal compatibility restriction increases the nonnegative majorant.

Proof, step 2 — PROVEN, first tree bound. A connected collection with a
chosen root has a spanning tree. Allow repeated atom labels to enlarge its
sum. The rooted tree series is bounded by iteration from zero of

    T_i=v_i exp(Σ_{j:S_j∩S_i≠∅} T_j).

The coefficients count unordered children, equivalently labelled trees with
factor 1/(n−1)!. The function v_i e^{|S_i|} is a supersolution because
Σ_{j:S_j∩S_i≠∅}v_j e^{|S_j|}≤q|S_i|≤|S_i|. Marking an atom whose support
contains v and using the product bound for the union weight yields

    sup_v Σ_{X∋v}e^{(μ_0+1)|X|}||w(X)||∞≤q.                  (20)

Each originally distinct collection is counted at least once; allowing
repetitions, many roots and many spanning trees only enlarges the bound.

Proof, step 3 — PROVEN, logarithmic graph bound. For an ordered tuple
X₁,…,X_n, define φ^T as the alternating sum over connected spanning
subgraphs of its overlap graph, with φ^T=1 for n=1. Order the graph's
edges. Kruskal's algorithm partitions connected subgraphs into intervals
[τ,R(τ)] indexed by spanning trees: an extra edge can be present exactly
when it is later than every edge along its tree path. The alternating sum
on an interval is (−1)^{n−1}(1−1)^{|R(τ)\τ|}, of modulus ≤1. Thus |φ^T|
is at most the number of spanning trees. Apply the preceding rooted-tree
bound using (20) and define

    F_X=Σ_{n≥1}(1/n!)Σ_{∪_i X_i=X}φ^T(X₁,…,X_n)Π_i w(X_i). (21)

Marking a polymer containing a specified vertex cancels n in n! and gives
||F||_{μ_0}≤q. Repeated polymers are included in (21). Connected unions
carry every source read. The absolute locally uniform bound proves
holomorphy. Multiply every original atom f_S,d_a by a common complex t.
For |t|≤2 the first input bound is ≤2q≤1/2, so both tree expansions still
converge. Near t=0 the finite connected-graph identity gives Z(t)=expΣF_X(t).
The identity theorem reaches t=1. This constructs the exponential before
concluding nonvanishing. Summing the rooted bound over vertices gives the
modulus bounds in (19). ∎

**PROVEN — full factors and reference comparison.** If
log P=p_const+Σ_Xp_X with ||p||_{μ_0}≤p_* and fixed p_const, then on the
same domain

    D(z)=D(0) exp{Σ_X[p_X(z)−p_X(0)+F_X(z)−F_X(0)]},
    ||K||_{μ_0}≤2p_*+2q.                                    (22)

An explicitly bounded P and (19) bound D(0); (3) is a separate actual-model
bound when D is the bare denominator. The two-point full log variation is
≤2(p_*+q)|Γ|. The reduced log variation alone is ≤2q|Γ|. A global
source-dependent p_const must instead remain as a separate displayed factor;
it cannot be hidden in (22)'s constant reference.

If two instances have the same μ and identical atom functions/lists off a
set A, their coefficients in (21) agree for X∩A=∅. Subtraction gives a
reduced reference log cost ≤2q|A| when both norms are ≤q. The prefactor
cost is separate. For decoupling across a region O this is a boundary
estimate only if the removed/changed atoms all cross the boundary and all
other atoms/measures coincide; each connected changed cluster then meets
the inner vertex boundary of O. Mere nonvanishing does not imply this
matching, and the boundary activities remain functions of the boundary
fields inside a subsequent integral.

**PROVEN identity; OPEN smallness.** The actual producer (R10)/(R11)
is now constructed. It is a product-Haar finite connected gas with its
actual history factors; no assertion that it satisfies (18) is made.
The pointwise successful gas in (12) is still insufficient, and its
interacting sea cannot be declared a product measure. For any hard
indicator Θ attaining zero, ||Θ−1||∞=1. On a nonempty support this
alone exceeds (18)'s budget. The following different bound uses integrated
failure masses and proves the expansion to which such a bound applies.

### 5.1 Hard cuts as connected failure types with an integrated majorant

**PROVEN — exact hard-cut expansion.** Let θ_i=1−1_{E_i} be a finite
list of actual zero/one requirements on a product probability space μ,
with fixed connected full read supports S_i. The E_i can overlap. Join
labels when their supports intersect. For each nonempty connected set C
of distinct labels introduce a failure type with

    S_C=⋃_{i∈C}S_i,       d_C=(−1)^{|C|}1_{⋂_{i∈C}E_i}.

Two such types are compatible exactly when their supports are disjoint.
Expanding Π_i(1−1_{E_i}) and taking the support-overlap components of
each chosen label set proves the pointwise identity

    Π_i θ_i=Σ_{F compatible}Π_{C∈F}d_C.                     (R15)

Every subset occurs exactly once, including the empty subset. In
particular all simultaneous failures are present; overlapping events are
one type, not falsely independent types. Multiplying by exp(−ΣU_S) and
integrating proves (17) for this specified cut, without a sup-norm
smallness assertion. For (R10) one may take the θ list to be its χ_Q
and the actual I_{j,F_j|h}; (R3) proves these are zero/one functions.
For a refined history term one may instead use its individual χ, ζ,
a and 1−a requirements. A “failure event” here means failure of that
particular required predicate, not necessarily physical large curvature.
For a required rare-history event its complement can have large mass.
The Θ in (R15) must not be replaced by a different smoother cutoff.

**PROVEN — an L¹ version of the mixed bound.** In (17) keep disjoint
defect supports and define

    δ_a=sup_{z∈D} ∫|d_a(W_{S_a},z)|dμ_{S_a},
    q₁=sup_v[Σ_{S∋v}e^{(μ_0+2)|S|}||e^{−U_S}−1||∞
                         +Σ_{a:S_a∋v}e^{(μ_0+2)|S_a|}δ_a]. (R16)

Assume d_a is pointwise holomorphic in z, with an integrable envelope on
each compact subdomain; assume the analogous hypotheses for U. For a
finite family, q₁≤1/4 implies exactly (19)–(22) with q₁ in place of q.
For the source-independent hard events in (R15), δ_C is the actual joint
event probability μ(⋂_{i∈C}E_i), not ||d_C||∞. The event must be fixed
in the analytic parameters; a moving real coarse-field indicator gives
no coarse-field holomorphy by this statement.

Proof: for a selected collection of interaction atoms f_i and compatible
defects, take absolute values, bound each f_i by its supremum, and use
disjointness of the defect coordinate supports to obtain

    |E_μ[Π_i f_i Π_{a∈F}d_a]|
           ≤Π_i||f_i||∞ · Π_{a∈F}δ_a.                     (R17)

Interaction atoms can overlap defects; no conditional independence of
those atoms was asserted. Removing them by a supremum is what permits
the last factorization. Apply this bound to each connected collection.
The first tree proof in §5 now uses v_i=e^{(μ_0+1)|S_i|} times either
||f_i||∞ or δ_i. Compatibility is dropped only **after** (R17) has
been used on the actual compatible collections. The same supersolution
gives (20), with q₁. The second tree proof and its t-continuation then
give (19)/(21). Integrable envelopes justify parameter integration, and
the absolute rooted bounds justify the logarithmic series. Prefactor and
reference subtraction give (22) unchanged. ∎

This proves a way for a small integrated failure mass to enter a cluster
estimate without the false sup-norm inference. It does not prove q₁≤1/4
for (R10). The unadapted Haar interactions already have the large-u
problem of (17b), and (R15)'s **joint** failure masses and multiplicities
need bounds, especially for large history supports. The TC input must
supply these masses under the very reference used in the expansion;
an estimate under another interacting conditional law is not (R16).
Contour-side terms require their actual complex measures/densities and
total-variation bounds; they are not indicator events in (R15).

## 6. Nested holes: apply R10 without losing the inactive contribution

**PROVEN conditional use of brief-authorized, reviewed LIB1 R10.** Start with the original
connected F_X (or K_X) on Γ, and fix Λ⊆Ω⊆Γ independently of sources. For
X meeting Λ enlarge it by the inactive components of Γ\Λ at distance ≤1:

    R_Λ(X)=X ∪ ⋃{H component of Γ\Λ:dist(H,X)≤1},
    K'_Y=Σ_{X:R_Λ(X)=Y, X∩Λ≠∅}K_X,
    K_inactive=Σ_{X:X∩Λ=∅}K_X.                               (23)

For input supports in LIB1's P_Ω, R10 gives exactly

    Σ_XK_X=K_inactive+Σ_YK'_Y,
    ||K'||_{μ;Λ,act}≤||K||_{μ;Ω,act}≤||K||_μ.                (24)

The first application may take Ω=Γ; later nested applications use the
already saturated supports. Source locality and analyticity are preserved
because X⊆R_Λ(X). The inactive term stays **inside** any remaining
integration or failure sum. It may depend on sources and is not a constant
normalization. Applying (24) inside each fixed-F summand of (12) is exact
but does not bound the expectation or the failure sum.

For arbitrary holes (24) is an active-root, active-size norm. If a consumer
requires the full saturated-support norm, LIB1 additionally requires every
hole component to have at most M blocks and supplies

    ||K'||_μ≤9M ||K||_{(1+8M)μ}.                              (25)

Retaining the inactive family as well costs at most (1+9M) times that
stronger input norm. Without that size/rate input, retain unsaturated
physical labels for (1), and the separate active norm for saturated labels.
No conversion uniform in unbounded M is claimed. For Λ=∅ the whole exponent
is inactive; for Λ=Γ there is no change. These identities carry every
prefactor from (14), (17) or (22) unchanged.

## 7. Inputs consumed

| Input | Exact scope consumed | Status and missing output |
|---|---|---|
| Decision-4 soft kernel; LARGE55 recursion; RLARGE §3; history return H1–H14 | Original chain, cut-good quotient, fixed reference and explicit H12 history extension | Rebuilt through all finite effective levels in (R1)–(R14). The history convention is specified rather than equated to unspecified σ^J. No main/audit status is assigned. |
| LIB1 R10 and its norm-control correction/reviews | (23)–(25), with original-source supports, inactive term, fixed masks and bounded-hole condition where needed | Brief-authorized, reviewed input; no new origin/main landing claim. No returned-denominator bound is attributed to it. |
| RECOVERY_CLUSTER_ASTRA and its review | Connected-support product-measure mechanism with all original sources, complete factors, β≥0 | Generic conditional theorem supported by its review. §5 rebuilds the mechanism including local defects. The actual-integral identity remains an input to that theorem. |
| SOURCE_LOCAL_RETURN and fixed-reference CONTINUATION | Exact tree/Haar factors, fixed-source sector, linear term, determinant and complement interfaces | Used at their stated bare/chart scope in §4. No arbitrary-history or full-domain assertion imported. |
| SOURCE_LOCAL_HISTORY_RETURN H20–H25 and its review | When its displayed q/d_q smallness holds, successful gas has ∥V^F∥_μ≤d_q on D_(ρ,λ)(u) | Only the successful pointwise gas in (12). Its failure and sea factors remain present. |
| **Active fixed-source-radius lane — named input FR** | A common original-source disc sup_p abs(ε_p)<ρ_* (and any separately required coarse tube), fixed-domain identities and original-source support atoms for all substituted maps; a localized source-interaction budget h_src at weight β | Requested form, **not received/consumed as proved**. A finite source germ or a bound requiring ρ_*p(u)²→0 does not supply this form. |
| **Active finite-coupling remainder lane — named input KR** | Exact action allocation S_0, ell, Q, Haar/normalizer terms, inherited weights; local h_rem and prefactor norm p_* on FR's domain, with real u and the actual kernel held fixed | Requested form, **not received/consumed as proved**. A kernel remainder is useful but does not identify the full return indicator or its reference. |
| **Original-law tails / active graded-complement lane — named input TC** | Uniform bounds for the actual connected joint-event masses δ_C and multiplicities in (R15)/(R16), under the chosen reference, plus complex side-term total variation and reference ratios | Requested form, **not received/consumed as proved**. (R15)–(R17) construct the hard-event expansion and its sufficient integrated bound; changing the underlying law requires a proved density comparison. |

HANDOFF now records scoped reviews for the fixed-source, single-kernel and
coercivity constructions, and active selected-core and graded-complement
authors. Those status reports are not assumed to meet the stronger
interfaces above; their derivations are not duplicated in this lane.
FR, KR and TC need not be independent. No independence or near-closure count
is inferred from three names. Their work is not duplicated here. A physical
axiom, empirical fit or new primitive supplies none of the missing bounds.

## 8. Consumers

| Consumer | What is now explicit | Open use condition |
|---|---|---|
| CX / corrected CX-R | Actual product-Haar identity (R10)/(R11), exact hard-event expansion (R15), and sufficient integrated criterion (R16) | Prove smallness/local prefactor budgets for this representation, or match an adapted Gaussian representation with every sector included. Its Gaussian (ID) is not inferred from an arbitrary finite gas. |
| STEP55 §5.4 and S9 | (R6) identifies local and joint N/D; full conditional denominator is O D. (R14) retains every chart sector. (14)/(16) retain every Gaussian factor on a selected chart | Uniform admissible-history positive reference, complex zero-free domain, full norm, and normalized numerator estimates. Fixed real-fibre holomorphy (R13) alone is insufficient. |
| HANDOFF remaining proof path, step 2 | (R8) performs the complete failure/history sum as an identity; (R4) proves the exact density recursion. LIB1 R10 retains inactive terms | Estimates through the remaining expectation, reference comparison and quantitative induction remain OPEN. |
| CODEX_REVIEW_STEP R11 and item 6 | Finite actual denominator, source/coarse holomorphy and nonuniform germ are now explicit; all full-vs-reduced factors remain | Uniform zero-freeness is OPEN. No O(card(Y) H_V) estimate is assigned to the full unnormalized prefactor. |

## 9. Open residue and next decision

**PROVEN, identity deliverable.** Equations (R1)–(R14) construct the actual
effective density, legal histories, original variables/collars, cuts,
joint denominator and reference, and give a finite connected expansion
covering every term. This is an exact algebraic RG rewriting. It is not
the analytic RG theorem. The choice of histories in (R2)/(R3) is explicit;
matching a different specified σ^J convention requires replacing its joint
indicator, not declaring it equal to this one.

The prefactors can now be matched without relying on a logarithm:

| Factor/operation | In the actual Haar construction | In a selected current-field chart |
|---|---|---|
| Frozen normalization | Full conditional denominator is O_{k,B}D_{k,h,B}; (R10) divides by the explicit O once | Apply (14) to D as defined in (R6); multiply by O only if the full conditional convention is used |
| Earlier density and histories | Original lower-level chain and Ξ_h in (R10) | J from (R5) remains inside the pulled-back/tree-averaged insertion; an exact alternative expression replaces J, not multiplies it |
| Haar/gauge volume | Normalized product Haar, gauge variables unremoved | c_N^n and unit tree-gauge volume under §4's stated boundary-preserving forest |
| Gaussian scale and Hessian | None introduced | (2πσ²)^{d/2} det Q^{−1/2}, with σ²=N/u_k; actual slice Jacobian required for another slice |
| Main action and linear term | Original factors in W; b_k is cancelled by (R5) | e^{−S_0}; ell and every quadratic mismatch stay in U unless an exact critical-point argument removes ell |
| Cut mass | χ_B is an actual factor, not a deleted domain | N_χ and the remaining actual pulled-back cut/history insertion both remain |
| Outside-sector/contour terms | Already integrated in (R10) | Σ_lD_l and any oriented E_side in (R14) are added |
| Source-independent reference | D(0,η,Vbar) on γ>0; otherwise no target division | Divide every sector by that same reference if using D/Nref; §4's Z_ref is 1 for unnormalized D |

In particular, writing A for all the selected-chart prefactors and Z_sel
for its exact reduced expectation, the full quotient is

    r=N/[A Z_sel+E],       E=Σ_lD_l+E_side.                  (R18)

Only when the indicated factors are nonzero and compatible logarithms
exist may one write log D=log A+log Z_sel+Log(1+E/(A Z_sel)).
The last term needs its own locality estimate. Setting it to zero, or
calling all of log A an O(H_V) remainder, would repeat R11's defect.
Corrected CX-R (ID)/(FULL)/(VAR) can be used for the full D only after
that reduction and its estimates have actually been established.

**OPEN — precise B2 sub-lemmas.** (i) A useful history/collar class with
a quantitative lower bound for γ and the full reference (R12), on a
source/coarse domain independent of volume, depth and hole size.
(ii) Original-source-local bounds for every prefactor and inherited
interaction in an adapted reference representation. (iii) Bounds on
the connected joint failure masses/multiplicities in (R16), on that
same reference and domain, plus complex side-term total variation.
The elementary Haar majorant (17b) grows with u; (R13)'s germ shrinks
with the number of readers. Neither is the missing estimate. The L¹
theorem (R15)–(R17) fixes the hard-cut sup-norm error but does not certify
these actual-model budgets. FR/KR/TC are requested with the exact forms
in §7; no active coordinator result is silently used.

**OPEN — precise B3 sub-lemmas.** (i) Control the reference ratio after
the remaining integrals and the whole sum (R8), retaining its
history-dependent Z_{k,A}^{cut,0}. A pointwise fixed-F comparison cannot
be pulled through that expression without this proof. (ii) Establish
the full original-source norm for the produced coefficients through the
hole operation, using (25)'s hypotheses or a proved alternative; the
active norm (24) is insufficient. (iii) Show that the output of this
step satisfies the same analytic/reference/activity hypotheses at the
next effective level. (R4)'s exact algebraic induction proves none of
these norm statements. Their literal match to the consumer's Gaussian
representation and normalized numerator remains OPEN.

**ARGUED, next decision.** Use (R10)/(R14) as the immutable integration
target while choosing an adapted reference. The next useful input is
a local joint-failure/reference estimate satisfying (R16), paired with
the selected-core interaction budget on the same domain. A global
history atom in (R11) cannot simply be relabelled as a small local atom.
No impossibility, exhausted-route, mass-gap or retained-status claim is
made. B1's exact construction is separate from B2/B3's remaining estimates.

```yaml
actual_current_surface_status: open
target_claim_type: positive_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact finite effective-history denominator and complete connected identity, with a proved integrated hard-cut criterion; uniform analytic/history/scale bounds remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
