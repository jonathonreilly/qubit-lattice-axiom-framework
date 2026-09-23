# Independent consequences for the actual unselected first output

2026-09-23. The checked prepared-flat theorem does imply nontrivial statements
for the actual output without discarding its other half or assuming that half
has a state limit. They require distinguishing finite electric windows, total
number probabilities and trace-norm state convergence.

For a restarted actual first output, the six-record density has a controlled
finite-window limit **after time smearing**. For the deterministic original
all-A-plus, zero-field initialization, the exact first target clock supplies
that smearing automatically. The full density then has a fixed-time limit on
every finite electric window, uniformly on compact time intervals. That limit
is subnormalized: its trace is (1+exp(-16 kappa t))/2. Hence for every fixed
t>0 the normalized full target density has no trace-norm convergent subsequence
under this joint-spin embedding. The deterministic microscopic density has the
same local limit and the same obstruction. This does not determine the exact
total six/eight-record probabilities; explicit bounds are obtained instead.

This is an independent pre-author-source consequence reconstruction. It uses
only the frozen prepared packet, checked ring spectrum and permitted parent
target. The current actual-first-output candidate, unprepared follow-ups,
tail folders and campaign planning surfaces remain unopened. The exact source
identities are in SOURCE_IDENTITIES.json. No candidate formula was supplied.

## 1. Model, source premises and topology

Use the same fixed oriented eight-site ring, hard-core q=0,+1,-1, staggered
Gauss background, total charge four, normalized integer spin S, and

    C=S(S+1),    eta=K C=delta/epsilon^2,

with K,delta,kappa>0 fixed. P requires all A occupied. The effective target
uses H2_S,H4_S and sqrt(kappa) B_(j,S) exactly as in the sealed prepared
packet. The rotor P spaces H_N for N=4,6,8 are embedded with circulation
f=E7 and Gauss E_e=f+g_e(q). All spin spaces use their complete physical
electric intervals, embedded in these common rotor spaces.

The reused mathematical premises are:

1. On H6, H2 is bounded, its only physical point eigenvalue is -4, and its
   eigenspace projection F has the smooth finite-range compact frame already
   checked. Extra fiber kernels at isolated angles are not additional
   normalizable eigenvectors.
2. The prepared theorem supplies the ordinary-time no-event limit on F with
   self-adjoint H_flat on D(f^2), including its generated electric operator
   and bounded H4. Its loss is 4 kappa. Strong convergence extends to every
   normalizable prepared input and trace-class density with convergent spin
   embeddings; no uniform moment assumption is needed for that extension.
3. The bounded fixed-graph parent theorem approximates deterministic
   P-supported microscopic initial densities by the full spin target with
   trace error O(epsilon), uniformly in S on compact time intervals.

These are source-bound checked conditional results in a supplied model, not
formal retained/audit verdicts. No cubic pre-first-event field theorem or
unprepared-state limit is imported.

For a fixed integer R>=0 define Pi_R^(N) to project onto the physical P
states in H_N satisfying max_e |E_e|<=R. This is finite rank and increases
strongly to I on H_N as R grows. A finite electric-window observable means
an arbitrary bounded operator O=Pi_R^(N) O Pi_R^(N), with R independent of
S. Off-diagonal field and matter matrix elements are allowed, not only
diagonal probabilities. Finite-window convergence means trace-norm convergence
of Pi_R rho_S Pi_R for each fixed R. It does not mean convergence for the
infinite-rank number projection I_(H_N), nor for R growing with S.

Let

    V_S(t)=exp[-it(eta H2_S+delta H4_S-i kappa R_S/2)],
    R_S=sum_j B_(j,S)^dagger B_(j,S)

on H6, with the whole-box zero extension from the prepared proof if needed.
The physical spin space is reducing. Centering by the scalar phase exp(-4i
eta t) gives the prepared strong limit

    W(t)=exp(-2 kappa t) U(t) F,
    U(t)=exp(-it H_flat) on F H6.                       (1)

The scalar phase cancels in every density below.

## 2. Uniform finite-spin loss bound and the adjoint limit

