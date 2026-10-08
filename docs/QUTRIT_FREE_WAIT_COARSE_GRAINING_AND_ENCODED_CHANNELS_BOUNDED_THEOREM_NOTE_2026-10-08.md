---
claim_id: qutrit_free_wait_coarse_graining_and_encoded_channels_bounded_theorem_note_2026-10-08
claim_type: bounded_theorem
claim_scope: "For the supplied qutrit GKLS model with three separate downward jumps, arbitrary nonnegative rates and a diagonal Hamiltonian, an explicit CPTP coarse graining intertwines free evolution with a qubit amplitude-damping semigroup, including its Hamiltonian phase. At the exact matching scope, the accepted OpenAI family-276 theorem gives this encoded free-wait channel's unassisted classical capacity. An exact midpoint-swap witness, two complete encoded Echo formulas, a rational mismatch and a positive exceptional GAD branch delimit that identification. These are conditional channel theorems, not a native dynamical derivation, empirical Echo prediction, full qutrit capacity formula, or exclusion of all encodings."
upstream_dependencies: []
runner: scripts/qutrit_free_wait_coarse_graining_and_encoded_channels_2026_10_08.py
---

# Qutrit free waiting, coarse graining, and encoded channels

**Type:** bounded_theorem. **Status:** conditional-support; unaudited.

The explicit map that merges level 1 into level 0 while retaining the 0–2
coherence converts the entire supplied free qutrit evolution into an exact
qubit amplitude-damping channel. This statement holds for every input matrix,
not just populations. It gives a communication-capacity consequence after the
channel is matched to the accepted formalized theorem below. It does not give
an Echo population or voltage prediction.

The midpoint 1–2 swap cannot act on this quotient alone. Computing the whole
encoded Echo sequences separately yields two different qubit channels. One
is a classical Z-channel; the other has an exact GAD matching criterion and
does match GAD on the positive branch `a=c=0`. A rational example outside that
branch preserves an explicit mismatch. No statement here exhausts other
encodings, pulse models, or readouts.

## 1. Model, quantifiers, and premise boundary

Let `Eij=|i><j|` be the nine matrix units of `M3(C)`, with levels ordered
`0,1,2`. Let `Fij` denote the four matrix units of a qubit ordered `g,e`.
For all finite real rates `a,b,c>=0`, real energies `h0,h1,h2`, and `t>=0`,
set

\[
 H=\operatorname{diag}(h_0,h_1,h_2),\qquad r=b+c,
 \qquad \mathcal D[J](\rho)=J\rho J^\dagger-
 \tfrac12(J^\dagger J\rho+\rho J^\dagger J),
\]
\[
 \mathcal L_3(\rho)=-i[H,\rho]+a\mathcal D[E_{01}](\rho)
     +b\mathcal D[E_{12}](\rho)+c\mathcal D[E_{02}](\rho),
 \qquad \mathcal E_t=e^{t\mathcal L_3}.                 \tag{1}
\]

The energies are in the frequency convention of (1), with the factor of
`hbar` absorbed. The three jumps are **separate** rank-one operators. A
coherent sum of jumps defines a different quantum generator even when its
population equations coincide; Section 7 supplies an exact witness.

| Item | Role in this theorem |
| --- | --- |
| `M3(C)`, the basis, three separate jumps, constant rates, diagonal `H` | Supplied mathematical model; no framework derivation claimed |
| Nonnegative rates and nonnegative waiting times | Hypotheses ensuring the explicit channels below are CPTP |
| Instantaneous `S12`, equal half waits, and the stated input/output maps | Additional hypotheses only for the Echo constructions |
| Independent repetitions of the same channel with arbitrary encoding and collective decoding | Communication task required for the capacity statement |
| Matrix algebra, finite-dimensional linear ODE uniqueness, Kraus positivity | Mathematical tools; not new physical premises |
| `OAI.GAD.main` at the pinned OpenAI source revision | Accepted external mathematical import at the scope in Section 4 |

