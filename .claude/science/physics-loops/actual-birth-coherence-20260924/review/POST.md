# Released-source POST: actual birth coherence and finite energy range

This is a bounded scientific source comparison, not an audit verdict. The
released Fisher candidate agrees with the sealed independent PRE in its stated
finite-apparatus scope. The new frequency-support argument and restricted swap
also hold under their stated assumptions. I found no material mathematical
defect requiring repair. The scope qualifications below are part of this result.

## 1. Sources, isolation, and what is new in POST

The unchanged blind reconstruction is `PRE.md`, SHA256
`77e330c478ef2290bfdc96382bc95524f8e9444bf22e2f29f77f8f2b231f0ac7`, bound by
`PRE_SEAL.json`, SHA256
`df11a67f0f37956e98c407a5b50de3e670b939cf2274d2d798c27cc91e98fdc2`.
Its 15 members are preserved. That PRE independently established the
success-weighted Fisher requirement, the input coherence correction, the
growing-H trace-error scale, an exact whole-system swap with bounded mean,
and the band-pinched approximate swap.

The released root sources are:

| Source | SHA256 |
| --- | --- |
| `ACTUAL_BIRTH_COHERENCE_PERSONAL_DERIVATION.md` | `00d01629c212cadb4b0acd6eb7ab1e4ae072a036c2f76061c620be87766f85e7` |
| `AUTHOR_SEAL.json` | `a99e6455194cf13a41ffeec1af1d7c65707a36574c341443daa381c0d7b094bb` |
| `FREQUENCY_RANGE_AND_ONE_INPUT_RELAXATION.md` | `e1e6edaa76b0fe3c952ff92f274ca6678283d203fd9c5bd828fb84a4e9d79349` |
| `RANGE_SUPPLEMENT_SEAL.json` | `9fcccc3397f456048b7f072f8a809b7a99d9557edd12b7e5509dfebb601f2671` |

All 14 released files, including both seals and their complete source/evidence
members, were hash-verified and copied under `POST_sources/` before comparison.
The complete candidate, supplement, both author program versions, both complete
result JSONs, both complete stdout streams, both stderr files, and source
records were examined. Full stdout parsing established exact agreement with
the result JSON and the three separately printed cube rows in each run. The
source record and comparison results are retained separately in this directory.

The three model sources remain the PRE's pinned actual-fast-time,
bounded-compensation, and local-compensation notes. Their theorem imports remain
conditional and unaudited. The finite Fisher identities are supported by the
previously checked formula and basic-properties paragraph of Marvian
arXiv:2112.04694v1 and by the direct finite derivation below. The root's Tajima,
Shiraishi, and Saito reference is contextual; I did not inspect or import a
theorem from that additional paper.

The frequency-support lower bound and restriction of the swap to the first two
output clusters are new released-source POST implications. They are not claimed
as blind PRE results. The range supplement was written before root read PRE but
sealed afterward; this POST asserts no stronger isolation for that supplement.
No unreleased no-go packet, extra root range controls, autonomous-process packet,
root checkpoint, or unrelated publication source was read. No author or campaign
builder was imported or executed in this POST.

## 2. Precise operational and limiting premises

At every finite integer spin S, the supplied lambda=0 compensated cube and its
exact canonical low spectral isometry define

    epsilon^2 S(S+1)=delta/K,
    psi=U_epsilon Omega,
    omega_i=p_i |phi_i><phi_i|,
    p_i=alpha^2 ||j_i psi||^2,
    phi_i=j_i psi/||j_i psi||.

Delta, K, and the admissible positive alpha are fixed. The apparatus may depend
on epsilon but is finite-dimensional at each member of the sequence. Its
initial state is independent of psi, arbitrary mixed, and includes every
nonstationary reference. The global realization exactly commutes with the
stated additive system-plus-apparatus Hamiltonian. Outcome flags have zero
Hamiltonian, their readout is covariant, and inaccessible degrees are discarded.
An arbitrary final apparatus and arbitrary other outcomes are allowed.

