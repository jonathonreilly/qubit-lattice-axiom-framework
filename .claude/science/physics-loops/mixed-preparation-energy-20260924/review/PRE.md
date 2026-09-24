# Independent PRE: fixed finite electric-word preparations

The zero-field pure input is not essential to the leading actual-birth energy
or the stated finite-apparatus Fisher/frequency lower bounds. On every fixed
finite span of physical N=4 low electric words, those leading coefficients are
uniform over all density operators, including epsilon-dependent mixtures,
coherences and rank changes. The decisive fact is an operator statement: the
rotor leading low and first-high birth maps are constant multiples of
isometries carrying the same input label. A mixed-state commutator witness
then supplies the Fisher lower bound. Variance alone does not.

This reconstruction is conditional on the supplied model and the unchanged
parent perturbation estimates. It precedes release or reading of
`preparation-uniform-personal` and does not use that directory, the current
campaign checkpoint, or `continuous-coherence-personal`. No author code or
campaign numerical builder was imported. This is not a formal audit or a new
certification of the transitive parents.

## 1. Fixed support, model and reused hypotheses

Retain the cube with A={0,3,5,6}, B={1,2,4,7}, A-to-B edges, original Gauss
constraint `div E=q-1_A`, integer spin S, C=S(S+1), lambda=0 compensation,
and fixed positive delta,K with `epsilon^2 C=delta/K`. Write

    h=W+epsilon T+epsilon^2 C_S,   T=-(F+F*),
    H=delta epsilon^-4 h,         F=sum_a F_a.

The N=4, W=0 physical sector has all A charges +1 and every B vacant:
total charge is four, and all four occupied sites are already on A. Its
electric words are precisely the allowed divergence-free integer fields.

Fix a nonzero finite-dimensional subspace V spanned by finitely many such
word basis vectors. V and its electric labels do not grow with S. Let P_V
denote its projector and let rho_epsilon be any density supported in V;
neither convergence of rho_epsilon nor a lower bound on its nonzero
eigenvalues is required. For sufficiently large S every word and every
finite leading birth path lies inside the spin box.

Let U_4 be the exact canonical Hermitian low-band isometry with the parent's
positive polar convention. The actual input is `rho_in=U_4 rho_epsilon U_4*`.
Choose one original edge-(0,1) mark j_i: plus, minus, or their stipulated
coherent sum. Define

    k_i=j_i U_4 P_V,  z_i=Tr(k_i rho_epsilon k_i*),
    theta_i=k_i rho_epsilon k_i*/z_i.

Thus theta_i is the actual normalized conditional birth density, usually
mixed. No energy projection is inserted into the mark.

The following source results are reused, with their stated fixed-graph,
uniform-in-S hypotheses: analytic canonical spectral rotations and parity
expansions; the exact local identity for the first-high birth coordinate;
the canonical low Hamiltonian

    U* H U|P = delta epsilon^-2 D/C + delta H4_S + O(epsilon^2)
             = K D + delta H4_S + O(epsilon^2),             (1)

with uniformly bounded H4_S and remainder; and separated Hermitian clusters
with grade-one center delta epsilon^-4 and remainder O(epsilon^-2).
The apparatus parent's finite-dimensional SLD variational inequality,
additivity/monotonicity and covariance frequency lemma are also reused.
Their hypotheses are retained below. Source identities are listed in Section
10 and the seal. This PRE does not use a trace-density limit to estimate an
unbounded microscopic energy.

## 2. Operator-valued birth coordinates

On the N=4 low domain define the maps

    B_i,S=j_i F P_4=j_i F_0 P_4,
    R_i,S=(1/2)j_i F^2 P_4-F B_i,S=-F_0 B_i,S.             (2)

