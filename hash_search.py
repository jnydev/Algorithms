class HashSearch:
    def hash_search(self, data, search_value):
        hash_value = self.hash_function(search_value, len(data))
        while data[hash_value] != 0:
            if data[hash_value] == search_value:
                return hash_value
            else:
                hash_value = hash_value + 1
                hash_value = self.hash_function(hash_value, len(data))
        return -1

    @staticmethod
    def hash_function(data, k):
        return data % k

    def hash_store(self, src, target):
        i = 0
        while i < len(src):
            hash_value = self.hash_function(src[i], len(target))
            while target[hash_value] != 0:
                hash_value = hash_value + 1
                hash_value = self.hash_function(hash_value, len(target))
            target[hash_value] = src[i]
            i = i + 1
        return


if __name__ == "__main__":

    org_data = [12, 25, 36, 20, 30, 8, 42]
    hash_data = [0]*11
    print("org_data is: " + str(org_data))
    print("hash_data is : " + str(hash_data))

    hs = HashSearch()
    hs.hash_store(org_data, hash_data)
    print("hash_data is: " + str(hash_data))

    ret = hs.hash_search(hash_data, 8)
    if ret == -1:
        print("The value not found")
    else:
        print("The value found at index : " + str(ret))

    ret = hs.hash_search(hash_data, 10)
    if ret == -1:
        print("The value not found")
    else:
        print("The value found index : " + str(ret))
