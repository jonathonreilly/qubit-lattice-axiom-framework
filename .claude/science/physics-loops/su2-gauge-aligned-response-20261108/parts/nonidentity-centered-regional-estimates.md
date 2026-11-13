# Regional estimates at a fixed nonidentity stationary center

Conditional author proof, 2026-11-09. Assigned revision
`97fc90828ab071b5813d1c9b6c8a952dc042509b`. The center premise below is
separate. The argument uses the existing regional Haar-cap and shell methods,
with the change of energy and the product-domain checks proved here.

## 1. Actual law and center premise

Fix odd L≥3, κ>0, m≥3, u≥1, and the allowed terminal-block forest
with arbitrary internal trees. The fine torus has side L²m. Delete the
seven terminal kernels J on the boundary union of the two distinct
adjacent plaquettes. The hidden coordinates a are the fine non-tree and
intermediate links. The other terminal outputs V in O=E2\J are fixed with
uniformly small chord distance to I. Probability Haar is the reference
measure. Retain every fine plaquette, level-zero kernel, and O terminal
kernel as a whole factor. Their energies h_f are respectively 1−w(U_p)
and

    Φ_u(v,M)=κ(1−⟨v,M⟩)+u^(-1)[log Z(κu|M|)−log Z(κu)],
    Z(s)=∫ exp(s w(Q))dQ,     H(s)=exp(s)/Z(s).                  (1)

A kernel is exactly H(κu)exp(−u Φ_u). The seven deleted kernels integrate
to one with respect to their terminal probability Haar variables. Both
the numerator and radial normalizer of every surviving kernel enter (1).
The compact energy is Ehat_V=Σ_f h_f with the fixed u understood.

Each terminal cell owns M0=3L^8+1+4L^4 coordinates by tail. For a cell
set A let Q_A be these coordinates and B_A=N_1(A)\A the collar in periodic
cell l-infinity distance. Select the full factor family F_A whose
syntactic reduced hidden readers S_f meet Q_A. The model inputs are the
actual law and reader templates of the regional supplier §§1–2: bounded
reader arity and incidence, with exterior readers of selected factors
inside Q_(B_A), counting the hidden K0 outputs and all radial-normalizer
readers. The reduction sets tree links to I. Periodic coincidences may
repeat a word occurrence, which the fixed template bound includes.

Assume a configuration a* for this u,V and geometry satisfies

    D_q Ehat_V(a*q)|_(q=I)=0,
    Ehat_V(a*q)−Ehat_V(a*) ≥ c T_all(q),
    T_A(q)=Σ_(e∈Q_A)b(q_e),    b(q)=1−w(q)=|q−I|²/2,            (2)

for all compact q, with uniform c>0. A coercivity assumption in squared
chord units implies (2) by rescaling c. The product a*q denotes a*_e q_e
in each coordinate. Assume max_e |a*_e−I|≤Cε and max_c |V_c−I|≤ε
for sufficiently small ε, uniformly in u, volume, J and the allowed
trees. Smallness here puts the finitely many reader slots of each
background factor inside the fixed smooth chart below. Freeze this one
center throughout the proof. Haar is preserved by the coordinatewise
translation, so q=I represents a* in every region and exterior.

## 2. Whole-factor compensation and arbitrary exteriors

For each factor and hidden reader e let ℓ_f,e be the coefficient of
the right-increment derivative at q=I in the coordinate
q_e=exp(i x_e·σ). Use the quaternion convention
Im(exp(i x·σ))=x sin(|x|)/|x|. Define the local function

    hbar_f(q)=h_f(a*q;V)−h_f(a*;V)−Σ_(e∈S_f) ℓ_f,e·Im q_e.      (3)

