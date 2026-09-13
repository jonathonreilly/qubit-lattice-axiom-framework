# Fixed output Records under one local content law and three occurrence kernels

Author construction,2026-09-13. Written before its exact finite checks.
This is an axiom-facing compatibility test on physical Z³, with supplied
finite preparation, matrix possibility presentation, readout context and
occurrence kernel. It is not a Born derivation or a microscopic quantum
apparatus. The nonlocal occurrence choice is explicit, and the desired
joint correlations are supplied there rather than inferred from the axioms.
Its output matrices generally include nonprojector Gaussian values; only
their binary statistic matches that comparison. Thus it does not implement
the owner-selected matching-projector event map or full projective-history
sector Law. No axiom or primitive is amended.

## 1. Exact target and governing distinction

The current minimal memo at main cda8b1445e21b3908a0a520710e0dae57b7bc3a3
supplies a nearest-neighbor content distribution conditional on formation.
It does not specify which sites form, their joint occurrence probabilities,
a transition law or a physical clock. The current support/site-separation
note gives only a finite abstract-label witness and explicitly does not
embed it in Z³ or construct a process. Here the target is a complete finite
Record process on actual Z³ with one fixed content law and fixed final
output sites, followed by an absorbing continuation.

The proposed positive statement is: there is one full-support, translation-
and proper-cubic-covariant nearest-neighbor content law and one finite
prepared geometry for which three explicitly different occurrence kernels
produce binary output CHSH values0,2sqrt2 and4(19/20)^6. Every trial forms
both fixed output Records; all stochastic branches are retained. Each
forming site's conditional content law is exactly the same local law,
conditioned on its complete past and on its formation. No unrecorded
quantum state or hidden history variable is used as a framework state.

The model domain is the specified finite preparation and its finite
descendant Record configurations on the whole infinite lattice, including
all their translations and proper cubic rotations. Its continuous matrix
contents are not replaced by a binary possibility space. This conditional
domain does not assert that the preparation is physically generated or
that all arbitrary lattice states are covered by an autonomous dynamics.

## 2. One content law on the full matrix possibility presentation

Use M2(C), with its eight real coordinates, as the supplied matrix-content
presentation. This is the same type used in the repo's explicit Gaussian
matrix-Record constructions, not a claim that the axioms choose a Gaussian.
Define a fixed probability measure Gamma by

    Gamma(dX)=pi^-4 exp(-Tr X†X) d^8X.

The four complex entry integrals each equal pi, so Gamma is normalized.
Its density is everywhere positive; its support is all M2(C). It is
invariant under X↦UXU† for unitary U, because Hilbert–Schmidt norm and the
real Lebesgue measure are preserved. No internal axis is selected by Gamma.

Let eta be the finite list of contents at present nearest-neighbor Records.
There are at most six entries. With lambda=19/20, define

    F_eta=lambda*(1/|eta|)sum_(X in eta)delta_X+(1-lambda)Gamma
           if eta is nonempty,
    F_empty=Gamma.                                       (2.1)

Multiplicities of equal neighbor contents are retained in the empirical
measure. This gives exactly one normalized probability measure for every
neighbor condition. It varies with eta, is unchanged under permutations
of the six directions, and is equivariant under simultaneous unitary
conjugation of the contents. Translation/proper-cubic covariance follows
from using the actual nearest-neighbor list and no coordinate weights.

Every F_eta has full support, so every locked matrix remains supported even
if its neighborhood later changes. This satisfies both formation-time
support and the stronger possible reading of continued support for old
Records. No scalar is assigned to a missing site and no readout map is
applied to absence. The empty-list case defines a distribution for a future
formation event, not a readout of emptiness.

The Gaussian and lambda are named model choices. Their values and the
matrix realization are not newly derived or approved foundation premises.

## 3. Fixed content readout and its exact binary channel

Supply Z=diag(1,-1), P_s=(I+sZ)/2 for s=±1, and the fixed readout function

    r(X)=+1 if Re Tr(ZX)>=0, and-1 otherwise.              (3.1)

It is a function of content alone, identical at every site and stage.
In particular r(P_s)=s. It is an experimental calibration/context choice,
not a derivation of a preferred internal possibility. Alternatively the
primitive readout can be the matrix content itself and(3.1) is a fixed
subsequent statistic of that readout. The same Z is held fixed in all three
comparison models. The content law(2.1) does not use Z.

