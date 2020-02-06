
import random as rand
import vectors_misc as vm


class Particle:

    rand.seed()

    def __init__(self, dbounds):
        self.d = len(dbounds)
        self.pos = []
        for d in dbounds:
            self.pos.append(d[0] + rand.random() * (d[1] - d[0]))
        self.v = [0] * self.d
        self.speed = 0
        self.best = self.pos.copy()
        self.best_fit = 0

    def update_v(self, gbest, k1, k2, k3):
        v1 = vm.vscale(self.v, k1)
        v2 = vm.vscale(vm.vsub(self.best, self.pos), k2)
        v3 = vm.vscale(vm.vsub(gbest, self.pos), k3)
        self.v = vm.vadd(vm.vadd(v1, v2), v3)

        # print("inert: {}, s_best: {}, g_best: {}, v: {}".format(v1, v2, v3, self.v))

    def update_pos(self, dbounds):
        self.pos = vm.vadd(self.pos, self.v)
        for i in range(self.d):
            if self.pos[i] < dbounds[i][0]:
                self.pos[i] = dbounds[i][0]
            elif self.pos[i] > dbounds[i][1]:
                self.pos[i] = dbounds[i][1]
