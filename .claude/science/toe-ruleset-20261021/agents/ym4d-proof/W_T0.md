# W-T0: a magnetic boundary witness and its OS reduction

Author: Codex, 2026-10-29. Status: **conditional support**, with exact
cutoff and comparator lemmas. Independent review: recorded in
[W_T0_LOG.md](W_T0_LOG.md). No Yang–Mills estimate is proved here.

The conclusion concerns a theory with the **specified magnetic observable
family**, not an abstract Hilbert space or every possible identification
with a free theory. There is no mass-gap claim. This is a research note,
not the consolidated public proof required by PROCESS_LIGHT.

Two corrections to the requested formulation are necessary. First, a
single-scale one-point gap against all free normalizations is false: a
Maxwell covariance can match that value exactly (§5.3). The valid uniform
gap is a two-scale finite-moment witness (§5). Second, the four named YM
inputs do not themselves supply OS0–OS3 on the enlarged algebra. The
common-algebra premise of N1F/N1S must be stated for the enlarged family;
its remaining analytic content is explicit in §6. A boundary Hilbert
extension can already be constructed conditionally on second moments (§2),
but it does not establish the entire E(4)-covariant local theory.

## 1. Objects, normalization, and the common sequence

Fix N ≥ 2, odd L ≥ 3, c_t > 0, integers m_0,d_0 ≥ 0, and a fixed
nonzero reference coupling g_ref in **FLOW's convention**. Set

    a_K = L^(-K),   u_k = g_k^(-2),   t^{(m)} = c_t L^(-2m),
    k = K-m,       t_0 := t^{(m_0)},   τ = t/a_K².

Here t_0 is a named coarse flow time, not the grid value with index zero.
R denotes physical size; R_F denotes the additive flow error. The Wilson
measure has action u_0 Σ_p s(U_p), s(U)=1−Re tr(U)/N. Thus

    u_k = 2N/g_std,k²,       g_std,k² = 2N g_k².                 (1)

This is FLOW §0, “Coupling variable”; it also corrects the trajectory
identification flagged by CODEX_REVIEW_OSLEAF F3. No equality of measures
is inferred by equating the two differently normalized couplings.

**(F-B), an inherited open trajectory premise.** The same bare measure
used for the e-field and the magnetic field has, on every required depth,

    0 < U_-(m) ≤ u_(K-m) ≤ U_+(m),
    U_±(m) = g_ref^(-2) + β_± m log L ± R_F,
    0 < β_- ≤ β_+,     0 ≤ R_F < ∞.                              (2)

Choose m_0 so U_-(m_0)>0. All constants are independent of K,R. Only
U_-(m)→∞ and U_+(m_0)<∞ enter the separation proof. This is the precise
part of F-tune consumed here; neither the tuning nor the flow is derived.

On the periodic spatial slice at Euclidean time s, evolve its spatial
links by the 3D Wilson gradient flow, with action
S_3(V)=2Σ_(x,i<j≤3) Re tr(1−V_ij(x)). Fix the invariant link metric/time
normalization so its abelian linearization is ∂_τ A=−d* d A. Define

    B_(K,R)(t;s,x) = τ² · 2 Σ_(i<j≤3) Re tr(1−V_ij(τ;s,x)),
    f_(K,R)^B(t) = ω_(K,R)(B_(K,R)(t;0,0)).                  (3)

This is HINT2_55 R1.9's 𝓑, with its flow and action normalization fixed.
It is uncentered. Vacuum subtraction would change the comparator and is
not allowed silently. For anti-Hermitian generators with
−tr(T^aT^b)=δ_ab/2, expanding a smooth plaquette gives
2 Re tr(1−V_ij)=a⁴ Σ_a(F_ij^a)²/2+o(a⁴), so its quadratic continuum
counterpart is t²Σ_(i,j,a)(F_ij^a)²/4. This expansion fixes a convention;
it is not a continuum estimate on random YM fields.

**(SEQ), inherited from N1F/N1S.** Fix ONE sequence (K_j,R_j), K_j→∞,
R_j→∞, and ONE countable determining hierarchy, enlarged to include the
magnetic labels, bounded truncations, mixed tests and observable/group
pairs needed below. A further subsequence is always taken simultaneously
for these and the original e-field tests. Flat cutoffs have R_j/a_j even,
so the reflection through time zero is a site reflection. All bounds
below refer to this same bare measure and trajectory.

For N1S use continuum extraction at each fixed R first, then R→∞, with
radius-uniform bounds for the enlarged hierarchy. If a lattice diagonal
is required, enumerate its scalar test values z_1,z_2,… (including mixed
RP forms and symmetry defects). Choose R_j so the first j continuum values
are within 1/j of their limiting values, then a fixed-R_j cutoff with
a_j<1/j so those same j values are within 1/j of the sphere values.
Each fixed coordinate then differs by at most 2/j. This proves the
diagonal assertion **provided those fixed-R limits and uniform extension
bounds exist**. It does not construct a spatial magnetic flow on the
sphere or infer its transport from the torus formula.

## 2. Library entries: cutoff support, limits, and the boundary vector

### 2.1 Cutoff boundedness and exact site-reflection pairing

**Lemma B-cut.** At fixed K,R and finite τ, (3) is a smooth,
gauge-invariant function of the spatial links of its single time slice,
and

    0 ≤ B_(K,R)(t;s,x) ≤ 12N τ².                            (4)

Proof. The flow is a smooth ODE on a finite product of compact SU(N)'s;
its smooth bounded vector field extends its unique solution to every
finite flow time. Its action and link metric are invariant under slice
gauge transformations, so uniqueness makes the flow equivariant.
No links from another time slice occur in this ODE. Each of the three
terms Re tr(1−V_ij) lies in [0,2N], which proves (4). The bound grows
as a^(-4) at fixed physical t and supplies no continuum moment bound. ∎

