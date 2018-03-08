class BinarySearch:

    def binary_search(self, data, search_value):
        tail = len(data) -1
        head = 0
        while head <= tail:
            center = int((head + tail) / 2)
            if data[center] == search_value:
                print("The value: " + str(search_value) + " found !!")
                return
            elif data[center] < search_value:
                head = center + 1
            else:
                tail = center - 1
        print("The value: " +str(search_value)+" not found !!")
        return

if __name__ == "__main__":
    count = 0
    data_set = [0]
    while count < 100:
        count = count + 1
        data_set.append(count)
    bn = BinarySearch()
    bn.binary_search(data_set, 17)
    bn.binary_search(data_set, 101)