The real Gaussian coordinate Re Tr(ZX) is nondegenerate, centered and
symmetric. Thus r(X) is fair under Gamma and ties have probability zero.
If exactly one neighboring Record has content X and r(X)=s, a fresh draw
from F has readout t with probability

    B_(t,s)=(1+lambda*t*s)/2,
    B=[[39/40,1/40],[1/40,39/40]].                        (3.2)

This holds for every matrix X, including non-Hermitian Gaussian values
and the fixed tie convention. A two-neighbor list P_+,P_- gives a fair
readout under F. The full draw is still a mixture of matrix atoms and a
continuous Gaussian; (3.2) is only its proven binary marginal.

Three successive one-neighbor draws multiply the conditional readout mean
by lambda³. If two such chains use independent fresh draws conditional on
their starting signs S,T, their final product mean is lambda^6*S*T. Put

    kappa=lambda^6=47045881/64000000.                     (3.3)

The independence here is explicit supplied transition data, not an
independence axiom or a conclusion from spatial distance alone.

## 4. Literal physical placement

Let e1,e2,e3 be the three canonical coordinate vectors, with output centers
y_A=(0,0,0), y_B=(20,0,0). At each wing w prepare source Records

    y_w+3e1 with content P_+,
    y_w-3e1 with content P_-.

The first and second relay candidates are y_w±2e1 and y_w±e1. Neither
relay is initially recorded. The final output is the SAME site y_w for
either arm. The setting site is c_w=y_w+10e2, initially unrecorded, with
prepared neighbors c_w+e3 carrying P_+ and c_w-e3 carrying P_-.

Four further prepared marker Records sit at

    f=(-10,-10,-10):10I,
    f+e1:11I,
    f+2e2:12I,
    f+3e3:13I.                                          (4.1)

They neighbor no site that forms during the experiment. All other sites
of Z³ initially have no Record. Thus there are12 prepared Records: four
arm sources, four setting neighbors and four markers. Every physical site
still has its M2 possibility domain; unlisted sites are not removed from
the lattice or declared readable.

The exact forming-site neighbor lists are:

| stage/site | present nearest-neighbor Records just before formation |
|---|---|
| setting c_w | c_w+e3 and c_w-e3, with P_+ and P_- |
| selected first relay y_w+2s e1 | only y_w+3s e1, with P_s |
| selected second relay y_w+s e1 | only y_w+2s e1, with its already formed content |
| fixed output y_w | only y_w+s e1, with its already formed content |

Both wings can perform a stage together: their centers differ by20 in e1,
so no listed neighbor comes from the other wing. The setting rows are ten
units away in e2, and the marker rows are farther still. The unselected
opposite relay arm remains empty. In particular, the opposite prepared
source at distance3 never contaminates the final output's neighbor list.
These statements concern the six actual physical neighbors, not virtual
edge adjacency or an isolated degree-one graph.

## 5. A normalized kernel on current Record configurations

The initial state R0 is the finite Record configuration in section4.
The following rules specify a Markov kernel on its reachable configurations.
Use fresh independent random variables for content draws at distinct new
sites conditional on each selected occurrence set.

1. From R0, both setting sites form. Each draws from its two-neighbor F
   law, independently. Their readouts define a=(1-r(c_A))/2 and
   b=(1-r(c_B))/2. All four setting pairs have probability1/4.
2. Given the setting Records, sample(S,T) from one supplied normalized
   table Q_ab on{±1}². At wing A only y_A+2S e1 forms; at wing B only
   y_B+2T e1 forms. Their contents are independently drawn from the
   one-neighbor law(2.1), after this occurrence choice.
3. The corresponding second relays y_A+S e1,y_B+T e1 form, with fresh
   independent one-neighbor F draws.
4. Both fixed output sites y_A,y_B form, again with fresh independent
   one-neighbor F draws. The resulting configuration is absorbing.

Every transition adds exactly two Records, leaves all old contents unchanged
and assigns no site a second Record. Final configurations have20 Records.
The selected arms in later stages are recoverable from present relay
locations; the settings are recoverable from their permanent contents.
The stage is recoverable from which designated positive Record occurrences
are already present. No stored hidden quantum state, erased history or
independent clock variable is needed to make this a kernel of the current
Record configuration. The four transition steps are not a physical time or
rate claim. Absorbing continuation defines every later finite prefix.

