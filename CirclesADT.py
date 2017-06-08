class BannedZone:
    def __init__(self, x=0, z=0, r=20):
        self.bannedZoneX = [x]
        self.bannedZoneZ = [z]
        self.bannedZoneR = [r]
        if x is not None and z is not None and r is not None:
            self.counter = 1
        else:
            self.counter = 0

    def ban_zone(self, x, z, r=20):
        self.bannedZoneX += [x]
        self.bannedZoneZ += [z]
        self.bannedZoneR += [r]
        self.counter += 1
        return x, z, r

    def is_available(self, x, z):
        for i in range(self.counter):
            if (x - self.bannedZoneX[i]) ** 2 + (z - self.bannedZoneZ[i]) ** 2 <= self.bannedZoneR[i] ** 2:
                return False
        return True

    def unban_zone_with_index(self, index):
        if 0 <= index < self.counter:
            raise IndexError("index not found")
        x, z, r = self.bannedZoneX[index], self.bannedZoneZ[index], self.bannedZoneR[index]
        self.bannedZoneX.remove(x)
        self.bannedZoneZ.remove(z)
        self.bannedZoneR.remove(r)
        self.counter -= 1
        return x, z, r

    def unban_zone_with_values(self, x, z, r):
        if not (x in self.bannedZoneX and z in self.bannedZoneZ and r in self.bannedZoneR and
                self.bannedZoneX.index(x) == self.bannedZoneZ.index(z) == self.bannedZoneR.index(r)):
            raise IndexError("coordinates nor found")
        self.bannedZoneX.remove(x)
        self.bannedZoneZ.remove(z)
        self.bannedZoneR.remove(r)
        self.counter -= 1
        return x, z, r

    def x_values(self):
        return self.bannedZoneX

    def z_values(self):
        return self.bannedZoneZ

    def r_values(self):
        return self.bannedZoneR

    def all_values(self):
        values = []
        for i in range(self.counter):
            values.append((self.bannedZoneX, self.bannedZoneZ, self.bannedZoneR))
        return values

    def __str__(self):
        string = ""
        for i in range(self.counter):
            string += "Zone {0}: ({1}, {2}), radius = {3};"\
                .format(i+1, self.bannedZoneX[i], self.bannedZoneZ[i], self.bannedZoneR[i])
        return string

    def __iadd__(self, other):
        if type(other) == tuple or type(other) == list:
                self.ban_zone(other[0], other[1], other[2])
        else:
            for i in range(other.counter):
                x, z, r = other.all_values[i]
                self.ban_zone(x, z, r)

    def __add__(self, other):
        from copy import deepcopy as dc
        reserve = dc(self)
        for i in range(other.counter):
            x, z, r = other.all_values[i]
            reserve.ban_zone(x, z, r)
        return reserve

    def __getitem__(self, index):
        return self.all_values()[index]

    def __len__(self):
        return self.counter

    def __bool__(self):
        return bool(self.counter)

