## 3. Method (claim type: construction + numerical evidence)

### 3.1 Why not a local finite-temperature trace (exact obstruction, proved)

**Lemma 3.** In a periodic worldline (trace) representation, let `n_p` be the net signed number of
flips of plaquette `p` over one period (sign = sense of circulation reversed). Periodicity forces the
integer chain `n = sum_p n_p p` to be a 2-cycle (`∂n = 0` on links). Pair insertion/removal of
consecutive flips of one plaquette (opposite signs) and time shifts leave every `n_p` unchanged, so a
local-update trace QMC samples only the `n = 0` class, whereas `Tr e^{-beta H}` sums over all classes
(cube boundaries and the three global plane classes).

*Proof.* Consecutive flips of the same plaquette with no intervening change of its links alternate
the circulation, hence carry opposite signs; insertion/removal changes `n_p` by `+1-1 = 0`; shifts do
not change counts. ∎

Numerical confirmation (L=2, exact thermal trace on the 864 component, `logs/step2_validate_L2.log`
[INFO] lines): at beta=4, V=0 the local trace QMC gives E = -7.95 vs exact -9.02 and N_flip z = +6.9;
at V=0.5, E = -3.08 vs -4.24. The class restriction is a large bias, not a subtlety. Repairing it needs
non-local class-changing moves (cube moves change only the local classes; the three plane classes need
L^2 coherent flips); I did not build them.

### 3.2 What is used: guide-free open-path projector (PIGS-type), continuous time

`Z(T) = sum_{s,s'} <s'| e^{-T H} |s>` over the canonical flip component = `<1|e^{-TH}|1>` with the
uniform trial state `|1>` on both ends. No importance function: the uniform vector has positive
overlap with the Perron ground state of the component, the path weight is
`g^{n} exp(-V ∫_0^T N_flip dτ)` (nonnegative, §2), and the middle `τ = T/2` is distributed as
`|psi_{T/2}|^2` with `psi_{T/2} = e^{-TH/2}|1>`, which converges to `|psi_0|^2` as `T -> ∞`.

Moves (all detailed-balanced; `scripts/qmc.py`): (i) pair insertion/removal of two flips of one
plaquette inside a segment where its four links are constant; (ii) single-kink time shift within the
same window; (iii) single-kink insertion/removal at either free end (changes start/end state, so all
flip-count classes are reachable — no class restriction); the diagonal `V` weight is integrated
exactly piecewise (`delta_toggle_fast`, bit-identical to a reference implementation on 8524 random
intervals, `logs/test_delta_fast.log`). Estimators: middle-state `S_T(k)`, flippability spectra,
`E_mid = V<N_f(mid)> - <#kinks in (T/2-w, T/2+w)>/(2w)`, mixed energy
`E_mix = (V-g)<N_f(end)>` (= Rayleigh quotient of `psi_{T/2}`, an upper bound on the component
ground energy, monotone in `T`), and the transverse imaginary-time correlator
`C(τ) = sum_a sum_{b≠a} Re <E_b(k_a, T/2) E_b(k_a, T/2+τ)^*>/N_v`.

Note: `E_mid` and `E_mix` estimate the **same** exact number `<1|H e^{-TH}|1>/Z` (H commutes with the
propagator). Their difference is therefore a parameter-free equilibration diagnostic of the middle.

### 3.3 Sampler bug found and fixed during validation (disclosed)

The first validation showed the kink count low by 1.5-3% (z down to -4.5 against the exact identity
`<n> = gT<N_f(end)>` at V=0). Single-move transition rates matched a pure-Python reference exactly;
the cause was a **state-dependent number of moves per sweep** (proportional to the current kink
count), which biases the law sampled at measurement times. Fixed by freezing the number of moves
after thermalisation; the exact fixed-end `P(n)` at T=0.3 is then reproduced
(0.1675/0.2002/0.2403/0.1807 vs 0.1665/0.1998/0.2397/0.1798).
