import numpy as np

def calculate(lista):
  if len(lista) < 9:
    raise ValueError ("List must contain nine numbers.")

  # make lists for the 3x3 array
  l1 = lista[:3]
  l2 = lista[3:6]
  l3 = lista[6:]

  # 3x3 array
  data=np.array([l1,l2,l3])

  # make the calc in order
  mean = [np.mean(data, axis = 0).tolist(), np.mean(data, axis = 1).tolist(), np.mean(data).tolist()]
  var = [np.var(data, axis = 0).tolist(), np.var(data, axis = 1).tolist(), np.var(data).tolist()]
  std = [np.std(data, axis = 0).tolist(), np.std(data, axis = 1).tolist(), np.std(data).tolist()]
  mx = [np.max(data, axis = 0).tolist(), np.max(data, axis = 1).tolist(), np.max(data).tolist()]
  mn = [np.min(data, axis = 0).tolist(), np.min(data, axis = 1).tolist(), np.min(data).tolist()]
  plus = [np.sum(data, axis = 0).tolist(), np.sum(data, axis = 1).tolist(), np.sum(data).tolist()]
  
  #unite in calculations
  calculations = {"mean":mean, "variance":var,"standard deviation": std, "max":mx, "min":mn, "sum":plus}




  return calculations
