# WAVE 1 — DERIVATION B (operator / representation-theory side)

Worker report. Not a note, not a PR, not an audit verdict. Written against
`origin/main` content at `FETCH_HEAD = 02f9359281f3e6bd849396da33710308a27a3949`
(2026-07-24). Every `docs/` file quoted below was checked byte-identical
between the local worktree and `FETCH_HEAD` before quoting
(`git diff --stat HEAD FETCH_HEAD -- <file>` empty for each).

---

## 1. VERDICT (stated first, because it is a negative)

**The route assigned to Derivation B is already foreclosed by landed content,
and the foreclosure is correct. I reproduce it independently and sharpen it.**

Three separable results, in decreasing order of how much of them is new:

**(B-1) The Frobenius-Schur indicator of the charged-lepton corner carrier's
doublet is `0` (COMPLEX type), not `+1` and not `-1`.** This is landed
(2026-06-07) and I rebuilt it exactly (95 exact sympy gates, §5–§7). The binary
posed in my task — "real structure ⇒ count `n`, or quaternionic doubling ⇒
count `2n`" — presupposes `FS ∈ {+1, -1}`. The carrier sits in the third case.

**(B-2) `FS = 0` is not a *failure* to decide the count. `FS = 0` is, exactly
and definitionally, the statement that the count-once / count-twice binary
EXISTS.** This is the sharpening I can contribute. The indicator trichotomy is
precisely a trichotomy about the relation between the real and complex
dimension of an isotype:

| indicator | `dim_R`(real irrep) vs `dim_C`(complex irrep) | `End_R` | is there a count binary? |
|---|---|---|---|
| `FS = +1` | `dim_R = dim_C` | `R` | **no** — the two counts coincide |
| `FS = 0`  | `dim_R = 2 · dim_C` | `C` | **yes** — the two counts differ by exactly the factor 2 in question |
| `FS = -1` | `dim_R = 4 · dim_C` | `H` | **no** — the factor is 4, not the binary's 2 |

Computing `FS = 0` therefore *reports the existence of the binary back to you*.
It is the one value of the three that is structurally incapable of resolving it.
A derivation that computes `FS` and then reads off a horn is reading its own
premise.

**(B-3) The task's own premise — "is `K/CPT` a real structure or a quaternionic
one?" — is itself not fixed by the carrier's representation theory.** On the
doublet block `ω ⊕ ω̄` the space of `C_3`-equivariant antilinear maps is
2-complex-dimensional, and it contains antiunitary representatives with
`J² = +1` AND with `J² = -1`, *both of which commute with the entire K-real mass
family* (§8, gates Q1–Q8, exact). The landed physical `K` happens to have
`K² = +1` — that is a property of the **supplied** `K`, not something the
carrier forces. So the real-vs-quaternionic question has an answer only because
a specific `K` was supplied, and once supplied it still does not move `r`.

**Bottom line for the campaign.** Derivation B does not deliver a horn. It
delivers a *reason* the operator-side route cannot deliver one, and that reason
is stronger than "nobody has managed it": the invariant being computed is
constant on the entire family the answer varies over (§9). I recommend the
campaign treat the FS/reality lane as **closed**, and I flag in §11 the one
place the operator side is *not* closed.

---

## 2. CRITICAL HONESTY CHECK — the repo already answers this

My task asked me to search `docs/` for Frobenius-Schur, reality census,
CP-completion, kcpt, and to say plainly if the question is already answered.
**It is answered, in four separate landed places, one of which names my exact
route and marks it ruled out.** Verbatim, with `file:line`:

### 2.1 The indicator itself, landed 2026-06-07

`docs/KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md:15-16`

> - The C₃ nontrivial irreps `ω, ω̄` are **Frobenius-Schur complex type**
>   (`FS(ω) = FS(ω̄) = 0`, since `ω ≠ ω̄`).
>   The real 2-dimensional "doublet" is the **realification of a complex-type
>   irrep**. [runner (1)]

same file `:31`

> The FS typing does **not** by itself prove `r = 1/2` is selected.

same file `:40-46`

> `FS = 0` (complex type) plus the complex `M₂(ℂ)` carrier (Quantum axiom) are
> **necessary but not sufficient** to force `r = 1/2`:
>
> - The native flavor complex structure `J_cs = (C − C²)/√3` is a genuine
>   complex structure on the doublet (`J_cs² = −P_doublet`) **but commutes with
>   the entire K/CPT-real mass family** `H = aI + bC + b̄C²` (`[J_cs, H] = 0`).
>   It is therefore **measure-neutral** — silent on `r`, unable to select the
>   complex-type / holomorphic readout over the realified one. [runner (3)]

### 2.2 My exact route, listed as RULED OUT in a landed no-go's N1 table

`docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md:157`

> | Complex-type/orientation/Frobenius-Schur route | RULED OUT BY PRIOR as selector | The complex-type/orientation note supplies type information, not the asymmetric weighting rule; see [`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md`](KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md). |

same file `:42-48` — the enumerated lens list contains "CPT / antiunitary",
i.e. the exact object my task asks me to classify:

> An adversarial reframing of the **static** polarization selector class: 14
> prior refuted/attempted routes mapped, then **8 selection-principle
> lenses** were tested (framework-native complex structure `J_cs`; geometric
> quantization / Kähler polarization; minimum-information / MDL record;
> equivariant holomorphic index; KMS / modular; Grassmann / Pfaffian
> statistics; CPT / antiunitary; canonical quantization uniqueness).
> **Result inside the tested class: 0 of 8 survived.**

same file `:58-60` — and it names the failure mode as **circularity**, which is
exactly the supervisor's Wave-0 predicted risk:

> Transferring an operator-symmetry onto "the energy counts `b` once" is a
> category slip and is **circular** (it assumes the asymmetric `(1,1)` split it
> claims to derive).