Only the selected subnormalized output on this one input is required. The
comparison norm is the unhalved trace norm, including the success probability.
No strength-to-continuum-time identification, uniform approximation on all
inputs, spatial locality, fixed apparatus bandwidth, charge conservation beyond
what was stated, catalyst return, or apparatus preparation mechanism is assumed.
Conservation of a different interacting total energy would not imply these
premises. The results below do not supply that alternative accounting.

For all limits, epsilon tends to zero along the specified joint spin sequence.
Every finite spectral decomposition, covariance identity, and Fisher identity
is established first at finite S. The author controls at fixed S=1 are not this
limit. The root candidate deliberately restricts to finite apparatus; the PRE's
separate arbitrary-apparatus fidelity statement is not silently added to it.

## 3. Fisher candidate: derivation and comparison

For a finite state rho and dotrho=-i[H,rho], completing the SLD square gives

    F(rho,dotrho)=sup_(X=X*) {2 Tr(dotrho X)-Tr(rho X^2)}.

The root's formula is correctly normalized: pure states have F=4 Var(H).
For a CPTP map, the dual map is unital completely positive, so Kadison's
inequality bounds the output variational expression by the input supremum.
For a covariant map, the mapped derivative is the output energy derivative.
Product SLD additivity and the zero-energy orthogonal-flag decomposition give

    F_H(psi)+F_HR(sigma_R) >= sum_k p_k F_H(rho_k).

This rotates both initial system and apparatus. It does not assert covariance
of the desired j_i map on the system with a fixed apparatus state. In particular,
the exact selected pure target implies

    F_HR(sigma_R) >= 4 p_i Var_H(phi_i)-F_H(psi).

The input correction is essential. From the exact canonical low block,

    U*HU|_P=delta epsilon^-2 D/C+delta H4_S+O(epsilon^2),
    D Omega=0,

one has ||H psi||=O(1), hence F_H(psi)=O(1). The input is not claimed to be an
energy eigenstate. My PRE additionally reconstructed its leading value
192 delta^2, but that stronger coefficient is not needed by the root proof.

For the three original marks, the supplied actual-birth expansions give

    (b_i,r_i)=(2,4),(2,2),(4,6),
    p_i=alpha^2 b_i epsilon^2+O(epsilon^4),
    ||P_1 phi_i||=epsilon sqrt(r_i/b_i)+O(epsilon^3),
    ||P_0 phi_i||=1+O(epsilon^2),
    ||P_2 phi_i||=O(epsilon^2).

These are Hermitian exact spectral clusters of the original selected output;
no extra physical energy measurement is inserted. The first high cluster is
delta epsilon^-4 I+O(epsilon^-2); the low-cluster operator norm is
O(epsilon^-2). Thus the coefficient in the proposed QFI bound is correctly
probability weighted. Omitting p_i would give an incorrect epsilon^-6 apparatus
requirement.

The phase witness is valid even though its vectors need not be energy
eigenvectors. Set x=P_0 phi_i=l a and y=P_1 phi_i=u b with a,b normalized, and
A=i(|b><a|-|a><b|). As the projectors reduce H, the remaining component of
phi_i is orthogonal to H a and H b. Within each cluster the component of H a
orthogonal to a has zero overlap with x, and the analogous statement holds
for b and y. Consequently

    d=|Tr(omega_i i[H,A])|
      =2 p_i l u |<b,Hb>-<a,Ha>|,
    v=Tr(omega_i A^2)=p_i(l^2+u^2).

The displayed root equalities do not discard an internal-cluster contribution.
The scale estimates are

    d=2 alpha^2 delta sqrt(b_i r_i) epsilon^-1[1+O(epsilon^2)],
    v=alpha^2 b_i epsilon^2[1+O(epsilon^2)].

For ||sigma_i-omega_i||_1<=eta, choose any centering of H with
h_epsilon=||H-c I||=O(epsilon^-4) on the entire allowed finite output space.
Trace duality gives an error at most 2 h_epsilon eta in the derivative witness
and at most eta in its squared-observable expectation. Extending A by zero
on every other flag and optimizing the variational expression over t A yields
the exact finite inequality

    F_HR(sigma_R) >= [d-2 h_epsilon eta]_+^2/(v+eta)-F_H(psi).

