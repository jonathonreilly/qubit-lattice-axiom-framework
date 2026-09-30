# Narrow independent-check correction

Root and axial_check identified a support-count underestimate in section 7.
Axial magnetic-pair centers separated by 2e_i share only one B neighbor.
Their two complete stars contain 2 A plus 11 B factors, so the encoded
qubit count is 2+11(2+6q_E)=24+66q_E. The former 22+60q_E count covers only
diagonal centers, which share two B neighbors. The 7a_block spatial diameter,
cell allocation, resource certificate, Hamiltonian, errors and ledger are
unchanged. Exactly that one expression was corrected in REPORT.md.

Original report and manifest bytes are preserved under historical/initial-freeze.
Original REPORT SHA256 b3e4a1f2567e06d3fc37cab450e1412116b90db0871927bc4b8bfb967186b35b.
Original MANIFEST SHA256 54fb1719f12065ad4c924bb34acb9f810d35c1803c91eb7a4b25eff4a12281b1.
