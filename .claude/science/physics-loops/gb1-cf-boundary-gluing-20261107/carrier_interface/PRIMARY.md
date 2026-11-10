# A detector with only a carrier input

2026-11-09 local date. Frozen supervisor proof before independent comparison.
Parent: 95a40545b05ba3039a83819cf41158d049e2596a.
Main: bf92a1d763030836ed55631d5d7a7ef3b288f284.
Axiom source SHA256: 301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc.
Claim type: bounded_theorem. Proposed status: conditional-support.
No Born rule, quantum state geometry or axiom amendment is used.

## 1. The input boundary is a physical condition

Let lambda name a preparation procedure and C be a finite set of complete
incoming carrier-record configurations. Preparation lambda supplies a law
mu_lambda(c). This law is a supplied preparation condition, not a derivation
of its numerical weights from the axioms. Let d denote the detector's fixed
program, H its accessible record history and B a declared output event.

The required condition is stronger than deleting a label from a formula:
given c and d, the detector must have the same history law for every lambda.
Call that law K_d(dh|c). A sufficient microscopic specification is:

* initial apparatus records have a conditional law alpha_d(a|c) independent
  of lambda; a fixed apparatus is the special case of a point mass;
* the formation/transition kernels on successive accessible histories are
  fixed functions of c, the apparatus and those histories, including any
  accessible controls, with no remaining lambda dependence;
* no later source message, correlated clock/randomness, or outside record
  can influence the experiment before its declared end;
* a joint history law exists. For the finite construction below there are
  exactly two new records; in a general bounded experiment, include failure
  or noncompletion as an outcome rather than conditioning it away.

For finitely many steps, multiply the successive conditional kernels and
sum over a. Every factor is independent of lambda, so the resulting K_d is
independent of lambda. Adaptive controls also fit when they depend only on
accessible history and source-independent private randomness. This derives
the common history kernel from the specified dynamics and isolation; the
Admissibility content-distribution clause alone supplies neither joint
histories nor formation rates. The explicit lattice model in section 4
proves its own isolation rather than assuming it from spatial separation.

The incoming variable must include all carrier records that can affect the
law, not merely a selected marginal or a coarse readout. Equality of those
complete carrier laws suffices; whether a smaller description suffices is
a separate conditional-independence question.

## 2. Distinguishability and effects from the common kernel

Ordinary total probability gives

    Pr_lambda^d(B) = sum_c mu_lambda(c) e_(d,B)(c),
    e_(d,B)(c) = K_d(B|c),       0 <= e_(d,B)(c) <= 1.

These e are operational effects on carrier configurations. Complementation
gives e_(B^c)=1-e_B and disjoint events in one history space give
e_(B union D)=e_B+e_D. This is a statement about event probabilities, not
the discarded scalar-additivity axiom for record collections. No inner
product, matrix positivity cone or trace pairing is needed.

Equal mu therefore implies equal probabilities for every accessible history
event and every allowed detector program. This remains true for adaptive
use and repeated processing of the same input under the common-kernel
conditions. It does not assert that independently supplied fresh carriers
have the same information content as one carrier.

For two incoming laws mu,nu, put Delta_c=mu(c)-nu(c) and

    TV(mu,nu) = (1/2) sum_c |Delta_c| = sum_(Delta_c>0) Delta_c.

For every effect 0<=e<=1, its positive contribution is at most the latter
sum and its negative contribution has the same total magnitude. Consequently

    |Pr_mu(B)-Pr_nu(B)| <= TV(mu,nu).

The same bound applies to the entire outgoing history law by taking the
supremum over B. With equal prior odds, a decision event B that guesses mu
has success probability [1+Pr_mu(B)-Pr_nu(B)]/2, hence at most
(1+TV(mu,nu))/2. If the indicator of S={c:mu(c)>nu(c)} is an available
effect, equality is achieved. Availability is not inferred from the bound.
Perfect discrimination requires disjoint input supports; it is sufficient
when all indicators can be tested. Repeated copying cannot evade this bound.

For an arbitrary allowed effect family E, the actual distinguishability is
sup_(e in E)|sum_c Delta_c e(c)|, assuming complement closure. It can be
strictly below TV. Operational preparation equivalence means equality on E;
equal carrier laws always imply equivalence, but the converse needs a
separating family. No unrestricted-effect assumption is hidden here.

If an additional classical mixture protocol chooses preparations independently
of the apparatus and preserves the interface conditions, its carrier law is
the corresponding convex mixture. The response is affine by the displayed
sum. All mixture laws need not be physically preparable under bare axioms.

## 3. Why weaker privacy conditions fail

