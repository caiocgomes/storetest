from collections import namedtuple
from UserGeneration import sexSampler, educationSampler, incomeSampler, ageGroupSampler


incomeTranslate = {0: 'C', 1: 'B', 2: 'A'}
eduTranslate = {0: 'Ensino Medio', 1: 'Ensino Superior', 2: 'Pos Graduacao'}
ageTranslate = {0: '17 - 20', 1: '21 - 30', 2: '30 - 50', 3: '50+'}

class User(namedtuple('User', "userid sex education incomeGroup ageGroup")):

    _lastid = 0

    def __new__(cls):
        cls._lastid += 1
        sex = sexSampler()
        ageGroup = ageGroupSampler()
        education = educationSampler(ageGroup)
        incomeGroup = incomeSampler(ageGroup, education)
        return super(User, cls).__new__(cls, cls._lastid, sex, education, incomeGroup, ageGroup)

    def toDict(self):
        return {'usrSex': self.sex,
                'usrEdu': eduTranslate[self.education],
                'usrInc': incomeTranslate[self.incomeGroup],
                'usrAge': ageTranslate[self.ageGroup]}
