# Quark Route-2 c_TE Magnitude Structural Status Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded structural-status probe and open-theorem sharpening.
**Status authority:** independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.
**Primary runner:** scripts/quark_route2_cte_magnitude_structural_status_bounded_2026_06_12.py
**Runner cache:** logs/runner-cache/quark_route2_cte_magnitude_structural_status_bounded_2026_06_12.txt

No literature values, external citations, fitted comparator numbers, live
endpoint values, new axioms, new primitive declarations, or physical
`kappa_EW` weighting rules are used. The calculation uses exact rational
arithmetic and repo-internal notes only. Existing declared inputs are restated
or demoted to declared context; no status outcome is asserted here.

Context pointer, not an authority link: scripts/runner_cache.py.

## One-Hop Authorities

- [W77_NOTE.md](../.claude/tmp/refs/W77_NOTE.md) for the one-parameter
  positive E-row residual, the separated sign result, and the statement that
  the magnitude target remains open.
- [W67_NOTE.md](../.claude/tmp/refs/W67_NOTE.md) for the typed-bridge
  obstruction: `F_adj` is not by itself a Route-2 center readout, and the
  E-center lift `q_E = 15/8` is not supplied by the Fierz fraction.
- [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) for the exact
  `F_adj = (N_c^2 - 1)/N_c^2` support and the connected-trace/readout
  boundary.
- [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md)
  for the Record/Quantum boundary separating channel count from physical
  weighting/readout.
- [EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  for the exact SU(`N_c`) Fierz channel decomposition and adjoint dimension
  fraction.
- [CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md](CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md)
  for the singlet-projector and `3 x 3bar = 1 + 8` complement form of the same
  SU(3) singlet-adjoint split.
- [YT_P3_MSBAR_TO_POLE_K3_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md](YT_P3_MSBAR_TO_POLE_K3_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md)
  for the repo-internal declared exact SU(3) color-Casimir product
  `C_F^2 T_F = 8/9`. Only that exact color-algebra line is used; its loop
  integrals, comparator values, and transport context are not used.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) and
  [axiom_premise_nodes.json](audit/data/axiom_premise_nodes.json) for the
  boundary that Record supplies no readout context, weighting, normalization,
  probability rule, or physical observable bridge, and for the check that the
  approved primitive registry does not declare a Route-2 magnitude selector.

## Quote Anchors

W77 gives the reduced residual and sign separation:

```text
E_pos = { lambda*(1,rho_E) : lambda > 0, rho_E > -6 }
```

and:

```text
The magnitude remains open
```

W67 states the magnitude-specific blocker:

```text
neither supplies the E-center lift q_E = 15/8
```

and:

```text
F_adj is not typed as a Route-2 center readout.
```

RCONN_DERIVED_NOTE preserves the exact support but separates readout:

```text
F_adj = dim(adj) / dim(N_c x N_c-bar) = (N_c^2 - 1) / N_c^2.
```

and:

```text
What does not follow from that algebra is the physical readout rule
```

The Record/Quantum boundary is the same wall in the physical route:

```text
Count is not weight.
```

and:

```text
Record does not supply the missing readout context.
```

The singlet-projector authority records the same color split as a complement:

```text
The 8-dimensional adjoint representation is the orthogonal complement
```

The K3 color-tensor note supplies a separate exact SU(3) color-algebra hit:

```text
C_F^2 T_F    =  8/9
```

## Exact Magnitude-Only Algebra

W77 already separated the sign. On the positive E-row family, with the T-side
values used by the Route-2 endpoint algebra,

```text
q_E = 1 + rho_E/6 > 0
c_TE = -5/(3*q_E) < 0
```

Therefore the magnitude alone is

```text
|c_TE| = 5/(3*q_E).
```

The exact Fierz adjoint fraction is

```text
F_adj(N_c) = (N_c^2 - 1)/N_c^2.
```

A magnitude-only structural identity would not need the Fierz fraction to carry
the minus sign. W77 supplies the sign separately. The exact theorem needed is:

```text
|c_TE| = F_adj(N_c).
```

Inside W77's endpoint algebra this is equivalent to:

```text
q_E(N_c) = 5/(3*F_adj(N_c))
         = 5*N_c^2/(3*(N_c^2 - 1)),

rho_E(N_c) = 6*(q_E(N_c) - 1)
           = 2*(2*N_c^2 + 3)/(N_c^2 - 1).
```

At `N_c = 3` this gives exactly:

```text
q_E = 15/8,
rho_E = 21/4,
c_TE = -8/9.
```

This is a partial magnitude route sharper than W67: sign typing and magnitude
selection are separable. What remains missing is not the minus sign; it is a
source-domain/readout theorem selecting the exact `q_E(N_c)` above, or
equivalently selecting `rho_E(N_c)`.

## Structural Appearance Count

This W80 probe distinguishes independent structural appearances from multiple
forms of the same SU(3) decomposition.