Here F on the left of B_i,S is the N=6 hopping operator. For the local
equality, F_0 squared vanishes; distinct-center hops commute, including
hard-core blocking of a common B target; and a mark at center 0 commutes
with the other-center hops. Exactly two orderings of each different-center
pair occur in F squared. Their factor one half cancels all the other-center
terms in F B_i,S. The same-center term remains with a minus sign. These are
finite-spin identities, not rotor-only approximations.

Let V_6 be the parent's canonical full Hermitian cluster unitary, with bare
N=6 grades Pi_0, Pi_1, Pi_2. In its coordinates,

    Pi_0 V_6* k_i = epsilon B_i,S P_V + O(epsilon^3),
    Pi_1 V_6* k_i = epsilon^2 R_i,S P_V + O(epsilon^4),
    Pi_2 V_6* k_i = O(epsilon^3).                         (3)

The source's low/complement rotation gives the same displayed leading maps;
resolving the complement into its separate Hermitian clusters does not
alter these leading orders. Uniform analytic bounds and W parity justify
the remainders. All are operator-norm bounds on V, so subsequent trace
estimates hold uniformly for every rho_epsilon in the stated class.

## 3. Exact finite-spin weights and the rotor isometries

For a field value e define squared shift weights

    d(e)=1-e(e-1)/C,       u(e)=1-e(e+1)/C,

for lowering and raising the field, respectively. Moves outside the spin
box are blocked. Let e_0=E_01, e_2=E_02 and e_4=E_04 on an input word, and
abbreviate d_j=d(e_j), u_j=u(e_j).

The two terms of B_sigma,S first move the positive charge at 0 to leaf 2
or 4 and then create the sigma,-sigma pair at 0,1. Their amplitudes are

    sqrt(w_sigma(e_0) d_2),  sqrt(w_sigma(e_0) d_4),
    w_+(e)=u(e),            w_-(e)=d(e).

Their electric shifts are `sigma e_01-e_02` and
`sigma e_01-e_04`, respectively, where e_ab here denotes a unit edge vector.
The final occupied B leaf distinguishes the two outputs.

For R_+,S, the two histories have the same final matter configuration and
electric shift `e_01-e_02-e_04`. Their amplitudes add to
`-2 sqrt(u_0 d_2 d_4)`. For R_-,S, the two final negative-charge locations
are different. The amplitudes are
`-sqrt(d_0 d_2 u_4)` and `-sqrt(d_0 u_2 d_4)`, with shifts
`-e_01-e_02+e_04` and `-e_01+e_02-e_04`. All R words have vacancies at 0
and the opposite vertex 7. Every fixed channel translates E injectively.

These matter distinctions and injective translations prove the following
operator identities on the electric-word basis, including their zero
off-diagonal entries:

    B_+,S* B_+,S = u_0(d_2+d_4),
    B_-,S* B_-,S = d_0(d_2+d_4),
    R_+,S* R_+,S = 4 u_0 d_2 d_4,
    R_-,S* R_-,S = d_0(d_2 u_4+u_2 d_4).                  (4)

The plus and minus B ranges are orthogonal. Their R ranges are also
orthogonal: the negative charge is at 1 for plus and at 2 or 4 for minus.
Consequently both Gram operators for the coherent mark are the sums of the
corresponding plus/minus expressions in (4).

In the rotor all displayed shift weights are one. Hence, on the entire
physical N=4 low rotor space,

    B_i* B_i=b_i I,  R_i* R_i=r_i I,
    (b_i,r_i)=(2,4), (2,2), (4,6).                        (5)

The ranges of B_i and R_i are in different W grades. Therefore
`L_i=B_i/sqrt(b_i)` and `M_i=R_i/sqrt(r_i)` are two orthogonal isometries
carrying the same input Hilbert space. This is stronger than the old
single-word norm calculation and is the mixed-state ingredient needed here.

On V, all fields occurring in (4) stay bounded. Thus

    ||(B_i,S-B_i)P_V||+||(R_i,S-R_i)P_V||=O(1/C)=O(epsilon^2),
    B_i,S*B_i,S|V=b_i I_V+O(epsilon^2),
    R_i,S*R_i,S|V=r_i I_V+O(epsilon^2).                   (6)