An apparatus marginal independent of the preparation is insufficient. Let
C be a fair bit under both labels lambda=0,1. Prepare an apparatus bit A=C
when lambda=0, and A=1-C when lambda=1. Both C and A separately have the same
fair marginal under both preparations, but the fixed detector output C XOR A
distinguishes the labels perfectly. The missing condition is the joint
carrier/apparatus law: alpha(A|C,lambda) depends on lambda. This is a finite
probability counterexample to a weaker interface premise, not a lattice
realization claim for this particular two-bit preparation procedure.

Likewise, being outside the initial neighborhood does not alone forbid
later influence through neighbors. This task therefore does not infer an
all-time closed input boundary from a distance cutoff. Its explicit process
has no enabled relay sites. An unrestricted relay dynamics or an unrecorded
preparation-dependent clock would require a different interface analysis.

No full quantum geometry follows from the common-kernel formula. Restricted
tests can identify distinct carrier laws: if a four-symbol carrier c=(x,y)
is tested only by its individual bits and their mixtures/complements, the
equal mixture of 00,11 and the equal mixture of 01,10 have identical test
statistics despite different carrier laws. Allowing the parity test separates
them. This is an abstract restricted-observation example, not a claim that
the native decoder in section 4 hides either bit. The measurement restriction
must itself be physically justified before using that quotient as a state space.

## 4. A native family with a genuinely inaccessible source label

Fix finite integers K,M>=2 and T>=1. K is the carrier alphabet size; M is
the number of fine output labels; T is the number of preparation procedures.
These are supplied code parameters. There is one fixed rule for all
carrier values, programs and preparation labels at these parameters.

Every integer v denotes the scalar matrix vI in M2(C). In a prepared frame:

* header records -1,-2,-3,-4 occupy 0,e1,e2,e3, respectively;
* the carrier a in {0,...,K-1} occupies 2e1;
* a program q occupies 2e2;
* fine and coarse targets f=3e1, z=3e1+e2 are initially blank;
* the source label -5-lambda, lambda in {0,...,T-1}, occupies 20e1.

The detector patch has eight sites, six initially recorded. The source is
a ninth site. The patch has L1 diameter at most five, and its distance from
the source is at least seventeen. Use radius R=6, with the center excluded
from its conditional content neighborhood. All translated/properly rotated
copies belong to the legal domain. The source is external to the detector's
readout interface; the rule below prevents it from sending any relay signal.

The program encodes g:{0,...,K-1}->{0,...,M-1} and h:{0,...,M-1}->{0,1}:

    G = sum_(a=0)^(K-1) g(a) M^a,
    H = sum_(b=0)^(M-1) h(b) 2^b,
    q = G + M^K H,       0 <= q < Q=M^K 2^M.

Base-M digits and the binary bits give a unique decoder. The program is
fixed for an experiment and carries no preparation identity. Readout maps
each used scalar record vI to v, and maps all other matrices to one constant
"other" value. This is an explicitly supplied content code and decoder,
not a claim that these codewords are density matrices of a quantum qubit.

Let A_code be the union of {0,...,Q-1}, the four negative header values and
the T negative source-label values, times I. The carrier and both output
alphabets are subsets of this finite set. Let R0(a,q,lambda) be the seven
initial records, R1 add g(a)I at f, and R2 add h(g(a))I at z.

Define the local rule at any site x as follows. From records at
0<||y-x||_1<=6, require exactly one of each header, a proper cubic frame,
all mandatory seed records at their decoded locations and values, and no
extra visible records. Enable x=f with Dirac content g(a)I when its visible
configuration is precisely the six-record detector seed. Enable x=z with
Dirac content h(g(a))I when it is precisely that seed plus the required fine
record. Each enabled absent site has rate one. All other sites have rate
zero and content law

    F = (1/2) Uniform(A_code) + (1/2)[p delta_I+(1-p)delta_0],
    p = (1/2+l)/(1+k),

where k counts visible records and l counts those equal to I. Ambiguous or
invalid parses also take this fallback. Formation never acts on an occupied
site. The clock law uses independent exponential waits, with no correlation
to lambda beyond the present carrier records. The content rule is total on
arbitrary matrix-valued neighborhoods; the claimed invariant global domain
is only these prepared prefixes and their spatial copies.

The frame is reconstructed from records, so translations and proper rotations
commute with the rule. Every used scalar content is fixed by algebra
relabelings. The content law varies with the neighborhood, including through
the fallback counts. A site can be enabled only by the unique four global
headers and must then equal their f or z. Thus no outside site, including
any site between the source and detector, can form. All detector targets
see the whole detector and never see the source. Only f is enabled at R0,
then only z at R1, then none at R2. There are exactly two births, each after
an exponential rate-one wait, almost surely; mean total time is two in the
chosen units, independent of lambda,a,q.

