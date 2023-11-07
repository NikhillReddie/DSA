import random

def hash_function(Key, m):
    return Key % m

class ListNode:
    def __init__(self, Data):
        self.Data = Data
        self.next = None

def create_hash_table(Data, m):
    hash_table = [None] * m
    for item in Data:
        Index = hash_function(item, m)
        if hash_table[Index] is None:
            hash_table[Index] = ListNode(item)
        else:
            current = hash_table[Index]
            while current.next:
                current = current.next
            current.next = ListNode(item)
    return hash_table

def search_hash_table(hash_table, Key, m):
    Index = hash_function(Key, m)
    current = hash_table[Index]
    Count = 1
    while current:
        if current.Data == Key:
            return Count
        current = current.next
        Count += 1
    return Count

Student_ids = [random.randint(1000, 9999) for _ in range(500)]

m = 503  # a prime number close to 500/3

hash_table = create_hash_table(Student_ids, m)

found_ids = random.sample(Student_ids, 17)
not_found_ids = [random.randint(0, 9999) for _ in range(3)]

for Search_id in found_ids + not_found_ids:
    Count = search_hash_table(hash_table, Search_id, m)
    result = "Found" if Search_id in found_ids else "Not Found"
    print(f"Search ID: {Search_id}, Result: {result}, Computation Time: {Count}")

def sequential_search(Data, Key):
    Count = 0
    for item in Data:
        Count += 1
        if item == Key:
            return Count
    return Count

for Search_id in found_ids + not_found_ids:
    Count = sequential_search(Student_ids, Search_id)
    result = "Found" if Search_id in found_ids else "Not Found"
    print(f"The Search ID: {Search_id}, Result: {result}, The Computation Time: {Count}")
