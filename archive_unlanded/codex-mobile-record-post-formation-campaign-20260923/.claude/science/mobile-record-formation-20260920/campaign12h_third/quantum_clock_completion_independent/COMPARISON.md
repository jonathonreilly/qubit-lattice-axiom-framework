# Quantum clock and coherent completion: bounded post-seal comparison

Date: 2026-09-22. This is selective scientific source review, not a publication,
retention, or formal audit determination. **No unresolved substantive finding or
source correction is identified within the requested scope.**

The independent reconstruction was completed before author-source access in
`REPORT.md`, SHA256
`5549bbd2f79d579521db0e49fa47a61525bed2945593a269fcaf71f1b4ab695d`,
and `PRE_COMPARISON_SEAL.json`, SHA256
`5e850f785c0f41eb34d75a30f84f86830963763b57cac1b6f6bcaa7466531395`.
Its six source and 21 artifact bindings still authenticate. This comparison is
new evidence; it does not replace or retroactively expand that blind work.

## 1. Exact author sources and read boundary

Author files are in the parent `campaign12h_third` directory. The authorized
12-artifact seal is `QUANTUM_CLOCK_AND_COHERENT_COMPLETION_AUTHOR_SEAL.json`,
SHA256 `7231481bd65aec211905948c3f30c0e55d4923ccf89bd281ef40c758d26d1195`.
All 12 bound files authenticate at their recorded lengths and SHA256 identities.
The complete source arguments and both complete runner implementations were read.
An initially truncated aggregate read of the coherent note was repaired with a
complete 221-line read before assessment. Every result field was read, including
the 48 clock rows, 111 observability rows, and exact/projector/gauge controls.
The stdout streams were parsed completely and matched against result fields;
both stderr streams are empty. Both execution receipts were inspected.

| Source | SHA256 |
| --- | --- |
| `TWO_VACANCY_QUANTUM_COMPLETION_CLOCK.md` | `5849e8066c34d3dd9a4291abbd0699a8a09fd82ce7cc0a861e54582ab1970126` |
| `quantum_last_pair_clock_screen.py` | `09762dd51fc97fa3396669ee0e34954e62bff902431ea534aea21c93e8c55a0c` |
| `QUANTUM_LAST_PAIR_CLOCK_SCREEN_RESULTS.json` | `b6876881e8965685aba82c7a7b95fb4181d29e6625ddf193538defac3ee6fd55` |
| `COHERENT_RING_FORMATION_WITHOUT_OCCUPATION_MONITORING.md` | `2d33882276f09cd118145441072af71d4fd6ca839d2be34ac8bb966cde40eaad` |
| `coherent_ring_contact_observability_check.py` | `cc355c2267976e57113f0e3516809961a91e00267bb6804e6ef9e6a3f096244c` |
| `COHERENT_RING_CONTACT_OBSERVABILITY_RESULTS.json` | `cd064c1bc487cc9590359c72f6bb2d2c980f4018a4ebe5da224c09759098e92e` |

The final seal records the complete identities, including logs and receipts.
No author runner was executed or imported. The contextual Sinkovicz reference
was not independently reviewed: no theorem from it is needed for the elementary
trace identity, and the author explicitly does not import one. The archived
author SymPy failure described in the clock note lies outside the authorized
12-file packet and was not opened or authenticated. Its repaired final source
and successful final output were inspected. Later CQ/cutoff, fresh-readout,
local RK-cooling sources, checkpoint, and registry remain unopened.

## 2. Clock theorem and normalization

Sections 1–5 of the clock note agree with the independently derived generator,
operator Poisson equation, dark space, and finite-dimensional singular limits.
The hole/record occupation convention causes no factor change because
`D[n]=D[I-n]`. For configurations differing by one allowed hop, the two affected
site projectors give total coherence decay **d**, not 2d. The stated effective
strong-monitoring jump rate `2 kappa^2/d` follows from this convention.

For a stable transient generator `L=A-{Gamma,.}/2` with unital A,
`L(I)=-Gamma`, hence tracing `-L^dagger F=I` gives `Tr(Gamma F)=D`.
The general identity requires stable absorption and unitality; the note states
both premises. Translation covariance then makes each localized adjacent
configuration's mean `(K-1)/(2 beta)` for d>0 and kappa!=0. It does not make the
mean of every coherent superposition supported on adjacent configurations equal
to that value, and the note does not claim this stronger statement.

The exhaustion of the unmonitored dark space is sound. In a translation sector
P, the relative hopping coefficient is `2 kappa cos(P/2)`; zero contact amplitude
successively kills all coefficients unless P=pi. The parity condition at the
opposite-pair orbit leaves

    r_K = K/2 - 2 + 1_(4 divides K).

