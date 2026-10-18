# Independent referee record for OBS-3

## VERDICT: CONFIRMED WITH CORRECTIONS

The fixed `TEXTURE-ESCAPE` reading is met in the worker's declared one-loop carrier family.  The decisive object is not the rounded `complex128` matrix stored in `univ_B_gen.npz`, but the exact equal-modulus ansatz defined by the parameters and formula in `scripts/univ.py:78-85`: it has one exactly common complex diagonal entry and six exactly equal off-diagonal moduli, reproduces the chosen PDG-2024 mass ratios and CKM data far inside their experimental errors, and gives an exactly S3-invariant one-loop data set.  Cubic covariance then puts each quark corner/axis tensor in the two-dimensional invariant space

\[
T(c,a)=\alpha+\beta\delta_{ca},
\]

which is removed exactly by the already-allowed per-field speed and tetragonal counterterms (`scripts/obs3_core.py:131-143`).  Thus the observed CKM matrix does **not** force the OBS-2 one-loop flavour-pattern Lorentz violation in this family.

The corrections are material.  S2 is phase-blind only for separately propagating, non-mixing off-diagonal carriers; the diagonal Higgs-symbol term contains the full real Gram matrix and can depend on relative diagonal phases.  Equal entry moduli alone are therefore not sufficient for the selective-symbol models.  The saved double-precision B-gen arrays are not below the direct bounds when evaluated as literal matrices.  The M1 construction establishes the OBS-2 example numerically and would cancel all rows if exact, but the report does not prove its “for any \(W_u\)” quantifier.  The flat-flat/circulant theorem and the L-word theorem are correct; the “up-flat + M2: no structural zero” conclusion is not proved.  The all-orders covariance claim is exact at the symmetric point \(v=0\), not at an arbitrary fixed non-invariant vev.

## Scope and independent checks

- I used the fixed reading at `TESTS.md:395-410`, not the later summary language at `TESTS.md:412-423`.
- I checked the assembly formulas against the actual one-loop kernel code (`scripts/yuk_lv_obs2_copy.py:1-18,57-94,179-210`) and the OBS-3 assembly (`scripts/obs3_core.py:82-143,178-246`).
- I independently reconstructed B-gen from both the serialized matrices and the stored parameter vector.  High-precision calculations used `mpmath` at 80-100 decimal digits, converting each saved binary64 component by its exact integer ratio rather than by a shortened decimal string.
- All Python checks were run one at a time through `zsh capped.sh /dev/stdout ...` with `OMP_NUM_THREADS=2`.  Their watchdog peaks were 11.7-73.7 MB RSS, below the 0.3 GB requirement.
- I checked the worker's recalled inputs against the official [PDG 2024 quark summary](https://pdg.lbl.gov/2024/tables/rpp2024-sum-quarks.pdf) and [PDG 2024 CKM review](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-ckm-matrix.pdf).
- I did not modify any worker file and did not create `REFEREE_VERDICT.md`.

## 1. S2 and Lemma S

### 1.1 What the one-loop models actually compute

The underlying one-loop self-energy is quadratic in the vertex (`scripts/yuk_lv_obs2_copy.py:7-12`).  OBS-3 assembles it as

\[
T_H(c,a)=\sum_{s,t}\operatorname{Re}(\eta_s\eta_t^*)I_{st}(c,a),
\]

and, for M2,

