
import gc
import tracemalloc

def create_objects():
    objects = []
    for i in range(10000):
        objects.append([i] * 10)
    return objects

def display_memory():
    current, peak = tracemalloc.get_traced_memory()
    print("Current memory usage:", current, "bytes")
    print("Peak memory usage:", peak, "bytes")

tracemalloc.start()

print("Initial memory usage:")
display_memory()

print("\nCreating objects...")
data = create_objects()

print("\nMemory usage after creating objects:")
display_memory()

del data

print("\nObjects deleted.")

gc.collect()

print("\nMemory usage after garbage collection:")
display_memory()

tracemalloc.stop()

print("\nGarbage collection completed successfully!")
