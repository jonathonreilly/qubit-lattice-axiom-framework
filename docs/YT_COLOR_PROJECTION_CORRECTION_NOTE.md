# Y_T Color Projection Operator-Map No-Go and Conditional Family

**Date:** 2026-04-15; repaired 2026-05-23; operator-map closure 2026-07-11
**Claim type:** no_go
**Claim scope:** Exact operator-map no-go that the SU(`N_c`) adjoint
projector's dimension fraction, including `8/9` at `N_c = 3`, does not equal
its action on a color-singlet scalar source and does not supply that source's
dynamical two-point/LSZ normalization; broader colored-composite and direct
response routes remain open.
**Type:** no_go proposal for independent audit-lane review.
**Primary runner:** `scripts/frontier_yt_color_projection_correction.py`

## Claim Boundary

This row no longer derives or certifies the package specialization

```text
    y_t(phys) = y_t(Ward) * sqrt(8/9).
```

The cited exact color algebra fixes the channel fractions

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

This family is bookkeeping, not an operator derivation: `kappa_Y` names an
otherwise-unsupplied relative readout coefficient after the adjoint weight has
been normalized to one. It must not be identified with a Hilbert-Schmidt
projection, a connected correlator, or a scalar pole residue unless a separate
matching theorem proves that identification.

The familiar package value

```text
    K_Y(0) = 8/9
```

is therefore the **connected-trace specialization** `kappa_Y = 0`, not a
derived theorem on the current source surface. The full-trace completion

```text
    K_Y(1) = 1
```

is equally compatible with the cited Fierz/channel-count arithmetic.

This note proves the following narrow no-go:

> From the cited exact SU(3) Fierz/channel-count result and
> a color-singlet scalar source, the Yukawa-side connected-trace selector
> `kappa_Y = 0` cannot be derived. The exact `8/9` is the rank fraction of the
> adjoint projector on the *whole color-matrix space*, whereas the same
> projector annihilates the specific color-singlet scalar insertion. A
> connected cumulant does not alter that source direction. Any use of
> `sqrt(8/9)` in the Y_T lane is therefore a conditional specialization until
> a separate dynamical scalar two-point or matching theorem supplies the
> missing map.

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

Only item 1 is an exact algebraic result. Item 2 is the load-bearing
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

### 2. Projector Rank Is Not Projector Action

The Fierz decomposition defines exact Hilbert-Schmidt orthogonal projectors on
`End(C^N_c)`:

```text
    P_1(M)   = Tr(M)/N_c I_color,
    P_adj(M) = M - Tr(M)/N_c I_color.
```

As superoperators, their ranks are

```text
    rank(P_1) = 1,
    rank(P_adj) = N_c^2 - 1.
```

Consequently

```text
    rank(P_adj) / dim End(C^N_c)
      = (N_c^2 - 1)/N_c^2
      = F_adj.
```

This is what the dimension fraction measures. It is a normalized
superoperator trace (equivalently, the mean adjoint projection energy over any
orthonormal basis of the full matrix space). It is not the result of applying
the projector to a specified scalar insertion.

For the color-singlet scalar source, invariance requires

```text
    U^dagger M_phi U = M_phi             for every U in SU(N_c).
```

The fundamental commutant is the scalar line, so `M_phi = c I_color`. Direct
evaluation gives

```text
    P_1(M_phi) = M_phi,
    P_adj(M_phi) = 0,
    ||P_adj(M_phi)||_HS^2 / ||M_phi||_HS^2 = 0.
```

At `N_c = 3`, both statements are simultaneously true:

```text
    rank fraction of the adjoint projector = 8/9,
    adjoint fraction of the specific scalar insertion = 0.
```

Equating them is therefore a category error, not an unfinished arithmetic
step. The first is a property of a projector on an entire operator space; the
second is the projector's action on one vector in that space.

The same fact can be stated representation-theoretically. A color-singlet
scalar source carries the trivial representation, while a traceless color
insertion carries the adjoint. Since

```text
    Hom_SU(N_c)(1, adj) = 0,
```

there is no nonzero SU(`N_c`)-equivariant linear map that turns the scalar
source alone into an adjoint insertion. Supplying an additional colored
carrier or a different source domain would be new matching structure, not a
consequence of channel counting.

### 3. A Connected Cumulant Does Not Change The Source Tangent

