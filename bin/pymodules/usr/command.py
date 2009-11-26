"""this is executed when you press '.' in the ogre window, the viewer main window.
used for quick testing of py commands."""

import rexviewer as r
import math

print "--- *** ---"

#print dir(r)

#some prim
idnum = 720011 #the cube most far away from the screen in Toni & Petri 's test sim
#idnum = 0
new_id = 9999999

#av ent
av_entid = 8880000

def rotate(e):
    o = e.orientation    
    newort = (o[0], o[1], o[2] + 0.5, o[3])
    print "Rotating to ort:", newort
    e.orientation = newort
    #assert e.orientation[2] > (oldz+0.9) #xxx some logic fail here?
    #print "TEST ORIENTATION SUCCEEDED", e.orientation[2], oldortz
    
def move(e):
    p = e.pos #.pos - the w.i.p. api has a shortcut now that instead of a placeable with loc,rot,scale it just gives loc now directly
    oldx = p[0] #p.x - Vector3 not wrapped (yet), just gives a tuple
    #p.x += 1 #change the x-coordinate
    newpos = (p[0] - 1, p[1], p[2])
    print "Moving to move to pos:", newpos
    e.pos = newpos

if 0:
    print "Testing taking a screenshot..."
    
    path = "pymodules/webserver/screenshot/"
    pic = "current.png"
    
    hmm = r.takeScreenshot(path, pic)
    
if 0:
    print "Testing event sending, camera for now..."#   , r.SwitchCameraState
    hmm = r.sendEvent(r.SwitchCameraState)
    print "test done?", hmm

if 0:
    print "Testing camera swap..."
    hmm = r.switchCameraState()
    #print hmm
    
if 0: #get entity
    #idnum = new_id
    print "Getting entity id", idnum,
    e = r.getEntity(idnum)
    print "got:", e
    #print dir(r)
    rotate(e)
    #move(e)

if 0: #test avatar tracking, works :)
    av_entid = 2628869553
    print "<:::",
    try:
        a = r.getEntity(av_entid)
    except:
        print "could find the avatar with the given id", av_entid
    else:
        print "Avatar pos:", a.pos,
        print ":::>"
        """
        perhaps some local script could track movement?
        make a sound of a nearby object of interest, 
        like when a pet or a friend moves?
        """
        
        if 0:
            #test what happens when we move the av
            #a.pos = a.pos[0] + 1, a.pos[1], a.pos[2]
            """crash, because of how network updates are coded in the internals: 
            XXX RexServerConnecion.cpp
            RexServerConnection::SendMultipleObjectUpdatePacket(std::vector<Scene::EntityPtr> entity_ptr_list)
            const Foundation::ComponentInterfacePtr &prim_component = entity_ptr_list[i]->GetComponent("EC_OpenSimPrim");
            (because avatars don't have the prim component"""
            
            #rotating the av
            rotate(a)

if 0: #push an event, input and/or chat
    #from eventsource import viewer
    #from modulemanager import m 
    import circuits_manager
    mm = circuits_manager.ComponentRunner.instance
    print mm
    
    #mm.INPUT_EVENT(r.MoveForwardPressed)
    
    #a chat message again now too
    mm.RexNetMsgChatFromSimulator("Bob", "- that's me, Bob.")
    
    #previous pyglet stuff, was an ncoming chat msg event
    #m.dispatch_event('on_chat', "input", "testing")
    #print viewer._event_stack

if 0: #create entity
    #not safe now:
    """
    New entity created:16:39:22 [Foundation] Error: Can't create entity with given i
d because it's already used: 9999999
Assertion failed: px != 0, file D:\k2\rex\viewer\trunk\external_libs\include\boo
st/shared_ptr.hpp, line 419
    """
    print "Testing entity creation"
    meshname = "axes.mesh"
    
    avatar = r.getEntity(r.getUserAvatarId())
    ent = r.createEntity(meshname)
    #print "New entity created:", ent, ent.pos
    ent.pos = avatar.pos
    ent.scale = 0.0, 0.0, 0.0
    #print "new pos", ent.pos, ent.scale

if 0: #placeable and text tests
    print "Testing..."
    e = r.getEntity(8880005)    

    #~ try:
        #~ e.pos = 1
    #~ except Exception, e:
        #~ print e
        
    #e.orientation = "well this ain't a quarternion."
    #e.scale = ("does", "this", "work")
    def test():
        print "this ain't a string..."
    
    e.text = "swoot"
    e.text = 1
    e.text = ("swoot", "ness")
    e.text = (1, 2)
    e.text = test
    
    e.pos = 1
    
    print e.text, e.pos, e.scale, e.orientation
    
