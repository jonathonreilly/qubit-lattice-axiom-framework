# Review of the two fixed dark-source stationary scattering witnesses

**Finding:** both fixed stationary claims are supported under their stated
conditional Hamiltonians. I found no material defect in the channel closure,
boundary signs, common phase, positive two-body realization or exact-residual
argument. An independently assembled full-basis certificate reproduces both
strict error ceilings. This supports conditional stationary-channel reuse;
it does not establish a normalizable-input autonomous operation, the original
all-site strength cap, a wavepacket theorem, or retained audit status.

The original witness satisfies `||R(k0)-alpha W|| < 5.2e-13`. The later witness
satisfies `<1.76e-13` and the added incident cap two on both old sites. Its
source and clock-contact sites still exceed two. Both witnesses use one
clock momentum and two old-dependent total energies, not a four-channel
scattering matrix at one common total energy. The four amplitudes form a
well-defined old operator at fixed clock momentum; this distinction is
explicit in the later source and does not invalidate the comparison.

There is one non-blocking evidence-label defect. The author function
`compact(q)` writes `upper_float=float(q)` in
[certify_point.py](sources/author/certify_point.py), line 28, and
[certify_old_cap.py](sources/old_cap/certify_old_cap.py), line 29. This is
round-to-nearest, not outward rounding. In particular the old-cap target's
stored float is below its exact rational value. All decisive author gates
use the rational strings and exact `Fraction` comparisons, so neither strict
ceiling is compromised. Treat these float fields as approximate displays;
future numerical consumers must use the rational field or an outward-rounded
bound. The reviewer outputs name their displays `approximate_float`.

## Scope and exact reviewed identities

The original complete [ROUTE](sources/author/ROUTE.md), both original verifier
programs, their actual input/result/receipt files, and the complete later
[RESULT](sources/old_cap/RESULT.md) and verifier delta were read. The original
author's different-path program was source-exposed. Its label is not treated
as independent reviewer acceptance. The fixed coefficients were transcribed
from each note into reviewer code and checked exactly against the saved
parameter maps; no optimizer was rerun or trusted as a certificate.

| Frozen source | SHA256 |
|---|---|
| Original ROUTE.md | `04ffdf68d3bdadf17f5c0838dde2a8a2bd1608d786ea58e427c5c25fd33ef8d1` |
| Original certify_point.py | `74460bcbd0db30671a6d676b79d24d1ebb5439523df62a5fa3c231760b010558` |
| Original independent_check.py | `06e14d43a2f0b9f09c594dd547981d5e25002997e6df661d542221c400632d0d` |
| Original rational_point_certificate.json | `c4c8c4bd27054497edd87b8fe5deda86bf221e5e95ac395a13aca9b5e879d971` |
| Old-cap RESULT.md | `397c18e02c0d583bdc3e51df8f5c513f677b448862526a362eac4cc43577af00` |
| Old-cap certify_old_cap.py | `acbf5b37b2705a6a2b47ab23a48d92ca4cfb7be2f5bb4993fa4d04e94418b636` |
| Old-cap check_old_cap.py | `f4bb2cf596615b8aea97ea71aa7fb2f6a3024c7af7945d80b340b2711c231b5c` |
| Old-cap rational_point_certificate.json | `6f057d8a580217d29a09d7683462f5b35b71de093e75c8d07a12283cde33593f` |

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) and
[OLD_CAP_SOURCE_MANIFEST.json](OLD_CAP_SOURCE_MANIFEST.json) bind the complete
review inputs. Root initially named `FINAL_MANIFEST.json` for the old-cap
variant; that path was absent. Root corrected the pointer to the actual
`FILE_MANIFEST.json`, whose listed source identities were checked before
freezing. This was a handoff naming correction, not a scientific discrepancy.

The scientific source revision is `c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc`.
Methodology authority is the supplied current-main snapshot
`5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2`. Its reviewer skill, freshness rule
and proof-search governance were read from the already captured exact files.
The user's selected model and effort were preserved. This is a same-model,
source-exposed analytical and computational review, with independently written
assembly and square-root proposal machinery. It is not blind discovery,
model diversity, formal verification, a formal audit or laboratory evidence.
My earlier seven-stage rail derivation and the root reflection construction
are not premises here. The separate generic packet bridge was not inspected
or imported.

