# Focused independent supplier check

**Disposition:** the stationary-class witness, coherent first-event approximation, positive bounded-energy cap, refusal and mean-energy estimates, and programmed one-shot evolution are mathematically supported within their stated conditional scope. No consequential mathematical defect was found. One normalization sentence should be made explicit when this construction is reused: the mark sum chooses either the resolved instrument or the coherent instrument, not their union.

The checked source is `../independent-energy-supplier-route/REPORT.md`, SHA256 `3775534ada55c1625ea207af407104261006ade7eb87bcf06c8a77ebfe0a0733`. `FROZEN_INPUTS.json` binds its other files, five previously independently checked coefficient/domain inputs, and seven actual landed source arguments read at main `e75578f7136401d4bd750131671aed9212c06291`. This is a focused mathematical check, not a formal no-go gate, audit, native-premise adoption, or a review of every transitive source claim.

I read the author report and checker, then independently derived the supplier identities below and wrote a different exact finite-battery fixture without importing or running the author's program. The already checked rotor compression coefficients were reused as expressly authorized; they were not regenerated. Their frozen identities all match the author's bindings. No other campaign output was edited.

## 1. Original instrument and stationary-apparatus witness

For a torus with `N` A vertices there are `6N` A-to-B edges. The two alternative original instruments have:

- Resolved marks `(a,b,σ)`, `σ=±`: `12N` labels and `B_m†B_m=5I` on the prebirth sector.
- Coherent marks `(a,b,c)`: `6N` labels and `B_m=B_++B_-`, with `B_m†B_m=10I` there.

Each selected family has total loss `60NI`, so the corresponding `W=(60N)^(-1/2) Σ_m B_m⊗|m>` is an isometry. Taking all three labels per edge together would instead give `W†W=2I` and is not the source's intended original instrument. All checks here use one stipulated family. The coherent branch is not split into extra measured sign labels.

Let `U` strongly commute with additive endpoint energy, the independent apparatus state be stationary, and each fixed mark effect commute with apparatus energy. Moving the product time-translation group through `U`, the initial apparatus state, the effect and the partial trace proves marked-map covariance. For a nonzero single-Kraus map `ρ↦c BρB†`, equality of all its input outputs makes the two time-conjugated Kraus operators differ by a phase. This remains true for infinite separable input/output Hilbert spaces: equality on pure states and their superpositions fixes one common phase. Continuity and the group law make that phase a character of the real line. Thus

\[
e^{-it h_{out}}B e^{it h_{in}}=e^{-i\omega t}B,
\quad h_{out}B-Bh_{in}=\omega B.
\]

The generator relation is justified on finite-field physical vectors, which are mapped by the finite-word `B` into the output energy domain. With `B†B=nI`, a necessary consequence is

\[
G=n^{-1}B^\dagger h_{out}B-h_{in}=\omega I.
\]

The report's four-edge circulation `z` has zero divergence at every vertex and is nonzero. Reading the frozen full Laurent coefficients yields `c_z=2/5` for minus, plus and coherent marks. The electric compression is diagonal in this field basis, so

\[
\langle z|G|0\rangle=2\delta/5\ne0.
\]

This directly contradicts the necessary scalar compression. The normalized `(|0>±|z>)/√2` expectations differ by `4δ/5`, also verified. No inverse of `B` or inference from a single energy mean is used. The conclusion requires **all prebirth inputs**, a stationary independent apparatus, additive conservation and invariant fixed-label readout. It does not exclude one-orbit matching, correlated inputs, changing interaction energies or coherent apparatus resources.

## 2. Strong energy intertwinement, including domains

Use the unitary Fourier transform with kernel `exp(+iτE)`, so battery energy is `−i∂τ` and `T_u` is multiplication by `exp(iτu)`. The bounded fiber operator

\[
Y(\tau)=e^{-i\tau h_{out}}W e^{i\tau h_{in}}
\]

