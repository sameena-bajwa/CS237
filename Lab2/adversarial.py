    self.badInserts = []
    self.badLookups = []

    def adversarialInserts(self):
        self.personalBF = [0]*self.numBits
        self.badInserts = []
        count = 0
        for i in range (16384):
            flag = True
            val = [0] * self.numHashFunctions
            for j in range (self.numHashFunctions):
                val[j] = self.hash.pairwiseHash_i(i, j)
                if self.personalBF[val[j]] != 0:
                    flag = False
            if flag:
                self.badInserts.append(val[j])
                for j in range (self.numHashFunctions):
                    count += 1
                    self.personalBF[val[j]] = 1
        for i in range(len(self.badInserts)):
            self.insert(self.badInserts[i])
        return self.badInserts

    def adversarialLookups(self):
        self.badLookups = []
        for i in range (16384):
            if i not in self.badInserts:
                if self.lookup(i):
                    self.badLookups.append(i)
        count = 0
        for i in range (len(self.badLookups)):
            if self.lookup(self.badLookups[i]):
                count += 1
        return count * 1.0 / len(self.badLookups)
