class LinkedList:
  def __init__(self, val):
    self.val = val
    self.next = None

class Solution:
  def reverseList(self, head: LinkedList) -> LinkedList:
    prev = None
    cur = head

    while cur:
      # 交换当前
      nextCur = cur.next
      cur.next = prev
      # 位置后移
      prev = cur
      cur = nextCur

    return prev

def printLinkedList(head: LinkedList):
  cursor = head
  result = ''
  while cursor:
    result += str(cursor.val) + ' -> '
    cursor = cursor.next
  result += 'Ø'
  print(result)

# init
node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node1.next = node2
node2.next = node3

printLinkedList(node1)

slu = Solution()
result = slu.reverseList(node1)

printLinkedList(result)


  