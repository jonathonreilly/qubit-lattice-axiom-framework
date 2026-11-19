import sys
p=sys.argv[1]; t=open(p,encoding='utf-8').read()
def rep(a,b):
    global t
    assert t.count(a)==1, (t.count(a), a[:70])
    t=t.replace(a,b)
rep("""- S3 reason up: done. C1-C13 argued: forest faces solved exactly (the only proved corners); faces at infinity useless; (i) is free and all cost is in (ii); four properties (ii) must use; exact sum-rule form of (ii) on a star path.""",
"""- S3 reason up: done. C1-C13 argued: forest faces solved exactly; (i) is free and all cost is in (ii); four properties (ii) must use; exact sum-rule form of (ii) on a star path. Corrected later in place: the sheet face is a proved end-point given N4c (after step 3); C12 and the block-product row (step 5).""")
rep("""| four-cycle $\\{12,23,34,41\\}$ | itself | a model with planes 13 and 24 missing; its closed surfaces are products of a loop in the 13-plane with a loop in the 24-plane | unknown to this run; no source found |""",
"""| four-cycle $\\{12,23,34,41\\}$ | itself | a model with planes 13 and 24 missing; its closed surfaces are products of a loop in the 13-plane with a loop in the 24-plane | unknown to this run at step 3; no source found. Taken up in step 7.2 (C15, route F4), there with the relabelling in which planes 12 and 34 are the missing ones |""")
open(p,'w',encoding='utf-8').write(t)
print('ok')
