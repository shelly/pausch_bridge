import lumiversepython as L
import time

rig = L.Rig("/home/teacher/Lumiverse/PBridge.rig.json")
rig.init()

sent = ""
sent2 = ""
color = (0, 0, 0)
color2 = (0, 0, 0)

# loc: top or bot
def updateText(loc, text, c):
	if not (loc == "top" or loc == "bottom"):
		print "not valid loc"
		return

	if loc == "top":
		sent = text
		color = c
	else:
		sent2 = text
		color2 = c

	sent = text + ((60 - len(text)) * " ")
	sent2 = text2 + ((60 - len(text2)) * " ")
	print ("sent is " + str(len(sent)) + ", sent2 is " + str(len(sent2)))

	# play animation of text from gates
	idx = 0
	while(idx < 60):
		if (idx < len(sent) and sent[idx] != " "):
			rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0.5, 0, 0)
			rig.updateOnce()
	       		time.sleep(0.1)
		idx = idx + 1

	# play animation of text from purnell
	idx = 0
	while(idx < 60):
		if (idx < len(sent2) and sent2[idx] != " "):
	        	rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 1)
	        	rig.updateOnce()
	        	time.sleep(0.2)
	        idx = idx + 1
	time.sleep(0.5)

	# fade out
	idx = 5
	while(idx >= 0):
		if (idx < len(sent) and sent[idx] != " "):
			rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw((color[0] * idx * 0.2), (color[1] * idx * 0.2), (color[2] * idx * 0.2))
			rig.updateOnce()
	       	time.sleep(0.1)
        if (idx < len(sent2) and sent2[idx] != " "):
            rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw((color[0] * idx * 0.2), (color[1] * idx * 0.2), (color[2] * idx * 0.2))
            rig.updateOnce()
            time.sleep(0.1)
	    idx = idx - 1
	# time.sleep(0.5)

	# # turn everything off
	# idx = 0
	# while (idx < 60):
	# 	rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0, 0, 0)
	# 	rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 0)
	# 	idx = idx + 1
	# rig.updateOnce()
	# time.sleep(0.3)

	# turn space spots white
	idx = 0
	while (idx < 60):
		if (len(sent) + len(sent2) < 60):
			print "HERE"
			idx2 = len(sent)
			while (idx2 < 60 - len(sent2)):
				rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
	        	        rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
		else:
			if (sent[idx] == " " and sent2[59-idx] == " "):
				rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
		        	rig.select("$side=bot[$panel=" + str(idx) + "]").setRGBRaw(1, 1, 1)
		idx = idx + 1

	rig.updateOnce()
	time.sleep(0.2)
