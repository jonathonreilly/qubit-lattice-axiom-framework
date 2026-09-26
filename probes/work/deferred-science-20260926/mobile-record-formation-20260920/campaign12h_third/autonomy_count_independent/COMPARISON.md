# Frozen author-source comparison

The carrier formulas, formation-count invariant, physical electric-monitoring
law and terminal-state calculation agree with the sealed independent
reconstruction. The independent post-seal checks below also reproduce the
reported exact bounds and finite combinatorial data. One narrow scope
clarification, F1, remains against the frozen prose: the ring completion
theorem should expressly exclude arbitrary extra N,T-commuting jumps allowed
in the earlier count-identity section. No formula or numerical correction
is indicated. This is a bounded scientific comparison, not a formal audit
or publication decision.

## F1: separate the completion model from the broader count-identity class

`FORMATION_COUNT_CONTROLS_GAUGE_COHERENCE.md`, Section 1, allows every other
jump that commutes with N and T. Section 3 subsequently supplies hopping,
occupation monitoring, H0 and births and states completion, but does not
explicitly remove that broader other-jump allowance. Section 4 again says
"the other jumps commute with T." The intended model is clear from the
proof and the neutral brief; its exclusion of arbitrary added jumps should
also be explicit in the theorem's premises.

A sufficient narrow addition in Section 3 is:

> The completion assertion here contains only the specified hopping,
> occupation-preserving H0, occupation-monitoring jumps and birth terms.
> It does not extend to arbitrary additional jumps allowed in Section 1.

The same restriction should govern Section 4's use of this completion
theorem; replacing its generic "other jumps" by "occupation-monitoring
jumps" would make that reference unambiguous. The broader count identity
and the conditional statement "if occupation completes" remain unchanged.

This is a consequential qualification, not a preference for extra caveats.
The pre-sealed exact C4 example has unit hopping H, P projecting onto
non-contact occupation pattern (1,0,1,0), and rho=P/2. Its additional jump

    L=P+2i P H

commutes with N and T, yet D_L(rho)=i[H,rho]. All births and occupation
monitors vanish on rho, so it is a stationary nonfull density. Thus the
Section 1 commutators alone do not justify Section 3's conclusion. The
source's stationary Hilbert-Schmidt argument applies to the intended list
of terms and cannot silently include this additional dissipator.

The parent has confirmed the intended restricted ring model. This report
retains the original source identities; F1 remains open until the actual
corrected delta is independently acknowledged. No primary source was edited.

## Autonomous rail argument and the added finite controls

The complete rail note was read. Its single dressed bond, W conjugacy,
arbitrary-input arrival mixture and reference-system extension agree with
the pre-sealed proof. The fresh-fuel reduction correctly distinguishes
the local channel from the joint gate. The finite-range claim explicitly
belongs to the supplied rail geometry and engineered gate support. It does
not claim a native M2/site construction.

The rest-energy statement also has the needed qualification: the quoted
channel is in the interaction picture of mD. Thus adding mD does not
mistakenly discard a relative phase on arbitrary D-sector superpositions.
The lower spectral bound and the harmless 2J identity shift are correct.
The note expressly excludes additional noncommuting matter/field energies,
an autonomous fresh-carrier supply and a derived initial arrow of motion.

Its packet conventions give velocity +2J sin k for the i^r preparation.
All position/velocity means, variances and the symmetrized covariance
agree with the independently checked rational sums. The one-sided variance
inequality and derivative of its ratio supply a bound uniform over all
unmeasured later times; this does not establish monotone passage. The
characteristic-function proof of the limiting velocity distribution is
valid for this smooth compact-packet Fourier amplitude. Its limit has no
zero-velocity atom. The directional integral, both general upper bounds,
and the distinction between a finite-time bound and an asymptotic limit
are correct.

The three exact displayed nonpassage bounds were recomputed from the
independent moment formulas, obtaining respectively

    17917/1122850,
    118417/42549554,
    516317/674687394.

All decimal entries agree. The seven reported directional tails were
reconstructed by expanding (1-sin s)^M on [0,pi] and integrating each
integer sine power, an alternative to the author's finite Fourier sum.
The exact expressions coincide for M=1,2,4,8,16,40,80. An independent
high-precision beta integral confirms the reported decimal diagnostics,
including the small M=40 and M=80 values. Positivity for all M follows
from the integral, rather than decimal cancellation.

The new localized-packet nonmonotonicity control is correctly scoped. For
a walker at zero, reflection symmetry gives p(t)=(1-J_0(2t)^2)/2 at J=1.
The author's rational alternating-series brackets are valid even though
the first few term magnitudes at argument 4 are not decreasing: the
complete finite prefix is included and the remaining tail is decreasing.
The comparison independently used terms through n=24/25, whose brackets
lie strictly inside the author's n=20/21 brackets, and proves
p(1)-p(2) has an exact positive rational lower bound approximately
0.05380044524521028. The exact rational is retained in
`COMPARISON_RESULTS.json`; no decimal sign test is the evidence.

Both full checker implementations were inspected. The rail checker uses
the actual 18-dimensional local matter/field system and a two-state probe,
then two 216-dimensional finite rail matrices. Its Gauss/resource matrices,
defect orientation, adjoint reverse link, plane-wave boundary equations
and fuel Kraus extraction implement the displayed definitions. The finite
moment matrices have sufficient padding for the tested first/second
moments. These checks are consistent with the independently established
local algebra and 13-site mixture control. No author matrix suite was
rerun, and finite matrices are not treated as proof of the infinite-rail
limit. The note and runner both make that boundary explicit.

