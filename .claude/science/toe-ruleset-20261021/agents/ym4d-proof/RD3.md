# RD3 — a positive failed history, its normalized next step, and the remaining estimates

**B2/B3 at the requested uniform RG scope: OPEN.** This note constructs a
specific RD history with a nonempty failed component and a genuine hole. It
proves positive references on that history, a common **finite-volume** complex
domain, a comparison after the remaining integration, and the full-norm hole
cost. It does not establish a source radius independent of volume, small
local interactions on this history, a Peierls bound in the required reference
law, or closure of the quantitative effective-level induction.

PROVEN means the written mathematical implication at its stated scope;
ARGUED identifies a proposed next construction; OPEN names an unmet estimate.
No audit status is assigned. Source identities and independent review are
recorded in [RD3_LOG.md](RD3_LOG.md). [RD.md](RD.md) is unchanged.

The small/large-field method is due to Tadeusz Balaban. Jonathan Dimock's
[Part II](https://arxiv.org/abs/1212.5562) and
[Part III](https://arxiv.org/abs/1304.0705) explain the method for scalar d=3.
They supply attribution, not an SU(N) theorem used here. All new estimates
below are proved in the text; LIB1 R10 is the explicitly authorized reviewed
input. There is no load-bearing memory-only [m] item.

## 1. A real history, with a positive-measure witness — PROVEN

Use precisely RD (R1)–(R6), including its H12 completion convention. Fix
N≥2, odd L≥3, real u_0,u_1,κ>0 and t_j=κu_j. Take compatible finite periodic
lattices through level two so that the level-one **block** graph is
Γ_1=(Z/TZ)^4, T≥7. The level-zero block graph has side LT. Write E_j for
level-j links and P_0 for the number of original Wilson plaquettes. Sources
ε_p occur only in the original Wilson action. Set both interior curvature
cuts to ε_cut,0=ε_cut,1=1. This is a legal fixed cut, not an assertion that
it meets a small-chart theorem. Set n_0=n_1=1; the positive completion
thresholds remain arbitrary.

Choose two adjacent Γ_0 blocks Y_0={q_0,q_0+e_1} inside the same containing
Γ_1 block v_0. Translate v_0 to 0. Fix the one-stage failure history

    h=(F_0),             F_0={Y_0}.
    H_1=N_1(π_0(Y_0))={−1,0,1}^4,       |H_1|=81.       (D1)

N_1 here is RD's sup-distance collar. H_1 is also connected in the face
graph. Since T≥7 it has no wrap identifications. The active set is
A_1=Γ_1\H_1. For the next local quotient choose B={v_*}, v_*=(2,0,0,0).
Thus B is active and face-adjacent to the hole. No hole field is deleted.

Here is a field witnessing that this is a positive-mass history, rather
than a formally legal zero summand. In each of the two blocks put

    g=diag(−1,−1,1,…,1)∈SU(N)

on the oriented e_1 link based at within-block coordinates (1,1,1,1); put
identity on every other level-zero link. Every plaquette reading either
marked link stays inside its block: its transverse coordinates range from
0 to 2 and its e_1 coordinates from 1 to 2. Such a plaquette equals g or
g^−1, so its distance from identity is 2. Every other plaquette is identity.
Consequently the bad-block set is exactly Y_0. Its unique G_2 component
has size 2>n_0, so it fails regardless of U_1 or the completion test.

Let δ=1/16 and vary every link in an open operator-norm δ-ball about this
field. Telescoping a product of four unitary factors bounds its plaquette
change by 4δ=1/4. Good plaquettes remain below the cut 1; the displayed bad
plaquettes stay above it. On this whole product set Ξ_h=1 **for every real
U_1**. It is a subset used for a lower bound; the actual history still
includes all its other configurations, including successful components.

For explicit mass bounds put

    m_δ=(1+4√2 N/δ)^(−2N²),
    l_h=m_δ^|E_0| exp(−2u_0 P_0−2t_0|E_1|),
    u_h=exp(2t_0|E_1|).                                    (D2)

Every Haar δ-ball has mass at least m_δ. To verify this bound, embed SU(N)
in the 2N² real entry coordinates in [−1,1]. Subdivide into cells with side
at most δ/(2√2 N). The number of cells is at most
(1+4√2 N/δ)^(2N²) and their Frobenius diameter is at most δ/2. Representatives
of occupied cells give a cover by translates of the open δ-ball; Haar
invariance proves the bound. Also 0≤s≤2, ||M||≤1 gives
e^(−2t)≤N_t(M)≤1 and e^(−2t)≤k_t≤e^(2t). Hence the actual inherited density

    ρ_{1,h}^ε(U_1)=∫Ξ_h(U_0,U_1)e^(−u_0Σ_p(1+ε_p)s_p)
                                      K_0(U_1,U_0)dU_0

obeys

    0<l_h≤ρ_{1,h}^0(U_1)≤u_h                              (D3)

uniformly over all real U_1. The lower bound uses only the witnessed cap;
the upper bound integrates the full Haar probability. In particular this
history has positive mass on all of the real fibres used below. Its very
small l_h is a global finite-volume lower bound, not a local Peierls price.

**Scope.** This constructs one permitted history at the specified cuts. It
does not replace the small thresholds, large size cutoffs or legacy σ-history
needed by another consumer. A version with such parameters must prove its
own witness and estimates. The method can be tried on a larger failed set;
no all-history estimate follows from the present example.

## 2. The actual next quotient and a complete normalized step — PROVEN

Let I(B),P_1(B),C_1(B) be RD's current interior links and their plaquette and
kernel readers. Freeze **all** η=U_1 outside I(B), including the hole fields.
Set c_B=|C_1(B)|≤8, n_I=4L³(L−1), and define the explicit bookkeeping factor

    a_B(η)=exp{u_1Σ_{p∉P_1(B)}s(U_{1,p})}.

These exterior plaquettes read no variable integrated in the local quotient.
Substitute J_{1,h}=ρ_{1,h}/b_1 into RD (R6). The actual expressions are

    D_h^ε(η,V)=a_B(η)∫χ_B(U_1)ρ_{1,h}^ε(U_1)
                          Π_{c∈C_1(B)}k_{t_1}(V_c;M_c(U_1))dU_{1,I(B)},
    N_h^ε(η,V)=a_B(η)∫ζ_B(U_1)ρ_{1,h}^ε(U_1)
                          Π_{c∈C_1(B)}k_{t_1}(V_c;M_c(U_1))dU_{1,I(B)},
    r_h=N_h/D_h.                                           (D4)

Thus b_1 did not approximate the inherited density: its **exterior inverse**
a_B survives. It cancels in r_h, but not in D_h. The full conditional
denominator convention is O_{1,B}D_h, with

    O_{1,B}=a_B^−1 Π_{c∉C_1(B)}k_{t_1}(V_c;M_c(U_1)).       (D5)

No earlier kernel normalizer or history is absent from ρ_{1,h}. All earlier
fields remain integrated. The numerator here is the R6 bad integral without
an additional current insertion. If a current completion/failure selector
is needed it must also be retained, as in R6/R8. In particular, with η=1,
the identity interior is a completion and e_flat≤max_{c∈C(B)}||V_c−1||.
On the real patch where this maximum is below ε_loc,1, B is a successful
return and its raw quotient is exactly (D4). This identifies a nonempty
real consumer patch; it does not analytically continue a moving indicator.

Choose any real Vbar. The exact reference Nref_h=D_h^0(η,Vbar) satisfies

    a_B m_δ^n_I l_h e^(−2t_1 c_B) ≤ Nref_h
                              ≤ a_B u_h e^(2t_1 c_B).     (D6)

The lower current cap puts all I(B) links near identity and hence satisfies
χ_B, independently of η. This proves (D6) using (D3). Replacing one internal
link by g gives a positive cap for N_h as well, though no lower numerator
bound is needed. The resulting real quotient estimate is only

    0≤r_h^0≤m_δ^(−n_I) (u_h/l_h) e^(4t_1 c_B).            (D7)

Its right side grows with volume and coupling. It is not a small returned
activity bound and gives no Peierls suppression.

To perform the next integration rather than stop at its local quotient,
retain h and sum **all** current failures:

    R_h^ε(V)=∫ρ_{1,h}^ε(U_1)K_1(V,U_1)dU_1
            =Σ_{F_1}ρ_{2,(h,F_1)}^ε(V),
    A_h^ε=∫ρ_{1,h}^ε(U_1)dU_1,
    p_{2,h}^ε(V)=R_h^ε(V)/A_h^ε.                          (D8)

The first equality to the failure sum follows from the pointwise partition
Σ_{F_1}I_{1,F_1|h}=1; no selected term is substituted for that sum. Each
normalized Decision-4 kernel integrates to one in its output, so

    ∫R_h^ε(V)dV=A_h^ε,       ∫p_{2,h}^ε(V)dV=1             (D9)

whenever A_h^ε≠0. For real zero sources,

    l_h≤A_h^0≤u_h,
    l_h e^(−2t_1|E_2|)≤R_h^0(V)≤u_h e^(2t_1|E_2|).       (D10)

This is a complete normalized finite step on this past history. Division by
A_h is explicitly conditioning on h. For the full unconditioned step its
weight A_h/Z_0 must be retained, where Z_0=∫ρ_0. Summing over all h gives
Σ_h A_h=Z_0; summing their unnormalized R_h recovers ρ_2. Equations (D8)–(D10)
close algebra and positivity, not the desired local effective-action bounds.

## 3. One common complex domain, with its loss displayed — PROVEN

Keep η real. For each new coarse link let V_c=Vbar_c exp Z_c,
Z_c∈sl(N,C), with Vbar real. Use RD's exact continuation

    k_t^C(V;M)=exp{−t[1−(tr(V^−1M)+tr(M*V))/(2N)]}/N_t(M).

All M are evaluated on real integration/frozen variables, so M* does not
conjugate an analytic parameter. The original selectors in ρ_{1,h} do not
read the new V. Their bounded measurability does not prevent source or
terminal-V holomorphy. A **new** selector I_{1,F_1|h}(U_1,V) is not covered;
this is why (D8) summed F_1 before making this claim.

Let C_tot=|E_2| and choose

    ρ=1/(8u_0P_0),
    α=min{1/4, log(1+1/(4t_1 C_tot))},
    D_fin={|ε_p|<ρ for all p, ||Z_c||op<α for all c}.       (D11)

P_0,C_tot are positive in the displayed lattice. The comparison of an
integrand with its positive zero-source integrand at Vbar has the form e^H,
where, for any of D_h,N_h,R_h and their versions with Ξ_h removed,

    |H|≤r=2u_0Σ_p|ε_p|+t_1Σ_c(e^(||Z_c||op)−1)<1/2.      (D12)

Only C_1(B) is needed in the local version of the second sum; using all
E_2 makes the domain common to the complete step. The bound follows from
s≤2, ||M||≤1, ||e^(±Z)−1||≤e^(||Z||)−1 and |tr A|≤N||A||. Kernel
normalizers at both levels are unchanged in this comparison.

For any positive finite reference measure ν normalized to one and |H|≤r<π/2,

    e^(−r)cos r≤|E_ν e^H|≤e^r,
    |Log E_ν e^H|≤2r−log cos r.                           (D13)

Indeed each integrand has real part at least e^(−r)cos r and lies in the
convex sector |arg|≤r. The principal logarithm has real part between
−r+log cos r and r and imaginary part in [−r,r], which proves the bound.
Compact-domain domination proves holomorphy; the right half-plane supplies
the specified branch. The same argument with the terminal sum omitted
applies to A_h. Consequently all of the positive denominators used in
(D4), (D8) and (D9) are nonzero on D_fin (on the source disc for A_h).
These are actual complete integrals, with a hard failed history retained.

For example, N_h/N_h(0), D_h/Nref_h, and R_h/R_h(0) obey (D13), so their
quotient logarithmic variations cost at most 4r−2log cos r. The real patch
identified after (D5) therefore has a holomorphic quotient continuation on
the corresponding local chart at Vbar=1. This does not extend the selected
indicator itself beyond that real patch.

**OPEN — uniform domain.** In (D11), ρ decreases as (u_0P_0)^−1 and α
can decrease as (t_1|E_2|)^−1. These are sufficient radii, not locations of
actual zeros. The fixed-radius coordinator output FR is still required
at the exact all-history scope, or a different proof must replace (D12).

## 4. The hard-cut species and the precise smallness failure

### 4.1 A valid integrated species expansion — PROVEN, conditional estimate

Keep RD's exact hard predicates. Under a **fixed product reference** μ,
write each required indicator as θ_i=1−1_{E_i}, with connected full reader
support S_i. For each overlap-connected nonempty set C of distinct predicate
labels define

    d_C=(−1)^|C| 1_{∩_{i∈C}E_i},       S_C=∪_{i∈C}S_i.

Then Π_iθ_i equals the gas of these d_C with pairwise disjoint supports.
Proof: expand inclusion-exclusion, partition each selected label set into
its unique support-overlap components, and multiply their signs and events.
This identity includes simultaneous failures. In the actual RD construction
the factors include χ_B and I_{0,F_0}, with their full reading sets.

After multiplying by interaction factors f_S=e^(−U_S)−1 and integrating,
every compatible mixed collection has the majorant

    |E_μ Π_S f_S Π_{C∈F}d_C|
        ≤Π_S||f_S||∞ Π_{C∈F} μ(∩_{i∈C}E_i).               (D14)

Take the interaction suprema first; disjoint defect-coordinate sets then
factor under μ. This proves the relevant use of L1 masses, including
overlapping failure events within a type. Using RD §5's two tree sums, the
sufficient input at β=μ_0+2, μ_0≥0, is exactly

    q_1=sup_v[Σ_{S∋v}e^(β|S|)||f_S||∞
              +Σ_{C:S_C∋v}e^(β|S_C|)μ(∩_{i∈C}E_i)]≤1/4. (D15)

Under (D15) RD gives a holomorphic connected logarithm with full rooted
norm ≤q_1. We use this already proved conditional result, not claim a new
cluster theorem. This fixes the hard-cut sup-norm mismatch. It does **not**
prove (D15) for the present history.

If a matched reference producer gives δ_C≤b_C e^(−τ n_C), the exact failure
budget to check is sup_v Σ_{C:S_C∋v}e^(β|S_C|)b_C e^(−τ n_C). For example,
if |S_C|≤c n_C and the sum of b_C at each root and size n is ≤A^n, then
it is at most r_f/(1−r_f), r_f=Ae^(βc−τ)<1. This follows by summing the
geometric series. The budget requires e^h h+r_f/(1−r_f)≤1/4 when
||U||_β≤h. Neither those bounds nor their common measure are given by a
Peierls price under a different law.

RLARGE's reviewed bad-only conditional price and LARGE55 MIS/PRICE have
specific laws and hypotheses. MIS bounds forward mismatch probabilities;
our prescribed Y_0 is a **size-failed fine-curvature component**, not that
event. PRICE needs the unproved effective-action/coercivity inputs.
REVIEW_RLARGE_V3 also identifies the future-tilt/reference gap. None yields
the product-reference joint masses in (D15) for this inherited denominator.
TC therefore remains a named requested input. No coordinator tail theorem
is derived or silently strengthened here.

### 4.2 What happens to a required rare species on normalization — PROVEN

There is an additional issue specific to a nonempty prescribed history.
Let μ be a probability, E a required event with 0<p=μ(E)<1, and d=1_E.
Treating d as a species of an **unnormalized sum over histories** costs p.
For the normalized selected history the insertion is d/p, and

    ∫|d/p|dμ=1,
    e^(β|S_E|)∫|d/p|dμ=e^(β|S_E|)>1/4.                  (D16)

Thus (D15) actually fails for the attempted representation that inserts
this normalized mandatory species as a small defect. It is not repaired
by making p exponentially small. Expanding the required predicate instead
as 1−1_{E^c} costs 1−p, which also fails whenever
e^(β|S_E|)(1−p)>1/4. These statements do not assert a value of p for Ξ_h
under a chosen adapted reference. They identify the error in that use of a
Peierls price. At the purely pointwise level ||θ−1||∞=1 whenever θ vanishes.

**ARGUED — a remaining constructive route.** Extract p as a reference and
use μ_E=1_E μ/p. If E reads only S_E and μ is a product, μ_E remains a
product between S_E and its complement, but its variables inside S_E can
be correlated. Treat S_E as one integration cell, retain its entire
geometric/source size, and re-prove interaction estimates in that norm.
For Ξ_h the requirement of no other failures can be global; splitting it
into mandatory defects and absence conditions must be exact. No locality
or budget for that split is assumed here. This route is not ruled out by
(D16).

## 5. Reference comparison after the actual integration — PROVEN finite scope

For either local denominator D_h or the complete R_h of (D8), let I_h(z)
denote the integral, and I_*(z) the **same** integral with Ξ_h omitted.
Use the same η, kernels, cuts and source-independent a_B in the local case.
Both positive real references are finite and nonzero. After cancelling that
common prefactor, let ν_* be the normalized real zero-source integration
law and p_h=ν_*(Ξ_h)>0. Define ν_h=Ξ_hν_*/p_h. Then, exactly,

    [I_h(z)/I_*(z)]/[I_h(0)/I_*(0)]
          = E_{ν_h}e^H / E_{ν_*}e^H.                    (D17)

This is a ratio of **already integrated** functions. It neither replaces
E exp by exp E nor pulls a boundary activity outside its integral. Every
previous field, hole variable, and surviving history predicate is included
in the two laws. Applying (D13) on their common D_fin gives

    e^(−2r)cos r ≤ |(D17)| ≤ e^(2r)/cos r,
    |Log(D17)|≤4r−2log cos r.                             (D18)

The price p_h cancels from the normalized variation, not from the original
history weight. For the common all-cut reference of R8 the different
Z_{1,A_1}^{cut,0} must still be kept: (D17) compares inherited-history to
unconditioned-history integrals. The following calculation compares to the
actual all-cut reference as well, at finite scope.

### 5.1 The R8 all-cut reference through the remaining integration — PROVEN

Let P_{1,tot} be the number of all level-one plaquettes and set

    Z_A(V)=Z_{1,A_1}^{cut,0}(V)=∫χ_{A_1}(U_1)b_1(U_1)K_1(V,U_1)dU_1,
    Q_h^ε(V)=R_h^ε(V)/Z_A(V).

This Q_h is the whole right side of RD R8 for fixed h after summing F_1,
including its interacting expectation, all B replacements, and all failures.
It is not a successful-gas factor. The missing cuts in H_1 remain missing;
the fields in H_1 are integrated with every reader still present. A cap for
**all** level-one links satisfies χ_{A_1}. Thus for real V,

    z_−:=m_δ^|E_1| e^(−2u_1P_{1,tot}−2t_1|E_2|)≤Z_A(V)≤e^(2t_1|E_2|),
    l_h e^(−4t_1|E_2|)≤Q_h^0(V)
                 ≤u_h m_δ^(−|E_1|)e^(2u_1P_{1,tot}+4t_1|E_2|). (RC1)

The upper bound on Z_A uses b_1≤1, χ≤1 and normalized Haar; the lower
bound and (D10) give both ratio bounds. Unlike (D6), this reference has no
inherited density, exactly as R8 requires.

At a real Vbar, normalize the positive integrands of R_h^0(Vbar) and
Z_A(Vbar) to laws ν_h^R and ν_A. On D_fin,

    Q_h^ε(V)/Q_h^0(Vbar)
         = E_{ν_h^R}e^(H_R) / E_{ν_A}e^(H_A),
    |H_R|≤r,
    |H_A|≤t_1Σ_c(e^(||Z_c||op)−1)≤r.                    (RC2)

Here H_A has no original-source term. Both integrals are actually
performed before the ratio is estimated. Applying (D13) proves that Z_A
is nonzero on D_fin and gives exactly the modulus and logarithm bounds
(D18) for (RC2). The two laws need not agree or be product measures.

Finally integrate the **real** new coarse field with its actual reference
weight, rather than cancel Z_A pointwise and then discard its integral:

    Zbar_A=∫Z_A(V)dV=∫χ_{A_1}b_1 dU_1,
    ∫Q_h^ε(V) Z_A(V)dV/Zbar_A = A_h^ε/Zbar_A,
    m_δ^|E_1|e^(−2u_1P_{1,tot})≤Zbar_A≤1.                (RC3)

This uses (D9) and kernel normalization after the complete integration;
it does not invoke a forward-cone deletion in the presence of readers.
At zero sources the last ratio lies between l_h and
u_h m_δ^(−|E_1|)e^(2u_1P_{1,tot}). Its normalized source variation obeys (D13)
with the terminal sum removed. The original history mass remains in A_h.

These are explicit comparisons through R8's remaining sea integral and
through the terminal reference-weighted integral. Their cap costs are
extensive and their complex radius is D_fin. The local, volume-independent
comparison required by B3 is still OPEN.

### 5.2 The uniform comparison input and a locality diagnostic

A second exact comparison makes that remaining interface explicit. If the
two actual integrands under one measure are w(z,x)e^{g(z,x)} and w(z,x),
then

    I/I_ref−1=∫w(e^g−1)/∫w,
    |I/I_ref−1|≤T_ref(z)(e^a−1),
    T_ref(z)=∫|w|/|∫w|,              sup_x|g|≤a.          (D19)

For a positive real measure, pointwise e^(−a)≤e^g≤e^a gives the same
multiplicative comparison after integration. For a complex reference,
(D19) proves the needed total-variation cost rather than assuming it is
one. If w=w_0e^H, w_0≥0 and |H|≤r, (D13) gives
T_ref≤e^(2r)/cos r. To get a logarithm by this test requires

    [e^(2r)/cos r](e^a−1)<1.                             (D20)

This is an evaluated sufficient finite-domain comparison. It has no spatial
locality conclusion. On the proposed fixed product radius ρ_*>0 the present
bound uses a uniform majorant at least 2u_0P_0ρ_*, so it leaves its sector
range as volume grows. This is failure of this sufficient estimate, not
evidence that the actual integral vanishes.

**Exact diagnostic for omitting T_ref.** On two points take complex weights
w=(1,−(1−d)), 0<d<1, and g=(a,0), a>0. Then I_ref=d and
I/I_ref=1+(e^a−1)/d, unbounded as d decreases. A pointwise bound on g
alone therefore does not imply the claimed integrated complex comparison.
This finite algebraic diagnostic is not an SU(N) counterexample.

There is also a directly testable locality obligation. For the local D_h,
at zero sources and fixed real V,

    ∂_{ε_p}∂_{ε_q}log D_h = u_0² Cov_{ν_h}(s_p,s_q).       (D21)

It follows by differentiating the complete positive finite integral twice.
A source-local cluster bound would control these and higher connected
correlations on the **conditioned interacting** law ν_h. A marginal price
for Ξ_h does not itself supply such estimates. This names a concrete next
quantity, without replacing the full norm by a second-derivative test.

## 6. Full source norm across this actual hole — PROVEN implication

Use exactly LIB1 R10 with Ω=Γ_1, Λ=Γ_1\H_1 and the original source-reader
supports X, nonempty and face-connected. For μ≥0 the full norm is
sup_v Σ_{X∋v}e^(μ|X|)sup_D|K_X|, on one common parameter domain D.
For any supplied local family K_X set

    K'_Y=Σ_{X∩Λ≠∅:R_Λ(X)=Y}K_X,
    K_inactive=Σ_{X⊆H_1}K_X.

Then Σ_X K_X=K_inactive+Σ_Y K'_Y. Both terms stay inside every remaining
integral. The geometry in (D1) verifies the bounded-hole hypothesis M=81.
Consequently LIB1 directly gives

    ||K'||_μ≤729 ||K||_{649μ},
    ||K_inactive plus K'||_μ≤730 ||K||_{649μ}.             (D22)

The second norm treats the inactive and active families as labelled families
with their full supports; coincident supports can be combined by triangle
inequality. This is the full root/full size norm, not the active norm.

For this **one** hole a sharper fixed-geometry variant avoids the rate loss.
Its closed face-neighbourhood has

    |N[H_1]|=3^4+8·3^3=297.

Indeed an exterior face neighbour has exactly one coordinate ±2 and the
other three in {−1,0,1}; T≥7 prevents identification. There is only one hole,
so |R_Λ(X)|≤|X|+81. For an active output root v, v∈R_Λ(X) implies v∈X;
for an inactive root, a contributing X meets N[H_1]. Summing over the at
most 297 possible input roots proves

    ||K'||_μ≤297 e^(81μ)||K||_μ,
    ||K_inactive plus K'||_μ≤(1+297 e^(81μ))||K||_μ.       (D23)

This is a proof from R10's set map, independent of any activity expansion.
For example the single support {v_*} becomes H_1∪{v_*}, of size 82;
its weight is e^(82μ), even though it has one active vertex. Nothing
permits charging it e^μ in the full norm. Source differences cost a factor
two if inferred from absolute K bounds; Cauchy estimates use an inner disc
of the same original source variables. No hole source is forgotten.

**OPEN — analytic input and induction.** (D23) is uniform in total volume
for this specified hole, provided its input K bound is. No such bound for
the actual fully integrated K has been proved above. Enlarging/merging holes
at later histories changes 81 and 297; neither (D22) nor (D23) asserts a
constant independent of arbitrary history. Keeping unsaturated reader labels
is a possible different norm interface, not a silent use of (D23) without
its geometry.

## 7. CX-R and STEP55, factor by factor

**PROVEN — accounting identity, OPEN — uniform local budgets.** RD's real
tree/chart change of variables, when applicable to (D4), has

    D_sel=A_sel Z_sel,
    A_sel=c_N^n(2πσ²)^(d/2) e^(−S_0) det(Q)^(−1/2)N_χ,
    Z_sel=E_{μ_p}[Θ_h e^(−U)],      σ²=N/u_1,
    D_h=A_sel Z_sel+E_comp+E_side.                         (D24)

Here n is the number of free chart links, d=(N²−1)n, and Q is the chosen
positive real Gaussian matrix before any justified complex continuation.
S_eff=−log w_{1,B} is one permitted allocation; J=ρ_{1,h}/b_1
remains in Θ_h. Changing the allocation requires removing the same factor
from Θ_h. The reference normalization is 1 for unnormalized D_h; for
D_h/Nref_h divide **every** term in (D24) by Nref_h. The linear term in
S_eff and any quadratic mismatch remain in U unless a critical point of
that exact action has been justified. E_side is zero if no contour is
changed; otherwise it is the oriented difference of the selected integrals.
E_comp contains every omitted real sector, with the original history.

| Factor | Exact place and available budget | Missing quantitative match |
|---|---|---|
| Artificial Wilson factor b_1 | a_B in (D4); cancels only in N/D. On real η, 0≤log a_B≤2u_1 card(P_1\P_1(B)). Each plaquette is a local term; the crude full norm is ≤48u_1L⁴e^(4μ). | This real-field budget is not a complex continuation through inherited selectors; it is not small. |
| Frozen convention O | (D5); multiply D by it only for the full conditional convention. Every external kernel occurs once. | Bounds/cancellation in whatever quotient convention a downstream consumer actually uses. |
| Earlier kernels, normalizers, history | In ρ_{1,h}, or equivalently J in Θ_h. Individual real abs(log N_t(M))≤2t; (D2)–(D6) bound the complete integral. | A source-local decomposition of the **integrated** inherited contribution on a common domain. |
| Haar and permitted tree gauge | Unit normalized gauge volume, c_N^n; the exponential-chart Jacobian j is retained as −log j in U. | Actual chart and local source bounds; a different slice requires its own Jacobian. |
| Gaussian scale and Hessian | (2πσ²)^(d/2)det Q^(−1/2). | Uniform log-determinant/source-support estimate for the actual Q. |
| Main action and residual | e^(−S_0), with ell^TσCW and the full remainder in U. | KR's actual full-action local budget, including inherited terms. |
| White cut | N_χ=γ(χ_p); μ_p normalized. Remaining original hard predicates stay in Θ_h. | A matched fixed-domain construction; (D15) or another estimate for the remaining hard pieces. |
| Failed charts / contours | E=E_comp+E_side, additive in (D24). | A locally controlled logarithm of 1+E/(A_sel Z_sel), or another complete expansion. |
| Real reference | Nref_h in (D6); conditional history mass A_h in (D8) is a different reference. | Local logarithmic/reference bounds at all histories and levels. |

The plaquette budget in the first row uses at most 24L⁴ plaquette incidences
per block, each of size ≤2u_1 with support of at most four blocks. It is an
explicit finite real-data budget; it is not an estimate for log ρ_{1,h}.

For E=E_comp+E_side, the RD quotient on the real patch identified after
(D5) has the denominator accounting required for a prospective STEP55
application:

    r_h=N_h/[A_sel Z_sel+E].                               (D25)

Identification with any separately specified STEP55 history convention
remains an additional requirement.

Only on a domain where the indicated factors and branches exist is

    Δlog D_h=Δlog(c_N^n(2πσ²)^(d/2))−ΔS_0−½Δlogdet Q
             +Δlog N_χ+Δlog Z_sel+ΔLog(1+E/(A_sel Z_sel)) (D26)

valid. Constants can cancel; source-dependent terms cannot be called
O(H_V) merely because nonzero. This is the corrected CX-R (ID/FULL/VAR)
accounting and preserves CODEX_REVIEW_STEP R11's determinant diagnostic.
The finite Haar proof above does not identify a Gaussian product-cut
representation satisfying CX-R's hypotheses. Its instantiation and the
STEP55 returned-activity norm remain OPEN.

## 8. Exact induction, failed inequalities, and remaining sub-lemmas

**PROVEN — finite recursion.** RD R3 partitions unity at each pair of real
fields. Append its actual indicator and normalized kernel to the existing
chain, integrate, then sum new records to obtain R1. Fubini is justified by
bounded kernels and compact Haar domains on finite source sets. This proves
the same exact induction for histories extending (D1), including zero-mass
children. A zero-mass child stays zero and is never used as a denominator.

**OPEN — quantitative induction.** It would require the output of (D8), or
each legitimately selected child with its reference, to satisfy the same
source/coarse-domain, prefactor and connected-activity estimates as its
input. Our lower reference and domain depend on the number of original
variables; the children can have new holes and new moving selectors. No
constant-parameter induction follows from (D9).

| Attempt / exact inequality | Outcome | Classification |
|---|---|---|
| Hard predicate as a small sup-norm atom: e^(β card(S)) sup abs(Θ−1)≤1/4 | **Fails** if Θ reaches zero: left side ≥e^β. | Obstruction to this particular small-atom representation. |
| Normalized required species in (D15): e^(β card(S_E))∫abs(1_E/p)≤1/4 | **Fails**, left side e^(β card(S_E)). | Normalization/technique obstruction, not an obstruction to RG. |
| Original Haar interactions satisfy the weak-coupling smallness test | **Not established**; RD (17b)'s sufficient bound 48u(1+ρ)L⁴e^(4β)+16κue^(2β) grows with u. | This estimate fails to certify smallness; it does not lower-bound the actual optimum. |
| Common fixed ρ_* justified by (D12): 2u_0P_0ρ_*+t_1C_tot(e^α−1)<π/2 | **Fails as a uniform sufficient bound** when P_0 is unbounded. | Sector-estimate failure; no actual zero is exhibited. |
| Complex reference comparison without T_ref in (D19) | **False** for the explicit two-point diagnostic. | Obstruction to that general inference, not an SU(N) counterexample. |
| Full norm replaced by active norm at this hole | **Wrong**: singleton enlargement has size 82. | Bookkeeping defect repaired by (D22)/(D23). |
| Matched Peierls/joint-failure and connected-cumulant estimates for this h | **OPEN**, no inequality of the required strength proved or refuted. | Missing science, not a failed numerical check or impossibility theorem. |

Precise remaining sub-lemmas, with no independence count intended:

1. **B2-domain (FR interface).** A common original-source radius and required
   complex boundary domain for the actual returned quotients and their
   effective outputs, with fixed analytic integration sectors or a proved
   treatment of moving hard selectors. Replace the volume cost in (D12).
2. **B2-reference/interaction (KR interface).** Produce local full-factor
   logarithmic budgets for the actual inherited density and prefactors, on
   that domain and with the same real references; bound its nonlinear
   interaction in the norm consumed by the expansion. A single-kernel
   remainder does not establish this statement.
3. **B2-failures (TC interface).** Under that very reference, prove the joint
   event masses/multiplicities and complex contour total variations needed
   by (D15), or construct a different exact expansion. For mandatory
   histories explain explicitly where their mass is extracted and estimate
   the resulting conditioned interaction, rather than reuse p after it
   cancels. No original-law coercivity calculation is duplicated here.
4. **B3-integrated comparison.** Strengthen the finite actual-reference
   comparison (RC1)–(RC3), after the whole sea/failure sum, to a uniform
   local estimate replacing (D18)–(D20), with control of connected source
   correlations such as (D21).
   The different Z_{k,A(h)} factors and inactive terms remain present.
5. **B3-hole/closure.** Supply the input K for (D22)/(D23); then establish
   a compatible full norm for new/merged holes and show that the next
   effective output satisfies items 1–4. Identify the exact history
   convention and every factor in (D24)–(D26) with the consumer. Algebraic
   recursion alone is insufficient.

These are proof obligations, not adopted physical premises. An adapted
conditioned reference with a proved local correlation estimate is the next
constructive target. No complete normalized **uniform** RG step, T_OS,
continuum existence, mass gap, or no-go theorem is claimed.

## 9. No-go discipline scope check — no exhausted-route packet

**N1.** Real routes considered: unadapted Haar/sector estimates (worked,
finite results and exact failed sufficient bounds above); integrated
rare-event species (worked to (D14)–(D16)); an adapted conditioned reference
(proposed, its local estimates unproved). Smooth partitions with derivative
costs and direct all-order cumulant estimates remain untested alternatives.
No five-family exhaustion or packet PASS is claimed.

**N2.** Domain, reference, failure and induction obligations are not asserted
independent. A matched local expansion can address the first three together;
induction includes them at the next level. Their pairwise non-implications
have not been established, so there is no independent-wall count.

**N3.** Supplied model, fixed history/cuts, positivity, real frozen data,
product-measure hypotheses in (D14), bounded hole geometry in (D22)/(D23),
and separately proposed FR/KR/TC interfaces are explicit. A Gaussian chart
is conditional in (D24), not hidden in the finite Haar proof.

**N4.** RD R16 matches the small-defect criterion actually tested. LIB1 R10
matches the saturation map, not the sea integral. R11 of CODEX_REVIEW_STEP
matches the full-factor error. RLARGE/LARGE55 prices have different law or
event hypotheses and are therefore not treated as witnesses that RD3's
remaining estimate is either proved or impossible.

**N5.** (D16) concerns one normalized event; the two-point example concerns
one complex integration inference; (D23) concerns full block supports.
The domain bound concerns a finite-lattice worst-case sector estimate.
No mode-by-mode, continuum, spectrum or physical no-go follows. No numerical
experiment or unexecuted numerical certificate is reported as passed.

**N6.** Keeping original reader labels, changing a compatible consumer norm,
or extracting a history mass are mathematical choices, not new physical
axioms. The approved primitive registry does not resolve or create the
analytic obligations in this note.

**N7.** Strongest counter-route to a broad negative conclusion: retain
mandatory events in a conditioned reference, expand only the remaining
weak interactions with their full original-source supports, and integrate
the inactive variables before estimating the final logarithm. RD's exact
identity and LIB1's retained inactive term allow this. The terminal task is
a uniform local cumulant/reference theorem under that conditioned law;
(D16) does not refute it.

**N8.** The earlier hard-cut error was already repaired by RD's L1 criterion;
LIB1 repairs active/full norm confusion with an explicit geometric cost.
The related sea construction addresses a coarse-integrated reference under
its own hypotheses. These repairs show why a failed estimate cannot be
promoted to a general obstruction. They do not close the fixed-V/local
induction demanded here. Scope: partial attempt with named untested routes.

```yaml
actual_current_surface_status: open
target_claim_type: positive_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit positive failed history and finite normalized next step; integrated reference comparison and exact full-hole cost proved, uniform B2/B3 analytic induction open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
