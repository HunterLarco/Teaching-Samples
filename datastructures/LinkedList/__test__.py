from singlylinked import SinglyLinkedList


LISTS = [
  SinglyLinkedList
]


if __name__ == '__main__':
  for linkedlist in LISTS:
    llist = linkedlist(range(100))
    clone = llist.clone()
    llist.append(100)
    print('original', *llist)
    print()
    print('clone', *clone)
    print()
    
    clone.insert(0, -2)
    clone.insert(1, -1)
    clone.insert(-100, -3)
    clone.insert(1000, 200)
    print(*clone)
    print()
    
    clone.remove(69)
    clone.remove(70)
    clone.remove(71)
    clone.remove(73)
    print(*clone)
    print()
    
    print(clone.index(71))
    print(clone.index(200))
    print(clone.index(-3))
    print(clone.count(0))
    print(clone.count(-123))
    print()
    
    clone += [1, 2, 3, 4]
    clone2 = clone + [5, 6, 7]
    clone2.append(8)
    
    print(*clone)
    print()
    print(*clone2)
    print()
    print(clone.count(4))
    print(4 in clone)
    print(400 in clone)
    print()
    
    clone = linkedlist(range(10))
    print(*clone)
    clone[2] = 0
    clone[9] = 0
    clone[10] = 10
    clone[-1] = 11
    # clone[14] = 0
    print(*clone)
    print()
    
    print(clone[1])
    print(clone[-1])
    print(clone[-3])
    print(*clone)
    print()
    
    del clone[3]
    del clone[2]
    del clone[7]
    del clone[-1]
    print(*clone)
    print()
    
    