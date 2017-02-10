from five import grok
from plone.directives import dexterity, form
from eval.cop.content.cop_discussion import ICOPDiscussion

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ICOPDiscussion)
    grok.require('zope2.View')
    grok.template('cop_discussion_view')
    grok.name('view')

