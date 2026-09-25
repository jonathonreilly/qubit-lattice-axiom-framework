# Released-source POST: native ground-sector filling

No material mathematical correction is required for the released root theorem on equal even cubic tori with \(L\ge6\), at fixed graph and fixed positive \(\tau\) before \(g\downarrow0\). The root's constants, physical color trial, treatment of the gated electric operator, and strict endpoint exclusions agree with the independently sealed PRE after accounting for the factor of two in the magnetic notation. The root bounds are valid sufficient bounds; the PRE's sharper incidence estimates and broader geometry are separately attributed below.

This is a released-source comparison, not a second blind reconstruction or an applied audit verdict. The complete root argument, working derivation, control program, all scientific output rows and execution/source records were read as data. No root or parent scientific program was executed. The PRE, its 35 sealed members, and its seal remain byte-identical.

## 1. Exact sources and chronology

The released report is `post_sources/native-ground-filling-personal/NATIVE_GROUND_SECTOR_FILLING_ROOT.md`, SHA256 `aef82e905d9270ae543501dd7548687fae93fda806cc8dd7b7c8861aafe8cadb`. Its `AUTHOR_SEAL.json`, SHA256 `0b72c3cd4dd5404a53de9808a5bf99fab48eab182defedba729b695ff4202066`, binds nine members and records 2026-09-25 02:55:49.585286 UTC. All nine members and their released live origins were verified.

The comparison anchor is my `PRE.md`, SHA256 `edaaee9321fe99e298acba00dd5c8b9dd750529595806eb04d844bbd27f38b72`, with `PRE_SEAL.json`, SHA256 `0d420d0263cb53ed341d79f361cfc7ee2dae9125f976b6715216bd48a5cd8384`, sealed at 03:23:23.028861 UTC. The author seal precedes that PRE seal. The PRE was completed without reading this candidate. The definition-only clarification \(K=g^2/(2\tau)\), \(\delta=1/(4\tau g^2)\), hence \(K/\delta=2g^4\), was already preserved in the PRE packet; it was not a disclosure of the author's argument.

The shared scientific parents remain exactly:

- `LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`, SHA256 `7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a`.
- `LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md`, SHA256 `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b`.

Their exact main revision `60c5f194d940a7bbaf1cdd545296e31d74a02f1a` was bound in the PRE, and their live bytes were refreshed here. Their model and domain statements are reused under the same hypotheses, without rerunning or re-certifying their scientific controls. Applicable instructions and reviewer skill were reused from the current verified instruction packet.

The author's source inventory openly records earlier one-pair author/checker work as motivating provisional context. I read those inventory entries only. The referenced packets were not opened or live-hash-checked, and this POST does not certify their contents or attribute root35's entire history as independent of them. The released root35 proof supplies the arbitrary-occupancy argument used here without relying on an unreviewed one-pair theorem.

## 2. Model, factor of two, colors and geometry

Both arguments use the same Hamiltonian

\[
h_g=\frac{g^2}{2\tau}D+\frac{H_4}{4\tau g^2},\qquad
D=\sum_{a\to b:q_b=0}E_{ab}(E_{ab}-q_a),
\]

with the original unsigned tensor hard-core algebra. Integer \(E_{ab}\) and \(q_a=\pm1\) make every retained summand of \(D\) nonnegative. The empty-B gate is not dropped. In the PRE, \(Q_{\rm PRE}=-H_4\); the root's full magnetic symbol is \(H_4(\theta)=-2K_m(\theta)\), and its occupation matrix \(Q_m\) is intertwined with \(K_m(0)\) by \(J_m\). Thus the PRE's full magnetic symbol is \(2K_m\), while its uniform half-filling trial value \(T\) is \(2R_{n/2}\). This is a notation conversion, not a claim that an occupation matrix is the full color operator.

Summed Gauss law gives \(N=n+m\), \(m\) even and exactly \(m/2\) negative charges. Every such matter word has an integer tree-supported reference flow. The remaining flows form the full integer cycle lattice. No charge color, Gauss-compatible flow or harmonic winding direction is discarded in the lower bounds.

For each occupied B set there are \(\binom{n+m}{m/2}\) color assignments. Every legal outward/return path permutes the occupied charge slots bijectively, so it sends the uniform allowed-color vector at one occupancy set to the uniform vector at its output. The return may use an old B record; both arguments retain these paths. At zero cycle angle all coefficients are nonnegative integers. This proves the root's intertwining relation and its all-color row bound without irreducibility or a claim about the rest of the color spectrum.

