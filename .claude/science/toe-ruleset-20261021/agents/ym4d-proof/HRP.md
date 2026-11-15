# H_RP: author theorem packet

## PRE-STATED — 2026-10-29

This section contains target statements only. It records no successful result.

1. On a finite periodic hypercubic lattice with even extent in the reflected
   direction, the SU(N) Wilson measure with reflection-symmetric nonnegative
   plaquette couplings is reflection positive for link and site reflections,
   including both periodic reflection planes, on the appropriate closed-half
   observable algebra. The domain of gauge-invariant versus general observables
   and the treatment of boundary links are part of the statement to establish.
2. A normalized conditional soft-RG chain has the Wilson measure as its bare
   marginal. Reflection-covariant, bare-link local observable polynomials with
   positive-half support therefore satisfy the same inequality. Changes of
   measure, observable normalization and coupling trajectories must be identified.
3. On a common convergent sequence, finite polynomial RP forms pass to the limit.
   Extension beyond the determining test algebra consumes explicit continuity
   and extension hypotheses; it does not establish H_reg or (EXT).
4. Each coordinate reflection of SPHERE55's actual doubled digital-ball prism
   regulator is to be proved RP, or refuted by an explicit cell-level witness.
   A regulator repair, if needed, must identify every disturbed hypothesis.
5. Coordinate great-sphere RP, with separately supplied local rotational
   covariance and convergence, is the RP input to N1S. Equatorial RP alone is
   not a substitute for that input.
6. The finite checks specified in checks/hrp_criteria.md test the algebra only.
   A failed negative control is to be reported, not replaced silently.
7. This is an author packet for later independent review, not a banked result,
   an audit verdict, a complete Yang–Mills existence proof or a mass-gap proof.

## 1. Scope, conventions and source boundary

**Status convention.** PROVEN below means a written author proof from the
displayed mathematical hypotheses. It does not mean independently reviewed or
banked. ARGUED denotes a proposal without a completed proof. OPEN denotes an
undischarged input. The finite Wilson regulator is supplied; no derivation of
it from the framework's physical axioms is claimed.

The exact sources are pinned in `checks/hrp_sources_initial.json`, with main
at `ca2bc7ddf64790da96cd43d42017d000fbfe4808`. The target arrows are
ASSEMBLY55 §3 N1F/N1S, §4 N3 and §7 F3/F25. The old L9a entry is actually
at PROOF lines 4929ff in this revision, not near line 1016 (which contains
the S4′/S4″ definitions). CODEX_REVIEW_HINT's bare-marginal result is in
§5, under `Lemma BARE`, rather than its §4 arithmetic discussion.

Let G=SU(N), N≥2, and assign one variable U_e to each positively oriented
geometric lattice edge, with U_{e^{-1}}=U_e^{-1}. Distinct periodic edges
remain distinct even when an extent is 2. Haar measures are normalized.
For an oriented plaquette p set

    s(U_p)=1−Re Tr(U_p)/N,
    dμ=Z⁻¹ exp(−Σ_p β_p s(U_p)) Π_e dU_e.

Here all β_p are finite real numbers, and Z is finite and strictly positive
because the graph is finite, G compact, and the density continuous and
strictly positive. An orientation reversal or a change of starting vertex
does not change s. Reflection r acts on directed edges geometrically;
ρU has link (ρU)_e=U_{r(e)}, using the inverse for reversed traversal.
The antilinear observable reflection is

    ΘF(U)=overline{F(ρU)},       Q_μ(F,G)=μ((ΘF)G).

The half-algebra consists of all bounded complex measurable functions of
edges geometrically contained in the specified closed positive half.
An edge crossing a link-reflection plane is not in that half-algebra.
For site reflection, links lying in a fixed plane ARE included. Support
means geometric edge support, not just the set of endpoint names; this
distinction matters on the extent-2 periodic multigraph. Bounded observables
already include every finite-cutoff polynomial used here. Under the theorem's
reflection-invariant measure the conclusion extends to L² half-observables:
truncate F radially in magnitude, and use ordinary Cauchy–Schwarz and
||F∘ρ||₂=||F||₂ to pass the reflected form to the L² limit.

For TEST functions use a different symbol: Rf(x_1,…,x_n)=f(rx_1,…,rx_n)
is linear, while f^*(x_1,…,x_n)=overline{f(x_n,…,x_1)} includes conjugation.
OSLEAF55 writes Θf^* for what is written R(f^*) here. In particular the
observable ΘA_F is antilinear in F, and equals A_{R(F^*)}; conjugation
must occur exactly once.

## 2. Positive kernels and an exact substitute for temporal gauge

### 2.1 Wilson kernel — PROVEN

For c≥0 and A,B∈SU(N),

    K_c(B,A)=exp(c Re Tr(BA†))
      = Σ_{r,s} (c/2)^{|r|+|s|}/(r!s!)
          φ_{r,s}(B) overline{φ_{r,s}(A)},
    φ_{r,s}(A)=Π_{i,j} A_{ij}^{r_ij} overline{A_ij}^{s_ij}.

Expand each scalar exponential in
Re Tr(BA†)=½Σ_ij(B_ij overline{A_ij}+overline{B_ij}A_ij).
Every coefficient is nonnegative. Since |A_ij|,|B_ij|≤1, the sum of the
absolute values is at most exp(cN²); hence the series converges uniformly
and absolutely. For any finite family A_l and coefficients z_l its
quadratic form is a sum of nonnegative multiples of
|Σ_l z_l overline{φ_{r,s}(A_l)}|². Finite products of such kernels have
the same property by multiplying their feature expansions. The same
uniform bound permits termwise integration against bounded functions and
finite measures. This proves the integrated statement, not merely
pointwise positivity of the Boltzmann weight.

An independent algebraic route re-verifies the June 5 main note's sign
step. For a finite-dimensional unitary representation R,

    exp(c Re χ_R(g))
      = Σ_{n≥0}(c/2)^n/n! χ_{(R⊕R̄)^{⊗n}}(g)
      = Σ_λ [Σ_n(c/2)^n M_{λ,n}/n!] χ_λ(g).

An invariant subspace has invariant orthogonal complement by unitarity,
so each finite tensor power splits into irreducibles with integer
multiplicities M_{λ,n}≥0. Its dimension is (2 dim R)^n, which bounds the
sum of absolute character terms. The resulting majorant is exp(c dim R).
Finally χ_λ(BA†)=Σ_ij D^λ_ij(B) overline{D^λ_ij(A)}. This gives a second
positive feature expansion with all interchanges justified. Taking R
fundamental and c=β_p/N gives exactly the same Wilson kernel. No external
reflection-positivity theorem is used in either argument.

