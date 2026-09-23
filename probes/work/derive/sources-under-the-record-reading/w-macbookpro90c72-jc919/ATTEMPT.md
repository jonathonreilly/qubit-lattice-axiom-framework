# J:derive:sources-under-the-record-reading:a4: the formation ledger is exact for every amplitude; the star is a perfect point charge and nothing larger is; a source in two places separates the readings

**Provenance.**
- Worker `w-macbookpro90c72-jc919`, model `claude-opus-5-5`, one session. Unit a4 (attempt 4 of 4). The axioms memo was read in full this session.
- **Plan, formed before reading the prior attempt:**
  - (b) the field's self-energy `−(γ/12) e·g·e`, with `g` the potential of `(1 − average)` with the walls held, and the energy a record needs to keep the ledger;
  - (a) momentum and ledger bookkeeping from block 55 T1–T3;
  - (c) a source in two places;
  - (d) a sentence-by-sentence reading.
- **The prior attempt a3** (worker `j556e`) is the same model family and has not been refereed. It points to blocks 56, 58 and 67, also same family and unrefereed.
  - Its exact kept-ledger condition (block 58 T1) coincides with the one derived here.
  - This attempt reproduces its star value `1188/1091` with independent code.
- **New here:**
  - the static law is linear for every amplitude, moving ones included;
  - the star's closed form, with a proof;
  - an exact counterexample showing that a3's "locality" (wall-independence) holds for the star only;
  - a discriminator that does not need the source to stay unformed.
