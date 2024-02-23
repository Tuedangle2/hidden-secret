@namespace
class SpriteKind:
    chest1 = SpriteKind.create()
    emty = SpriteKind.create()
    chest2 = SpriteKind.create()
    housekeeper1_1 = SpriteKind.create()
    tree = SpriteKind.create()

def on_up_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f f 2 f e f . . 
                        . . f f f 2 f e e 2 2 f f f . . 
                        . . f e 2 f f e e 2 f e e f . . 
                        . f f e f f e e e f e e e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . . e f f f f f f f f 4 e . . 
                        . . . 4 f 2 2 2 2 2 e d d 4 . . 
                        . . . e f f f f f f e e 4 . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e f 2 f f f 2 f 2 e f . . 
                        . . f f f 2 2 e e f 2 f f f . . 
                        . . f e e f 2 e e f f 2 e f . . 
                        . f f e e e f e e e f f e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f e . . . 
                        . . 4 d d e 2 2 2 2 2 f 4 . . . 
                        . . . 4 e e f f f f f f e . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        100,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 2 2 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """),
            img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e d d 4 . . . . 
                        . . . f 2 2 2 2 e d d e . . . . 
                        . . f f 5 5 4 4 f e e f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_on_overlap(sprite, otherSprite):
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    adventure.add_to_textlog("Do you want to open the chest?")
    adventure.add_to_textlog("Press A to Open")
    adventure.add_to_textlog("Press B to Back")
    
    def on_pause_until():
        pass
    pause_until(on_pause_until)
    
    if controller.A.is_pressed():
        adventure.clear_text_log()
        adventure.add_image_to_text_log(img("""
            .........................fffffff...
                        ................ffffffbbffddddddff.
                        ...............ffdddbbffddddffdddf.
                        .............ffdddbbbffddddffddddf.
                        ............ffdddbbffdddddfdddddef.
                        ..........ffdddbbbffddddffdddffeff.
                        .........ffdddbbffdddddfddddfeeff..
                        ........fdddbbffdddddfffddfeeef....
                        ......ffdddbffdddddfdfdddfeeff.....
                        .....ffdddbfbbffddfdfddfeefff......
                        ....fddddbfbfffffddddffeeff........
                        ...fdddddfbbfbcfcfddfdefff.........
                        .ffddddbbfbbfccfcfddeefff..........
                        ffddccbbbfbbfffccfeeeff............
                        fffcffccbfbbbbbccfeeff.............
                        .fcccffcccffccccffef...............
                        ..fff...fffffffffff................
                        ...................................
                        ...................................
        """))
        adventure.add_to_textlog("You found an old piece of paper")
        Chest2.set_kind(SpriteKind.emty)
        Chest2.set_image(img("""
            . b b b b b b b b b b b b b b . 
                        b e 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
                        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                        b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                        b b b b b b b d d b b b b b b b 
                        . b b b b b b c c b b b b b b . 
                        b c c c c c b c c b c c c c c b 
                        b c c c c c c b b c c c c c c b 
                        b c c c c c c c c c c c c c c b 
                        b c c c c c c c c c c c c c c b 
                        b b b b b b b b b b b b b b b b 
                        b e e e e e e e e e e e e e e b 
                        b e e e e e e e e e e e e e e b 
                        b c e e e e e e e e e e e e c b 
                        b b b b b b b b b b b b b b b b 
                        . b b . . . . . . . . . . b b .
        """))
        adventure.clear_text_log()
        adventure.add_image_to_text_log(img("""
            .........................fffffff...
                        ................ffffffbbffddddddff.
                        ...............ffdddbbffddddffdddf.
                        .............ffdddbbbffddddffddddf.
                        ............ffdddbbffdddddfdddddef.
                        ..........ffdddbbbffddddffdddffeff.
                        .........ffdddbbffdddddfddddfeeff..
                        ........fdddbbffdddddfffddfeeef....
                        ......ffdddbffdddddfdfdddfeeff.....
                        .....ffdddbfbbffddfdfddfeefff......
                        ....fddddbfbfffffddddffeeff........
                        ...fdddddfbbfbcfcfddfdefff.........
                        .ffddddbbfbbfccfcfddeefff..........
                        ffddccbbbfbbfffccfeeeff............
                        fffcffccbfbbbbbccfeeff.............
                        .fcccffcccffccccffef...............
                        ..fff...fffffffffff................
                        ...................................
                        ...................................
        """))
        adventure.add_to_textlog("Do you want to read it?")
        adventure.add_to_textlog("")
        adventure.add_to_textlog("Press A to Read")
        adventure.add_to_textlog("Press B to Back")
        
        def on_pause_until2():
            pass
        pause_until(on_pause_until2)
        
        if controller.A.is_pressed():
            adventure.clear_text_log()
            adventure.add_to_textlog("People are gradually becoming afraid of their dreams, and that is the power of \"it\".")
            pause(10000)
            adventure.clear_text_log()
            tiles.set_current_tilemap(tilemap("""
                level1
            """))
        else:
            adventure.clear_text_log()
            tiles.set_current_tilemap(tilemap("""
                level1
            """))
    else:
        adventure.clear_text_log()
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
sprites.on_overlap(SpriteKind.player, SpriteKind.chest2, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global key1
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    adventure.add_to_textlog("Do you want to open the chest?")
    adventure.add_to_textlog("Press A to Open")
    adventure.add_to_textlog("Press B to Back")
    
    def on_pause_until3():
        pass
    pause_until(on_pause_until3)
    
    if controller.A.is_pressed():
        adventure.clear_text_log()
        key1 += 1
        adventure.add_image_to_text_log(img("""
            ....................
                        ....................
                        ....................
                        ....................
                        ....................
                        ....................
                        ..............fff...
                        .............f555f..
                        .ffffffffffff5fff5f.
                        f5555555555555f1f5f.
                        .ffffffffffff5fff5f.
                        ...f555f.....f555f..
                        ..f55555f.....fff...
                        ...f555f............
                        ..f5fff5f...........
                        ..f5f.f5f...........
                        ...ff.ff............
                        ....................
                        ....................
                        ....................
        """))
        adventure.add_to_textlog("You found a key")
        chest12.set_kind(SpriteKind.emty)
        chest12.set_image(img("""
            . b b b b b b b b b b b b b b . 
                        b e 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
                        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                        b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                        b b b b b b b d d b b b b b b b 
                        . b b b b b b c c b b b b b b . 
                        b c c c c c b c c b c c c c c b 
                        b c c c c c c b b c c c c c c b 
                        b c c c c c c c c c c c c c c b 
                        b c c c c c c c c c c c c c c b 
                        b b b b b b b b b b b b b b b b 
                        b e e e e e e e e e e e e e e b 
                        b e e e e e e e e e e e e e e b 
                        b c e e e e e e e e e e e e c b 
                        b b b b b b b b b b b b b b b b 
                        . b b . . . . . . . . . . b b .
        """))
        adventure.clear_text_log()
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
    else:
        adventure.clear_text_log()
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
sprites.on_overlap(SpriteKind.player, SpriteKind.chest1, on_on_overlap2)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e e e d d d f . . . 
                        . . . . . f 4 d d e 4 e f . . . 
                        . . . . . f e d d e 2 2 f . . . 
                        . . . . f f f e e f 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . 4 d d e 4 4 4 e f . . . 
                        . . . . e d d e 2 2 2 2 f . . . 
                        . . . . f e e f 4 4 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def forest():
    global tree1, tree2, tree3, tree4, tree5, tree11, tree12, tree13, tree14, tree15, tree6, tree7, tree8, tree9, tree10
    tree1 = sprites.create(img("""
            ........................
                    ...........ff..........8
                    ..........f88f........86
                    .........ff88ff......886
                    .........f8888f......866
                    ........f888888f....8666
                    ......ff88888888ff886666
                    .....f888888888888666666
                    .....ff88888888888866666
                    .....f888888888888666666
                    ....f88ff88888ff86688666
                    ....ffff88fff88f88886688
                    .....f8f8ff8ff8f88686886
                    ....f88fff88ffff86688866
                    ....f8ffff8fffff86888868
                    ....fff88ffffff888866888
                    ....f888ffff8fff86668888
                    ...f888ff8f88f8866688686
                    ..f8888888888f8666666666
                    .f88f8888888886686666666
                    .fff88888888888866666666
                    .ff888888888888666666666
                    ..ff88f888f88f8866866686
                    ..f8ff88fff88f8688668886
                    .f88ff8ff8f8f86688688686
                    f88ff8ff88ff866886886688
                    ffff88f88fff888866866888
                    .ffffffffffff88888888888
                    .ff888ff88ff888666886688
                    .f888ff888ff886668866688
                    f888888888f8866666666686
                    fff888f88888888666866666
                    ..ffff88f888888888668666
                    .....f8ff88f888ff8688668
                    ......fff8fff88fff888688
                    .........ffeeff......88e
                    .........feeeef......fee
                    .........feeeef......fee
                    ........feeefeef....feee
                    ........fefeffef....fefe
        """),
        SpriteKind.tree)
    tree2 = sprites.create(img("""
            ........................
                    8..........ff..........8
                    68........f88f........86
                    688......ff88ff......886
                    668......f8888f......866
                    6668....f888888f....8666
                    666688ff88888888ff886666
                    666666888888888888666666
                    666668888888888888866666
                    666666888888888888666666
                    66888668f88888ff86688666
                    8668688888fff88f88886688
                    8868668f8ff8ff8f88686886
                    8888868fff88ffff86688866
                    88888888ff8fffff86888868
                    888668888ffffff888866888
                    68886668ffff8fff86668888
                    6868866688f88f8866688686
                    6866666688888f8666666666
                    666666666888886686666666
                    666666668688888866666666
                    666666666888888666666666
                    6866668666888f8866866686
                    6886866886688f8688668886
                    866888688888f86688688686
                    8866888868ff866886886688
                    88868688668f888866866888
                    88888668868ff88888888888
                    68868868688f888666886688
                    668666666688886668866688
                    666666666668866666666686
                    666668666888888666866666
                    666666888888888888668666
                    6668868ff88f888ff8688668
                    8668888ff8fff88fff888688
                    e88......ffeeff......88e
                    eef......feeeef......fee
                    eef......feeeef......fee
                    feef....feeefeef....feee
                    ffef....fefeffef....fefe
        """),
        SpriteKind.tree)
    tree3 = sprites.create(img("""
            ........................
                    8..........ff...........
                    68........f88f..........
                    688......ff88ff.........
                    668......f8888f.........
                    6668....f888888f........
                    666688ff88888888ff......
                    666666888888888888f.....
                    66666888888888888ff.....
                    666666888888888888f.....
                    66888668f88888fff88f....
                    8668688888fff88f8fff....
                    8868668f8ff8ff8f88f.....
                    8888868fff88fffff8f.....
                    88888888ff8fffffffff....
                    888668888ffffff88fff....
                    68886668ffff8fff888f....
                    6868866688f88f8ff888f...
                    6866666688888f888888f...
                    666666666888888888888f..
                    66666666868888888888f8f.
                    666666666888888888888ff.
                    6866668666888f8888f888f.
                    6886866886688ff8f88ff88f
                    866888688888f88fff8fffff
                    8866888868ffff88ffff8f..
                    88868688668ffff8f8ff88f.
                    88888668868ffffff88ff8f.
                    68868868688f8ff8ff8f8ff.
                    66866666668888f8888888ff
                    66666666666888888888888f
                    66666866688888888f888ff.
                    666666888888888888ffff..
                    6668868ff88f888ff8f.....
                    8668888ff8fff88ffff.....
                    e88......ffeeff.........
                    eef......feeeef.........
                    eef......feeeef.........
                    feef....feeefeef........
                    ffef....fefeffef........
        """),
        SpriteKind.tree)
    tree4 = sprites.create(img("""
            ........................
                    ...........88..........f
                    ..........8668........f8
                    .........886688......ff8
                    .........866668......f88
                    ........86666668....f888
                    ......886666666688ff8888
                    .....8666666666666888888
                    .....8866666666668888888
                    .....8666666666666888888
                    ....8668866666888668f888
                    ....888866888668688888ff
                    .....86868868868668f8ff8
                    ....866888668888868fff88
                    ....8688886888888888ff8f
                    ....88866888888668888fff
                    ....8666888868886668ffff
                    ...8666886866868866688f8
                    ..8666666666686666668888
                    .86686666666666666666888
                    .88866666666666666668688
                    .88666666666666666666888
                    ..8866866686686666866688
                    ..8688668886688686688668
                    .86688688686866888688888
                    8668868866888866888868ff
                    88886686688888868688668f
                    .8888888888888888668868f
                    .8866688668868868868688f
                    .86668866688668666666688
                    866666666686666666666668
                    888666866666666668666888
                    ..8888668666666666888888
                    .....86886686668868ff88f
                    ......8886888668888ff8ff
                    .........88ee88......ffe
                    .........feeeef......fee
                    .........feeeef......fee
                    ........feeefeef....feee
                    ........fefeffef....fefe
        """),
        SpriteKind.tree)
    tree5 = sprites.create(img("""
            ........................
                    f..........88...........
                    8f........8668..........
                    8ff......886688.........
                    88f......866668.........
                    888f....86666668........
                    8888ff886666666688......
                    8888886666666666668.....
                    8888888666666666688.....
                    8888886666666666668.....
                    88ff8668866666888668....
                    f88f8888668886686888....
                    ff8f886868868868668.....
                    ffff866888668888868.....
                    ffff8688886888888888....
                    fff88886688888866888....
                    8fff8666888868886668....
                    8f8866688686686886668...
                    8f8666666666686666668...
                    8866866666666666666668..
                    88886666666666666666868.
                    88866666666666666666688.
                    8f886686668668666686668.
                    8f8688668886688686688668
                    f86688688686866888688888
                    8668868866888866888868..
                    88886686688888868688668.
                    f8888888888888888668868.
                    88866688668868868868688.
                    886668866688668666666688
                    866666666686666666666668
                    88866686666666666866688.
                    8888886686666666668888..
                    888ff86886686668868.....
                    f88fff8886888668888.....
                    eff......88ee88.........
                    eef......feeeef.........
                    eef......feeeef.........
                    feef....feeefeef........
                    ffef....fefeffef........
        """),
        SpriteKind.tree)
    tree11 = sprites.create(img("""
            ........................
                    ...........ff..........8
                    ..........f88f........86
                    .........ff88ff......886
                    .........f8888f......866
                    ........f888888f....8666
                    ......ff88888888ff886666
                    .....f888888888888666666
                    .....ff88888888888866666
                    .....f888888888888666666
                    ....f88ff88888ff86688666
                    ....ffff88fff88f88886688
                    .....f8f8ff8ff8f88686886
                    ....f88fff88ffff86688866
                    ....f8ffff8fffff86888868
                    ....fff88ffffff888866888
                    ....f888ffff8fff86668888
                    ...f888ff8f88f8866688686
                    ..f8888888888f8666666666
                    .f88f8888888886686666666
                    .fff88888888888866666666
                    .ff888888888888666666666
                    ..ff88f888f88f8866866686
                    ..f8ff88fff88f8688668886
                    .f88ff8ff8f8f86688688686
                    f88ff8ff88ff866886886688
                    ffff88f88fff888866866888
                    .ffffffffffff88888888888
                    .ff888ff88ff888666886688
                    .f888ff888ff886668866688
                    f888888888f8866666666686
                    fff888f88888888666866666
                    ..ffff88f888888888668666
                    .....f8ff88f888ff8688668
                    ......fff8fff88fff888688
                    .........ffeeff......88e
                    .........feeeef......fee
                    .........feeeef......fee
                    ........feeefeef....feee
                    ........fefeffef....fefe
        """),
        SpriteKind.tree)
    tree12 = sprites.create(img("""
            ........................
                    8..........ff..........8
                    68........f88f........86
                    688......ff88ff......886
                    668......f8888f......866
                    6668....f888888f....8666
                    666688ff88888888ff886666
                    666666888888888888666666
                    666668888888888888866666
                    666666888888888888666666
                    66888668f88888ff86688666
                    8668688888fff88f88886688
                    8868668f8ff8ff8f88686886
                    8888868fff88ffff86688866
                    88888888ff8fffff86888868
                    888668888ffffff888866888
                    68886668ffff8fff86668888
                    6868866688f88f8866688686
                    6866666688888f8666666666
                    666666666888886686666666
                    666666668688888866666666
                    666666666888888666666666
                    6866668666888f8866866686
                    6886866886688f8688668886
                    866888688888f86688688686
                    8866888868ff866886886688
                    88868688668f888866866888
                    88888668868ff88888888888
                    68868868688f888666886688
                    668666666688886668866688
                    666666666668866666666686
                    666668666888888666866666
                    666666888888888888668666
                    6668868ff88f888ff8688668
                    8668888ff8fff88fff888688
                    e88......ffeeff......88e
                    eef......feeeef......fee
                    eef......feeeef......fee
                    feef....feeefeef....feee
                    ffef....fefeffef....fefe
        """),
        SpriteKind.tree)
    tree13 = sprites.create(img("""
            ........................
                    8..........ff...........
                    68........f88f..........
                    688......ff88ff.........
                    668......f8888f.........
                    6668....f888888f........
                    666688ff88888888ff......
                    666666888888888888f.....
                    66666888888888888ff.....
                    666666888888888888f.....
                    66888668f88888fff88f....
                    8668688888fff88f8fff....
                    8868668f8ff8ff8f88f.....
                    8888868fff88fffff8f.....
                    88888888ff8fffffffff....
                    888668888ffffff88fff....
                    68886668ffff8fff888f....
                    6868866688f88f8ff888f...
                    6866666688888f888888f...
                    666666666888888888888f..
                    66666666868888888888f8f.
                    666666666888888888888ff.
                    6866668666888f8888f888f.
                    6886866886688ff8f88ff88f
                    866888688888f88fff8fffff
                    8866888868ffff88ffff8f..
                    88868688668ffff8f8ff88f.
                    88888668868ffffff88ff8f.
                    68868868688f8ff8ff8f8ff.
                    66866666668888f8888888ff
                    66666666666888888888888f
                    66666866688888888f888ff.
                    666666888888888888ffff..
                    6668868ff88f888ff8f.....
                    8668888ff8fff88ffff.....
                    e88......ffeeff.........
                    eef......feeeef.........
                    eef......feeeef.........
                    feef....feeefeef........
                    ffef....fefeffef........
        """),
        SpriteKind.tree)
    tree14 = sprites.create(img("""
            ........................
                    ...........88..........f
                    ..........8668........f8
                    .........886688......ff8
                    .........866668......f88
                    ........86666668....f888
                    ......886666666688ff8888
                    .....8666666666666888888
                    .....8866666666668888888
                    .....8666666666666888888
                    ....8668866666888668f888
                    ....888866888668688888ff
                    .....86868868868668f8ff8
                    ....866888668888868fff88
                    ....8688886888888888ff8f
                    ....88866888888668888fff
                    ....8666888868886668ffff
                    ...8666886866868866688f8
                    ..8666666666686666668888
                    .86686666666666666666888
                    .88866666666666666668688
                    .88666666666666666666888
                    ..8866866686686666866688
                    ..8688668886688686688668
                    .86688688686866888688888
                    8668868866888866888868ff
                    88886686688888868688668f
                    .8888888888888888668868f
                    .8866688668868868868688f
                    .86668866688668666666688
                    866666666686666666666668
                    888666866666666668666888
                    ..8888668666666666888888
                    .....86886686668868ff88f
                    ......8886888668888ff8ff
                    .........88ee88......ffe
                    .........feeeef......fee
                    .........feeeef......fee
                    ........feeefeef....feee
                    ........fefeffef....fefe
        """),
        SpriteKind.tree)
    tree15 = sprites.create(img("""
            ........................
                    f..........88...........
                    8f........8668..........
                    8ff......886688.........
                    88f......866668.........
                    888f....86666668........
                    8888ff886666666688......
                    8888886666666666668.....
                    8888888666666666688.....
                    8888886666666666668.....
                    88ff8668866666888668....
                    f88f8888668886686888....
                    ff8f886868868868668.....
                    ffff866888668888868.....
                    ffff8688886888888888....
                    fff88886688888866888....
                    8fff8666888868886668....
                    8f8866688686686886668...
                    8f8666666666686666668...
                    8866866666666666666668..
                    88886666666666666666868.
                    88866666666666666666688.
                    8f886686668668666686668.
                    8f8688668886688686688668
                    f86688688686866888688888
                    8668868866888866888868..
                    88886686688888868688668.
                    f8888888888888888668868.
                    88866688668868868868688.
                    886668866688668666666688
                    866666666686666666666668
                    88866686666666666866688.
                    8888886686666666668888..
                    888ff86886686668868.....
                    f88fff8886888668888.....
                    eff......88ee88.........
                    eef......feeeef.........
                    eef......feeeef.........
                    feef....feeefeef........
                    ffef....fefeffef........
        """),
        SpriteKind.tree)
    tree6 = sprites.create(img("""
            ........................
                    ...........ff..........8
                    ..........f88f........86
                    .........ff88ff......886
                    .........f8888f......866
                    ........f888888f....8666
                    ......ff88888888ff886666
                    .....f888888888888666666
                    .....ff88888888888866666
                    .....f888888888888666666
                    ....f88ff88888ff86688666
                    ....ffff88fff88f88886688
                    .....f8f8ff8ff8f88686886
                    ....f88fff88ffff86688866
                    ....f8ffff8fffff86888868
                    ....fff88ffffff888866888
                    ....f888ffff8fff86668888
                    ...f888ff8f88f8866688686
                    ..f8888888888f8666666666
                    .f88f8888888886686666666
                    .fff88888888888866666666
                    .ff888888888888666666666
                    ..ff88f888f88f8866866686
                    ..f8ff88fff88f8688668886
                    .f88ff8ff8f8f86688688686
                    f88ff8ff88ff866886886688
                    ffff88f88fff888866866888
                    .ffffffffffff88888888888
                    .ff888ff88ff888666886688
                    .f888ff888ff886668866688
                    f888888888f8866666666686
                    fff888f88888888666866666
                    ..ffff88f888888888668666
                    .....f8ff88f888ff8688668
                    ......fff8fff88fff888688
                    .........ffeeff......88e
                    .........feeeef......fee
                    .........feeeef......fee
                    ........feeefeef....feee
                    ........fefeffef....fefe
        """),
        SpriteKind.tree)
    tree7 = sprites.create(img("""
            ........................
                    8..........ff..........8
                    68........f88f........86
                    688......ff88ff......886
                    668......f8888f......866
                    6668....f888888f....8666
                    666688ff88888888ff886666
                    666666888888888888666666
                    666668888888888888866666
                    666666888888888888666666
                    66888668f88888ff86688666
                    8668688888fff88f88886688
                    8868668f8ff8ff8f88686886
                    8888868fff88ffff86688866
                    88888888ff8fffff86888868
                    888668888ffffff888866888
                    68886668ffff8fff86668888
                    6868866688f88f8866688686
                    6866666688888f8666666666
                    666666666888886686666666
                    666666668688888866666666
                    666666666888888666666666
                    6866668666888f8866866686
                    6886866886688f8688668886
                    866888688888f86688688686
                    8866888868ff866886886688
                    88868688668f888866866888
                    88888668868ff88888888888
                    68868868688f888666886688
                    668666666688886668866688
                    666666666668866666666686
                    666668666888888666866666
                    666666888888888888668666
                    6668868ff88f888ff8688668
                    8668888ff8fff88fff888688
                    e88......ffeeff......88e
                    eef......feeeef......fee
                    eef......feeeef......fee
                    feef....feeefeef....feee
                    ffef....fefeffef....fefe
        """),
        SpriteKind.tree)
    tree8 = sprites.create(img("""
            ........................
                    8..........ff...........
                    68........f88f..........
                    688......ff88ff.........
                    668......f8888f.........
                    6668....f888888f........
                    666688ff88888888ff......
                    666666888888888888f.....
                    66666888888888888ff.....
                    666666888888888888f.....
                    66888668f88888fff88f....
                    8668688888fff88f8fff....
                    8868668f8ff8ff8f88f.....
                    8888868fff88fffff8f.....
                    88888888ff8fffffffff....
                    888668888ffffff88fff....
                    68886668ffff8fff888f....
                    6868866688f88f8ff888f...
                    6866666688888f888888f...
                    666666666888888888888f..
                    66666666868888888888f8f.
                    666666666888888888888ff.
                    6866668666888f8888f888f.
                    6886866886688ff8f88ff88f
                    866888688888f88fff8fffff
                    8866888868ffff88ffff8f..
                    88868688668ffff8f8ff88f.
                    88888668868ffffff88ff8f.
                    68868868688f8ff8ff8f8ff.
                    66866666668888f8888888ff
                    66666666666888888888888f
                    66666866688888888f888ff.
                    666666888888888888ffff..
                    6668868ff88f888ff8f.....
                    8668888ff8fff88ffff.....
                    e88......ffeeff.........
                    eef......feeeef.........
                    eef......feeeef.........
                    feef....feeefeef........
                    ffef....fefeffef........
        """),
        SpriteKind.tree)
    tree9 = sprites.create(img("""
            ........................
                    ...........88..........f
                    ..........8668........f8
                    .........886688......ff8
                    .........866668......f88
                    ........86666668....f888
                    ......886666666688ff8888
                    .....8666666666666888888
                    .....8866666666668888888
                    .....8666666666666888888
                    ....8668866666888668f888
                    ....888866888668688888ff
                    .....86868868868668f8ff8
                    ....866888668888868fff88
                    ....8688886888888888ff8f
                    ....88866888888668888fff
                    ....8666888868886668ffff
                    ...8666886866868866688f8
                    ..8666666666686666668888
                    .86686666666666666666888
                    .88866666666666666668688
                    .88666666666666666666888
                    ..8866866686686666866688
                    ..8688668886688686688668
                    .86688688686866888688888
                    8668868866888866888868ff
                    88886686688888868688668f
                    .8888888888888888668868f
                    .8866688668868868868688f
                    .86668866688668666666688
                    866666666686666666666668
                    888666866666666668666888
                    ..8888668666666666888888
                    .....86886686668868ff88f
                    ......8886888668888ff8ff
                    .........88ee88......ffe
                    .........feeeef......fee
                    .........feeeef......fee
                    ........feeefeef....feee
                    ........fefeffef....fefe
        """),
        SpriteKind.tree)
    tree10 = sprites.create(img("""
            ........................
                    f..........88...........
                    8f........8668..........
                    8ff......886688.........
                    88f......866668.........
                    888f....86666668........
                    8888ff886666666688......
                    8888886666666666668.....
                    8888888666666666688.....
                    8888886666666666668.....
                    88ff8668866666888668....
                    f88f8888668886686888....
                    ff8f886868868868668.....
                    ffff866888668888868.....
                    ffff8688886888888888....
                    fff88886688888866888....
                    8fff8666888868886668....
                    8f8866688686686886668...
                    8f8666666666686666668...
                    8866866666666666666668..
                    88886666666666666666868.
                    88866666666666666666688.
                    8f886686668668666686668.
                    8f8688668886688686688668
                    f86688688686866888688888
                    8668868866888866888868..
                    88886686688888868688668.
                    f8888888888888888668868.
                    88866688668868868868688.
                    886668866688668666666688
                    866666666686666666666668
                    88866686666666666866688.
                    8888886686666666668888..
                    888ff86886686668868.....
                    f88fff8886888668888.....
                    eff......88ee88.........
                    eef......feeeef.........
                    eef......feeeef.........
                    feef....feeefeef........
                    ffef....fefeffef........
        """),
        SpriteKind.tree)
    tiles.place_on_tile(tree1, tiles.get_tile_location(64, 76))
    tiles.place_on_tile(tree2, tiles.get_tile_location(65, 76))
    tiles.place_on_tile(tree3, tiles.get_tile_location(66, 76))
    tiles.place_on_tile(tree4, tiles.get_tile_location(67, 76))
    tiles.place_on_tile(tree5, tiles.get_tile_location(68, 76))
    tiles.place_on_tile(tree6, tiles.get_tile_location(64, 77))
    tiles.place_on_tile(tree7, tiles.get_tile_location(65, 77))
    tiles.place_on_tile(tree8, tiles.get_tile_location(66, 77))
    tiles.place_on_tile(tree9, tiles.get_tile_location(67, 77))
    tiles.place_on_tile(tree10, tiles.get_tile_location(68, 77))
    tiles.place_on_tile(tree11, tiles.get_tile_location(64, 78))
    tiles.place_on_tile(tree12, tiles.get_tile_location(65, 78))
    tiles.place_on_tile(tree13, tiles.get_tile_location(66, 78))
    tiles.place_on_tile(tree14, tiles.get_tile_location(67, 78))
    tiles.place_on_tile(tree15, tiles.get_tile_location(68, 78))

def on_on_overlap3(sprite3, otherSprite3):
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    adventure.add_image_to_text_log(img("""
        .....................
                .....................
                .....................
                .....................
                ...........fffffffff.
                ...........ffffffffff
                .........fffddddddddf
                .........fffddddddddd
                .........fffddddddddd
                .........fffddfdddfdd
                .........dddddddddddd
                .........eedddddddddd
                ...........eeeeeeeee.
                ............ff121ff..
                ...........ffff2ffff.
                ...........fffffffff.
                ...........1fffffff1.
                ...........dfffffffd.
                ..............f.f....
                ..............f.f....
    """))
    adventure.add_to_textlog("Hello Misstress, a lot")
sprites.on_overlap(SpriteKind.player, SpriteKind.housekeeper1_1, on_on_overlap3)

def on_up_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . . f e 4 d d d d 4 e f e . . 
                        . . f e f 2 2 2 2 e d d 4 e . . 
                        . . e 4 f 2 2 2 2 e d d e . . . 
                        . . . . f 4 4 5 5 f e e . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 2 2 2 2 2 2 e f f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 2 2 2 2 f e f . . 
                        . . . e d d e 2 2 2 2 f 4 e . . 
                        . . . . e e f 5 5 4 4 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        100,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

tree10: Sprite = None
tree9: Sprite = None
tree8: Sprite = None
tree7: Sprite = None
tree6: Sprite = None
tree15: Sprite = None
tree14: Sprite = None
tree13: Sprite = None
tree12: Sprite = None
tree11: Sprite = None
tree5: Sprite = None
tree4: Sprite = None
tree3: Sprite = None
tree2: Sprite = None
tree1: Sprite = None
Chest2: Sprite = None
chest12: Sprite = None
mySprite: Sprite = None
info.set_life(5)
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
chest12 = sprites.create(img("""
        . . b b b b b b b b b b b b . . 
            . b e 4 4 4 4 4 4 4 4 4 4 e b . 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e e 4 4 4 4 4 4 4 4 4 4 e e b 
            b e e e e e e e e e e e e e e b 
            b e e e e e e e e e e e e e e b 
            b b b b b b b d d b b b b b b b 
            c b b b b b b c c b b b b b b c 
            c c c c c c b c c b c c c c c c 
            b e e e e e c b b c e e e e e b 
            b e e e e e e e e e e e e e e b 
            b c e e e e e e e e e e e e c b 
            b b b b b b b b b b b b b b b b 
            . b b . . . . . . . . . . b b .
    """),
    SpriteKind.chest1)
chest12.set_position(185, 1273)
key1 = 0
Chest2 = sprites.create(img("""
        . . b b b b b b b b b b b b . . 
            . b e 4 4 4 4 4 4 4 4 4 4 e b . 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e e 4 4 4 4 4 4 4 4 4 4 e e b 
            b e e e e e e e e e e e e e e b 
            b e e e e e e e e e e e e e e b 
            b b b b b b b d d b b b b b b b 
            c b b b b b b c c b b b b b b c 
            c c c c c c b c c b c c c c c c 
            b e e e e e c b b c e e e e e b 
            b e e e e e e e e e e e e e e b 
            b c e e e e e e e e e e e e c b 
            b b b b b b b b b b b b b b b b 
            . b b . . . . . . . . . . b b .
    """),
    SpriteKind.chest2)
tiles.place_on_tile(Chest2, tiles.get_tile_location(26, 78))
housekeeper = sprites.create(img("""
        .....................
            .....................
            .....................
            .....................
            ...........fffffffff.
            ...........ffffffffff
            .........fffddddddddf
            .........fffddddddddd
            .........fffddddddddd
            .........fffddfdddfdd
            .........dddddddddddd
            .........eedddddddddd
            ...........eeeeeeeee.
            ............ff121ff..
            ...........ffff2ffff.
            ...........fffffffff.
            ...........1fffffff1.
            ...........dfffffffd.
            ..............f.f....
            ..............f.f....
    """),
    SpriteKind.housekeeper1_1)
tiles.place_on_tile(housekeeper, tiles.get_tile_location(55, 22))
forest()