On equal even \(L\ge6\) tori, overlap-one and overlap-two pair counts are \(3n\) and \(6n\). Their union sizes 11 and 10 give per-B union incidences 33 and 60 by bipartition-preserving translation transitivity. The root correctly excludes side-four wrap coincidences. Its formulas are not asserted for \(L=4\) or rectangular tori; the PRE's treatment of those geometries is additional work.

## 3. Exact local and variational constants

The root's \((s_a,s_c,t)\) are exactly the PRE's \((u_a,u_c,w)\). Its polynomial \(P_r\) equals the PRE's exact local return count. All 147 grouped rows, including multiplicities, agree with the sealed PRE's independently enumerated 3072 masks. The root bounds use union occupation \(\ell=s_a+s_c-t\) and union vacancies \(z=12-r-\ell\); the PRE uses the different incidence counts \(s_a+s_c\) and \(12-s_a-s_c\).

The five root table entries recomputed from those stored PRE counts are:

| \(r,t\) | patterns | \(\max(P_r-v)/\ell\) | \(\max P_r/z\) |
|---|---:|---:|---:|
| 1,0 | 36 | 69/2 | 28 |
| 1,1 | 36 | 40 | 24 |
| 2,0 | 25 | 37 | 104/3 |
| 2,1 | 25 | 44 | 80/3 |
| 2,2 | 25 | 38 | 23 |

Zero denominators are handled correctly: \(\ell=0\) gives \(P_r=v\), and \(z=0\) gives \(P_r=0\). Hence the root's union inequalities and

\[
B_m=\min\{321n+3960m,\;3004(n-m)\}
\]

follow, with \(3960=33\cdot40+60\cdot44\) and \(3004=33\cdot28+60\cdot104/3\). Positive path multiplicities and the symmetric row estimate make this an operator bound over all colors and cycle angles. Together with \(D\ge0\), it implies \(e_m(g)\ge-B_m/(2\tau g^2)\).

The squared-path union weights are \((35,390,800)\) for overlap one and \((36,416,704)\) for overlap two in both reconstructions. The root's binomial average equals the PRE's falling-factorial formula. The new read-only comparison evaluates that latter formula on all 26 stored artificial 12-site cases and all 28 stored torus occupancies. Every exact fraction agrees. Odd occupancies in the artificial combinatorial check are not being presented as physical Gauss sectors.

The half-filling quotient satisfies exactly

\[
\frac{R_{n/2}}n=\frac{1905}{2}
 +\frac{378}{n-1}+\frac{414(2n-3)}{(n-1)(n-3)}>\frac{1905}{2}.
\]

The strict finite-volume excess and all four stored values for \(L=6,8,10,12\) agree. The \(L=6,8\) trials also match the stored PRE geometry results with exactly the factor of two. Neither quotient is claimed to be an eigenvalue or an optimal trial.

## 4. Physical trial, operator domain and limit

The root repairs the nonnormalizable zero-angle vector by using a smooth, real, even, normalized bump of width \(g\) in every cycle angle. This is valid on the actual physical Hilbert space. At fixed graph the set of matter words is finite, the chosen reference flows are finite, and each electric operator is an affine first derivative in the complete cycle coordinates. A smooth bump supported inside an angle chart extends smoothly to the torus and lies in the domain of every required second derivative. The finite-color vector times that bump is consequently in \(D(D)\), even though \(D\) is gated and need not control every electric direction.

First derivatives scale as \(g^{-1}\), so the retained electric quadratic form is \(O_L(g^{-2})\). The fixed finite Laurent matrix has bounded derivatives on the chart. Its scalar expectation in the real color vector is even under \(\theta\mapsto-\theta\), since the real path coefficients pair complex-conjugate phases and the scalar expectation is real. Its difference from the zero-angle value is therefore \(O_L(g^2)\). Integration against the normalized bump preserves these bounds. This yields

\[
e_{n/2}(g)\le-\frac{R_{n/2}}{2\tau g^2}+C_{L,\tau}.
\]

The constant may grow with volume. Harmonic-angle localization is allowed for this global variational infimum; it is not the Haar distribution of a specified zero-winding preparation and does not prove the same trial bound after imposing an additional winding restriction.

The two excluded filling ranges give \(B_m\le(1905/2)n\). The positive finite-volume excess above this value, divided by \(2\tau g^2\), eventually exceeds the bounded trial error. Therefore both endpoints are excluded strictly:

\[
421/2640<m/n<4103/6008.
\]