On H6 a next birth is possible precisely when the two vacant B positions
are adjacent. Then there is one A center between them. For a fixed resolved
edge mark there is only one possible prior old-record destination: the other
B neighbor of that A. Its final charge and field uniquely recover the initial
charge and field. Thus each B_(j,S)^dagger B_(j,S) is diagonal in the physical
charge/field basis. There are four possible resolved paths from an adjacent
configuration and none from an opposite pair. Each path's squared amplitude
is a product of two normalized-shift squared amplitudes, both at most one.
Consequently, as a complete physical-space operator inequality for every S,

    0 <= R_S <= 4 Q_adj <= 4 I.                        (2)

The two newborn orientations on a fixed edge have orthogonal output ranges,
so their cross-Gram is zero at finite S. The coherent and resolved total
losses therefore agree exactly; (2) holds for both stipulated instruments.
This uses the post-PRE clarification in the checked prepared packet, not its
superseded runner comment. Individual coherent recycling outputs are still
different because their cross-output density operators need not vanish.

In particular every normalized physical six-record no-event input satisfies

    exp(-4 kappa t) <= tr[V_S(t) rho V_S(t)^dagger] <= 1. (3)

There is also a needed adjoint version of the prepared vector theorem:

    exp(+4i eta t) V_S(t)^dagger F
      -> exp(-2 kappa t) U(t)^dagger F                 (4)

strongly, uniformly on compact time intervals. This is not inferred from
forward strong convergence alone. To prove it, repeat the sealed core
corrector argument with both Hamiltonian signs reversed and the loss sign
unchanged. The exact generator becomes +i H_S-kappa R_S/2 and remains a
contraction. The compressed electric diagonal remains self-adjoint on D(f^2)
with its sign reversed; weight propagation uses commutation and bounded
weighted shifts, not positivity of that diagonal. All remainder and crossing
inverse estimates use absolute norms and survive the sign change. The same
small corrector and density extension prove (4). No new gap or field-moment
assumption is introduced.

It follows that for a fixed positive trace-class input rho, and any vectors
u,v in F H6,

    <u,V_S rho V_S^dagger v>
       -> <u,W rho W^dagger v>                         (5)

uniformly on compact times. Trace-norm convergent embedded initial sequences
may replace rho by contractivity. This identifies flat matrix elements even
when rho has flat/complement coherences and the complementary component itself
has no known limit.

## 3. A compactness consequence for arbitrary actual outputs

Put sigma_S(t)=V_S(t) rho V_S(t)^dagger and

    sigma_F(t)=exp(-4 kappa t) U(t) F rho F U(t)^dagger. (6)

For every finite-window observable O and every scalar a in L^1([0,T]),

    integral_0^T a(t) tr[O sigma_S(t)] dt
       -> integral_0^T a(t) tr[O sigma_F(t)] dt.         (7)

Equivalently, the time-smeared density compressed to any fixed electric
window converges in trace norm. Equation (7) supplies no pointwise-in-time
six-record finite-window limit after a fixed externally prescribed restart.

Here is a direct proof which does not assume dispersive decay, a complementary
semigroup limit, or a uniform spin gap. The sigma_S are positive and have
trace at most tr rho. Extract weak-star L^infinity subsequences of their
countably many physical matrix entries. Positivity and the uniform bound
on every finite diagonal sum pass to the limit, giving for almost every t
a positive trace-class sigma(t) with tr sigma(t)<=tr rho. This can be done
simultaneously on a countable dense set of finite-support vectors and time
tests; boundedness extends the result to all compact-operator tests.

The no-event equation, tested against a finite-rank finite-field K and a
smooth compactly supported scalar a(t), and divided by eta, gives

    integral a(t) tr([H2_S,K] sigma_S(t)) dt -> 0.       (8)

The integrated derivative term is O(eta^-1), as are the bounded H4 and loss
terms. H2_S and its adjoint converge strongly with uniform norm bounds, so
[H2_S,K]->[H2,K] in operator norm. The limiting density therefore commutes
with H2 for almost every t. A positive compact operator commuting with a
bounded self-adjoint H2 has its nonzero finite-dimensional eigenspaces
invariant under H2. Diagonalizing H2 on each such eigenspace shows that its
support lies entirely in the point spectral subspace of H2. By premise 1,

    sigma(t)=F sigma(t) F.                             (9)

