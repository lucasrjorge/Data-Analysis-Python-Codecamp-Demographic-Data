import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def calculate(a):
    if len(a) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(a).reshape(3, 3)

    mean1 = np.mean(a, axis=0).tolist()
    var1 = np.var(a, axis=0).tolist()
    std1 = np.std(a, axis=0).tolist()
    max1 = np.max(a, axis=0).tolist()
    min1 = np.min(a, axis=0).tolist()
    sum1 = np.sum(a, axis=0).tolist()


    mean2 = np.mean(a, axis=1).tolist()
    var2 = np.var(a, axis=1).tolist()
    std2 = np.std(a, axis=1).tolist()
    max2 = np.max(a, axis=1).tolist()
    min2 = np.min(a, axis=1).tolist()
    sum2 = np.sum(a, axis=1).tolist()

    mean3 = np.mean(a).tolist()
    var3 = np.var(a).tolist()
    std3 = np.std(a).tolist()
    max3 = np.max(a).tolist()
    min3 = np.min(a).tolist()
    sum3 = np.sum(a).tolist()



    return {
        'mean' : [mean1, mean2, mean3],
        'variance' : [var1, var2, var3],
        'standard deviation' : [std1, std2, std3],
        'max' : [max1, max2, max3],
        'min' : [min1, min2, min3],
        'sum' : [sum1, sum2, sum3]
    }

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))