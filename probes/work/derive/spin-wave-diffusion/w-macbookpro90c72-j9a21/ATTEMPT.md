# spin-wave-diffusion, attempt 4 (worker w-macbookpro90c72-j9a21, model grok-4.6)

Own plan: exact return sums `G_L` for the 2+1 kernel at `L=2,3,4` and the linearized zero-mode identity, before combining with a1–a3. Those attempts (same family) treated the nonlinear Jacobian and `L=1` self-noise; this is the linear kinematic table they interpolate.

## (1) The statement attempted

**Statement (PARTIAL).** For `φ=(1+e^{ik_1}+e^{ik_2})/3`,
`1-|φ|²=(6-2\cos k_1-2\cos k_2-2\cos(k_1-k_2))/9`. The plane return sum `G_L=N^{-1}∑_{k≠0} 1/(1-|φ|²)` is exactly `G_2=27/32`, `G_3=11/9`, `G_4=189/128`. The linearized zero mode has `φ(0)=1` and Cartesian variance `σ² t / N` per component, so `D_1 L²/σ²=1` exactly for the linear law. The nonlinear factor `1/|m|²` and the `L=1` self-noise of a1 are not re-derived here.

## (2) Steps

**Step 1 — cosine identity (PROVED; CHECKED V1).** Expand `|1+e^{ik_1}+e^{ik_2}|²/9`.

**Step 2 — `G_L` (CHECKED V2).** Cosines in `Q` on `L=2,3,4`.

**Step 3 — zero mode (PROVED; CHECKED V3).** `P` is an average of three predecessors, doubly stochastic, `φ(0)=1`. Mean of `N` iid noises of variance `σ²` has variance `σ²/N`.

## (3) Where the route stops

Linear law only. The nonlinear `D_1 L²/σ² → 1` at fixed `L` as `β→∞` follows if the extra factors `1/|M|²` and a1’s `[1-6β/(e^{6β}-1)]/A(3β)` both tend to 1, which they do (`σ²→0`, `A→1`), but that identification is a1+a2, not proved here as a single expansion with remainder.

## (4) What would finish it

A remainder `O(σ² G_L + 1/N)` controlling both factors together, two-sided, compared with the executed `1.34,1.14,1.06,1.02`.
