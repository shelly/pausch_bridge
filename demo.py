import lumiversepython as L
import time

rig = L.Rig("/home/teacher/Lumiverse/PBridge.rig.json")
rig.init()

idx = 0
sent  = "i am having a bad day. life sucks."
sent2 = "cheer up! everything will be okay."

sent = sent + ((60 - len(sent)) * " ")
sent2 = sent2 + ((60 - len(sent2)) * " ")
print ("sent is " + str(len(sent)) + ", sent2 is " + str(len(sent2)))

while(idx < 60):
	if (idx < len(sent) and sent[idx] != " "):
		rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0.5, 0, 0)
		rig.updateOnce()
       		time.sleep(0.1)
#	if (sent2[idx] != " "):
 #               rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 1)
#		rig.updateOnce()
 #       	time.sleep(0.2)
	# rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(0, 1, 0)
	# rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0, 0, 0)
	idx = idx + 1

idx = 0
while(idx < 60):
  #      rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0.5, 0, 0)
	if (idx < len(sent2) and sent2[idx] != " "):
        	rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 1)
        	rig.updateOnce()
        	time.sleep(0.2)
        # rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0, 0, 0)
        idx = idx + 1
time.sleep(0.5)

idx = 0
while (idx < 60):
	rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0, 0, 0)
	rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 0)
#	rig.select("$panel=" + str(idx) + "]").setRGBRaw(0, 0, 0)
	idx = idx + 1
#rig.updateOnce()
time.sleep(0.3)

idx = 0
while (idx < 60):
	if (len(sent) + len(sent2) < 60):
		print "HERE"
		idx2 = len(sent)
		while (idx2 < 60-len(sent2)):
			rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
        	        rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
	else:
		if (sent[idx] == " " and sent2[59-idx] == " "):
			rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
	        	rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
	#	rig.select("$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
	idx = idx + 1

#rig.updateOnce()
time.sleep(0.2)