if 0: #send chat
    r.sendChat("hello from new realXtend Naali!")
    #print "called sendchat ok"
    
if 0: #print test
    r.logInfo("this is a test print!")
    
if 0: #camera pitch
    dy = 0.1
    dp = 0
    #dp = -0.1
    #dp = 0.1
    r.setCameraYawPitch(dy, dp)
    print r.getCameraYawPitch()
        
if 0: #avatar set yaw (turn)
    a = -1.0
    print "setting avatar yaw with %f" % a
    r.setAvatarYaw(a)

if 0: #avatar rotation #XXX crashes when the avatar is not there! XXX
    x = 0
    y = 0 
    z = -1 #this is the actual rotation thingie
    w = 0
    print "rotating the avatar to", (x, y, z, w)    
    r.setAvatarRotation(x, y, z, w)
    
if 0: #create a new qt canvas
    try:
        c = r.c
    except: #initial run
        c = r.createCanvas()
        r.c = c
    else: #the canvas has already been created
        #import PythonQt
        #print globals()
        #print '=============='
        #print 'box' in globals()
        #print dir(PythonQt)
        #print box
        print "~~~"
        #print "test t:", test
        #print "canvas t:", __canvas__
    print c
    
if 0: #add a signal handler to the ui loaded above, i.e. create a slot and connect it
    r.c.label.text = "py-commanded"
    def changed(v):
        print "val changed to: %f" % v
    #print r.c.label.connect('clicked()', changed)
    print r.c.doubleSpinBox.connect('valueChanged(double)', changed)
    print r.c.children()
    print dir(r.c)
    
if 0: #for the box test ui created in code - works
    # define our own python method that appends the text from the line edit
    # to the text browser
    box = r.c
    def appendLine():
        box.browser.append(box.edit.text)
    box.button1.connect('clicked()', appendLine)
    box.edit.connect('returnPressed()', appendLine)
    
if 0: #python-ogre test - using the extension lib in the embedded context :o
    #import sys
    #sys.path.append('pymodules/ogre.zip')
    #didn't work for some reason yet - should .pyd s work from zips too?
    #apparently it should work: http://mail.python.org/pipermail/python-list/2008-March/653795.html
    
    #based on the info in http://www.ogre3d.org/addonforums/viewtopic.php?f=3&t=8743&hilit=embed
    import ogre.renderer.OGRE as ogre
    root = ogre.Root.getSingleton()
    #print dir(r)
    print root.isInitialised()
    rs = root.getRenderSystem()
    #rs.setAmbientLight(1, 1, 1)
    vp = rs._getViewport()
    #print vp
    bg = vp.getBackgroundColour()
    #only affects when not connected, when caelum is not there i figure
    vp.setBackgroundColour(ogre.ColourValue(0.1, 0.2, 0))
    
    cam = vp.getCamera()
    #print cam
    
    sm = root.getSceneManager("SceneManager")
    print sm
    
    def drawline():
        try:
            mcounter = r.mcounter
        except: #first execution
            print "first exec"
            mcounter = 1
        else:
            mcounter += 1
            #print "incremented manual object counter to", mcounter
        r.mcounter = mcounter
        print "Creating manual object index", mcounter
        mob =  sm.createManualObject("manual%d" % mcounter)
        mnode = sm.getRootSceneNode().createChildSceneNode("manual%d_node" % mcounter)
        
        try:
            mmaterial = r.mmaterial
        except: #first execution
            mmaterial = ogre.MaterialManager.getSingleton().create("manual1Material","debugger")
            mmaterial.setReceiveShadows(False)
            tech = mmaterial.getTechnique(0)
            tech.setLightingEnabled(True)
            pass0 = tech.getPass(0)
            pass0.setDiffuse(0, 0, 1, 0)
            pass0.setAmbient(0, 0, 1)
            pass0.setSelfIllumination(0, 0, 1)
            r.mmaterial = mmaterial
            print "created the manual material"
        else:
            pass
            #print "got the existing manual material"
            
        mob.begin("manual1Material", ogre.RenderOperation.OT_LINE_LIST)
        mob.position(40, 240, 55 - mcounter)
        mob.position(240, 10, 10 + mcounter)
        #etc 
        mob.end()
        mnode.attachObject(mob)
        
    drawline()

