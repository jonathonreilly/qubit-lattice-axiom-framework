# Exact finite projector histories in a local-copy Record process

Author construction,2026-09-13. Proof written before its checker.
This is a positive conditional embedding of a supplied finite trace history
into actual Z3 Record configurations. Quantum probabilities, preparation,
projective registration and the nonlocal occurrence kernel are explicit
inputs. No Born derivation, independent physical calibration, native quantum
apparatus, causal Hamiltonian, clock, axiom amendment or primitive is claimed.

The first data Record appears at an outcome-dependent site. A later copy
reaches a fixed output register. This distinction is part of the theorem.
It must not be erased by calling the terminal copy the first measurement.

## 1. Domain and exact theorem

Fix a positive integer N. Supply a positive normalized two-qubit matrix
rho in M4(C), and at each round n=0,...,N-1 and wing w=0,1 supply two
binary rank-one projective programs

    P_(n,w,a)^s,  a=0,1, s=+1,-1,
    (P^s)†=P^s=(P^s)^2, P^+P^-=0, P^++P^-=I2.          (1.1)

The programs need not be the same across rounds or wings, and different
programs may coincide. At each round fresh independent fair setting bits
a,b choose one program at each wing. A supplied conditional trace rule
assigns the two outcome signs s,t the probability

    Q_h,ab(s,t)=Tr[J sigma_h J]/Tr sigma_h,
    J=P_(n,0,a)^s tensor P_(n,1,b)^t,
    sigma_h=M_h rho M_h†,                               (1.2)

where M_h is the chronological product of earlier joint event projectors.
Only supported histories with Tr sigma_h>0 are conditioning domains.
Zero children have zero mass and are never used as later denominators.

For every such finite input there is a Record Markov process, with one
fixed nearest-neighbor content law independent of N,rho and the programs,
having the following properties:

* its physical sites are all of Z3; it changes only a stated finite subset;
* every initial and later Record remains supported under its current local
  content distribution, every old content is permanent, and every site is
  written at most once;
* every new data Record has exactly the selected matching projector content;
* the first data occurrences carry the supplied trace history(1.2), every
  subsequent relay is a trace-certain repeat of that same program, and the
  final output sites are fixed before the settings and outcomes;
* the preparation/calculator, settings, stage, programs and past data are
  reconstructible from current Records, with no additional evolving state;
* there are24N+16 prepared Records and at most56N+16 Records at completion,
  and at most16N discrete transitions before absorbing continuation;
* the whole supplied-domain law is translation/proper-cubic covariant.

These are finite-horizon quantifiers: every N admits the stated finite
preparation and the same local content rule. An infinite prepared universe,
finite-density continuing apparatus, arbitrary POVMs, arbitrary entangled
events, dynamic material carrier and metric causality are not conclusions.

The target is narrower than the selected sector Law's complete physical
replacement criterion. It realizes its trace/projector history algebra using
outcome-dependent first-event placement and additional repeated data Records.
It does not derive the desired trace probabilities as a content distribution
at one common, outcome-independent FIRST event site. Physical calibration
of these mathematical projector Records as measurements remains supplied.

## 2. One intrinsic content law and supported permanent preparations

Use the full M2(C) matrix possibility presentation. For the list eta of
present nearest-neighbor contents, with multiplicity retained, define

    F_empty=delta_0,
    F_eta=(1/|eta|)sum_(X in eta)delta_X  if eta is nonempty. (2.1)

There is one normalized probability measure for every neighbor condition.
Its support is a subset of the full possibility domain; the domain is not
replaced by a binary menu. The rule varies with neighbor content, is
unchanged by permutation of spatial directions, and is equivariant under
algebra automorphisms, because these preserve zero and equality. No norm,
Gaussian, internal axis, trace weight or projective criterion enters(2.1).
The algebra's zero is intrinsically distinguished by its additive identity,
not by an extra preferred basis or physical outcome.

Every prepared Record below has an adjacent permanent buddy with the same
content. Therefore its content remains in the empirical support regardless
of later additional neighbors. Every new data Record has one predecessor
with the same projector content that remains permanent; therefore it too
stays supported forever. A newly formed setting has one of its two initial
seed contents, so one unchanged seed continues to support it.

No empty site is read or assigned a readout value. F_empty is a future
formation distribution, not a reading of absence. The initial nonzero
prepared Records are supplied boundary data. Their manufacture from a
different initial configuration is not proved by their support condition.
The rule is not offered as the uniquely selected physical content law.

## 3. Literal banks, setting registers and fixed outputs

Let e1,e2,e3 be the coordinate axes. For round n and wing w use the center

    c_(n,w)=(40(2n+w),0,0).                              (3.1)

