# Standard-Model Relativistic Degrees-of-Freedom Count — Registered Physical-Input Bridge and Finite Arithmetic

**Date:** 2026-05-17; narrowed 2026-05-26; authority bridge added 2026-07-19
**Claim type:** bounded_theorem
**Author status:** exact support; independent re-audit required. Effective
status remains audit-lane-owned; this note does not author an audit verdict.
**Runner:** [`scripts/frontier_sm_relativistic_dof_finite_inventory.py`](../scripts/frontier_sm_relativistic_dof_finite_inventory.py)
**Status authority:** independent audit lane only.

## Purpose

The audit blocker was not the arithmetic `28 + (7/8) * 90 = 106.75`;
it was that the one-hop packet did not establish the Standard-Model inventory
or its interpretation as relativistic thermal states. This revision addresses
that named bridge at the conventional-physics boundary: the exact inventory
and high-temperature interpretation below are tied to two located standard
references, while the runner checks that the source-backed factors reproduce
the displayed totals and rational sum.

This note records a bounded physical-input bridge and finite arithmetic
certificate. Given the explicitly scoped ideal-gas Standard Model inventory
established by the authority packet below, and using the retained fermion/boson thermal factor
supplied by
[`HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md),
the effective relativistic count is `g_* = 106.75`.

The Standard Model inventory remains an external physical input, now supplied
through an exact, auditable literature-authority packet rather than an
unattributed declaration. This certificate is not a framework derivation of
which particles nature contains and does not add an axiom, approved primitive,
or admission registry.

## Registered physical-input authority and scope

This Class-C note is registered in
[`docs/audit/data/doc_authority_registry.json`](audit/data/doc_authority_registry.json).
Under the document-authority policy, registration gives no premise weight by
itself: only this scope-pinned claim can acquire weight after independent
audit. The target row records `authority_role =
scope_pinned_external_physical_input`, `pre_audit_premise_weight = none`, and
the exact source locators below. Those fields make the physical-input packet
machine-visible without turning it into an axiom, an approved primitive, or an
accepted premise. The external physical-input role is carried by the following
exact source items.

| source | exact item used | physical-input statement supplied here |
|---|---|---|
| E. Husdal, “On Effective Degrees of Freedom in the Early Universe,” *Galaxies* **4** (2016) 78, [doi:10.3390/galaxies4040078](https://doi.org/10.3390/galaxies4040078), [arXiv:1609.04979](https://arxiv.org/abs/1609.04979) | Table 1 and Sections 3, 4.4, and 4.5 | Table 1 gives the Standard Model degeneracies; Section 3 totals them as `28` bosonic and `90` fermionic degrees of freedom when all Standard Model particles are present; Sections 4.4–4.5 identify the ultrarelativistic, zero-chemical-potential equilibrium weighting for energy density. |
| M. Giovannini, *A Primer on the Physics of the Cosmic Microwave Background*, [arXiv:astro-ph/0703730](https://arxiv.org/abs/astro-ph/0703730) | Appendix B.4, pp. 159–160, Eqs. (B.40)–(B.43) | For an electroweak-symmetric Standard Model plasma in thermodynamic equilibrium, it expands the quark count as `6*2*2*3=72`, gives `18` leptonic states, expands the bosonic count as `16+8+4=28`, totals the fermions as `90`, and obtains `g_rho=g_s=106.75`. |

The bounded physical scope certified here is:

- the minimal Standard Model particle content with three generations and one
  complex Higgs doublet;
- no thermally populated sterile/right-handed-neutrino states;
- a thermodynamic-equilibrium, zero-chemical-potential ideal plasma;
- temperature high enough that the listed species are ultrarelativistic and
  electroweak symmetry is restored; and
- the free-particle state-count value, with interaction, finite-mass, threshold,
  and beyond-Standard-Model corrections excluded.

Within exactly that scope, the external sources establish both the inventory
multiplicities and why those multiplicities are the thermal state count. The
runner verifies the local source-to-row mapping and the arithmetic, but does
not pretend to reproduce or independently prove the cited physics.

## Authority-backed inventory

Unbroken electroweak bookkeeping. The `factors` column is the canonical local
machine-readable inventory consumed by the runner; the prose column explains
the physical interpretation.

| sector | interpretation | factors | relativistic states |
|---|---|---:|---:|
| gluons | 8 adjoint color states, each with 2 transverse polarizations | `8 * 2` | `16` |
| `SU(2)_L` gauge bosons | 3 gauge bosons, each with 2 transverse polarizations | `3 * 2` | `6` |
| `U(1)_Y` gauge boson | 1 gauge boson with 2 transverse polarizations | `1 * 2` | `2` |
| complex Higgs doublet | 4 real scalar components | `4` | `4` |

Therefore `g_bosonic = 16 + 6 + 2 + 4 = 28`.

Fermionic bookkeeping:

| sector | interpretation | factors | relativistic states |
|---|---|---:|---:|
| quarks | 6 flavors, 3 colors, 2 spin states, particle/antiparticle | `6 * 3 * 2 * 2` | `72` |
| charged leptons | 3 flavors, 2 spin states, particle/antiparticle | `3 * 2 * 2` | `12` |
| active neutrinos | 3 flavors and 2 helicity/antiparticle states | `3 * 2` | `6` |

Therefore `g_fermionic = 72 + 12 + 6 = 90`.

With the retained fermion weight `7/8`,

```text
g_* = g_bosonic + (7/8) g_fermionic
    = 28 + (7/8) * 90
    = 427/4
    = 106.75.
```

The broken-phase bookkeeping has the same bosonic total:
`16` gluon states + `2` photon states + `9` massive `W+, W-, Z` vector
states + `1` Higgs scalar state = `28`. This is recorded only as a finite
bookkeeping equality, not as a thermal-phase derivation.

## Boundary

This row claims the source-backed conventional inventory and finite arithmetic
only within the registered physical scope above. It does not claim:

- a framework derivation of the Standard Model particle inventory;
- a framework derivation of the fermion thermal factor;
- that electroweak thermal equilibrium follows from framework primitives;
- applicability at arbitrary temperature, chemical potential, or decoupling
  history;
- inclusion of interaction corrections or beyond-Standard-Model species;
- an exact interacting Standard Model equation of state;
- closure of any downstream DM-leptogenesis row;
- any new axiom or audit verdict.

Downstream physical use of `g_* = 106.75` must carry the registered scope
honestly. This row converts an unattributed hard-coded assumption into a
located external physical-input bridge plus exact arithmetic; it does not
convert the conventional Standard Model content into a framework derivation.

## Literature classification

The two located sources above are `literature theorem` inputs with the narrow
role `physical inventory and thermal-count bridge`. They supply the external
authority for the bounded conventional-physics scope of this note;
they do not provide framework derivation closure for Standard Model particle
content. Additional references are context only:

- Kolb & Turner, *The Early Universe* (1990), Table 3.1.
- Mukhanov, *Physical Foundations of Cosmology* (2005), Ch. 3.

## Downstream Usage

This bounded wrapper is consumed by thermal-side rows that need the `g_*`
count, including the DM-leptogenesis equilibrium and `H_rad` lanes. Those rows
must cite the exact registered scope above, not treat `106.75` as a
temperature-independent or framework-derived value.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_sm_relativistic_dof_finite_inventory.py
```

Expected result:

```text
SM relativistic DOF finite inventory certificate: PASS
PASS=<n> FAIL=0
```
