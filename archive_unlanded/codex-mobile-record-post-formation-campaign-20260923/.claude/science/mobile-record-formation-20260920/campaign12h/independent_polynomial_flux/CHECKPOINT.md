# Current independent checkpoint

No primary source has been read. The three analytic derivations are complete
in REPORT.md, and all 33 groups of independent exact controls passed.

- For k>=1, summing over edge-window offsets telescopes to the difference
  of adjacent k-site tensor blocks. Homogeneous products are stationary.
  With P=E S and normalized seven probabilities, J_a=p_a(partial_a P-kP)
  for all seven labels, equivalently J_occupied=C grad P_restricted.
  This supplies nonlinear entropy compatibility and the previously sealed
  Euler/fluctuation proof hypotheses for fixed k and fixed positive floor.
- The cubic target has balanced spectrum +/-|alpha|rho^2 sqrt(3(1-rho))
  times the wavevector norm and four zeros. At q_i=rho/3,
  J_rho^i=3alpha(1-rho)(rho^2 g_i+3g_i^3),
  J_gj^i=alpha rho^3 delta_ij/3
    +3alpha[rho(1-rho)g_i-3g_i^3]g_j,
  J_(qj-rho/3)^i=3alpha(3delta_ij-1)g_i^3.
  These nonlinear expressions are only cubically covariant in general,
  and the zero-quadrupole manifold is not preserved by generic spatial
  profiles.
- Periodic zero sum implies a de Bruijn coboundary G. Central-endpoint
  antisymmetry gives G(x,y,z)=S(x,y)+S(y,z)-S(x,z)+A(x,y,z), with S
  symmetric and A fully alternating. G and S share an additive constant
  gauge; the alternating part is uniquely determined and contributes zero
  product current. Proper-cubic mean potentials are exactly
  P_i=(u+v rho+w q_i)g_i, modulo irrelevant constants. All-density nonzero
  isotropy requires u=0,w=-3v/2,v!=0. The alternating microscopic class
  is real and includes the proper-cubic chiral determinant example.

The controls include exact degree-1-through-5 product currents, all cubic
six-site strings, symbolic six-field currents and spectrum, the explicit
continuous-rotation defect, rational classification dimensions certified
by modular lower bounds plus explicit kernels, and a proper-cubic
alternating microscopic witness with zero actual product currents.
RUN.log and RESULTS.json are byte-identical. The corrected symbolic-symbol
and relative-path bookkeeping mistakes are preserved in ATTEMPT_1* and
EXECUTION_NOTES.md. No unresolved mathematical obligation remains under
the reported hypotheses; no broader classification or nonlinear continuous
rotational theorem is claimed.

Final verification confirmed the complete 33-check result and identical
full output, including the added exact tensor-value and constant-gauge
checks. All six imported report/seal identities were rechecked unchanged.
PRE_SOURCE_SEAL.json records the completed artifact identities. The next
action is returning the bounded findings; no primary-source comparison,
new calculation branch, audit or publication action is part of this task.
