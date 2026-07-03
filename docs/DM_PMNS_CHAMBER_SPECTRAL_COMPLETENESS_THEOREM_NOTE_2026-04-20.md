# DM PMNS Chamber Spectral Completeness Boundary Note

**Date:** 2026-04-20
**Lane:** DM A-BCC / open import `I11`
**Status:** bounded support - listed-root support; chamber-completeness
upper bound is not derived
**Type:** source boundary repair for the former compact-completeness theorem

**Status authority:** independent audit lane only. This source note does
not set or move its own audit verdict; downstream audit lane and packet
status are decided by the audit lane.

**Primary runner:**
`scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py`

**Interval companion:**
[`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)

---

## 0. Why this note is repaired

An earlier version of this note stated that the compact active-chamber
`chi^2 = 0` PMNS set was exactly three points:

- Basin 1 on `sigma = (2,1,0)`;
- Basin 2 on `sigma = (2,1,0)`;
- Basin X on `sigma = (2,0,1)`.

The May 16 Krawczyk companion sharpened the science and exposed the missing
half of that claim. It certifies existence and local uniqueness for the 8
listed reduced spectral roots and certifies the chamber-side sign for those
8 boxes. It does **not** certify an upper bound excluding additional reduced
roots outside the listed boxes, and it does **not** certify that the four
other row permutations carry no chamber roots.

This repair keeps the supported computation and removes the unsupported
global-completeness wording.

## 1. Inputs

This note depends on:

- [DM_PMNS_ASYMPTOTIC_SOURCE_NO_GO_NOTE_2026-04-20.md](./DM_PMNS_ASYMPTOTIC_SOURCE_NO_GO_NOTE_2026-04-20.md)
- [DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md](./DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md)
- [DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md](./DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md)
- [DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)

The asymptotic source no-go removes the unbounded basin loophole that this
compact-chamber packet complements; the active-half-plane theorem supplies
the chamber inequality `q_+ + delta >= sqrt(8/3)`; the affine
point-selection boundary supplies the affine Hermitian family
`H(m, delta, q_+) = H_base + m T_m + delta T_delta + q_+ T_q`.

## 2. Question

After `DM_PMNS_ASYMPTOTIC_SOURCE_NO_GO_NOTE_2026-04-20.md` rules out
unbounded exact PMNS-fit basins, what is actually supported for the
remaining compact chamber problem?

## 3. Bottom line

Bounded support only.

On the two branches with electron row fixed to the third axis,

```text
sigma = (2,1,0),  sigma = (2,0,1),
```

the PMNS angle constraints admit an ordered-eigenvalue reduction. In the
finite multistart computation and in the Krawczyk companion boxes:

- the `sigma = (2,1,0)` reduced system has the four listed roots
  `{Basin 1, Basin 2, Basin N, Basin P}`;
- the `sigma = (2,0,1)` reduced system has the four listed roots
  `{Basin X, X_a, X_b, X_c}`;
- the active-chamber inequality

```text
q_+ + delta >= sqrt(8/3)
```

strictly contains the listed boxes around

```text
{Basin 1, Basin 2, Basin X}
```

and strictly excludes the listed boxes around the other five candidates.

The finite direct chamber sweep over all six row permutations returns the
same three listed chamber roots. That is a useful empirical cross-check,
but it is not a proof that no other chamber roots exist.

## 4. Supported statement

**Proposition (listed chamber-root support).** Fix the target PMNS angle
triple

```text
(sin^2 theta_12, sin^2 theta_13, sin^2 theta_23)
= (0.307, 0.0218, 0.545).
```

On the affine DM Hermitian family

```text
H(m, delta, q_+) = H_base + m T_m + delta T_delta + q_+ T_q,
```

the source computation supports the following finite listed-root packet:

- the ordered-eigenvalue reduction recovers four listed real roots on
  `sigma = (2,1,0)`, namely `Basin 1`, `Basin 2`, `Basin N`, `Basin P`;
- it recovers four listed real roots on `sigma = (2,0,1)`, namely
  `Basin X`, `X_a`, `X_b`, `X_c`;
- the Krawczyk companion certifies a unique reduced-system zero in a
  radius-`10^-6` box around each of the 8 listed candidates;
- interval evaluation of `q_+ + delta - sqrt(8/3)` on those boxes certifies
  that the listed chamber survivors are `Basin 1`, `Basin 2`, and `Basin X`.

This proposition is a listed-root support statement, not a compact
chamber-completeness theorem.

## 5. Computed root packet

The runner's current listed chart points are:

- `sigma = (2,1,0)`:
  - Basin 1: `(0.657061342210, 0.933806343759, 0.715042329587)`
  - Basin 2: `(28.006188289565, 20.721831213931, 5.011599458305)`
  - Basin N: `(0.501997247472, 0.853543345404, 0.425916455114)`
  - Basin P: `(1.037883050950, 1.433018557503, -1.329548075477)`
- `sigma = (2,0,1)`:
  - Basin X: `(21.128263668694, 12.680028023619, 2.089234805861)`
  - plus three off-chamber companions.

Their chamber margins are:

- Basin 1: `+0.0158555`;
- Basin 2: `+24.1004`;
- Basin N: `-0.3535`;
- Basin P: `-1.5295`;
- Basin X: `+13.1363`;
- the three `sigma = (2,0,1)` companions: all negative.

So the listed Krawczyk boxes split cleanly into three chamber-side boxes and
five off-chamber boxes.

## 6. Consequence for `I11`

This packet does **not** close `I11`.

It strengthens the compact-chamber support side:

- the asymptotic theorem removes the infinity-tail loophole;
- this packet and the Krawczyk companion certify the existence and chamber
  sign of the 8 listed reduced-system roots.

The remaining `I11` gap is the upper-bound side:

- no additional reduced-spectral roots outside the listed boxes;
- no additional chamber `chi^2 = 0` roots on the other row permutations.

Until one of those exclusion certificates is supplied, downstream consumers
may cite this packet only as bounded listed-root support.

## 7. What this does and does not say

What is supported:

- the 8 listed reduced-system roots exist in disjoint Krawczyk boxes;
- the three listed chamber survivors lie strictly in the active chamber;
- the five listed off-chamber companions lie strictly outside it;
- the finite direct chamber sweep returns the same three listed survivors.

What is not claimed:

- exact compact chamber completeness;
- an upper bound excluding additional reduced roots;
- a Sturm, resultant, or cover-based no-other-roots certificate;
- that Basin 1 is selected without further law;
- that off-chamber real roots are physically relevant;
- that `sigma_hier` is derived.

## 8. Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py
```

Expected final line:

```text
PASS=11  FAIL=0
```
