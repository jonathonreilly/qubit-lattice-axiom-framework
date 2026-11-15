# Primary reconstruction of the proposed 2606.19362 continuum-gap bridge

This is a bounded examination of the actual derivations in Mir Faizal and
Arshid Shabir, [arXiv:2606.19362v1](https://arxiv.org/pdf/2606.19362v1),
including its appended Parts II–IV and the covariance result cited in its
weak-coupling argument. The examined chain does not establish the requested
full, non-free, four-dimensional SU(N) continuum theory with a positive
physical Hamiltonian gap. Several displayed implications are false as
stated; explicit counterexamples below identify the failed inferences.
This conclusion concerns this proof chain, not the truth of the Yang–Mills
mass-gap conjecture, and not every argument in the 593-page aggregate.

There is usable bounded mathematics: normalized pushforward identities,
positive-operator comparison under explicitly assumed ordering, and a gap
criterion from decay on a dense physical source algebra. They are rebuilt
below. None supplies the missing Yang–Mills hypotheses merely from finite
range, reflection positivity, a local Hessian gap, or a finite-distance
comparison of regulators. The note makes no retained/audit-status change.

## 1. Source coordinates, target, and the strong-coupling grant

References below use **PDF page numbers**, followed where useful by the
paper's printed number. The main manuscript is PDF 1–248; PDF 250 describes
the appended papers. Part I occupies PDF 251–365; II, 366–455; III,
456–552; IV, 553–593. Thus Part II printed page = PDF−365, Part III =
PDF−455, and Part IV = PDF−552. The main printed page = PDF−2 in the
sections used here. All four appended papers are read from the same
versioned arXiv PDF; their journal attribution is not independent evidence
of validity.

The target holds N≥2 fixed and requires one and the same normalized,
gauge-invariant correlation hierarchy along a continuum trajectory. It
requires the full physical source algebra, Euclidean symmetry and OS
reconstruction, a non-free theory, a unique vacuum, and a nonzero sector
of finite positive physical energy with spectrum bounded below by m>0.
A gap for an auxiliary Gaussian, a conditional sector, a blocked Hessian,
or selected loops does not substitute for that target.

Main §3, especially Theorem 3.3 and (3.41)–(3.46), PDF 28–30, uses a
small-inverse-coupling window 0<β≤β₂. With positive transfer operator
T and lattice-time decay exponent μ(β)>0 on a dense centered algebra,
the spectral conclusion is H=−a⁻¹log T with gap at least μ(β)/a. The
spectral implication is valid under those hypotheses; §8 reconstructs it.
This note **grants** the source's fixed-a strong-coupling input for testing
the subsequent bridge. It does not certify the whole character/polymer
expansion in main §3 or appended Part I.

The usual Wilson convention in the source is β=2N/g₀². Thus its small-β
character-expansion window is not the β(a)→∞ weak-bare-coupling end of
an asymptotically free continuum trajectory. Keeping β in that fixed
window and letting a→0 can drive every fixed-lattice excited energy to
infinity. It is necessary to prove entry/matching on the same trajectory,
with physical-time and source normalizations retained. A positive
fixed-spacing gap alone does not prove this matching or nontriviality.

## 2. First unsupported inference in the examined bridge: the FRD projection

After granting §3, the earliest definite failure located in the examined
§4→§5→§10 bridge is main §4.1, PDF 31 (printed 29), immediately after
(4.2). The source defines E by retaining boundary values and extending
them harmonically into each block. It then asserts that E is a
self-adjoint contraction on ℓ² and uses this to form orthogonal differences
Πⱼ=Eⱼ−Eⱼ₊₁ in (4.3)–(4.7).

For the scalar Laplacian on a three-vertex path, with the two endpoints
as boundary, this definition gives

    E = [[1,   0,   0],
         [1/2, 0, 1/2],
         [0,   0,   1]].                                  (C1)

E²=E, but E≠E*. For x=(1,0,1), ||Ex||²=3>2=||x||². This is not a
dimension-specific objection: in a genuine four-dimensional Dirichlet
block, an interior basis vector has zero boundary trace and E eᵢ=0,
whereas a boundary basis vector has nonzero harmonic extension at an
adjacent interior point. Hence ⟨eᵢ,Ee_b⟩≠⟨Eeᵢ,e_b⟩ in the stated ℓ²
inner product. A projection orthogonal in a Dirichlet-energy inner product
is a different object and does not validate the printed ℓ² assertions.

The alternative covariance difference in main Theorem 4.1,
(4.12)–(4.17), PDF 32–35, also needs an ordering that is not proved.
Nested subspaces do not make differences of positive compressions positive:
for 0<r<1, let

    C = [[1,r],[r,1]] > 0,  P=I,  Q=diag(1,0).
    PCP − QCQ = [[0,r],[r,1]],  determinant = −r².          (C2)

The same issue invalidates the inference in (4.17) from nonnegative OS
forms to a nonnegative difference merely because one subspace is smaller.
Similarly, a finite-range factor on either side of a covariance does not
by itself make the sandwich finite range; the identity factor already
shows this. A covariance cancellation identity must be established.

The primary dependency actually consulted is Brydges, Guadagni and Mitter,
[Finite range Decomposition of Gaussian Processes,
math-ph/0303013v3](https://arxiv.org/pdf/math-ph/0303013v3), Theorem 1.1
and §3, PDF 3 and 6–10. For the scalar translation-invariant resolvent
Gᵃ=(a−Δ)⁻¹ in d≥3, it constructs a **translation-averaged Poisson map** A,
not the asserted ℓ² Dirichlet projection. Its (3.8)–(3.16) give

    Γ = Gᵃ − A Gᵃ A*,
    Γ-hat(p) = [1−|A-hat(p)|²] Gᵃ-hat(p) ≥ 0,             (C3)

using translation invariance and |A-hat|≤1. Finite range follows separately
from harmonicity away from the covariance singularity. Equations
(3.27)–(3.32) then iterate the exact decomposition. These are substantive
hypotheses and cancellations. The cited scalar Gaussian theorem does not
prove the source's arbitrary-background projection, reflection positivity
of each covariant piece, or interacting normalized Yang–Mills RG bounds.
BGM (1.2) and (4.5)–(4.6) also distinguish exact Gaussian integration from
the additional task of controlling an interacting activity.

A second local defect, main Lemma 4.2, (4.21)–(4.24), PDF 36–37, is the
curvature-only comparison of an open transporter with the identity.
For flat pure gauge links U_xy=h_x h_y⁻¹, every plaquette curvature is
zero but W(x→x_B)=h_x h_B⁻¹ can be nonidentity. Thus
||W−I||≤c||F||Lʲ fails without an explicit gauge/trivialization or a
gauge-covariant comparison. This does not forbid curvature estimates
after the required gauge/frame construction; it identifies its omission.

## 3. Transfer ordering and physical units are separate obligations

### 3.1 Deleting mixed Gram entries is not a positive compression

Main Lemma 5.3, (5.22)–(5.28), PDF 51–53, constructs a positive Gram
matrix C_{αβ}=⟨X_α,X_β⟩ from centered observables. It calls the entries
connecting different coarse cells a principal submatrix and concludes
C_mix≥0, hence the required D_k≥0 in

    T_{k+1}=V_k* T_k^b V_k − D_k + E_k.                  (C4)

The two-cell example C in (C2) is a positive Gram matrix, while its mixed
part is [[0,r],[r,0]], with eigenvalues ±r. A principal submatrix retains
the diagonal entries for a subset of individual indices; selecting
off-diagonal pairs is not such a compression. Vacuum centering and
reflection positivity supply the full Gram positivity, not this sign.

Main Appendix D, PDF 193–199, contains valid abstract operator comparison
lemmas but does not repair this missing ordering. Its positivity argument
for the difference of interpolated RP kernels, especially (D.24), needs
more than positivity of each interpolation point: the derivative of a
positive family need not be positive. Consequently D≥0 remains a
Yang–Mills input, not a consequence established by the displayed Gram
argument.

### 3.2 Dimensionless defects need the physical-time conversion

In main Theorem 5.4, (5.30)–(5.37), PDF 54–55, the notation Δ changes
from the contraction gap 1−λ₂ to the physical energy

    m_k = −a_k⁻¹ log λ_k,    a_{k+1}=b a_k.

Granting the spectral inequality λ_{k+1}≤λ_k^b+ε_k gives exactly

    m_{k+1} ≥ m_k
      − a_{k+1}⁻¹ log[1+ε_k exp(a_{k+1}m_k)].             (C5)

PDF 55 then infers exp(a_{k+1}Δ_k)≤exp(a_{k+1}) from Δ_k≥0 and calls
the geometrically growing a_k uniformly comparable to 1. Neither
inference follows. A fixed choice of units cannot uniformly bound b^k.
An unweighted sum of operator defects does not provide the weighted
physical-energy budget in (C5).

Here is an exact positive-transfer counterexample to that abstract
implication. On C² take Ω=(1,0), a_k=b^k, b≥2, k≥1, and

    T_k=diag(1,4⁻ᵏ),
    E_k=diag(0,4⁻⁽ᵏ⁺¹⁾−4⁻ᵇᵏ),    V_k=I, D_k=0.         (C6)

Then T_{k+1}=T_k^b+E_k, E_k≥0, E_kΩ=0, and
Σ_{k≥1}||E_k||≤1/12. The initial contraction gap is 3/4, so even a
strict dimensionless defect budget is available. Nevertheless the
physical gap m_k=k log(4)/b^k tends to zero. This is an operator-level
counterexample to the inference, not a proposed Yang–Mills model.

Main Theorem 5.6, PDF 57, additionally needs a strict loss budget below
the starting gap; finiteness of a sum alone is insufficient. Appendix D
uses a fixed physical time τ in (D.1), which is the correct setting for
the bounded lemma in §8. It does not prove that the original multiscale
construction has the requisite fixed-τ comparisons and strict budget.

Part III Appendix E, (E.6)–(E.16), PDF 551–552, exposes the same issue.
Its final positive physical gap relies explicitly on a separately supplied
scale-independent clustering bound S2. The assertion that summability
alone prevents erosion is false. Moreover E.1 defines d as graph distance:
conversion from e^(−m*d_graph) to a physical-time estimate, with all
source prefactors controlled, must be tracked along the actual trajectory.

## 4. The claimed coarse coupling changes the fine marginal

Part II (8.14)–(8.18), PDF 416–417, defines

    μ_{k+1}=B_*[(Θ_k/Z_k) μ_k],
    dπ_k(U,V)=(Θ_k(U)/Z_k) δ_{B(U)}(dV) dμ_k(U),
    Z_k=∫Θ_k dμ_k.                                      (C7)

The claimed marginals are μ_k and μ_{k+1}. Direct integration over V
instead gives (Θ_k/Z_k)μ_k as the fine marginal. It equals μ_k only
if Θ_k=Z_k μ_k-almost everywhere. The proposed OS norm identity (8.18)
omits this insertion. Reflection symmetry of Θ does not make it
constant or remove it from a normalized expectation.

Thus an isometry or vacuum-preserving contraction from the original fine
OS space is not obtained by the asserted identity. One can use the
reweighted fine space, or explicitly retain Radon–Nikodym factors and
control their effect on all sources, but that is a different proof.
The collar factors in (8.21)–(8.22) have bounds c_σ^(2w+1) and
C_σ^(2w+1), which are not uniform in the growing collar width. Locality
does not turn multiplication by a nonconstant positive function into
the identity in operator norm or make it vacuum-preserving.

Part II §6, (6.27)–(6.29), PDF 406–407, has another normalization
problem. It claims a bound μ_{k,σ}(SF_k^c)≤exp(−c′λ), while λ is an
auxiliary suppression parameter inserted through R_k and not present in
the displayed original μ_{k,σ} or event SF_k. For a fixed positive
finite-volume density and a nonempty open large-field event, that
probability is positive and independent of λ; it cannot satisfy the
bound for arbitrarily large λ with a fixed c′>0. If c′ is permitted to
depend on λ, the displayed estimate gives no uniform exponential
suppression without a lower bound on that rate. Suppression in a newly reweighted law
does not prove suppression under the original normalized law. This
does not rule out genuine large-field estimates for the original law.

## 5. The weak-coupling entry is not established

### 5.1 The norm and Gaussian remainder estimates fail as printed

Main Definition 10.1, (10.8)–(10.9), PDF 111, controls only derivatives
through finite order p at **A=0**. The claimed Banach norm therefore
vanishes on nonzero analytic activities with sufficiently high-order
zeros. Already in one scalar coordinate, G(A)=A^(2q), 2q>p, has zero
displayed seminorm but a nonzero Gaussian average at A=0. Thus (10.14),
PDF 113, asserting that Gaussian translation/averaging contracts this
seminorm, is false. The same obstruction can be realized with sufficiently
high powers of a local nonnegative gauge-invariant curvature polynomial:
its origin jet vanishes but its Gaussian average need not vanish.

A field regulator, a controlled analytic neighborhood, or a consistent
quotient closed under Gaussian integration could support a different
theorem. No such construction is supplied by (10.8)–(10.14). In particular,
finite jets at zero do not bound the L∞ norm on unbounded Gaussian fields
used in (10.26), PDF 115.

There is a separate exact test of Proposition 10.3. Equations
(10.22)–(10.23), PDF 114, define U_n as the source cumulants of
log∫exp(⟨J,φ⟩)exp(gV+K)dμ_C(φ). At g=K=0,

    U₂(f,f)=⟨f,Cf⟩>0                                  (C8)

for any f outside the covariance kernel. But (10.30)–(10.32), PDF 116,
remove the zero-interaction contribution and conclude that the sum of
these cumulant norms is bounded by C₁g²+C₂g||K||+C₃||K||²=0. Centering
the vacuum and first cumulant does not remove Gaussian covariance.
Interaction-only remainders could be defined instead, but those are not
the U_n in the displayed definition and require their own estimates.

### 5.2 An upper recurrence is not the missing all-scale trajectory

Main (10.34)–(10.35), PDF 116–119, claims

    ||K_{k+1}||≤θ||K_k||+c₁g_k²,
    g_{k+1}=g_k−β₀g_k³+R_k,
    |R_k|≤c₂|g_k|⁵+c₃|g_k|||K_k||+c₃||K_k||².          (C9)

Even granting these estimates, a fixed polydisc ||K||≤δ* does not make
the last two terms uniformly smaller than β₀g³/2 as g→0. An invariant
relation between K and g, with the required constants, is missing.
The first recurrence, with g_k² of order 1/k, allows an irrelevant
activity of order 1/k; it does not imply exponential decay or summability.
At (10.59), PDF 123, the bound by sums of g_j² is then treated as
summable although the asserted asymptotic-freedom rate gives a harmonic
series. Later homogeneous remainder formulas do not follow from the
inhomogeneous c₁g² term without a proved change of coordinates/invariant
trajectory.

There is also an unresolved scale convention. Main (10.38), PDF 117,
coarsens a_{k+1}=b a_k, and §10.2 uses μ_k=μ₀b^(−k), but the displayed
decreasing coupling recursion is assigned the ultraviolet AF sign;
Theorem 10.7 subsequently uses μ_k=μ₀b^k. Reversing the index can be a
legitimate reformulation only with an actual inverse/tuned trajectory
and consistent physical observables. No such repair is proved by these
inconsistent labels alone.

### 5.3 Appended Part IV does not supply the missing entry

Part IV Theorem 5.4, (5.17)–(5.24), PDF 576–577, assumes contraction
on an irrelevant sector, bounded scalar response on a one-dimensional
Gaussian sector, and quadratic nonlinear upper bounds. It then infers
both |g′_K(β*)|≥c₀>0 and |g_K(β*)|≤C₀ρ^K in (5.24).

Those implications fail for the explicit sector map on R²

    R_k(β,(x,y))=(x,ρy),  0<ρ<1,
    G=R×{0}, R={0}×R, Q=0, Φ₀(β)=(h,0), h≠0.          (C10)

All the listed sector upper estimates hold, with scalar multiplier 1
and zero mixing, while g′_K=0 and g_K=h. With Φ₀(β)=(β,0) on an
interval contained in (0,∞), the scalar response is nonzero but there
is still no root g_K(β)=0 in that interval. These are counterexamples
to the asserted consequence of the abstract hypotheses, not to a
particular Yang–Mills flow. Such a flow must provide additional response,
image, domain, and tuning estimates.

Part IV Appendix A.9, PDF 590–592, repeats the missing response and
implicit-function step while keeping the bare coupling in a compact
character-expansion interval. That does not establish β(a)→∞, passage
through all intermediate scales, or entry into the strong-coupling domain
of the **same** normalized continuum trajectory. Its invocation of FRD
and BGM supplies neither the interacting scalar response nor the
large-field/history estimates. Appendix A.10 also closes its induction
using 2Cr+Cr²≤0 for positive C,r. This last elementary lemma is repairable
with an appropriate smallness assumption and q=ρ+Cr<1; repairing it
does not supply the missing entry map.

## 6. Full-hierarchy matching and reconstruction remain unproved

Main Theorem 10.8, (10.78)–(10.81), PDF 128–129, seeks equality of the
AF and strong-coupling Schwinger families. Its displayed estimate has
the form

    D_{k+1}≤D_k+Cε_k,
    D_K≤D₀+C Σ_{k<K}ε_k.                                (C11)

A finite right-hand side does not tend to zero. The constant sequence
D_k=d>0 with ε_k=0 already refutes the equality inference. Finite
Lipschitz distance between initial data does not make that distance
vanish. Also, DΩ=0 does not remove ⟨Ω,A D BΩ⟩ for inserted observables.

Part IV Theorems 4.7–4.8, PDF 571–572, and Appendix A.8, PDF 589,
repeat continuity-to-equality. The latter claims polygonal chains
between fixed distinct data can have arbitrarily small total length.
The triangle inequality bounds that length below by their distance;
subdivision does not shrink it.

A physical-semigroup illustration makes the missing data concrete.
Let P project onto the constant vector of a two-state probability space,
Q=I−P, and T_m(t)=P+e^(−mt)Q for m>0. These reversible Markov
semigroups are positive and reflection positive, have the same uniform
one-slice law, and cluster exponentially. Their correlations for the
centered sign observable are e^(−m|t|), hence differ when m differs.
Continuity, a shared marginal, and positive gaps do not identify their
full time-dependent hierarchies. Equality follows if the **same marginal
and the same semigroup with the same insertion operators** are proved;
it is that equality which the source's finite error estimate does not
establish.

There are further direct failures in the full-continuum reconstruction,
even if its missing uniform bounds are granted. Main §7.2, PDF 83,
extends symmetry by claiming the hypercubic rotation group is dense in
O(4). The signed-permutation rotation group is finite and is not dense.
PDF 85 subsequently assumes an O(a_k) error for arbitrary rotations
without deriving an estimate on the interacting correlation hierarchy.
The internal isotropic regulator premise supplies hypercubic kinetic
form, not this missing continuum rotational theorem.

Main (7.25), PDF 85, additionally asserts
||[τ_tF]||_OS=||[F]||_OS from Euclidean time-translation invariance.
Reflection gives θτ_t=τ_{−t}θ, not commutation. For a centered vector
with spectral measure ν,

    ||e^(−tH)ψ||²=∫e^(−2tE)dν(E),                        (C12)

which is strictly smaller at positive energy. Taken literally together
with the claimed self-adjoint contraction semigroup, the asserted
isometry would force H=0. The valid OS reconstruction uses contraction
and continuity with the appropriate proof, not this equality. This
identifies a repairable reconstruction error; it does not invalidate
the general OS reconstruction theorem.

Finally, main §7 starts with a fixed finite family of gauge-invariant
generators. A limit for that family is not automatically the full
physical local algebra. Uniform source bounds, consistency as the family
grows, density, identification of the renormalized observables, and
reflection positivity for that same hierarchy must be supplied.

## 7. Nontriviality and non-freeness are not preserved by the stated bounds

Part III §10, PDF 527, combines a smooth spectral cutoff equal to 1 on
[0,σ] and zero for λ≥2σ, (10.7), with a representation
χ(λ)=∫₀∞e^(−sλ)dν(s) by a finite positive measure, (10.8). A nonzero
positive Laplace transform is strictly positive at every finite λ≥0;
it cannot have that compact spectral support. Thus the particular
projected law used in this argument is not defined by both stated
properties simultaneously. A noncompact completely monotone cutoff
or a different RP construction would require an explicit replacement.

Part III Theorem 10.4, (10.23)–(10.25), PDF 530–531, claims a constant
c*>0 uniform for every 0<β≤β₀ while deriving a leading term
A_Nβ⁶+O(β⁷). Even granting that expansion, its limit is zero as β↓0;
setting c*=A_Nβ₀⁶/2 gives the wrong lower-bound direction. Fixed
elementary plaquettes also shrink in physical size as a→0, so such a
lattice statement would still require a source-renormalization bridge.

Part III Theorem 10.5, (10.33)–(10.35), PDF 531–532, proposes
transport of a fourth cumulant. Its correctly iterated lower bound is

    a_k ≥ ρ^(k−k₀)a_{k₀}
            − Σ_{j=k₀}^{k−1}ρ^(k−1−j)δ_j,  0<ρ<1.       (C13)

It then infers liminf a_k≥a_{k₀}−Σδ_j. The exact sequence
a_k=a_{k₀}ρ^(k−k₀), δ_j=0, satisfies all of (C13) and tends to zero.
An unweighted lower bound cannot survive the stated contracting source
normalization. A renormalized source with a proved nonvanishing product
of overlap factors, or another finite-scale physical witness, is needed.

Moreover a nonzero fourth cumulant of a nonlinear gauge-invariant
observable does not by itself exclude a free underlying field. For
X∼N(0,1), O=X²−1 has

    log E exp(tO)=−t−(1/2)log(1−2t),   κ₄(O)=48.          (C14)

Thus the assertion that all higher connected cumulants of arbitrary
local observables vanish for Gaussian measures is false. Wick
comparisons must concern the identified basic fields or the correctly
specified composite hierarchy. No non-free Yang–Mills conclusion follows
from the unqualified plaquette-cumulant test.

## 8. Bounded library statements that survive reconstruction

### L1. Exact normalized block law

Let μ be a probability law and K(dV|U) a Markov kernel with
∫K(dV|U)=1 for every U. Then π(dU,dV)=μ(dU)K(dV|U) has fine marginal
μ and coarse marginal ν=μK. For bounded source functions,

    ∫F(U)G(V)dπ = ∫F(U)[∫G(V)K(dV|U)]dμ(U).             (L1)

Both assertions follow directly by integration. Inserting a factor
Θ(U)/μ(Θ) changes the fine law unless Θ is almost surely constant;
(C7) is exactly this distinction. Reflection positivity of ν follows,
for a deterministic block map B, if B commutes with reflection **and**
pulls every positive-half observable back into the fine positive-half
algebra: ν(θF F)=μ(θ(F∘B)(F∘B))≥0. For a stochastic kernel, an
appropriate factorization of its reflected joint law is an additional
hypothesis; normalization and reflection covariance alone do not prove it.

### L2. Fixed-physical-time spectral comparison

This rebuilds the valid abstract core of main Appendix D and Part II
Appendix B, PDF 452–455. Let A and B be positive self-adjoint
contractions on Hilbert spaces H and K with unit vacua Ω_H, Ω_K,
AΩ_H=Ω_H, BΩ_K=Ω_K. Let W:K→H satisfy ||W||≤1,
WΩ_K=Ω_H and W*Ω_H=Ω_K. Suppose in quadratic-form order

    B ≤ W* A W + E,       E=E*,  ||E||≤ε.                (L2a)

Writing q_A=||A|Ω_H⊥||, each unit ψ⊥Ω_K satisfies Wψ⊥Ω_H and

    ⟨ψ,Bψ⟩≤q_A||Wψ||²+ε≤q_A+ε.

Hence q_B≤q_A+ε, without assuming a discrete second eigenvalue. If
A_k=e^(−τH_k) at one fixed physical τ>0 and these comparisons hold
at every step with 0<q₀+Σ ε_k=q<1, then

    spec(H_k|Ω_k⊥) ⊂ [−τ⁻¹log q,∞)                    (L2b)

for every k. The ordering, vacuum compatibility, common physical τ,
and strict budget are hypotheses. Parts II/D do not establish them
for the source's full original Wilson hierarchy by the arguments tested
above. Under strong convergence through compatible dense embeddings,
the bound passes to the limit by taking matrix elements; the existence
of those embeddings and of that limit remains separate.

### L3. Physical-time decay on a dense centered algebra gives the gap

Let H≥0 be self-adjoint with HΩ=0. Let D be dense in Ω⊥. Suppose a
common m>0 exists and, for each ψ∈D, there are finite C_ψ,t_ψ such that

    0≤⟨ψ,e^(−tH)ψ⟩≤C_ψ e^(−mt),   t≥t_ψ.              (L3a)

The spectral measure ν_ψ is positive. If ν_ψ([0,m−η])>0 for any
η>0, the left side is at least ν_ψ([0,m−η])e^(−(m−η)t), contradicting
(L3a) as t→∞. Therefore the spectral projection 1_[0,m)(H) vanishes
on D, and by boundedness on Ω⊥. Thus the vacuum is unique and the
physical excited spectrum is contained in [m,∞). This is the valid
mechanism in main §3.3 and the gap argument invoked in Part III
Appendix E; it does not derive its uniform Yang–Mills input.

To ensure a nonzero finite-energy sector, also require some centered
continuum vector ψ with ⟨ψ,e^(−t₀H)ψ⟩>0 at finite t₀>0. Its
nonzero spectral measure has positive mass in [m,M] for some finite M,
since [m,∞) is the countable union of such intervals. L3 alone is
vacuously true when Ω⊥={0}; a limiting variance confined to t=0 does
not supply this positive-time witness. Non-freeness remains a further
hierarchy statement even after this witness and the gap are established.

## 9. Match to the actual finite-u Wilson/S4′ lane

Only after the primary chain was checked, the lane's actual law definition
was read in [PROOF.md](PROOF.md), Decision 4 ([historical lines 2838–2874](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ac67a941deafacb6cccbb9b90e3be393108efea3/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/PROOF.md#L2838)), and the FK1 definition in
[FINITE_COUPLING_KERNEL_ASTRA.md](FINITE_COUPLING_KERNEL_ASTRA.md). With probability Haar and u=g⁻²,

    k_c(V_c|U)=exp[−κu(1−Re tr(V_c⁻¹ M̄_c(U))/N)]/N_c(U),
    N_c(U)=∫exp[−κu(1−Re tr(V⁻¹ M̄_c(U))/N)]dV,
    K(V|U)=∏_c k_c(V_c|U),   ∫K(V|U)dV=1.              (M1)

Here M̄ is the paired S4′ mean of fine contour transporters. Thus L1
matches the original normalized finite-u law exactly. All fine source
insertions can be retained in the joint law. The auxiliary V variables
are not automatically the deterministic S4′/S4″ observable iterates;
the source identity must identify the desired physical algebra.

There is no established concrete match from (M1) to L2's required
positive ordering, fixed-time embeddings and summable strict physical
budget, or to L3's continuum-uniform bounds on a dense centered algebra.
Part II's extra Θ insertion fails the fine-marginal check. Main §4's
open-transporter estimate fails for gauge-equivalent flat data. The
scalar BGM covariance does not replace the nonlinear covariant
finite-u normalized law. Finite-kernel Laplace asymptotics or a positive
conditional Hessian are not a Hamiltonian gap for that law.

The missing constructive package still includes the normalized
all-history/extraction estimate and renormalized sources, a genuine
weak-to-strong trajectory with constants and domains, the physical-time
spectral budget, full-algebra continuum/rotation control, and a
non-free positive-time excitation witness. These are dependencies of
one proposed bridge; this note does not count them as independent
impossibility walls or claim to have exhausted alternative routes.

The registered Lattice, Qubit, Admissibility and Record premises and the
approved scale-reference, kinetic-isotropy and realized-state primitives
are left intact. The scale reference converts units; kinetic isotropy
fixes the regulator kinetic form; neither supplies the missing
dimensionless dynamical/RG bounds. No primitive is reclassified as an
unapproved axiom or used to import an absent theorem.

## 10. Scientific scope and possible repairs

The source's fixed-a spectral implication and abstract comparison
lemmas are useful under their exact hypotheses. An alternative genuine
covariant FRD, a regulator-controlled analytic norm, a proved tuned RG
trajectory, and a vanishing comparison of the same complete hierarchy
could change the conclusion for a revised proof. Those possibilities
remain open. The finite counterexamples in this note refute particular
displayed implications, not all such constructions and not Yang–Mills
existence itself.

This is a partial primary-source read with a complete reconstruction
of the counterexamples and bounded lemmas stated here. It is not a
full review of all 593 pages. No numerical scientific result, new
Yang–Mills existence theorem, physical-gap theorem, or independent
peer-review attestation is claimed. The accompanying provenance records
the exact source snapshots, actual page coverage, local-law reads,
methodology pin and frozen-file identity. A fresh different reviewer is
required before any substantive result is integrated.