For θ(s,x)=(−s,x), B(t;0,x) is θ-fixed. On an even periodic time lattice,
write the links as U=(U_∂,U_+,U_-), where U_∂ consists of the two fixed
site planes. Every plaquette is wholly in one closed half, and
S_W=S_++θS_+, splitting the boundary plaquettes equally. Product Haar
measure and the substitution U_-=θU'_+ give, for any positive-half A,

    q_j(A,A) := ω_j(overline{θA} A)
      = Z_j^(-1) ∫dU_∂ |∫dU_+ A(U_∂,U_+)e^(-S_+) |² ≥ 0. (5)

This rebuilds the site-reflection argument used by OSLEAF55 RP-lat.
In particular B∈𝔄_+∩𝔄_- and

    ||[B]||_j² = ω_j(B²),     <Ω_j,[B]> = ω_j(B).             (6)

The same holds for every bounded function of slice observables and
their spatial translates. A shift to 0<s<R/2 is supported in the positive
time half (every fixed s>0 is allowed eventually as R grows). It is generally **not compactly local in space** (§6.1).

### 2.2 Second moments and the correct limit passage

**Lemma B-limit.** Suppose nonnegative variables X_j converge in law to
X and sup_j E X_j²≤C<∞. Then

    E X²≤C,       E X_j→E X.                                (7)

Indeed min(x²,M) is bounded continuous; convergence followed by monotone
convergence gives E X²≤C. Also
E[X_j−min(X_j,M)]≤E[X_j 1_(X_j>M)]≤C/M, and the same bound holds for X.
Convergence of the truncated means and then M→∞ prove (7).
The identical argument applies to every coordinate of a joint limit.

Uniform second moments imply tightness for any countable magnetic family:
for coordinate ℓ choose R_ℓ with C_ℓ/R_ℓ²≤ε2^(-ℓ); the probability of
leaving ∏_ℓ[0,R_ℓ] is ≤ε. A metric inducing the countable product topology
is Σ_ℓ2^(-ℓ)min(1,|x_ℓ−y_ℓ|); finite-coordinate diagonal extraction shows
the displayed product is compact. To extract a law, diagonalize the
finite-dimensional distribution functions on rational rectangles, taking
one-sided limits at continuity points. Tightness prevents lost mass;
the resulting consistent finite-dimensional probability laws specify
the countable-coordinate law. All this extraction may refine the already
chosen e-test subsequence. It does **not** assert an ordinary probability
law for the singular smeared e-field.

Second-moment **convergence** is not a consequence: X_j=√j with
probability 1/j, zero otherwise, converges in law to zero, while E X_j²=1.
Thus a limiting vector norm below is E X², not automatically
lim_j E X_j². L² tail uniform integrability or L² convergence would be
additional information. A first moment alone is insufficient: a positive
variable with density (3/2)x^(-5/2) on [1,∞) has finite mean and infinite
second moment.

### 2.3 A common boundary Hilbert extension that can actually be proved

Let 𝒜_(e,+) be OSLEAF55's ordered positive-half test space, not the
polynomial space containing e(f)². Assume its cutoff RP forms q_j(F,G)
converge on a countable dense family and obey its stated uniform
continuity bounds. Let X_(j,ℓ) be a countable family of boundary variables
(3), satisfying the moment bounds of §4, with joint limiting law ν.

**Lemma B-boundary.** After one further common subsequence there is a
positive form on finite sums bF, F∈𝒜_(e,+), where b is in the bounded
algebra generated by the real truncations χ_M(X_ℓ)=min(X_ℓ,M), M rational
positive. Its Hilbert completion ℋ_∂ contains ℋ_e isometrically and a
vector b_ℓ=[X_ℓ] such that

    ||b_ℓ||² = ∫X_ℓ²dν < ∞,
    <Ω,b_ℓ> = ∫X_ℓdν = lim_j ω_j(X_(j,ℓ)).                 (8)

Proof. A boundary b factors out of the inner integral in (5); hence

    q_j(bF,bF) ≤ ||b||_∞² q_j(F,F).                          (9)

For finite sums, positivity and the elementary quadratic inequality
q(v+λw,v+λw)≥0 imply Cauchy–Schwarz. Thus each mixed Gram entry has a
uniform bound. Diagonalize all such entries on the countable rational
test/truncation algebra; every finite limiting Gram matrix remains
positive. Inequality (9) and the e-test continuity bounds extend the
form to each allowed test F. Its restriction to 𝒜_(e,+) is precisely
the original form, giving the isometric embedding after quotienting
null vectors and completing. Multiplication by any bounded boundary b
is well-defined and has norm ≤||b||_∞, since (9) holds with F replaced
by any finite sum b_iF_i.

