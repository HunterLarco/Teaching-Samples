class SinglyLinkedListNode(object):
  def __init__(self, value, node=None):
    self.value = value
    self.next = node
  
  def __repr__(self):
    return repr(self.value)


class SinglyLinkedListIterator(object):
  def __init__(self, linkedlist):
    self._node = linkedlist._root
  
  def __next__(self):
    if self._node:
      response = self._node
      self._node = self._node.next
      return response
    else:
      raise StopIteration


class SinglyLinkedList(object):
  def __init__(self, iterable):
    self._root = None
    self._len = 0
    self.extend(iterable)
  
  def _nodeGenerator(self):
    node = self._root
    while node:
      yield node
      node = node.next
  
  def _nodeAt(self, index):
    gen = self._nodeGenerator()
    for i, node in enumerate(gen):
      if i == index:
        return node
  
  def extend(self, iterable):
    node = self._nodeAt(len(self)-1)
    for item in iterable:
      newnode = SinglyLinkedListNode(item)
      if node == None:
        self._root = newnode
      else:
        node.next = newnode
      node = newnode
      self._len += 1
  
  def append(self, value):
    newnode = SinglyLinkedListNode(value)
    node = self._nodeAt(len(self)-1)
    if node == None:
      self._root = newnode
    else:
      node.next = newnode
    self._len += 1
  
  def insert(self, index, value):
    if len(self) == 0:
      self.append(value)
      return
    
    fixedIndex = max(0, min(len(self), index))
    self._len += 1
    newnode = SinglyLinkedListNode(value)
    
    if fixedIndex == 0:
      newnode.next = self._root
      self._root = newnode
      return
    
    prevnode = self._nodeAt(fixedIndex - 1)
    newnode.next = prevnode.next
    prevnode.next = newnode
  
  def remove(self, value):
    lastnode = None
    for node in self._nodeGenerator():
      if node.value == value:
        if lastnode == None:
          self._root = node.next
        else:
          lastnode.next = node.next
        self._len -= 1
        break
      lastnode = node
  
  def clone(self):
    return SinglyLinkedList(node.value for node in self)
  
  def count(self, value):
    count = 0
    for node in self._nodeGenerator():
      if node.value == value:
        count += 1
    return count
  
  def index(self, value):
    for i, node in enumerate(self._nodeGenerator()):
      if node.value == value:
        return i
    return -1
  
  def __delitem__(self, index):
    if index < 0:
      index -= len(self) * (index // len(self))
    prevnode = self._nodeAt(index-1)
    if prevnode == None or prevnode.next == None:
      raise IndexError('list index out of range')
    prevnode.next = prevnode.next.next
    self._len -= 1
    
  def __getitem__(self, index):
    if index < 0:
      index -= len(self) * (index // len(self))
    node = self._nodeAt(index)
    if node == None:
      raise IndexError('list index out of range')
    return node.value
  
  def __setitem__(self, index, value):
    if index < 0:
      index -= len(self) * (index // len(self))
    if index == len(self):
      self.append(value)
    elif index > len(self):
      raise IndexError('list assignment index out of range')
    else:
      node = self._nodeAt(index)
      node.value = value
  
  def __iter__(self):
    return SinglyLinkedListIterator(self)
  
  def __iadd__(self, iterable):
    self.extend(iterable)
    return self
  
  def __add__(self, iterable):
    clone = self.clone()
    clone.extend(iterable)
    return clone
  
  def __contains__(self, value):
    return self.index(value) != -1
  
  def __len__(self):
    return self._len
  
  def __repr__(self):
    return repr(list(self))
  