## Complete asymptotic channels and the literal old Hamiltonian

In physical order `(old1,old2,A,B)`, the source vacuum is exactly invariant
under `B=K+C+G`, and `B(psi tensor |00>)=K psi tensor |00>`. Every term in
`C+G` annihilates that vacuum, including the source hopping. Source excitation
number is preserved by the bulk. Hence the vacuum and its orthogonal
complement Q are reducing subspaces. Since `K>=I`, and all the other displayed
blocks are positive,

    Q B Q >= [1+min(DeltaA,DeltaB)] Q.

This statement does not require K to commute with the occupied-source old
couplings. During collision `[H,K]` can be nonzero. It is the asymptotic
channel structure, not a conserved old Hamiltonian during collision, that
ensures elastic old-energy output at these incoming energies.

| Exact resource or closure quantity | Original witness | Old-cap witness |
|---|---:|---:|
| Clock bandwidth `4J` | `1.555612607490684` | `0.120084428428128` |
| Other-vacuum-band separation `2-4J` | `0.444387392509316` | `1.879915571571872` |
| Source-band margin `min(Delta)-2-4J` | `>1.11106871217564` | `0.066742080468886` |
| Common physical scalar `nu=-mu1` | `0.151066135275764` | `1.459892813020969` |

The source margin compares the source threshold against the top of the upper
vacuum band, `3+4J`; it pays the entire old-energy release of two. Both vacuum
bands are disjoint and lie below every source-excited band. Each interior
momentum therefore has one open vacuum channel per parity p and old energy s.
At fixed total energy there are two parity channels; the exact `X1X2`
symmetry prevents mixing between them. No source channel is omitted because
it happens to have small numerical weight.

The full physical basis was assembled independently by bit operations in the
reviewer calculation. It checks the dark vacuum and `X1X2` commutator exactly.
The source-excited subspace used for certification has dimension twelve and
contains both parity sectors together. The two boundary systems have dimension
32 with two open-channel right-hand sides each.

The original eight-dimensional parity reduction is correct. In the normalized
joint old basis, `ZZ=Z`, `X1=X`, `X2=pX`. The one-source-excitation block is

    [[aA I+Z+gA X, -h I], [-h I, aB I+Z+p gB X]].

For `xA=lambda-aA` and `xB=lambda-aB`, its determinant is the determinant of
`(xA I-Z-gA X)(xB I-Z-p gB X)-h^2 I`. The coefficients of I, Z, X and iY are
respectively `xA*xB+1+p*gA*gB-h^2`, `-(xA+xB)`,
`-(gA*xB+p*gB*xA)` and `p*gB-gA`. Taking the two-dimensional determinant
gives exactly the displayed quartic, including the positive final square.
The source-double-excitation block has the stated two eigenvalues
`2+DeltaA+DeltaB+2h+u+gA+gB +/- sqrt(1+(gA+p*gB)^2)`.
Together with vacuum energies 1 and 3, this accounts for all eight states
per parity. The rounded spectral lists are unnecessary for the closure proof.

## Boundary signs, scalar and exact unit modulus

For a bulk eigenvector with energy b, the recurrence is

    (E-b-2J)x_n + J x_(n-1) + J x_(n+1) = 0.

Let `T(E)` multiply the open mode by `z=exp(ik)` and each closed mode by its
real decaying root r. At reference site one, the lead is an incoming wave
`z^(-(n-1))e`, an outgoing wave and closed evanescent terms. Thus

    x2 = T x1 + (z^-1-z)e,
    E-B-2J+J T = F,
    J x0 + (F-VB)x1 = 2iJ sin(k)e.

At site zero the equation is
`(E-B-2J-VA)x0+J x1=0`. These are precisely the source M and right-hand side.
For a closed mode `F=-J/r=-(D+sign(D)*sqrt(D^2-4J^2))/2`; for the open mode
`F=-J/z`. The sign change in the other old-vacuum closed channel for an upper
old input is therefore required and is handled correctly. The measured
reflection amplitude is `<e,x1>-1`.

