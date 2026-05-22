# Quark Bimodule NORM-Existence Theorem

**Date:** 2026-04-19 (2026-05-19: audit-conditional repair — bridge-family
and retained-constant inputs declared as explicit admitted imports;
retained scope narrowed to the **conditional algebraic lift** of an
already-admitted bridge family `a_u(kappa)` onto complementary
real-linear endomorphisms of the admitted one-real channel `I`).
**Lane:** Quark up-amplitude / bimodule LO closure
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-19 narrowing):** the **retained** content of
this note is a **valid algebraic lift conditional on the admitted
bridge family + admitted carrier + admitted retained constants**. Given
the admitted carrier `I = R * Im(p)`, the admitted retained scalars
(`p`, `rho = 1/sqrt(42)`, `sin_d = sqrt(5/6)`, `supp = 6/7`, `delta_A1
= 1/42`), and the admitted one-parameter bridge family `a_u(kappa) =
sin_d * (1 - rho*kappa)` for `kappa ∈ [sqrt(6/7), 1]` (all imported
from the same-day endpoint-obstruction lane and the upstream CKM
retained packet), the note proves the **purely algebraic fact** that
the scalar pair `D_kappa := rho*kappa * Id_I`, `U_kappa := (1 -
rho*kappa) * Id_I` defines complementary real-linear endomorphisms of
the one-real channel `I` whose evaluation on `Im(p)` reproduces the
admitted bridge amplitudes. This is **explicitly NOT** an axiom-first
existence theorem for an LO split law on the bimodule; it is a
**conditional algebraic lift** of an already-admitted bridge family.
**Status:** bounded conditional algebraic-lift theorem on the current
branch; this does not yet select the physical
law uniquely, but, **conditional on the admitted bridge-family /
carrier / retained-constant inputs**, it resolves the binary residue
"does an LO split law exist on the bimodule given the admitted bridge
family?" with a clean **yes**
**Primary runner:** `scripts/frontier_quark_bimodule_norm_existence_theorem.py`

---

## 2026-05-19 audit-conditional repair: admitted-context block + conditional-lift retain

This section is the load-bearing repair record. It does not change any
algebraic content of the chain below, the runner output, or any
runner-checked numerical equality. It tightens the language so that
three previously-implicit load-bearing imports are **explicit admitted
context**, and locks the retained scope to the **conditional
algebraic lift** the runner actually verifies.

### Admitted-context block (explicit imports)

The following are **not derived in this note**. They are imported as
admitted context from the surrounding quark / CKM lanes and are
flagged explicitly here so no reader can mistake them for results
retained by this note's restricted packet:

- **Admitted import I-1 (carrier).** The one-real imaginary channel
  `I := R * Im(p)` of the CKM `1 (+) 5` bimodule — i.e. the carrier on
  which `D_kappa` and `U_kappa` live as real-linear endomorphisms — is
  **imported** from the upstream CKM retained packet. The derivation
  of this carrier from primitives (sole axiom + retained-grade inputs)
  is NOT performed inside this note. In particular, the identification
  of `I` with the load-bearing one-real channel of the bimodule is
  taken as data.
- **Admitted import I-2 (retained scalar atoms).** The retained quark
  atoms

  ```text
  p = cos_d + i sin_d,    |p|^2 = 1,
  r = rho + i eta = p / sqrt(7),
  rho = 1 / sqrt(42),
  sin_d = sqrt(5/6),
  supp = 6/7,
  delta_A1 = 1/42
  ```

  are **imported** as admitted retained constants from the upstream
  retained CKM packet. They are used here as data; no first-principles
  derivation of any of them is offered in the present note.
- **Admitted import I-3 (bridge family).** The exact one-parameter
  bridge family

  ```text
  a_u(kappa) = sin_d * (1 - rho * kappa),   kappa ∈ [sqrt(6/7), 1],
  ```

  together with its three distinguished exact points
  `kappa_support = sqrt(6/7)`, `kappa_target = 48/49`, `kappa_BICAC =
  1`, is **imported** from the same-day endpoint-obstruction theorem
  (`docs/QUARK_BICAC_ENDPOINT_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`,
  audit row `quark_bicac_endpoint_obstruction_theorem_note_2026-04-19`).
  The present note does NOT regenerate the bridge family from
  primitives; it consumes it as data.

### Conditional-lift retain (exactly what stays retained)

The retained content of this note is exactly the following
**conditional algebraic lift**, verified by the registered runner
`scripts/frontier_quark_bimodule_norm_existence_theorem.py`:

