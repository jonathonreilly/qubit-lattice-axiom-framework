# Wave 1 / Derivation A — Berezin mode content of the charged-lepton corner carrier

**Worker:** Derivation A (action / Berezin-measure side), 2026-07-24.
**Surface:** `origin/main` at `02f9359281`, fetched at session start.
**Status authority:** this is a source-side worker report. It sets no audit
verdict, adopts no premise, adds no axiom and no new vocabulary, and edits
no repo file other than itself.

---

## 1. Result, stated once

**The mode count is `n`, not `2n` — and the mode count does not decide the
campaign's binary.** Both halves of that sentence are load-bearing.

On the landed corner carrier the coherent-state Berezin representation of the
CAR algebra carries **`n = 3` independent complex modes per Grassmann copy —
one canonical pair `(theta_chi, thetabar_chi)` per character channel
`chi in {1, w, wbar}`, hence 6 Grassmann generators.** The K-conjugate partner
channel `V_wbar` **IS an independent Berezin integration variable**: it is a
distinct generator of the same Grassmann algebra, and integrating over it is a
separate integration. Nothing in the action's reality/conjugation structure
identifies it with `theta_w`, because `K` is antilinear on coefficients and
Berezin generators carry no reality condition that an antilinear map could
quotient.

That answer is derivable. It is also **r-neutral**, for three independent
reasons which I derive below:

- **(A1)** The `|det_C|^2` horn is not obtained by integrating the partner
  channel "again". It is obtained by **adjoining a second disjoint field
  copy**, and every whole-carrier copy-doubling multiplies the singlet and
  doublet exponents **together**: `(1,1) -> (2,2) -> (3,3)`. Every
  doublet-to-singlet ratio is unchanged. The determinant-power axis is
  therefore incapable of moving `r`.
- **(A2)** The r-dial `r = |b|^2/a^2` is a ratio of **coupling** data (the
  coefficient of `I` versus the coefficient of `C`). The Berezin measure
  partitions the **fermion one-particle space**. These are partitions of two
  different spaces, and the character transform carries neither onto the
  other: the coupling cell `{a I}` maps to the character vector `(a,a,a)`,
  which meets **every** character cell, and the character cell `{chi_1}` pulls
  back to `(I + C + C^2)/3`, which meets **every** coupling cell.
- **(A3)** If one nonetheless forces the identification "Berezin slot =
  formation cell", the Berezin slots are the **character channels**, and
  2-cell equipartition on character channels gives
  `r = 17/2 - 6 sqrt(2) ~ 0.0147` — the landed *idempotent/eigenvalue*
  reading — which is **neither** horn of the campaign's binary.

So the honest output of Derivation A is a **sharpened circularity, plus one
new derived obstruction**. The sharpening is stronger than "the polarization
is unselected": it is that **the action/Berezin axis cannot in principle
select `r` through mode counting**, because mode counts live on the wrong
space and every doubling available on this surface is r-neutral. The new
derived obstruction (Section 9) is that the only Berezin object that *does*
produce the count-once exponent pair — a 2-mode "holomorphic half" carrier
`V_1 (+) V_w` — has a partition function that is **not K-invariant**, and its
`w`-versus-`wbar` label is a lattice-rotation frame orientation, so it is not
selectable by carrier data.

I hold Section 8's "wrong space" claim most strongly (it is exact algebra).
I flag Section 11's uncertainty list as genuinely open.

---

## 2. Kill-check — what is already landed, and exactly where it stops

The campaign's rule 1 requires a kill-check before construction. The route is
**not** foreclosed by a landed no-go. It is something more awkward: **the
central question has already been answered on `main`, and the answer is
r-neutral.**

`docs/KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md:56-58`
already computed the measure order:

> **Fact 1 — the measure is first-order.** The Berezin integral of the
> single-pair-per-site Grassmann measure is computed by explicit
> exterior-algebra expansion and nested single-generator Berezin

and `:66` records the doubling that is available:

> **Fact 2 — exact corner factorization; the taste square is r-neutral.**

and `:92-97` relocates the count-twice source away from the measure entirely:

> Hermitian-channel restriction of the probe coupling (check 16). So on this
> surface the second-order (count-twice) structure is not supplied by the
> measure, the corner sector, or the taste doubling — it is supplied by the
> **parameter restriction** `c = b̄`, which is the K-reality selector already
> named as an operative admitted input in

`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:177`
then computed the r-neutrality of the generator-count doubling explicitly:

> 3. **r-neutral doubling.** `lam_0^2 * |lam_1|^4 = (lam_0 * |lam_1|^2)^2`

and `:114` flags the generator-count-to-occupancy-slot bridge as declared, not
derived:

> declared bookkeeping; no framework clause identifies occupancy slots with

and `:199`:

> `m` to generator-count correspondence is declared bookkeeping, never an

**Consequence for the campaign statement.** The campaign's target names four
framings as equivalent:

> Does the physical charged-lepton matter action count the K/CPT
> orbit (equivalently: the holomorphic determinant grain det_C;
> equivalently: the 2-cell quotient menu; equivalently: 6 Grassmann
> generators per triple copy) ONCE, or count each sector/channel
> separately (|det_C|^2 realified grain; 3-cell carrier menu; 12
> generators)?

(`.claude/science/physics-loops/koide-mode-content-campaign-20260724/CAMPAIGN.md:14-19`)

Sections 7-8 below show, in exact algebra, that **"6 vs 12 generators" is not
equivalent to "2-cell vs 3-cell menu"**. The generator-count axis is
`(m, m)`-shaped and r-neutral; the menu axis is `(1,1)` versus `(1,2)`-shaped
and r-deciding. This is a break in the campaign's own equivalence chain, and
it is the single most important thing in this report. I did not go looking for
it; the algebra forced it.

