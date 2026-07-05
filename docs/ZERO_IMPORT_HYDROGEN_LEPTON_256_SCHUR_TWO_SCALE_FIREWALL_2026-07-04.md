# Zero-Import Hydrogen: Lepton `1/256` Schur Two-Scale Firewall

**Date:** 2026-07-04
**Type:** partial-narrowing support note with named walls
**Claim type:** meta / bounded route firewall
**Status:** support-only. This note does not promote a retained claim, does not
derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_schur_two_scale_firewall.py`

## Scope

This note attacks Route B from
`ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md`: can the existing
`g^2/64` Schur/leptogenesis-looking surface close the charged-lepton
suppression

```text
y_scale(v) = g_2(v) * (1/sqrt(2)) * S_l,
S_l        = 1/256?
```

This matters for zero-import hydrogen because a retained electron mass is the
first blocker in

```text
E_H = m_e alpha(0)^2.
```

## Exact Arithmetic

The Schur-shaped algebra is exact:

```text
(g/sqrt(2))^2 / 32 = g^2 / 64.
```

The lattice weak-coupling surface gives

```text
g_2^2 |_lattice = 1/4,
g_2^2 |_lattice / 64 = 1/256.
```

That is the positive content: the `/64` route can hit the required
charged-lepton suppression if the suppression slot uses the lattice weak
coupling.

But the charged-lepton scale formula also contains a front factor `g_2(v)`.
If the same Schur expression is evaluated at the weak scale instead of the
lattice scale, the suppression is not `1/256`:

```text
g_2(v)^2 / 64 ~= 0.00656     for bounded g_2(v) = 0.6480,
1/256          = 0.00390625.
```

So the all-weak-scale substitution overshoots the target suppression by
approximately `68%`. With the older cycle-12 benchmark `G_WEAK = 0.653`, the
overshoot is approximately `71%`.

The route therefore needs a two-scale statement:

```text
y_scale(v) = [g_2(v) / sqrt(2)] * [g_2^2 |_lattice / 64].
```

That identity is algebraically the desired lepton-scale target, but the
mixed-scale split is a theorem to derive, not a convention to assume.

## Substitution Tests

| substitution | formula | status |
|---|---|---|
| target mixed-scale split | `[g_2(v)/sqrt(2)] * [(1/4)/64]` | gives the desired `g_2(v)/(sqrt(2)*256)` |
| all weak-scale Schur | `[g_2(v)/sqrt(2)] * [g_2(v)^2/64]` | too large by `g_2(v)^2/(1/4) - 1` |
| all lattice-scale Schur | `[(1/2)/sqrt(2)] * [(1/4)/64]` | too small by replacing the physical front factor with `1/2` |

This is the firewall: Route B is not simply "derive `/64`." It must derive a
protected lattice-normalization suppression while allowing the gauge anchor in
front to run to `g_2(v)`.

## Relation To The Neutrino Schur Surface

`DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md`
already shows that the `g^2/64` algebra is real and has teeth:

```text
y_nu^eff = j^2/m = (g/sqrt(2))^2/32 = g^2/64.
```

However that row is bounded on named admissions:

- ADM-1: physical readout `j = g/sqrt(2)`;
- ADM-2: physical weak coupling `g`;
- ADM-3: graph-shift-to-Dirac-Higgs phi-space transport.

It is also a neutrino-sector statement. A charged-lepton reuse must supply its
own sector bridge and its own two-scale split. The neutrino Schur result is
therefore a high-value template, not a charged-lepton closure.

## Named Residuals For Route B

The `/64` route is reduced to four explicit residuals:

| wall | residual |
|---|---|
| B1 | Charged-lepton Schur carrier: derive a lepton scalar block with second-order return `j^2/m`. |
| B2 | Denominator/readout: derive the charged-lepton analog of `j = g/sqrt(2)` and `m = 32`, or an equivalent `/64` normalization. |
| B3 | Sector identity: prove the resulting Schur coefficient is the charged-lepton suppression `S_l`, not a neutrino/leptogenesis coefficient. |
| B4 | Two-scale split: prove the suppression uses the lattice `g_2^2 = 1/4` while the front factor uses `g_2(v)`, or provide a running law that lands on the same target. |

The precision residual from the lepton `1/256` structural probe remains
separate: the empirical divisor is `256.08`, not exact `256`. A future closure
must either derive the small correction or show why exact `256` receives a
controlled downstream correction.

The A3 precision firewall
`ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md`
pins the target correction for both Route A and Route B:
`C_A3 = 0.999678091...` after exact `256`, or a direct noninteger-divisor
theorem.

## No-Go Discipline Gate

This section applies the no-go discipline to avoid overclaiming the firewall.
The broad claim "the Schur `/64` route cannot close charged leptons" is **not**
shipped. The narrow claim is: the currently documented `g^2/64` handles close
only the exact algebra; charged-lepton use requires B1-B4.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| mixed-scale lattice suppressor | Use `[g_2(v)/sqrt(2)] * [g_2^2|_lattice/64]`. | OPEN and strongest: it gives the target exactly, but B1-B4 must be derived. |
| all weak-scale Schur | Use `[g_2(v)/sqrt(2)] * [g_2(v)^2/64]`. | ATTEMPTED. Arithmetic overshoots the target by about `68%` for bounded `g_2(v)=0.6480`. |
| all lattice-scale Schur | Use `[(1/2)/sqrt(2)] * [(1/4)/64]`. | ATTEMPTED. It loses the physical weak-scale front factor and undershoots the target by about `23%`. |
| neutrino Schur transplant | Reuse `y_nu^eff = g^2/64`. | ATTEMPTED. Exact algebra transfers as a template, but ADM-1/2/3 and sector identity remain unclosed for charged leptons. |
| leptogenesis convention | Reuse `y_0 = g_weak^2/64`. | ATTEMPTED. Same arithmetic as Schur, but convention-to-`S_l` and two-scale split remain unproved. |
| `M_2(C)^tensor4` | Use `4^4 = 256` instead of Schur. | OPEN parallel route; attacks the exponent selector, not the `/64` normalization. |
| empirical `m_W/256` | Use observed `a_lepton^2 ~= m_W/256`. | RULED OUT AS ZERO-IMPORT ROUTE: comparator/open-gate input, not a retained derivation. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| B1 <-> B2 | no in either direction | independent |
| B1 <-> B3 | no in either direction | independent |
| B1 <-> B4 | no in either direction | independent |
| B2 <-> B3 | no in either direction | independent |
| B2 <-> B4 | no in either direction | independent |
| B3 <-> B4 | no in either direction | independent |

Deriving a Schur block does not identify it as the charged-lepton suppression;
deriving `/64` does not prove the two-scale split; proving the split does not
derive the sector carrier.

### N3 - Hidden-wall scan

The potentially hidden phrases are explicit:

| phrase class | classification |
|---|---|
| `lattice` | retained weak-coupling value from the cited `G_WEAK_FROM_FRAMEWORK` surface; not a physical-scale value. |
| `weak scale` | bounded comparator surface for `g_2(v)`, not a retained input to this note. |
| `Schur` | exact algebra template; physical charged-lepton carrier is B1-B3. |
| `mixed-scale` | explicit B4 wall, not assumed. |
| `primitive` | registry checked; approved primitives supply no selector, weighting, normalization, or mass value. |

No hidden admission is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `G_WEAK_FROM_FRAMEWORK_NOTE_2026-05-03.md` | lattice `g_2^2/64 = 1/256` within a convention | partial: supplies arithmetic, not B1/B3/B4 |
| `DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md` | neutrino `g^2/64` Schur assembly bounded on ADM-1/2/3 | partial: template, not charged-lepton sector |
| `DM_NEUTRINO_VSEL_CURVATURE_TASTE_TO_DIRAC_TRANSPORT_OBSTRUCTION_NO_GO_NOTE_2026-06-07.md` | graph-shift-to-Dirac phi-space transport for neutrino ADM-3 | partial: warns about transport, not direct charged-lepton route |
| `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md` | charged-lepton `1/256` structural-vs-fit/exponent question | yes for target and precision residual |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md` | route-level target selection | yes |

