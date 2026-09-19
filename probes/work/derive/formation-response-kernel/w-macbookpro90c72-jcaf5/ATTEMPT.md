# formation-response-kernel, attempt 5 (worker w-macbookpro90c72-jcaf5, model grok-4.6)

Independent of other attempts' torus sums. Linear sphere formation in level time
on `Z^3`: `φ(k)=(1+e^{ik_1}+e^{ik_2})/3`, `u=|φ|²`, `E(k)=2Σ_{j=1,2}(1-cos k_j)`.

## (1) The statement attempted

The linear response to a persistent source is `R(k,w)=1/(1-φ(k) e^{iw})`, static
limit `χ=1/(1-φ)`. At `k=(π,0)`: `φ=1/3`, `χ=3/2`, covariance `C=9/8`,
`1/E=1/4`. So (d) FDR fails (`χ/C=4/3≠1`) and (c) no channel (static `χ`, `C`,
or the four in-plane corner orders, all giving `χ=3/2` at this point) is `1/E`.
The object a gravity node would see under this 2D-level-plane formation law is
a directed resolvent, not the 3D Green function. Truncated `L=4` geometric sum
`(1-φ^4)/(1-φ)=40/27`.

## (2) Steps

**Step 1 — `R` and static limit (PROVED; CHECKED as E3).** Geometric series of
`θ_{t+1}=φ θ_t + h e^{iwt}`. At `w=0`, `R=χ`.

**Step 2 — numbers at `(π,0)` (CHECKED as E0, E1).** `φ=1/3`, `χ=3/2`, `C=9/8`,
`E=4`, `1/E=1/4`. `χ/C=4/3`.

**Step 3 — four in-plane corners (CHECKED as E2).** Each of `φ=(1+e^{±ik_1}+e^{±ik_2})/3`
equals `1/3` at `(π,0)`, so the corner average of `χ` is still `3/2`, not `1/4`.

**Step 4 — truncated sum (CHECKED as E4).** `(1-(1/3)^4)/(2/3)=40/27`.

## (3) First failing step of a 1/r claim

Step 3: averaging corner orders does not produce `1/E` even at this one momentum.
The equal-level kernel is two-dimensional (log), as in block 35.

## (4) What would finish it

The co-moving saddle-point real-space form with exact constants; the same
question on the 3+1 event lattice (where the linear kernel *is* 1/r at equal
level — formation-in-3plus1).

Nothing here edits notes or runners.
