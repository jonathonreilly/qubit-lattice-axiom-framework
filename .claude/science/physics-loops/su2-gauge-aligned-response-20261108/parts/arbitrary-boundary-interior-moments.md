# Arbitrary-exterior interior moments for the compact two-step quotient

Author proof, 2026-11-09; independent mathematical check pending. This note
uses the actual full compact two-step quotient, terminal V=I, β=u≥1,
λ=κu, fixed odd L≥3 and κ>0. It does not condition on a chart or a good
exterior. No covariance, connected response, physical gap or full gluing
claim follows from the moment estimate proved here.

Inputs read in full: `compact-energy-coercivity.md`, `local-conditional-tail.md`,
and `rough-component-bound.md`, at the root worktree snapshot recorded below.
The inherited base is `55fd670ff8995427b24617b2273bd3f78b7559d9`.
Workflow/workhorse instructions were already read for this coherent assignment;
its preflight passed. No numerical, network or Git action is used here. The
previous `chart-fourth-connected-bound.md` is preserved. Only this deliverable
is written. The reference-cap method follows the prior repo work credited by
the local-tail input (and its Bałaban/Dimock antecedents); the additional step
here is the exact radial comparison under arbitrary exterior data.

## 1. Exact statement, ownership and reader conventions

Use periodic terminal-cell l-infinity distance. Each cell owns the retained
links whose tails it contains: all fine non-tree links and all intermediate
links, exactly M=3L^8+1+4L^4 coordinates. Set b_e=1−w(a_e)∈[0,2].
For a nonempty cell set R, J_R contains all M|R| owned coordinates. Let P_R
and C_R be every whole plaquette or kernel factor whose syntactic retained
readers meet J_R, including all input words, hidden outputs and constant
normalizers. As proved in the input reader count, every such exterior reader
belongs to B=N_1(R)\R. Let T_R=Σ_(e∈J_R)b_e and T_B(z)=Σ_(e∈J_B)b_e(z).
We deliberately include all owned collar coordinates in T_B, even unused ones.

For every exterior z, the conditional density relative to normalized product
Haar is exactly

    D_R(z)^(-1) exp[−u E_R(a,z)] Π_(c∈C_R) H(κu r_c),
    H(t)=exp(t)/Z(t),
    E_R=Σ_(p∈P_R)(1−w(U_p))+κΣ_(c∈C_R)(r_c−<v_c,M_c>).

There exist λ0>0 and A,B0<∞ depending only on L,κ and the supplied forest
geometry, independent of volume,R,z,u, such that

    log E[exp(λ0 u T_R)|z] ≤ A|R|+B0 u T_B(z).           (1)

Consequently, for constants a,b≥0 independent of those variables,

    E[T_R|z] ≤ a|R|/u+b T_B(z).                         (2)

Take any larger cell region Ω, fix an entirely arbitrary exterior to Ω, and
let its law be the exact Gibbs conditional above. For any x and integer
s≥0 such that N_s(x)⊂Ω, there are C<∞ and q∈(0,1), uniform also in Ω
and its exterior, with

    E[Σ_(e owned by x)b_e] ≤ C/u+C(2s+1)^4 q^s.          (3)

Thus sufficiently deep interior coordinates have O(1/u) mean chord-square,
with an explicit boundary-distance remainder. The statement is about the
conditional mean, not pointwise smallness or correlations.

## 2. Global upper bounds on individual energy factors

For a unitary word Q=A_1⋯A_l, telescoping and Cauchy–Schwarz give

    1−w(Q)=|I−Q|²/2 ≤ l Σ_(j=1)^l [1−w(A_j)].         (4)

Inverse occurrences have the same b and multiplicities are retained; tree
links and terminal links are I and contribute zero. For an arithmetic mean
M of path words P and a unitary output v,

    0≤ψ:=|M|−<v,M>≤1−<v,M>
       =average_P [1−w(v†P)]
       ≤(p+1) average_P Σ_(occurrences in v†P) b_e,      (5)

where p=5L bounds input word length. This uses |M|≤1 and no derivative
of |M|; M=0 is included. Similarly

    0≤1−|M|≤1−w(M)=average_P[1−w(P)]
                     ≤p average_P Σ_(occurrences in P)b_e. (6)

Plaquettes have length four. Every retained link occurs in at most six
plaquette factors and nine output-inclusive kernel factors. Counting repeated
word occurrences by p+1 yields finite constants K_E,K_r, depending only on
L,κ, such that for ANY selected factor family

    Σ selected energy factors ≤ K_E Σ all their retained readers b_e,
    κ Σ selected kernels (1−r_c) ≤ K_r Σ all their retained readers b_e. (7)

A direct conservative choice is K_E=24+9κ(p+1)² and K_r=9κp²;
these enlarge the actual multiplicity sums and are not asserted optimal.
Summing over all readers in any containing cell set remains an upper bound.
The same constants bound arbitrary subfamilies, including outside factors.