The route is therefore not a corpse, but the campaign's *reason* for
expecting it to work ("nobody has built the carrier's CAR algebra and counted
its Berezin modes") is answered by the count being **r-blind**, not by the
count being unavailable.

---

## 3. The carrier, built

I rebuild the carrier rather than cite it. The delivered corner carrier is
quoted verbatim from
`docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md:50-52`:

> The real cyclic `C` with `C^3 = I_3` and `C^T = C^2`, the character projectors
> `P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for `chi in {1, w, conj(w)}`,
> `w = -1/2 + (sqrt(3)/2)*i`, and entrywise conjugation `K` in the canonical basis.

Explicitly, in the corner (hw=1 kernel) basis `v_mu(x) = (-1)^{x_mu}`:

```text
        [0 0 1]                                  1     sqrt(3)
  C  =  [1 0 0],      C^3 = I,   C^T = C^2,  w = - -  + ------- i .
        [0 1 0]                                  2       2
```

Character projectors, and their K-orbit structure (`K` = entrywise conjugation):

```text
  P_1    = (I +   C +   C^2)/3
  P_w    = (I + wbar C + w    C^2)/3
  P_wbar = (I + w    C + wbar C^2)/3

  P_1 + P_w + P_wbar = I ,     C P_chi = chi P_chi ,

  K P_1 K    = P_1        (K-FIXED singlet channel)
  K P_w K    = P_wbar     }  one two-element K-orbit
  K P_wbar K = P_w        }  (the doublet)
```

The carrier is **real**: it is the complexification of the real 3-dimensional
lattice subspace `V_R = span_R{v_1, v_2, v_3}`, because the corner plane waves
are real lattice functions. This is why `K` exists on it at all. Write

```text
  V   = V_R (x) C  =  V_1 (+) V_w (+) V_wbar        (dim_C = 3)
  V_R = R.(1,1,1)/sqrt(3)  (+)  W                   (dim_R = 1 + 2)
```

where `W` is the 2-dimensional real `C_3`-irrep of complex type, and
`W (x) C = V_w (+) V_wbar`. **The K-orbit structure and the real-irrep
structure are the same structure**: `{V_1}` and `{V_w, V_wbar}` are the two
`C_3`-isotypic summands of `V_R`.

The coupling (probe, not derived — see Section 11, assumption A-4) is the
Hermitian section

```text
  W_H(a,b) = a I + b C + bbar C^2 ,   a in R,  b = b_1 + i b_2 in C .
```

Its three channel values are exactly (worker probe, exact sympy):

```text
  lam_0 = a + 2 b_1
  lam_1 = a -   b_1 - sqrt(3) b_2
  lam_2 = a -   b_1 + sqrt(3) b_2
```

All three are **real** on the Hermitian section, and `K` (which acts as
`b_2 -> -b_2`) **fixes `lam_0` and swaps `lam_1 <-> lam_2`**. Two consequences
worth stating because they are easy to get wrong:

- On the Hermitian section, `conj(lam_1) = lam_1`, **not** `lam_2`. The
  familiar "`lam_2 = conj(lam_1)`, hence `det3 = lam_0 |lam_1|^2`" grouping
  belongs to the *entrywise-real* locus `(a,b,c) in R^3` of the spectral-pairing
  lineage, **not** to the Hermitian section on which Koide's `Q` is read. The
  two loci intersect only at real `b` (where `lam_1 = lam_2`). I flag this in
  Section 11 as a live cross-note scope hazard.
- On both loci the K-orbit partition of the channel set is the same:
  `{0} u {1,2}`.

Determinant, from the same probe:

```text
  det W_H = a^3 - 3 a |b|^2 + 2 b_1^3 - 6 b_1 b_2^2
          = a^3 - 3 a |b|^2 + 2 Re(b^3)
          = a^3 - 3 a |b|^2 + 2 |b|^3 cos(3 delta) ,     b = |b| e^{i delta}
```

and the two Koide moments:

```text
  sum_k lam_k   = 3 a
  sum_k lam_k^2 = 3 a^2 + 6 |b|^2 = Tr(W_H^dag W_H)

  Q = (sum lam_k^2)/(sum lam_k)^2 = 1/3 + (2/3) r ,      r = |b|^2/a^2 .
```

---

## 4. The CAR algebra, built small and explicit

Attach one complex fermion mode to each character channel. Generators
`a_chi`, `a_chi^dag` for `chi in {1, w, wbar}`, i.e. `n = 3`:

```text
  {a_i , a_j^dag} = delta_ij ,     {a_i , a_j} = 0 ,     i,j in {1,w,wbar}.
```

I realize this concretely by Jordan-Wigner on the 8-dimensional Fock space
`Lambda(V)`, occupation basis `|n_1 n_w n_wbar>`, `n_i in {0,1}`:

```text
  a_k |...n_k...>  =  (-1)^{sum_{i<k} n_i} n_k |...(n_k - 1)...|
  dim Fock = 2^n = 2^3 = 8 ,     8 = 1 + 3 + 3 + 1  (grade decomposition).
```

The worker probe verifies all nine anticommutators
`{a_i, a_j^dag} = delta_ij` and all nine `{a_i, a_j} = 0` as exact `8 x 8`
matrix identities (gate `CAR-1`, Section 12). No CAR relation is assumed.

`K` does **not** act inside this algebra as an automorphism of the mode
labels alone: it is antilinear, and it acts on the *label set* by the
transposition `w <-> wbar` together with complex conjugation of coefficients.
That is the entire content of "the doublet is one K-orbit". Note carefully:
**`K` maps `a_w` to `a_wbar`; it does not identify them.** An antilinear map
exchanging two generators is not a relation between them.

---

## 5. Coherent states, the resolution of identity, and the measure

Adjoin Grassmann generators `theta_i`, `thetabar_i` (`i = 1, w, wbar`),
anticommuting with each other and with all `a_i, a_i^dag`. Define

```text
  |theta>  =  prod_i (1 - theta_i a_i^dag) |0>        =>  a_i |theta> = theta_i |theta>
  <theta|  =  <0| prod_i (1 - a_i thetabar_i)         =>  <theta| a_i^dag = <theta| thetabar_i
  <theta|theta'> = exp( sum_i thetabar_i theta'_i ) .
