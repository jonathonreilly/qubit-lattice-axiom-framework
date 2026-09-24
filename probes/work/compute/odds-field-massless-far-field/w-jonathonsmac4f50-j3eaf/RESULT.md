# The far field of one record on the massless surface — run 1

Worker `w-jonathonsmac4f50-j3eaf`, model `claude-opus-5-5`. Blocks 41, 42 and 103 were written by the same model family (Claude). The derivation problem `odds-field-on-the-massless-surface` had J attempts from the same family, which were not read. Everything here was derived independently.

## 1. The third-order law (exact, sympy)

**Setting.** Take a lean `v` along the record's content axis, and write `x = 3λ₁v`. Let `α` be the axial quadrupole it generates, `π(s) = (1 + 3m·e(s) + Q(s))/6` with `Q(±z) = 2α` and `Q(orth) = −α`, and write `a = λ₂α`. For smooth neighbours the map gives:

- `lean' = 2x + 20ax − (10/3)x³`
- `α' = 6λ₂α + 5x²` (plus higher orders)

**Reduction.** On the surface `5p = 7q + 4r` one has `λ₁ = 1/6`, so `x = v/2`. With the quadrupole slaved, `α = 5x²/(1 − 6λ₂)`, and the fixed point gives

`Δv = u v³`, with `u = 5/2 − 75λ₂/(1 − 6λ₂)`.

**Consequences.**
- A Coulomb tail `v = A(r)/r` therefore runs as `A⁻² = a + 2u log r`.
- `u > 0` if and only if `λ₂ < 1/36`.

| triple | λ₂ | 6λ₂ | u | predicted b = 2u |
|---|---|---|---|---|
| (3,1,2) | 0 | 0 | 5/2 | 5 |
| (14,6,7) | 1/8 | 3/4 | −35 | −70 |
| (11,5,5) | 1/6 | 1 (quadrupole massless too) | — | undefined |

## 2. Is the unpolarised field stable on the surface? (one-site map, 40-digit arithmetic, 4000 iterations)

| triple | lean 0.01 → | quadrupole +0.01 → | reading |
|---|---|---|---|
| (3,1,2) | 0.00866 | 0 | stable. The marginal cubic decay matches `c = 5/12` exactly: `1/v² = 10⁴ + 2·(5/12)·4000`. |
| (14,6,7) | **0.898** | decays | **unstable**: the lean runs to an ordered state |
| (11,5,5) | **0.935** | **ordered** (quadrupole 0.935) | **unstable** in both channels |

**What this means.**
- At `(14,6,7)` and `(11,5,5)` the unpolarised field orders spontaneously on the massless surface itself.
- The full map around a record reaches no fixed point in 3000 accelerated iterations, on a torus of 21 or in a cube of 41 with uniform boundary.
- So there is no Coulomb-plus-log far field at these two triples.
- The log law exists only on the part of the surface with `λ₂ < 1/36`, of which `(3,1,2)` is a member.

## 3. The far field at (3,1,2) (floating point)

**Tori** (`r·v(r)`; periodic images and the neutral uniform mode make it rise):

| side | iterations | fit over r = 3..L/3 |
|---|---|---|
| 27 | 437 | `A⁻² = 19.17 − 5.28 log r` |
| 41 | 862 | `A⁻² = 20.86 − 4.76 log r` |
| 61 | 1649 | `A⁻² = 22.90 − 4.63 log r` |

The mean lean over the torus is `3.9·10⁻²`, `2.5·10⁻²` and `1.7·10⁻²` respectively. On tori the far field cannot be read.

**Cubes with uniform odds held on the boundary** (`A = v/(4πG_D)`, with `G_D` the Dirichlet lattice Green function):
- cube 41: A runs 0.280 → 0.244 over r = 1..13, and the fit gives `b = 0.89`.
- cube 61: A runs 0.277 → 0.234 over r = 1..20, and the fit gives `b = 1.04`.

**The lattice obeys the reduced law site by site.** In cube 41, the full-map residual `v − (1/6)Σv_y` equals `−(5/12)v³` to 5.5%, 1.7%, 0.8% and 0.7% at r = 3, 5, 8 and 12. The deviation falls off as the field becomes smooth. A scalar solve of `v = (1/6)Σv − (5/12)v³`, with the near field held, reproduces the full solution to about 0.1%. So `u = 5/2` holds on the lattice.

**The wall explains the small fitted b.** The continuum law `Δv = (5/2)v³`, matched at r = 3 and with a wall at R, gives these fitted b values:

| R | fit range | fitted b |
|---|---|---|
| 30 | r = 3..20 | 0.89 |
| 300 | r = 3..30 | 3.07 |
| 3000 | r = 3..300 | 3.58 |
| 30000 | r = 3..3000 | 3.86 |
| 3·10⁵ | r = 3..3·10⁴ | 4.03 |

- The wall at R = 30 reproduces the lattice cubes (0.89 and 1.04).
- `b` approaches `2u = 5` only for `r ≪ R`, and only slowly.

## 4. HIT

The task expected a Coulomb-plus-log far field at all three triples on the massless surface. The exact third-order law shows that such a field exists only where `λ₂ < 1/36`:
- **(14,6,7):** the quadrupole that the lean creates feeds the lean back, so `u = −35`.
- **(11,5,5):** the quadrupole is also massless and is unstable at second order.
- In both cases the unpolarised field orders spontaneously.

At `(3,1,2)`, `u = 5/2` is confirmed site by site. The fitted `b ≈ 1` is the finite box, not a failure of `b = 2u`.