The continuous spectral component cannot carry a nonzero commuting
trace-class density. This fact uses the physical operator, not a chosen
angle fiber or a normalized state at one angle.

Equation (5) identifies all matrix elements of the remaining F block with
(6). Hence every subsequential local time-weak limit is sigma_F. The
bounded set of these matrix-entry/time functionals is metrizable using a
countable dense set, so uniqueness gives (7) for the whole sequence. Approximation
of an L^1 time weight by smooth weights is uniform using the trace bound.
Finite dimensionality of each window converts its entrywise convergence to
trace norm. This completes the consequence without solving the complement.

## 4. Survival and subsequent formation after an actual first mark

Let w=tr(F rho F) for a normalized actual output. Decompose rho into its
F/F, Q/Q and cross blocks, Q=I-F. The F/F no-event contribution has trace
w exp(-4 kappa t) in the limit by the prepared theorem. The Q/Q contribution
is nonnegative and at most 1-w. The trace of each cross contribution tends
to zero uniformly on compact time intervals: combine forward prepared
convergence with (4), or first check finite-rank cross operators and use
trace approximation. Thus, with s_S(t)=tr sigma_S(t),

    exp(-4 kappa t) <= s_S(t),
    limsup s_S(t) <= 1-w+w exp(-4 kappa t).             (10)

The upper inequality has an o(1) remainder uniform on any fixed compact
time interval for a fixed input or a trace-convergent input sequence. It is
not asserted as an exact finite-S upper bound. The lower bound is exact.

For both specified normalized first-mark outputs the checked physical flat
weight is w=1/2. Therefore the next-event probability obeys

    (1-exp(-4 kappa t))/2 <= liminf Pr_S(next by t)
       <= limsup Pr_S(next by t) <= 1-exp(-4 kappa t).   (11)

These are bounds, not an exponential waiting law for the unselected output.
In particular replacing the initial output by its normalized F projection
would wrongly delete a probability one-half branch.

There is a stronger *local* statement for the endpoint eight-record density.
All sites are occupied after this next event, and H2,H4 and later jumps vanish.
Hence

    tau_(8,S)(t)=kappa sum_j integral_0^t
                       B_(j,S) sigma_S(u) B_(j,S)^dagger du.

For a finite-window O8, B_(j,S)^dagger O8 B_(j,S) converges in operator norm
to the corresponding rotor operator and has support in a fixed enlarged
finite electric window. A hop/birth path shifts f by at most one and any
link field by at most one. Thus (7) proves pointwise finite-window convergence
of tau_(8,S)(t) to

    tau_(8,F)(t)=kappa sum_j integral_0^t
                              B_j sigma_F(u) B_j^dagger du. (12)

Uniform bounded derivatives of these integrated blocks give convergence
uniformly on compact times after each window compression. Its global trace
is w(1-exp(-4 kappa t)). This trace is a local-limit mass, not necessarily the
limit of the actual total eight-record probability. The identity operator on
H8 is not a finite-window observable.

## 5. Exact first target clock from deterministic zero field

Now initialize the original target in the normalized physical vector v0:
all four A sites plus, all B sites vacant, and every E_e=0. This is allowed
for every integer S>=1. In the N=4 P sector only that matter word is possible.
A change in circulation requires a complete eight-hop circuit, so H2 and H4
are diagonal in f there. At f=0 every link shift in a relevant path has
unit amplitude, including at S=1. Direct path enumeration gives exactly

    H2_S v0=-8 v0,      H4_S v0=24 v0.                  (13)

There are eight outward hop choices. For the Z norm, there are twenty
unordered legal disjoint-outward-hop pairs, each with two orders, giving
||Z v0||^2=80 and 8^2-80/2=24. These paths only use fields 0,+/-1.

For each of the sixteen resolved first channels, precisely one old-record
destination is legal. Its hop and the subsequent empty-edge birth use
different links initially at zero, so both normalized amplitudes are one.
The output vector psi_j has norm one and is independent of S>=1. For the
eight coherent edge channels the output is the positive sum of the two
resolved outputs, with squared norm two. Distinct input f values yield
orthogonal outputs for a fixed channel, so the first loss has no hidden
off-diagonal circulation term. Its action on v0 is exactly 16 v0.