Write the color-singlet scalar source matrix as

```text
    J(h) = h I_color.
```

The functional second derivative of `log Z[h]` produces a connected cumulant,
but its inserted color direction remains

```text
    dJ/dh = I_color,
    P_adj(dJ/dh) = 0.
```

Subtracting a vacuum expectation value changes the cumulant topology; it does
not replace the source tangent by a traceless matrix. Thus “connected” in
`<O O>_connected` and “adjoint/traceless” in the Fierz decomposition are
different operations. A theorem identifying them would need a new
source-to-operator map and a dynamical scalar two-point normalization.

### 4. Color-Blind Scaling Cannot Select kappa_Y

If a color-blind scaling factor `z` multiplies both channels, then

```text
    C -> z C,
    S -> z S.
```

The normalized Yukawa readout

```text
    K_Y(kappa_Y) = C + kappa_Y S
```

is not changed in a way that selects `kappa_Y`. The same cited
color-blind scaling data admit at least these two completions:

```text
    Completion A: kappa_Y = 0,  K_Y = 8/9.
    Completion B: kappa_Y = 1,  K_Y = 1.
```

Both completions satisfy the cited Fierz data and the same color-blind
scaling law, but they give different Yukawa corrections. Therefore the
selector is underdetermined by those premises.

### 5. Direct Projection Gives The Opposite Completion

The self-contained projector algebra above gives, for a nonzero Hermitian
color insertion `M_color`,

```text
    rho_singlet(M_color)
      = (|Tr_color M_color|^2 / N_c) / Tr_color(M_color^2).
```

It classifies the two named color insertions exactly:

```text
    M_color = I_color              -> rho_singlet = 1, rho_adjoint = 0,
    M_color = sqrt(2) t^A          -> rho_singlet = 0, rho_adjoint = 1.
```

If a future theorem ties the bookkeeping coefficient to this projection, then
an identity insertion would select `kappa_Y = 1`, giving
`K_Y = 1`, not `K_Y = 8/9`. A traceless adjoint insertion would select
`kappa_Y = 0` if a future theorem identified that as the Yukawa-side color
insertion. This note does not derive that insertion. The direct projection
route therefore points to the full-trace completion, not to the historical
connected-trace specialization.

### 6. Independence Witness

At `N_c = 3`, define two models with identical cited channel data:

```text
    C = 8/9,
    S = 1/9,
    z C and z S under any shared color-blind scaling z.
```

Model A sets `kappa_Y = 0`, so `K_Y = 8/9`.
Model B sets `kappa_Y = 1`, so `K_Y = 1`.

No equation in the cited packet distinguishes A from B. Since A and B agree
on the cited premises and disagree on the claimed correction, the
claimed correction is not derivable from those premises. The projector result
is stronger for the direct scalar-operator reading: it fixes the scalar
insertion to the singlet line and hence does not produce `F_adj` at all.

## No-Go Discipline Gate

**Status:** PASS for the narrow packet-level and color-singlet-source no-go
above. The claim is not a repo-wide impossibility theorem; it says that the
cited Fierz packet plus a scalar source confined to the trivial color
representation does not derive `kappa_Y = 0`.

### N1 - Alternative Route Enumeration

1. **Fierz dimensions route.** Attempt: derive `kappa_Y = 0` from the
   exact `F_adj = 8/9`, `F_singlet = 1/9` channel-count data in
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
   packet contains no same-surface scalar/taste-condensate matching theorem that
   identifies that traceless insertion as the physical Yukawa-side color
   structure. Honesty marker: ATTEMPTED.
6. **Projector-rank route.** Attempt: read the rank fraction of `P_adj` as its
   action on the scalar insertion. Failure: the runner constructs both objects
   independently and finds `rank(P_adj)/N_c^2 = 1-1/N_c^2` while
   `P_adj(I_color)=0`. Honesty marker: ATTEMPTED.
7. **Connected-cumulant route.** Attempt: use VEV subtraction or `log Z`
   differentiation to convert the scalar source into a traceless color
   insertion. Failure: `J(h)=hI_color` has source tangent `I_color` before and
   after connected subtraction. Honesty marker: ATTEMPTED.
8. **Isotropic-ensemble route.** Attempt: realize `F_adj` as the average
   adjoint projection energy over the full matrix space. This average is exact,
   but an isotropic operator-space covariance is an additional premise and the
   physical scalar source is confined to the singlet line. Honesty marker:
   ATTEMPTED.

