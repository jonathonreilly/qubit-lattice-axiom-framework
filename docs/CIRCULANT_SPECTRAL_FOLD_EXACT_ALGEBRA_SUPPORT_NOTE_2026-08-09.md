# Exact algebra of the three-dimensional Hermitian circulant spectral fold, with one measured signed-root scan

Date: 2026-08-09

Authority: none

Audit: unset

Status: proposed_retained

Claim type: bounded_theorem (support only; every unit is bounded to the
definitions stipulated in this file and restated in the runners, and section 8
is labelled a measurement wherever it appears)

Sections 1 to 7 below are exact rational/integer mathematics on objects
stipulated in this file and restated in the runners; section 8 is an
explicitly measured comparison against imported charged-lepton masses. This
package makes statements about those stipulated objects and about nothing
else: it derives nothing from the framework axioms, identifies nothing with a
physical quantity, and selects among nothing. Every unit says what it does
NOT establish.

Imports: three measured charged-lepton masses, used only in section 8 and
named there with their in-repo provenance; the classical irrationality of pi,
cited in section 7 for the unbounded form of a statement the runner verifies
only on a declared finite family. Nothing else. All other definitions are
stipulated in this file and restated in the runners, which pin no axiom bytes,
read no note, execute no git-history object, and consume no fitted value.

Runners:

- [`salvaged_circulant_spectral_fold_2026_08_09.py`](../scripts/salvaged_circulant_spectral_fold_2026_08_09.py)
  (primary; 45 computed checks, fail-closed, exit 0 only on full PASS;
  no declared file inputs and no generated output on a normal run)
- [`salvaged_circulant_spectral_fold_independent_check_2026_08_09.py`](../scripts/salvaged_circulant_spectral_fold_independent_check_2026_08_09.py)
  (independent check; 35 computed checks; each unit listed in its docstring
  is recomputed by a different exact method, and that list is the honest
  statement of its coverage; it additionally executes the primary as a
  subprocess to a temporary path, requires exit 0, recomputes the payload
  digest, compares the fresh payload against a
  canonical summary assembled from its own methods, and runs two tamper
  regressions every time — a byte tamper must break the digest, and the same
  tamper to a selected canonical-summary field with a recomputed self-digest
  must still be rejected by the selected-summary comparison)

Constitutional effect: none. This package changes no axiom, foundation,
primitive, dependency policy, queue, audit result, or audit status.

Reproduction: both runners are self-contained Python 3 standard-library
programs. `python3 scripts/salvaged_circulant_spectral_fold_2026_08_09.py`
then `python3 scripts/salvaged_circulant_spectral_fold_independent_check_2026_08_09.py`;
both exit 0 with the check counts above from a checkout containing this note
and its two runners, without a ledger, monolith, or other science artifact.
Normal verification writes no repository output; the independent check uses
only a temporary payload emitted by a fresh primary subprocess.

## The stipulated objects

All of section 1 to 7 lives on these definitions and on nothing else.

- `C` is the 3-cycle permutation matrix acting by `(C v)_0 = v_2`,
  `(C v)_1 = v_0`, `(C v)_2 = v_1`.
- `H(a, b) = a I + b C + conj(b) C^T` for a real number `a` and a
  complex number `b = x + i y`; `B = |b|` and `delta = arg b`, so
  `x = B cos delta` and `y = B sin delta`.
- `e1`, `e2`, `e3` are the characteristic-polynomial coefficients of
  `H`: the trace, the sum of the principal 2-by-2 minors, and the
  determinant.
- `Phi = (1/3) arccos(cos 3 delta)`, the folded argument recovered from
  an unordered spectrum when `B > 0`.
- `I_alpha(v) = alpha (v_0 + v_1 + v_2)` on `Q^3`, for rational `alpha`.
- `2/9` is a stipulated rational comparator constant. Nothing in this
  package identifies it with any physical, lattice, or measured
  quantity; it appears only as the number against which two exact
  statements and one measurement are reported.

