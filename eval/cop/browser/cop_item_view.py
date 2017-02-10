from five import grok
from plone.directives import dexterity, form
from eval.cop.content.cop_item import ICOPItem

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ICOPItem)
    grok.require('zope2.View')
    grok.template('cop_item_view')
    grok.name('view')
    
    def news_items(self):
        catalog = self.context.portal_catalog
        context = self.context
        news = catalog.unrestrictedSearchResults(path={'query':'/'.join(context.getPhysicalPath()), 'depth':1}, portal_type='News Item', sort_order='reverse', sort_on='created')
        return news
    
    def get_items(self, portal_type=None):
        catalog = self.context.portal_catalog
        context = self.context
        brains = catalog.unrestrictedSearchResults(path={'query':'/'.join(context.getPhysicalPath()), 'depth':1}, portal_type=portal_type, sort_order='reverse', sort_on='created', sort_limit=5)[:5]
        return brains
