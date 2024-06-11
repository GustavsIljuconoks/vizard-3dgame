import viz
import vizfx
import vizact

# Set basic settings
viz.go() #viz.FULLSCREEN
viz.MainView.setPosition(0, 5, 2)
viz.MainView.setEuler(0, 135, 180)
viz.setMultiSample(4)
viz.fov(60)
viz.mouse(viz.OFF)

gameScene = viz.add('resources/chessgame.gltf')
gameScene.enable(viz.LIGHTING)

# Reduce ambient light
vizfx.setAmbientColor([0.1]*3)

# Add a spot light
lamp = viz.addSpotLight(spread=30, pos=(0,4,0))
lamp.setEuler(0, 110, 160)  # Set the angles to point downwards
lamp.setPosition(0, 5, 1)  # Set the position above the table
lamp.setIntensity(1)
lamp.setSpotPenumbra(0.5)
lamp.color(viz.YELLOW)

# TODO: Create element spawner function
bishop = viz.addChild('resources/bishop.obj')
bishop.setPosition([0, 0, -0.05])

bishop.enable(viz.LIGHTING)
bishop.specular([1, 1, 1, 1])
bishop.shininess(20)

picked_object = None
def onPick():
    global picked_object
    picked_object = viz.pick()
    if picked_object == gameScene:
        picked_object = None  # Do not allow picking of gameScene

def mymouse(e):
    global picked_object
    if picked_object:
        _, current_y, _ = picked_object.getPosition()
        picked_object.setPosition([(e.x - 0.5) * 6, current_y, e.y * 4])

vizact.onmousedown(viz.MOUSEBUTTON_LEFT, onPick)
viz.callback(viz.MOUSE_MOVE_EVENT, mymouse)
