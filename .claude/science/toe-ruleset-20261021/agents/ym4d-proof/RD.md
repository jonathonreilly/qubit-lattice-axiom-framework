# RD — the actual returned denominator and a complete-factor completion criterion

**Theorem RD at the requested history/scale/volume-uniform scope: OPEN.**
This note proves the bare denominator identification, explicit positive
reference bounds, a finite-region complex-source estimate, and a conditional
cluster theorem that retains local failed-return insertions. It does not
identify the full history-dependent Haar integral with that theorem's product
reference representation. In particular, it does not turn the confirmed CX-R
implication into an actual all-history RG step.

Author source: `9658cc870d82401001e56b29f351aec5f5f58fa1`.
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

**OPEN — target statement.** For every admissible one-step return region Y,
history h, and fixed hole/collar geometry, identify the actual quotient
denominator D_{k,h,Y}(z) and its reference. On a common product domain in the
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
its inherited interactions and every failed-return contribution. Replacing
it by the bare Wilson action, an empty history, a single chart or a pointwise
successful gas changes the theorem. The explicit bare realization and the
completion criterion below keep these distinctions.

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
Let S_eff include the actual kernel normalizers and every gauge-invariant
inherited term if present; a non-invariant insertion remains in the tree
average. Choose a real symmetric positive definite Q, set
σ²=N/u, C=Q^{−1/2}, and define **without deleting a term**

    S_0=S_eff(b),   ell=∂_aS_eff(e^a b)|_0,
    R_Q(a)=S_eff(e^a b)−S_0−ell^T a−a^TQa/(2σ²),
    U(W)=ell^TσCW+R_Q(σCW)−Σ_e log j((σCW)_e).              (13)

A quadratic mismatch stays in R_Q. ell vanishes only at a critical point
of the **exact** action. Put a=σCW and take a fixed product Gaussian cut
χ_p(W) whose entire image lies in the injective chart with j>0. Θ_h retains
the pulled-back original cut and history insertion. The selected real sector
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

**ARGUED — application route; OPEN — actual producer.** Equation (17) is
a useful destination for (12) or (15), with all errors represented by d_a.
Neither equation is already (17): ν_cut^0 is interacting, and arbitrary
chart complements/contour sides need not be bounded local functions of the
chosen product variables. Constructing that representation is this lane's
undischarged obligation. Inserting Θ_h into d=Θ_h−1 does not prove (18).
A real tail probability bound alone is not the sup-norm/locality bound in
(18). A measure-valued defect expansion or another cluster method is a live
alternative, not certified by this lemma.

## 6. Nested holes: apply R10 without losing the inactive contribution

**PROVEN conditional use of landed LIB1 R10.** Start with the original
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
| Decision-4 soft kernel; RLARGE §3; history return H1–H14 | The original Haar weight, cuts, frozen links, D_Y^ε, and compensated zero-source replacement | Rebuilt in §§2–3 at bare level zero. The source references are candidate-lane evidence; no main/audit status is assigned. |
| LIB1 R10 and its norm-control correction/reviews | (23)–(25), with original-source supports, inactive term, fixed masks and bounded-hole condition where needed | Consumed as landed under the explicit brief. No returned-denominator bound is attributed to it. |
| RECOVERY_CLUSTER_ASTRA and its review | Connected-support product-measure mechanism with all original sources, complete factors, β≥0 | Generic conditional theorem supported by its review. §5 rebuilds the mechanism including local defects. The actual-integral identity remains an input to that theorem. |
| SOURCE_LOCAL_RETURN and fixed-reference CONTINUATION | Exact tree/Haar factors, fixed-source sector, linear term, determinant and complement interfaces | Used at their stated bare/chart scope in §4. No arbitrary-history or full-domain assertion imported. |
| SOURCE_LOCAL_HISTORY_RETURN H20–H25 and its review | When its displayed q/d_q smallness holds, successful gas has ∥V^F∥_μ≤d_q on D_(ρ,λ)(u) | Only the successful pointwise gas in (12). Its failure and sea factors remain present. |
| **Active fixed-source-radius lane — named input FR** | A common original-source disc sup_p abs(ε_p)<ρ_* (and any separately required coarse tube), fixed-domain identities and original-source support atoms for all substituted maps; a localized source-interaction budget h_src at weight β | Requested form, **not received/consumed as proved**. A finite source germ or a bound requiring ρ_*p(u)²→0 does not supply this form. |
| **Active finite-coupling remainder lane — named input KR** | Exact action allocation S_0, ell, Q, Haar/normalizer terms, inherited weights; local h_rem and prefactor norm p_* on FR's domain, with real u and the actual kernel held fixed | Requested form, **not received/consumed as proved**. A kernel remainder is useful but does not identify the full return indicator or its reference. |
| **Active original-law coercivity/tails lane — named input TC** | For the actual defects once constructed, a uniform localized majorant δ_f for (18), or a specified replacement bound for a measure-valued cluster argument, including reference ratios and failure-label multiplicity | Requested form, **not received/consumed as proved**. An unnormalized energy estimate or an integrated real tail bound is not silently upgraded to this stronger input. RD still owns construction/matching of the defect representation. |

