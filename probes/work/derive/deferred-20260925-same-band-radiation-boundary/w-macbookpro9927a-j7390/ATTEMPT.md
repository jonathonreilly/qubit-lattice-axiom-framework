# Same-band radiation boundary: an interband single-quantum amplitude (block 149 recovery)

Task `J:derive:deferred-20260925-same-band-radiation-boundary:a1`, worker `w-macbookpro9927a-j7390`, model claude-opus-5-5 (owner-requested recovery).
Files in this directory:
- `check.py`: exact sympy for S1–S3, with rigorous `mpmath.iv` enclosures in S3/S4; under 1 s; `TOTAL: PASS=4 FAIL=0`.
- `make_status.py`, which writes `RECOVERY_STATUS.json`: sha256-verified heads and the `origin/main` SHA.

**Sources.**
- **The recovered note.** Block 149 (PR #9242, open, not on main).
  - Task's frozen head: `bea8e806aa`, sha256 of the note `a3955597…`.
  - Current head: `5aacd93e4b`, sha256 `27f9b2b9…`. It adds T5: the filled sea can absorb, pair creation is open, and no rate is computed.
- **Landed on `origin/main` `25b8c1874f`:**
  - blocks 54 and 139 (the walk);
  - blocks 62 and 101 (the member at `alpha = K/4`);
  - block 136 (the action with `+(1/2) sum Theta_ij h_ij`, and the densities);
  - block 120 (the stress `Theta_ij = phi_j^T K_i^j`).

**Corrections preserved.**
- The universal kinematic no-go is refuted: interband energy/momentum resonances exist (current head T5). This attempt does not repeat it.
- T1–T4 concern transitions within one band.

**Related prior work.** Block 149 is not mine. My #9204 used the same beat form factor `K_q` for the member–walker identity; it is disclosed and reused here as an independent re-derivation (S1). The related task `nonlinear-moving-source-completion` is distinct and not duplicated.

## 1. Statement attempted

**Setting (supplied clauses; nothing adopted, no gravitational claim).**
- **The coupling** is block 136's `V = (1/2) sum_x Theta_ij(x) h_ij(x)`.
  - `Theta_ij = phi_j^T K_i^j`, with `K_a^j = (1/2)Re[psi^dag(x+e_a) sigma_a (P_j psi)(x) + (P_j psi)^dag(x+e_a) sigma_a psi(x)]` and `P_j = S_j C_j`.
  - `h` is one of the member's transverse-traceless (TT) travelling disturbances at wave vector `q`, with frequency `|p(q)|`, where `p_j = 2 sin(q_j/2)` (block 149 T1 at `alpha = K/4`, unit rate).
- **Single-quantum assumption (explicit).** One disturbance carries energy `|p(q)|`.
- **Process.** Pair creation from the half-filled sea: a filled lower-band state `k' = k - q` goes to an empty upper-band state `k`. It needs `|s(k)| + |s(k')| = |p(q)|`.

**Claims.**
- **(a) Exact suppression at the symmetric resonances.** At `k = q/2 + pi nu` the vertex vanishes. These are the resonances block 149 T5 names.
- **(b) A nonzero allowed amplitude** at an exact non-symmetric resonance.

## 2. Steps

**S1. The vertex. PROVED; CHECKED S1.**
- From the definitions,

  `<k,u| K_a^j(x) |k',u'> = (1/2) e^{-iq.x} e^{-iq_a/2} cos(Kbar_a) (P_j(k) + P_j(k')) u^dag sigma_a u'`,

  with `q = k - k'` and `Kbar = (k + k')/2`. Check S1 verifies this as a Laurent identity in `e^{ik/2}` and `e^{ik'/2}`, for every `a` and `j`.
- The average `phi_j^T` multiplies it by `(1/2)(1 + e^{-iq_j}) prod_{l != j} cos q_l`.
- With `h_ij(x) = eps_ij e^{iq.x}`, the amplitude is

  `(1/8) sum_ij eps_ij (1 + e^{-iq_j}) prod_{l!=j} cos q_l e^{-iq_i/2} cos(Kbar_i) (P_j(k) + P_j(k')) u+^dag sigma_i u-`.

**S2. Suppression at the symmetric resonances. PROVED; CHECKED S2.**
- **The resonances.** At `k = q/2 + pi nu`, `nu` in `{0,1}^3`, and `k' = k - q`, the pair energy is `2|s(q/2)| = |p(q)|` exactly.
- **The vanishing.** There `P_j(k) + P_j(k') = 0` and `h(k) + h(k') = 0`, because `sin 2k` has period `pi` and `sin k` is odd. So both the stress vertex and the energy-density vertex `(1/2)u^dag(h(k) + h(k'))u'` vanish identically.
- **The shape of the resonance set.** The symmetric point is a critical point of the pair energy: the gradient of `|s|` is odd. Numerically it is a saddle (Hessian eigenvalues about −0.69, 1.05, 1.55 at the witness `q`), so the resonance set through it is locally a cone, and the vertex vanishes at its tip.

**S3. An exact non-symmetric resonance. CHECKED S3 (exact, with rigorous enclosure).**
- **The line.** Take `sin(q/2) = (3/5, 5/13, 8/17)` and the line `k = (kappa, q2/2, q3/2)`. With `t = tan(kappa/2)` the resonance condition becomes `sqrt(X + A) + sqrt(Y + A) = 2 sqrt(Z + A)`.
- **The polynomial.** Squared twice, this is an exact degree-8 polynomial in `t`, with the symmetric point `t = 1/3` as a double root.
- **Its other real roots.** They include `-3`, the pi-image of the symmetric point, and `t* = 0.150995526415394654…` (`kappa* = 0.2997268…`). The root `t*` is isolated by a Sturm interval of width below `1e-39`.
- **Genuineness.** At `t*`, `4Z + 2A - X - Y > 0`, so the root solves the unsquared equation, and `|s(k*)| + |s(k*')| - |p(q)|` encloses 0.

**S4. The amplitude is nonzero. CHECKED S4 (rigorous `mpmath.iv`).**
- **The TT tensors.** `eps+ = |e2|^2 e1 e1^T - |e1|^2 e2 e2^T` and `eps x = e1 e2^T + e2 e1^T`, with `e1 = (0, p3, -p2)` and `e2 = p x e1`. They are exactly transverse to `p(q)`, traceless and symmetric.
- **Which components survive.** At `k*`, `Kbar = (kappa* - q1/2, 0, 0)`, and only `j = 1` survives, since the `P_2` and `P_3` sums vanish. The factors:
  - `P_1(k*) + P_1(k*') = sin(2kappa* - q1) cos q1 = -0.17770…`, nonzero;
  - `cos Kbar_1 != 0`;
  - `(1 + e^{-iq1}) cos q2 cos q3 != 0`.
- **The spinor factor.** `|sum_i eps_i1 cos Kbar_i u+^dag sigma_i u-|^2 = Tr(Pi+ (c.sigma) Pi- (c.sigma)^dag)`.
  - For `eps+` it is `0.2432` in the pulled-back (block 120 staggered) convention and `0.4541` without the pullback phase.
  - For `eps x` it is `0.1891` and `0.137`.
  - All are enclosed away from 0.
- **Occupation.** In the half-filled sea the lower state `k*'` is filled and the upper state `k*` is empty. So the fermionic transition `sea -> sea - k*' + k*` has amplitude equal to this one-body matrix element, up to sign.

## 3. Result, first unresolved step and obligations

**Result.**
- With block 136's stress coupling and one TT quantum of energy `|p(q)|`, the interband single-quantum process (pair creation from the filled sea) has a nonzero allowed amplitude at an exact resonance.
- The same vertex vanishes exactly at the symmetric resonances `k = q/2 + pi nu`, where the pair energy equals the member's frequency identically.
- So block 149 T5's open channel is not suppressed by the vertex, except at its symmetric points.

**First unresolved step: the rate.** It needs:
- the phase-space integral of `|amplitude|^2` over the resonance surface, where the vertex vanishes linearly at the symmetric saddle;
- the member quantum's normalization, since the landed notes supply no quantization of the member.

**Remaining obligations.**
1. The rate and its threshold behaviour. With the staggered mass the channel closes for `|p(q)| < 2mu` (block 149 T5).
2. The clock (energy-density) and shift couplings at non-symmetric resonances.
3. Any supplied selection rule that would kill these resonances. None was found here.
