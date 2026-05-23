# Topological-Instanton Infrastructure — Named Non-Derivation Imports

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Status:** bounded named-import umbrella wrapper for four textbook
results from Yang-Mills topological-instanton infrastructure consumed
by the external narrow theorem notes covering 4D instanton action,
meron half-action, fractional instantons on twisted `T^4`, and
fractional-instanton dilute-gas condensates.
**Status authority:** independent audit lane only.

## Purpose

This wrapper note documents four textbook Yang-Mills /
gauge-topology results as named non-derivation imports so downstream
external narrow theorem notes (notably
`INSTANTON_4D_ACTION_8PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`,
`MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`,
`FRACTIONAL_INSTANTON_DILUTE_GAS_CONDENSATE_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`)
can register a one-hop dependency rather than carry the four textbook
results as unattributed external citations. (Downstream consumers
backticked here to avoid length-2 cycles — load-bearing citation
direction is *downstream theorem → this textbook import*, recorded in
each consumer's "## Upstream authority" section.)

## Imports covered

### 1. Bogomolny bound and BPST `|Q| = 1` solution

Statement: for a Euclidean Yang-Mills field with second Chern number
`Q = (1 / 8 pi^2) ∫ tr(F ∧ F)`, the Euclidean Yang-Mills action
satisfies the **Bogomolny bound**

```
S_E  =  (1 / 4) ∫ tr(F ∧ *F)  >=  (8 pi^2 / g^2)  |Q|,
```

with equality saturated when `F = +/- *F` (self-dual or anti-self-dual).
The **BPST instanton** (Belavin, Polyakov, Schwartz, Tyupkin 1975) is
the canonical `|Q| = 1` solution of the self-dual equation on `R^4`
with `S_E = 8 pi^2 / g^2`.

References: A. A. Belavin, A. M. Polyakov, A. S. Schwartz,
Yu. S. Tyupkin, "Pseudoparticle Solutions of the Yang-Mills
Equations," *Phys. Lett. B* **59**, 85 (1975); E. B. Bogomolny,
"Stability of classical solutions," *Sov. J. Nucl. Phys.* **24**, 449
(1976).

Role: provides the bound `S_E >= (8 pi^2 / g^2) |Q|` and the saturation
configuration that fixes the canonical `8 pi^2 / g^2` 4D instanton
action.

### 2. Atiyah-Singer index theorem (integrality of `Q`)

Statement: on a compact 4-manifold the second Chern number `Q` of a
Yang-Mills bundle is the **Atiyah-Singer index** of the chiral Dirac
operator coupled to the gauge field; it is a topological invariant
taking values in `Z`.

Reference: M. F. Atiyah, I. M. Singer, "The index of elliptic
operators: I-V," *Annals of Math.* **87**, 484 (1968), and subsequent
papers in the series.

Role: ensures `Q in Z` on compact Yang-Mills configurations (so that
the Bogomolny minimum `S_E = (8 pi^2 / g^2) |Q|` is quantized).

### 3. Luescher admissibility and gradient-flow lattice charge

Statement: on a four-dimensional lattice with sufficiently fine
spacing, the Luescher admissibility condition
`||1 - U_p|| < epsilon` for every plaquette `U_p` defines a smooth
sector of lattice gauge configurations on which the Wilson gradient
flow converges to a continuum-instanton charge `Q_flow in Z` matching
the continuum Atiyah-Singer index.

References: M. Luescher, "Topological structure of the QCD vacuum
revealed by overlap fermions," *Nucl. Phys. B (Proc. Suppl.)* **94**,
112 (2001); M. Luescher, "Properties and uses of the Wilson flow in
lattice QCD," *JHEP* **08**, 071 (2010).

Role: provides the lattice-side admissibility / gradient-flow
construction that recovers the continuum integer topological charge
`Q` from a discrete `T^4` lattice computation. Consumed by the meron
half-action sector (which requires twisted boundary conditions
preserved by the flow) and the fractional-instanton dilute-gas
constructions (which require admissible patching to control
fractional `Q = k / N` sectors on twisted `T^4`).

### 4. Twisted-`T^4` 't Hooft fluxes and fractional `Q = k / N`

Statement: on the 4-torus `T^4` with `'t Hooft` twist matrices
`Omega_{mu, nu}` valued in `Z_N`, the second Chern number is shifted
by a fractional contribution

```
Q  =  k / N   +   (integer)
```

with `k = (1 / 2) sum_{mu < nu} n_{mu nu} n_{rho sigma}
epsilon^{mu nu rho sigma}` determined by the twist `n_{mu nu}`.

References: G. 't Hooft, "A property of electric and magnetic flux in
nonabelian gauge theories," *Nucl. Phys. B* **153**, 141 (1979);
P. van Baal, "Some results for SU(N) gauge fields on the
hypertorus," *Comm. Math. Phys.* **94**, 397 (1984).

Role: provides the canonical fractional-topological-charge sector
`Q = k / N` on twisted `T^4` consumed by the meron half-action
external narrow theorem (`Q = 1 / 2`, action `4 pi^2 / g^2`) and the
fractional-instanton dilute-gas condensate.

## What this note does NOT claim

- This is NOT a re-derivation of any of the cited textbook results.
- This is NOT a framework-level derivation of the topological-charge
  quantization from `Cl(3)` on `Z^3` alone.
- The bounded scope is the named non-derivation import only.

## Downstream usage

This wrapper is consumed by:

- [INSTANTON_4D_ACTION_8PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md](INSTANTON_4D_ACTION_8PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md) — uses Bogomolny + BPST + Atiyah-Singer + Luescher.
- [MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md](MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md) — uses Luescher + twisted-`T^4` `'t Hooft / van Baal` for the `Q = 1/2`, `S = 4 pi^2 / g^2` sector.
- [FRACTIONAL_INSTANTON_DILUTE_GAS_CONDENSATE_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md](FRACTIONAL_INSTANTON_DILUTE_GAS_CONDENSATE_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md) — uses Luescher + twisted-`T^4` `'t Hooft / van Baal` for fractional `Q = k / N` sectors on twisted `T^4`.

## Boundary

This wrapper note is a named-import-only bounded theorem covering
four textbook gauge-topology imports. It does not claim:

- a framework derivation of any of the imported textbook theorems;
- closure of any downstream external narrow theorem;
- a tighter audit-tier status for the consumers.

Its only function is to provide a citeable one-hop authority for the
four textbook gauge-topology results so downstream external narrow
theorem notes register the imports cleanly instead of carrying them
as unattributed external citations.
