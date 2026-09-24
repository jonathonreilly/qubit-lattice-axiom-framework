# Milestone-six publication comparison

No material mathematical, source-adaptation or completed-evidence discrepancy
was found in the specified publication. The positive time-integrated variance
lower bound and the separately attributed PRE enhancements are supported
within the stated conditional model and provisional parent assumptions. This
is a bounded final comparison against preserved PRE/POST evidence, not a new
blind derivation or formal audit.

## Exact scope and identities

The publication root is
`/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/integrated-variance-publication`.
Its observed base revision is
`c234d47c9d99b7fd5590957ec08d9083877d25e6`.

The complete 466-line note and 283-line runner were read:

| Source | SHA256 |
| --- | --- |
| `docs/TIME_INTEGRATED_MICROSCOPIC_CUBE_BIRTH_VARIANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `f667f03f5b6b9fd1e50e3c01f800e19d754dae8281354ff2d0196d97ddbd44ae` |
| `scripts/time_integrated_microscopic_cube_birth_variance_2026_09_24.py` | `1482440722ca5c91dea2067b0c0ba2024c1c2a31ea93bf1736fe62c5fcaa48bc` |

`SIXTH_PUBLICATION_FROZEN_SOURCES.json` is in that publication root, rather
than directly in the external campaign base. Its declared source hashes and
base revision agree. The external execution record and wrapper log were also
read and verified. Exact absolute paths and all reviewed source/evidence
hashes are preserved in `PUBLICATION_COMPARISON_SOURCE_PINS.json`.

The independent PRE and POST remain unchanged, respectively at SHA256
`57819426fec612dcb000612dcb8419cca34d3538904dcaefea13fb4820181d8e` and
`5a53e72b0efa31bfd73d3d94246378a7748cf0e71f7f1f28a3ef374334e5f9d5`.
Their seals and sealed evidence were reverified. The previously reviewed
transitive parents were reused at their unchanged identities. The complete
`averaged-variance-personal/PRE_EXTENSION_ROOT_REVIEW.md` was read; it
accurately records a post-disclosure review of the PRE enhancements.

## The published mathematical claim

The publication keeps the original compensated lambda=0 cube, actual
normalized first birth, complete original subsequent ensemble, positive
fixed delta, K and kappa, and the supplied joint spin scaling. Its first-birth
ket is now explicitly `j_i F_infinity Omega/sqrt(b_i)` with Omega in N=4.
The subsequent maps `B_j=j_j F_infinity P` act from N=6 to N=8. This removes
the earlier harmless reuse of notation across those two roles.

The physical observable remains the Hermitian microscopic H. The exact
no-event generator is `H-i kappa Gamma_S/(2 epsilon^2)`, and the terminal
N=8 energy is zero. Therefore the full ensemble has second moment
`||H v||^2`, without survival normalization. The low-vector identity, weighted
trajectory estimate, rectangular Sylvester inverse and probability coefficient
from the frozen root proof are carried over correctly. The global low
operator norm and the bound on the actual low trajectory are kept distinct.
The Sylvester estimate retains its dimension-independent operator-norm proof.

For each fixed `0<a<b<infinity`, the claimed lower bound is

    liminf epsilon^2 integral_a^b Var_H(rho_i(t)) dt
      >= (kappa/2)[S_i(a)-S_i(b)]
      >= (kappa/2) exp(-16 kappa a)
                    [1-exp(-2 kappa(b-a))] > 0.

Sections 5 and 6 correctly add the following PRE-origin results and identify
their origin explicitly.

1. Equation (17) retains the nonnegative derivative remainder
   `epsilon^2 integral ||v'||^2`. The exact energy identity has the correct
   positive endpoint coefficient. Its boundary term after integration is
   `(kappa/2)[<v,Gamma_S v>]_a^b=O(epsilon^2)`. The controlled limit of
   `Gamma_S v/epsilon` supplies the displayed survival coefficient.
   Replacing that survival difference by the actual microscopic second-birth
   probability increment is justified by uniform no-event norm convergence.
2. Equation (18) alternatively retains
   `epsilon^2 integral ||H E_1 v||^2`. Its integration-by-parts estimate and
   the inherited `E_1 v=O(epsilon^(9/4))`, `E_2 v=O(epsilon^4)` bounds give
   the stated vanishing cross terms. The first bound applies after
   `t>=epsilon`, which is sufficient on every fixed `[a,b]` with a>0 for
   small epsilon. The coarse `O(epsilon^(-7/2))` upper bound is consistent
   and is not described as sharp.
