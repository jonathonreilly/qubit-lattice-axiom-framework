# Block 181 adversarial reality-premise check (exact arithmetic)

Scope: `Bench("12x6",12,6)`, `r=Bench.r`, constant volume `7/5`, pinned levels
`{0,1}` at shear zero and the others at `3/5`, `s_t=0`, `m=1`; no worktree edit.
Let `a=43/35`, `d=129/175`, `J=[[0,1],[-1,0]]`, and
`u_+=(1,i)/sqrt(2)`, `u_-=(1,-i)/sqrt(2)`.

## C1 — rebuild of all four legs

For `B_k=(f_(k,1,0),f_(k,1,1))`, exact reduction gives
`B_k^dag B_k=I_2` and, for BOTH `k=1,2`,
`B_k^dag Q(+3/5) B_k=aI+dJ`, `B_k^dag Q(-3/5) B_k=aI-dJ`.
The fixed-slice reflection is the identity on these columns.  Hence
`Theta f_(1,1,b)=r conj(f_(1,1,b))=f_(2,1,b)` for `b=0,1`, entrywise.
Define `g_+=B_1u_+`, `g_-=B_1u_-`, `h_+=B_2u_+`, `h_-=B_2u_-`.
At `s_x=+3/5`, `Qg_+=lambda_+g_+`, `Qg_-=lambda_-g_-`,
`Qh_+=lambda_+h_+`, `Qh_-=lambda_-h_-`, where
`lambda_+=43/35+(129/175)i`, `lambda_-=43/35-(129/175)i`.
Exactly, `Theta g_+=h_-`, `Theta h_-=g_+`, `Theta g_-=h_+`, and
`Theta h_+=g_-`: the orbits are `O_+={g_+,h_-}` and `O_-={g_-,h_+}`.
At `s_x=-3/5`, the same four lines remain eigenlines and every `lambda_+/-`
assignment reverses; equivalently `Q_c(-3/5)=Q_c(+3/5)^T`.
**Verdict C1: PASS.** Every algebraic leg of the supervisor's construction closes.

## C2 — precedent is not the arbiter's rule

The landed arbiter commits to this algorithm, and only this algorithm:
`real_slots=tr(P_d)=2`; under a SUPPLIED holomorphic polarization with
`J^2=-P_d`, `complex_slots=real_slots//2=1`; then `r=n/2` and
`Q=(1+2r)/3` additively (`berezin_detc...py:247-264,279-289`).
Its premise text says the doublet polarization is **SUPPLIED**, either two real
slots or a **chosen** `J` giving one complex slot, and says no route there derives
the choice (`KOIDE_BEREZIN...NOTE:41-50`).  Neither runner nor premise mentions
`Theta`, antiunitary orbits, or an operation quotienting arbitrary conjugate lines.
b179 itself built the real `R[Z_3]` rank-2 doublet, then chose the holomorphic
realization `T_1` with ambient `i` as `J` (`b179_embed_findings.md:44-56`); its
being `{f_1,f_2}` under `Theta` is therefore a coincident description, not its rule.
Classification: **consistent-but-unstated, not entailed**.  Promoting it to
“every `Theta`-orbit automatically is one slot” contradicts POLARIZATION-SELECT's
explicit supplied/not-derived boundary.  The precedent-to-rule inference fails.
**Verdict C2: FAIL (central).** The reality premise is not dissolved by the arbiter.

## C3 — orientation is grading-equivalent, not a selector

`s_x=3/5` is fixed for this imposed one-fixture benchmark at
`ADMISSIBILITY...EMBEDDING...NOTE:64-67` and as `BENCH_SX=3/5` at closure-audit-two
runner line 568; the committed action *class* itself keeps symbolic `s_x`.
The landed staggered grading `X_0(t,x)=(-1)^(t+x)` commutes with `H_q` and
anticommutes with the connection residue (`...SCALING_PROBE...NOTE:112-126`).
Thus, exactly at `s_t=0`, `X_0^2=I` and
`X_0 Q(+3/5) X_0=Q(-3/5)`; moreover `X_0 g_+=-g_-`, `X_0 h_-=-h_+`, so it
swaps `O_+ <-> O_-`.  The sign is a landed grading-equivalent orientation
convention, not an invariant physical discriminator (and `X_0` is not a
fixed-`s_x` symmetry or an established gauge quotient).
Even on the alternative “physically fixed sign” reading, the sign only orders
the eigenvalue labels; it supplies no projector that deletes the other orbit.
**Verdict C3: FAIL.** Neither reading yields a justified one-orbit count.

## C4 — sector bookkeeping

The four lines do reduce to **two**, not one, slots under the proposed orbit rule:
`{g_+,h_-}` and `{g_-,h_+}`.  Each orbit already contains its own `k=2`
conjugate/antiparticle partner, since `Theta` closes within that orbit; therefore
`O_-` is not the missing antiparticle half of `O_+`.  It is a second independent
doublet/copy candidate (calling it a spectator “generation” would add semantics).
Keeping both gives `n=2`, `r=n/2=1`, `Q=(1+2r)/3=1`.  Selecting `O_+` (or `O_-`)
to obtain `n=1`, `r=1/2`, `Q=2/3` leaves the other orbit unaccounted and is
exactly an additional selector/quotient premise; the sign of `s_x` does not do it.
**Verdict C4: FAIL.** The final `Q=2/3` arithmetic is not closed.

## C5 — volume-carrier scope

The b180 finding stands exactly.  On its 8x4 profile `nu_x=(1,2,3,4)`, the full
`t=1` slice remains a direct summand of `Q,W9`, but the order-two character space
leaks: Q leakage is 52 nonzeros (8 from `c`), W9 leakage 40 (4 from `c`), with
the cited `-9sqrt(2)/64` and `20850sqrt(2)/528989`.  The compressed blocks are
`[[59/32,13/10],[-13/10,13/6]]` and
`diag(209900/528989,582350/1586967)`, not the fiber law/scalar pairing.
**Verdict C5: PASS as an attack.** Only temporal disconnection survives; the fiber is carrier-locked.

## Overall verdict

**REFUTED.** C1 verifies the supervisor's four exact identities, but C2 defeats
the precedent-to-rule step, C3 defeats orientation-as-selector, and C4 exposes
the leftover second doublet.  The honest constant-carrier result is two
`Theta`-orbits/two complex slots, hence `r=1,Q=1`, absent a named new quotient.

## Eight-line summary
1. C1 PASS: `Theta f_1=f_2`, both eigenline pairings, exact eigenvalues, and the `s_x` assignment swap all close.
2. C2 FAIL: the arbiter counts a supplied `J`-polarized real doublet; it states no general `Theta`-orbit rule.
3. The b179 `Theta`-orbit description is consistent-but-unstated coincidence, not an entailed counting precedent.
4. C3 FAIL: landed `X_0` maps `Q(+3/5)` to `Q(-3/5)` and swaps the two orbits; the sign is not a selector.
5. C4 FAIL: four eigenlines become two `Theta`-orbits, and each orbit already contains its own conjugate partner.
6. The leftover orbit is a second doublet/copy candidate; keeping it yields `n=2,r=1,Q=1`, not `Q=2/3`.
7. C5 PASS as attack: b180's non-flat reflection-symmetric volume counterexample is reproduced exactly.
8. Overall: the premise-free dissolution is refuted; `Q=2/3` still needs a named one-orbit selector/quotient.
