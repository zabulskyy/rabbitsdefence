class Zones:
    """
    This class is created to allow quick access to coordinates
    In game there is possibility to spawn rabbits and you are not allowed to spawn them too close to eacch other
    That's why we need ADT to calculate if coordinates are allowed to spawn rabbits
    """
    def __init__(self, x=0, z=0, r=20):
        """
        coordinates (0,0) with radius 20 are default for tower where player is
        banned zone with index i has properties:
            x coord == bannedZoneX[i]
            z coord == bannedZoneZ[i]
            radius == bannedZoneR[i]
        :param x: coordinate x, int
        :param z: coordinate z, int
        :param r: radius of banned zone, int
        """
        self._bannedZoneX = [x]
        self._bannedZoneZ = [z]
        self._bannedZoneR = [r]
        if x is not None and z is not None and r is not None:
            self._counter = 1
        else:
            self._counter = 0

    def ban_zone(self, x, z, r):
        """
        every time rabbit is spawned we should ban it's coordinates for other rabbits
        :param x: int or list
        :param z: int or list
        :param r: int or list
        """
        self._bannedZoneX += list(x)
        self._bannedZoneZ += list(z)
        self._bannedZoneR += list(r)
        self._counter += 1

    def is_available(self, x, z):
        """
        check if spot is available
        :param x:
        :param z:
        :return: bool
        """
        for i in range(self._counter):
            if (x - self._bannedZoneX[i]) ** 2 + (z - self._bannedZoneZ[i]) ** 2 <= self._bannedZoneR[i] ** 2:
                return False
        return True

    def unban_zone_with_index(self, index):
        """
        remove zone from banned with index
        :param index: int
        """
        if not (0 <= index < self._counter - 1):
            raise IndexError("index not found")
        x, z, r = self._bannedZoneX[index], self._bannedZoneZ[index], self._bannedZoneR[index]
        self._bannedZoneX.remove(x)
        self._bannedZoneZ.remove(z)
        self._bannedZoneR.remove(r)
        self._counter -= 1

    def unban_zone_with_values(self, x, z, r):
        """
        remove zone from banned with values
        :param x: int
        :param z: int
        :param r: int
        """
        if not (x in self._bannedZoneX and z in self._bannedZoneZ and r in self._bannedZoneR and
                self._bannedZoneX.index(x) == self._bannedZoneZ.index(z) == self._bannedZoneR.index(r)):
            raise IndexError("Coordinates not found")
        self._bannedZoneX.remove(x)
        self._bannedZoneZ.remove(z)
        self._bannedZoneR.remove(r)
        self._counter -= 1

    @property
    def x_values(self):
        """
        list of x coordinates
        :return: list
        """
        return self._bannedZoneX

    @property
    def z_values(self):
        """
        list of z coordinates
        :return: list
        """
        return self._bannedZoneZ

    @property
    def r_values(self):
        """
        list of radius
        :return: list
        """
        return self._bannedZoneR

    @property
    def all_values(self):
        """
        list of all values
        :return: list
        """
        values = []
        for i in range(self._counter):
            values += [[self._bannedZoneX[i], self._bannedZoneZ[i], self._bannedZoneR[i]]]
        return values

    def __str__(self):
        string = ""
        for i in range(self._counter):
            string += "Zone {0}: ({1}, {2}), radius = {3};\n"\
                .format(i+1, self._bannedZoneX[i], self._bannedZoneZ[i], self._bannedZoneR[i])
        return string

    def __iadd__(self, other):
        if type(other) == tuple or type(other) == list:
                self.ban_zone(other[0], other[1], other[2])
        else:
            for i in range(other.counter):
                x, z, r = other.all_values[i]
                self.ban_zone(x, z, r)

    def __add__(self, other):
        """
        :param other: zonesADT
        :return:
        """
        from copy import deepcopy as dc
        reserve = dc(self)
        for i in range(len(other)):
            x, z, r = other.all_values[i]
            reserve.ban_zone(x, z, r)
        return reserve

    def __getitem__(self, index):
        """
        :param index: int
        :return:
        """
        return self.all_values[index]

    def __len__(self):
        return self._counter

    def __bool__(self):
        return bool(self._counter)
