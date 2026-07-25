# Exercise Three — Literature Proof-Template Search for an Isotypic Relative Normalization

**Date:** 2026-07-24
**Sector:** EX3 (literature proof templates; templates only, never imported as authority)
**Status:** exercise report. Not a repo note, not a claim, not an audit input. No axiom,
no primitive, no verdict, no promotion. Nothing here is landed; every literature item
below is a **comparator template**, never a premise.
**Working tree:** `origin/main` fetched at session start (tip `1652deb63b`).

---

## 0. Framework refresher — surfaces actually read before any conclusion

Read in full or in the load-bearing part, in this order, before forming any view:

1. `docs/MINIMAL_AXIOMS_2026-06-29.md` — Lattice / Qubit / Admissibility / Record; the
   Qualification clause; "Axioms and approved primitives are the complete supplied
   foundation"; the explicit statement that Admissibility supplies **no** transfer
   operator, weights, or probabilities.
2. `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` — the four registered nodes and
   the "do not grant more than the source note declares" rule (item 5 explicitly names
   *normalization rule* and *weighting* as separate).
3. `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` — units conversion only, zero dimensionless
   content. **This is load-bearing for §4 below**: it means a *scale* is granted as a ruler
   but a *dimensionless scale ratio* is not.
4. `docs/audit/data/axiom_premise_nodes.json` — the complete supplied foundation
   (`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
   `realized_state_primitive`) and their exclusion notes.
5. `docs/ai_methodology/skills/review-loop/SKILL.md` — axiom vs approved-primitive
   boundary, Record guardrails, "no new repo-wide axioms / theory language / primitives".
6. `docs/repo/CONTROLLED_VOCABULARY.md` (existence + `claim_type` enum checked). I propose
   **no new repo vocabulary**; the descriptive labels below are exercise-local and would
   need vocab review before any `docs/` surface uses them.

Repo prior art read (so this sector does not re-walk closed ground):

- `docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`
- `docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md` (the wall itself)
- `docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`
  (the 8-lens / 0-of-8 no-go)
- `docs/KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`
- `docs/KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md`
- `docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
- `docs/ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md`
- `docs/FLAVOR_EQUIVARIANT_ETA_COMPLEMENTARITY_NOTE_2026-05-30.md`
- `docs/KOIDE_OCTAHEDRAL_OVERCONSTRAINS_VALUE_BIT_NARROW_NOTE_2026-06-02.md`
- `docs/KOIDE_R_IS_THE_WEIGHTING_PRINCIPLE_DIAL_RECORD_DYNAMICS_WEIGHTING_BLIND_BOUNDED_THEOREM_NOTE_2026-06-15.md`
- `docs/FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md`

For the purpose of this exercise all four axioms and all four registered primitives are
marked **ASSUMPTIONS**, and repo content is treated as challengeable. §6 records where I
think existing repo framing is misleading.

---

## 1. Executive summary — the single most important finding

The template search does not return a selector. It returns a **sign obstruction**, and the
obstruction is exactly computable on the framework's own carrier with no new input:

> **Every literature template in this territory that actually fixes an isotypic relative
> normalization does so from a POSITIVE spectral/measure-theoretic weight, and every
> positive `C_3`-covariant weight over-weights the trivial isotype. Concretely, for any
> positive covariant semigroup `rho` on the generation carrier, the induced invariant form
> sits at `g_0/g_1 = (S + 2F)/(S - F)` with `S = Tr(rho) > 0`, `F = Tr(rho R) > 0`, hence
> `g_0/g_1 > 1` strictly, with `-> 1` only in the ultra-local limit. The charged-lepton
> point `r = 1/2` lies on the *unreachable side* of the flat point. Reaching it requires
> exactly `F/S = -1/5`: a negative equivariant trace, i.e. a genuine grading.**

That is why 8 static lenses and 95 exact reality-type gates all failed and why the HS
metric, the heat-kernel arrow, einselection and max-record-entropy all landed at or above
the flat point: they are all positive weights, and positivity alone already forbids the
target half-cone. This reframes the wall from "which of two conventions" to a **one-sided
Perron-Frobenius bound with a sharp numeric breach condition**.

Everything in §2 is the census that produces this; §4 is the exact statement and the
verified numbers; §5 is the first artifact.

---

## 2. The wall in template language

The object every template must act on:

- Carrier: the real regular representation `R[Z_3] = R (+) C` — one trivial isotype
  (1 real dim) and one nontrivial isotype (2 real dims, complex type).
- Free datum: the `C_3`-invariant positive symmetric forms are exactly
  `diag(g_0, g_1, g_1)` (Schur: the commutant of the real doublet is `C`, whose symmetric
  part is `R.I`), a 2-parameter cone with one invariant `r = g_0/g_1`.
- Named points: **flat** `diag(1,1,1)` -> `r = 1`; **HS** `diag(3,6,6)` -> `r = 1/2`
  (charged-lepton target).
- Landed obstruction: `koide_frobenius_isotype_split_uniqueness` — PD + Ad-invariance +
  isotype orthogonality leave `beta` free. Symmetry cannot close it, by construction.

**Therefore the only admissible template shape is: a theorem whose hypotheses are NOT
purely representation-theoretic and whose conclusion is a specific point of this cone.**
That is the exact filter applied below. A template fails immediately if its conclusion is
a function of `(|G|, d_pi, chi_pi)` alone, because those are constant on the cone.

---

## 3. The census

Verdict key: **VOID** = hypotheses cannot be met natively or the theorem's output is
cone-constant; **ECHO** = the theorem reproduces the same free parameter somewhere else;
**FORECLOSED** = it is a listed dead route wearing a new name; **LIVE** = survives the
filter and has a native first artifact.

### 3.1 Plancherel / Peter-Weyl measure on a finite group — **VOID (and already probed)**

*Theorem.* For finite `G`, `C[G] = (+)_pi End(V_pi)` and the Plancherel measure on `Ghat`
is `mu(pi) = d_pi^2/|G|`; the decomposition is an isometry when each block carries the
`d_pi`-scaled Hilbert-Schmidt form.

*Hypotheses.* A group and its group algebra. Nothing else.

*What it fixes.* The relative block normalization — **as `d_pi^2/|G|`**.

*Native meetability.* Fully met. `C_3` is supplied by the carrier.

*Why it does not help.* For `Z_3` all `d_pi = 1`, so Plancherel is **uniform**, and over
`R` the doublet (two conjugate characters) carries twice the singlet: dimension weighting,
`r = 1`, i.e. the flat point. The theorem is a genuine theorem and its answer is the flat
point. It cannot produce `1/2` without an extra "count a conjugate pair once" step — which
*is* the disputed bit. Repo `probe12` reached the same terminus (both sub-derivations (a)
and (b) close; the closure step to `(1,1)` fails at the convention trap). Watatani index
`9/3 = 3` likewise reproduces dimension bookkeeping.

*Repo-native translation that would be required.* Prove that the framework's readout is a
functional on the **real** group algebra whose blocks are `{R, C}` rather than on `C[Z_3]`
whose blocks are the three characters. That is a reality-type input -> **FORECLOSED** by
the FS/complex-type foreclosure. This is the first appearance of a pattern that recurs in
almost every family below.

### 3.2 Minimal index / minimal conditional expectation (Longo, Hiai, Kosaki) — **VOID**

*Theorem.* For an inclusion of finite index there is a unique conditional expectation
minimizing the index; for `B (subset) A = (+)_i M_{n_i}`, the minimal expectation weights
the blocks by their statistical dimensions, and Longo's theorem identifies minimal index
with statistical dimension in the AQFT superselection setting.

*Hypotheses.* An inclusion of C*-algebras with finite index.

*What it fixes.* A canonical relative weight on the blocks — **equal to the dimensions**.

*Native meetability.* An inclusion is available (`A^{C_3} (subset) A`), so hypotheses are
meetable. That is precisely the problem: the canonical answer is dimension weighting again.

*Verdict.* The "canonical trace" that operator algebra supplies is the dimension trace.
It lands on the flat point.

### 3.3 Markov trace / Perron-Frobenius weights of a Jones tower — **VOID by a lemma**

This was my strongest a-priori candidate, because Markov-trace weights are famously **not**
dimension weights (Temperley-Lieb gives quantum dimensions `[n]_q`), and they come from the
*inclusion* (a tower/dynamical datum), not from symmetry.

*Theorem.* For a connected unital inclusion of finite-dimensional C*-algebras with Bratteli
matrix `Lambda`, the Markov trace exists, is unique, and its block weight vector is the
Perron-Frobenius eigenvector of `Lambda^T Lambda`, with modulus `||Lambda||^2`.

*Why it dies here — the lemma.* The blocks we must weight are `C_3`-isotypes, so the tower
must be `C_3`-equivariant, so the Bratteli matrix is a **branching/fusion matrix in
`Rep(C_3)`**. But the Frobenius-Perron eigenvector of a fusion matrix is the unique positive
ring homomorphism from the Grothendieck ring to `R`, i.e. the **FP dimension**, and for
`Rep(G)` the FP dimension *is* the ordinary dimension. Checked explicitly over `R`:
`doub (x) triv = doub`, `doub (x) doub = 2 triv (+) doub`, matrix `[[0,2],[1,1]]`, whose
PF (left) eigenvector is `(1,2)` with eigenvalue `2` — the real dimension vector. Over `C`
it is `(1,1,1)` -> doublet total `2`. **Both give the flat point.**

*The fork, stated honestly.* Non-dimensional PF weights require a non-group-like fusion
structure (subfactor with principal graph `E_6`, `A_n`, etc.). But the sectors being
weighted are defined by a group, so the tower cannot be non-group-like without destroying
the very decomposition. Both prongs closed. **This fork is a first-artifact-grade lemma in
its own right** (see §5, artifact B).

*The one crack.* If the isotypes are *tensored with objects of different quantum dimension*
in a larger structure (the counting-bit note's open "sector-factorization on the per-site
`M_2(C) (x) R[C_3]` algebra"), FP weights can differ from `(1,2)`. That crack is the
already-named open gate, not a new route.

### 3.4 Equivariant index theory (Atiyah-Singer / Atiyah-Bott / McKean-Singer) — **VOID; already closed natively**

*Theorem.* `Str(g e^{-tD^2})` is `t`-independent and equals a sum of fixed-point data.

*What it fixes.* A signed **integer** mode count per isotype, valued in `R(G)`.

*Decisive mismatch (the strongest single reason index theory cannot touch this wall).* The
Koide magnitude is a **sesquilinear energy**, not a determinant and not a mode count. An
index is additive and integral; `r = 1/2` requires a **multiplicative `1/2` on the `|b|^2`
coefficient** (`6 -> 3`). No index theorem produces a multiplicative rescaling of a
quadratic form. The repo already established this on the built realization
(`KOIDE_KAHLER_DIRAC_..._INDEX_ROUTE_CLOSED`, runner 22/22): over all 8 `C_3`-equivariant
`Z_2` gradings the index is a signed count in `{+-1, +-3}` and cannot reweight the doublet
energy. **Do not re-propose this.**

### 3.5 Equivariant localization: Atiyah-Bott / Lefschetz / orbifold heat trace — **VOID by a structural singularity; already instantiated natively**

*Theorem.* `Str(g|H^*) = sum_{fixed pts} (local character)/det(1 - dg|_N)`.

*Native meetability.* **Fully met, and already computed in the repo.** The body-diagonal
proper cubic rotation has `det_R(I - g|_N) = 3` for both nonidentity elements, giving
`L_{C_3}(N) = 2/9` (`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE`), with an ambient lattice
face (`ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE`).

*Decisive mismatch.* Localization data is indexed by **group elements**, and the identity
term is exactly the one with no isolated fixed locus (`det(1 - 1) = 0`). Every localization
weight formula therefore **omits or diverges on the trivial sector** — the very sector whose
relative weight is being asked for. The repo's `L = 2/9` is literally defined as a sum over
`k = 1, 2` only. Localization tells you about the *nontrivial* isotypes relative to each
other, where `C_3` symmetry already ties them; it is structurally silent on singlet-vs-doublet.
Independently, `FLAVOR_EQUIVARIANT_ETA_COMPLEMENTARITY` shows `2/9` is not an `eta` and
sits in the `delta` (phase) channel, not the `r` (magnitude) channel.

### 3.6 Duistermaat-Heckman / Berline-Vergne — **VOID at the hypothesis level**

*Hypotheses.* A **connected compact torus** acting on a symplectic manifold with a moment
map; the DH measure is the pushforward of Liouville measure.

*Native meetability.* **Impossible.** `C_3` is finite: no Lie algebra, no moment map, no
Liouville pushforward. There is no finite-group DH theorem; the finite-group analogue *is*
the Lefschetz formula of §3.5.

*The embedding escape and why it fails.* Embedding `Z_3 (subset) U(1)` does not shrink the
cone: `U(1)` acting with weight 0 on the singlet and weight 1 on the doublet still has
commutant `R (+) C`, so `diag(g_0, g_1, g_1)` survives verbatim. Enlarging the group only
helps if the two isotypes merge into one irrep — which is the octahedral route, and the repo
already proved that `O_h` **erases** the split rather than weighting it (`|O_h|`-invariant
forms are 1-dimensional; the largest `O_h` subgroup fixing `(1,1,1)` has order 6 and still
leaves the 2-dimensional freedom). Group enlargement is a closed direction.

*Related sub-check I ran and report as negative.* A `C_3`-invariant **contact** form on the
carrier does exist (`alpha = lambda da + (x dy - y dx)`), and contact geometry natively
counts an odd-dimensional space as `Reeb (+) symplectic plane = 1 + 1` — exactly the block
reading. But `lambda` is free, and `lambda` *is* the ratio. **ECHO**, not a selector.

### 3.7 Reidemeister / Ray-Singer / analytic torsion — **ECHO (the free parameter is a theorem there too)**

This is the family the brief flags as "a RATIO of sector determinants is the whole
invariant", and it is worth being precise about why it cannot be borrowed.

*Theorem.* Analytic torsion is not a number: it is an element of the (graded) determinant
line of the cohomology of the complex. It becomes a number only after a **metric on
cohomology** is chosen, and the Ray-Singer/Quillen metric anomaly formulas compute exactly
how the number changes when that metric changes (Bismut-Gillet-Soule; Bismut-Zhang;
Cheeger-Muller in the acyclic case).

*Two independent disqualifications.*

1. **Acyclicity excludes the trivial isotype.** Classical R-torsion for lens spaces
   `L(p;q) = S^3/Z_p` is a product over **nontrivial** characters,
   `tau = prod_{k != 0} (zeta^k - 1)(zeta^{qk} - 1)`; the trivial isotype is where the
   complex is not acyclic and torsion is undefined. Same structural defect as §3.5.
2. **In the non-acyclic case the free parameter is imported by name.** The undetermined
   metric on `H^*` of the trivial summand is a one-parameter positive scale, and the
   torsion scales by it. The template does not fix the ratio; it *is* a theorem that the
   ratio is not fixed.

*Repo-native translation that would be required.* One would have to derive the metric on
the trivial-isotype cohomology from Lattice/Qubit/Admissibility/Record — which is verbatim
the original problem. **This family is the cleanest example of a template that looks like it
answers the question and provably restates it.**

### 3.8 Selberg / Ruelle / Artin-Ihara trace formulas and zeta functions — **VOID (leading order is dimension weighting, by theorem)**

*Theorem (discrete, and therefore the one whose hypotheses the framework could meet).* For a
Galois covering `Y -> X` of finite graphs with group `G`,
`zeta_Y(u) = prod_{pi in Ghat} L(u, pi)^{d_pi}`, with
`L(u, rho) = (1-u^2)^{chi(X) deg rho} / det(I - A_rho u + (D_rho - I)u^2)`.

*What it fixes.* The **exponent** with which each isotype enters — and the exponent is
`d_pi`. For `Z_3`: all `d_pi = 1`, three factors, so the doublet enters with total degree 2.
Dimension weighting. Flat point.

*Native meetability.* Genuinely high: `Z^3` with nearest-neighbour adjacency and a `C_3`
deck action is exactly a finite-graph Galois cover, and the framework supplies the graph.
This is a case where the hypotheses *can* be met and the answer is the one we do not want.

*Deeper reason, worth recording.* The maximal-entropy (Parry) measure on a connected Galois
cover is deck-invariant, so isotypes equidistribute (Chebotarev). **Equidistribution is the
dynamical twin of the equivariant Weyl law** (§3.9): both say the leading term is dimension
weighting, with no free parameter. Non-dimensional isotypic behaviour lives only in the
subdominant zeros — see §4.

### 3.9 Heat kernel / zeta-regularized determinants on representation-graded spaces — **converted into the LIVE result of §4**

*Theorem (equivariant Weyl law; Donnelly, Bruning-Heintze, Ramacher).* For a `G`-invariant
elliptic operator, the isotypic spectral counting functions satisfy Weyl's law with leading
coefficients proportional to `d_pi^2/|G|`; fixed-point sets contribute at **subleading**
order.

*What it fixes.* The relative isotypic spectral density — **at leading order, as dimension
weighting**; at subleading order, by fixed-point (Lefschetz) data.

*Zeta-determinant sub-check, reported negative.* The scaling anomaly
`det_zeta(lambda A) = lambda^{zeta_A(0)} det_zeta(A)` makes `zeta(0)` a "regularized
dimension" that can be non-integral — the one mechanism in this family that yields
non-dimensional relative weights. But on a **finite-dimensional** carrier `zeta(0) = dim`
exactly, so the mechanism is empty here. The multiplicative (Kontsevich-Vishik/Wodzicki)
anomaly is an anomaly of *products*, not of *direct sums*, so it never sees a block
decomposition. Both dead.

*What survives.* The **finite-`t`** equivariant heat trace is not at leading order, and its
isotypic weights genuinely run. That is the only surviving handle in the entire census, and
§4 computes it exactly — and it closes negatively, with a sharp breach condition.

### 3.10 Anomaly / anomaly inflow forcing a relative factor — **FORECLOSED or additive**

Two sub-families, both dead for different reasons:

- **Pfaffian vs determinant (Majorana vs Dirac):** the canonical place a factor `1/2`
  appears between a "real" and a "complex" sector, `det^{1/2} = Pf`. This is precisely the
  reduced-trace-vs-regular-trace / `[C:R] = 2` distinction, i.e. a **reality-type selector**.
  **FORECLOSED**, and consistent with the repo's `Majorana -> r = 1` finding.
- **APS `rho`-invariant / local anomaly cancellation:** `rho_alpha = eta_alpha - dim(alpha)
  eta_triv` is metric-independent **only** with the coefficient `dim(alpha)`, because the
  metric-dependent local term is proportional to `dim(alpha)`. This is a genuine theorem in
  which a dynamical requirement *forces* a relative isotypic normalization — and it forces
  **dimension weighting**. It is therefore a decisive-falsifier-shaped result for `r = 1/2`,
  not a route to it. `FLAVOR_EQUIVARIANT_ETA_COMPLEMENTARITY` independently reached "eta is
  loud exactly where breaking is impossible"; I concur and add the mechanism.

*Also checked and negative:* `H^2(Z_3, U(1)) = 0`, so `Z_3` has trivial Schur multiplier and
**no projective/cocycle twist exists** that could alter the isotype structure. And
`Vec_{Z_3}^omega` has all objects invertible, so 3-cocycle twists leave all quantum
dimensions equal to 1. The "twist the category" escape is empty for this group.

### 3.11 Modular / KMS / Tomita-Takesaki — **ECHO, and it names the disease**

Already lens 5 of the 8-lens no-go, but the structural reason deserves to be recorded
because it explains the whole census:

> For a multi-block algebra `A = A_1 (+) A_2`, the traces form a simplex with two extreme
> points; **every** convex combination is a trace. The relative weight of central summands
> is exactly the part of a state that the algebra does not determine. Modular theory is
> canonically attached to a *state*, and the framework's `realized_state_primitive`
> explicitly supplies no measure, weighting, normalization, or probability rule.

So the wall is not an accident of `C_3`: it is the statement that a **central distribution
is state data, not algebra data**. Any template that claims to fix it must smuggle in a
state, an inclusion (§3.3), or a positivity/locality principle (§4).

### 3.12 Fusion-categorical / TQFT / Verlinde sector weights — **VOID**

`S_{0i}/S_{00} = d_i`; for `Z_3` Dijkgraaf-Witten all quantum dimensions are 1 and the
groupoid-cardinality weights are uniform. Modular-invariant partition functions
(Cappelli-Itzykson-Zuber-type constraints) do force integer relative multiplicities from a
consistency condition rather than from symmetry — the right *shape* — but for `Z_3` the
diagonal invariant is uniform, and the only consistency condition that would force `(1,1)`
is "sum over blocks of the **real** algebra". Reality again. **FORECLOSED.**

### 3.13 Formal degrees / Harish-Chandra Plancherel — **VOID at the hypothesis level**

Formal degrees are the canonical example of a *measure-theoretic* normalization that is not
a dimension, and the Hiraga-Ichino-Ikeda formal-degree conjecture fixes them by adjoint
gamma-factors. But formal degrees are non-dimensional only for groups with continuous
Plancherel measure (real/p-adic reductive). For a **finite** group the formal degree *is*
the dimension. No room.

---

## 4. The LIVE result: a one-sided Perron-Frobenius bound on the framework's own carrier

This is the only thing the census produced that is both native and decisive. It is a no-go,
not a selector — which the brief says is an equally welcome outcome.

### 4.1 Setup (all objects already landed; no new input)

`ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02` proves exactly, on the periodic
cubic lattice `Z_N^3` with `Delta = 6I - A` and the proper cubic coordinate cycle
`R(x1,x2,x3) = (x3,x1,x2)`:

```
Tr(f(Delta) R^j) = sum_{R^j k = k} f(Deltahat(k)),   j = 1, 2
Tr(exp(-t Delta) R^j) = sum_{m=0}^{N-1} exp(-t (6 - 6 cos(2 pi m / N)))
```

Write `S(t) = Tr(e^{-t Delta})` and `F(t) = Tr(e^{-t Delta} R) = Tr(e^{-t Delta} R^2)`.
`F` is the sub-sum of `S` over the `N` body-diagonal momenta, so

```
0 < F(t) < S(t)    for all t > 0 and all N > 1     (strict; verified)
```

### 4.2 The isotypic weights and the induced cone point

Isotypic projectors for 1-dimensional characters: `P_pi = (1/3) sum_j conj(chi_pi(R^j)) R^j`.
Hence

```
w_triv(t)    = Tr(P_triv  e^{-t Delta}) = (S + 2F)/3
w_nontriv(t) = Tr(P_omega e^{-t Delta}) = (S -  F)/3     (same for omega-bar)
```

The induced `C_3`-invariant positive form on the carrier is
`G(t) = w_triv P_triv + w_nontriv P_doublet`, i.e. the cone point
`diag(g_0, g_1, g_1)` with `g_0 = w_triv`, `g_1 = w_nontriv` (per real doublet direction).
Therefore

```
r(t) = g_0/g_1 = (S + 2F)/(S - F)
```

### 4.3 The bound, and the breach condition

Because `0 < F < S`:

```
r(t) > 1  strictly, for every t > 0 and every N > 1.
r(t) -> (N^3 + 2N)/(N^3 - N) -> 1^+   as t -> 0 then N -> infinity   (the FLAT point)
r(t) -> infinity                       as t -> infinity               (singlet dominance)
```

Solving `r = 1/2` and `r = 1` for `x = F/S` (exact, sympy):

```
r = 1   <=>  F/S =  0
r = 1/2 <=>  F/S = -1/5
```

**Verified numerically** (script `pf_check.py`, exact lattice sums, `N in {3,6,12}`,
`t in [1e-6, 100]`): `r` is strictly `> 1` and monotone increasing throughout; e.g.
`N=12`: `r(1e-6) = 1.0209790`, `r(0.5) = 1.0509560`, `r(3) = 1.5188382`,
`r(10) = 7.3824101`. `F < S` confirmed directly by the diagonal-sub-momentum identity.

### 4.4 What this means

1. **The target lies in the unreachable half-cone.** Positive covariant weights only ever
   *over*-weight the trivial isotype, because the Perron-Frobenius ground state of any
   positive covariant semigroup is itself trivial-isotype. `r = 1/2` requires *under*-
   weighting the singlet. So the failure is not "we have not found the right positive
   functional"; it is that **no positive functional of this class exists**.
2. **It explains the whole failure record in one sentence.** HS metric -> `r = 1`;
   heat-kernel arrow -> `r -> 1`; einselection -> `r = 1`; max-record-entropy -> a
   stationary point but sector-blind; 8 static lenses -> 0/8; 95 FS gates -> constant. All of
   these are positive weights or cone-constant invariants. Positivity forbids one side;
   symmetry cannot pick a point on the other.
3. **It converts the open "grading" handle into a number.** The counting-bit note says the
   right-shaped object is "a grading, not a complex structure". This computation says
   exactly *which* grading: one whose equivariant supertrace satisfies

   ```
   F/S = Tr(Gamma e^{-t D^2} R) / Tr(Gamma e^{-t D^2}) = -1/5
   ```

   That is a sharp, falsifiable, dimensionless target on any candidate graded operator, and
   `|F| <= S` means it is in range. It also immediately exposes the positivity tension: the
   repo already computed `Str(eps e^{-tD^2}) = 0` for the physical L/R grading, and `S = 0`
   gives `r = -2` (not a positive form). So the required object is tightly constrained:
   a grading with `S != 0`, `F/S = -1/5`, and `w_triv, w_nontriv > 0`
   (`F/S = -1/5` gives `w_triv = 3S/5`, `w_nontriv = 6S/5`, both positive for `S > 0` —
   **so the constraint is satisfiable in principle**, which is what makes it a real target
   rather than a dead end).
4. **Honest reading.** As stated, this is a no-go for the positive-weight template class and
   a specification for the graded class. It is *not* a derivation of `r`, and it does not by
   itself close the wall in either direction.

---

## 5. First artifacts (concrete, ranked)

**Artifact A (primary) — `ex3_pf_bound_equivariant_heat_weight.py`.**
Exact runner on `Z_N^3`, `N in {3,...,16}`, symbolic in `t` where possible:
(i) reprove `Tr(e^{-tDelta}R^j) = sum_m e^{-t(6-6cos(2 pi m/N))}` from the lattice (do not
cite the landed note — rebuild it, per the repo's build-cited-algebra rule);
(ii) prove `0 < F < S` by the sub-momentum identity;
(iii) derive `r(t) = (S+2F)/(S-F)` from the isotypic projectors;
(iv) certify `r(t) > 1` strictly and `dr/dt > 0`;
(v) solve exactly for the breach condition `F/S = -1/5`;
(vi) **comparator gate**: instantiate the flat point and the HS point natively and show
the flat point is the `t -> 0`, `N -> infinity` limit while the HS point is unreachable.
Deliverable shape: a bounded no-go plus a numeric specification, not a value claim.

**Artifact B (secondary) — the FP-dimension fork lemma.**
Exact runner: for `Rep_R(C_3)` and `Rep_C(C_3)`, build the fusion matrices, compute the
Frobenius-Perron eigenvector, and certify it equals the dimension vector (`(1,2)` real,
`(1,1,1)` complex). Then certify that any `C_3`-equivariant Bratteli matrix is a branching
matrix, hence its Markov trace is the dimension trace. Conclusion: **the Markov-trace /
Perron-Frobenius template — the only template family capable of non-dimensional weights —
collapses to dimension weighting on any equivariant tower.** This kills the strongest
a-priori candidate cleanly and permanently, and it is 30 lines of exact linear algebra.

**Artifact C (falsifier, cheap) — the sector-dependence filter.**
A three-line check that any proposed universal selector is falsified by the registered
non-charged-lepton `r` values (down `~0.597`, up `~0.773`). Any template whose output is a
function of `C_3` representation theory alone predicts the *same* `r` in every sector.
`FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND` already made this point for one functional;
it generalizes to the whole census and should be a standing gate on future proposals.

---

## 6. Where I think existing repo framing is misleading

Recorded as required by the exercise, not as claims:

1. **"One counting bit" is arguably the wrong shape.** `r` is a point on a continuous cone,
   and the registered non-lepton sectors sit at `~0.597` and `~0.773` — neither `1/2` nor
   `1`. Calling the residual a *binary* bit is a framing that fits the charged-lepton sector
   and silently excludes the comparators. The honest residual is a **continuous dial with
   two distinguished points**, which is what the exercise brief states and what the cone
   picture supports.
2. **"The framework's over-determined default is `Q = 1`" is stronger than the evidence.**
   §4 shows the positive-weight class lands at `r > 1` for any finite reading scale and only
   *approaches* `r = 1` in the ultra-local, infinite-volume limit. The flat point is a
   *limit*, not a default; at any finite reading the positive class over-weights the singlet.
3. **The Plancherel probe's terminus should be restated.** `probe12` records the closure step
   as failing "at the convention trap". The sharper statement is that the theorem *does*
   close, with the answer *dimension weighting*; there is no trap, there is a result that is
   not the desired one. That matters because it turns a "blocked probe" into a decisive
   comparator.

---

## 7. What this sector did NOT find, stated plainly

- **No template fixes `r = 1/2`.** Not one. Every family that fixes an isotypic relative
  normalization at all fixes it to dimension weighting (Plancherel, minimal index, Markov/FP,
  Artin-Ihara exponents, equivariant Weyl law, APS `rho`), and the families that could give
  something else either reproduce the free parameter verbatim (analytic torsion, modular/KMS,
  contact normalization) or cannot have their hypotheses met (Duistermaat-Heckman, formal
  degrees, zeta-scaling anomaly in finite dimension).
- **No literature authority is imported.** Every item above is a comparator; the only thing
  used as input is the framework's own landed lattice identity, and Artifact A rebuilds even
  that.
- **The wall is not solved.** §4 is a no-go for one large template class plus a numeric
  specification for the one open handle. It is not a derivation of `r` and not a proof that
  `r` is underivable.
- **Risk that §4 collapses into known content.** The main risk is that a reviewer reads
  `r(t) > 1` as a restatement of "the heat-kernel arrow flows `r -> 1`" (counting-bit
  synthesis §5). It is not the same statement — that one is a long-time attractor claim about
  a flow on `r`, this one is a strict one-sided bound on the *reachable set* of an entire
  functional class at every scale — but the distinction must be made explicit in any note, and
  the `F/S = -1/5` breach condition is the part that is unambiguously new.

---

## Sources (comparator literature only — never authority)

- [Frobenius-Perron dimension (nLab)](https://ncatlab.org/nlab/show/Frobenius-Perron+dimension)
- [Etingof-Nikshych-Ostrik, *On fusion categories*, Annals 162 (2005)](https://annals.math.princeton.edu/wp-content/uploads/annals-v162-n2-p01.pdf)
- [Perron-Frobenius theorem notes, V. S. Sunder (IMSc)](https://www.imsc.res.in/~sunder/pf.pdf)
- [The embedding theorem for finite depth subfactor planar algebras (arXiv:1007.3173)](https://arxiv.org/abs/1007.3173)
- [On conditional expectations of finite index (arXiv:math/9804074)](https://arxiv.org/pdf/math/9804074)
- [Minimal index and dimension for 2-C*-categories with finite-dimensional centers (arXiv:1805.09234)](https://arxiv.org/pdf/1805.09234)
- [Bismut, *Equivariant de Rham torsions*, Annals 159 (2004)](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n1-p02.pdf)
- [Equivariant torsion and G-CW-complexes (arXiv:dg-ga/9711011)](https://arxiv.org/pdf/dg-ga/9711011)
- [The variation formulas for the equivariant Ray-Singer metric (arXiv:0904.4569)](https://arxiv.org/pdf/0904.4569)
- [Terras-Stark, *Zeta functions of finite graphs and coverings, III*](https://mathweb.ucsd.edu/~aterras/graphbrauersiegel.pdf)
- [Artin-Ihara L-functions for hypergraphs (Adv. Math. 2024)](https://www.sciencedirect.com/science/article/abs/pii/S0001870824002603)
- [Ramacher, *Singular equivariant asymptotics and Weyl's law* (arXiv:1001.1515)](https://arxiv.org/abs/1001.1515)
- [Addendum to "Singular equivariant asymptotics and Weyl's law" (arXiv:1507.05611)](https://arxiv.org/pdf/1507.05611)