is an isometry at every `τ`. It defines the energy-line lift without requiring an unjustified absolutely convergent double spectral sum.

A group proof establishes strong energy intertwinement without differentiating arbitrary vectors. On a joint wavefunction, input total evolution acts as

\[
(e^{-it K_{in}}f)(\tau)=e^{-it h_{in}}f(\tau-t).
\]

The identity

\[
e^{-it h_{out}}Y(\tau-t)=Y(\tau)e^{-it h_{in}}
\]

therefore gives `e^(−itKout) Ytilde = Ytilde e^(−itKin)` for every real `t`. Spectral projectors and generator domains follow from this group intertwining. Adding the same scalar to input/output system energies leaves `Y` unchanged.

The battery interval projections commute with the corresponding total-energy groups. Hence `C_b=P_out Ytilde P_in` strongly intertwines the two capped additive energies. It follows that `C_b†C_b` commutes strongly with input energy and `C_bC_b†` with output energy. Their positive defect roots do too. Functional calculus gives the cross identity
`sqrt(I−C_b†C_b) C_b†=C_b† sqrt(I−C_bC_b†)`.
It proves both-sided unitarity of the displayed Julia block and its strong commutation with direct-sum total energy. Different input/output code dimensions cause no obstruction. The ready/refusal and accepted codes must be realized as orthogonal reducing codes with zero-energy labels, as supplied in the report; identity extension on their reducing complement is legitimate.

## 3. Rotor commutator constants and exact input class

The landed pair source supplies `H4=−2Σ S_ac†S_ac`, `S_ac=F_cF_aP`. Its prebirth formula and the previously checked geometry give

\[
h_{in}=KD-618\delta N+\delta V,
\quad \|V\|\le24N,\quad V\Omega\perp\Omega,
\quad \|V\Omega\|^2=48N.
\]

The last norm follows from `6N` distinct unoriented elementary plaquettes, two distinct nonzero shifts each, coefficient `−2`; the stated large torus avoids aliases. Bounded perturbation makes `h_in` self-adjoint on `Dom D`. Its group preserves this domain and the graph norm of `KD+δV`. For every real `s`,

\[
K\|D\phi_s\|\le\|(KD+\delta V)\phi_s\|+\delta\|V\|
\le\delta\sqrt{48N}+24\delta N.
\]

This is a norm estimate, not the weaker mean-energy estimate.

For an individual destination/sign branch, the exact electric difference multiplier is

\[
f(E)=-\sum_{x\in\{b,d\}}\sum_{c\sim x}E_{cx}^2
 -(1-\sigma)(E_{0b}+E_{0d}).
\]

On physical prebirth fields, `D=ΣE²`. The removed squares sum to at most `D`; for the minus sign,
`2|E_0b+E_0d|≤E_0b²+E_0d²+2≤D+2`.
Thus `|f|≤2D+2`. Distinct destination/sign matter words are orthogonal, so this bound holds for each normalized original resolved or coherent branch. In particular the branch maps `Dom D_pre` into `Dom D_out`; it does not assert domain preservation on arbitrary later charge words, where the masked electric operator can be degenerate.

The sharper full-carrier bound `||F_a||²≤12` is valid. On a sector with `o` occupied neighbouring B vertices, each source word has `6−o` outgoing choices and each target word has at most `o+1` possible inverse choices. This includes both charge signs. Rotor shifts are permutations of field words, so the same row/column Schur bound applies on the full countable physical basis, with Gauss restriction only removing entries:

\[
\|F_a\|^2\le\max_{0\le o\le5}(6-o)(o+1)=12.
\]

The independent exact matter-incidence enumeration reproduced all six degree pairs. Hence `||−2S_ac†S_ac||≤288` on the full P space. On the prebirth sector its actual `35` or `34+U+U†` form gives the sharper bound `72`. The prebirth subspace reduces each such pair term. Using `288` on the output and `72` only on the input is essential; replacing both by the prebirth bound would be invalid.

