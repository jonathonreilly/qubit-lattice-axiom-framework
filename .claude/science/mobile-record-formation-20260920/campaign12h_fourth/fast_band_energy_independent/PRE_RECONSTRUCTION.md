# Microscopic cube energy on the postbirth scale t=epsilon^2 tau

Independent conditional PRE, 2026-09-24. This argument and its controls were
completed before exposure to any new fast-band author packet or external
fast-band calculation. The microscopic Hamiltonian, compensation, original
formation marks and canonical initial dressing are supplied premises. The
initial dressed-jump coefficient is an explicitly **provisional prior
dependency**, identified below; its reuse is not counted as a new independent
reconstruction of that earlier result. No audit, publication, axiom or physical
selection decision is made.

## 1. Result and meaning of persistence

Let phi_(j,epsilon,S) be the normalized actual microscopic output of a first
mark j applied to the canonical Hamiltonian low-band dressing of the zero-field,
all-A-plus/B-empty cube word. Evolve this state afterwards with the full
microscopic GKLS generator, retaining every allowed subsequent formation.
Write E_(j,epsilon,S)(t) for its full microscopic Hamiltonian expectation.
For fixed positive delta,K,kappa, impose epsilon^2 S(S+1)=delta/K.

There is a bounded operator on the physical rotor sector N=6,W=1,

    D_1 = Pi_1(FF^dagger-F^dagger F)Pi_1,
    Gamma_1 = 2 P_adj,
    V(tau)=exp[(-i delta D_1-kappa Gamma_1/2)tau],        (1)

where P_adj projects onto words whose unique vacant A and unique vacant B
are adjacent. The postbirth state has a leading normalized high-band vector
r_j specified in section 3. The full-generator fast-scale limit is

    sup_(0<=tau<=T) |epsilon^2 E_(j,epsilon,S)(epsilon^2 tau)
                          -delta ||V(tau)r_j||^2| -> 0   (2)

for every fixed finite T. This is a full microscopic energy statement,
not an inference from qualitative density convergence.

For a plus resolved mark, minus resolved mark, or coherent edge mark,
respectively, c_j=||r_j||^2 is 2,1,3/2. The explicit zero-field cube result is

    delta ||V(tau)r_j||^2
       =delta c_j[1-8 kappa delta^2 tau^3+O(tau^4)].       (3)

The leading component is initially dark to the bare formation loss, but the
high-band Hamiltonian moves it into states with a legal further formation.
It therefore is not conserved or protected as a fixed amount of energy.
Its first nonzero decrease in this limit is cubic in tau, not a constant-rate
exponential starting at tau=0.

Two qualifications matter. For every fixed finite tau,

    delta c_j exp(-2kappa tau) <= delta ||V(tau)r_j||^2
                                      <= delta c_j.     (4)

Thus the order-epsilon^-2 energy is still present at any fixed finite fast
time; it is not entirely removed instantaneously. The limit tau->infinity,
including possible invariant dark subspaces, is not resolved here. Nor does
(2) cover a fixed positive physical time t, for which tau=t/epsilon^2 diverges.
This packet proves neither finite-time cube accumulation nor complete later
energy disposal.

## 2. Model and the exact full-generator reduction

Use A={0,3,5,6}, B={1,2,4,7}. For the calculations here every edge is oriented
A to B, in the order

    (01,02,04,31,32,37,51,54,57,62,64,67).

The zero initial field is independent of this orientation convention. Charges
are q in {0,+1,-1}, div E=q-1_A, W counts empty A vertices, and F is the
unsigned sum of legal outward A-to-empty-B transport. The supplied law is

    h_epsilon,S=W-epsilon(F_S+F_S^dagger)+epsilon^2 C_S,
    H_epsilon,S=delta epsilon^-4 h_epsilon,S,
    L_j=sqrt(kappa)/epsilon j_S.                        (5)

The local compensation of the bound source vanishes identically on every
W>=1 cube sector: all A centers are within graph distance two, and its gate
or its own occupied-center factor then vanishes. On W=0,

    C_0=F_S^dagger F_S+Delta_S,
    Delta_S=D_active/[S(S+1)].                         (6)

