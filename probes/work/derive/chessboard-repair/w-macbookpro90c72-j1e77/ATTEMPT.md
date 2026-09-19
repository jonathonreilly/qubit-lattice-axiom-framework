# chessboard-repair, attempt 2 (worker w-macbookpro90c72-j1e77, model grok-4.6)

Own plan: candidate (iii) of the task, cells of side two. Locked from the block 17 note (PR #8151) and `probes/work/pr8151/chessboard_dissemination_witness.py` before reading a1/a3/a4 in full. After locking: a1 is refereed-confirmed (216m via site-class counting in 2D and bond-plane RP in 3D); a3 is a no-go for pure bond-plane *orbits* of size N. This attempt is the 2-cell tiling geometry, which those attempts did not close.

Defect: T3 disseminates by site reflections; the orbit of a canonical direction-`i` bond is one transverse-parity class (`N/2^{d-1}` bonds), not `D_all`.

## (1) The statement attempted

**Statement (PARTIAL / no-go for (iii) as a single tiling).** Let a *2-cell* of even corner `c∈(2Z)^d` on the even torus `(Z/SZ)^d` (`S` even) be the set of sites `c+{0,1}^d`. The direction-`i` bonds whose *starting* site lies in the cell and has even coordinate `i` relative to `c` are the cell’s direction-`i` bonds. Then:

- each such 2-cell contains **every** transverse-parity class of direction-`i` bonds, exactly once per class in 3D (`2^{d-1}` bonds) and twice-per-class? No: 2 bonds in 2D (one per y-parity), 4 in 3D (one per (y,z)-parity);
- all those bonds have **even** longitudinal base `x_i`;
- the disjoint even-corner tiling has `(S/2)^d` cells; the union of their direction-`i` bonds has size `N/2`, not `N`.

So a Peierls event attached to 2-cells of one tiling, even if it fires on all transverse parities inside the cell, disseminates at most the even-longitudinal half of `D_all`. Route (iii) as a *partition* into 2-cells does not repair T3. (Overlapping 2-windows of every parity would cover `D_all` but are not a chessboard product.)

Independently, the six-axis weight matrix `W` has eigenvalues `p+q+4r`, `p-q` (×3), `p+q-2r` (×2); for `p,q,r≥0`, `W⪰0` iff `p≥q` and `p+q≥2r` (the task’s computed lead for (ii), verified before any reliance).

## (2) Steps

**Step 1 — `W` spectrum (PROVED; CHECKED C1).** On the ordered basis `(+e_x,-e_x,+e_y,-e_y,+e_z,-e_z)`, `W_{aa}=p`, antipode `q`, else `r`. Characteristic polynomial / `eigenvals` give the three values with those multiplicities. Nonnegativity of the three is `p≥q` and `p+q≥2r` once `p+q+4r≥0`, which holds for `p,q,r≥0`. Samples: `(3,1,2)` and `(216,1,1)` on the PSD side; `(1,3,2)` and `(5,2,4)` off it.

**Step 2 — 2-cell inventory (PROVED; CHECKED C2).** A direction-`i` bond is determined by its start `x` and axis `i`. Inside the 2-window, the start must have relative coordinate `i` equal to 0 (the `+e_i` edge of the cube), and relative transverse coordinates in `{0,1}`. That is one start per transverse-parity class, all with even `x_i` when `c` is even. Union over even `c` is exactly the even-`x_i` direction-`i` bonds, cardinality `N/2`. Checked on `(Z/4)^2`, `(Z/6)^2`, `(Z/4)^3`, `(Z/6)^3`.

**Step 3 — no-go (PROVED).** T3’s intended event `D_all` has `N` direction-`i` bonds. A chessboard on the coarse lattice of even 2-cells can force only the bonds that live in those cells. That set is not `D_all`. Combining with site-reflection (which fixes transverse parity, already fully present in the cell) does not move `x_i` mod 2. Bond-plane reflections *would* move longitudinal parity; that is route (ii), not (iii).

## (3) First failure of route (iii) as a tiling

Step 3: the 2-cell partition does not see odd-`x_i` bonds. What would repair (iii) is a second tiling (odd corners along `i`), i.e. two coarse chessboards, or overlapping windows, neither of which is a single chessboard product in the sense of T3.

## (4) What would finish it

A chessboard on the product of the even-`i` and odd-`i` 2-tilings (two events `E_{\mathrm{even}}`, `E_{\mathrm{odd}}`, Cauchy–Schwarz `μ(D_all)^2 ≤ μ(E_{\mathrm{even}})μ(E_{\mathrm{odd}})`) together with a 2-cell analogue of a1’s line lemma, giving an explicit `ε`. Or accept a1’s refereed 216m and stop.
