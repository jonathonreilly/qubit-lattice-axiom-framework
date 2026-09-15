from pathlib import Path
import importlib.util,unittest,sys
r=Path('/private/tmp/review-drain-20260915');p=r/'train40/docs/audit/scripts/tests/test_review_receipt.py';spec=importlib.util.spec_from_file_location('regression',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.TOOL=Path(__file__).with_name('review_receipt.py');result=unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromModule(m));sys.exit(not result.wasSuccessful())