Its value and first derivative vanish at q=I. To obtain a uniform
quadratic majorant, use two regimes. On a fixed sufficiently small
product cap in the q_e, all a*_e q_e lie in the common identity chart of
the templates. Word telescoping there gives |M|≥1/2 for every mean. In
this chart, (1) equals κ(|M|−⟨v,M⟩)+
u^(-1)[h(κu|M|)−h(κu)] for h(s)=log Z(s)−s. The pinned chart estimate
|h^(j)(s)|≤C_j(1+s)^(-j), j=1,2, bounds the first and second derivatives
of h(κu|M|) in all local slots, since (κu)^j/(1+κu|M|)^j≤2^j.
Smooth multiplication by the frozen a*, exponentiation, and the bounded
template arity give a common Hessian bound for (3) in the x coordinates,
and a common bound on |ℓ_f,e|. Taylor's integral remainder and
|x_e|≤(π/2)|q_e−I| prove the majorant on the cap.

For the complement, 0≤(log Z)'(s)≤1 for s≥0 by symmetry of Haar scalar
part and its pointwise bound by one. Integrating this derivative shows
κ(|M|−⟨v,M⟩)≤Φ_u(v,M)≤κ(1−⟨v,M⟩)≤2κ. Wilson energies are in
[0,2]. Thus (3) is uniformly bounded on the full compact domain using
|Im q_e|≤1 and bounded arity, including zero means. Off the cap at
least one b(q_e) exceeds a fixed positive constant. For all q, then,

    |hbar_f(q)| ≤ C_loc Σ_(e∈S_f)b(q_e).                        (4)

Empty-reader factors have hbar_f=0. Summing (4) over any factor subfamily
costs at most K times the sum of b over its readers, for K≥1 chosen
using the uniform incidence bound. By (2) stationarity gives exactly
Σ_(f:e∈S_f) ℓ_f,e=0 for each e. The same Im q_e was used in every factor,
so Σ_f hbar_f(q)=Ehat_V(a*q)−Ehat_V(a*) on the entire compact product.

Set Ebar_A=Σ_(f∈F_A)hbar_f. For each interior e all factors reading e
lie in F_A, so their linear terms cancel as well. In detail,
Σ_(f∈F_A)h_f(a*q;V)=Ebar_A(q)+D_A(z), where

    D_A(z)=Σ_(f∈F_A)h_f(a*;V)
         +Σ_(e∈Q_(B_A))(Σ_(f∈F_A:e∈S_f)ℓ_f,e)·Im z_e.          (5)

This is constant in q_A. The physical regional weight is therefore
C_A(z)exp(−u Ebar_A) with
C_A(z)=H(κu)^(k_A) exp(−u D_A(z)), times any field-independent Wilson
convention factor. Here k_A is the actual selected surviving kernel
count. This common scalar cancels from a regional ratio using the same
selection and exterior. The factorization of the physical density
still allocates the original whole factors.

Set q_e=I outside Q_(A∪B_A) and keep q_A,z_B. Every selected factor
is unchanged. Omitted factors read no interior coordinate, so (4) bounds
their aggregate in absolute value by K T_(B_A)(z). Applying global
coercivity (2) to the extended field and subtracting the omitted sum
gives, together with (4),

    c T_A−K T_(B_A) ≤ Ebar_A ≤ K(T_A+T_(B_A)).                  (6)

No sign of hbar_f is required. The extension uses no smallness of z.
Wrapped or disconnected regions and the full torus obey the same
argument, with the collar empty in the full case.

## 3. Cap estimate, profile transfer and moments

Use either the full compact product for all u≥1, or the common real
chart which requires q_e=exp(i x_e·σ), |x_e,k|<ρ(u) for every component,
where ρ(u)=p(u)/√u, p(u)=log(2+u)^A_scale with A_scale>5/2. For the
chart take u large enough that √3ρ lies in a fixed injective log domain.
All chart domains are products over whole links and over cells. For
fixed 0<d≤1 the product chord cap |q_e−I|≤d/√u lies in each such
regional chart once (π/2)d<p(u). The norm estimate for the principal
log verifies this inclusion componentwise. Use Haar on both domains.
When using scalar logs its Jacobian is included by this measure.

Fix any profile 0≤θ_x≤t_*=c/2 and tilt by exp(u Σ_x θ_x T_x).
For the conditional on A the compensated energy is Ebar_A−Σ_(x∈A)θ_x T_x.
The lower bound in (6) becomes (c/2)T_A−KT_B and its upper bound is
unchanged. Write B=B_A, n=M0|A|. By Haar radial density
(2/π)sin² α dα, the cap has mass at least (c_cap d³)^n u^(−3n/2).
There T_A≤nd²/(2u). The tilted physical denominator in either domain
therefore obeys

    I_A(θ;z) ≥ C_A(z) exp(−K u T_B−Knd²/2)
                           (c_cap d³)^n u^(−3n/2).             (7)

