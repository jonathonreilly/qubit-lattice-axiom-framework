# Referee: pinned sphere order and stiffness, a3

Author `w-macbookpro90c72-j7ebb` (claude-opus-5-5). Referee `w-macbookpro90c72-j4c75` (grok-4.6).

The author's script was not imported. The domination route (b)–(d) was not reopened. Positivity of the spherical eigenvalues for every degree above 1 was not re-proved.

## What holds

On contents `{empty, +1, −1}` the bond kernel is positive semidefinite if and only if `c ≥ 1/cosh β`. The odd direction `(0, 1, −1)` has eigenvalue `2c sinh β`. The even block has determinant `2c cosh β − 2`. At `c = 1/cosh β` the determinant vanishes and a 2×2 minor is `4 tanh β`, so the rank is 2.

The sphere kernel's block on (empty, the constant function) is `[[1, 1], [1, c sinh(β)/β]]`. It forces `c ≥ β/sinh β`, and at that value the block has rank one. The integrals give `i₀ = sinh(β)/β` and `i₁ = (β cosh β − sinh β)/β²`. The numerator of `i₁` vanishes at 0 and has derivative `β sinh β`, so `i₁ > 0` for `β > 0`.

On the `4³` torus the Green function of `−Δ`, with the zero mode removed, satisfies `G₀ − G₁ = (1 − 1/N)/6`. The vacancy cost is `a_L = 2/(1 − (G₀ − G(2,0,0))) = 320/129`. A direct solve of the twisted dissipation, one site removed, drops it from `64` to `7936/129`, which is `64 − 320/129`.

For any cost `a`, `ρ² / (β(1 − aε)) = (1/β)(1 + (a − 2)ε) + O(ε²)` with `ρ = 1 − ε`. A `160³` quadrature of `G₀ − G(2,0,0)` on `Z³` gives `a = 2.531138`, in agreement with the printed digits, and below the six-bond value `3`. That quadrature is not a closed form.

## What was not rebuilt

Higher-degree eigenvalues of `e^{β s·s'}`, and the twisted-domination argument for long-range order.

`SUMMARY: PARTIAL the two-valued bond kernel is positive semidefinite iff c >= 1/cosh beta, and has rank 2 there. The sphere kernel's empty-constant block requires c >= beta/sinh beta, with i0 = sinh(beta)/beta and i1 > 0. On the 4^3 torus one vacancy drops the twisted dissipation from 64 to 7936/129 = 64 - 320/129. The stiffness factor is (1/beta)(1 + (a - 2) epsilon) + O(epsilon^2). A 160^3 quadrature gives a = 2.5311 on Z^3. Higher spherical eigenvalues and the domination route were not re-proved.`
