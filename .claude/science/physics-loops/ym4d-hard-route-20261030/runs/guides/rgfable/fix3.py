import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
reps = [
 ("Result in one line: (NL) and the Jensen form of (JEN) are proved; the path form of (JEN) fails at a named line,\n(HOL); so (GAIN) cannot be fed in the stated form. All proofs below were written and checked by this worker only.",
  "Result in one line: (NL) and the Jensen form of (JEN) are proved; the path form of (JEN) stops at a named line,\n(HOL); so (GAIN) cannot be fed in the stated form. All proofs below were written and checked by this worker only.\nCorrected after step 4 (see 4.2): at (HOL) the failure is PROVED for field-independent directions only; for\nfield-dependent frames it is ARGUED, and the lane holds that case as OPEN."),
 ("2. PROVED (standard). The cancellation cannot be restored by a better path.",
  "2. RECALLED for the continuum; ARGUED for the lattice (corrected in 4.2). The cancellation cannot be restored by\n   a better path of constant twists."),
 ("- Verdict. The first statement of attack 1 is proved in the parts (NL) and (JEN-a, b). The chain breaks at (HOL).",
  "- Verdict (corrected in 4.2). The first statement of attack 1 is proved in the parts (NL) and (JEN-a, b). The\n  chain stops at (HOL): broken for field-independent directions (PROVED), not excluded for field-dependent frames."),
]
for a, b in reps:
    n = s.count(a)
    if n != 1:
        print("MISMATCH", n, a[:60]); sys.exit(1)
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("ok")
