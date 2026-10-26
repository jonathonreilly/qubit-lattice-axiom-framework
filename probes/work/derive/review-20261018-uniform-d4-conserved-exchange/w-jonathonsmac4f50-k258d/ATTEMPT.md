# Attempt: uniform conserved-source exchange on the D4 carrier
Task `J:derive:review-20261018-uniform-d4-conserved-exchange:a1`. Same-family (Sonnet 5.5), unrefereed, owner-requested research work. Not accepted science. No status words are claimed.

## Plain-language summary
The earlier note fits the exchange between two conserved sources to `alpha<T1,T2> + beta trT1* trT2`. The fitted numbers (-4, 4/3 or 2) are accurate to second order in the momentum q. The full tensor is only accurate to first order in generic directions (the residual .0033 at q=.02 halves to .0016 at .01). I found where the first-order error comes from. It is a phase in the trace term: the trace of the source is measured with the plain sum of diagonal entries, but the lattice couples it with the weights `w_mu = exp(-i q_mu)`. Swap in the weighted trace and the remainder drops to second order in every direction I sampled. I also checked two places where uniformity fails or needs care: the rank change at q=0, and the complex null cone `q.q = 0`. The full uniform statement is not proved. The route stops at a perturbation lemma (step 13).

## Read before concluding
I read `docs/MINIMAL_AXIOMS_2026-06-29.md` (full text, sha256 93af34cf...) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (full text), plus both D4-cone notes of 2026-10-18 on main. The frozen commit `77565121a9e2598aa4daed6413c5c723241654a5` exists, and both source objects match their sha256 values (see `RECOVERY_STATUS.json`). Current main (a77a3449c9) has the same bytes for both.

## Setting and premises (what the axioms say vs what a lane supplied)
- Axioms say: Z^3 sites, qubit possibility domain, local nearest-neighbour admissibility, records. They say nothing about Regge actions, 4D triangulations, Euclidean lengths or scalar stress. The qualification section of the axioms says further structure needs a derivation or an approved primitive. The approved primitives are `scale_reference_primitive`, `kinetic_isotropy_primitive` and `realized_state_primitive`. The kinetic one fixes `c_t = c_s` only.
- Supplied by the lane (ASSUMED, not derived here): the 96-simplex D4-cone triangulation, the Regge Hessian `Q(q)` built from area and dihedral derivatives, the nearest-neighbour scalar `K0`, the corner stress `S`, the segment map `b`, the face weight `kappa`, and the index-3 tick coordinate. Nothing is selected by the axioms. No physical gravity identification and no nonlinear action symmetry is assumed.
- Object studied: `K_ij(q) = (q.q) B(T'_i;-q) R(q) Q(q)^+ R(-q)^T B(T_j;q)`, with `T` in the lattice-conserved space `N(q) = {T symmetric: (w-1).T = 0}` and `T'` in `N(-q)`. For real q, `N(-q)` is the complex conjugate of `N(q)` and this is the source's `conj(B) R Q^+ R^T B q^2`. For complex q it is the analytic bilinear continuation, with the gauge solve done as `(Q + lambda G(q) G(-q)^T)^{-1}`. `Q^+` is the inverse on the gauge complement.
- Comparison forms (T = S/2): `F_plain = alpha<T1',T2> + beta trT1' trT2` (source), and `F_w = alpha<T1',T2> + beta (sum_mu w_mu(-q) T1'_mumu)(sum_mu w_mu(q) T2_mumu)` (new). Here `alpha = -4`, and `beta = 4/3` at `kappa = 0` or `2` at `kappa = 1/24`.
- Everything numerical is float64 with stated tolerances, so it is CHECKED and not exact. Exact claims use sympy or Fractions.

