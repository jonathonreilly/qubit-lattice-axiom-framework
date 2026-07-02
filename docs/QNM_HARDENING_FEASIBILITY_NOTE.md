# QNM Hardening Feasibility Note

**Type:** open_gate candidate
**Status:** bounded hard-bar negative; no positive QNM hardening law certified
**Date:** 2026-04-05  
**Primary runner:** [`scripts/qnm_hardening_stability_certificate.py`](../scripts/qnm_hardening_stability_certificate.py)
**Runner cache:** [`logs/runner-cache/qnm_hardening_stability_certificate.txt`](../logs/runner-cache/qnm_hardening_stability_certificate.txt)
**Scope:** decide whether any exact-lattice self-consistent spectral claim can
be made review-safely from the current code/branch context

This note is intentionally conservative. It does **not** promote the branch
QNM story to a retained `main` claim. It only asks what would be required to
make the claim review-safe, and whether the current chain is already close
enough.

Historical branch-side anchor:

- [`scripts/qnm_scaling.py`](../scripts/qnm_scaling.py)

Relevant current `main` context:

- [`POISSON_SELF_GRAVITY_LOOP_NOTE.md`](POISSON_SELF_GRAVITY_LOOP_NOTE.md)
- [`POISSON_SELF_GRAVITY_BORN_AUDIT_NOTE.md`](POISSON_SELF_GRAVITY_BORN_AUDIT_NOTE.md)
- [`GATE_B_POISSON_SELF_GRAVITY_NOTE.md`](GATE_B_POISSON_SELF_GRAVITY_NOTE.md)

## 2026-05-26 hard-bar certificate

The primary runner adds the controls requested by the audit row on reduced,
deterministic grids. It does not certify a positive spectral law. It certifies
the bounded negative boundary that the tested hardening minima are not
sub-Nyquist features.

The runner checks:

1. **`G = 0` null:** with the same source strength, no absorption peaks pass
   either threshold (`0.5` or `0.8`) in the tested windows.
2. **Matched fixed-field control:** the self-coupled relaxed fields are frozen
   before the `k` scan, so the spectrum is tested as a fixed-field propagation
   problem rather than a moving field-update loop.
3. **Fixed-field Born/Sorkin audit:** the three-source `I3/P` check on each
   returned fixed field is machine clean (`< 1e-11`).
4. **Nyquist exclusion:** every apparent self-coupled absorption minimum in
   the tested cases lies at or beyond `0.95*pi/h`; the sub-Nyquist peak set is
   empty.
5. **Threshold, window, damping, and refinement stability:** the empty
   sub-Nyquist peak set is stable for thresholds `0.5` and `0.8`, windows
   `k=2..8` and `k=2..10`, damping `0.05` and `0.10`, and the `h=1.0` to
   `h=0.75` refinement check.

Representative cached output:

```text
coarse-damping005: h=1.00 damping=0.05 nyquist=3.142 relax_residual=1.543e-03 born_i3=4.863e-16
  window=k2-8 threshold=0.5 G0_peaks=[] G0.10_peaks=[5.0] sub_nyquist_G0.10=[]
coarse-damping010: h=1.00 damping=0.10 nyquist=3.142 relax_residual=2.038e-03 born_i3=3.290e-16
  window=k2-10 threshold=0.8 G0_peaks=[] G0.10_peaks=[5.0, 8.0] sub_nyquist_G0.10=[]
refined-damping005: h=0.75 damping=0.05 nyquist=4.189 relax_residual=4.188e-03 born_i3=2.737e-15
  window=k2-10 threshold=0.8 G0_peaks=[] G0.10_peaks=[5.0, 7.5] sub_nyquist_G0.10=[]
```

The safe read is therefore negative and bounded: the current QNM-hardening
story has not passed the hard bars needed for a positive exact-lattice
spectral claim.

## Branch claim surface

The branch harness sweeps self-coupling `G` and source mass `s`, then looks
for escape-spectrum minima across a `k` scan.

The strongest branch-side headline is:

- peak locations depend on `G`
- peak locations are approximately independent of `s`

That is scientifically interesting, but it is not yet review-safe as a
mainline spectral claim.

## Why it is not yet review-safe

The current branch story is missing the controls that the retained `main`
bars now require.

### 1. No `G = 0` null

There is no frozen `G = 0` spectral null showing that the peaks collapse to the
baseline when self-coupling is removed.

Without that, the claim can still be a coupling trend, but not yet a clean
self-consistent spectral effect.

### 2. Nyquist artifact risk is real

The branch audit already flagged a `k = 6.5` artifact tied to the Nyquist
boundary.

That means the spectrum cannot be promoted until the non-Nyquist peaks are
shown to survive:

- peak-threshold changes
- `h` refinement
- `W` changes
- damping changes
- explicit exclusion of the Nyquist-adjacent artifact

### 3. No matched fixed-field control

The branch harness compares self-consistent field runs, but it does not yet
freeze a matched fixed-field control that isolates the spectral effect from the
field-update loop itself.

That control is needed if the final claim is to be interpreted as a
self-consistent spectral signature rather than a generic escape-minimum
pattern.

### 4. No Born check on the converged field

The mainline self-gravity audit already showed that step-local Born can be
clean while end-to-end Born drifts in the loop.

The branch QNM harness does not yet package a corresponding Born audit on the
converged spectral family.

That matters because a spectral claim that depends on the self-consistent loop
needs to survive the same linearity checks as the rest of the project.

### 5. No refinement / threshold stability pack

The branch harness does not yet freeze a stability pack showing that the peak
locations and spacings are stable under:

- spatial refinement
- peak-threshold variation
- window selection
- damping variation

Without that, the peak spacing is still analysis-choice sensitive.

## What would be needed for a future positive claim

To make a positive QNM-style claim review-safe, a later branch would need a
narrow, frozen chain with all of the following:

1. `G = 0` null
2. fixed-field matched control
3. Born check on the converged field
4. explicit Nyquist-artifact exclusion
5. refinement and threshold stability
6. a dedicated note/log pair

## Downstream source-boundary firewall

Allowed downstream uses of this packet are limited to:

- cite the bounded negative hard-bar result that the tested current
  self-coupled minima are Nyquist-unsafe;
- cite the controls that were run: `G=0` null, matched fixed-field control,
  fixed-field Born/Sorkin check, threshold/window/damping variation, and the
  `h=1.0` to `h=0.75` refinement check;
- cite the future positive-target requirements listed above.

Forbidden downstream uses without a new retained bridge:

- do not cite this packet as a positive QNM spectral law;
- do not cite it as evidence for stable sub-Nyquist QNM hardening peaks;
- do not cite the branch-side `G`-dependent peak story without a fresh
  dedicated note/log pair;
- do not promote the QNM lane unless the future runner supplies stable
  sub-Nyquist peaks with `G=0` or null controls, fixed-field Born/Sorkin
  checks, threshold/window/damping/refinement controls, and a dedicated note
  and log pair.

## Safest current phrasing

The safest claim surface today is:

- the branch QNM harness suggests a `G`-dependent escape spectrum on a
  self-consistent field family
- the 2026-05-26 hard-bar runner finds the tested apparent minima only at
  Nyquist-unsafe locations
- the result is therefore a bounded negative/open-gate boundary, not a
  positive spectral law

## Verdict

**feasibility: no positive QNM hardening certificate on the tested bounded
surface**

The QNM lane remains scientifically interesting, but this branch supplies a
reviewable reason not to promote the current hardening story: the tested
self-coupled minima do not survive the sub-Nyquist hard bars. Any future
positive claim must exhibit stable sub-Nyquist peaks under the same control
family, or a stronger one.
