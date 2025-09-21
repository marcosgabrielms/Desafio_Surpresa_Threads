import threading
import time

def worker(thread_id):
    """A função que cada thread irá executar."""
    print(f"----> Thread {thread_id}: Iniciando.")
    for i in range(5):
        print(f"----> Thread {thread_id}: executando a iteração {i + 1}")
        time.sleep(1) # Pausa por 1 segundo
    print(f"====== Thread {thread_id}: Finalizando. ======")

if __name__ == "__main__":
    threads = []
    num_threads = 3

    print("Main: Iniciando o programa e criando as threads...\n")

    # Criando e iniciando as threads
    for i in range(num_threads):
       
        thread = threading.Thread(target=worker, args=(i + 1,))
        threads.append(thread)
        thread.start() # Inicia a thread

    print("\nMain: Todas as threads foram criadas. Aguardando a finalização delas...\n")

    
    for thread in threads:
        thread.join()

    print("\nMain: Todas as threads finalizaram. Encerrando o programa.")