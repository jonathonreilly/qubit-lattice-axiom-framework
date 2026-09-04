# Uniform Energy-Density Rescaling: Background Susceptibility And Continuity Checks

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim scope:** On a declared free one-dimensional staggered-fermion
comparator at `N=256`, the static susceptibility of a background modulation of
the full local energy density vanishes at zero momentum under uniform
Hamiltonian rescaling, has a measured leading `q^2` coefficient at the sampled
masses, and satisfies the implemented lattice continuity identity.

**Primary runner:**
[`scripts/energy_channel_induced_kernel_2026_07_08.py`](../scripts/energy_channel_induced_kernel_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/energy_channel_induced_kernel_2026_07_08.txt`](../logs/runner-cache/energy_channel_induced_kernel_2026_07_08.txt)

## Declared Background Calculation

Let `h_n` be the local one-body energy density whose sum is the comparator
Hamiltonian `H`. For a nondynamical background profile `ell_n`, the perturbed
Hamiltonian is

```text
H(ell) = H + sum_n ell_n h_n.
```

The runner computes the positive Lehmann susceptibility

```text
chi(q) = 2 sum_occ,emp |<emp|h(q)|occ>|^2/(eps_emp-eps_occ).
```

The word “background” is load-bearing: `ell_n` is an external parameter in
this calculation, not a field degree of freedom.

## Results

1. **Uniform rescaling.** At `q=0`, `h(0)=H`. In the energy eigenbasis its
   occupied-to-empty matrix elements vanish, so `chi(0)=0`. The runner obtains
   values between `2.0e-28` and `4.1e-28` for
   `m in {0,0.05,0.2,0.5}`. Independently, the ground-state energy of
   `(1+epsilon)H` is linear in `epsilon` to relative second-difference error at
   most `1.4e-15`.
2. **Finite-momentum fit.** Fitting the four smallest nonzero sampled momenta
   to `chi(q)=Aq^2+Bq^4` gives positive coefficients
   `A=7.67,1.46,0.0334,0.00149` at the four masses, with relative fit residual
   at most `2.9e-2`. These are comparator- and fit-window-specific response
   measurements.
3. **Continuity identity.** For `m in {0.2,0.5}` and momentum indices
   `q_index in {1,2}`, the runner verifies

   ```text
   (eps_j-eps_i)<j|h(q)|i> = (1-exp(-iq))<j|j_E(q)|i>
   ```

   and the corresponding Lehmann-kernel relation. The largest pairwise and
   kernel relative residuals are `4.3e-12` and `1.4e-13`.

## What Does Not Follow

The zero uniform susceptibility is the kinematics of rescaling the entire
Hamiltonian. It does not make the background profile dynamical. It does not
establish a massless particle, a gauge redundancy, a lapse field, a Poisson
law, gravitational dynamics, or an energy-source bridge. The finite-`q`
response is a matter susceptibility only.

## Boundaries

- The calculation uses a free `d=1`, `N=256` comparator and the displayed
  local-energy convention.
- The response and fitted coefficients are numerical. The exact algebraic
  input is the uniform identity `sum_n h_n=H` and the local continuity
  relation implemented by the runner.
- No interacting or compact-gauge leg is included; no validated prerequisite
  engine for such a leg is supplied as a dependency.
- Audit classification and verdict remain the responsibility of the
  independent audit lane.

## Dependencies

No prior source note is load-bearing. The comparator, background coupling,
response convention, and continuity check are defined here and implemented by
the paired runner.
