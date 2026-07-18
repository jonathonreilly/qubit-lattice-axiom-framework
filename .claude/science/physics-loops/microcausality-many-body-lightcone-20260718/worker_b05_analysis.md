# Exact adjacency/reach enumeration for bonds and plaquettes on Z^3

## Scope and conventions

This report treats a walk of length `k` as a sequence of exactly `k` terms `(T_1, ..., T_k)`. Consecutive terms must be distinct and share at least one lattice site. “Mixed” means that both bonds and faces are allowed at every position; it does not require a type change. The fixed site is `X = (0,0,0)`, the fixed bond is `{(0,0,0),(1,0,0)}`, and the fixed face is the unit square in the `xy` plane anchored at the origin.

The enumeration is performed independently in centered boxes `[-R,R]^3` for `R = 4` and `R = 6`. Only terms whose full supports lie in the box are generated. All requested local and reach quantities are compared across the two radii.

## Verbatim script output

```text
=== CENTERED BOX radius=4, coordinates=[-4,4] ===
generated terms: bonds=1944, faces=1728
TABLE 1 / local incidence and adjacency
bonds incident to X: 6
faces containing X: 12
fixed bond -> adjacent bonds: 10
fixed bond -> adjacent faces: 20
fixed face -> adjacent bonds: 20
fixed face -> adjacent faces (self excluded): 32
fixed bond total degree: 30
fixed face total degree: 52
D=max(type degrees): 52
TABLE 2 / diameters and reach
bond support l1 diameter: 1
face support l1 diameter: 2
k=1: terminal terms=18, max distance=2, comparison to 2k: =
k=2: terminal terms=204, max distance=4, comparison to 2k: =
k=3: terminal terms=798, max distance=6, comparison to 2k: =
length-2 transitions bond->bond: 60
length-2 transitions bond->face: 120
length-2 transitions face->bond: 240
length-2 transitions face->face: 384
terms containing X: 18
exact length-2 mixed-walk count: 804
product bound (#start terms)*D: 936
exact count <= product bound: True

=== CENTERED BOX radius=6, coordinates=[-6,6] ===
generated terms: bonds=6084, faces=5616
TABLE 1 / local incidence and adjacency
bonds incident to X: 6
faces containing X: 12
fixed bond -> adjacent bonds: 10
fixed bond -> adjacent faces: 20
fixed face -> adjacent bonds: 20
fixed face -> adjacent faces (self excluded): 32
fixed bond total degree: 30
fixed face total degree: 52
D=max(type degrees): 52
TABLE 2 / diameters and reach
bond support l1 diameter: 1
face support l1 diameter: 2
k=1: terminal terms=18, max distance=2, comparison to 2k: =
k=2: terminal terms=204, max distance=4, comparison to 2k: =
k=3: terminal terms=798, max distance=6, comparison to 2k: =
length-2 transitions bond->bond: 60
length-2 transitions bond->face: 120
length-2 transitions face->bond: 240
length-2 transitions face->face: 384
terms containing X: 18
exact length-2 mixed-walk count: 804
product bound (#start terms)*D: 936
exact count <= product bound: True

=== BOX-STABILITY CHECK: radius 4 versus radius 6 ===
site_bonds: True
site_faces: True
bond_adj_bonds: True
bond_adj_faces: True
face_adj_bonds: True
face_adj_faces: True
bond_degree: True
face_degree: True
maximum_degree: True
bond_diameter: True
face_diameter: True
reach_rows: True
origin_terms: True
transition_counts: True
length_2_walk_count: True
product_bound: True
within_bound: True
all requested quantities stable: True
unstable keys: []
```

## Deliverable table 1: exact local counts

| Quantity | Radius 4 | Radius 6 | Stable exact value |
|---|---:|---:|---:|
| Bonds incident to one fixed site | 6 | 6 | 6 |
| Faces containing one fixed site | 12 | 12 | 12 |
| Bonds adjacent to one fixed bond | 10 | 10 | 10 |
| Faces adjacent to one fixed bond | 20 | 20 | 20 |
| Bonds adjacent to one fixed face | 20 | 20 | 20 |
| Faces adjacent to one fixed face, excluding itself | 32 | 32 | 32 |
| Total degree from a bond start | 30 | 30 | 30 |
| Total degree from a face start | 52 | 52 | 52 |
| `D = max(30,52)` | 52 | 52 | 52 |

Thus the type-specific totals are 30 for a bond start and 52 for a face start, and the maximum total term-adjacency degree is `D = 52`. Translation and coordinate-axis symmetry make the fixed representatives exhaustive for the two term types.

### Hand cross-checks for table 1

These derivations are independent checks of the values printed by the script:

