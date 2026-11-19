---
claim_id: zero_shift_with_slips_fails_on_rotating_flows_because_slips_never_move_the_loci_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the zero-shift frame with one-cube slips (whole-site relabellings) under a differentially rotating (frame-dragging) flow w(r) ~ r^-3: a one-cube slip sigma(x) = x + b on a region S is a bijection of the sites iff S + b = S, so a slip face that ends is no relabelling (12 x 12 torus check: 144/144 against 139/144 images); slips permute contents among fixed loci, so the loci are the flow image, locally the lattice A Z^d with A = R(w t)(1 + g u n^T), g = r w' t = -3 w t (symbolic); if that lattice has shortest vector lam1 < 1/2 its points lie on lines more than 2 apart, so no relabelling, slip or dislocation builds an in-window cell at unit density (gap lemma; minimum-spanning-tree check 3.335 against 3.333); an azimuth along lattice direction (p, q) is a closed horocycle reaching lam1 = 1/sqrt(p^2 + q^2), so only axis and diagonal shear directions stay in the window; the slip rule on both face orientations equals Lagrange-Gauss reduction (3000 lattices, 0 left with shear > 1/2); a bare slip breaks Gauss's law on the face rows and a flux string along the face restores it (10 x 10 classical check). Finite diagnostics: the out-of-window fraction of (azimuth, g) rises from 0 at g ~ 0.5 to about 0.24 (3/(4 pi) = 0.239) and matches the exact-flow-image fraction for g = 2, 4; in 3D it saturates near 0.16. Hence zero shift with slips fails on rotating flows. Estimates against Earth's and the Sun's frame dragging (GP-B, LAGEOS orbits) are estimates. Supplied model, finite diagnostic: zero shift on zero-angular-momentum observers, the window ratio 2 at unit density, the cell-area floor 1/2, a classical integer electric field, the measured J, R, ages and orbits."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/zero_shift_with_slips_fails_on_rotating_flows_because_slips_never_move_the_loci_2026_10_22.py
---

# Zero shift with slips fails on rotating flows because slips never move the loci