## 1. The family is self-adjoint and its characteristic coefficients are exact

Exact results, verified as polynomial identities over `Q(i)[a, x, y]`
by the primary and independently on a 4-by-4-by-4 grid of 64 distinct
rational points by the checker (both sides have degree at most three in
each variable, so grid agreement proves the identity):

    H = H^dagger identically
    e1 = 3 a
    e2 = 3 a^2 - 3 (x^2 + y^2)
    e3 = a^3 - 3 a (x^2 + y^2) + 2 (x^3 - 3 x y^2)

The reduction `x^3 - 3 x y^2 = B^3 cos 3 delta` is the triple-angle
identity, verified exactly in the form
`(c^3 - 3 c s^2) - (4 c^3 - 3 c) = -3 c (c^2 + s^2 - 1)`, which vanishes
on the unit circle.

The three discrete-Fourier vectors `v_k = (1, w^k, w^{2k})`, with `w` a
primitive cube root of unity, satisfy `C v_k = w^{-k} v_k` and
`C^T v_k = w^{k} v_k`; both actions are computed from the stipulated
matrix rather than written out by hand, exactly in the Eisenstein
integers by the primary and, by an explicit matrix-vector action in
`Q(i, w)`, by the checker. The per-index eigenvalue is therefore

    lambda_k = a + 2 B cos(delta - 2 pi k / 3)

with a MINUS sign in the argument for those eigenvectors. That sign is
pinned per index in both runners: each also requires the opposite
assignment to FAIL the eigenvector equation, so the orientation is a
computed fact and not a label. At the level of the unordered spectrum
the two conventions agree — the opposite convention `delta + 2 pi k / 3`
gives the same three-element multiset, because `k -> -k` is a bijection
of `Z/3` — and both runners verify that coincidence exactly (71 rational
turn samples in the primary, all 64 grid points in the checker).

Not established: any physical carrier, state, or readout. These are
statements about the stipulated matrix family only.

## 2. Exact inversion on `B > 0`, with the degenerate stratum excluded

Exact identities:

    e1^2 - 3 e2 = 9 B^2
    e3 - a^3 + 3 a B^2 = 2 B^3 cos 3 delta
    b^3 = (x^3 - 3 x y^2) + i (3 x^2 y - y^3)
    (x^2 + y^2)^3 = (x^3 - 3 x y^2)^2 + (3 x^2 y - y^3)^2

so on `B > 0` the unordered spectrum determines `a = e1/3`,
`B = sqrt(e1^2 - 3 e2)/3` and `cos 3 delta`, and the last identity — a
sum of two squares — bounds `|cos 3 delta| <= 1` exactly, so
`Phi` lies in `[0, pi/3]`. That bound uses only the squares of the two
parts of `b^3`, so the third identity above is carried as a separate
exact statement: both parts are pinned with their signs by expanding
`(x + i y)^3` and separating it, which is what the runners check. The
primary verifies the recovery forward on rational samples; the checker
rebuilds `(e1, e2, e3)` from the recovered parameters in the reverse
direction on all 64 grid points.

The exclusion `B > 0` is necessary, and an exact witness shows why:
`B = 0` forces `x = y = 0`, the spectrum is the triple root
`{a, a, a}`, the discriminant vanishes, and the recovery's denominator
`2 B^3` is zero. On that stratum the argument is not a coordinate at
all, and `Phi` is undefined rather than merely uncomputed. Both runners
evaluate that stratum directly.

Not established: any identification of the recovered parameters with a
measured or physical quantity.

## 3. The dihedral fold, with the endpoints qualified

Stipulated: the two maps `delta -> delta + 2 pi / 3` and
`delta -> -delta` on the argument circle.

