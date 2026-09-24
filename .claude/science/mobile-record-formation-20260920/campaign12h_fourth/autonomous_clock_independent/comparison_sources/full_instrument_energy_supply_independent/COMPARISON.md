# Comparison of the released finite-supply construction

Completed source comparison, 2026-09-24. The independent PRE was sealed at
`8b2c02e41a68f0ad9d085e3056031383d92f553cb3b0745bd13654b415a0805d`
before the target author proof, code and results were released. All 22 PRE
bindings remain byte-for-byte unchanged. This is a scientific comparison,
not an audit verdict or a publication/landing decision.

## 1. Source identity and disposition

The complete released note is
`../full_instrument_energy_supply_author/FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS.md`,
SHA256 `6b9c4ae27ee49754e905f0d990b766be94f2c9ee8a624da01208a6da14b20288`.
Its author seal is
`469d1f35340e2615d7c7e9d4bbad4a18a111fc04bdb49105fb9120cdb0c7ee83`.
All thirteen author artifacts and six bound scientific dependencies were
authenticated. The complete proof, both complete control scripts, planning
and development records, execution receipt, and full numerical results were
read. The two run logs duplicate their corresponding JSON result bytes; their
stderr files are empty. The pinned microscopic builder was read for source
comparison but was never imported into an independent calculation.

**No mathematical correction to the frozen author note is required at its
stated scope.** The generic construction, its reference-uniform bound and
correlated same-reservoir composition agree with the independently sealed
PRE. The author's looser collision error bound is valid. The exact
stationary-input joint energy/flag probability statement is also supported,
with its energy-stationarity qualification essential. The electric-family
application is conditional on the explicitly attributed, separately checked
microscopic robustness premise and is correctly limited to the finite star.

| Claim in released note | Disposition | Basis |
|---|---|---|
| Exact finite unitary, positive reservoir, arbitrary finite spectrum | Supported | Same independently derived complete vector-charge sectors; no commensurability premise |
| Diamond error <= min(2,8 sin(pi/[2(L+1)])) | Supported | Independent isometry argument in PRE; matching constants |
| Same reservoir, complete finite flag history, no reset | Supported | Exact blockwise product identity; reservoir correlations retained |
| CP collision with the original jumps | Supported | Exact Kraus completeness and independent generator expansion |
| One-step error tau^2(7g^2+4hg), tau g<=1/2 | Supported, conservative | Direct check below; independent PRE has a stronger separate bound |
| Exact stationary-input final energy/flag probabilities | Supported | New general argument, exact rational control, complete-star histories |
| Uniform leading energy limit over the electric family | Supported conditionally | Explicitly bound independent uniform Duhamel premise plus moment error |
| Autonomous reservoir, physical selection, exact continuous event times | Not claimed | The note keeps these obligations separate |

## 2. Generic lift and the sequence statement

The author's finite cube, complete label blocks, identity on incomplete
blocks and product sine preparation coincide mathematically with section 4
of this task's PRE. The auxiliary charges are Q_a=N_a+P_a. Conserving them
conserves H+H_R even when physical energy eigenspaces contain additional
degeneracies. The reference can have arbitrary dimension; the operator-norm
bound on the controlled-translation isometry supplies the diamond bound.
The preparation is buffered at both finite boundaries, so there is no cyclic
wrap or use of a nonunitary truncation as a physical unitary.

For the sequence, all finite zero-energy flags belong to one enlarged system
space from the start. Every lift uses the same complete sectors and same
identity boundary rule. Thus the product identity is exact, not a replacement
of the actual correlated reservoir by its initial state. The author's rule
that later gates do not act on earlier readout flags permits deferred
measurement. The theorem bounds a finite complete discrete history; its
reservoir error does not grow with the number of gates on the same bounded
energetic system. The memory and scheduling resources still grow. It is not
a uniform finite-resource theorem for indefinitely many fresh energetic
systems, nor an exact catalyst-return assertion.

The independent PRE also has an optional single integer-ladder construction.
The released note does not need it: one ladder per distinct positive gap is
sufficient for noncommensurate spectra. The finite-spectrum application is
per specified Hamiltonian; the resource Hamiltonian and designed couplings
can depend on lambda. Neither packet supplies a single physically selected
reservoir law common to all lambda.

## 3. Collision estimate and attribution of stronger statements