FR, KR and TC need not be independent. No independence or near-closure count
is inferred from three names. Their work is not duplicated here. A physical
axiom, empirical fit or new primitive supplies none of the missing bounds.

## 8. Consumers

| Consumer | What is now explicit | Open use condition |
|---|---|---|
| CX / corrected CX-R | (17)–(21) give a sufficient cluster criterion including local failed-return insertions; supports include actual original source reads | Derive (17) for the complete returned integral and verify (18), rather than assume its exponential. |
| STEP55 §5.4 and S9 | Bare D_Y^ε is (2); its positive reference is (3); (14) and (16) retain gauge/Haar, main, linear, determinant and cut factors; (15) retains the rest | All required histories, coarse complex tube, inherited density, region-uniform source domain and normalized numerator estimates. |
| HANDOFF remaining proof path, step 2 | Exact reference/failure identity (11)–(12), plus R10's inactive and active bookkeeping (23)–(25) | Control the interacting sea/failure expression and match it through the actual next RG level. |
| CODEX_REVIEW_STEP R11 and item 6 | Full vs reduced logarithms are separated. A finite actual-integral domain (6) is proved; the generic complete-factor implication is rebuilt with defects | The uniform actual-denominator assertion is still OPEN. The refuted O(card(Y) H_V) bound for the full unnormalized prefactor is not reinstated. |

## 9. Open residue and next decision

**OPEN, primary obligation.** For the exact effective-level conditional
density and legal history/collar family, construct a product-reference
identity of the form (17), or a different independently proved linked
expansion, that includes all of (12)/(15) and supplies original-source
support bounds. The present data do not give this identity and its norm.
The fixed-source-reference alternative removes complex division in local
activities but leaves the interacting source expectation to be controlled.

**OPEN, quantitative and domain obligations.** Establish the common source
radius, complex coarse-field continuation when required, nonzero/bounded
actual reference factors, and uniform failed-return bounds. Close the
effective-action/history induction rather than reuse a bare theorem at
higher levels. If saturated full supports are required, also supply (25)'s
geometry/rate hypothesis or a different proved norm interface.

**ARGUED, next construction.** Use the exact fixed zero-source reference to
avoid complex local quotient poles; build a connected expansion for its sea
and failed-return insertions. Test its *local* failure majorants against
TC before attempting an extensive logarithm. Keep the fixed-chart CX-R
route as a separate option, retaining its complements and original support
atoms. The tested elementary phase-sector route closes only (6).

The stronger condition (17)–(18) is a sufficient construction problem; RD
does not imply that such bounded defect functions exist. The alternative
“prove that (12) already has the desired local analytic logarithm” is
target-equivalent and would merely restate the main obligation. Neither is
counted as a discharged lemma. No impossibility, exhaustion of all routes,
mass gap, full RG step or retained scientific status is claimed.

```yaml
actual_current_surface_status: open
target_claim_type: positive_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact bare denominator/reference matching and a proved conditional defect-cluster criterion; complete history/scale-uniform instantiation remains open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