Constants depend on V but not on the density within V. In particular, no
allowed sequence of mixtures or coherences can make the leading mark
probability vanish. At a moving spin-boundary input this conclusion fails:
for circulation n=S on 0-1-3-2-0, u(E_01)=0 and the plus mark is leading-order
blocked. That example is outside the fixed-span premise.

## 4. Uniform actual-birth energy moments

Equations (3)-(6) give

    z_i=b_i epsilon^2+O(epsilon^4).                       (7)

The canonical low input energy-vector norm is uniformly bounded on V by
(1), since D is bounded on a fixed finite set of words. For the same reason,
the leading born low vectors B_i,S V have bounded D. In the exact low
coordinate, the normalized output is supported there up to an
O(epsilon^2) operator correction; multiplication of that correction by the
global low Hamiltonian norm O(epsilon^-2) still gives O(1).

The actual full-H moment expansions consequently are, uniformly in rho_epsilon,

    Tr(H theta_i)=delta (r_i/b_i) epsilon^-2+O(1),
    Tr(H^2 theta_i)=delta^2 (r_i/b_i) epsilon^-6+O(epsilon^-4),
    Var_theta_i(H)=delta^2 (r_i/b_i) epsilon^-6+O(epsilon^-4). (8)

One may also obtain these by tracing the parent's operator expansions:
the finite-spin slow numerator `Tr(Q_S B_i,S rho B_i,S*)` is O(1/C), while
`Tr(R_i,S rho R_i,S*)=r_i+O(1/C)`. The first-high probability is
`epsilon^2 r_i/b_i+O(epsilon^4)`, its gap is
`delta epsilon^-4+O(epsilon^-2)`, and the second-high probability is
O(epsilon^4). These give (8); the squared mean is only O(epsilon^-4).
Mixedness does not change these leading linear-moment coefficients or the
order of the mean-square subtraction.

This is an initial actual-birth statement. No new later-time theorem or
uniform extension to input supports growing with epsilon is asserted here.

## 5. A density-independent phase witness

All following isometries have domain V. Embed their finite leading word
ranges in the large-S physical box and define

    L_epsilon=V_6 L_i|V,      M_epsilon=V_6 M_i|V,
    A_epsilon=i(M_epsilon L_epsilon* - L_epsilon M_epsilon*),
    Q_epsilon=M_epsilon L_epsilon* + L_epsilon M_epsilon*. (9)

They obey `||A_epsilon||=||Q_epsilon||=1` and
`A_epsilon^2=L_epsilon L_epsilon*+M_epsilon M_epsilon*`.
They are mathematical witnesses inside the selected flag, not extra physical
measurements added to the formation target. They depend on V, the mark and
epsilon, but not on rho_epsilon or its eigenvectors.

Fix the apparatus parent's positive selected amplitude alpha, independent
of epsilon and small enough for the marked CP operation to be a valid
instrument outcome. The target is

    omega_i=alpha^2 k_i rho_epsilon k_i*=p_i theta_i,
    p_i=alpha^2 b_i epsilon^2+O(epsilon^4).                (10)

Equations (3),(6), conjugated by V_6, imply its exact low/first-high block is

    P_1^H omega_i P_0^H
       =alpha^2 epsilon^3 sqrt(b_i r_i)
           M_epsilon rho_epsilon L_epsilon* + O_1(epsilon^5). (11)

The subscript 1 means trace norm. The remainder follows from bounded
operator errors and `||rho_epsilon||_1=1`. Two isometries preserve singular
values, so `||M_epsilon rho_epsilon L_epsilon*||_1=Tr rho_epsilon=1`.
Mixing cannot cancel this block: it distributes its positive singular
weights among the same paired input labels. Thus

    ||P_1^H omega_i P_0^H||_1
        =alpha^2 sqrt(b_i r_i) epsilon^3+O(epsilon^5),
    Tr(omega_i Q_epsilon)
        =2 alpha^2 sqrt(b_i r_i) epsilon^3+O(epsilon^5).   (12)

