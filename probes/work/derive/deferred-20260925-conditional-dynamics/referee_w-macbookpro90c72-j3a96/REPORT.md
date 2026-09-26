# Referee: deferred-20260925-conditional-dynamics a1

Worker `w-macbookpro90c72-j3a96` (`grok-4.6`). Author `w-jonathonsmac4f50-jd81c` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed countermodel. Under the supplied Heisenberg bond, record compression, and trace rule, the isolated site's `λ` is not a function of the final records. It depends on when the partner's record formed.

## What was checked

- **Records as fields.** `P_q σ_a P_q = q_a P_q` for every unit `q`. Five unit records, three at 120° and an antipodal pair, sum to zero.
- **The bond.** `σ·σ = 2 SWAP − 1`, and `U(τ) = e^{i J τ}(cos 2Jτ − i sin 2Jτ SWAP)` solves `i dU/dτ = J σ·σ U`.
- **The history.** `x` starts at `+z` and `y` at `+x`. The trace-rule weight of `y`'s record `+z` is `(1 + sin² 2Jτ)/2`. The conditional `z`-component of `x` is `cos²(2Jτ)/(1 + sin² 2Jτ)`.
- **Isolation.** In the field `J ẑ`, the Bloch vector precesses at `2J` and its time average is `(0, 0, r_z)`.
- **The same records.** `λ(0) = 1`, `λ(π/(8J)) = 1/3`, `λ(π/(4J)) = 0`.
- **The other outcome.** A `−z` record leaves `x` at `+z` for every `τ`.
- **A supplied clock.** A constant hazard `f`, weighted by the record's own weight, gives `λ̄ = (8J² + f²)/(24J² + f²)`. It depends on `f/J`.
