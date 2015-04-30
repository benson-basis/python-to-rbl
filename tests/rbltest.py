from pythontorbljvm import rbl

def test_rbl():
    RBL = rbl.Rbl(root='rbl-je-7.12.104', version='7.12.104')
    factory = RBL.factory()
    annotator = RBL.annotator(factory, language='eng')

    something = annotator.annotate(RBL.charsequence("George Washington slept here."))
    assert something.getTokens().size() == 5
    george = something.getTokens().get(0).getText()
    assert george == 'George'
