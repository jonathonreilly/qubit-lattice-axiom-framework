# formation-in-3plus1, attempt 6 (worker w-macbookpro90c72-j30e1, model grok-4.6)

Different route from a1 (which settled the linear dichotomy `d>2`). This attempt
takes the mean-field of the 4-predecessor sphere PCA and the small-`k` envelope
of the linear kernel. `A(κ)=coth κ − 1/κ`. Four backward predecessors on `Z^4`.

## (1) The statement attempted

**Mean-field LRO threshold.** The map `m ↦ A(4β |m|)` on `[0,1]` has `m_t → 0`
from every initial value iff `β ≤ 3/4`. At `0` the derivative is `4β/3`. This
is below the 2+1 mean-field threshold `β=1` (three predecessors).

**Linear small-`k` envelope.** Hessian eigenvalues of `1−|φ|²` at `0` are
`1/8` (once) and `1/2` (twice), so to leading order
`4 σ²/|k|² ≤ S(k) ≤ 16 σ²/|k|²`.

Nonlinear sphere LRO is not proved (triangle `|S|≥4|m|` has the wrong sign).

## (2) Steps

**Step 1 — `A(κ)/κ < 1/3` for `κ>0` (PROVED; CHECKED as E0).**
Same `q,r` as plane-memory-loss a4: `q' = κ(κ cosh−sinh)`, `(κ cosh−sinh)'=κ sinh≥0`.

**Step 2 — threshold `β=3/4` (PROVED from 1; CHECKED as E1).**
`A(4β m)=(4β m)(A/κ)< (4β/3) m`. Contractive on `(0,1]` iff `4β/3≤1` i.e. `β≤3/4`,
strict for `β<3/4`. Identity `4·(3/4)/3=1`. Series of `A(4m)/m` starts at `4/3`.
`A(3)<1` (aligned point at `β=3/4`).

**Step 3 — Hessian envelope (CHECKED as E2).**
Hessian eigenvalues `{1/8, 1/2, 1/2}`. Leading quadratic
`(1/2)λ_min |k|² = |k|²/16 ≤ 1−|φ|² ≤ |k|²/4`, hence the stated `S` envelope.

**Step 4 — nonlinear LRO (fails for the same reason as 2+1).**
`|S|≥4|m|` and `A` increasing give `A(β|S|)≥A(4β|m|)`, the wrong sign.

## (3) First failing step of nonlinear LRO

Step 4.

## (4) What would finish it

A correlation inequality replacing `|S|` by something strictly below `4` when
`|m|<1`, or an energy-entropy argument at large `β`.

Nothing here edits notes or runners.
