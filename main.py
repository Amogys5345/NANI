from random import choice,randint
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.health_bar import HealthBar

app = Ursina()


grass_texture = load_texture("Assets\Textures\Old Textures/Grass_Block.png")
stone_texture = load_texture("Assets\Textures\Old Textures/Stone_Block.png")
brick_texture = load_texture("Assets\Textures\Old Textures/Brick_Block.png")
dirt_texture = load_texture("Assets\Textures\Old Textures/Dirt_Block.png")
diamond_block = load_texture("Assets\Textures\Old Textures/diamond_block.png")
wood_texture = load_texture("Assets/Textures/Wood_Block.png")
sky_texture = load_texture("Assets/Textures/Skybox.png")
arm_texture = load_texture("Assets\Textures\Old Textures/Arm_Texture.png")
grass = load_texture("Assets\Textures\Old Textures/maxresdefault.png")
punch_sound = Audio("Assets/SFX/dictaphone.audio (3).mp3", loop=False, autoplay=False)
window.exit_button.visible = False
block_pick = 1
list_tex = [grass_texture,wood_texture,dirt_texture,brick_texture,stone_texture]


def update():
    global block_pick
    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()

    if held_keys["1"]: block_pick = 1
    if held_keys["2"]: block_pick = 2
    if held_keys["3"]: block_pick = 3
    if held_keys["4"]: block_pick = 4
    if held_keys["5"]: block_pick = 5
    if held_keys["6"]: block_pick = 6
    if held_keys["7"]: quit()



class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="Sphere",
            texture=sky_texture,
            scale=90,
            double_sided=True
        )



class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="Assets/Models/Arm",
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.6)
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=random.choice(list_tex) ):
        super().__init__(
            parent=scene,
            position=position,
            model="Assets/Models/Block",
            origin_y=0.7,
            texture=texture,
            color=color.color(0, 0, random.uniform(1, 0.9)),
            highlight_color=color.light_gray,
            scale=0.50017
        )


    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 5: voxel = Voxel(position=self.position + mouse.normal, texture=wood_texture)
                if block_pick == 6: voxel = Voxel(position=self.position + mouse.normal, texture=diamond_block)


            if key == "right mouse down":
                punch_sound.play()
                destroy(self)


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 2, z),texture=grass_texture)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 1, z),texture=dirt_texture)


voxel = Voxel(position=(randint(1,19), -2, randint(1,19)),texture=diamond_block)
voxel = Voxel(position=(randint(1,19), -2, randint(1,19)),texture=diamond_block)
voxel = Voxel(position=(randint(1,19), -2, randint(1,19)),texture=diamond_block)


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z),texture=dirt_texture)
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, -1, z),texture=stone_texture)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, -2, z),texture=stone_texture)

for z in range(20):
    for x in range(20):
            voxel = Voxel(position=(x, -3, z),texture=stone_texture)





player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()