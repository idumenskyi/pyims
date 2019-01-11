from skpy import Skype
sk = Skype("YOUR SKYPE USERNAME", "YOU SKYPE PASSWORD") # connect to Skype
ch = sk.contacts["SKYPE USERNAME FOR CONVERSATION"].chat # 1-to-1 conversation
mess = ch.sendMsg("HI TEST")
rms = ch.getMsgs()
print(rms)
print(rms[1].content)
