# Bare alpha_3 / alpha_em Conditional Bookkeeping Lemma

Date: 2026-04-25

**Repair date:** 2026-06-07
**Canonical repair packet:** [`docs/FRAMEWORK_BARE_ALPHA_RATIO_ASSUMED_INPUT_IDENTITY_SUPPORT_NOTE_2026-04-30.md`](../../docs/FRAMEWORK_BARE_ALPHA_RATIO_ASSUMED_INPUT_IDENTITY_SUPPORT_NOTE_2026-04-30.md)
**Location:** `archive_unlanded/framework-bare-alpha-assumed-input-salvage-2026-04-30/`
**Status:** archived boundary repair - conditional algebra lemma only
**Primary verifier:** `scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py`

This file remains archived. It is not a live retained theorem, not
retained-grade support authority, and not authority for an electroweak
normalization lane.

The canonical live repair packet is the formal assumed-input identity note
linked above. This archived wrapper is kept only so the original audited-failed
row has a direct same-path handoff to the narrowed source boundary.

## Why the original claim failed

The audit found that the arithmetic was correct but the authority boundary was
not. The original source treated the result as a support corollary on a
retained EW-normalization surface while the verifier itself could not establish
that retained authority. The allowed repair was to narrow the source to a pure
conditional algebra lemma over explicit bookkeeping assumptions.

That is the whole purpose of this repaired archived note.

## Conditional assumptions

Assume only the following dimension-indexed bare bookkeeping inputs:

```text
d in Z, d >= 1
g_3^2 = 1
g_2^2 = 1/(d + 1)
g_Y^2 = 1/(d + 2)
```

For the numerical specialization in this file, set `d = 3`.

These supplied inputs are hypotheses of the lemma. This note does not derive
them from Cl(3), from the Standard Model, from a retained EW lane, or from any
accepted minimal-input stack.

## Lemma

Under the supplied inputs above,

```text
1/g_em^2 = 1/g_2^2 + 1/g_Y^2 = 2d + 3
```

and therefore

```text
g_em^2 = 1/(2d + 3)
alpha_3(bare) / alpha_em(bare) = g_3^2 / g_em^2 = 2d + 3.
```

At `d = 3`,

```text
alpha_3(bare) / alpha_em(bare) = 9.
```

The same supplied-input algebra gives

```text
sin^2(theta_W)(bare)
  = g_Y^2 / (g_2^2 + g_Y^2)
  = (d + 1)/(2d + 3)
  = 4/9      at d = 3.
```

Compared only as a formal normalization contrast, not as a phenomenological
claim,

```text
4/9 - 3/8 = 5/72.
```

## Checked identities

The verifier checks:

- `g_3^2 = 1`;
- `g_2^2 = 1/(d+1)`;
- `g_Y^2 = 1/(d+2)`;
- `1/g_2^2 + 1/g_Y^2 = 2d + 3`;
- `g_em^2 = 1/(2d + 3)`;
- `sin^2(theta_W) = (d + 1)/(2d + 3)`;
- `alpha_3(bare) / alpha_em(bare) = 2d + 3`;
- the `d = 3` values `9`, `4/9`, `5/9`, `1/(36 pi)`, and `5/72`;
- the small dimension fingerprint table `d=2,3,4,5 -> 7,9,11,13`.

## What this does not claim

- It does not assert that a retained EW-normalization lane exists for this
  archived row.
- It does not promote a Cl(3) -> SM support packet into the accepted
  minimal-input stack.
- It does not derive the supplied bare bookkeeping inputs.
- It does not claim direct low-energy `alpha_3/alpha_em` phenomenology.
- It does not claim an `M_Z`, `v`, RGE, projection, or threshold result.
- It does not claim SU(5) unification or SU(5)-style normalization.
- It does not alter any live `alpha_s(M_Z)` or `alpha_s(v)` derivation.

## Safe Use

Safe:

```text
if the supplied bare bookkeeping inputs hold, then
alpha_3(bare) / alpha_em(bare) = 2d + 3, hence 9 at d = 3.
```

Unsafe:

```text
the framework has retained EW authority for this archived row;
bare ratio 9 is a direct low-energy observable;
the supplied bookkeeping inputs are derived here.
```

## Reproduction

```bash
python3 scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py
```

Expected final line:

```text
VERDICT: FORMAL ASSUMED-INPUT IDENTITY THEOREM VERIFIED
```
