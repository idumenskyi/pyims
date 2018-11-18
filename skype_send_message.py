from skpy import Skype
sk = Skype("nexus12141", "2202414q") # connect to Skype
ch = sk.contacts["nexus12142"].chat # 1-to-1 conversation
mess = ch.sendMsg("HI TEST")
rms = ch.getMsgs()
print(rms)
print(rms[1].content)
