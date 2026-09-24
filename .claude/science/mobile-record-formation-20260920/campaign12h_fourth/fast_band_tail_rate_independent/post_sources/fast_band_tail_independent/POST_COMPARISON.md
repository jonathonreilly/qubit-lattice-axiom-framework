# Bounded POST comparison: rotor cube fast-band tail

The released proof and exact certificates agree with the independent PRE under
their full stated hypotheses. No mathematical correction is required. Both
prove strong decay for every fixed normalizable physical rotor state in the
specified W=1, N=6, total-charge-four cube sector, with fixed delta,kappa>0,
while the semigroup has norm one at every finite fast time. This is a bounded
source comparison, not an audit, retained-status, publication, or fixed-positive-
physical-time conclusion.

The new POST control reconstructs all 288 released nonzero Laurent terms, the
complete integer rank-witness and Gram matrices, both determinants, the change
between the two Gauss cycle bases, and all physical first-mark residual vectors.
The residuals 1/12,1/12,1/6 belong to the exceptional flat fiber. They are not
physical late-time survival weights. All 22 PRE artifacts remain unchanged.

## 1. Bindings and exposure boundary

The complete root proof, exact control, full exact certificate, exploration
source/data, retained failed integer-power source and logs, plan, scope record,
development record, receipt, and seal were read or exhaustively reconstructed.
No author Python was imported or executed. POST uses the immutable independent
PRE engine and new independent matrix/path code. Source snapshots are local and
bound by POST_SOURCE_BINDINGS.json.

| Object | SHA256 |
| --- | --- |
| Immutable independent PRE seal | `070337f415cd81ddafa7178790863a2ecc542bcb23d6a142b681e10f4cec853e` |
| Immutable independent PRE proof | `4fac5d28f39bfe747f50c2a8ca083353a92f6a58bddaf46456127d9770d0e5de` |
| Released root tail proof | `9d73530905763400ce31f66188c5eb9c5c1a0336e0c444bbe4f1c23c0c19fc7a` |
| Released root tail seal | `646d5a33082c0d44a8af5a25a22b61da9b8ca89275651f80458c2a9c7f7f02e6` |
| Root complete exact certificate | `9761680bde05c651c01a421e80b8aeac358ae9b24da717cc7b0b05d48d186a0b` |
| Completed compact-time dependency seal | `5824c37555272e57a1b5b0b1214bcb5441a86dd9362f18bb157bbeec960a4ef5` |
| Completed compact-time comparison report | `b410adb5ef459052023e8deb5090ecc76913974bc3d2c9792db1f471c5d141bf` |

Authentication covers all 18 tail-author artifacts and 6 bound source files,
plus the released compact-time report and its final seal. Root had reviewed
and authenticated this packet's 22 PRE artifacts before release. The PRE was
sealed before exposure to the root tail result. Neither the current campaign
CHECKPOINT, external personal tail directory, nor unreleased peer material was
read. Paths appearing in preserved tracebacks are historical provenance, not
additional files opened by this comparison.

## 2. The different Gauss trees are unitarily equivalent

Both packets use the same A-to-B edge order

    (01,02,04,31,32,37,51,54,57,62,64,67)

and exactly the same 168 matter-word ordering. Both retain all 36 W=0 and 36
W=2 intermediate labels when constructing G=Pi1(FF*-F*F)Pi1, and all 96 W=1
labels, split into 24 dark and 72 bright labels. Their cycle coordinates differ:

    independent PRE chords: (32,54,57,64,67),
    root chords:            (01,37,54,57,64).

Let C_I be the independent integral cycle matrix and C_A the root matrix. Write
E0_I(q) and E0_A(q) for the corresponding tree reference fields. Taking root
chord components of the independent representation derives

    n_A = a(q)+M n_I,
    a(q) = E0_I(q) restricted to root chords,

    M = [ 1  1  0  0 -1
          0  0 -1  0 -1
          0  1  0  0  0
          0  0  1  0  0
          0  0  0  1  0 ],       det M=1.

The POST control derives this matrix from the frozen PRE cycles, verifies that
M and its inverse are integral, and reconstructs C_A=C_I M^-1. Every one of
the root's 60 cycle-matrix entries agrees. For all 168 charge words it derives

    E0_A(q)=E0_I(q)-C_A a(q)

and checks Gauss and the vanishing root chord components. Thus these are two
coordinates on the same full physical l2 space, not different flux truncations.

With the PRE's positive-exponent Fourier convention,

    theta_I=M^T theta_A,
    rhat_A(q,theta_A)=exp[i theta_A.a(q)] rhat_I(q,M^T theta_A).

