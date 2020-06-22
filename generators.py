import memory_profiler as mem_profile
import random
import time

names = ['Ovansa', 'Muhammad', 'Amin', 'Ibrahim', 'Aduvoh']
majors = ['Maths', 'Art', 'Elect. Engineering', 'Computer Science', 'Agriculture']

print(f"Memory before {mem_profile.memory_usage()} Mb")

def people_list(num_people):
    result = []

    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)

    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

t1 = time.process_time()
people_generator(1000000)
t2 = time.process_time()

print(f"Memory after {mem_profile.memory_usage()} Mb")
print(f"Took {t2 - t1} seconds")
