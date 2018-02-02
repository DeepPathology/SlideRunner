"""

        This is SlideRunner - An Open Source Annotation Tool 
        for Digital Histology Slides.

         Marc Aubreville, Pattern Recognition Lab, 
         Friedrich-Alexander University Erlangen-Nuremberg 
         marc.aubreville@fau.de

        If you use this software in research, please citer our paper:
        M. Aubreville, C. Bertram, R. Klopfleisch and A. Maier:
        SlideRunner - A Tool for Massive Cell Annotations in Whole Slide Images
        Bildverarbeitung fuer die Medizin 2018, Springer Verlag, Berlin-Heidelberg

"""

def addSpotAnnotation(self, classID, event, typeAnno=1):
    self.saveLastViewport()
    pos_image = self.getMouseEventPosition(event)
    p1 = self.region[0]
    xpos_orig = int(pos_image[0] * self.getZoomValue() + p1[0])
    ypos_orig = int(pos_image[1] * self.getZoomValue() + p1[1])
    annotation = [xpos_orig, ypos_orig]
    if (classID is not None):
        self.lastAnnotationClass = classID
        self.showAnnoclass()
        self.writeDebug('added object center annotation of class %d, slide %d, person %d' % ( classID, self.slideUID,self.retrieveAnnotator(event)))
    xpos = int((annotation[0] - p1[0]) / self.getZoomValue())
    
    self.db.insertNewSpotAnnotation(xpos_orig,ypos_orig, self.slideUID, classID,self.retrieveAnnotator(event), type=typeAnno )
    self.showDBentryCount()
    self.showImage()

    self.showAnnotationsInOverview()

def addPolygonAnnotation(self,classID,event):
    """
        Polygon annotation is ready. Add to database.
    """
    self.saveLastViewport()
    self.ui.annotationMode=0
    self.db.insertNewPolygonAnnotation(self.ui.annotationsList,
                                self.slideUID,classID, self.retrieveAnnotator(event))
    self.showImage()
    self.showAnnotationsInOverview()
    self.writeDebug('added polygon annotation of class %d, slide %d, person %d' % ( classID, self.slideUID,self.retrieveAnnotator(event)))
    

def addAreaAnnotation(self, classID, event):
    self.saveLastViewport()
    pt2 = self.getMouseEventPosition(event)
    x1 = min(pt2[0],self.ui.anno_pt1[0])
    x2 = max(pt2[0],self.ui.anno_pt1[0])
    y1 = min(pt2[1],self.ui.anno_pt1[1])
    y2 = max(pt2[1],self.ui.anno_pt1[1])

    pos_image = self.getMouseEventPosition(event)
    leftUpper = self.region[0]
    xpos_orig_1 = int(x1 * self.getZoomValue() + leftUpper[0])
    ypos_orig_1 = int(y1 * self.getZoomValue() + leftUpper[1])
    xpos_orig_2 = int(x2 * self.getZoomValue() + leftUpper[0])
    ypos_orig_2 = int(y2 * self.getZoomValue() + leftUpper[1])

    self.lastAnnotationClass = classID
    self.showAnnoclass()

    self.db.insertNewAreaAnnotation(xpos_orig_1,ypos_orig_1,xpos_orig_2,ypos_orig_2,
                                self.slideUID,classID, self.retrieveAnnotator(event))

    self.showDBentryCount()
    self.showImage()
    self.showAnnotationsInOverview()
    self.writeDebug('added polygon annotation of class %d, slide %d, person %d' % ( classID, self.slideUID,self.retrieveAnnotator(event)))
