# Independent direct-field implementation check, original source

Review date: 2026-10-12. This is the assigned focused scientific implementation
check, not a formal audit, new research campaign, or landing review of the
whole branch. The parent chat authored the solver. This reviewer read its full
285-line original source, the complete derivation note and frozen contract,
and the upstream `galaxy_forward.py` source needed to establish the mass/data
roles. Writes are confined to the assigned independent review directories.

## Source and scope

- Preserved base: `6caad9d83931922a6d086f45b0a7465f5c5f3af6`.
- Original solver SHA-256:
  `0d02f2a476d6f1edf71ae53fa84132b355ea9853703748ae98ecac76a9b0b096`.
- Derivation SHA-256:
  `ad7e69fefbdf57dd6f0e961ff9e54ed96a2e4cf0000f983dbb0c16cb3e075c46`.
- Contract SHA-256:
  `f6225b00b62a82b050586535a933f82d8320783d7934d35ef0ce9e8f31d49b93`.

Full source snapshots are in this directory. The receipt
`source_snapshot.json` in the corresponding runtime review directory records
identities. Applicable guidance was read from local `origin/main`
`516cb69d8487ff04f8a48e065d3dcbe71d7dd237` and `origin/ai/execution`
`3a4b2c66a1ead7a1c48b4359627e968f681e3c39`. No fetch was performed under the
read-only dispatch. The science workflow, review-loop focused lenses, axiom
memo and primitive registry were consulted. No supplied lattice premise is
being used to derive QUMOND here.

## Independent reconstruction of the load-bearing projection

Let A be the outward potential-gradient input, with A_r=a_l P_l and
A_theta=b_l partial_theta P_l for one even mode. Orthogonality on the full
sphere gives the author's upper-hemisphere factors `(2l+1)` and
`(2l+1)/(l(l+1))`. The angular Laplacian eigenvalue is `-l(l+1)`, hence

    H_l = a_l' + 2 a_l/r - l(l+1) b_l/r.

The radial Green solution follows from the homogeneous solutions r^l and
r^(-l-1), whose weighted Wronskian is `-(2l+1)`:

    phi_l = -[r^(-l-1) I_l + r^l J_l]/(2l+1),
    I_l = integral_0^r t^(l+2) H_l(t) dt,
    J_l = integral_r^infinity t^(1-l) H_l(t) dt.

Differentiation cancels the local H terms and independently gives

    phi_l' = [(l+1) r^(-l-2) I_l - l r^(l-1) J_l]/(2l+1).

Integration by parts instead gives
`I_l=r^(l+2)a_l-l integral_0^r t^(l+1)[a_l+(l+1)b_l]dt` and
`J_l=-r^(1-l)a_l+(l+1) integral_r^infinity t^(-l)[a_l-l b_l]dt`.
Substitution yields exactly the implemented subtraction
`a_l-l(l+1)(S_l+T_l)/(2l+1)`. The code's signs, powers and coefficient
normalizations are correct. The log-radius kernels have rates `l+2` and
`l-1`; the forward and reverse linear-cell weights in the code have the
correct orientation. The small-cell series is the integral of
`y exp(-k y)` through the stated order.

The monopole has `(r^2 phi_0')'=(r^2 a_0)'`; absence of a point source at the
origin sets its integration constant to zero. Thus `phi_0'=a_0`, without a
false zero-potential condition at infinity. Higher-mode boundary terms vanish
for these finite-mass isolated sources. Numerical zero initial/final S/T
values remain a finite-cutoff approximation requiring the declared boundary
check; the continuum derivation does not itself certify those cutoffs.

At the sheet A_R is even and A_z odd. In distributional divergence,
`partial_z A_z` contains `2 A_z(R,0+) delta(z)`. The angular integration by
parts over the full sphere already contains this jump; projecting the two
one-sided vector traces does not omit it. A_theta can have a finite jump at
the equator even though each finite even-l basis derivative vanishes exactly
there. This explains slow pointwise series convergence and makes the
resolution gate consequential. Using the exact local radial trace is
consistent with the continuum projection; it does not prove that the
remaining mode sum has converged.

## Newtonian source, units and data roles

Azimuthally averaging a displaced normalized planar Gaussian gives
`Sigma=M exp(-(R-A)^2/(2 sigma^2)) i0e(RA/sigma^2)/(2 pi sigma^2)`.
Its Fourier-Bessel transform is the stated Gaussian factor times `J0(kA)`.
The potential kernel is `-G M integral dk J0(kR)J0(kA)exp(-sigma^2 k^2/2)Z`;
differentiation gives the code's positive `k J1` radial and `k J0 V` vertical
forces. The gas-sheet jump is `2 pi G Sigma`; the finite stellar vertical
trace vanishes. The removable kh=1 limits and relation
`-partial_z Z=k V` are correct.