Using the cluster center and width bounds in the commutator gives

    d_i=|Tr(omega_i i[H,A_epsilon])|
       =2 alpha^2 delta sqrt(b_i r_i) epsilon^-1+O(epsilon),
    v_i=Tr(omega_i A_epsilon^2)
       =alpha^2 b_i epsilon^2+O(epsilon^4).               (13)

For detail, the scalar grade-one center times (11) supplies the first
term of d_i. Multiplying its O_1(epsilon^5) error by O(epsilon^-4) costs
O(epsilon). The cluster-width commutators have norm O(epsilon^-2) and
pair only low/first-high blocks, whose trace norm is O(epsilon^3); they
also cost O(epsilon). Other grades do not couple through A_epsilon.
This proves (13) without purity, a density spectral gap, or a continuity
claim for Fisher information at diverging Hamiltonian norm.

## 6. Robust mixed-state Fisher bound

Use energetic SLD Fisher information F_H. The reused finite-dimensional
variational inequality, applicable also to mixed states, is

    F_H(theta)>=|Tr(theta i[H,A])|^2/Tr(theta A^2).

It follows by restricting the SLD variational expression to real scalar
multiples of A; it is not a variance lower bound. On the exact selected
target, (13) and homogeneity imply

    p_i F_H(theta_i)>=d_i^2/v_i
          =4 alpha^2 delta^2 r_i epsilon^-4[1+O(epsilon^2)]. (14)

The general upper inequality `F_H(theta)<=4 Var_theta(H)` and (8) give
the matching upper coefficient. Consequently

    epsilon^4 p_i F_H(theta_i) -> 4 alpha^2 delta^2 r_i,
    epsilon^6 F_H(theta_i) -> 4 delta^2 r_i/b_i,           (15)

uniformly over densities on V. Equality of the leading Fisher and
four-variance coefficients is proved by the witness plus the upper bound;
it is not assumed for mixed states.

For an implementation retain exactly the apparatus parent's hypotheses:
a finite-dimensional apparatus initially independent of rho_in; every
nonstationary reference counted in it; additive energy conservation or
the associated covariant channel; stationary zero-energy flags; and
subnormalized selected-state error
`||sigma_i-omega_i||_1<=eta_epsilon`. Let
`h_epsilon=||H-c_epsilon I||=O(epsilon^-4)` on the finite relevant system.
The witness on the entire flagged output then proves the finite inequality

    F_HR(sigma_R) >=
       [d_i-2 h_epsilon eta_epsilon]_+^2/(v_i+eta_epsilon)
       - F_H(rho_in).                                   (16)

The input contribution is uniformly O(1), since
`F_H(rho_in)<=4 Tr(H^2 rho_in)` and (1) bounds `H U_4|V`.
It is not set equal to four times input variance. If
`eta_epsilon=o(epsilon^3)`, (13),(16) yield

    liminf epsilon^4 F_HR(sigma_R)
       >=4 alpha^2 delta^2 r_i.                          (17)

The constants are 16, 8, 24 times alpha squared delta squared for plus,
minus and coherent, respectively. This holds for arbitrary varying
rho_epsilon in the fixed span, and for mixed apparatus states. It is an
initial resource requirement, not a claim about consumption, return,
correlations at the end, or the whole instrument on arbitrary inputs.

## 7. Frequency range and the error-scale limitation

The canonical input is supported exactly in the N=4 Hermitian low cluster,
whose spectral width is `B_in=O(epsilon^-2)`. Its O(1) Fisher/energy-vector
bound must not be mistaken for an O(1) exact spectral bandwidth. Let

    G_epsilon=min spec(H|P_1^H)-max spec(H|P_0^H)
             =delta epsilon^-4+O(epsilon^-2).