```

**Pinned Berezin convention.** Left Berezin derivative, normalized by
`int d(theta) theta = 1`, differentials written left to right with the
**rightmost acting first**, and measure ordering

```text
  D(thetabar, theta) := d thetabar_n d theta_n  ...  d thetabar_1 d theta_1 .
```

This is the ordering displayed verbatim at
`docs/ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md:33-35`:

```text
integral d(chibar_n)d(chi_n)...d(chibar_1)d(chi_1)
         exp(-sum_ij chibar_i K_ij chi_j)
  = det_C(K).
```

Under this pinned ordering the overall sign is **computed, not chosen**. My
worker probe scanned four orderings against both the left and right Berezin
derivative and found (exact, `n = 1,2,3`):

| derivative | ordering | value / `det_C` |
|---|---|---|
| left | `d th_1 d thb_1 ... d th_n d thb_n` | `(-1)^n` |
| left | `d thb_n d th_n ... d thb_1 d th_1` | `+1` |
| left | `d thb_1 d th_1 ... d thb_n d th_n` | `+1` |
| right | `d th_n d thb_n ... d th_1 d thb_1` | `+1` |

The `(-1)^n` entries are the convention residual; they are a sign, never an
exponent, and they cannot move `r`. All algebra below uses row 2.

**Resolution of identity.** With the pinned measure,

```text
  1_Fock  =  int D(thetabar, theta)  e^{- sum_i thetabar_i theta_i}  |theta><theta| .
```

I verify this **not** by citation but by expanding `|theta><theta|` as an
`8 x 8` matrix of Grassmann elements and performing all 64 Berezin integrals
in a from-scratch exterior-algebra engine; every diagonal entry evaluates to
`1` and every off-diagonal entry to `0` (gate `CAR-2`). The trace formula that
follows is

```text
  Tr O  =  int D(thetabar, theta)  e^{- thetabar . theta}  < -theta | O | theta > .
```

**Gaussian.** For any `n x n` complex `M`,

```text
  int D(thetabar, theta)  exp( - sum_{i,j} thetabar_i M_ij theta_j )  =  det_C(M) .
```

Verified from scratch at `n = 1, 2, 3` with fully generic symbolic `M`
(gate `BZ-1`), by exterior-algebra expansion and nested single-generator
Berezin integration — **no determinant identity is used anywhere in the
engine**.

---

## 6. The decisive question: is the K-conjugate partner an independent
integration variable?

The campaign asks the right question. Here is the derivation of its answer,
with the two candidate readings of "K-conjugate partner" separated, because
conflating them is where the corpus's own equivalence chain breaks.

### 6.1 Reading 1 — the partner *channel* `theta_wbar` inside one field column

The lattice field content is pinned by the realization gate, quoted verbatim
from `docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md:91-94`:

> - **Matter-statistics clause.** The matter measure on the Quantum + Lattice
>   baseline is the finite single-mode Grassmann partition, one pair
>   `(χ_x, χ̄_x)` per site, on the dim-2 per-site Cl(3) module;
>   bosonic second quantization is excluded.

From that clause the derivation is three lines:

1. One independent complex Grassmann pair per **site**. The hw=1 kernel
   triplet is a **3-dimensional subspace** of the (real) lattice function
   space. The field's component along that subspace is the triple
   `theta_mu = <v_mu, chi>`, `mu = 1,2,3`, of **three independent complex
   Grassmann numbers**, with three independent `thetabar_mu`.
2. Passing to the character basis is an invertible **constant** linear change
   `theta_chi = sum_mu (F)_{chi mu} theta_mu`. Independence is preserved:
   `{theta_1, theta_w, theta_wbar}` is again a free generating set. The
   measure changes by the constant Jacobian `det(F)^{-1}`, which cancels
   against the kernel transformation (see the passive-invariance law quoted in
   Section 7.2).
3. Therefore `theta_wbar` is a **generator of the Grassmann algebra distinct
   from `theta_w`**, and `int d thetabar_wbar d theta_wbar` is a genuinely
   separate integration.

**Could a reality condition tie them?** Only by imposing `theta` K-real, i.e.
`theta_mu^* = theta_mu` in the (real) corner basis, hence
`theta_wbar = (theta_w)^*`. Two facts block this on the landed surface:

- The gate clause above supplies an **independent pair** `(chi_x, chibar_x)`,
  not a real (Majorana-type) generator; imposing K-reality is a *different*
  field content, not a reading of this one.
- Even if imposed, it does not produce a 2-slot doublet on a 3-dimensional
  carrier: a single K-real triple has an **odd** number (3) of real Grassmann
  generators, and the Berezin Gaussian of an odd-dimensional antisymmetric
  kernel vanishes identically (`Pf` of a `3 x 3` antisymmetric form is `0`).
  Recovering a nonzero weight requires a *pair* of copies — which is a
  doubling, and Section 7 shows every doubling is r-neutral.

**Answer to Reading 1: the K-conjugate partner channel IS an independent
integration variable.** The measure carries `n = 3` complex modes, 6 Grassmann
generators, one canonical pair per character channel. Antilinearity is the
reason: `K` permutes generator *labels* and conjugates *coefficients*; the
Berezin measure is a top form built from the generators, and a label
permutation is a relabelling of the top form, never a reduction of its degree.

### 6.2 Reading 2 — the barred partner `thetabar` versus `theta`

`thetabar` is independent of `theta` for a **charged** field, and is the
dependent object only under a Majorana condition. Charged leptons carry
electric charge, so on any reading in which the corner carrier is the
charged-lepton generation index, the Majorana identification is unavailable.
This is the `chi/chibar` independence already fixed by the gate clause. It
gives determinant power **one**, not two.

**Answer to Reading 2: also independent; the Gaussian is `det_C`, first
power.** This matches the landed Fact 1 quoted in Section 2 and is *not* new.

---

## 7. What the mode count actually produces — and why it is r-neutral

### 7.1 The two horns, computed

With the pinned measure, one copy on the full carrier gives (gate `BZ-2`,
generic symbolic `(a,b,c)`):

```text
  Z_1 = int D(thetabar,theta) exp( - thetabar W(a,b,c) theta )
      = det_3 = a^3 + b^3 + c^3 - 3abc
      = lam_0 lam_1 lam_2 .
