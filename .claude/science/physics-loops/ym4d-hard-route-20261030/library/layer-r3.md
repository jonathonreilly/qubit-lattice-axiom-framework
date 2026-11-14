# LAYER-THM, round 3: identifications and admission

Codex; checkout
`98a768cc8e87e5dac90b4570548719ada61fa1eb`, 2026-11-07.
FINISH row 448. Research text, not an audit; no status is granted.
No computer-assisted argument is used. This generation has no independent check.

Credit Tadeusz Balaban for the averaging, propagators, response and walk method.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their account, for the source statements. Their proved arguments and the
completed repository arguments are inputs, not new contributions here.

## 1. Scope and source conventions

I, II, III and SA denote the supplied complete account and outline at
`31a47c543775`. Source locators are physical lines. Their hashes agree with
the table in layer-pkg §1. The source directory is a snapshot, not a Git
checkout. There is no `prior/layer-r3.md`. The registry assigns LAYER-THM
and CA-LAYER to this lane. PI, B98-P5, and the global stage-response
identification keep their existing owners. Their work is not repeated.

Use layer-pkg's spaces, full stencils, datum norm, seven-term nonlinearity
and equation (S5). Use walks-gw's **product of primitive tags** for a
composite. A tag within a primitive is a union tag. These conventions
differ when two factors visit the same cube. All estimates below are
conditional on the actual operators having the stated domains.

The input GW is the theorem of walks-gw, including its common choice of
PI constants and its stronger source-to-graph estimate (P18). Its proof
and B98-P5's local analytic port are not independently checked here.
The repairs and qualifications in b98p5-r3-gate are retained. In particular,
the finer collar and actual minimizer tube are not certified by its census.

The outline index was searched first. Chunk 10 and obligations.md lead to
SA 10354–10464 and 10562–10582. They prescribe reduction before switching,
and distinguish the two response systems away from physical pairs. They
do not identify the general-field layer or the partner current needed here.

## 2. The switched coefficient m_H

### 2.1 What algebra identifies

Write A for A', h=A-HX, and Xi=Theta A-V'(A). At switches one,
I 14386–14495 identifies the chart current and its reduced representation.
This is already proved there. At arbitrary switches, define the **candidate**

    m_c = Q^T k + Lambda^T j_J H - Delta' H,
    k = (q_J-a) ell^(-1).                                  (M1)

Every factor retains its primitive tags. Delta' is the first-order
curvature correction, not the component Laplacian. Let J_def be the
current obtained from the third item of the chart definition at these
operators. Direct substitution of h=A-HX, without any inverse identity,
gives

    J_def = P_0^T Xi + Q^T(q_0-a)ell^(-1)b
            - Delta' A - m_c X + F(W,h).                   (M2)

Thus (M1) really is the coefficient of X in this expression. The step
does not identify its remaining A,b terms with the rider.

Let L_sigma=Delta_W+K_W-P_1(sigma). The difference between (M2) and
the proposed rider J_red=L_sigma A-m_c X+F(W,h) is exactly

    D_sigma = P_0^T Xi + Q^T(q_0-a)ell^(-1)b
                         -(Delta'+L_sigma)A.              (M3)

At j=0, sigma=1, the account proves D_sigma=0. At arbitrary switches
no such identity follows from (S5). This isolates the failing step:
the representation identity is being used after its hypotheses have gone.
Its proof uses Delta_a P_0G_0=P_0^T,
Delta_a H_0=Q^T q_0 ell^(-1), and QA=ell^(-1)b. None of these
switched identities is a consequence of the assigned fixed-point
equation. The last one already fails in the test below.

### 2.2 A zero-switch test, with actual formulas

Take an admitted flat torus, J=0, a nonempty full decoupling family,
and set every switch to zero. All primitive walks have nonempty complete
footprints, including the identity pieces fixed in walks-gw. Consequently
G_0, q_0, q_J, G, H_0, H and Lambda vanish at this parameter.
For j=0 and any sufficiently small block datum b, (S5) then gives
A=0, X=0, h=0. The nonlinear functions vanish at zero.
Equation (M2), however, gives

    J_def(0;b) = -Q^T a ell^(-1)b,   J_red(0;b)=0.          (M4)

Choose b with Q^T a ell^(-1)b nonzero. Such a b exists: at a flat
one-level tower the averaging row is nonzero and a,ell are positive
diagonal maps. Equivalently, use a height-zero identity row. Scaling b
makes it fit any positive datum radius. This is a finite symbolic example;
it uses no evaluated spectrum or enumeration.

There is a second test. At zero switches (M1) gives
m_c=-Q^T a ell^(-1), which is nonzero. I 72720–72728 instead requires
the m_H kernel to vanish unless both legs lie in a retained component.
With an empty retained region that kernel must be zero. Therefore (M1)
with an **untagged** diagonal mass is not that localized operator.
The fact that X=0 at this particular datum does not establish an identity
of the operators; the source states a kernel assertion.

These tests distinguish two extensions of an unswitched formula. They
do not refute the unnamed layer theorem, or prove that it must use J_def.
I 15307–15320 assigns composites by the earlier chart formulas while
explicitly choosing the reduced fixed-point equation for the field;
the later rider assumes a reduced current representation. Identifying those extensions is
precisely what remains necessary. Replacing the untagged local mass by a
localized mass is a change of definition and requires a matching proof.

### 2.3 The candidate has the required bound, on the admitted class

GW's first-order kernel bounds and its averaging transpose densities give
the following weighted operator bounds, with the same physical pairings:
Q^T: block power -3 to F; k: B to block power -3;
H: B to E; j_J: E to scalar power -4;
Lambda^T: scalar power -4 to F; Delta': E to F.
The local diagonal part of k is bounded by the fixed mass-coefficient
ceiling in its scaled units, included in c_k below.
Denote these constants by c_Q,c_k,h,c_j,c_Lambda,c_Delta.
The triangle inequality gives, for every admitted p,

    |m_c b|_{-3,p} <=
      (c_Q c_k + c_Lambda c_j h + c_Delta h)|b|_p.          (M5)

For each composition, insert its nonnegative kernel majorants, use
p(z)/p(y)<=exp(delta d(y,z)), and sum in order. This proves (M5)
with full source measures. Absolute tails converge by the same estimate.
Thus m_c is holomorphic and (M5) is uniform on the common admitted domain.
It does not require a graph bound on H or derivatives of J.

Three attempted closures have now been decided. Reduction before
switching produces (M1) and (M5), but not the asserted kernel locality
with its untagged diagonal. Reduction after switching leaves (M3), with
the nonzero test (M4). Analytic continuation from sigma=1 cannot remove
it: one parameter value is not an open set of switch values. The exact
remaining supplier is the literal reduced m_H word assignment, including
its local diagonal, and its agreement with the current used by each link.

## 3. General-field conversion FM and FD

### 3.1 FD for the specified GW operator

Let B_sigma be the **bare constrained operator with the word assignment
used in GW**, obtained by setting the independent current to zero in
GW's G. This specifies an operator, not merely its unswitched value.
The stronger estimate (P18) in walks-gw §8 gives

    ||B_sigma f||^Delta_p <= g_b |f|_{-3,p}.               (F1)

Indeed all current vertices disappear in the absolutely convergent
series, and the remaining majorant is a subseries of the same positive
majorant. Its endpoint Laplacian estimate, source measure, and weight
ratio are unchanged. The bound holds for complex f, all admitted p,
and the same switch polydisc. Uniform convergence also gives holomorphy.
This proves FD on the GW class; no second-difference bound on f is used.

There is a second precise reading sometimes possible for a printed bare
operator. If it is **defined as the composite**

    B_sigma^comp = G_0(sigma)-H_0(sigma) ell Q G_0(sigma),

the endpoint graph bounds on G_0,H_0 and the native bound on ell Q G_0
give FD with constant g_0^Delta+h_0^Delta c_(ell Q G_0).
Products retain their primitive tags. This proves a bound for that
composite; it does not identify it with a separately switched primitive
B_sigma. They agree at one by the unswitched algebra. That agreement
does not identify their switched series.

Full-footprint confinement proves the corresponding component support
statement for either specified construction: a nonzero word has every
read and both endpoints in one retained component. A component on which
f vanishes contributes zero. This is the support statement needed in
U01, U23 and U25. It requires the complete read set, not just the output
bond's position.

**Exact remaining FD step at a use.** Identify its printed
tilde G_0(sigma), or its completion operator, with one of these two
specified operators on the same rows, boundary conditions and physical
pairings, and put its f in F_p on the whole parameter domain. Once this
is done FD is supplied by (F1), not a new open graph theorem. A value
decay estimate for an operator of a similar name is insufficient.

### 3.2 FM: an exact equality to test

The conversion at sigma=1 is already proved in layer-pkg §7. In that
convention a physical force f enters the bare equation as -B_1 f and
the datum is j=B_1 f. The identities T_1 B_1=G_1 and the bare
resolvent identity give the same forced equation as (S5).

At general switches, inserting the **prescribed** datum j=B_sigma f
into (S5) gives exactly

    z = -T_sigma B_sigma f + G_sigma Theta_sigma H_0(sigma)b
                            -G_sigma V'_sigma(A').       (F2)

