# Physical cross-program rewrite composition — Cycle 404 note — 2026-07-18

Authority: none
Audit: unset

## Question and disposition

Cycle 404 changes exactly W2 of the Cycle-401 finite-composition grammar: the two uses may now carry different program labels. It constructs an explicit bounded reversible program-register rewrite between the uses, not a host relabel, and exhausts all 342 lawful ordered cross-program pairs inside the seven fixed Cycle-398 banks.

The result is constructive. A supplied three-M2 rewrite register carries

\[
d=p\mathbin{\mathrm{XOR}}q,
\qquad
R|p,d\rangle=|p\mathbin{\mathrm{XOR}}d,d\rangle=|q,d\rangle .
\]

In register shorthand: `R|p,d> = |p XOR d,d>`.
The XOR rewrite maps p,d to p XOR d,d.

The same fixed Cycle-398 bank update is used before and after (R). Three parallel CNOTs, with the three delta bits controlling their corresponding program bits, implement (R). The runner verifies every one of its 64 basis actions, the inverse action, (R^{-1}=R), (R^2=I), and exact forward/inverse register recovery. There is no program-dependent dispatch in the application routine: it ends in `return rewrite @ state`.

On the declared code space, every actual tensor block is

\[
K^{(q)}_b K^{(p)}_a,
\]

and the blockwise physical encoding verifies

\[
E G_{\mathrm{logical}}=G_{\mathrm{physical}}E
\]

at (L=3) and held (L=6). This direct-sum block equality is the global equality on the declared basis-state program/delta code. It does not derive preparation of (p), (d), either blank pointer, or the bank invocation.

Certificate shorthand: `E G_logical = G_physical E`; the tested fixtures are L=3 and held L=6.

## Declared finite grammar

Only pairs (p\ne q) in the same fixed bank are admitted. The supplied delta must equal (p\mathbin{\mathrm{XOR}}q). Same-program pairs remain the Cycle-401 surface; cross-bank pairs, a third use, and arbitrary set partitions are outside this cycle.

For a pair whose first and second programs have (n_p,n_q\leq8) pointer outcomes, the five exhaustive presentations are:

1. **ordered-fine:** every singleton ((a,b));
2. **first-pointer marginal:** fix (a), sum every (b);
3. **second-pointer marginal:** fix (b), sum every (a);
4. **unordered-pair symmetrization:** orbit ((a,b)\leftrightarrow(b,a)) when both labels exist in the rectangular (n_p\times n_q) domain, otherwise a singleton boundary orbit;
5. **same-versus-different pointer:** (a=b) against (a\ne b).

The runner requires each rule to partition every fine branch exactly once.

| Bank | Lawful programs | Ordered (p\ne q) pairs | Fine branches | First/second marginal occurrences | Swap-orbit occurrences |
|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 56 | 734 | 203 each | 506 |
| 1 | 8 | 56 | 1,330 | 273 each | 826 |
| 2 | 8 | 56 | 1,470 | 287 each | 910 |
| 3 | 8 | 56 | 2,016 | 336 each | 1,176 |
| 4 | 8 | 56 | 2,016 | 336 each | 1,176 |
| 5 | 8 | 56 | 2,548 | 378 each | 1,588 |
| 6 | 3 | 6 | 384 | 48 each | 216 |
| **Total** | **51 supplied programs** | **342** | **10,498** | **1,861 each** | **6,398** |

The same-versus-different family contributes 684 occurrences. Thus the exact surface contains 10,498 ordered fine branches, 1,710 cross-program menus, and 21,302 effect occurrences. Sampling is absent.

## Effect incidence and retained process tags

Cycle 401 is the fixed baseline: 353 menus, 636 equal-effect classes, exact integer rank 192. The five Cycle-404 families are appended in the declared order.

| Cumulative added family | Menus × classes | Exact rank | New classes at this step | Rank gain at this step |
|---|---:|---:|---:|---:|
| ordered-fine | 695 × 1,030 | 371 | 394 | 179 |
| first-pointer marginal | 1,037 × 1,030 | 371 | 0 | 0 |
| second-pointer marginal | 1,379 × 1,351 | 550 | 321 | 179 |
| unordered-pair symmetrization | 1,721 × 2,803 | 884 | 1,452 | 334 |
| same-versus-different pointer | 2,063 × 3,348 | 1,159 | 545 | 275 |

The final system has **2,063 menus, 3,348 classes, exact rank 1,159** and affine dimension 2,189. Relative to Cycle 401 there are **2,712 new effect classes** and the **rank gain is 967**.

The first-pointer zero increment has a direct scoped explanation:

\[
\sum_b (K_b^{(q)}K_a^{(p)})^\dagger(K_b^{(q)}K_a^{(p)})
=K_a^{(p)\dagger}\left(\sum_b K_b^{(q)\dagger}K_b^{(q)}\right)K_a^{(p)}
=K_a^{(p)\dagger}K_a^{(p)}.
\]

That is an effect-incidence identity only. It is not permission to erase the second-use process.

