# CKM Mass-Basis NNI Structural Identities Note

**Date:** 2026-06-17
**Type:** positive_theorem
**Claim type:** positive_theorem
**Status:** source-side structural theorem; independent audit required before any downstream status change.
**Status authority:** independent audit lane only. This note does not set,
predict, or estimate any audit outcome.
**Runner:**
[`scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py`](../scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py)
**Cached log:**
[`logs/runner-cache/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.txt`](../logs/runner-cache/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.txt)

## Claim

This note isolates the source theorem inside the older mass-basis NNI
Cabibbo route.

Let `0 < m_1 < m_2 < m_3` be arbitrary positive masses and let
`c_12, c_23 > 0` be arbitrary geometric-basis NNI off-diagonal
coefficients. Define

```text
M_ij^geom = c_ij^geom sqrt(m_i m_j)
c_13^geom = c_12 c_23
Phi_ij(c_ij^geom) = c_ij^phys = c_ij^geom sqrt(m_i / m_j),  i < j.
```

Then the following identities hold identically:

| ID | Identity | Status |
|---|---|---|
| T1 | `sqrt(m_1/m_3) = sqrt(m_1/m_2) sqrt(m_2/m_3)` | algebraic identity |
| T2 | `M_13^geom / (M_12^geom M_23^geom) = 1/m_2` when `c_13^geom = c_12 c_23` | algebraic identity |
| T3 | `Phi_13(c_13^geom) = Phi_12(c_12) Phi_23(c_23)` | algebraic identity |
| T4 | `c_13^phys / c_13^geom = sqrt(m_1/m_3)`, independent of `c_12, c_23` | algebraic identity |

The proof is internal to the displayed definitions. No quark masses, CKM
entries, fitted coefficients, PDG values, or observed target values enter
the theorem.

## Proof

For T1,

```text
sqrt(m_1/m_2) sqrt(m_2/m_3) = sqrt(m_1 m_2 / (m_2 m_3))
                            = sqrt(m_1/m_3).
```

For T2, with `c_13^geom = c_12 c_23`,

```text
M_13^geom / (M_12^geom M_23^geom)
 = c_12 c_23 sqrt(m_1 m_3)
   / (c_12 sqrt(m_1 m_2) c_23 sqrt(m_2 m_3))
 = 1 / m_2.
```

For T3,

```text
Phi_13(c_13^geom)
 = c_12 c_23 sqrt(m_1/m_3)
 = c_12 c_23 sqrt(m_1/m_2) sqrt(m_2/m_3)
 = Phi_12(c_12) Phi_23(c_23),
```

where the middle equality is T1.

For T4,

```text
c_13^phys / c_13^geom
 = (c_13^geom sqrt(m_1/m_3)) / c_13^geom
 = sqrt(m_1/m_3).
```

The final expression contains no `c_12` or `c_23`, so the gap factor is
coefficient-independent on this structural surface.

## Source Boundary

This exact-support note does not derive:

- quark masses;
- fitted geometric NNI coefficients;
- the CKM matrix;
- the Cabibbo angle;
- a Jarlskog invariant;
- Wolfenstein parameters.

It only proves the framework-local algebraic identities used when the older
Cabibbo runner applies the mass-basis NNI normalization. Any numerical
Cabibbo comparison remains a bounded/import-dependent illustration unless
the mass inputs and NNI coefficients are separately derived on the framework
surface.

## Relationship To The Cabibbo Work-History Note

`docs/work_history/ckm/CABIBBO_BOUND_NOTE.md` may cite this file for the
structural NNI identities T1-T4. It may not use this file as a first-principles
derivation of the numerical value `|V_us| = 0.2251`, because that value still
depends on imported quark masses and calibrated NNI coefficients in the
historical runner.

## Verification

Run:

```bash
python3 scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py
```

The runner performs symbolic checks of T1-T4 with positive SymPy symbols and
deterministic exact rational controls. It intentionally contains no PDG or
fitted CKM constants.
