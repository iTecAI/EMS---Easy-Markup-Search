import pyquery as pq
import urllib2 as url
class parser(): #much like how one would do it in HTMLParser, but easier.
    def __init__(self, html): #init parser class
        self.html = html

    #list all elements with class
    def getElementsByClass(self, eclass):
        classindex = pq.allIndex(self.html, 'class="') #get all classes mentioned ANYWHERE
        classes = []
        for c in classindex: #get raw classes
            c_start = c + 7
            c_end = self.html.find('"', c_start)
            classes.append(self.html[c_start:c_end])

        approved = []
        c_count = 0
        for c in classes: #check for classes with match
            contained = True
            for i in eclass.split(' '):
                if i in c:
                    pass
                else:
                    contained = False
            if contained:
                approved.append(classindex[c_count])
                print c
            c_count += 1

        elements = [] #init list elements
        for c in approved: #begin handling element indexes
            start = self.html.rfind('<', 0, c) #find beginning of tag
            etype = ''
            i = start + 1
            while self.html[i] != ' ': #find tag type
                etype = etype + self.html[i]
                i += 1
            end = self.html.find('</' + etype + '>', c) + 2 + len(etype) #find end of element
            elements.append(self.html[start:end - 1 - len(etype)]) #add element to list
        return elements

    #get element with ID
    def getElementById(self, eid):
        idindex = pq.allIndex(self.html, 'id="') #find all ids
        ids = []
        for i in idindex: #get raw ids
            i_start = i + 4
            i_end = self.html.find('"', i_start)
            ids.append(self.html[i_start:i_end])

        approved = []
        i_count = 0
        elementindex = None
        for Id in ids: #check for id with match
            contained = True
            for i in eid.split(' '):
                if i in Id:
                    pass
                else:
                    contained = False
            if contained:
                elementindex = idindex[i_count]
                print Id
                break
            i_count += 1
            if elementindex != None:
                break
        if elementindex == None:
            ereturn = None
        else:
            start = self.html.rfind('<', 0, elementindex) #find beginning of tag
            etype = ''
            i = start + 1
            while self.html[i] != ' ': #find tag type
                etype = etype + self.html[i]
                i += 1
            end = self.html.find('</' + etype + '>', elementindex) + 2 + len(etype) #find end of element
            ereturn = self.html[start:end - 1 - len(etype)]
            return ereturn
            

    #list elements of a type
    def getElementsByType(self, etype):
        estarts = pq.allIndex(self.html, '<' + etype + ' ')
        elements = []
        for i in estarts:
            end = self.html.find('</' + etype + '>', i) + 2 + len(etype)
            elements.append(self.html[i:end + 1])
        return elements

    #get content of a <p>, <h1>, <title>, etc.
    def getContent(self, estring):
        etype = '' #get tag type
        i = 1
        while self.html[i] != ' ': #find tag type
            etype = etype + estring[i]
            i += 1
        cbegin = estring.find('>') #find content start
        cend = estring.find('</' + etype + '>') #find content end
        content = estring[cbegin + 1:cend] #get content
        return content

    #get attrs of an element
    def getAttrs(self, estring):
        es_end = estring.find('">') #fine start tag end
        start_tag = estring[:es_end + 2] #get full start tag
        attr_locs = pq.allIndex(start_tag, '="') #find attrs
        attrs = {} #init attr dict
        for loc in attr_locs: #add all attrs to dict
            key = estring[estring.rfind(' ', 0, loc) + 1:loc]
            val = estring[loc + 2:estring.find('"', loc + 2, len(estring))]
            attrs[key] = val

        return attrs