## Count law, monitoring and ring theorem

The complete count note was read. Its stated branch algebra gives exactly
the independent dual law, including the treatment of f(K+2) as unnecessary
because P_e vanishes at full occupation. The polynomial definition at
chi=0 is correct. The finite-time estimate

    |<P_full T>-<O_chi>_initial| <= |chi| Prob[N<K]

follows since every nonfull exponent is at least one and each count-sector
T has norm one. It extends to the decaying conserved quantity with the
same error estimate after the stated electric monitoring is added.

The electric paragraph explicitly supplies [E_e,N]=0, E_e^2=I/4 and
{E_e,T}=0. It therefore passes the independently identified commutator
qualification, and the rate lambda=sum_e delta_e/2 is correct. There is
no electric-monitoring finding to repair.

For the restricted Section 3 model, every occupation pattern has the two
complementary physical words. Each legal occupation exchange maps its
entire fiber bijectively to the next fiber. The fixed-count pattern graph
is connected, each nonfull level contains a contact, and positive
occupation monitoring supports the stationary-density proof. Nonzero
inhomogeneous hopping and positive inhomogeneous birth/monitoring rates
do not change these facts when the stated T hypotheses hold. The finite
exponential tail and mean are model-dependent, not uniform in K. The
whole-density terminal limit follows from completion, positivity of the
full/nonfull blocks, T covariance and the two-dimensional full fiber.

Translation invariance is unnecessary. The current note states that
correctly, and its translation-breaking hopping control is meaningful.
The terminal purity (1+chi^K)/2, the positive-cat fidelity within its
stated 0<=chi<=1 domain, and the fixed-|chi|<1 large-K global-coherence
limit follow directly. None is a claim about every local correlation,
native record-only observability or photon physics.

The ring checker correctly implements q_i=b_i-b_(i-1), both birth branches,
all whole-fiber hops and the symbolic invariant. Its T-breaking diagonal
electric H0 is a valid premise-removal control. Its final stationarity
assertions verify the proposed full state; they do not themselves prove
convergence, which remains the separate analytic argument.

Independent post-seal counting checks every reported K=4,6,8 local channel
multiplicity and fixed-N contact count. Each oriented birth branch has
2^(K-3) matrix entries, and each hop matrix has 2^(K-1). For h=K-N holes,
the number of no-contact patterns is the number of size-h independent
sets on a cycle: K/(K-h) binomial(K-h,h) for h<=K/2, and zero otherwise.
Subtracting it from binomial(K,h) reproduces every contact row, including
the full h=0 boundary. Full-state indices, electric eigenvalues and the
symbolic coherence/purity entries also match. This counting route is
independent of the author's graph traversal.

The sealed independent full-Liouvillian controls remain the independent
dynamic check. They show that the transient occupation clock can depend
on chi despite common instantaneous loss and a rate-independent terminal
coherence formula. The current note does not make the stronger, false
clock-identification claim.

## Authentication, read coverage and limits

All 13 artifacts in the authorized author seal authenticate. Both complete
notes, both complete checker scripts, every result field, both full stdout
streams, both empty stderr files, both receipts and the context receipt
were read. Each stdout is byte-identical to its complete result JSON.
Each zero-exit receipt and result bind the corresponding checker hash.
The earlier independent six source and fifteen artifact bindings still
authenticate, and no earlier evidence was changed.

`comparison_check.py` imports no author code. Its first execution passed.
It performs source/receipt authentication and the selective exact checks
described above; its complete log, empty stderr, result and receipt are
preserved. There was no failed attempt in this comparison.

The contextual repository/literature receipt was authenticated as one of
the 13 supplied artifacts. The underlying historical notes, cited papers,
read claims, and old draft archive were not independently reopened or
authenticated in this exactly scoped comparison. They supply attribution
and author history, not a load-bearing theorem import here. No completeness
claim about that broader literature or repository history is made.

The separate quantum-clock/coherent-ring-completion files, checkpoint,
registry and all later frontier artifacts remain unopened. The new seal
binds this bounded comparison to the reviewed source bytes. F1 is the
only unresolved source correction; no mathematical or numerical defect
was found within the reviewed scope.

## Primary identities

- Author seal: `fc3e56328ffbf995b9ee34432e6fd9187a48a9cc6bff48d549c928d7c4499358`.
- Rail note: `7c8f77aed1e6b35f2816ad8944c9f0f6fdc40c7fa3bc20a130b09eaf986424d7`.
- Rail checker: `7bfc1048e170c1d6b192e34d89a994bbed423e4784508609e42779089b80a936`.
- Count note: `7c3444041d1d348d35390e9388d03b03d45e5811456e71bb784dfc87fac46ebe`.
- Count checker: `12ad19fa19580f693fda77665484c3a178208f0fe93c1a41e9dfa5bc5d26a6be`.
- Independent pre-comparison seal: `2fca7f6f5052aed71e25f24120eb2e8813e60d6e489e9093c8f3da29b0c13e14`.

Every remaining author/dependency/output identity appears in the final
comparison seal, with its exact byte length and path.