Every old record retains admissible support. Removing a seed record from
its own neighborhood leaves a mandatory hole, so the fallback supports it.
Removing the fine record at R1 exposes its enabling seed. Removing it at
R2 leaves an extra coarse record, hence fallback. Removing the coarse
record at R2 exposes its enabling predecessor. The source has no visible
records near it and has positive fallback mass. Every used fallback atom
has mass at least 1/(2|A_code|). Recorded zero is distinct from absence.
This proves support and permanence, not merely an instruction never to overwrite.

For any chosen preparation family mu_lambda(a), sample a in the initial
condition and keep the detector seed/program otherwise fixed. The external
source record may contain lambda, but every detector transition, content and
waiting law conditioned on a is identical for all lambda. This proves the
closed input boundary for the supplied process. Different preparation labels
with the same mu give the same complete detector histories; this is not a
renaming of distinct labels as distinct incoming symbols. Distinct incoming
symbols can also be distinguishable, as the next section shows.

## 5. The effects and geometry actually realized

For fixed g,h the actual fine outcome is g(a), and the actual coarse bit is
h(g(a)), with both the carrier and fine record retained. Therefore

    Pr_lambda(coarse=1) = sum_a mu_lambda(a) h(g(a)).

For every subset S of the K-symbol carrier alphabet, take M=2, g=1_S and
h(0)=0,h(1)=1. One rule with these fixed K,M realizes every such program.
All indicator effects are therefore physically available in this chosen
family. They separate all distinct carrier distributions and attain the TV
testing bound. For example, on a two-symbol carrier, mu=(3/4,1/4) and
nu=(1/4,3/4) have TV=1/2 and equal-prior best success 3/4. The indicator of
the first symbol attains that value. Labels with identical mu have success
at most 1/2. These values are hand calculations, not numerical executions.

With M=K and g(a)=a, one fixed program copies the incoming symbol to the
fine output while preserving the carrier. It perfectly distinguishes K
point-prepared carrier values without accessing the source label. For every
finite K this uses one incoming carrier site and the same eight-site spatial
layout; its supplied code, program alphabet, decoder and law parameters
depend on K. It is not one fixed finite-capacity device asserted to implement
all K simultaneously. It shows that label exclusion by itself, within this
literal scalar-code family, imposes no universal two-symbol capacity bound.
The output apparatus's dimension is not identified with that of one qubit.

If arbitrary classical mixtures of carrier preparations are additionally
available, the operational state set of this full indicator family is the
simplex Delta_(K-1): indicator values recover every component mu(a), and
every mixture of point preparations produces its probability vector.
This is a derived description for the selected family, not a new ontology
or a theorem that every allowed lattice realization must be classical.

If independent classical randomization of the detector program is also
available, every effect e in [0,1]^K is realized. Choose a random subset S
with weight

    w_S = product_(a in S) e(a) product_(a not in S) [1-e(a)].

The weights are nonnegative and sum to one; their sum over S containing a
is e(a). Run the deterministic indicator program for that S. This derives
the response from a supplied randomization protocol, not its weights from
the axioms. The program record persists; equal coarse statistics do not
identify full histories or future uses.

More generally, any finite normalized classical response menu p_b(a)>=0,
sum_b p_b(a)=1, is realized with M fine labels by randomizing over maps g
with weights w_g=product_a p_(g(a))(a). Summing over maps with g(a)=b gives
p_b(a). A fixed h groups those actual outputs. In particular e,f with
e+f<=1 have a common three-outcome realization with probabilities e,f,1-e-f.
Thus full classical effect addition and refinement are realizable under
the independent program-mixture premise. They do not select M2 quantum
geometry. Reading a trace formula from an afterwards chosen diagonal
embedding would restate these probabilities rather than derive their law.

## 6. Scope and next physical question

The closed-input theorem, exact native isolation, support proof, classifier
construction and capacity family are the proved conditional results here.
Initial preparation laws, the scalar decoder, finite program code, chosen
local activation/rates, inaccessible source interface and optional mixture
protocols remain named inputs. The general theorem does not supply an
arbitrary lattice's joint formation law. No global classicality, Bell
restriction, quantum impossibility, minimal axiom change, continuum, vacuum
or mass-gap conclusion follows.

The next quantum question concerns which carrier contents can actually be
prepared, which distinctions a physical decoder can read, and which source-
independent detectors are physically realizable. Removing a label closes
one leakage channel; the native construction shows that it does not alone
derive the quantum capacity or effect cone. An axiom change is not proposed.