> **Theorem (conditional algebraic lift on `I`).** Assume the admitted
> imports I-1 (carrier `I = R * Im(p)`), I-2 (retained scalar atoms),
> and I-3 (bridge family `a_u(kappa)` on `kappa ∈ [sqrt(6/7), 1]`).
> Then for every retained `kappa` in that interval, the scalar pair
>
> ```text
> D_kappa := rho * kappa * Id_I,
> U_kappa := (1 - rho * kappa) * Id_I
> ```
>
> defines complementary real-linear endomorphisms of `I` —
> `U_kappa + D_kappa = Id_I`, positive contractions on the retained
> interval — whose evaluation on `Im(p)` reproduces the admitted
> bridge amplitudes `U_kappa(Im(p)) = a_u(kappa)`. In particular, the
> support, target, and BICAC points all realize **conditional**
> bimodule split maps on `I`.

This statement is **purely finite-dimensional linear algebra on the
admitted one-real channel** `I`. It is conditional on the admitted
imports I-1, I-2, I-3 and does NOT purport to derive an LO split law
on the bimodule from axiom-first primitives.

### Out-of-binding-scope (explicitly not retained)

The following readings of the same algebra are explicitly **not**
retained by this note:

- any claim that the present note independently derives the carrier
  `I` from primitives;
- any claim that the present note derives the bridge family
  `a_u(kappa)` from primitives (that family is imported from the
  endpoint-obstruction lane);
- any claim that the existence of complementary scalars `D_kappa`,
  `U_kappa` on `I` constitutes an **axiom-first** existence theorem
  for an LO split law on the bimodule — the existence shown is
  **conditional on the three admitted imports** above;
- any reading that promotes "conditional algebraic lift on `I`" to
  "uniqueness / canonicalization of the LO split law on the
  bimodule"; the latter is the open positive target (see §5).

### Honest scope-narrow audit trail

This 2026-05-19 repair is honest narrowing only. It (a) makes admitted
imports I-1 (carrier), I-2 (retained scalar atoms), and I-3 (bridge
family) explicit in the boundary block, (b) restricts the **retained**
content of the note to the conditional algebraic lift the runner
verifies, and (c) preserves the prior chain text below unchanged for
audit-trail continuity. It does NOT change any algebraic content,
runner output, or runner-checked equality. The source-side
`claim_type` is narrowed to `bounded_theorem` because the live claim is
conditional on admitted imports I-1, I-2, and I-3; the independent
audit lane owns the refreshed `audit_status`.

---

## 0. Executive summary

*(Note: per the 2026-05-19 audit-conditional repair above, all
constructions in this summary are **conditional on the admitted
imports I-1 (carrier `I`), I-2 (retained scalar atoms), and I-3
(bridge family `a_u(kappa)`)**. The summary below is preserved
unchanged for audit-trail continuity but should be read against the
admitted-context block.)*

Let

```text
I := R * Im(p)
```

be the one-real imaginary channel on the retained CKM projector ray
`p = cos_d + i sin_d`, with `|p|^2 = 1` and retained scalar claim

```text
a_d = rho = Re(r) = 1 / sqrt(42).
```

For this branch, call a real-linear ownership-response map on the normalized
channel `I` a **NORM law**.

The exact bridge family already on the branch,

```text
a_u(kappa) = Im(p) * (1 - rho * kappa),
kappa in [sqrt(6/7), 1],
```

lifts directly to actual complementary endomorphisms of `I`:

```text
D_kappa(x) = rho * kappa * x,
U_kappa(x) = (1 - rho * kappa) * x.
```

Here `D_kappa` is the down-sector share and `U_kappa` is the up-sector share.
They satisfy

```text
U_kappa + D_kappa = Id_I
```

for every retained `kappa`, and applying `U_kappa` to `Im(p)` reproduces the
exact quark bridge amplitudes.

So the open quark residue is no longer:

> "does any LO split law exist on the bimodule?"

It is now the sharper question:

> which NORM law on the bimodule is canonical, natural, or retained-physics
> selected?

---

## 1. Setup

Retained quark atoms:

```text
p = cos_d + i sin_d,      |p|^2 = 1,
r = rho + i eta = p / sqrt(7),
rho = 1 / sqrt(42),
sin_d = sqrt(5/6),
supp = 6/7,
delta_A1 = 1/42.
```

The same-day endpoint-obstruction theorem already proved that the quark packet
carries the exact one-parameter bridge family

```text
a_u(kappa) = sin_d * (1 - rho * kappa),
```

with three distinguished exact points:

```text
kappa_support = sqrt(6/7),
kappa_target  = 48/49,
kappa_BICAC   = 1.
```

The present note asks a different question: do those bridge amplitudes
correspond to actual bimodule split maps on the retained imaginary channel?

---

## 2. The theorem

Because `I = R * Im(p)` is one-real-dimensional, every real-linear
endomorphism of `I` is multiplication by a scalar.