Compression of each local hole number is `(2/K) P_D`, because translation acts
as the scalar -1 throughout this dark space and the total number of holes is
two. This justifies the compressed dephaser `-(2-4/K)` without assuming that
the uncompressed number operators preserve the dark space.

For fixed K, beta>0, kappa!=0, the zero eigenspace of the unmonitored operator
generator is exactly `rho -> P_D rho P_D`; its complementary block is stable.
The Schur-complement expansion therefore proves the weak-d coefficient. The
strong-d expansion uses two separate eliminations: first coherences, then
contact populations with fixed loss beta. The remaining classical Dirichlet
matrix is invertible because every noncontact configuration reaches contact.
These arguments establish the displayed operator limits, not merely agreement
of finitely many scalar means.

In particular the two uniform-mixture limits match the sealed reconstruction:

    lim_(d->0+) d E[tau] = r_K/[(K-1)(K-2)],
    lim_(d->infinity) E[tau]/d = (K-2)(K-3)/(48 kappa^2).

The complete six reported symbolic C4 quantities reduce exactly to the
independent rational formulas. As a separate reduction check, a newly assembled
full 4,356-unknown matrix-unit Poisson equation at K=12, d=0.3, beta=kappa=1
was solved without translation or reflection reduction. The mixed, adjacent,
and opposite means differ from the author row by at most `2.665e-14`.
The maximum full-entry residual is `2.448e-13`, the Hermiticity residual
`1.819e-13`, and the smallest numerical eigenvalue of the mean operator is
`2.37826891693`. These are floating-point checks, not interval certification.

The source correctly restricts all asymptotics to fixed K and excludes extra
H0. Its statements do not imply a size-uniform rate, an optimal monitoring
strength, or a joint limit in kappa, beta, d, and K. The independent additional
observation that the d=0 adjacent mean is `(D-r_K)/(beta K)`, rather than the
d>0 value, remains useful: the stability premise changes at d=0, so this
discontinuity does not contradict the author's sum rule. Likewise, a dark
state's existence does not by itself prove empty-start access to it.

## 3. Coherent contact observability and one-site monitoring

The all-size proof in sections 2–3 is the same boundary-amplitude mechanism
obtained before source access. Suppose amplitudes already vanish whenever the
minimum cyclic hole gap is at most r. At a configuration obtained by moving
one member of a gap-(r+1) pair inward, the diagonal potential multiplies zero.
Only the two outward predecessors can escape the known zero region. Their
coefficients are exactly `t_x` and `conjugate(t_y)`. Both are nonzero.

For h>=3, translating the chosen pair reaches the next fixed hole. The final
amplitude is zero, and backward propagation kills the starting amplitude.
For h=2, traversing the cycle instead gives
`psi=(-1)^K exp(2i Phi) psi`. The author assumes even K, so the sufficient
condition is precisely `exp(2i Phi)!=1`. Shorter antipodal translation orbits
still obey the K-step identity. At exceptional flux the note properly gives
no converse: nonuniform magnitudes or diagonal potentials can remove dark
states. Extra off-diagonal Hamiltonian terms are explicitly excluded from the
induction, and positive diagonal loss at every contact is an indispensable
premise. Positive contact diagonal entries of an otherwise arbitrary
off-diagonal loss operator would not suffice.

Absence of a contact-free H-invariant subspace places every eigenvalue of
`H-i Gamma/2` strictly in the lower half-plane. The finite no-birth semigroup
is therefore stable. Birth gains lower h by two, so the full transient
generator is triangular in hole sectors and has a finite-model exponential
bound, allowing a larger prefactor and a smaller exponent for Jordan blocks.
Off-diagonal coherences between count sectors do not supply a surviving
nonfull probability: the positive diagonal count blocks already decay, and
positivity bounds the cross blocks. No unique full internal state follows for
arbitrary initial data.

The one-site argument is also valid. A stationary nonfull positive density has
zero contact loss. The Hilbert-Schmidt identity forces commutation with the
monitored occupation projector, then with H. Its range is invariant under
both. In the block with a hole at the monitored site, the second hole is on a
path whose endpoint is a contact state; the tridiagonal recurrence excludes
an eigenvector vanishing there. In the other block, two holes move on the
remaining path. The gap induction terminates at the open boundary because
the second outward predecessor is absent. Compression is legitimate since
the candidate range is invariant under both H and the projector. The argument
uses the hole projector; its complement is the physical record occupation
projector and has exactly the same invariant subspaces and dephaser.

A separate exact seven-vertex path control used six unequal complex hoppings
and a non-additive diagonal potential. Over Q(i), the contact-observability
ranks on its 15-dimensional noncontact subspace were `5,9,12,14,15` as powers
0 through 4 were added. This controls the open-path step without substituting
finite ranks for the amplitude induction. The original independent packet
already contains all-size arguments, exceptional-flux countercontrols, and
separate exact one-monitor cases.