As an independent convention test, the reviewer code sets the contacts to zero
in the scalar free half-line problem and verifies exactly, using rational
complex arithmetic, `r=-z^4` at reference site one. This also follows from the
Dirichlet condition at site minus one. Reversing the injection sign fails
that identity. The author finite-lead comparison's translation factor
`z^[-2(L-2)]` is likewise correct: the incident and reflected amplitudes each
acquire their own propagation factor between the end site and site one.

The conserved discrete current may be written
`2J Im(<x_n,x_(n+1)>)`. It vanishes at the endpoint; each closed real-root
channel carries zero current. In the open channel its value is
`2J sin(k)(|r|^2-1)`. The certified matrix inverses give unique boundary
solutions, and `sin(k)>0`, so `|r|=1` exactly at each certified point. No
small numerical modulus defect is promoted to exact unitarity. The open
clock speed has equal magnitude on incoming and outgoing waves and is the
same for both old-energy bands at common k, so no omitted velocity ratio
changes the four-amplitude old operator.

The positive vacancy block is `nu(I-n_c1)=nu I+mu1 n_c1`.
Consequently `H_physical=H_signed+nu I` on the complete Hilbert space.
Both the physical total energies and bulk thresholds shift by nu; their
differences and reflection amplitudes are unchanged. Physical evolution
retains `exp(-i nu tau)`. The source explicitly accounts for this factor;
it is not an independently adjustable old-energy phase.

Finally W has eigenvalues `(-7+24i)/25` at p=+1 and one at p=-1. The same
exact amplitude `alpha=r_(-1,-1)` is used for every s and p. There is no
separate phase fit for the two old energies. The old operator difference is
diagonal in the common `(ZZ,XX)` basis, so its norm is the maximum scalar
difference; tensoring a passive reference leaves that norm unchanged. This
is a stationary asymptotic-channel norm, not a full prepared-clock isometry.

## Exact error certificate and independent reconstruction

The author certificate's inequalities are valid. If `D>=d I`, `d>2J`, then
`A=D^2-4J^2 I` is positive and its positive square root S obeys
`S>=(d-2J)I`. For a symmetric rational proposal `S_hat`,

    S_hat >= [d-||S_hat-D||_infinity] I = b I.

The checked b is positive. Put `a=d-2J`. For `X=S_hat-S`, the exact identity
`S_hat X+X S=S_hat^2-A` gives

    ||X||_2 <= ||S_hat^2-A||_2/(a+b)
             <= ||S_hat^2-A||_infinity/(a+b).

The first inequality follows by integrating
`exp(-t S_hat)(S_hat^2-A)exp(-t S)` from zero to infinity. Symmetry of the
residual justifies the second. For the author's six-dimensional block,
the F error is at most `(sqrt(6)/2)||X||_2 < (3/2)||X||_2` in infinity norm.
The other closed-vacuum square root uses the elementary difference-of-squares
residual bound with the proper sign of D. The fixed scalar proposals are
positive. The reviewer uses an exact integer-square-root interval for that
scalar, so this positivity is not inherited from a floating sign assumption.

For the rational matrix `M_hat` and rational inverse proposal N,
`gamma=||I-M_hat N||_infinity<1` implies

    ||M_hat^-1||_infinity <= ||N||_infinity/(1-gamma) = L.

This is a right-inverse certificate for a square finite matrix and is valid.
The author `abs(real)+abs(imag)` row sums upper-bound the ordinary complex
matrix infinity norm. If `||M-M_hat||_infinity<=delta` and `L delta<1`,

    ||M^-1||_infinity <= L/(1-L delta),
    ||x-x_hat||_infinity <= [L/(1-L delta)]
       (||M_hat x_hat-b_rhs||_infinity + delta ||x_hat||_infinity).

These quantities are calculated and compared as exact fractions. Mpmath
proposes a witness; its reported precision is not used as an error guarantee.
The alpha uncertainty is included in every scalar target comparison, and
`|w_p|=1` gives its coefficient one. The l1 sum of real and imaginary
comparison residuals safely bounds their complex absolute value.

