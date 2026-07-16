# Observable-Principle P1 Bridge — Symmetry-Type / Energy-Readout Narrow Note

**Date:** 2026-06-02
**Claim type:** no_go
**Type:** no_go
**Claim scope:** narrow no_go that tests the **symmetry-type readout reframe**
as a candidate instance of the open forward path **(a′)** recorded in
`OBSERVABLE_PRINCIPLE_P1_EXPONENT_SELECTOR_DICHOTOMY_NARROW_NOTE_2026-06-02.md`
(#2504): a "genuinely new owner-approved premise introducing a separate physical
**structure**, **outside** the sector-composition selector class `𝒞`." The
reframe proposes that the v-chain's **additive** readout `W = log|det(D+J)|` is
**forced** (a representation-theory theorem, not a selection) by the fact that
the VEV `v` is an **energy** — i.e. an eigenvalue of a generator of a
**continuous** (time-translation) symmetry, which is additive over a tensor
product `H = H_A ⊗ I + I ⊗ H_B` — while **multiplicative** readouts
(parity/`C`/`G`/`Z_n`, the framework's `Z_3` characters for Koide/color/
generation) are characters of **discrete** symmetries, multiplicative on tensor
products. The finding is that the **symmetry-type law is a correct theorem**,
but the **energy route to the v-chain additive readout does NOT escape `𝒞`**:
it lands in **face ADD = P1** (and its intensive/Born variant in **face
BLIND**), or it relocates the **same** multiplicative→additive (exp/log)
dichotomy **one level up** (to the dynamics' generator). It pins, but does not
retire, the admitted P1 premise of
[`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md).

> **Statement (the energy route is P1-equivalent).** Read the v-chain scalar
> as an **energy-sector** quantity. Two pivots carry the reframe:
>
> - **Pivot 1 — "energies/the Hamiltonian are additive over the tensor
>   product."** This is true for the **non-interacting / tensor-factorized**
>   class (`U_{AB} = U_A ⊗ U_B ⟹ H = H_A ⊗ I + I ⊗ H_B`, eigenvalues add;
>   §3.2, runner T2). But (i) it is **not supplied by the Qubit axiom** — the
>   Lattice/Qubit/Admissibility/Record baseline fixes the lattice, local algebra, and finite
>   scalar record readout, not dynamics (`MINIMAL_AXIOMS_2026-06-29.md`);
>   and (ii) in the framework's **realized** free quadratic sector the
>   Hamiltonian is itself **defined** as `Ĥ = −log(T̂²)/(2a_τ)` with `T̂²`
>   a **product** over modes (`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`):
>   "`H` additive" `⟺` "`T̂²` multiplicative" is the **same exp/log move**, one
>   level up. The whole family `{(T̂²)^s}` is a **single `{r ↦ r^s}` orbit**
>   and the additive generator is the `s → 0` (`log`) member (§3.3, runner
>   T5). So Pivot 1 sits in **face ADD** of #2504's dichotomy applied at the
>   transfer-operator level — it does **not** supply an additive readout
>   **prior to** a `log` choice.
> - **Pivot 2 — "the v-chain scalar `W` IS the free energy / an energy-sector
>   quantity."** This identification is exactly content **(II.b)** of the
>   structural-reframing no-go
>   (`OBSERVABLE_PRINCIPLE_P1_BRIDGE_STRUCTURAL_REFRAMING_NARROW_NOTE_2026-05-21.md`),
>   already proven **(II.b) `⇔` P1**. And the framework's free-energy density is
>   **defined** via the per-matrix-entry log-det convention
>   `Δf := (1/n)(ln|det(D+m)| − ln|det D|)`
>   (`HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_2026-05-16.md`,
>   which **explicitly disclaims** any physical free-energy identification
>   beyond that log-det convention): it **presupposes** `log|det|`, it does not
>   derive it (§3.4, runner T7).
>
> Therefore the energy route reaches the additive readout **only through** the
> additivity content P1 already names — at the partition-function level
> (Pivot 2 = (II.b) = P1) or at the generator level (Pivot 1 = the same exp/log
> one level up, face ADD). The intensive/Born (per-site) energy density is the
> **face-BLIND** instance and singles **nothing** (§3.5, runner T8). The
> symmetry-type law itself — additive generators on tensor products have
> additive eigenvalues; discrete-group elements have multiplicative characters;
> `exp`/`log` is the algebra↔group bridge — is a **theorem** (runner T2/T3/T4),
> reproven from elementary tensor algebra and cited framework context; it is
> **not** the disputed step.

**Result.** The symmetry-type readout reframe is a **correct
representation-theory theorem** about *which* ledger an observable uses, but
the energy route to the v-chain **additive** readout is **P1-equivalent**
(diagnosis: it reduces to P1): it does **not** instantiate #2504's
out-of-class path (a′), because "energies add" and "`W = log Z` is additive"
are the **same** multiplicative→additive (`exp`/`log`) content read at two
levels, and the identification "`W` is the free energy" is the admitted
classification step (II.b). This **confirms and extends** #2456/#2504: the most
natural path-(a′) candidate (the energy ledger) collapses into the dichotomy.
This note does NOT close P1; it pins the energy route as P1-equivalent.

**Status boundary:** independent post-landing review only. This source note does not
set or predict a review outcome; later status is generated by the audit
pipeline after independent review. The `no_go` label is a source-side
claim-boundary declaration, not an audit verdict.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent post-landing
process.
**Primary runner:**
[`scripts/audit_companion_observable_principle_p1_symmetry_type_energy_readout_2026_06_02.py`](../scripts/audit_companion_observable_principle_p1_symmetry_type_energy_readout_2026_06_02.py)

## 0. Honest framing up front

#2504
(`OBSERVABLE_PRINCIPLE_P1_EXPONENT_SELECTOR_DICHOTOMY_NARROW_NOTE_2026-06-02.md`)
proved that **within the sector-composition selector class `𝒞`** every
exponent-fixing selector is either **BLIND** (orbit-invariant under `{r ↦ r^p}`,
singles nothing) or **ADD** (references the bare generator value = additivity =
P1, unique `log` by Cauchy/Shannon-Khinchin). It **left open** exactly one
forward path: **(a′)** a genuinely new owner-approved premise that lives **outside**
`𝒞` — one that "legitimately introduces a privileged scale by a separate
physical mechanism (not by importing `r^{p₀}` into a selector statement)."

**This note tests the single most natural candidate for (a′): the energy
ledger.** The reframe is attractive and physically correct *as a classification
of observables*: physics carries **two** readouts, and an observable's readout
is fixed by its **symmetry type** —

- **ADDITIVE** quantum numbers (charge, baryon/lepton number, energy/mass) are
  **eigenvalues of generators of continuous symmetries** (Lie **algebra**; on a
  tensor product the generator is the **direct sum** `H = H_A ⊗ I + I ⊗ H_B`,
  so eigenvalues **add**);
- **MULTIPLICATIVE** quantum numbers (parity, `C`, `G`, `R`-parity, `Z_n`) are
  **characters of discrete symmetries** (group element; on a tensor product it
  acts multiplicatively, so characters **multiply**);
- the bridge is the **same** `exp`/`log` relating `group = exp(algebra)` and
  `Z = exp(log Z)`.

The framework already uses **both** ledgers (§1): `log|det|` for the
additive action/free-energy v-chain; `Z_3` characters for the discrete
Koide/color/generation labels. The reframe's claim is that this makes the
v-chain additive readout a **theorem** (the VEV is an energy ⟹ additive),
not a P1 selection — i.e. an out-of-class structural input.

**The honest finding is that the symmetry-type *law* is a theorem, but the
*energy route to the v-chain additive readout* is P1-equivalent.** The reason
is the two pivots above: at the partition-function level the identification "the
v-chain scalar is the free energy" is content (II.b), already proven `⇔` P1;
and at the generator level "energies add" is established **via** `H = −log(T̂²)`
with `T̂²` multiplicative, which is the **same** `exp`/`log` move one level up —
the additive ledger's coordinate **is** `log`, by the very `exp`/`log`
universality, not independently of it. The energy route therefore does **not**
introduce a privileged scale by a mechanism outside `𝒞`; it re-enters `𝒞` at
face ADD.

**The honest boundary.** This is a reduces-to-P1 outcome with
**positive content**: it closes the energy-ledger candidate for path (a′) and
explains *why* (the dynamics' additive generator is the same exp/log object as
the additive partition-function readout). It does **not** claim that *every*
conceivable out-of-class owner-approved premise is foreclosed — #2504's (a′) remains open
for premises that introduce a privileged scale by a mechanism that is **not**
the energy/free-energy ledger and **not** a sector-composition selector.

This note explicitly DOES NOT:

- claim P1 is false; `W = log|det(D+J)|` remains the natural physical choice,
  and the symmetry-type classification of additive-vs-multiplicative readouts is
  correct;
- claim the symmetry-type law is wrong or circular — it is a reproven theorem
  (runner T2/T3/T4); only the *energy route to the additive readout* is found
  P1-equivalent;
- claim #2504's path (a′) is fully foreclosed — only the **energy/free-energy
  ledger** instance of it is closed here;
- promote or alter the status of
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, #2456, #2504, the `det`-character
  note, the FORM-premise integrity note, the two-stage synthesis, the Route D
  consolidated no-go, the structural-reframing no-go, the six existing no-go
  rows, the Matsubara free-energy / transfer-matrix rows, the staggered-Dirac
  realization gate, or any upstream row;
- add a new framework axiom or repo-wide vocabulary tag or class name.
  "Additive ledger," "multiplicative ledger," "energy route," "Pivot 1/2,"
  "symmetry-type" are local descriptive labels; "(BLIND)," "(ADD)," "face,"
  "orbit," "(II.a)," "(II.b)" are mapped to the existing #2504 / #2456 /
  structural-reframing vocabulary, not new repo tags.

## 1. Mandatory four exercises

### Exercise 1 — Assumption audit

Each premise consumed, with type and ledger status:

| Premise | Type | Status / source |
|---|---|---|
| For `U_{AB} = U_A ⊗ U_B`, the generator is `H = H_A ⊗ I + I ⊗ H_B` and `spec(H) = { e_a + e_b }` | elementary tensor / Lie-algebra | reproven runner T2 (small matrices); Wigner additive-quantum-number comparator |
| A discrete-group element on a tensor product `g_A ⊗ g_B` has character `χ(g_A)·χ(g_B)` (`= tr ⊗ tr`) | elementary representation theory | reproven runner T3 (`Z_3` regular rep + generic `2×2`); Wigner multiplicative-quantum-number comparator |
| `exp`/`log` is the algebra↔group bridge and the `Z = exp(log Z)` bridge — the same `(ℝ_+,×) → (ℝ,+)` homomorphism | elementary | reproven runner T4 |
| `Ĥ = −log(T̂²)/(2a_τ)`, `T̂² = ⊗_p diag(1, e^{−2E(p)})`, `Ĥ = Σ_p E(p) n_p` (free quadratic sector) | finite second-quantization functor | `AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`; reproven runner T5 |
| `det(D_A ⊕ D_B + J) = Z_A·Z_B`; `r(A ⊕ B) = r(A)·r(B)` on the real-`D` sector | standard linear algebra | non-derivation import (elementary; runner T4/T7) |
| `Z[J] = det(D+J)` on a finite block as the source-deformed amplitude | finite determinant context | imported as in the parent note; same Berezin/Grassmann origin (staggered-Dirac realization gate) |
| `Δf := (1/n)(ln|det(D+m)| − ln|det D|)` is the framework's free-energy density (per-matrix-entry log-det convention) | density-normalization convention | `HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_2026-05-16.md` (explicitly disclaims physical free-energy identification beyond log-det); reproven runner T7 |
| (II.b) `W = log|Z|` identification `⇔` P1 | reproven equivalence | `OBSERVABLE_PRINCIPLE_P1_BRIDGE_STRUCTURAL_REFRAMING_NARROW_NOTE_2026-05-21.md`; reproven runner T7 |
| Lattice + Qubit + Admissibility + Record baseline; **no dynamics** | framework baseline | `MINIMAL_AXIOMS_2026-06-29.md` |
| Additive + measurable on `(ℝ_+,×)` `⇒ c·log` (Cauchy/Shannon-Khinchin) | functional-equation classification | reproven in #2504 runner T7 / structural-reframing note; literature comparator only |

**Decisive observations.**

1. The symmetry-type **law** (additive generators → additive eigenvalues;
   discrete-group elements → multiplicative characters; `exp`/`log` bridge) is a
   **theorem**, reproven here. It is **not** the disputed step and is **not**
   re-attempted as a wall.
2. The disputed step is the **identification of the v-chain scalar with the
   energy/free-energy ledger**. That identification is content (II.b) of the
   structural-reframing no-go — proven `⇔` P1 — at the partition-function level.
3. The one route that could make the energy ledger an **independent** structural
   input is **Pivot 1** ("the generator `H` is additive, prior to and
   independent of any `log` choice"). The decisive finding is that in this
   framework `H` is **built from** `−log(T̂²)` with `T̂²` multiplicative; the
   additive `H` is the **`log` member** of the `{(T̂²)^s}` orbit, **not** prior
   to it. So Pivot 1 is **face ADD** one level up, not an out-of-class input.

**Conclusion of Exercise 1.** The route consumes, beyond standard math and the
framework baseline, exactly the **identification of the v-chain scalar with the
energy/free-energy ledger** — which is (II.b) = P1 — and the claim that the
additive generator is a prior structure — which is the same exp/log move one
level up. No premise outside `𝒞` is introduced; the admitted-premise count of
the parent note is not reduced.

### Exercise 2 — Elon Musk first-principles

Strip to first principles. The reframe says: an additive readout is **forced**
when the quantity is an **energy** (continuous-symmetry eigenvalue), because the
generator of a tensor product of independent evolutions is the **direct sum**,
whose eigenvalues **add**. That part is **true and is a theorem** (runner T2):
if the dynamics factorizes, `U_{AB} = U_A ⊗ U_B`, then `H = H_A ⊗ I + I ⊗ H_B`
and `e_{ab} = e_a + e_b`. The crux is whether this **forces** the v-chain
additive readout **without** re-importing P1.

It does not, for two first-principles reasons.

- **The "energies add" fact lives at the SAME exp/log layer.** The Lattice/Qubit/Admissibility/Record baseline commits
  **no** dynamics; the Hamiltonian enters only through a derivation lane. In the
  framework's realized free quadratic sector that lane **constructs** `Ĥ` as
  `Ĥ = −log(T̂²)/(2a_τ)` with `T̂² = ⊗_p diag(1, e^{−2E(p)})` (runner T5). So
  "`Ĥ` is additive (`Σ_p E(p) n_p`)" is **identical** to "`T̂²` is
  multiplicative over the tensor product," via the **same** `exp`/`log` map that
  takes `Z = exp(log Z)`. The additive coordinate `−log((T̂²)^s)/(2s) = Ĥ` is
  the **`log` member** of the one-parameter orbit `{(T̂²)^s}` (runner T5) —
  exactly face ADD of #2504's dichotomy, applied to the transfer operator
  instead of the partition function. "Energies add" is **not** a structure
  prior to `log`; it **is** `log`.
- **Additivity of `H` is the INDEPENDENT (non-interacting) class, which is
  P1's own hypothesis.** Energy is not additive in general: for interacting
  subsystems `H_int = H_A ⊗ I + I ⊗ H_B + g·(X_A ⊗ X_B)` the spectrum does
  **not** add (runner T6). "The VEV is an energy" forces additivity **only**
  when the subsystems are independent (tensor-factorized dynamics) — which is
  precisely **P1's "independent subsystems"** clause. The energy route therefore
  **imports** P1's independence hypothesis; it does not replace it.

What is left that could be an **out-of-class** input? Only the bare assertion
"the v-chain scalar **is** the free energy." But the framework's free energy is
**defined** by the log-det convention `Δf := (1/n)(ln|det(D+m)| − ln|det D|)`
(runner T7), so the assertion **presupposes** `log|det|`; and the
identification "`W` is the canonical free-energy/cumulant generator" is content
(II.b), proven `⇔` P1. There is **no third leg** of the energy route that lives
outside `𝒞`.

**First-principles bottom line.** The symmetry-type law is a theorem; the
energy route to the v-chain additive readout reduces to (i) the same exp/log
move one level up (Pivot 1 = face ADD at the transfer operator) and (ii) the
(II.b) free-energy identification (= P1) at the partition function. Both are
P1-equivalent. The energy ledger is **not** an out-of-class path-(a′) input.

### Exercise 3 — Literature search

External authorities directly relevant:

1. **E. P. Wigner (1931/1959).** *Group Theory and Its Application to the
   Quantum Mechanics of Atomic Spectra*, Ch. 11–12, 26. The
   **additive-vs-multiplicative** quantum-number dichotomy: additive numbers
   from generators of continuous symmetries (energy, charge, angular-momentum
   `z`-component), multiplicative numbers (parity, signature) from discrete-group
   elements. **Comparator** for the symmetry-type law: it **classifies which
   ledger** a quantum number uses; it does **not** derive that the framework's
   `W` is the energy ledger rather than a multiplicative one.
2. **J. E. Marsden & T. S. Ratiu (1999).** *Introduction to Mechanics and
   Symmetry*, §9 (momentum maps); **B. C. Hall (2015).** *Lie Groups, Lie
   Algebras, and Representations*, GTM 222, §3 (`exp`), §2.5. `group =
   exp(algebra)`; additive Lie-algebra generators exponentiate to multiplicative
   group elements. **Comparator** for the `exp`/`log` bridge (runner T4): the
   bridge is standard; it is the **same** map as `Z = exp(log Z)`. It does not
   single out which observable is additive.
3. **A.-L. Cauchy (1821).** *Cours d'Analyse*, §V; **J. Aczél (1966).**
   *Lectures on Functional Equations*, §2.1 Thm 1; **C. E. Shannon (1948),**
   §6; **A. I. Khinchin (1957),** Thm 1. Additive + regular on `(ℝ_+,×)`
   `⇒ c·log`. **Comparator** for face ADD: additivity is the **hypothesis**,
   `log` is the **output**; it does not derive additivity (the circularity
   flag).
4. **R. P. Feynman & A. R. Hibbs (1965).** *Quantum Mechanics and Path
   Integrals*, §10; **J. I. Kapusta & C. Gale (2006).** *Finite-Temperature
   Field Theory*, §2. The Euclidean partition function `Z = Tr e^{−βH}`
   factorizes over a tensor product **because `H` is additive**, and `F = −T log
   Z` is the additive thermodynamic potential. **Comparator** for Pivot 2: the
   free energy's additivity is **inherited from `H`'s additivity** through the
   **same** `log` — exactly the relocation this note formalizes. The literature
   **admits** `H`-additivity (the cluster/extensivity property); it does not
   derive it from a non-additive structure.
5. **R. Haag (1992).** *Local Quantum Physics*, §II–III; **S. Weinberg
   (1995).** *QFT I*, §4.4. Cluster decomposition / additivity of the energy
   over independent regions is an **axiom / classification criterion**, never
   derived from a more primitive non-additive structure. **Comparator** for
   Pivot 1: the additive-`H` / cluster property is uniformly **admitted**.
6. **O. Bratteli & D. W. Robinson (1981).** *Operator Algebras and Quantum
   Statistical Mechanics II*, §5.3 (finite-system KMS ⇔ Gibbs); **M. Reed &
   B. Simon (1975).** *Methods of Modern Mathematical Physics II*, §X (`H` as a
   self-adjoint generator). **Comparator** for the transfer-matrix realization:
   `H = −log T` / `T = e^{−τH}` is the standard transfer-operator ↔ Hamiltonian
   bridge — the **same** `exp`/`log`, supporting Pivot 1's relocation.

**Literature observation.** Wigner classifies *which* ledger an observable uses
but does not select the ledger for `W`; the Lie-theory sources give the
`exp`/`log` bridge as the **same** map as `Z = exp(log Z)`; the
finite-temperature and algebraic-QFT sources uniformly **admit** `H`-additivity
/ cluster decomposition and **inherit** free-energy additivity from it through
`log`. No source derives the additive readout for `W` from a non-additive
structure outside the additivity hypothesis. This matches the runner's reproven
finding: the symmetry-type law is a theorem; the energy route to `W`'s additive
readout is P1-equivalent.

### Exercise 4 — Math search (Tao-style)

**Pose the bare math problem.** Two readouts on a tensor-product / direct-sum
substrate: (A) eigenvalues of `H = H_A ⊗ I + I ⊗ H_B` (additive); (M) characters
of `g_A ⊗ g_B` (multiplicative). (i) Prove the two readout laws. (ii) Prove the
`exp`/`log` bridge is the same map as `Z = exp(log Z)`. (iii) Decide whether
declaring the v-chain scalar an **energy** forces its additive readout **without**
the additivity hypothesis, given that the framework realizes `H = −log(T̂²)` and
defines its free energy by the log-det convention.

**Math answer.**

- (i) `spec(H_A ⊗ I + I ⊗ H_B) = { e_a + e_b }` (runner T2);
  `χ(g_A ⊗ g_B) = tr(g_A ⊗ g_B) = (tr g_A)(tr g_B) = χ(g_A)χ(g_B)` (runner T3).
  Both are elementary tensor identities. **Theorem.**
- (ii) `exp(H_A ⊗ I + I ⊗ H_B) = exp(H_A) ⊗ exp(H_B)` on commuting summands
  (runner T4); and on block-diagonal `D`, `Z = Z_A·Z_B`, `log Z = log Z_A +
  log Z_B` (runner T4). The same `(ℝ_+,×) → (ℝ,+)` homomorphism. **Theorem.**
- (iii) **No.** Declaring `W` an energy forces additivity only **(a)** in the
  **independent** class (interacting `H` does not add, runner T6 — and that
  class is P1's own hypothesis), and **(b)** through the additive generator,
  which the framework **builds** as `Ĥ = −log(T̂²)/(2a_τ)` with `{(T̂²)^s}` a
  single `{r ↦ r^s}` orbit whose additive member is `log` (runner T5). So the
  additive readout is the **`log` member of the orbit** — face ADD — not a prior
  structure. The remaining leg, "`W` **is** the free energy," is defined by the
  log-det convention (runner T7) and is content (II.b) `⇔` P1. **P1-equivalent.**

**Math danger flag (per discipline).** "Energies add over the tensor product"
and "`W = log Z` is additive" are the **same** multiplicative→additive content
read at two levels (generator/group vs partition-function/free-energy). Using
either to "derive `log`" is **circular**: additivity is the hypothesis at both
levels. This note does **not** use it to derive `log`; it uses the two-level
identity to **prove the energy route is P1-equivalent** — the energy ledger's
additive coordinate **is** `log`, by the exp/log universality. The circularity
is flagged explicitly.

**Conclusion of math search.** The symmetry-type law is a theorem; the energy
route to the v-chain additive readout lands in face ADD (= P1) or relocates the
same exp/log dichotomy one level up. No out-of-class path-(a′) input is supplied
by the energy ledger.

## 2. The two ledgers and the precise question

The reframe's **structure** is correct and worth stating cleanly. An
observable's readout is fixed by its symmetry type:

| Ledger | Symmetry type | Object | Tensor-product law | Framework instance |
|---|---|---|---|---|
| **Additive** | continuous (Lie **algebra**) | generator `H` (eigenvalue) | `H = H_A ⊗ I + I ⊗ H_B` ⟹ `e_a + e_b` | `W = log|det(D+J)|` (action / free energy / v-chain) |
| **Multiplicative** | discrete (Lie **group** element) | character `χ` | `χ(g_A ⊗ g_B) = χ(g_A)χ(g_B)` | `Z_3` characters (Koide / color / generation) |
| **Bridge** | `group = exp(algebra)` | `exp`/`log` | same `(ℝ_+,×) ↔ (ℝ,+)` | same as `Z = exp(log Z)` |

**The precise question this note decides.** Is "the v-chain scalar `W` is
additive" **forced** — as an out-of-class structural input per #2504's (a′) — by
"the VEV is an **energy** (a continuous-symmetry eigenvalue), additive by the
tensor structure **prior to** any readout choice"? Or does the route re-import
P1's additivity?

The answer hinges on **where the additivity enters**. The symmetry-type law is a
theorem (it fixes *which ledger* a given symmetry uses). But to apply it to `W`,
the reframe must (Pivot 2) **identify** `W` with the energy/free-energy ledger,
and (Pivot 1) treat the energy ledger's additivity as a structure **prior to**
the `log` readout. §3 shows both legs are P1-equivalent.

## 3. Load-bearing steps

### 3.1 The symmetry-type law is a theorem (runner T2/T3/T4)

- **Additive (a):** for a tensor-product Hilbert space and **independent**
  evolution `U_{AB} = U_A ⊗ U_B`, the generator is `H = H_A ⊗ I + I ⊗ H_B`,
  whose eigenvalues are `e_a + e_b` (reproven on small explicit matrices,
  including the non-degenerate numeric instance `{1,5} ⊕ {2,11} → {3,7,12,16}`;
  runner T2). This is the Lie-**algebra** / continuous-symmetry / additive
  quantum-number side (Wigner comparator).
- **Multiplicative (b):** a discrete-group element acting as `g_A ⊗ g_B` has
  multiplicative character `χ(g_A ⊗ g_B) = χ(g_A)·χ(g_B)` (reproven on the
  `Z_3` regular representation — character vector `(3,0,0)` — and on a generic
  `2×2 ⊗ 2×2` via `tr(M ⊗ N) = tr M·tr N`; runner T3). This is the Lie-**group**
  / discrete-symmetry / multiplicative quantum-number side (the `Z_3` used by
  Koide/color).
- **Bridge (c):** `exp(H_A ⊗ I + I ⊗ H_B) = exp(H_A) ⊗ exp(H_B)` (algebra →
  group), and `Z = det(D_A ⊕ D_B) = Z_A·Z_B`, `log Z = log Z_A + log Z_B`
  (partition-function → free-energy). The same `(ℝ_+,×) → (ℝ,+)` homomorphism
  `t ↦ exp(t)` and its inverse `log` (runner T4).

**This law is not in dispute.** It is reproven from elementary tensor algebra
and cited framework context. The dispute is
only whether applying it to `W` is forced or selected.

### 3.2 Pivot 1 — "energies add" is the exp/log move one level up (runner T5)

The Lattice/Qubit/Admissibility/Record baseline commits **no dynamics**
(`MINIMAL_AXIOMS_2026-06-29.md`; dynamics enter only through their named
derivation lanes). In the framework's realized free quadratic sector
(`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`), the
Hamiltonian is **constructed** as

```text
   T̂² = ⊗_p diag(1, e^{−2 E(p)}),      Ĥ = −log(T̂²)/(2 a_τ) = Σ_p E(p) n_p.
```

So "`Ĥ` is additive" is **identical** to "`T̂²` is multiplicative over the
tensor product," via the **same** `exp`/`log` map (runner T5: `Ĥ = −log(T̂²)/2 =
E_1 n_1 + E_2 n_2` exactly). Moreover the **whole family** `{(T̂²)^s}` is
multiplicative over modes for every `s` (`(T̂²)^s = ⊗_p diag(1, e^{−2sE(p)})`,
runner T5) — a **single `{r ↦ r^s}` orbit** — and the additive generator is the
`s → 0` (`log`) member: `−log((T̂²)^s)/(2s) = Ĥ` for every `s` (runner T5). Thus
"`Ĥ` additive" sits in **face ADD** of #2504's dichotomy, applied at the
**transfer-operator** level. It does **not** supply an additive readout **prior
to** a `log` choice; the additive coordinate **is** the `log` member of the
orbit.

**Steelman (runner T6).** Additivity of `H` is **not generic**. For an
interacting `H_int = H_A ⊗ I + I ⊗ H_B + g(X_A ⊗ X_B)` with `g ≠ 0` the
spectrum does **not** add (its characteristic polynomial carries `g`; the
numeric `g = 1` spectrum `≠ {−2,0,0,2}`). "The VEV is an energy" forces
additivity **only** in the independent / tensor-factorized class — which is
exactly P1's "independent subsystems" clause. The energy route **imports** that
clause; it does not replace it.

### 3.3 Pivot 2 — "`W` is the free energy" is content (II.b) `⇔` P1 (runner T7)

The framework's free-energy density is **defined** by the per-matrix-entry
log-det convention

```text
   Δf(L_t, m) := (1/n_matrix)·(ln|det(D + m)| − ln|det D|)
```

(`HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_2026-05-16.md`,
which **explicitly disclaims** "a physical electroweak free-energy or
effective-potential identification beyond the per-matrix-entry log-det
convention"). The Matsubara density `ln(1 + m²/c)` is reproduced **from**
`ln|det|` (runner T7: `ln(m² + c) − ln(c) = ln(1 + m²/c)`). So "`W` is the free
energy" **presupposes** `log|det|`; it does not derive the additive readout from
a prior additive-`H` object.

And the identification "the framework's physical scalar generator **is** the
canonical free-energy / cumulant generator" is content **(II.b)** of the
structural-reframing no-go, already proven **(II.b) `⇔` P1**: if `W = log|Z|`
then `W` is additive on block-diagonal `D` (runner T7); and additivity (with the
multiplicative input `r = |det| > 0`) forces `W = c·log|Z|` by the Cauchy
classifier, while every `F_p` (`p ≠ 0`) fails additivity (runner T7). The
identification **is** the admitted classification step.

### 3.4 Synthesis — the energy route lands in face ADD (runner T8)

Combining §3.2–§3.3: the energy route reaches the additive readout **only**
through additivity content P1 already names.

- **Face ADD (the energy ledger).** The selector "read the additive (energy)
  quantum number" references the **bare** additive value `Φ(r) = log r` in the
  composite law `Φ(r_A r_B) = Φ(r_A) + Φ(r_B)` (runner T8). That is bare
  additivity = **(Add) = P1** (#2504 §3.3).
- **Face BLIND (the intensive / Born variant).** The **intensive** (per-site,
  normalized) energy density is orbit-invariant — `−log((T̂²)^s)/(2s) = E` for
  **every** `s` (runner T8) — so it returns the same object for every exponent
  and **singles nothing** (the #2504/#2456 Born/normalized-gradient result, here
  at the energy level).

There is **no third energy readout** that fixes a finite nonzero exponent
without referencing the bare additive value. The energy route therefore
**collapses into #2504's dichotomy** `{face ADD = P1, face BLIND = nothing}`,
relocated to the energy ledger. It is **not** an out-of-class path-(a′) input.

### 3.5 Why this is not a derivation of `log` (circularity flag)

The two-level identity — "energies add" (generator level) `≡` "`W = log Z` is
additive" (partition-function level), both via the same `exp`/`log` — is exactly
what makes the energy route **look** like an independent derivation and is
exactly **why it is not**. Additivity is the **hypothesis** at both levels; the
`exp`/`log` universality (Cauchy/Shannon-Khinchin) then forces `log`. Using the
energy ledger to "derive" the additive readout would be circular. This note uses
it only to **prove the energy route is P1-equivalent**.

## 4. What this closes / what remains admitted

### 4.1 What this closes (positive content despite negative outcome)

- **Closes the energy/free-energy-ledger instance of #2504's path (a′).** The
  single most natural candidate for an out-of-class structural input — "the
  v-chain scalar is an energy, hence additive by the tensor structure" — is
  shown to land in **face ADD** (= P1) or to relocate the **same** `exp`/`log`
  dichotomy one level up. The energy ledger is **not** outside `𝒞`.
- **Explains *why* the energy route is circular.** The dynamics' additive
  generator `Ĥ = −log(T̂²)` is the **same** `exp`/`log` object as the additive
  partition-function readout `W = log Z`. "Energies add" and "`W` is additive"
  are two readings of one multiplicative→additive identity.
- **Confirms the symmetry-type law as a theorem.** The additive-vs-multiplicative
  readout classification (continuous→additive, discrete→multiplicative,
  `exp`/`log` bridge) is reproven from elementary tensor algebra and cited
  framework context (runner T2/T3/T4). The
  framework's **both-ledgers** usage (`log|det|` additive; `Z_3` multiplicative)
  is consistent (§1, runner T1).
- **Provides a reusable closer.** Future agents proposing "the additive readout
  is forced because the quantity is an energy" can be pointed to §3.2/§3.3:
  either the additive generator is the `log` member of the transfer orbit (face
  ADD), or the free-energy identification is (II.b) = P1, or the intensive
  variant is face BLIND.

### 4.2 What remains admitted

- **P1 itself** (the exponent-fixing additivity step) remains an admitted
  physical-principle selection premise of
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`. This note does not retire it; it
  pins the energy route as P1-equivalent.
- **#2504's path (a′) is NOT fully foreclosed.** Only the **energy/free-energy
  ledger** instance is closed here. A genuinely new owner-approved premise that
  introduces a privileged scale by a mechanism that is **neither** the energy
  ledger **nor** a sector-composition selector remains research-grade open and
  is **not** claimed impossible.
- The parent note's audit row keeps its live ledger status; this `no_go`
  provides additional rigorous structural backing.

### 4.3 Forward paths (out of scope of this note)

- **(a′)** Discover/derive a new owner-approved premise **outside `𝒞`** and
  **outside the energy/free-energy ledger** that fixes the exponent by a
  separate physical scale mechanism. Research-grade open; no such premise is
  identified, and this note's theorem does not foreclose it.
- **(b)** Accept P1 (the exponent-fixing step) as a permanent classification
  premise (current state of the parent note).

### 4.4 No-Go Discipline Gate

**Status:** PASS for this narrow negative route claim. The negative claim is not
"P1 is impossible" and not "the symmetry-type law is wrong"; it is that the
**energy/free-energy ledger route** to the v-chain additive readout is
P1-equivalent — it lands in **face ADD** or relocates the **same** `exp`/`log`
dichotomy one level up. The symmetry-type law and the `exp`/`log` bridge are
reproven theorems; the class boundary is stated explicitly.

**N1 — Alternative route enumeration.**

| Route tested against the negative claim | Marker | Why it does not break this narrow no_go |
|---|---|---|
| Symmetry-type law (additive/multiplicative readouts) | THEOREM (not admitted) | Reproven (runner T2/T3/T4); classifies *which ledger*, does not select the ledger for `W`. |
| Energies-add via tensor structure (Pivot 1) | FACE ADD (one level up) | `Ĥ = −log(T̂²)`; `{(T̂²)^s}` one orbit; additive member is `log` (runner T5). |
| Energies-add for interacting subsystems | RULED OUT | Spectrum does not add for `g ≠ 0` (runner T6); additivity is the independent-class = P1 hypothesis. |
| "`W` is the free energy / energy-sector quantity" (Pivot 2) | FACE ADD = (II.b) = P1 | Free energy defined by log-det convention (runner T7); (II.b) `⇔` P1 (structural-reframing note). |
| Intensive / Born energy density | FACE BLIND | Orbit-invariant; `−log((T̂²)^s)/(2s) = E` for all `s` (runner T8); singles nothing. |
| New owner-approved premise **outside `𝒞` and outside the energy ledger** | OPEN (a′) | Not foreclosed; must be stated and audited separately. |
| Convention/reframe accepting P1 as a classification premise | OPEN FOR USER/REPO POLICY | Names/ratifies the premise; not a derivation. |

**N2 — Wall-independence audit.** The walls collapse to one load-bearing wall on
the energy route: the additive generator is the `log` member of the transfer
orbit (Pivot 1, face ADD) and the free-energy identification is (II.b) = P1
(Pivot 2). The symmetry-type law and the `exp`/`log` bridge are *separate
theorems*, not walls.

**N3 — Hidden-wall scan.** "Additive ledger," "multiplicative ledger," "energy
route," "Pivot 1/2," "symmetry-type" are local descriptive labels; "(BLIND),"
"(ADD)," "face," "orbit," "(II.a)," "(II.b)" are mapped to the existing #2504 /
#2456 / structural-reframing vocabulary, **not** new repo tags or a parent
framing. The disputed step (identifying `W` with the energy ledger) is named
explicitly as the tested admission; the load-bearing result is the elementary
tensor algebra plus the transfer-operator `H = −log(T²)` realization, not the
audit status of any framework row named for orientation.

**N4 — Residual matching.** The residual attacked is exactly "fix the v-chain
additive readout by declaring it an energy." Both pivots reduce to additivity
(face ADD); the symmetry-type law is kept separate and is not used as a witness
against itself.

**N5 — Rhetoric audit.** The claim is at the energy-route resolution. It does
**not** assert the symmetry-type law is false, a lattice-wide / per-site no-go,
or that #2504's (a′) is fully foreclosed (only the energy-ledger instance is
closed).

**N6 — Partial-closure path scan.** Two partial paths remain: (a′) an
out-of-class, non-energy-ledger premise introducing a separate scale
mechanism; and accepting the exponent-fixing step as a named classification
premise. Neither is called a new axiom and neither is foreclosed.

**N7 — Steelman.** A hostile reviewer insists "energy is *physically* additive,
prior to any `log` bookkeeping — that is an out-of-class structural fact, not a
selection." Response: in *this* framework the Hamiltonian is **not** a primitive
(the baseline carries no dynamics) and is **realized** as `Ĥ = −log(T̂²)` with `T̂²`
multiplicative; its additivity is the `log` member of the transfer orbit (runner
T5), and holds **only** in the independent class (runner T6), which is P1's
hypothesis. The "prior physical additivity of energy" is, operationally, the
admitted additive/cluster property (Haag; Weinberg §4.4) — face ADD. A genuinely
out-of-class scale mechanism that is **not** the energy ledger is the residual
(a′); this note does not claim it impossible.

**N8 — Cross-cycle echo.** The same wall shape appears in Route D, the locality,
extensivity, structural-reframing, #2456, and #2504 no-gos. This note adds the
**energy/free-energy ledger** as another route that collapses into the orbit
dichotomy (face ADD), and confirms the symmetry-type law as the theorem that
classifies the two ledgers without selecting the ledger for `W`. It does **not**
claim universal P1 impossibility.

## 5. Comparison with route portfolio

| Route | Axis / mechanism | Outcome | Relation to this note |
|---|---|---|---|
| Route D consolidated no-go | direct-sum `F_p` selection | no_go | the `F_p` obstruction the energy route also hits (at the transfer orbit) |
| Locality of source-derivatives | cross-block 2nd-deriv (Loc) | existing no-go | (Loc) is the `K = 0` member of face ADD |
| Extensivity route | integer-`N` scaling | existing no-go | a weak (Add) variant; face ADD |
| Structural reframing (cumulant) | `W = log Z` identification (II.b) | existing no-go | **Pivot 2 IS (II.b); proven `⇔` P1 there** |
| `det`-character form selection | operator-product character | bounded_theorem | Stage FORM; orthogonal to the energy route |
| FORM-premise integrity (#2503) | `(M)` co-admission | no_go | the form atom; this note is the exponent/energy atom |
| Two-stage synthesis | FORM collapse + Gibbs scale | bounded_theorem | the Gibbs/energy scale is face ADD here |
| #2456 exponent-fixing irreducibility | (Add)⇔(Loc)⇔(Pot) + Born | no_go (four selectors) | this note adds the energy ledger as another face-ADD route |
| #2504 exponent-fixing selector dichotomy | orbit `{r↦r^p}` dichotomy on `𝒞` | no_go (class `𝒞`) | **this note tests its open path (a′) for the energy ledger and closes that instance** |
| **This note — symmetry-type / energy readout** | **energy ledger via `H = −log(T̂²)` + (II.b) free-energy** | **no_go (energy-ledger instance of (a′))** | **the energy route lands in face ADD = P1; symmetry-type law is a theorem** |

**Structural distinction.** #2504 proved the dichotomy on the
sector-composition selector class and flagged (a′): an out-of-class structural
premise introducing a separate scale. This note takes the **energy ledger** —
the most natural such candidate, and the one the reframe proposes — and shows it
is **not** out of class: at the partition-function level it is (II.b) = P1, and
at the generator level it is the same `exp`/`log` move one level up (face ADD),
with the intensive variant face BLIND. The symmetry-type **law** is confirmed as
a theorem; what it cannot do is select the energy ledger for `W` without P1.

## 6. Hypothesis set used (forbidden-imports check)

The note uses only:

- Elementary tensor algebra: `spec(H_A ⊗ I + I ⊗ H_B) = { e_a + e_b }`;
  `χ(g_A ⊗ g_B) = χ(g_A)χ(g_B)`; `exp(H_A ⊗ I + I ⊗ H_B) = exp(H_A) ⊗ exp(H_B)`
  (runner T2/T3/T4).
- Elementary determinant algebra on block-diagonal direct sums
  (`Z = Z_A·Z_B`, `log Z = log Z_A + log Z_B`; runner T4/T7).
- The framework's free quadratic-sector realization `Ĥ = −log(T̂²)/(2a_τ)`,
  `T̂² = ⊗_p diag(1, e^{−2E(p)})` (runner T5), from the cited two-step
  transfer-matrix note.
- The per-matrix-entry log-det free-energy convention `Δf` (runner T7), from the
  Matsubara free-energy-density note (which disclaims any physical free-energy
  identification beyond the log-det convention).
- The (II.b) `⇔` P1 equivalence (runner T7), from the structural-reframing note.
- The Cauchy/Shannon-Khinchin uniqueness instance — literature comparator only;
  reproven elsewhere (#2504 runner T7).

No fitted parameters. No observed values. No PDG comparators (the `v` numerical
readout of the parent note is **not** consumed). No new framework axiom (per
`feedback_no_new_axioms.md`). No new repo-wide vocabulary tag or class name (per
`feedback_no_new_repo_vocabulary.md`); only repo-canonical terms and the
existing #2504 / #2456 / structural-reframing vocabulary. No promotion of any
cited framework note's audit status.

## 7. Forbidden imports check

- No PDG observed values consumed (the parent note's `v = 246.28 GeV` readout is
  not consumed).
- No literature numerical comparators consumed.
- No fitted selectors consumed.
- No admitted unit conventions load-bearing on the claim.
- No same-surface family arguments.
- No new repo vocabulary or class tags.

## 8. Reproduction

```bash
python3 scripts/audit_companion_observable_principle_p1_symmetry_type_energy_readout_2026_06_02.py
```

Expected scorecard: `PASS=27, FAIL=0` at exact SymPy precision. A passing run
supports ONLY the bounded finding above (the symmetry-type readout law is a
representation-theory theorem; the energy route to the v-chain additive readout
collapses into the #2504 face ADD = P1 via both pivots, with the intensive
variant face BLIND). It does **NOT** close P1, does **NOT** claim #2504's (a′)
is fully foreclosed, does **NOT** promote any framework row, and consumes no
fitted or observed numerical targets.

## 9. Validation

Primary runner:
[`scripts/audit_companion_observable_principle_p1_symmetry_type_energy_readout_2026_06_02.py`](../scripts/audit_companion_observable_principle_p1_symmetry_type_energy_readout_2026_06_02.py)
verifies at exact SymPy / Fraction precision:

- **T1** structure survey: additive readout `log|det|` (parent + Matsubara
  free-energy) and multiplicative readout `Z_3` character (Koide / DM-neutrino /
  color-generation gate) both present and used consistently.
- **T2** symmetry-type law (a): `spec(H_A ⊗ I + I ⊗ H_B) = { e_a + e_b }`
  (eigenvalues add), reproven on small matrices.
- **T3** symmetry-type law (b): `χ(g_A ⊗ g_B) = χ(g_A)·χ(g_B)` (characters
  multiply), reproven on the `Z_3` regular rep and a generic `2×2 ⊗ 2×2`.
- **T4** `exp`/`log` bridge: `exp(H_A ⊗ I + I ⊗ H_B) = exp(H_A) ⊗ exp(H_B)`
  (algebra→group) and `log(Z_A Z_B) = log Z_A + log Z_B` (partition→free-energy)
  are the same `(ℝ_+,×) → (ℝ,+)` homomorphism.
- **T5** PIVOT 1: `Ĥ = −log(T̂²)/2 = Σ_p E(p) n_p`; `{(T̂²)^s}` is one
  `{r↦r^s}` orbit; the additive coordinate `−log((T̂²)^s)/(2s) = Ĥ` for every
  `s` — energies-add is face ADD at the transfer level.
- **T6** PIVOT 1 steelman: interacting `H_int` (`g ≠ 0`) does NOT have the
  additive spectrum — additivity is the independent (non-interacting) class =
  P1's hypothesis.
- **T7** PIVOT 2: `Δf := ln|det(D+m)| − ln|det D|` reproduces the Matsubara
  density (presupposes `log|det|`); (II.b) `W = log|Z|` `⇒` additivity, and
  `F_p` (`p ≠ 0`) fails additivity — (II.b) `⇔` P1.
- **T8** synthesis: the energy readout is bare additivity (face ADD = P1); the
  intensive (normalized) energy density is orbit-invariant (face BLIND); no
  third energy readout fixes a finite nonzero exponent.
- **T9** live-ledger context presence (no dependency status consumed).
- **T10** note honest-scope strings present (including the plain-text phrase
  "does NOT close P1"); forbidden status-promotion / overclaim verdict tokens
  (the retention and reduced-kernel verdict strings the runner enumerates)
  absent.
- **T11** source-note boundary declarations present.

## 10. Cross-references

Load-bearing (markdown-linked) authorities: **none** — the load-bearing content
is the elementary tensor algebra, the transfer-operator `H = −log(T²)`
realization, and the reproven (II.b) `⇔` P1 / Cauchy skeleton; the framework
rows below are target/context only and their audit statuses are not consumed.

- [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  — parent broad row whose P1 admitted premise this `no_go` pins. Its audit
  status is unaffected by this row.
- `OBSERVABLE_PRINCIPLE_P1_EXPONENT_SELECTOR_DICHOTOMY_NARROW_NOTE_2026-06-02.md`
  (#2504; not a markdown-linked edge until it lands on main) — whose open path
  (a′) this note tests for the energy/free-energy ledger and closes that
  instance.
- [`OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md`](OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md)
  — #2456, the predecessor pinning the exponent atom under the four enumerated
  selectors.
- [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_STRUCTURAL_REFRAMING_NARROW_NOTE_2026-05-21.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_STRUCTURAL_REFRAMING_NARROW_NOTE_2026-05-21.md)
  — supplies content (II.b) `⇔` P1 (Pivot 2).
- [`HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_2026-05-16.md`](HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_2026-05-16.md)
  — the free-energy density defined by the log-det convention (Pivot 2 source).
- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  — the free quadratic-sector realization `Ĥ = −log(T̂²)/(2a_τ)` (Pivot 1
  source).
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  — the Lattice/Qubit/Admissibility/Record baseline and the fact that dynamics are not part
  of the baseline.
- [`KOIDE_Q_TWO_THIRDS_Z3_CHARACTER_NORM_SPLIT_RECASTING_THEOREM_NOTE_2026-05-10.md`](KOIDE_Q_TWO_THIRDS_Z3_CHARACTER_NORM_SPLIT_RECASTING_THEOREM_NOTE_2026-05-10.md),
  [`DM_NEUTRINO_Z3_CHARACTER_TRANSFER_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_Z3_CHARACTER_TRANSFER_THEOREM_NOTE_2026-04-15.md),
  [`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md`](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md)
  — the multiplicative-ledger (`Z_3` character) usage (structure survey, §1).

External mathematics (cited inline as comparator, not as derivation input):
E. P. Wigner (1931/1959) Ch. 11–12, 26; J. E. Marsden & T. S. Ratiu (1999) §9;
B. C. Hall (2015) §2.5, §3; A.-L. Cauchy (1821) §V; J. Aczél (1966) §2.1 Thm 1;
C. E. Shannon (1948) §6; A. I. Khinchin (1957) Thm 1; R. P. Feynman & A. R.
Hibbs (1965) §10; J. I. Kapusta & C. Gale (2006) §2; R. Haag (1992) §II–III;
S. Weinberg (1995) §4.4; O. Bratteli & D. W. Robinson (1981) §5.3; M. Reed &
B. Simon (1975) §X.

### Source-note boundary

**Hypothesis set used:** (1) elementary tensor algebra (additive generators add
eigenvalues; discrete-group elements multiply characters; `exp`/`log` bridge;
runner T2/T3/T4); (2) the framework's free quadratic-sector realization
`Ĥ = −log(T̂²)`, `T̂² = ⊗_p diag(1, e^{−2E(p)})` (runner T5); (3) the
per-matrix-entry log-det free-energy convention `Δf` (runner T7); (4) the
(II.b) `⇔` P1 equivalence (runner T7); (5) the Cauchy/Shannon-Khinchin
uniqueness instance (literature comparator only). The physical identification of
the readout with `det(D+J)` is not assumed closed — it remains gated by the
staggered-Dirac realization gate, as in the parent note.

**Forbidden-imports check:** this note introduces **no** new framework axiom and
**no** new repo vocabulary or class tags. It uses only standard mathematical
terms and the repo-canonical / #2504 / #2456 / structural-reframing vocabulary.
"Additive ledger," "multiplicative ledger," "energy route," "Pivot 1/2,"
"symmetry-type" are local descriptive labels; "(BLIND)," "(ADD)," "face,"
"orbit," "(II.a)," "(II.b)" are mapped to the existing vocabulary, **not** new
repo tags or a parent framing.

**No-promotion statement:** this note does **not** promote, demote, or set the
audit status of `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, #2456, #2504, the
`det`-character note, the FORM-premise integrity note, the two-stage synthesis,
the Route D consolidated no-go, the structural-reframing no-go, the six existing
no-go rows, the Matsubara free-energy / transfer-matrix rows, the
staggered-Dirac realization gate, or any other upstream row. The independent
post-landing process is the only status-setting path.

**Circularity check (explicit).** "Energies/the Hamiltonian are additive over the
tensor product" and "`W = log Z` is additive" are the **same**
multiplicative→additive (`exp`/`log`) content read at two levels (generator/group
vs partition-function/free-energy). Using either to **derive** `log` is
circular: additivity is the hypothesis at both levels. This note uses the
two-level identity only to **prove the energy route is P1-equivalent** (diagnosis:
reduces to P1), never as a derivation of `log`.