## Steps
1. **ASSUMED.** The supplied carrier, action and scalar coupling above.
2. **PROVED** (E1; reproduction, not new). The exact Laurent Ward identity `sum_mu u_mu S_mu,nu = -d_nu[K0(y)-K0(x)]/4`, checked symbolically per component.
3. **PROVED** (E2; mild, probably known). For every `v != 0` (real or complex), the map `T -> v.T` from symmetric 4x4 tensors onto C^4 is onto, by the explicit right inverse `T = y a^T + a y^T - (v.y) a a^T` with `v.a = 1`. So `dim N(q) = 6` for every q with `w != 1`. There is no rank drop of the conserved-source space anywhere in the small-momentum region except q=0. The space `N(q)` is therefore well defined, and gauge-independence of K on it follows from step 2 plus `ker Q = ran G` (step 7).
4. **PROVED** (E3). Put `T~_mn = exp(-i(q_m+q_n)/2) T_mn` and `p = 2 sin(q/2)`. Then `(w-1).T = -i e^{iq_nu/2} (p.T~)_nu`. Lattice conservation is exactly conservation of the staggered tensor `T~` with the real lattice momentum `p`, and `tr T~ = sum_mu w_mu T_mumu`.
5. **PROVED** (E4). `d/dt` at 0 of `[w(-q)-weighted trace] x [w(q)-weighted trace]`, with `q = t n`, equals `i[(n.d1)(tr2) - (tr1)(n.d2)]`, where `d_k` is the diagonal of `T_k`. The alpha term has no first-order change, because the staggering phases are unimodular and cancel in `<T1',T2>`. So `F_w - F_plain = L + O(q^2)` with `L = i beta/4 [(q.d1')(tr2) - (tr1')(q.d2)]`.
6. **PROVED** (E5, E6; exact rational arithmetic).
   - `L` vanishes identically on axis and tick directions (row a of T is zero, so `n.d = T_aa = 0`) and on the body direction (`sum_mu T_mu,nu = 0` for all nu, so `n.d = tr/2`).
   - It is nonzero in generic directions. Exact example: `n = (1,2,0,0)`, `T1 = vv^T` with `v = (2,-1,1,0)`, `T2 = uu^T` with `u = (0,0,1,1)`. Both are continuum-conserved (`n.T = 0`) and the form equals 12.
   - `L` is imaginary anti-Hermitian. It vanishes on any pair with real `n.d` and real `tr`, so real-part or real-source fits cannot see it.
   - This matches the pattern in the source note: axis, tick and body residuals reach the second-order floor and generic ones do not.
7. **CHECKED** (N1, N2a-c; float64). With analytic derivatives, disjoint from the source's finite differences:
   - **Hessian.** It agrees with centred finite differences entrywise to 3e-10.
   - **q = 0.** `Q(0)` has nullity 40, gauge rank 28, and a nonzero spectral gap 2.4222. The rank changes at q=0 are gauge rank 28 -> 32 and nullity 40 -> 32 + 8 low modes.
   - **Real q in 51 directions, `|q| = .02, .01`.** The nullity of `Q(q)` is exactly 32 (= gauge rank). There are exactly 8 low modes, `{-1/2 (x2), -1/4 (x5), +1/4 (x1)} |q|^2 (1 + O(q^2))`, direction independent, with deviation ratio 4.000 between the two scales. Every other mode has `|ev| >= 2.42`.
   - **Reading (not proved).** Five of the low modes look like transverse-traceless modes, one like the conformal mode, and two like the partner pair.
8. **CHECKED** (N4, N4b). With the analytic Hessian, the source diagnostic is reproduced: generic residuals 0.003295 (kappa=0) and 0.004885 (kappa=1/24) at .02, exactly half at .01. The fitted `alpha, beta` are accurate to O(q^2). So a small coefficient error does not bound the tensor remainder, which is O(q).
9. **CHECKED** (N5). The exact first-order remainder against `F_plain` is `L` (step 5): the relative defect `|D - L|/|L|` is 0.012, 0.006, 0.003 at q = .02, .01, .005, halving with q. This is the mechanism for the generic O(q) residual.
10. **CHECKED** (N3a/b, N7; sampled, not uniform).
   - **Real directions.** Over 51 real directions (40 random, near-axis, near-body and special), at both kappa:
     - the remainder against `F_w` has ratio .02/.01 in [3.98, 4.02], i.e. O(q^2), with `sup |rem|/|q|^2 = 0.122` (kappa=0) and 0.121 (kappa=1/24);
     - the remainder against `F_plain` has ratio 2.00 (O(q)) in generic directions and sup `|rem|/|q|` = 0.195 and 0.289.
   - **Complex directions.** Over 6 random complex directions with `|q.q| ~ |q|^2`, the bilinear continuation gives ratios 4.00 for `F_w` and 2.00 for `F_plain`.