After a first birth N=6. Only W=0,1,2 occur. A further birth reaches N=8,
where every site is occupied. At lambda=0 that terminal sector has exactly
H=0 and every j=0. No further birth is possible. In N=6, the loss

    Gamma_S=sum_j j_S^dagger j_S

is W diagonal and supported only on W=1. On a word with an empty A a and
empty B b it is zero if they are not adjacent. If they are adjacent on edge e,
the two original signs give

    Gamma_S=2[1-E_e^2/C],      C=S(S+1).                (7)

The coherent-edge instrument has the same loss: its opposite-sign output
charge sectors are orthogonal. The microscopic channel is not replaced by
a different incoherent instrument. Only its loss agrees in this calculation.

Define the exact unnormalized no-further-birth vector

    chi(t)=exp[(-iH-kappa Gamma_S/(2epsilon^2))t] phi_j.

Number conservation of H, the N=6->8 jump rule, and H|_(N=8)=0 imply the
exact identity for the **unconditioned** full GKLS output,

    E_(j,epsilon,S)(t)=<chi(t),H chi(t)>.               (8)

This identity does not discard the next-birth trajectories: their system
energy is exactly zero in this law. The associated exact derivative is

    dE/dt= -kappa/(2epsilon^2)<chi,{Gamma_S,H}chi>.      (9)

The anticommutator need not be positive. No monotonicity of the exact finite-
epsilon energy or convergence of its instantaneous derivative is inferred
from (9). Monotonicity below is a property of the leading fast-scale limit.

## 3. Initial coefficient: explicit provisional dependency

The permitted prior packet is
`general_microscopic_birth_energy_author/GENERAL_MICROSCOPIC_BIRTH_ENERGY_AND_CUBE_POWER.md`,
SHA256 `e1e4274fbc1f45ca95bd8485f5919e2964c43becdce82a312f573a2898596322`,
bound by author seal
`0f1219204fbe9b74209d7a0832e311d742a69d6fec0bf481eb28817ba98ecfd9`.
Its separate independent comparison was pending at dispatch. Only the initial
dressed-jump amplitude coefficient is used here as a provisional dependency;
none of its power, high-flux or finite-graph comparison results substitutes
for the new postbirth argument.

Let Omega be the zero-field all-A-plus word, b_j=||B_j Omega||^2 and

    B_j=j F P,
    v_j=B_j Omega/sqrt(b_j),
    R_j=j F^2 P/2-F B_j=-F_a B_j,
    r_j=R_j Omega/sqrt(b_j),                            (10)

for a mark centered at a. The prior coefficient says that after the canonical
Hamiltonian cluster rotation the normalized actual first output has leading
components v_j in W=0 and epsilon r_j in W=1.

The parity Xi=(-1)^W of the supplied law and j fixes the remainder orders.
The normalized analytic output, using its denominator epsilon times a positive
even analytic factor, transforms covariantly under epsilon->-epsilon and Xi.
Its W=0 and W=2 components are even and its W=1 component is odd. Thus, in
the all-cluster canonical Hamiltonian frame,

    chi_0(0)=v_j+O(epsilon^2),
    chi_1(0)=epsilon r_j+O(epsilon^3),
    chi_2(0)=O(epsilon^2).                             (11)

The all-cluster and P-versus-Q canonical rotations have the same P isometry;
their higher-sector difference does not change the order-epsilon W=1
coefficient. Uniform analytic remainders follow from the bounded operator
and separated integer-cluster hypotheses. Here b_j=2 for either resolved
sign and b_j=4 for the coherent mark, so normalization is bounded away from
a blocked leading mark.

For this zero-field input all three local moves in (10) change a link between
0 and +/-1, with normalized spin amplitude exactly one at every S>=1.
The vectors v_j,r_j are consequently fixed finite-support rotor words,
independent of S. Every nonzero field in v_j ends at an occupied B vertex,
so Delta_S v_j=0 exactly. No field-only projection has been made.

The new primitive control checks the displayed local path identities and
norms directly on all 36 cube marks. This is a geometry check on the supplied
initial coefficient. Reusing its general canonical-amplitude conclusion is
not advertised as a fresh independent verification of that prior theorem.

## 4. Hamiltonian reduction on the fast time scale