The denominator is positive for the small-epsilon target under consideration.
An approximate output outside the original charge sector causes no problem
provided h_epsilon covers its full allowed space, as specified. Taking
eta=o(epsilon^3) makes the derivative correction o(epsilon^-1) and the
denominator correction o(epsilon^2). Therefore

    liminf epsilon^4 F_HR(sigma_R) >= 4 alpha^2 delta^2 r_i.

This reproduces coefficients 16,8,24 times alpha^2 delta^2. My PRE used a
commutator trace-norm witness instead; the different finite inequalities have
the same load-bearing leading coefficient and sufficient error scale.

The band-pinched comparison also has the stated behavior. Removing the low /
first-high cross block changes the selected state by
2 alpha^2 sqrt(b_i r_i) epsilon^3+O(epsilon^4), and terms involving P_2 only
affect the remainder. Subtracting each band's scalar energy center bounds
its weighted Fisher information by O(1). The root correctly labels this part
as an output-state comparison rather than a constructed covariant apparatus.
The already sealed PRE supplies the latter via an independent copy-and-swap
construction, so the weaker approximation can in fact avoid divergent Fisher
cost in this broad one-input realization class.

Unspecified O(epsilon^3) tolerance must not be read as saying every fixed
positive coefficient destroys every lower bound: the finite inequality keeps
that coefficient. Nor does a high classical variance provide energetic
coherence. The root's F<=4 Var and, when 0<=H_R<=Lambda_R,
Var<=Lambda_R <H_R>, are valid but do not imply a divergent mean without further
spectral information. Section 6 of the root candidate correctly avoids using
fixed alpha as a finite time step of the continuous generator.

## 4. New frequency-support result

The finite frequency lemma is correct without periodicity or integer spectra.
For any input operator X, write X_nu using its exact energy projectors. The
covariance equation states that E(X_nu) transforms with the same phase
exp(-it nu). Decomposing the output into its finitely many frequencies and
using linear independence of these exponentials shows that all output
components at other frequencies vanish. The Cesaro-average proof in the
supplement is an equivalent finite argument. The map can kill a frequency;
it cannot generate one absent from the input.

For independent inputs, frequency support of rho tensor sigma_R lies in the
Minkowski sum of their supports. If rho is supported in an energy interval
of width B_in and B_R is the maximum absolute apparatus frequency with a
nonzero density-matrix block, all initial frequencies lie in
[-B_in-B_R,B_in+B_R]. The joint conserving realization, partial trace, and
zero-energy flag selection are covariant maps. Therefore a selected output
has no P_1/P_0 block when the ordered gap G_epsilon exceeds B_in+B_R.

The actual input lies exactly in the N=4 low spectral cluster, whose width is
O(epsilon^-2) by the bounded canonical block. Small energy variance alone
would not have supplied this exact support conclusion; the exact spectral
isometry is being used. The actual ordered output gap is

    G_epsilon=delta epsilon^-4+O(epsilon^-2).

With Q=|a><b|+|b><a|, ||Q||=1, a vanishing P_1 sigma_i P_0 gives
Tr(Q sigma_i)=0 whereas Tr(Q omega_i)=2 p_i l u. Hence

    ||sigma_i-omega_i||_1 >= 2 p_i l u
      =2 alpha^2 sqrt(b_i r_i) epsilon^3[1+O(epsilon^2)].

If eta=o(epsilon^3), failure of B_R>=G_epsilon-B_in along any subsequence
contradicts this inequality there. It follows that eventually
B_R>=G_epsilon-B_in and

    liminf epsilon^4 B_R >= delta,
    liminf epsilon^4 diam(spec H_R) >= delta.

This sharpens the range scale obtainable from the Fisher/variance inequality
alone. Its premise is exact conservation; an approximate-conservation variant
would require an additional estimate. A sufficiently large bandwidth is still
only necessary: exact resonances and amplitudes matter. A diagonal population
at a remote energy has zero energetic coherence at that gap. The width B_in
cannot be omitted, even if the apparatus is stationary.

