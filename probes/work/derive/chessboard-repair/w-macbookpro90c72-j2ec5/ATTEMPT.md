# chessboard-repair, attempt 4 (worker w-macbookpro90c72-j2ec5, model grok-4.6)

Route (i) of the task: combine parity classes by Cauchy–Schwarz. Independent of a1's bond-plane RP
(route ii). Plan formed before reading a1: site reflections give one transverse-parity class; CS over
the 2^{d−1} classes recovers "every direction-i bond is bad" at the cost of the worst class's mass.

## (1) The statement attempted

**Statement.** Assume `p ≥ m = max(q, r)`. Site reflections disseminate a canonical direction-`i` bond
to the class `E_i^π` of all direction-`i` bonds with the same transverse parities (orbit size `N/2^{d−1}`).
Every pattern in `E_i^π` has at least `N` bad bonds in 2D and at least `3N/4` in 3D for `2L ≥ 4`
(one-line lemma `bad(s)+2 bad(s,a) ≥ n` on proper cycles), hence
`μ(E_i^π)^{1/N} ≤ 6m/p` in 2D and `≤ 6(m/p)^{3/4}` in 3D.
Cauchy–Schwarz over the `2^{d−1}` classes:
`μ(∩_π E_i^π)^{1/N} ≤ max_π μ(E_i^π)^{1/N}`.
The intersection is "every direction-`i` bond is bad", T3's *intended* event. Therefore T4's
`ε = 6m/p` is valid in 2D (`p ≥ 216m`), and in 3D CS cannot beat `ε = 6(m/p)^{3/4}`
(`p ≥ 1296m = 6^4 m`). Route (i) recovers the 2D theorem as stated and does **not** recover the
3D constant 216. (Bond-plane RP, a1 route (ii), is a different route; not used here.)

## (2) Steps

**Step 1 — orbit (PROVED; CHECKED).** `θ_{j,k}: x_j ↦ 2k − x_j` preserves the parity of every
coordinate `j ≠ i` of a direction-`i` bond. On `(Z/4)^2` the orbit of `((0,0),(1,0))` has size 8
and a single y-parity.

**Step 2 — one-line lemma (PROVED; CHECKED).** Cyclic `s`, proper cyclic `a` (`a_t ≠ a_{t+1}`):
each good bond of `s` forces a mismatch with `a`; each site is in two bonds, so
`bad(s) + 2 bad(s,a) ≥ n`. Exhaustive at `n = 4, 6` (alphabet 5).

**Step 3 — counting (PROVED; CHECKED).** 2D, `2L ≥ 4`: even rows contribute `N/2` bad horizontals;
each odd row against both neighbouring even rows gives `bad_h + U + D ≥ 2L`; verticals counted once.
Total `≥ N`. 3D: class lines `N/4` plus two odd-parity families `N/4` each, total `3N/4`.
Sharpness patterns (even rows alternate `0,2`, odd rows constant `0`; 3D: class lines alternate
`0,2`, others `0`) attain `N` and `3N/4` on sides 4 and 6. The 4×2 torus is degenerate (`+e_y = −e_y`)
and is not used.

**Step 4 — mass bound (PROVED).** `p ≥ m` ⇒ weight decreases in the number of bad bonds.
`Σ_{E} Π φ ≤ 6^N m^{b_0} p^{dN − b_0}`, `Z ≥ 6 p^{dN}`, so
`μ^{1/N} ≤ 6^{(N−1)/N} (m/p)^{b_0/N} ≤ 6 (m/p)^{b_0/N}`.

**Step 5 — Cauchy–Schwarz combination (PROVED).** Hölder/CS:
`μ(∩_{α=1}^k A_α) ≤ (Π_α μ(A_α))^{1/k} ≤ max_α μ(A_α)`.
`k = 2^{d−1}` classes, each with the bound of Step 4, so the full "every direction-`i` bond bad"
event has the same `N`-th root bound as one class. In 2D that is `6m/p`; T5's `ε ≤ 1/36` needs
`p ≥ 216m`. In 3D it is `6(m/p)^{3/4}`; `6(m/p)^{3/4} ≤ 1/36` iff `p/m ≥ 216^{4/3} = 6^4 = 1296`.
CHECKED: `6^3 = 216`, `6^4 = 1296`.

**Step 6 — 3D no-go for route (i) (PROVED).** CS cannot improve the exponent `3/4`, because it
never beats the worst factor. Site reflections cannot mix transverse parities, so no further
dissemination is available on this route. Improving 3D to 216 requires a reflection that moves
parity (bond-plane, route (ii)) or a coarser cell (route (iii)), not attempted here.

## (3) First unclosed step

None for the statement above. The true optimal threshold (`p ≈ 3.6` executed) is not reached.

## (4) What would finish it

Bond-plane RP (eigenvalues `p+q+4r`, `p−q` ×3, `p+q−2r` ×2; PSD iff `p ≥ q` and `p+q ≥ 2r`)
or a Peierls count on `(2Z)^d`. Route (i) is complete as a 2D repair and a 3D no-go.