### 2.2 Splitting crossing links — PROVEN

Suppose a reflection exchanges two disjoint vertex halves and reverses
each crossing edge separately. Orient each crossing edge from its negative
endpoint to its positive endpoint and call its variable C_v. Introduce
two independent Haar variables h_{v,−},h_{v,+}, one from each endpoint to
an auxiliary midpoint, and substitute

    C_v=h_{v,−} h_{v,+}^{−1}.

This substitution pushes product Haar measure to Haar measure exactly:
for fixed h_{v,+}, right invariance gives
∫f(h_{v,−}h_{v,+}^{−1})dh_{v,−}=∫f(C_v)dC_v; then integrate h_{v,+}.
Apply independently to every crossing edge, even if several edges meet
at a vertex. Reflection exchanges h_{v,+} and h_{v,−}, and therefore
inverts C_v as required. An observable of original positive-half edges
does not depend on the auxiliary negative-half variables. Thus the OS
form of the original model equals the form of this enlarged product-Haar
model on the lifted observable.

For a crossing square, let U_- and U_+ denote its tangential edges, with
the same orientation under reflection. Its boundary word, based on the
negative side, is

    U_- C_w U_+^{-1} C_v^{-1}.

After the substitution, cyclicity of trace rewrites its trace as Tr(BA†),
where

    B=h_{v,−}^{−1} U_- h_{w,−},
    A=h_{v,+}^{−1} U_+ h_{w,+},       B=ρA.

This is the needed positive-half factorization. Before splitting or gauge
fixing, writing the raw plaquette as Wρ(W)^{-1} with W depending only on
the original positive links would omit the crossing links. The auxiliary
variables remedy that omission without imposing any holonomy condition.

If every interaction is either within one half or such a crossing square,
and the same-half actions are reflected copies, the enlarged density is

    h(X_+)h(X_-) · Π_{p crossing} e^{-β_p} K_{β_p/N}(B_p,A_p),

where h is real and positive and X_± include the corresponding auxiliary
half-links. Insert §2.1 and integrate the two independent halves. For
every bounded half-observable F,

    Z Q_μ(F,F)=e^{-Σ_cross β_p} Σ_α d_α
       |∫ F(X)h(X) overline{Φ_α(X)}dX|² ≥0.

All sums are absolutely integrable. This proves RP for ALL bounded
half-observables, including non-gauge-invariant ones, whenever the
crossing β_p≥0. Same-half coefficients need only be real and paired.
It also proves every finite reflected Gram matrix PSD by applying the
formula to Σ_i z_i F_i. This is a general finite-graph lemma, not a
global temporal-gauge assertion.

### 2.3 Gauge-averaging comparison — PROVEN

For disjoint vertex halves, average F over gauge transformations at all
positive vertices, obtaining P_+F. These transformations do not change
ΘF, which depends only on negative-half edges. Gauge invariance of μ
therefore gives μ((ΘF)F)=μ((ΘF)P_+F). Now average independently over
negative-vertex transformations to obtain

    μ((ΘF)F)=μ((ΘP_+F)P_+F).

A gauge-invariant F is fixed by P_+. On a torus of time extent at least
4 the crossing links of both link planes form a matching: each boundary
vertex has exactly one such link. A gauge transformation at each positive
endpoint, equal to its negative-to-positive crossing link C_v, sets that
link to identity, with the negative endpoint fixed. For fixed C all
other changes are left/right Haar translations. This verifies the
older gauge-invariant proof on the periodic torus. It fixes ONLY the
crossing links, not every temporal link. Temporal Polyakov holonomy
remains in the unfixed links. At extent 2 that matching argument is
unavailable, but §2.2 still applies. Neither proof restricts to trivial
Polyakov holonomy. Gauge averaging here is unnecessary for the stronger
§2.2 theorem and is not asserted for shared site-boundary vertices.

## 3. H_RP-flat: the complete finite-torus theorem

### 3.1 Link reflection, including the wrap plane — PROVEN

Let Λ=(Z/2mZ)×Π_{i=1}^{d−1}(Z/L_iZ), d≥2, m≥1, L_i≥2, with the usual
periodic cubical cells and distinct oriented edge labels. Set
r_l(t,x)=(1−t,x). The fixed geometric planes are t=½ and t=m+½.
The positive vertex layers are t=1,…,m. The crossing temporal edges
are precisely those based at t=0 and t=m. Their negative-to-positive
orientations are opposite at the two planes. The positive-half temporal
edges have bases 1,…,m−1; the negative-half ones have bases m+1,…,2m−1.

Every purely spatial plaquette lies in a single vertex layer. A temporal
plaquette based at t lies entirely in a half unless t=0 or m. At either
exception it is a crossing square of §2.2, is reflected to itself up to
boundary orientation, and has one tangential edge on each side. Reflection
maps a temporal base t to −t modulo 2m and a spatial layer t to 1−t.
These observations exhaust every plaquette, including the wrap family;
none is deleted. They remain true when m=1 using the geometric cells.

Assume β_{r_l p}=β_p and β_p≥0 for crossing plaquettes. Pair the
same-half terms, with arbitrary paired finite real coefficients. Apply
§2.2 at BOTH cuts at once. It gives

    μ((Θ_l F)F)≥0 for every bounded measurable F in the closed-half algebra.

In particular, β_p≥0 for every plaquette is sufficient; strict positivity
is unnecessary, and β_p=0 contributes the constant kernel 1. The sign
is used only in the expansion of the crossing exponential, not in Haar
invariance, normalization, or the same-half factors. Position dependence
is unrestricted apart from reflection pairing and these sign conditions.

### 3.2 Site reflection and its two boundary slices — PROVEN

Set r_s(t,x)=(−t,x), with fixed site planes t=0,m and closed positive
half the geometric arc 0≤t≤m. Let W be all spatial links inside BOTH
fixed planes. Reflection fixes each such directed link pointwise; it
does not act on W by group inversion. Let X_+ and X_- be the remaining
edge variables in the two respective halves. Each elementary plaquette
is either entirely on a fixed plane or in one closed half. None has
points in both open halves. This is the nearest-neighbor cell property;
it is not a claim about arbitrary extended-loop actions.

For paired real couplings, write

    S=S_0(W)+S_+(X_+,W)+S_+(ρX_-,W).