### N2 - Wall-Independence Audit

The exact color-algebra wall and the dynamical wall are distinct:

1. **Operator-domain wall:** the scalar source is in the singlet line, and no
   nonzero equivariant map `1 -> adj` exists without another colored carrier.
2. **Normalization wall:** a scalar LSZ factor is a dynamical two-point/pole
   normalization for a specified source. The Fierz projector rank supplies no
   such kernel or residue.

A future positive theorem must either derive a new source/matching domain that
escapes the first wall and then close the second, or bypass the adjoint route
and compute the physical scalar response directly.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| operator-domain wall / normalization wall | no: a permitted source does not compute its residue | no: a residue for the singlet source does not create an adjoint source map | yes |

### N3 - Hidden-Wall Scan

Phrases such as "physical Yukawa-side readout," "color-blind scaling,"
"connected cumulant," and "connected-trace specialization" are not used as
derived inputs. They name different operations whose proposed identification
is being tested. The hidden admissions found by the scan are precisely an
unsupplied source-to-color-matrix matching map and an unsupplied dynamical
scalar two-point normalization.

The required phrase scan gives:

| Phrase family | Hit | Classification |
|---|---|---|
| `we assume`, `by construction`, `as is standard`, `naturally`, `obviously`, `standard QFT` | none | no hidden premise |
| `the framework provides`, `bridge context`, `background`, `registered` | none | no hidden premise |
| `canonical` | canonical LSZ normalization in N6 | explicit open positive target, not proof input |

### N4 - Residual Matching

The Fierz note attacks the channel-count residual, not the Yukawa selector or
scalar-residue residual. This note constructs the Fierz projectors again to
test the missing bridge itself. The operator-map result matches the quoted
residual exactly: a projector's normalized rank cannot be substituted for its
action on the physical scalar source, still less for a dynamical LSZ residue.

No prior no-go is load-bearing for the new result:

| Prior surface | Residual attacked there | Residual tested here | Exact match? | Use here |
|---|---|---|---|---|
| `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md` | exact singlet/adjoint decomposition and dimensions | rank-versus-action map | input only, not a prior no-go | one-hop algebra authority |
| `YT_SCALAR_TASTE_CONDENSATE_SELECTOR_NO_GO_NOTE_2026-05-23.md` | direct one-Higgs identity insertion cannot be nonzero traceless | rank fraction cannot become scalar LSZ residue | partial subroute only | non-load-bearing echo |
| `EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md` | EW-current physical matching coefficient | Yukawa scalar matching coefficient | no | analogy only |
| `YT_CONNECTED_SOURCE_SELECTOR_SCALAR_LIFT_NO_GO_NOTE_2026-05-29.md` | color-matrix source quotient does not lift to scalar `h` source | scalar source tangent stays on `I_color` | same domain mismatch, different theorem | non-load-bearing echo |
| `YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md` | pole purity leaves absolute scalar normalization free | channel rank does not supply scalar residue | same normalization wall, different shortcut | non-load-bearing echo |

### N5 - Rhetoric Audit

The negative phrase "cannot be derived" is restricted to the cited exact
packet plus a scalar source in the trivial color representation. The note does
not claim that no lattice-wide, colored-composite, dynamical two-point, or
future matching route can determine a scalar normalization. Those broader
resolutions are explicitly left open.

| Resolution | Tested statement | Disposition |
|---|---|---|
| color-matrix element / source tangent | `P_adj(I_color)=0` and the invariant traceless subspace is zero-dimensional | proved exactly for `N_c=2,3,4,5`; algebraic proof covers every `N_c>=2` |
| local source coordinate | `J(h)=hI_color` retains tangent `I_color` under VEV/connected subtraction | proved at the declared source-map level |
| momentum mode / lattice block / lattice-wide dynamics | interacting operator mixing and scalar pole residues | not tested and explicitly excluded |

Accordingly the no-go is about the declared source map and the forbidden
rank-to-residue substitution, not about every dynamical resolution.

### N6 - Partial-Closure Path Scan

The legitimate closure paths are visible and are not classified as new
axioms:

1. derive a same-surface dynamical scalar two-point kernel and canonical LSZ
   residue for the actual singlet source, accepting whatever normalization it
   produces rather than inserting `8/9`;
