# Universal QG Optional Textbook Comparison Note

**Date:** 2026-04-15 (originally); 2026-05-05 (meta retag for re-seed);
2026-05-06 (zero-authority runner closure); 2026-07-10 (finite-predicate
closure)
**Type:** meta
**Status:** audit-checkable packaging hub for optional textbook-comparison
crosswalks against the universal-QG canonical textbook closure target.
**Not** a theorem, claim, or new authority surface.
**Authority role:** zero — this row exists only to anchor a citation hub
for downstream universal-QG notes that need a stable target for "optional
textbook comparison" callouts.
**Audit target:** the finite repository predicate `Z := Z0 AND ... AND Z5`
below, and no scientific proposition.
**Status authority:** independent audit lane only; the runner supplies a
repository-state certificate, not an audit verdict.
**Primary runner:** `scripts/universal_qg_optional_textbook_comparison_meta_check.py`
**Runner cache:** `logs/runner-cache/universal_qg_optional_textbook_comparison_meta_check.txt`

The runner is a metadata invariant check only; it is not a physics
derivation.

**Audit-readiness metadata repair (2026-06-17).** This source-side repair
exposes the runner and cache in plain header fields and makes the runner fail
if the cache metadata is removed. It does not change this row's zero-authority
role and does not assert an audit outcome.

## 0. Scope retag (2026-05-05)

This rewrite adds an explicit `**Type:** meta` header and removes theorem-like
section names from the body. The note is a packaging row only: it gives
downstream universal-QG notes a stable place to cite optional textbook
comparison callouts, but it does not assert a theorem, introduce a physics
runner, or provide authority for any physics step. The 2026-05-06 runner added
above checks only the metadata boundary.

## 1. Auditable zero-authority invariant

The auditable item in this row is the following repository metadata
invariant, not a continuum theorem:

- `Z0`: the source row is typed as `meta`.
- `Z1`: the status line explicitly negates theorem, claim, and new authority
  roles.
- `Z2`: the authority role is `zero`.
- `Z3`: this note has no markdown links to other docs, so it registers no
  upstream theorem dependency edge for itself; cross-references below are
  code-span filenames for navigation only.
- `Z4`: the complete packaging-only source body is SHA-pinned by the runner;
  in that pinned body every substantive textbook-comparison result is forced
  out to its own claim row with its own load-bearing step, runner, and audit.
  Any source change invalidates the pin until the source and runner are
  reviewed together and the cache is refreshed.
- `Z5`: current inbound mentions of this filename are guarded as optional
  packaging callouts rather than load-bearing theorem authority.

The primary runner replays `Z0`-`Z5` directly against the repository text. A
passing run certifies only this zero-authority metadata guard. It does not
certify, import, or strengthen any universal-QG continuum, weak-measure,
geometric-action, or textbook-equivalence theorem.

### Finite closure certificate

Let `N` be this source file and let `D` be the finite set of current Markdown
files under `docs/`, excluding `N` itself and the entire `docs/audit/` subtree.
That subtree contains audit infrastructure, generated audit surfaces, and
audit history rather than current dependent claim notes. Define:

- `S(N)` to mean that `N` satisfies the source-local guards `Z0`-`Z4`;
- `I(N,D)` to mean that every current inbound occurrence of this filename in
  `D` has both an optional-comparison marker and an explicit non-authority /
  packaging guard; and
- `Z(N,D) := S(N) AND I(N,D)`.

The runner reads and SHA-pins all of `N`, enumerates `D`, and evaluates every
conjunct in this definition. Therefore a passing run closes `Z(N,D)` for the
checked checkout by finite inspection. This exhaustiveness is the entire
derivation burden of this meta row. It neither assumes nor establishes the
truth, completeness, or audit grade of any physics note named below.

The certificate is falsified if any source-local guard fails, if this note
acquires a markdown dependency edge, or if any current inbound occurrence is
not explicitly optional and non-authoritative. Any edit to this source,
including a substantive textbook comparison added here, invalidates the `Z4`
source pin; such a comparison must be moved to its own claim row before a
reviewer refreshes this metadata certificate.

## 2. What this note is for

The phrase "canonical textbook continuum target" is a navigation label here,
not a statement about that target's truth, completeness, or audit grade. This
note is a packaging hub providing a stable citation target for downstream
universal-QG notes that need a named row to attach optional-comparison callouts
to:

- public convention comparison;
- manuscript appendix packaging;
- notation / normalization crosswalks against alternate textbook packages.

It carries **no** derivation, **no** new claim, **no** physics runner, and
**no** authority. Its only runner is the metadata invariant check named
above. It is infrastructure metadata for the universal-QG citation graph.

## 3. What this note is *not* for

This note **must not** be used to:

- assign, change, or extend the status of the universal-QG theorem stack;
- introduce a new "comparison" claim that the audit lane would have to
  ratify;
- act as a one-hop authority for any downstream theorem;
- substitute for the claim row that supplies the canonical textbook continuum
  closure.

If a universal-QG downstream note needs a *substantive* textbook-comparison
result, that must live in its own claim row with its own load-bearing
step, runner, and independent audit review — not here.

## 4. Cross-references (informational only)

The universal-QG canonical textbook closure parent and sibling claim rows are
not load-bearing for this meta packaging note. They are listed here only so a
reader landing on this row by citation can navigate to the substantive rows:

- `UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE.md`
- `UNIVERSAL_QG_CANONICAL_SMOOTH_GRAVITATIONAL_WEAK_MEASURE_NOTE.md`
- `UNIVERSAL_QG_CANONICAL_TEXTBOOK_GEOMETRIC_ACTION_EQUIVALENCE_NOTE.md`
- `UNIVERSAL_QG_CANONICAL_TEXTBOOK_WEAK_MEASURE_EQUIVALENCE_NOTE.md`
- `UNIVERSAL_QG_CONTINUUM_BRIDGE_REDUCTION_NOTE.md`

These are the substantive claim rows. This note is *not* one of them, and its
metadata certificate does not assign any grade to them.