## 3. Absolute coercivity localized with an arbitrary collar cost

Let c_E>0 be the global compact-coercivity constant from the first input:
E(full field)≥c_E Σ all retained b_e. Given a on J_R and z outside, construct
a full field a-tilde that agrees on J_R and J_B and equals I everywhere else.
Because every selected factor reads only R∪B, its value is unchanged. Every
omitted factor reads no J_R; its only nonidentity retained readers are in J_B.
Equation (7) thus bounds the sum of omitted nonnegative energy factors by
K_E T_B. Global coercivity gives

    E_R(a,z) ≥ c_E T_R−K_E T_B(z).                      (8)

The c_E T_B contribution could be retained but is unnecessary. This argument
uses full-factor selection; an output-only or normalizer-truncated selection
would not justify it. It works even for disconnected R, wrapped collars, or
R equal to the whole torus, where B is empty and no factor is omitted.
Separately (7) directly gives

    E_R(a,z)≤K_E(T_R+T_B),
    κΣ_(c∈C_R)(1−r_c)≤K_r(T_R+T_B).                   (9)

## 4. Exact normalizer comparison and matched Haar powers

Under the positive tilted Haar law proportional to exp(tw(Q)),

    (log H)'(t)=1−E_t w(Q).

For t≥0, E_t w lies in [0,1]: the upper bound is pointwise, and the lower
bound follows by pairing w and −w in the symmetric Haar marginal, since
w sinh(tw)≥0. Therefore 0≤(log H)'≤1 for t≥0. For every r∈[0,1],

    H(κu) exp[−κu(1−r)]≤H(κur)≤H(κu).                 (10)

This includes r=0 and kernels whose normalizer is constant under the local
conditioning. Instead of estimating H(κu) by u^(3/2), we retain it exactly;
it will cancel for the actual number k=|C_R| of selected kernels.

Choose any fixed 0<d0≤1 and integrate the product cap
K={|a_e−I|≤d0/sqrt(u), e∈J_R}. Put n=|J_R|=M|R|. On K,
T_R≤n d0²/(2u). The normalized Haar cap estimate is
Haar{|Q−I|≤h}≥c_cap h³ for 0<h≤1, with c_cap>0 fixed.
Using (9),(10) inside the exact denominator gives

    D_R(z)≥H(κu)^k exp[−(K_E+K_r)u T_B
                            −(K_E+K_r)n d0²/2]
                       (c_cap d0³)^n u^(−3n/2).        (11)

No lower bound on individual r_c and no smooth exterior hypothesis entered.
Its loss for an arbitrary collar is explicitly exp[−const·u T_B].

Choose λ0=c_E/2. The unnormalized numerator for exp(λ0uT_R), by (8),(10),
is at most

    H(κu)^k exp[K_E u T_B]
          Π_(e∈J_R) integral_SU(2) exp[−(c_Eu/2)b(Q)]dQ
       ≤H(κu)^k exp[K_EuT_B] K_0^n u^(−3n/2).          (12)

Here K_0 depends only on c_E. To verify the Haar integral bound directly,
write b=1−cos θ and Haar radial density (2/π)sin²θ dθ. Use
1−cos θ≥2θ²/π² and sin²θ≤θ² on [0,π], and extend the Gaussian
integral to infinity. This bounds the integral by a constant times t^(−3/2)
for every t>0, so small c_Eu introduces no exception.

Dividing (12) by (11) cancels BOTH H(κu)^k and u^(−3n/2), with no omitted
constant normalizers and no estimate depending on total volume. Thus (1)
holds with B0=2K_E+K_r and any nonnegative A at least

    M [log(K_0/(c_cap d0³))+(K_E+K_r)d0²/2].             (13)

Enlarge A if necessary. Jensen applied to exp(λ0uT_R) gives (2) with
a=A/λ0, b=B0/λ0. Increasing b to max(b,1) keeps (2) valid and ensures
the strict contraction parameter below belongs to (0,1).

## 5. Tower property and interior iteration

Fix the exact conditional law μ_Ω with arbitrary exterior to Ω. For
R_r=N_r(x)⊂Ω put m_r=E_(μ_Ω) T_(R_r). For 0≤r<s, the collar of R_r
is exactly R_(r+1)\R_r in periodic l-infinity distance. Conditional on all
coordinates outside J_(R_r), the Gibbs density inside is the same complete
factor conditional used in (1), because all other factors cancel. Applying
(2) pointwise and then the tower property gives

    m_r≤a|R_r|/u+b(m_(r+1)−m_r),
    m_r≤q m_(r+1)+[a/(1+b)]|R_r|/u,
    q=b/(1+b)∈(0,1).                                   (14)

