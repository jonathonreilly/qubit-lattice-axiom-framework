# Mixed-preparation publication comparison

No material mathematical, scope or source/evidence discrepancy was found.
The complete published note and adapted runner agree with the sealed PRE/POST
within the conditional fixed-finite-span claim. No source repair is required
for that scope. This is a final comparison of released sources, not a new
independent reconstruction, formal audit or adoption of the parent premises.

## Source boundary and preserved record

The publication tree was read at HEAD
`e846ee9d4133f65d3778fa4dc36524a9ada6db6b`, the unchanged PR9079 base.
The four requested publication identities match exactly:

| File | SHA256 |
| --- | --- |
| `docs/MIXED_LOW_FIELD_INPUTS_RETAIN_CUBE_BIRTH_ENERGY_AND_COHERENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `04bf4ad2def6a5d8e7a0ab711d4e6e52d1933eb9d28366b1cdb5dee1383d9726` |
| `scripts/mixed_low_field_inputs_cube_birth_energy_and_coherence_2026_09_24.py` | `ec6abee27fc084839d8c50f8d386ffc20010668bbcb681044ff8be0827bfb802` |
| `outputs/mixed_low_field_birth_energy_20260924/MIXED_PREPARATION_CONTROL_RESULTS.json` | `60d3ee81cc9a35b6e396a383f93c95a400b4dd803f3984779d0fe4d178c2d6e1` |
| `logs/runner-cache/mixed_low_field_inputs_cube_birth_energy_and_coherence_2026_09_24.txt` | `125a86e284d83feee379c89948ff6acd4a511cf222defb7b4fcb812a229a3515` |

The PRE and POST hashes remain, respectively,
`b0820179fddd987438afbe69acef5912813d93530050a8ef67156292a4f21647`
and `52df4b1f7dd3a94dcf7f27e41548d11d141893f646e6df220ed5b42502da2c46`.
Their seals and all five PRE and three POST members were reverified unchanged.
The released author proof/control seals and every member also remain unchanged.
All five analytic parents in the published runner have the exact hashes used
in PRE. Their established estimates were reused without recertification.
Absolute paths and every reviewed source/evidence hash are recorded in
`PUBLICATION_COMPARISON_SOURCE_PINS.json`.

## Mathematical scope and source adaptation

The publication retains the original lambda=0 compensated model, joint spin
scaling, canonical Hermitian preparation, and original plus/minus/coherent
marks. A single finite physical N=4 low electric-word span is fixed as
epsilon tends to zero; the density, its coherences and rank may vary inside
that span. The local operator Gram identities and finite-spin diagonal
weights match PRE/POST. The coefficients `(b,r)=(2,4),(2,2),(4,6)` and the
actual selected normalization yield the stated conditional mean
`delta(r/b) epsilon^-2+O(1)` and variance
`delta^2(r/b) epsilon^-6[1+O(epsilon^2)]`.

The added explicit weighted estimate is safe: a unit shift on one link obeys
`w(E+/-e)<=3 w(E)` for `w=1+sum E_e^2`, and applying the reverse shift gives
the reciprocal bound. The diagonal D/C commutes with w. Thus the previously
reviewed weighted canonical series argument still supplies bounded low
energy-vector action for the stated fixed input class; it does not assert
a bounded global low-band Hamiltonian norm.

The density-independent paired-isometry witness, its probability weight,
input-Fisher subtraction and noisy-error amplification retain their reviewed
orders. The apparatus Fisher conclusion uses selected unhalved trace error
`o(epsilon^3)` and the finite initially product additive-covariance premises.
It is not inferred from mixed-state variance. The explicit coherence-bandwidth
definition is consistent with the finite-frequency lemma, and the exact input
low-band width remains `O(epsilon^-2)`. This preserves the lower coefficients
`4 alpha^2 delta^2 r` for scaled apparatus Fisher and `delta` for scaled
coherence bandwidth and spectral diameter.

The one-input attaining relaxation still uses an input-dependent preloaded
mixed state, retains the selected probability, and has selected error
`O(epsilon^4)`, bounded mean above the ground energy and matching leading
Fisher/range coefficients. It is not a universal implementation of the mark,
nor does it attain every prescribed tolerance below `o(epsilon^3)`.
Growing support, spin-boundary families, different conservation hypotheses,
later-time variance and continuous-time rate identification remain outside
the claim. The moving-boundary counterexample and conditional parent status
are preserved. The new provenance paragraphs correctly distinguish the
sealed author controls from the separately written PRE controls.

## Completed evidence correspondence

All ten computational helper/control functions are AST-identical to the
frozen author script. After removing the output-directory creation and final
`TOTAL` print, main is AST-identical as well. The fully inspected source diff
contains only the shebang/docstring, timeout/input declarations, output path
and those two main additions. There is no new scientific implementation or
external builder reuse introduced by this adaptation.

The ordered six-input fingerprint was recomputed from the actual source
bytes using the canonical cache encoding. It equals the cache header:
`dde9bf0b61f22fd12c6b927c0deb2f8d9da890b9e64bdb8e528b84689622dc77`.
The runner hash also matches the header and result. The cache records exit 0,
status ok and elapsed 0.30 seconds. The authorized root receipt's matching
EIGHTH entry records 0.29747700691223145 seconds, one stdout object and zero
stderr bytes, consistent with the rounded cache time and empty stderr body.

The entire cache stdout contains one complete JSON object followed only by
`TOTAL: PASS=2 FAIL=0`; its 63,786 characters are below the cache limit. The
JSON text matches the full published result byte for byte apart from its
terminal newline. Every scientific value equals the sealed author result
exactly after removing only the top-level elapsed time and source hash.
The complete original result rows were already inspected in POST; exact
correspondence permits their reuse. The local operator controls and mixed
two-band example retain their stated finite scope. Their agreement does not
prove the joint limit or realize an apparatus.

The read-only bookkeeping script `publication_evidence_checks.py` completed
with exit 0; its complete JSON/log preserve these checks. No physics runner
was imported or rerun. No unrelated active scientific packet was read, and
all new files are confined to this independent directory. Publication,
retained and audit state were left unchanged. There are no material findings
requiring correction in the reviewed publication.
