import sys
import h5py

def main(argv:str):
    if len(argv) != 3 or ".h5" not in argv[1]:
        print(f"Usage: {argv[0]} <file.h5> <index_name>")

    h5_res = h5py.File(argv[1], 'r')
    keys = h5_res.keys()
    for key in keys:
        elem = h5_res.get(key)[argv[2]]
        l = list()
        for num in elem:
            l.append(num)
        print(l)
    h5_res.close()


if __name__=='__main__':
    main(sys.argv)