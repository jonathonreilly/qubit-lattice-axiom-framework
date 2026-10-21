## 1. Supplied model (named premise)

Source of the conventions: `docs/THE_PURE_SPIN_HALF_LINK_MODEL_ON_THE_CUBIC_TORUS_IS_GAPLESS_DECONFINED_AND_UNORDERED_AT_L_12_WITH_A_QUADRATIC_TRANSVERSE_MODE_NOT_A_MAXWELL_PHOTON_BOUNDED_NOTE_2026-09-04.md`
(Definitions block) and the runner of
`docs/RING_MODEL_BETWEEN_THE_ROKHSAR_KIVELSON_AND_PURE_RING_POINTS_SMALL_TORUS_AND_VARIATIONAL_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`.

- Periodic cubic torus `L^3`, one spin-1/2 per link, `E_l = sigma^z_l/2`, `U_l = sigma^+_l`.
- Gauss law `G_v = (div E)_v - rho_v = 0` with **`rho_v = 0` on every cubic torus** (3 in / 3 out).
  The repo's staggered background `2 rho = ±(-1)^i` is declared only for the 2D *ladder*
  (09-04 note, "Definitions"); the task text's "staggered background" does not apply to the cubic
  torus. Every exact statement in §2 holds for any static background, because the gauge used is
  diagonal and the background only selects the sector.
- `H = -g sum_p (U_p + U_p^dag) + V sum_p n_p`, `n_p` = 1 if `p` is flippable (circulating).
  RK point `V = g`. Units `g = 1`.
- Sector: the flip component of the repo canonical zero-winding state
  `sigma_x = (-1)^y, sigma_y = sigma_z = (-1)^x` (frozen components exist on every even torus:
  `docs/RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md`).

## 2. Stoquasticity (exact; claim type: proved theorem + exhaustive finite certificate)

**Theorem 1.** For every `L >= 2` and every static background, in the basis of Gauss-legal
`sigma^z` configurations, `<s'|H|s> = -g` if `s' = F_p s` for a flippable plaquette `p`, and 0 for
every other `s' != s`. Hence `H` is stoquastic for `g >= 0`.

*Proof.* `U_p` is the oriented product `s^+ s^+ s^- s^-` on the four links of `p`; spin-1/2 ladder
operators have matrix elements in `{0, 1}` in the `sigma^z` basis, so `U_p + U_p^dag` maps `|s>` to
`|F_p s>` with amplitude 1 if `p` circulates in `s` (exactly one of `U_p`, `U_p^dag` acts) and to 0
otherwise. Two distinct plaquettes have distinct link sets (checked for L = 2,3,4,6,8,10,12; for
`L >= 3` it is immediate), so `F_p s = F_q s` forces `p = q` and no matrix element is a sum. The
`V` term is diagonal. ∎

**Theorem 2 (sign of g).** Let `L` be even and
`Lambda = {x-links (v,x) with y+z even} ∪ {y-links (v,y) with z even}`, `D = prod_{l in Lambda} sigma^z_l`.
Then every plaquette contains an odd number of `Lambda` links, so `D (U_p + U_p^dag) D = -(U_p + U_p^dag)`
for all `p` and `D H(g,V) D = H(-g,V)` on the whole Hilbert space; `D` is diagonal, so it preserves the
Gauss law, every winding sector and every flip component. Hence `H(-g)` is stoquastic in the gauged
basis `D|s>`, with the same spectrum sector by sector.

*Proof.* xy-plaquette at `v`: its x-links sit at `(y,z)` and `(y+1,z)`, whose `y+z` parities differ
(one in `Lambda`); its two y-links have the same `z` (both or neither in `Lambda`): odd.
yz-plaquette: y-links at `z` and `z+1` (exactly one in `Lambda`), no x-links: odd.
xz-plaquette: x-links at `(y,z)` and `(y,z+1)` (exactly one), no y-links: odd. Periodicity of
`Lambda` needs `L` even. Since `sigma^z` anticommutes with `sigma^±`, an odd count flips the sign. ∎

**Remark (odd L, exact).** For odd `L` no diagonal ±1 gauge maps `g -> -g`: the xy-plaquettes of one
plane form a mod-2 2-cycle `C` (every link lies in 0 or 2 of them), so `sum_{p in C} |Lambda ∩ ∂p|` is
even for every link set `Lambda`, but it would equal `|C| = L^2` (odd) mod 2. (The cubic π-flux
consistency `6π ≡ 0` is necessary but not sufficient; the global plane classes matter.)
Odd `L` has an empty zero-winding sector anyway (10-01 note).

**Certificate.** `scripts/step1_stoquastic.py` → `logs/step1_stoquastic.log`, `TOTAL: PASS=26 FAIL=0`:
odd-count property for L = 2..12; an independent GF(2) solve of `delta(Lambda) = 1` exists for
L = 2, 4, 6 and is inconsistent for L = 3, 5; exact L = 2 (9600 Gauss states, 937 flip components,
largest 864 — repo values): all off-diagonals equal -1 (no multiplicity), `D H(+g) D == H(-g)` exactly,
the spectra of `H(+g)` and `H(-g)` agree on all 937 components to 7e-14 for V = 0, 0.5, 0.9, and the
global `E0(V=0) = -9.0267209135` (repo value) lies in the 864-state component.

**Consequence.** Path-integral weights `g^n exp(-V ∫ N_flip)` are nonnegative for either sign of `g`
on even tori: no sign problem, every winding sector.