| Appearance | Exact value at `N_c=3` | Counted independent? | Reason |
|---|---:|---:|---|
| Fierz adjoint fraction `F_adj = dim(adj)/dim(3 x 3bar)` | `8/9` | yes | This is the primary SU(3) singlet-adjoint channel-count structure. |
| Singlet-projector complement `3 x 3bar = 1 + 8` | `8/9` | no additional count | Same singlet-adjoint split as `F_adj`, written as projector/complement data. |
| Physical connected-trace specialization `kappa_EW = 0` | `8/9` | no additional count | Same `F_adj` with the physical selector withheld by the Record/Quantum boundary. |
| Route-2 target `|c_TE| = 8/9` | `8/9` | no additional count | This is the bridge magnitude needing explanation, not an independent support structure. |
| SU(3) Casimir product `C_F^2 T_F` | `8/9` | yes | Separate color-tensor monomial; exact at SU(3), but not the same `N_c`-function as `F_adj`. |
| PMNS chart constant `E_2^2 = 8/9` | `8/9` | no | The cited PMNS note itself classifies the simple `1 - 1/9` origin as structurally arbitrary in that role. It is not used here. |

Independent structural appearance count: 2.

The two counted appearances both live on the SU(3) color-algebra side:

```text
F_adj(3) = 8/9,
C_F(3)^2*T_F = (4/3)^2*(1/2) = 8/9.
```

They are independent as color-algebra expressions at `N_c = 3`, but they do not
by themselves type the Route-2 E-center readout. In particular,

```text
C_F(N_c)^2*T_F = (N_c^2 - 1)^2/(8*N_c^2)
```

does not track `F_adj(N_c)` away from `N_c = 3`.

## No-Coincidence Adjudication

Because `8/9` appears in two independent SU(3) color-algebra structures and
the Route-2 bridge magnitude needs exactly `8/9`, the no-coincidence principle
does flag a structural question. The sharpened open theorem is:

```text
derive q_E(N_c) = 5*N_c^2/(3*(N_c^2 - 1))
```

on the Route-2 source-domain/readout surface, or equivalently derive:

```text
rho_E(N_c) = 2*(2*N_c^2 + 3)/(N_c^2 - 1).
```

At `N_c = 3`, that theorem realizes the desired magnitude:

```text
|c_TE| = F_adj = 8/9.
```

With W77's sign result, it would also realize:

```text
c_TE = -F_adj.
```

This note does not derive that theorem. It records the structural pressure and
the exact theorem form required to turn the pressure into a bridge. The
Record/Quantum boundary remains intact: no channel count is a physical
weighting rule, and no approved primitive in the registry declares the missing
Route-2 magnitude selector.

## N_c Variation Falsifiers

All entries are exact rationals.

| `N_c` | `F_adj(N_c)` | fixed W77 target `|c_TE|` from `rho_E=21/4` | fixed target tracks? | structural `q_E(N_c)` | structural `rho_E(N_c)` | structural `|c_TE|` |
|---:|---:|---:|---:|---:|---:|---:|
| `2` | `3/4` | `8/9` | no | `20/9` | `22/3` | `3/4` |
| `3` | `8/9` | `8/9` | yes | `15/8` | `21/4` | `8/9` |
| `4` | `15/16` | `8/9` | no | `16/9` | `14/3` | `15/16` |

This falsifies a fixed-number reading: if `rho_E=21/4` is held fixed while
`N_c` is varied, the target does not track `F_adj`. It supports the structural
form of the open theorem: if the target is lifted to the exact
`q_E(N_c)` above, `|c_TE|` tracks `F_adj(N_c)` identically.

The independent Casimir-product appearance is SU(3)-specific:

| `N_c` | `C_F(N_c)^2*T_F` | `F_adj(N_c)` | tracks? |
|---:|---:|---:|---:|
| `2` | `9/32` | `3/4` | no |
| `3` | `8/9` | `8/9` | yes |
| `4` | `225/128` | `15/16` | no |

Thus the Casimir-product hit is a real second SU(3) color-algebra appearance,
but not the `N_c`-parametric bridge theorem.

## Boundary

This note does not establish:

- a physical connected-trace selector `kappa_EW = 0`;
- a physical EW-current weighting, normalization, probability, or observable
  bridge;
- a Route-2 E-center readout theorem;
- a derivation of `q_E = 15/8` or `rho_E = 21/4`;
- a live endpoint fit or comparator-based nearest-rational selection;
- a new primitive or new axiom;
- any audit outcome.

Current bounded outcome: the magnitude equality is not derived as a structural
identity by the present authority bank. It is also not demoted to a
single-source numerical pun: a second exact SU(3) color-algebra appearance was
found. The result is a sharpened open theorem for the magnitude route, with the
withheld Route-2 readout selection named exactly.

## No-Go Discipline Gate

Freshness note: the local no-go discipline skill was checked against the local
`origin/main` copy. No fetch was run, and the repo was not moved.