The [preparation-transfer note](QUTRIT_PREPARATION_TRANSFER_OPEN_GATE_NOTE_2026-09-27.md)
supplies the original model context. None of its fitted rates, observations,
target curves, residuals, or empirical conclusions is a premise of the proof
or an input to the runner. The framework's minimal axioms and registered
primitives do not supply (1), its clock, state preparation, or measurement
instrument here. No premise is adopted and no native-theory obligation is
retired. The empty graph dependency list means that this mathematical
construction is self-contained apart from the explicit external capacity
import; it does not claim unconditional physical applicability.

## 2. The full free propagator and its CPTP certificate

For a duration `s>=0`, write

\[
 A_s=e^{-as},\qquad B_s=e^{-rs},\qquad
 D_s=b\int_0^s e^{-a(s-u)}e^{-ru}\,du
 =\begin{cases}
 b(A_s-B_s)/(r-a),&r\ne a,\\
 bs e^{-as},&r=a.
 \end{cases}                                         \tag{2}
\]

The integral definition covers zero rates and the coincident-rate branch.
It gives `D_s>=0`. Also `A_s,B_s` lie in `(0,1]` for finite `s`, and

\[
 (1-B_s-D_s)'=cB_s+aD_s\ge0,\qquad
 1-B_0-D_0=0.
\]

Consequently `0<=D_s<=1-B_s`. Solving the triangular diagonal equations and
the six scalar off-diagonal equations gives, for every complex matrix `rho`,

\[
\begin{aligned}
 (\mathcal E_s\rho)_{00}&=\rho_{00}+(1-A_s)\rho_{11}
                                 +(1-B_s-D_s)\rho_{22},\\
 (\mathcal E_s\rho)_{11}&=A_s\rho_{11}+D_s\rho_{22},\\
 (\mathcal E_s\rho)_{22}&=B_s\rho_{22},\\
 (\mathcal E_s\rho)_{ij}&=e^{-i(h_i-h_j)s}
                  e^{-(d_i+d_j)s/2}\rho_{ij}\quad(i\ne j),
 \qquad(d_0,d_1,d_2)=(0,a,r).
\end{aligned}                                        \tag{3}
\]

For completeness, a Kraus representation of (3) is

\[
\begin{aligned}
 M_0&=\operatorname{diag}(e^{-ih_0s},\sqrt{A_s}e^{-ih_1s},
                                          \sqrt{B_s}e^{-ih_2s}),\\
 M_{10}&=\sqrt{1-A_s}\,E_{01},\qquad
 M_{21}=\sqrt{D_s}\,E_{12},\qquad
 M_{20}=\sqrt{1-B_s-D_s}\,E_{02}.
\end{aligned}                                        \tag{4}
\]

The preceding inequalities make all square roots real and nonnegative.
Direct multiplication yields `sum Mj† Mj=I3` and exactly (3). Thus complete
positivity and trace preservation follow without deleting a level or
postselecting: at every ancillary dimension the channel is a sum of maps
`(Mj tensor I) R (Mj† tensor I)` on positive matrices. Equations (3) satisfy
`d E_s/ds=L3 E_s` and `E_0=id` on all nine matrix units, so finite-dimensional
ODE uniqueness identifies them with the exponential in (1).

## 3. Exact coarse graining and free-wait intertwining

Define the qubit-valued channel

\[
 K_0=|g\rangle\langle0|+|e\rangle\langle2|,\qquad
 K_1=|g\rangle\langle1|,\qquad
 \mathcal C_{02}(\rho)=\sum_{j=0}^1K_j\rho K_j^\dagger
 =\begin{pmatrix}\rho_{00}+\rho_{11}&\rho_{02}\\
                         \rho_{20}&\rho_{22}\end{pmatrix}.       \tag{5}
\]

`K0†K0+K1†K1=E00+E22+E11=I3`. The same ancillary Kraus argument proves CPTP.
Let

\[
 H_2=\operatorname{diag}(h_0,h_2),\qquad
 \mathcal L_2(\sigma)=-i[H_2,\sigma]+r\mathcal D[F_{01}](\sigma),
 \qquad \ell_{ij}=-i(h_i-h_j)-\tfrac12(d_i+d_j).
\]

Here is the complete matrix-unit calculation. The last column is also
`L2(C02(Eij))` in each row.