[reviewer_certificate.py](reviewer_certificate.py) independently constructs
the full physical matrix without a parity reduction or importing author code.
It uses twelve Newton iterations at 90 decimal digits to propose the
twelve-dimensional square root, then rationally rounds at denominator
`10^60`. Exact residuals and the same independently checked Sylvester lemma
certify it. Here `sqrt(12)/2<2` is used for the matrix-norm conversion. Each
full 32-dimensional boundary inverse and two-column state solution is checked
by exact residuals. A conservative factor two converts the resulting
two-channel matrix error to a parity-amplitude error. No numerical
eigendecomposition is used by this reconstruction.

The coefficient-only delta is recorded in
[OLD_CAP_CHECKER_DELTA.diff](OLD_CAP_CHECKER_DELTA.diff), with the second
source [reviewer_old_cap_delta.py](reviewer_old_cap_delta.py). It changes the
frozen exact coefficients, input/output paths, explicit old-coupling cap and
target ceiling; the already reviewed proof machinery is unchanged.

| Independently certified quantity | Original | Old-cap delta |
|---|---:|---:|
| Maximum point error, approximate display of exact rational bound | `5.194235725739695e-13` | `1.752474830885985e-13` |
| Strict stated ceiling checked exactly | `5.2e-13` | `1.76e-13` |
| Largest reviewer reflection-amplitude uncertainty | `<4.09e-54` | `<2.06e-55` |
| Largest full-basis inverse infinity bound, approximate | `1033.4565239575884` | `229.33244945953757` |
| Error after removing the lambdaA contact, numerical discriminator | `1.599614274458166` | `0.17342309095639322` |

The full-basis inverse norm need not equal the author's parity-basis norm;
infinity norms depend on basis. The larger old-cap value above is not a
disagreement with its parity bound below 163.903. Both are adequate for their
respective exact residual estimates.

The target comparison is not guaranteed by its own construction. Replacing
the target by its complex conjugate gives an exact error lower bound
`48/25 - certified_error > 1.91` for each witness. Removing the lambdaA
contact changes the physical boundary matrix and fails the point gate by
the large numerical amounts shown. That term-drop calculation is diagnostic;
the listed rigorous bounds belong to the unchanged witnesses. Parameters
were calibrated to the supplied W, so this is a verified design witness,
not a prediction of W from microscopic physics.

The later note's wrapped phase ceiling is also valid. If the chord error is
less than `d=176/10^15`, unitarity gives angle `2 asin(chord/2)`, bounded by
`d/(1-d^2/4) < 177/10^15`. The last inequality was checked with exact fractions.
It is a consequence of the certified stationary chord, not an extra fit.

Exact numerical results are in [RESULTS.json](RESULTS.json) and
[old_cap_delta/RESULTS.json](old_cap_delta/RESULTS.json). All rational square
roots, boundary matrices, inverse proposals, state proposals and right-hand
sides needed to inspect the reviewer certificates are preserved in
[WITNESS.json](WITNESS.json) and
[old_cap_delta/WITNESS.json](old_cap_delta/WITNESS.json). The author files
preserve scalar certificate metrics but not these full proposal matrices;
the reviewer files supply separately generated witnesses rather than
pretending to recover the historical author's in-memory matrices.

## Positive supports and incident loads

Every displayed installed block has support on one site or one listed cubic
nearest-neighbor edge. The source hopping core `nA+nB-L_AB` has eigenvalues
`0,0,2,2`; its norm is two. Each occupation-conditioned block
`n(I+X)` has eigenvalues `0,0,0,2` on its two qubits. The number and vacancy
projectors have norm one, and `nA nB` has norm one. All their multiplying
coefficients are strictly positive in both witnesses. K has eigenvalues one
and three and stays installed with its literal coefficients. No term uses
a projector on global clock number, a hidden three-body support or W itself.

| Site | Incident norm formula, excluding literal old K | Original, approximate | Old-cap, exact terminating value |
|---|---|---:|---:|
| old1 | `2gA` | `39.999996310531664` | `1.993757127633340` |
| old2 | `2gB` | `19.739168471156288` | `1.198638631120596` |
| A | `DeltaA+2gA+2h+u+2lambdaA` | `100.4609384820457` | `20.332662089993454` |
| B | `DeltaB+2gB+2h+u+2lambdaB` | `84.39591810244605` | `17.078839343776311` |
| c0 | `3J+2lambdaA+mu0` | `2.405352234687743` | `8.015120691541701` |
| c1 | `4J+2lambdaB+nu` | `6.701339506160476` | `6.730044773026091` |
| later clock site | `4J` | `1.555612607490684` | `0.120084428428128` |