\[
T_{\rm fl,L}(c,a)=\sum_{c'\ne c}|Y_{cc'}|^2K(c,c',a),\qquad
T_{\rm fl,R}(c,a)=\sum_{c'\ne c}|Y_{c'c}|^2K(c,c',a).
\]

These are exactly the operations in `scripts/obs3_core.py:83-105,122-129`.  The carrier conclusions are:

- **M1:** by definition the frozen off-diagonal condensates are omitted from this loop, so only the diagonal Higgs-symbol data enter (`PREREG.md:73-78`).
- **M2 with separate covariant \(\tau_x\sigma_c\) carriers:** the external and internal corner fix the carrier momentum, distinct carriers are summed incoherently, and only \(|Y_{cc'}|^2\) enters.  Off-diagonal Yukawa phases therefore drop out in the declared no-carrier-mixing model.
- **On-site covariant M2 carrier:** the numerical identity \(K(c,c',a)=I_{00}(c',a)\) is supported to \(8.3\times10^{-13}\) relative over the sampled grids (`scripts/structure2.py:8-19`; `scripts/structure2.out:1-7`).  The exact change-of-variable/spin-conjugation argument is plausible and gives
  \[
  T_L(c,a)=\kappa_\perp(YY^\dagger)_{cc}+\Delta\kappa |Y_{ca}|^2,
  \]
  with the transposed expression on the right.
- **Selective and range-2 diagonal symbols:** phases do not generally disappear.  The code uses \(\operatorname{Re}(\eta_s\eta_t^*)\), not merely \(|\eta_s|^2\) (`scripts/obs3_core.py:83-93,107-118`).  Thus the relevant object is the full real Gram matrix of the symbol coefficients, not only its diagonal and not only the entrywise moduli of \(Y\).

The last point narrows the statement at `REPORT.md:68-75`.  “The phases of the off-diagonal entries never enter” is correct under the declared carrier assumptions.  “CKM phases never enter” without that qualifier is too broad, because phases can affect the diagonal symbol coefficients or a carrier-mixing quadratic form.  The report itself states “no carrier mixing” at `REPORT.md:68` and should retain that hypothesis prominently.

### 1.2 Independent phase counterexample

I evaluated a toy texture with every one of the nine entry moduli equal to one and diagonal phases \((0,0,\pi/2)\).  It therefore has exactly equal diagonal moduli and exactly equal off-diagonal moduli.  At \(N=48,m_0=m_H=0.1,\Delta=0.5\), the worker's own kernels give

| diagonal-symbol split | M1 max residual | M2 max residual |
|---|---:|---:|
| trace | \(1.1216\times10^{-3}\) | \(1.1216\times10^{-3}\) |
| selective | \(1.7976\times10^{-3}\) | \(1.7976\times10^{-3}\) |

By contrast, common diagonal phase and the \((0,2\pi/3,4\pi/3)\) character pattern reduce the same check to the \(3\)-\(4\times10^{-16}\) integration/symmetrisation floor.  Therefore **equal diagonal and off-diagonal moduli are not, by themselves, a sufficient Lemma-S hypothesis for arbitrary selective diagonal symbols**.  B-gen survives this correction because its three diagonal entries are the same complex number by construction (`scripts/univ.py:78-85`), a condition stronger than equal diagonal moduli.  B-gen120 uses the special cubic-character phase pattern, not arbitrary diagonal phases (`scripts/univ.py:77,84,103-105`).

### 1.3 Lemma S itself

Lemma S is correct when phrased in terms of the **entire one-loop data set** being S3-invariant.  The simultaneous permutation action on the three hw1 corners and the three axes has only two invariant tensors, \(1\) and \(\delta_{ca}\).  Hence covariance gives

\[
T(c,a)=\alpha+\beta\delta_{ca}.
\]

The projection in `scripts/obs3_core.py:132-136` removes exactly those two components.  Subsequent mass-eigenstate projection cannot recreate a residual (`scripts/obs3_core.py:138-143,206-213`).  This is regulator- and placement-independent as an exact symmetry statement, provided the regulator, carrier propagators, and vertices all obey the same cubic action.

The “if and only if \(|Y|^{\circ2}=oJ+(d-o)I\)” sentence at `REPORT.md:92` is valid only in the narrower on-site, phase-blind kernel class for which the displayed \(\kappa_\perp,\Delta\kappa\) formula applies.  It is false if read as a theorem for arbitrary selective-symbol realizations, as the counterexample above shows.

## 2. The B-gen fit and exact-equality crux

### 2.1 PDG inputs

The recalled quark central values in `PREREG.md:82-88` agree with the PDG-2024 summary:

| quantity | worker | PDG 2024 |
|---|---:|---:|
| \(m_u(2\,\mathrm{GeV})\) | 2.16 MeV | \(2.16\pm0.07\) MeV |
| \(m_d(2\,\mathrm{GeV})\) | 4.70 MeV | \(4.70\pm0.07\) MeV |
| \(m_s(2\,\mathrm{GeV})\) | 93.5 MeV | \(93.5\pm0.8\) MeV |
| \(m_c(m_c)\) | 1.2730 GeV | \(1.2730\pm0.0046\) GeV |
| \(m_b(m_b)\) | 4.183 GeV | \(4.183\pm0.007\) GeV |
| direct \(m_t\) | 172.57 GeV | \(172.57\pm0.29\) GeV |

The Wolfenstein inputs \(\lambda=0.22501\), \(A=0.826\), \(\bar\rho=0.1591\), \(\bar\eta=0.3523\), the global-fit moduli, and \(J=(3.12^{+0.13}_{-0.12})\times10^{-5}\) also agree with the PDG-2024 CKM review.  The direct \(|V_{us}|\) recalled as 0.2243 is merely rounded from 0.22431.

One physics caveat is missing from the report: these six masses are not running Yukawa eigenvalues at one common scale.  The light masses are quoted at 2 GeV, \(c,b\) at their own masses, and the top entry is a direct kinematic mass.  This does not invalidate an existence fit at the precision needed here, but it means the displayed texture is not yet a common-scale Standard-Model Yukawa fit.

### 2.2 Independent reconstruction of the fit

The fit is defined at `scripts/univ.py:70-99`: four mass ratios, the nine moduli of the unitary CKM matrix generated from the PDG Wolfenstein parameters, and \(|J|\).  The texture is then saved at `scripts/univ.py:119-130`.  This is a redundant set of CKM observables, so the printed “\(\chi^2\)” is an optimizer residual with diagonal nominal weights, not a statistically meaningful independent-data chi-square.

Reconstructing the texture at 80-digit precision from the saved B-gen parameter vector gives:

| observable | high-precision result relative to target |
|---|---:|
| \(y_u/y_t\) | relative/log difference \(-3.80\times10^{-12}\) |
| \(y_c/y_t\) | \(-1.34\times10^{-15}\) |
| \(y_d/y_b\) | \(+6.97\times10^{-15}\) |
| \(y_s/y_b\) | \(-3.98\times10^{-16}\) |
| largest CKM-modulus pull | \(4.4\times10^{-12}\) |
| \(|J|-J_{\rm PDG}\) | \(-8.27\times10^{-19}\) |

The high-precision weighted residual is \(1.44\times10^{-17}\), rather than the stored binary64 value \(7.31\times10^{-23}\) (`scripts/univ.out:10`).  The difference is numerical conditioning of the tiny first singular value and binary64 optimization.  Both residuals are utterly negligible relative to the experimental uncertainties.  The defensible wording is “reproduces the chosen PDG central inputs to at least \(10^{-11}\) pull,” not a literal mathematical equality to exact empirical real numbers.

### 2.3 Are the modulus equalities imposed or fitted?

They are imposed **exactly by the mathematical parameterization**, not obtained approximately from the optimizer.  In `scripts/univ.py:78-85` every off-diagonal element is \(e^{i\phi_{ij}}\), every ordinary B-gen diagonal element is the same real \(e^r\), and the whole matrix is later multiplied by one sector-wide scale (`scripts/univ.py:121-123`).  Thus:

- the three diagonal moduli are exactly equal;
- the six off-diagonal moduli are exactly equal;
- the diagonal value is free to differ from the off-diagonal value;
- the fit varies phases and the diagonal/off-diagonal ratio without relaxing those equalities.

This confirms the crux behind the quoted 0.3331 versus 0.3334: those are the allowed diagonal and off-diagonal common values, not an inequality among members of either class (`scripts/univ.out:21-36`).

### 2.4 Literal saved matrices versus the exact ansatz

The serialized arrays are `complex128`, so calls to `exp(i*phase)` do not land exactly on the unit circle.  Reading their binary components exactly at 100 digits gives:

| saved matrix | diagonal modulus spread | off-diagonal modulus spread | relative off-diagonal spread |
|---|---:|---:|---:|
| \(Y_u\) | 0 (bitwise equal) | \(5.4932\times10^{-17}\) | \(1.6620\times10^{-16}\) |
| \(Y_d\) | 0 (bitwise equal) | \(1.7527\times10^{-18}\) | \(2.1803\times10^{-16}\) |

I then evaluated the report's exact on-site S2 formula at high precision with the six \(N=96\) \((\kappa_\perp,\kappa_\parallel)\) pairs printed at `scripts/structure2.out:2-7`, using the saved \(W,X,Y\) arrays as literal matrices.  The worst per-field residual is \(5.80\times10^{-19}\).  The first-generation ring coefficients are:

| row from literal saved arrays | largest magnitude | direct bound | ratio |
|---|---:|---:|---:|
| \(\mathring c^u\) (negative sign) | \(1.19\times10^{-19}\) | \(3\times10^{-23}\) | \(3.97\times10^3\) |
| \(|\mathring d^u|\) | \(2.14\times10^{-20}\) | \(3\times10^{-23}\) | \(7.12\times10^2\) |
| \(\mathring c^d\) (negative sign) | \(5.02\times10^{-20}\) | \(10^{-22}\) | \(5.02\times10^2\) |
| \(|\mathring d^d|\) | \(5.04\times10^{-20}\) | \(10^{-22}\) | \(5.04\times10^2\) |

The official rows are at `kr_paper.tex:10426-10439` and `kr_tables_text/kr_v19.txt:26420-26449,26464-26494`.  The worker's own binary64 assembly likewise prints a worst fixed-row ratio \(1.41\times10^4\) for B-gen (`scripts/univ.out:45`) and correctly recognizes this as a roundoff problem (`REPORT.md:50-52`).

Therefore the saved matrices are **not themselves a numerical certificate at \(10^{-22}\)**.  The escape is instead an exact algebraic realization obtained by reconstructing \(Y(p)\) from `p` with unit-modulus exponentials.  That reconstruction has exactly zero modulus spreads for any real parameter values and still matches the PDG data at the precisions above.  The report should preserve this distinction.

### 2.5 Electron row

The statement that “every row is zero” (`REPORT.md:20-24`) is slightly too strong.  The charged-lepton Yukawa contribution is S3-invariant, but the fixed PMNS/neutrino contribution is not.  At \(N=96,m_0=0.025,\Delta=0.5\), I reproduce a maximum M2 electron anisotropic coefficient \(2.06\times10^{-23}\), comfortably below the code's \(2\times10^{-20}\) electron comparator (`scripts/obs3_core.py:173,216-228`).  Thus the electron row is safe, not identically zero.

## 3. M1 diagonal equalisation

### 3.1 What is exact

A right-handed rotation changes \(X_d\), hence the corner-basis placement of entries in

\[
Y_d=W_d\,\mathrm{diag}(y_d,y_s,y_b)X_d^\dagger,
\]

without changing the singular values or \(W_u^\dagger W_d=V_{\rm CKM}\) (`PREREG.md:66-67`).  M1 assigns only the corner-diagonal entries to the loop and treats the off-diagonal entries as frozen condensates (`PREREG.md:73-78`).  Therefore, if an exact right rotation makes all three diagonal entries the same complex number, the M1 data are S3-invariant and Lemma S kills both isotropic and anisotropic residuals.  This includes selective and range-2 symbols when their three coefficients are the same, because they form a cubic scalar sum.

For the OBS-2 embedding \(W_u=F\), the up texture is already circulant.  An exact change of \(X_d\) alone is therefore sufficient to remove the OBS-2 down source in M1 while leaving masses and CKM unchanged.  Conditional on the equalisation, the statement “including the anisotropic rows” is correct.

### 3.2 What is only numerical

The routine at `scripts/univ.py:46-58` is a 20-start nonlinear least-squares search, not a proof.  It is applied to only three choices of \(W_u\) at `scripts/univ.py:59-67`.  The OBS-2 example reaches a relative diagonal spread \(1.5\times10^{-16}\), but the literal saved realization still prints a worst fixed-row ratio 869 (`scripts/univ.out:2-3`).

As an independent stress test, I repeated the same optimization for 160 Haar-random \(W\)'s and mass hierarchies \((\epsilon^2,\epsilon,1)\) with \(\epsilon=10^{-1},10^{-3},10^{-6},10^{-12}\).  Every case reached relative diagonal-equality residual below \(9\times10^{-15}\).  This strongly supports generic existence but does not discharge the universal quantifier.

Finding: **the exhibited OBS-2 rotation is a credible numerical construction and its exact limit zeros every M1 row; the statement that this can be done for every \(W_u\) is not proved by the packet.**  A theorem on one-sided unitary constant-diagonalisation, or a constructive proof specialized to positive nondegenerate singular values in dimension three, is still required for “any \(W_u\).”  This does not affect `TEXTURE-ESCAPE`, which already has the independent B-gen witness.

## 4. The theorem claims

### 4.1 Flat-flat iff circulant-equivalent

Confirmed in dimension three, with “equivalent” understood to allow independent row/column permutations and rephasings as at `REPORT.md:96-100`.

If \(W_u\) and \(W_d\) are flat, \(\sqrt3W_u\) and \(\sqrt3W_d\) are order-three complex Hadamard matrices.  Dephasing makes a nontrivial row \((1,a,b)\); orthogonality requires \(1+a+b=0\), and unit moduli force \(\{a,b\}=\{\omega,\omega^2\}\), exactly the elementary check in `scripts/algebra.py:11-17`.  Hence every order-three complex Hadamard is monomially equivalent to \(F_3\), as catalogued by [Tadej and Życzkowski](https://chaos.if.uj.edu.pl/~karol/pdf/TZ06.pdf).  The product \(W_u^\dagger W_d\) is consequently monomially equivalent to \(F^\dagger D F\), which is circulant.  Conversely, a circulant-equivalent unitary is obtained from two flat Fourier-equivalent matrices.

The Latin-square modulus pattern is a necessary consequence.  The direct PDG-2024 smallest-row entries \(0.00382(20)\) and \(0.0411(12)\) differ by 30.6 nominal standard deviations (`scripts/algebra.py:18-28`; `scripts/algebra.out:6-13`).  Correlations are not included in that simple pull, but the discrepancy is far too large to affect the qualitative exclusion.

### 4.2 “Up flat + M2: no structural zero”

Not confirmed as a theorem.  The packet proves useful narrower facts:

- an up-flat \(W_u\) cannot also make every column of \(W_d=W_uV\) flat for the observed non-circulant-equivalent CKM;
- the reported lower bounds on individual down-column non-flatness follow from the triangle bound in `scripts/algebra.py:31-35` and are numerically consistent with `scripts/algebra.out:18-20`;
- the Q contribution to one down isotropic row changes sign over the scanned phases (`scripts/structure2.py:20-34`; `scripts/structure2.out:8`), which demonstrates tuned zeros rather than a sign obstruction.

The inference at `REPORT.md:126-130` is not valid: failure of S3 invariance removes one sufficient all-row cancellation mechanism, but it does not prove that every other kernel-independent cancellation is impossible.  The report explicitly says the joint \(d^c\) condition was not checked (`REPORT.md:127`), and the selective-class evidence is a local Powell search (`PREREG_FOLLOWUP_2026-10-15.md:22-24`; `scripts/upflat.py:44-58`).

No-go stress test:

1. **S3 equal-modulus route:** excluded within the up-flat mass-carrying M2 restriction by the flat-flat theorem.
2. **Direct-row projection route:** not excluded; a measured row can vanish without the full per-field tensor vanishing.
3. **Q versus \(d^c\) cancellation:** not excluded and expressly left unchecked.
4. **Selective/range-2 kernel identities:** sampled numerically, not exhaustively classified.
5. **Correlated carrier multiplets or carrier mixing:** outside the declared no-mixing calculation, so unavailable for this narrow model but not a general X2 no-go.
6. **Known partial escapes:** E1 already shows that observable-row flatness can evade a stronger-looking per-field criterion (`REPORT.md:107-114`), and M1 shows that right-handed placement matters.

The witness residual in `scripts/structure2.py:20-34` is only the Q part of the down isotropic row, whereas the advertised conclusion covers full vector, axial, and anisotropic direct rows.  This fails residual matching and resolution matching.  The strongest honest statement is: **no S3-invariant up-flat M2 realization exists in the specified on-site mass-carrying subclass; the searches found only tuned point cancellations and no bracket-robust safe point.**  A general “no structural zero” theorem remains open.

### 4.3 L-words

Confirmed as a finite-dimensional algebra statement, with a conditional physics conclusion.  For nondegenerate observed masses and nontrivial CKM, \([H_u,H_d]\ne0\).  A noncommutative unital *-subalgebra of \(M_3\) is unitarily equivalent to either \(M_3\) or \(M_2\oplus\mathbb C\).  Either algebra contains a rank-one projector onto a vector whose corner-basis moduli are not all equal.  Since that projector is a noncommutative polynomial in \(H_u,H_d\), at least one contributing word has a corner-dependent diagonal.  This validates `REPORT.md:144-147`.

It does **not** prove that the actual two-loop self-energy resolves that word with a nonzero independent kernel.  The report correctly labels the \(10^{-9}\)-\(10^{-10}\) size as suggested (`REPORT.md:149-157`; `scripts/structure2.py:35-46`).  The estimate is arithmetically reasonable—\(1.3\times10^{-4}\times1.6\times10^{-5}\times O(0.3)\sim10^{-10}\)—but it is not a two-loop calculation.

## 5. Mechanism 1

### 5.1 All-orders statement

At the exactly symmetric point, the statement is correct.  If all law-level couplings and propagators transform covariantly and flavour breaking occurs only through vevs, then at \(v=0\) the all-orders effective action retains the cubic symmetry.  The two-index corner/axis kinetic tensor is therefore \(\alpha+\beta\delta_{ca}\), and the defined residual is zero.

The equation at `REPORT.md:134-136` needs its vev argument shown explicitly.  For a non-invariant fixed vev,

\[
U_R\Sigma_v(p)U_R^\dagger=\Sigma_{Rv}(Rp),
\]

not generally \(\Sigma_v(Rp)\).  Covariance relates two rotated vacua; it does not make one symmetry-breaking vacuum invariant.  Therefore “zero residual for any vev pattern” is false if read after inserting a fixed arbitrary vev.  The exact all-orders zero applies in the unbroken symmetric phase, while nonzero-vev effects require an expansion in vev insertions.

### 5.2 Suppression estimate and FCNC

The estimate \(y^2(va)^2\) is dimensionally reasonable for a chirality-preserving kinetic correction whose first flavour-breaking contribution needs two Yukawa/vev mass insertions.  With \(v=174\) GeV and \(a^{-1}=M_{\rm Pl}\), it is about \(2\times10^{-34}\), and multiplying \(a\) by 600 gives about \(7\times10^{-29}\), consistent with the quoted orders at `REPORT.md:137`.  It remains suggested: logarithms, infrared sensitivity, the exact carrier spectrum, and whether a lower-order symmetry-allowed operator exists have not been computed.

The FCNC issue is correctly identified (`REPORT.md:138`).  Multiple hw2 electroweak-doublet carriers with order-one flavour-off-diagonal top-sector couplings generically mediate tree-level neutral flavour change unless alignment, heaviness, or another selection rule removes it.  Since no scalar spectrum, alignment theorem, or flavour bound is supplied, this is an open viability cost, not a minor bookkeeping point.

## 6. Fixed reading and scope

The fixed criterion is existential: one realization in the stated family must keep every direct-row residual inside its bound after the already-allowed speed and tetragonal subtractions (`TESTS.md:397-410`; `PREREG.md:8-20`).  It does not demand naturalness, a unique realization, or that every saved floating-point array itself resolve \(10^{-22}\).

B-gen lies inside the **declared effective family**:

- its SVD supplies \(W_u,W_d,X_u,X_d\) with \(W_u^\dagger W_d=V\) (`scripts/univ.py:86-99,119-128`);
- its diagonal Higgs couplings use the allowed on-site/selective symbols (`PREREG.md:63-72`);
- its six orientation-dependent off-diagonal phases use the allowed corner-selective \(\tau_x\sigma_c\) carriers (`PREREG.md:73-78`; `REPORT.md:56-59`);
- the quark residual is exactly zero for the exact parameterized texture, while the fixed electron contribution is nonzero but safely below its direct bound.

Thus `TEXTURE-ESCAPE` is met as worded.  The scope is strictly: one loop; continuous time and the X2 walker; symmetric-phase nearest-neighbour Higgs; the no-carrier-mixing M1/M2 effective carrier rules as built; the sampled regulator/placement/symbol bracket; and no RG running from \(1/a\) (`REPORT.md:34-37`).  It is **not** a proof that a complete gauged Spin(10) X2 UV realization with the required carrier multiplets, vacuum alignment, scalar masses, and FCNC safety exists.  It also does not refute X2-L8's weaker symmetry statement that CKM permits/forces a traceless-strain channel (`X2_COMBO_REPORT.md:126-136`); it shows that the coefficient of the one-loop direct-speed residual can vanish in the enlarged texture/carrier family.

## Per-item disposition

1. **S2 and Lemma S:** confirmed after narrowing.  Off-diagonal phases drop out only for separate non-mixing carriers; diagonal symbol phases can enter.  Lemma S is exact for fully S3-invariant loop data, but equal moduli alone do not guarantee that hypothesis for selective symbols.
2. **B-gen fit:** confirmed as an observationally exact fit and exact-modulus parameterization.  The PDG inputs are recalled correctly.  The stored binary64 matrices themselves fail the \(10^{-22}\) rows by \(5\times10^2\)-\(4\times10^3\) in an independent high-precision evaluation; reconstructing the exact ansatz from `p` restores the identity.  The mass inputs mix renormalization scales, and the printed chi-square is not statistical.
3. **M1 diagonal equalisation:** confirmed for the exhibited OBS-2 realization at numerical/construction level; if equality is exact, every M1 row including anisotropic rows vanishes and a down right-handed rotation alone suffices.  “For any \(W_u\)” is not proved.
4. **Theorems:** flat-flat iff circulant-equivalent is confirmed; the observed CKM strongly violates the necessary Latin-square pattern.  “Up flat + M2: no structural zero” is not confirmed beyond the narrower absence of an S3-invariant solution.  The L-word algebra theorem is confirmed, while its two-loop realization and size remain suggested.
5. **Mechanism 1:** exact all-orders zero at \(v=0\) is confirmed; zero at an arbitrary fixed vev is not.  The \((va)^2\) estimate is reasonable but uncomputed.  The FCNC problem is correctly identified and unresolved.
6. **Fixed reading:** `TEXTURE-ESCAPE` is met in the declared effective one-loop family, with the scope and artifact-precision qualifications above.

## Strongest correct statement

Within the explicitly declared one-loop, symmetric-phase X2 Yukawa/carrier family, the observed PDG-2024 quark masses and CKM data admit an equal-modulus B-gen texture whose **exact parameterization** makes the complete quark one-loop data S3-invariant; cubic covariance then forces \(T(c,a)=\alpha+\beta\delta_{ca}\), so the already-allowed per-field speed and tetragonal counterterms remove the quark residual identically, while the tiny neutrino-induced electron remainder stays below its bound.  Therefore OBS-2's \(c_{TT}^d\sim-2\times10^{-8}\) is a consequence of its chosen texture/carrier placement and is not forced by CKM at one loop.  This conclusion does not make the rounded `.npz` matrices a \(10^{-22}\)-accurate certificate, does not prove universal M1 diagonal equalisation or the up-flat-M2 no-go, and does not establish an all-orders broken-vacuum escape, a two-loop cancellation, or an FCNC-safe gauged UV completion.
