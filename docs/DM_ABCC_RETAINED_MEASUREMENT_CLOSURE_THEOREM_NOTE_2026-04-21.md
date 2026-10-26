# DM A-BCC supplied endpoint comparison and conditional path implication

**Date:** 2026-04-21; corrected 2026-10-21
**Type:** open_gate
**Status:** finite supplied fixtures; physical source/path selection open.
**Scope:** finite Hermitian endpoint computations on supplied decimal coordinates;
conditional inertia-continuity implication. No physical basin-selection closure.
**Primary runner:** `scripts/frontier_dm_abcc_retained_measurement_closure_2026_04_21.py`

## Supplied objects

Supply the Hermitian family H(m,d,q)=H_base+m T_M+d T_D+q T_Q, with
E1=sqrt(8/3), E2=sqrt(8)/3, gamma=1/2, and

```text
H_base = [[0,E1,-E1-i gamma],[E1,0,-E2],[-E1+i gamma,-E2,0]]
T_M = [[1,0,0],[0,0,1],[0,1,0]]
T_D = [[0,-1,1],[-1,1,0],[1,0,-1]]
T_Q = [[0,1,1],[1,0,1],[1,1,0]]
Basin 1 = (0.657061342210, 0.933806343759, 0.715042329587)
Basin 2 = (28.005676879468, 20.721919153777, 5.011726669406)
Basin X = (21.128264303040, 12.680028385305, 2.089234625632)
```

These literal decimal triples are supplied examples, not solutions derived or
certified complete by this note. The labels preserve the earlier package's
nomenclature; they do not identify a physical state or establish PMNS fits.

## Finite result

At these supplied endpoints the runner constructs the matrices and computes
both their determinants and Hermitian eigenvalues. H_base and Basin 1 have
inertia (one positive, two negative); Basin 2 and Basin X have inertia
(two positive, one negative). Basin 1 also satisfies d+q>sqrt(8/3).
The determinant sign alone is not a complete inertia certificate for arbitrary
Hermitian matrices, so the eigenvalue counts are checked explicitly. Numerical
eigenvalue separation and determinant/product agreement are finite floating-point
controls, not interval certificates for nearby fitted solutions.

## Conditional mathematical implication

For any continuous path of nonsingular Hermitian matrices starting at H_base,
the inertia remains (1,2): ordered eigenvalues are continuous and none can cross
zero. Thus a path to either of the two supplied opposite-inertia endpoints must
be singular somewhere. This says neither that every path crosses exactly once
nor that the particular straight path to Basin 1 is nonsingular.

Equal inertia places matrices in the same component of the full nonsingular
Hermitian space, by unitary diagonalization and sign-preserving interpolation
of eigenvalues. It need not put them in the same connected component of a
restricted affine source surface. No restricted-component identification is
made here without a path witness.

## Withdrawn integration conclusion and recovery

The original source at Git commit
`f24d17d97d372df977476e4a69674577f31af575` executed seven upstream runners and
accepted their exit codes and selected stdout phrases as an A-BCC closure
certificate. Its literal three-basin table was not an exhaustive source census.
That source and its negative review evidence remain recoverable; its 15/0 run
is evidence of the old runner's behavior, not physical selection.

The former claims that the complete active chart is exactly these three basins,
that a sigma-chain physically selects Basin 1, and that later current/packet
notes close the microscopic selector are withdrawn. Finite candidate checks,
supplied branch restrictions and coordinate recovery do not establish those
claims. The current default executes no subprocess dependencies or stdout-authority
checks; dormant historical utilities remain preserved but are not invoked.
Its scientific inputs are the displayed supplied matrix and decimal constants;
the paired note is declared as provenance context.

The original dependency names remain historical context, not current premises:
`DM_ABCC_PMNS_NONSINGULARITY_THEOREM_NOTE_2026-04-19.md`,
`DM_ABCC_SIGNATURE_FORCING_THEOREM_NOTE_2026-04-19.md`,
`DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md`,
`DM_SIGMA_HIER_UPPER_OCTANT_SELECTOR_THEOREM_NOTE_2026-04-20.md`, and
`DM_ABCC_FIVE_BASIN_CHAMBER_DPLE_SUPPORT_THEOREM_NOTE_2026-04-21.md`.
Their independent scopes must be assessed before any stronger composition.

## Open obligations

Physical source selection, exhaustive PMNS-compatible basin classification,
certified path nonsingularity on a selected physical source, and an actual
framework-to-measurement bridge remain open here. This note does not prove an
axiom-level no-go or alter an audit status. The original claim identifier and
filename are retained for traceability, not as a closure assertion.

## Verification

`python3 scripts/frontier_dm_abcc_retained_measurement_closure_2026_04_21.py`
computes the finite matrix facts above and exits nonzero if a required check
fails. It does not execute the historical upstream theorem stack.

## Conditional context, not inherited closure authority

- [conditional signature](DM_ABCC_SIGNATURE_FORCING_THEOREM_NOTE_2026-04-19.md)
- [PNS diagnostics](DM_PNS_ATTACK_CASCADE_NOTE_2026-04-19.md)
- [nonsingularity context](DM_ABCC_PMNS_NONSINGULARITY_THEOREM_NOTE_2026-04-19.md)