S_0 contains each fixed-plane plaquette once. Conditioning on W and
reflecting the negative variables gives exactly

    Z Q_μ(F,F)=∫ e^{-S_0(W)}
       |∫ F(X_+,W)e^{-S_+(X_+,W)}dX_+|² dW ≥0.

This includes all bounded complex measurable F depending on W and X_+,
without gauge invariance. Both fixed planes are integrated, so there is
no discarded periodic boundary term. Here even the nonnegativity of
β_p is unnecessary: all finite real reflection-symmetric Wilson
coefficients give a positive fixed-plane weight and the displayed square.
At extent 2 classify temporal edges by the arc they traverse, not merely
their endpoint pair. The same formula holds. A negative-coupling test
on a site-contained plaquette is consequently not a general RP control.

### 3.3 Mixed reflection comparison — PROVEN, auxiliary

On an odd temporal circle 2m+1≥3, r(t)=−t has one site plane t=0 and
one link plane t=m+½. Condition on the spatial links at t=0 as in §3.2,
split the crossing links at the other plane as in §2.2, and expand only
those crossing kernels. The result is an integral over W of sums of
nonnegative squares. This re-verifies PROOF L9a-m for paired real
same-half couplings and nonnegative crossing coefficients. N1F's current
even-volume sequence does not consume this auxiliary result.

## 4. Transfer to the actual soft chain

### 4.1 The zero-source bare marginal — PROVEN

PROOF `Decision 4: the RG kernel` (lines 2051ff), RLARGE §0 `The exact
chain`, ROTDEF §5.1, and SPHERE55 §1.6 specify

    W_ch(U_0,…,U_K)=exp(−S_0(U_0)) Π_{j<K} K_j(U_{j+1}|U_j),
    K_j(V|U)=Π_c exp{−κu_j[1−Re Tr(V_c^{-1}M̄_c(U))/N]}/N_j(M̄_c(U)),

where N_j(M) is the integral of that same numerator over V_c. Each
normalizer is finite and strictly positive for real finite parameters;
M̄ is a finite mean of unitary path transporters, so ||M̄||≤1. Integrate
U_K, U_{K−1}, …, U_1, using ∫K_j(V|U)dV=1 pointwise. Tonelli applies
to the positive density, and bounded observables are integrable. Thus

    ∫W_ch Π_{j≥1}dU_j=exp(−S_0(U_0)),
    Z_ch=Z_Wilson,       E_ch[A(U_0)]=μ_Wilson(A).

This independently proves the exact assertion identified as `Lemma BARE`
in CODEX_REVIEW_HINT §5. No RP assertion about the full joint law, the
coarse marginal, or a conditional law at fixed U_K is needed or inferred.
The kernel parameters may be selected by a fixed-point/flow construction;
for every finite selected set of real parameters the identity is unchanged.

### 4.2 Which operations change the measure — PROVEN identities; scope OPEN

| Operation on disk | Effect relevant to RP |
|---|---|
| S4′ order-averaged contours; S4″ measurable block map (PROOF §1) | Changes a deterministic observable map or the center of a normalized auxiliary kernel. It does not reweight U_0. Block observables still require their own half-support check. |
| Division by N_j(M̄(U)) | Essential to ∫K_j=1. Although it depends on U, it cancels after integrating the complete normalized kernel. Dropping it WOULD reweight the bare measure. |
| Multiplicative Z(a)>0 and real additive centering of e_a | Changes observable values, not μ. Reflection covariance persists if the deterministic normalizations/centering are reflection-paired. |
| Changing the chosen real bare coupling with a,R | Changes μ to another Wilson measure. §§3.1–3.2 apply separately at each cutoff if the stated signs/symmetry hold. No uniform lower β bound is required. |
| Sphere profile β_Q=2N/G(aΩ(z_Q))² | Changes the homogeneous bare model to a position-dependent Wilson model. §5 verifies the needed pairing; equivalence to a flat Wilson trajectory is not proved. |
| Nonzero e-source η, SRCAN55 §2.1 | DOES reweight the bare measure: u_0(p)=u_0−h_η(p), h_η(p)=½Σ_{x∈corners(p)}η(x). Complex or asymmetric η need not define an RP measure. The proof applies at η=0, or at a separately verified real symmetric nonnegative shifted profile. |
| Conditioning on a coarse field or selecting one defect/history event (RLARGE §0) | Generally changes the bare law. The full sum/integral over histories restores the original law; positivity of an individual conditioned contribution is not asserted. |

The source identity follows by multiplying W_ch by
exp(Σ_x a⁴η(x)e_a(x)) and collecting the plaquette coefficient. SRCAN55
keeps the kernels and their normalizations fixed during that tilt.
Computing derivatives at zero source does not require RP at complex
sources. A non-Wilson residual action, omitted history, extra terminal
coarse weight, or conditioning cannot be smuggled into the above marginal
identity. No such extra factor occurs in the cited zero-source definition.
This checks those definitions, not every historical approximation in the
7202-line PROOF file.

PROOF's original β_W=2N/g_std² and RLARGE's convention u=1/g_lane²=β_W
use different coupling names. The RP theorem is stated in terms of the
actual coefficient of s(U_p), avoiding a normalization identification.
OSLEAF55 §6 TR-1 makes R/a even and TR-6 conditionally selects a real
positive g_bare; existence and compatibility of that trajectory remain
OPEN inputs and are not consequences of this theorem.

### 4.3 Bare-link locality and positive-half polynomials — PROVEN

ROTDEF §2.2 defines the clover energy e_a(x) as a finite real sum of
Wilson plaquette energies, with all its links in the coordinate-distance-a
neighborhood of x. Its clover set is permuted by a coordinate reflection,
so e_a(ρU,x)=e_a(U,rx). A real reflection-paired centering c_a(x) and
nonzero real paired normalization Z_a(x) give the same identity for
ê_a(x)=(e_a(x)−c_a(x))/Z_a(x). In particular c_a(x)=μ(e_a(x)) is paired
because the action and Haar measure are reflection invariant.

If the support of a test function lies more than a from BOTH boundaries
of the chosen positive arc, its lattice sum Σ_x v_a(x)f(x)ê_a(x) is
positive-half measurable, for real reflected volume weights v_a.
At a site plane the closed-half algebra also permits tangential links
on the plane; distance ≥a suffices for the clover stencil. For a fixed
compact positive-time test with min t=δ>0, and an exhausting torus, these
conditions hold eventually: a<δ and the distant periodic plane is beyond
the entire support and stencil. Products and finite linear combinations
of such observables are still bounded half-observables at each finite
cutoff, even though their bounds may grow with a^{-1}.

