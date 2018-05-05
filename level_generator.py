import numpy as np
import os


class LevelGenerator(object):
    '''
    If this constructor is overridden, call it with super().__init__(dir, game) from the subclass.
    '''

    def __init__(self, dir, game):
        self.dir = dir
        if self.dir[-1] != "/":
            self.dir += "/"
        self.game = game.lower()
        
    def generate(self):
        '''
        :return: the id and path of the next level to be evaluated.
        '''
        raise NotImplementedError


class ParamGenerator(LevelGenerator):

    def __init__(self, dir, game, width=None, height=None):
        super().__init__(dir, game)
        self.c = 0
        self.width = width
        self.height = height
        self.script = os.path.dirname(os.path.realpath(__file__)) + '/lib/gvgai_generator/app.js'

    def generate(self, params=[], difficulty=None):
        name = self.game + "_" + str(self.c)
        if self.width is not None and self.height is not None:
            params = [self.width, self.height] + params
        if difficulty is not None:
            params = ["difficulty", difficulty] + params
        params = [str(param) for param in params]
        param_str = " ".join(params)
        file = self.dir + name + ".txt"
        os.system("node " + self.script + " " + self.game + " " + file + " " + param_str)
        self.c += 1
        path = os.path.abspath(file)
        return path

#gen = ParamGenerator("./levels/", "zelda", width=13, height=9)
#level = gen.generate()
#print(level)