from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create("172.16.8.104", 4711)

tnt = 46
lava = 10

x, y, z = mc.player.getPos()

mc.setBlocks(x+1, y+1, z+1, x+100, y+100, z+100, tnt)