This center is the fixed final output register, initially without a Record.
Enumerate the four program/outcome options by

    j(a,s)=2a+(1-s)/2+1,   j in{1,2,3,4}.                (3.2)

Prepare a source and matching buddy for each j:

    c+(3j,3,0):P_(n,w,a)^s,
    c+(3j,3,1):P_(n,w,a)^s.                              (3.3)

The selected first relay is c+(3j,2,0). Its continuation path is

    c+(3j,2,0), c+(3j,1,0), c+(3j,0,0),
    c+(3j-1,0,0),...,c+(1,0,0),c.                       (3.4)

It contains exactly L_j=3j+3 new data sites, between6 and15. All other
candidate data sites remain empty during that wing/round. The source
locations are three units apart, and all unselected sources are three
units above the spine. Their buddies are one unit farther in e3. At every
new site in(3.4), the only already present nearest-neighbor Record is its
immediate predecessor: the selected source for the first relay, otherwise
the previous path site. A right-angle turn creates a distance-two pair,
not an extra nearest neighbor. No other round/wing lies within one lattice
edge, since centers differ by40 while a bank extends only12 in e1.
Consequently every data draw from(2.1) is exactly delta_(P_(n,w,a)^s).

The setting site is d=c+(0,10,0), initially empty. Prepare

    d+e3,d+2e3:P_Z^+,
    d-e3,d-2e3:P_Z^-,  P_Z^s=(I+sZ)/2, Z=diag(1,-1).   (3.5)

Each setting seed has its matching guard as a buddy. At setting formation,
the only present nearest neighbors are d+e3,d-e3. Thus(2.1) gives exactly
one-half delta_(P_Z^+) plus one-half delta_(P_Z^-). Define the setting bit
by which of these two contents is read. Form the two wings' settings
independently conditional on the preceding history. Every pair(a,b) has
conditional weight1/4, independent of the supplied pre-round rho_h.

The actual primitive readout can be the matrix content X itself, a function
of content alone. Identifying its program/outcome label uses the separately
read program Records and the declared typed experimental map(1.1). This
does not make an absent site readable or put a program-dependent value into
the primitive readout. Physical calibration of that typed map remains open.

Each wing/round has eight bank Records and four setting Records initially,
so(3.3)–(3.5) use24N prepared Records in total.

## 4. Permanent preparation blocks and a recoverable frame

Write the two-qubit preparation in four M2 blocks:

    rho=[[B00,B01],[B10,B11]].                            (4.1)

Store these blocks, in that fixed order, at

    b_k=(-50+5k,-50,-50), k=0,1,2,3,
    b_k+e2 carrying the same B block.                    (4.2)

These eight Records are outside every experimental neighbor shell. They
are permanently admissible because of their buddies. A law-side calculator
reads and reconstructs(4.1); rho is not an additional unrecorded state.
The stated domain includes precisely positive normalized reconstructed rho.
Its blocks have operator norm at most1, including off-diagonal blocks:
each is a compression between two subspaces of a positive trace-one matrix.

For an unambiguous rigid frame, put f=(-10,-10,-10) and prepare

    f,f-e1:10I;
    f+e1,f+2e1:11I;
    f+2e2,f+2e2+e1:12I;
    f+3e3,f+3e3+e1:13I.                                 (4.3)

Every marker has a same-content buddy. No marker is a neighbor of an event
or preparation-block site. All nonmarker contents have norm at most1:
they are preparation blocks or projectors, and every later draw copies one
of those. Thus no later Record can be confused with a marker value.

Of the two10I sites, only f has a nearest11I neighbor. This identifies f
and e1. Of the12I sites, only f+2e2 has distance2 from f; this identifies
e2. Of the13I sites, only f+3e3 has distance3 from f; this identifies e3.
All operational sites, block indices, program labels and round numbers
are therefore recoverable from the permanent marked Record configuration.
The eight markers plus eight preparation-block Records account for the
remaining16 prepared Records.

Transport the preparation and kernel by every lattice translation and
proper cubic rotation. The recovered frame is unique and permanent; two
different transported domains cannot assign different answers to one
configuration. The local rule(2.1) is already covariant without markers.
This gives K(gR,gB)=K(R,B) on the union of transported prepared domains.
A supplied experiment selects a frame; the law selects no absolute site.

## 5. The current-Record kernel

At a configuration in the declared domain, find the first round whose two
fixed output Registers are not both present. Completed earlier rounds,
their selected first relays and projector contents are permanent.
Reconstruct sigma_h from(4.1) and these earlier first-relay contents in
round order. This is a deterministic function of current Records. No
saved wavefunction, process tensor, hidden random seed or step counter
is included in the physical state.

For that round perform these operations:

1. If its settings have not formed, form the two setting Records with the
   independent fair laws in section3. No data Record forms in this step.
