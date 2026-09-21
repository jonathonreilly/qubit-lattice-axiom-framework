# odds-field-additive-sources, attempt 3 of 4 — the additivity clause was removed on purpose

Worker `w-jonathonsmac4f50-j38d3` (`claude-opus-5`), unit `J-derive-odds-field-additive-sources:a3`.

**Provenance.** No prior attempt existed on this problem at claim time. Two inputs come from
elsewhere and are **same model family** (`claude-opus-5`), not independent: block 42's linearized
results as the unit states them (the operator, `m² = (1−6l₁)/l₁`, the massless surface, the
executed `r·v(r) ≈ 0.28–0.30`), and the pinned-set capacity identity `c = M⁻¹1`, which I derived
yesterday in `J:derive:persistent-sources:a3` (issue #8543) and reuse here rather than re-deriving.

## 1. What is claimed

### (a) Every route is a boundary value, and additivity was deliberately deleted

I read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full. It supplies exactly one channel by which a
site's neighbours affect it — Admissibility:

> "for each site, the probability distribution over the possibilities is **determined by, and
> varies with, the nearest-neighbor conditions**."

That is **conditioning**. It fixes a value; it does not contribute a term. The enumeration the
unit asks for is short, and every entry lands on the same side:

| route | verdict |
|---|---|
| the record's locked content, as its neighbour's condition | **boundary value** |
| its bare occupancy, content unread, as a condition | **boundary value** |
| its own distribution — a record *has* none, it is locked | collapses to the first |
| an unformed neighbour's distribution as a condition (the reading under test) | still a condition — and by Record the field is **unreadable**, so not an observable |

And the decisive point is in the memo itself, twice:

> "Finite additivity, a named scalar collection functional `I`, and an assigned value `I(empty)=0`
> are **not** Record axiom content."
>
> "The 2026-08-13 owner-approved revision **removed** the named scalar functional `I`, finite
> additivity over disjoint record collections, and `I(empty)=0` from Record."

with such rows required to "likewise cite a separate retained authority or remain
conditional/open".

> **Answer to (a): there is no reading available from axiom content alone in which a record is an
> additive source.** The clause that would have licensed summing contributions from disjoint
> records was in the axiom set until 2026-08-13 and was deliberately taken out. An additive source
> is therefore downstream content needing its own retained authority — which is precisely the
> status the gravity lane cannot assume.

### (b) The additivity criterion is exact

For two records at separation `d`, the pinned-set solve gives `C₂ = 2/(G(0)+G(d))` against
`C₁ = 1/G(0)`, so

```
C₂ / (2 C₁)  =  G(0) / (G(0) + G(d))        exactly,
```

and **capacities add to within 10 % exactly when `G(d)/G(0) ≤ 1/9`**. This is a criterion, not a
fit. Exact Fraction capacities at `m² = 5` (the `(2,1,2)` triple):

| d | L=5 | L=6 | L=7 | `G(d)/G(0)` at L=7 |
|---|---|---|---|---|
| 1 | 0.909840 | 0.909946 | 0.909959 | 0.098951 |
| 2 | 0.988835 | 0.989795 | 0.989902 | 0.010201 |
| 3 | — | 0.997822 | 0.998790 | 0.001212 |

So on a screened triple **even adjacent records already add to within 10 %** — `0.098951` sits just
under `1/9 = 0.1111`. The three tori agree to five decimals and converge monotonically in `L`.

The reason is that screening is short on every stable triple: `1/m = 0.447` at `(2,1,2)`, `0.707`
at `(3,1,3)`, `0.775` at `(5,2,4)`, `0.816` at `(7,3,5)` — all **under one lattice spacing**.

For an `N³` array the capacity is strictly below `N³C₁`: `0.968` of it at `N=2`, `0.955` at `N=3`
(L=7, spacing 2), with the charges running `9.7237 … 10.0371` — outer records carrying more. That
gradient **is** the shielding.

### (c) The crossover, and what it costs the gravity lane

A dilute body of spacing `d` and size `D` holds `(D/d)³` records, so additive strength would be
`(D/d)³c₁`; but records that fix the odds at their sites are a **conductor**, whose massless
capacity grows like its linear size `κD`. Equating:

```
D* = sqrt(κ) · d^{3/2} / sqrt(c₁)
```

— the form the unit expects. Past `D*` a body's charge saturates at its capacity and **stops being
proportional to the matter in it**. A `1/r` law between two large bodies would read
`C(D₁)C(D₂)/r` with each `C` growing like a *linear size*, not a mass. No choice of scale repairs
that; the saturation is geometric.

**On the massless surface it is worse**, and that is the case the lane cares about: `(3,1,2)` sits
exactly on `5p = 7q + 4r`, `m = 0`, no screening, `G(d)/G(0)` falling only like `1/d` — so the
exact criterion `≤ 1/9` is not met at any separation a lattice body offers.

## 2. The steps

1. **CHECKED (`A1`).** Six exact-text assertions against the axiom memo, including both sentences
   recording the removal of finite additivity.
2. **PROVED + CHECKED (`A2`).** `1 − 6l₁` has numerator `7q + 4r − 5p`, so `m² = 0` exactly on
   `5p = 7q + 4r`; `(3,1,2)` is on it; four stable triples with `m²` and screening length.
3. **CHECKED (`A3`).** Green functions by **cubic-group orbit reduction** — one equation per orbit
   (20 unknowns at L=7 instead of 343) — **validated against the full 125-site solve at L=5**, six
   displacements agreeing as exact rationals.
4. **PROVED + CHECKED (`A4`).** The `C₂/(2C₁) = G(0)/(G(0)+G(d))` identity verified against the
   solve at every `d`, on all three tori.
5. **CHECKED (`A5`).** Sub-additivity of `N³` arrays and the charge gradient.
6. **PROVED (`A6`).** `D*` solved symbolically.

## 3. Where this stops

- **The massless case is argued, not computed.** On a torus `m = 0` makes the operator singular on
  the constant mode, so the exact-Fraction machinery here cannot run at `(3,1,2)`. I rely on the
  unit's own executed `r·v(r) ≈ 0.28–0.30`, and everything I say about the massless surface
  inherits that. A finite-volume treatment with a compensating background is the obvious fix and I
  did not do it.
- **`κ` is not computed.** `D*` is exact *given* that a conductor's capacity grows like `κD`; I
  neither derive `κ` for this lattice operator nor verify the linear-size law numerically. Bodies
  large enough to test it do not fit in a torus of side 5–7.
- **(b) is answered for screened triples only**, where the answer turns out to be "essentially any
  separation". The interesting regime — long range, near the massless surface — is exactly where
  the torus is too small and the operator degenerates.
- **The `N³` arrays are tiny** (8 and 27 records) and two of the three configurations tile the
  torus, which removes the boundary entirely. Only `L=7, N=3` has both an interior and an outside.
- **(a) is a reading of the axiom text, not a theorem.** I claim the memo licenses no additive
  source; someone could argue a fifth route I did not enumerate. The four I list are the ones the
  text's own vocabulary ("conditions", "locks", "readable") admits.

## 4. What would finish it

1. The massless case properly: fix the zero mode with a uniform background and redo the exact
   capacities at `(3,1,2)`. That is the configuration the gravity lane actually needs, and it is
   the one this attempt could not compute.
2. Compute `κ` — the capacity of a solid lattice cube of side `D` — and check `C ∝ D` directly.
   That turns `D*` from a scaling into a number.
3. Decide whether the gravity lane wants to register an additive source as an approved primitive.
   §(a) says it cannot be derived from the axioms as they stand; the memo's own procedure for that
   is a retained derivation, a bridge, or explicit approved-primitive registration.
4. Another model family on all of it: the capacity identity in §(b) is reused from my own work of
   yesterday.

## 5. Running it

```
python3 probes/work/derive/odds-field-additive-sources/w-jonathonsmac4f50-j38d3/check.py
```

`sympy` only; 31 checks, exact rational arithmetic throughout; runs in a few seconds.

**A performance note worth recording:** the first version of this script took over 43 minutes and
had to be killed. The cause was `sympy.nsimplify` applied to values that were *already* exact
rationals — it hunts for closed forms and effectively hangs. Replacing it with `sympy.Rational`
took the same computation to 0.02 s. The orbit reduction (343 → 20 unknowns) is what makes L=7
affordable at all; both are in the script.
