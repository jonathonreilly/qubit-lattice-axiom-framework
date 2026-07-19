# Physical frame-covariant effect-identity tournament — Cycle 408 note — 2026-07-18

Authority: none
Audit: unset

## Question and result

Cycle 404 exposed a `C_num` interface defect. Its supplied 13-decimal matrix-entry key represented the actual cross-program surface by 3,150 cross classes and the installed surface by 3,348 classes. After proper-cubic rotation, rebuilding that key produced 3,149/3,347 classes in 16 of 24 frames even though the two merged representatives were separated by only about (5.2\times10^{-16}). Physical branch transport and transported-class residuals remained below tolerance.

Cycle 408 runs three effect-identity routes on the actual 342-pair, 1,710-menu, 21,302-occurrence Cycle-404 surface:

- **Route A — source-derived symbolic expressions:** identify an effect by the sorted multiset of its actual Kraus-word tokens ((\mathrm{bank},p,a,q,b)).
- **Route B — oriented-Bloch covariant classes:** encode scalar plus oriented Bloch coordinates once as integers, then act on the integer Bloch vector with the exact proper-cubic signed-permutation matrices.
- **Route C — orbit-canonical invariants:** discard orientation and retain the lexicographically least Route-B Bloch tuple in the 24-frame orbit.

Route B is constructive on this finite surface. A resolution sweep from 9 through 15 decimals selects **13 decimals** as the finest tested candidate with zero action failures and maximal retained class count. It gives 3,149 cross classes and 3,347 installed classes, is stable under all 24 proper-cubic frames and all 576 frame products, and preserves all 4,014 retained process tags.

The correction is material but narrow. The installed normalization system changes from Cycle 404’s 2,063 × 3,348, exact rank 1,159 to **2,063 × 3,347, exact rank 1,158**. The Cycle-404 rank correction is minus one, and its class correction is also minus one. Relative to Cycle 401, the corrected cross-program gain is 2,711 classes and 966 exact ranks. No physical update, effect matrix, process matrix, or physical fixture changes.

This is a constructive finite-surface codec/interface, not a new physical law.

## Common surface and direct equality audit

The runner reconstructs every Cycle-404 cross-program branch from the actual first-use/XOR-rewrite/second-use tensor. It then reconstructs the 1,710 menus in the original family order and retains the 21,302 effect/process occurrences.

The direct matrix audit uses a declared (10^{-12}) Frobenius equality radius only to test collisions and splits on the finite representative set. At that radius there is exactly one pair of distinct legacy matrix-entry keys; its direct residual is (5.17\times10^{-16}). Route B merges exactly that pair. It produces:

- no Route-B class containing representatives separated above (10^{-12});
- no direct-equal pair split across Route-B identifiers;
- 3,149 rather than 3,150 cross classes;
- 3,347 rather than 3,348 installed classes.

The (10^{-12}) audit radius and the 9–15 resolution sweep are supplied numerical interface choices. Stability outside this actual surface is not inferred.

## Route A — source-derived symbolic expressions

For a grouped effect

\[
F=\sum_{(a,b)\in S}(K_b^{(q)}K_a^{(p)})^\dagger
                       (K_b^{(q)}K_a^{(p)}),
\]

Route A stores the sorted token multiset

\[
\bigl((\mathrm{bank},p,a,q,b):(a,b)\in S\bigr).
\]

This identifier is carried exactly through grouping and never depends on floating matrix entries. Identical word multisets reproduce the same matrix below tolerance, and no symbolic identifier collides across Route-B oriented classes.

The cost is decisive: Route A yields **19,004 symbolic classes** and a 1,710 × 19,004 incidence matrix of exact rank 1,710. It splits 1,677 Route-B physical effect classes, with as many as 306 symbolic identifiers for one oriented effect. It also turns the process quotient into 19,004 identifier/process pairs even though only 4,014 distinct Choi process tags exist.

