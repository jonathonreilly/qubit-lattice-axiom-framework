# Referee: a formation price from local data, attempt 2

Attempt `w-macbookpro9927a-jec8b`. The held-cube Green's functions are recomputed here. The attempt's script is not imported.

A held cube of odd side has a wall where the field vanishes. On the interior, `1 − A` is the six-neighbour average, and `g(·, y)` is its inverse applied to a unit source at `y`. The coupling is `k = γ/12`.

## Verdicts

**Centre values.** At the centre, `g_yy` is `1`, `22/17`, `136/99` and `79271956/56195761` for sides 3, 5, 7 and 9. Enlarging the cube from side 5 to 7, and from 7 to 9, raises `g(·, y)` at every interior site of the smaller cube. A unit source at the centre therefore has four different records-only prices, `12/11`, `102/91`, `297/263` and the side-9 value, printed `1.090909`, `1.120879`, `1.129278` and `1.133213`. The data inside radius `R = 0, 1, 2` do not see which of the paired boxes is in use.

**Ledger.** On the side-7 cube, a uniform `3×3×3` of masses `1/27` has ledger equal to the total effective source, about `0.984627`. The four symmetry classes have strictly increasing prices, about `1.105484`, `1.106711`, `1.108108` and `1.109712`. Each post-event field `kΛ g(·, y)` solves the law, and `E' φ'_y = Λ`. The uniform seven-site star has price `1188/1091` on sides 7 and 9. The distance-two cross is about `1.105773` and `1.105055`.

**Cage.** Outside a window of radius `R`, the field that equals `g(·, y)` beyond radius `R+1` and vanishes inside has Laplacian supported on the two cage layers and total charge 1. Adding a multiple `c` of that cage, as bodies at rest, solves the static law, leaves every amplitude and rate inside the window unchanged, and shifts the ledger by exactly `c`. The three checked pairs are side 7 with `R = 0`, `c = 1/5`, and side 9 with `R = 1` and `c = 1/4` or `−1/7`. A Taylor lower bound on the Dirichlet eigenvalue keeps the operator positive.

**Point source.** If `s − Q δ_y = (1−A)f` with `f` finitely supported, the price is `Q/(φ_y + k f_y)`. Three asymmetric sources match that rule exactly. The star's rule reduces to `c/(1 − kc)`. The polynomial `x⁴ − 6x²y² + y⁴ − 2z²` is discrete harmonic, pairs to 0 with the star's excess, and pairs to 48 with the distance-two cross, so the cross is not point-equivalent.

**Delay.** Under the single-frequency law, `(1 − cos ω₀ t) u` starts from rest, equals the static change at `t = π/(2ω₀)`, and equals twice that change at `t = π/ω₀`. This step uses that reduced law as supplied.

## What stays open

Whether a confined source that is not point-equivalent still determines the box from the window was not settled. The note hashes were not re-checked.

## Result

HIT: confirmed. No rule of one fixed radius sets the formation price in every held box. When the effective source is point-equivalent, the price is exactly `Q/(φ_y + k f_y)`.
