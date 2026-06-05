# Koide Orientation-Blind Count And B-Field Gate

**Date:** 2026-05-30
**Claim type:** open_gate
**Status:** source note; downstream status is decided by independent review.
**Primary runner:** [`scripts/frontier_koide_orientation_blind_count_b_field_gate_2026_05_30.py`](../scripts/frontier_koide_orientation_blind_count_b_field_gate_2026_05_30.py)

## Result

The local doublet algebra narrows the charged-lepton Koide question to one
specific bridge:

```text
Is the circulant coefficient b a dynamical first-order field amplitude,
or is it a static background coupling?
```

The runner verifies that the per-block count is orientation-blind.  The
conjugation map on the `b`-plane flips the complex orientation but preserves the
metric and therefore preserves the rank count.  Thus the orientation choice
does not by itself block the one-mode count.

The runner also verifies that the native doublet geometry does not decide the
role of `b`.  If `b` is a first-order field amplitude, its two real coordinates
are already a phase space and count as one mode.  If `b` is a static coupling,
the corresponding phase space is `T*(R^2)` and counts as two modes.  The
unbuilt bridge is the identification of the circulant coefficient with the
Kähler-Dirac field amplitude on the same doublet component.

## Verified Local Facts

1. On the real `b`-plane, the native Kähler triple is
   `g = 6 I_2`, `J2 = [[0,-1],[1,0]]`, and `omega = g J2`.  The runner checks
   `J2^2 = -I`, antisymmetry and nondegeneracy of `omega`, and compatibility
   `omega(u,v) = g(u,J2 v)`.
2. The conjugation map `b -> b-bar` is `c = diag(1,-1)`.  It satisfies
   `c J2 c^-1 = -J2` and `c^T omega c = -omega`, but also
   `c^T g c = g`.  It flips orientation while preserving the rank count
   `dim(R^2)/2 = 1`.
3. For the circulant charged-lepton matrix
   `H = a I + b C + b-bar C^2`, the runner re-derives
   `Q = trace(H^2)/trace(H)^2 = (a^2 + 2 |b|^2)/(3 a^2) = (1 + 2r)/3`.
   Hence `Q = 2/3` at `r = |b|^2/a^2 = 1/2`.
4. The existence of `omega` alone does not choose between the one-mode and
   two-mode readings.  The choice is the action-order role of `b`: first-order
   field amplitude versus static coupling.
5. A pure dark-state cooling jump `|f1><f2|` between the two doublet Fourier
   modes is orthogonal to the native circulant algebra `span{I,C,C^2}` in the
   Hilbert-Schmidt metric.  A route using that jump is therefore outside the
   local circulant algebra tested here.
6. The Kähler-Dirac operator on `Lambda*(C^3)` has zero
   `Lambda^1 -> Lambda^1` block in the runner's finite model.  The
   form-degree field index does not directly identify the circulant coefficient
   `b`; a separate index-map bridge would be needed.

## Boundary

This note does not derive the charged-lepton Koide value.  It does not approve
a new axiom, primitive, or Tier-A admission.  It also does not claim that all
possible routes are closed.  It records an open gate with exact local support:

```text
B-coupling -> B-field bridge open.
```

If a separately reviewed bridge identifies the circulant coefficient `b` with a
first-order Kähler-Dirac field amplitude on the doublet component, then the
per-block route supplies the one-mode count and the local formula gives
`Q = 2/3` at `r = 1/2`.  Without that bridge, the native doublet geometry and
the local `Q` arithmetic do not select between the one-mode and two-mode
readings.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_orientation_blind_count_b_field_gate_2026_05_30.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: orientation-blind count and B-field gate checks pass; the B-coupling
to B-field bridge remains open.
```