Route A therefore imports construction provenance. Bank labels, program labels, pointer labels, and a chosen Kraus refinement become part of “effect identity.” This is useful as a derivation/debug certificate but is not selected as intrinsic physical effect identity. Its deletion audit makes the distinction concrete: removing a structurally zero Kraus word changes the provenance identifier in 296 fine branches while leaving the matrix effect unchanged.

## Route B — oriented-Bloch covariant classes

For an effect (F=sI+xX+yY+zZ), Route B forms

\[
Q_{13}(F)=
\left(
\operatorname{round}(10^{13}s),
\operatorname{round}(10^{13}x),
\operatorname{round}(10^{13}y),
\operatorname{round}(10^{13}z)
\right).
\]

The scalar is invariant. For a proper-cubic frame (g\), the three integer Bloch coordinates transform by exact signed permutation:

\[
g\cdot(s,\mathbf v)=(s,g\mathbf v).
\]

This is derived from each matrix’s scalar/Bloch decomposition and from the supplied integer frame matrices. It does not carry bank, program, pointer, or family provenance.

### Resolution sweep

| Decimals | Installed classes | Frame-action failures |
|---:|---:|---:|
| 9 | 3,183 | 0 |
| 10 | 3,333 | 0 |
| 11 | 3,347 | 0 |
| 12 | 3,347 | 0 |
| **13** | **3,347** | **0** |
| 14 | 3,348 | 40 |
| 15 | 3,347 | 496 |

The written selection rule is the finest tested zero-failure candidate with the maximal stable class count. It selects 13 without using incidence rank as the selection target.

### Proper-cubic action table

The runner derives the frame multiplication table directly from integer 3 × 3 products. It checks:

- all 24 frames are proper, integer, and orthogonal;
- all **576 frame products** close and match their matrix products exactly;
- the identity frame, all inverses, and all 13,824 associativity triples;
- direct matrix rotation followed by re-encoding equals integer Route-B action for every installed class and every frame;
- sequential and table-composed action agree for every installed class and all 576 products.

Every integer action residual is zero. Because orientation remains in (Q_{13}), cubic-related but differently oriented effects remain distinguishable.

### Incidence and processes

| Surface | Menus × Route-B classes | Exact rank |
|---|---:|---:|
| Cycle-404 cross additions | 1,710 × 3,149 | 1,059 |
| Cycle-401 source plus Cycle-404 additions | 2,063 × 3,347 | 1,158 |

The corrected cross process quotient has **4,014 effect/process pairs**, 4,014 unique process tags, 233 effect classes with multiple process tags, and at most 36 process tags for one class. Effect identity still does not merge different processes.

## Route C — orbit-canonical invariants

Route C maps (Q_{13}(F)=(s,\mathbf v)) to

\[
C_{13}(F)=\left(s,\min_{g\in O}\,g\mathbf v\right),
\]

where (O) is the 24-element proper-cubic group and the minimum is lexicographic. It is exactly frame invariant on the tested surface and depends only on the matrix-derived Route-B tuple plus the group action.

Pure orbit canonicalization is not selected as effect identity because it merges physically distinct oriented effects. On the cross surface it has 2,893 orbit classes, 256 fewer than Route B. There are 216 multi-member orbit groups; one contains only the numerical duplicate repaired by Route B, while 215 groups merge **312 physically distinct oriented effect pairs**. Their same-frame Frobenius separations range from (2.03\times10^{-9}) to (0.4714).

Route C’s diagnostic incidence systems are:

| Surface | Menus × orbit classes | Exact rank |
|---|---:|---:|
| Cycle-404 cross additions | 1,710 × 2,893 | 1,045 |
| Installed combined surface | 2,063 × 3,074 | 1,142 |

Those ranks describe the orbit quotient, not the physical oriented-effect normalization system. Route C retains all 4,014 process tags, but compresses them into 370 multi-process orbit classes with as many as 102 tags per orbit class. Adding an orientation coordinate repairs the merge and returns to the Route-B structure.