```

Two **disjoint** copies, the second carrying the K-conjugate presentation,
give (gate `BZ-3`, 12 generators, direct symbolic expansion):

```text
  Z_2 = det_3(a,b,c) . det_3(abar,bbar,cbar)
      = |det_3|^2      on the entrywise-real locus.
```

The 12-generator horn is **not** "integrating the partner channel a second
time" — that is impossible, the partner channel is already integrated once
inside `Z_1`. It is **adjoining a second field copy**. This is a field-content
change, exactly as the landed exponent note recorded at
`docs/OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md:52-55`:

> **Adversarial multiplicity (B6):** in the complex-mode realization the
> exponent-2 atom (`a²`) is obtainable *only* by doubling the field content
> (computed: two independent modes → `a²`) — i.e. by changing the
> *realization*, never by a readout choice.

### 7.2 The r-neutrality theorem for copy-doubling

Write the K-orbit product `Omega := lam_1 lam_2` (K-invariant: gate `PT-3`).
Then, exactly:

```text
  Z_m  =  (lam_0 Omega)^m  =  lam_0^m  Omega^m ,    m = 1, 2, 3, ...
```

so the (singlet, doublet-orbit) exponent pair is

```text
  m = 1  (6 generators)  ->  (1,1)
  m = 2  (12 generators) ->  (2,2)
  m = 3  (18 generators) ->  (3,3)
```

verified exactly for `m = 1,2,3` (gate `EX-1`). **Every doublet-to-singlet
exponent ratio equals 1 for every `m`.** The generator-count axis moves the
overall power and nothing else. The same is true of the other doubling
available on this surface — the taste-conjugate square, recorded at
`docs/KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md:66`
as *"the taste square is r-neutral"* and reproven here as
`det_3 -> det_3^2`, channel-uniform (gate `EX-2`).

Two further exactness facts I reproved rather than cited:

- **No constant converts the horns.** There is no scalar `kappa` with
  `kappa . det_3 = det_3^2` identically: the forced values at `(a,b,c) =
  (1,0,0)` and `(2,0,0)` are `1` and `8` (gate `EX-3`).
- **Passive coordinate changes convert nothing.** Consumed verbatim from
  `docs/ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md:102-110`:

  > For an invertible coordinate change `Psi=M Xi`, the kernel becomes
  > `M^T A_K M`. Pfaffians and Berezin measures transform as
  > `Pf(M^T A_K M) = det(M) Pf(A_K)`, `D(Psi) = det(M)^(-1) D(Xi)`
  > for the paired orientation convention. The factors cancel in the Gaussian.

  In particular the corner-basis to character-basis change used in Section 6.1
  step 2 is exactly such a change and is value-preserving.

**Conclusion of Section 7.** `det_C` versus `|det_C|^2` is a real and exactly
computable fork, and I have derived which side the landed measure sits on
(`det_C`, first power, `n = 3` modes). **That fork cannot produce `r = 1/2`
versus `r = 1`.** The campaign's link "det_C grain <=> 2-cell menu" does not
hold.

---

## 8. Where the r-fork actually lives: it is a partition of a different space

This is the sharpest finding and I derive it from scratch.

### 8.1 The dial is coupling data

```text
  r = |b|^2 / a^2 ,    a = coefficient of I ,   b = coefficient of C .
```

`r` is forced into these coordinates by the Koide functional itself, not by
convention: `sum_k lam_k = 3a` and `sum_k lam_k^2 = 3a^2 + 6|b|^2`, so

```text
  Q = (3a^2 + 6|b|^2)/(9a^2) = 1/3 + (2/3) r .
```

The two-sector energy split that the landed dictionary uses is therefore the
**group-element** split of the coupling:

```text
  E_s = || a I ||^2_HS          = 3 a^2
  E_d = || b C + bbar C^2 ||^2_HS = 6 |b|^2        (gate PT-1)
  E_s + E_d = Tr(W_H^dag W_H) = sum_k lam_k^2 .
```

and the dictionary itself is flagged in its own source as a modeling element,
`docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md:359-364`:

> 2. **The energy dictionary.** The identification that a formation state
>    distributes the total channel energy as shares —
>    `E_s = w E_tot`, `E_d = (1-w) E_tot`, against the first-order section
>    fork's channel decomposition `E_s = 3a^2`, `E_d = 6|b|^2` — is **this
>    note's own declared modeling element** (the energy-to-formation-state
>    bridge).

With `E_s = w E_tot`, `E_d = (1-w) E_tot`:

```text
  a^2 = w E_tot / 3 ,     |b|^2 = (1-w) E_tot / 6 ,     r = (1-w)/(2w)
  w = 1/2 -> r = 1/2 ;    w = 1/3 -> r = 1                    (gate PT-2)
