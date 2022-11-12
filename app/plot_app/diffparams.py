
def diffparams(params_1,params_2):
    param_names = []
    param_base = []
    param_current = []
    param_colors = []

    param_names=list(set(list(params_1.keys())+list(params_2.keys())))
    param_names.sort()
    
    for p in param_names:    
        b=''
        c=''
        if p in params_1:
            b=params_1[p]

        if p in params_2:
            c=params_2[p]

        param_base.append(b)
        param_current.append(c)
        if c==b:
            param_colors.append('green')
        else:
            param_colors.append('red')

    return [param_names,param_base,param_current,param_colors]