Put r1=16 kappa, r2=4 kappa. The N=4 target no-event density is therefore

    rho_(4,S)(t)=exp(-r1 t)|v0><v0|                     (14)

for every S>=1. This is an exact *target* clock; it is not claimed to be an
exact clock of the bare microscopic model at finite epsilon.

Let A be the constant first-event source density, including its rate:

    A=kappa sum_j |psi_j><psi_j|                        (15)

for resolved channels. For coherent channels use the eight unnormalized
positive-sum outputs in the same formula. Then tr A=r1 and
tr(F A F)=r1/2 for either instrument. The independent control checks all
sixteen resolved and eight coherent outputs, including cut-edge field shifts.

The exact six-record target block from this deterministic initialization is

    rho_(6,S)(t)
      =integral_0^t exp(-r1 s) V_S(t-s) A V_S(t-s)^dagger ds
      =exp(-r1 t) integral_0^t exp(r1 u) V_S(u) A V_S(u)^dagger du. (16)

The scalar fast phase cancels in the density. Equation (16) is an exact
triangular-sector semigroup identity. It does not condition a microscopic
trajectory at a random first stopping time.

## 6. Fixed-time local limit for the actual original evolution

The time weight in (16) is an allowed L^1 weight in (7). Therefore for each
fixed electric window and each ordinary t,

    rho_(6,S)(t) -> Phi(t) locally,
    Phi(t)=integral_0^t exp(-r1 s) exp(-r2(t-s))
                     U(t-s) F A F U(t-s)^dagger ds.      (17)

This convergence is uniform for t in a compact interval. Indeed the second
expression in (16) has uniformly bounded trace-norm derivative, at most
2 r1 on normalized full inputs. Window compression preserves that bound,
so finite-dimensional equicontinuity upgrades pointwise convergence to
uniform convergence. There is no unsupported interchange of the spin limit
with a sharp microscopic stopping-time preparation.

The eight-record block has the exact source integral of the six-record block.
Finite-window convergence and finite propagation of the bounded B operators
give, uniformly on compact times,

    rho_(8,S)(t) -> Psi(t) locally,
    Psi(t)=kappa sum_j integral_0^t B_j Phi(u) B_j^dagger du. (18)

The four-record block remains (14). The full finite-window limit is thus the
explicit positive trace-class operator

    rho_loc(t)=exp(-r1 t)|v0><v0| + Phi(t) + Psi(t),      (19)

with the three terms in orthogonal record-number sectors. It retains all
instrument-dependent field and matter coherences present in A and the B_j.
No assertion about the escaping complementary component is needed.

Define

    a(t)=exp(-r1 t),
    g(t)=r1/(r1-r2) [exp(-r2 t)-exp(-r1 t)]
        =(4/3)[exp(-4 kappa t)-exp(-16 kappa t)],
    h(t)=1-a(t)-g(t).                                  (20)

Since the F loss is scalar r2, the traces in (17)--(19) are

    tr Phi(t)=g(t)/2,       tr Psi(t)=h(t)/2,
    tr rho_loc(t)=(1+a(t))/2.                            (21)

For every fixed t>0 this is less than one. Finite windows exhaust the common
rotor Hilbert space. Any trace-norm limit of a subsequence of the normalized
rho_S(t) would have the same matrix entries as rho_loc(t), and hence would
equal rho_loc(t). Trace continuity would then give trace one, contradicting
(21). Therefore **at any fixed t>0, the original normalized target densities
have no trace-norm convergent subsequence in the specified common embedding**.

This is a precise topology/initialization result. It is compatible with the
controlled finite-window limit just proved, with possible weaker descriptions
of probability at increasing fields, and with possible limits of total number
probabilities. It does not establish that every observable lacks a limit, that
normalizable flat preparations fail, or that the microscopic theory is
inconsistent. The missing local mass is exactly (1-a(t))/2; it is the half of
formed outputs not supported by the physical flat point spectrum.

## 7. Total number-probability bounds and microscopic transfer

Write p_(N,S)(t)=tr rho_(N,S)(t). The identity on each H_N is noncompact, so
its probabilities must be bounded separately rather than read off (21).
Using (3), (10) with tr(F A F)=r1/2, and the exact convolution (16),

    p_(4,S)(t)=a(t),
    g(t) <= p_(6,S)(t),
    limsup p_(6,S)(t) <= [1-a(t)+g(t)]/2,
    h(t)/2 <= liminf p_(8,S)(t)
             <= limsup p_(8,S)(t) <= h(t).             (22)

