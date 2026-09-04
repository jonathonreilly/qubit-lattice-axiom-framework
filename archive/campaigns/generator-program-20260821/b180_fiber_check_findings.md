# Block 180 adversarial fiber check (exact arithmetic)

Target: the supervisor's `THE FIBER THEOREM`, on its stated imposed fixtures.  No worktree files were edited.
Conventions: `herm(A)=(A+A^dagger)/2`; at 12x6, columns of `B` are
`f_(t,b)=3^(-1/2) sum_(j=0)^2 omega^(-j)|t,b+2j>`, ordered `(t,b)`;
`J=[[0,1],[-1,0]]`, so `J^2=-I`.

## C1 — 12x6 restriction

Rebuilt `Width(6,"const")` after setting `RULES["const"](t,x)=7/5`.
`Q` and `W9=herm(Q^-1)` are 36x36; `B^dagger B=I_12`, `QB=B(B^dagger QB)`,
`W9B=B(B^dagger W9B)`, and `W_1=herm(Q_1^-1)` exactly (with two-sided inverse residuals zero).
Thus `Q_1=B^dagger Q B` and `W_1=B^dagger W9 B` are genuine 12x12 invariant restrictions.
All off-diagonal 2x2 blocks in row or column `t=1` vanish in BOTH `Q_1` and `W_1`.
Every diagonal block `(W_1)_(tt)=w_t I_2` exactly, with
`w_0=w_2=1124199510121924999000/2102382743382041526923`,
`w_1=875/1462`, `w_3=w_5=59966038499032694000/123669573140120089819`,
and `w_4=2667060781000/5517939189281`.
Hence the claimed reflection classes `{0,2}`, `{3,5}`, `{1}`, `{4}` are exact.
**Verdict C1: PASS.** The matrix decomposition and degeneracy claims are correct on this fixture.

## C2 — the record-slice block as a dial law

Leaving `s_x=s` symbolic before restriction gives exactly
`Q_c=[[43/35,43s/35],[-43s/35,43/35]]=(43/35)(I+sJ)`; both `c` cross-blocks remain zero symbolically.
At `s=3/5`, the off-diagonal magnitude is `129/175`; at `s=1/3` it is `43/105`;
at `s=-2/5` it is `-86/175`.  Therefore `b=a s_x` is a law on this construction, not a one-point fit.
The eigenvalues are `(43/35)(1 +/- i s)` and `det Q_c=(1849/1225)(1+s^2)`.
At `s=0`, `Q_c=(43/35)I_2`: the eigenvalue is double and transport supplies no eigenline splitting.
**Verdict C2: PASS.** The law and its stated degenerate limit are exact (up to the displayed convention for `J`).

## C3 — 8x4 replication

Set `COVER_T=8`, used `Width(4,"const")`, and used the natural order-two `x -> x+2`
character `2^(-1/2)(|t,b>-|t,b+2>)`.  The resulting invariant restrictions are 8x8.
The `t=c=1` row and column blocks vanish off diagonal in both restricted `Q` and `W9`.
Its blocks are again `Q_c=(43/35)(I+s_x J)` symbolically and `W9_c=(875/1462)I_2`
at `s_x=3/5`.  Exact invariance and `W_restricted=herm(Q_restricted^-1)` also hold.
**Verdict C3: PASS.** The decoupling and c-block law are not a 12x6 wrap accident.

## C4 — the counting inference

The record pin selects a complex 2-dimensional direct summand; diagonalizing `Q_c` at `s_x!=0`
splits it as TWO independent one-dimensional complex eigenspaces.  Conjugation exchanges them,
but exchange by an anti-linear symmetry is not identification and does not lower complex dimension.
Their arbiter implements only `r_from_slot_count(n)=n/2` and `q_from_r(r)=(1+2r)/3`.
For its holomorphic cell, “one complex slot” is obtained by first proving a REAL rank-2 doublet
with `J^2=-P_d`, then dividing the REAL slot count by two.  It has no conjugation-gauge operation.
Feeding the present 2x2 COMPLEX holomorphic block honestly gives `n=2`, hence `r=1`, `Q=1`;
`n=1`, `r=1/2`, `Q=2/3` follows only after imposing a reality condition/anti-linear quotient
relating the two eigen-coordinates.  That quotient is neither produced by decoupling nor by splitting.
**Verdict C4: FAIL (central refutation).** “Conjugation is gauge” is an added selector/quotient premise,
not an arbiter-compatible consequence; the theorem reduces 12 copies to 2, not 1.

## C5 — non-constant reflection-symmetric volume

At 8x4 take the established exact profile `nu(t,x)=(1,2,3,4)_x`, repeated in `t`.
With zero shear its quotient Hodge is non-flat diagonal `(25/16,3/2,17/8,17/6)` per level,
while both reflection defects `rHr-H` and `rHr-H^T` have exactly zero nonzero entries.
Restoring the fiber-fixture shears and dials, the FULL four-site `t=1` slice remains a direct
summand of both `Q` and `W9`; therefore projected cross-level blocks still vanish.
But the order-two `k=1` space is not invariant: `(I-BB^dagger)QB` has 52 nonzeros
(8 from the c columns), including `-9 sqrt(2)/64`; the W9 leakage has 40 (4 from c),
including `20850 sqrt(2)/528989`.  The compressed blocks become
`Q_c=[[59/32,13/10],[-13/10,13/6]]` and
`W9_c=diag(209900/528989,582350/1586967)`, so neither claimed c-block law nor fiber scalarity survives.
**Verdict C5: FAIL for fiber selection (temporal decoupling alone survives).** The theorem is carrier-locked.

## Overall verdict

**REFUTED.** C1-C3 establish a true constant-carrier matrix lemma, but C4's step from a selected
`C^2` sector to one complex slot is invalid under the cited arbiter, and C5 shows the purported
fiber sector is not stable under a non-flat reflection-symmetric volume already admitted by the lane.
Safe boundary: the disconnection selects a two-complex-dimensional record-slice sector on the
constant carrier; transport diagonalizes it into two conjugate eigenlines.  No existing rule quotients them.

## Eight-line summary

1. Exact 12x12 restrictions exist and the constant-carrier `t=1` block decouples in Q and W9.
2. Every constant-carrier W9 diagonal fiber is scalar; `{0,2}` and `{3,5}` are exact degeneracies.
3. Symbolically, `Q_c=(43/35)(I+s_x J)`; checks at `3/5,1/3,-2/5` and `0` close exactly.
4. At `s_x=0` the block is scalar and transport supplies no eigenline distinction.
5. The 8x4 constant-carrier order-two character has the same decoupling and c-block law.
6. Their arbiter counts two independent complex eigenlines as two slots: `r=1`, `Q=1`.
7. Calling the conjugate exchange “gauge” is an extra quotient/reality premise, not arbiter machinery.
8. A non-flat reflection-symmetric volume keeps the whole slice disconnected but destroys the fiber theorem.
