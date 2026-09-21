# Polynomial relaxation and formation: bounded independent source check

2026-09-21. The complete frozen mathematical note and author runner were
reviewed. I found no unresolved mathematical defect in the displayed
comparison, killing estimates or sufficient torus schedule. One minor
executable coverage omission remains in the frozen runner, specified below.
This is a selective scientific review, not a formal audit or landing verdict.

## Finding F1: intended numerical cycle-six fixture is silently skipped

At `geometric_polynomial_relaxation_check.py:150`, `killing_bounds()` selects
`'cycle6'`, whereas `graph_cases()` calls this graph `'cycle_6'`. Consequently
the numerical uniform-exit/joint-clock/mean group has 35 rows across seven
actual fixtures, rather than including that intended eighth fixture. The
separate exact rational group does check `cycle6`, and the independent blind
suite checks its resolvents and bounds too. Thus this is a coverage defect,
not a counterexample to the theorem or a missing proof argument.

Narrow correction: replace only this selector by `'cycle_6'`, preserve the
old source/results, and run the affected killing group. The original source
is still frozen at the hash below. No primary edit was made by this reviewer.

## Reconstructed proof and constants

Let G be connected, finite and simple on 2K vertices with a perfect matching,
K>=2; let Omega be its near-perfect matchings, P its perfect matchings,
n=|Omega|, Z=|P|, R=n/Z. At geometric slide rate kappa, the prior independently
checked construction gives irreducibility on Omega. This is a geometric
statement; it does not assert ergodicity of all immutable marked histories.

The auxiliary Broder chain includes completion/deletion solely for comparison.
If A is the near/full incidence matrix, A1=h in {0,1} and A^T1=K1. Its
near-state trace is exactly

    L_trace = L_slide + kappa(H-AA^T/K).

In particular, a self-return excursion is not a trace jump. Harmonic extension
to each full matching gives energy factor n/(n+Z), and conditional variance
gives at least the same factor. They cancel in the Poincare comparison:
gap(trace)>=gap(Broder).

An ordered parent pair F-e,F-f is connected by at most2(K-1) real immutable
record slides along a simple path in the contracted reference graph. These
routes repeat no micro-edge. Every micro-edge can have at most two reference
perfect matchings, determined by completing the holes of either endpoint.
The factor two is necessary: our C4 fixture realizes both references on one
slide edge. At most2K^2 ordered paths use a micro-edge. Keeping the ordered
sum's factor1/2 gives

    E_trace <= C_K E_slide,  C_K=1+2K(K-1).

The Jerrum--Sinclair Theorem3.6 conductance bound is Phi>=1/(16mR^2).
The original chain selects a graph edge and additionally holds with
probability1/2; hence P=I+B/(2m*kappa), not I+B/kappa or I+B/(m*kappa).
Theorem2.2's reversible lazy-chain decay gives gap(P)>=Phi^2/2. Therefore

    g >= kappa/(256mR^4 C_K).

