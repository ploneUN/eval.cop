from five import grok
from plone.directives import dexterity, form
from eval.cop.content.community_of_practice import ICommunityofPractice

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ICommunityofPractice)
    grok.require('zope2.View')
    grok.template('community_of_practice_view')
    grok.name('view')