Only pair terms touching the root or one of its 18 distance-two A neighbours contribute to the first-mark commutator. Independent geometric enumeration gives 264 unordered pairs. The disjoint terms cancel by the source's local-extension argument, not by a projection of the magnetic dynamics. For every normalized mark,

\[
\|(H_{4,out}V_m-V_mH_{4,in})\phi\|\le264(288+72)\|\phi\|=95040\|\phi\|.
\]

Stacking the orthogonal original labels averages their squared norms with weights summing to one. Combining with the electric bound proves exactly

\[
\|(h_{out}W-Wh_{in})\phi_s\|\le
C=\delta(95040+48N+2\sqrt{48N})+2K.
\]

There are `9N` pair terms. On the full physical P space each integer electric summand `E(E±1)` is nonnegative, so

\[
h^+=h+2592\delta NI\ge0.
\]

On the input, `h_in^+Ω=δ(1974NΩ+VΩ)`; the two terms are orthogonal. Group invariance gives

\[
\|h_{in}^+\phi_s\|=J=\delta\sqrt{(1974N)^2+48N}.
\]

Consequently `||h_out^+ Wφ_s||≤C+J=:S`, uniformly for all real `s`, and the same bound holds after each fiber's output evolution. At `L=24,K=δ=1`, I obtain `C=427970` and `J=13644288.012158055`, agreeing with the source arithmetic. These constants are fixed-volume bounds on the stated orbit, not operator norms of the unbounded rotor Hamiltonian or uniform later-event estimates.

## 4. Packet, cap, and retained-output errors

The sine packet vanishes at both endpoints, so its weak derivative has no boundary delta. Its derivative squared norm is exactly `π²/w²`; unitary Plancherel gives the reported Fourier second moment. Differentiating `Y(τ)φ_s` is valid on the domains just established and samples `φ_(s−τ)`, for which the same `C` bound holds. Thus

\[
\|(Y(\tau)-W)\phi_s\|\le C|\tau|,
\qquad e_w\le2\pi C/w.
\]

This controls the full marked output after battery trace and original-label dephasing, uniformly over the orbit and its mixtures. It is not an all-input diamond estimate.

For the uncapped output `χ`, strong intertwinement preserves total-energy spectral support. With positive `h^+`, the input battery lies in `[E0,E0+w]`, so:

1. The output total energy is at least `E0`. On `E_B<0` this forces `h_out^+>E0`, hence probability at most `S²/E0²`.
2. On `E_B>Ecap=E0+w+A`, positive output system energy forces total energy above `Ecap`. Its input spectral probability is bounded by the probability `h_in^+>A`, at most `J²/A²`.

These are inclusions of commuting spectral projections, not inequalities about means. The actual Julia refusal probability equals `||(I−P_out)χ||²`, so the two disjoint boundary events give

\[
p\le S^2/E0^2+J^2/A^2.
\]

Projecting an output vector and retaining the full refusal mass gives the accepted error `e_a≤e_w+2√p` and full marked-output error `e_a+p`, exactly as stated. A bound above one may of course be clipped, but is still a valid loose probability upper bound. No postselection renormalization is used.

Both the accepted subnormalized state and target normalized state have second system-energy moment at most `S²`; output battery projection commutes with the system energy. Splitting system energy at `M` bounds their mean difference by
`M e_a+2S²/M`, whose optimum is `2√2 S√e_a`.
This moment argument is necessary; trace closeness alone would not suffice.

For refusal, `R=sqrt(I−C_b†C_b)` strongly commutes with the positive capped input total energy `Kcal=h_in^++E_B`. It preserves its domain. Positivity gives `h_in^+≤Kcal`, but no commutation of `R` with `h_in^+` is needed:

\[
\begin{aligned}
\langle R\psi,h_{in}^+R\psi\rangle
&\le\langle R\psi,\mathcal K R\psi\rangle\\
&=E0p+\langle R^2\psi,(\mathcal K-E0)\psi\rangle\\
&\le E0p+(J+w)\sqrt p.
\end{aligned}
\]