```

### 8.2 The Berezin slots are character data

The Gaussian factorizes into one-mode integrals **only in the eigenbasis of
the kernel**, which for a circulant coupling is the character basis:

```text
  Z_1 = prod_{chi} ( int d thetabar_chi d theta_chi  e^{ - thetabar_chi lam_chi theta_chi } )
      = lam_1 . lam_w . lam_wbar .
```

So the canonical "one slot per atom" decomposition supplied by the measure is
indexed by `{chi_1, chi_w, chi_wbar}` — the **character channels**.

### 8.3 The two partitions do not correspond

The character transform `(a,b,c) <-> (lam_0, lam_1, lam_2)` is invertible and
(by Parseval, `sum_k |lam_k|^2 = 3 sum |coeff|^2`) a similitude of the HS
metric. It nonetheless carries **neither** cell menu onto the other:

```text
  coupling cell { a I }        --character-->  (a, a, a)      : meets ALL 3 character cells
  character cell { chi_1 }     --coupling--->  (I+C+C^2)/3    : meets ALL 3 coupling cells
```

both verified exactly (gates `PT-7`, `PT-8`). The two 2-cell menus are
therefore **different partitions of different spaces**, not two names for one
partition. A count of Berezin slots is a statement about the second; `w` is a
statement about the first. There is no arrow between them on the landed
surface — which is precisely the object named at
`docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md:382-384`:

> - **Not** an inference that the tied measure's count-twice analytic grain is
>   itself the formation law. That inference is the missing binding theorem
>   isolated in T4.

### 8.4 And if you force the binding anyway, you get neither horn

Suppose an auditor grants the binding "one formation cell per Berezin slot".
Then the cells are the character channels, the 2-cell menu is
`{chi_1} u {chi_w, chi_wbar}`, and equipartition reads
`lam_0^2 = lam_1^2 + lam_2^2`. At real `b` this is `(a+2b)^2 = 2(a-b)^2`, and

```text
  r = 17/2 - 6 sqrt(2)  ~  0.0147        (and the conjugate root 17/2 + 6 sqrt 2)
```

exactly (gate `PT-6`). That value is already in the landed corpus as the third
competing reading,
`docs/ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:104-108`:

```text
| reading | condition | result |
|---|---|---|
| generator-channel Hilbert-Schmidt | `3a^2 = 6b^2` | `r = 1/2` |
| dimension/per-mode | `a^2 = b^2` | `r = 1` |
| idempotent/eigenvalue | `(a + 2b)^2 = 2(a - b)^2` | `r = 17/2 - 6 sqrt(2)` |
```

**So the Berezin route, even with the missing binding theorem handed to it for
free, lands on the `idempotent/eigenvalue` row — neither horn of the
campaign's binary.** I regard this as the decisive negative of Derivation A.
It is not a claim that `r = 17/2 - 6 sqrt(2)` is physical; it is a claim that
the measure-slot partition is simply not the partition `w` is defined on.

Summary table (all rows exact, all reproven here):

| cell menu | space partitioned | 2-cell equipartition | landed name |
|---|---|---|---|
| `{I} u {C, C^2}` | coupling / group algebra | `r = 1/2` | generator-channel Hilbert-Schmidt |
| real dims of the same | coupling, `(1,2)` weighting | `r = 1` | dimension/per-mode |
| `{chi_1} u {chi_w, chi_wbar}` | fermion one-particle space (= Berezin slots) | `r = 17/2 - 6 sqrt 2` | idempotent/eigenvalue |

---

## 9. The one Berezin object that *does* give count-once — and its obstruction

For completeness I built the object whose exponent pair is genuinely `(1,1)`
in the *doublet-channel* sense: a Grassmann field valued in a **half** of the
carrier,

```text
  V_half := V_1 (+) V_w         (2 complex modes, 4 Grassmann generators)

  Z_half = int D  exp( - thetabar W|_{V_half} theta )  =  lam_0 lam_1     (gate HF-1)
```

This is exactly the "one holomorphic mode" reading named at
`docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md:35`:

> the generation readout count the complex doublet `b` as **one holomorphic mode**

Two derived facts about it, both new here as displayed algebra on the
delivered carrier:

**(H-a) It is not K-covariant.** `Z_half` is not invariant under
`K : b_2 -> -b_2`; instead

```text
  K : Z_half = lam_0 lam_1  |-->  lam_0 lam_2 = Z_half'         (gate HF-3, HF-4)
```

whereas the full 3-mode and doubled 6-mode partition functions **are**
K-invariant (gate `HF-2`). Equivalently, at the projector level,

```text
  P_half := P_1 + P_w ,     K P_half K = P_1 + P_wbar  !=  P_half      (gate KS-3,4)
```

so `V_half` is **not a K-stable subspace** of the delivered carrier, while
`V_R (x) C` is. A half-carrier is therefore not a lattice-delivered subobject;
it must be supplied.

**(H-b) Its orientation is not carrier-selectable.** Which half — `V_w` or
`V_wbar` — is exactly the label that
`docs/KCPT_CORNER_CARRIER_TWO_PRESENTATION_SWAP_PROPER_ROTATION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-07-18.md:124-127`
proves is a lattice-rotation frame choice:

> element of the proper cubic rotation group named by the LATTICE axiom. Thus, on this
> restricted surface, the `w` versus `wbar` label is a rotation-frame orientation at the
> `C_3[111]` axis. A carrier-only tie-breaker invariant under the delivered rotation cannot
> distinguish the two; a larger joint construction may consume additional internal or

I also reproved, on this carrier, that the framework's own native complex
structure cannot do the selecting:

```text
  J_cs = (C - C^2)/sqrt(3) ,   J_cs real antisymmetric,   J_cs^2 = -(I - P_1),
  [J_cs , W_H] = 0 ,
  R(t) = P_1 + cos t (I - P_1) + sin t J_cs  is SO(3),  det R = +1,
  det( R(t) W_H ) = det W_H   for all t                        (gates J-1..J-5)
