from twisted.words.xish import domish
from wokkel.xmppim import MessageProtocol, AvailablePresence
from todo import ToDo

class EchoBotProtocol(MessageProtocol):
    def connectionMade(self):
        print "Connected!"

        # send initial presence
        self.send(AvailablePresence())

    def connectionLost(self, reason):
        print "Disconnected!"

    def onMessage(self, msg):
        print msg.body
        if msg["type"] == 'chat' and hasattr(msg, "body"):
            answer = ""
            if msg.body is not None:
                todo = ToDo(str(msg.body))
                answer = todo.execute()
                reply = domish.Element((None, "message"))
                reply["to"] = "samet2@gmail.com"
                reply["type"] = 'chat'
                reply.addElement("body", content=answer)

            self.send(reply)