2. With settings present and no first relay present, compute(1.2) and choose
   the pair(s,t) with those probabilities. Form exactly the two selected
   first-relay sites j(a,s),j(b,t). Their contents are deterministic draws
   from the local empirical rule, hence the matching projectors.
3. Once a first relay exists, recover j from its location. Advance each
   unfinished wing by one site along(3.4), drawing from its one-neighbor
   empirical law. A completed wing adds no more Records. Continue until
   both fixed outputs are present; the next transition begins the next round.
4. Once every round is complete, use the identity kernel forever.

These are one fixed set of formulas on all states in the supplied domain.
For variable matrix preparations and programs, the trace products are
polynomial in their entries and conjugates and the conditional ratios
have positive denominators on the supported domain. Thus the weights and
copy maps are Borel; the finite atomic transitions define a measurable
kernel throughout the stated continuous matrix-input family.
The language about which designated sites are present describes a Record
configuration and never assigns a readable value to absence. There is no
state ambiguity when one wing finishes sooner: the other wing still has
a unique unfinished path. The stage and the selected paths are always
recoverable from the current permanent occurrences.

The joint first-relay choice is explicitly nonlocal: it uses both settings,
the global preparation blocks and earlier joint history. The law does not
derive local causal generation of this coupling. The number of path steps
can depend on the outcome and is not a physical-time or no-signalling
claim about an apparatus clock. Simultaneous new sites are never nearest
neighbors; subsequent one-site extensions are therefore well-defined.

All possible transitions have nonnegative normalized weights. For settings
this is the product of two fair empirical measures. For first relays,
projector completeness gives sum_(s,t)Tr(J sigma_h J)=Tr sigma_h. Subsequent
data steps and absorbing continuation are deterministic. Induction gives
a probability measure on every finite history prefix. The process makes
at most16N transitions, after which identity continuation defines every
later prefix without any infinite-product or thermodynamic assumption.

Conditional on the complete past AND formation at a specified physical
site, its content law is exactly(2.1). At a first-relay site, conditioning
on its formation already identifies its selected program/outcome bank,
and the law is the corresponding delta projector. At a terminal site,
its predecessor Record determines the same delta. The pair of outcome
probabilities before the occurrence choice is(1.2); these are different
conditioning questions. It would be incorrect to report the trace weights
as newly derived values of the per-site local copying law.

A one-site refinement of the joint first-relay step is also available.
Choose the first wing with probability1/2, choose its outcome by the
corresponding trace marginal, and append its first relay alone. At the
next step append the other first relay using the conditional trace law.
The first wing is recoverable from which first relay is present. Once
both are present, the order need not be retained: the two projectors
commute, so both orders give the same surviving matrix and the same
future kernel. Each order has joint outcome weight Q/2; summing orders
gives Q. This provides genuine one-event prefix configurations and exact
confluence of their completed ledgers. The refinement uses the same
Records and at most17N transitions. Its ordered histories additionally
carry the explicit order-choice weights; no spacelike timing is inferred.

## 6. Exact selected history law, including every relay

Let the chronological joint projectors for the first relays be J_1,...,J_m.
Sequential use of(1.2) telescopes:

    product_(i=1)^m Q_i
      =Tr[J_m...J_1 rho J_1...J_m],                      (6.1)

because Tr rho=1. Including fair settings multiplies each supported
setting/outcome history by4^-m. This proves positivity, normalization,
prefix consistency and the selected trace cylinder for all m<=N, not
only an isolated comparison table. No fitting or numerical trace table is
used to establish(6.1).

At a supported first event in a round, let sigma'=J sigma_h J. On wing A,
write A=P_A^s tensor I. Then A sigma' A=sigma' because A J=J. Its matching
repeat has conditional trace weight1 and its orthogonal alternative has
weight0. The identical argument holds at wing B. Opposite-wing projectors
commute, so any interleaving of repeated path copies preserves sigma'.
Therefore all additional data Records in(3.4) are legitimate trace-certain
repeats on the declared typed mathematical sector. The full augmented data
history has exactly the first-relay history's weight. Summing the auxiliary
paths to the fixed terminal registers gives the same cylinder(6.1).

This statement concerns the typed data-Record subsequence. Prepared banks,
matrix blocks, markers and fair setting Records are apparatus/boundary data,
not extra projective measurements of the same logical two-qubit system.
Their roles are reconstructed from the declared geometry. The distinction
is supplied experimental interpretation, not a physical calibration theorem.

For a product preparation rho_A tensor rho_B, local projectors preserve
the product form on each supported branch, and(1.2) factorizes into the
two local trace weights. For any positive sigma_h, summing over the remote
outcome gives Tr[(P_A^s tensor I)sigma_h]/Tr sigma_h, independent of the
remote program. This proves the usual per-round outcome no-signalling
identity conditional on the common pre-round history. It does not supply
relativistic locality of the global occurrence mechanism or its scheduling.