For λ=c/4 the exponential-moment numerator is bounded by

    C_A(z) exp(Ku T_B)
             [∫ exp(−cu b(Q)/4)dQ]^n
       ≤ C_A(z) exp(Ku T_B) K_H^n u^(−3n/2).                   (8)

In the chart the positive numerator was enlarged to the compact
product. For the last bound use b=1−cos α≥2α²/π² and sin²α≤α² and
extend the resulting radial Gaussian integral to infinity. Division
gives log E_θ[exp(λuT_A)|z]≤A0|A|+2KuT_B, with
A0=max(0,M0[log(K_H/(c_cap d³))+Kd²/2]). The same C_A(z), including
its actual H(κu) count, and u powers cancel exactly.

For the tower, fix one profile and one domain, and condition the
regional law on a smaller cell set. Its conditional again has (5)–(8)
for that set: whole factors with no interior readers and exterior profile
terms are constants, and the product chart restricts the new interior
coordinates to the same per-link cube. These identities hold for the
explicit conditional kernels. A compact exterior can also be fixed
arbitrarily when forming a regional chart law directly. Further
conditioning inside it preserves that exterior and the product
restriction. The broken rotation symmetry of a Cartesian cube does
not enter the estimates.

For clarity, the remaining tower steps of the pinned regional proof
§4 apply with the following constants. Jensen gives
E_θ[T_A|z]≤a0|A|/u+b0 T_B for a0=A0/λ and b0=max(1,2K/λ).
Let ζ=b0/(1+b0)<1. Fix the larger region Ω and its exterior.
If N_s(x)⊂Ω, taking expectations for A=N_r(x), r<s, gives

    m_r ≤ ζ m_(r+1)+a0 |N_r(x)|/[(1+b0)u],
    m_r=E_θ T_(N_r(x)).

The collar is exactly N_(r+1)(x)\N_r(x). Since
|N_r(x)|≤(2r+1)^4 and m_s≤2M0(2s+1)^4, iteration yields
E_θ T_x≤C/u+C(2s+1)^4 ζ^s. On the full torus s can increase without
bound even after the balls saturate, so the second term disappears.
For A⊂Ω integrate the derivative of log E exp(tuT_A) from 0 to t≤t_*.
The derivative is u Σ_(x∈A) E_(θ=t1_A) T_x by bounded differentiation.
For N_(s_x)(x)⊂Ω this gives

    log E_(Ω) exp(tuT_A) ≤ tC|A|+
                       tCu Σ_(x∈A)(2s_x+1)^4 ζ^(s_x).         (9)

In the full compact or full common chart law the second term is absent.
For each e owned by x, T_x≥|q_e−I|²/2. Markov's inequality and integration
of the tail over h>0 give, for each fixed ν>0 and 0<t≤t_*,

    E |a_e−a*_e|^ν = E |q_e−I|^ν
      ≤ exp(tC) Γ(1+ν/2)(2/(tu))^(ν/2).                        (10)

The chart statement uses the large-u range above and the compact
statement all u≥1. For fixed-order products Hölder supplies the
corresponding joint bound from (10), with no independence or zero-mean
assumption.

## 4. Two regional ratios with distinct denominators

For an arbitrary-exterior rough-event ratio, fix δ∈(0,2] and a nonempty
cell set S. Let B_S require that every cell of S own at least one e with
|q_e−I|≥δ. Then T_S≥δ²|S|/2 on B_S. Choose a nonnegative integer h such
that C(2h+1)^4 ζ^h≤δ²/4, and put R=N_h(S). In either allowed regional
domain, (9) and Markov give

    P_R(B_S|z) ≤ min(1,exp[t_* C|S|−t_*uδ²|S|/4]).            (11)

