def barycentre(x_dict, y_dict, z_dict):
    barycentres = {}
    for i in range(0, len(x_dict)):
        temp = 't' + str(i)
        x_mean = (sum(x_dict[temp].values())/len(x_dict[temp]))
        y_mean = (sum(y_dict[temp].values())/len(y_dict[temp]))
        z_mean = (sum(z_dict[temp].values())/len(z_dict[temp]))
        barycentres[temp] = {'x':x_mean, 'y':y_mean, 'z':z_mean}
    return barycentres