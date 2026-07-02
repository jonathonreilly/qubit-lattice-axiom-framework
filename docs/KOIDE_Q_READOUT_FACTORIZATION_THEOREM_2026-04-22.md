# Koide Q Readout Factorization Theorem

**Date:** 2026-04-22
**Claim type:** bounded_theorem
**Status:** exact support theorem on the admitted first-live second-order
readout grammar; not a closure theorem
**Purpose:** replace the weakest remaining phrase in the second-order `Q` route

> the selector should live on the second-order returned operator

with the strongest exact quotient statement currently available on the retained
`Γ_1 / T_1` grammar.

**Primary runner:** `scripts/frontier_koide_q_readout_factorization_theorem.py`

---

## Audit scope

This note has been narrowed in response to an auditor verdict
(`audit_status=audited_conditional`, `claim_type=positive_theorem`,
`scope_too_broad`).

**Auditor's repair target (verbatim):**

> scope_too_broad: split out the exact rank/kernel quotient as the clean
> bounded theorem, or add a theorem and runner check proving that local
> bosonic first-live species-resolving C3-covariant admissibility forces
> constancy on span(e_z).

**2026-06-17 repair:** this note now takes the second auditor-approved
repair route for the first-live grammar. Sections 1-2 retain the exact
rank/kernel quotient of the linear map `L : R^4 -> Diag_3(R)`. Section 3 adds
the separate theorem-and-runner check that first-live operational
admissibility forces constancy on `span(e_z)`.

The repair is intentionally local. "First-live" is used in its operational
readout sense: two weight packages are equivalent for a first-live selector
when they have the same returned species operator
`P_{T_1} Gamma_1 W Gamma_1 P_{T_1}`. Therefore any scalar selector admitted
inside this first-live readout grammar must factor through the returned
operator `L(W) = diag(u,v,w)`. Since `span(e_z) = ker L`, kernel constancy is a
theorem of the admitted first-live grammar, not an additional physical
carrier-identification assumption.

This does **not** prove that the physical charged-lepton selector must belong
to this first-live class, does not identify the reduced two-block determinant
carrier as the physical charged-lepton carrier, and does not fix the separate
`D_red = I_2` response-unit normalization.

---

## 1. Exact map

On the retained charged-lepton readout grammar, define the second-order map

```text
L(W) = P_{T_1} Γ_1 W Γ_1 P_{T_1}
```

on the four reachable/intermediate-state weight slots

```text
W = u P_{O_0} + v P_{(1,1,0)} + w P_{(1,0,1)} + z P_{(0,1,1)}.
```

The exact single-slot images are

```text
P_{T_1} Γ_1 P_{O_0} Γ_1 P_{T_1}     = diag(1,0,0)
P_{T_1} Γ_1 P_{(1,1,0)} Γ_1 P_{T_1} = diag(0,1,0)
P_{T_1} Γ_1 P_{(1,0,1)} Γ_1 P_{T_1} = diag(0,0,1)
P_{T_1} Γ_1 P_{(0,1,1)} Γ_1 P_{T_1} = 0.
```

So the readout map is exactly

```text
L(u,v,w,z) = diag(u,v,w).
```

---

## 2. Quotient theorem (bounded)

The map `L : R^4 -> Diag_3(R)` has:

- rank `3`,
- kernel `span{(0,0,0,1)}`,
- image equal to the full diagonal species space.

Therefore

```text
R^4 / span(e_unreach)  ≅  Diag_3(R),
```

and two weight packages have the same first-live returned operator if and only
if they differ only in the unreachable slot `z`.

This is the clean bounded theorem of the note: the exact rank/kernel quotient
of the linear readout map `L` on the retained `Γ_1 / T_1` grammar. It is a
purely linear-algebraic statement about `L`, independent of any selector
admissibility hypothesis.

---

## 3. First-live kernel-invariance theorem (bounded repair)

Within the admitted first-live readout grammar:

- local,
- bosonic/even in `Γ_1`,
- first-live on `T_1`,
- species-resolving,
- `C_3`-covariant,

the operational first-live object is the returned species operator

```text
R_{Γ_1}(W) = diag(u,v,w).
```

So any scalar selector `S` admitted inside this first-live grammar factors as

```text
S(W) = Phi(R_{Gamma_1}(W)) = Phi(L(W))
```

for some scalar `Phi` on `Diag_3(R)`. If two weight packages differ by the
unreachable slot,

```text
W' = W + lambda e_z,
```

then

```text
L(W') = L(W),
```

because `e_z` spans `ker L`. Therefore

```text
S(W') = Phi(L(W')) = Phi(L(W)) = S(W).
```

This proves constancy on `span(e_z)` for every selector admitted in the
first-live readout grammar. The companion runner checks this theorem directly:
it verifies the exact kernel, the quotient fibers, the `C_3` intertwining on
the returned operator, and symbolic invariance of an arbitrary
returned-operator scalar under unreachable-slot shifts.

The exact species Fourier transport then sends that returned operator to the
Koide carrier `H_cyc`, and the cyclic quadratic scalar sector reduces to the
same two-slot carrier `(E_+, E_perp)`.

Thus the old identification language inside the admitted first-live
second-order class is upgraded to an exact statement:

```text
admitted first-live selector = scalar on the exact second-order returned
operator
```

It is exact only inside the admitted first-live grammar. A selector that
depends directly on the unreachable coordinate `z` is not a counterexample to
this theorem; it is simply not first-live, because it distinguishes two weight
packages with the same returned species operator.

---

## 4. Honest scope

### What this note claims (bounded theorem)

1. on the first-live second-order readout grammar, the linear readout map
   `L : R^4 -> Diag_3(R)` has rank `3`, kernel `span{e_z}`, and image equal
   to the full diagonal species space;
2. equivalently, the unreachable slot `z` is the entire kernel of `L`, and
   `R^4 / span(e_z) ≅ Diag_3(R)`.
3. inside the admitted first-live readout grammar, every scalar selector
   factors through `L`, hence every such selector is constant on `span(e_z)`.

### What this note does not claim

1. it does not claim that every formally writable scalar on the four-slot
   weight vector is first-live; a `z`-sensitive scalar is excluded precisely
   because it distinguishes equal returned operators;
2. it does not claim a universal statement about all possible higher-order or
   nonlocal carriers;
3. it does not touch the separate `delta` bridge;
4. it does not rewrite authority surfaces;
5. it does not by itself prove that the physical charged-lepton selector must
   belong to this admitted first-live class;
6. it does not identify the reduced two-block determinant carrier as the
   physical charged-lepton carrier or fix the `D_red = I_2` normalization.

---

## 5. Bottom line

The strongest clean **bounded** statement for review is:

> on the retained `Γ_1 / T_1` grammar, the exact second-order readout map
> `L : R^4 -> Diag_3(R)` has rank `3` and kernel `span{e_z}`, so
> `R^4 / span(e_z) ≅ Diag_3(R)`; moreover, any scalar selector admitted as
> first-live factors through this returned operator and is therefore constant
> on `span(e_z)`.

That closes the previously conditional kernel-invariance substep inside the
admitted first-live readout grammar. The remaining open issue beyond this
statement is still the physical identification of the second-order `Q` route,
including the separate source-free and `D_red = I_2` normalization bridges.