For OSLEAF55 D8's finite-sequence map A_F, each multi-test has compact
support with every insertion at strictly positive time. The same stencil
argument puts A_F in the half-algebra. Reflection commutes exactly with
the lattice summation. Consequently

    Σ_{n,m} S^{a,R}_{n+m}(R(F_n^*)⊗F_m)
       = μ_Wilson((ΘA_F)A_F) = E_ch[(ΘA_F)A_F] ≥0.

The reversed order in F_n^* merely permutes commuting lattice factors;
complex conjugation is retained. This identity uses bare links, not the
auxiliary soft variables. Fixed positive-time gradient flow is not a
strictly supported observable and is not covered by this support proof.

## 5. Coordinate-reflection RP for SPHERE55's actual K_a

### 5.1 Cell automorphism and weights — PROVEN

Use SPHERE55 §§1.2–1.4 verbatim: vertices a(Z⁴+(½,½,½,½)); D_a is the
union of closed cubes centered at ak and contained in B_R. The cube
criterion is Σ_ν a²(|k_ν|+½)²≤R². It is invariant under every coordinate
sign change. Thus θ_μ sends cubes of D_a to cubes, and sends a boundary
3-face (one incident 4-cube) to a boundary 3-face. Acting simultaneously
on both charts and trivially on the collar coordinate gives an
automorphism of

    K_a=D_a ∪ (∂D_a×[0,1]) ∪ θ_eq D_a.

Its cells are the chart cubes, their copies, and c×[0,1] for boundary
3-faces c. The action is a sum over their 2-faces with

    β̂_p=¼Σ_{Q⊃p}β_Q,       β_Q=2N/G(aΩ(z_Q))²,
    Ω(z)=2R²/(R²+|z|²).

Assume the prescribed G is defined, real, finite and nonzero at these
finitely many local spacings. Then β_Q>0. More generally arbitrary
nonnegative β_Q with β_{θ_μQ}=β_Q suffice. The center z_Q of a chart cube
or of the base c of a prism reflects to θ_μ z_Q. Radial Ω therefore gives
β_{θ_μQ}=β_Q, and reindexing the incidence sum gives
β̂_{θ_μp}=β̂_p≥0. The formula `(β/4)k_e` in SPHERE55 §2 is a shorthand
valid for constant cell coupling. For its actual nonconstant profile the
sum above is the correct formula; sign and reflection symmetry follow
without any bound on k_e or any uniform seam-to-bulk ratio.

Independent link Haar measure is invariant because θ_μ permutes edge
variables and may invert them; compact-group Haar is invariant under
inversion. The Wilson DENSITY is reflection invariant but is not a
product density. The product assumption applies to the reference Haar
measure, not to μ_Wilson.

### 5.2 Exhaustive crossing-cell classification — PROVEN

No vertex has x_μ=0. A chart cube meets both open halves only if its
μ interval is [−a/2,a/2], and is then invariant under θ_μ. A boundary
3-face meeting both halves must have μ as a free coordinate with that
same interval, so it too is invariant. The corresponding prism is
invariant. This verifies the crossing condition also for 4-cells, but
holonomies in this action belong to 2-faces, which are classified next.

Every 2-face is one of the following; duplicate incidences are already
combined in β̂_p.

1. A chart square, including a square on ∂D_a. It crosses x_μ=0 only
   when μ is one of its two directions and its μ interval is centered
   at zero. It is then individually θ_μ-invariant, with two chart
   crossing edges and one tangential edge in each half, exactly §2.2.
2. A seam square e×[0,1], for a boundary edge e=(v,w). The seam links
   C_v=(v,θ_eq v) preserve chart coordinates. They therefore lie wholly
   in one μ half and never cross x_μ=0. This square crosses only if e
   is a μ edge from v_μ=−a/2 to w_μ=+a/2, so w=θ_μv. It is individually
   invariant. Its two crossing edges are e in the south chart and its
   north-chart copy; its two tangential edges are C_v and C_w.

For case 2 write B_s for the south link v→w and B_n for its north-chart
copy. The exact boundary word is

    B_s C_w B_n^{-1} C_v^{-1}.

Splitting B_s=h_{s,−}h_{s,+}^{−1} and
B_n=h_{n,−}h_{n,+}^{−1} rewrites its real trace as Re Tr(W_+W_-†), with

    W_+=h_{s,+}^{−1} C_w h_{n,+},
    W_-=h_{s,−}^{−1} C_v h_{n,−}=ρW_+.

This explicitly supplies the previously compressed prism step, including
the noncommutative order. Alternatively the chart crossing links form a
matching: each vertex on x_μ=±a/2 has at most one μ edge to the opposite
layer; the two charts have distinct vertices. They can be set to identity
for gauge-invariant F exactly as in §2.3. The displayed boundary word
then becomes C_w C_v^{-1}. No seam edge is inadvertently gauge-fixed as
a crossing edge. In both approaches the weight is β̂_p≥0 and all
remaining plaquettes pair within their halves.

Thus all the geometric, coefficient and measure conditions in the brief
are satisfied.
There is no exceptional crossing prism and no regulator change is
needed. The argument does not need the digital-ball topology proof,
Moise's theorem, a smooth triangulation, seam transparency, or the
numerically observed range of incidence counts.

### 5.3 Sphere theorem and N1S's precise input — PROVEN conditionally

Apply §2.2 to §5.1–§5.2. For every μ=1,…,4 and every bounded measurable
function of K_a's links contained in {x_μ≥0},

    μ_{K_a}((Θ_μF)F)≥0.

This includes gauge-invariant observables and proves the claimed finite
RP directly for SPHERE55's position-dependent regulator. Normalized
soft kernels leave that bare measure unchanged by §4.1. For local
observables in the south cap, eventually far from the seam, the clover
support and covariance argument in §4.3 applies. For other observable
maps the explicitly required condition is local half-support and
reflection covariance, not just gauge invariance.

Under stereographic embedding, x_μ=0 is X_μ=0, a great sphere through
S and N. In z=2x coordinates near S, θ_μ is exactly z_μ↦−z_μ at every
R. Pass first a→0 at fixed R using §6. Once the continuum sphere
functional is separately proved SO(4)_S-invariant on the relevant cap
test domain, every great sphere through S is a conjugate of one of
these coordinate reflections by SO(4)_S. Rotate the positive-half test,
apply coordinate RP, and rotate back using invariance: this proves RP
for all those great spheres on that domain. It uses invariance of the
state, not averaging over rotated states and not mere covariance of
the observable map.