2. derive a new SU(3)-equivariant source/matching construction with additional
   colored carriers whose singlet composite has a calculable disconnected
   coefficient;
3. bypass `kappa_Y` through a direct physical response or top-correlator
   theorem.

There is also a convention reframe that does not count as new physics: before
a canonical scalar field normalization is supplied, a constant factor can be
moved between the scalar field and its Yukawa coefficient. In that situation
`K_Y` is bookkeeping, while a field-redefinition-invariant amplitude is the
proper target. This reframe does not derive `sqrt(8/9)`; it prevents an unfixed
field coordinate from being presented as a physical prediction.

If such a theorem lands, this no-go must be re-audited rather than treated as
permanent.

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

A hostile reviewer could argue that interactions make the scalar two-point
kernel sample adjoint virtual states even though the external source is a
singlet. That can happen dynamically and is not excluded here. It still does
not make the result equal to the adjoint *dimension fraction*: the required
kernel, weights, momentum dependence, and normalization must be calculated.
The no-go rejects only the substitution of channel rank for that calculation.

### N8 - Cross-Cycle Echo

The closest echoes are the EW-side matching-rule open gate, the one-Higgs
identity-insertion obstruction, the scalar connected-source domain mismatch,
and the pole-row normalization freedom. The new result does not merely repeat
them: it identifies their common algebraic core as rank-versus-action and
source-domain mismatch. A future dynamical source theorem can still retire the
normalization wall.

| Echo | Later retirement mechanism found? | Applicability here |
|---|---|---|
| EW matching-rule gate | no physical coefficient theorem found on the current source surface | same need for a source-specific matching calculation |
| scalar identity-insertion route | no; alternative matching rules remain open | incorporated as the direct-source boundary, not globalized |
| connected-source scalar lift | no; a new color-matrix source authority would be required | same possible escape, explicitly left open |
| pole-row normalization freedom | canonical operator/LSZ theorem or physical response could retire it | carried forward as the exact positive target |
| normalization conventions elsewhere in the repo | some numeric walls were retired as vacuous field/coupling rescalings | applied here only to demote unfixed `K_Y`; it does not produce the desired factor |

## Consequences For The Y_T Lane

Safe wording:

> The Y_T color-projection lane has an exact Fierz core and a
> conditional Yukawa readout family
> `K_Y(kappa_Y) = 8/9 + kappa_Y/9`. The package value `sqrt(8/9)` is the
> connected-trace specialization `kappa_Y = 0`, not a derived physical
> matching theorem. On the direct color-singlet scalar-source interpretation,
> the adjoint projector annihilates the insertion rather than returning its
> `8/9` rank fraction.

Unsafe wording: treating the `sqrt(8/9)` package value as a derived physical
top-Yukawa correction rather than as a conditional connected-trace
specialization.

This repair does not close the full top-Yukawa derivation. It prevents the
old Class-F definition-as-derivation pattern from propagating and leaves a
precise remaining target:

```text
derive kappa_Y = 0 from a matching theorem not already blocked by
the color-singlet scalar operator-map obstruction; or compute the
same-surface dynamical scalar two-point/LSZ normalization directly,
without substituting the adjoint projector rank for that calculation.
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
- a dynamical scalar two-point function or LSZ residue;
- any PDG numerical comparator.

The older numerical tables are intentionally removed from the load-bearing
claim. Comparator agreement after choosing `kappa_Y = 0` is not evidence that
the selector has been derived.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_yt_color_projection_correction.py
```

The SHA-pinned paired output is
[`logs/runner-cache/frontier_yt_color_projection_correction.txt`](../logs/runner-cache/frontier_yt_color_projection_correction.txt).

The runner checks exact rational arithmetic for the corrected conditional
family, the two-completion independence witness, and color-blind-scaling
invariance. Independently of the dimension formula, it constructs the
singlet/adjoint projectors over exact rational matrix units for
`N_c = 2, 3, 4, 5`, computes their ranks by Gaussian elimination, checks
`P_adj(I_color) = 0`, solves the invariant and invariant-traceless commutant
dimensions, and verifies that the connected scalar source tangent stays on
the identity line. It also verifies that this source note does not reintroduce
the old unconditional `sqrt(8/9)` claim or the stale reversed
singlet/adjoint parameterization.
