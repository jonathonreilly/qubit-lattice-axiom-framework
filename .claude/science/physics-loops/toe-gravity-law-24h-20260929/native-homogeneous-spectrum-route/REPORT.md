# Homogeneous canonical spectrum of the actual supplied native pair law

**Type:** bounded_theorem author candidate.
**Status:** conditional-support, pending focused independent proof check.
No formal review, audit, retained status, main edit or PR is claimed.

For the unchanged full-site M2 Hamiltonian, this packet gives two actual
homogeneous spectral restrictions and a direct variational control. It does
not establish a finite-density phase or local density spectral weight.

1. On even cubic tori, every odd-N eigenvalue is at least eightfold degenerate.
   The exact operators are U_i=exp(i pi sum_x x_i n_x), with
   [U_i,H0]=0 and T_i U_j T_i*=(-1)^(N delta_ij)U_j. Eight distinct translation
   triples prove orthogonality. See `EXACT_PARITIES.md`.
2. For any sufficiently large cubic L and N/L noninteger, the actual canonical
   ground is degenerate OR its same-N gap obeys Delta_N<=C_h logL/L. The proof
   constructs charge-preserving, spatially separated Gaussian-filter twists
   on the full tensor carrier and uses the gap only on neutral vectors from
   that canonical ground. There is no full-ground or chemical-potential
   support-line premise. See `SECTOR_FLUX.md`.
3. An elementary affine twist gives an actual normalized, same-N trial of
   energy excess at most162(3mu+24tau)(2pi)^2 N/L^2, with momentum shifted by
   +/-2piN/L. For a unique canonical ground and noninteger N/L it is orthogonal.
   At fixed positive density this bound grows like L; the two-cut proof is
   what avoids that three-dimensional cost. See `DIRECT_TWIST.md`.

The second result is a justified application/adaptation of known LSM machinery,
not claimed as a novel general LSM theorem. The first is an exact projective
symmetry argument for these literal pair rows. The useful change from the
survey-only starting point is a proof for the actual fixed-N sector, which
cannot be obtained by simply declaring it a bounded local tensor product.
Neither result silently turns the checked nearby-field response into a
homogeneous density-response theorem. No standalone milestone PR is proposed.

## Exact law, carrier and order

At every site b_x=|0><1| and n_x=b_x* b_x on C2. Different sites commute.
Use all original axial and signed plane pair words

 d_i(x)=b_(x+e_i)b_(x-e_i),
 v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j),
 QE1=(d1-d2)/sqrt2, QE2=(d1+d2-2d3)/sqrt6,
 QTij=(1/2)sum_(s,t) v_ij^(s,t).

With m_x=sum_(d in{+/-2e_i,+/-e_i+/-e_j}) n_(x+d), the actual law is

 H0=mu N-2mu sum PE-mu sum PT
       +mu sum_x n_x binom(m_x,2)+tau sum_(x,j,A)|Delta_j QA(x)|^2
   =S+mu Ddiag+W,
 S=(2mu/3)sum_x|d1+d2+d3|^2
      +(mu/4)sum_(x,i<j,r<s)|v_ij^r-v_ij^s|^2,
 Ddiag=(1/2)sum_x n_x(m_x-1)(m_x-2).

In particular the S term is retained. The route's shorthand description
H0=mu D plus pair gradients is not interpreted as permission to omit S.
The main grouping has radius2, at most25 sites, norm h=182mu+240tau, and
number-neutral terms. The lattice, tensor product, Hamiltonian, basis,
expectation rule, periodic boundary conditions and fixed positive couplings
are supplied model inputs. The exact charge sector is a mathematical choice;
neither a realized-state primitive nor the EOS selects it. No framework
primitive is added or declared inadequate.

The flux statement is uniform over integers N at each finite L; its only
large-volume limit is L->infinity with mu,tau fixed. It requires the actual
finite arithmetic N/L noninteger. A fixed density can admit both commensurate
and noncommensurate volume/number sequences. On even tori, the odd-N case is
already in the exact-degeneracy branch. The new positive-gap restriction is
especially relevant to even N not divisible by L if the sector ground is
unique. No gap above a degenerate groundspace is inferred.

## Main proof discriminator

Let psi be the unique canonical ground, rho=N/V and G=Q_X-rho|X| for a
half-slab X. The global Gaussian generator has Fourier multiplier

                 i(1-exp(-a omega^2))/omega.

Since dH(theta)/dtheta=i[G,H(theta)], its action on the ground differs from
G by exp[-a(H(theta)-E_N)^2]G psi_theta. G psi_theta is neutral and orthogonal
to the ground, so its norm is bounded by V exp(-a Delta_N^2), regardless of
energies in other sectors. This exact vector identity is the decisive sector
step; no projected-space locality theorem is invoked.

Restricting real-time evolution to two separated slabs gives exactly local
commuting twists W1,W2, with explicitly priced norm error. Moving only the
first cut gives TW1T* and the phase exp(2pi i N/L); the centered-charge scalar
at2pi is retained in the proof. The normalized trial W1 psi has energy at
most E_N+2hV eta and shifted translation expectation within2eta, where under
the contradiction hypothesis Delta_N>=16384(1+2e*129h)logL/L,

                  eta<=C'_h L^7[exp(-L/64)+L^-32].

