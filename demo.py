import lumiversepython as L
import time

rig = L.Rig("/home/teacher/Lumiverse/PBridge.rig.json")
rig.init()

idx = 0
while(idx < 60):
	rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(1, 0, 0)
	rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(0, 0, 1)
	rig.updateOnce()
	time.sleep(0.2)
	idx = idx + 1

idx = 0
while(idx < 60):
        rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0.5, 0, 0)
        rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(0, 0, 0.5)
        rig.updateOnce()
        time.sleep(0.2)
        idx = idx + 1