```

so the `J_cs`-flow is measure-neutral: it defines a holomorphic structure but
preserves every determinant, hence selects no half. This reproduces, from the
carrier rather than by citation, the landed measure-neutrality statement.

**Net.** Count-once is a well-defined Berezin object; it requires a
non-K-stable half-carrier; and no carrier-invariant datum on the delivered
surface picks the half. This is the polarization, restated as an exact
obstruction on the lattice-delivered carrier rather than as an abstract
choice.

---

## 10. Sharpened statement of the circularity, and exactly what would fix it

The campaign asked for a mode count and warned that the honest outcome might
be "a sharpened statement of the circularity". That is the outcome, and here
is the sharpening in one displayed block:

```text
DERIVED (this report):
  measure side   : n = 3 complex modes, 6 generators, det_C, first power.
                   The K-conjugate partner channel is an INDEPENDENT
                   Berezin integration variable.
  doubling axis  : every available doubling (copy, taste) is (m,m) --
                   r-NEUTRAL. det_C vs |det_C|^2 cannot move r.
  half-carrier   : the (1,1) object exists but is not K-stable and its
                   w/wbar orientation is a lattice-rotation frame choice.

NOT DERIVED, and NOT derivable through mode counting:
  the r-dial w lives on a partition of the COUPLING (group-algebra
  coefficients a vs b). Berezin slots live on a partition of the FERMION
  one-particle space (characters). Neither partition maps to the other.
  Forcing "slot = cell" gives r = 17/2 - 6 sqrt 2, neither horn.
