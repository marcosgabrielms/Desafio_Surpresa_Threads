# Demonstração de Multithreading em Python

Este é um script simples em Python que demonstra a criação e execução de múltiplas threads de forma concorrente, utilizando a biblioteca padrão `threading`.

O objetivo é mostrar como executar tarefas "ao mesmo tempo", com uma saída no console que evidencia a intercalação das operações de cada thread.

## ⚙️ Tecnologias Utilizadas

* **Python 3**
* **Módulo `threading`**: Para a criação e gerenciamento das threads.
* **Módulo `time`**: Para usar a função `sleep()` e simular uma tarefa que leva tempo.

## 📖 Como Funciona

1.  **Função `worker`**: Uma função é definida para ser o alvo de cada thread. Ela simula uma tarefa que leva 5 segundos para ser concluída, imprimindo uma mensagem a cada segundo.
2.  **Criação das Threads**: No bloco principal do script, um loop cria 3 instâncias da classe `threading.Thread`. Cada instância é configurada para executar a função `worker`.
3.  **Início da Execução**: O método `.start()` é chamado em cada objeto de thread, o que agenda sua execução pelo sistema operacional. A partir daqui, as threads rodam concorrentemente.
4.  **Sincronização**: O método `.join()` é chamado para cada thread. Isso faz com que o script principal pause e espere até que todas as threads tenham concluído suas tarefas antes de prosseguir e encerrar o programa.

## 🚀 Como Executar

### Pré-requisitos
* Ter o [Python 3](https://www.python.org/downloads/) instalado.

### Passos
1.  Clone o repositório:
    ```sh
    git clone [https://github.com/marcosgabrielms/Desafio_Surpresa_Threads.git](https://github.com/marcosgabrielms/Desafio_Surpresa_Threads.git)
    ```
2.  Navegue até a pasta do projeto:
    ```sh
    cd Desafio_Surpresa_Threads
    ```
3.  Execute o script Python:
    ```sh
    python multithread.py
    ```
    *(Assumindo que o nome do arquivo é `multithread.py`)*

## 🖥️ Saída Esperada

A saída no terminal será semelhante a esta, mostrando claramente as mensagens das diferentes threads sendo impressas de forma intercalada, provando que elas estão rodando em paralelo.

Com certeza! Aqui está um README.md focado exclusivamente na implementação em Python.

Markdown

# Demonstração de Multithreading em Python

Este é um script simples em Python que demonstra a criação e execução de múltiplas threads de forma concorrente, utilizando a biblioteca padrão `threading`.

O objetivo é mostrar como executar tarefas "ao mesmo tempo", com uma saída no console que evidencia a intercalação das operações de cada thread.

## ⚙️ Tecnologias Utilizadas

* **Python 3**
* **Módulo `threading`**: Para a criação e gerenciamento das threads.
* **Módulo `time`**: Para usar a função `sleep()` e simular uma tarefa que leva tempo.

## 📖 Como Funciona

1.  **Função `worker`**: Uma função é definida para ser o alvo de cada thread. Ela simula uma tarefa que leva 5 segundos para ser concluída, imprimindo uma mensagem a cada segundo.
2.  **Criação das Threads**: No bloco principal do script, um loop cria 3 instâncias da classe `threading.Thread`. Cada instância é configurada para executar a função `worker`.
3.  **Início da Execução**: O método `.start()` é chamado em cada objeto de thread, o que agenda sua execução pelo sistema operacional. A partir daqui, as threads rodam concorrentemente.
4.  **Sincronização**: O método `.join()` é chamado para cada thread. Isso faz com que o script principal pause e espere até que todas as threads tenham concluído suas tarefas antes de prosseguir e encerrar o programa.

## 🚀 Como Executar

### Pré-requisitos
* Ter o [Python 3](https://www.python.org/downloads/) instalado.

### Passos
1.  Clone o repositório:
    ```sh
    git clone [https://github.com/marcosgabrielms/Desafio_Surpresa_Threads.git](https://github.com/marcosgabrielms/Desafio_Surpresa_Threads.git)
    ```
2.  Navegue até a pasta do projeto:
    ```sh
    cd Desafio_Surpresa_Threads
    ```
3.  Execute o script Python:
    ```sh
    python multithread.py
    ```
    *(Assumindo que o nome do arquivo é `multithread.py`)*

## 🖥️ Saída Esperada

A saída no terminal será semelhante a esta, mostrando claramente as mensagens das diferentes threads sendo impressas de forma intercalada, provando que elas estão rodando em paralelo.
```
Main: Iniciando o programa e criando as threads...

----> Thread 1: Iniciando.
----> Thread 2: Iniciando.
----> Thread 3: Iniciando.

Main: Todas as threads foram criadas. Aguardando a finalização delas...

----> Thread 1: executando a iteração 1
----> Thread 3: executando a iteração 1
----> Thread 2: executando a iteração 1
----> Thread 2: executando a iteração 2
----> Thread 1: executando a iteração 2
----> Thread 3: executando a iteração 2
...
...
====== Thread 2: Finalizando. ======
====== Thread 1: Finalizando. ======
====== Thread 3: Finalizando. ======

Main: Todas as threads finalizaram. Encerrando o programa.
```