### 2.3 The real-vs-quaternionic question, landed 2026-06-08

`docs/KOIDE_KODIM_REAL_STRUCTURE_ROUTE_EMPTY_R_UNDETERMINED_BOUNDED_NO_GO_NOTE_2026-06-08.md:38-40`

> 1. **`J² = +1`, not `−1`** (A,B). KO-dimension 3 *requires* `J²=−1`; the
>    framework's `J=U_swap∘conj` is an involution (`J²=+1`). With `JD=+DJ` the
>    pair `(+,+)` is KO-dim 0 or 7, and since **no within-generation `ℤ₂`
>    grading `χ` anticommutes with a generic circulant `D`**, the generation
>    triple is **odd = KO-dim 7, ungraded**.

same file `:74-77`

> The axioms and the real structure **name no `r`**. So **`r` is undetermined
> by {Lattice, Quantum, Record} + the real structure / KO-dimension** — the
> discriminating datum lives below their resolution.

**This is a direct, landed, dated answer to the literal question in my task.**
The K/CPT structure is a REAL structure (`J² = +1`), it is NOT quaternionic,
and that fact is explicitly recorded as *not* selecting `r`.

### 2.4 The KCPT reality-census lane (2026-07-19/20) — the same answer at scale

`docs/KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md:19`

> `FS = (0, 0, 0, 0, +1)`.

`docs/KCPT_EXTENDED_GROUP_REALITY_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md:19`

> `FS_H = (+1, +1, +1, +1, +1, +1)`  — every constituent is real / orthogonal type.

same file `:27`

> `(0, 0, 0, 0, +1)` over ranks (4, 4, 6, 6, 12)  →  `(+1, +1, +1, +1, +1, +1)`
> over (8, 8, 12, 12, 12, 12).

and, in that note's own boundary, same file `:51`

> It fixes no free parameter, selects no bulk sign-family member, and chooses no
> dynamics; it is r-neutral, orientation-neutral, and takes no external
> numerical or literature input.

**The KCPT census declares itself `r`-neutral in its own boundary sentence.**
And §9.2 below shows *why* it must: the `0 → +1` flip is produced BY the
doubling, so it cannot be evidence about the doubling.

### 2.5 Ledger status of everything quoted (checked live, not from memory)

Read from `docs/audit/data/ledger/**` and cross-checked against
`docs/audit/data/audit_ledger.json`:

| claim_id | claim_type | effective_status |
|---|---|---|
| `koide_doublet_is_frobenius_schur_complex_type_orientation_bounded_note_2026-06-07` | bounded_theorem | **unaudited** |
| `koide_kodim_real_structure_route_empty_r_undetermined_bounded_no_go_note_2026-06-08` | no_go | **unaudited** |
| `koide_r_half_polarization_selector_tested_static_readout_no_go_note_2026-06-08` | no_go | **unaudited** |
| `koide_real_rep_block_count_permitted_not_forced_note_2026-05-30` | no_go | **unaudited** |
| `koide_reality_type_permitted_not_forced_note_2026-05-30` | bounded_theorem | **unaudited** |
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | no_go | **unaudited** |
| `kcpt_holomorphic_reality_cp_census_frobenius_schur_bounded_theorem_note_2026-07-20` | bounded_theorem | **unaudited** |
| `kcpt_extended_group_reality_census_frobenius_schur_bounded_theorem_note_2026-07-20` | bounded_theorem | **unaudited** |
| `kcpt_cp_completion_under_extended_group_bounded_theorem_note_2026-07-20` | bounded_theorem | **unaudited** |
| `koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04` | bounded_theorem | **unaudited** |
| `kcpt_coupling_triple_berezin_count_binary_measure_collapse_bounded_theorem_note_2026-07-17` | bounded_theorem | **unaudited** |

**FLAG (stale status citation on main).**
`docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:72`
calls `koide_frobenius_isotype_split_uniqueness` **`retained_no_go`** (also at
`:140`, `:151`, `:188`). The live ledger says **`unaudited`**. I did not rely on
the label: I re-derived the free-parameter fact independently (§9.1, gates
G3/G4). Flagging because the campaign must not treat the free-parameter
foreclosure as retained-grade on the strength of that sentence. I am not
asserting the label is *wrong* — only that it does not match the live ledger
today, and I am not authorized to change either.

**Consequence for the campaign's Hard Rule 1 (kill-check).** The kill-check
bites on this lane. Derivation B is a re-walk unless it produces something the
landed notes do not have. §6–§9 are my attempt at exactly that; §10 says what I
think is genuinely new versus merely reproduced.

---

## 3. The carrier and the group, identified from landed content

The campaign says "the charged-lepton corner carrier". Landed content pins it:

`docs/KCPT_CORNER_CARRIER_ANTILINEAR_NONHERMITIAN_KREAL_READOUT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md:41-45`

> The corner carrier is `C = [[0,0,1],[1,0,0],[0,1,0]]`, real, with `C^3 = I_3`,
> `C^T = C^2`, and `K C K = C`. The unnormalized channel vectors are the singlet
> `v0 = (1,1,1)^T` and the conjugate doublet pair
> `vw = (1, conj(w), conj(w)^2)^T`, `vwb = conj(vw)`, with `C vw = w vw` and
> `C vwb = conj(w) vwb`.

`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:58-64`

