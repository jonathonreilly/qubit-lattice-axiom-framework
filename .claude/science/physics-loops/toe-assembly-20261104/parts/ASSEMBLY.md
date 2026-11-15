## State of attack

Bookkeeping only. Written 2026-11-13 from `TOE_ASSEMBLY.md` at commit `70ef4aaf65`. This file adds no mathematics and grants nothing.

The assembly theorem is `TOE_ASSEMBLY.md` line 721. It is conditional on 18 parts, on T0 with bridges Y1 to Y5, on the coherence obligation AS0 (line 719) and on the working set S of section 3. Line 735 says: "Today every part is open or holds only on supplied models; the ledger has no retained row; **S** is empty; T0 is not proved."

The working set S is a premise, not a statement: only the owner adopts it. Parts LW2 and GB1 are named in section 5 but not in the theorem.

Section 7.1 and the import lines of section 5 disagree on nine edges. In 7.1 only: LW1 to ST1, GA2 to ST1, CH1 to ST1, GA2 to FL2, GA2 to CS1. In the import lines only: GR2 to LZ1, LZ1 to GA2, ZM1 to CH1, MT1 to FL1. The part files here use the 7.1 edges, and GB1's own import line. Not resolved here.

## Obligations

- open: T1-T9 given LW1,ZM1,TM1,ST1,LZ1,BR1,MT1,GA1,GA2,CH1,CG1,FL1,EW1,FL2,VC1,GR1,GR2,CS1,T0,AS0 -> frontier
- open: AS0 given LW1,ZM1,VC1 -> T1-T9
- open: T0 -> GA2

## Requests

- owner: the working set S (PS-1 to PS-11 and the later decisions in section 3) is the root premise of every part. PR #10140 proposes it; the landing review held that PR on 2026-11-13.