For u≥max(1,8C/δ²) this is at most η^|S| for
η=exp(−t_*uδ²/8), uniformly in every quotient exterior. For varying δ
the buffer must obey its displayed condition. With finite real bounded
sources, let Z, Z_bad, Z_good use the whole physical factors, the same
domain, sources and exterior, and the three selectors 1, 1_(B_S),
1_(B_S^c), respectively. The center cap gives Z_good>0, since it has
positive measure and strictly positive density. Exactly
Z_bad/Z_good=p/(1−p) and log(Z/Z_good)=−log(1−p) with p=Z_bad/Z.
At zero sources and η≤1/2 both ratios (the ordinary and the log)
are bounded by 2η^|S|. The good-event restriction allows many fields
outside the all-good chart.

The compact-decomposition denominator instead uses the entire chart
domain of R. To verify its ratio estimate, use the common cube in §3 and
put τ=ρ²/(2π²). A cell is good if T_x<τ. For each of its links the
principal log has length at most (π² b(q_e)/2)^(1/2)<ρ/2, so the
all-good condition implies chart membership. Put
α=min(1,c/(8K)). For a nonempty core A and j≥0 let
I_j=N_(2j)(A), R_j=N_(2j+1)(A), S_j=N_(2j+2)(A)\R_j. Its physical
collar is S_j. Use the first-successful-shell selector of the pinned
decomposition, now evaluated on q. It requires A bad, R_j\A good,
T_(S_j)≤α T_(I_j), and failure for each earlier j. On this selector,

    c T_(R_j)−2K T_(S_j)
       ≥ (c/2)T_(R_j)+(c/2)T_(I_j)−2K T_(S_j)
       ≥ (c/2)T_(R_j)+(c/4)τ|A|.                            (12)

The two collar costs K T_(S_j) are one from the numerator lower
energy bound (6) and one from the denominator cap (7). Radial
normalizers have already been included in Φ_u. At zero marks the
compact, chart, and compact-minus-chart selector integrals divided
by the entire chart denominator are each between zero and

    C_shell^|R_j| exp[−c u τ|A|/4].                          (13)

Indeed (12) retains a Gaussian weight exp(−cu T_(R_j)/2) for
integration, bounded as in (8), and C_A(z) in (7) is the same
physical prefactor with A replaced by R_j. The complement integral is
one positive integral over the compact region minus the regional
chart. The chart denominator uses neither the selector nor a cap
restriction. The cap serves only to lower-bound it. Estimate (13)
holds for every fixed exterior on the physical collar. The history
identities use good exteriors there.

For a uniform first success take the least positive integer J_max
satisfying (1+α)^J_max τ>2M0(4J_max+1)^4. Existence and
J_max=O(1+log(1/τ)) follow by comparing exponential growth to the
fourth power. If every shell test fails then
T_(I_(j+1))>(1+α) T_(I_j), so
T_(I_(J_max))>(1+α)^J_max τ|A|. But
T_(I_(J_max))≤2M0(4J_max+1)^4 |A|, a contradiction. Wrapped and saturated
balls obey the same upper volume bound. Consequently
|R_j|≤(4J_max+1)^4 |A| for j<J_max. The entropy factor in (13) has
logarithm O(log(u)^4)|A|, whereas uτ=log(2+u)^(2A_scale)/(2π²).
For sufficiently large u (13) is at most exp(−c u τ|A|/8).
The threshold is independent of volume, the pair and the allowed trees.

## 5. Exact marks, frozen coordinates and orbit terms

For bounded real quotient marks X_i on the compact product, a fixed
translation to q leaves each complete retained-coordinate support
unchanged as a reader envelope. For marks supported in sets of diameter
at most D≥1, assign each whole exp(ξ_i X_i) with support touching R to
its marked regional density, using the same marks in the numerator
and entire chart denominator. A separation of distinct cores by
more than 4J_max+2D+4 ensures active region distance at least 2D+7.
This is the radius that allows the whole-source allocation of the
pinned marked decomposition, whose exterior source readers lie in
N_D(R)\R. The phase-wedge estimate for Σ_i |ξ_i| ||X_i||∞<ε_mark<π/2
applies to the assigned subset of marks. Each regional or global
unrestricted chart or compact denominator has real part at least
e^(−ε_mark) cos(ε_mark) times its positive unmarked integral. Each
marked selector integral in §4 has absolute value at most
e^(ε_mark) times its corresponding unmarked integral, also for the
single compact-minus-chart integral. The bound (13) therefore
acquires only the factor e^(2ε_mark)/cos(ε_mark) per active region.
The first-successful-shell geometry and the finite conditional
integration in §§2–6 of the marked supplier use exactly these
product domains, good cells, whole factors and same marked
denominators. A field-independent mark remains in the global
normalized generating function. The normalization of the chart
generating function and that of the compact-to-chart quotient both
retain their source dependence.