> - **Supplied corner carrier (R1b).** The real cyclic `C` with `C^3 = I_3`, the
>   coupling triple `W(a,b,c) = a*I + b*C + c*C^2`, the character projectors
>   `P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for
>   `chi in {1, w, conj(w)}`, `w = -1/2 + (sqrt(3)/2)*i`, and entrywise
>   conjugation `K` in the canonical basis, all as pinned by the
>   spectral-pairing note. **FLAG — supplied surface:** this is the mechanism
>   lineage's declared corner surface, not a derived physical carrier.

So, answering the first requirement of my task:

- **Group actually acting:** `C_3 = ⟨C⟩ ≅ Z/3`, order 3. (Not a larger group.
  The `hw=1` three-corner carrier's *observable algebra* is `M_3(C)`
  — `docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md` link
  L3 — but the symmetry that organises the mass operator into isotypes, and the
  only group the reality question is asked about, is `C_3`.)
- **Representation the charged-lepton corner carries:** the regular
  representation `R[Z_3]`, complexifying to `C^3 = 1 ⊕ ω ⊕ ω̄`. The Koide
  `r` question lives entirely on the doublet part `ω ⊕ ω̄`.
- **`K/CPT`:** entrywise complex conjugation in the canonical basis, `K C K = C`,
  `K² = +1`. The framework's *real structure* in the KO/NCG sense is the landed
  `J = U_swap ∘ conj` with `U C U = C²` (`KOIDE_KODIM...:32-33`).

**FLAG — carrier status is SUPPLIED, not derived.** The note itself flags this
(`R1b`, quoted above). Everything below inherits that. The campaign's target
sentence "build the CAR algebra of the charged-lepton corner carrier natively"
cannot be discharged on a supplied surface; the surface would first have to be
derived. I did not attempt that and it is not in my task.

---

## 4. What I ran (all exact, all in scratch — no repo files created)

Three scratch runners, `sympy`, exact (`Rational`/cyclotomic, no floats in any
load-bearing comparison — noting the repo lesson that sympy `==` is structural
and `Float ≠ Rational`; one gate initially failed on exactly that and was fixed
to `sp.Integer` arithmetic):

| runner | gates | result |
|---|---|---|
| `fs_derivation_b.py` — carrier, FS, real structure, invariant cone, `ν → w → r → Q`, Berezin doubling | 71 | `TOTAL: PASS=71 FAIL=0` |
| `fs_mutation_battery.py` — CONSTRUCTION-mutation probes of the FS routine | 16 | `TOTAL: PASS=16 FAIL=0` |
| `fs_antiunitary_space.py` — space of equivariant antilinear maps | 8 | `TOTAL: PASS=8 FAIL=0` |

Located under the session scratchpad
`/private/tmp/claude-502/.../scratchpad/`. **These are worker probes, not
gates** (campaign Hard Rule 4 / lesson 55). §12 designs the gates a real runner
would carry.

---

## 5. The Frobenius-Schur indicator, computed exactly

### 5.1 The computation

`FS(χ) = |G|^{-1} Σ_{g∈G} χ(g²)`. For `G = C_3 = {e, C, C²}` and
`χ_k(C^j) = ω^{kj}` with `ω = -1/2 + (√3/2)i`:

Squares: `e² = e`, `C² = C²`, `(C²)² = C⁴ = C`. So the multiset `{g² : g ∈ G}`
is `{e, C², C}` — a bijection of `G` (3 is odd), which is the whole reason the
answer is a character sum of the *same* character.

**Trivial character `χ_0 ≡ 1`:**

```
FS(χ_0) = (1/3)[ χ_0(e) + χ_0(C²) + χ_0(C) ]
        = (1/3)[ 1 + 1 + 1 ]
        = 1
```

**Doublet character `χ_1(C^j) = ω^j`:**

```
FS(χ_1) = (1/3)[ χ_1(e) + χ_1(C²) + χ_1(C) ]
        = (1/3)[ 1 + ω² + ω ]
        = (1/3)[ 1 + (ω + ω²) ]
        = (1/3)[ 1 + (-1) ]            since 1 + ω + ω² = 0
        = 0