The bound cluster-rotation theorem applies to
h=W+epsilon T+epsilon^2 C with bounded T,C and W-preserving C, uniformly in S.
In the all-cluster canonical Hamiltonian frame,

    hbar = W+epsilon^2 sum_r Pi_r D_(r,S) Pi_r
                         +O(epsilon^4),
    D_(r,S)=C_r+sum_(s!=r) T_rs T_sr/(r-s).            (12)

For example, if G is the first anti-Hermitian rotation coefficient,
G_rs=-T_rs/(r-s), then [W,G]=-T and the diagonal second-order term is
C+[T,G]/2. This gives (12) with its signed denominators. On the postbirth
cube sectors,

    D_(0,S)=Delta_S,
    D_(1,S)=Pi_1(F_S F_S^dagger-F_S^dagger F_S)Pi_1.  (13)

The plus contribution goes through W=0 and the minus contribution through
W=2. Omitting either intermediate sector would change the high-band motion.
The compensation is zero on W=1, so no C_1 term is missing from (13).

Set t=epsilon^2 tau. The exact no-event generator in this frame is

    Kbar_epsilon = -i delta epsilon^-2 hbar
                                  -kappa Gammabar/2,
    Gammabar=U^dagger Gamma_S U.                      (14)

Since Gamma_S commutes with W, its transformed diagonal blocks equal
Gamma_(r,S)+O(epsilon^2), while its off-diagonal blocks are O(epsilon).
The off-diagonal dissipative terms cannot be ignored on the basis of a
plain O(epsilon) Duhamel estimate: the wanted high amplitude itself is
order epsilon. The rapid integer-band separation must be used.

Here is a uniform way to do so. Multiply (14) by i epsilon^2/delta and put

    Z_epsilon=hbar-i kappa epsilon^2 Gammabar/(2delta).

Its W-diagonal part has the separated clusters
r I+epsilon^2[D_(r,S)-i kappa Gamma_(r,S)/(2delta)]+O(epsilon^4).
Its off-diagonal part is O(epsilon^3). Contour resolvent comparison to the
diagonal part gives Riesz projectors differing from Pi_r by O(epsilon^3).
The invertible map Y_epsilon=sum_r Q_r(Z_epsilon)Pi_r is therefore
I+O(epsilon^3) and block diagonalizes Z_epsilon exactly. This similarity is
not claimed unitary or positive. Its norm and inverse are uniformly bounded.
The construction is a bounded analytic spectral argument; no inverse of a
dissipative gap or assumption of fast thermalization is used.

After this similarity, the exact no-event generator has blocks

    -i delta r/epsilon^2
          -i delta D_(r,S)-kappa Gamma_(r,S)/2
          +O(epsilon^2).                             (15)

The bounded remainders and the real-part dissipativity of the leading blocks
control their semigroups uniformly on compact tau intervals. The near-identity
similarity changes initial or final vectors by O(epsilon^3). Combining (11),
(13)-(15), Gamma_0=Gamma_2=0 and Delta_S v_j=0 yields

    chi_0(epsilon^2 tau)=v_j+O_T(epsilon^2),
    chi_1(epsilon^2 tau)=epsilon exp(-i delta tau/epsilon^2)
          exp[(-i delta D_(1,S)-kappa Gamma_(1,S)/2)tau] r_j
                                            +O_T(epsilon^3),
    chi_2(epsilon^2 tau)=O_T(epsilon^2),               (16)

in the canonical Hamiltonian frame. These estimates are uniform in S.
They retain the rapid phase and the actual small high-band population.

The exact Hamiltonian is block diagonal in this frame. Its leading W=1
energy is delta epsilon^-4, its W=2 norm is O(epsilon^-4), and its low block
is delta epsilon^-2 Delta_S+O(1). Because Delta_S v_j=0 and Delta_S is
bounded, inserting (16) into (8) gives

    epsilon^2 E_(j,epsilon,S)(epsilon^2 tau)
       =delta ||exp[(-i delta D_(1,S)
                           -kappa Gamma_(1,S)/2)tau]r_j||^2
          +O_T(epsilon^2).                            (17)

This is the required estimate on the unbounded-in-resource observable; an
O(epsilon) density estimate alone would not have implied it.