| Input | `L3(input)` | `C02(input)` | `C02(L3(input))` |
| --- | --- | --- | --- |
| `E00` | `0` | `F00` | `0` |
| `E01` | `ell01 E01` | `0` | `0` |
| `E02` | `ell02 E02` | `F01` | `ell02 F01` |
| `E10` | `ell10 E10` | `0` | `0` |
| `E11` | `a(E00-E11)` | `F00` | `0` |
| `E12` | `ell12 E12` | `0` | `0` |
| `E20` | `ell20 E20` | `F10` | `ell20 F10` |
| `E21` | `ell21 E21` | `0` | `0` |
| `E22` | `c E00+b E11-r E22` | `F11` | `r(F00-F11)` |

The units span `M3(C)`, proving the linear-map identity

\[
 \mathcal C_{02}\mathcal L_3=\mathcal L_2\mathcal C_{02}.        \tag{6}
\]

Induction gives `C02 L3^n=L2^n C02`. The matrix exponential series converge
absolutely in finite dimension, so for every `t>=0`

\[
 \mathcal C_{02}\mathcal E_t=e^{t\mathcal L_2}\mathcal C_{02}.
                                                               \tag{7}
\]

This proof includes the Hamiltonian part: only the retained 0–2 coherence
sees a phase, with exactly the splitting `h0-h2`. No equality involving `h1`
is required. The qutrit isometric encoder

\[
 J_{02}=|0\rangle\langle g|+|2\rangle\langle e|,\qquad
 \mathcal J_{02}(\sigma)=J_{02}\sigma J_{02}^\dagger
\]

satisfies `C02 J02=id` at the channel level. Therefore the complete encoded
free-wait channel is

\[
 \Phi_t=\mathcal C_{02}\mathcal E_t\mathcal J_{02}
       =\operatorname{Ad}_{W_t}\circ\mathcal A_{1-\eta,0},
 \quad W_t=e^{-itH_2},\quad\eta=e^{-rt},                       \tag{8}
\]
\[
 \Phi_t\begin{pmatrix}1-p&z\\\overline z&p\end{pmatrix}
 =\begin{pmatrix}1-\eta p&\sqrt\eta e^{-i(h_0-h_2)t}z\\
      \sqrt\eta e^{i(h_0-h_2)t}\overline z&\eta p\end{pmatrix}.
                                                               \tag{9}
\]

The subspace `span{0,2}` need not be invariant: its leakage `b` into level 1
is included by (5). If `r=0`, nonnegativity forces `b=c=0`, and (8) is a
unitary channel even when `a>0`. At `t=0` it is the identity. The branch
`r=a`, including all rates zero, uses the second line of (2) and has no
singular division. These facts hold independently of any measured rate.

## 4. Capacity at the exact accepted formalized scope