```

**Conjugate doublet character `χ_2(C^j) = ω^{2j} = ω̄^j`:** identical algebra,

```
FS(χ_2) = (1/3)[ 1 + ω⁴ + ω² ] = (1/3)[ 1 + ω + ω² ] = (1/3)[1 - 1] = 0
```

**Independent route — the full carrier.** The regular representation on `C^3`
has `χ_reg(e) = 3`, `χ_reg(C) = χ_reg(C²) = 0`:

```
FS(reg) = (1/3)[ χ_reg(e) + χ_reg(C²) + χ_reg(C) ] = (1/3)[3 + 0 + 0] = 1
```

and the constituent sum agrees: `FS(χ_0) + FS(χ_1) + FS(χ_2) = 1 + 0 + 0 = 1`.
Two routes, same answer (gates B1–B7).

### 5.2 Result

```
FS(trivial)    = +1     real / orthogonal type
FS(ω)          =  0     COMPLEX type
FS(ω̄)          =  0     COMPLEX type
FS(ω ⊕ ω̄) sum  =  0
FS(full carrier C^3) = +1
```

**Answer to my task's binary: NEITHER. The charged-lepton doublet is
complex type.** Rejector gates B4/B5 explicitly assert `FS(ω) ≠ +1` and
`FS(ω) ≠ -1`.

### 5.3 CONSTRUCTION-mutation probes (campaign Hard Rule 3, lesson 53)

An FS routine that always returns `0` would produce `FS(ω) = 0` for free. So the
mutation battery mutates the **construction** (the explicit matrix group, closed
multiplicatively from generators — no character table is typed in) and checks
the routine spans the full trichotomy:

| mutation | group (closed from generators) | `FS` | discriminates |
|---|---|---:|---|
| M0 — the actual constituent | `⟨[ω]⟩`, order 3 | `0` | the claim |
| M1 — mutate character to real | `⟨[-1]⟩ = Z_2`, order 2 | `+1` | routine **can** return `+1` |
| M2 — mutate order 3 → 4 | `⟨[i]⟩ = Z_4`, order 4 | `0` | complex type is not a `C_3` artifact |
| M3 — mutate to a quaternionic carrier | `⟨diag(i,-i), [[0,1],[-1,0]]⟩ = Q_8`, order 8 | `-1` | routine **can** return `-1` |
| M4 — CP-complete M0 | `⟨diag(ω,ω̄), swap⟩ = S_3`, order 6 | `+1` | see §9.2 |
| M5 — full carrier | `⟨C⟩` on `R^3`, order 3 | `+1` | consistency |
| M6 — doublet block alone | `⟨diag(ω,ω̄)⟩`, order 3 | `0` | the claim, second frame |

Gate M7: `{+1, 0, -1} ⊆ observed`. **The routine returns all three values on
mutated constructions and `0` on the actual one.** `FS(ω) = 0` is therefore a
computed fact, not a default.

---

## 6. What `FS = 0` means as an operator statement

Restated as antilinear-operator existence, which is the form my task asks for:

- `FS(V) = +1` ⟺ there is an invariant antiunitary `J : V → V` with `J² = +1`
  (a **real structure**); its fixed set `V^J` is a real form,
  `dim_R V^J = dim_C V`.
- `FS(V) = -1` ⟺ there is an invariant antiunitary `J : V → V` with `J² = -1`
  (a **quaternionic structure**); `V` has no invariant real form.
- `FS(V) = 0` ⟺ **there is no invariant antilinear map `V → V` at all** except
  `0`.

For the doublet constituent `ω` this last case is verified directly rather than
inferred (gate C3). An invariant antilinear `J` on the line `span{vw}` must have
the form `x·vw ↦ x̄·t·vw`. Equivariance under `C`:

```
J(C · x vw) = J(ω x vw) = conj(ω x) t vw = ω̄ x̄ t vw
C · (J(x vw)) = C · (x̄ t vw)            = ω  x̄ t vw
```

Equality for all `x` forces `ω̄ t = ω t`, i.e. `(ω - ω̄) t = 0`. Since
`ω - ω̄ = i√3 ≠ 0`, we get `t = 0`. `sympy` returns `[{t: 0}]` (gate C3).

**So `K` cannot act on the charged-lepton doublet constituent at all.** It
necessarily maps `ω → ω̄`, a *different* irreducible (gate C6:
`K vw = vwb`). This is the operator content of `FS = 0`.

---

## 7. The translation chain, stated as separately checkable claims

My task asks for the indicator → mode count → `w` → `r` translation with each
step a separate claim. Here it is. **Steps T1–T3 and T6–T9 are exact and hold.
Step T4→T5 is where the chain breaks, and it breaks structurally.**

**T1 (exact, gates B1–B7).** `FS(ω) = FS(ω̄) = 0`; `FS(1) = +1`; the carrier
total is `+1`.

**T2 (exact, gate C3).** `FS(ω) = 0` ⟺ the only `C_3`-equivariant antilinear map
`ω → ω` is `0`.

**T3 (exact, gates C6–C9).** `K` maps `ω ↔ ω̄`; the fixed set of `K` on the
doublet block is the real 2-plane `D = (ω ⊕ ω̄)^K = span_R{ vw + vwb,
i(vw - vwb) }`, with `dim_R D = 2 = dim_C(ω ⊕ ω̄)`. **`K` is a genuine real
structure on the doublet block, with real form of real dimension 2.** Not
quaternionic.

**T4 (exact, gates F1–F6).** `End_R(D) ≅ C`, generated by `J_cs = (C - C²)/√3`:
`J_cs` is real, `J_cs² = -P_doublet`, `J_cs` commutes with `K` (because it is
real), hence descends to `D`, making `(D, J_cs)` a 1-dimensional complex vector
space.

**⟹ At T4 the object is simultaneously `2` real modes and `1` complex mode.
Both descriptions are exact and refer to the same 2-real-dimensional object.
There is no third fact in the representation theory that adjudicates.**

**T5 (THE BROKEN STEP).** To get a mode *count* one must choose whether the
measure integrates `D` as `R²` or as `C¹`. The FS indicator is a single integer
attached to a representation; it is by construction invariant under everything
that distinguishes those two integrations (§9.1). **`FS = 0` is exactly the
condition under which `dim_R = 2 · dim_C`, i.e. exactly the condition under
which the two counts differ by the factor 2 the binary is about.** The indicator
reports the binary; it does not resolve it.

The landed refutation of the tempting shortcut at this step, verbatim
(`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md:71-73`):

> **N7 steelman.** A reader could argue that complex type should select the
> holomorphic readout by default. The exact commutation `[J_cs,H]=0` defeats
> that as a static proof because the complex structure is measure-neutral.

I re-verified `[J_cs, M] = 0` for `M = aI + bC + b̄C²` with symbolic `a, b_re,
b_im` (gate F5). It holds identically.

**T6 (exact, gates H1–H2).** Sector Hilbert-Schmidt norms on the Hermitian
circulant:

```
‖ a I ‖²_HS            = tr( (aI)† (aI) )                    = 3 a²
‖ bC + b̄C² ‖²_HS       = tr( (b̄C² + bC)(bC + b̄C²) )
                       = tr( 2|b|² I + b̄² C + b² C² )
                       = 6 |b|²
```

**T7 (exact, gates H3–H5).** Introduce the ONE integer the whole binary reduces
to: `ν` = number of equipartition slots carried by the doublet isotype (the
singlet carries 1). Equipartition:

```
‖aI‖²_HS / 1 = ‖bC + b̄C²‖²_HS / ν
        3 a² = 6 |b|² / ν
   |b|² / a² = ν / 2