## Deletion and malformed-domain controls

- Route A: deleting one word changes all 19,004 symbolic identifiers, including 296 structural-zero fine branches whose matrix effect is unchanged. This is a provenance false positive, not physical deletion sensitivity.
- Route B: the legacy surface contains two raw representatives for one Route-B identifier. Deleting either leaves 3,347 classes; deleting both leaves 3,346, demonstrating representative redundancy without hiding class removal.
- Route C: deleting the identity frame from its 24-frame canonicalization causes 9,022 frame-invariance failures. The invariant depends on the complete declared group.
- Dropped/mutated frame tables and malformed matrices, frames, resolutions, symbolic tokens, and identifiers reject rather than invoking host repair.

## Physical preservation

All three routes label existing effects; none changes the physical network. The cold runner rechecks:

- `E G_logical = G_physical E` at L=3 and held L=6;
- held leakage below (1.9\times10^{-16}) and zero role-constraint residual;
- bounded cross-use support of 32 M2;
- all 24 physical proper-cubic frames with zero branch failures;
- the one-particle mass fixture;
- the Cycle-230 contact intertwiner and load-bearing contact deletion in every bank.

The raw legacy matrix-entry diagnostic continues to report 16 re-key differences. Route B repairs that interface by acting on the encoded oriented Bloch integer tuple; it does not reinterpret the raw diagnostic as physical failure.

## Supplied structure and scope boundary

Supplied:

- the actual Cycle-404 matrices, grouping grammar, processes, and physical compiler;
- the 24 proper-cubic integer frames;
- the finite resolution sweep 9–15 and its selection rule;
- the (10^{-12}) direct-residual audit radius;
- scalar/Bloch decomposition and decimal integer quantization;
- effect functionality at the selected finite codec and separately retained Choi process tags.

Derived on the finite surface:

- the Route-B identifiers;
- the exact 24 × 24 frame product table and class action;
- the one-class/one-rank Cycle-404 correction;
- Route-A provenance splits and Route-C orientation merges.

Not derived:

- a resolution valid for effects outside the Cycle-404 surface;
- covariance under arbitrary continuous rotations;
- autonomous generation of effect or process labels;
- universal effect identity or universal menu eligibility;
- Born selection, probability interpretation, actuality/history sampling, Record formation, or frequency;
- a global no-go, minimum-content result, or constitutional conclusion.

Pointer registers remain instrument outputs, not realized occurrences or Records. Wrapped phase is not physical energy, and a generator element is not a rate.

## N1–N8 discipline gate

### N1 — Alternative route enumeration

Five routes were actually tested:

1. **ATTEMPTED — legacy matrix-entry re-key:** rotate then rebuild the Cycle-404 key; 16 frame-dependent differences recur.
2. **ATTEMPTED — Route A source expression:** carry exact Kraus-word multisets; collision-free but provenance-dependent and over-splitting.
3. **ATTEMPTED — Route B oriented covariant tuple:** quantize once and apply exact integer frame action; constructive on the finite surface.
4. **ATTEMPTED — Route C pure orbit invariant:** frame invariant but orientation-erasing.
5. **ATTEMPTED — orbit invariant plus orientation coordinate:** restores oriented identity and reduces to the Route-B information content.

The route dispositions are scoped observations, not a minimum or impossibility theorem.

### N2 — Condition-independence audit

The explicit conditions are:

- W1: the finite Cycle-404 effect/process surface;
- W2: the 9–15 resolution sweep and 13-decimal selection rule;
- W3: the supplied 24-element proper-cubic group;
- W4: retention of orientation in physical effect identity;
- W5: effect functionality with process tags retained separately.

