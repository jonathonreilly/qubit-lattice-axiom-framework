# Checked coupled response of the constructed cosmology

Direct campaign lead calculation, completed 2026-10-13. Conditional-support;
no formal audit status, independent empirical validation or TOE claim.

The supplied canonical two-scalar action and constructed dust expansion give
an exact coupled scalar/dust/metric linear system. The physical density and
optical potentials follow from the universal conformal matter metric. For
the short-wave, slowly evolving matter branch, with no independently large
free scalar wave, the leading responses are mu=1, Sigma=1/(1+a), and
gamma=(1-a)/(1+a). The supplied m=.3 growing-mode equation matches the same-m
GR comparison in that limit. Finite wave-number corrections are explicitly
integrated, not silently discarded.

The exposed E_G summary at z=.32 gives .44102737734973785 for a=1/2499,
versus .44120385889329516 for same-m GR and the historical submitted-paper
summary .392+/-.065. The standardized candidate residual is .75427. The
paper's extra approximately 5 percent calibration scale is separate. Its
geometry, tracer bias, projections and simulation corrections were not
reprocessed. This is an exposed summary diagnostic, not a survey likelihood
or a new test independent of model development.

The exact vacuum family has a neutral scalar-u direction. Its unforced
linear modes and the resonant response to a decaying dust-density source are
derived separately. The selected u=0 member is not uniquely attracting among
the vacuum family. Finite-density response was checked with 160 nonlinear
integrations and four variational integrations; their finite-time damping
does not establish a global basin, initial-condition selection or complete
physical stability. The density coordinates require sigma>0 and comparisons
are at fixed Einstein log scale, not fixed physical redshift.

The first parent run passed 648 controls. A complete independent proper-time
derivation checked the constraints, trace, scalar equations and homogeneous
variation. Its prose findings were accepted in DIRECT_PERTURBATION_RESPONSE_v2.md:
the constraint and trace cannot test the scalar-u acceleration, vacuum mode
formulae require zero dust perturbation unless the forcing term is added,
and positive-density/fixed-coordinate limitations are explicit. Original
proof and execution remain preserved.

The independent numerical reconstruction passed 1,489 controls using
proper-time dynamics, conserved particle number and projection of tangents
onto fixed Einstein log scale; a further 705 controls checked derivatives,
lineage and the adversarial source mutation. It independently reproduced the
stored predictions. It also demonstrated a real validation failure: removing
the scalar-u/chi coupling from the original implementation still passed all
648 original controls, while changing all 16 basis-response cases. The
original equations were correct; their controls were incomplete.

Parent v2 adds 30 complex-step potential-Hessian controls and 120 comparisons
of the full seven-by-seven evolution matrix against the proper-time
covariant equations. All 798 controls pass. The maximum normalized operator
error is 1.107665544182402e-15. Every one of the seven original scientific
sections and all 648 original check records is exactly unchanged. The same
independent reviewer rebuilt the operator through a separate coordinate
matrix transformation with 65-digit potential derivatives: 512 affected
controls pass. The same omitted-coupling mutant now fails all 120 operator
checks. This closes the demonstrated gap, without asserting that a finite
fixture set detects every conceivable implementation error.

The parent read both complete original reports and affected reports, and
verified 112+138 mathematical and 83+55 numerical source/evidence path
identities. Exact review reports, source snapshots, failed mutants, execution
logs, predictions and receipts remain in the two independent review folders.
The first numeric review receipt is
5f11f2a9cbcfa943d45949cf84aaf0fd2a51bb3004f489af15da46bac88306cb;
its affected confirmation receipt is
53d6d4537273f848f44d33dd98004154ab8d1a1a1f23a3a267bdd470ef006a66.

The next physical obligations are radiation and baryonic transfer,
primordial fluctuations and their preparation, matter/clock matching,
nonlinear structure, raw observations, vacuum-energy scale, and quantum
completion. The constructed background remains chosen from already exposed
information; none of these checks makes that choice an independent
prediction.