The collar variables may be strongly correlated; no independence is used.
Since |R_r|≤(2r+1)^4 on every periodic torus, iteration yields

    m_0≤q^s m_s+[a/((1+b)u)] Σ_(r=0)^(s−1)q^r(2r+1)^4.

Pointwise T_(R_s)≤2M|R_s|, so

    m_0≤2M(2s+1)^4q^s+C1/u,
    C1=[a/(1+b)]Σ_(r≥0)q^r(2r+1)^4<∞.                  (15)

Equation (3) follows with C≥max(2M,C1). At s=0 the iteration is empty
and the bound is the elementary compact bound m_0≤2M. If a ball is already
the whole torus, its next collar is empty; (14) is still valid, with
m_(r+1)=m_r. For Ω equal to the whole torus, arbitrary s is permitted,
so sending s to infinity in (15) gives m_0≤C1/u for every cell, without
requiring translation invariance of the chosen forest. For proper Ω, (15)
holds for every available interior radius and makes no assertion that its
boundary remainder vanishes when u alone tends to infinity.

## 6. Checkpoint and precise limits

Closed at author-proof level: global word-based energy upper bounds;
local lower energy bound with arbitrary collar cost; the exact monotone
normalizer comparison; the conditional exponential moment with matching
Haar powers; and the one-cell interior estimate by conditional iteration.
All assertions retain both hidden levels and every selected normalizer.
The exact factor-selection convention, finite reader radius and compact
coercivity are load-bearing inherited inputs. Their identities are below.
Independent verification of this new proof is pending.

This is not a claim that arbitrary exterior data induce weak dependence.
Small expected b_e does not control covariance or the two-source/two-score
connected cumulant, and differentiation of (1) is not used to claim such a
bound. Compact rough-field connected gluing and source-complete conditional
normalization remain separate tasks. No source prompts, audit status, axioms,
original input notes or earlier proof draft were changed.

Input SHA-256 identities (provenance, not mathematical validation):

- `compact-energy-coercivity.md`: `7e8e798759239aadfc8c137125bf23f6d1de2cac18b714ddca70ea294cbaa4aa`
- `local-conditional-tail.md`: `cf47acdfe0deea09fe49f7b08d90d45a3aac0df3251062ba4f67f566e639072d`
- `rough-component-bound.md`: `1a4c40385f1fc492033f261f8ed938bed23f32475eb9a116347fd7361f9e9c44`


## 7. Strengthening: uniform radial tilts and joint rare-set bounds

This section strengthens (1)–(3) for the actual full compact law, without a
component-event or good-exterior assumption. Independent checking is pending.
Constants here are uniform over the entire tilt profile; they may be larger
than the particular untilted constants in (13)–(15). Write T_x for the sum
of b_e over coordinates owned by cell x, and retain c_E from (8).

For a profile 0≤θ_x≤t_*=c_E/2, tilt the full Gibbs density by

    exp[u Σ_x θ_x T_x].                                (16)

On a region Ω with fixed arbitrary exterior, only terms with x∈Ω affect
its normalized law. All terms outside Ω are constants and cancel. On further
conditioning to R⊂Ω, ownership makes every tilt with x∉R constant as well.
Thus the exact conditional negative leading energy is

    E_R^θ(a,z)=E_R(a,z)−Σ_(x∈R)θ_x T_x(a),             (17)

with the same full factor sets, Haar measures and H factors. No exterior
penalty has been dropped from E_R; only additive constants from the explicit
tilts cancel. E_R^θ need not be nonnegative, which causes no problem: the
proof below uses its stated lower bound, not nonnegativity of tilted factors.

By (8) and θ_x≤c_E/2,

    E_R^θ≥(c_E/2)T_R−K_E T_B.                          (18)

Because θ_x≥0, E_R^θ≤E_R, so the original cap denominator lower bound
(11) remains valid without alteration. The H comparison (10) is unchanged.
For λ_*=c_E/4, the numerator for exp(λ_*uT_R) now has residual damping
exp[−(c_Eu/4)T_R]. Repeating the exact product Haar integral in (12), with
c_E/4 replacing c_E/2, proves

    log E_θ[exp(λ_*uT_R)|z]
        ≤ A_*|R|+B_* u T_B,                            (19)

uniformly in θ,R,z,volume,u≥1. One may retain B_*=2K_E+K_r; A_* uses
the new Haar integral constant in (13). In particular all normalizers,
including those constant under conditioning, still cancel by their exact
common H(κu)^k factor. The reserve c_E/4 is positive even when some θ_x
reach t_*; the bound does not rely on strict interior tilt parameters.

