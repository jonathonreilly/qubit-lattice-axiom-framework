# PR230 Block130 Neutral H3/H4 Transfer/Coupling Construction Attempt

Status: exact negative boundary / neutral H3/H4 authority is not constructible
from the completed finite source/taste-radial row packet.

## Scope

Block130 pivots after Block129 from strict Schur/Feshbach pole authority to the
neutral route.  It tries to construct the missing H3/H4 packet from current
same-surface material:

- H3: physical neutral transfer, off-diagonal generator, primitive-cone
  certificate, irreducibility certificate, or equivalent accepted authority;
- H4: source/canonical-Higgs coupling authority;
- current finite support: the completed `63 x 11 = 693`
  `C_ss/C_sx/C_xx` rows.

## Result

No strict neutral authority is present.  The runner finds:

- `693` finite source/taste-radial rows across all `63` completed chunks;
- zero expected strict neutral artifact sidecars;
- zero strict neutral/primitive/offdiagonal/source-coupling tokens in the raw
  completed higher-shell files;
- H1/H2 Z3 and heat-kernel material remains mathematical support only, not a
  PR230 physical transfer or H4 coupling selector;
- the two-source primitive-transfer candidate still rejects finite
  `C_sx/C_xx` rows as physical transfer;
- Block128 source-Higgs fallback and Block129 Schur fallback remain blocked.

The constructive obstruction is a two-completion witness.  For the sample
chunk001, mode `(0,0,0)` row,

- `C_ss = 0.12246420767668034`
- `C_sx = -0.0001185778127224799`
- `C_xx = 0.2809106039893544`

adjoin an orthogonal neutral `n` with `C_sn=0`, `C_xn=0`, and
`C_nn=C_xx`.  The family

```text
H(theta) = cos(theta) x + sin(theta) n
```

preserves the observed finite `C_ss/C_sx/C_xx` rows, but changes the normalized
source coupling.  At `theta=0`, the normalized source coupling is
`-0.00022372749929547354`; at `theta=pi/3`, it is
`-0.0001118637496477368`.

Similarly, two positive candidate transfer matrices on the hidden neutral
plane,

```text
T0 = [[1, 0], [0, 1]]
T1 = [[1, 0.25], [0.25, 1]]
```

have the same current equal-time row data but different off-diagonal generator
content.  The witness is not physical transfer authority.  It shows exactly
why the current finite row surface does not determine H3 or H4 without an
accepted same-surface action/transfer theorem and source/canonical-Higgs
coupling certificate.

## Claim Boundary

This block does not claim retained or `proposed_retained` closure.  It does not
promote finite equal-time `C_sx/C_xx` rows to physical transfer, pole residues,
canonical `C_sH/C_HH` rows, or canonical-Higgs authority.  It does not use
`H_unit`, `yt_ward_identity`, `y_t_bare`, observed targets, observed W/Z or
`g2`, `alpha_LM`, plaquette, `u0`, or unit assumptions for `kappa_s`, `c2`, or
`Z_match`.

## Exact Next Action

The neutral route reopens only with a new accepted same-surface physical
transfer/off-diagonal generator or primitive/irreducibility certificate plus
source/canonical-Higgs coupling authority.  Without that artifact, pivot back
to the action-first source-Higgs row contract or strict W/Z production rows
only if a new strict artifact appears.
