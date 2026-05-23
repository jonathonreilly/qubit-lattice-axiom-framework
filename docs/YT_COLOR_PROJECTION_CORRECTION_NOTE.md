# Y_T Color Projection Matching No-Go and Conditional Family

**Date:** 2026-04-15; repaired 2026-05-23
**Claim type:** no_go
**Type:** no_go proposal for independent audit-lane review.
**Primary runner:** `scripts/frontier_yt_color_projection_correction.py`

## Claim Boundary

This row no longer derives or certifies the package specialization

```text
    y_t(phys) = y_t(Ward) * sqrt(8/9).
```

The retained color algebra fixes the exact channel fractions

```text
    F_adj = (N_c^2 - 1) / N_c^2,
    F_singlet = 1 / N_c^2,
```

so at `N_c = 3`,

```text
    F_adj = 8/9,    F_singlet = 1/9.
```

It does **not** fix the physical Yukawa-side readout coefficient selecting
how much of the singlet/disconnected color channel is included in the
physical scalar normalization. The corrected conditional family is

```text
    K_Y(kappa_Y) = F_adj + kappa_Y * F_singlet
                 = 8/9 + kappa_Y/9        at N_c = 3,

    y_t(phys; kappa_Y) = y_t(Ward) * sqrt(K_Y(kappa_Y)).
```

The familiar package value

```text
    K_Y(0) = 8/9
```

is therefore the **connected-trace specialization** `kappa_Y = 0`, not a
derived theorem on the current retained surface. The full-trace completion

```text
    K_Y(1) = 1
```

is equally compatible with the retained Fierz/channel-count arithmetic.

This note proposes the following no-go:

> From the currently retained SU(3) Fierz/channel-count theorem, the
> retained Hilbert-Schmidt color-projection lemma, and color-blind CMT-style
> scaling alone, the Yukawa-side connected-trace selector `kappa_Y = 0`
> cannot be derived. Any use of `sqrt(8/9)` in the Y_T lane is a conditional
> specialization until a separate scalar/taste-condensate matching theorem
> derives that selector from framework operators.

## Cited Authorities

Load-bearing one-hop authority:

