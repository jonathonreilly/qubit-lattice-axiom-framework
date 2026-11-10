# A detector with only a carrier input

2026-11-09 local date. Integrated research source; comparison receipts are kept separately.
PRIMARY.md preserves the original frozen proof.
Parent: 95a40545b05ba3039a83819cf41158d049e2596a.
Main: bf92a1d763030836ed55631d5d7a7ef3b288f284.
Axiom source SHA256: 301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc.
Claim type: bounded_theorem. Status: conditional-support; not audited.
No Born rule, quantum state geometry or axiom amendment is used.

## 1. The input boundary is a physical condition

Let lambda name a preparation procedure and C be a finite set of complete
incoming carrier-record configurations. Preparation lambda supplies a law
mu_lambda(c). This law is a supplied preparation condition, not a derivation
of its numerical weights from the axioms. Let d denote the detector's fixed
context (program, apparatus placement and orientation), H its accessible
record history and B a declared output event. Those apparatus data are held
fixed across the preparations being compared; spatial covariance alone does
not prevent a preparation-dependent placement from carrying information.

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

For finitely many steps, multiply the successive measurable conditional
kernels and integrate over apparatus variables. Sums are integrals when
waiting times or apparatus variables are continuous. Every factor is
independent of lambda, so the resulting K_d is independent of lambda. Adaptive controls also fit when they depend only on
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
Perfect discrimination that always returns a conclusive answer requires
disjoint input supports; it is sufficient when all indicators can be tested.
Repeated copying cannot evade this bound.

For an arbitrary allowed effect family E, the actual distinguishability is
sup_(e in E)|sum_c Delta_c e(c)|, assuming complement closure. It can be
strictly below TV. Operational preparation equivalence means equality on E;
equal carrier laws always imply equivalence, but the converse needs a
separating family. No unrestricted-effect assumption is hidden here.

Postselection is different. For mu=(1/2,1/2,0) and nu=(0,1/2,1/2), reporting
only carrier symbols 0 or 2 identifies the source without error on accepted
trials, but rejects half the trials under either preparation. TV is 1/2;
the best always-answering success probability is 3/4. A failure flag must
remain in the full outcome law; conditioning on acceptance changes the
ensemble and need not preserve the same TV bound or affine normalization.

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
uses a single-test family consisting only of individual bits and their
mixtures/complements, the
equal mixture of 00,11 and the equal mixture of 01,10 have identical test
statistics despite different carrier laws. Allowing a joint read of both
bits or the parity test separates
them. This is an abstract restricted-observation example, not a claim that
the native decoder in section 4 hides either bit. The measurement restriction
must itself be physically justified before using that quotient as a state space.

## 4. A native family with an isolated source label

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

Define the content kernel at any site x before applying an occupancy mask.
From records at 0<||y-x||_1<=6, require exactly one of each header, a proper
cubic frame and all six mandatory DETECTOR seed records at their decoded
locations and values. Require equality to the complete target-specific
pattern below; no records beyond that pattern may be visible. The external
source record is never a seed requirement. At x=f assign Dirac content g(a)I when
its visible configuration is precisely that detector seed. At x=z assign
Dirac content h(g(a))I when it is precisely that seed plus the required fine
record. All other pattern/site conditions give the fallback content law

    F = (1/2) Uniform(A_code) + (1/2)[p delta_I+(1-p)delta_0],
    p = (1/2+l)/(1+k),

where k counts visible records and l counts those equal to I. Ambiguous or
invalid parses also take this fallback. Formation rate is one exactly when
one of the two Dirac patterns matches AND x is absent; it is zero otherwise.
Occupancy never changes the center-excluded content kernel used to test old
record support. The clock law uses independent exponential waits, with no correlation
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

Every old record retains admissible support. Removing a detector seed record
from its own neighborhood leaves a mandatory hole, so the fallback supports it.
Removing the fine record at R1 exposes its enabling seed. Removing it at
R2 leaves an extra coarse record, hence fallback. Removing the coarse
record at R2 exposes its enabling predecessor. The source has no visible
records near it and has positive fallback mass. Every used fallback atom
has mass at least 1/(2|A_code|). Recorded zero is distinct from absence.
This proves support and permanence, not merely an instruction never to overwrite.

For any chosen preparation family mu_lambda(a), sample a in the initial
condition and keep the detector seed/program, placement and orientation
otherwise fixed. Applying a common spatial transformation gives another
experiment with the same result. The external source record may contain lambda, but every detector transition, content and
waiting law conditioned on a is identical for all lambda. This proves the
closed input boundary for the supplied process. Different preparation labels
with the same mu give the same complete detector histories; this is not a
renaming of distinct labels as distinct incoming symbols. Distinct incoming
symbols can also be distinguishable, as the next section shows.

## 5. The effects and geometry actually realized

For fixed g,h the actual fine outcome is g(a), and the actual coarse bit is
h(g(a)), with both the carrier and fine record retained. The effects described
next refer to these specified output questions; reads of other detector
records can enlarge the allowed effect family. The common-kernel bound
already covers that larger record history. No timestamp readout is supplied:
the model's waiting times are mathematical variables, not automatically
readable records. Therefore

    Pr_lambda(coarse=1) = sum_a mu_lambda(a) h(g(a)).

