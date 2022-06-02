@namespace
class SpriteKind:
    Text = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
    """),
    on_overlap_tile2)

tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.set_background_color(9)
chicken = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 5 5 5 5 5 . . . . . . 
            . . . 5 5 5 5 5 5 5 5 5 5 4 4 4 
            . . . . 5 5 5 5 5 5 f 5 5 5 5 4 
            . . . 5 5 5 5 5 5 5 5 5 5 5 4 4 
            . . . . 5 5 5 5 5 5 5 5 5 4 2 2 
            . . . 5 5 5 5 5 5 5 5 5 5 2 2 . 
            . . . . . 5 5 5 5 5 5 5 . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
chicken.set_position(20, 40)

def on_forever():
    chicken.set_velocity(0, chicken.vy + 5)
    scene.camera_follow_sprite(chicken)
    chicken.set_velocity(45, chicken.vy)
forever(on_forever)

def on_forever2():
    
    def on_overlap_tile3(sprite3, location3):
        pass
    scene.on_overlap_tile(SpriteKind.player, img("""
        
    """), on_overlap_tile3)
    
    if controller.A.is_pressed():
        chicken.set_velocity(0, chicken.vy - 200)
        pause(500)
        chicken.set_stay_in_screen(True)
        chicken.start_effect(effects.fire)
forever(on_forever2)
