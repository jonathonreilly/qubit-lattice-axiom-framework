# Y_T Source-Higgs Pole-Row Normalization No-Go

**Date:** 2026-05-23
**Claim type:** no_go
**Type:** no_go proposal for independent audit-lane review.
**Primary runner:** `scripts/frontier_yt_source_higgs_pole_row_normalization_no_go.py`

## Claim Boundary

This note proves a narrow negative boundary for PR230's source-Higgs pole-row
route:

> Strict `C_ss/C_sH/C_HH` single-pole rows and the Gram-purity identity
> `Res(C_sH)^2 = Res(C_ss) Res(C_HH)` can certify common-pole support, but
> they cannot by themselves select the absolute scalar/source normalization,
> and therefore cannot by themselves derive the Yukawa-side selector
> `kappa_Y = 0` or close positive Y_T.

The result is not a global no-go for Y_T. It only rules out one proposed
shortcut: using pole-row purity alone as the missing normalization bridge.
A future theorem can still close this route by deriving canonical `O_H`,
canonical scalar LSZ normalization, and same-surface source/action authority
from the current Cl(3)/Z^3 substrate.

## Cited Context

Load-bearing algebra in this note is self-contained. The following repo
surfaces are context for the target and the remaining open gates:

- [`YT_PR230_CONSOLIDATED_STATUS_NOTE_2026-05-22.md`](YT_PR230_CONSOLIDATED_STATUS_NOTE_2026-05-22.md)
  records the current minimum PR230 support packet and lists the remaining
  gates: same-surface source/action authority, canonical `O_H`, scalar LSZ
  normalization, strict pole rows or W/Z bypass, and matching/running.
- [`YT_COLOR_PROJECTION_CORRECTION_NOTE.md`](YT_COLOR_PROJECTION_CORRECTION_NOTE.md)
  records the current `K_Y(kappa_Y) = 8/9 + kappa_Y/9` family and the fact
  that `kappa_Y = 0` is not selected by retained Fierz/channel-count data.
- [`OBSERVABLE_PRINCIPLE_SCALE_INVARIANT_SOURCE_RESPONSE_NARROW_THEOREM_NOTE_2026-05-16.md`](OBSERVABLE_PRINCIPLE_SCALE_INVARIANT_SOURCE_RESPONSE_NARROW_THEOREM_NOTE_2026-05-16.md)
  is a useful analogy: normalized source-response ratios can cancel an
  overall source scale. This note applies the same scale-invariance warning
  to pole-row residue purity.

These context notes are not used to derive the no-go. The no-go follows from
the elementary pole-residue algebra below.

## Pole-Row Algebra

Assume the desired strict source-Higgs row has a single dominant state with
mass `m` and positive pole amplitudes `A_s`, `A_H`:

```text
C_ss(t) = A_s^2 exp(-m t),
C_sH(t) = A_s A_H exp(-m t),
C_HH(t) = A_H^2 exp(-m t).
```

Then the Gram-purity identity is exact:

```text
Res(C_sH)^2 = Res(C_ss) Res(C_HH).
```

This identity is valuable: it shows that the source operator and the Higgs
candidate overlap the same one-particle pole in the tested model class.
However, it does not fix the normalization of either operator. Under the
field/source rescaling

```text
s -> mu s,
H -> lambda H,
```

the residues transform as

```text
Res(C_ss) -> mu^2 Res(C_ss),
Res(C_sH) -> mu lambda Res(C_sH),
Res(C_HH) -> lambda^2 Res(C_HH).
```

The Gram-purity determinant remains zero:

```text
(mu lambda Res(C_sH))^2
  = (mu^2 Res(C_ss)) (lambda^2 Res(C_HH)).
```

The pole mass extracted from the time ratio is also unchanged:

```text
C(t) / C(t + 1) = exp(m).
```

Thus common-pole purity and mass extraction are invariant under the same
operator-normalization freedom that an absolute Yukawa readout would need to
fix.

## kappa_Y Ambiguity

The repaired color-projection family is

```text
K_Y(kappa_Y) = 8/9 + kappa_Y/9.
```

Two completions remain algebraically distinct:

```text
connected trace:  kappa_Y = 0,  K_Y = 8/9,
full trace:       kappa_Y = 1,  K_Y = 1.
```

The ratio between these two squared normalizations is

