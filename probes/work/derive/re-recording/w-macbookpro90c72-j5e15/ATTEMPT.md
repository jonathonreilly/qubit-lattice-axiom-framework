# re-recording, attempt 1 (worker w-macbookpro90c72-j5e15, model grok-4.6)

Prior grok attempt a4 exists; this route is different: the doubled graph of *six-neighbour* synchronous re-recording (no self-loop) and its Laplacian spectrum `{E, 12−E}`, including a zone-corner kernel that the seven-stencil light-cone graph does not have. Nothing here assumes re-recording is admissible.

## (1) The statement attempted

(a) Asynchronous re-recording with `K(s | S) ∝ exp(β s·S)`, `S` the sum of the six current neighbours, is the heat-bath of the static nearest-neighbour law. Exact detailed balance holds on the 4-cycle for Ising weights, independently of the clock rates. The stationary law is therefore the static comparator, and block 19's Green-function sandwich is its equal-time covariance (sphere, `β` large).

(b) Synchronous re-recording (all sites at once) is reversible with respect to `π(s) ∝ ∏_x Z(S_x(s))`, `S_x` the six-neighbour sum, by the bilinear identity for the undirected 6-stencil. `π` is the `s`-marginal of Heisenberg on `Γ_6`: two copies of the torus, edges `(x,σ)—(y,s)` iff `y` is a nearest neighbour of `x` (no self-loop). The Laplacian spectrum of `Γ_6` is `{E(k), 12−E(k)}`. At the zone corner `E=12`, the odd eigenvalue vanishes: a staggered odd mode is a kernel. FSS therefore does *not* give a uniform `1/E` infrared bound for `π` (unlike the 7-stencil light-cone graph, whose self-loops make the odd corner eigenvalue `2`). On the `2×2×2` cube at `(3,1,2)` the static and sync all-+x probabilities differ.

(c) Async transfers the uniqueness regions, ordered phase, and kernel of the static law (blocks 03, 17, 19, 21). Sync transfers only after doubling, and the extra zero mode blocks a direct copy of G2. Small-`β` sync is a pairwise model with symbol `(6−E)^2`, not `E`.

## (2) Steps

**Step 1 — async detailed balance (PROVED; CHECKED A).** Only site `x` updates. The static weight changes by the six bonds at `x`: `π(s)/π(s^{x←s'}) = exp(β (s_x−s'_x)·S_x)`. The heat-bath kernel is `exp(β s'_x·S_x)/Z(S_x)`. Detailed balance follows, for any positive clock rates (the holding rates cancel in the stationary equation). Checked on `C_4` Ising with `t=e^β=2`, all sites, both flips.

**Step 2 — sync bilinear identity (PROVED; CHECKED S).** `N(x)={x±e_j}` is undirected. `∑_x s'_x·S_x(s) = ∑_x ∑_{y nn x} s'_x·s_y = ∑_y s_y·S_y(s')`. Hence `π(s)P(s→s') = C exp(β ∑ s'_x·S_x(s))` is symmetric. Checked as an integer vector identity on `(Z/4Z)^3` (384 directed 6-edges).

**Step 3 — `Γ_6` spectrum (PROVED; CHECKED G).** Adjacency: `(Af)(x,0)=∑_{y nn x} f(y,1)`. Stencil multiplier `μ(k)=2∑_j cos k_j = 6−E(k)`. Laplacian `Δ=6I−A` has eigenvalues `6∓μ`, i.e. `E(k)` (even sector, both layers equal) and `12−E(k)` (odd sector). At `k=(π,π,π)`, `E=12`, `12−E=0`: the odd staggered mode `f(x,0)=−f(x,1)=(−1)^{|x|}` is a kernel (nearest neighbours flip the stagger, the two contributions cancel). The 7-stencil of light-cone formation adds the self-loop `(x,0)—(x,1)`, degree 7, and the same mode has eigenvalue `2`. **The self-loop is what makes the light-cone doubled graph massive in the odd corner; 6-neighbour sync does not have it.**

**Step 4 — cube (CHECKED C).** At `(3,1,2)` on the `2×2×2` cube (12 edges; `±e_j` coincide so the 6-stencil double-counts each of the 3 graph neighbours): static `P(all +x)=p^{12}/Z_{\mathrm{st}}=59049/775835648`; sync `P(all +x)=Z_1^8/Z_{\mathrm{sy}}` with `Z_1=p^6+q^6+4r^6`, a different rational. So the two stationary laws are not equal even on this window. (On `L=2` the 6-stencil is degenerate; the `L=4` bilinear check is the nondegenerate identity.)

**Step 5 — small `β` (PROVED; CHECKED B).** `log Z(β|S|)=const + (β²/6)|S|^2+O(β^4)`. `|S|^2` for the 6-sum has Fourier symbol `(6−E(k))^2`, analytic and nonzero at `k=0`. The static law's quadratic piece is `E(k)`. The two interactions differ at every order that is kept.

**Step 6 — what transfers (PROVED as a reading of the identities).** Async = static: everything proved for the static law transfers (uniqueness at small `β`, six-axis order, sphere Green sandwich). Sync: reversibility and the Gibbs identification transfer; FSS G2 does not transfer as a uniform `1/E` bound, because of Step 3's kernel. Whether that kernel is lifted by the `|s|=1` constraint (it is an infrared statement about the graph, not about the spherical measure) is not decided here.

## (3) Where the route stops

The zone-corner kernel of `Γ_6` is a graph fact; it is not a proof that `π` has a massless staggered channel (the spherical measure may still gap it). FSS on `Γ_6` is not re-run (the zero eigenvalue makes Gaussian domination on that mode vacuous). The cube uses the degenerate `L=2` 6-stencil. Attracting / value-dependent async rates are not needed: they share the static stationary law.

## (4) What would finish it

FSS on `Γ_6` with the zero mode projected out, or a proof that the odd staggered channel is gapped by `|s|=1`; a nondegenerate torus (`L=4`) comparison of sync vs static marginals; the large-`β` expansion of `log Z(β|S|)` for the 6-sum (leading `β|S|`) against the static `β ∑_{\mathrm{nn}} s·s'`.