Narrow bounded statement being stress-tested: current repo-internal authorities
do not derive the Route-2 magnitude theorem `|c_TE| = F_adj`, but they do
sharpen it to the exact `q_E(N_c)` theorem above and flag the equality as a
structural open question.

**N1 alternative routes.**

| Route | Marker | Result |
|---|---|---|
| Magnitude-only endpoint algebra | ATTEMPTED | Separates sign from magnitude and derives the exact equivalent theorem `q_E(N_c) = 5*N_c^2/(3*(N_c^2 - 1))`; does not derive that theorem. |
| W67 signed typed bridge | RULED OUT BY PRIOR for typing | W67 blocks `F_adj` as a signed Route-2 center readout; W77 now supplies the sign separately, leaving magnitude selection. |
| Singlet-projector complement | ATTEMPTED | Confirms `8/9` as `8` of `9`, but this is the same singlet-adjoint split as `F_adj`. |
| SU(3) Casimir product `C_F^2 T_F` | ATTEMPTED | Gives a second exact color-algebra `8/9`, but it does not track `F_adj(N_c)` away from `N_c=3`. |
| Physical `kappa_EW` route | RULED OUT BY PRIOR for this packet | Rconn kappa note withholds physical readout/weighting; Count is not weight. |
| Fixed-number target under `N_c` variation | ATTEMPTED | Fails at `N_c=2,4`; a structural theorem must be `N_c`-parametric. |
| Live endpoint comparator | NOT USED | Forbidden here; no fitted endpoint value or nearest-rational selector is an input. |

**N2 wall independence.**

Collapsed walls:

| Wall | Meaning | Relation |
|---|---|---|
| W1 | missing Route-2 magnitude-selection theorem for `q_E(N_c)` | closes the W80 magnitude if supplied |
| W2 | physical `kappa_EW` readout/weighting selector, if one routes through physical `R_phys` | independent of W1; a physical selector still would not by itself type the Route-2 endpoint map |
| W3 | SU(3)-specific Casimir coincidence lacks an `N_c`-tracking theorem | independent diagnostic; it sharpens no-coincidence pressure but is not W1 |

**N3 hidden-wall scan.**

Phrases re-read: "structural", "current authority bank", "source-domain",
"readout", "Record", "physical", "selector", and "approved primitive".
Each load-bearing use is tied to a linked source note or to the exact rational
equations above. No live comparator, new weighting rule, or hidden primitive is
introduced.

**N4 residual matching.**

| Witness | Witness residual | Current residual | Match |
|---|---|---|---|
| [W77_NOTE.md](../.claude/tmp/refs/W77_NOTE.md) | sign is separated; magnitude remains open | same magnitude residual, now tested as magnitude-only identity | yes |
| [W67_NOTE.md](../.claude/tmp/refs/W67_NOTE.md) | `F_adj` cannot type signed Route-2 center ratio | same typed bridge blocked; sign is no longer the issue | yes, narrowed |
| [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) | exact `F_adj` support does not supply physical readout rule | same Fierz support; physical route kept separate | yes |
| [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md) | channel count is not physical weight | same boundary if routing through `R_phys(kappa_EW)` | yes |

**N5 rhetoric audit.**

The negative statement is scoped to the current linked authority bank and the
exact W77 endpoint family. It is not a statement against future source-domain
theorems, owner-approved conventions, or alternate Route-2 readout primitives.
The positive no-coincidence statement is also scoped: it flags a structural open
question, not a derived bridge.

**N6 partial-closure path scan.**

The primitive registry lists `minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. Their source notes
do not declare a Route-2 readout bridge, physical observable identification,
weighting rule, probability rule, normalization rule, or E-center magnitude
selector. A future non-axiom theorem, explicit convention, or owner-approved
admission could still supply the `q_E(N_c)` theorem and later retire that
import; this note keeps that as an open path rather than calling it a new axiom.

**N7 steelman.**

A hostile reviewer could argue that two independent SU(3) color-algebra hits
are already enough under no-coincidence discipline: `F_adj = 8/9` and
`C_F^2 T_F = 8/9` both land on the exact Route-2 magnitude, and W77 has already
removed the sign problem. This note accepts that pressure and records the
sharpened theorem it demands. The remaining gap is the source-domain/readout
step selecting `q_E(N_c)` on the Route-2 E-center surface without importing a
physical `kappa_EW` weighting rule.

**N8 cross-cycle echo.**

The same wall shape appears in W67, W77, the Rconn readout boundary, and the
older Route-2 naturality packet: endpoint algebra works after an E-center
magnitude is supplied, while color count, registration, and positivity alone do
not choose the E-center lift. W80 narrows the target to a magnitude-only
theorem and adds the independent SU(3) Casimir-product echo.

No-Go discipline checklist outcome: PASS for checklist completeness only; this
is not an audit verdict and not a claim-status prediction.

## Verification

Run:

```bash
python3 scripts/quark_route2_cte_magnitude_structural_status_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=62, FAIL=0
```
