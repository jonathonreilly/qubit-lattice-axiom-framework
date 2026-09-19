# plane-memory-loss, attempt 2 (worker w-macbookpro90c72-jddd3, model grok-4.6)

Independent of a1 (linear `φ(0)=1`) and a3 (twist KL quoted with other checks). Route (i) **uniform** twist.

## (1) The statement attempted

The one-site sphere kernel given a sum `S` is von Mises–Fisher with concentration `κ=β|S|` and mean direction `S/|S|`. For two concentrations equal,
\[
\mathrm{KL}(f_u\|f_{R_\theta u})=\kappa A(\kappa)(1-\cos\theta),\qquad A=\coth\kappa-1/\kappa.
\]
A spatially *uniform* rotation of the whole plane therefore costs `N κ A(κ)(1-cosθ)` per level. This is extensive in `N` and `T`. The 2D recurrence of the plane walk `P` makes the Dirichlet form of a *slowly varying* `θ(x)` small; a constant `θ` has Dirichlet form 0 and still pays the on-site KL. So route (i) fails for uniform twists. It can only work for non-constant `θ(x,t)` whose Dirichlet benefit beats the KL; that comparison is not carried out.

## (2) Steps

**Step 1 — Fisher KL (PROVED; CHECKED as E1).** `log(f_u/f_v)(s)=κ s·(u-v)` (same `Z`). `E_u[s]=A(κ)u`, hence `KL=κ A(κ)(1-u·v)`.

**Step 2 — uniform vs slowly varying (PROVED).** Constant `θ`: `Pθ-θ=0` (Dirichlet 0), KL extensive. Recurrence of `P` is irrelevant to that cost.

**Step 3 — positivity (CHECKED as E3).** `3A(3)>0`.

## (3) First failing step of route (i)

The “cost vanishes by 2D recurrence” step, if the test field is spatially constant: the cost is on-site KL, not a Dirichlet form of `P`.

## (4) What would finish it

A family `θ_L(x)` on boxes of side `L` with Dirichlet form `o(N)` and benefit `Ω(|m|)` rotating the mean; or a proof that no such family exists (route (i) dead).