More formally, each stage uses a finite sum over occurrence sets followed
by a finite product of the Borel measures F_eta. The resulting kernel is
measurable in all current matrix contents; its total mass is one. Standard
finite kernel composition therefore defines the complete continuous-content
history measure. It is not necessary to simulate or enumerate its continuum
of matrix-valued histories. There is no missing global extension: the
process is defined on all Z³, changes only the displayed finite sites and
continues by the identity kernel after stage4.

Conditional on a complete pre-event history and on formation at any
selected physical site, its content distribution is EXACTLY F_eta. The
occurrence choice happens before and independently of that site's fresh
content draw conditional on the current history. Jointly formed sites are
not nearest neighbors. Subsequent posterior conditioning on future Records
is a different statistical operation; it is not identified with a
formation-time content law.

The initial12 Records are supplied preparation data. The process does not
derive their manufacture or claim a positive probability of selecting their
exact matrices from a continuous Gaussian preparation. Full support makes
their contents admissible, but it is not a preparation theorem. The model
is a finite-preparation, finite-prefix construction on the infinite lattice,
not an asserted description of every allowed cosmological initial state.

## 6. Covariance and lack of a privileged physical site

Let G be the group of lattice translations and proper cubic rotations.
For g in G transport the entire preparation, all sites and the transition
kernel by g. The four marker contents are distinct scalar matrices, and
their relative displacement lengths1,2,3 are distinct. They recover the
origin f and oriented coordinate frame uniquely on every translated/rotated
prepared domain. This remains true if an exceptional continuous draw has
one of the marker values: uniqueness does not require all later contents
to differ from them. To see this geometrically, join possible occupied sites
when their displacement is an axis vector of length at most3. Apart from
the marker component, every connected component of the union of all event
and prepared sites is a single straight line: a wing's relay/source line
or a setting's three-site line. Such a component cannot contain the three
independent axis arms of the marker frame. The four-site marker component
has exactly one three-axis corner f, and the three distinct arm lengths
fix its orientation. Thus a second transported preparation cannot fit
inside any descendant configuration. No nonidentity element of G fixes
the marked preparation, and descendants from different frames cannot create
conflicting definitions of the kernel.

It follows that transported definitions agree whenever their prepared
domains coincide: there is only one recovered frame. Equivalently,

    K(gR,gB)=K(R,B)

for Borel sets of successor Record configurations. The local law F is
already covariant without the markers. The supplied preparation selects
the experiment's center, wing direction and operational roles; the law
privileges no absolute lattice site. The readout context Z selects a
prepared experimental basis, not a basis in the content law.

The covariance domain can also be transported by internal unitary
conjugation of all contents and Z. The fixed readout then obeys
r_(UZU†)(UXU†)=r_Z(X), while F transforms equivariantly. No internal axis
is built into the local substrate rule. This is covariance of a family of
prepared/readout contexts; it does not identify distinct contexts as the
same physical state.

## 7. Three explicit occurrence choices and their fixed-site outputs

Let A_out=r(R(y_A)),B_out=r(R(y_B)). These are readouts of the two fixed
new output Records. They are not the selected arm locations S,T.
Given a,b,S,T, equation(3.2) is used THREE times per wing, so

    E[A_out|S,T,a,b]=lambda³ S,
    E[B_out|S,T,a,b]=lambda³ T,
    E[A_out B_out|S,T,a,b]=kappa S T.                     (7.1)

For an unbiased arm table, the output table has unbiased marginals and

    P(A_out=x,B_out=y|a,b)=[1+x y E_ab]/4,
    E_ab=kappa sum_(s,t)st Q_ab(s,t).                    (7.2)

Define the CHSH statistic S_CHSH=|E00+E01+E10-E11|.

**Independent choice.** Q_ab(s,t)=1/4 gives E_ab=0 and S_CHSH=0.

**Specified quantum-comparison choice.** Put

    Q_ab(s,t)=[1-st(-1)^(ab)/(sqrt2*kappa)]/4.             (7.3)

