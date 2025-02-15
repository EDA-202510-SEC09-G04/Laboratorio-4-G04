def new_queue():
    new_queue = {
        'size': 0,
        'elements': []
    }
    return new_queue

def enqueue(my_queue, element):
    last = my_queue['size']-1
    my_queue['elements'][last] = element
    my_queue['size'] += 1
    return my_queue
        

def size(my_queue):
    return my_queue['size']

def dequeue(my_queue):
    my_queue['elements'][0] = element
    
    my_queue['size'] -= 1
    return my_queue
