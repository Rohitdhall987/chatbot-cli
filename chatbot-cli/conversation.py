class Conversation:
    def __init__(self):
        self.__convo = []

    def add(self, message: str):
        self.__convo.append(message)

    def getConvo(self):
        return self.__convo