If the invoked field equation instead has force term -G_sigma f,
its equality with (F2) requires

    (T_sigma B_sigma-G_sigma)f=0.                         (F3)

If it is the bare switched equation z=-j+B_sigma(Theta_sigma A'-V'),
it requires the resolvent of that switched B_sigma instead. Neither
identity follows from agreement at sigma=1. In the composite convention
each visit is tagged in each factor; a primitive word with a shared
cube and the product of its factors have different switch monomials.
The already given word test in layer-pkg §7 applies. Resumming at fixed
sigma changes the assigned analytic function unless its word identity
has first been proved. This is the exact FM failure, before any
estimate or coupling choice.

### 3.3 A conversion that can be constructed, with its limitation

GW removes one analytic obstacle to a *different* datum. On E^Delta_p,
the embedding into E_p has norm at most one, so

    ||Gamma_sigma||_(E^Delta_p -> E^Delta_p) <= C_kappa |J|_{-3}.

Choose the common independent-current ceiling after kappa so that the
right side is at most 1/2. Then

    T_sigma^(-1) = sum_(n>=0) (-Gamma_sigma)^n,
    j_eff = T_sigma^(-1) G_sigma f,                       (F4)
    ||j_eff||^Delta_p <= 2 g_Delta |f|_{-3,p}.

The geometric majorant proves convergence in operator norm. Multiplying
finite partial sums by I+Gamma leaves a remainder tending to zero on
both sides; hence this is an inverse. Uniform convergence on smaller
parameter polydiscs proves holomorphy. Each summand preserves retained
components, including the identity term, so the inverse preserves them.
These are elementary Banach-space proofs; no numerical inverse is used.
The **pair** datum is admitted when
2g_Delta |f|_{-3,p}+|b|_p<epsilon; for example, allocate epsilon/2
to each of its two terms. All constants are chosen before the final
coupling ceiling and uniformly in p.

Substitution now gives -T_sigma j_eff=-G_sigma f exactly. Thus a
general-force equation with this force and the same remaining terms
has the unique small (S5) solution with datum (j_eff,b). At one,
j_eff=B_1 f. At other switches (F4) does **not** prove j_eff=B_sigma f;
that is again (F3). Consequently this construction cannot replace the
explicit datum in U02 or the prescribed completion germ in U26. It
closes invertibility and radius control for the alternative conversion,
while leaving the actual convention test visible.

### 3.4 Which calls require the conversion

The last table gives a field entry for every U. The relevant source
distinctions, rather than a single universal field hypothesis, are:

* U01 explicitly uses the field-datum substitution at I 72534. U02
  explicitly sets j_3=tilde G_0(sigma)J_3 at I 73103–73140. U03 uses
  those same links on the product polydisc. These need the literal
  operator match for (F1) and the force identity (F2), or (F3) if the
  force convention is -G_sigma f. At one FM is settled.
* U04's presentation hypotheses and U17's healing links inherit this
  source convention. They do not state an independent field equation
  that proves the match. U23/U25 need, in addition, zero forcing on
  each full retained footprint when using zero off a component.
* The completion source near I 92540–92602 has the form
  G''(sigma)J_c+[G''(sigma)-G''(1)]Q''*mu. The cancellation
  G''(1)Q''*mu=0 is an identity at one only. U26 and the explicit
  field estimate at I 142530–142543 require graph control of these
  actual terms. If G'' is identified with a GW operator and Q''*mu
  is in its F_p domain, triangle inequalities give the graph bound
  for the difference. They do not turn value decay into a graph
  bound, or prove the boundary-distance improvement without its
  marked full-footprint estimate. These matches remain missing.
* U05–U13, U19–U22, U27–U28 and U31–U32 concern block-only (0,b)
  calls or their consequences; their j=0 needs no FM. A source-free call can still have an
  independent base current J. U14–U16, U18, U20, U29–U30 are
  implications about furnished data; they inherit FM only when their
  furnished data came from a source-bearing link. U33 compares two
  constructions, so a one-cutoff source conversion is not RC. U34
  needs the actual field support/conversion wherever its continuation
  uses a source-bearing earlier link.

Thus FD is a deduction from the new GW input on a specified admitted
operator family; FM for the actual switched source-bearing links is
not settled by that bound. No invocation is repaired by renaming its
datum.

## 4. Admission certificates

### 4.1 What a certificate must quantify over

For a use U, let D_U be its *entire prescribed parameter domain*, not
its real centre. A certificate is universal over the determining sets,
real representatives, twists, independent currents, intermediate images,
data and weights reached on D_U. Use these three separately checkable
records:

