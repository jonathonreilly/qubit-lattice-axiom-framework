# The hard-core sea in one dimension, exactly — attempt 1

Worker `w-jonathonsmac4f50-j19eb`, model `claude-opus-5-5`. Task `J:derive:the-hard-core-sea-in-one-dimension-exactly:a1`.

**Provenance.**
- Blocks 54, 55, 76 and 78 were written by the same model family (Claude Opus). They are open and unrefereed.
- The two-record reduction of the sibling unit `the-two-record-pull-under-exclusion:a1` is also same-family. That unit found that two records on a chain are free charge fermions. I re-derive it here for many records on a ring and do not cite it as authority.
- The referee should come from another family. There were no prior attempts on this problem at claim time.

**Scope.**
- The reduced walk is `H = φ σ₃ D φ`, with `(Dψ)(x) = (ψ(x+1) − ψ(x−1))/(2i)`, on a ring of even length `N`.
- The Record axiom is taken in the owner's reading: one record per site at a time, each with a coin (block 78).
- Both exchange signs are treated. Nothing is adopted. The parked decisions are untouched. No gravitational claim is made.
- The free sea is the comparator (block 76), not the framework's state.

## 1. The exact statement attempted

**(a) The reduction (PROVED; CHECKED by full diagonalisation).**
- On a ring the compressed many-record generator is exactly a direct sum over the cyclic momentum `J` of the coin sequence.
- Each block is **one band of free spinless charge fermions**, with hopping `φ_x φ_{x+1}/(2i)` and twist `θ_J = 2πJ/N_p`. For the bosonic sign, add `π(N_p − 1)`.
- Each block comes with the `D(J)` coin sequences of that momentum, where `D(J) = N_p⁻¹ Σ_r e^{−2πiJr/N_p} 2^{gcd(r, N_p)}`, an integer.
- Full diagonalisation of the many-record space at `N = 6, 8` agrees in ground energy and degeneracy for both signs and both fillings. For example, at `N = 6`, `N_p = 3` the ground energy is `−(sin π/9 + sin 2π/9 + sin 4π/9)`, 4-fold.

**(b) Energy per site.**
- The hard-core sea has one charge band where the free sea has two coin bands.
- At the filling `N − 2`, which would occupy every negative one-body state of the free sea, the hard-core energy is minus the two highest levels of a band that sums to zero. So `|E₀|/N ≤ 2/N → 0`, against the free sea's `−2/π`.
- At half filling the hard-core energy per site tends to `−1/π` (`−0.3184` at `N = 64`).

**(c) The polarisability.** This is the second-order response to `u = ε cos(2πmx/N)`, split as in block 76 into a volume term `c₀ Σ e^u` and a gradient stiffness `κ`.
- **At half filling** the hard-core `κ` is **positive** and converges: 0.0817, 0.0801, 0.0797 and 0.0796 at `N = 8, 16, 32, 64`. That is the free sea's sign; the free sea's `κ` at the next wavelength is 0.0884 down to 0.0797.
- **At the filling `N − 2`** the hard-core response is **negative and grows without bound**: −0.28, −4.5, −40.5 and −337 at `N = 8, 16, 32, 64`. These are two holes near the top of the band, with no local stiffness. The sign is opposite to the free sea's positive stiffness.

**(d) The chessboard of clocks.** It stays exactly invisible: `φ_x φ_{x+1} = 1` gives `φHφ = H`, with or without exclusion.

**Both halves of the task's HIT condition hold at the filling `N − 2`.**
- The interacting `κ` has the opposite sign.
- The ground state is degenerate over coin sequences (6/4 at `N = 6`, 10/14 at `N = 8`, for fermionic/bosonic; the counts grow like `2^{N_p}/N_p`), with an energy set by two holes. "The filled negative branch" has no sea meaning under exclusion.

## 2. Steps

### Step 1 — the reduction (PROVED; CHECKED 1.1, 1.4, X1, X2)
- **Records cannot pass.** In one dimension with nearest-neighbour hops, a record moves only onto an empty neighbouring site. So the cyclic order of the records, and with it their coin sequence up to rotation, is conserved.
- **The coin sign is a gauge.** On an even ring, the gauge `(−1)^x` on down coins turns `σ₃D` into `D` for both coins (1.1). The charge dynamics is therefore coin-independent, with hopping `φ_x φ_{x+1}/(2i)`.
- **The twist.** Carrying every record once around the ring rotates the coin sequence by one place. In the sector where that rotation acts as `e^{2πiJ/N_p}`, the charge fermions carry the twist `θ_J`.
  - For fermionic records the wrap bond also carries `(−1)^{N_p−1}`, which is already the fermion boundary condition.
  - For hard-core bosons, mapping to fermions adds `π(N_p − 1)`.
- **The counts.** `D(J)` counts the coin sequences with rotation eigenvalue `e^{2πiJ/N_p}`. Computed exactly with Ramanujan sums, and cross-checked against the defining sum for `N_p = 3, 4, 6` (1.4).
- **Checks.** The full many-record diagonalisation, of dimension up to 1,792 at `N = 8`, agrees with the reduction (X1). The `N = 6`, `N_p = 3` ground energy has the closed form above (X2).

### Step 2 — energy per site (PROVED; CHECKED 1.3, 3.1)
- A full twisted band sums to zero: `Σ_n sin((2πn + θ)/N) = 0` (1.3).
- So `N − 2` charges have energy minus the two highest levels, `|E₀| ≤ 2`.
- The free sea at the same filling fills both coin bands' negative states: `−2Σ_{k: sin k > 0} sin k → −(2/π)N`.
- Values (3.1):

  | `N` | hard-core, per site | free, per site |
  |---|---|---|
  | 8 | −0.2310 | −0.6036 |
  | 64 | −0.0312 | −0.6361 |

### Step 3 — the polarisability (executed; CHECKED X3, X4)
- **Definition.** `κ = [d²E₀/dε² − c₀N/2]/(N |q|²_lat/2)`, with `c₀ = E₀/N`. This is block 76's split into a volume term and a gradient part.
- **The reduction matches the full response.** It reproduces the full diagonalisation's second derivative at `N = 8` (X3).
- **Results (X4).**
  - Half filling: `κ > 0`, converging to `0.0796`.
  - Filling `N − 2`: negative, growing like a power of `N`. The two holes sit near the band top, where the level spacing is `O(N⁻²)`. Level repulsion there makes the second-order shift of `E₀` negative and large.
- **The free sea at `m = 1`.** Its gradient part is 0 to within the finite difference at every `N` tried (−0.0000 to −0.0001; its full response is the volume term), and `+0.08` at `m = 2`. This is reported, not claimed as a limit. I compare signs at `m = 2`.

### Step 4 — the chessboard (PROVED; CHECKED 1.2)
`φ_x = a^{(−1)^x}` gives `φ_x φ_{x+1} = 1` on every bond, so `φDφ = D`. The compressed generator is built from the same bond products, so it is invariant too.

## 3. Where the route stops

- The polarisability is floating point. Only its identities and the reduction are exact.
- The negative response at `N − 2` is a finite-number-of-holes effect whose per-site value diverges. That divergence is itself the statement: no local stiffness exists there.
- Three dimensions is not treated. There records can pass one another, and the one-dimensional reduction fails.

## 4. What would finish it

1. The three-dimensional hard-core problem: small tori by exact diagonalisation, or a reduction if one exists.
2. An exact second-order formula for the charge band's `κ` at half filling. The coincidence `0.0796 ≈ 1/(4π)` is noticed, not claimed.
3. An owner's reading of which filling "the sea" would be under exclusion, if any.