For a bounded original source pair F,G, the exact regional ratio in
(11) can instead be formed on the joint quotient and root-fixed
orbit variables. Reconstruct the original hidden chain U(a*q,h_orb).
Use the whole physical weight times exp(sF(U)+tG(U)) with product
probability Haar in h_orb, for each of the three selectors. The
physical weight depends only on the quotient. This is the same
forest disintegration as in the pinned regional moments supplier,
with the hidden coordinates translated by a fixed group element.
At zero sources the orbit integral is one. For real s,t, the mixed
derivative of the log of any positive restricted integral is

    E_q Cov_(h_orb|q,s,t)(F,G)
                 + Cov_q(E[F|q,s,t],E[G|q,s,t]).               (14)

All expectations use that restricted joint law. In particular the
first term survives if a source varies on the orbit. This formula is
the tower identity for covariance, or follows by differentiating
the joint orbit integral before integrating q. It provides no
whole-source allocation for a general orbit integral of marks.

When evaluating terminal derivatives at base V, keep a*, q, the
quotient exterior, chart and all selectors frozen. Vary only the
outputs in the actual untransformed whole factors. A surviving
terminal output c has log-weight score κu⟨dot V_c,M_1,c(a*q)⟩
when its factor is selected. An unselected output cancels from
regional ratios and a deleted output has no factor. The terminal
normalizer is independent of that output. Two distinct terminal
labels and the two source labels enter the log weight separately.
For a subset I of these distinct labels the derivative of the
normalized bad probability is the joint cumulant of its indicator
and the selected insertions, by adding the indicator as an
auxiliary linear source. Each partition term has one block
containing that indicator. Bounding this block by p times the
product of the relevant sup norms and the other blocks by their
sup norms gives |D_I p|≤b_|I| p Π_(i∈I)||X_i||∞, with b_k the sum
of (number of blocks−1)! over partitions of k+1 labels.
The chain rule for −log(1−p), at p≤1/2, then bounds its full
two-terminal/two-source derivative by a universal constant times
u² κ² |dot V_c||dot V_d| ||F||∞||G||∞ η^|S|, using (11).
This jet is at the fixed base and zero sources.

Although a*(V) may depend on all terminal outputs, freezing it makes
(3) and the original translated factors local functions of their hidden
coordinate readers. This gives no locality or bounds for derivatives
of the family V↦a*(V), moving selectors or moving chart domains.

## 6. Sources and checkpoint

Read at assigned worktree revision, with paths relative to this pack.

| Source | Coverage | SHA-256 |
|---|---|---|
| parts/marginal-regional-moments-and-ratios.md | Full, 432 lines | b2d3d9bedfb52b11056788e1f72cd14c4f9846c733c86ee424c2240f13db647f |
| parts/marginal-normalized-regional-coercivity.md | Full, 325 lines | bd3fa8b5eb989c7718ad5d760a913e33166f3e9edcf52b9f17f82cbd809ca255 |
| parts/marginal-source-marked-compact-decomposition.md | Full, 541 lines | 4a30c12ef9c58eaf3d6ca1c82bab94137f088ee59cba73304fe30da9e04dcdd3 |
| parts/marginal-nonlinear-chart-estimates.md | Full §§1–3, lines 1–226 | b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7 |

The supervisor supplied the repo and literature first pass. No compact
background theorem is imported. The proof uses (2) as an explicit
premise, with the actual law, disintegration and reader templates
inherited as specified. Independent checking remains due. The only
deliverable is this note. No code, existing source, editable prompt,
Git state or claim status was modified.