The exact rational inequality2 kappa²>1 makes every entry strictly
positive. Each table is normalized and has both marginals1/2. Equations
(7.1)–(7.2) give

    E_ab=-(-1)^(ab)/sqrt2,    S_CHSH=2sqrt2.              (7.4)

This is the usual singlet four-setting comparison table, for directions
a0=z,a1=x,b0=(z+x)/sqrt2,b1=(z-x)/sqrt2. The table is not predicted here:
(7.3) was chosen to reproduce it after the declared local noise. This
construction does not supply general qubit calibration or all quantum
experiments. It retains every Gaussian/noise branch and every trial.

**Larger-correlation comparison.** Set Q_ab(s,t)=1/2 when
st=(-1)^(ab) and zero otherwise. The arm marginals are still fair, and

    E_ab=kappa(-1)^(ab),
    S_CHSH=4kappa=47045881/16000000>2sqrt2.                (7.5)

This comparison is deliberately different from the quantum table. It is
not a physical prediction. All three constructions use the same F, same
lambda, same full matrix support, same geometry/preparation, same readout,
same setting process and same three local relay draws. Only Q_ab changes.

Every trial forms the same two final output sites, with no rejected
experiment, missing output or outcome-dependent final detector location.
The experiment's output labels come from Record content. Intermediate
occurrence geometry carries the initially chosen arm information and the
local content draws transmit a noisy version of it to the fixed outputs.

## 8. The causal distinction and the remaining physics

The nonlocal operation is explicit: stage2 selects the pair of arm
occurrences from Q_ab after consulting BOTH permanent setting Records.
Spatial nearest-neighbor dependence of F does not constrain that supplied
occurrence kernel. The construction has no derived speed limit, Hamiltonian,
relativistic causal separation, autonomous scheduler or physical time metric.
It should not be described as a local hidden-variable realization of the
quantum table or a microscopic native quantum measurement.

For comparison, a separately supplied factorization

    P(x,y|a,b)=integral rho(dh) P_A(x|a,h)P_B(y|b,h),

with rho independent of a,b, gives the elementary CHSH bound2. If
A_a(h),B_b(h) are the response means in[-1,1], its integrand satisfies

    |A0(B0+B1)+A1(B0-B1)|
      <=|B0+B1|+|B0-B1|
      =2 max(|B0|,|B1|)<=2.

The occurrence kernel used above is not asserted to have this additional
factorization. The distinction is the same locality/setting-independence
distinction explicitly stated in the original CHSH primary paper,
[Clauser, Horne, Shimony and Holt(1969)](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.23.880),
page881. The inequality here is rederived, not imported without hypotheses.
The paper was consulted for its statement of those premises; no historical
priority or new Bell theorem is claimed.

The construction exposes a concrete next requirement for an intended
physical theory: specify and justify the occurrence kernel and how it
respects the intended causal/dynamical structure, as well as its preparation
and readout. The existing local content clause alone is not the missing
microscopic process. These supplied comparison models force no axiom edit;
they preserve an explicit same-axiom route that an axiom-pressure argument
would have to address. They do not establish a TOE or solve the native
matter/Record interface. A physical law might select the quantum table,
but this construction has supplied that selection rather than derived it.

## Verification status

The continuous-kernel, support, geometry, covariance and conditional-law
proof was written before the checker. Its first execution passed63 checks.
For each of four settings and each of three tables, exact Q(sqrt2) channel
powers agree with the complete2916-path sum: four arm pairs and27 independent
copy/fresh-plus/fresh-minus histories per wing. All histories are retained,
including noise branches that reverse the input sign. Geometry is checked
against all six physical neighbors at every stage, with768 transported
neighbor cases under all24 proper rotations and a nontrivial translation.
The complete24-site union of possible event and prepared locations admits
only the specified marker frame, including exceptional matrix-content
values. The written covariance proof above was strengthened to make this
last geometric argument explicit after the first successful check.

Adverse comparisons distinguish omitted noise steps, arm-location readout,
copy-only postselection and an accidental opposite nearest-neighbor source.
They are finite diagnostic comparisons, not yet packaged source-mutant
evidence. The continuous matrix support and Borel kernel are proved in the
text; a finite binary checker does not verify those claims by enumeration.
No Monte Carlo, fitted parameter or outcome postselection is used.
Independent source review and any formal status remain pending.