For any retained `kappa in [sqrt(6/7), 1]`, define

```text
D_kappa := rho * kappa * Id_I,
U_kappa := (1 - rho * kappa) * Id_I.
```

Then:

1. `D_kappa, U_kappa in End_R(I)` are well-defined real-linear maps;
2. they are complementary:

   ```text
   U_kappa + D_kappa = Id_I;
   ```

3. they are positive contractions on the physical interval because
   `0 <= rho * kappa <= rho < 1`;
4. evaluating on `Im(p)` reproduces the exact bridge family:

   ```text
   U_kappa(Im(p)) = Im(p) * (1 - rho * kappa) = a_u(kappa).
   ```

### Formal statement

> **Theorem (NORM existence on the quark bimodule — conditional algebraic
> lift form, 2026-05-19 narrowing).** Assume the admitted imports I-1
> (carrier `I = R * Im(p)` of the CKM `1 (+) 5` bimodule), I-2
> (retained scalar atoms), and I-3 (bridge family `a_u(kappa)` on
> `kappa ∈ [sqrt(6/7), 1]`). Then every retained bridge factor `kappa
> ∈ [sqrt(6/7), 1]` determines a real complementary split law on `I`
>
> ```text
> D_kappa(x) = rho * kappa * x,
> U_kappa(x) = (1 - rho * kappa) * x.
> ```
>
> In particular, the support, target, and BICAC points are all
> realized as **conditional** LO bimodule split maps on `I` —
> conditional on the admitted imports I-1, I-2, I-3.

So the binary existence question, **read in its conditional-lift
form**, has the answer **yes**. The note does NOT promote this to an
axiom-first existence theorem; the existence is conditional on the
admitted imports declared in the 2026-05-19 audit-conditional repair
block above.

---

## 3. Distinguished exact laws

### 3.1 Support law

At

```text
kappa_support = sqrt(supp) = sqrt(6/7),
```

the up map gives

```text
U_support(Im(p))
= sin_d * (1 - rho * sqrt(6/7))
= sin_d * (1 - 1/7)
= sin_d * 6/7
= sin_d * supp.
```

### 3.2 Retained target law

At

```text
kappa_target = 1 - supp * delta_A1 = 48/49,
```

the up map gives

```text
U_target(Im(p)) = sin_d * (1 - 48 rho / 49) = 0.7748865611...
```

which is the retained preferred target already present in the RPSR packet.

### 3.3 BICAC law

At

```text
kappa_BICAC = 1,
```

the split law becomes

```text
D_BICAC(x) = rho x,
U_BICAC(x) = (1-rho) x.
```

Evaluating on `Im(p)` gives

```text
a_u = sin_d * (1-rho),
```

hence

```text
a_u + rho * sin_d = sin_d,
```

which is exactly STRC-LO / BICAC.

---

## 4. Scientific consequence

This theorem does **not** yet choose the physical endpoint. The same-day
endpoint-obstruction theorem remains fully in force: the current retained
packet does not derive `kappa = 1`.

What changes is the shape of the residue.

Before this note, a fair question was:

> perhaps the quark packet does not even define a genuine LO split law on the
> bimodule.

After this note, that possibility is gone. The branch now knows that:

1. the retained bridge interval lifts to honest complementary bimodule maps on
   the one-real imaginary channel;
2. the three exact bridge points are not just scalar formulas, but actual
   endomorphism laws on `I`;
3. the remaining issue is **canonicalization**, not existence.

That is the precise role of this theorem.

---

## 5. Relation to what remains

The next same-day strengthening is the NORM-naturality theorem:

- `docs/QUARK_BIMODULE_NORM_NATURALITY_THEOREM_NOTE_2026-04-19.md`
- `scripts/frontier_quark_bimodule_norm_naturality_theorem.py`

That theorem shows that if one asks for a normalized affine extension of the
split law across the full ownership interval `a in [0,1]`, then BICAC is the
unique such extension.

So the open quark gap is now bracketed exactly:

- **NORM existence:** yes;
- **endpoint uniqueness from retained packet alone:** no;
- **unique normalized affine extension:** yes, but only after adding the
  naturality requirement.

---

## 6. Runner summary

The companion runner verifies:

- the retained interval is nonempty;
- support / target / BICAC all lie in it;
- each `D_kappa, U_kappa` is real-linear on `I`;
- complementarity `U_kappa + D_kappa = Id_I`;
- positivity / contractivity on the retained interval;
- exact recovery of the bridge amplitudes;
- exact support endpoint, exact target value, and exact BICAC closure.

Expected runner status:

```text
PASS=10
FAIL=0
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [quark_bicac_endpoint_obstruction_theorem_note_2026-04-19](QUARK_BICAC_ENDPOINT_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md)
