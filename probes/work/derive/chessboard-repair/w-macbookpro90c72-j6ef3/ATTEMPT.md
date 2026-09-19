# chessboard-repair, attempt 3 (worker w-macbookpro90c72-j6ef3, model grok-4.6)

Independent of a1 (site-reflection + one-line lemma) and grok a4 (Cauchy–Schwarz over parity classes). Route (ii): bond-plane reflection positivity of the six-axis static law, and whether those reflections disseminate a bad direction-`i` bond to every direction-`i` bond.

## (1) The statement attempted

The 6×6 bond weight `W` (`p` same axis, `q` opposite, `r` orthogonal) has eigenvalues `p+q+4r` (once), `p−q` (three times), `p+q−2r` (twice). It is positive semidefinite iff `p≥q` and `p+q≥2r`. On the line `(p,1,2)` that is `p≥3`, with `p=3` on the boundary. The FLS sufficient condition for reflection positivity through planes bisecting bonds is therefore available on the whole regime of interest.

Pure bond-plane reflections, however, send a direction-`i` bond to an orbit of size `N/2` (even start in the longitudinal coordinate), not `N`. They mix the *transverse* parity that site reflections preserve, but they do not produce the odd-start longitudinal bonds. So they do not make T3's disseminated event “every direction-`i` bond is bad”. Combining site reflections in the bond direction with bond-plane reflections in the transverse directions does give orbit `N`. Route (ii) with bond planes *alone* fails to repair T4; the eigenvalue lead is confirmed.

## (2) Steps

**Step 1 — eigenvalues (PROVED; CHECKED W).** Index the menu `0:+x, 1:−x, 2:+y, 3:−y, 4:+z, 5:−z`. `W_{aa}=p`, `W_{a,−a}=q`, else `r`. The all-ones vector is an eigenvector with `p+q+4r`. The three antipodal differences `(e_a−e_{−a})` give `p−q`. The two traceless even combinations that are constant on each antipodal pair and orthogonal to all-ones give `p+q−2r`. Checked by sympy `eigenvals` / `eigenvects`. PSD ⇔ all three families nonnegative ⇔ `p≥q` and `p+q≥2r` (the remaining eigenvalue is positive for `p,q,r>0`). Witnesses: `(3,1,2)` has `p+q−2r=0`; `(5,2,4)` has `−1`; `(1,3,2)` has `p−q=−2`; `(4,1,2)` is definite.

**Step 2 — bond-plane geometry (PROVED; CHECKED O).** A bond-plane reflection in direction `i` is `x_i ↦ 2k+1−x_i`. The orbit of the origin's direction-0 bond under all such reflections, all directions, all `k`, has size `N/2` on even-side tori `(Z/SZ)^d` for `(d,S)∈{(2,4),(2,6),(3,4),(3,6)}`, and consists entirely of direction-0 bonds with even longitudinal start. Site-plane reflections `x_i ↦ 2k−x_i` of the same bond have size `N/2` (2D) and `N/4` (3D), matching the defect. The mixed group — site reflections in direction 0, bond-plane reflections in the other directions — has orbit `N`.

**Step 3 — why bond planes alone miss half (PROVED).** A direction-0 bond is a pair `{x, x+e_0}`. Bond reflection in direction 0 sends this pair to another pair whose canonical start has the same parity of `x_0` (the two endpoints are swapped or shifted by an even amount on even `S`). Transverse bond reflections change `x_⊥` arbitrarily but leave `x_0` parity. Hence only `N/2` bonds. T3's “every direction-`i` bond” is not this event.

**Step 4 — consequence for T4 (PROVED; CHECKED T).** Even if chessboard estimates apply to the bond-plane orbit (FLS when `W` is PSD), the event they bound is not D_all. T4's `ε=6m/p` for `μ(D_all)^{1/N}` does not follow from bond-plane RP alone. The mixed group of Step 2 would need *both* site-plane RP and bond-plane RP; site-plane RP of the six-axis law is a different condition and is not claimed here.

## (3) Where the route stops

**First failing step of a T4 repair by bond planes alone: the orbit is `N/2`, not `N`.** The RP condition is not the obstruction on `(p,1,2)` for `p≥3`. Using the mixed group requires site-plane RP, which this attempt does not prove. 2D/3D thresholds are therefore not improved by this route beyond what a1/a4 already do with other methods.

## (4) What would finish it

A proof of site-plane RP on the same `(p,q,r)` region, so the mixed group is RP and disseminates to all `N` direction-`i` bonds, restoring `ε=6m/p` in 2D and 3D (`p≥216 m`); or a chessboard estimate that uses the `N/2` orbit and still beats `1296 m` in 3D.
