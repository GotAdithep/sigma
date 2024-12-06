class Quest:
    def __init__(self, title="Builder", level=1, reward=0, job="Build School"):
        self.__title = title
        self.__level = level
        self.__reward = reward
        self.__job = job


    def get_title(self):
        return self.__title


    def get_level(self):
        return self.__level


    def get_reward(self):
        return self.__reward


    def get_job(self):
        return self.__job


    def __str__(self):
        return f'''[Quest "{self.__job}" for Level {self.__level} {self.__title}, $ {self.__reward}]'''


a = Quest('sigma',1,2,'jjj')
print(a)
b = Quest(level=1, reward=0)
print(b)