- [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  supplies the exact SU(`N_c`) decomposition
  `N_c \otimes \bar N_c = 1 \oplus adj` and the exact dimension fraction
  `F_adj = (N_c^2 - 1) / N_c^2`.

Plain-text context, not load-bearing authority for this no-go:
`RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`
for the exact Hilbert-Schmidt color-projection guardrail,
`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md` for the analogous
EW-side underdetermination no-go, `YT_WARD_IDENTITY_DERIVATION_THEOREM.md`,
`YT_EW_COLOR_PROJECTION_THEOREM.md`, `YUKAWA_COLOR_PROJECTION_THEOREM.md`,
`RCONN_DERIVED_NOTE.md`, and the older UV-to-IR Y_T transport notes.

## What Was Wrong Before

The old positive framing mixed three distinct statements:

1. The exact representation-theory fact `F_adj = 8/9`.
2. The physical scalar/readout assertion that the Yukawa vertex should use
   only the connected/traceless channel, i.e. `kappa_Y = 0`.
3. The numerical observation that applying `sqrt(8/9)` moves downstream
   comparator values closer to the accepted top-mass region.

Only item 1 is a retained algebraic theorem. Item 2 is the load-bearing
bridge, and item 3 is a comparator check. The prior row also carried an
internal parameterization conflict: one subsection used the connected-trace
form repaired here, while another inverted the singlet and adjoint weights.
The repaired row uses the connected-trace form throughout, because it is the
one for which the historical package value is the specialization
`kappa_Y = 0`.

## Proof of Underdetermination

### 1. Fierz Fixes Dimensions, Not The Physical Readout

The Fierz/channel-count theorem fixes only the decomposition

```text
    N_c \otimes \bar N_c = 1 \oplus adj
```

and therefore the normalized channel sizes

```text
    C = F_adj = (N_c^2 - 1) / N_c^2,
    S = F_singlet = 1 / N_c^2,
    C + S = 1.
```

It does not say whether the physical scalar normalization should read `C`,
`C + S`, or `C + kappa_Y S`.

### 2. Color-Blind Scaling Cannot Select kappa_Y

If a color-blind scaling factor `z` multiplies both channels, then

```text
    C -> z C,
    S -> z S.
```

The normalized Yukawa readout

```text
    K_Y(kappa_Y) = C + kappa_Y S
```

is not changed in a way that selects `kappa_Y`. The same retained
color-blind scaling data admit at least these two completions:

```text
    Completion A: kappa_Y = 0,  K_Y = 8/9.
    Completion B: kappa_Y = 1,  K_Y = 1.
```

Both completions satisfy the retained Fierz data and the same color-blind
scaling law, but they give different Yukawa corrections. Therefore the
selector is underdetermined by those premises.

### 3. The Retained Vertex Projection Lemma Does Not Rescue sqrt(8/9)

The retained Hilbert-Schmidt projection lemma gives, for a color insertion
`M_color`,

```text
    rho_singlet(M_color)
      = (|Tr_color M_color|^2 / N_c) / Tr_color(M_color^2).
```

It classifies the two named color insertions exactly:

```text
    M_color = I_color              -> rho_singlet = 1, rho_adjoint = 0,
    M_color = sqrt(2) t^A          -> rho_singlet = 0, rho_adjoint = 1.
```

If a future theorem ties the Yukawa-side readout coefficient to this
projection, then a color-blind physical Yukawa vertex `I_color` selects
`kappa_Y = 1`, giving `K_Y = 1`, not `K_Y = 8/9`. A traceless adjoint
insertion selects `kappa_Y = 0`, but that is not the color structure of a
color-singlet Higgs Yukawa vertex. The projection lemma therefore supplies
an exact guardrail, not a derivation of the historical package factor.

### 4. Independence Witness

At `N_c = 3`, define two models with identical retained primitive data:

```text
    C = 8/9,
    S = 1/9,
    z C and z S under any shared color-blind scaling z.
```

Model A sets `kappa_Y = 0`, so `K_Y = 8/9`.
Model B sets `kappa_Y = 1`, so `K_Y = 1`.

No retained equation in the cited packet distinguishes A from B. Since A and
B agree on the retained premises and disagree on the claimed correction, the
claimed correction is not derivable from those premises.

## Consequences For The Y_T Lane

Safe wording:

> The Y_T color-projection lane has an exact retained Fierz core and a
> conditional Yukawa readout family
> `K_Y(kappa_Y) = 8/9 + kappa_Y/9`. The package value `sqrt(8/9)` is the
> connected-trace specialization `kappa_Y = 0`, not an audit-clean physical
> matching theorem.

Unsafe wording: treating the `sqrt(8/9)` package value as a derived physical
top-Yukawa correction rather than as a conditional connected-trace
specialization.

This repair does not close the full top-Yukawa derivation. It prevents the
old Class-F definition-as-derivation pattern from propagating and leaves a
precise remaining target:

```text
derive kappa_Y = 0 from the scalar/taste-condensate operator,
the SU(3) lattice two-point function, canonical field normalization,
and the physical color structure of the Higgs Yukawa vertex.
```

If that future theorem lands, this no-go should be re-audited against the
new dependency. Until then, the `sqrt(8/9)` row is not a derived theorem;
it is conditional support only.

## Out Of Scope

This note does not derive:

- the Ward identity or `y_t/g_s = 1/sqrt(6)`;
- a staggered-fermion top correlator mass measurement;
- the physical `v = 246 GeV` input;
- SM RGE running or MSbar-to-pole conversion;
- `kappa_Y = 0`;
- any PDG numerical comparator.

The older numerical tables are intentionally removed from the load-bearing
claim. Comparator agreement after choosing `kappa_Y = 0` is not evidence that
the selector has been derived.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_yt_color_projection_correction.py
```

The runner checks exact rational arithmetic for the corrected conditional
family, the two-completion independence witness, the color-blind-scaling
invariance, and the vertex-projection guardrail. It also verifies that this
source note does not reintroduce the old unconditional `sqrt(8/9)` claim or
the stale reversed singlet/adjoint parameterization.