Across the cross grammar there are 3,150 equal-effect keys: 438 match Cycle-401 keys and 2,712 are new. The process quotient retains **4,015 effect/process pairs**, 4,014 unique process tags, and **233 effect keys carry multiple process tags**. As many as 36 process tags occur for one effect key, and the largest same-effect distinct-process Choi separator exceeds 0.92. Equal effects are not used to merge distinct processes.

## Physical certificate

The actual network is

\[
G_\times=(G_{\mathrm{bank}}\otimes I_{d,a})
(R_{p,d}\otimes I_{a,\mathrm{matter}})
(G_{\mathrm{bank}}\otimes I_d),
\]

where the displayed juxtaposition denotes ordered circuit composition. The executable uses tensor contraction of the two fixed carrier matrices with the explicit 64-by-64 rewrite permutation; a separately constructed direct tensor is used only as the test oracle. Every lawful product is extracted from the actual network tensor.

The cold certificate checks:

- sequential network versus direct (K_b^{(q)}K_a^{(p)}) tensor residual below (1.2\times10^{-10});
- exact rewrite forward and inverse actions on all 64 register states;
- full logical network isometry on the 128-dimensional program/delta/matter input;
- off-target program output is zero;
- branchwise (E G_{\mathrm{logical}}-G_{\mathrm{physical}}E), leakage, and local role-constraint residuals below tolerance at (L=3) and held (L=6);
- 16 inherited physical matrix-unit pairs, matter transition union 20 M2, and maximum matter transition support at most 20 M2;
- maximum controlled cross-use support 32 M2, patch 68 M2, and installed overhead 35 M2 per bank;
- if all seven bank auxiliaries are co-located, 84 auxiliary M2 and 107 M2 including the shared 23-M2 base;
- port, local-check, and Wilson failures zero;
- branch covariance and transported-class effect-incidence covariance under all 24 proper-cubic frames;
- the one-particle mass fixture and the physical Cycle-230 contact intertwiner;
- contact deletion changes every bank at the update/effect/process audit resolution;
- exhaustive fine-branch, coarse-group, and process-branch deletion classification, with positive-product changes and structurally zero products reported separately, plus rewrite and delta deletion controls;
- malformed pair, delta, pointer-domain, and grouping-domain rejection.

The XOR rewrite acts only on six bounded register M2. The support and overhead are constant per fixed bank/cell; no global ordering, parity string, nonlocal service, or host-side program rewrite is introduced.

### Frame-transport versus raw key diagnostic

The covariance claim transports each already-declared effect class together with its matrix representative. For every menu occurrence and every proper-cubic frame, the rotated occurrence equals the rotated representative of its original class below tolerance; therefore the transported incidence relation has zero failures. This is the relevant covariance test because a frame acts on physical/effect representatives, not by inventing new functionality labels.

A deliberately separate diagnostic rebuilds the supplied 13-decimal binary64 matrix key after rotation. It differs from the transported incidence labels in 16 of the 24 frames because rotate-then-round crosses decimal codec boundaries for some mathematically equal representatives. The runner reports those **16 raw re-key differences** explicitly and does not silently reinterpret them as physical class splitting. The physical branch-frame residual, transported-class residual, and direct network-versus-ordered-product residual remain zero within tolerance. Thus the raw re-key result is a codec-label diagnostic and a named `C_num` caveat, not the definition of proper-cubic covariance.

Concretely, the raw re-key rebuild reports 3,348 columns in eight frames and 3,347 columns in sixteen frames. Transporting the original class labels gives zero failures in every frame, with maximum representative residual (1.70\times10^{-15}); the actual sequential-network versus direct-product tensor residual is exactly zero.

### Deletion classification

The exhaustive deletion audit does not call structural zeros “visible.” Of 10,498 fine products, 10,202 positive-product deletions change the effect and 296 structural-zero fine products are inert. Across 21,302 coarse-group effect deletions, 20,892 are positive and 410 groups are structurally zero. At the retained Choi-process resolution, 20,693 deletions are nonzero and 609 are zero-operator deletions. Each of the 342 ordered pairs also has a deterministically selected positive branch whose removal produces completeness defect at least 0.0756. Setting the rewrite delta to zero gives the wrong target label in all 342 pairs; deleting the rewrite changes effects by as much as 0.609 and Choi processes by as much as 0.837.

## Supplied structure and residual boundaries

Supplied:

- the 51 Cycle-398 programs and their grouping into seven fixed banks;
- the positive-square-root compiler and Cycle-230 contact postcomposition inside those programs;
- the ordered-pair grammar (p\ne q) within a bank;
- preparation of the program basis label (p) and delta basis label (d=p\mathbin{\mathrm{XOR}}q);
- two blank three-M2 pointers and the bank invocation;
- the three-CNOT fixed rewrite circuit;
- the five grouping rules and the 13-decimal effect-functionality key;
- the process tag as the Choi sum of retained ordered Kraus products;
- physical encoding, role constraints, proper-cubic frame transport, size fixtures, mass fixture, and contact fixture.

Not supplied or derived here:

