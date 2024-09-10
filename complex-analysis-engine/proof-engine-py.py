def holomorph(deriverbar_omgivning):
    if (deriverbar_omgivning == True):
        return True
    else:
        return "Not holomorph"


def deriverbar(z, region_D):
    if (z == True):
        return True
    else:
        return "Not deriverbar i D"


is_holo = holomorph(deriverbar("regionD"))
print("is holo?", is_holo)


def isogonal():
    if ("vinklars storlek beveras"):
        return True


def konform(gamma_1, gamma_2):
    if ("vinklars storlek och riktning beveras"):
        return True
    else:
        return False
