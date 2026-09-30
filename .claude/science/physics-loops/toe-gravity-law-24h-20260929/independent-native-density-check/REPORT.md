# Independent check of the uniform native pair pulse

No blocking mathematical error was found in the frozen trial-state argument.
The exact finite-volume state gives the stated volume-uniform upper bound on
ground energy and lower bound on ground density. **Coercivity is not assumed
or established in this check**; its consequences below remain conditional.
This is a focused check, not a formal audit/PASS, a phase classification, or
a derivation of physical qubits, Hamiltonian time, preparation, or readout from
the framework axioms.

The checked `native-density-trial/REPORT.md` has SHA256
`ce0f3e87eb6893dcbaae772377869a9ff1804c3c67c5cec8887c2f7636e35d5e`.
Its complete report and bindings were read, together with the full
`native-stability-route/REPORT.md` and the selective independent stability
report. Their advertised source hashes match the actual bytes. The original
native definitions and Gram check were already independently reconstructed
in this campaign; the load-bearing pair calculation is repeated below from
the actual hard-core operators. No author code was imported.

## The actual state and its two-particle zero energy

On each stated torus `L>=5`, use the physical-site qubit annihilator `b_x`
with different-site factors commuting. Set

`d_i(x)=b_(x+ei)b_(x-ei)`,
`Q_1(x)=(d_1(x)-d_2(x))/sqrt(2)`.

Every opposite pair has a unique center and axis at these side lengths:
interchanging its endpoints would require `4e_i=0` on the torus, impossible
for `L>=5`, and different axes cannot produce the same displacement. An
opposite pair also cannot equal an orthogonal-axis pair. Consequently

`<Omega,Q_1(x) Q_1(y)^dagger Omega>=delta_xy`.

Writing `Phi=sum_x Q_1(x)^dagger Omega`, this gives `||Phi||^2=V` and
`N Phi=2 Phi`. The literal five-channel contractions are

`Q_A(y) Phi = delta_(A,E1) Omega`,

independent of `y`. The second E channel cancels by its two equal opposite-
pair coefficients, and every T channel annihilates these opposite-pair
states. Thus the closing Hamiltonian acts as

`H Phi=(2mu-2mu)Phi=0`.

Every triple occupation projector is zero on the whole two-particle sector,
so `V3 Phi=0`. More importantly for the mobile model,
`[Q_A(y+ei)-Q_A(y)]Phi=0` for every `y,i,A`, before applying the adjoint.
Therefore the full `W_tau` annihilates `Phi` and

`H0 Omega=0`, `H0 Phi=0`, `H0=H+V3+W_tau`.

This does not claim that the mobile Hamiltonian annihilates an isolated
compact E pair. In the author's first paragraph, “zero vector” should be
read as **zero-energy vector**: `Phi` is nonzero and has norm squared `V`.

The positivity needed later is independently recovered from the stated
operator completion, not from two-particle data. With the eighteen-neighbor
pair graph and `m_x=sum_(d in D)n_(x+d)`, expanding the E projection and the
four-word T differences gives

`H=A_SOS+mu sum_x n_x(1-m_x)`.

Axial pairs occur at one shell center and orthogonal pairs at two; this is
why the diagonal pair-graph term in `A_SOS` has coefficient `2mu` per edge.
Adding the actual `153` centered triple terms gives

`H+V3=A_SOS+(mu/2)sum_x n_x(m_x-1)(m_x-2)>=0`.

The diagonal polynomial is nonnegative on the integer spectrum `0,...,18`;
this is an operator statement on the full carrier. Since `W_tau` is a sum
of positive gradient squares, `H0>=0`. This does not imply any positive
density coercivity estimate.

## Local norms and support count

The Hermitian generator

`K=sum_x K_x`, `K_x=i(Q_1(x)^dagger-Q_1(x))`

acts on four distinct physical sites. Its two disjoint opposite-pair pieces
commute. Each unscaled piece `i(d_i^dagger-d_i)` has spectrum `-1,0,0,1`;
hence `||K_x||=sqrt(2)`, and the author's looser bound `||K_x||<3` is safe.
The exact local matrix check obtains the characteristic polynomial of
`sqrt(2)K_x` as `z^6(z^2-1)^4(z^2-4)`. No bosonic substitution is involved.

Each physical site belongs to exactly four translated K supports, at centers
shifted by `+/-e1,+/-e2`. Also
`K Omega=i Phi`, so `||K Omega||^2=V`. The normalized exact trial is
`psi(t)=exp(-itK)Omega`; its normalization is automatic at every finite
volume and every real time.

The author groups `H0=sum_x h_x` using the onsite term, all five attractions
centered at `x`, the `153=binom(18,2)` triple terms, and the fifteen gradient
squares based at `x`. Every shifted pair endpoint in the latter is either
`x`, `x+2ei`, or `x+ei+/-ej`. Thus the complete support lies within

`{x} union {x+/-ei} union (x+D)`, of size `1+6+18=25`.

The uniform bounds `||Q_A||<=2` follow directly from the absolute sums of
their pair-word coefficients: `sqrt(2)`, `4/sqrt(6)`, and `2` for E1, E2,
and each T respectively. Therefore

* onsite plus attraction: `mu+2mu*(2*4)+mu*(3*4)=29mu`;
* triples: at most `153mu`;
* fifteen gradients: `15tau*(2+2)^2=240tau`.

It follows that `||h_x||<=182mu+240tau=h_*`. The terms `h_x` need not be
positive, and no such assertion is used.