The external import is `OAI.GAD.main` in
[the production `Main.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/InformationTheory/AmplitudeDamping/Main.lean).
Its [model definitions](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/InformationTheory/AmplitudeDamping/Model.lean)
use four Kraus operators with `gamma,nu` in `[0,1]`. The proved
[`local_channel` identity](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/InformationTheory/AmplitudeDamping/Channel.lean)
has population `p -> (1-gamma)p+gamma nu` and coherence multiplier
`sqrt(1-gamma)`. Thus `nu=0`, `gamma=1-eta` matches (8) after its explicit
output unitary.

The [family-276 scope statement](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/276.md)
and production theorem cover unrestricted tensor-power Holevo additivity,
an attained scalar optimum, its equality to operational unassisted classical
capacity, and attainment of the block Holevo value by optimal phase-pair
product ensembles. The channel is memoryless; decoding may be collective.
The import does not cover additivity with an arbitrary different partner or
a requirement of separate output measurements. This packet uses precisely
that formalized scope, as an accepted external theorem under the owner's
2026-10-08 instruction. It does not claim a local Lean rebuild or an independent
verification of the entire external proof.

Let `h2(x)=-x log2 x-(1-x)log2(1-x)`, with `0 log 0=0`. Then (8) has

\[
 \boxed{\quad C(\Phi_t)=
 \max_{0\le p\le1}\left[
 h_2(\eta p)-h_2\!\left(\frac{1+\sqrt{1-4\eta(1-\eta)p^2}}2\right)
 \right].\quad}                                               \tag{10}
\]

The units are bits per use of the **supplied channel**. For any maximizing
`p`, the equiprobable signals
`sqrt(1-p)|g> +/- sqrt(p)|e>` and their independent products attain the
corresponding block Holevo value; reliable codes at rates below (10) may
use collective decoding. The scalar determinant under the square root is
`eta(1-eta)p^2`: direct calculation on the two pure inputs gives it, and
their average output is `diag(1-eta p,eta p)`. The external theorem supplies
optimality over arbitrary ensembles and entangled block inputs, not merely
the value of this pair. At `eta=1` the capacity is one bit/use; at the
amplitude-damping endpoint `eta=0` it is zero. The latter is also the free
channel limit when `r>0` and `t` tends to infinity.

For clarity, a fixed output unitary preserves all decoding probabilities:
replace each output POVM effect `M` by `W_t M W_t†`, at every tensor power.
It also preserves output entropies. Thus the phase in (9) changes neither
the Holevo quantities nor operational capacity used by the import.

Equation (10) is an achievable subchannel rate for `E_t` if the stated
encoding and output processing are available. Any qubit block code can be
encoded by `J02` on each use and its POVM pulled back through the unital
positive adjoint of `C02` on each output. Hence the unconstrained qutrit
capacity is at least (10); no equality with that larger optimization is
claimed. Likewise the invariant `span{0,1}` channel gives an amplitude-damping
subchannel at rate `a`. Physical access to these encoders, collective
measurements, a stationary channel and repeated independent uses is not
established by the preparation-transfer experiment. This result is not an
Echo prediction, an empirical rate fit, or a repair of its recorded mismatch.

## 5. An exact midpoint information-loss witness

Let `S12` fix `|0>` and interchange `|1>,|2>`, and write
`S(rho)=S12 rho S12†`. The states `E00,E11` satisfy

\[
 \mathcal C_{02}(E_{00})=\mathcal C_{02}(E_{11})=F_{00},
 \quad
 \mathcal C_{02}\mathcal S(E_{00})=F_{00},\qquad
 \mathcal C_{02}\mathcal S(E_{11})=F_{11}.                       \tag{11}
\]

Their output difference is `diag(1,-1)`. Equal quotient inputs would have to
give equal outputs under any single-valued quotient map. Consequently no
qubit channel `Q` can satisfy `C02 S=Q C02` on all qutrit states. This is a
statement about this specific quotient and this pulse. It does not rule out
an end-to-end channel identification after a chosen input encoding; that
requires computing the whole composition, as follows.

## 6. Two complete encoded Echo channels

Fix `tau>=0`, total wait `2 tau`, and define

\[
 \mathcal T_\tau=\mathcal E_\tau\mathcal S\mathcal E_\tau,
 \qquad A=A_\tau,\ B=B_\tau,\ D=D_\tau.                         \tag{12}
\]

The durations are equal and the pulse is exactly the instantaneous
permutation stated above. There is no final pulse beyond the expressly
defined output operations. `tau=0` still includes that midpoint pulse.

**Encoding 02 and output C02.** For every input state with excited population
`p` and coherence `z`,

\[
 (\mathcal C_{02}\mathcal T_\tau\mathcal J_{02})
 \begin{pmatrix}1-p&z\\\overline z&p\end{pmatrix}
  =\begin{pmatrix}1-BDp&0\\0&BDp\end{pmatrix}.                \tag{13}
\]

To derive it, after the first wait the level-1 population is `Dp`. The swap
puts it in level 2; the second wait retains a fraction `B`. The original
0–2 coherence becomes a 0–1 coherence after the swap, survives in that
matrix unit during the second diagonal-H wait, and is killed by `C02`.
This proves (13), including complex input coherences. It is the classical
Z-channel with transmission `BD`. For finite `tau>0` and `b>0`, the integral
in (2) and `B>0` imply `BD>0`; it is not GAD in the displayed convention,
because a GAD channel's population slope equals its coherence multiplier
squared. If `b=0` or `tau=0`, `D=0` and this map is instead the constant-ground
GAD endpoint. The statement does not exclude other qubit interfaces.

**Encoding 12, output C12 followed by X.** Define

\[
\begin{aligned}
 J_{12}&=|1\rangle\langle g|+|2\rangle\langle e|,\\
 L_0&=|g\rangle\langle1|+|e\rangle\langle2|,\qquad
 L_1=|g\rangle\langle0|,\\
 \mathcal C_{12}(\rho)&=\sum_{j=0}^1L_j\rho L_j^\dagger
   =\begin{pmatrix}\rho_{00}+\rho_{11}&\rho_{12}\\
                         \rho_{21}&\rho_{22}\end{pmatrix},
 \qquad X=F_{01}+F_{10}.
\end{aligned}
\]

`J12†J12=I2` and `sum Lj†Lj=I3`; these are legitimate CPTP input/output
operations. The complete channel
`Psi_tau=Ad_X C12 T_tau J12` is

\[
 \Psi_\tau\begin{pmatrix}1-p&z\\\overline z&p\end{pmatrix}
 =\begin{pmatrix}1-q&ABz\\AB\overline z&q\end{pmatrix},
 \qquad q=1-AB+B(A-D)p.                                      \tag{14}
\]

Indeed the first-wait populations are `A(1-p)+Dp` in level 1 and `Bp` in
level 2. After swapping and waiting, level 2 has
`AB(1-p)+BDp`. The output `X` complements this probability. For coherences,
`E12` is multiplied in the first wait by
`exp(-(a+r)tau/2-i(h1-h2)tau)`, is swapped to `E21`, and acquires the opposite
Hamiltonian phase in the second wait. Their product is `AB`; the final `X`
restores the orientation of the input coherence. Thus (14) is valid for
arbitrary diagonal `H`, and has no hidden zero-H assumption.

Put `k=AB` and `s=B(A-D)`. For this specified channel and output convention,
GAD equality holds **if and only if**

\[
                       s=k^2.                               \tag{15}
\]

Necessity follows from `s=1-gamma` and `k=sqrt(1-gamma)`. Conversely, if
`k<1` and (15) holds, choose `gamma=1-k^2` and `nu=1/(1+k)`. These lie in
`[0,1]`, give `gamma nu=1-k`, and reproduce every entry of (14). If `k=1`,
the nonnegative-rate model implies `D=0`, and (14) is the identity GAD
channel with `gamma=0` and any `nu`. An arbitrary unitary redefinition of the
input/output interface is not being classified here.

A useful **positive branch** is `a=c=0`: then `A=1`, `D=1-B` (including
`b=0`), and (15) holds. The second encoded Echo channel is exactly
`GAD(1-B^2,1/(1+B))`. The same accepted theorem applies to this specially
supplied channel if the same communication hypotheses hold. This exception
prevents interpreting a failure at another rate triple as a universal Echo
or encoding exclusion.

A small exact control uses dimensionless supplied rates `a=b=c=1` and
`tau=log(2)`. Equation (2) gives

\[
 A=\tfrac12,\quad B=\tfrac14,\quad D=\tfrac14,\qquad
 BD=\tfrac1{16},\quad
 q=\tfrac78+\tfrac1{16}p,\quad z\mapsto\tfrac18z,
 \quad k^2-s=-\tfrac3{64}.                                  \tag{16}
\]

Thus this second channel does not satisfy (15), while the first channel
has a nonzero Z-channel transmission. The runner also composes exact finite
Kraus matrices at this point, checks all four input units, and checks the
15 principal minors of each qubit Choi matrix. Those controls establish
that the mismatch is between well-defined CPTP channels, rather than a
trace-losing truncation. They are author-side algebraic checks, not a claim
of independent review.

Other edges are explicit. At zero wait, (13) is constant ground and (14)
is identity. The same holds at arbitrary equal waits if all rates vanish:
the diagonal phases cancel in (14). For the nonzero coincident-rate example
`a=b=1,c=0,tau=1`, (2) gives `A=B=D=e^-1`, so (14) has zero population slope
and nonzero coherence `e^-2`, failing (15). This uses the continuous branch
without dividing by `r-a`. No rounded calibration rate is used in these
examples.

## 7. Related exact scope checks

On populations the generator is

\[
 L_{\rm pop}=\begin{pmatrix}0&a&c\\0&-a&b\\0&0&-r\end{pmatrix}.
\]

A deterministic two-cell partition descends to a two-state Markov generator
exactly when states merged into the same cell have the same total outgoing
rate into the other cell. This is necessary by applying the purported
quotient to the merged basis vectors; it is sufficient by the resulting
column identities. The three possibilities are exhaustive:

| Merged levels | Retained singleton | Necessary and sufficient condition |
| --- | --- | --- |
| `0,1` | `2` | Always; decay rate `b+c` |
| `1,2` | `0` | `a=c`; decay from the merged cell to 0 is then `a` |
| `0,2` | `1` | `b=0`; decay from 1 to the merged cell is then `a` |

This population classification does not by itself identify the quantum
coherences of a channel. Likewise, restricting the full evolution to a
coordinate two-dimensional subspace is trace preserving for every state in
that subspace precisely as follows: `span{0,1}` always; `span{0,2}` iff `b=0`;
`span{1,2}` iff `a=c=0`. Necessity follows from the outside-level population
derivatives `(0,0)`, `(0,b)`, and `(a,c)` respectively, on the two basis
states; sufficiency follows because `H` and all nonzero jumps then preserve
the indicated subspace. In particular, omitting level 0 from a general
1–2 experiment is not a trace-preserving channel construction.

The bosonic control from the earlier kinetic review also remains exact.
Vacuum oscillator loss has the coherent ladder jump, on levels 0–2,

\[
 L_{\rm ladder}=E_{01}+\sqrt2 E_{12}.
\]

Its population equations match the separate jumps only when `b=2a,c=0`.
Even then, for `a>0` the quantum generators differ:

\[
 a\big(\mathcal D[L_{\rm ladder}]-\mathcal D[E_{01}]
                  -2\mathcal D[E_{12}]\big)(E_{12})
          =a\sqrt2 E_{01}\ne0.                              \tag{17}
\]

The anticommutator parts agree; the ladder's coherent gain term supplies
the displayed difference. The trivial `a=0` case has no difference. This is
a witness against that particular bosonic identification, not against all
bosonic encodings. For a separate valid bosonic example, vacuum pure loss
of transmissivity `1/2` restricted to these three levels has Kraus operators

\[
 N_0=\operatorname{diag}(1,1/\sqrt2,1/2),\qquad
 N_1=(E_{01}+E_{12})/\sqrt2,\qquad N_2=E_{02}/2.
\]

They sum to a trace-preserving channel and send `I3/3` to
`diag(7/12,1/3,1/12)`. This preserves the earlier exact binomial-thinning
example without importing an entropy-photon-number theorem into a channel
that does not match its hypotheses. No bosonic entropy inequality is a
dependency of (6), (10), or the Echo formulas.

## 8. Source identities and accepted-import disposition

The source base is framework commit
`ed04ee2736b5bddb4e9064966505e3c3dfe003de`; the new files are a provisional
addition, with no inherited audit verdict. The source preparation note at
that commit has SHA-256
`2f1bb5863eb7067f1aef0dea424a37f10eded3b5f2a6d34985784a194fe7a388`.
The earlier analysis is preserved in the external research packet
`openai_math_20261007/execution/kinetic`: `RESULTS.txt` Sections 3–4,
`exact_checks.py` function `channels`, and `echo_composite_check.py`. Their
SHA-256 values respectively are
`5aa044e3457684c5a6f94fdc1f8795082053cdb29f77b400329ccdc01b63617c`,
`4e2bee32e3301ac5edfc4a37780d3037df4f7c57ee139af2466a7ae9555e9cac`, and
`a8983f4bb2fece54c666ccd8f1b8200b9160f6bcc313ed960b7bc3ab06afe357`.
These are provenance, not runtime inputs. The new runner reproduces the
algebra with its own complete definitions and exact rates.

All external theorem links are pinned to OpenAI math commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The actual accepted declaration is
`OAI.GAD.main`, mapped by
[`AmplitudeDamping.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/AmplitudeDamping.json)
to `OAI.InformationTheory.AmplitudeDamping.Main`, and listed in
[`formalization.yaml`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/formalization.yaml).
The comparator's `sorry` is a challenge placeholder, not the production
proof used for this import. The production `Main.lean` supplies a proof of
the conjunction described in Section 4. The comparator configuration permits
only `propext`, `Quot.sound`, and `Classical.choice`; this packet records that
declared contract and does not claim to have rerun the comparator.