Non-matching surfaces are not counted as charged-lepton closure witnesses.

### N5 - Rhetoric audit

The note does not claim "`g^2/64` is not useful" or "no Schur route exists."
It tests three resolutions:

| resolution | tested? | outcome |
|---|---|---|
| exact algebra | yes | `(g/sqrt(2))^2/32 = g^2/64`. |
| scale placement | yes | lattice suppression fits; weak-scale suppression overshoots. |
| charged-lepton sector identity | no closure | named B1/B3 walls. |
| all possible Schur-like operator constructions | no | not claimed closed. |

### N6 - Partial-closure path scan

The primitive registry was checked. The approved scale, kinetic-isotropy, and
realized-state primitives do not supply the needed selector, normalization,
running law, or mass value.

Legitimate partial-closure paths remain:

- derive a charged-lepton Schur carrier with `m=32`;
- prove `/64` is a charged-lepton scalar normalization rather than a
  leptogenesis convention;
- prove the suppression is a lattice-normalized invariant while the front
  gauge anchor runs;
- derive a small correction from exact `256` to the empirical `256.08`.

These are import-retirement paths, not new axioms.

### N7 - Steelman

A hostile reviewer can argue that the mixed-scale split is not suspicious but
exactly what a lattice normalization should do: the discrete scalar
normalization is fixed at the bare lattice surface, while the external gauge
anchor runs to the electroweak scale. On that reading,
`[g_2(v)/sqrt(2)] * [g_2^2|_lattice/64]` is not a hack; it is the natural
renormalized charged-lepton boundary condition. The strongest next move is to
derive that renormalization statement rather than dismiss Route B.

### N8 - Cross-cycle echo

The repo has already seen this pattern in `G_WEAK_FROM_FRAMEWORK`: an apparent
missing phenomenological input became a retained lattice primitive plus a
running residual. The same mechanism may apply here. This note therefore keeps
Route B alive and names B4 as the exact analogue: not "missing 256", but
"derive the lattice-normalized suppression and its physical-scale front
factor."

**Gate result:** broad no-go fails; narrowed two-scale firewall passes. Route B
remains live, but it has four explicit residuals B1-B4.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of a charged-lepton Schur carrier.
- No proof that `S_l = y_nu^eff` or `S_l = y_0_lattice`.
- No derivation of the two-scale split.
- No derivation of the `256.08` correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_schur_two_scale_firewall.py
```

The verifier checks the exact Schur arithmetic, the lattice/weak-scale
substitution split, the named residuals, the no-go discipline section, and the
non-claim boundary.
