import pyglet
hp = 100
hp_max = hp
window = pyglet.window.Window(width=800, height=600)
mainhero_sprite = pyglet.image.load('SpriteMainHero.png')
mainhero_sprite = pyglet.sprite.Sprite(mainhero_sprite, x=0, y=0)
lava_sprite = pyglet.image.load('Lava.png')
label = pyglet.text.Label( 'HP: ' + (str(hp)) + ' Max HP: ' + (str(hp_max)),
                          font_name='Times New Roman',
                          font_size=11,
                          x=0, y=580)

batch = pyglet.graphics.Batch()
npc_sprites = [] 
npc_sprites.append(pyglet.sprite.Sprite(lava_sprite, x=200, y=200, batch=batch))

lava_is_dead = False

@window.event
def on_draw():
        window.clear()
        batch.draw()
        mainhero_sprite.draw()
        label.draw()
@window.event
def on_key_press(key, modifiers):

        if(key == pyglet.window.key.UP):
                mainhero_sprite.y += 10
                print(mainhero_sprite.y)

        if(key == pyglet.window.key.DOWN):
                mainhero_sprite.y -= 10
                print(mainhero_sprite.y)

        if(key == pyglet.window.key.RIGHT):
                mainhero_sprite.x += 10
                print(mainhero_sprite.x)

        if(key == pyglet.window.key.LEFT):
                mainhero_sprite.x -= 10
                print(mainhero_sprite.x)

def update(dt):
        if mainhero_sprite.y > 570:
                mainhero_sprite.y = 570
                #print("Collided!")
        if mainhero_sprite.y < 0:
                mainhero_sprite.y = 0
                #print("Collided!")
        if mainhero_sprite.x > 770:
                mainhero_sprite.x = 770
                #print("Collided!") 
        if mainhero_sprite.x < 0:
                mainhero_sprite.x = 0
                #print("Collided!")                      
pyglet.clock.schedule_interval(update, 0.01)

def update(dt):
        global lava_is_dead
        global hp
        global max_hp
        if mainhero_sprite.x < npc_sprites[0].x + npc_sprites[0].width and mainhero_sprite.x + mainhero_sprite.width > npc_sprites[0].x and mainhero_sprite.y < npc_sprites[0].y + npc_sprites[0].height and mainhero_sprite.y + mainhero_sprite.height > npc_sprites[0].y and lava_is_dead == False:
                npc_sprites[0].delete()
                hp -= 1
                label.text =  'HP: ' + (str(hp)) + ' Max HP: ' + (str(hp_max))
                lava_is_dead = True
pyglet.clock.schedule_interval(update, 0.01)


pyglet.app.run()