- Site to bonds: three coordinate axes times two directions gives `3 * 2 = 6`. Agreement.
- Site to faces: choose one of three coordinate planes, and place the site at any of four corners, giving `3 * 4 = 12`. Agreement.
- Bond to bonds: its two endpoints each have six incident bonds. Their incident-bond sets intersect only in the fixed bond, so the union contains `6 + 6 - 1 = 11` bonds including the fixed bond; removing it gives `10`. Agreement.
- Bond to faces: each endpoint lies in 12 faces. Exactly four faces contain the whole fixed bond (two transverse coordinate directions times two sides), so the union contains `12 + 12 - 4 = 20` faces. Agreement.
- Face to bonds: the square has four perimeter bonds. At each of its four vertices, four additional incident bonds are not perimeter bonds, and these are distinct, giving `4 + 4 * 4 = 20`. Agreement.
- Face to faces: in the plane of the fixed `xy` face, the faces touching at least one of its vertices form a `3 * 3 = 9` block. For `xz` faces, each of the two fixed `y` levels contributes `3 * 2 = 6`, hence 12; `yz` faces similarly contribute 12. This gives `9 + 12 + 12 = 33` including the fixed face, hence `32` after excluding it. Agreement.
- The total degrees are consequently `10 + 20 = 30` for a bond and `20 + 32 = 52` for a face. Agreement.

## Deliverable table 2: diameters and walk reach

| Quantity | Radius 4 | Radius 6 | Stable exact value / comparison |
|---|---:|---:|---|
| Bond-support `l1` diameter | 1 | 1 | 1 |
| Face-support `l1` diameter | 2 | 2 | 2 |
| `k=1` maximum distance from `X` | 2 | 2 | `2 = 2k` |
| `k=2` maximum distance from `X` | 4 | 4 | `4 = 2k` |
| `k=3` maximum distance from `X` | 6 | 6 | `6 = 2k` |

The enumerated maximum equals the a priori `2k` bound for each requested walk length; it is neither less nor more. In particular, no bound violation was found. The script also prints the numbers of distinct possible terminal terms as 18, 204, and 798 for `k=1,2,3`, respectively, and these are stable at both radii.

### Hand cross-checks for diameters and reach

A bond's endpoints are one graph edge apart, giving diameter 1. Opposite vertices of a unit face differ by one step in each of two coordinate directions, giving diameter 2. Agreement with the enumerated diameters.

For the upper bound, start at the site `X` in `T_1`; reaching any site of `T_1` costs at most its diameter. At every transition, choose a shared site of `T_j` and `T_{j+1}` and then cross `T_{j+1}` at a cost no greater than its diameter. Since every allowed term has diameter at most 2, a `k`-term walk reaches at most `2k`.

The bound is attained by successive `xy` faces: take `T_1` anchored at `(0,0,0)`, `T_2` anchored at `(1,1,0)`, and `T_3` anchored at `(2,2,0)`. Consecutive faces share `(1,1,0)` and `(2,2,0)`, respectively, while the far corners reached after one, two, and three terms are `(1,1,0)`, `(2,2,0)`, and `(3,3,0)`, at distances 2, 4, and 6. This agrees with the brute-force maxima.

## Exact length-2 mixed-walk count

Here a length-2 walk is an ordered adjacent pair `(T_1,T_2)`, with `T_1` any term containing `X`. The script's type-resolved counts are:

| Start type | Next bond | Next face | Row total |
|---|---:|---:|---:|
| Bond | 60 | 120 | 180 |
| Face | 240 | 384 | 624 |
| Total | 300 | 504 | 804 |

The exact enumerated count is therefore 804. There are `6 + 12 = 18` possible first terms, and `D = 52`, so the requested product bound is

`(# terms containing X) * D = 18 * 52 = 936`.

Thus `804 <= 936`, as also printed by the script.

As an independent arithmetic cross-check, the six bond starts each have 10 bond and 20 face continuations, while the twelve face starts each have 20 bond and 32 face continuations:

`6 * (10 + 20) + 12 * (20 + 32) = 180 + 624 = 804`.

This agrees with both the type-resolved enumeration and the exact total.

## Box-stability result

Every requested incidence, adjacency, diameter, reach, transition-count, and product-bound field is identical at radii 4 and 6. The script reports `all requested quantities stable: True` and an empty unstable-key list. Therefore there is no box-instability flag.

## LIMITS

- Walk reach was brute-forced only for the requested lengths `k = 1,2,3`; no brute-force claim is made for larger `k`.
- The computation checks the two requested centered finite boxes, not every finite radius. Translation and coordinate symmetry are used to identify the fixed bond and fixed face with their term types.
- The count treats “mixed” as allowing either term type at each position; it does not require `T_1` and `T_2` to have different types.