There are finitely many number sectors, so at least one sector attains the minimum of their spectral infima. This statement does not require a normalizable eigenvector at that infimum. The order is fixed graph and \(\tau>0\), then \(g\downarrow0\). A bounded pair count is excluded on graphs large enough relative to that count, once each such graph's own small-g threshold is met. It is not a uniform thermodynamic statement at fixed \(g\).

## 5. Distinct PRE additions and unchanged limitations

On the common \(L\ge6\) domain, the PRE's incidence bounds translate to root normalization as \(\min\{321n+3906m,2520(n-m)\}\), sharper than the root's union bounds. They give the coarser eventual interval \(421/2604\le m/n\le209/336\), with still stronger finite-n bounds from the exact trial quotient. This difference does not invalidate the root's weaker constants.

The PRE additionally covers simple rectangular cubic tori with all sides even and at least four, explicitly counts the side-four winding coincidences, proves full occupancy is excluded for every positive \(K,\delta\), and provides the finite-support quantitative remainder

\[
r_G(\eta,R)=4T/(2R+1)+\eta B_G(R),\qquad \eta=K/\delta,
\]

with an explicit Gauss-compatible electric-support bound. Its cycle-box construction and magnetic spectral characterization remain PRE-attributed. The finite-support remainder is not a claim of a better asymptotic rate than the root's smooth bump: the root gives a bounded error in physical energy, whereas the particular PRE box choice gives \(O_G(\eta^{1/3})\) in scaled energy. The two constructions serve different quantitative purposes.

The conclusions are about the supplied common Hamiltonian. Neither proof transfers microscopic spectral infima from a density-limit theorem, fixes an exact minimizing filling, proves an ordered phase or degeneracy, selects a physical vacuum, or proves a decay, relaxation or stationary formation process. The Hamiltonian preserves number while the formation instrument raises it; an energy comparison does not identify a dynamical attractor. The root's observational paragraph is properly conditional on an additional vacuum identification. No observed mass, reservoir, empirical exclusion or universal detector conclusion follows.

## 6. Evidence, tooling limitation and disposition

The root source `ground_filling_certificates.py` has SHA256 `197f7e83393b2d6fade8eaa5e6eb14dcab8f21d77e5dc56a566f1d37ee813080`. The source independently organizes its direct intermediate-set Gram count and polynomial check, using exact integer/fraction arithmetic. Its 49,447-byte `GROUND_FILLING_CERTIFICATES.json` is byte-identical to `CONTROL.stdout`, SHA256 `7942738261ffbcdd5dc28b75ea3f88dfcfce298129d9dba40253e9ea406a7f57`. The stored execution is exit zero, empty stderr, elapsed 0.34177000005729496 seconds. These are verified stored facts, not a fresh root run by this checker. The code/output cover all local masks and four finite geometries, not a many-body rotor diagonalization or volume limit.

The new `post_check.py`, SHA256 `8886068fd7204f5fd2fc826be2a3181956d838735d899e7f3fb7cfccd02f2501`, only reads, hashes and parses source/evidence and prints a report. Its sole execution, fully retained in `post_verification_attempt01/`, exited zero with empty stderr. The complete stdout, SHA256 `24369e4b581f544641b23f1f087c532af15b0e254f5cc5230099fd1e16601589`, was read, including every rational comparison. It does not rerun either earlier scientific control, and it does not constitute new independent geometry enumeration for \(L=10,12\).

The sealed PRE's `verify_pre.py` has a misleading read-only description: lines 69, 132 and 146 write `CONTROL_EXTENSION_DIFF.txt`, `SOURCE_PINS.json` and `VERIFICATION_REPORT.json`. It was inspected as text/AST and was not executed during POST. The root also reported that it did not execute this utility. Its bytes and the previous seal are preserved; the tooling limitation is not hidden by editing historical evidence. The new verifier has no filesystem mutation calls; only its outer recorder writes new POST artifacts. No mathematical result depends on rerunning the old utility.

The root's working-derivation typographical artifact remains unchanged. Several diagnostic schema-display attempts were truncated; they were not counted as complete reads. Complete bounded root-note reads, the previously completed full scientific row reads, and the complete new verification output supply the actual review coverage. No scientific/control failure or source discrepancy was found or erased.

This POST requires no change to the released scientific theorem. It preserves the different proof strengths and review provenance, the operational warning about the old verifier, and all stated fixed-graph/model limitations. `POST_SOURCE_PINS.json` and the separate `POST_SEAL.json` bind this report and new evidence. No source, publication, retained status or audit record was modified.
