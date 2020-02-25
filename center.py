def center(x_dict, y_dict, z_dict, barycenters):
    """
    A noter, on considere ici que la clef j est un int, pas un str
    Exemple: x_dict['t0'][1] et pas x_dict['t0']['1']
    """
    for i in range(0, len(x_dict)):
        temp = 't' + str(i)
        for j in range(1, len(x_dict[temp])+1):
            x_dict[temp][j] = x_dict[temp][j] - barycenters[temp]['x']
            y_dict[temp][j] = y_dict[temp][j] - barycenters[temp]['y']
            z_dict[temp][j] = z_dict[temp][j] - barycenters[temp]['z']
    return