For a fixed program, observing only its fine/coarse outputs distinguishes
carrier laws exactly through the pushed-forward distribution
p_lambda(b)=sum_(g(a)=b) mu_lambda(a). The coarse record is a function of the
fine record. For two preparations, the exact fine-output distance is

    TV(g_*mu,g_*nu) = (1/2) sum_b |sum_(g(a)=b) [mu(a)-nu(a)]|.

It equals input TV exactly when no g-fiber combines a strictly positive and
a strictly negative input difference. This is the equality condition in the
triangle inequality applied separately to each fiber. The same formula with
h composed with g gives the coarse-output distance. Timing is a common
independent factor and changes neither distance. Additional direct reads of
the carrier would be a larger interface; they are not needed for the copying
or programmed-indicator tests below.

For every subset S of the K-symbol carrier alphabet and any fixed M>=2,
take g=1_S and h(0)=0,h(1)=1, setting unused h entries to zero. One rule
with these fixed K,M realizes every such program.
All indicator effects are therefore physically available in this chosen
family. They separate all distinct carrier distributions and attain the TV
testing bound. For example, on a two-symbol carrier, mu=(3/4,1/4) and
nu=(1/4,3/4) have TV=1/2 and equal-prior best success 3/4. The indicator of
the first symbol attains that value. Labels with identical mu have success
at most 1/2. These values are hand calculations, not numerical executions.

Choose T>=K and include the K point preparations mu_a=delta_a. With M>=K
and g(a)=a, one fixed program copies the incoming symbol to the fine output
while preserving the carrier. It perfectly distinguishes those K prepared
carrier values without accessing the source label. An arbitrary previously
fixed preparation family need not contain these point preparations. For every
finite K this uses one incoming carrier site and the same eight-site spatial
layout; its supplied code, program alphabet, decoder and law parameters
depend on K. It is not one fixed finite-capacity device asserted to implement
all K simultaneously. It shows that label exclusion by itself, within this
literal scalar-code family, imposes no universal two-symbol capacity bound.
The output apparatus's dimension is not identified with that of one qubit.

For a concrete separation between signal and preparation label, use T=2K
procedures with mu_lambda=delta_(floor(lambda/2)). The copier distinguishes
K different carrier contents, but each pair of external procedure labels is
indistinguishable by the detector. The same law permits overlapping carrier
laws, with their discrimination limited by section 2. It does not recover
the preparation procedure merely by renaming its inaccessible label.

As an OPTIONAL quantum-representation test, suppose these K point inputs
could be represented by densities rho_a on C^d and one fixed POVM E_b with
tr(rho_a E_b)=delta_(a,b). Then 0<=rho_a<=I implies

    1=tr(rho_a E_a)<=tr(E_a),   K<=sum_(a=0)^(K-1) tr(E_a)<=d.

For K>2 this interface cannot be faithfully represented by a lone qubit
without extra accessible information. This is a consequence of the chosen
scalar code and decoder, not a proof that a physical quantum sector is
impossible. In this example the apparatus starts identically for every a,
and the source label cannot affect its records; the obstruction in the
comparison is no longer caused by access to that external label. The matrix
pairing is used only to test the proposed representation, never to produce
the detector's probabilities.

If arbitrary classical mixtures of carrier preparations are additionally
available, the operational state set of this full indicator family is the
simplex Delta_(K-1): indicator values recover every component mu(a), and
every mixture of point preparations produces its probability vector.
This is a derived description for the selected family, not a new ontology
or a theorem that every allowed lattice realization must be classical.

If independent classical randomization of the detector program is also
available, it provides one sufficient way to realize every effect e in
[0,1]^K through the specified coarse output. Choose a random subset S
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
p_b(a). A fixed h groups those actual outputs. For a fixed M>=3, any e,f
with e+f<=1 have a common three-outcome realization with probabilities
e,f,1-e-f (all remaining fine labels have probability zero). Choosing
M>=max(K,3) permits copying, all indicators and this refinement under one
fixed K,M rule. Arbitrary menus larger than that fixed M are not claimed.
Thus full classical effect addition and this pair refinement are realizable under
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

The finite total-variation testing identity is standard; see Yihong Wu,
[Information-theoretic methods for high-dimensional statistics, section 4.3,
Theorem 4.3](https://www.stat.yale.edu/~yw562/teaching/it-stats.pdf).
Only the indexed theorem extract was accessible during this task; the full
PDF fetch failed. The finite case and the required detector factorization
are proved here, rather than imported as unchecked physical premises.
[ASSUMPTIONS.md](ASSUMPTIONS.md) records the inputs and
[NO_GO_DISCIPLINE_CHECKLIST.md](NO_GO_DISCIPLINE_CHECKLIST.md) limits the
comparison claims. No novelty is asserted for data processing, classical
statistical effects, randomization of deterministic maps, or the dimension bound.