Exact results. The unordered spectrum is invariant under both maps —
the first relabels the index by `k -> k + 1`, the second by `k -> -k`
together with the evenness of cosine. The generated group consists
exactly of the six maps `delta -> s delta + 2 pi k / 3` with
`s` in `{+1, -1}` and `k` in `{0, 1, 2}`, and its composition law is

    (s2, k2) . (s1, k1) = (s2 s1, (s2 k1 + k2) mod 3)

with the right factor acting first. The outer reflection sign multiplies
the inner translation; the group is the dihedral group of order six and
is not abelian, so the order of composition is load-bearing. Both
runners verify the law itself, by two different methods: the primary
identifies each of the 36 composites by its own action on five generic
arguments and compares it with the predicted element, and the checker
represents the six maps as permutations of one six-point orbit and
composes them as permutations. Each requires the resulting 6-by-6 table
to be a Latin square and the group to be non-abelian, and the two tables
are compared against the table in a freshly emitted primary payload.

For an unordered spectrum with `B > 0` the set of arguments in
`[0, 2 pi)` carrying it is exactly that orbit. Its size is **six
generically and three at the six fold endpoints**
`delta` in `{0, pi/3, 2 pi/3, pi, 4 pi/3, 5 pi/3}`, which are exactly
the arguments with `cos 3 delta = +-1`, that is `Phi` equal to `0` or
`pi/3`. The primary verifies the dichotomy and the endpoint
characterisation over 300 rational turn samples (60 of size three, 240
of size six) in `Q/Z`; the checker reproduces both by integer coset
arithmetic in `Z/N` with `N = 3q`. The count of six therefore holds off
the endpoints and the count of three holds at them; the six endpoints
are published above and are exhibited as witnesses by both runners.

Not established: anything about registration or about any physical
multiplicity. These are statements about the stipulated argument
circle.

## 4. `Phi` is a similarity invariant, not a form-class invariant

`Phi` depends on `H` only through `(e1, e2, e3)`, which are the
coefficients of the characteristic polynomial and hence invariant under
`H -> S H S^{-1}` for every invertible `S`. So `Phi` is invariant under
arbitrary similarity, and in particular under arbitrary unitary
conjugation — including conjugations that carry `H` out of the
circulant form class, which the primary exhibits and confirms by an
exact commutator test. The primary verifies invariance through the
trace/minor/determinant evaluation on exact Gaussian-rational
transforms; the checker verifies it through power traces and Newton's
identities. Both also exhibit a self-adjoint perturbation that does move
the coefficients, so the invariance is not vacuous.

Not established: any conservation law and any dynamics. Invariance here
is spectrum invariance and nothing more; it is strictly weaker than, and
not special to, any preservation property one might wish to attach to
it.

## 5. The 3-cycle permutation matrix: fixed line and normal-plane angle

Exact results: `C` is orthogonal, fixes the all-ones line, and its
fixed subspace is exactly that line (`rank(C - I) = 2`). The sum-zero
plane is `C`-invariant, and in the basis `u1 = (1, -1, 0)`,
`u2 = (0, 1, -1)` the restriction is exactly

    [[0, -1], [1, -1]]

with trace `-1` and determinant `1`, so it is a plane rotation with
`2 cos theta = -1` and `theta = 2 pi / 3`. The matrix is published entry
by entry and checked entry by entry, because trace and determinant alone
do not distinguish it from its transpose. The primary computes the
restriction in the explicit plane basis; the checker derives the same
angle from the characteristic polynomial `t^3 - 1` and the
Cayley-Hamilton relation `R^2 + R + I = 0` on the plane, and rebuilds
the same matrix from the images of the basis vectors.

Not established: any identification of this line, this plane, or this
angle with any physical space, direction, generation structure, or
angle. It is a property of a 3-by-3 permutation matrix.

## 6. The equal-coefficient linear functional

Exact results: `I_alpha(1, 1, 1) = 3 alpha`; the value is injective in
`alpha`; and in the tested rational family
`{0, 1/9, 1/3, 1, 2/27, -5/4}` exactly one member, `alpha = 2/27`, reaches
the stipulated comparator `2/9`. The checker recomputes all three by
coordinate summation rather than from the closed form.

