# Assumptions and Imports — monopole-derived-note 2026-05-16

## Adopted ledger for this loop

The monopole derivation chain is honest only when each input is labeled by
its role: framework axiom, derived consequence, or non-derivation import.

### Lattice axioms (no new axioms required)

1. **Cl(3) on Z^3 with edge-valued U(1) phase** — gauge field is
   `theta_{edge} in [0, 2*pi)`. This is a framework axiom on the accepted
   physical-lattice reading. **No new axiom is added by this loop.**

### Derived consequences (no import needed)

2. **Compactness of U(1) on the lattice** — follows from edge being a
   group element exp(i*theta).
3. **Magnetic charge quantization** — m(cube) is integer for every cube,
   for every configuration. Verified numerically on 100 random L=8 configs.
4. **Dirac quantization e*g = 2*pi** — follows from 2-pi periodicity of theta.
5. **Existence of monopole as topological excitation** — `pi_1(U(1)) = Z`
   via the compact lattice avatar.
6. **Lattice Coulomb Green's function at origin G_lat(0) = 0.2527** —
   sum over non-zero lattice momenta of 1/hat{k}^2 on Z^3 (BKM cubic-lattice
   value, verified by the runner at L=64 to 4 significant figures).
7. **Self-energy formula shape M_mono = c * beta * (1/a)** with c = G_lat(0)
   — Banks-Myerson-Kogut 1977, Polyakov 1977. The shape is exact for the
   compact-U(1) Wilson action; the coefficient c depends on the lattice
   geometry but not on the coupling.

### Non-derivation imports (named explicitly)

8. **Wilson action** — simplest compact U(1) action S = -beta * sum cos(Phi_P).
   Role: action choice. Other compact actions (Villain, improved) would shift
   c_lat by O(10%) but stay in the same Planckian band. Not derived from
   axioms.
9. **Planck-scale package pin a^(-1) = M_Pl** — on the accepted
   physical-lattice reading. Role: scale identification. Not derived in this
   note; carried as a package pin elsewhere in the framework.
10. **alpha_EM(M_Pl) from one-loop SM RG running from alpha_EM(M_Z) = 1/127.9
    with b_EM = -80/9** — gives alpha_EM^{-1}(M_Pl) ~ 72.1. Role: bridge
    import for the numerical prefactor `beta = 1/(4*pi*alpha_EM(M_Pl)) ~ 5.74`.
    This is the load-bearing import flagged by the auditor: the headline
    "1.43 M_Pl" depends linearly on this value. Two-loop running and
    threshold-matching corrections are not implemented; the prefactor
    therefore inherits the uncertainty in this extrapolation. **Not derived
    from lattice axioms.**

### Cosmology imports (overclosure section)

11. **Standard FRW cosmology with entropy conservation** for the Omega_mono
    calculation. Standard but not derived from the lattice axiom packet.
12. **Kibble mechanism at the graph-growth epoch** — one monopole per
    correlation volume at field formation. Standard topological-defect
    cosmology.

## Counterfactual pass

For each non-derivation import, what does the alternative direction open?

| Import | Alternative | Direction opened |
|---|---|---|
| Wilson action | Villain / improved | shift c_lat by O(10%); does not change Planckian band |
| a^(-1) = M_Pl pin | Sub-Planckian a^(-1) | M_mono drops linearly; need a different argument that lattice spacing IS Planck-scale |
| alpha_EM(M_Pl) one-loop | Two-loop / threshold | shifts beta by O(10-30%); does not change order of magnitude |
| alpha_EM(M_Pl) one-loop | non-perturbative / Landau pole reached | the import breaks; the linear formula c*beta*M_Pl is no longer the right framework, but the order-of-magnitude M ~ M_Pl persists from the lattice-scale argument |

The **order-of-magnitude prediction M_mono ~ M_Planck** is robust across the
full plausible alpha_EM(M_Pl) range (alpha^{-1} in [30, 60] gives M_mono in
[0.60, 1.21] M_Pl). The **exact numerical prefactor "1.43"** is conditional
on the specific one-loop SM RG extrapolation.

## Implication for claim type

- The shape `M_mono = c_lat * beta * M_Pl` with `c_lat = 0.2527` derived from
  the lattice Coulomb Green's function is a **bounded theorem**: closed
  derivation given the imports.
- The numerical headline `M_mono = 1.43 M_Planck` is **bounded support** with
  alpha_EM(M_Pl) as an explicit non-derivation import.
- The order-of-magnitude statement `M_mono ~ M_Planck` is the **robust**
  cross-import headline.

## Step 4 numerical "cross-check" — what it actually does

The auditor flagged that the runner's Step 4 (direct numerical Wilson action
on L = 6..12 lattices) returns Delta S of order 246-444 and a derived
"M / M_Pl" of order 400-700. This DOES NOT validate the analytic 1.43 M_Pl;
the gap is 2-3 orders of magnitude.

Honest explanation (the original note did not give this clearly):

The function `_construct_monopole_config` builds a continuum Wu-Yang style
gauge potential `A_phi = g (1 - cos_th) / (2 r sin_th)` around each
monopole, then projects it onto the lattice edges. This vector potential
is **Dirac-string singular**: its discrete curl produces large plaquette
fluxes near the z-axis "string", which the bare Wilson action `S = -sum_P
cos(Phi_P)` then assigns large action density to. The bulk of `Delta S` is
**string action**, not monopole self-energy.

A correct numerical measurement of the BKM coefficient `c_lat ~ 0.2527`
requires either:

- Monte Carlo sampling of the partition function and extracting the
  free-energy difference (not just the bare action of one configuration);
- explicitly subtracting the Dirac-string contribution (DeGrand-Toussaint
  dual-lattice prescription, or `M(beta) -> infinity` excited-link
  resummation);
- working in the Villain formulation where the string is gauged away
  exactly.

None of these is implemented in the current runner, and implementing them
correctly is its own multi-day numerical project. The runner's Step 4
therefore should NOT be presented as a quantitative cross-check of the
analytic prefactor. It IS a valid **topology check** that the constructed
configuration:

- carries the intended integer monopole-antimonopole charges (Step 1);
- satisfies Gauss's law globally (total charge = 0).

Both of those pass for every L in {6, 8, 10, 12}, which the runner already
verifies and prints.

## Adopted scope for this note

- **Step 1** (compactness, integer charges): derived theorem, retained-class
  consequence.
- **Step 2** (Dirac quantization): derived theorem.
- **Step 3** (analytic self-energy via lattice Coulomb Green's function):
  derived modulo the named non-derivation imports (Wilson action, Planck pin,
  alpha_EM(M_Pl)). c_lat = 0.2527 itself is closed lattice arithmetic.
- **Step 4** (numerical configuration on small L): re-scoped to a **topology
  check** of the constructed configuration, not a self-energy measurement.
  Bare Wilson action values reported with an explicit note that they are
  dominated by Dirac-string artifacts.
- **Step 5** (overclosure / inflation requirement): bounded consequence given
  Step 3's M_mono ~ M_Pl and the cosmology imports.

This is a **bounded support / bounded theorem** package, not retained flagship.
The note's existing publication disposition (`bounded companion only`) is
already consistent with that scope; this iteration aligns the in-note
language with that disposition.
