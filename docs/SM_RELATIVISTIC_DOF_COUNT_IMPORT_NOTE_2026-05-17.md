# Standard-Model Relativistic Degrees-of-Freedom Count — Literature-Conditioned Inventory and Finite Arithmetic

**Date:** 2026-05-17; narrowed 2026-05-26; literature attribution added
2026-07-19
**Claim type:** bounded_theorem
**Author status:** bounded support theorem; independent re-audit required.
The physical inventory and thermal interpretation remain load-bearing
literature inputs, so this revision does not claim retained closure.
**Runner:** [`scripts/frontier_sm_relativistic_dof_finite_inventory.py`](../scripts/frontier_sm_relativistic_dof_finite_inventory.py)
**Status authority:** independent audit lane only.

## Purpose

The exact arithmetic is

```text
28 + (7/8) * 90 = 427/4 = 106.75.
```

The non-arithmetic inputs are the Standard-Model state inventory and the
idealized high-temperature conditions under which those states contribute as
relativistic thermal degrees of freedom. This revision gives those inputs
exact literature attribution and states their scope. It does not turn them
into framework-derived content, an axiom, an approved primitive, or another
premise type.

Conditional on the literature-supplied inventory and thermal assumptions
below, and using the retained fermion/boson thermal factor supplied by
[`HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md),
the finite arithmetic gives `g_* = 106.75`.

## Literature Inputs and Scope

The following exact source locations were checked for this revision. They are
standard/literature inputs, not framework derivations and not
chain-satisfying premises merely because they are cited.

| source | exact item used | statement used conditionally here |
|---|---|---|
| E. Husdal, “On Effective Degrees of Freedom in the Early Universe,” *Galaxies* **4** (2016) 78, [doi:10.3390/galaxies4040078](https://doi.org/10.3390/galaxies4040078), [arXiv:1609.04979](https://arxiv.org/abs/1609.04979) | Section 3 and Table 1; Sections 4.3–4.5 | Table 1 gives the conventional Standard-Model degeneracies; Section 3 totals them as `28` bosonic and `90` fermionic degrees of freedom at high temperature. Sections 4.3–4.5 state the equilibrium ideal-gas treatment, the approximation that chemical potentials are set to zero, the ultrarelativistic limit, and the fermion weighting for energy density. |
| M. Giovannini, *A Primer on the Physics of the Cosmic Microwave Background*, [arXiv:astro-ph/0703730](https://arxiv.org/abs/astro-ph/0703730) | Appendix B.4, pp. 159–160, Eqs. (B.40)–(B.43), including the intervening count on p. 160 | For a thermodynamic-equilibrium plasma with restored electroweak symmetry, it expands the quark count as `6*2*2*3=72`, gives `18` leptonic states, expands the bosonic count as `16+8+4=28`, totals the fermions as `90`, and obtains `g_rho=g_s=106.75`. |

The conditional physical scope is:

- minimal Standard Model particle content with three generations and one
  complex Higgs doublet;
- no thermally populated sterile/right-handed-neutrino states;
- a thermodynamic-equilibrium ideal plasma with chemical potentials neglected;
- temperature high enough that the listed species are ultrarelativistic and
  electroweak symmetry is restored; and
- the free-particle state-count value, excluding interaction, finite-mass,
  threshold, decoupling, and beyond-Standard-Model corrections.

The runner checks the local source locators, the note-to-inventory mapping,
and the arithmetic. It does not fetch, reproduce, or independently prove the
cited physics.

## Literature-Conditioned Inventory

Unbroken electroweak bookkeeping. The `factors` column is the local
machine-readable inventory consumed by the runner.

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
states + `1` Higgs scalar state = `28`. This is only a finite bookkeeping
equality, not a thermal-phase derivation.

## Boundary

This row claims exact finite arithmetic conditional on the explicitly named
literature inputs and thermal scope above. The citations remove anonymous
attribution; they do not close the existing conditional audit by themselves.
In particular, this literature-conditioned inventory is not a framework
derivation of which particles nature contains.
The row does not claim:

- a framework derivation of the Standard Model particle inventory;
- a framework derivation of the fermion thermal factor;
- that electroweak thermal equilibrium follows from framework primitives;
- applicability at arbitrary temperature, chemical potential, or decoupling
  history;
- inclusion of interaction corrections or beyond-Standard-Model species;
- an exact interacting Standard Model equation of state;
- closure of any downstream dark-matter/leptogenesis row;
- a new axiom, approved primitive, document-authority role, or audit verdict.

Downstream physical use of `g_* = 106.75` must carry the literature imports
and the complete conditional scope. Under the current premise policy, the
inventory remains a non-satisfying condition unless a retained derivation or
bridge supplies it.

## Import Classification

The Husdal and Giovannini items are load-bearing `standard/literature
correction` inputs with the narrow role `physical inventory and thermal-count
interpretation`. They are explicitly disclosed and scope-limited. They do not
provide framework derivation closure for Standard Model particle content.

Additional references are context only:

- Kolb & Turner, *The Early Universe* (1990), Table 3.1.
- Mukhanov, *Physical Foundations of Cosmology* (2005), Ch. 3.

## Downstream Usage

This bounded arithmetic wrapper is consumed by thermal-side rows that need the
`g_*` count, including the dark-matter/leptogenesis equilibrium and `H_rad`
lanes. Those rows must cite the exact conditional scope above, not treat
`106.75` as temperature-independent or framework-derived.

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
