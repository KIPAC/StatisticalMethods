class SolutionMissingError(Exception):
    def __init__(self):
        Exception.__init__(self, "This code/cell still needs to be completed!")

class ToBeCompleted:
    def __init__(self, tutorial_name):
        self._path = 'completions/' + tutorial_name + '/'
        try:
            f = open(self._path + 'files.txt')
            self._files = [s.strip('\n').strip() for s in f.readlines()]
            f.close()
            self._raise = False
            self._i = -1
        except:
            self._raise = True
    def __call__(self, index=None):
        if self._raise:
            raise SolutionMissingError
        else:
            if index is None:
                self._i += 1
            else:
                self._i = index
            #print('Executing completion', self._files[self._i])
            exec(open(self._path + self._files[self._i]).read(), globals())

TBC = ToBeCompleted(TutorialName) # TutorialName must be defined at global scope already

TBC_above = TBC # alias