Now let R→∞ on the common family and use §6 again. RP for planes through
the origin is inherited. The separate N1S contraction/H_Euc input
supplies translations; conjugating by a translation gives RP for every
affine hyperplane. No equatorial RP or transport of an observable across
the equator enters this chain. Local SO(5) invariance, all-order Ward
control, U-sep/U-mom, and the diagonal construction remain supplied
conditions, not outputs of the finite RP theorem. No finite-cutoff
SO(5) symmetry is claimed or restored; the regulator's exact symmetry
remains H(4)×⟨θ_eq⟩. Since no regulator change is made, there is no new
disturbance of SPHERE55 §5.2's conditional cap-contraction hypotheses.

## 6. Limit passage in the two actual observable formulations

### 6.1 Literal N1F polynomial contract — PROVEN implication

Fix the common continuum algebra and its positive-half polynomial P,
and suppose its lattice approximants P_j obey §4.3 eventually. Assume
the ONE subsequence selected by H_reg has convergent expectations of
all the finitely many products in (ΘP_j)P_j, with the limit equal to
the intended continuum products. Then

    ω((ΘP)P)=lim_j μ_j((ΘP_j)P_j)≥0.

No subsequence depending on P is extracted. Every fixed P is treated
on the already selected common sequence. If the determining family
does not explicitly include these pairings, H_reg must supply uniform
equicontinuity and density sufficient to extend convergence to them.
It is not enough to know convergence of one-field means or weak
convergence without control of unbounded products. Neither clustering,
uniqueness, an infrared gap nor all-order factorial constants enter
this finite-sum inference. Those may be needed for other inputs.

With an approximate observable map one instead needs, for this fixed P,
an error bound Q_j(P_j)≥−ε_j(P), ε_j(P)→0, or a vanishing difference
from the exact form in the same moment topology. The same limit proves
RP. For the local clover/site-reflection choice the errors are exactly
zero eventually. A link plane can also be placed at the fixed continuum
plane by shifting the lattice origin; if one instead keeps a plane at
a_j/2 and compares with θ:t↦−t, uniform test-function equicontinuity
is an additional consumed hypothesis for that vanishing translation.

### 6.2 OSLEAF55's restricted OS domain — PROVEN implication

This is a different domain, not an unconditional replacement of the
literal polynomial contract. Write

    D_{+,n}=C_c^∞({0<t_1<…<t_n}),
    S_{+,n}={F∈S(R^{4n}):F=0 off {0<t_1<…<t_n}},
    ^0S_n={F∈S(R^{4n}): all derivatives vanish on coincidences}.

Use finite sequences F=(F_n) and the star/conjugation convention of
OSLEAF55 D3, with R the LINEAR test reflection defined in §1.
For F_n,G_m∈D_+, R(F_n^*)⊗G_m has compact support off all
coincidences: the negative and positive time tuples are separated, and
times within each tuple are strictly ordered. Thus the identity at the
end of §4.3 pairs only separated Schwinger distributions.

Consume from H_reg-sep/(EXT) the following precise facts, without
proving their Yang–Mills estimates here:

1. Along the common sequence, S_n^{(j)} converges on every compact
   off-diagonal test needed in these pairings, for every finite n.
2. The limits extend continuously to ^0S_n in the inherited Schwartz
   topology, with the compatible normalizations and support maps.
   Uniform seminorm bounds and convergence on a determining family
   are a sufficient way to deliver 1–2. The shrinking-separation
   estimates named (EXT)/(SP_λ) are proposed producers, not assumed
   proved merely by being named.

For compact ordered F, there are only finitely many n,m, so exact
lattice RP passes to Σ_nm S_{n+m}(R(F_n^*)⊗F_m)≥0. To pass to all S_+
requires only a deterministic density argument plus fact 2. A smooth
function zero on the complement of the open time-ordering cone is
flat on its boundary. Cut it off at large |x|, then multiply by smooth
cutoffs zero for t_1≤ε or t_{i+1}−t_i≤ε and equal to one when each gap
is ≥2ε. Each derivative of the cutoff is O(ε^{-k}), while Taylor's
formula and boundary flatness bound the affected derivatives of F by
O(ε^M) for arbitrary M on the compact set. Choosing M>k proves
Schwartz convergence after first controlling the tails. Hence D_+ is
dense in S_+. The tensor/reflection map is continuous in Schwartz
seminorms (Leibniz and (1+|x|²+|y|²)≤(1+|x|²)(1+|y|²)), and its
range is flat on coincidences. Continuity of S therefore passes RP
to every finite sequence in the restricted positive space.

These steps re-prove the RP portion of OSLEAF55 Lemma RP-lat with
geometric half-edge support, CLOSURE-sep(d), and the RP part of CONTRACT-sep.
The original endpoint-only RP-lat wording is false at temporal extent two;
OSLEAF55 now distinguishes its two geometric arcs, as in §1 here. This
finite-domain correction does not supply any continuum convergence input.
These steps do not verify
that file's reconstruction theorem, quantitative EXT proof, growth
constants, or owner choice of algebra. In particular e(f)² generally
is NOT an element of this restricted domain: f⊗f need not be flat at
same-half coincidences. Restricted convergence cannot establish
ordinary polynomial moment convergence by relabeling it. Thus N1F's
literal algebra choice/F2a and N1S's U-mom versus U-sep formulation
remain explicit upstream issues even after the finite H_RP leaf closes.

### 6.3 Iterated sphere limit and diagonal — PROVEN implication

At fixed R the same finite-sum/density proof works for K_a and θ_μ,
with cap test pullbacks and reflection-paired volume weights. The
necessary regularity constants may depend on R at this first stage.
For the second limit use N1S's supplied radius-uniform continuity and
convergence on the SAME local test algebra to pass each RP form as
R→∞. Angular conjugation and affine-plane transport are exactly as
in §5.3. A diagonal a_j(R_j),R_j sequence is usable only when the
separately supplied diagonal lemma ensures convergence of all these
finitely many pairings for every member of the common determining
family. RP itself costs no new uniform error estimate because its
finite-cutoff inequality is exact. This does not supply the diagonal
lemma or control the symmetry defects along that diagonal.

## 7. Inputs consumed and import status