Writing D for that charge-dependent diagonal phase, one obtains

    G_A(theta_A)=D(theta_A) G_I(M^T theta_A) D(theta_A)*.

D preserves dark/bright charge supports and Gamma. This gauge factor matters
when comparing actual matrices; only identifying the torus variables would
omit it. The control verifies the full rank-witness block with this factor.
The root witness theta_A=(pi,0,0,0,0) maps to PRE chord phases
(-1,-1,1,1,-1), with D(q)=(-1)^(a(q)_0).

## 3. Exact Laurent and rank reconstruction

The new control constructs F as a sparse matrix with a single integer Laurent
monomial for each legal outward charge move, in the PRE coordinates. It forms
FF* and F*F by matrix multiplication, retaining all intermediate charge labels.
For each G entry from q to q', a PRE exponent e becomes the root exponent

    e_A=M e+a(q')-a(q).

After this exact substitution, every coefficient and exponent in all 288
released bright-from-dark Laurent terms agrees. The complete dark-to-dark
Laurent block vanishes before any phases are evaluated. This independently
checks the root's stronger explicit polynomial cancellation, which is also
explained structurally in PRE: disjoint moves of both vacancies cancel, a
single-vacancy move becomes bright, and the three diagonal returns through
each neighboring W sector cancel.

Evaluating the reconstructed polynomial at the root's integer phase produces
exactly its entire 72 by 24 Q matrix. Its entire 24 by 24 Gram matrix agrees,
and independent exact determinant calculation gives

    det(Q^T Q)=4688333314034185078308864,
    det Q[rows 0..21,24,42; all columns]=-768.

The row indices here refer to the ordered bright sublist. The PRE's separate
certificate uses a different phase and a different minor, with determinant
-222208 and an independent modular full-rank witness over F_5. Both are valid
nonzero Laurent-polynomial witnesses; their determinant values are not meant
to coincide. The exact POST matrix is additionally checked by invoking only
the frozen PRE exact matrix builder at the transformed phase and conjugating
by D. This check does not use a root builder or a floating rank threshold.

The proof implications agree in full, not just at headline level. A nonzero
Laurent minor has a Haar-null zero set by polynomial induction and Fubini.
Almost every fiber therefore has injective bright-from-dark coupling. If its
dissipative generator had an imaginary-axis eigenvector, the real inner
product would force that vector into ker Gamma; the bright projection would
then contradict injectivity, using delta,kappa>0. Finite-dimensional spectral
decay follows at almost every fiber. Contraction bounds the squared norm by
the original integrable Fourier density, and dominated convergence gives
strong decay for every physical l2 state. Neither proof asserts a uniform
fiber gap or treats a numerical phase scan as this measure-theoretic argument.

The root's finite-time lower bound is also correct. Since 0<=Gamma<=2,

    d||V(tau)r||^2/dtau >= -2 kappa ||V(tau)r||^2,

so Gronwall yields

    exp(-2 kappa tau)||r||^2 <= ||V(tau)r||^2 <= ||r||^2.

This supplies strict finite-fast-time positivity for nonzero r while allowing
the infinite-fast-time limit to vanish. It does not strengthen the separate
microscopic estimate to unbounded tau.

## 4. Flat fiber and actual first-mark residuals

At the flat phase, both coordinate systems and their gauge factors coincide.
Exact rank 23 of Q means its dark kernel is one dimensional. Let u be the
uniform dark charge vector normalized by sqrt(24). The zero dark block gives
G u=0 and Gamma u=0, hence both L u=0 and L* u=0 for
L=-i delta G-kappa Gamma/2. Thus span(u) is reducing. Any imaginary-axis
eigenvector in its orthogonal complement would again be a dark kernel vector,
which is impossible. The complement decays, so the finite flat-fiber limit is
precisely the orthogonal projection onto u. No hidden zero-eigenvalue Jordan
block survives: L* u=0 also rules out a chain mapping into u.

The POST control separately constructs physical original first-output paths
from the zero-field all-A-plus word, using B_i=j_i F Omega and R_i=-F_0 B_i.
It retains actual integer field words before taking any fiber value. In the
edge order above, the only nonzero R words are:

| First sign | q | First three field entries; remaining nine zero | Coefficient |
| --- | --- | --- | ---: |
| plus | (0,-1,1,1,1,1,1,0) | (1,-1,-1) | -2 |
| minus | (0,1,-1,1,1,1,1,0) | (-1,1,-1) | -1 |
| minus | (0,1,1,1,-1,1,1,0) | (-1,-1,1) | -1 |

The coherent mark is the sum of these three physical words. All Gauss equations
are checked. These give b=(2,2,4), ||R||^2=(4,2,6) for plus, minus, coherent.
At flat phase the sums of R amplitudes are -2,-2,-4. Therefore the projection
of the normalized high vector R/sqrt(b) onto u has squared norm

    |sum amplitudes|^2/(24 b) = 1/12, 1/12, 1/6,

while the initial flat-fiber squared norms are 2,1,3/2. All six entries in the
root's three physical-vector certificates, including the repeated coherent
components, agree exactly. These calculations are newly reconstructed POST
checks, not claims that the PRE had already computed these numerical residuals.

These residuals describe a single exceptional fiber. A delta function at that
fiber is not physical L2; the full physical R words are finite-support states
whose Fourier amplitudes occupy the whole torus. Their physical norm tends to
zero by the theorem. Conversely, for each finite tau continuity near the flat
fiber permits a normalized Fourier packet with norm ratio arbitrarily close
to one. This proves ||V(tau)||=1; the packet can depend on tau. Neither packet
claims one normalizable state with a nonzero infinite-time survival weight.

## 5. Evidence, retained failures, and dependency status

The successful independent POST run contains 453 recorded checks, including
complete exact matrices, all polynomial entries, all tree/reference changes,
and all physical residual certificates. The count is bookkeeping; the exact
construction and analytic proof are the evidence. All eight exploratory root
phase rows and all four single-edge exploratory rows were also reproduced
through the reconstructed Laurent matrix, solely as exploration. The maximum
singular-value difference is 2.665e-15, far below the unchanged comparison
threshold 2e-12; their numerical rank threshold remains 1e-10 and is not a
proof premise.

The root's retained first exact attempt was read completely. Python negative
integer powers of -1 introduced SymPy floating entries, and a structural
integer equality assertion failed before a determinant was evaluated. The
complete source diff in AUTHOR_INTEGER_FIX.diff shows that the correction uses
integer parity directly and requires Integer entries. It changes no physical
entry or mathematical rank condition and relaxes no numerical tolerance.
Its failed source, stdout and stderr are included unchanged in the snapshots.

The first independent POST attempt also failed, after the exact comparisons
and physical residual checks had succeeded. Its auxiliary random-phase
exploration reused a frozen PRE routine containing bitwise `array_equal` for
two numerical constructions of Gamma. That check was exact on the PRE's
quarter-root phases but need not be bitwise exact after floating evaluation
at arbitrary phases. The PRE routine was not edited and the failure was not
reported as a completed run. The original POST code, result with checks, and
traceback are retained. The successful attempt evaluates G for the exploratory
phase comparison directly from the independently reconstructed Laurent matrix;
it no longer computes an irrelevant floating Gamma in that step. All comparison
thresholds and all exact scientific assertions remain unchanged. See
POST_DEVELOPMENT_RECORD.md and POST_RUN_CHANGE.diff.

The prior compact-time dependency now has a completed scoped comparison. Its
complete report and final seal were read and authenticated here. Root separately
reports full review and authentication of all 80 bindings. This packet does
not claim to repeat that complete code/evidence review. The report finds no
required correction in the leading compact-time energy curve or second-birth
coefficient, while preserving an explicitly failed auxiliary comparison of two
historical floating runs at its original 5e-8 threshold. That failed comparison
is still failed; no tolerance or source status is silently upgraded here.

The dependency can therefore be reused as independently checked within its
stated original-lambda-zero, zero-field, canonical actual-first-output, compact-
fast-time scope. The PRE's description of it as separately provisional is
preserved as historical PRE text. This POST updates the dependency record, not
those PRE bytes and not its formal retained/audit status. Conditional on that
compact theorem, the resulting f_i(tau) tends to zero in the sequential order
already stated in the root note.

## 6. Scope and disposition

No correction is required in the released tail formulas or full hypotheses.
The essential restrictions are the fixed cube, rotor integer-flux space,
N=6 and total charge four, W=1, unchanged original marks, and fixed positive
delta and kappa. Delta=0 or kappa=0 are excluded and invalidate strong decay.
A single fiber is never identified with a normalizable physical state.

The result does not exchange the compact joint limit with tau->infinity; does
not let tau=t/epsilon^2 inside the compact estimate; does not classify finite-
spin late-time behavior or all exceptional fibers; and gives no state-specific
tail rate, laboratory-time energy theorem, physical sink, heat/work, reservoir,
selected law, volume limit, or empirical conclusion. These are limits of the
proved claim rather than missing steps in its proof.

All PRE and root bytes remain unchanged. No editable prompt, workflow, author
source, or platform instruction was modified. There was no commit, publication,
audit verdict, subagent, or deadline extension. The final seal binds the exact
sources, completed and failed controls, raw logs, report, and unchanged PRE.
