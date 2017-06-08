from zonesADT import Zones

print("Start testing...\n")

zones1 = Zones()
assert not zones1.is_available(5, 5)
zones2 = Zones()
assert type(zones1) == type(zones2)

zones1.ban_zone([20], [20], [10])
zones1.ban_zone([60], [60], [10])

print(zones1)

assert not zones1.is_available(20, 20)
assert zones1.is_available(100, 100)

zones1.unban_zone_with_index(1)
assert zones1.is_available(30, 30)

print(zones1)
assert zones1.x_values == [0, 60]
assert zones1.z_values == [0, 60]
assert zones1.r_values == [20, 10]
assert zones1.all_values == [[0, 0, 20], [60, 60, 10]]
assert zones1[1] == [60, 60, 10]

assert not zones1.is_available(60, 60)
zones1.unban_zone_with_values(60, 60, 10)
assert zones1.is_available(61, 61)


print("Passed!")