For the singlet in round1 with A0=Z,A1=X,B0=(Z+X)/sqrt2,B1=(Z-X)/sqrt2,
the standard projector product gives E00=E01=E10=-1/sqrt2,E11=+1/sqrt2,
and CHSH magnitude2sqrt2. These values follow from the SUPPLIED trace rule
and preparation. The local content rule has supplied no probability
selection, and the target comparison was known during construction.

For a separate one-round comparison, hold the same preparation, programs,
geometry, setting process, readout and content rule(2.1) fixed. Replace only
the first-relay occurrence table by either uniform Q(s,t)=1/4 or
Q(s,t)=1/2 when st=(-1)^(ab), zero otherwise. The identical deterministic
copy process gives CHSH0 or4 respectively, while the trace choice gives
2sqrt2. In this particular Bell fixture, one fixed content-only binary
statistic also suffices: r(X)=sign Re Tr[(2Z+X_Pauli)X]. Its positive-axis
expectations are2,1,3/sqrt2,1/sqrt2 for the four displayed directions,
so every matching projector P_e^s has statistic s independently of e.
The matrix X in r denotes content; X_Pauli is the fixed Pauli matrix.
No final location or absent-site value is used as that output statistic.
The two alternative tables are deliberately supplied comparison laws;
they are not claimed to obey the selected trace sector Law or describe
physical experiments. The all-N trace-history theorem retains(1.2).

## 7. Physical support, resource bound and scope

Initially every Record has a same-content buddy, so(2.1) supports all
24N+16 supplied contents. All setting outcomes are drawn from two supported
neighbor atoms and retain a matching seed. Every data site has exactly one
same-projector predecessor when it forms, which remains forever. Adding
subsequent nearest neighbors cannot remove any existing matching neighbor.
All old and new Records therefore remain locally supported, including
after the local neighborhood changes. There is no need to assign mass to
an exact point under a continuous Gaussian or to weaken continued support.

Each round adds two setting Records plus L_j+L_k data Records. Since
6<=L_j,L_k<=15,

    14<=new Records per round<=32,
    38N+16<=final Records<=56N+16.                       (7.1)

The lower count is an attainable geometric bound, not a claim that every
supplied trace table gives positive mass to its minimizing branch. Every
round takes one setting transition plus at most15 data transitions. Thus
at most16N transitions occur. All experiment sites fit in a box of length
80N+O(1) in e1 and fixed transverse dimensions, with the fixed preparation
and marker region included. Occupied resources and reserved box volume are
O(N), for the declared two-program/two-wing domain. These are exact counts
of supplied Records/sites, not a cost of manufacturing them or running a
physical clock. The calculator's arithmetic memory is not an additional
ontic state; its computational time is not priced as a physical resource.

The construction realizes more than a sign-only Bell table: full matching
projector contents, complete finite trace cylinders, actual nearest-neighbor
formation laws and supported permanent physical preparations coexist.
However, the quantum weights have been supplied in a global occurrence
law, and their first data sites depend on the outcomes. The later fixed
output is already a repeat of a committed result. This is a finite prepared
history embedding, not the benchmark's stronger local-marginal theorem
at one fresh common first-event site and not a native measurement model.

The current minimal memo permits named conditional law domains and does not
supply occurrence weights. The selected projective-sector source supplies
the trace history and matching-projector benchmark conditionally. No input
is silently promoted to an axiom derivation or approved primitive. This
positive example is one route an axiom-pressure argument must address;
it is not an exhaustive comparison of possible laws or a universal no-go.

## 8. Verification plan and authority

The all-N geometry, support, Markov sufficiency and trace induction above
were written before finite checking. The checker should reconstruct a
two-round noncommuting fixture, all settings and supported outcomes,
compare direct chronological matrix products with sequential occurrence
updates, and insert actual repeated data projectors. Independently inspect
all six neighbors of every path step, initial and continued support, all
24 proper rotations, four-block reconstruction, zero branches, product
factorization, singlet correlations and the stated counts. Tests should
reject missing projectors, skipped updates, wrong bank indices, source
contamination and readout/location substitution. Numerical agreement alone
does not establish the all-N proof. Independent source review remains pending.


The final author checker passed29 grouped checks. Direct density updates and
pure-ensemble amplitudes agree on240 positive two-round prefixes, with32
zero children excluded from conditioning. It verifies2682 repeated data
layers, actual Record-only reconstruction of224 final histories, physical
paths at horizons1,2,7 and720 transported neighbor-law cases. These are
finite checks of the written all-N argument, not an independent source
review. No mathematical predicate failed or tolerance was relaxed.