```

so **`r = ν/2`** exactly. `ν = 1` (count-once, one slot per K-orbit) ⟹
`r = 1/2`. `ν = 2` (count-twice, one slot per channel atom) ⟹ `r = 1`.

**T8 (exact, gates H6–H8).** The per-slot weight is `w = 1/(1 + ν)`:
`ν = 1 ⟹ w = 1/2`; `ν = 2 ⟹ w = 1/3`. These are exactly the campaign's `w`
values, and eliminating `ν` gives the closed relation

```
w = 1/(1 + 2r)     equivalently     r = (1 - w)/(2w)
```

verified symbolically (gate H8), not checked only at the two endpoints.

**T9 (exact, gates H9–H13).** The Koide lever, rebuilt from the circulant
spectrum rather than cited. With `λ_k = a + 2|b| cos(δ + 2πk/3)`, `k = 0,1,2`:

```
Σ_k λ_k  = 3a + 2|b| Σ_k cos(δ + 2πk/3) = 3a + 0 = 3a
Σ_k λ_k² = 3a² + 4a|b| Σ_k cos(δ+2πk/3) + 4|b|² Σ_k cos²(δ+2πk/3)
         = 3a² + 0 + 4|b|² · (3/2)
         = 3a² + 6|b|²

Q = (Σ λ_k²)/(Σ λ_k)² = (3a² + 6|b|²)/(9a²) = (1 + 2r)/3
```

`r = 1/2 ⟹ Q = 2/3`; `r = 1 ⟹ Q = 1`.

**Chain summary.** T1→T4 exact and landed-consistent. T4→T5 does not close, for
a structural reason. T6→T9 exact, and they show the whole binary is the single
integer `ν ∈ {1, 2}`.

---

## 8. The task's premise itself is not carrier-forced (new, §B-3)

My task asks me to classify `K/CPT` as real or quaternionic. I did (T3: real).
But the classification is a property of the **supplied** `K`, not of the
carrier. Exact computation (gates Q1–Q8):

On the doublet block in the frame `(vw, vwb)`, the general antilinear map is

```
J( x·vw + y·vwb ) = μ ȳ · vw + ν x̄ · vwb ,      μ, ν ∈ C
```

**Q1 — every such `J` is `C_3`-equivariant, for all `(μ, ν)`.** The antilinearity
conjugates the character twist and it cancels:
`J(C v)` has `vw`-coefficient `μ · conj(ω̄ y) = μ ω ȳ`, and `C(J v)` has
`vw`-coefficient `ω · μ ȳ`. Equal identically. Likewise on `vwb`.

**Q2 — the square.**

```
J²( x vw + y vwb ) = (ν̄ μ) x · vw + (μ̄ ν) y · vwb
```

with `μ̄ν = conj(ν̄μ)`, so `J²` is a real scalar exactly when `ν̄μ ∈ R`.
Antiunitarity in the frame where `vw ⊥ vwb` with equal norms requires
`|μ| = |ν| = 1`, hence `ν̄μ` has modulus 1, hence `J² = ±1`.

**Q3 — `(μ, ν) = (1, 1)` gives `J² = +1`: a REAL structure.**
**Q4 — `(μ, ν) = (1, -1)` gives `J² = -1`: a QUATERNIONIC structure.**
**Q5 — both are antiunitary.**

**Q6 — and both commute with the entire K-real mass family.** On entrywise-real
triples `M` acts as `diag(λ_1, λ̄_1)` on `(vw, vwb)`; then

```
J(M v)  has vw-coeff  μ · conj(λ̄_1 y) = μ λ_1 ȳ
M(J v)  has vw-coeff  λ_1 · μ ȳ
```

identical, for every `(μ, ν)`. Same on `vwb`. **So the quaternionic
representative is just as compatible with the landed mass structure as the real
one.**

**Q7/Q8 — the space of equivariant antilinear maps is 2-complex-dimensional on
`ω ⊕ ω̄` and 0-dimensional on `ω`.**

**Interpretation, stated carefully.** This is *not* a claim that the framework's
`K` is quaternionic — it is not; `K² = +1` (gate E3, and landed
`KOIDE_KODIM...:38-39`). It is the observation that the real-vs-quaternionic
trichotomy is only rigid on **irreducibles**, and the doublet constituent `ω` is
the case where **no** antilinear map exists. Once you pass to the reducible
block `ω ⊕ ω̄` where `K` does live, rigidity is gone and both squares occur. So, **in my own words (this is not a
quotation from any note)**:

*Asking "is the K/CPT structure real or quaternionic?" of the charged-lepton
corner carrier is asking a question the carrier does not answer. It answers only
relative to a supplied `K`, and the supplied `K` is then measure-neutral anyway.*

**FLAG — uncertainty.** I have not checked whether the `J² = -1` representative
is compatible with *every* landed structure on the carrier (e.g. reflection
positivity, or the `KOIDE_REALITY_FAVORS_SIGNED_READOUT` orientation). I checked
`C_3`-equivariance, antiunitarity, and commutation with the K-real mass family.
A stronger constraint elsewhere could exclude it. This does not affect the main
verdict, which rests on the supplied real `K`.

---

## 9. Two independent demonstrations that the indicator cannot select

### 9.1 The invariant-form cone: FS is constant where `r` varies

The relative weight between the two isotypes is exactly what `r` measures
(T7). So the question is: does anything in the representation theory pin that
relative weight?

**Setup, rebuilt (gates G1–G7).** The Hermitian circulants have the real basis
`{ I, C + C², i(C - C²) }` with coordinates `(a, b_re, b_im)`. Conjugation by
`D_g = diag(1, ω, ω²)` satisfies `D_g C D_g^{-1} = ω C` (gate G1) — a genuine
order-3 symmetry of the carrier, acting on coordinates as `a` fixed, `b ↦ ω b`,
i.e. the block matrix

```
Rot = [ 1     0        0     ]
      [ 0   -1/2   -√3/2     ]
      [ 0    √3/2   -1/2     ]
