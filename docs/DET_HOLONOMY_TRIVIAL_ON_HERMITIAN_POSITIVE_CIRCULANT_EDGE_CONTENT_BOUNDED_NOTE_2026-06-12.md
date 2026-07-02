# Det-Holonomy Is Trivial on Hermitian Positive Circulant Edge Content (Bounded Wall)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_det_holonomy_trivial_hermitian_positive_circulant_2026_06_12.py`
**Cached output:** `logs/runner-cache/frontier_det_holonomy_trivial_hermitian_positive_circulant_2026_06_12.txt`
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Status:** source proposal; the audit lane grades. Runner `PASS=20 FAIL=0`.

**No-promotion statement:** this note does not promote, demote, or set the audit status of any existing row; it records a bounded source-side theorem and a named wall.

## Boundary

This note proves V1-V3 below. It does not evaluate the non-Hermitian/directed route or the off-domain sign-sector route as carrier routes. It does not close the R-eta carrier question in either direction, and it makes no claim about R-eta itself. Firewall: no R-eta claim either way; no readings, no cells; r never fixed.

The point is a named wall with its structural reason exposed: positive Hermitian edge content has trivial polar unitary. The wall identifies live routes and names them as the next path; it is not a route termination.

## The Supplied Surface

Let `C` be the 3-cycle shift matrix and consider the supplied Hermitian circulant class

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T
```

on the positivity domain `a > 2B > 0`. Its eigenvalues are
`lambda_k = a + 2B cos(delta + 2 pi k/3)`, so the domain makes every eigenvalue positive.
This is the on-site/edge content surface used along the `C_3[111]` 3-cycle in this bounded check.

The composite-link construction is the one named in context below: `U_eff = polar(M(x,y))`.
Here the supplied edge content is Hermitian positive-definite, so the composite link is tested at the Hermitian-positive corner of that construction.

## Theorem

**V1 - One-line identity [symbolic + numeric check].** For any positive-definite Hermitian matrix `P`, the polar decomposition `P = U |P|` has `U = I` exactly. Since `P^dagger = P` and `P > 0`, `|P| = (P^dagger P)^(1/2) = (P^2)^(1/2) = P`; hence `U = P |P|^-1 = P P^-1 = I`. The runner verifies this symbolically for generic `3 x 3` `P = A^dagger A + epsilon I` and by two numeric witnesses.

**V2 - Trivial det holonomy on the supplied surface [scan + harmonics + K-parity check].** For any cycle whose composite-link edge content is Hermitian positive-definite, every composite link is exactly `I`, the cycle holonomy is exactly `I`, and the determinant phase
`phi(delta) := arg det Hol` is identically zero. In particular, for the supplied circulant class on `a > 2B > 0` along the `C_3[111]` 3-cycle, the runner scans 25 `delta` values at two `(a,B)` pairs. The scan finds no constant, `cos(3 delta)`, `sin(3 delta)`, `cos(6 delta)`, or `sin(6 delta)` component to machine precision, and the K-parity decomposition is identically zero to the same tolerance.

**V3 - The named wall and the next path [negative controls + boundary check].** The det-holonomy route supplies no carrier angle on the Hermitian positive circulant surface for the structural reason V1, not for a numerical accident. The next path is named by this wall:

- **(a) Non-Hermitian / directed edge bilinears.** The induced-holonomy construction's generic cross-edge `M(x,y)` is generically non-Hermitian; the Hermitian-positive case checked here is a degenerate corner of that family.
- **(b) Off-positivity-domain sign sectors.** When some `lambda_k < 0`, the Hermitian polar factor is a nontrivial reflection, and determinant phases can be pi-valued.

Neither route is evaluated here as an R-eta carrier route. The runner includes one negative-control witness for (a) and one for (b) to keep both routes concrete as the next path.

## No-Go Discipline Gate

**Result:** PASS as a narrow bounded wall. No global det-holonomy route
termination is shipped; the two escape routes in V3 remain live.

**N1 alternative routes.**

1. Hermitian positive edge content as carrier: ruled out on this supplied
   surface by V1-V2.
2. Non-Hermitian / directed edge bilinears: not ruled out; V3 gives a
   concrete witness that the polar factor can move.
3. Off-positivity-domain sign sectors: not ruled out; V3 gives a concrete
   reflection-phase witness.
4. Direct R-eta density/readout route: not tested and not consumed here.
5. Generic induced-holonomy `M(x,y)` route: not ruled out; the Hermitian
   positive case is a degenerate corner of that broader construction.

**N2 wall independence.** The Hermitian-positivity wall, directed-edge route,
and sign-sector route are distinct domain restrictions. Closing the Hermitian
positive corner does not close the directed or sign-sector cases.

**N3 hidden-wall scan.** The note uses no observed lepton masses, fitted
selector, measure, weight, new axiom, new primitive, or audit verdict.

**N4 residual matching.** The residual is exactly the determinant phase on
Hermitian positive circulant edge content. It is not the residual for the
non-Hermitian, sign-sector, or R-eta readout routes.

**N5 rhetoric audit.** The negative statement is at the supplied
Hermitian-positive edge-content resolution and its 3-cycle composite. It is
not stated for generic edge bilinears, off-domain sectors, or lattice-wide
carrier closure.

**N6 partial-closure path.** The route can still close through either named
escape path if a future theorem supplies a physical carrier and readout bridge.
This note keeps those paths visible rather than turning the wall into an axiom
or terminal no-go.

**N7 steelman.** A hostile reviewer would say the physically relevant
composite link need not be Hermitian positive at all; directed bilinears or
sign sectors could carry the determinant phase. That counterargument is
accepted here and is the next path.

**N8 cross-cycle echo.** Similar carrier walls in the flavor/readout lanes
have been useful when they name the exact failed surface and preserve escape
routes. This note follows that pattern: it closes one supplied corner and
keeps the carrier problem open.

## Does Not

- Does not evaluate non-Hermitian/directed edge bilinears as a carrier route.
- Does not evaluate off-domain sign sectors as a carrier route.
- Does not close the R-eta carrier question in either direction.
- Does not claim anything about R-eta itself.
- Does not introduce readings, cells, a fixed r, a new axiom, a new primitive, a new measure, or a new weight.
- Does not alter the induced-holonomy source note, the R-eta chain, or any audit status.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (the framing boundary; the algebra is self-contained).

## Context

- `INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md`
  (unaudited; the composite-link construction home for `U_eff = polar(M(x,y))` and the determinant-phase open thread scoped by this wall; facts used here are reproven in the runner).
- `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  (the R-eta chain this carrier question serves; no content is consumed).

## Runner Checks

The runner performs the V1 symbolic identity, generic positive-definite numeric witnesses, circulant positivity and polar-unitary witnesses, the `25 x 2` delta scan, harmonic projection checks, K-parity checks, the two negative controls, and source-note boundary checks for the firewall, walls-move language, link inventory, context formatting, no-promotion statement, and status-authority lines.
