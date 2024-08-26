from multiprocessing import Process, Queue, Pipe

def producer(queue):
    for i in range(5):
        queue.put(i)
    queue.put(None)

def consumer(queue):
    while True:
        data = queue.get()
        if data is None:
            break
        print("Received: ", data)

def sender(conn):
    for i in range(5):
        conn.send(i)
    conn.close()

def reciver(conn):
    while True:
        data = conn.recv()
        if data is None:
            break
        print("Received: ", data)

if __name__ == '__main__':
    #     queue = Queue()
    #     p1 = Process(target=producer, args=(queue,))
    #     p2 = Process(target=consumer, args=(queue,))
    #     p1.start()
    #     p2.start()
    #     p1.join()
    #     p2.join()
    parent_conn, child_conn = Pipe()
    p1 = Process(target=sender, args=(child_conn,))
    p2 = Process(target=reciver, args=(parent_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()