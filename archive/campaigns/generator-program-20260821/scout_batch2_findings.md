# Adversarial check: scout batch 2 (S5 + S7)

Status: **COMPLETE**

Construction authority: landed b190 note
`docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md`
and its landed exact runner
`scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_2026_08_25.py`.

Pinned fixture: `m = 9/20`, `c = 5/13`, `T = 16`, deep core `t0 = 3`.
All arithmetic in this check is exact over `QQ`; `nsimplify` is not used.

## S5 — response profile

**Verdict: the six quoted numbers are exact, but the literal "per-single-cell"
wording is refuted by the landed b190 cell definition.** They are the response
of the **sum of all four spatial cells at temporal anchor `s`**, together with
their four image partners. A single b190 cell is indexed by both `(s,x)` and
does not give the quoted number.

The exact volume derivative used was

```text
dB = d/dδ shear_hodge(5/13, 1-δ)|_0
   = [[-1,       0,       0, 0],
      [ 0, -169/144,  65/144, 0],
      [ 0,   65/144, -169/144, 0],
      [ 0,       0,       0, 1]].
```

For each local anchor `(s,x)`, its reflected image anchor is
`(T-1-s,x)`, with the image block conjugated by b190's
`OFFSET_PERMUTATION`. I formed `dQ = m dH + dH D - D^T dH`,
`dG = -G dQ G`, extracted `dK_c` and `dL2` using the landed pairing indices,
and evaluated `tr(K_c^-1 (dL2 - dK_c W))` exactly.

The literal single-spatial-cell responses split by spatial parity:

| `s` | `x = 0,2` | `x = 1,3` |
| ---: | ---: | ---: |
| 1 | `0` | `0` |
| 2 | `-20900678024945648/88720444282163745` | `3696627775012096/29573481427387915` |
| 3 | `149518897051870024/147867407136939575` | `-58407092043276376/29573481427387915` |
| 4 | `-8956827997451709214445818024208/5276875808912607540299962640625` | `-9240193544760129528102927764736/1758958602970869180099987546875` |
| 5 | `907245269067878860293432/222484997463417708034375` | `244236620114250432855608/222484997463417708034375` |
| 6 | `0` | `0` |

Summing the four spatial anchors gives the scout's table exactly:

| `s` | exact full-slice-cell response | comparison |
| ---: | ---: | :---: |
| 1 | `0` | exact match |
| 2 | `-3924317879963744/17744088856432749` | exact match |
| 3 | `-285033126329023712/147867407136939575` | exact match |
| 4 | `-73354817263464195597509202636832/5276875808912607540299962640625` | exact match |
| 5 | `+38264746670503590368/3696685178423489375` | exact match |
| 6 | `0` | exact match |

The endpoint zeros are the stated window law. A local cell anchored at `s`
occupies slices `{s,s+1}`; this intersects the response window `[3,5]` exactly
for `s = 2,3,4,5`, while `{1,2}` and `{6,7}` are disjoint. Thus the `s=1`
and `s=6` zeros hold for every spatial anchor separately, not only after a
cancellation in the spatial sum.

The `s=4 -> s=5` sign flip is also exact and robust before summation: both
spatial-parity values are negative at `s=4` and positive at `s=5`.

## S7 — volume interval

**Verdict: all five requested points hold. Both hostile probes also hold.**
Consequently, any assertion that `(1/10,1]` (or `[1/10,1]`) is the maximal
positivity interval is refuted by exact counterexamples on both sides.

At each volume I rebuilt `B = shear_hodge(5/13,v)`, then the full b190 action
and its exact inverse over `QQ`, and finally `W = K_c^-1 L2` at `T=16`,
`t0=3`. The table gives the two primitive integer quadratic factors in the
form `(a,C,a)` for `a z^2 - C z + a`; each factor occurs with multiplicity two.
`margin` is `C-2a`, and `Delta = C^2-4a^2`.

| `v` | primitive factors `(a,C,a)`, each squared | margins | discriminants | result |
| ---: | --- | --- | --- | :---: |
| `4/5` | `(31260675,302948719,31260675)`; `(50327125,139773119,50327125)` | `240427369`; `39118869` | `87869007137918461`; `9405246751925661` | HOLD |
| `3/5` | `(964625,2690274,964625)`; `(6057575,53690866,6057575)` | `761024`; `41575716` | `3515568632576`; `2735932232307456` | HOLD |
| `2/5` | `(154718175,1228109794,154718175)`; `(191334625,536004194,191334625)` | `918673444`; `153334944` | `1412502811417399936`; `140864741090027136` | HOLD |
| `1/5` | `(9229575,65883826,9229575)`; `(9861625,27701426,9861625)` | `47424676`; `7978176` | `3999938309675776`; `378362411870976` | HOLD |
| `1/10` | `(21760118175,150049193794,21760118175)`; `(22147734625,62233488194,22147734625)` | `106528957444`; `17938018944` | `20620749586269506791936`; `1910918456715041819136` | HOLD |
| `1/100` | `(207461386358175,1412992189424194,207461386358175)`; `(207498839574625,583071737558594,207498839574625)` | `998069416707844`; `168074058409344` | `1824386020055153498463715227136`; `167749577440334068823807694336` | **HOLD outside claimed lower edge** |
| `6/5` | `(3801625,10499666,3801625)`; `(6132725,66574198,6132725)` | `2896416`; `54308748` | `52433575549056`; `4281682575640704` | **HOLD outside claimed upper edge** |

For every row, `a > 0`, `Delta > 0`, and `C-2a > 0`. Hence each quadratic has
two distinct real positive roots. Palindromy gives product exactly `1`, so each
pair is reciprocal. The two primitive triples are distinct at every volume, so
the two reciprocal pairs are distinct as well.

There is also a bracket inconsistency in the scout wording: `(1/10,1]` excludes
`v=1/10`, while the scout explicitly claims and this check confirms positivity
at `v=1/10`. If the phrase "only `(1/10,1]`" was intended merely as a
conservative sampled range rather than a maximality claim, the honest result is
that the sampled positive set already extends at least to the two additional
points `1/100` and `6/5`; these finite probes do not determine the true endpoint
or prove positivity on the continuous intervals between samples.

## Final disposition

- **S5 numeric table:** confirmed exactly for a four-spatial-cell slice sum;
  refuted as a literal response of one b190 `(s,x)` cell. The zero-window law
  and the `s=4 -> s=5` sign flip survive even at individual spatial anchors.
- **S7 five requested points:** confirmed exactly.
- **S7 claimed exclusive interval:** refuted if meant maximally; exact positive
  counterexamples occur at both `v=1/100` and `v=6/5`.
- No float arithmetic, tolerance, or `nsimplify` was used.

Status: **COMPLETE**