| Exact external file | SHA-256 of inspected bytes |
| --- | --- |
| `lean/docs/276.md` | `34d51d11d25cf4d1108b3914cfcb7d13a9df63a0cb3dd82071406f07c0640a99` |
| `lean/OAI/InformationTheory/AmplitudeDamping/Model.lean` | `709ab56f351cb6ebee2497f58ecfb722c4828d60cf3d6cd68f9358d8d7551f08` |
| `lean/OAI/InformationTheory/AmplitudeDamping/Channel.lean` | `e172ad790e4e02bf10e028b59e87d3339e148be0d208e7638cf9eb391f7cc35d` |
| `lean/OAI/InformationTheory/AmplitudeDamping/Main.lean` | `24aeebc34cbc3932d57e82236613dd086c1233a27c461717a5337facc7a31d87` |
| `lean/ComparatorChallenges/AmplitudeDamping.json` | `d5fd3b206d67df3786b22e25c25e9a7364ea70ee02a6d2d8b478b76e9ef7d70b` |

The matching definitions and theorem statements, including operational
capacity and collective POVMs, were read. The external proof's transitive
Lean dependencies were not re-verified for this packet, in accordance with
the accepted-import instruction. Its paper's stronger arbitrary-partner
extension is not imported. None of our newly proved qutrit matrix identities
is covered by the external formalization merely because its conclusion is
used afterwards.

