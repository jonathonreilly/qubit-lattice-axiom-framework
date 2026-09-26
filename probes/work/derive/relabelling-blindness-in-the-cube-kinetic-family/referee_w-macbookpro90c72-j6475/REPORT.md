# Referee: relabelling blindness in the cube kinetic family, attempt 2

Attempt `w-macbookpro9927a-jf51d`. The Euler conditions and the mode pencil are recomputed here. The attempt's script is not imported.

The strain is symmetric, `R₁ = p² tr h − p·h·p`, and `R₂` is the quadratic member in the attempt. The cube kinetic term has three numbers `(M₁, M₂, M₃)`, and the antisymmetric rate has coefficient `N`. A relabelling `ξ` changes the frame by `δε = −ξ pᵀ`.

## Verdicts

**Gradient.** With `δh = ppᵀ ζ(t)` and a multiplier shift through `ζ'''`, every Euler derivative vanishes if and only if `(M₁, M₂, M₃) = (0, c, −c)` and the shift is `u → u + (c/K) ζ''`. The change of the Lagrangian is `d(c ζ′ R₁)/dt`. The coefficient `N` is not fixed.

**Transverse.** With `ξ = (p × b) ζ(t)`, the same test forces `(M₁, M₂, M₃) = (M, 2M, 0)`, `N = 0`, and no multiplier shift. The Lagrangian is then unchanged.

**Both.** The union of the two sets of conditions leaves only the zero kinetic term.

**Cube forms.** Invariance of a quadratic form in the nine rate components under a quarter turn, a third turn about `(1,1,1)`, and inversion leaves exactly four numbers: `Σ V_jj²`, `Σ_{i<j} V_ii V_jj`, `Σ sym(V)_ij²`, and `Σ antisym(V)_ij²`. Adding an arbitrary antisymmetric coin rotation changes the form unless the last coefficient vanishes.

**Modes.** For the gradient survivor with `c = −2` and `K = 1`, the `(h, u)` pencil has rank 6 at `p = (1,2,2)` and at `p = (2/5, 1/3, −3/7)`. The gcd of its maximal minors has root `p²/4` of multiplicity two, and no other nonzero root. The rotation block decouples with determinant `(2 N X)³`. At `X = p²/4` the kernel is three-dimensional: the transverse-traceless pair, plus the gauge vector `h = ppᵀ`, `u = 2X`, which is null at every `X`.

## What stays open

Orders beyond the second strain, and a field that would couple to the drifting transverse relabellings, were not classified. Nothing here fixes `α/K`.

## Result

HIT: confirmed. A gradient relabelling is a symmetry exactly for `(0, c, −c)` with shift `(c/K) ζ''`. A transverse relabelling is a symmetry exactly for `(M, 2M, 0)` with no shift. Only the zero term satisfies both.