Here `||R²ψ||≤√p` and `||(Kcal−E0)ψ||≤J+w`. Adding this retained refusal energy proves the complete bound (13). The common scalar shift cancels because both complete output states have trace one. Strong conservation of `Kcal` also gives the exact battery/system mean ledger on these finite-moment inputs. The stated family `w=λS, E0=A=λ³S` makes both the marked error and mean-energy error tend to zero; the constants and powers in its displayed bound are correct.

## 5. Non-recurrence one-shot sign and free-reference limitation

Let `t*>0`, `g=π/(2t*)`, `V*=exp(+iKcal t*)U_b`, and form the self-adjoint off-diagonal `Q` in the source. Strong commutation of `U_b` with `Kcal` gives `Q²=I` and strong commutation of `Q` with `Kcal`. Thus `Kcal+g(I+Q)` is self-adjoint on `Dom Kcal` and positive. Its evolution on a ready clock is

\[
e^{-it_*[\mathcal K+g(I+Q)]}|0\rangle\psi
=-\,|1\rangle e^{-it_*\mathcal K}V_*\psi
=-\,|1\rangle U_b\psi.
\]

The **positive** program phase is correct. The author fixture uses a recurrence time where `exp(−iKcal t*)=I`, so that fixture alone cannot test this sign. My independent fixture uses `t*=π/3`, `g=3/2`; it verifies the exact arrival and detects the opposite sign as incorrect.

If the battery freely evolves during an unknown wait `s`, its Fourier weight is shifted to `|βhat(τ−s)|²`. In the sharp-reference limit the fixed lift on `φ_s` therefore produces
`Y(s)φ_s=exp(−is h_out)WΩ`, whereas the intended original first-event output is `W exp(−is h_in)Ω`. These generally differ. This is precisely the controlled/free-dwell distinction in the landed shared-battery source. The orbit-uniform single-operation estimate does not provide a freely rephased battery, Poisson waiting time, later-event correlations, irreversible flags or a spatially local supplier. The source correctly leaves those gaps open.

## 6. Independent exact controls and coverage

The new fixture has `h_in=diag(0,2)`, `h_out=diag(0,4)`, a Hadamard `W`, and battery levels `0,…,4`. It is different from the author's one-input `0→(0,1)` fixture. Its 20-dimensional Julia unitary is checked in both orders and commutes exactly with its additive energy. For a coherent input and sine-profile packet on levels `1,2,3`, the exact uncapped losses are `5/16` below zero and `1/16` above the cap; the retained refusal is `3/8`. Initial system/battery means are `(1,2)` and complete final means `(9/8,15/8)`. Both sums are exactly three. Refusal system energy is `3/8`, below the independently evaluated refusal bound.

The 40-dimensional two-state-clock control verifies the involution, energy commutation and arrival at `π/3`; the wrong free-phase sign is an explicit failing alternative. A coherent two-level calculation also confirms that freely evolving the reference changes the desired output density matrix. These finite controls check algebra and signs; the preceding proof, not a rotor cutoff, establishes the unbounded-input and continuous-cap assertions.

Actual reproduction:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-supplier-check/check.py
```

The run completed successfully with `TOTAL: PASS=7 FAIL=0`; exact values are in `results.json` and `run.log`. The declared deadline and stop sentinel were checked before work. No heavy simulation, network mutation, earlier-report edit, or audit operation occurred.

The finite-energy-supply, autonomous-clock, shared-battery, local-quench and actual-cube-coherence sources were read where relevant to identify their actual premise and scope boundaries. Their general prior machinery was not claimed as new. Their finite-dimensional or CAR locality estimates were not imported as unbounded-rotor or spatial-locality results. This check supports reuse only of the precise stationary class and supplied one-shot first-event approximation established above.
