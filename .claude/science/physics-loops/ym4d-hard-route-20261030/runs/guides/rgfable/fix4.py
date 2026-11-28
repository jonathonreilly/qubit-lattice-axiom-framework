import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
reps = [
 ("Status: started. This file is written in stages.",
  "Status: done (steps 1 to 5 written; RESULT line at the end). This file was written in stages.\nLiterature: every citation in this file is recalled from memory. No paper was opened in this run. Treat each\ncitation as RECALLED until it is read."),
 ("- Hierarchical models: Gawedzki and Kupiainen (1986, hierarchical O(N) sigma model, from weak coupling to the\n  high-temperature fixed point).",
  "- Hierarchical models: Gawedzki and Kupiainen (1986, hierarchical O(N) sigma model, from weak coupling to the\n  high-temperature fixed point; as I recall for large N only)."),
 ("Haller and Kennedy (1996); Bertini, Cirillo and Olivieri (1999,\n2005):",
  "Haller and Kennedy (1996); Bertini, Cirillo and Olivieri (1999\nand later; years not checked):"),
 ("### 4.3 What the comparison says\n",
  "4. Remark 4 of my 1.4 is the lane's K7 test. The lane holds it at BELIEF grade, and row 995 doubts the 1981 end\n   point. Its theorem-grade form is Proposition V (row 712).\n\n### 4.3 What the comparison says\n"),
]
for a, b in reps:
    n = s.count(a)
    if n != 1:
        print("MISMATCH", n, repr(a[:70])); sys.exit(1)
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("ok")