| Pair | Independence result |
|---|---|
| W1–W2 | A matrix surface does not choose a decimal resolution, and a resolution does not generate matrices. |
| W1–W3 | The effect surface and group action are separately supplied. |
| W1–W4 | Effects do not decide whether orientation is retained in a quotient. |
| W1–W5 | Matrices do not imply a functionality/process quotient policy. |
| W2–W3 | Quantization and group multiplication are independent interface structures. |
| W2–W4 | A stable quantization can be used with or without orientation. |
| W2–W5 | Numerical identity resolution does not decide process equality. |
| W3–W4 | The group exists whether its orbits are quotiented or oriented. |
| W3–W5 | Frame transport does not select effect/process functionality. |
| W4–W5 | Orientation retention and process-tag retention address different information. |

No condition follows automatically from another on the tested surface.

### N3 — Hidden-condition scan

The load-bearing conditions are named: finite actual surface, scalar/Bloch coordinates, 9–15 sweep, 13-decimal choice, (10^{-12}) audit radius, complete proper-cubic group, orientation retention, and separate process tags. “Canonical” appears only in the declared Route-C orbit operation and does not confer physical identity. No host-side label repair is hidden.

### N4 — Residual matching

| Witness | Witness residual | Cycle-408 residual | Match? |
|---|---|---|---|
| Cycle 383/385 | decimal matrix-key equality for incidence | legacy key behavior | yes |
| Cycle 404 raw re-key diagnostic | 16 frame-dependent class changes | Route-B frame re-encoding/action | yes |
| Cycle 404 physical covariance | branch and transported-class residuals | preservation under relabeling | yes |
| Cycle 404 process quotient | equal effects with separate Choi tags | Route-A/B/C process retention | yes |

No source-response, Born, actuality, or Record residual is used as evidence about the codec.

### N5 — Rhetoric audit

Tests occur at matrix representative, occurrence, class, menu-incidence, process-tag, frame-action, and physical-branch resolutions. Route A’s disposition is only about intrinsic effect identity on this surface; it remains a valid provenance certificate. Route C’s disposition is only about standalone oriented-effect identity; it remains a valid orbit descriptor. No lattice-wide, continuous-rotation, or universal-effect negative statement is made.

### N6 — Partial-closure path scan

Cycle 408 is itself an import-retirement path for the Cycle-404 codec defect: replace rotate-then-re-key with a matrix-derived oriented tuple and exact discrete group action. A second constructive path is Route C augmented with orientation, which carries the same essential information. Neither path changes axioms or physics. Exact symbolic/algebraic encodings outside the current numerical compiler remain live extensions.

### N7 — Steelman

A hostile reviewer can reasonably demand an exact algebraic-number representation of every compiled Kraus coefficient, eliminating decimal quantization entirely, or a rigorously interval-certified equality relation whose resolution is derived from upstream error bounds rather than a finite sweep. Such a codec could retain Route B’s covariance while extending beyond this finite surface and might alter the corrected class census. Cycle 408 therefore claims only the tested finite interface and leaves exact/interval construction as the strongest next route.

### N8 — Cross-cycle echo

- Cycle 383 introduced the matrix key used for effect functionality.
- Cycle 385 used it to construct incidence systems.
- Cycle 401 showed that effect equality must not erase process tags.
- Cycle 404 exposed frame-sensitive raw re-keying while physical transported covariance remained exact.
- Cycle 408 repairs that same codec residual with an oriented group action and corrects the finite rank by one.

The echo is interface-specific; it is not evidence for a substrate obstruction.

**Gate disposition: PASS for the constructive Route-B finite-surface codec and narrow route dispositions only.** No minimum, impossibility, universal identity, or axiom-pressure claim passes this gate.

## Claim status

- Route B finite Cycle-404 effect codec: constructive.
- Cycle-404 class/rank correction: exact finite incidence result.
- Route A: retained as provenance/derivation certificate, not selected as intrinsic effect identity.
- Route C: retained as orbit descriptor, not selected alone as oriented effect identity.
- Born selection: not claimed.
- Universal effect-identity law: not claimed.
- Axiom pressure: not claimed.
- Authority: none.
- Audit: unset.
