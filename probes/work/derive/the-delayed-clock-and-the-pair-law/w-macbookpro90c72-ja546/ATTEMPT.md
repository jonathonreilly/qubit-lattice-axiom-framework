# the delayed clock and the pair law, attempt 2 of 2

Worker `w-macbookpro90c72-ja546`. No earlier attempt files were on this worktree.

## 1. Statement attempted

The field relaxes by
`du_z/dt = Γ w_z ((1/6) Σ_e u_{z+e} − u_z + log(κ)(n_z − n̄))`,
with `w = exp(u)`, and a record leaves its site toward each neighbor at rate `w_x/d`.

**(a)** A single record does not trap its direction, at any finite `Γ`. Its embedded jump chain is simple random walk. What the delay can change is only the waiting time.

**(b)** No stationary law of product form — a law of the record positions times one deterministic field — exists when `log κ ≠ 0`.

## 2. Steps

**S1 (PROVED).** The rate to each neighbor is the same number, `w_x/d`. The field, however lagged, is a common factor. The next site is a uniform random neighbor. The embedded chain on a regular graph is simple random walk. Directional self-trapping does not occur.

**S2 (PROVED; CHECKED).** For records held fixed, `w_z > 0` only reparametrizes time. The equilibria are exactly the solutions of the discrete equation
`(u_{z+1}+u_{z−1})/2 − u_z + logκ (δ − 1/L) = 0`
on a ring (the same Green profile as the instantaneous clock). In the mean-zero gauge,
`u_z = −(log κ)/L · (z(L−z) − (L²−1)/6)`,
so the clock at the record is `u_0 = (log κ)(L²−1)/(6L)`. If `log κ < 0` this is negative: the record's own equilibrium clock is slow. That slowdown is already present at `Γ = ∞`. It is not a trail effect.

**S3 (PROVED).** Suppose a product `μ(positions) δ(u − ū)` were stationary. The field drift at a flat `ū` is `Γ e^{ū} logκ (n_z − n̄)`, which is not identically zero on the support of any law that has a record. The drift at the equilibrium bump `u*(positions)` is zero only while the records stay put. A hop leaves `u*` behind, and `u*` of the old positions is not `u*` of the new ones when `log κ ≠ 0` (checked: on the ring of length 4, `u_0 − u_1 = −3/4` for `log κ = −1`). So neither the flat field nor the slaved bump is invariant under the joint process.

**S4 (ASSUMED).** Block 95's instantaneous detailed balance is used only as the `Γ → ∞` comparison, not as an input to S1–S3.

## 3. Where this stops

The first-order-in-`1/Γ` correction to the two-record separation law is not computed. The embedded chain being unbiased does not fix the continuous-time occupation measure of two records, because the slower clock waits longer.

## 4. What would finish it

A ring with two records and a spectral gap for the linear relaxation, giving the `O(1/Γ)` shift of the separation weight.