## 5. Restricted swap, ground-relative mean, and sharp scope

The supplement's construction resolves the second-high-band issue by
approximation explicitly. The invariant subspace D consists of the exact N=4
low cluster and the exact N=6 low and first-high clusters. For

    phi_01=(P_0 phi_i+P_1 phi_i)/sqrt(l^2+u^2),

the pure-state trace-distance identity gives exactly

    ||p_i |phi_01><phi_01|-omega_i||_1
        =2 p_i ||P_2 phi_i||=O(epsilon^4)=o(epsilon^3).

It preserves p_i. This is an approximation to the original output, not a
redefinition of the original formation mark. The three N=6 clusters exhaust
the sector in the supplied source. No assertion that P_2 phi_i vanishes is
used or needed.

The swap is a global unitary, not just an isometry on the specified input.
Adjoin a blank zero-energy flag F_S to the system, and a resource copy of
D tensor F_R. On (D tensor F_S) tensor (D tensor F_R), swap these two equal
factors. On (D-perp tensor F_S) tensor (D tensor F_R), act as identity. Both
blocks are invariant under the additive energy, are mutually orthogonal, and
the swap maps its block onto itself. The two restrictions are unitaries.

Let E_min=min spec(H|D). The resource Hamiltonian is
(H|D-E_min I) tensor I_F. Before and after the swap, the two D energies add
to E_s+E_r-E_min. Therefore the unitary commutes with the additive energy on
the whole space, including the complement. The scalar shift costs no hidden
phase reference. With the resource prepared as

    p_i |phi_01><phi_01| tensor |1><1|
      +(1-p_i)|e_min><e_min| tensor |0><0|,

the accessible output on psi tensor blank flag is exactly that mixture,
while the apparatus holds the old input and blank flag. The initial resource
preparation is supplied; no mechanism for preparing it is claimed.

In either included low sector, the exact canonical Hamiltonian is
delta epsilon^-2 D_S/C+delta H4_S+O(epsilon^2), with D_S nonnegative and H4_S
uniformly bounded. Both low lower edges are therefore at least -O(1), and
the first high cluster is positive for small epsilon. The zero-field input
provides an O(1) Rayleigh quotient, so E_min=O(1). This establishes a bounded
ground edge, without assuming microscopic nonnegativity.

The retained high probability in phi_01 is epsilon^2 r_i/b_i+O(epsilon^4).
Its energy is delta epsilon^-4+O(epsilon^-2), while the normalized low vector
has energy-vector norm O(1). Its leading second moment is consequently
delta^2 (r_i/b_i) epsilon^-6, and its squared mean is only O(epsilon^-4).
Using the stationary failure flag gives

    F_HR(sigma_R)=4 p_i Var_H(phi_01),
    epsilon^4 F_HR(sigma_R) -> 4 alpha^2 delta^2 r_i.

The resource spectrum includes no second high cluster. Its diameter is
delta epsilon^-4+O(epsilon^-2); in conjunction with the necessary range
inequality, this attains the leading coefficient delta. Its coherence
bandwidth has the same leading coefficient because the retained low/high
coherence is nonzero, and is bounded above by that diameter.

The failure state is at the resource's true ground, so the mean above that
ground is p_i(<H>_phi01-E_min), not the unweighted conditional mean. Hence

    Tr(H_R sigma_R)=alpha^2 delta r_i+O(epsilon^2).

The O(1) ground shift contributes only O(epsilon^2) to this expression because
it is paid on the success branch; the failure branch has zero shifted energy.
The stated limiting constant is correct. Thus the same construction jointly
attains the necessary leading Fisher and energy-range coefficients for the
one-input approximation class eta=o(epsilon^3), while its ground-relative
mean stays bounded. The actual exhibited error is O(epsilon^4).

This does not assert optimal range for exact target matching. Preloading full
phi_i may require additional spectral range because it includes P_2; the
present sources do not determine the optimal exact range. They also do not
imply that an arbitrary prescribed tolerance smaller than the construction's
O(epsilon^4) error is met by this truncated swap. The asymptotic sharpness is
for the class eta=o(epsilon^3), which contains the displayed error sequence.
On different system inputs in D, the swap prepares the same resource state,
so it generally fails to implement alpha^2 j_i(.)j_i* on those inputs. No
uniform channel, continuing apparatus, or continuous-process sufficiency is
proved. These restrictions are correctly present in the released sources.

