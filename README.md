OBS: Não foi usada a biblioteca PySimpleGUI com o intuito de proporcionar um aprendizado maior - usando a biblioteca tkinter padrão,
tivemos uma interação maior com os métodos nativos e as dificuldades de se implementar um gerenciador de gráficos do zero.

# Proposta inicial projeto final - POO

**Disciplina:** SSC0103 — Programação Orientada a Objetos\
**Professor:** Dr. Márcio Delamaro\
**Alunos PAE:** Lucas Lagôa e Misael Jr

Grupo: 22
Rafael Zimmer, ********\
Jhonathan Oliveira Alves, ********\
Bruno Germano do Nascimento, ********\
Pedro Rossi Silva Rodrigues, ********

Preview do aplicativo:

![Preview](https://github.com/rzimmerdev/oop-cinema/blob/95aaef13b624dcc75dcad17de4d5533df64246b0/files/preview.png)

## 1. Aplicação
>Área: Visualização de vídeos e gestão de tarefas agendadas

>Projeto: Programa para gerir um sistema de filmes em cartazes, assim como agendar
filmes, bilhetes e avaliações, em suma, um cinema digital.

## 2. Descrição e proposta

O programa irá lidar com arquivos do tipo CSV, assim como um sistema de interação
para o usuário. Será possível adicionar uma tela principal, que irá dar opções para o usuário
ver os filmes em cartaz, comprar ingressos, assim como assistir o filme quando o mesmo
começar. Além disso, será possível criar ‘backups’ dos filmes, assim como das avaliações,
para compartilhar entre diversas instâncias que sejam parte da mesma franquia de cinema.

Essa proposta de projeto foi feita em mente buscando proporcionar à toda a população uma forma de assistir a filmes diretamente pela plataforma do cinema
online, diante da pandemia do Covid-19, além de evitar certas franquias irem à falência.

De certa forma, transformar essa forma de mídia em algo 100% digital não impede
de forma alguma que os cinemas continuem a funcionar de forma presencial, mas sim
possibilita acesso a um novo mercado, sendo útil tanto pro cliente que tem agora acesso
aos filmes em lançamento sem ter de necessariamente assinar um serviço de ‘streaming’,
assim como para os cinemas, que tem agora mais chance de competir no mercado de
mídias digitais.

## 3. Objetivo principal

Implementando o projeto de um cinema digital, o nosso grupo irá colocar em prática os
conceitos aprendidos referentes à criação de módulos, unit testing, manipulação de
arquivos e também a interação com ‘interfaces’ gráficas — conceitos amplamente
dependentes do conteúdo de programação orientada a objetos.

Além disso, iremos ter que aprender a utilizar as bibliotecas Tkinter, que implementa
funcionalidades para ‘interfaces’ gráficas em Python, como também realizar testes unitários
para entradas e saídas de backups e valores salvos ou enviados para arquivos. Em suma, é
uma forma de aplicar o conteúdo aprendido em meios não explicitamente vistos em aula,
que irá fundamentar-nos no conteúdo da matéria toda, pois teremos de pesquisar
e consequentemente desenvolver a capacidade de aprender por conta própria além do que
já vimos anteriormente.

Não apenas, esse trabalho em grupo dará-nos a possibilidade de entendermos na
prática o processo de desenvolvimento em torno de objetos e módulos, assim como o
pipeline de desenvolvimento em grupo de forma mais simplificada, mas mesmo assim ainda
próximo à realidade da profissão.

## 4. Objetivo específico

Em termos mais técnicos, o projeto deverá abordar uma forma de organização
modular, com modelos para virtualizar a interação do usuário com a biblioteca Tkinter,
assim como módulos para tratar a criação de backup de filmes, confirmar a compra de
ingressos e efetivamente planejar os jobs para projetar os filmes na tela quando necessário.

## 5. Funcionalidades a serem desenvolvidas

Iremos começar com uma interface no Console para simplesmente gerenciar a
criação de novos filmes, suas descrições, assim como criar backups dos sistemas de
informação simplificados gerados. Em sequência, iremos separar o projeto nos seguintes
módulos e atribuir um membro à cada, assim como a responsabilidade de projetar casos de
teste para permitir uma integração entre os diferentes módulos de forma imperiosa.

>* **Interface gráfica** — para visualizar os filmes e chamar interativamente os módulos:
  * Acessar a página de compra de ingressos.
  * Na página de compra, ver informações relativas aos filmes.
  * Com ingressos, assistir os filmes por meio da interface diretamente.
>* **Backup e sincronização** — transferência de arquivos entre diferentes instâncias:
  * Salvar as informações para o funcionamento dos outros módulos.
  * Verificar a integridade dos arquivos de backup, no formato CSV.
  * Popular os módulos e suas instâncias com as informações salvas.
>* **Filmes e descrições** — criação de filmes, com cartazes e descrições diferentes:
  * Receber diferentes tipos de informações relativas aos filmes.
  * Remover filmes, adicionar filmes, mudar horários e notificar clientes.
  * Adicionar avaliações dos clientes sobre os filmes e o cinema.
>* **Compra de ingressos** — criar e guardar informações de clientes e ingressos:
  * Verificar a veracidade do ingresso.
  * Atribuir ao ingresso o valor do filme, e o horário.
  * Guardar seguramente as informações do cliente.


### Especificaçoes
Com as funcionalidades e módulos descritos acima, nosso programa irá
possivelmente utilizar os seguintes conceitos importantes para otimizar a eficiência do
mesmo, assim como tornar o desenvolvimento expansível:

_Design patterns:_ fábrica de objetos; Adaptador; Fachada; Memento; Observador.\
_Algoritmos:_ Stack; hash-map;\
_Pipeline:_ Testes unitários; Integração modular;
