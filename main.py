class ChunkGenerator:
    def __init__(self, data, chunk_size):
        self.data = data
        self.chunk_size = chunk_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        chunk = self.data[self.index:self.index + self.chunk_size]
        self.index += self.chunk_size
        return chunk

def chunk_generator(data, chunk_size):
    return ChunkGenerator(data, chunk_size)

def main():
    data = [i for i in range(100)]
    chunk_size = 10
    generator = chunk_generator(data, chunk_size)
    for i, chunk in enumerate(generator):
        print(f"Chunk {i+1}: {chunk}")

class DataProcessor:
    def __init__(self, data, chunk_size):
        self.data = data
        self.chunk_size = chunk_size

    def process(self):
        generator = chunk_generator(self.data, self.chunk_size)
        for i, chunk in enumerate(generator):
            self.process_chunk(chunk)

    def process_chunk(self, chunk):
        print(f"Processing chunk: {chunk}")

def main2():
    data = [i for i in range(100)]
    chunk_size = 10
    processor = DataProcessor(data, chunk_size)
    processor.process()

class DataLoader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename, 'r') as file:
            data = [line.strip() for line in file.readlines()]
        return data

def main3():
    loader = DataLoader('data.txt')
    data = loader.load()
    chunk_size = 10
    generator = chunk_generator(data, chunk_size)
    for i, chunk in enumerate(generator):
        print(f"Chunk {i+1}: {chunk}")

class DataSaver:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')

def main4():
    data = [i for i in range(100)]
    saver = DataSaver('data.txt')
    saver.save(data)

if __name__ == "__main__":
    main()
    main2()
    main3()
    main4()