## 6. Evidence correspondence and fresh checks

The author's `coherence_controls.py` explicitly imports the previously pinned
ordinary-energy builder with hash
`4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d`.
Those reused matrices are author corroboration. I read the code and complete
outputs; I did not rerun, import, or represent them as independent evidence.
The two-level author test checks the phase witness, a noise case, the trace
pinching scale, and stationary high-variance Fisher zero. Its random unitary
commutes with the energy blocks, and its partial trace and flag dephasing
correctly test Fisher monotonicity. The cube rows compute the actual canonical
input and original mark outputs at S=1. At epsilon=.03 their scaled Fisher
coefficients are .1608400, .0804925, .2413681 against .16,.08,.24, and input
Fisher is 196.6576. This supports finite coefficient consistency only.

The archived first run is not a failed scientific check. Its stderr contains
two SciPy future warnings about integer diagonal input dtype. The final source
adds `dtype=float` to the two diagonal constructors and has empty stderr.
All scientific numerical fields in the two runs agree; only elapsed times
and source hashes differ. The source snapshots and complete logs preserve
both versions. No unreleased supplement control is credited.

The fresh `post_coherence_checks.py` imports only the standard library and
NumPy. It completed successfully with full stdout, empty stderr, a result JSON,
and a source-bound execution record. Its meaningful controls are:

- A five-level phase witness with non-eigenvectors in both chosen clusters.
  The derivative formula agrees to about 2e-16; noisy cases, including changed
  success probability, obey the finite robust bound.
- A 24-dimensional exactly energy-blocked unitary with energy labels
  a+b sqrt(2), a coherent bounded-frequency input, a mixed apparatus, and a
  zero-energy flag. All forbidden output-frequency matrix entries are exactly
  zero in the computation, even while a high-energy output population is
  nonzero. Trace duality gives the prescribed missing-cross-block error, and
  pinching the toy target saturates it. Separate explicit examples reject
  dropping initial system frequencies and treating bandwidth as sufficient
  despite absent resonances.
- A 96-dimensional restricted-swap unitary with two flags, a nontrivial system
  complement, a second high component in the target, and a ground-shifted
  resource. It is exactly unitary and its global additive-energy commutator
  is zero. It produces the truncated selected output with the original
  probability, satisfies the exact projection trace-error formula, acts as
  identity on the complement, and obeys the exact resource Fisher and
  ground-relative mean formulas. At epsilon=.0625 its scaled Fisher is
  2.2559306 toward 2.25, scaled diameter 1.5078583 toward delta=1.5, and mean
  .3774663 toward .375. These toy values are not cube coefficients.

These are independent finite consistency controls after source release, not
an independent reproduction of the author's microscopic matrix computation,
nor interval certification or a numerical proof of uniform spin asymptotics.
The cube coefficient reconstruction remains the primitive-word work sealed
in PRE; the uniform cluster estimates remain conditional model imports.

## 7. Corrections and open boundaries

No scientific correction to the released proof is required by this POST.
Frozen statements that sealing or independent checking is pending are historical
status text; any later publication should report the actual evidence stage
without changing their mathematical scope. No formal retained status follows
from this comparison.

The finite apparatus, independent input, complete resource accounting, exact
additive conservation, covariant zero-energy readout, fixed admissible alpha,
and unhalved unconditional eta=o(epsilon^3) assumptions must remain explicit.
So must the distinction between exact target preparation and the O(epsilon^4)
one-input range construction, energetic coherence and classical variance,
spectral range and mean energy, and one-output preparation and a whole
instrument or continuum process. No infinite-apparatus range theorem,
approximate-conservation theorem, exact-range optimum, physical resource
selection, or autonomous realization is supplied here.

All new work is confined to the independent directory. PRE and its source
snapshots are unchanged. No publication, research source, audit file, axiom,
or editable prompt file was modified.
