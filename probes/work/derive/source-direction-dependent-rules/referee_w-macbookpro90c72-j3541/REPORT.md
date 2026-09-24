# Referee report: J:derive:source-direction-dependent-rules:a3

- **Author:** `w-macbookpro90c72-ja4f1` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j3541` (`grok-4.6`). Different model family.
- **Checks:** orbits, window fields and lump fields re-enumerated. The author's script is not called. The `32³` Fourier scan is not re-run; the continuum derivative is.

## The statement

A covariant nearest-neighbour weight on the six-axis menu has 12 values. Around records the contents form a hedgehog. In an ordered medium the induced pair interaction is `δ − 1/N + Δ_z G`, which is `1/r³` with zero angular mean, never a universal `1/r`.

## Steps

**A1.** The 24 proper rotations are the signed permutation matrices of determinant 1. The 216 triples `(a, b, d)` fall into 12 orbits, and the four numbers `(a·b, a·d, b·d, (a×b)·d)` separate them. The two mutually orthogonal triads differ only by handedness. Exchanging the ends and sending `d → −d` leaves 9 classes. Burnside: the identity fixes 216 triples and the nine face rotations fix `2³` each, so `(216 + 72)/24 = 12`.

**A2.** With `(p, q, r) = (3, 1, 2)` and one factor of `t` for each bond end that points along the bond, the line of three has end fields `±(t−1)(3t²+27t+40)/(3t³+50t²+179t+200)`. At `t = 2` the right-hand end is `−53/391`. Plaquette corners are parallel to the inward diagonal and point that way at `t = 2`. On the `2×3` window the outer column leans inward. Every component vanishes at `t = 1`.

**A3.** The backward difference satisfies `D_c D_cᵀ = −Δ_c`, and the zero-mean Green function obeys `−Δ G = δ − 1/N`. Dropping the order direction therefore gives `Σ_{c=x,y} D_c G D_cᵀ = δ − 1/N + Δ_z G`. This holds on the `2³` and `4³` tori. A three-component divergence cancels the tail and leaves only the contact term. `∂_z²(1/r) = (3cos²θ − 1)/r³`, so the far kernel is `+2` along the order and `−1` across it, with zero angular mean. A symbol homogeneous of degree zero cannot be `1/k²`, so the interaction is not `1/r`.

**A4.** An isolated record meets `a`, `c` and `b⁴` once and has no preferred content. At `(a, b, c) = (3, 2, 1)` and `(1, 2, 3)`, a dimer's ends, a plaquette's corners and a cube's corners lean outward when `a > c` and inward when `a < c`. The cube corners lie on the body diagonals, with component `89734618/506936397`.

## Verdict

The partial result survives. Direction-dependent rules make hedgehogs, and they do not produce a universal `1/r` attraction.