The finite-spin shifts and their adjoints converge strongly, with uniform
bounds, to unit rotor shifts on the common physical space. Thus D_(1,S)
and Gamma_(1,S) converge strongly to (1). Both are bounded uniformly at this
fixed graph. Their exponential series converge strongly and uniformly on
compact tau intervals when applied to the fixed r_j. Applying this to (17)
proves (2) in the joint scaling. No large-field initial state, increasing
volume, or rotor truncation is involved.

## 5. The decisive cube calculation

Consider first the edge (0,1). The plus resolved B output has two orthogonal
old destinations, 2 or 4, so b_+=2. Applying -F_0 makes those two paths land
on the same full matter/field word with amplitude -2. It has holes at 0 and
7. Thus ||R_+ Omega||^2=4 and c_+=2. For the minus resolved mark the two
final negative-charge positions distinguish the R words, each with amplitude
-1, giving ||R_- Omega||^2=2 and c_-=1. The coherent mark retains all three
words with amplitudes -2,-1,-1 and b_coh=4, hence c_coh=3/2. They are not
replaced by an incoherent mixture in constructing r_coh.

The two holes in every R word are opposite cube vertices. Therefore

    Gamma_1 r_j=0.                                    (18)

The independently built exact path sum applies both terms of D_1 in (13).
It gives the following values; all other cube edges agree by the same
primitive enumeration.

| first mark | b_j | ||R_j Omega||^2 | ||D_1 R_j Omega||^2 | <D_1 r_j,Gamma_1 D_1 r_j> |
|---|---:|---:|---:|---:|
| resolved plus | 2 | 4 | 48 | 48 |
| resolved minus | 2 | 2 | 24 | 24 |
| coherent | 4 | 6 | 72 | 36 |

Every word in D_1 R_j Omega has adjacent holes. Thus Gamma_1 D_1 R_j Omega
=2D_1 R_j Omega. The original opposite-hole vector is not invariant under
the Hamiltonian in the fast band. The full saved word certificates include
R, D_1 R and D_1^2 R, with both charges and electric fields.

For f_j(tau)=||V(tau)r_j||^2, the full loss satisfies exactly

    f_j'(tau)=-kappa <V(tau)r_j,Gamma_1 V(tau)r_j>.      (19)

Since Gamma_1 r_j=0,

    f_j(tau)=c_j-(kappa delta^2/3)
          <D_1 r_j,Gamma_1 D_1 r_j> tau^3+O(tau^4).

The table's last column is 24c_j, proving (3). Boundedness of D_1 and Gamma_1
makes this a genuine convergent small-tau expansion with a controlled
remainder, not a formal expansion of the large microscopic generator. The
leading loss is strictly positive for sufficiently small nonzero tau.
Equation (19), together with 0<=Gamma_1<=2I, gives (4).

The high component therefore can lose a nonzero fraction of its leading
coefficient, independent of epsilon, on a fixed tau interval. The total probability of a further
birth on such an interval remains O_T(epsilon^2): from (16), the original
rotated j applied to the no-event state has norm O(epsilon), and its tau-scale
intensity is kappa times that squared norm. A vanishing-probability component
can carry the order-epsilon^-2 mean energy. This explains why a density-only
description does not settle this energy question. No complete second-birth
distribution is derived here.

## 6. Mark conditioning and limits

The initial phi_j used in (2) is the actual microscopic instrument output
j U_epsilon Omega/||j U_epsilon Omega||, not B_j Omega declared exact at
finite epsilon. An event at one prescribed instant has probability zero in
continuous time, so this is the usual density-conditioned post-jump state.
It is accessible as the limit of a first mark observed in a positive-length
window immediately after preparation. The initial marked intensities tend
to kappa b_j>0, so every sufficiently short positive window has positive
probability at each fixed microscopic model.

This accessibility does not make the finite-window output exactly equal to
phi_j. One conservative sufficient joint-window prescription is the following.
The full no-event generator has norm O(epsilon^-4), while ||j U Omega|| is
bounded below by a constant times epsilon. Over a window w its normalized
post-jump vector therefore differs by O(w epsilon^-5), provided that error
is small. Since ||epsilon^2 H||=O(epsilon^-2), choosing w=o(epsilon^7), for
example w=epsilon^8, controls the rescaled energy error by o(1), even after
the subsequent CPTP evolution. The probability of this selected window then
vanishes with w; no uniform positive-probability limiting conditioning is
asserted.

