# Referee report: J:derive:the-ledgers-force-identity-exactly-on-the-lattice:a1

- **Author:** `w-macbookpro90c72-j152a` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-jc631` (`grok-4.6`). Different model family.
- **Checks:** bond form, polarization, sublattice counterexample, parity, twelve plane waves, and the upwind telescope, in Gaussian rationals. The author's script is not called.

## The statement

The force is the bond cross energy times the difference of the rate: `f_j(x) = d_jφ(x) ε_j(x) + d_jφ(x−e_j) ε_j(x−e_j)`. It is not a function of the energy density. Curl ledgers stay rate-free; a rate-carrying ledger's requirement, built from `𝔢` and `J`, matches the content only at long wavelength. Reach three carries `cos 2k`.

## Steps

**S2–S4.** With `C[v]ψ(x) = ½(v(x)ψ(x+e) + v(x−e)ψ(x−e))` and `dφ(x) = φ(x+e)−φ(x)`, the real part splits into the two bonds. On one fixed state of the 4-torus, every site and direction matches, including the two-step form with its extra `½`. Polarization `ε = (ρ_x+ρ_y)/2 − ½ Re[(dψ)†(dχ)]` matches on the same state. `dφ = ½Λ du` with `u = 2 log φ` cancels algebraically.

**S5.** An even-sublattice state has `ρ = 0` at all 64 sites, because `H` only hops, and `f_1 ≠ 0` at 56 sites once `φ` varies. No factorisation through the energy density.

**S9.** `ΓH = −HΓ` on that torus.

**S10.** Twelve plane waves on the 4-torus (one momentum in `{π/2, 3π/2}`, energy `±1`) are eigenstates. The first-order forces are `𝔢 cos k_j (η(x+e)−η(x−e))` and `½ 𝔢 cos 2k_j (η(x+2e)−η(x−2e))`. The waves `(π/2,0,0)` and `(0,π/2,0)` at energy 1 both have `𝔢 = 2` and zero bond current, and opposite `cos k_1`.

**S8.** At `B = 0` the upwind `δu_x = −Σ_a ξ_a(x)(1 − w(x−e_a)/w(x))` cancels `Σ w_x(ξ(x+e)−ξ(x))` exactly on the 4-torus.

The curl ledger's invariance under `B → B+dξ` is used as stated from block 64; it was not re-derived from the note. The kinetic term in (c) is the Lagrangian substitution given in the attempt.

## Verdict

The partial result survives. The content's force is the bond form, and a requirement built only from `𝔢` and `J` cannot match it beyond long wavelength.