Theorem3.6 explicitly allows general graphs with a perfect matching, despite
the preceding section's initial bipartite setup. Its statement, hypotheses,
factor16 and proposal convention were checked against the supplied primary
PDF. The whole published conductance proof was not independently reproved.
[Jerrum and Sinclair, 1989, Theorems2.2 and3.6](https://people.eecs.berkeley.edu/~sinclair/perm.pdf).

For the actual finite symmetric chain, the L2 spectral estimate gives
2TV(P_t(x,.),pi)<=min(2,sqrt(n-1)e^(-gt)). Integration split at
log(n)/(2g) gives the centered inverse bound

    ||A0 f||infty <= T_G ||f||infty,  T_G=(1+log n)/g.

At birth rate beta for adjacent holes, p=pi(h)=KZ/n. For a full-geometry
event D, the killed equation is (L+beta H)u=beta a_D and pi(a_D)=pU(D).
Writing u=c+v gives ||v||<=beta T_G and
c-U(D)=-pi(hv)/p. The inequality |pi(hv)|<=p||v|| cancels the small hazard
fraction exactly; no inverse-p factor is required. Uniformly over entrance
states and laws,

    TV(exit,U) <= min(1,2beta T_G),
    |E[e^(-lambda beta p tau)1_D]-U(D)/(1+lambda)|
      <= beta T_G(1+lambda p)(1+1/(1+lambda)).

For the mean, z=beta p E[tau] satisfies (L+beta H)z=beta p and pi(hz)=p.
Its centered equation is v=-beta A0(hz), since A0 kills constants. Thus,
when2beta T_G<1,

    sup |beta p E[tau]-1| <= 2beta T_G/(1-2beta T_G).

Finite mean follows first from finite irreducibility and a nonempty killing
set. The mean limit is therefore proved separately from distributional
convergence. The clock starts at the two-vacancy entrance. Only the final
geometry bound extends immediately to arbitrary initially nonfull states,
using the earlier almost-sure filling result and uniform entrance bound.

For fixed d>2 and even cubic side N>=4, K=N^d/2 and m=2dK. The unchanged
Taggi Eq.(2.5) input gives R<=K^2/(2d); C_K<=2K^2 and n<=2^m then give

    g_N >= kappa*d^3/(64K^11),
    T_G <= 64K^11(1+2dK log2)/(kappa*d^3).

Consequently (beta_N/kappa)K^12 ->0 is sufficient for the stated uniform
exit-TV, fixed-lambda event-transform and scaled-mean conclusions. Combining
the mean estimate with chi_N=R/K and the previously checked Taggi lower/upper
statements yields the displayed bounds on beta_N E[tau]/V. The imported
convention uses opposite-sublattice averaging and strictly positive-time
returns r_d; the factor1/2 converting K=V/2 is correct.
[Taggi, arXiv:1909.06558v3, Theorem2.1 and Eq.(2.5)](https://arxiv.org/html/1909.06558v3).

## Evidence, failures and verification boundary

The full independent derivation is `PRE_COMPARISON_DERIVATION.md`. It and
the checker/results/logs were sealed before author-checker bodies or outputs
were accessed. The precomparison seal is
`2b20f617c76901ce78756702c6fac7a4390eec56776db74caef8a4caba14c8fd`.

The independent checker uses eleven explicitly recorded graphs: paths,
cycles, complete graphs, a diamond, K3,3, a cube and two distinct bridge
fixtures. It verifies exact Schur matrices, lazy edge-proposal normalization,
harmonic energy/variance, centered inverses, ordered routes and immutable
record legality. Exact cut minimization covers auxiliary spaces of at most
12 states. Eight fixtures have exact killed-resolvent checks for four beta
values, every entrance state and every target subset, and two nonzero Laplace
parameters. Spectral eigenvalues and comparisons to logarithmic bounds are
numerical corroboration, distinguished from exact matrix identities.

After sealing, comparison authenticated all four author groups and every
recorded log row: 123 graph fixtures, 3776 routed pairs including zero-length
self pairs, five exact cases and 35 numerical killing rows. It did not rerun
the full author suite. Selective fresh comparison instead matched eleven
complete matrix assemblies, independently recomputed all25 reported rational
values in the five exact cases, and checked five stabilized-solver cases
against exact rational inverses on a separate 12-state endpoint-killed path.
The complete author source was read; pure functions were extracted through
AST to avoid executing module imports or its output-writing main routine.

One independent failed attempt is retained: a constant-hazard symbolic
identity was tested using structural equality before simplification. Only
that simplification was added; the original checker, full logs and receipt
remain in this directory. The successful run's stderr is empty.

The author's preserved first run failed an unscaled floating killed-solve
row-normalization check. The final source replaces that solve with its
constant/centered Schur decomposition, whose algebra I reconstructed and
whose numerical outputs I compared to exact rational inverses. The original
failure remains authenticated; the direct-solve discrepancies are reported,
not concealed. This stabilization is not a mathematical premise change.

The primary PDF web fetch failed due to source size; local byte-pinned PDF
pages were used. Extraction warned about rotated text, so the decisive
Theorem3.6 and Theorem2.2 formulas were also checked visually. Third-party
PDFs, page extracts and images remain external. `LITERATURE_RECEIPT.json`
records exact read boundaries. Taggi's statement/hypothesis review is reused
at its unchanged source identity, not represented as a new whole-proof check.

Scope limits remain substantive: general graphs can have large R, so no
unconditional polynomial general-graph bound follows. Fixed beta is not
covered by the volume-selection conclusion. The Laplace bound is for fixed
lambda and does not claim total variation of the whole continuous-clock
joint law. Neither the total empty-start duration nor marked-state mixing,
phase structure, wave dynamics or a quantum realization is established.
Disconnected/no-perfect-matching countercontrols remain in the earlier
sealed dependency evidence. Constant hazard does not force a finite-beta
uniform exit geometry: on C4, its worst-state exit TV is
beta/[2(beta+4)] when kappa=1, although its clock is exactly exponential.

## Source identities and reproduction

- Candidate note: `f9d12f1fccc3ea54d3b640deaccdcbb04749db1d6ac5b7b2708193a4a0dd89bb`.
- Author runner: `fded420e936b93bee16aeba4bfed676363d0298e6c1268fa5193cea5ef0c0202`.
- Author RESULTS: `b90a22ad82a110715b457f0ab27c4ed5694fb1502cbe1dff2a03cb8dd937f779`.
- JS1989 PDF: `607ee31f4dbea8dd7cc3f59ca27915252334671268c6b4251069a23cd8ada3e9`.
- Taggi v3 PDF: `50a6f8a42cd5865a509efb706823e2dd0061233f49e6ec06d5395a627c1d2517`.

`FINAL_SEAL.json` binds all dependencies, source files and local evidence.
From this directory, `python3 independent_check.py` runs the independent
finite controls; `python3 compare_author.py` runs the selective comparison
against the frozen author identities. These commands rewrite only their
local result files, so use a copied evidence directory to preserve the seal.
No primary source, prior evidence, Git state, audit status or production
observables were changed or inspected outside the declared scope.
