# Fixed first two-source native Ward certificate

The general comparison, finite covariance table, source moment recurrence,
and new trial have been derived before this calculation. The source formulas
use at most24 Clifford words through the fifth action; moments through order
ten have been derived symbolically. This is a small scalar calculation from
named supplied native premises, not a Fock-space solve or an empirical fit.

Use the two existing degree-two p families (residual and variational), copied
byte-for-byte from pinned a2aca4bc quartic INPUTS. Do not reoptimize p here.
Replace the previous constant-q inner trial by [W,p(D)]Omega and compute its
NEW nominal from all90 ordered disjoint pair terms. The retained old nominal
is comparison data only and is not a new input to that number.

The new nominal simplifies, with p_j=P coefficients and q_j=O coefficients,
to

    N = 60p0²+24p0q0+6q0²
        -312p2²-96p2q2-24q2²
        +72(2mu-nu/3)p1p2.                              (P.1)

The individual class kernels and both exact trial norms are saved in
BLOCK12_NOMINAL_FORMULAS.json. Compare (P.1) with their weighted sum before
using it; do not delete an ordered class or assume each is positive.

Recover mu=3m1 and nu=3m3_O-4mu from the accepted vacuum moment intervals,
with outward rational arithmetic. These two defining moment rows are therefore
NOT independent tests of the new recurrence. Use the separate accepted
omega5 and omega7/9 intervals for L5,L7,L9. Compare the remaining new vacuum
moment formulas with the accepted order0..10 intervals before proceeding.
Source truth and the common infinite gap delta=1/4 remain inherited and
conditional; this calculation does not re-audit them.

Initially use ONLY broad analytical Green bounds

    1/6 <= A0 <= 17/60,
    2/5 <= C0 <= 8/15.

The A0 upper is the primary infinite node proof; its lower is Jensen.
Cauchy–Schwarz C0²<=A0 and 17/60<(8/15)² give the upper C0 bound. Jensen
gives C0>=1/sqrt6>2/5. This first calculation does not use the provisional
Block6 stronger chart or its improved numerical bound.

For each source psi=Omega and psi=W_A Omega, evaluate its residual-majorant
polynomial expectation from the derived moments. Use the gap bound and the
same15 positive quartic envelopes indexed by unordered t,u from{1,2,4,8,16}.
Every candidate is a globally valid bound; select the smallest certified
upper. Preserve the affine A0,C0 dependence BEFORE interval substitution.
No new oracle, quadrature or continuous parameter search is run.

Let E_A and Y_A be outward upper roots of those two source error bounds.
Use F_A=Y_A+||W_A||E_A, with ||W_P||<=sqrt(72A0_upper), ||W_O||=sqrt12.
Sum twelve P and three O squared errors, compute both new trial norms,
and apply the original posterior comparison with the new N. Save all
candidate uppers, selected parameters, error components, interval endpoints,
input hashes and status. A negative squared-norm upper refuses the run;
a negative lower endpoint may use the known nonnegative norm domain.
An interval containing zero remains inconclusive.

Prospective budget:60 seconds and384MiB for the scalar certificate. Exact
rational arithmetic and outward integer-square-root brackets are used. The
previous symbolic derivation completed in0.57seconds; this is not a claim
that the new interval calculation has already met its budget. If the broad
Green widths dominate, decide a separately specified refinement afterward,
preserving this first result. No result can retroactively change this contract.