```

**Solving `Rotᵀ G Rot = G` over all symmetric `G` (gate G3) gives**

```
G = diag(g_0, g_1, g_1),     g_0, g_1 > 0 free
```

a **two-parameter cone with the singlet:doublet ratio FREE** (gate G4). This
independently reproduces the landed
`docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md:29`,

> B_{alpha,beta}(A,B) = alpha Tr(AB) + beta tr(A) tr(B).

positive-definite on `alpha > 0`, `alpha + 3 beta > 0` (`:49-51`) — also a
two-parameter cone with free ratio, on the larger `Herm(3)` surface. Two
different surfaces, same free parameter.

**The two horns are two points of that one cone (gates G5–G7, H14–H16):**

```
equal-sector-energy locus of G = diag(g_0, g_1, g_1):
        g_0 a² = g_1 |b|²      ⟹      r = |b|²/a² = g_0 / g_1

Hilbert-Schmidt point   G_HS   = diag(3, 6, 6)   ⟹  r = 3/6 = 1/2   (count-once)
flat per-coordinate     G_flat = diag(1, 1, 1)   ⟹  r = 1/1 = 1     (count-twice)
```

Both `G_HS` and `G_flat` are verified to lie in the invariant cone (G6, G7).

**The no-go (gates L1–L3).** `FS` is computed from the *character* of the
representation. Rescaling an isotype by a positive scalar is an isomorphism of
representations; it changes no character value. Therefore

```
FS is CONSTANT — (+1, 0, 0) — at every point of the cone,
while r sweeps all of (0, ∞) across the same points.
```

Gate L2 exhibits `r ∈ {1/7, 1/2, 11/13, 1, 5/2}` at cone points where
`FS = (+1, 0, 0)` throughout. **A constant function cannot select a point of a
one-parameter family.** This is not "FS happens not to work here"; it is that
FS is an invariant of a structure that the answer does not depend on.

### 9.2 The CP-completion circularity, demonstrated

The KCPT lane records that adjoining the CP/conjugating element flips the census
(`KCPT_EXTENDED_GROUP_REALITY_CENSUS...:27`, quoted in §2.4):
`(0,0,0,0,+1)` over ranks `(4,4,6,6,12)` becomes `(+1,+1,+1,+1,+1,+1)` over
`(8,8,12,12,12,12)`. **Note the ranks: `4 → 8` and `6 → 12`. The `FS = +1` is
obtained on a block of DOUBLED complex dimension.**

Rebuilt natively at `C_3` scale (gates D1–D6, M4), so I am not citing it:

`S_3 = C_3 ⋊ ⟨σ⟩` with `σ : C ↦ C²` is the smallest linear model of "adjoin the
conjugating element". Its 2-dimensional irrep restricts to `ω ⊕ ω̄`. Character:
`χ(e) = 2`, `χ(3\text{-cycle}) = ω + ω² = -1`, `χ(\text{transposition}) = 0`.
Squares in `S_3`: `e² = e` (1 element), `(3\text{-cycle})² =` a 3-cycle
(2 elements), `(\text{transposition})² = e` (3 elements). So

```
FS_{S_3}(2-dim) = (1/6)[ 1·χ(e) + 2·χ(3-cycle) + 3·χ(e) ]
                = (1/6)[ 1·2   + 2·(-1)        + 3·2    ]
                = (1/6)[ 2 - 2 + 6 ]
                = 1