- cross-bank pair eligibility;
- a third or later use;
- arbitrary set-partition eligibility;
- autonomous or coherent generation of the delta label;
- autonomous bank, menu, or grouping genesis;
- a sampling rule, selected numerical grade, or universal menu eligibility;
- Born selection, probability interpretation, actuality/history sampling, Record formation, or a frequency theorem;
- a global no-go, minimum-content result, or constitutional conclusion.

The pointer outputs are instrument registers, not realized occurrences or Records. A generator element is not called a rate, and wrapped phase is not called physical energy.

## N1–N8 discipline gate

### N1 — Alternative route enumeration

Seven genuinely distinct audit resolutions were run: ordered-fine effects, first-pointer marginals, second-pointer marginals, swap orbits, same/different pointer groups, retained Choi process tags, and explicit rewrite/deletion behavior. The physical route is not simulated by a host substitution: it is a fixed reversible circuit between two fixed-carrier uses.

### N2 — Condition-independence audit

The five conditions are:

- W1: the finite seven-bank program table;
- W2: supplied (d=p\mathbin{\mathrm{XOR}}q) and the explicit reversible rewrite;
- W3: exactly two ordered carrier uses;
- W4: exactly five declared grouping rules;
- W5: 13-decimal equal-effect incidence plus separately retained Choi process tags.

All ten pairwise dependencies were audited:

| Pair | Dependence result |
|---|---|
| W1–W2 | W2 maps labels only inside the supplied W1 bank code; neither generates the other. |
| W1–W3 | W1 supplies blocks; W3 supplies ordered composition. |
| W1–W4 | Bank programs do not select grouping rules. |
| W1–W5 | Program tables do not imply an effect-functionality quotient. |
| W2–W3 | The rewrite changes the second label; two uses alone leave (p) unchanged. |
| W2–W4 | Register dynamics do not choose pointer coarse-graining. |
| W2–W5 | Register equality is distinct from effect/process equality. |
| W3–W4 | Ordered use does not choose one of the five partitions. |
| W3–W5 | Composition produces effects/processes but not their quotient policy. |
| W4–W5 | Group membership and equality/functionality are independent supplied structures. |

### N3 — Hidden-condition scan

The apparent constructive strength depends on named walls: basis-state delta preparation, fixed-bank locality, (p\ne q), two uses only, pointer capacity eight, rectangular swap-orbit convention, effect-functionality premise, and inherited physical encoding/frame/contact fixtures. Cross-bank routing, coherent delta superpositions, arbitrary partitions, and autonomous scheduling remain outside the lawful domain. No hidden host relabel is used.

### N4 — Residual matching

Matching witnesses are required at the exact claimed resolution: actual tensor block versus (K_b^{(q)}K_a^{(p)}), forward/inverse rewrite basis state, effect incidence class, retained process Choi tag, and physical branch intertwiner. Route-specific nonmatches are not promoted to shared obstructions. In particular, the first-pointer rank increment is zero while the four other effect families add rank; that mixed evidence forbids a composition-wide negative inference.

### N5 — Rhetoric audit

The finite statements quantify only the 342 within-bank ordered pairs and five declared presentations. “Exhaustive” always modifies that written grammar. “Redundant” modifies only first-pointer effect incidence; it does not modify process tags, physical rewrite dynamics, other groupings, later uses, cross-bank schedules, or probability semantics.

### N6 — Partial-closure path scan

This cycle closes one explicit W2 path: bounded basis-state cross-program rewriting within a bank. At least five live extensions remain: cross-bank routing, chained rewrites/third use, coherent delta control, alternative lawful pointer partitions, and endogenous program/delta preparation. Therefore no new primitive, minimum content, or axiom change follows.

### N7 — Steelman

The strongest counter-position is constructive: a larger reversible controller could coherently carry bank identity, program differences, and longer schedules; richer partitions could expose further independent effects; and an endogenous selection mechanism might replace the supplied basis-state delta. Cycle 404 strengthens that position because a six-M2 local rewrite already produces a large positive class/rank gain. The broader negative claim is therefore demoted rather than shipped.

### N8 — Cross-cycle echo

- Cycle 390 showed that new physical menus can overlap while retaining process differences.
- Cycle 398 exhausted and physically installed the scoped (G55[2{:}8]) grammar without a rank gain.
- Cycle 401 added same-program two-use groupings and gained 581 classes and 161 ranks.
- Cycle 404 changes W2 and gains a further 2,712 classes and 967 ranks.

These echoes demonstrate that rank behavior is grammar-dependent. A zero increment in one family or cycle is not a substrate-level obstruction.

**Gate disposition: PASS only for the finite census and first-pointer effect-incidence redundancy.** The gate fails for any composition-wide nonforcing, minimum-content, or axiom-pressure inference.

## Claim status

- Physical within-bank basis-state program rewrite: constructive finite certificate.
- Cross-program effects and processes: constructive finite certificate.
- First-pointer effect-incidence redundancy: exact scoped identity.
- Born selection: not claimed.
- Universal menu eligibility: not claimed.
- Axiom pressure: not claimed.
- Authority: none.
- Audit: unset.

Cycle 404 is a positive physical compiler extension under an explicit supplied controller. It changes implementation reach, not constitutional status.