| Input consumed | Exact use | Status here |
|---|---|---|
| Finite SU(N) links, normalized independent Haar, Wilson plaquette action | §§1–5 | Supplied regulator, not a derived physical premise |
| Even temporal torus and geometric half support | §3 link/site proofs | Checked completely; extent-2 convention explicit |
| Reflection-paired finite real β; crossing β≥0 | Positive kernel and paired half factors | Checked; site reflection needs no β sign |
| SPHERE55 digital cubes, collar prisms, radial real coupling | §5 cell/weight classification | Re-derived for every admissible finite K_a |
| Decision-4 pointwise normalized kernels, no terminal weight, zero source | §4.1 bare marginal | Re-derived exactly |
| Local bare-link clover, real paired normalization/centering | §4.3 | Definitions checked; no uniform moment estimate inferred |
| Common sequence and convergence of RP pairings | §6.1 or §6.2 fact 1 | H_reg input, OPEN as a Yang–Mills construction |
| Continuous limiting functional on the stated domain | §6.2 fact 2 and density | H_reg/(EXT) input, OPEN here |
| SO(4)_S state invariance, contraction/translation invariance | §5.3 all great/affine planes | Conditional H_Euc input, not a consequence of RP |
| Radius-uniform continuity, common algebra and diagonal compatibility | §6.3 N1S transfer | Supplied N1S/ALG/DIAG inputs, not proved here |

`IMPORTED-AND-REVERIFIED` below applies only to the specifically listed
mathematical component, not an entire upstream note or its status.

The main-source locators are `git show <pinned-origin/main>:docs/<name>`:

- June 5: `AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`.
- May 10: `REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`.
- June 2: `GAUGE_OS_STEP1_WILSON_PLAQUETTE_DECOMPOSITION_THETA_INVARIANCE_REFLECTION_HERMITICITY_NARROW_THEOREM_NOTE_2026-06-02.md`.
- April 29: `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`.

| Source | Import status | Used or contradicted, with verified boundary |
|---|---|---|
| Main June 5 Wilson temporal-gauge bridge | IMPORTED-AND-REVERIFIED | §2's representation-ring coefficients, convergence and integrated positive kernel are re-derived in §2.1. Its open-slab carrier does not prove the periodic case; §§2.2–3 supply that extension without global gauge fixing. |
| Main May 10 gauge-half Cauchy–Schwarz note | IMPORTED-AND-REVERIFIED | Its scoped norm identity follows by substituting F(θx)=overline F(x) and S_+(θx)=S_+(x). Used only as scope comparison. Those hypotheses are not generic Wilson half-observable hypotheses; no Wilson RP theorem is imported from it. |
| Main June 2 plaquette-decomposition note | IMPORTED-AND-REVERIFIED | Its two periodic crossing families and holonomy restriction are checked in §§2.3–3. A periodic gauge sends the temporal holonomy P to gPg^{-1}; all temporal links can be identity only if P=I. Conversely the recursion g_{t+1}=g_tU_0(t) is periodic when P=I. Its restricted gauge is not imposed here. Its phrase “site reflection” for t↦−1−t is geometrically a link reflection. |
| Main April 29 axiom-first RP parent | IMPORTED-NOT-YET-REVERIFIED | Its bounded pure-gauge dependency is handled above. The coupled staggered/fermionic transfer and joint-Gram claims are not used or reverified. It supplies no periodic pure-gauge closure here. |
| PROOF L9a, L9a-m | IMPORTED-AND-REVERIFIED | Finite link/site/mixed RP re-derived with explicit domains and two-plane handling. The matching sentence needs time extent ≥4; half-link splitting handles extent 2. Its numerical c4 receipts are not reused as exact certificates. |
| PROOF L9a′, S4′/S4″ | IMPORTED-NOT-YET-REVERIFIED | Definitions read to distinguish deterministic block maps from auxiliary soft fields; block iteration/branch-covariance theorem is unnecessary for bare clover RP and is not independently certified here. |
| CODEX_REVIEW_P4 §1.1 | IMPORTED-AND-REVERIFIED | The matching-link change of variables is re-derived in §2.3. Coordinate-prism RP requires the additional §5 classification. |
| CODEX_REVIEW_P4 §4.1; PANEL_P1 closure | IMPORTED-AND-REVERIFIED | Only their finite-sum RP limit implication, under actual convergence of products, is used and re-proved in §6. Other invariance/regularity inputs remain external. |
| CODEX_REVIEW_HINT `Lemma BARE`; ROTDEF §5.1 | IMPORTED-AND-REVERIFIED | Pointwise normalization and reverse integration prove exactly the bare marginal, §4.1. |
| OSLEAF55 D2–D8, RP-lat and RP portions of CLOSURE/CONTRACT | IMPORTED-AND-REVERIFIED | Restricted-domain RP transfer is re-proved in §6.2 using geometric half-edge support. The original endpoint-only wording at temporal extent two was defective and is corrected in OSLEAF55; the source reviews remain historical and the affected confirmation is separate. This supplies no continuum convergence hypothesis. |
| OSLEAF55 quantitative EXT, reconstruction and trajectory existence | IMPORTED-NOT-YET-REVERIFIED | Consumed only as named open/supplied hypotheses where needed; no analytic estimate is promoted. |