Let X=tau Gamma and S=sqrt(I-X), with 0<=X<=I/2. The author's remainder
R=S-I+X/2 satisfies ||R||<=tau^2 g^2/2. Because S and I-X/2 are contractions,
replacing one by the other in its sandwich costs at most 2||R||. The remaining
quadratic sandwich term has norm at most tau^2 g^2/4. This proves the claimed
5tau^2g^2/4 distance from I+tau D. With ||D||_diamond<=2g, the author's
exponential Taylor bound is at most 2tau^2g^2 exp(2tau g). For tau g<=1/2,

    5/4 + 2 exp(1) < 7.

Its product-formula contribution is at most 4hg tau^2 because the surrounding
semigroups are channels and ||[A,D]||_diamond<=8hg. Thus equations (10)-(11)
of the released note follow. They are conservative, not erroneous. The
unnormalized Choi trace norm in the source control is an upper bound on the
diamond norm, while the normalized Choi tests in PRE are particular entangled
inputs. Neither finite numerical sample is the proof of the general bound.

The independently obtained exact identity

    Psi_tau-(I+tau D)=D[I-sqrt(I-tau Gamma)]

and the sharper one-step estimate 4g(h+g)tau^2 for tau g<=1 belong to this
task's sealed PRE. They are not retroactively attributed to the root note.
Likewise the PRE precision sequence eta=C^-6, N=O(C^9), with vanishing
absolute first and second energy-moment errors, is an additional independently
derived sufficient sequence. The root's weaker precision is enough for its
different stated conclusion: the leading mean divided by C. There is no
conflict between those scopes.

## 4. Exact stationary-input energy/flag probabilities

Here is a density-operator derivation of the new load-bearing statement.
Let the input on system plus initialized zero-energy flags be stationary:

    rho=sum_a rho_a,       rho_a=P_a rho P_a.

Write beta for the normalized buffered reservoir vector and
T_(a-b)=T^(v_a-v_b). On the accessible complete sectors the lifted output is

    sum_(a,b,c) [P_b U rho_a U^dagger P_c]
          tensor T_(a-b)|beta><beta|T_(a-c)^dagger.

Every translated vector has norm one because the finite buffer contains its
support. Fix a final energy block b and a flag outcome represented by an
effect F_f on the zero-energy flags. P_b and F_f commute. In the expectation
of P_b F_f, only the b=c terms survive, and their reservoir traces equal one.
The result is exactly

    tr[P_b F_f U rho U^dagger].

This proves all joint energy/flag probabilities. It also proves equality of
the energy-dephased joint system/flag density. Replacing U by the complete
product U_n...U_1 proves the whole discrete-history statement with the same
reservoir. An intermediate reduced input need not be stationary: stationarity
is required of the initial input to the full product, and the proof keeps the
reservoir correlations. The original lambda=0 dressed star input is exactly
in its zero-energy block, as required.

The scope is precise. It does not assert exact coherences between distinct
final system energies. For an entangled external reference, energy/flag
probabilities depend only on the stationary system marginal and are still
exact. A stronger claim about the joint conditional reference state would
require the *joint input* to be block diagonal in system energy, not merely
its system marginal. The released note claims probabilities and moments,
not that stronger reference-state equality.

The new exact rational control in `comparison_control.py` uses a four-state
system with a two-dimensional ground eigenspace and positive levels 1 and
sqrt(2), two fresh flags, and the same finite two-ladder reservoir for both
gates. It checks input coherence within the degenerate ground block, both
positive-energy inputs, and a stationary mixture with weights 1/2,1/3,1/6.
All joint final energy/two-flag probabilities agree exactly as rational
numbers. Cross-energy output coherences differ, providing a sensitivity check
against turning the probability statement into exact channel equality. The
profile for this exact control is a normalized rational buffered product;
the probability argument requires only normalization and support, not the
particular sine shape.

There is an explicit counterexample to dropping stationarity. On levels
0,1 take psi=(3/5,4/5) and

    U=[[3/5,4/5],[-4/5,3/5]],      U psi=|0>.

For a normalized buffered battery with nearest-shift overlap t, the finite
lift's final ground probability is

    337/625 + (288/625)t.

For the author's sine profile at L=2, t=1/2 and this is 481/625, whereas the
ideal probability is 1. The exact rational control uses buffered amplitudes
(3/5,4/5), whose t=12/25, and obtains 11881/15625 exactly. Thus arbitrary
coherent-input energy probabilities are approximate, not exact. This is an
essential hypothesis check, not a counterexample to the released theorem.

## 5. The electric-family extension and moment limits

The released dependencies were read in full:

- `microscopic_electric_robustness_author/STAR_ENERGY_COST_ACROSS_THE_ELECTRIC_FAMILY.md`,
  SHA256 `a7dfe854f72be6e30b7aa4bbb61e10c5e7876b6cd62698735968af33ae0477c2`;
