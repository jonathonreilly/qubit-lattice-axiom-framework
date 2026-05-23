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

> From the currently retained SU(3) Fierz/channel-count theorem and
> color-blind scaling alone, the Yukawa-side connected-trace selector
> `kappa_Y = 0` cannot be derived. Any use of `sqrt(8/9)` in the Y_T lane is
> a conditional specialization until a separate scalar/taste-condensate
> matching theorem derives that selector from framework operators.

## Cited Authorities

Load-bearing one-hop authority:

- [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  supplies the exact SU(`N_c`) decomposition
  `N_c \otimes \bar N_c = 1 \oplus adj` and the exact dimension fraction
  `F_adj = (N_c^2 - 1) / N_c^2`.

Plain-text context, not load-bearing authority for this no-go:
`RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`
for a non-load-bearing projection guardrail,
`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md` for the analogous
EW-side underdetermination pattern, `YT_WARD_IDENTITY_DERIVATION_THEOREM.md`,
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

### 3. Non-Load-Bearing Projection Guardrail Does Not Supply The Selector

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
projection, then an identity insertion would select `kappa_Y = 1`, giving
`K_Y = 1`, not `K_Y = 8/9`. A traceless adjoint insertion would select
`kappa_Y = 0` if a future theorem identified that as the Yukawa-side color
insertion. This note does not derive that insertion. This paragraph is a
contextual guardrail only; the load-bearing no-go proof above uses the Fierz
channel fractions and the two-completion witness.

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

## No-Go Discipline Gate

**Status:** PASS for the narrow packet-level no-go above. The claim is not a
repo-wide impossibility theorem; it is only the statement that the cited
retained packet does not derive `kappa_Y = 0`.

### N1 - Alternative Route Enumeration

1. **Fierz dimensions route.** Attempt: derive `kappa_Y = 0` from the
   retained `F_adj = 8/9`, `F_singlet = 1/9` channel-count data in
   `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`. Failure:
   those data are shared by the `kappa_Y = 0` and `kappa_Y = 1`
   completions above. Honesty marker: ATTEMPTED.
2. **Color-blind normalization route.** Attempt: use a shared scalar or CMT
   normalization factor to select the connected channel. Failure: any shared
   factor multiplies `F_adj` and `F_singlet` together and cancels from the
   normalized family `K_Y(kappa_Y)`. Honesty marker: ATTEMPTED.
3. **Projection-identity route.** Attempt: identify `kappa_Y` with the
   Hilbert-Schmidt singlet projection discussed in the non-load-bearing
   context note
   `RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`.
   Failure: that route classifies insertions but still does not derive which
   insertion is the physical Yukawa readout. Honesty marker: ATTEMPTED.
4. **Identity-insertion route.** Attempt: use the color-blind identity
   insertion as the Yukawa vertex. Failure: under the projection guardrail
   this gives `kappa_Y = 1` and `K_Y = 1`, not the historical package value
   `K_Y = 8/9`. Honesty marker: ATTEMPTED.
5. **Traceless-insertion route.** Attempt: take a traceless adjoint insertion
   so the projection guardrail gives `kappa_Y = 0`. Failure: the current
   packet contains no retained scalar/taste-condensate matching theorem that
   identifies that traceless insertion as the physical Yukawa-side color
   structure. Honesty marker: ATTEMPTED.

### N2 - Wall-Independence Audit

The collapsed wall set has one load-bearing wall: a retained theorem deriving
the physical Yukawa-side selector `kappa_Y = 0`. The apparent subwalls
"physical color insertion," "scalar/taste-condensate matching," and
"canonical field normalization" are not independent in this no-go; any future
positive theorem must close them together or state their residuals separately.

### N3 - Hidden-Wall Scan

Phrases such as "physical Yukawa-side readout," "color-blind scaling," and
"connected-trace specialization" are not used as derived inputs. They name
the missing selector family and the tested completions. The only hidden
admission found by the scan is exactly the collapsed wall above:
`kappa_Y = 0` has no retained derivation in the cited packet.

### N4 - Residual Matching

The Fierz note attacks the channel-count residual, not the Yukawa selector
residual. The projection context attacks the identity/traceless projection
residual, not the Yukawa selector residual. This no-go therefore does not
cite either source as a prior no-go witness. It uses the Fierz theorem as the
load-bearing positive algebraic input and shows that the cited channel data
leave `kappa_Y = 0` underdetermined.

### N5 - Rhetoric Audit

The negative phrase "cannot be derived" is restricted to the cited retained
packet and to the scalar readout coefficient `kappa_Y`. The note does not
claim that no lattice-wide, condensate, two-point-function, or future
operator route can derive the selector. Those broader resolutions are
explicitly left as the next positive target.

### N6 - Partial-Closure Path Scan

The legitimate closure path is visible and not classified as a new axiom:
derive `kappa_Y = 0` from the scalar/taste-condensate operator, the SU(3)
lattice two-point function, canonical field normalization, and the physical
Yukawa-side color insertion. If that theorem lands, this no-go must be
re-audited rather than treated as permanent.

Non-load-bearing follow-up route test:
`YT_SCALAR_TASTE_CONDENSATE_SELECTOR_NO_GO_NOTE_2026-05-23.md`
shows that the most direct one-Higgs scalar/taste-condensate selector route
does **not** close this path: the color-singlet scalar insertion is
proportional to `I_color`, while `kappa_Y = 0` would require a nonzero
traceless color insertion. This narrows the legitimate closure path further:
it must derive a different matching rule for `kappa_Y`, or a different
framework-native scalar insertion, rather than silently equating connected
scalar fluctuation with traceless color insertion.

### N7 - Steelman

A hostile reviewer could argue that a color-singlet Higgs Yukawa vertex or a
connected-correlator prescription should force the connected trace and hence
`kappa_Y = 0`. That route is plausible enough to be the next science target,
but it is not present in the cited retained packet. The current note therefore
does not reject that route; it only prevents the route from being silently
imported.

### N8 - Cross-Cycle Echo

The closest echo is the EW-side matching-rule open gate: exact channel
algebra did not by itself select the physical matching coefficient. That
prior pattern supports narrowing this row to packet-level underdetermination,
not declaring a permanent no-go. The same import-retirement mechanism could
apply here if a future source theorem derives the selector.

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
derive kappa_Y = 0 from a matching theorem not already blocked by
the color-singlet scalar/taste identity-insertion no-go, or replace
the scalar insertion with a framework-native nonzero traceless color
structure without leaving the physical one-Higgs top-Yukawa target.
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