Literature access: [Osterwalder–Seiler (1978)](https://doi.org/10.1016/0003-4916(78)90039-8)
was located by publisher title/abstract but the article/PDF fetch returned
403. [Seiler, LNP 159 (1982)](https://link.springer.com/book/10.1007/3-540-11559-5)
and its lattice chapter were located, but the full chapter is subscription
content. Their detailed theorem hypotheses are IMPORTED-NOT-YET-REVERIFIED;
any recalled attribution of this method to them is [m], non-load-bearing.
[Fröhlich–Israel–Lieb–Simon, 1978 IHES preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/FROHLICH/1978-1980/P_78_224/P_78_224_web.pdf),
§2, Theorems 2.1–2.2, was actually read: it motivates expanding a paired
interaction into a positive cone, with commuting half-algebras. §2 here
supplies its own bounded, absolutely convergent scalar proof. No numerical
constant, reconstruction result or unverified literature hypothesis is
load-bearing. This packet claims re-verification and closure of the named
interface gap, not novelty of Wilson RP.

## 8. Exact finite-check construction and current evidence

The immutable criteria are `checks/hrp_criteria.md`; its initial stat,
size and SHA-256 are in HRP_LOG.md. `checks/hrp_exact.py` uses only
standard-library integer and rational arithmetic. Each Gram is saved as
an integer numerator matrix divided by its positive exact normalization.
PSD is checked through exact Schur complements, including zero pivots;
a negative pivot or a zero-diagonal/nonzero-off-diagonal 2×2 block
certifies a negative eigenvalue by congruence. No floating eigenvalue
tolerance is used. Code is a check of the proof, not its premise.

The declared finite observable bases are subalgebra bases, not a claim
to exhaust every positive-half gauge observable:

- On 4×2, fix one spatial tree link in each time slice. Let g_t be
  the remaining spatial holonomy, and use indicators of its conjugacy
  class. For link reflection the basis is all class pairs (g_1,g_2);
  for site reflection it is all triples (g_0,g_1,g_2), including both
  fixed slices. Full Haar support makes these indicators independent.
- The transfer matrix sums BOTH temporal links between adjacent slices:
  T_t(g,h)=Σ_{c0,c1}w_{t,0}(c0c1^{-1})
  w_{t,1}(c1 h c0^{-1}g^{-1}). Spatial tree gauge is legitimate on
  each slice because it fixes a tree, not its spatial loop. Gauge
  invariance of class indicators and Haar changes of variables remove
  only a constant factor. Multiplying T_0T_1T_2T_3 with the displayed
  insertions sums the closed time cycle, including temporal holonomy.
  Normalization cancels the omitted Haar/group-order constants.
- Z2 uses normalized real character (1,−1); Z3 uses (1,−½,−½); Q8
  uses Re Tr/2 of its faithful SU(2) representation (1,−1,0,…,0).
  The choice β=k log2 for Z2/Q8, β=2k log2 for Z3 makes the weights
  rational. Multiplying each plaquette weight by a positive constant
  yields integer tables (2^{2k},1), (2^{3k},1,1), and
  (2^{2k},1,2^k,…,2^k), respectively, for k≥0. This multiplication
  does not change a normalized expectation. k profiles are fixed in
  the script before its first calculation.
- Every group has 4×2×2 cases consisting of two independently weighted
  t-x sheets (t-y and x-y coefficients zero); the observed y=0 sheet
  has exactly its 2D Gram since the other partition factor cancels.
  These are valid nonnegative-coupling 3D Wilson models, but do not test
  inter-sheet interactions. Additional 4×2×2 Z2 cases have strictly
  positive, position-dependent coefficients on all 48 plaquettes and
  a 32-element spatial tree-gauge indicator basis. The positive theorem
  for fully coupled 3D Q8/Z3 is the written proof, not a computed check.
- An independent direct enumeration of every original-link Z2 4×2
  configuration compares normalized Gram entries against the transfer
  method for both reflections. This is an independent implementation
  path inside the same author context, not independent scientific review.
- The sphere geometry checker builds actual four-dimensional D_a and
  ∂D_a×[0,1] at rational R/a, using exact incidence sums and radial
  cell weights. It tests all four coordinate reflections, including
  crossing prism faces. An exhaustive Q8 word-identity check separately
  tests the noncommutative half-link factorization. The finite integration
  model is the six-face
  prism over a boundary square of the central 4-cube, with weights
  inherited from the full K_a incidence sum. Its five non-tree edge
  variables are enumerated for all three groups. Its Gram basis is
  the conjugacy-class indicators of the positive prism face holonomy.
  It is explicitly a local prism model, not a full-K_a partition sum.

The negative controls deliberately distinguish two defects. A negative
crossing coefficient can give a Hermitian Gram with a negative direction.
Breaking reflection symmetry can instead make the Gram non-Hermitian;
failure of Hermiticity already violates RP, but need not give a negative
eigenvalue of that nonsymmetric matrix. In the one-cell control the four
independent Z2 loop fluxes a+,b+,a−,b− have density proportional to
exp((log2)a+b−), representing one crossing closed walk and no reflected
partner. On the character basis (1,a,b,ab) its normalized raw Gram is

    [1  0   0  0]
    [0  0   0  0]
    [0  3/5 0  0]
    [0  0   0  0].

This follows directly by summing independent signs: only 1 and a+b−
have nonzero expectations. The raw eigenvalues are 1,0,0,0; its Hermitian
part has eigenvalues 1,3/10,−3/10,0, and F=a−b has Q(F,F)=−3/5.
This exact hand derivation detects RP failure but FAILS the brief's
literal raw-negative-eigenvalue criterion. The script is required to
report that failure rather than call it a successful negative spectrum.
This intentionally malformed extended cell is not a claimed defect in K_a.

For the asymmetric-coupling control a separate hand analysis also warns
against demanding a negative raw eigenvalue. In the Z2 holonomy-pair
indicator basis, write K=[[34,16],[16,34]], whose eigenvalues are 50 and
18 (the two temporal Haar-link sums are computed directly from weights
(4,1)). Changing one interior plaquette from k=1 to k=2 gives the
same-half transfer values 130 and 40, from weights (16,1) and (4,1).
The raw Gram numerator is

    D_- (K⊗K) D_+,
    D_-=diag(34,16,16,34),   D_+=diag(130,40,40,130).

It is nonsymmetric, but similar via
S=diag(sqrt((D_-)_i/(D_+)_i)) to
sqrt(D_-D_+) (K⊗K) sqrt(D_-D_+), which is strictly positive definite.
Thus this particular raw matrix has positive real eigenvalues despite
failing the Hermiticity required for RP. This is an exact analytic
prediction before any Gram computation, not a reported script outcome.
Both asymmetry controls remain in the runner, with failures disclosed.

**Execution status:** the first run stopped at the priority prerequisite:
the sandbox denied `nice`'s setpriority call. No finite Gram calculation
ran in that attempt. Its stdout/stderr/time receipts are preserved as
`checks/hrp_attempt1_*`. Execution remains pending the specific resource
constraint clarification recorded in HRP_LOG.md. The written theorems
above do not depend on those missing numerical receipts.

**[RHRP-7 fix 2026-10-29]** Later evidence: [lead's rerun outside the sandbox](checks/hrp_lead_rerun.md).

## 9. Banking statement and consumer map

### [RHRP-7 fix 2026-10-29] Exact consumer statements and qualifications

**Author proposal for independent review, not yet banked.** This wording-only
revision replaces the paraphrased RP exports in the original §9, quoted below.
Its finite-theorem scope, other consumer boundaries and exclusions still apply.

**N1F / ASSEMBLY55 N3; PANEL_P1 §3 item 2 (verbatim).**

> The approximants to every positive-half polynomial obey reflection positivity, or have negative errors tending to zero, for one common time reflection. Localization/renormalization errors are controlled in the same moment topology.

For the zero-source Wilson state and the reflection-compatible local bare-link/clover maps proved here, the inequality is exact eventually for every fixed positive-half polynomial; there is no polynomial-dependent subsequence. Convergence of the required products, the common algebra and any extension to its declared continuum domain remain H_reg/(EXT)/ALG hypotheses. For the exact maps here those errors vanish eventually.

**N1S / ASSEMBLY55 N3 (verbatim).**

> RP for great spheres through the base point S

At finite cutoff HRP proves the four coordinate reflections. At fixed R it gives the quoted great-sphere property on the specified cap domain after the separately supplied continuum convergence and SO(4)_S state invariance. Radius-uniform convergence/continuity and the supplied translation-invariance step give the flat-limit affine-plane property. The ordinary-moment version and the restricted OS-domain version remain distinct conditional statements; the latter does not silently replace literal N1F/N1S. No declaration that H_reg, H_Euc, the trajectory or the physical theory exists should accompany this export.

**CODEX_REVIEW_P4 §4.1 item 4 and its qualifications (verbatim excerpts).**

> Assume continuum sphere states $\omega_R$ have already been constructed, with O(5) invariance, great-sphere RP on the chosen local algebra, and compatible field normalizations. For each compact $K\subset\mathbb R^4$, a sufficient local condition is equicontinuity of every pulled-back Schwinger functional in a fixed test-function seminorm, together with moment control strong enough to pass products.

> Each polynomial RP expression is a finite sum of convergent moments. RP passes for planes through zero; translation invariance moves it to every affine hyperplane.

> Weak convergence alone is enough for bounded continuous half-algebra observables. For unbounded local fields the moment or uniform-integrability hypotheses above are indispensable; weak convergence alone does not preserve expectations of their products.

These are consumer hypotheses and an RP implication, not a claim that HRP
constructs the sphere states or supplies their invariance or moment bounds.

**OSLEAF55 CLOSURE-sep and CONTRACT-sep (verbatim RP clauses).**

> - **(H_RP-sep)** Lemma RP-lat (exact; no input).
> - (d) E2 (RP for θ; with (c), for every affine hyperplane);

The CLOSURE-sep export uses §6.2's common-sequence convergence on compact
separated tests and continuous extension to the restricted OS domain.
Conclusion (c), used for affine hyperplanes, requires the separately supplied
H_Euc-sep hypothesis. This export does not establish ordinary polynomial
moments or any other CLOSURE-sep conclusion.

CONTRACT-sep's supplied assumptions, including the RP consumer, are:

> - **(U-sep)** |S^R_n(F)| ≤ α(n!)^β|F|_{sn} with s, α, β independent of R and n (the separated replacement of SPHERE55's U-mom;
>   OPEN, the first half of ML8);
> - **(K-inv)** exact local Killing invariance on 𝒟 for every n: S^R_n(F∘ψ^{-1}_{R,v}) = S^R_n(F) for the boost and pole-rotation
>   Killing fields v whose flow path keeps supp F inside the chart domain away from the seam, ψ_{R,v} := χ_R^{-1}∘(flow of v)∘χ_R
>   (all-order input: ML7; CODEX_REVIEW_SPHERE Finding 7);
> - **(RP-pole)** RP for the four coordinate great spheres through S (banked finite-cutoff RP, passed to S^R by CLOSURE-sep (d)).

The fixed-R continuum extraction, restricted cap domain, compatible
normalizations and radius-uniform convergence/continuity remain those of
§§6.2–6.3. (U-sep) and (K-inv) remain separate inputs. The phrase
“banked finite-cutoff RP” is quoted consumer wording; this revision grants
no banking or retained status. These restricted-domain exports do not
silently replace literal N1F/N1S.

### Original §9 wording (preserved verbatim)

> **Author proposal for independent review, not yet banked.** The result
> eligible for later banking is the conjunction of:
>
> 1. §§2–3: finite periodic SU(N) Wilson link and site RP on the stated
>    full bounded half-algebras, both periodic planes included, for
>    reflection-paired nonnegative plaquette coefficients (with the
>    sharper sign qualifications stated there), without global temporal
>    gauge or a trivial-holonomy restriction.
> 2. §4: exact zero-source bare-marginal identity and exact RP for local
>    bare-link positive-half approximants, including the actual clover
>    observables with reflection-compatible normalization and support.
> 3. §5: RP for every θ_μ of SPHERE55's actual cubical-prism regulator
>    under its real radial nonnegative coefficient prescription; no
>    regulator repair needed.
> 4. §6: RP closure on the common limit sequence under the precise
>    convergence and continuity hypotheses for the selected domain;
>    great/affine-plane transport only under separately supplied state
>    invariance. The ordinary-polynomial and restricted OS domains are
>    distinct conditional exports.
>
> | Consumer inspected | What it may consume | What remains separate |
> |---|---|---|
> | ASSEMBLY55 N3 → N1F / PANEL_P1 §3 item 2 | Exact finite RP and §6.1 for every polynomial whose required moments converge on the common sequence | H_reg, common algebra and its contact/domain choice; no arbitrary moment existence inferred |
> | ASSEMBLY55 F3, N3 → N1S / CODEX_REVIEW_P4 §4.1 item 4 | Coordinate great-sphere RP from §5, then §5.3/§6.3 | All-order cap state invariance, U-sep or actual moments, DIAG and compatible normalizations |
> | SPHERE55 §§1.5, 2, 5.2, 13 | Actual θ_μ crossing-cell proof; corrected statement of its role | Seam transparency and SO(5) restoration remain analytic inputs |
> | OSLEAF55 D8, RP-lat, CLOSURE-sep(d), CONTRACT-sep RP-pole, E8, BRIDGE(iii) | Finite RP and restricted-domain closure, §6.2 | EXT/SP_λ estimates, reconstruction, algebra acceptance, all other BRIDGE claims |
> | ROTDEF §2.2 and §9 locality/RP discussion | Bare local support and zero-source marginal | No transfer of auxiliary coarse-law positivity or of fixed-flow-time locality |
> | PROOF L9a / E8.1 / E8*-red and L8c | Finite bounded gauge-invariant half RP; §3.3 if a mixed reflection is used | Chessboard iteration, block support/covariance L9a′ and limit identities still need their own proofs |
> | HANDOFF wording tracked by ASSEMBLY55 F25 | This author's proposed scope and pending-review status | No edit to PROOF's banking ledger; no retained status granted |
>
> The upstream inputs H_reg, (EXT), ALG, H_Euc, H_int, trajectory existence,
> and the physical existence/mass-gap target are not closed by this packet.
> The author check cannot fulfill the brief's separate-review requirement.
> No commit, push, PR, axiom edit, audit record or ledger mutation is made.