if 0:
    #print "Importing PythonQt..."
    import PythonQt
    #print dir(PythonQt)
    #print "Importing PythonQt.QtGui..."
    #import PythonQt.QtGui as gui
    #print dir(gui)
    import PythonQt.QtUiTools as uitools
    print dir(uitools.QUiLoader)
    #print dir(gui.QTreeWidgetItem)
    

if 0:
    from PythonQt.QtGui import *

    group = QGroupBox()
    box = QVBoxLayout(group)
    print dir(box)
    push1 =  QPushButton(group)
    box.addWidget(push1)
    push2 =  QPushButton(group)
    box.addWidget(push2)
    check =  QCheckBox(group)
    check.text = 'check me'
    group.title = 'my title'
    push1.text = 'press me'
    push2.text = 'press me2'
    box.addWidget(check)
    group.show()

if 0:
    box = r.c.widget
    def funk(item):
        print "got index...", item
        box.treeWidget.currentItem().setText(0, "doooood")
    r.c.widget.treeWidget.disconnect('activated(QModelIndex)', r.c.itemActivated)
    r.c.itemActivated = funk
    r.c.widget.treeWidget.connect('activated(QModelIndex)', funk)
    print type(r.c)

if 0:
    box = r.c.widget.treeWidget
    box.clear()
    
if 0: #populating the EditGui window
    from PythonQt.QtGui import *
    from PythonQt.QtCore import QPoint
    box = r.c.widget
    box.label.text = "hmm"

    children = []
    children.append(QTreeWidgetItem(box.treeWidget))
    children[0].setText(0, "swoot")
    children.append(QTreeWidgetItem(box.treeWidget))
    children.append(QTreeWidgetItem(box.treeWidget))
    children.append(QTreeWidgetItem(box.treeWidget))
    print len(children)
    #~ def test(item, idx):
        #~ print "worked...", item, idx
    #~ box.treeWidget.connect('itemActivated(QTreeWidgetItem)', test)
    #box.treeWidget.connect('itemActivated', test)
    #box.treeWidget.itemClicked.connect(box.treeWidget.itemClickedSetSelected)
    
    #~ pos = QPoint(0,1)
    #~ thingie5 = box.treeWidget.indexAt(pos)  
    #print box.treeWidget.findChild
    #index = box.treeWidget.currentIndex()
    #print box.treeWidget.activated(index), index
    #print dir(box.treeWidget)

if 0:
    box = r.c.widget
    #print box, dir(box.treeWidget)
    text = box.treeWidget.currentItem().text(0)
    print text
    print type(text), r.c.widgetList
    print r.c.widgetList[720010]

if 0: #QtUI::UICanvas::External ?! not here...
    from PythonQt.QtUiTools import QUiLoader
    from PythonQt.QtCore import QFile, QIODevice
    #print dir(quil)  
    #print dir(PythonQt.QtCore.QIODevice)
    loader = QUiLoader()
    canvas = r.createCanvas(0)
    
    file = QFile("pymodules/usr/editobject.ui")
    iodev = QIODevice(file)

    widget = loader.load(file)
    canvas.AddWidget(widget)
    canvas.Show()
    
if 0: #collada load testing
    import collada
    print collada.Collada
    try:
        pycollada_test
    except:
        import pycollada_test
    else:
        pycollada_test = reload(pycollada_test)

if 0: #canvas size edit
    box = r.c
    #print dir(box.widget.size)
    #print box.widget.size.width()#, box.widget.size.height
    #print type(box.canvas)
    #box.canvas.size.setHeight(600)#
    #box.canvas.adjustSize()
    width = box.widget.size.width()
    height = box.widget.size.height()
    print width, height
    box.canvas.resize(width, height)
    #print box.canvas.resize(380, 250)
    
if 0: #ogre cam test and vectors
    import ogre.renderer.OGRE as ogre
    root = ogre.Root.getSingleton()
    #print dir(r)
    print root.isInitialised()
    rs = root.getRenderSystem()
    
    vp = rs._getViewport()
    
    
    #~ print dir(ogre.Vector3)
    #~ vec = ogre.Vector3(5, 5, 5).normalisedCopy() 
    #~ print vec, type(vec)
    cam = vp.getCamera()
    
    #print dir(cam)
    #print cam.Orientation, cam.DerivedOrientation, cam.getOrientation()
    #~ print "\n"
    #~ print cam.getRight(), cam.getUp()