## 9. Reproduction and later formalization targets

The standalone
[runner](../scripts/qutrit_free_wait_coarse_graining_and_encoded_channels_2026_10_08.py)
uses Python and SymPy, with `AUDIT_TIMEOUT_SEC=120` and no external or mutable
repository inputs. Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/qutrit_free_wait_coarse_graining_and_encoded_channels_2026_10_08.py
```

The complete execution output is stored through `scripts/runner_cache.py` in
[the canonical cache](../logs/runner-cache/qutrit_free_wait_coarse_graining_and_encoded_channels_2026_10_08.txt),
bound to the runner's content hash. It includes every matrix-unit result,
both ODE branches, continuous-limit check, channel composition controls,
exact rational mismatch, positive exceptional branch, bosonic witness and
`TOTAL: PASS=145 FAIL=0`. The runner does not numerically optimize capacity,
prove the external capacity theorem, test hardware adequacy, or certify an
independent review. All computations are small exact matrices; no dataset
or empirical holdout is opened.

Later Lean audit work has concrete targets, rather than an unspecified
request to formalize the physics:

1. Define `M3(C) -> M2(C)` rectangular Kraus maps `C02,C12` and isometries
   `J02,J12`; prove completeness and ancillary positivity for these matrices.
2. Define (1), expand all nine units, prove (6) as equality of complex-linear
   maps, and prove (7) by the matrix exponential series. Track `H2` and the
   0–2 phase explicitly.
3. Formalize (2) using the integral first, its two closed-form branches,
   `D>=0`, `B+D<=1`, and the Kraus/ODE certificate (3)–(4), including zero rates.
4. Identify (8) with the actual `OAI.GAD.channel` at `nu=0` through its basis
   equivalence; prove capacity and Holevo invariance under the output unitary,
   then instantiate the accepted `OAI.GAD.main` without strengthening it.
5. Formalize (11) as a failure of factorization through this specific `C02`;
   prove the two full channel formulas on four units, including phase
   cancellation, the exact criterion (15), the positive branch and rational
   counterexample. Preserve both sides of that classification.
6. Formalize the three population quotients, coordinate leakage conditions,
   and the separate-jump/ladder witness if those subsidiary statements are
   retained in the audited unit.

The new proof remains a conditional mathematical source with exact checks.
Selective independent source review is recorded in the branch packet.
The Lean targets above and any formal retained-status audit remain later work;
no new Lean proof, adopted physical premise, or empirical validation is claimed.