## 4. Physical gauge sectors and formation-count coherence

The physical application uses the specified charge-complement symmetry.
Choosing representatives with electric bit b_0=0 gives one extra sign on the
edge-zero hop in the T=-1 sector. Thus the total phases differ by pi while
`exp(2i Phi)` is the same. No additional fermionic exchange sign is required:
this is a direct change of basis among hard-core physical bit words.

An independent exact K=6, two-hole calculation was added after source access.
It uses edge amplitudes `(1+i,2,3,4,5,6)`, nonuniform contact losses, and an H0
that is `f(A) I + g(A) T` within every occupation fiber. The full 30-dimensional
physical Hamiltonian commutes with T. Both 15-dimensional compressions equal
the claimed hard-core Hamiltonians, including diagonal energies `f+g` and
`f-g`, and their loss matrices agree exactly. Their hopping products are
`720(1+i)` and `-720(1+i)`, respectively, giving `exp(2i Phi)=i` in both.

This confirms that an allowed H0 need not be simply proportional to identity
on the two-dimensional physical fiber: commutation with occupations and T is
enough to make it a real scalar potential separately in each T sector.
The positive stationary-state/count argument then handles coherence between
the sectors; one cannot hide a nonfull positive density entirely in a cross
block with zero positive diagonal blocks.

For the real common-chi coarse birth map, T covariance and the previously
checked count-weighted identity yield the stated terminal empty-cat density
`(I+chi^(K/2) T)/2`. One-site occupation monitoring commutes with T and retains
this conclusion. The source uses the specified hopping/H0/birth model, with
the indicated occupation monitor if present; it does not reintroduce the
previously refuted arbitrary-extra-N,T-commuting-jump completion claim. The
supplied empty cat, common real chi, T symmetry, and completed occupation are
essential. The conclusion neither generates coherence from an incoherent
vacant mixture nor establishes a unique stationary state for arbitrary inputs.

## 5. Runner/evidence comparison and preserved failure

The clock runner's translation representative, Hamiltonian signs, monitoring
diagonal, contact loss, and reconstruction match its Poisson equation. Its
48 declared grid rows and 24 full-matrix checks are present. The maximum
recorded reduced residual is `6.359357485052897e-13`, consistent with the prose.
Larger reduced rows are appropriately described as exploratory floating-point
calculations. No finite-screen optimization or thermodynamic scaling conclusion
is smuggled into the theorem.

The contact runner implements row observability after eliminating contact
basis rows, closing the remaining span under the compressed H and, where
requested, the diagonal monitor. Full rank modulo the verified prime 65537,
with i mapped to 256, does certify full rank over Q(i): a zero Gaussian-integer
minor would remain zero under this ring homomorphism. The finite-field
row reductions only compute that rank. Rank deficits are not lower bounds on
the characteristic-zero nullity; the author separately supplies exact rational
dark projectors and their dimensions, so the claimed deficient cases are
supported. This reasoning does not turn 111 finite cases into an all-size
theorem; the independent amplitude proof supplies that step.

All 111 rows have the declared dimensions and contact/free counts, expected
deficits or full-rank status, and the declared grouping. The result contains
nine positive-even-hole T-sector checks at K=4,6,8 and six exact dark-projector
checks at K=4,...,14. The h=0 terminal sector is trivial and is not one of those
nine executed rows. No full author-suite rerun was needed. Receipt and stream
authentication is evidence provenance, not independent mathematical evidence.

The new comparison checker initially stopped on a SymPy domain-conversion
exception: the unexpanded Gaussian expression `-3*i*(2+i)` was rejected by
conversion to Q(i). The original script, complete traceback, empty stdout,
receipt, and diagnosis are preserved under
`failed_attempts/comparison_gaussian_conversion/`. The sole repair expands
matrix entries before the same exact conversion/rank calculation. Inputs,
field, target rank, and other checks are unchanged. The final run passes with
empty stderr. The earlier blind packet's separate numerical-conditioning
failure and resolution remain untouched.

Reproduce the bounded post-seal controls with:

    python3 comparison_check.py

The script authenticates the original independent and author seals, checks
result/receipt/stream consistency, compares C4 formulas exactly, solves one
unreduced Poisson problem, and assembles the two new exact finite controls.
It does not import or execute author code. Full outputs and the execution
receipt accompany this report; `FINAL_SEAL.json` binds the original packet,
authorized author sources, new controls, and preserved failed attempt.

No primary source was edited. No further mathematical claim, native physical
implementation, phase theorem, publication disposition, or audit status is
assigned by this comparison.
