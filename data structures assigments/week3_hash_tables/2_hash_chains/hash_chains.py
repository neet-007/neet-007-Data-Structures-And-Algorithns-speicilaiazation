# python3
#import random
#import string
#from pprint import pprint
class ListNode():
    def __init__(self, value, prev=None, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList():
    def __init__(self) -> None:
        self.size = 0
        self.head = self.tail = None

    def create_node(self, value):
        return ListNode(value=value)

    def addFront(self, value):
        self.size += 1
        node = self.create_node(value)

        if not self.head:
            self.head = self.tail = node
            return

        self.head.prev = node
        node.next = self.head

        self.head = node

    def addBack(self, value):
        self.size += 1
        node = self.create_node(value)

        if not self.tail:
            self.head = self.tail = None
            return

        self.tail.next = node
        node.prev = self.tail

        self.tail = node


    def remove(self, value):
        node = self.find(value)

        if not node:
            return False

        self.size -= 1

        if self.head == node:
            self.head = node.next

            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return True

        if self.tail == node:
            self.tail = node.prev

            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return True

        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = node.prev = None

        return True

    def find(self, value) -> ListNode | None:
        if not self.head:
            return None

        if self.head.value == value:
            return self.head

        if self.tail == value:
            return self.tail

        curr = self.head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next

        return None
"""
def generate_random_strings(num_strings, string_length=6, seed=42):
    # Set the seed for reproducibility
    random.seed(seed)

    # Define characters and their weights
    characters = string.ascii_lowercase
    weights = [5 if char == 'a' else 1 for char in characters]  # 'a' has a higher chance of being selected

    # Generate random strings with weighted characters
    random_strings = [''.join(random.choices(characters, weights=weights, k=string_length)) for _ in range(num_strings)]

    return random_strings

def rand_q():
    int_ = random.randint(0, 3)

    if int_ == 0:
        return 'add'
    if int_ == 1:
        return 'del'
    if int_ == 2:
        return 'find'
    if int_ == 3:
        return 'check'

def stress_test():
    num_q = random.randint(1, 1000)
    bucket_size = random.randint(num_q // 5, num_q)

    proc = QueryProcessor(bucket_size)
    flag = True
    while flag:
        strings_ = generate_random_strings(num_q)
        print('test start')
        test = {
            'num_q':num_q,
            'bucket_size':bucket_size,
            'failed_at':'',
            'val1':'',
            'val2':'',
            'queries':[]
        }
        for word in strings_:
            q = rand_q()
            if q == 'add' or q == 'del' or q == 'find':
                val = proc.process_query(Query([q, word]))
                val_2 = proc.process_query_(Query([q, word]))
            else:
                rand__ = random.randint(0, bucket_size)
                val = proc.process_query(Query([q, str(rand__)]))
                val_2 = proc.process_query_(Query([q, str(rand__)]))

            test['queries'].append(q + ' ' + (str(rand__) if q == 'check' else word))
            if val != val_2:
                test['failed_at'] = q + ' ' + (str(rand__) if q == 'check' else word)
                test['val1'] = val
                test['val2'] = val_2
                pprint(test)
                flag = False
                break

        print('test end')
"""
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [DoublyLinkedList() for _ in range(bucket_count)]
        #self.elems_ = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')
        #return 'yes' if was_found else 'no'

    def write_chain(self, chain):
        print(' '.join(chain))
        #return ' '.join(chain)

    def read_query(self):
        #return Query(q)
        return Query(input().split())

    def process_query(self, query:Query):
        if query.type == 'check':

            results = []
            list_ = self.elems[query.ind]
            curr = list_.head

            while curr:
                results.append(curr.value)
                curr = curr.next

            return self.write_chain(results)
            #return results

        if query.type == 'add':
            list_ = self.elems[self._hash_func(query.s)]

            if list_.find(query.s):
                return

            list_.addFront(query.s)

            return

        if query.type == 'find':
            list_ = self.elems[self._hash_func(query.s)]
            #return 'yes' if list_.find(query.s) else 'no'
            return self.write_search_result(list_.find(query.s))

        if query.type == 'del':
            list_ = self.elems[self._hash_func(query.s)]
            list_.remove(query.s)

            return
    """
    def process_query_(self, query:Query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            results = []

            for i in range(len(self.elems_) - 1, -1, -1):
                if self._hash_func(self.elems_[i]) == query.ind:
                    results.append(self.elems_[i])
            #results.append(self.write_chain(cur for cur in reversed(self.elems_)
             #           if self._hash_func(cur) == query.ind))

            return results
        else:
            try:
                ind = self.elems_.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                return 'yes' if ind != -1 else 'no'
                # return self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems_.append(query.s)
            else:
                if ind != -1:
                    self.elems_.pop(ind)
    """
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
    #stress_test()
