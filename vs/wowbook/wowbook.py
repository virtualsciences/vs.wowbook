from zope.component import getUtility
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.documentviewer.browser.views import DocumentViewerView


class WowBookView(DocumentViewerView):

    def pages(self):
        if self.enabled:
            data = self.dv_data()
            path = data['resources']['page']['image']
            number = data['pages']

            return [('<img src="' + path + '" alt="Page {page}" ' +
                'style="width: 100%"/>').format(size='large', page=str(i+1))
                for i in range(number)]

        return []

    def iframe(self, target, height):
        return (
            '<iframe src="' + self.context.absolute_url() + '/' + target +
            '" style="width: 100%; height: ' + height + '"/>')


class WowBookUtils(WowBookView):

    def index(self):
        return self