For the finite apparatus define its initial coherence bandwidth B_R as in
the parent: the largest energy difference carrying a nonzero density block.
If `B_R+B_in<G_epsilon`, finite-dimensional covariance forces
`P_1^H sigma_i P_0^H=0`. The Q_epsilon witness therefore gives

    eta_epsilon >= |Tr((omega_i-sigma_i)Q_epsilon)|
       =2 alpha^2 sqrt(b_i r_i) epsilon^3+O(epsilon^5).    (18)

For `eta_epsilon=o(epsilon^3)` this is impossible eventually. Hence

    B_R>=G_epsilon-B_in eventually,
    liminf epsilon^4 B_R >= delta,
    liminf epsilon^4 diam(spec H_R) >= delta.             (19)

The finite frequency lemma concerns actual coherence frequencies, not
classical energy populations. A large spectral diameter is necessary but
does not supply missing resonances or their amplitudes by itself.

The error restriction remains consequential for mixed inputs. Pinching
omega_i into its exact three Hermitian clusters preserves both energy
moments, but its distance from omega_i is

    2 alpha^2 sqrt(b_i r_i) epsilon^3+O(epsilon^4).         (20)

The leading contribution is twice the trace norm of (11); all blocks
involving grade two are O_1(epsilon^4) or smaller. The pinched selected
branch has only O(1) weighted Fisher information: the low energy-vector
term contributes O(epsilon^2); the first-high probability is O(epsilon^4)
and its internal squared spectral width O(epsilon^-4); the second-high
contribution is O(epsilon^2). A stationary failure flag completes the
state without adding Fisher information. Thus the unchanged large variance
of this mixed comparison does not enforce the divergent Fisher resource.
An unspecified O(epsilon^3) error cannot support (17) by this argument.
This is a limitation of the approximation premise, not a conserving
implementation of the pinched target or an optimal error-threshold theorem.

## 8. Optional one-input comparison with bounded apparatus mean

The parent's deliberately weak state-preparation relaxation extends to any
one of these mixed inputs. Let P_01=P_0^H+P_1^H and normalize
`theta_01=P_01 theta_i P_01/Tr(P_01 theta_i)`. The omitted probability is
O(epsilon^4), so a purification projection and trace-norm contraction give
`||theta_01-theta_i||_1<=2 sqrt(Tr(P_2^H theta_i))=O(epsilon^2)`.
Retaining p_i gives selected error O(epsilon^4).

Use the parent's invariant subspace consisting of the N=4 low cluster and
the N=6 low/first-high clusters, a matching finite replica with a zero-energy
flag, and the conserving swap. Preload

    sigma_R=p_i theta_01 tensor |1><1|
               +(1-p_i)|ground><ground| tensor |0><0|.

The same witness and upper moment bound prove
`epsilon^4 p_i F_H(theta_01)->4 alpha^2 delta^2 r_i`;
one must not replace mixed-state F_H(theta_01) exactly by four variance.
Flag additivity therefore gives the matching leading apparatus Fisher
coefficient. The spectral diameter is
`delta epsilon^-4+O(epsilon^-2)`. The parent lower-edge argument is unchanged:
D is nonnegative, the other low terms are bounded, and a zero-field test
vector gives a bounded upper bound on the minimum. Above its true ground,

    Tr(H_R sigma_R)=alpha^2 delta r_i+O(epsilon^2).         (21)

The low branch has bounded conditional energy, while the success-weighted
high population is `alpha^2 r_i epsilon^4+O(epsilon^6)`; these facts give
(21). This is a supplied preloaded state, depending on the selected input
density. The same apparatus state generally does not implement j_i on other
densities in V. No uniform-channel sufficiency, optimal mean cost, apparatus
selection or continuous-process result follows. The construction is a
mathematical comparison explaining why (17),(19) do not imply divergent mean
apparatus energy.