```text
K_Y(1) / K_Y(0) = 9/8.
```

But a Higgs/source normalization rescaling with `lambda^2 = 9/8` absorbs this
exact factor in the pole residues while preserving both pole mass and
Gram purity. Therefore pole-row evidence alone cannot distinguish the
connected-trace specialization from the full-trace completion. Selecting
`kappa_Y = 0` still requires an independent canonical-normalization theorem,
not merely cleaner pole rows.

## Consequence For PR230

Strict `C_ss/C_sH/C_HH` rows are still useful evidence. They can support:

1. same-pole overlap between the source operator and a Higgs candidate;
2. finite-volume and model-class checks for the source-Higgs bridge;
3. mass extraction on the tested surface.

They cannot support:

1. absolute scalar LSZ normalization;
2. `kappa_Y = 0`;
3. `sqrt(8/9)` as an unconditional Y_T correction;
4. positive Y_T closure.

The next positive target is therefore sharper: derive canonical `O_H` and
canonical scalar LSZ normalization on the same accepted source/action surface.
Once that normalization is supplied, strict pole rows can become useful
supporting evidence rather than a substitute for the missing theorem.

## No-Go Discipline Gate

**Status:** PASS for the narrow pole-row-normalization no-go above. This is
not a no-go against direct top correlator measurement, W/Z physical-response
bypasses, source/action admission routes, canonical `O_H` routes, or a future
same-surface LSZ theorem.

### N1 - Alternative Route Enumeration

1. **Gram-purity route.** Attempt: use
   `Res(C_sH)^2 = Res(C_ss) Res(C_HH)` to prove source-Higgs identity.
   Failure: the identity is invariant under `H -> lambda H` and `s -> mu s`.
   It proves common-pole rank one, not absolute normalization.
2. **Mass-extraction route.** Attempt: use the common exponential decay to fix
   the Yukawa coupling. Failure: the effective mass is amplitude-blind.
3. **Residue-ratio route.** Attempt: use `Res(C_sH)/sqrt(Res(C_ss) Res(C_HH))`.
   Failure: for a rank-one pole this ratio is exactly one after normalization,
   independent of the absolute operator scale.
4. **kappa_Y absorption route.** Attempt: compare `K_Y(0)=8/9` with `K_Y(1)=1`.
   Failure: their ratio is absorbed by the unfixed scalar normalization
   `lambda^2 = 9/8`.

### N2 - Wall-Independence Audit

The live wall is canonical normalization, not data quality in the pole row.
Better statistics, lower finite-volume error, or cleaner Gram purity do not
remove the `lambda` freedom. A future positive theorem must close the
canonical `O_H`/LSZ normalization wall directly or use an independent physical
response that fixes the same scale.

### N3 - Hidden-Wall Scan

Terms such as "common pole," "strict pole row," and "Gram purity" are not used
as synonyms for "canonical scalar normalization." The note keeps those roles
separate.

### N4 - Residual Matching

This no-go matches the remaining PR230 residual identified in the consolidated
status note: source-Higgs pole rows or a W/Z bypass are still open only after
canonical source/action and scalar normalization are supplied. The result does
not duplicate the color-projection no-go, which concerns Fierz/channel-count
underdetermination; it shows that pole rows alone do not repair that
underdetermination.

### N5 - Rhetoric Audit

Negative wording is restricted to "pole-row purity alone cannot select
absolute normalization." The note does not say Y_T cannot be derived.

### N6 - Partial-Closure Path Scan

The positive closure path remains visible:

```text
accepted same-surface source/action
  + canonical O_H
  + canonical scalar LSZ normalization
  + strict pole-row support or W/Z response
  -> possible Y_T retained-proposal route.
```

This packet only prevents treating the third item as a replacement for the
first two.

## Firewalls

This packet does not use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed
top/Yukawa targets, `alpha_LM`, plaquette/u0, package-v, Planck, alpha_s, or a
fitted selector as load-bearing input. It does not pre-promote downstream
Y_T, EW, or top-mass claims.

## Verification

```text
python3 scripts/frontier_yt_source_higgs_pole_row_normalization_no_go.py
```

Expected result:

```text
RESULT: PASS=50 FAIL=0
```

The green result means the no-go algebra and overclaim guards are internally
consistent. It does not mean positive Y_T closure has been obtained.
