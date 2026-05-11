from src.io.reader import load_graph
from src.algorithms.bfs import bfs
import random


def normalize_user(name: str) -> str:
    return "user:" + name.strip().lower().replace(" ", "_")


def normalize_music(name: str) -> str:
    return "music:" + name.strip().lower().replace(" ", "_")


def ensure_node(graph, node):
    if node not in graph.get_vertices():
        graph.add_vertex(node)


def main():
    graph = load_graph('data/syncora_graph.json')

    print('🎵 Syncora — Grafo carregado com sucesso.')
    print(f'📊 {len(graph.get_vertices())} vértices encontrados.')

    while True:
        print('\n------------------------------')
        print('1 - Buscar próximos')
        print('2 - Adicionar usuário + música')
        print('0 - Sair')

        op = input('> ')

        # ==========================================
        # BUSCAR PRÓXIMOS
        # ==========================================
        if op == '1':

            user_input = input('Seu nome: ')
            music_input = input('Sua música favorita: ')

            user_node = normalize_user(user_input)
            music_node = normalize_music(music_input)

            # garante que os nós existem
            ensure_node(graph, user_node)
            ensure_node(graph, music_node)

            # cria conexão automaticamente
            if music_node not in graph.get_neighbors(user_node):
                graph.add_edge(user_node, music_node)

            # procura pessoas ouvindo a mesma música
            connected_users = []

            for neighbor in graph.get_neighbors(music_node):
                if neighbor.startswith("user:") and neighbor != user_node:
                    connected_users.append(neighbor)

            # ninguém encontrado
            if not connected_users:
                print("\n😔 Nenhuma conexão encontrada no momento.")

            else:
                # escolhe alguém aleatório
                matched_user = random.choice(connected_users)

                # remove prefixo user:
                matched_name = (
                    matched_user
                    .replace("user:", "")
                    .replace("_", " ")
                    .title()
                )

                print("\n🎧 Conexão encontrada!")
                print(
                    f"{user_input} e {matched_name} "
                    f"estão ouvindo {music_input} agora."
                )

                resposta = input("\nDeseja se conectar? (s/n): ")

                if resposta.lower() == "s":
                    print("✅ Conexão realizada!")
                else:
                    print("❌ Conexão ignorada.")

        # ==========================================
        # ADICIONAR USUÁRIO + MÚSICA
        # ==========================================
        elif op == '2':

            user_input = input('Seu nome: ')
            music_input = input('Nome da música: ')

            user_node = normalize_user(user_input)
            music_node = normalize_music(music_input)

            # garante nós existentes
            ensure_node(graph, user_node)
            ensure_node(graph, music_node)

            # evita conexão duplicada
            if music_node not in graph.get_neighbors(user_node):
                graph.add_edge(user_node, music_node)

            print(f'\n✅ {user_input} agora está ouvindo {music_input}')

        # ==========================================
        # SAIR
        # ==========================================
        elif op == '0':
            print('👋 Encerrando Syncora...')
            break

        else:
            print('❌ Opção inválida')


if __name__ == '__main__':
    main()