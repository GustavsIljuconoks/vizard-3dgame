import viz
import vizfx
import vizact

# Set basic settings
def setup_scene():
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

    return gameScene

# Define piece models
piece_models = {
    'pawn': 'resources/pawn.obj',
    'rook': 'resources/rook.obj',
    'knight': 'resources/knight.obj',
    'bishop': 'resources/bishop.obj',
    'queen': 'resources/queen.obj',
    'king': 'resources/king.obj'
}

# Function to create and position pieces
def create_piece(piece_type, position):
    piece = viz.addChild(piece_models[piece_type])
    piece.setPosition(position)
    piece.enable(viz.LIGHTING)
    piece.specular([1, 1, 1, 1])
    piece.shininess(20)
    return piece

# Populate the board
def populate_board(gameScene):
    pieces = []

    # Piece positions
    positions = [
        [0, 0, -0.05], [0.65, 0, -0.05],
        [1.45, 0, -0.05], [-0.045, 0, -0.05],
        [-0.01, 0, -0.05], [1.05, 0, -0.05],
        [0.22, 0, -0.05], [-0.2, 0, -0.05]
    ]

    # Add bishops
    bishop = create_piece('bishop', positions[0])
    bishop2 = create_piece('bishop', positions[1])
    pieces.extend([bishop, bishop2])

    # Add rooks
    rook = create_piece('rook', positions[2])
    rook2 = create_piece('rook', positions[3])
    pieces.extend([rook, rook2])

    # Add knights
    knight = create_piece('knight', positions[4])
    knight2 = create_piece('knight', positions[5])
    pieces.extend([knight, knight2])

    # Add king and queen
    king = create_piece('king', positions[6])
    queen = create_piece('queen', positions[7])
    pieces.extend([king, queen])

    # Add pawns
    for position in positions:
        pawn = create_piece('pawn', [position[0], position[1], position[2] - 0.35])
        pieces.append(pawn)

    picked_object = None

    def onPick():
        nonlocal picked_object
        picked_object = viz.pick()
        if picked_object == gameScene:
            picked_object = None  # Do not allow picking of gameScene

    def mymouse(e):
        nonlocal picked_object
        if picked_object:
            _, current_y, _ = picked_object.getPosition()
            picked_object.setPosition([(e.x - 0.5) * 6, current_y, e.y * 4])

    vizact.onmousedown(viz.MOUSEBUTTON_LEFT, onPick)
    viz.callback(viz.MOUSE_MOVE_EVENT, mymouse)

    return pieces

# Main function
def main():
    gameScene = setup_scene()
    populate_board(gameScene)

if __name__ == "__main__":
    main()