Not established: any identification of `I_alpha` with a readout, any
statement about the full set of constraints such a functional might
satisfy, and any selection of a member by anything. Exhibiting an
expression that reaches a value selects nothing.

## 7. A bounded exact separation from multiples of `2 pi`

Exact result on a declared finite family: for every rational `q = m/d`
with `1 <= d <= 60` and `|m| <= 60` — 7260 pairs — the number `2/9` is
separated from `2 pi q`, with a verified separation of at least
`1.7595e-03`. The verification uses a rational enclosure of `pi` computed
in-file from an alternating arctangent series with its own tail bound
(Machin's formula in the primary, `pi = 4 arctan(1/2) + 4 arctan(1/3)`
in the checker, with the two enclosures required to overlap).

The unbounded form of the statement — `2/9` differs from `2 pi q` for
EVERY rational `q` — follows from the irrationality of `pi` (Lambert,
1761), which is cited classical mathematics, not a repository result.
The runners verify only the declared finite family.

Not established: anything about what any convention, readout, or
registration does or does not convert. This is arithmetic between a
rational number and rational multiples of `2 pi`.

## 8. Measured support only: the signed-root scan

This section is a MEASUREMENT, not a derivation, and nothing above
consumes it.

Stipulated: a sign assignment `(s_e, s_mu, s_tau)` in `{+1, -1}^3` maps
the three imported masses to the triple `lambda_k = s_k sqrt(m_k)`,
which is then fed to the section-2 recovery.

Imported values (measured, not derived here): `m_e = 0.51099895 MeV`,
`m_mu = 105.6583755 MeV`, `m_tau = 1776.86 MeV`. Their in-repo
provenance is the repository's charged-lepton comparator baseline
recorded in
[`CLOSURE_T2_DF_PHYSICAL_CONSEQUENCES_NOTE_2026-05-10_t2df.md`](CLOSURE_T2_DF_PHYSICAL_CONSEQUENCES_NOTE_2026-05-10_t2df.md);
that note records them as a PDG-2024 comparator baseline, and no
in-repo pin to a specific published edition or uncertainty is available.
They are observational comparator inputs and carry no derivational
weight.

Explicit conditions, all load-bearing for the numbers below:

1. the signed-root convention is a stipulated CONDITION, not a result —
   the three signs are chosen here, all eight choices are evaluated, and
   the value depends on which one is read;
2. the comparator `2/9` is a stipulated rational number, with no
   identification claimed;
3. the arithmetic is double precision, so the quoted digits are float
   measurements, not exact values.

Before any of those numbers is quoted, the primary checks its float
inversion against four stipulated `(a, B, delta)` triples pushed through
the section-1 eigenvalue formula and inverted back, so every sign in
that inversion is load-bearing for a value that is checked.

Measured, with the full table published and NO threshold applied: all
eight assignments were evaluated; ordered by distance to the comparator
the distances are

    7.409267e-06, 2.208323e-02, 2.724152e-02, 5.011466e-02,
    5.755116e-01, 6.027457e-01, 6.248363e-01, 6.528678e-01

The smallest belongs to the all-positive assignment; the next smallest
is about 2.98e+03 times larger. The checker reproduces all eight values
by an independent bisection method (modulus from the second central
moment, argument by bisection on the largest spectral value) and
reproduces the ordering.