**Loc[U].** Identify the literal PI rows and corner blocks, its field
and scalar spaces, and its whole-action Hessian. For every required
anchor x of height j there must be one real gauge on the entire
N(x), of closed half-width r_N ell_j, with
ell_lambda|A|, ell_lambda^2|nabla A| <= L^2 a_0. Here r_N=7M_t,
hat r=(2L+2)M_t; exterior points have level zero. This is (S1-loc),
not just the gauges on some interior test cubes. The twist obeys
(S2) on the field bonds and (S2+) on **every coefficient read** in
Omega_0^+, including protruding plaquettes and exterior differences.
The independent current obeys the common -3 ceiling. Finally the
gap, divisibility and room assumptions of PI/GW hold, including

    torus side >= max(2 hat r+2, t_F M_F) ell_k,           (A1)
    switch cube side / ell_k >=
                       max(4 hat r+8L, 64 kappa/mu).     (A2)

Changing the outer boundary convention requires a new identification;
the inverse of a restricted matrix is not the restriction of its
inverse. The account's inner-plaquette variational problem and PI's
whole-action Hessian on a finite field support must likewise be matched,
including their boundary rows. Neither word “localized” fixes this.

**Avg[U].** For every actually read positive-height averaging row and
its transpose, supply the real-reference S^pl hypothesis of b98p5-r3
§4, or a frame satisfying its local port. Include the entire double
block, any finer collar, the same logarithm branch and a larger complex
ball on which the Cauchy derivative estimates are made. The density is
the fine physical density, not just a value bound on the average.
At height zero the averaging row is linear. If a minimizer is used to
supply the reference, its *actual* tube must fit this larger ball.

**E[U].** Identify U's equation with (S5), with its native seven-term
nonlinearity and pairings; establish the primitive estimates (3) of
layer-pkg from Loc[U], Avg[U], GW and the corresponding local analytic
estimates; then check that every datum/image on D_U stays in the
contraction and uniqueness balls. The nonlinear contraction already
proved in layer-pkg then proves existence and holomorphy. It is not
necessary to solve that contraction again at 34 uses. For the four
current entries, also require the actual P_1 word assignment and the
m_H/current identity isolated in §2. Denote this additional condition
by **M[U]**, and denote the resulting four-entry estimate by **N[U]**.
E[U] alone does not supply M[U].

These are mathematical predicates, not checks discharged by an inventory.

### 4.2 Admission implications that do close

**Interior local models.** PI Proposition 3.1 applies to aligned cells
of side s_i, with s_i a multiple of M_b ell_i and
s_i >= 12 M_b ell_i, with its stated separation and common floors.
The source's (S1) tests then give (S1-loc) at every anchor whose N(x)
is contained in Omega_0. The proof is exactly PI's cube-cover proof;
no new analytic estimate is needed. If Omega_0 is the whole torus,
this eliminates the outer-boundary issue, subject to (A1). If it is
proper, the statement stops at N(x) intersecting its complement.
There one must supply a real gauge on the entire N(x), not extend an
interior gauge by declaration.

The outline geometry indexed in chunk 09 is relevant but does not
silently finish this port. SA 9593–9625 specifies separated cubes of
side mathfrak M ell_i, identifies mathfrak M with its walk size M_1,
and distinguishes inward-row conventions and the inner action.
SA 9776–9789 lists separated construction sequences and collars;
9913 requires the collar boundary to stay in one layer; 9916 specifies
the order of constants. To use the interior implication one must
identify those actual cells/rows with PI's, choose mathfrak M divisible
by M_b and at least 12 M_b, and retain every boundary read. The
separation assertions in those outline passages are sketches, not
replacement proofs of admission on D_U. U08 supplies more particular
geometric hypotheses, as recorded below.

**A supplied frame follows from admitted local models.** This is a useful
reduction of the number of independent admission obligations. GW §7
already proves that the double block E_c of a height-j row lies in
the appropriate local model(s), with levels j and j-1 when j>0.
Use its supplied gauge on the whole carrier. The change between those
two scale units costs only a fixed power of L; (S2+) controls every
extra read. Taking a_0,a_1 small enough for the fixed local port
puts this representative in its frame class. B98-P5's local port
then supplies the analytic average, its derivative and transpose
density on the smaller ball. Thus **Loc[U] plus the GW carrier
identification and larger-ball inclusion implies Avg[U]**. A separate
global S^pl proof is unnecessary on this route. What remains at an
unadmitted row is precisely the absent frame or domain inclusion; a
scalar curvature estimate does not fill it in.

**The PL109 route.** When full CMP109 (i)–(iii) membership and its real
representative are expressly available, the inclusion in
print-inverse-r2 at I 12935–13035 gives the plaquette bound of S^pl
under c_12 L M B_109 alpha_0 <= a_0 and its alpha_1,current ceilings,
with 17M_1<=LM, 17M_1<=c_12 LM and c_12 L>=2. This supplies the
real-reference carrier hypothesis wherever those tests apply. It
does not provide (S1-loc) for a larger exterior patch, or the complex
radius at a reached point. The source's relaxed class containing only
(3.35), (3.37) and a current bound has no such implication. The island
counterexample and the stronger-class repair in b98p5-r3 are already
established; they are not repeated here.

**Constants and tubes.** Choose once the stronger flat/parametrix
constants required by GW, then M_t and the PI scale and gap floors,
then a common kappa and compatible switch geometry, then the common
small real/twist/current ceilings and datum radii. The extra current
ceiling in (F4) is imposed at this last step. All uses must fit these
same choices before the final coupling ceiling. For example, a
consumer's rate delta_0/8 must be at most GW's admissible rate; naming
it a small fixed rate is not an inequality. A constant chosen on one
base does not automatically remain uniform on a product of reached
bases.

In the minimizer route use the actual constant C_1^(172). The valid
external-radius restriction is r_ext <= min(1/2,C_1^(172) epsilon_1/2),
with the stated norm conversions. One cannot replace C_1^(172) by
max(C_1^(172),1) in its radius conclusion. Shrinking a_A does not
improve the fixed ratio between a_A/10 and C_1^(172)a_A/4. The
outer analytic room and the finer Lambda'_0 collar left conditional
by b98p5-r3 §4 and its gate remain conditional here. The local port's
operator-norm constants, for a ball parameter rho, may be taken as
c_4=rho/sqrt(N), C_2=4N/rho, C'=8N/rho, C_3=16N/rho, subject also
to the separate published thresholds. These constants do not certify
that a particular minimizer tube lies in that ball.

### 4.3 The attempted admissions, use by use

In this table **L** means all of the literal Loc requirements in §4.1,
including (A1)–(A2) and the common constants, on the named domain.
**A** means the complete Avg record there, with its larger analytic
ball. “Missing L/A” specifies an unproved implication for that actual
domain; it is not a claim that no member can be admitted. An inherited
call carries the originating call's unproved conditions. No new inverse
or average is needed in an algebraic implication about a furnished
triple. Sources are given once more in the final coverage table.

