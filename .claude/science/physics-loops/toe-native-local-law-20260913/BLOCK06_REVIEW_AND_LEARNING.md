# Common-frame milestone and next derivation

BLOCK06 constructed a specified finite-range native frame coupling for which
the two opposite Weyl nodes have the same inverse metric. The smallness bound
preserves exactly those two zeros for constant coefficients. The polar frame
action cancels the fixed-metric spin-strain residual when the metric is varied
with the spinor. The complete half-density Weyl operator contains a derived
scalar spin-connection term; opposite nodes need opposite signs, supplied by
one native z hopping. A polynomial inverse and local difference stencil give
a controlled variable-frame approximation, with an analytical low-band error
bound. None of these constructions selects a physical frame action.

PR8092 is OPEN and MERGEABLE at preserved head
4ad50beb2237097578815a623d963f3427cdcd78, branch
physics-loop/native-common-frame-20260913. Science commit:
cfd1c2365e49f3f43eec75c73d7a58b3c8e2c43e. Its single note and primary runner
are self-contained. The canonical 60-second run completed in 3.764 seconds,
423 checks and 22 effective mathematical mutations. These are author checks,
not independent review or an audit verdict. The isolated checkout was clean
and its HEAD equaled its remote before removal. PR8092_DELIVERY.json records
the verification. DISK_SWEEP_20260913.json records the additional clean,
main-contained checkout removed without touching archive directories or gc.

Cold review narrowed all-real-F language to a common quadratic form (a metric
when invertible), retained the constant-frame smallness condition, and removed
the overbroad assertion that nonuniform frames cannot have global momentum.
The full frame derivative includes C(F). The optimized symbolic checker has
the same 160 assertions and now takes 1.735 seconds; algebraic expansion before
general simplification changes execution cost, not the tested identities.
The milestone also removed duplicate route reporting inside nested loops;
its preserved recovery packet distinguishes path enumeration from independent
evidence. No independent review has been obtained in this personal run.

The next high-value question is the metric action and its reciprocal source
on this same carrier. Current-main gravity sources were read before selecting
it: the full finite-k W Hessian note of June 9 and all 493 lines of its primary
already identify a declared 3D Euclidean midpoint-link Hessian. Its Ward-selected
improvement is a different coupling and the detailed finite results explicitly
leave Einstein dynamics and scaling open. The finite TT, stress-seagull,
staggered TT, cosmological, quartic/quintic Ward and canonical-channel notes
were also read. These are not a 3+1 Hamiltonian vacuum response of the present
two-node carrier. Their finite channel findings must not be imported as that
response, and their negative rhetoric does not exclude a different continuum
limit or coupling.

The June 17 Sakharov summary contains an internal normalization issue: its
displayed matching 1/(16 pi G)=(4 pi)^(-2) Nf Lambda^2/3 algebraically implies
G=3 pi/(Nf Lambda^2), whereas it prints 48 pi^3/(Nf Lambda^2). Its primary
prints that matching rather than deriving it. This is a source-review finding,
not a correction of physical Newton normalization, which needs determinant,
regulator and action conventions. No source or audit status has been changed.

Rerank: derive the full strain response and its universal infrared tensor
before attempting to identify induced Einstein dynamics. Keep the local
zero- and two-derivative action coefficients explicit; their signs and values
can depend on the supplied metric coupling and counterterms. Further error-bound
variants or additional lapse means would add less information at this point.
Continue personally until 2026-09-14T00:14:41Z.