Both old sites additionally see the original norm-three K block. The old-cap
gain is real and exactly checked; it is not an all-site cap. The c0 clock
load increases relative to the original witness. The endpoint term `J n_c0`
is included in its `3J`, and the positive vacancy projector is included at
c1. Counting a source hopping block as its displayed positive block is
explicit; a different actuator decomposition would need its own resource
account.

Clock number is conserved. On each fixed-number sector the diagonal clock
load is `2J N` and the total available hopping degree is at most `2N`, so
the clock restriction has norm at most `4J N`. Positive bounded finite
old/source/contact operators can be added on that sector. Their orthogonal
direct sum defines a positive selfadjoint operator in the specified
finite-excitation representation. This validates the mathematical positive
extension, not its native fabrication, energy identification or preparation.

## Execution and exposure limits

The original author receipts, stdout/stderr and exact result files were
inspected as supplied historical evidence. Their finite-lead checks are
different assembly/path diagnostics. The reported discrepancies are near
floating precision and do not themselves certify `10^-13` accuracy, lead
convergence rates or any dynamical finite-clock horizon. In particular the
old-cap discrepancies increase with some lead lengths; the note only claims
their observed bound, not monotone convergence. The rational certificates,
not those binary64 differences, support the strict point claims.

The reviewer used one calculation method, executed once for the original
witness and once for the subsequently authorized frozen coefficient delta.
Both exits were zero; both stderr files are empty. The exact commands,
source hashes at launch/finish, output hashes and resource observations are
in [RUN_RECEIPT.json](RUN_RECEIPT.json) and
[old_cap_delta/RUN_RECEIPT.json](old_cap_delta/RUN_RECEIPT.json).

| Actual reviewer execution | Original | Old-cap delta |
|---|---:|---:|
| Parent-observed elapsed seconds | `1.4072473333217204` | `1.3733761669136584` |
| Child user CPU seconds | `1.164255` | `1.191690` |
| Child system CPU seconds | `0.040983` | `0.048474` |
| Observed peak RSS bytes | `40288256` | `40255488` |
| Enforced wall / child CPU caps | `120 / 90 seconds` | `120 / 90 seconds` |

Each run uses two 32-by-32 boundary matrices with two right-hand sides at
each of two old-dependent energies, and a twelve-dimensional source square
root. No time evolution or large packet was simulated. Thread environment
variables were set to one; hardware thread use was not measured. Program
versions and complete streams are retained. No author program, search or
unaffected reviewer calculation was rerun for provenance alone.

## Safe disposition and remaining science

The narrow supported result is a pair of fixed rational stationary designs
for the supplied literal K and W, with rigorous scalar residual bounds,
complete asymptotic channel closure and positive nearest-neighbor two-body
supports. The later design also meets the added old-site cap two. Native
permission for these occupation-conditioned couplers, exact calibrated
coefficients, source preparation, one-head input and the infinite blank
tail remains supplied.

No claim here licenses an all-future complete-output operation from a
normalizable input. That would still require a certified momentum interval,
boundary resolvent/derivative control, a correctly normalized generalized
eigenfunction packet, comparison with the same independently prepared product
input for every old state, uniform incoming/contact/closed-channel tail
bounds and control of bound-state overlap. A fixed finite clock would need
a separate horizon estimate. These obligations are not inherited from the
new generic packet bridge and were not discharged by this review. A tunable
family or exact target equation would be additional work for arbitrary
accuracy below either fixed calibration residual. Reset, indefinite reuse,
exact permanent capture and Record formation remain outside the claims.

This is a reviewer recommendation for conditional stationary support, not an
author acceptance record or an independent retained audit. All reviewer writes
are confined to this review directory. No Git, PR, network, other-chat,
shared-checkpoint, editable-prompt, axiom or audit changes were made.