- `microscopic_electric_robustness_independent/PRE_RECONSTRUCTION.md`,
  SHA256 `145bc27edb4a791a89b5d624943ef99102692783b0de5e8cfc7615e0c19c0f40`;
- that independent PRE seal,
  `92f534204e822fbbc38f4cfbd8a5f6d1d33f09b727d7bead68fd22dfb4734faa`.

All 22 bindings of the electric independent PRE were authenticated. Its
uniform-in-lambda Duhamel argument is used as an explicit separately checked
premise, not silently attributed to this task. The bound |w|>=Omega d is
valid because the real addition ell=lambda K is nonnegative. Its resulting
A_epsilon=O(epsilon^3), B_epsilon=O(epsilon^2) are uniform on lambda in [0,1],
and the mismatch estimate controls the large microscopic no-event energy.
This supplies the leading finite-time coefficient used by the author; no
qualitative density theorem is substituted for that moment estimate.

On this complete sixteen-state star, H_lambda=H_0+K lambda E2 and 0<=E2<=3.
At fixed positive delta,K,kappa in the joint scaling, h_lambda=O(C^2) and
g=O(C), uniformly in lambda. Shifting the minimum eigenvalue leaves at most
fifteen distinct positive gaps, each O(C^2). These facts are sufficient for
the generic reservoir theorem. There is no requirement that the perturbed
gaps remain rational or that their multiplicities stay the same.

The author's L=O(C^2), tau=O(C^-5) prescription can make each contribution
to its channel bound at most C^-2/2. Thus h_lambda zeta=O(1), which divided
by C is O(C^-1). It reproduces the leading mean/C coefficient uniformly over
the stipulated electric family. It does **not** claim vanishing absolute
energy error under that particular resource choice. The prepared reservoir
energy O(C^4), the dimension bound (L+2)^15, and O(C^5) blank flags are valid
loose sufficient bounds. The same dressed preparation has initial energy
O(C^-1) but is not an eigenstate for lambda>0; the author correctly uses the
general moment-error estimate there, not the stationary-input exactness.

The conclusion that energy conservation with arbitrarily engineered growing
resources does not by itself select lambda is supported as this conditional
existence statement. It makes no claim about a physically fixed bath, spatial
locality, autonomous clocks, bounded coupling strength, optimal supply, or
selection under additional reservoir laws.

## 6. New calculations and verification limits

The comparison script imports only this task's frozen `control.py`, whose
SHA256 is checked before import. It never imports the root model builder.
Using that own primitive sixteen-state model, it reconstructs all eight
released collision rows, including lambda=1 with the original coherent marks.
The largest difference across exact-channel energy, collision energy,
superoperator Frobenius error and unnormalized Choi trace norm is
4.440892098500626e-14. This agrees within the explicit 2e-10 comparison
threshold; no model normalization or tolerance was changed to obtain it.

The same own model checks two successive steps for both instruments: all 49
resolved or 16 coherent discrete histories are retained. For the stationary
lambda=0 input the largest joint history/energy probability residual is
5.551115123125783e-16; the complete-history total probability differs from
one by less than 2e-15. These numerical controls supplement the exact generic
probability argument and the rational complete-block test. They do not assert
an exact finite-bin continuous-time jump instrument.

The first comparison-control execution passed every assertion. Complete
outputs, source hashes and timing are in `COMPARISON_CONTROL_RESULTS.json`,
`COMPARISON_RUN.stdout.log`, `COMPARISON_RUN.stderr.log`, and
`COMPARISON_RUN_RECEIPT.json`. Existing PRE failures remain preserved; no
PRE or frozen author bytes were edited.

## 7. Private bibliographic binding and final disposition

The versioned Åberg PDF in the sealed private PRE is an external
bibliographic provenance binding, SHA256
`f25314c4d44716b54b2643404f4d646f730400e6ecdb8b4bcf11ac00a2250e2a`.
It is intentionally **not a public artifact and must not be staged or
published**. The private original and PRE seal remain unchanged. The public
packet can retain the bibliographic URL and hash without requiring that PDF
to be present. No copied third-party PDF or text extract has been added to
this comparison. `PRESERVATION_AND_PUBLICATION_RECEIPT.json` explicitly
separates that external binding from the 21 other PRE artifacts.

Required scientific corrections: none. Preserve the stated limitations and
the attribution of the stronger independent CP/moment results. The delivered
unit is a conditional finite supplied-resource construction and its independent
comparison. Autonomy, exact event-time laws, physical preparation/selection,
and optimized or bounded-resource implementation remain outside the result.