if 0:
    canvas = r.c.canvas
    for child in canvas.children():
        child.delete()
    canvas.close()
    #canvas.deleteLater()
    
if 0: #pygame window test
    try:
        r.pygame
    except AttributeError: #first run
        import pygame
        r.pygame = pygame
        s = pygame.display.set_mode((320, 200))
        print s,
        r.pygame_s =  s #screen
        print r.pygame_s
        
    else:
        s = r.pygame_s
    print s
    
    s.fill((64, 95, 73))
    pygame.display.flip()
    
    #works :)=======

if 0: #testing the removal of canvases
    canvas = r.c.canvas
    modu = r.getQtModule()
    #print dir(modu)
    bool = modu.RemoveCanvasFromControlBar(canvas)
    print bool
    
if 0:
    print "Testing..."
    e = r.getEntity(8880001)  
    print e
    start_x = e.pos[0]
    start_y = e.pos[1]
    start_z = e.pos[2]
    end_x = e.pos[0]
    end_y = e.pos[1]
    end_z = e.pos[2]
        
    r.sendObjectAddPacket(start_x, start_y, start_z, end_x, end_y, end_z)

if 0: 
    id = r.getUserAvatarId()
    ent = r.getEntity(id)
    print "User's avatar_id:", id
    print "Avatar's mesh_name:", ent.mesh
    ent.mesh = "cruncah1.mesh"
    
if 0:
    print r.getCameraUp()
    print r.getCameraRight()

if 0: #test changing the mesh asset a prim is using
    ent_id = 1659586053 #penkki, arkku was: 2461025163
    #print arkku_id, type(arkku_id)
    ent = r.getEntity(ent_id)
    print "Test entity:", ent
    print ent.mesh
    ent.mesh = 1 #should raise an exception
    ruukku = "681b1680-fab5-4203-83a7-c567571c6acf"
    penkki = "04d335b6-8f0c-480e-a941-33517bf438d8"
    ent.mesh = penkki #"35da6174-8743-4026-a83e-18b23984120d"
    print "new mesh set:", ent.mesh
    
    print "sending prim data update to server"
    r.sendRexPrimData(ent.id) #arkku
    print "..done", ent.mesh
    
if 0: #testing vector3/quat wrapping 
    #import PythonQt
    #print PythonQt.__dict__.has_key("Core::Vector3df")
    #Vector3 = PythonQt.__dict__["Core::Vector3df"]
    from PythonQt import *
    from editgui.conversions import *
    
    print "Creating Vectors:"
    vec = Vector3df(0, 0, 0)
    print "vec1 (%.1f, %.1f, %.1f)" % (vec.x(), vec.y(), vec.z())
    
    vec2 = Vector3df(1, 1, 1)
    print "vec2 (%.1f, %.1f, %.1f)" % (vec2.x(), vec2.y(), vec2.z())
    
    print "distance between the two", vec.getDistanceFrom(vec2)
    
    vec.setx(1.0)
    vec.sety(1.0)
    vec.setz(1.0)
    
    print "changed vec1 (%.1f, %.1f, %.1f)" % (vec.x(), vec.y(), vec.z())
    print "new distance between the two", vec.getDistanceFrom(vec2)
    
    vec.setx(4.0)
    vec.sety(4.0)
    vec.setz(4.0)
    print "changed vec1 (%.1f, %.1f, %.1f)" % (vec.x(), vec.y(), vec.z())
    print "another new distance between the two", vec.getDistanceFrom(vec2)
    
    print "Creating quats:"
    quat = Quaternion(0, 0, 0, 0)
    print "quat (%.4f, %.4f, %.4f, %.4f)" % (quat.x(), quat.y(), quat.z(), quat.w())
    
    quat.setx(2.0)
    quat.sety(2.0)
    quat.setz(3.0)
    quat.setw(2.0)
    print "changed quat (%.4f, %.4f, %.4f, %.4f)" % (quat.x(), quat.y(), quat.z(), quat.w())
    
    print "Quat to Euler:"
    x = 0.707
    y = 0
    z = 0
    w = 0.707
    quat = Quaternion(x, y, z, w)
    euls = Vector3df(0,0,0)
    quat.toEuler(euls)
    euls2 = quat_to_euler((x, y, z, w))
    print "eulers (%.1f, %.1f, %.1f)" % (math.degrees(euls.x()), math.degrees(euls.y()), math.degrees(euls.z()))
    print "eulers2", euls2
    
    print "Euler to Quat:"
    x = math.radians(0)
    y = math.radians(90)
    z = math.radians(0)
    
    euler = Vector3df(x, y, z)
    #~ quat_from_euler = Quaternion(euler)
    #~ print "quat from eulers (%.4f, %.4f, %.4f, %.4f)" % (quat_from_euler.x(), quat_from_euler.y(), quat_from_euler.z(), quat_from_euler.w())

    quat_from_euler = Quaternion(x, y, z)
    print "quat from eulers (%.4f, %.4f, %.4f, %.4f)" % (quat_from_euler.x(), quat_from_euler.y(), quat_from_euler.z(), quat_from_euler.w())
        
    from editgui.conversions import *
    euler = euler_to_quat((0, 90, 0))
    print "quat from eulers", euler
    
