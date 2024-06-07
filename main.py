import viz
import vizact

viz.go()

customObject = viz.add('resources/chessgame.gltf')
customObject.setPosition([0, 0, 5])

dir_light = viz.addDirectionalLight()
dir_light.direction(0, -1, 0)
dir_light.intensity(0.8)

head_light = viz.MainView.getHeadLight()
head_light.intensity(0.5)

point_lights = []
light_positions = [(-10, 5, -10), (-10, 5, 10), (10, 5, -10), (10, 5, 10)]

for pos in light_positions:
    point_light = viz.addPointLight()
    point_light.setPosition(pos[0], pos[1], pos[2])
    point_light.intensity(0.6)
    point_lights.append(point_light)