Jensen gives the analogue of (2) with a_*=A_*/λ_*, b_*=B_*/λ_*.
Enlarge b_* to at least one and set q_*=b_*/(1+b_*)∈(0,1). The tower
argument (14) uses conditionals of the same fixed profile θ, so it applies
unchanged and yields constants C_*<∞ independent of θ with

    E_(Ω,θ) T_x ≤ C_*/u+C_*(2s+1)^4q_*^s,
                         whenever N_s(x)⊂Ω.            (20)

Here C_* can be chosen as max(2M,[a_*/(1+b_*)]
Σ_(r≥0)q_*^r(2r+1)^4). The profile can be entirely inhomogeneous;
translation invariance was not used. On the whole torus, arbitrarily large
s are allowed and the last term vanishes, giving

    E_θ T_x≤C_*/u for every x and every allowed θ.       (21)

### 7.1 Coupling-parameter integration and all-set exponential moments

For any cell set A in the full torus define, in the UNTILTED full compact law,

    f_A(t)=log E exp(tu T_A),  T_A=Σ_(x∈A)T_x.

Finite compact integration allows differentiation at all real t. For
0≤t≤t_* its exact derivative is

    f_A'(t)=u Σ_(x∈A) E_(θ=t 1_A) T_x≤C_* |A|,         (22)

using (21). Since f_A(0)=0, deterministic integration in t proves

    log E exp(tu T_A)≤C_* t |A|,  0≤t≤t_*.             (23)

No covariance inequality or substitution by products of means occurs.
The same proof permits integration from any allowed background profile
along a nonnegative direction while the whole path remains in the allowed
profile box, but (23) only needs the path beginning at zero.

Let R_A(δ) be the event that EVERY x∈A owns at least one retained coordinate
with chord distance |a_e−I|≥δ, for 0≤δ≤2. The witnesses in distinct cells
are distinct by ownership. Pointwise on this event,

    T_A≥δ²|A|/2.

Markov's inequality and (23) therefore give, for every 0<t≤t_*,

    P(R_A(δ))≤min{1, exp[(C_*t−tuδ²/2)|A|]}.            (24)

This holds for every deterministic A, including disconnected sets, wrapped
sets and the whole torus, without collars or component conditions. The empty
set has probability one and both sides are one. If uδ²>2C_*, the choice
t=t_* supplies exponential rarity in |A|. At δ=0 the bound is simply one.
This is a joint all-rough-event bound, not independent Bernoulli domination:
no corresponding uniform conditional single-cell probability bound under
arbitrary exterior has been proved.

### 7.2 One-coordinate tails and every fixed positive moment

For a retained coordinate e owned by x, b_e≤T_x, so (23) with A={x}
gives, for 0≤h≤2 and any fixed 0<t≤t_*,

    P(|a_e−I|≥h)≤min{1, exp(C_*t)exp(−tu h²/2)}.        (25)

For h>2 the probability is zero, so the Gaussian upper bound continues to
hold. For every fixed real p>0, tail integration yields

    E|a_e−I|^p
       =p integral_0^2 h^(p−1)P(|a_e−I|>h)dh
       ≤exp(C_*t) Γ(1+p/2) (2/(tu))^(p/2).              (26)

Thus the full compact quotient has volume-uniform O(u^(−p/2)) chord moments
of every fixed order, without a chart restriction. Bounded local collections
inherit corresponding norm moments by finite-sum inequalities. These are
radial/chord moments; signed-coordinate centering or invariant-source Taylor
claims require their own symmetry and regularity statements. This supplies
an alternative concentration route, not a replacement for the spatial
covariance input in the earlier chart four-insertion proof.

### 7.3 Exponential moments with arbitrary exterior to a larger region

Under μ_Ω with arbitrary fixed exterior, take A⊂Ω and choose, independently
for each x∈A, any integer s_x≥0 with N_(s_x)(x)⊂Ω. Define
f_(Ω,A)(t)=log E_(μ_Ω)exp(tuT_A). The same derivative identity (22)
now uses (20), uniformly for θ=t1_A throughout 0≤t≤t_*. Therefore

    log E_(μ_Ω)exp(tuT_A)
      ≤t C_*|A|+t C_*u Σ_(x∈A)(2s_x+1)^4q_*^(s_x),
                                      0≤t≤t_*.         (27)

No conditioning or independence among the balls is needed; their overlap is
irrelevant to the expectation sum. Applying Markov gives the analogous
joint rough-cell bound with the additional displayed boundary-distance cost.
Equation (27) does not assert that this cost is small near arbitrary rough
exterior data. Constants are uniform in that data, its tilt profile and the
volume.

Updated author checkpoint: (19)–(27) establish uniform radial-profile moment
control, all-set joint rough-cell tails in the full compact torus, and fixed
coordinate moments, in addition to the arbitrary-exterior interior estimate.
They do not establish decay of connected cumulants, covariance mixing, or
source-complete gluing. In particular neither rare-set bounds nor individual
small fluctuations alone justify such conclusions. Independent checking of
the final strengthened proof remains pending.