With M in solar masses and R in kpc, G produces `(km/s)^2/kpc`. One such
acceleration unit is `3.240779289444365e-14 m/s^2`, so the frozen a0 is
`2363.029994974699` in field units. Circular velocity would require `v^2=R g_R`;
the present solver returns force and does not perform a velocity fit.

The source equation, nu function, isolated axisymmetry/reflection symmetry,
gas sheet, finite stellar height, G, reconstructed masses and previously
fitted global U/a0 are disclosed inputs. The upstream fixed height law and
component mass normalizations are inherited modeling inputs, not independent
predictions. The four contract-pinned files still match their SHA-256 values.
Independent recomputation reproduces every eligible galaxy's bin and complete
ranking. The new solver never loads the sealed velocity target file. Reading
the NPZ key inventory finds no target `*_v` or `*_error` arrays in that source
archive. None of these checks certify the astrophysical adequacy of the source
reconstruction or a fit of QUMOND to observations.

## Independent controls and findings

The standalone `independent_fixture.py` imports no author code. It computes
H analytically for `a=alpha r^(l-1)e^-r`, `b=beta r^(l-1)e^-r`, then performs
adaptive quadrature of I/J in the differentiated Green formula above. A
separate probe executes the author as the subject against that saved fixture.
No expected value is generated with the author's angular projection, S/T
formula, recurrence, or helpers.

The independent radial-only l=2, transverse-only l=2 and mixed l=4 controls
give max error normalized by max absolute expected force as follows:

| Control (l, alpha, beta) | nr=384 | nr=768 | nr=1536 |
| --- | ---: | ---: | ---: |
| (2,1,0) | 2.1244e-4 | 5.4925e-5 | 1.3673e-5 |
| (2,0,1) | 1.7402e-4 | 4.3402e-5 | 1.0938e-5 |
| (4,1,-0.2) | 9.3306e-4 | 2.3275e-4 | 5.8067e-5 |

An independent vertical-source convolution agrees to `1.1103e-16` absolute.
The full probe, including original controls and the mutation below, ran in
0.816 s at approximately 104 MB maximum RSS and one configured numerical
thread. Original controls were reproduced successfully.

1. **Missing decisive control, confirmed.** Original solver lines 167 and
   175-231: replacing `full = local_norm - correction_modes.sum(axis=1)` by
   `full = local_norm.copy()` still passes every original control. Spherical,
   Kuzmin, manufactured-gradient and real-source nu=1 controls all have zero
   true correction. The independent non-gradient controls reject this mutant
   with normalized errors `2.4374`, `1.0000` and `3.0703`. The original code
   itself passes the new controls; the defect is in the original validation
   coverage. Reported to the author for a source-side non-gradient assertion.

2. **Numerical acceptance pending, confirmed.** The first coarse/fine QUMOND
   runs change by `1.39257%` (NGC2976), `1.48805%` (UGC07577), and `0.390847%`
   (KK98-251). The first two exceed the frozen `0.5%` resolution gate. Fine
   nu=1 errors are respectively `2.2430e-5`, `4.7008e-4`, `3.5698e-5`, all
   within its separate `0.003` gate. Fine direct midplane errors are below
   `8e-15`. These checks do not license a one-percent force budget, source
   subset expansion, or observational residual inspection yet. The author
   is diagnosing the mode tail. This is an unresolved numerical gate, not a
   counterexample to the continuum field equation.

3. **Zero-radial-force edge case.** Line 166 evaluates `nu(abs(mr)/a0)` eagerly
   inside `np.where`; `mr==0` raises even if the full vector has nonzero sheet
   normal component. This contradicts preserving a valid full-vector
   calculation through a nonpositive radial comparator. It does not affect
   the recorded three-galaxy outputs. The author has acknowledged a narrow
   masked-evaluation fix; affected confirmation is pending.

The runtime receipts `independent_fixture_v1.json`, `author_probe_v1.json`,
and `source_and_gates_v1.json` retain values, exact input identities, and the
mutation. The executed commands were the two Python scripts in this directory
in sequence; logs are in the runtime review directory. No fitting, target
selection by model agreement, formal audit, pipeline, commit, push, or external
publication was performed. Combined integration checks belong to an eventual
landing and are outside this focused dispatch.

Disposition: the continuum derivation and original implementation agree, and
the new independent numerical controls support the nonzero projection. Final
source confirmation remains open for the author's fixes and numerical gates.