Not established: any derivation of these numbers, any selection of the
sign convention by physics, any identification of `Phi` with a physical
readout, and any claim that the smallest distance is significant. A
measured near-coincidence under a stipulated convention is support, and
this note carries it as support.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: null
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "the downstream consumer is not yet known and this note names none; the exact algebra of sections 1 to 7 is available unchanged to any consumer that is later derived"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: "three charged-lepton masses used only in section 8, labelled measured support with their in-repo provenance named"
claim_type_reason: "sections 1 to 6 are exact rational/integer identities on definitions stipulated in the note and restated in the runners, each recomputed by a second independent exact method; section 7 is exact on a declared finite family of 7260 rational pairs, with the unbounded form cited to classical mathematics rather than proved here; section 8 is an explicitly measured comparison under a stipulated sign condition that nothing else consumes — so the live surface is bounded support, and the bounded_theorem target covers the stipulated-object statements only"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/salvaged_circulant_spectral_fold_independent_check_2026_08_09.py
```

The `packet_helper_runner` line declares the independent checker
claim-scoped and co-load-bearing: it does not import the primary, so the
packet builder cannot reach it by transitive imports, and no audit
packet for this note is complete without it. The matching entries must be
present in both packet consumers, as recorded below.

## Review record

This is a self-contained salvage. Closed, unlanded PR #5995 and its
ancestors grant no authority to this packet; their broad reclassification
and negative claims were dropped and are not inherited here. The retained
scope ends at the stipulated-object exact results in sections 1 to 7 and
the explicitly measured, comparator-only scan in section 8. No audit verdict
is applied by this record.

Hard landing condition: the following exact claim-scoped entry must remain
present, identically, in `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in both
`docs/audit/scripts/build_citation_graph.py` and
`scripts/audit_packet_script_deps.py`:

```python
"circulant_spectral_fold_exact_algebra_support_note_2026-08-09": [
    "scripts/salvaged_circulant_spectral_fold_independent_check_2026_08_09.py",
],
```

## Scope discipline, and what is mechanically scanned

Every limiting sentence in this note is a statement about what THIS
package establishes, on this package's own stipulated objects. Two of
those sentences are also enforced mechanically, and the enforcement is
described here at its true scope rather than at a wider one:

- the primary scans its own source text and the payload it can emit into
  its optional temporary receipt for the overclaim vocabulary of the
  review-loop conformance spec, section 3. The one span exempt from that scan is the
  token table itself, bounded by two marker comments, and a further
  check parses the exempt span and requires it to contain that table and
  nothing else;
- the independent check scans the surfaces the primary cannot reach: its
  own source, the primary's source, and the primary's freshly emitted payload.
  It also requires both exempt spans to be the same bounded table, so
  the two tables cannot drift apart;
- this note is not scanned by either runner: it is not inside the package a runner
  may read without breaking self-containment, and the repository's own
  controlled-vocabulary lint owns it.

Every section additionally carries a non-empty statement of what it does
not establish, on every surface — note prose, runner docstrings, emitted
strings, and payloads alike — and the primary gates the presence and
length of those statements.

This package asserts only the positive statements of sections 1 to 8, on
its own stipulated objects. It states no outcome of the kind the
repository's discipline gate for negative results governs, and it
presents no such gate as passed.

## Verdict

On stipulated definitions, the three-dimensional Hermitian circulant
family has exact characteristic coefficients, an exact spectrum
inversion on `B > 0` bounded by a sum-of-two-squares identity, and a
dihedral argument fold whose group has order six with composition law
`(s2, k2) . (s1, k1) = (s2 s1, (s2 k1 + k2) mod 3)` and whose preimage
count is six generically and three at its six endpoints; the recovered
argument is a similarity invariant, the 3-cycle permutation matrix
restricts to `[[0, -1], [1, -1]]` on its normal plane and so rotates it
by `2 pi / 3`, the equal-coefficient functional at the all-ones vector
is `3 alpha`, and `2/9` is separated from `2 pi q` across a declared
finite rational family. Against three imported charged-lepton masses
under a stipulated signed-root condition, the all-positive assignment
lands `7.41e-06` from the comparator `2/9` and the next assignment about
2.98e+03 times further — a measurement, published in full, with no
threshold and no significance claimed. Independent audit is still
required. The author-side `proposed_retained` status proposes only this
bounded support claim for audit; it asserts no audit verdict or effective
grade.
