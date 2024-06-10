import viz
import vizact
import vizcam

# Set basic settings
viz.go() # viz.FULLSCREEN
viz.MainView.setPosition(0, 5, 2)
viz.MainView.setEuler(0, 135, 180)
viz.setMultiSample(4)
viz.fov(60)
viz.mouse(viz.OFF)

gameScene = viz.add('resources/chessgame.gltf')
# WASD movment
# tracker = vizcam.addWalkNavigate(moveScale=10.0)
# tracker.setPosition([0, 2, 1.5])
# viz.link(tracker,viz.MainView)
# viz.mouse.setVisible(False)

soccerball = viz.addChild('soccerball.osgb')
soccerball.setPosition([-0.5, 4, -1])

picked_object = None
def onPick():
    global picked_object
    picked_object = viz.pick()
    if picked_object == gameScene:
        picked_object = None  # Do not allow picking of gameScene

def mymouse(e):
    global picked_object
    if picked_object:
        picked_object.setPosition([(e.x - 0.5) * 6, e.y * 4, 5])

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, onPick)
viz.callback(viz.MOUSE_MOVE_EVENT, mymouse)