```

**`FS` flipped `0 → +1`, and the complex dimension went `1 → 2`.** Exactly the
KCPT pattern, at the smallest possible scale.

**The circularity, stated exactly.** "Real type" on the doublet is available
*only after* the conjugate partner has been adjoined to the object. The `FS = +1`
is therefore a **consequence** of having performed the doubling, and cannot be
used as evidence about whether the doubling is physical. Contrast gate D6: the
trivial character is `FS = +1` under both `C_3` and `S_3` with **no** dimension
change — so the doubling in the doublet case is not an artifact of changing the
group, it is the specific `FS = 0 → +1` mechanism.

This is the operator-side form of the landed warning at
`KOIDE_R_HALF_POLARIZATION_SELECTOR...:58-60` (§2.2): *"a category slip and is
**circular** (it assumes the asymmetric `(1,1)` split it claims to derive)"*. My
contribution is to show it is not merely a rhetorical risk but an identity:
adjoining the conjugator is the doubling.

---

## 10. Sub-findings and flagged uncertainties

**10.1 (FLAG — a possible defect in the campaign's own framing).** The campaign
states the binary "four equivalent ways", including "6 Grassmann generators per
triple copy" vs "12 generators". **In its landed realization, the 6→12 generator
doubling is `r`-NEUTRAL.** Verbatim,
`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:177-180`:

> 3. **r-neutral doubling.** `lam_0^2 * |lam_1|^4 = (lam_0 * |lam_1|^2)^2`
>    identically on entrywise-real triples: the singlet exponent and the
>    doublet exponent double together, and every doublet-to-singlet power
>    ratio is unchanged.

I verified this independently (gates K1–K5): `det W = λ_0 λ_1 λ_2 = λ_0 |λ_1|²`
on real triples, and the 12-generator value is `det W ² = λ_0² |λ_1|⁴`, whose
singlet:doublet exponent ratio `2:2` equals the 6-generator `1:1`. **The
whole-copy doubling is symmetric; the `r`-relevant doubling is asymmetric (the
singlet channel is `K`-FIXED, only the doublet is a 2-element `K`-orbit).**
Those are different operations. The landed note itself flags its translation as
declared, not derived (`:198-200`):

> The translation is declared, not derived: the `m` to generator-count
> correspondence is declared bookkeeping, never an equivalence claim, and the
> selection between the horns is not made here.

**Recommendation:** the campaign should not treat "6 vs 12 generators" as
interchangeable with "`w = 1/2` vs `w = 1/3`". As landed, they are not. If the
campaign's kill-check depends on that equivalence, it needs re-derivation. I
flag this rather than resolve it — it is outside my task and I may be missing a
step that reconciles them.

**10.2 (positive, small).** The entire binary compresses to a single integer
`ν ∈ {1, 2}` via `r = ν/2`, `w = 1/(1+ν)`, `Q = (1 + 2r)/3` (T7–T9, exact). This
is a cleaner statement of the campaign target than the four-way equivalence, and
it makes explicit that the target is an *integer-valued slot multiplicity*, not
a continuous parameter. Any closing theorem must produce that integer.

**10.3 (FLAG — stale status label on main).** See §2.5:
`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:72`
labels `koide_frobenius_isotype_split_uniqueness` `retained_no_go`; live ledger
says `unaudited`.

**10.4 (FLAG — scope).** I worked on the `C_3` corner surface, which is the
surface the Koide `r` question is posed on. I did **not** rebuild the KCPT
`L = 4, N = 64` lattice census (`|G_amb| = 768`, `|H| = 1536`); I read it and
quoted it. If the campaign later argues the physical carrier is the KCPT
`N = 64` object rather than the `C_3` triple, my §9.1 cone argument would have
to be redone there. I expect it to survive (the cone-freedom argument is
general), but **I have not checked it and am not claiming it**.

**10.5 (FLAG — odd real dimension, unresolved).** The full carrier `R^3` has
**odd** real dimension, so it admits no complex structure at all, and a CAR
algebra on 3 real Majorana modes has no integral complex-mode count. Landed
content addresses this head-on and says the odd direction is irrelevant —
`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:44-48`
(the quote begins mid-line 44):

> **That framing is wrong.** `det_C` only needs a complex structure on the
> **doublet**, which is **2-dimensional (even)** and **already carries** `J_cs`
> with no extra structure. The odd direction is the *singlet* (the `0`-eigenvector
> of `J_cs`), irrelevant to the doublet.

I record this because the campaign's stated attack is "build the CAR algebra of
the carrier and COUNT its Berezin modes". On `R^3` that count is not an integer;
on the declared 6-generator surface the carrier has already been complexified to
`C^3`, i.e. **the polarization was supplied when the Berezin surface was
declared**. That is the supervisor's Wave-0 predicted circularity appearing in
the campaign's own chosen machinery. I flag it; I have not proven that every
possible CAR construction inherits it.

---

## 11. What is NOT foreclosed (stated so the campaign does not over-read this)

I am reporting a negative on the **static / representation-theoretic** lane
only. The landed no-go scopes itself the same way, and I agree with its scope,
`KOIDE_R_HALF_POLARIZATION_SELECTOR...:89-99`:

> A genuine count-once needs either a SUSY superpotential (chiral protection,
> holomorphic by construction) — which the framework **lacks** (Seiberg) — or a
> **dynamical first-order / index** realization of the readout (not the second-order
> modulus). That is the only non-circular place `r=1/2` could live, and it is
> *currently leaning r=1*:

[lines 93–96 elided: they name the Kähler-Dirac note and its `det D = |det M|² → r=1`
finding. Resuming verbatim at `:96`]

> The decisive
> open sub-question (the AC_φλ staggered-Dirac corner realization): does the actual
> matter action deliver a *first-order* `det D` (Pfaffian/index, count-once) or the
> *second-order* modulus (`det D†D`, rank-2, count-twice)?

That matches the campaign's own stated open door ("a future physical CAR/action
theorem that derives a specific Gaussian measure"). **Derivation B's finding is
that the operator/reality side cannot supply it, and that any attempt to read
the count off a reality invariant is circular in the precise sense of §9.2.**
The remaining live question is whether the *action* is first-order or
second-order — which is Derivation A's territory, not mine.

---

## 12. Gate designs for the answer reached

The answer reached is a negative, so the gates gate the negative. Each carries a
wrong-value or counter-object rejector, and each is exact.

### Group A — the indicator (the claim)

| gate | discriminates | rejector |
|---|---|---|
| `G-FS-CARRIER` | `C^3 = I_3`, `C^T = C^2`, `C` real, rebuilt from the matrix, not asserted | `C² ≠ I` (order is exactly 3) |
| `G-FS-C3` | `FS(1, ω, ω̄) = (+1, 0, 0)` from `FS(χ)=|G|^{-1}Σχ(g²)` over the closed group | `FS(ω) ≠ +1`, `FS(ω) ≠ -1` |
| `G-FS-REG` | independent route: `FS(regular) = +1` **and** `= Σ_k FS(χ_k)` | `FS(reg) ≠ 0`, `≠ 3` |
| `G-FS-MUTATE` | the SAME routine returns `+1` on `Z_2`, `0` on `Z_4`, `-1` on `Q_8`, `+1` on `S_3` — all from multiplicative closure of explicit generators | routine must span `{+1, 0, -1}`; if it cannot return `-1`, FAIL |
| `G-ANTILIN-NULL` | the only `C_3`-equivariant antilinear map on `ω` is `0` (solve `ω̄t = ωt`) | a nonzero solution ⇒ FAIL |

### Group B — the real structure (the task's literal question)

| gate | discriminates | rejector |
|---|---|---|
| `G-K-REAL` | `K C K = C`, `K² = +1`; `K vw = vwb` | `K vw ≠ vw` (K does not preserve the constituent) |
| `G-J-INVOL` | `U² = I`, `U C U = C²`, `J = U∘conj` has `J² = +1` | `J² ≠ -1` — pins REAL, excludes quaternionic |
| `G-J-MASS` | `U conj(M) U = M` for symbolic `(a, b_re, b_im)` | must fail on a non-circulant `M` |
| `G-ANTILIN-BOTH` | on `ω ⊕ ω̄`, `(μ,ν)=(1,1)` gives `J²=+1` and `(μ,ν)=(1,-1)` gives `J²=-1`, **both** equivariant, antiunitary, and commuting with `diag(λ_1, λ̄_1)` | if `J²=-1` fails to commute with the mass family, the §8 claim FAILS |

### Group C — measure-neutrality (why the indicator cannot act)

| gate | discriminates | rejector |
|---|---|---|
| `G-JCS` | `J_cs = (C-C²)/√3` real, `J_cs² = -P_doublet`, `[J_cs, K] = 0` | `J_cs² ≠ -I_3` (it annihilates the singlet — a non-vacuity witness) |
| `G-JCS-NEUTRAL` | `[J_cs, M] = 0` for symbolic `(a, b_re, b_im)` | must FAIL for a non-circulant perturbation, else vacuous |

### Group D — the cone (the structural no-go)

| gate | discriminates | rejector |
|---|---|---|
| `G-CONE-DIM` | solving `Rotᵀ G Rot = G` over symmetric `G` yields exactly **2** free parameters, `G = diag(g_0, g_1, g_1)` | 1 free parameter ⇒ FAIL (ratio would be pinned); 6 ⇒ FAIL (`Rot` not acting) |
| `G-CONE-ROT` | `D_g C D_g^{-1} = ω C` and `Rot³ = I` — the symmetry is real, not assumed | `Rot² = I` ⇒ FAIL |
| `G-CONE-BOTH-IN` | `G_HS = diag(3,6,6)` and `G_flat = diag(1,1,1)` both satisfy the invariance | either failing ⇒ the horns are not both admissible ⇒ claim FAILS |
| `G-CONE-R` | `r = g_0/g_1` on the equal-sector locus; `r(3,6) = 1/2`; `r(1,1) = 1` | `r(3,6) ≠ 1` and `r(1,1) ≠ 1/2` (orientation not inverted) |
| `G-FS-CONSTANT` | `FS` is `(+1,0,0)` at ≥5 cone points where `r ∈ {1/7, 1/2, 11/13, 1, 5/2}` — **constant invariant, varying target** | if `FS` varies across cone points ⇒ the no-go FAILS and the route reopens |

### Group E — the CP-completion circularity

| gate | discriminates | rejector |
|---|---|---|
| `G-CP-FLIP` | `FS_{C_3}(ω) = 0` → `FS_{S_3}(2\text{-dim}) = +1`, with `dim_C: 1 → 2` | `FS_{S_3} ≠ 0`, `≠ -1` |
| `G-CP-CONTRAST` | the trivial character is `+1` under **both** groups with **no** dimension change | if the trivial also doubled, the flip would be a group artifact ⇒ FAIL |
| `G-CP-PIN` | source pin: the KCPT extended-census note contains the literal string `(0, 0, 0, 0, +1)` and the literal string `(+1, +1, +1, +1, +1, +1)` | absent ⇒ FAIL |

### Group F — the translation arithmetic

| gate | discriminates | rejector |
|---|---|---|
| `G-HS-NORMS` | `‖aI‖²_HS = 3a²`, `‖bC+b̄C²‖²_HS = 6\|b\|²`, symbolic | wrong coefficient ⇒ FAIL |
| `G-NU-R` | `r = ν/2` symbolically in `ν`, not only at `ν ∈ {1,2}` | `r(1) ≠ 1`, `r(2) ≠ 1/2` (orientation) |
| `G-W-R` | `w = 1/(1+ν)` and `w = 1/(1+2r)` as a symbolic identity | endpoint-only checking ⇒ insufficient |
| `G-Q-LEVER` | `Σλ_k = 3a`, `Σλ_k² = 3a² + 6\|b\|²`, `Q = (1+2r)/3` rebuilt from `λ_k = a + 2\|b\|cos(δ + 2πk/3)`, `δ` symbolic | `Q` must be independent of `δ`; `δ`-dependence ⇒ FAIL |
| `G-BEREZIN-NEUTRAL` | `det W ² = λ_0² \|λ_1\|⁴` and exponent ratio `2:2 = 1:1` — the whole-copy doubling is `r`-neutral | no constant `κ` with `κ·det W = det W ²`: forced values `1` at `(1,0,0)` and `8` at `(2,0,0)` |

**Sympy hygiene note (repo lesson).** `sympy` `==` is structural and
`Float ≠ Rational`. Every comparison above must be built from `sp.Integer` /
`sp.Rational` and compared via `sp.simplify(lhs - rhs) == 0`, never via Python
`/` on ints. One of my gates initially failed for exactly this reason
(`(1 + 2*1)/3` produced a `Float`); it is recorded here so a real runner does
not repeat it.

**Total exact gates run in this report: 95 (71 + 16 + 8), all PASS.**

---

## 13. One-paragraph handoff to the supervisor

The Frobenius-Schur indicator of the charged-lepton corner carrier's doublet is
`0` — complex type — which is landed since 2026-06-07, which I rebuilt exactly,
and which is the one value of the trichotomy that *reports* the count-once /
count-twice binary rather than resolving it. The `K/CPT` structure is a genuine
real structure (`J² = +1`, not quaternionic), also landed, also rebuilt, and
also explicitly recorded as `r`-silent. My route appears verbatim as `RULED OUT
BY PRIOR` in a landed no-go's route table. The one thing I can add beyond the
landed record is a structural reason rather than a case list: the FS indicator
is constant on the entire two-parameter invariant-form cone, while `r` sweeps
`(0, ∞)` across that same cone — so no reality-type invariant can ever select
the count — and the apparent counter-evidence (`FS = 0 → +1` under
CP-completion) is produced *by* the doubling, at doubled dimension, so using it
is an identity, not an argument. **Derivation B returns a sharp negative and
should not be continued.** If Derivation A independently reaches count-once from
the action side, B does not contradict it; B says only that the reality
structure cannot be A's reason. If A also fails, the honest campaign output is
that the binary is a supplied polarization, and §10.5 argues the campaign's own
Berezin machinery supplies it at declaration time.
