# EXERCISE FOUR — broad mathematics sector search for a non-reality-type singlet/doublet discriminator

**Date:** 2026-07-24 · **Sector:** broad mathematics · **Base:** `origin/main` @ `1652deb63b`
**Status:** exercise output only. Nothing proposed for landing. No audit verdict set or predicted.
No axiom or primitive added. Every algebraic fact below was rebuilt natively in exact
sympy (probe `ex4_probe.py`, 26 gates, run in scratchpad; not a repo runner).

## Framework surfaces read before any conclusion

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (Lattice / Qubit / Admissibility / Record; Qualification;
  the "Relation To Dynamics" and "Open Gates" sections)
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`
- `docs/audit/data/axiom_premise_nodes.json` (4 canonical ids: `minimal_axioms`,
  `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`)
- `docs/ai_methodology/skills/review-loop/SKILL.md` (premise-type enforcement; Record guardrails;
  no new vocabulary; primitive registry check)
- `docs/repo/CONTROLLED_VOCABULARY.md` — consulted; **this report proposes no new repo name.**

Wall-specific surfaces read: `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`,
`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md` (the 8 lenses),
`FLAVOR_OPERATOR_SPECTRAL_FUNCTIONALS_DO_NOT_FORCE_R_HALF_NO_GO_NOTE_2026-06-02.md`,
`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`, `FLAVOR_DOUBLET_ROTATION_EXHAUSTIVE_NOTE_2026-05-30.md`,
`scripts/koide_infogeom_foot45_native.py`, `scripts/frontier_koide_a1_twisted_k_theory_probe.py`,
and the wave-1 campaign state at
`.claude/science/physics-loops/koide-mode-content-campaign-20260724/CAMPAIGN.md`.

**As instructed, axioms and approved primitives are treated as ASSUMPTIONS here.** Two repo framings
are challenged below (§0 and §E4).

---

## §0 — A framing correction that changes what must be searched for

Before the sweep: exact recomputation (gates F1–F6) shows the two named horns are **the same
quadratic form written in two Fourier-dual bases**, not two candidate metrics on one space.

With `H = aI + bC + b̄C²` and spectrum `λ_k = a + bω^k + b̄ω^{-k}`:

```
Σ_k λ_k = 3a                       Σ_k λ_k² = 3a² + 6|b|²
```

So `diag(3,6,6)` in the coefficient coordinates `(a, Re b, Im b)` **is** the flat Euclidean form
`Σ_k λ_k²` on the generation-spectrum space; and the "flat" coefficient form `a² + |b|²` pulls back
to weights `(1/3, 1/6, 1/6)` on the spectrum, i.e. ratio `2` — the *dual* horn. The horns are
exchanged by the DFT; `r = 1` is the self-dual point.

Consequently, in orthonormal spectrum coordinates (`s²  = 3a²` singlet-isotype norm², `d² = 6|b|²`
doublet-isotype norm²), with **no metric choice at all** (the metric is already in `Q`'s numerator):

```
Q = Σλ² / (Σλ)² = (1/3)(1 + d²/s²)          Q = 2/3  ⟺  d² = s²
```

**The counting bit is therefore not "which invariant form" but "why should the two isotypic
components of the realized spectrum carry equal norm".** `d²/s² = 1` gives `Q = 2/3`;
equipartition *per real dimension* gives `d²/s² = 2` and `Q = 1`. This matters for the search: a
tool that fixes a *metric* is structurally the wrong shape; a tool that fixes an *isotypic
normalization across blocks* is the right shape. Several entries below fail exactly on this seam.

Note also that `d²/s²` is a property of the **realized state**, and `realized_state_primitive`
supplies the slot but explicitly no weighting, measure, or typicality. Any equipartition argument
that says "the two isotypes are equally weighted because that is generic/typical" is barred by that
primitive's policing clauses. This is a genuine constraint on the target, not a technicality.

---

## §A — Chentsov / monotone-metric direction: **DECISIVE NEGATIVE, with the reason**

*(the direction the orchestrator most wanted interrogated)*

**Object.** The positive cone `C_3 = R³_{>0}` of unnormalized spectra `(λ_0, λ_1, λ_2)` with its
`S_3` (hence `C_3`) coordinate action; singlet = the mass direction `(1,1,1)`, doublet = the
tangent space to the fixed-mass slice.

**Tool.** Invariance under **congruent Markov embeddings** (Chentsov's morphisms), which is the
hypothesis of the uniqueness theorem.

**Result (gates A1–A8, exact).** Define, for arbitrary functions `A, B` of the total mass `|p|`,

```
g_p(u,v) = A(|p|) Σ_i u_i v_i / p_i  +  B(|p|) (Σ_i u_i)(Σ_j v_j)
```

For the congruent embedding `3 → 6`, `f(p)_{(i,0)} = p_i q_i`, `f(p)_{(i,1)} = p_i(1-q_i)`, sympy
verifies **exactly and for symbolic `A, B, q_i`** that `g^{(6)}_{f(p)}(df·u, df·v) = g^{(3)}_p(u,v)`,
and that mass is preserved. Permutation invariance is likewise exact.

At the barycentre the metric is `A·I + B·J`: spectrum `{A, A, A+3B}`, so

```
r = g_singlet / g_doublet = 1 + 3B/A          positivity (A>0, A+3B>0)  ⟺  r ∈ (0, ∞)
r = 1    ⟺ B = 0        (the Fisher/Shahshahani cone metric — the FLAT horn)
r = 1/2  ⟺ B = -A/6     (still exactly Markov-invariant, still positive definite — the HS horn)
```

**Both horns are realized by genuinely, exactly Markov-invariant metrics.** The strongest
invariance hypothesis available in classical information geometry does not merely fail to select
`r` — it leaves *precisely* `r` free and nothing else.

**Why (the structural reason, which is the real deliverable).** Chentsov's uniqueness theorem, and
Petz's quantum classification, are theorems on a **fixed-mass / fixed-trace slice**. The tangent
space of that slice is exactly the doublet; the singlet is the radial mass direction, which is not
a tangent direction of the simplex at all. So `r` — the ratio of the mass-direction weight to the
tangential weight — is invisible to every such theorem *by construction*. Extending to the cone
reintroduces exactly one free function, and it is `r`.

This also explains, without new machinery, why the repo's earlier probe
(`scripts/koide_infogeom_foot45_native.py`) found the quantum geometric tensor identically zero and
the Fisher metric azimuthally symmetric: those are simplex-side facts, and `r` is not a simplex-side
quantity.

**Extension check (Petz, done natively).** All Petz monotone metrics restrict to the classical
Fisher metric on commuting (diagonal) states, and are defined on trace-1 density matrices, so the
quantum family adds nothing here: it is (i) a family, not unique, and (ii) trace-fixed.

**FIRST ARTIFACT (a decisive negative worth landing).** `scripts/…_chentsov_cone_invariance_no_go.py`:
the 8 exact gates above plus a construction-mutation rejector (perturb `g` off the `A·I + B·J` form
and show invariance *fails*, so the PASS is caused by the structure and not asserted). Deliverable:
a narrow no-go note stating "no Markov-congruent-invariant metric on the spectrum cone selects `r`;
`r` is exactly the residual freedom of the Chentsov class on the cone." This closes the entire
information-geometry attack class with a theorem rather than a probe list — the same shape as the
campaign's FS-constant-across-the-cone result, on a disjoint class.

---

## §B — Fusion-category dimension theory: **a genuine forcing that selects the WRONG horn**

**Object.** The fusion ring of the generation carrier's symmetry: `Rep(S_3)` (simples `1, ε, std`),
`Rep(C_3)` over `C` (three invertible simples), and the **real** fusion ring `Rep_R(C_3)` (basis
`1, D` with `D⊗D = 2·1 ⊕ D`).

**Tool.** Frobenius–Perron dimension — the theorem that *forces* a normalization: the unique
positive character of a fusion ring, given by the PF eigenvector of the fusion matrices.

**Result (gates B1–B3, exact).**
- `Rep(S_3)`: `d_std` is the positive root of `d² = 2 + d` ⇒ **`d_std = 2`, forced**.
- `Rep_R(C_3)`: `N_D = [[0,2],[1,1]]`, eigenvalues `{2, −1}` ⇒ **`FPdim_R(D) = 2`, forced**, so the
  forcing is *robust to the base field* — it does not become 1 over `R`.
- `Rep(C_3)/C`: the doublet is two invertible simples ⇒ categorical count 2.

**Verdict.** FPdim is a real forcing theorem and it gives the doublet the value **2** in every
version. A sector weighting read off categorical dimension is `(1,2)` ⇒ **`r = 1`, `Q = 1`** — the
non-Koide horn. There is no fusion-category structure on this generation carrier in which the
doublet has dimension 1: FPdim 1 means *invertible*, and `D⊗D` contains `1` with multiplicity 2.

**Honest boundary (why this is not yet a closure).** FPdim forces *dimensions*, not *carrier-form
weights*. `1` and `D` are non-isomorphic simples, so the space of invariant forms on `1 ⊕ D` still
has one scalar per simple (Schur) and the category supplies no map between them. What the category
*does* canonically fix is the trace on `End(X)` — and that trace is the ordinary matrix trace, i.e.
`r = 1` again.

**FIRST ARTIFACT.** `scripts/…_fusion_fpdim_forces_dimension_count.py`: build `N_D` from the actual
tensor decomposition (rebuilt from characters, not asserted), compute the PF eigenpair exactly, and
gate the rejector "if `FPdim(D)` were 1 the fusion ring would not be associative / `D` would be
invertible". Deliverable: a narrow bounded note **"categorical dimension forces the dimension count
`r = 1`, not the block count `r = 1/2`"** — a *falsifier for the Koide horn* conditional on a
categorical-dimension reading, which is a stronger and more useful statement than "unforced".

---

## §C — Subfactor / Jones-index / Markov-trace direction: **the best surviving lead**

This is the one entry that is both non-foreclosed and structurally capable of forcing. It is also
the only direction in the sweep that produces a *decisive* experiment whose failure mode is
informative.

**Object.** The commutant `End^{C_3}(V)` of the generation carrier and, above it, a **tower** of
finite-dimensional algebras generated by the framework's own nearest-neighbour Admissibility rule
(the Lattice/Qubit per-site algebra `M_2(C)` tensored along an admissible chain), with its Bratteli
diagram `Λ` at each level.

**Tool.** The **Markov trace**: for a connected Bratteli inclusion with matrix `Λ`, the trace whose
weight vector `s` satisfies `ΛΛᵀ s = β s` is **unique**, because a connected non-negative matrix has
a unique positive PF eigenvector (up to scale). This is a forcing theorem of exactly the shape the
wall needs, and it is a statement about *relative normalization between blocks* — the seam §0
identified — not about a metric.

**The precise diagnosis it yields (this is new for this wall).** Enumerating all `2×2` Bratteli
matrices with entries in `{0,1,2}` and computing PF weight ratios exactly:

| `Λ` | `s₁/s₀` | connected |
|---|---|---|
| `[[0,1],[0,0]]` | `0` | **no** — PF gives no relative normalization |
| `[[0,1],[0,1]]` | `1` | yes |
| `[[0,1],[0,2]]` | `2` | yes |
| `[[0,2],[0,1]]` | `1/2` | yes |
| `[[0,1],[1,1]]` | `(1+√5)/2` | yes |
| `[[1,2],[0,1]]` | `√2 − 1` | yes |
| `[[1,2],[2,0]]` | `(√17 − 1)/4` | yes |

Two facts fall out:

1. **The wall, restated operator-algebraically: the singlet and doublet blocks are *disconnected
   components* of the Bratteli diagram of the `C_3`-commutant, and Perron–Frobenius fixes weights
   only *within* a connected component.** This is the same content as the Schur foreclosure, but in
   a form that names what would remove it: a connecting inclusion.
2. **Generic connected diagrams force an *irrational* weight ratio.** Rational ratios `1, 2, 1/2`
   occur only for special (essentially block-scaled) `Λ`. So a Markov-trace computation on the
   framework's own tower has three possible outcomes, and *all three are informative*:
   - ratio `1/2`-equivalent ⇒ the Koide horn is **derived**;
   - ratio `1`-equivalent ⇒ the counting bit closes **against** Koide (publishable negative);
   - **any other value** ⇒ the landed binary framing is itself **wrong** — the counting bit is not
     a bit — which would be the most valuable outcome of all and is not currently on anyone's map.

**Is this foreclosed?** No. The 8 tested lenses were `J_cs`, geometric quantization / Kähler
polarization, MDL record, equivariant holomorphic index, KMS/modular, Grassmann/Pfaffian, CPT /
antiunitary, canonical-quantization uniqueness. The nearest, KMS/modular, is a statement about a
*given state's* modular automorphism group; the Markov trace is a statement about a *tower's* PF
structure and is a different object. Repo-wide, "Jones index"/"subfactor" occur only in the
`OBSERVABLE_PRINCIPLE_P1_BRIDGE_JONES_INDEX_SUBFACTOR_NARROW_NOTE_2026-05-21` lane and never in the
flavor lane; `"Markov trace"`, `"Frobenius-Perron"`, `"FPdim"` have **zero** occurrences in `docs/`
and `scripts/`.

**FIRST ARTIFACT (build this first).** `scripts/…_admissibility_tower_bratteli_markov_trace.py`:
(1) construct the two-site and three-site admissible algebra from the Lattice+Qubit+Admissibility
data as already realized in the repo's staggered/corner carrier, (2) compute its Bratteli matrix
`Λ` **by decomposing actual modules**, never by asserting multiplicities, (3) test connectivity of
`ΛΛᵀ` between the generation singlet and doublet blocks, and (4) if connected, compute the PF
eigenvector exactly and report `s₁/s₀`. **Kill-check gate to run first, inside the same runner:** if
the diagram is disconnected at every level, the runner must FAIL-report that and the lead dies
immediately — that is the cheap, decisive falsifier, and it should be gated with a
construction-mutation rejector (perturb the admissibility rule and show the diagram changes).

---

## §D — Directions swept and found EMPTY (each with the exact reason)

| Direction | Object / tool | Exact finding | Verdict |
|---|---|---|---|
| **Higher FS indicators** | `ν_n(χ) = |G|⁻¹ Σ_g χ(gⁿ)` on `C_3` | `ν_n(triv) = 1` ∀n; `ν_n(ω) = ν_n(ω̄) = [0,0,1,0,0,1]` for n=1..6 (exact, `ω = rootof(x²+x+1)`) | **Empty.** They separate singlet from doublet as a *partition* (0 vs 1) but are identical on `ω`/`ω̄` and are properties of the representation, hence constant along the form cone — the same blindness the campaign's FS result already proved. Partition, not weight. |
| **Twisted indicators / Schur multiplier / projective reps** | `H²(C_3, C^×)`, `H²(S_3, C^×)` | `C^×` is divisible ⇒ every 2-cocycle `c` on a cyclic group is the coboundary of `b(gⁱ) = tⁱ` with `t³ = c`; `H² = 0`. Same for `S_3`. | **Empty by theorem.** There is no twisted sector to carry a twisted indicator. This direction is not "hard", it is *vacuous* for this group. |
| **Modular rep theory at the bad prime 3** | `F_3[C_3] = F_3[y]/y³` (verified: `x³−1 = (x−1)³` over `F_3`) | The algebra is local: exactly **one** simple Brauer character (trivial); decomposition matrix is the all-ones column `(1,1,1)ᵀ`; Cartan matrix `= (3)`. | **Empty, and worse than neutral: at `p = 3` the sector distinction *dissolves*.** The doublet's Brauer character is `2 ×` trivial, so the only mod-3 weight vector is `(1,2)` = the ordinary dimensions ⇒ `r = 1`. Characteristic 3 cannot separate what it cannot see. |
| **Galois descent on `Q(ω)`** | `Gal(Q(ω)/Q) = Z/2`, `ω ↔ ω̄` | A `Q`-rational readout is Galois-invariant, hence constant on Galois orbits: it can see the *orbit* `{ω, ω̄}` but assigns it no weight relative to `{triv}`. | **Empty**, and it reproduces the landed `KCPT_ORBIT_COUNT_IS_THE_PARTITION_NOT_THE_WEIGHT` content by a different route. Partition again. |
| **Arithmetic: Schur index** | `m_Q(χ_doublet)` | `C_3` abelian ⇒ the character field is a splitting field ⇒ `m = 1` at every place. | **Empty, but structurally revealing** — see §E1. |
| **(Twisted) equivariant K-theory** | `K_{C_3}^τ(pt)` | Already probed in `scripts/frontier_koide_a1_twisted_k_theory_probe.py` (NO-GO), and with `H²(C_3,U(1)) = 0` there is no twist at all; the base (positive cone) is contractible so `K_{C_3}(X) = R(C_3)`, whose natural pairing is the character inner product ⇒ weights `(1,2)`. | **Empty; already foreclosed.** Re-proposing it would be a re-walk. |
| **Hopf-algebra integral / Frobenius form** | Larson–Sweedler: the integral of a f.d. Hopf algebra is unique up to scalar | The resulting Frobenius form `λ(xy)` on `C[C_3]` is the *reversal* permutation form, invariant under the **adjoint** action (trivial here), not under the regular action that defines the singlet/doublet split. | **Empty by mismatch of action** — the unique object is invariant for the wrong group action. |

---

## §E — Four structural observations that outlive the sweep

**E1. Every "2" in this problem is a degree, and the only index is 1.** The factor that would give
`r = 1/2` is `dim_R End(D) = 2` (`= [Q(χ):Q]`, `= |Galois orbit|`, `= FPdim(D)`). The Schur index —
the arithmetic invariant that measures a genuine *division-algebra* obstruction — is **1** for this
character at every place. So the doublet's "2" is everywhere a *degree/orbit size*, never an index.
Degrees give partitions; only an index could give an asymmetric weight. **There is no division
algebra in this problem except `C` at the archimedean place**, and using that one is precisely the
foreclosed reality-type route. This is, I believe, the deepest reason the FS foreclosure is not an
accident: reality type is the *only* place a `2` of the required kind lives.

**E2. Every forcing theorem in the sweep lands on `r = 1`.** FPdim (§B), the mod-3 decomposition
matrix (§D), the categorical trace, the Watatani/Jones index of `R ⊂ C` (`= 2 = dim_R`), the
character inner product on `R(C_3)` — all give the doublet weight 2 per block, i.e. `(1,2)`, i.e.
`r = 1`. The tools that *cannot* force leave `r` free; the tools that *can* force select `Q = 1`.
**The honest current state of the mathematics is that it points against the Koide horn**, and the
repo should consider whether the publishable result here is a negative rather than a derivation.

**E3. The two horns are the two base fields.** Wedderburn block counts (gates E1–E3):
`Q[C_3] = Q ⊕ Q(ω)` and `R[C_3] = R ⊕ C` have **2** blocks; `C[C_3]` has **3**. The block count is
`(1,1)` over `Q` or `R` and `(1,2)` over `C`, and those are exactly the two horns. If this
identification is tight, then the counting bit ≡ the choice of base field for the generation
carrier — and the **Qubit axiom explicitly declares the real (`Cl(3,0)`) and complex (`M_2(C)`)
presentations equivalent and adds no further primitive structure**. On that reading the axioms
*cannot* force the count, and the wall's closure is a no-go at the axiom level rather than a missing
construction. **This is a claim, not a result** — the step "counting bit ≡ base-field choice" is
exactly what needs proving. **First artifact:** a runner that, for each of the enumerated forcing
tools, computes the weight vector over `Q`, `R`, and `C` and checks whether the tool's output is a
function of the base field alone. If it is, the no-go is a theorem about the axiom system and is
publishable as such (an explicitly welcomed closure outcome).

**E4. A challenge to a landed framing.** §0 shows `diag(3,6,6)` and `diag(1,1,1)` are the *same*
form in Fourier-dual bases, so calling them "two points on a cone of invariant forms" is at least
misleading: the `r`-cone is a cone of *bases*/normalizations, not of geometrically distinct
invariant structures, and the horns are exchanged by the DFT with `r = 1` self-dual. The landed
`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02` note calls `diag(3,6,6)` the "HS/coherent-state
metric on the coefficient surface" without recording that it is the flat spectrum form pushed
through the DFT. I flag this as a possible mis-framing to re-derive, alongside the campaign's own
flag #1 (the `r`-neutral 6-vs-12 Grassmann horn). Both flags point the same way: the four-way
equivalence at the head of the campaign may not be four equivalent statements.

---

## §F — Ranked output

1. **§C Markov trace / Bratteli PF on the Admissibility tower** — the only non-foreclosed direction
   with a genuine forcing theorem *of the right shape* (relative block normalization, not a metric),
   and the only one whose first artifact is decisive in all three outcomes, including the outcome
   that falsifies the binary framing itself. **Build this first.**
2. **§A Chentsov/Campbell cone no-go** — cheapest real deliverable: 8 exact gates already pass, and
   it closes the whole information-geometry class with a theorem plus the reason (trace-direction vs
   simplex-tangent), not a probe list.
3. **§B fusion/FPdim forces `r = 1`** — a landable falsifier for the Koide horn conditional on a
   categorical-dimension reading; also the sharpest statement of §E2.
4. **§E3 base-field identification** — highest ceiling (a no-go at the axiom level) but the
   load-bearing step is unproven; do not advertise it before the runner exists.
5. §D — six directions swept empty, each with an exact reason; useful as N1-table rows in any
   future no-go note, and they should stop these directions being re-proposed.

**Nothing in this report solves the wall.** Two of the five entries are negatives, one is a negative
pointing at the wrong horn, one is unproven, and only §C is a live construction.
