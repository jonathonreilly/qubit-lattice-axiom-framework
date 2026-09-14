# Block 7 — local reference encoding and fermionic locality

Status: active author derivation; independent review pending.

Source revision: b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf.

Question: for the specified all-parity Cycle703 encoding with bounded local
logical X loaders, can an arbitrary stabilizer-equivalent or non-Pauli
operator implement every spatially local CAR hopping with bounded support?
Test the missing common-encoding bridge rather than operator covariance alone.

Candidate invariant: an intermediate logical X anticommutes with a Jordan-
Wigner hopping, while a physical representative disjoint from its local
loader commutes. Derive an operator-norm approximation gap, geometric family
lower bound and explicit exchange witness. Check whether returned clean
ancillas, alternate stabilizer representatives or local circuit synthesis
change that invariant. Compare an explicit fixed-parity ordinary BKSF code
which does not supply local odd loaders; distinguish abstract encoding from
framework selection/physical-site formation. No axiom conclusion is planned.

Reading completed this block: full Cycle703 patch tableau covariance review
note; recurrent compiler tournament main narrative through locality section
and prior-art section, plus full finite-edge occupancy dictionary (previous
block rerank); exact source definitions of logical_rows, stream_terms and
local bounded dressed_stream_terms. Remaining source closure will be read
before source-specific claims. No foreign runner outcomes are called rerun.