3. The physical-star direct-sum proof establishes
   `2 I <= Lambda <= 16 I` on the physical rotor N=6 low sector. Freezing
   exterior fields and charges leaves each star field determined by Gauss's
   law; the rotor has no boundary deleting local entries. The unsigned
   same-sign block supplies a positive local Gram bound, while the
   opposite-sign block supplies only nonnegativity and an upper bound.
   The two active stars have disjoint occupied pairs, so the unique negative
   charge cannot remove both local lower bounds. This is the required
   operator argument for arbitrary physical superpositions.

The lower and upper rotor loss estimates give the survival inequality and
strict interval positivity with the stated constants. No corresponding
finite-spin lower bound is inferred. The complete proof retains both matter
and field, and does not substitute a rotor tail at a growing fast time.

The published restrictions remain necessary and correctly stated: the
interval is fixed and bounded away from zero; parameters and model are fixed
as specified; the ordinary-energy parent is provisional; neither unresolved
remainder is shown to vanish. The result supplies neither pointwise variance
behavior nor a sharp asymptotic for the full integral. The physical apparatus
and total-energy questions remain open. The machine-status block preserves
conditional support and the requirement of a formal audit before effective
retained status.

## Runner extraction and new local-star control

The four inlined builder functions `complete_spin_one`, `jump_matrix`,
`canonical_preparation` and `riesz_action` have identical ASTs to the pinned
ordinary-energy builder at SHA256
`4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d`.
The exact exponential-integral and three-grade functions are also unchanged
from the frozen author controls. In the cube control, the previous guarded
runtime import is replaced by calls to those identical local definitions;
its provenance record is adjusted accordingly. No numerical model change
was found. The original-word helper definitions are likewise unchanged.

The new local-star function builds the unsigned matrices from the local
charge rules, obtains Gram spectra `1,1,4` and `0,1,1,3,3,4`, and checks all
36 vacancy/negative-site labels. Their coverage counts are 24 labels with
one guaranteed same-sign center and 12 with two. Every coverage row agrees
with the preserved PRE after translating its explicit charge-vector labels.
Its alternative oriented matrix has a kernel as expected; that alternative
is not used for the supplied hopping convention.

Only this small new author function was replayed by AST extraction, and its
entire result equals the cache. This is a source-consistency check, not a
new independent reconstruction. The written physical-star argument supplies
the full rotor quantifier. The primary and expensive unchanged cube controls
were not rerun. The finite S=1 results remain clearly labeled as finite
corroboration outside the theorem's joint scaling.

## Completed cache and wrapper incident

The canonical cache has SHA256
`798d06fc344c941c72841aee55de266044d3e83771c9faebad6edc36c2416406`.
It records primary status `ok`, exit code 0, timeout 240 seconds and elapsed
time 47.67 seconds. The five-input fingerprint was recomputed directly from
the declared ordered paths and their complete bytes using the cache format:

    7cf998c03e1131be4115269ca68c9279ce49544e944d3c6e74d95f5ba9e3332b

It matches the header, and the runner hash matches the frozen source. The
full cache was read. Its stdout is below the truncation threshold and contains
exactly four complete JSON objects followed by `TOTAL: PASS=4 FAIL=0`.
The first three objects exactly match the three cube rows in the aggregate;
the fourth exactly matches the entire result file, whose SHA256 is
`4a6501b933299c5ac6a658b615725b8bc47ebdfaa613bb9fe6b3947137ff7958`.
Stderr is empty. All reused exact-word and toy values equal their frozen
author results, and every reused cube scientific value equals its earlier
result after excluding only elapsed-time fields.

The external execution record agrees with those observations. The wrapper
log retains `TypeError: vars() argument must have __dict__ attribute`.
The inspected cache API returns a dictionary only after writing the cache,
consistent with the reported failure in the later wrapper. The successful
primary record and the wrapper failure are distinguished; the exception is
not hidden or recast as a primary-run failure. This comparison neither
restamped the cache nor repeated that run.

The deterministic comparison script, complete log and JSON record are included
in this comparison's seal. All verification assertions completed successfully.
The publication, its cache and formal audit state were not modified.