The smallest nontrivial phase separation is>=4/L, and therefore the trial's
weight outside the original unique ground is at least1/L. This suffices for
the contradiction. The polynomial geometry cost is paid explicitly; neither
a fixed O(1) phase separation nor a gap along a one-cut path is assumed.

## Decisive actual negative controls and remaining strength

Continuous dipole-U(1) conservation is false: two disjoint axial pairs at
centers0,e2 have the exact matrix element-2tau/3 and coordinate-sum change2e2.
On odd L the pairs centered at0,e1 similarly have coefficient-2tau/3 but
opposite first-coordinate parity because of wrapping. These are actual rows
of H0; they delimit the discrete symmetry and even-torus hypotheses.

The N=1 sector is exactly H0=mu I. With its FULL ground projection removed,
every positive-frequency density spectral measure is zero. Thus exact
momentum partners alone cannot supply inelastic density weight. This is a
source-valid finite-sector discriminator, not a counterexample to a
positive-density collective phase.

For that stronger target, one sufficient remaining lemma is a homogeneous
lower bound on the density inverse-energy moment m_(-1), or a lower bound on
the full-ground-complement density trial together with its actual f-sum.
This is response-strength information. The flux theorem is weaker and cannot
supply it by relabeling its nonlocal trial. The already checked density-response
packet gives a modulation jump OR soft density spectrum at a nearby regular
field lambda*, not necessarily0. That exact distinction remains.

## Literature and refreshed prior scope

Current remote main was verified at
fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7. `PRIOR_REFRESH.json` binds the open
proposal inventory. The complete landed density-law note was read. The complete
native density-response report and its focused receipt were read, including
the pointwise-response discriminator; the odd-N pairing prior was inspected
at its exact absolute-energy statement. The current PR9413 canonical note was
read completely at d6197654f4100621083f72a421da2b8aff6b7391; its energy proof
closure is not imported into either new spectral proof. Its actual N/L filling
or ground uniqueness cannot be inferred from its dilute energy coefficients.

Main was searched for Lieb-Schultz, Oshikawa, flux insertion, dipole parity
and site-sign/eightfold variants. `MAIN_PRIOR_HITS.txt` captures the focused
keyword search. The complete matched Sep21 site-sign/coin note concerns a
single walker and explicitly distinguishes formal branch orbits from spectral
degeneracy. The clock-gauge twist note's relevant theorem mapping and twist
argument concern quantized two-form sources and local wraps; the PMNS transfer
and signed-gravity boundary notes concern other supplied observables. They
are nonmatching context, not premises or no-go authority. No claim of an
exhaustive worldwide novelty search is made.

Primary literature actually examined:

* Hastings [2021 survey](https://arxiv.org/html/2111.01854v1), sections3.1-3.4
  and the needed locality setup. Theorem3's unique-full-ground statement is
  kept separate from the canonical construction here.
* Hastings [2004 higher-dimensional proof](https://arxiv.org/html/cond-mat/0305505v6),
  the finite-velocity/spectral estimates, twisted boundaries, local density
  comparison and translation proof in sectionsIII-VI. It is the older spin
  formulation and is not silently used as a general-charge theorem.
* Hastings [2005 U(1) construction](https://arxiv.org/html/cond-mat/0411094v2),
  complete mathematical argument from system definitions through translated
  cuts and discussion. Its declared extension is to “systems at general
  filling fraction”; the local factors and centered-charge phase motivated
  the construction here. The Gaussian vector proof explicitly supplies the
  fixed-sector adaptation.
* [Dipole-conserving LSM paper](https://arxiv.org/html/2001.04477v1), sectionII.1
  and its stated conservation and periodic-boundary hypotheses. It requires
  continuous linear-phase conservation, refuted for this H0 by the actual
  row above. Its broader paper was not used as an authority for this model.

The literature is a mathematical construction/context input, not a fitted
value, physical law selector or native-record interpretation. The actual
algebra and bounds needed by the new conclusions are displayed in the proofs.

## Actual evidence, failures and handoff

One priced sparse exact control ran under5CPU/30wall/100MiB, BLAS/OpenMP1.
It returned exit0 and TOTAL PASS=10 FAIL=0:0.792173 childCPU seconds,
0.798316wall seconds,17,629,184B peak RSS. It checked918 original rows at27
seam representatives for each of L6,8, two full-center offdiagonal coefficient
sums, translation signs,25/129 geometry, the affine displacement bound and
literal singleton annihilation. RSS was measured at return, not claimed as
an unsupported OS hard-address-space limit. No Hilbert enumeration, eigenvalue
fit, large-torus simulation or numerical proof of the Gaussian bound occurred.

`CONTROL_EXPECTATIONS.md` and `CONTROL_FREEZE.json` precede execution.
`ROWS.stdout`, `ROWS.stderr`, `ROWS_RESULTS.json` and `CONTROL_EXECUTION.json`
are the actual captures. There were no scientific-control failures. Retrieval
failures (missing optional HTML parser, Python certificate error, guessed
HTML version404) are recorded in `RETRIEVAL_FAILURE.txt`; standard-library
processing/native curl and the primary web reader resolved them.

Selected methodology7146fe17 is kept consistent with the campaign. Existing
unchanged premise/procedure reads are reused where identified; no formal
conformance, N-gate, source review or integration PASS is asserted for this
research packet. Root has an independent precomparison derivation before
opening these proofs. The next action is that focused check. No substantial
downstream use of this new packet should precede it. All older route packets
remain immutable; only this directory was written.