| Use | Actual domain and E attempt | Loc attempt: exact remaining step | Avg attempt: exact remaining step |
|---|---|---|---|
| U01 | The exempted-set family extends its switches by one on K. The (S5) contraction would apply after identifying its field datum; its whole (a)–(f) premise is not E. | L on the actual exempted base, with every full footprint for the restriction; extension of switches does not establish local real gauges or exterior reads. | A for that base. Neither an S^pl certificate nor all its carrier frames/tube inclusions is supplied by exempting K. |
| U02 | Four reached links. The induction explicitly assumes full K(B_s;gamma) membership and datum sizes at every link. E follows if those admitted operators are the chosen GW/S5 ones; link 3 also needs FM. | L separately for B''_k at links 1 and 2, B_1 at link 3 and B_k at link 4, uniformly on the induction's parameter domain. Full K tests alone do not prove the needed exterior local models. | PL109 on each asserted full member, under the inclusion ceilings; A still needs all carriers and larger-ball inclusion at every reached base. |
| U03 | Same four **global** determining sets on a product of four switch polydiscs. E is inherited only if every intermediate image is admitted there. | Uniform L for those global sets and all intermediate bases. The local scaffold is explicitly not the determining set and cannot supply it. | Inherit U02's PL109 where membership holds; prove the common analytic carrier domain on the whole product, not separate germs. |
| U04 | Source-presentation family in treated-component input (i4). Its six proof steps assume the layer package; E and FM are not supplied by this input. | L for each actual presented/completed domain, including the reads at the treated-component boundary. | A on these actual bases; a presentation statement does not give real frames or a minimizer tube. |
| U05 | The real local bases U_0,U^0 on B^0=B_k(C), B^C=B''_k(C), their shifted real bases and the bidisc. A radius can be chosen after E and the explicitly imposed base/core hypotheses. | Interior thickness can use §4.2 once the actual cube grids and floors are matched. Missing L at every boundary-crossing N and on the perturbed bases, including the actual action convention. Zero twist at the centre is insufficient. | Where the named K109 hypothesis means the full representative, use PL109 on its test domain. The extra p(U_0)<=1 alone is not a small plaquette ceiling. Missing full carrier/tube inclusion for both bases and their shifts. |
| U06 | Two block-only calls (0,d_0),(0,f) on B^0,B^C. f contains the prescribed crossing/core gauge logarithms. E requires their sizes on the **whole** bidisc, as hypothesized in U05. | Same local sets and full reads as U05; no new L proof comes from writing a datum. | A for both actual nonlinear charts and crossing rows; neither datum smallness nor vanishing at zero proves it. |
| U07 | Linearization of the U06 chart. Existing graph estimate proves T^L=T H_0 after E; the alternate T^sharp=H is a different map. | Its explicitly relaxed three-clause class gives (3.35),(3.37),current, not L at all anchors. | A remains on that class. Only cube tests cannot supply the missing carrier frame. |
| U08 | The asserted local-solution scope uses (c1)–(c3): cubical nests, matching refinement off a collar and the unswitched host. E is an applicability assertion, not its proof. | These hypotheses support the interior route after matching mathfrak M, grids and PI floors. The unresolved step is a gauge on each N crossing the local outer boundary and matching the full exterior Hessian/twist reads, on both local systems. | A at collar/crossing rows and on each enlarged complex domain; a match of nests off a collar gives no frame inside that collar. |
| U09 | Full bidisc for the two U06 constructions. Use graph A' and first-order h, with N's four entries; the stronger printed graph-h shorthand is unnecessary. | Uniform L for both families, not just the real centre or a point satisfying the three displayed class inequalities. | Uniform A and datum inclusion on that bidisc. The proof's identification of A' with h does not certify an averaging domain. |
| U10 | Reality and derivative reality for an already defined local chart follow from conjugation and uniqueness. E is inherited from U06. | Inherit U06's L. Conjugation preserves an admitted real-representative domain; it cannot construct one. | Inherit U06's A; conjugation preserves the chosen real logarithm branch. |
| U11 | Shifted local **physical** chart with J=J(W). E and PH are required before differentiating its physical gauge identity. | L on the shifted physical base, including its boundary patch. Own-current equality does not imply the needed gauge radius. | A and the actual physical minimizer tube on that shifted base; the tube is the B98 §4 issue, not settled by criticality. |
| U12 | Gauge covariance on the admitted overlap of U11, then holomorphy in the fibre. | The real gauge transports an existing L certificate; it does not prove L for a new arbitrary complex-gauge ball. | Transport existing carrier frames and restrict to their common analytic overlap. The T^sharp alternative retains its extra (3.36) condition. |
| U13 | Choice of four floors and fixed constants for the two local constructions. | A common choice can be made once the U05/U08 L predicates and their grid identifications hold; the four-floor declaration by itself gives no exterior gauge. | Inherit their A. The constants must work on both larger domains before the final coupling choice. |
| U14 | A furnished (h,A',X), its represented current and the cutoff's smallness/collar conditions. The rider proof invokes no new solution. | No new L in this implication. Admission of the originating triple is inherited, and its current still needs M. | No new average. The supplied p_W<=1 and N_y(chi h)<=1/40 are rider hypotheses, not a replacement for A of the originating chart. |
| U15 | The stated relation h=A'-HX and the consumer's bound (e2). | Not needed for this seminorm triangle inequality. | Not needed. |
| U16 | Differences of furnished layers at two specified exponential profiles. E and N must hold for each actual base. | L for those actual kernels and admission of **both** rates under the common GW rate. | A for those kernels; an idle X norm or a stronger graph-h claim cannot supply it. |
| U17 | Healing uses full-domain (W_3,J_3) in K109(B''_k;gamma), agreeing with U_2 on the stated core, and source-bearing links 3,4. | L on B''_k and the inherited link-4 set, including the boundary of the matching core. Equality on the core does not prove an exterior local model. | PL109 under the full membership hypothesis and ceilings; A still needs the reached-base tube and completion carriers. |
| U18 | Weighted (T)/(L) layer bounds and a cut P_1 tail. | Inherited L and admissible profiles. The separate product-profile estimate for P_1(cut A') must also be furnished; N alone is not that estimate. | Inherited A for those kernels; the cut multiplication creates no new inverse admission. |
| U19 | Stage frame B, full K_P membership, block datum (0,b) of the stated size. E needs the actual stage/chart identity and the uniform radii. | L on every stage frame, with common M/M_1, current, switch and torus floors. The asserted global membership supplies S1/S2 on its own reads, not the missing match to all PI reads. | PL109 under the full K_P hypothesis; A needs the complete carrier domain and larger-ball inclusion. The independent stage-space identity is retained. |
| U20 | Only the constant 66 B_H K_cv is used. | Inherit the common L/N of U19; no new geometry. | Inherit U19's A; no new average. |
| U21 | Frozen B in the step and its enlarged B_(k+1) heredity source; raw and starred points are distinct. Datum entry also needs C_H^sharp>=1/80, supplied by the source's max(C_H^sharp,1) normalization. | L must hold on the full heredity image at both kinds of point. The source explicitly notes that the omitted (3.35)–(3.38) conditions prevent direct use of the cited minimizer proposition. | A for that image and its actual analytic tube; a real critical point alone supplies neither. PH applies only to its physical subcase. |
| U22 | Distinct localized B_Z, explicitly assumed to have the same constants and the whole ambient continuation domain. | L for B_Z and the ambient coefficient reads. U08 concerns different sets and does not prove this assumption. | A for B_Z, including its collar and full continuation tube, not the two earlier localized charts. |
| U23 | Zero off Y by component splitting of a furnished response. | Inherited L plus full-footprint component confinement and zero datum. A freely extended bounded second slot does not show that the field forcing vanishes there. | Inherited A, including rows crossing the component boundary before confinement is imposed. |
| U24 | Localized B_Z outside the earlier space geometry, at the exponential H_max profile and prescribed shift ceiling. | L on this B_Z with that profile, exactly the additional local input 10 assumed by the source. | A on its shifted domain, not inherited from an unrelated local geometry. |
| U25 | Continuation gluing for the later operation, using (a),(f). | Inherited L, actual datum support and full-footprint confinement. Zero extension of the current does not imply the corresponding field identity. | Inherited A throughout the gluing overlap, with its fixed branch. |
| U26 | Completion kernels, raw points and separately handled core. E/N require the actual G'' sources described in §3.4. | L for each completion operator's actual determining set and boundary conditions. The asserted field graph bound at I 142537 is the unresolved operator match of §3.1. | A for raw and core completion bases, with their full collars; value decay does not supply it. |
| U27 | All-block dilation on B=B_k^(n), full K_P membership, j=0, all complex product data. The local second slot is chi_t J^sharp[1]. | L for that stage frame on the full product domain; verify delta_0/8<=delta_* and the stated room/floors against (A1)–(A2). All named bump, entry and weighted hypotheses remain. | PL109 where full membership supplies its representative; A needs every reached carrier and complex ball. The independent stage-family identification remains an input. |
| U28 | Reuse of U27's source-free response data with extra A-slot hypotheses. | Inherit precisely U27's L; the extra hypotheses do not extend the operator domain. | Inherit U27's A. |
| U29 | Cut-current formula for a furnished bracket. | No new L in the formula; each originating bracket still needs L/M. Only the P_1 term is nonlocal in the cut multiplier. | No new average; inherit the bracket's A. |
| U30 | Parameterized brackets, then their composition with a carrier. | L/M for the originating kernels and actual compositions; joint admission on the stated parameter domain is still needed. | A for those kernels and each additionally evaluated carrier. Holomorphic notation alone gives no enlarged domain. |
| U31 | On both frames, B(t,tbar)=Q_B(W;eta(t+tbar zeta)H^w) is the block datum. The value estimate for Q_star gives a candidate size bound. | L on both actual bases, with E on the full tbar disc. The separate cross-grid comparisons B1,B2 are not consequences of L. | A must include this nonlinear datum's whole path. Prove its bound fits the layer radius on the full disc; a derivative/value estimate on a smaller chart is insufficient. |
| U32 | Exactly paired critical parents U(B^+,exp(i beta)V_0), sigma=1, complex beta and block data. E/PH and the stated refinement/relative-real-slice inputs identify the physical response. | L for both physical constructions on their common continued domain; exact pairing does not certify the local models. | A and the actual minimizer tubes for both cutoffs, including the finer collar. Holomorphy extends an identity only within this paired family. |
| U33 | General rippled parents and the desired comparison on their full domains. E on each side would give separate solutions, not RC. | L for both frames plus the native paired-domain, extension, multiplier and Holder hypotheses of §5.8. The off-shell and switched comparison steps in §6 are additionally missing. | A on both complete carrier families, including the finer collar and the complex ancestor tube; real-reference B98 admission alone does not compare them. |
| U34 | The literal relaxed earlier-frame class, with only (3.35),(3.37), pointwise clauses on Y^+ and cutoff independent current. | Missing L at every boundary-crossing patch and matching the whole stencil across partial Y. The relaxed tests do not imply S1-loc/S2+; zero extension of J does not repair them. | Missing S^pl or a supplied frame on all positive-height carriers and their complex balls. The known cube-only counterexample rules out deriving this merely from the two quoted conditions. |

The table ends every admission attempt at a specific local-model,
carrier, domain or operator identity. It does not assert that failure
to find a certificate is a theorem excluding the actual construction.
In particular there is no new no-go for the general layer theorem.

## 5. Clause (e)

The literal statement is still not recovered. The source census in
layer-find and the direct invocation readings give two distinct facts:

1. The concrete arguments consume existence/uniqueness and holomorphy
   (a), the repaired four-entry estimates (b), covariance/reality (c),
   the physical identification (d), component localization (f), the
   field-datum substitution and the current rider. No additional
   inequality, identity or domain property called (e) is exhibited
   by those calculations.
2. U01, I 72392–72399, nevertheless assumes the whole (a)–(f) theorem
   and later asserts its transfer. U08, I 94839–94843, includes (e)
   among the side clauses whose applicability is asserted. These
   blanket statements are themselves two uses of an unspecified
   predicate. They cannot be certified by checking only (a)–(d),(f).

There is a precise elimination argument for the **displayed concrete
consequences**. Replace each invocation by its inputs in the final
table: uniqueness in the same datum ball gives zero and gluing;
equivariance gives covariance; real conjugation gives reality; PH
gives the physical identities; the four native norms and the furnished
current representation give the rider bounds. These deductions have
no residual occurrence of (e). U15 even needs only the defining
seminorm triangle inequality. This verifies that inventing another
estimate and naming it (e) would supply no missing displayed calculation.

It does **not** prove the stronger sentence “no use needs (e).” In
logical terms, from proofs of predicates A,B,C,D,F one cannot prove
an unknown predicate E merely because no formula for E was supplied.
The attempted recovery fails at specifying that predicate, before a
mathematical proof can start. The attempted deletion fails at U01's
whole-package transfer and U08's side-clause assertion. One must either
recover the literal clause from a source, or explicitly weaken those
two assertions to their named concrete consequences. This note makes
neither change to the account. Letters (e) in §5.8's comparison/size
lemmas are clauses of different statements and do not recover the
missing layer clause.

## 6. Relative comparison at U33

### 6.1 The existing theorem, with its actual response

The six-residual comparison in CA-II §5.8 is already written out at
55882–56284; the energy-difference lemma is at 57711–57865 and the
three-member consequence at 58123–58205. This part of the target is
covered there and is not rederived here. It rebuilds Balaban's
comparison method under the native assumptions it lists. Its input
status is conditional on those assumptions, not on an index's word
“PROVED.”

The definitions at II 53598–53822 matter. Its response is the unique
small constrained critical point X of

    Sigma_0(X;U,m) = W_U(X) + (1/2)<L X,L X> - <C_U(X),m>,
    L=R D*,       Q_U(eta X)=B.                           (C1)

Here W_U is the action with its constant and linear terms subtracted;
m is an independently admitted block vector. In the presented-pair
response m_P=H_U^dagger J with the H_U fixed by that construction.
The transpose and quadratic pairing are the native physical bilinear
ones, complexified when the data are complex. They are not Hermitian
pairings that would destroy holomorphy. The response in this theorem
is fixed by its variational definition, not by substituting an
equivalent-at-one propagator representation.

Its two lattices are exactly paired, Omega'_(j+1)=Omega_j. The finer
Lambda'_0 collar remains part of the domain. The theorem assumes real
references U',U,W=M(U'), the prescribed C^beta regularity and closeness,
and small complex m,m'. It also assumes the weighted calculus,
constraint and divergence comparisons, the six-residual identity,
local background/nesting and extension comparisons, and the specified
averaging derivative bounds. Its N^Delta norm also includes the
gradient Holder seminorm, II 54305–54373; it is stronger than merely
the graph norm used for A' in this note. That native input must not
be replaced by N[U33]. For weights p,M,p_delta it requires

    p in M_rho, M in M_tau^A, p_delta in M_(rho+tau),
    rho+tau <= 5 delta_1, M<=1, p_delta<=4p,               (C2)

as well as the stated sup/radius bounds, the collar datum bound,
|a|,|m'-m|,L^(-theta lambda) <= M, and its metric/scale floors.
Its conclusion is

    |Y[X']-X|_x <= C_B^sharp (A p M+p_delta)(x).           (C3)

Complex final block and slot data are already allowed at these real
references. Their extension requires no new Schwarz argument here.

For the nonzero profiles isolated in layer-pkg §9.1, choose
p=|b| exp(-2.5 delta_1 d) and a mismatch majorant M at rate delta_1.
The rate sum is 3.5 delta_1<5 delta_1. If a needed datum discrepancy
is bounded by c p M, the constant in the weight inequality also
matters: p M belongs to M_(rho+tau)^A, not automatically to
M_(rho+tau). By the existing hull properties (w1)–(w2) at
II 54305–54373, take p_delta=c (p M)^[rho+tau]. Then
c p M<=p_delta<=c A p M. This meets p_delta<=4p when c A<=4
(or the corresponding smaller supremum bound for M is supplied).
It must still meet the theorem's absolute radius ceiling. The
zero-profile case follows from zero-data uniqueness when the prescribed
data vanish, or by a positive majorant limit when that is the chosen
formulation. The other radius, collar and native
hypotheses do not follow from this arithmetic. This is the existing
conditional profile supplier; a new profile proof would repeat work.

### 6.2 A precise obstruction to transferring that theorem to (S5)

Further bounded reading finds the account's explicit distinction at
II 58620–58685, the remark on the two off-shell extensions. It states
that replacing J by the independent current in **every** propagator,
including H, uses instead the constrained critical point of

    Sigma_off(X)=W_U(X)-<C_U(X),m_P>
                          +(1/2)<L X+h_P C_U(X),
                                  L X+h_P C_U(X)>.       (C4)

On shell the responses agree; off shell they are two extensions.
The account marks the two-cutoff comparison for (C4) outstanding.
This supplies a specific failed identification, not merely a missing
citation in layer-pkg. The h_P in (C4) is a coefficient of the gauge
condition, unrelated to our response h=A'-HX.

Here is the exact extra residual if one tries to use (C3) without
changing its proof. Freeze the base, put C=C_U, and write K=h_P.
Expanding the two bilinear squares gives

    Sigma_off-Sigma_0 = <L X,K C(X)>
                                  +(1/2)<K C(X),K C(X)>.

For a tangent u to the nonlinear constraint, differentiation gives

    r_P(X)[u] = <L u,K C(X)>
                      +<L X+K C(X),K DC(X)u>.            (C5)

Thus a critical point for (C4) is a critical point for (C1), with
the same m, only if r_P(X) vanishes on every such tangent. The
available one-cutoff bounds do not assert this identity. Also the
vector m must be matched: H_U^dagger J in (C1) cannot be replaced
by a current-dependent H_P^dagger J without a comparison of those
vectors. These are exact algebraic requirements. At nontrivial
switches one must first establish the nonlinear constraint and
stationarity equations themselves for the reduced switched response;
the unswitched inverse identities cannot establish them.

Trying instead to include the difference of (C5) in the six-residual
proof reaches the analytic failure named in that same remark: a
zeroth-order operator acts on a mismatch e_s controlled only in the
supremum norm. Tempering the weight changes decay, not the order of
that operator. The proposed route requires a Holder mismatch norm
and its preservation through the step. The account lists the seed
C^1 bound, the interpolated C^epsilon bound for fresh terms, and a
stability increment in C^1, but does not prove the preservation
statement. N[U33] bounds each layer separately; it neither compares
the coefficients K,m nor supplies that Holder mismatch bound. This
is where this transfer attempt stops. The global stage-response
identification remains with its registry owner, shift-map; it is
not solved by redefining the response here.

### 6.3 Checking the two possible continuations

**Complex ancestors.** The later corollary II 58369–58489 was checked
to avoid overlooking an existing supplier. It allows complex
ancestors only under holomorphic stage admission on 4 times the
ancestor polydisc, one-cutoff size there, and a real-trace presentation
bound. Its two-constants argument gives a square root of the mismatch
smallness. Its last paragraphs explicitly say that the corresponding
linear bound at complex ancestors is not asserted and would require
the response analysis on complex backgrounds. Therefore it cannot
prove the linear RC requested at U33 on its whole parameter domain.
Even its square-root version retains the real-trace growth hypothesis;
that is not obtained by the invocation alone.

**Switches.** The proposition and proof at II 58490–58619 distinguish
the presented-pair parameters from the switch family of walks on one
geometry. For the latter the only natural vertex is sigma=1.
At sigma=1_Y the walk sum is confined to Y, and both constraint and
stationarity acquire walk-sum defects. A comparison of these defects
between the two lattices is expressly unproved. Bounds at vertices
and separate one-cutoff bounds yield only
min(2^|B| beta,q^|B|G) for the Mobius coefficient, not the full-disc
small comparison. The source's polynomial example already proves
this distinction; it is not rerun here. Its conditional full-disc
statement assumes the desired comparison throughout that disc.
No analytic-continuation argument removes this hypothesis.

**Admitted subcase and exact end of the attempt.** At sigma=1, for
the response defined by (C1), with the paired real references and
all native hypotheses above, (C3) and the three-member comparison
are covered by CA-II §5.8. PH transfers a physical paired family
where the responses have actually been identified; U32 is of that
kind. General rippled independent-current parents in U33 still need
the (C4)/(S5) source-and-response identification, the estimates for
the added residual (C5) in its native norm, paired-domain/collar
admission, and the claimed extension to complex ancestors or
confined switches whenever those are in its domain. These are not
new names for the already proved six-residual theorem. They are the
precise hypotheses or additional residuals missing at its application.

## 7. Recovery and U01–U34 coverage

The following deductions were added in this round: the switched-current
defect (M3), the two zero-switch tests with their limited meaning,
the coefficient bound (M5), FD from GW's stronger endpoint estimate,
the invertible calibrated conversion (F4), the admission implications
and the explicit extra variational residual (C5). The established
PI/GW/B98 local results, the U07 repair, the cutoff repair, and the
§5.8 six-residual comparison were reused. There was no experiment,
computer-assisted proof, Lean check or independent review in this round.
All arguments added here are symbolic finite-dimensional algebra or
norm-convergent series estimates, with hypotheses and limits displayed;
they can be formulated as lemmas for Lean without an empirical oracle.
This is not a claim that their formalization has been carried out.

The unfinished suppliers are explicit: the current's actual switched
word assignment M; FM for the prescribed source-bearing links; the
per-use local-model/carrier/domain inclusions of §4; the literal
clause (e); and RC's added off-shell, complex-background and switched
comparisons. These are not inferred to be impossible. No scientific
status, registry entry, queue, prompt or platform instruction is changed.

For recovery, keep this note with `checks/layer-r3/checkpoint.md` and
its source-identity manifest. The next decisions are whether the actual
current and force conventions have literal suppliers, and which named
domain can first be given its complete L/A certificate. Do not reopen
the already covered profile theorem or the known graph-h counterexample.

The table reports only the **layer content consumed**. “Covered” may
be an implication from the consumer's expressly furnished objects;
it does not assert existence of those objects. “Covered conditionally”
names the extra inputs for the actual family. “Not covered” marks a
literal unfilled package or identification rather than silently replacing
it by a different theorem. Every Loc/Avg/E entry refers to the specific
domain and failing step in §4.3, not an unqualified class label.

Named inputs, in addition to Loc/Avg/E/M/N of §4.1:

* **GW**: walks-gw's theorem, its common constants, full footprints,
  physical pairings, product tags and (P18).
* **V[U]**: only the graph A' and first-order h estimates from E[U]
  and GW. It needs no identification of the rider's m_H.
* **FD[U]**: (F1) plus identification of the use's actual operator
  and force in its source space; **FM[U]**: the exact force identity
  (F2)/(F3) for its prescribed datum, including its branch.
* **LC**: component splitting on full footprints with both data
  zero on the component, layer-pkg §3. It is not inferred from the
  independent current alone.
* **EQ**: covariance/conjugation of the actual equations and uniqueness
  on the common admitted domain, layer-pkg §3.
* **PH**: the unswitched own-current identification K6,
  I 15669–15701, with admitted physical chart and its continuation
  within that paired physical family.
* **R[U]**: the local coefficient and transport hypotheses of
  layer-pkg §5.1 on the actual base and cut field. For a cut rider
  include its collar, p_W<=1, N_y(chi h)<=1/40 and cutoff hypotheses;
  use the repaired cutoff (5.7)–(5.8), not the impossible printed
  second-derivative bound. For an uncut current use the uncut version.
* **TL**: U07's proved linearization T^L=T H_0 and its graph bound,
  layer-thm-gate §8 / layer-pkg §6.1; **RC**: the still incomplete
  transfer specified in §6 of this note.

All weights/rates in N or V and all intermediate images in E are
quantified on the full domain. These conditions cannot be dropped
when a line uses a constant previously obtained from them.

| Use and source | Field convention | Updated coverage, with named inputs |
|---|---|---|
| U01 — I 72373–72538 | Field-datum substitution at I 72534. | **Not covered in full.** Its concrete (a),(b),(c),(d),(f), corollary/rider follow conditionally from Loc/Avg/E[U01], GW, M/N[U01], R[U01], EQ, PH, LC, FD[U01], FM[U01]. The whole (a)–(f) transfer additionally has the unspecified (e), §5. |
| U02 — I 73103–73140 | Link 3 prescribes tilde G_0(sigma)J_3; linked source calls inherit it. | **Covered conditionally** on Loc/Avg/E[U02] for all four sets, GW, M/N[U02], R[U02], LC, FD/FM[U02], and the induction's full membership and datum-size hypotheses. PL109 is available only under that full membership and its inclusion ceilings. |
| U03 — I 73546–73633 | Inherits U02 on the product switch domain. | **Covered conditionally** on Loc/Avg/E[U03], GW and FD/FM[U03] where source-bearing; every intermediate image must be admitted on that product. The existence/parameterization claim itself needs no new m_H estimate. |
| U04 — I 89955–90008 | Source-presentation convention is an input. | **Covered conditionally** on Loc/Avg/E[U04], GW, M/N[U04], R[U04], LC, FD/FM[U04] and its explicitly furnished presentation hypotheses. Those hypotheses do not prove their own operator match. |
| U05 — I 94180–94286 | Block-only local charts; independent base current allowed. | **Covered conditionally** as a radius choice after Loc/Avg/E[U05], GW, M/N[U05] where the full four-entry constant is used, and the stated real/perturbed-base and core admissions. The missing boundary frames and tubes are those in §4.3. |
| U06 — I 94303–94422 | j=0 in both calls. | **Covered conditionally** by Loc/Avg/E[U06], GW and full-bidisc size/admission of d_0,f. Zero at zero is an (S5) uniqueness consequence and needs no PH or FM. |
| U07 — I 94448–94586 | j=0 linearization. | **Covered conditionally for T^L** by Loc/Avg/E[U07], GW and TL; PH only for the physical identification. The alternate T^sharp is not identified with T^L and receives no graph bound from this argument. |
| U08 — I 94608–94843 | Block-only localized calls. | **Not covered as the full scope assertion.** Loc/Avg/E[U08], GW, M/N[U08], R[U08], EQ and PH give the named concrete conclusions once the §4.3 boundary/collar and whole-domain steps are supplied. Clause (e) remains undefined. Conditions (c1)–(c3) alone do not complete those admissions. |
| U09 — I 94846–95085 | Same two block-only families. | **Covered conditionally in the repaired consumed norms** by Loc/Avg/E[U09], GW, M/N[U09], R[U09] and whole-bidisc admission. Use first-order h and graph A'; the printed graph-h shorthand is not supplied or needed. |
| U10 — I 95682–95700 | Block chart already furnished. | **Covered conditionally** by inherited Loc/Avg/E[U10] and EQ on its conjugation-stable domain. Conjugating the unique solution and differentiating proves the stated reality. |
| U11 — I 95750–95790 | Unswitched physical block chart. | **Covered conditionally** by Loc/Avg/E[U11], PH, EQ and TL when its derivative bound is used, with the explicitly matched free-current identity on the shifted base. Criticality alone does not supply its minimizer tube. |
| U12 — I 95872–95908 | Same admitted physical/holomorphic overlap. | **Covered conditionally** by inherited Loc/Avg/E[U12], EQ and the admitted overlap (PH for its physical reading). The T^sharp form retains its separate (3.36) condition and remains a different form. |
| U13 — I 99780–99796, 99878–99892 | No new force conversion. | **Covered conditionally** as the ordered choice of common constants after Loc/Avg/E[U13], GW, M/N[U13], R[U13] for the two local systems. “Four floors” alone is not the exterior-model or uniform-domain certificate. |
| U14 — I 111489–111732 | A furnished triple/current, no new field call. | **Covered as a rider implication** by layer-pkg §5, the furnished representation M[U14], R[U14] and the repaired cutoff. Its origin still needs its own admission. This implication uses no fresh PI inverse or B98 average. |
| U15 — I 112180–112230 | No force map used. | **Covered** by h=A'-HX, the defining seminorms and the source's own bound (e2). The triangle inequality proves the consumed conclusion; N, PI and B98 are unnecessary here. |
| U16 — I 112580–112650 | Inherited from each furnished layer. | **Covered conditionally** on Loc/Avg/E[U16], GW, M/N[U16] at both specified exponential weights, their GW rate admission and the actual datum norm. FD/FM is inherited only for a source-bearing origin. The idle X norm is unused. |
| U17 — I 114790–114880 | Source-bearing healing links. | **Covered conditionally** on Loc/Avg/E[U17], GW, M/N[U17] at weight one, R[U17], FD/FM[U17] and the separate amplitude/composition/core hypotheses. PL109 uses the stated full K109 representative; the completion tube remains to be admitted. |
| U18 — I 115382–115410 | Inherited (T)/(L) data. | **Covered conditionally** on Loc/Avg/E[U18], GW, M/N[U18], R[U18], admitted weights, inherited FD/FM where applicable, and the separately stated product-profile bound for the P_1(cut A') tail. N alone does not prove that last bound. |
| U19 — I 116555–116669 | (0,b); base current may be independent. | **Covered conditionally** on Loc/Avg/E[U19], GW, M/N[U19], R[U19], the actual stage/chart identification and all datum/collar/switch ceilings. PL109 follows under its full K_P and inclusion hypotheses; it is not a complete Loc/Avg certificate. |
| U20 — I 125775–125792 | No new field call. | **Covered conditionally** by U19's admitted response-size constant V[U20] (or its stronger N[U20]) and the separately supplied K_cv. These give the finite 66 B_H K_cv used here; no new m_H identity is needed just to multiply constants. |
| U21 — I 131621–131695 | (0,b) on a frozen set. | **Covered conditionally in the repaired norms** on Loc/Avg/E[U21], GW, M/N[U21], R[U21], PH in the physical subcase, the heredity-image admission and the source's normalization C_H^sharp to max(C_H^sharp,1), or an explicit equivalent datum ceiling. |
| U22 — I 131725–131746 | Block data at B_Z. | **Covered conditionally** on Loc/Avg/E[U22], GW, M/N[U22] for the entries actually used, PH and the expressly assumed same-constant certificate on the full B_Z continuation domain. U08's domain is a different supplier. |
| U23 — I 136750–136770 | Source support matters if its origin has a field datum. | **Covered conditionally** by Loc/Avg/E[U23], GW, LC and FD/FM[U23] where present, with both actual data zero on every off-Y full footprint. A bounded independent-current extension supplies only the second slot. |
| U24 — I 137562–137603 | Localized response on its stated domain. | **Covered conditionally** on Loc/Avg/E[U24], GW, M/N[U24] at the specified exponential profile and the source's extra local input 10 including its shift ceiling. This source explicitly lies outside the earlier space geometry. |
| U25 — I 137978–138001 | Actual datum and support convention inherited. | **Covered conditionally** by Loc/Avg/E[U25], GW, LC, FD/FM[U25] when source-bearing, and the admitted branch overlap. Continuation gluing consumes rather than proves the full-footprint support identity. |
| U26 — I 138640–138667; field estimate I 142530–142543 | Actual G'' completion sources, §3.4. | **Covered conditionally** on Loc/Avg/E[U26], GW, M/N[U26], R[U26], FD/FM[U26] for those exact completion kernels and the separate threshold/frame conversions. Identification of G'' and admission of Q''*mu in its source space are still missing. |
| U27 — II 13888–14105 | j=0; second slot chi_t J^sharp[1]. | **Covered conditionally** on Loc/Avg/E[U27], GW, M/N[U27], uncut R[U27], the stage-family identification and all named bump, room, entry, absorption and weighted-space hypotheses on the full product domain. This is not the cut current J^sharp[chi_t]. |
| U28 — II 15390–15404 | Reuses U27's source-free response. | **Covered conditionally** by U27's same admitted data, Loc/Avg/E[U28], GW and M/N[U28] where reused, together with the separate A-slot assumptions. No new construction or admission is proved at this line. |
| U29 — II 20790–20808 | Furnished bracket, no new force equation. | **Covered conditionally as a current formula** by its furnished M[U29], R[U29] and layer-pkg (5.2), with the bracket's domain/locality hypotheses. Loc/Avg/E and any FD/FM belong to its originating call. |
| U30 — II 23160–23177, 23990–24005 | Furnished parameterized brackets; source-bearing origins retain FM. | **Covered conditionally** by Loc/Avg/E[U30], GW, M[U30], R[U30] and N[U30] when bounds are read, full parameter/carrier admission and inherited FD/FM where applicable. Parameterization does not identify a different source convention. |
| U31 — II 51814–52070 | Nonlinear **block** datum, not a field force. | **Covered conditionally** by Loc/Avg/E[U31], GW, V[U31], the complete averaging-domain/size bound for B(t,tbar) and the separate cross-construction B1,B2 comparisons. Its value use needs no rider m_H. |
| U32 — II 52107–52186 | Exactly paired critical block-data families, sigma=1. | **Covered conditionally** by Loc/Avg/E[U32], PH, exact pairing and the source's refinement/relative-real-slice hypotheses. Identity extends on that paired family; it does not identify independent-current responses. |
| U33 — II 52390–52518 | Two-cutoff response/slot match is RC, not single-call FM. | **Not covered on the full family.** CA-II 55882–56284 and 58123–58205 already supply the conditional comparison for (C1), with (C2) and all named native hypotheses. For U33 one still needs Loc/Avg/E on both sides, the source-vector/response identification, control of (C5), full paired-domain/collar admission, and its complex-ancestor/switched extension where claimed. §§6.2–6.3 locate the exact failures. |
| U34 — III 49210–49230, 49272–49288, 49454–49502 | Source-bearing earlier links require their field support/FM. | **Not covered on its literal relaxed class.** Loc/Avg/E[U34], GW, LC and FD/FM[U34] would supply the named existence/locality consequences, but the two stated coarse conditions give neither all-anchor S1-loc/S2+ nor the carrier/tube certificate nor the crossing-boundary field identity. |