For a summand of support size at most `s`, at most `4s` K terms overlap it.
Each commutator has norm at most `6` times the previous norm, and its support
adds at most three sites because an overlapping four-site support adds at
most three new sites. Expanding the nested commutator into sequences of
local terms and applying this count at each step gives

`||ad_K^r O|| <=24^r product_(j=0,...,r-1)(s+3j)||O||`.

This is an upper bound on the sum of connected sequences, including repeated
terms. It is not an assertion that the support of the entire commutator
stays small. Coincidences and periodic identifications only reduce the
number of possible local terms and sites. Applying the triangle inequality
after this bound to each `h_x` or `n_x` yields exactly

`C_H=244784332800*(182mu+240tau)`,
`C_N=92897280`,
`A=C_H/24=10199347200*(182mu+240tau)`,
`B=C_N/24=3870720`.

The constants are extremely loose but have no hidden volume dependence.

## Exact Taylor derivatives and global remainder

For any operator O in this finite Hilbert space,

`d^r/dt^r <O>_t = i^r <psi(t),ad_K^r(O)psi(t)>`.

Unitarity bounds its absolute value by the same time-independent nested-
commutator norm. Since `H0` kills both `Omega` and `K Omega`, the first four
Taylor coefficients through order three of its expectation vanish. To see
the third derivative directly, every term has a matrix element
`<K^a Omega,H0 K^b Omega>` with `a+b=3`; at least one of `a,b` is at most
one, and that side is annihilated. The same observation covers lower orders.
Integral Taylor remainder then gives

`0<=<H0>_t/V<=A t^4`.

For number, its value and first derivative at zero vanish and

`(<N>_t)''_(t=0)=2<K Omega,N K Omega>=4V`.

The exact number phase `R=exp(i pi N/2)` changes the sign of every quadratic
pair raising/lowering term in K, fixes the vacuum, and commutes with N.
Hence `<N>_t=<N>_(-t)`, so the third derivative vanishes too. The same fourth-
derivative remainder gives

`|<N>_t/V-2t^2|<=B t^4`.

These bounds hold for the full unitary trajectory. In particular there is
no condition `V t^2 << 1`, no discarded norm normalization, and no assumed
commutation of overlapping pair creators. The fourth-order norm bound was
established on the full carrier before taking this expectation.

## Variational conclusion and conditional coercivity consequence

For `H_nu=H0-nu N`, `nu>0`, write `y=t^2`. The exact inequalities imply

`<H_nu>_t/V <= (A+nu B)y^2-2nu y`
`= (A+nu B)(y-nu/(A+nu B))^2-nu^2/(A+nu B)`.

Choosing the actual finite pulse with `t^2=nu/(A+nu B)` gives

`E0(H_nu)/V <= -nu^2/(A+nu B)`.

For every ground-state density matrix, positivity of H0 separately implies
`E0>=-nu<N>`. Thus

`rho_ground=<N>/V >=nu/(A+nu B)>0`.

This lower bound is compatible with the hard-core ceiling one since it is
less than `1/B`. The exact two-particle zero vector also gives `E0<=-2nu`
on each finite torus; the two upper bounds can simply be combined by taking
their minimum. Nothing assumes that the trial is a number eigenstate or an
actual ground state. Its own density is order nu for small nu, but this
does not establish an upper bound of order nu on the ground density.

**Conditionally only**, suppose a separate proof supplies a volume-independent
`c>0` with `H0>=c N(N-2)/V`. Then for any ground state, Jensen's inequality
gives

`E0/V >=c rho^2-(nu+2c/V)rho`.

Together with `E0<=0`, this implies
`rho<=min(1,nu/c+2/V)`. Completing this last quadratic gives
`E0/V>=-(nu+2c/V)^2/(4c)`.

For thermodynamic accumulation points and `0<nu<=nu_*`, the resulting
conditional bounds can be stated with constants independent of nu:

`nu/(A+nu_* B)<=rho<=nu/c`,
`-nu^2/(4c)<=e<=-nu^2/(A+nu_* B)`.

This is the claimed linear-density/quadratic-energy onset control only if
the separate coercivity hypothesis is valid. Without it, the checked pulse
gives the one-sided energy and density statements above. Neither version
identifies condensation, an order parameter, a differentiable equation of
state, a Goldstone spectrum, tensor polarizations, or a record instrument.

## Actual controls and limits

One independent exact job was priced below ten seconds and 150 MB. With
BLAS/OMP capped at one thread, it completed in **0.913 seconds**, peak RSS
**64,438,272 bytes**. It checks the sixteen-state local generator, its first
three number derivatives, literal uniform-pair contractions and zero
Hamiltonian residuals on `L=5,6,7`, every gradient annihilator on those
tori, the support/incidence counts, and the exact variational square.
Only local matrices and sparse two-particle words are instantiated, not a
large full-carrier state or dense many-body spectrum. The actual K terms
touching the 25-site grouped support number `55,57,59` in those three
tori, all below the proof's bound `100`.

The all-volume result rests on the incidence and operator proof above; it is
not inferred by extrapolating these finite checks. No coercivity proof or
coercivity code was read as evidence for this report. Deadline and absent
stop sentinel were checked before computation. Only this new check
directory was written. Exact source bindings, the independent script,
results, and their manifest accompany this report. Apart from reading
“zero vector” as “zero-energy vector,” no correction to the trial bounds is
needed.
