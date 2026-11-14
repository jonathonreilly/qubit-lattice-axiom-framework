# Hadron Lane 1 B2 Dynamical Screening Boundary

**Type:** open_gate
**Review scope:** open bridge and source diagnostic. The runner's toy arithmetic and source-phrase checks illustrate supplied examples; its missing-input checklist is printed uncounted. None of it establishes a physical no-go or current audit authority.

**Date:** 2026-04-29
**Status:** open (bridge diagnostic). The current repo surface does not close
the B2 dynamical screening factor; no `sqrt(sigma)` status upgrade and no
hadron-mass claim.
**Loop:** `.claude/science/physics-loops/impact-campaign-20260429/`
**Runner:** `scripts/frontier_hadron_lane1_b2_dynamical_screening_boundary.py`

```yaml
actual_current_surface_status: open
conditional_surface_status: bounded-support
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "On the 2026-04-29 surface the pure-gauge payload does not fix the B2 screening factor; a determinant input is needed, for example an N_f=2+1 ensemble, a framework derivation of the determinant correction, or an explicitly budgeted external comparator (list not exhaustive)"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. Question

Lane 1 identifies `(B2)` as the load-bearing numerical gap for the
`sqrt(sigma)` route:

```text
quenched SU(3) string tension at beta=6.0
  -> N_f=2+1 dynamical string tension
```

The current bounded derivation uses the quenched Method-2 payload and a rough
screening factor near `0.96`. This block asks whether the existing repo data
can close that factor without a new dynamical calculation.

## 2. Boundary Statement (diagnostic, not a theorem)

**Statement.** The repo surface as of 2026-04-29 contains no sea-fermion
determinant data, so its pure-gauge beta=6.0 payload does not fix the `(B2)`
dynamical screening factor. The rough factor `0.96` is an input, not a
result of that payload.

This records which inputs are missing. It is not a theorem that no
framework derivation of the factor can exist: section 6 lists such a
derivation as one way to supply the missing input.

## 3. Argument

The current Method-2 string-tension payload has the form:

```text
beta = 6.0
r0/a = 5.37
sigma a^2 = 0.0465
sqrt(sigma)_quenched ~= 484 MeV
```

The B2 correction is not another pure-gauge observable. It changes the path
measure from the Wilson gauge measure to a sea-fermion determinant measure:

```text
dmu_quenched(U)  proportional to exp(-S_g(U)) dU
dmu_dyn(U)       proportional to exp(-S_g(U))
                              det(D_u + m_u) det(D_d + m_d) det(D_s + m_s) dU
```

The screening factor compares string tensions extracted under these two
different measures. The determinant factors, the sea masses, and a large-volume
Creutz-ratio extraction are therefore load-bearing inputs.

The current repo has a useful pure-gauge consistency runner at `L=4`, but the
confinement note already marks that as qualitative: quantitative extraction
requires large Wilson loops and volumes at least of order `16^4`. The existing
runner also does not include the sea-fermion determinant.

The runner's family of factors, `0.90`, `0.94`, `0.96` and `1.00`, is a
supplied example: the payload numbers above do not involve the factor, so
they do not pick one member of the family, while the `sqrt(sigma)` readouts
differ. The example shows what the payload lacks. It does not exhaust the
ways the factor could be fixed.

## 4. Runner Witness

The runner checks:

- current Lane 1 notes name B2 as the dominant numerical residual;
- the payload alone gives the 484 MeV quenched readout, with no factor as an
  input, while the supplied factor family gives distinct readouts;
- a toy determinant reweighting changes the measured observable and depends on
  the sea masses;
- the current `L=4` pure-gauge runner is not a large-volume dynamical
  extraction;
- two controls: a degenerate factor family fails the spread test, and a
  decoupled (very heavy) sea fails the determinant-change test.

The screening factors, the toy determinant bank and the sea masses are chosen
numbers. The text checks confirm phrases in the cited notes and in the
confinement runner source. The four missing-input items (Part 5 of the
runner) are a dated checklist of what the 2026-04-29 surface lacks. They are
stipulated, not computed, so the runner prints them as uncounted
`SUPPLIED CHECKLIST:` lines (repair of 2026-11-14). None of these checks is an
exhaustive physical obstruction.

Checks:

```bash
set -o pipefail; python3 scripts/frontier_hadron_lane1_b2_dynamical_screening_boundary.py | tee outputs/frontier_hadron_lane1_b2_dynamical_screening_boundary_2026-04-29.txt
python3 -m py_compile scripts/frontier_hadron_lane1_b2_dynamical_screening_boundary.py
```

Expected runner result:

```text
SUMMARY: PASS=17 FAIL=0
```

## 5. What This Records

This records that one narrow implication is unsupported on the current
surface:

```text
current pure-gauge beta=6.0 data + rough factor 0.96
  => closed B2 dynamical screening budget
```

The factor `0.96` is supplied, not derived from the pure-gauge data. The
current artifacts support only the bounded `sqrt(sigma)` readout and a list
of what is missing.

## 6. What Remains Open

Paths that would supply the missing input include the following; the list is
not exhaustive:

- a genuine `N_f=2+1` beta=6.0 determinant ensemble with controlled sea masses
  and large-volume Creutz ratios;
- a branch-local theorem deriving the determinant correction from framework
  structure;
- an explicitly budgeted external comparator, clearly marked as an admitted
  comparator rather than a framework-native derivation.

The note makes no pion, proton, neutron, spectroscopy, or form-factor claim.

## 7. Next Route

This was the second consecutive local boundary block in the campaign.
Per the long-running policy, the next science selection should force a stretch
attempt from minimal premises before more audit-only cycles.
