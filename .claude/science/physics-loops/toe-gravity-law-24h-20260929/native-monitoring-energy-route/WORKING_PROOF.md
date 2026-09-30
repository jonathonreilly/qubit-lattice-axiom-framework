# Candidate: energy growth under supplied native occupation monitoring

Root analytic derivation frozen before reuse or independent checking. Mainfb5da8dd, selected procedures7146fe17, original deadline2026-09-30T22:41:00.557005UTC. Extra dynamics below are a specified comparison instrument, not selected by the axioms. No computation has run. Mechanism provenance: the matter agent supplied a first-moment pin bound using onlyS; root independently reconstructed that bound and the moment normalization in PRE43b89b03, and then derived the fullS+W pinned matrix below. The readout-energy proof71dc7d53 is fully root checked84d0e46e. This new monitoring theorem remains UNCHECKED.

Use actual main H0=muDdiag+B*K B, whereB is the physical unordered pair-edge annihilator column,K is the positive S+W kernel,mu,tau>0,L>=5. LetP_x be its edge-space projection onto the18pairs incident tox. Summing the adjoint occupation-dephasing dissipators gives the exact full-carrier identity

Q_read=sum_x D[n_x]^*H0=sum_x B*P_x K P_x B-2B*K B.

This follows since[n_x,B_e]=-1_(x in e)B_e and everypair has2endpoints. Ddiag commutes with alln_x. No state/eigenvector assumption is used. The actual kernel and dephasing convention D[l]^*O=l*Ol-{l*l,O}/2 must remain fixed.

Candidate exact pinned matrices: the six axial incident edges have diagonal2mu/3+4tau and no offdiagonal pinned axial entries. In each coordinate plane the four incident plane edges form a cycle, with diagonal3mu/2+3tau and each neighboring offdiagonalmu/4-3tau/2. Distinct planes and axial/plane types do not mix. A gradient's cross-center term cannot survive a pin because two distinct nearest-neighbor pair centers cannot both containx: all possible centers are x+/-e_i, none adjacent atL>=5. Thus the W pin is exactly six copies of the same-center Gram; the two plane centers are still both included. The cycle eigenvalues are2mu,3mu/2+3tau (twice),mu+6tau. The axial value and2mu give the smallest eigenvalue

lambda_pin=min(2mu/3+4tau,2mu)=2c_read,
c_read=min(mu/3+2tau,mu).

This is an actual18by18 kernel compression, not compression of the physical Hilbert space. Its identity/literal signs must be independently checked before use. If correct, positivity under pinning yieldssum_x B*P_xKP_xB>=4c_read E_pair, whereE_pair=sum_edges n_in_j. The exact diagonal identityDdiag=N-2E_pair+V3/mu then gives

Q_read>=2c_read N-2H0+2(mu-c_read)Ddiag+(2c_read/mu)V3
       >=2c_read N-2H0.

Both remainders are positive becausec_read<=mu. This proves an all-state operator differential bound, not merely a spectral-ground expectation.

Supply the finite-volume master equationrho_dot=-i[H0-nuN,rho]+gamma(t)sum_x D[n_x]rho, with bounded integrablegamma>=0. It is an added occupation monitoring/dephasing law with a supplied clock; no actual framework instrument is identified. Nexpect=nbar is constant. SetGamma(t)=integral_0^t gamma(s)ds andE(t)=TrH0rho(t). The conditional bound above and integrating factor give

E(t)>=c_read nbar+(E(0)-c_read nbar) exp(-2Gamma(t)).

For low-energy inputE0<c_read nbar, maintainingE(t)<=Emax<c_read nbar necessarily requires

Gamma(t)<=0.5 log[(c_read nbar-E0)/(c_read nbar-Emax)].

IfE0/nbar andEmax/nbar areO(r) forr->0, the allowed integrated strength isO(r). This last statement is conditional on that supplied energy tolerance; existence of a phase or its physical monitoring is not claimed. Landed low-energy unitary trials supply smallE0/nbar without an open EOS, but need a separately named toleratedEmax. The fixed occupation instrument, basis, noise rates, time and energy-accounting apparatus remain imports. No universal per-Record cost, sharp-memory permanence, autonomous implementation or axiom inconsistency follows.

Required independent checks: exact full pinned matrices at actual unaliasedL and all signs, factor2 convention inQ_read, full-carrier count identity and positivity, nonconstant gamma integrating factor, and sharp distinction between optical on-site moments and lowq modes. Any control must be separately priced and guarded; no dense many-body enumeration is needed.
