import lumiversepython as L
import time

rig = L.Rig("/home/teacher/Lumiverse/PBridge.rig.json")
rig.init()

sent = ""
sent2 = ""

# loc: top or bot
def updateText(loc, text, color):
	if not (loc == "top" or loc == "bottom"):
		print "not valid loc"
		return

	if loc == "top":
		sent = text
	else:
		sent2 = text
		
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

	# turn everything off
	idx = 0
	while (idx < 60):
		rig.select("$side=top[$panel=" + str(idx) + "]").setRGBRaw(0, 0, 0)
		rig.select("$side=bot[$panel=" + str(60-idx) + "]").setRGBRaw(0, 0, 0)
		idx = idx + 1
	rig.updateOnce()
	time.sleep(0.3)

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
