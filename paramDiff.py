p1 = open("params1").read()
p2 = open("params2").read()
l = open("params.txt").read()

param_list = [ i.split(',')[0] for i in l.split('\n') ][:-1]
params_1 = [ i.split(',') for i in p1.split('\n')[:-1] if i.split(',')[0] in param_list ]
params_2 = [ i.split(',') for i in p2.split('\n')[:-1] if i.split(',')[0] in param_list ]

identical = []
ref_index = 0
for param in params_1[:]:
    if param in params_2:
        identical.append(param)
        params_1.remove(param)
        params_2.remove(param)

param_list_1 = [ i[0] for i in params_1 ]
param_list_2 = [ i[0] for i in params_2 ]
added = []
for param in params_2[:]:
    if param[0] not in param_list_1:
        added.append(param)
        params_2.remove(param)

removed = []
for param in params_1[:]:
    if param[0] not in param_list_2:
        removed.append(param)
        params_1.remove(param)

p1d = { i:j for i,j in params_1 }
p2d = { i:j for i,j in params_2 }

changed = []
for param in p1d.keys():
    changed.append([param, p1d[param], p2d[param]])

for param in removed:
    print('\033[91m- ' + str(param[0]) + ' = ' + str(param[1]))
for param in added:
    print('\033[92m+ ' + str(param[0]) + ' = ' + str(param[1]))
for param in changed:
    print('\033[97m' + str(param[0]) + ' = \033[91m' + str(param[1]) + '/\033[92m' + str(param[2]))
