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

data = [i for i in range(100)]
chunk_size = 10

generator = chunk_generator(data, chunk_size)

for chunk in generator:
    print(chunk)

def chunk_generator_function(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

data = [i for i in range(100)]
chunk_size = 10

for chunk in chunk_generator_function(data, chunk_size):
    print(chunk)

class ChunkGeneratorClass:
    def __init__(self, data, chunk_size):
        self.data = data
        self.chunk_size = chunk_size
        self.index = 0

    def next_chunk(self):
        if self.index >= len(self.data):
            return None
        chunk = self.data[self.index:self.index + self.chunk_size]
        self.index += self.chunk_size
        return chunk

data = [i for i in range(100)]
chunk_size = 10

generator = ChunkGeneratorClass(data, chunk_size)

while True:
    chunk = generator.next_chunk()
    if chunk is None:
        break
    print(chunk)

def chunk_generator_iterator(data, chunk_size):
    index = 0
    while index < len(data):
        chunk = data[index:index + chunk_size]
        yield chunk
        index += chunk_size

data = [i for i in range(100)]
chunk_size = 10

for chunk in chunk_generator_iterator(data, chunk_size):
    print(chunk)

def chunk_generator_loop(data, chunk_size):
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunks.append(data[i:i + chunk_size])
    return chunks

data = [i for i in range(100)]
chunk_size = 10

chunks = chunk_generator_loop(data, chunk_size)

for chunk in chunks:
    print(chunk)