## 9. Separate finite controls and their limits

`independent_preparation_checks.py` uses explicit (q,E) physical words,
checks Gauss after every action, and imports no prior builder. It tests a
fixed span of five words: zero field and plus/minus unit circulations on
two different squares. For the rotor and S=2,3,7,19, it directly computes
`j F^2/2-F j F`, compares with `-F_0 j F`, checks complete B/R Gram matrices
against (4), and checks the dark vacancy geometry. The largest Gram error
is about 1.3e-15; the recorded cancellation residuals vanish at the stated
floating threshold. Removing the one-half produces norm errors at least
2.35, so the test rejects that consequential alternative. A separate
circulation n=S example checks the leading blocked plus mark.

The mixed-state control uses those independently constructed rotor B/R
columns in an explicitly labeled two-cluster model. It is not the full
microscopic cube or its exact canonical rotation. It covers maximally
mixed, coherent full-rank, rank-two and single-word densities. The SLD
spectral formula agrees with the full-isometry witness and tends to the
predicted probability-weighted coefficient. A witness restricted to the
old zero-field label fails completely on an orthogonal input, while (9)
still succeeds. Cluster pinching preserves variance and removes the toy's
Fisher information, explicitly rejecting a variance-only mixed-state
inference. Added stationary noise obeys the trace-error bound (16).

For alpha=.1, delta=1.3 and epsilon=.03, the scaled selected toy Fisher
values are about .269914, .135078 and .405053, towards .2704, .1352 and
.4056. The same values occur for all tested densities, as required by the
isometry algebra. These are finite floating corroborations; the uniform
claim for all densities and the joint spin limit are carried by the proof.
No unchanged expensive cube calculations were repeated. The complete
result and stdout log are preserved, with source hashes.

## 10. Sources, edge cases and disposition

Exact source identities used:

- General microscopic birth operator/moment parent:
  `docs/GENERAL_MICROSCOPIC_BIRTH_ENERGY_AND_CUBE_POWER_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  SHA256 `9e13c659e9a418e9e77e619a3cbd82d371f8219003a92e49fb2cc9ac5f87d6c7`.
- Actual fast-time cube parent, used for exact cluster structure and known
  pure-input context:
  SHA256 `af0b8e6494ea54cdb450e430a45e9d89d9e1e931e21b9a74ab2b4ea260a3a718`.
- Bounded compensation target:
  SHA256 `f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9`.
- Local compensation/common field parent:
  SHA256 `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b`.
- Reviewed apparatus note at revision
  `e846ee9d4133f65d3778fa4dc36524a9ada6db6b`:
  `docs/ACTUAL_CUBE_BIRTH_APPARATUS_COHERENCE_AND_ENERGY_RANGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  SHA256 `150bd5ba19195a55402d8f74112417f37e168bf50f50dc94d7dcab7d1d3a96a7`.

The first and apparatus notes were read completely for this task; unchanged
transitive expansions and instruction sources already reviewed in this
campaign were reused, not recertified. The new candidate was not read.
Absolute source paths and the observed repository revisions are in the seal.

The claim allows arbitrary mixtures/coherences and varying rank within the
fixed finite span. It does not allow a growing span or flux moving to the
spin boundary, a vanishing selected amplitude without redoing the weighting,
an error merely tending to zero without its required rate, initial
system-apparatus correlations, uncounted phase references, or replacing
additive covariance by an unanalysed interacting-energy conservation law.
Bounds on variance are upper bounds on mixed-state Fisher unless a separate
witness is supplied. Exact low-band preparation remains a supplied premise.

Disposition: supported conditional uniform initial-birth and finite-apparatus
statements with the operator witness above. No new axiom, retained status,
physical reservoir selection, full-instrument realization or continuing
process result is claimed. The one-input relaxation remains deliberately
weaker than implementing the original operation on every input.
