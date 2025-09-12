from my_numpy import ArrayJoin

if __name__ == '__main__':
    arr1 = [1,2,3]
    arr2 = [4,5,6]
    res1 = ArrayJoin(arr1,arr2)
    print('concatenate()')
    res1.return_con()
    arr3 = [[1, 2], [3, 4]]
    arr4 = [[5, 6], [7, 8]]
    res2 = ArrayJoin(arr3,arr4)
    res2.return_con()
    res2.return_con(axis=1)
    print('stack()')
    res1.return_stack()
    res1.return_stack(axis=1)
    print('hstack()')
    res1.return_hstack()
    print('vstack()')
    res1.return_vstack()
    print('dstack()')
    res1.return_dstack()