```

**What would fix it — exactly three named objects, in decreasing plausibility
as I see them:**

1. **A binding theorem** of the shape `formation weight = F(measure data)` —
   the object the relocation note names as missing. This report *narrows* what
   such a theorem must do: it cannot be a slot count, because slot counts are
   character-indexed and give the third reading. It must be a map from
   character-indexed measure data to **coupling-coefficient** cells, and the
   character transform shows no such map is a restriction or a quotient.
2. **A coupling-dependent structure** on the Grassmann surface. The landed
   Berezin note computes that a coupling-dependent substitution *does* convert
   the horns (`A(W) = W`, `B = I` sends `det_3 -> det_3^2`,
   `docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:257-265`),
   so this class is live but is exactly the class where "derivation" and
   "insertion" are hardest to separate. Flagged, not endorsed.
3. **A selector for the half-carrier `V_1 (+) V_w`.** By (H-a)/(H-b) this must
   consume data outside the carrier — a co-transforming orientation datum or a
   joint (internal x corner) structure. The 2026-07-18 note explicitly leaves
   that door open and explicitly does not walk through it.

I want to be blunt about item 1: my Section 8.3 result makes a *slot-counting*
binding theorem look not merely unlanded but structurally unavailable. That is
the negative I am reporting. It does not forbid a binding theorem of some
other shape, and I make no claim about routes I did not test.

---

## 11. Assumptions, and every uncertainty I did not smooth

**Assumptions used (each named, none hidden):**

- **A-1.** The field content is the gate note's matter-statistics clause
  (Section 6.1 quote): one independent complex Grassmann pair per site. If
  that clause is later read as supplying a real/Majorana generator instead,
  Reading 1 of Section 6 changes; Section 7's r-neutrality does not.
- **A-2.** The corner carrier is the delivered hw=1 kernel triplet with real
  corner plane waves and entrywise `K` (Section 3 quote). The realness of the
  corner basis is load-bearing for `K` existing at all.
- **A-3.** The pinned Berezin ordering of Section 5. The sign residual
  `(-1)^n` is computed both ways and is never used as an exponent.
- **A-4.** The coupling `W_H(a,b)` is a **probe**, not a derived Yukawa. Its
  own source flags this verbatim
  (`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:97-98`:
  "**FLAG — probe, not derived form:** no Yukawa identification, physical
  action, or measure is derived for it, there or here."). Every statement in
  this report inherits that flag. **No physical charged-lepton action is
  derived anywhere here.**
- **A-5.** The energy dictionary `E_s = w E_tot`, `E_d = (1-w) E_tot` is the
  relocation note's declared modeling element (quoted in 8.1). Section 8.4's
  "even if you grant the binding" argument is conditional on it; Sections 6-7
  are not.

**Uncertainties I am deliberately leaving raw:**

- **U-1 (scope hazard, live).** Two different loci carry the phrase
  "count-once form". The spectral-pairing / Berezin lineage works on the
  **entrywise-real** locus `(a,b,c) in R^3`, where `lam_2 = conj(lam_1)` and
  `det_3 = lam_0 |lam_1|^2`. The Koide readout works on the **Hermitian
  section** `a in R, c = bbar`, where all three `lam_k` are real and
  `conj(lam_1) = lam_1 != lam_2`. They intersect only at real `b`. I verified
  both statements exactly (gates `PT-4a..4d`). Any downstream use of
  "`|lam_1|^2`" on the Hermitian section is, as far as I can tell, a scope
  slip. I flag it; I do not claim any specific note commits it, and I did not
  audit the notes for it.
- **U-2.** The "trivial isotype (real singlet `a`)" wording at
  `docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md:31-33`
  names `a` as the trivial isotype, but under the cyclic shift of coefficient
  index the trivial isotype of `(m_0,m_1,m_2)` is spanned by `(1,1,1)`, whose
  coefficient is `lam_0/3`, not `a`. The *arithmetic* everywhere downstream is
  unambiguously the group-element split (`3a^2`, `6|b|^2`), and that split is
  what the Koide moments force (Section 8.1). But the *name* and the *object*
  may not match. This is exactly the ambiguity Section 8.3 turns into a
  theorem, so I record it rather than resolve it.
- **U-3.** I did not test nonlinear or nilpotent-shifted Berezin changes of
  variables. The landed Berezin note names them untested
  (`:300-302`). My r-neutrality result (Section 7.2) is a statement about
  values of `Z_m`, and is untouched by that class; my Section 8 result is
  about partitions and is likewise untouched. But I cannot exclude that some
  generator-dependent Berezinian route does something I have not imagined.
- **U-4.** I worked at fixed lattice spacing, free `U = 1`, and on the corner
  sector only. Gauge dressing, the `U`-integrated measure, and interacting
  extensions are untouched. A coupling that is not circulant would break the
  character factorization of Section 8.2 entirely, and I have no result there.
- **U-5.** I did not attempt Derivation A's question for the taste index or
  for the Dirac L/R doubling as a *joint* structure. On the landed surface
  both are recorded as r-neutral; I reproved the taste square only
  (gate `EX-2`).

**What I deliberately did not re-walk** (campaign rule, foreclosed): the
multiplicative / `AC_phi_lambda` Schur bridge; the delta-pattern leg; and
"chiral => r = 1/2" in its Dirac-chirality sense. Section 9's half-carrier is
*K*-chirality on the internal generation index, which is a different object
from `gamma_5` chirality; I flag the adjacency explicitly rather than assume
the foreclosure does or does not reach it.

---

## 12. Verification — gate design for a runner

The checks below are written as a **specification a runner would implement**.
Everything I ran while writing this report was a **worker probe**, not a gate;
worker probes carry no certification weight. All gates are exact (`sympy`
rationals, radicals and symbols only) — **no floats anywhere**, including in
the mutation controls.

### Block CAR — the algebra, built not assumed

| id | gate | exact assertion |
|---|---|---|
| `CAR-1` | CAR relations | on the `8 x 8` Jordan-Wigner Fock rep, all 9 `{a_i,a_j^dag} - delta_ij I` and all 9 `{a_i,a_j}` are the zero matrix |
| `CAR-2` | resolution of identity | expanding `\|theta><theta\|` as an `8 x 8` matrix of Grassmann elements, all 64 integrals `int D e^{-thetabar.theta} (\|theta><theta\|)_{ij}` equal `delta_ij` |
| `CAR-3` | dimension | `dim Fock = 2^n`; assert `n = 3 => 8` and the grade profile `1,3,3,1` |

### Block BZ — the Berezin engine and the two horns

| id | gate | exact assertion |
|---|---|---|
| `BZ-0` | sign is computed | for `n = 1,2,3` and fully generic symbolic `M`, tabulate value/`det_C(M)` over the four orderings x two derivative conventions of Section 5; assert the pinned row is `+1` for all `n` and the `d th d thb` row is `(-1)^n` |
| `BZ-1` | Gaussian | `int D exp(-thetabar M theta) = det_C(M)` for generic symbolic `M`, `n = 1,2,3`, by exterior expansion and nested single-generator integration, **with no determinant identity available to the engine** |
| `BZ-2` | one copy | `Z_1 = det_3 = a^3+b^3+c^3-3abc = lam_0 lam_1 lam_2`, generic symbolic |
| `BZ-3` | two copies | the direct 12-generator integral equals `det_3(a,b,c) . det_3(ac,bc,cc)`, generic symbolic in all six parameters |

### Block PT — partitions, energies, and the dial

| id | gate | exact assertion |
|---|---|---|
| `PT-0` | carrier | `C^3 = I`, `C^T = C^2`, `C` entries in `{0,1}`; `sum_chi P_chi = I`; `C P_chi = chi P_chi`; `K P_1 K = P_1`, `K P_w K = P_wbar` |
| `PT-1` | group-element split | `Tr((aI)^dag(aI)) = 3a^2`; `Tr(D^dag D) = 6\|b\|^2` for `D = bC + bbar C^2`; sum equals `Tr(W_H^dag W_H) = sum lam_k^2` |
| `PT-2` | dial | solve `3a^2 = w E`, `6\|b\|^2 = (1-w)E` for `a^2, \|b\|^2` **first**, then form the ratio, then compare with `(1-w)/(2w)`; specialize `w = 1/2 -> r = 1/2`, `w = 1/3 -> r = 1`, and `Q = 1/3 + (2/3) r` |
| `PT-3` | orbit invariance | `lam_1 lam_2` invariant under `b_2 -> -b_2`; `lam_1` alone is not |
| `PT-4a..d` | locus separation | on the Hermitian section all `lam_k` real and `conj(lam_1) = lam_1 != lam_2`; on the entrywise-real locus `lam_2 = conj(lam_1)`; the loci intersect exactly at `b_2 = 0` |
| `PT-5` | HS metric | Hessian of `sum lam_k^2` in `(a, b_1, b_2)` is `diag(6,12,12)`, i.e. weights `(3,6,6)` — **not** flat |
| `PT-6` | third reading | solve `lam_0^2 = lam_1^2 + lam_2^2`; assert the exact solution set for `r` is `{17/2 - 6 sqrt 2, 17/2 + 6 sqrt 2}` as **radicals**, and that at `b_2 = 0` the equation is literally `(a+2b)^2 = 2(a-b)^2` |
| `PT-7` | non-correspondence I | the image of `(a,0,0)` under the character map is `(a,a,a)`; assert every character-cell projection of it is nonzero |
| `PT-8` | non-correspondence II | the pullback of `(1,0,0)` in character coordinates is `(I+C+C^2)/3`; assert every group-element coefficient is `1/3 != 0` |

### Block EX — exponent bookkeeping and r-neutrality

| id | gate | exact assertion |
|---|---|---|
| `EX-1` | copy tower | for `m = 1,2,3` there exist integers `(s,d)` with `Z_m = lam_0^s (lam_1 lam_2)^d`, and `(s,d) = (m,m)`; assert `d/s = 1` for all `m` |
| `EX-2` | taste square | `det_3 -> det_3^2` is channel-uniform: the exponent pair goes `(1,1) -> (2,2)` |
| `EX-3` | no constant conversion | assert no `kappa` satisfies `kappa det_3 = det_3^2` identically, by exhibiting the exact clash `kappa = 1` at `(1,0,0)` versus `kappa = 8` at `(2,0,0)` |

### Block HF / KS / J — the half-carrier and the polarization

| id | gate | exact assertion |
|---|---|---|
| `HF-1` | half value | the 2-mode integral on `V_1 (+) V_w` equals `lam_0 lam_1` |
| `HF-2` | K-invariance of the full horns | `Z_1` and `Z_1^2` are invariant under `b_2 -> -b_2` |
| `HF-3` | K-non-invariance of the half | `Z_half(b_2) - Z_half(-b_2) != 0` as a polynomial |
| `HF-4` | K sends half to half | `Z_half(-b_2) = lam_0 lam_2` exactly |
| `HF-5` | no exponent form | assert `lam_0 lam_1` is **not** equal to `lam_0^s (lam_1 lam_2)^d` for any `0 <= s,d <= 4` |
| `KS-3,4` | subspace stability | `K P_half K = P_1 + P_wbar != P_half`; `K I K = I` |
| `J-1..5` | measure neutrality | `J_cs = (C-C^2)/sqrt 3` real antisymmetric; `J_cs^2 = -(I-P_1)`; `[J_cs, W_H] = 0`; `R(t)` orthogonal with `det = +1`; `det(R(t) W_H) = det W_H` for symbolic `t` (use `trigsimp`, assert exact zero) |

### CONSTRUCTION-mutation probes (required by campaign rule 3)

These must **fail** if the construction is wrong, not merely if an assertion is
mistyped. Each mutates the *construction*, re-runs the same gate, and asserts a
**FAIL**.

| id | mutation | gate that must break | why it is decisive |
|---|---|---|---|
| `M-1` | drop `theta_wbar` and `thetabar_wbar` from the generating set (wrong generator count: 4 instead of 6) | `BZ-2` | `Z_1` becomes `lam_0 lam_1`, not `det_3`; catches an undercount of the K-orbit |
| `M-2` | add a spurious fourth channel `theta_4` with kernel entry `1` | `BZ-2`, `CAR-3` | `Z_1` unchanged in value but `dim Fock` becomes `16`; catches a silent overcount |
| `M-3` | replace `K` by **transpose** instead of entrywise conjugation | `PT-0` (`K P_w K = P_wbar`) | transpose fixes each `P_chi`; catches the wrong conjugation rule, which would collapse the K-orbit to two fixed points |
| `M-4` | replace `K` by the **adjoint** (`X -> X^dag`) | `PT-0`, `HF-3` | adjoint is conjugate-transpose; on circulants it agrees with `K` on the Hermitian section but not off it — catches a conjugation rule that is only accidentally right |
| `M-5` | impose `theta_wbar := thetabar_w` (a false reality condition) | `BZ-1` | the kernel becomes antisymmetric on an odd generator count and the Gaussian collapses to `0`; catches the Section 6.1 step-3 claim being asserted rather than derived |
| `M-6` | use the **reversed** measure ordering while keeping the pinned sign claim | `BZ-0` | value picks up `(-1)^n`; catches an unpinned convention masquerading as a result |
| `M-7` | swap the coupling-cell split for the character-cell split in `PT-2` (i.e. use `E_s = lam_0^2`, `E_d = lam_1^2+lam_2^2`) | `PT-2` | `r` moves from `1/2` to `17/2 - 6 sqrt 2`; this is the decisive probe for Section 8 — it shows the partition, not the measure, sets `r` |
| `M-8` | replace the circulant coupling by a generic non-circulant Hermitian `3 x 3` | `PT-3`, `BZ-2` factorization | the character factorization disappears entirely; catches any claim that "channel atoms" are carrier data rather than kernel-symmetry data |
| `M-9` | make the corner basis complex (e.g. `v_1 -> i v_1`) | `PT-0` (`K` well-defined), `KS` block | `K` is no longer entrywise conjugation on the delivered basis; catches assumption A-2 being used silently |
| `M-10` | in `EX-1`, doubling only the **doublet** sector (`lam_0 Omega -> lam_0 Omega^2`) | `EX-1` (`d/s = 1`) | ratio becomes `2`; this is the *only* mutation that moves `r`, and it is not a Berezin operation on this carrier — it is a hand-inserted asymmetry. Its existence is what makes the r-neutrality result meaningful rather than vacuous |

`M-10` is the probe I would most want an adversary to run: it exhibits the
exact shape of an r-moving doubling and shows that no generator-count,
copy-adjunction, taste-square, constant-substitution or passive-coordinate
operation on this surface has that shape.

### Expected scorecard shape

A runner implementing the above should report separate totals for the
**identity gates** and the **mutation controls**, with every mutation control
reported as an expected-FAIL that fired. A run in which any `M-*` passes is a
failed run, not a stronger result.

---

## 13. One-line answer to the assigned question

**`n`, not `2n`: the coherent-state Berezin representation of the landed
corner carrier carries three independent complex modes — one canonical pair
per character channel, six Grassmann generators — and the K-conjugate partner
channel is a genuinely independent integration variable; but this count is
r-neutral, because the `det_C`/`|det_C|^2` axis moves the singlet and doublet
exponents together `(m,m)`, and because `w` partitions the coupling while the
Berezin measure partitions the fermion one-particle space, with no map between
the two partitions.**