11. **CHECKED** (N6, other low modes). `beta(kappa) = 2 - (2/3)(1 - 24 kappa)^2` at six values of kappa to 1e-4. Reading: at leading order the two partner modes carry the whole kappa-dependence, and `kappa = 1/24` is the zero of their source coupling. `beta = 2` is then the value with `beta/alpha = -1/2` (the 4D trace-subtracted structure). The `kappa = 0` value 4/3 includes a partner contribution of -2/3. This is a finite statement, not a decoupling theorem.
12. **CHECKED, non-uniform** (N8). Approaching the complex null cone `q.q -> 0` (one family, `q.q = .75, .19, .02`):
   - the low eigenvalues scale as `(q.q) x {1/4 (x6), 1/2 (x2)}`, so the low block degenerates (rank change);
   - the remainder times `(q.q)/|q|^2` stays about 0.05-0.06, so the remainder behaves like `|q|^2/(q.q)`, not `|q|^2`.

   A direction-uniform bound over complex directions therefore needs `|q.q| >= c|q|^2`. The data are one family and three points. The scaling is checked, not proved.
13. **UNRESOLVED (first failing step, U1).** A uniform perturbation lemma. Show that `Q(tn)` is entire in `t`, with `Q0 = Q(0)` having kernel of dimension 40 and gap 2.4222 (checked). Then prove, uniformly for `n` on the real unit sphere:
   - (a) `ker Q(tn) = ran G(tn)` exactly for `0 < t <= eps`;
   - (b) the 8-mode block equals `t^2 A(n) + O(t^3)` with `A(n)` invertible on the gauge quotient (the exact `Q1, Q2` data are not extracted here; only the eigenvalues are checked);
   - (c) `K(tn) = F_w + O(t^2)` with an explicit constant.

   Until then the leading tensor form in step 10 is a sampled finite observation, not a uniform theorem. Also not done: complex directions near `q.q = 0` (step 12), and the effect of the off-site corner placement beyond the trace term (the `O(q^2)` terms are unanalysed).

## What is new relative to the sources
- Retrieval or reproduction (not new): steps 2, 8 and the numerical values in step 7 (note's 0.003295/0.004885, ratio 2).
- New, scoped, same-family and unrefereed:
  - the identification of the generic O(q) tensor residual with the first-order trace-registration phase (steps 4-6, 9). It is exact algebra plus a checked match to the actual exchange. It also explains why axis, tick and body directions are clean and why real-part fits miss it;
  - the w-weighted trace form `F_w`, checked to O(q^2) in the sampled real and complex directions (step 10);
  - the checked non-uniformity at the complex null cone (step 12);
  - the closed form `beta(kappa)` for the partner channel (step 11).
- Not claimed: any uniform theorem, any decoupling theorem, any physical identification. The source note already lists these as unproved, and they remain unproved.

## Not done / limits
- Float64 only for the Regge claims: no certified arithmetic. Conditioning is benign in the tested range (the lowest used eigenvalue is about 2.5e-5, with roundoff about 1e-15), but there is no interval bound.
- Sampling: 51 real and 6+3 complex directions at two scales. Nothing near the Brillouin-zone aliasing region (`w_mu = 1` for `q_mu = 2 pi`), since the question is small momentum.
- No cross-family confirmation run. The protocol asks for one, and it is not done here.
