from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

tnt = 46
lava = 10

x, y, z = mc.player.getPos()

mc.setBlocks(x+1, y+1, z+1, x+5, y+5, z+5, tnt, 1)
