from multiprocessing import Pool

p = Pool(5)
def f(x):
    return x*x

if __name__ == "__main__":
    p.map(f, [1,2,3])