The p6 lower bound and p8 upper bound are exact for the target at every S.
The other bounds admit o(1) errors uniform on compact times for this fixed
source. These intervals do not claim their endpoints are optimal or attained,
nor do they claim the total p6 and p8 limits exist. The function h is the
convolution CDF for rates r1 then r2; the actual unselected law is bracketed
between one half of h and h, rather than identified with either one.

Apply the parent's uniform-S deterministic microscopic-to-target estimate
to the original bare P state v0, with epsilon^2=delta/(K C). Its error tends
to zero. Thus (14), all finite-window limits (17)--(19), and the limiting
bounds (22) transfer to the microscopic densities with the same initialization.
Finite electric windows in the microscopic space may include W>0 matter
states; their extra population tends to zero by the same trace estimate.
The full microscopic density cannot acquire a trace-norm convergent
subsequence that the target lacks, because their distance is O(epsilon).

This is a deterministic full-density composition. It neither asserts nor
requires a theorem for normalized microscopic histories conditioned at a
random first mark, and it introduces no flat-sector projection operation.

## 8. Decisive checks, limits and source discipline

The new clock calculation enumerates exact physical two/four-hop paths from
v0; it verifies -8 and 24 and all first-channel amplitudes. Finite-spin checks
at S=1,2,4,8 agree exactly. Complete six-record matrices at S=1,2,4,8,16 have
diagonal R_S with spectrum in [0,4], zero loss on opposite occupied-B pairs,
and jumps changing f by at most one. The general proof is the injective
resolved-channel path count and normalized-weight bound in Section 2, not an
extrapolation of these finite checks.

The old independently checked local hop/flat-frame helpers are reused at
their sealed identities; no author code is imported. Python bytecode writing
was disabled so these calculations write only the new assigned directory.
The proof of the local consequence is the compactness/commutation argument
and the explicitly justified adjoint limit. No numerical observation of
dispersion or revival suppression substitutes for that proof.

For K=0.4,delta=0.7,kappa=0.3,T=0.6, a direct first-clock convolution of all
sixteen resolved channels was computed at S=4,8,16 with nested 257/513-point
Simpson grids. The refined p6 values are approximately 0.65610,0.66450,0.67377,
within the derived bounds 0.57416 and 0.75901. For the field window R=1 the
computed probabilities are about 0.46309,0.31230,0.30844, against local-limit
0.26156; for R=2 they are 0.65318,0.40617,0.38327, against 0.28707. These spins
are not advertised as negligible-error regimes or as evidence for a rate.
The largest difference between the two quadratures on these window values is
about 1.42e-7. The reference cutoff and adjoint/cross-term controls are retained
separately: increasing the flat reference cutoff from 12 to 20 changes the
two window probabilities by less than 1.1e-14 and the adjoint reference
vector by 6.6e-15. At S=4,8,16,32 the adjoint prepared-vector errors are
0.08762,0.03870,0.01889,0.01035; the corresponding evolved flat/complement
cross-term magnitudes are 0.002214,0.000595,0.000171,0.000083. These checks
include the physical boundary rather than truncating to a common small box.
All numerical controls are floating corroboration, not interval
certificates or a computed complementary limit.

No scientific assertion failed in the first consequence run. Its full result,
stdout/stderr and actual timed command receipt are preserved. The additional
source and adjoint/reference checks have their own receipts. SOURCE_IDENTITIES
authenticates all reused prepared artifacts and permitted sources. New source
comparison remains pending until this reconstruction is PRE-sealed.

The exact negative topology consequence was stress-tested with the applicable
N1--N8 questions in NO_GO_DISCIPLINE_CHECKLIST.md. This is a restricted-context
independent reconstruction, not a formal no-go publication/audit packet: no
Git commit, forbidden cross-campaign scan or retained-authority certification
is claimed. The direct mathematical contradiction in (21) is separate from
that procedural status. No new axiom, three-dimensional field phase,
volume-uniform claim, empirical prediction or TOE closure is asserted.