Claim type: bounded_theorem.
Primary runner: `scripts/zero_shift_with_slips_fails_on_rotating_flows_because_slips_never_move_the_loci_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. A causal, parameter-free frame for the update law is zero shift (the labels ride the normal observers) with one-cube slips: when a face's crossing shear passes 1/2, every site on one side is relabelled by one cube, which is a lattice automorphism and needs no rate parameter. In planar shear this keeps every cube within shear 1/2. This note asks whether the same holds on a differentially rotating flow, where frame dragging gives the zero-angular-momentum observers angular velocity w(r) = 2GJ/(c^2 r^3). The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Theorems.

1. A one-cube slip sigma(x) = x + b on a region S, identity elsewhere, is a relabelling (a bijection of the sites) iff S + b = S. A slip face that ends is no relabelling: its end must create or destroy sites and records, and a dislocation is an edit of the lattice axiom.
2. Under zero shift the labels carry the frame-dragging flow, so the label metric is a simple shear with g = r w'(r) t along (azimuth, radius), g = -3 w t for w ~ r^-3. Slips permute contents among fixed loci; they never move a locus. The loci are therefore the flow image of the initial lattice whatever the slips do: locally the lattice A Z^d with A = R(w t)(1 + g u n^T).
3. Gap lemma. If the local loci form a lattice with shortest vector lam1 < 1/2, its points lie on lines spaced 1/lam1 > 2. Any connected graph on them (any relabelling, any slip, with or without dislocations) has an edge of length at least 1/lam1, and a cell with all edges below 1/lam1 has its corners on one line (zero volume). At unit density this is outside every window of ratio 2.
4. An azimuth along lattice direction (p, q) is a closed horocycle of period p^2 + q^2 in g that reaches lam1 = 1/sqrt(p^2 + q^2). Axis and diagonal azimuths (the planar toy's directions) never leave the window; every other one does.
5. Slip on the azimuthal face at rate r w' removes the whole shear rate but leaves the lattice spinning at w(r). The runner computes the residual stretching (zero) and the lattice spin (w(r)); it states, and does not compute, that the orientation gradient then grows as w' t = g/r, a geometrically necessary dislocation density g/r of one sign that cannot annihilate, laid down on a cubic staircase where the slip face turns.
6. The slip rule on both face orientations (slip when a face's crossing shear passes 1/2) is the Lagrange-Gauss reduction: each slip shortens an edge, the rule stops at a reduced cell with shear at most 1/2, and what it leaves (the aspect 1/lam1^2) belongs to the loci, not the labels.
7. A bare slip breaks Gauss's law at the face rows (the crossing link pairs a site with a new partner). A flux string along the face restores it exactly, so a slip must be a covariant translation (contents carried with the in-face parallel transporter). The mismatch sums to zero along each face row because the face flux is unchanged.

B. Finite diagnostics.

8. The fraction of (azimuth, g in [g0, 2 g0]) with lam1 < 1/2 rises from 0 and saturates near 3/(4 pi) = 0.239. The runner quotes this value as the probability that a random unimodular planar lattice has lam1 < 1/2 (from the equidistribution of long horocycles); it compares against it and does not derive it. The worst row gap round a ring keeps growing.
9. On the exact zero-shift loci (no linearisation; annulus r in [3000, 3012]) the region where no relabelling can build a cell of half the unit area with edges below 2 appears once g ~ 1 and matches the horocycle fraction while g^3 << r. At g = 8 (g^3/r = 0.17) the rows curve, and the triangle test becomes a lower bound.
10. In 3D (random position, shear azimuth x radius) lattice planes of the loci more than 2 apart (dual lam1 < 1/2) appear once g ~ 1 and saturate near 0.16, below the Siegel mean 0.218 (an upper bound on the probability, quoted): the 3D flow is no kinder.

Hence zero shift with slips fails on rotating flows: the loci themselves leave the window, and no relabelling of contents among them can repair that.

## Derivation

Item 1 builds the slip map on a 12 x 12 torus for a band of rows (spanning the torus) and a half-row segment (a face that ends) and counts distinct images. Items 2 and 5 are sympy (the pullback metric of the rotation by w(r) t at (r, 0); the elastic stretching and spin after subtracting the slip rate). Item 3 builds a lattice with lam1 = 0.3 and takes the bottleneck of its minimum spanning tree. Items 4, 6 and 8 use a vectorised Lagrange-Gauss reduction of the sheared basis; item 6 runs the face-slip rule on 3000 random sheared lattices and compares with the reduction. Item 9 rotates every integer point of the annulus by its own angle (g0/3)(3000/r)^3 and, for every third interior point, takes the largest triangle with two neighbours closer than 2 (a cell-corner test). Item 10 applies LLL reduction to the dual of 1 + g u n^T for 700 random positions per g0. Item 7 shifts a band of a 10 x 10 integer electric field and charge pattern by one cube and adds the cumulative mismatch along each face row.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Slip bijection: band 144/144 images; half-row segment 139/144.
- Label metric [[1 + g^2, g], [g, 1]] at (r, 0); g/(w t) = -3 (symbolic).
- Gap lemma at lam1 = 0.3: minimum-spanning-tree bottleneck 3.335 against row spacing 3.333.
- Closed horocycles, minimum lam1: (1, 0) 1.000, (1, 1) 0.707, (2, 1) 0.447, (3, 1) 0.316, (3, 2) 0.277.
- Azimuthal-face slip: residual stretching [0, 0, 0, 0], lattice spin = W(r) (symbolic).
- Slip rule = Lagrange-Gauss: 3000 lattices, 55473 slips, shear > 1/2 left 0, longest-edge difference from the reduction 3e-13; aspect up to 402.
- Gauss's law: bare slip 16 violations on rows [3, 7]; covariant slip 0.

Finite diagnostics (supplied model, finite diagnostic):
- Out-of-window fraction (40000 samples per g0): g0 = 0.5: 0.000, 2: 0.204, 8: 0.239, 32: 0.237, 128: 0.241 (against 0.239).
- Largest row gap 1/lam1 round a ring: g0 = 0.5: 1.3, 2: 2.4, 8: 8.1, 32: 32.0, 128: 105.4.
- Exact flow image (about 226k loci; the count is printed as a fixed label), no in-window cell corner against linear lam1 < 1/2: g = 0.5: 0.000/0.000, 2: 0.151/0.148, 4: 0.212/0.212, 8: 0.110/0.238 (lower bound at g = 8).
- 3D dual planes more than 2 apart: g0 = 0.5: 0.000, 8: 0.163, 64: 0.159; Siegel mean 0.218.

The random draws use a fixed seed (20261022).

## Estimates against measurement

Estimates with supplied inputs (cube = sqrt(8 pi) l_P = 8.1e-35 m, age 1.4e17 s, measured J and R; g = 2 taken as the onset, where the out-of-window fraction already exceeds 0.1):
- Earth: surface g 1.4e+04; the loci leave the window out to r = 19 R (equator); GP-B at 1.10 R has g 1e+04, LAGEOS at 1.93 R has g 2e+03. Earth's surface reached g = 2 after 6e+05 yr.
- Sun: surface g 3.5e+05; the loci leave the window out to r = 56 R.
- Read as dilute dislocations instead: density 2e-37 per cube^2 with spacing 2e-16 m (Earth), 4e-38 per cube^2 with spacing 4e-16 m (Sun).
- Frame dragging is measured where the shear is far into the saturated regime (GP-B 37 +- 7 mas/yr against GR 39, quoted, not computed), with g^3 ~ 1e12 << r ~ 1e41 cubes, so the linear regime applies; there 15-24% of the loci (3D, 2D) admit no in-window cell under any relabelling.
- The runner states, and does not compute, that zoom does not help: the local lattice's shape depends on g only, which is the same at every rung (a block lattice 2^j Z^3 rides the same flow), so the out-of-window fraction is rung-independent.

## Boundary

Not claimed: a slip or shift law built on registers or quantum links; the corrected shift that would replace zero shift; any statement about dislocations beyond item 5's stated reading; rotating flows other than w ~ r^-3 at the linear frame-dragging level; the equidistribution value 3/(4 pi) and the Siegel mean as derived here (both quoted); the rung-independence statement (stated, not computed); experimental exclusion beyond the order-of-magnitude estimates. Planar shear along an axis or a diagonal is not affected (item 4).

## Supplied vs forced

Supplied: zero shift with loci on zero-angular-momentum observers, w = 2GJ/(c^2 r^3); the window ratio 2 at unit density; the cell-area floor 1/2 in item 9; the classical integer electric field in item 7; the onset g = 2; the measured J, R, ages and orbit radii; the quoted GP-B values. Forced, given those: slips are bijections only if their faces do not end; slips never move the loci; the gap lemma; the closed-horocycle minima; the equality of the slip rule and Lagrange-Gauss reduction; the flux-string repair of Gauss's law; the residual lattice spin w(r).

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. Item 1 uses that sites and records are neither created nor destroyed. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's window and its zero-shift-with-slips frame; the link registers' Gauss law. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/zero_shift_with_slips_fails_on_rotating_flows_because_slips_never_move_the_loci_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 2 s with about 210 MB resident, prints about 5.6 kB and ends with `TOTAL: PASS=12 FAIL=0`. Its random draws use a fixed seed; two repeated runs gave identical output apart from the elapsed-time line.