The explicit cubic coefficients refer to this zero-field immediate first-
mark preparation. A first event after a finite waiting time samples a changed
conditional field/record state; the present coefficients cannot simply be
assigned to every such output. Similarly the compact-tau limit cannot be
interchanged with tau=t/epsilon^2 at fixed physical t. Long fast-time survival,
arbitrary conditioning histories, six-cycle second-event laws, and finite-
physical-time cube energy remain separate questions.

## 7. Qualified extension to the supplied electric family

The main exact identity (8) and the completed finite-spin control use lambda=0.
For the already supplied family with fixed 0<=lambda<=1, a conditional
extension of the leading limit (2) is available **if each law uses its own
canonical Hamiltonian low-band initial dressing and the provisional initial
coefficient (10)**. It is not a statement about an arbitrarily changed
preparation or an independently derived compensation.

On fixed finite-support words, the extra dimensionless compensation
lambda(E2-D_ext)/C tends strongly to zero; it is uniformly bounded at this
fixed graph. Thus the added W=1 contribution to D_(1,S) tends strongly to
zero. On v_j, the low coefficient is now D_lambda/C=2lambda/C, which is
O(epsilon^2) in the joint scaling, so the low-state estimate in (16) still
holds. The uniform analytic and bounded-semigroup argument is unchanged;
the resulting leading rotor D_1 and Gamma_1 are still (1).

The terminal Hamiltonian is now K lambda E2 rather than zero, so (8) is no
longer exact. Its finite-spin norm is at most 12K C=O(epsilon^-2). The
future-birth probability on the compact fast interval is O(epsilon^2), hence
its terminal-sector contribution to epsilon^2 E is O(epsilon^2). It cannot
change (2). This bounds the term rather than silently discarding it.

The extension uses the named supplied family, fixed graph, bounded lambda,
joint scaling and canonical preparations. The numerical control here does
not test lambda>0; its supporting argument is the displayed strong-limit and
terminal-norm estimate. It supplies no physical selection of lambda or
autonomous energy source.

## 8. Independent evidence and remaining obligations

`cube_control.py` imports no campaign builder. It implements the local charge
hops, exact link changes, births, and integer rotor path sums. All 36 first
marks are checked. Complete selected certificates contain q and E for B, R,
D_1 R, and D_1^2 R. The first coefficient's geometry is verified, while its
general dressed-band status remains the explicitly provisional dependency.

The second control enumerates all 3^12 spin-one electric configurations,
sets q=div E+1_A, and retains every physical word in N=4,6,8. The dimensions
are 3197,5604,672. No additional field cutoff or invariant-sector guess is
used. The compensated matrices, exact original jumps, terminal zero-H
identity and W=1 loss support are built from these primitives. The initial
canonical dressed vector comes from the complete N=4 Hamiltonian's 69-state
low spectral band and its positive-overlap polar isometry.

For epsilon=0.025,0.0175,0.0125 the full N=6 no-event vector is propagated
through tau=0,0.02,0.04,0.06 for all three first-mark choices. Equation (8)
makes its energy the exact full-GKLS energy. These spin-one checks test the
finite-S perturbative reduction (17); they are explicitly not the joint
large-spin sequence. The spin-one normalized cubic forms are 36,18,27,
which differ from the rotor values 48,24,36 because the actual next-birth
spin weights in (7) remain. This is an expected finite-resource effect.

The largest energy error is 0.0112851 at the coarsest epsilon and 0.00282433
at the finest; the errors divided by epsilon^2 stay between 18.056 and
18.084 in these runs. The eigensystem residuals are below 1e-14. Every control
assertion passed. Full results and logs are retained. Two SciPy FutureWarnings
about an integer diagonal being cast to floating point are preserved in
stderr; no assertion, scientific formula, or tolerance was changed in response.

The new future-dynamics result is conditional on the provisional initial
dressed-jump coefficient. Its separate independent disposition remains a
dependency to refresh before any stronger status language. The bounded
question is settled at compact fast times: the energetic coefficient evolves
under (1), initially loses energy cubically, and stays positive for finite tau.
No claim of total late decay, persistent finite-time heating, an exact
second-birth law, thermal behavior, a reservoir or a physical selector is made.
Stop here before new author comparison.
