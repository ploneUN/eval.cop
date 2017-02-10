from collective.grok import gs
from eval.cop import MessageFactory as _

@gs.importstep(
    name=u'eval.cop', 
    title=_('eval.cop import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('eval.cop.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