if 0:
    avatar = r.getEntity(r.getUserAvatarId())
    avatar.text = "Swoot"
    import PythonQt as qt
    ent = r.getEntity(1392229722)
    print ent.name, ent.pos, ent.scale, ent.orientation, ent.prim
    pos = qt.Vector3df(ent.pos[0], ent.pos[1], ent.pos[2])
    print pos, pos.x(), pos.y(), pos.z()
    ent.pos = pos
    
if 0: #property editor tests
    #print r.c
    #print r, dir(r)
    pe = r.getPropertyEditor()
    #print pe, pe.setObject, pe.show
    pe.setObject(r.c.widget)
    pe.show()
    
if 0: #getting args from outside to run tests automatically
    import os
    naaliargs = os.getenv('NAALIARGS')
    print naaliargs

if 0:
    #print r.c.widget.move_button, dir(r.c.widget.move_button)
    #r.c.canvas.Show()
    print r.c.widget.move_button.isChecked(), r.c.widget.rotate_button.isChecked(), r.c.widget.scale_button.isChecked()
    #print  dir(r.c.widget.move_button)
    r.c.widget.move_button.setChecked(False)
    
if 0:
    from editgui.vector3 import Vector3 as V3
    fov = r.getCameraFOV()
    rightvec = V3(r.getCameraRight())
    campos = V3(r.getCameraPosition())
    ent = r.getEntity(r.getUserAvatarId())
    entpos = V3(ent.pos)
    width, height = r.getScreenSize()
    
    x = 613
    y = 345
    normalized_width = 1/width
    normalized_height = 1/height
    
    #print x * normalized_width
    
    length = (campos-entpos).length
    worldwidth = (math.tan(fov/2)*length) * 2

    #print campos, entpos, length, fov, width, height
    
    ent1 = r.createEntity("cruncah.mesh")
    ent1.pos = pos.x, pos.y+worldwidth/2, pos.z
    ent2 = r.createEntity("cruncah.mesh")
    ent2.pos = pos.x, pos.y+worldwidth/2, pos.z
    #~ newpos = 
    #~ print newpos
    
    
if 0: #bounding box tests
    ent = r.getEntity(r.getUserAvatarId())
    from editgui.vector3 import Vector3 as V3
    bb = list(ent.boundingbox)
    min = V3(bb[0], bb[1], bb[2])
    max = V3(bb[3], bb[4], bb[5])
    height = abs(bb[4] - bb[1]) *1.2
    width = abs(bb[3] - bb[0]) *1.2
    depth = abs(bb[5] - bb[2]) *1.2
    print ent.pos, min, max, height, width, depth
    
    r.box = r.createEntity("Selection.mesh")
    r.box.pos = ent.pos
    
    r.box.scale = depth, width, height
    r.box.orientation = ent.orientation
    #~ min_ent = r.createEntity("cruncah1.mesh")
    #~ min_ent.scale = 0.3, 0.3, 0.3
    #~ min_ent.pos = pos[0] + min.x, pos[1] + min.y, pos[2] + min.z 
    
    #~ max_ent = r.createEntity("cruncah1.mesh")
    #~ max_ent.scale = 0.3, 0.3, 0.3
    #~ max_ent.pos = pos[0] + max.x, pos[1] + max.y, pos[2] + max.z
    
if 0: #login - for running tests automatically
    print "starting opensim login"
    #user, pwd, server = "Test User", "test", "localhost:9000"
    user, pwd, server = "d d", "d", "world.evocativi.com:8002"
    r.startLoginOpensim(user, pwd, server)