On boundary vectors alone the form is ∫overline{b}c dν, because bounded
continuous functions of the joint X_j converge. For M,M'→∞,

    ||[χ_M(X_ℓ)]−[χ_(M')(X_ℓ)]||²
      = ∫|χ_M(X_ℓ)−χ_(M')(X_ℓ)|²dν → 0.

Here the integrable majorant is X_ℓ², furnished by (7). This defines
b_ℓ. Passing its norm and vacuum pairing to the limit proves (8).
The null quotient is legitimate: Cauchy–Schwarz shows that a zero-norm
vector is orthogonal to every vector. ∎

This proves a boundary extension and the requested norm mechanism without
pretending e has ordinary coincident moments. The vector can lie outside
the e-cyclic subspace. It supplies neither all mixed time-translated
products nor a continuous full Euclidean action. Those are precisely
the additional common-algebra/SHARP-B requirements below. In particular,
adding a sector and proving its non-freeness cannot by itself prove
non-freeness of the original e-only reconstructed theory.

If a common OS system realizes this boundary form, call its vector
[𝓑(t;0,x)]. Then

    f_B^YM(t) := <Ω,[𝓑(t;0,0)]> = ω(𝓑(t;0,0))              (10)

is a number in that reconstructed system. It is unchanged by a
vacuum-preserving equivalence that preserves this specified observable.
No densely defined operator acting on every field polynomial is claimed
from (8). Its vacuum-domain statement is exactly the finite norm in (8).

## 3. Library entry: the specified free comparator

### 3.1 Definition and reconstructed formula

Fix the observed color metric M⪰0 (for (3), M=I_(N²−1)). Define
𝔊_B^can to consist of centered Gaussian abelian field-strength theories
with N²−1 colors and tempered positive matrix spectral measure ρ(ds), s≥0,
whose **canonical reconstructed** magnetic two-point function at equal
time is

    ∫ρ(ds) ∫ d³p/(2π)³ · T_ij,kl(p)/(2√(|p|²+s)),
    T_ij,kl = p_i p_k δ_jl − p_i p_l δ_jk
              −p_j p_k δ_il + p_j p_l δ_ik.                 (11)

These are Maxwell, massive vector-curvature, and generalized-free
curvature comparators with the indicated observable calibration. The
positive spectral representation is their **definition** here, not an
imported tensor Källén–Lehmann theorem for interacting theories. No claim
that every free physical theory has this field family is made.

Their specified magnetic observable is

    𝓑_M^can(t,x) = (t²/4) Σ_(i,j≤3) (K_t³*F_ij)^T M(K_t³*F_ij),
    ρ_M(ds) := Tr(Mρ(ds)).                                  (12)

It is the uncentered square of finitely many commuting equal-time
Gaussian magnetic variables, when those variables have finite variance.
The identification of the YM label with (12) is part of membership in
this **marked comparator class**. It is not inferred from the
nonmultiplicative second-order map ID♮ on arbitrary observables.
Any companion e-observables in a full comparator must have a specified
consistent realization on its common test hierarchy; the proof below
uses only this fixed magnetic sector and makes no inference from an
unmarked equivalence or an unspecified e identification.

**Lemma B-free.** Its canonical reconstructed expectation is

    f_B^μ(t) = (1/(4π²)) ∫ρ_M(ds) J_B(ts),
    J_B(σ) = ∫_0^∞ v⁴ e^(-2v²)/√(v²+σ) dv,
    J_B(0)=1/8.                                             (13)

The exact finite-value condition at any fixed t>0 is

    ∫ min(1,s^(-1/2)) ρ_M(ds) < ∞,                         (14)

where the weight at s=0 is defined as 1. Under (14), all t>0 are
admissible; f_B^μ is nonincreasing in t and

    lim_(t↓0) f_B^μ(t) = ρ_M([0,∞))/(32π²) ∈ [0,∞].         (15)

Proof. The curl of a vector covariance with scalar mass denominator
(p_0²+|p|²+s)^(-1) gives T; a longitudinal term cancels in each curl.
For a magnetic component, T contains no p_0. Directly integrating
(p_0²+ω²)^(-1) by the arctangent gives
∫dp_0/[2π(p_0²+ω²)]=1/(2ω). This agrees with the equal-time covariance
(11), so no contact representative is being restricted to time zero.
For i≠j, T_ij,ij=p_i²+p_j²; summing the ordered pairs yields 4|p|².
Thus (12)'s expectation is

    t² ∫ρ_M(ds) ∫ d³p/(2π)³
                  |p|² e^(-2t|p|²)/(2√(|p|²+s)).            (16)

The angular measure is r²dr/(2π²). Substitution v=√t r gives (13).
With w=2v², ∫v³e^(-2v²)dv=(1/8)∫we^(-w)dw=1/8.
For 0≤σ≤1, J_B is bounded above and bounded positively below. For
σ≥1 its upper bound is σ^(-1/2)∫v⁴e^(-2v²)dv; restricting to 1≤v≤2
gives a positive constant times (1+σ)^(-1/2) as a lower bound. These
prove (14). The integrand decreases in σ, and increases to the σ=0
integrand as t↓0; positivity proves monotonicity and (15), including
infinite total spectral mass. ∎

**The free vacuum vector also has a second moment.** Write (12) as
Y^T A Y, with A⪰0 and Y a finite real Gaussian vector of covariance Q
after discarding unobserved directions. Expanding
E exp(z·Y)=exp(z^TQz/2) to order four gives the three Gaussian pairings.
Consequently

    E(𝓑²) = [Tr(AQ)]² + 2 Tr[(Q^(1/2)AQ^(1/2))²]
           ≤ 3[E𝓑]² < ∞.                                 (17)

The inequality follows by diagonalizing the finite positive matrix and
using Σλ_i²≤(Σλ_i)². Thus the equal-time square acting on the Gaussian
vacuum is a genuine vector, not just a finite formal expectation.

Allow also probability mixtures of these marked theories for which
the magnetic first and second moments required on the common domain
are finite, and marked scale-invariant free sectors with finite constant
f_B(t). Call this class 𝔉_B. Integrating nonnegative expectations
preserves f_B(t_1)≥f_B(t_0) whenever t_1<t_0. A sector with divergent
(14), or a mixture with infinite required second moment, cannot be a
matching member on this finite vacuum domain; that is a domain mismatch,
not a proof about the rest of its observables. For a semidefinite M,
only ρ_M is tested; an unobserved divergent color is not an obstruction.

### 3.2 Coefficient and representative corrections

For a Maxwell covariance C/p², (13) gives Tr(MC)/(32π²). With M=I and
C=g_std² I, the quadratic tree value is

    (N²−1) g_std²/(32π²)
       = N(N²−1) g_FLOW²/(16π²).                           (18)

This is the missing factor 2N at HINT2_55:302. It is a coefficient of
the specified quadratic comparator; no O(g⁴) bound for YM is asserted.

The canonical value (13) uses reconstructed equal-time covariance,
not arbitrary Euclidean contact terms. For example, a nonzero positive
polynomial contact in an observed magnetic covariance has p_0-polynomial
growth and cannot be integrated over p_0 at sharp time after only
spatial smoothing. It does not alter the canonical value by decree.
Requiring a matching canonical observable is part of the comparison.

The replacement for “only” at HINT2_55:312 and :555 is:
**“The time-zero magnetic construction is one sufficient route to a
reconstructed-theory number, provided its vacuum domain and common
observable realization are established.”** An ordinary ordered
positive-time OS test F also gives the reconstructed number
<Ω,[F]>=S(F), so a universal exclusivity assertion is false. Neither
observation removes the original 4D-flowed witness's identification gap.

## 4. Exact open inputs and their producers

The following are hypotheses, not results about YM. In addition to (F-B)
and (SEQ), retain the original N1F/N1S regularity, symmetry and RP inputs
on the **same enlarged system**, denoted **(ALG-B)** in §6. None is
silently supplied by the e-field-only construction.

**(MOM2-B).** For every magnetic label ℓ in the fixed countable enlarged
hierarchy (flow time t∈D={t^{(m)}:m≥m_0}, center, slice and orientation, with
specified cutoff approximants X_(K,R,ℓ)),

    sup_(admissible K,R) ω_(K,R)(X_(K,R,ℓ)²) ≤ C_ℓ < ∞.     (19)

For the flat basic label at t^{(m)}, admissible means K≥m+d_0, R≥R_0
and R/a_K even, with the center represented by a specified nearby lattice
site. Finite omitted depths obey (4). The constants are independent of
cutoff and volume; locally uniform versions in labels are needed wherever
ALG-B uses continuity. For
the basic plane these approximants are exactly (3); tilted/sphere
approximants must first be specified by ALG-B. No uniform bound as
t↓0 is required here. The minimal witness version uses just t_0 and
the chosen t_1; the all-grid version also gives the full UV statement.

**(TS-up)^B.** There exist C_+>0, 0≤ϑ<1 and d_0, independent of K,R,
such that for every K, R≥R_0 and d_0≤k≤K−m_0,

    f_(K,R)^B(t^{(K-k)}) ≤ C_+ g_k^(2(1−ϑ)).                 (20)

**(TS-low)^B.** There is c_->0, independent of K,R, such that for
K≥m_0+d_0 and R≥R_0,

    f_(K,R)^B(t_0) ≥ c_- g_(K-m_0)².                       (21)

Neither bound fixes a perturbative coefficient. For the sphere route
(19)–(21) must hold for the actual sphere approximants and trajectory,
uniformly in R and in the transported compact label families.

**(SHARP-B).** In the common continuum OS Hilbert system of ALG-B, the
spatially flowed magnetic family exists at sharp Euclidean time as a
vacuum vector. Precisely, for every selected (n,t,x), the positive-time
vectors obtained by translating normally by ε>0 satisfy

    [𝓑_n(t;x+εn)] → b_(n,t,x) in Hilbert norm as ε↓0,
    b_(n,t,x) = lim_(M→∞) [χ_M(𝓑_n(t;x))],
    ||b_(n,t,x)||² = ∫X_(n,t,x)² dν < ∞.                    (22)

Here the boundary truncations and ν are the **same joint limits of the
same cutoff observables** as in §2.3; the first line is evaluated in
the OS system with normal n. Local approximations, if used to define
the full-slice observable, must give this same limit. This is sharp-time
existence, finiteness and identification, not merely a finite numerical
expectation or a new random variable attached to the e-state. It asserts
only the vacuum domain of the unbounded magnetic square. A domain for
arbitrary products is separate. MOM2-B supplies the finite norm once
the boundary is identified; it does not prove the strong ε-limit.

### 4.1 What the named upstream sources do and do not supply

| Input | Existing source, exact scope, and missing version | Comparison with 4D 𝓔 |
|---|---|---|
| MOM2-B | SRCCD55 §3.3 **SRC-κ** starts “For n ≥ 2 and fine sites x_1, …, x_n with mutual distances ≥ 4a” and concerns e-cumulants; §3.2 says “For OS0 the minimal list is 𝒪_0 := {e_a}”. It does not contain the coincident square of the spatially flowed magnetic composite. A B-source extension with cutoff/volume-uniform second derivatives of the generating functional, a uniform first moment, and control of the LF part would supply (19). EXISTENCE X-SRC-GAP's **H-src-flow (OPEN)** is for 4D-flowed E_t and spacetime-smeared sources; its extension to this sharp-time observable, including point/spatial-smearing limits, remains open. | Stronger than MOM-E's mere 1+δ moment when 0<δ<1; if δ≥1, the moment exponent alone is no stronger. Removing temporal smoothing leaves an additional UV issue. No comparison inequality between the two random fields is known here. |
| (TS-up)^B | HINT2_55 R2.4 names **(SRC)**, “two-sided control of E[𝓔(t)(U₀) \| level-k field]”, or **(FLOW-BLK)**. Their 3D magnetic versions are needed for the proposed transport proof. The same section proposes **(LF-inst)** for concentrations surviving the flow. ASSEMBLY55 **N15/F17** leave this route open. No source supplies either the 3D transport or the relevant event/amplification bound. | The one-slice support is easier for RP. The upper estimate has at least the same unresolved bare-to-block transport task, and no established temporal smoothing. It is not shown easier; formal implication “𝓔 bound ⇒ B bound” is unavailable. |
| (TS-low)^B | HINT2_55 R2.4: “(SRC) at the coarse level plus anti-concentration of the level-k₀ fluctuation”. EXISTENCE §10.4 says the deterministic X-NTAF lower bound uses **H-Bal-1** and **H-loc-LF**. They apply to the S4c block law, not (3). A lower transport comparison for the magnetic observable together with a corresponding noise-free anti-concentration theorem would supply (21). | Same type of missing lower comparison, with no known ordering of difficulty. The deterministic bounded block witness's lower bound does not transfer merely because both observables are magnetic. |
| SHARP-B | HINT2_55 R1.9: “The 3D-flowed field at sharp time is not smoothed in time”; its YM finiteness is “not established”. CODEX_REVIEW_HINT2 F7 leaves its continuum observable/domain unverified. ASSEMBLY55 F1 explicitly lists “sharp-time finiteness”. No existing result supplies (22). | An extra sharp-time/domain task beyond fixed positive 4D flow, which smooths the time coordinate too. The 4D lane's nonperturbative estimates are themselves open; this is not a claim that all 4D problems are already solved. |

Two source distinctions matter. EXISTENCE §2 labels **H-Bal-1**
“IMPORTED-NOT-YET-REVERIFIED” and says “the proof was never seen by either
lane”; the stated volume uniformity and SU(N) extension are additional
conditions. It would supply a coupling bracket only in its own scheme
after conventions and trajectory were matched. It supplies no B moment
or sharp-time theorem. EXISTENCE §11.2 labels **H-loc-LF** “HYPOTHESIS
(new; no source)”; it is a regular-region/local-polymer description of
the deterministic block law. Its clause LF-P is

    ν_(K,m)(|V_p−1|≥ε_0/3) ≤ C_P exp(−a_P/g²).

It concerns a coarse plaquette, not all fine concentrations surviving
the 3D magnetic flow. H-loc-LF and the soft scheme's RLF are not
interchangeable. H-sg is an additional upper-bound input for the
deterministic block route, not a proof of (20).

**LF-inst is sufficient only after its missing transport hypotheses.**
For example, suppose one could prove a positive decomposition with
contributions bounded by C L^(4(k−j))1_(E_(j,k)), an appropriate small-field
bound, and

    P(E_(j,k))≤C exp(−c_LF u_j),
    u_j≥u_k+β_-(k−j)log L−R_F,      c_LF β_->4.             (23)

Then summing expectations of that large-field part gives at most

    C exp(c_LF R_F) exp(−c_LF u_k)
       /[1−L^(4−c_LF β_-)].                                (24)

This is just the geometric series in r=k−j≥0. It rebuilds the
conditional estimate; no event decomposition or probability bound for
YM is asserted. An analogous L² triangle estimate for the same terms
uses Σ_r L^(4r)P(E_(k-r,k))^(1/2), requiring c_LF β_->8 by that particular
method. Thus the first-moment sufficient condition in (23) does not
automatically furnish MOM2-B. Neither threshold is proved necessary.

In the units (1), the expression exp(−8π²/g_std²), **if supplied** as an
instanton weight, becomes exp(−(4π²/N)u). The source's stated one-loop
slope 11N²/(12π²) would give product 11N/3. These are a convention
conversion and conditional arithmetic, not a probability estimate or a
derivation of that slope. An arbitrary positive β_- from F-tune does
not supply the numerical lower bound required in (23).

CODEX_REVIEW_HINT2 F4 also corrects the attribution to Balaban: the
current source distinguishes a fixed small-field cut from Dimock's
exp(−c₂p_j²) template. Failure of the weaker proposed union-bound
estimate proves only that that estimate is insufficient. It does not
prove divergence of the actual YM expectation, necessity of LF-inst,
or that all Balaban/Dimock estimates have the weaker form. The
flow-survival claims in HINT2_55 R2.4 carry [m] there and are **not used**
in this proof. Balaban and Dimock are credited for the upstream RG
methods, without importing their estimates as established here.

## 5. Theorem T0-OS: the corrected separation reduction

### 5.1 Statement

Assume the common OS realization **(ALG-B)**, common sequence **(SEQ)**,
trajectory **(F-B)**, and **MOM2-B, (TS-up)^B, (TS-low)^B, SHARP-B**.
The common realization is an explicit premise, not a consequence of
the four scalar/moment inputs. Use the marked free class 𝔉_B of §3,
with the same labels, units and specified canonical magnetic composite.

Set

    A := c_-/U_+(m_0) > 0.

Choose any fixed integer m_1>m_0 with

    C_+ U_-(m_1)^(ϑ−1) ≤ A/2,      t_1 := t^{(m_1)} < t_0.    (25)

Such m_1 exists because β_->0 and ϑ<1. It is fixed before the cutoff
limit and independent of K,R. Define the continuous finite-moment
witness

    W_B(ω) := [f_B^ω(t_0)−f_B^ω(t_1)]_+,
    [x]_+ := max(x,0),          c := A/2.                   (26)

Then the reconstructed theory satisfies

    |W_B(ω_YM)−W_B(μ)| ≥ c > 0       for every μ∈𝔉_B.       (27)

Moreover,

    max_(t∈{t_0,t_1}) |f_B^YM(t)−f_B^μ(t)| ≥ A/4,           (28)
    f_B^YM(t_0)≥A,           lim_(m→∞) f_B^YM(t^{(m)})=0.        (29)

Consequently it is outside the marked comparator class. This establishes
the quantitative non-freeness implication at that scope, not absolute
non-freeness of an unmarked theory. No claim that 𝔉_B is exactly T_OS's
unresolved OWN-free choice is made.

### 5.2 Proof, including the OS step

For K≥m_1+d_0, (2), (20) and (21) yield

    f_(K,R)^B(t_0) ≥ c_-/u_(K-m_0) ≥ A,
    f_(K,R)^B(t_1) ≤ C_+ u_(K-m_1)^(ϑ−1) ≤ A/2.           (30)

The second inequality uses the negative exponent ϑ−1. Thus their
difference is at least A/2 uniformly in cutoff and volume. On the
common sequence, B-limit and MOM2-B give convergence of both means;
no subtraction of two unrelated limit points occurs. Equations (30)
therefore hold for their limiting means. For each fixed m the same
argument gives f_B^YM(t^{(m)})≤C_+U_-(m)^(ϑ−1), proving (29).

By B-boundary the limiting slice variable has the Hilbert vector
[𝓑(t)] with squared norm ∫𝓑(t)²dν. ALG-B and SHARP-B identify that
boundary extension with the sharp-time limit in the common reconstructed
system. Thus its mean is exactly <Ω,[𝓑(t)]>, by (8)–(10), at **both**
t_0 and t_1. This is the Euclidean-to-reconstructed bridge consumed in
(27); a first moment or an unrelated joint Euclidean state would not
provide it.

For every μ∈𝔉_B, B-free and mixture positivity give
f_B^μ(t_0)−f_B^μ(t_1)≤0. Therefore W_B(μ)=0, while (30) gives
W_B(ω_YM)≥A/2. This proves (27). Write y_i=f_B^YM(t_i) and
z_i=f_B^μ(t_i). Since y_0−y_1≥A/2 and z_0−z_1≤0,

    A/2 ≤ |(y_0−z_0)−(y_1−z_1)|
         ≤ |y_0−z_0|+|y_1−z_1|,

which proves (28). Finally a vacuum-preserving equivalence of marked
observable systems preserves these vector pairings, contradicting (27).
This is the asserted nonmembership. ∎

W_B is Lipschitz in its two moment coordinates:
|W_B(y)−W_B(z)|≤|y_0−z_0|+|y_1−z_1|. Thus it meets PANEL_P1's
finite-moment continuity condition once the common topology controls
these means. Only grid times are needed. On a translation-invariant
flat torus one can additionally rebuild HINT2's inter-scale estimate:
the spatial sum of the unscaled density in (3) is S_3; along its
negative gradient dS_3/dτ=−||∇S_3||²≤0. Translation invariance makes
the unscaled mean nonincreasing. Hence f^B(t)≤L⁴f^B(t^{(m+1)}) for
t^{(m+1)}≤t≤t^{(m)}, above the allowed cutoff depth. Continuous-time limit
statements would require the corresponding extended common hierarchy;
they are not needed for (27).

### 5.3 Why the literal requested one-point inequality cannot be asserted

Keep f_B(t) with its original meaning, the one-point function (13).
Let y=f_B^YM(t_0)>0. For M=I and n=N²−1, the Maxwell spectral measure

    ρ(ds) = (32π² y/n) I_n δ_0(ds)

is a legitimate nonzero member of 𝔊_B^can, has all the required Gaussian
magnetic moments by (17), and has f_B^μ(t_0)=y. Therefore

    |f_B^YM(t_0)−f_B^μ(t_0)| = 0.

It cannot be bounded below by a common positive c for every such μ.
This directly refutes that scalar formulation for the comparator class
allowed to vary its normalization. It does not refute the profile
separation (27)–(29). If an externally calibrated narrower class fixes
a positive uniform lower bound on its value at a chosen short scale,
then (20) can give a one-point separation there; that lower bound is
additional input. Nothing here derives it for arbitrary masses and
normalizations. Formula (27), not a renamed one-point function, is the
valid replacement matching PANEL_P1 item 4.

## 6. (ALG): the extension, its action, and the exact unproved interfaces

### 6.1 What cannot be included by notation

OSLEAF55 D2–D7 uses

    𝒜_e = ⊕_(q≥0) ^0𝒮((R⁴)^q),
    ^0𝒮 = Schwartz tests flat to every order on e-collisions,
    𝒜_(e,+): tests supported in 0<s_1<⋯<s_q.

Its product is partial. For ordered F,G the reflected product
ΘF*⊗G avoids every collision; f⊗f need not. The identity e(f)²∈𝒜_e
must not be used. A delta test supported on s=0 is also not an element
of this Schwartz test domain. The boundary construction in §2 adjoins
new variables and finite boundary moments; it does not obtain them by
evaluating the separated S_q on a forbidden diagonal.

Nor is the magnetic observable determined algebraically by the scalar
e-field. On smooth commuting Cartan-valued connections, compare constant
curvatures F_01=H and F_12=H, with the same nonzero H and all other
independent components zero. The scalar tr F² agrees at every point.
One realization is A_1=Hx_0; its time-zero spatial connection is zero
and its B is zero. Another is A_2=Hx_1; its spatial curvature is
constant and stationary under the 3D abelian flow, so B>0. Thus no
identity making B a function of all scalar e values holds on this
configuration domain. This is an algebraic counterexample, not a claim
about which configurations have positive YM probability, nor a proof
that a state-specific Hilbert closure is impossible.

Full-slice flow is spatially nonlocal. Already its abelian curvature
linearization is K_t³*F, where

    K_t³(z)=(4πt)^(-3/2) exp(−|z|²/(4t)) > 0

at every z. A smooth exact curvature perturbation far from x can change
the convolution at x (integration by parts against the nonconstant heat
kernel exhibits such a perturbation). Its magnetic square therefore
depends on arbitrarily distant spatial data. The same nonzero quadratic
variation is the contraction of the nonlinear flowed observable, so
strict finite spatial support cannot be asserted for that observable
either. Smearing its **center** over a compact set does not remove the
tails. OSLEAF55 §4 explicitly excludes flowed fields from its
“finite list of local gauge-invariant composites”.

These are the exact obstructions to a literal inclusion into the
existing e-only local test algebra. They do not prevent an enlarged
algebra with a suitable completion. They identify what must be built.

### 6.2 The covariant family and which transformations act

For a unit normal n, modulo n↔−n, define the proposed B_n(t;x) by
tangential magnetic flow on H_(n,x)={y:n·(y−x)=0}, with tangential
curvature and the induced three-dimensional metric. For g=(R,b)∈E(4),
the covariant label action is

    α_g B_n(t;x) = B_(Rn)(t;Rx+b).                          (31)

It obeys α_gα_h=α_(gh) by direct substitution. For smooth data, whenever
the classical tangential flows exist uniquely on the stated time interval,
the gradient-flow equation transforms with the induced metric and
gauge-invariant action; uniqueness gives (31) for the transformed field.
This proves covariance on that domain, not continuum existence or
uniqueness of the nonlinear flow. Invariance of a continuum random state
still needs H_Euc on this enlarged family.

For the parallel-slice family n=e_0, the subgroup preserving that family
is (O(1)×O(3))⋉R⁴. Spatial translations and O(3) rotations preserve a
fixed zero-time slice and act directly on its boundary algebra. Time
translations move it to parallel slices; nonnegative time translations
preserve the positive-half support. Time reflection fixes the zero-time
magnetic energy and exchanges the open halves. Rotations mixing time
and space act only after adjoining the n≠e_0 copies. A finite hypercubic
lattice provides exact coordinate-normal copies and discrete rotations,
not a dense rotation group or exact arbitrary-angle copies.

Moreover a tilted **full** hyperplane has arbitrarily positive and
negative x_0 whenever n is not parallel to e_0. No finite translation
puts its entire support in x_0≥0. Thus a tilted B with positive center
time cannot be inserted into the original positive-half cone just on
that basis. For each normal n use the support-defined cone 𝒜_(n,+);
α_g maps it to the cone for the transformed hyperplane. In the chosen
OS Hilbert space, spatial E(3) acts unitarily and positive time acts by
the reconstructed semigroup when the requisite continuity is supplied.
An arbitrary Euclidean rotation mixing time is not thereby a unitary
on that same Hilbert space.

### 6.3 A precise sufficient common-system contract (ALG-B), still OPEN

The proposed extension has a common local core containing the original
ordered e-tests and **specified local regularizations** of the magnetic
family, and a boundary/quasilocal completion containing full-slice B.
One possible cutoff regularization uses 3D flow on a finite spatial
domain with a fixed gauge-covariant boundary prescription. This is a
definition of approximants, not a proof of convergence to (3).

The following are the exact additional interface obligations for this
choice. They are part of the inherited N1F/N1S algebra hypotheses and
are not consequences of (19)–(22).

1. **Common maps and mixed OS0.** Specify local-core cutoff maps A_j(F)
   for e-tests and the local magnetic regularizations, their products
   on the permitted separated domain, and their conjugation/reflection
   maps. For each compact range of positive flow times, caps and
   regularization labels, the mixed r-insertion functionals must obey
   a common continuous test-space estimate of the form
   |S_(j,r)(F)|≤C^r(r!)^p p_(sr)(F), with C,p,s independent of j,R,r.
   Here p_(sr) is a specified Schwartz-type seminorm of order at most
   sr, including the chosen label topology; it must be matched to the
   reconstruction formulation actually used. No ordinary e(f)² or
   unspecified coincident extension is included. The e-only SRC-κ
   bounds do not establish this mixed estimate.
2. **Common action and mixed OS1.** The local-core domain and topology
   must carry the continuous action (31), together with the scalar
   action on e-tests. On every pair (F,g) in a countable determining
   family times a countable dense subgroup, require
   S_j(α_gF)−S_j(F)→0 along the same sequence. Rotated copies may be
   defined via controlled cutoff approximation; using unrelated rotated
   states does not define their joint law. For N1S require the fixed-R
   sphere action and the contraction bounds on these mixed tests too.
3. **Support-compatible mixed OS2 and OS3.** Only actual positive-half
   supported local regularizations enter the cone. Require their
   lattice reflection pairings to obey RP, or uniform errors tending
   to zero; their mixed limits and permitted permutations must exist.
   Unflowed e insertions stay strictly time ordered away from their
   collisions. Boundary truncation products may coincide with one
   another because their bounded joint moments are separately defined;
   this grants no new coincident e moment. On aligned flat slices (5)
   supplies RP exactly, including mixed cutoff e-observables. General
   tilted regularizations must satisfy the same support test, not merely
   have positive center times.
4. **Localization and completion.** For each magnetic label ℓ there
   must be compactly supported approximants X_(j,ℓ)^r, with support
   growing in the slice as r→∞, and a bound such as

       sup_j ||X_(j,ℓ)−X_(j,ℓ)^r||_(L²(ω_j)) → 0.          (32)

   Require compatible bounds for the reflected variables, transformed
   labels and each mixed test that is passed through this limit. This
   identifies the full-slice variable with a completion of the **same**
   local core; SHARP-B supplies its sharp-time identification. Another
   construction may replace (32), but must provide the same convergence
   and support conclusions. No such estimate is proved here.

**Conditional compatibility proof.** On the countable common core,
the bounds in item 1 make every coordinate bounded. Diagonalize them
all, along with every mixed RP form and symmetry defect. The estimate
|S_j(F)−S_k(F)|≤2C^r(r!)^p p_(sr)(F−F_d)
+|S_j(F_d)−S_k(F_d)| extends convergence from the dense tests F_d to
the stipulated test space, preserving the OS0 bound. Every RP form is
a finite sum of convergent entries and is nonnegative by item 3;
continuity extends it to the ordered cone. Bosonic permutation and
reality identities pass term by term, proving OS3. For fixed g in
the dense subgroup, item 2 gives invariance on the dense tests; test
continuity extends it to all F. Continuity in g then extends invariance
to E(4), proving OS1. Item 4 and Cauchy–Schwarz pass each controlled
quadratic form and mean to the completion; boundary truncation limits
are precisely §2.3. SHARP-B identifies the resulting boundary vectors
with the positive-time reconstructed system. These are the OS closure
steps N1F consumes, now with their full joint domain stated. ∎

This proof establishes compatibility **if the interface estimates and
maps exist**. It is not a construction of them. In particular:

- MOM2-B controls one-observable second moments, not all mixed orders
  required in item 1 or products such as B(s)A_F at s>0. Inequality (9)
  uses the reflection boundary and cannot just be moved to s>0.
- Defining (31) proves an action on labels, not state invariance in
  item 2; H_Euc for e alone says nothing about these mixed tests.
- The pure e cone stays OSLEAF55's ordered cone. The boundary module
  is a legitimate extension of that cone, not an evaluation of its
  forbidden contact distributions.
- A full-slice B belongs to a completion, not a fixed bounded local
  region. If PANEL_P1's “local” requires a strictly compactly supported
  witness, an additional uniform localization argument must produce
  that witness and preserve its free-comparator separation. Equation
  (32) on the YM side alone does not provide uniform approximation over
  the entire free class. That strict-local consumer is still open.

The common OS system in Theorem T0-OS is therefore the enlarged one.
Showing it is generated by the e-field, or that the boundary vector
belongs to ℋ_e with the required observable interpretation, would be
a further theorem. No tensor/multiple-field OS-to-Wightman theorem is
used here from memory; full local relativistic reconstruction remains
an inherited assembly obligation. The Hilbert quotient, norm, pairing,
and separation actually used in this note were rebuilt explicitly.

## 7. Consumer table: exact statements and the discharged portion

Quotes below are from the frozen local sources identified in the log.
Ellipses appearing inside a quote are those in the source. Source files
are not edited by this task.

| Consumer | Exact source quotation | What this note supplies; what remains |
|---|---|---|
| **ASSEMBLY55 N5**, flat | “A specified continuous finite-moment witness W vanishes on the named class of free physical theories and satisfies \|W(ω_{a_j,R_j})\| ≥ c > 0 … at fixed nonzero renormalized coupling. The witness is local and survives the physical OS quotient” | Equations (26)–(30) give the continuous witness and a uniform positive margin on the common sequence, conditional on the displayed premises. Equation (8), ALG-B and SHARP-B give its reconstructed pairings. Compact locality and the original e-only identification remain open as specified in §6. |
| **ASSEMBLY55 F1** | “H_int ↛ T_OS: the witness is not on the OS algebra”; “no file proves that non-freeness of the joint Euclidean state on 𝔈 implies non-freeness of the OS theory reconstructed from the e-field.” | Provides the boundary-vector mechanism and a reduction on an explicitly enlarged marked OS system. It does not prove the quoted implication for the original e-only theory or make the four YM leaves imply ALG-B. F1 is conditionally repaired at this enlarged-system scope, not unconditionally discharged. |
| **PANEL_P1 §3 item 4** | “A specified continuous finite-moment witness W vanishes on the named class of free physical theories and satisfies \|W(omega_{a_j,R_j})\| >= c > 0, with its sign or separation from zero controlled, at fixed nonzero renormalized coupling. The witness is local and survives the physical OS quotient; it does not count auxiliary soft noise.” | W_B has exactly the required zero value on the named marked free class and positive sign for the hypothesized YM values. It uses bare spatial links, not auxiliary soft noise. The common local-system and sharp-time prerequisites are exposed, rather than inferred from the finite-moment inequality. |
| **CODEX_REVIEW_P4 §4.3** | “Non-freeness is not a closed property.”; “P4 needs a fixed-scale, correctly normalized observable witness separated by a positive amount from its calibrated free Yang–Mills comparator, uniformly in both cutoff and radius.” | (25) fixes both physical scales before the limit; (1)/(18) fix normalization; (30) supplies a cutoff/radius-independent margin **if** the same bounds hold for the sphere magnetic construction. The order is fixed-R continuum then R→∞; §1 explains the conditional lattice diagonal. Sphere construction, mixed covariance, and radius-uniform bounds remain open. |

ASSEMBLY55 N15's exact status is “All **OPEN**”; F17's heading is
“(TS-up) needs a large-field estimate of instanton strength (OPEN, no
mechanism on disk).” This note leaves N15 open and narrows F17's
necessity wording to the conditional route (23)–(24), in accord with
CODEX_REVIEW_HINT2 F4. No source or audit status is changed.

## 8. Result and recovery boundary

Proved here: cutoff boundedness and temporal support; exact site RP;
a conditional boundary Hilbert extension with its correct norm and
vacuum pairing; moment limit passage without assuming second-moment
convergence; the canonical Gaussian formula, its domain, monotonicity
and 2N conversion; and Theorem T0-OS as the explicit conditional
two-scale separation reduction. The “only sharp-time” statement and
the requested universal one-point gap have been corrected by direct
counterexamples to those formulations.

Open: MOM2-B, both TS bounds, SHARP-B, the inherited F-tune/sequence
conditions, and the genuinely mixed/covariant/local content of ALG-B.
These contain substantive YM estimates and observable identifications;
calling the reduction proved does not discharge them. The consumer
match to a strictly local e-only theory and to an owner-selected full
meaning of “free” remains unresolved. This is the exact stopping
boundary of the requested author block, which explicitly forbids
proving the YM inputs. Review and verification receipts are in the log.