- **Related earlier units by the same model:** #8736 (a two-record ledger) and #8739, whose point body `φ₀ = 1/(1 + (γ/12)G₀(0)m)` is B1 on `Z³`. Neither is a premise here.
- **Setting.** Blocks 53, 54 and 55 are read on their PR branches (#8568, #8570, #8571). Nothing is adopted, the parked statistical postulate is not assumed or raised, and no gravitational claim is made.

## 1. The statement attempted

**Notation.**
- `F = (2/γ) Σ_bonds (φ_x − φ_y)²` (block 55 T4(c)), and `k = γ/12`.
- The walls of a box are held at the ambient rate `φ = 1`. They fix the unit of rate, so `μ = 0` inside.
- `g` is the potential of `(1 − average)` with the walls held at zero. On `Z³` (ambient held at infinity), `g_yy = G₀(0) = 1.5164`.

**(b) Theorem (PROVED; CHECKED B1–B6).**
- **The ledger is a quadratic form.** For any amplitude `χ` and hermitian `H`, the ledger `⟨χ|φHφ|χ⟩ + F` equals `φᵀMφ + (2/γ)Σ_bonds(φ_x − φ_y)²`, with `M_xy = Re χ_x†H_xyχ_y`. Its row sums `e_x = Σ_y M_xy` are block 55's energy density. So the static law is **linear** in `φ`:

  `(Mφ)_x + (2/γ)(6φ_x − Σ_{y∼x} φ_y) = 0` inside.

- **(i) One record of energy `E` at `y`.** `φ_y = 1/(1 + kEg_yy)`, and the ledger is `E/(1 + kEg_yy) = Eφ_y`.
- **(ii) The kept-ledger condition.** A formation event replaces an amplitude with static ledger `Λ` by one record at `y`. It keeps the ledger iff the record's energy is

  `E'_y = Λ/(1 − kΛg_yy)`,

  which needs `kΛg_yy < 1`. This holds for every amplitude, hopping energy included (B4). For amplitudes at rest it is block 58 T1's statement.
- **(iii) The weak field.** `Λ = E − k e·g·e + O(k²)`, so

  `E'_y − E = (γ/12)(E²g_yy − e·g·e) + O(γ²E³)`.

  This is the change of the field's self-energy when the source contracts from the energy density `e` to a point. On `Z³`, `g_yy = G₀(0)`, and in the continuum `e·g·e/E² → (3/2π)⟨1/r⟩`, which is `9/(5πR)` for a uniform ball. That continuum remark is not checked.
- **(iv) Where the record forms.** `E'_y` depends on `y` only through `g_yy`.
  - On `Z³`, `g_yy = G₀(0)` everywhere. So one energy, blind to the site, keeps the ledger exactly wherever the record forms, with no rule for where.
  - In a held box `g_yy` varies. For a `3³` cube amplitude in box 7 (`E = 1`, `γ = 1`) the kept-ledger energy takes four values, `1.10548` at a corner to `1.10971` at the centre. A site-blind energy then keeps the ledger only on average, and only for particular odds.
- **(v) The star.** Take `y` and its six neighbours, with weights `m₀` and `m₁` each.
  - Outside the star its field is exactly that of a point charge at `y`.
  - The kept-ledger energy is

    `E' = c/(1 − kc)`, with `c = m₀/(1 + km₀) + 6m₁`.

  - This is the same in every held box symmetric about `y`, and on `Z³`. For the uniform star at `γ = 1` it is `1188/1091`.
  - For larger cubic-symmetric amplitudes it fails: the 19-site ball and the distance-2 cross give kept-ledger energies differing between boxes 7 and 9 by `+8.4·10⁻⁵` and `−7.2·10⁻⁴` (exact).

**(a) Records only (PROVED from block 55 T1–T3; CHECKED A1).**
- **Where the momentum goes.** A packet that has formed no record sources nothing. It is pulled by records with block 54's force `−e∇u` and pulls nothing back.
  - With records at rest, the packet's momentum changes and nothing else's does. Records are permanent under the Record axiom, and they are immobile given the axioms' silence on motion.
  - The fixed arrangement of records acts as an external field. The momentum goes nowhere within the pair, because the records' fixed positions break translation invariance.
  - The ledger `⟨H_w⟩ + F[records]` is kept, but trivially: `H_w` is static, and `F` does not depend on the packet.
  - A1 gives the imbalance for unit energies in box 9: (pull on packet) + (pull on record) = the packet's pull, `−0.013010`. This is block 55 T3 with `S_packet = 0`.
- **If records move (the owner's reading of 2026-09-20).**
  - The packet's `⟨H_w⟩` changes at `Σ_x e_x du_x/dt` (T1) with nothing to balance it (T2(b), with `s` the records' source). So no ledger is kept.
  - The total momentum changes at the rate of the packet's pull (T3). Nothing in the pair takes up the momentum.
- **At formation.** A source appears where there was none; (b) states what the record's energy must be for the ledger to survive that event.

**(c) A discriminator from the test body's records (CHECKED C1; weak field).**
- **Setup.** A source `B` of energy 1 is in two places, `L` and `R`. As an amplitude it has half its energy at each. A test body `T` passes along a line, and its transverse kick is read from its own records.
- **The four possible kicks:**
  - `B` has formed at `L`: `δ_L = −0.161235`;
  - `B` has formed at `R`: `δ_R = +0.033643`;
  - `B` is unformed, under records only: `0`;
  - `B` is unformed, under amplitude sourcing: `δ_c = (δ_L + δ_R)/2 = −0.063796`, exactly, because the weak-field law and the kick are linear.

  (Box 9, sources at `(0,∓2,0)`, test line `y = −1`, `z = 0`.)
- **The discriminator.** Take the set of kicks over repeated runs. Under records only every kick lies in `{0, δ_L, δ_R}`. Under amplitude sourcing the value `δ_c` occurs whenever `B` is unformed during the passage, and `δ_c` is none of the other three whenever `δ_L ≠ ±δ_R`. One run with kick `δ_c` excludes records-only sourcing.
- **Assumptions about formation, named:**
  1. `T` forms records along its path that resolve its transverse position well enough to separate the four values. Its formation odds are not specified.
  2. `B`'s formation is all or nothing and at one place (the Record axiom: a record locks one possibility at one site). Whether and when `B` forms is **not** assumed; this is weaker than a single-lobe test, which needs `B` to stay unformed.
  3. `T`'s own source is negligible, and `T` does not cause `B` to form.
  4. The field follows its sources statically during the passage (block 55's static law).

**(d) The axioms, sentence by sentence (a reading, not a theorem).** "Both" means both readings (records only, amplitude sourcing) fit the sentence.

| sentence | records only (a) | amplitude sourcing (c) |
|---|---|---|
| "Records form." | fits | fits |
| "When present, a record locks exactly one admissible local possibility." | fits; the source is the locked content's energy, whose value is formation-rule content (b) | fits |
| "A site never carries more than one record; records are permanent." | fits; a formed source never disappears. Motion is not in the axioms (it is the owner's reading) | fits |
| "Only records are readable." | fits | fits; the field is read only through test bodies' records (C1 uses nothing else) |
| "A readout value is determined by record content alone." | fits | fits; which content forms is formation-rule content, outside this sentence |
| "A site with no record cannot be read." | fits | fits; an unrecorded amplitude sources without being read |
| "These axioms state only their named primitive content." | neither source clause is axiom content | same |
| "Further physical structure requires a retained derivation or bridge, or explicit approved-primitive registration, before use as a premise." | a named conditional here | a named conditional here |
| "A choice not fixed by the supplied structure remains a named conditional or open dependency." | the choice between (a) and (c) is such a choice; this attempt keeps it conditional | same |
| "A state is a configuration of records." with "at every state where the condition holds it gives exactly one answer." | fits directly: the field is a function of the configuration of records, one answer per state | the field depends on the amplitude, which is no part of a configuration of records. Two situations with the same records and different amplitudes get different fields, so (c)'s field law is a law in this sense only if the amplitude belongs to its supplied condition |
| "A law privileges no states." | fits (covariant rules) | fits |

So (a) fits every sentence. (c) fits the Record sentences, and fits Qualification's "state" and "one answer" sentences only if the amplitude is made part of the law's supplied condition.

## 2. Steps

**S1: the ledger is a quadratic form (PROVED; CHECKED B1, B4).**
- `⟨H_w⟩ = Σ_{x,y} φ_xφ_y χ_x†H_xyχ_y` (block 55 T1's proof). Its real symmetric part is `M`, because the imaginary parts cancel in the hermitian sum.
- `F` is quadratic in `φ`.
- `∂/∂u_x = (φ_x/2) ∂/∂φ_x`, so for positive rates stationarity in every interior `u_x` is stationarity in every `φ_x`: the linear system above.

**S2: one record (PROVED; CHECKED B1).**
- Off `y`, `φ` is harmonic, so `1 − φ = c·g(·,y)`.
- At `y`: `Eφ_y + (12/γ)(φ_y − avg φ) = 0`, and `avg g(·,y)` at `y` is `g_yy − 1`. This gives `c = kE/(1 + kEg_yy)` and `φ_y = 1/(1 + kEg_yy)`.
- The ledger is `Eφ_y² + (2/γ)·6c²g_yy = E/(1 + kEg_yy)`.

**S3: the kept-ledger condition (PROVED; CHECKED B2, B4).** Solve `E'/(1 + kE'g_yy) = Λ` for `E'`.

**S4: the weak field (PROVED; CHECKED B3, B4).**
1. Write `φ = 1 − ψ`. Then `Λ(1 − ψ) = E − 2e·ψ + (2/γ)·6ψ·(1 − avg)ψ + O(ψ²M)`.
2. Stationarity gives `ψ = k g e`, and `Λ = E − k e·g·e + O(k²)`.
3. Combine with S3.
- **Checked.** The exact ratio `(E' − E)/(k(E²g_yy − e·g·e))` is `1.0000099` at `γ = 10⁻⁴` and `1.00000099` at `10⁻⁵` (rest cube), and `1.00006` at `10⁻⁴` (moving star, hopping part of `⟨H⟩` `= −0.4583`).

**S5: the formation site (PROVED; CHECKED B2, B6).** `E'_y` depends on `y` only through `g_yy`. On `Z³`, translation invariance makes `g_yy` constant.

**S6: the star (PROVED; CHECKED B5).** Let `n_i` be the six neighbours of `y`, and take a box symmetric about `y`.
1. **Three reductions:**
   - for `x` not in the star, `Σ_i g(x, n_i) = 6g(x, y)`, from `(1 − avg)g(x,·) = δ_x` evaluated at `y`;
   - `g(n_i, y) = g_yy − 1`, from the equation at `y` and the symmetry;
   - `Σ_i g(n_j, n_i) = 6(g_yy − 1)`.
2. **The charges.** With `φ_y = a`, `φ_{n_i} = b` and charges `q₀ = km₀a`, `q₁ = km₁b`, the total charge is `Q = q₀ + 6q₁ = kΛ`. Outside the star the field is `Q·g(·,y)`, a point charge.
3. **Solving.** `b = 1 − (g_yy − 1)kΛ`, `a = b/(1 + km₀)`, and `Λ = bc`. Hence `1/Λ − kg_yy = 1/c − k`, which does not depend on the walls, and `E' = c/(1 − kc)`.
4. **Larger amplitudes.** They meet Green values that are not fixed by `g_yy` alone. B5 shows two exact counterexamples.

**S7: (a) (PROVED; CHECKED A1).** Block 55 T1, T2(b) and T3 with the packet's source zero, as stated.

**S8: (c) (PROVED; CHECKED C1).** The kicks are exact rationals from `g` in box 9, and `δ_c = (δ_L + δ_R)/2` by linearity.

**S9: (d).** A reading, set out in the table above.

## 3. The first failing step

- **No formation clause.** Nothing here derives the record's energy. (b) only says what it must be for the ledger to survive: `Λ/(1 − kΛg_yy)`. In a held box that value depends on the site; on `Z³` it does not.
- **The discriminator is weak-field.** Beyond linear order `δ_c` is not exactly the mean. It also rests on the test body's records resolving the four values, whose statistics depend on formation rules that are not supplied.
- **(d) is a reading.** In particular, whether an amplitude may belong to a law's "supplied condition" is for the owner to decide.

## 4. What would finish it

1. A formation clause that assigns the record's energy. It would have to give `E' = Λ/(1 − kΛg_yy)` for the ledger to be kept, site-dependent unless the ambient is held at infinity.
2. The discriminator executed with block 54's walk as the test body and a named rule for the test body's records, with frequencies. Those would need `B`'s formation odds; the support test above does not.
3. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/sources-under-the-record-reading/w-macbookpro90c72-jc919/check.py
```

The run takes about 50 s. Everything is exact rationals, apart from one 30-digit value of `G₀(0)`. It prints B1–B6, A1 and C1, then the SUMMARY and HIT lines.

Standard mathematics used, none as authority:
- exact sparse Gaussian elimination;
- the lattice mean-value property of `(1 − average)`;
- Watson's closed form for `G₀(0)`.
