class orderd_dict():
    values = []
    keys = []
    length = 0

    def insert_old(self, key, new_number):
        failure = True
        self.length += 1
        for i, number in enumerate(self.values):
            if new_number >= number:
                self.values = self.values[:i] + [new_number] + self.values[i:]
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                failure = False
                break

        if failure:
            self.values += [new_number]
            self.keys += [key]

    def insert(self, key, new_number):
        self.length += 1
        if self.length == 0:
            self.values = [new_number]
            self.keys = [key]
            return
        
        index = int(round(self.length / 2, 0))
        next_index = int(round(index / 2, 0))

        while next_index != 0 and index < self.length - 1:
            if self.values[index] > new_number:
                index -= next_index
            elif self.values[index] < new_number:
                index += next_index
            else:
                break

            next_index = int(round(next_index / 2, 0))

        self.values = self.values[:index] + [new_number] + self.values[index:]
        self.keys = self.keys[:index] + [key] + self.keys[index:]
        
        

    def get(self, desired_key):
        for i, key in enumerate(self.keys):
            if key == desired_key:
                return self.values[i]
            
        print("Key not Found")
        return None


    def pop_biggest(self):
        self.length -= 1
        biggest = self.keys[0], self.values[0]
        self.values = self.values[1:]
        self.keys = self.keys[1:]
        return biggest
    
    def pop_smallest(self):
        self.length -= 1
        smallest = self.keys[-1], self.values[-1]
        self.values = self.values[:-1]
        self.keys = self.keys[:-1]
        return smallest

    def __str__(self):
        nice_string = ""
        for i in range(self.length):
            nice_string += str(self.keys[i]) + " : " + str(self.values[i]) + "\n"

        nice_string += "Length = " + str(self.length)

        return nice_string
    

if __name__ == "__main__":
    import random
    import time

    start_time = time.time()

    o_dict = orderd_dict()

    for i in range(0, 100):
        o_dict.insert(i, random.randint(0,100))

    print(o_dict)

    print(f"completed in {time.time() - start_time}")
