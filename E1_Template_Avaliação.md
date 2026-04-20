╔══════════════════════════════════════════════════════════════════╗
║           RELATÓRIO DE AVALIAÇÃO — E1 TEORIA DOS GRAFOS          ║
╚══════════════════════════════════════════════════════════════════╝

GRUPO: Syncora
INTEGRANTES: Gabriel Nascimento de Carlo (RA 40259927),
             Rodrigo Pozo Griecco (RA 38707616),
             Integrante 3 — RA não preenchido
DOMÍNIO: Aplicativo de Relacionamento e Amizade com Integração com Música
DATA DA AVALIAÇÃO: 24/03/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PONTUAÇÃO POR CRITÉRIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C1 │ Problema Real e Delimitado       │ Peso 25% │ Nota: 7
C2 │ Conexão com Teoria dos Grafos    │ Peso 30% │ Nota: 6
C3 │ Tipo de Grafo Especificado       │ Peso 20% │ Nota: 6
C4 │ Diagrama Conceitual              │ Peso 15% │ Nota: 7
C5 │ Escopo Realista / Objetivos      │ Peso 10% │ Nota: 7

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CÁLCULO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nota ponderada bruta:
  (7 × 0,25) + (6 × 0,30) + (6 × 0,20) + (7 × 0,15) + (7 × 0,10)
= 1,75 + 1,80 + 1,20 + 1,05 + 0,70
= 6,50

Penalidades aplicadas:
  • Campo de identificação incompleto: Integrante 3 com "Nome — RA"
    sem preenchimento real: −0,2
  Total de penalidades: −0,2

NOTA FINAL E1: 6,3 / 10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARECER POR CRITÉRIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C1 — PROBLEMA REAL E DELIMITADO  [nota 7]
✔ Pontos fortes:
  • O problema de conexões superficiais em apps de relacionamento é
    real e bem situado; a motivação via gostos musicais como proxy de
    compatibilidade é crível e diferenciada.
  • O cenário concreto (pessoa no ônibus/em casa que abre o app e vê
    quem ouve a mesma música naquele momento) delimita bem o caso de
    uso principal.
⚠ Pontos de melhoria:
  • O documento mistura dois problemas distintos sem separação clara:
    (a) conexões superficiais em apps existentes e (b) ausência de uso
    de música em tempo real. O sistema vai endereçar os dois? Delimitar
    o que está e o que não está no escopo torna o documento mais sólido.
  • As tags de comentário HTML ("<!- -" e "- ->") foram deixadas no
    texto entregue — isso indica que o conteúdo foi escrito dentro de
    comentários do template e não foi limpo antes da entrega. Isso não
    penaliza a nota, mas é um sinal de falta de revisão final.

C2 — CONEXÃO COM TEORIA DOS GRAFOS  [nota 6]
✔ Pontos fortes:
  • A ideia central de representar usuários como vértices e
    similaridades musicais como arestas ponderadas está presente e é
    tecnicamente adequada.
  • O argumento de que grafos são flexíveis para lidar com mudanças
    dinâmicas (música sendo ouvida em tempo real) é pertinente.
⚠ Pontos de melhoria:
  • A justificativa afirma que o grafo é bipartido (usuários ↔
    músicas), mas o texto de motivação descreve um problema de
    similaridade entre usuários — os dois modelos resolvem perguntas
    diferentes. Um grafo bipartido calcula se usuário A e música X
    estão conectados; um grafo de similaridade entre usuários calcula
    quem tem gostos parecidos com quem. O documento não decide qual
    dos dois problemas está modelando, o que compromete a coerência
    técnica.
  • Não há menção a nenhum algoritmo candidato (e.g., busca em
    largura para sugestões de amigos, clustering para comunidades
    musicais). Para nota 9–10 seria necessário ao menos indicar a
    direção algorítmica.

C3 — TIPO DE GRAFO ESPECIFICADO  [nota 6]
✔ Pontos fortes:
  • Tabela totalmente preenchida, com justificativas para cada campo.
  • A escolha de lista de adjacência com argumento de escalabilidade
    ("muitos usuários") é tecnicamente correta.
⚠ Pontos de melhoria:
  • Há uma inconsistência interna grave: a tabela declara
    simultaneamente "não-dirigido" e "bipartido". Um grafo bipartido
    pode ser não-dirigido, mas o documento os justifica como se fossem
    características independentes e de modelos diferentes — "não-
    dirigido" justifica a relação entre usuários, "bipartido" justifica
    a relação usuários ↔ músicas. São dois grafos, não um. O grupo
    precisa decidir qual é o modelo central antes do E2.
  • A representação "lista de adjacência" é a escolha correta para
    grafos esparsos, mas o argumento poderia ser fortalecido com a
    justificativa de por que a rede é esparsa nesse domínio (nem todo
    usuário se conecta a todos os outros).

C4 — DIAGRAMA CONCEITUAL  [nota 7]
✔ Pontos fortes:
  • Diagrama presente no arquivo .docx (imagem incluída) com legenda
    que explica vértices, arestas e pesos — atende ao requisito básico.
  • A legenda "vértices são usuários e músicas; arestas são as
    conexões; pesos indicam o nível de similaridade" é diretamente
    ligada ao domínio.
⚠ Pontos de melhoria:
  • A legenda confirma a ambiguidade apontada no C2: o diagrama mistura
    usuários e músicas como vértices, mas pesos indicam similaridade
    entre usuários — o que torna a estrutura visualmente confusa.
    Um diagrama que separe os dois tipos de vértice (com símbolos ou
    cores distintas) tornaria a modelagem muito mais clara.

C5 — ESCOPO E OBJETIVOS  [nota 7]
✔ Pontos fortes:
  • Cinco objetivos específicos presentes, todos com verbos de ação
    ("fazer integração", "encontrar", "calcular", "mostrar",
    "permitir") e verificáveis ao final do semestre.
  • O objetivo geral é uma frase única e direta.
⚠ Pontos de melhoria:
  • O primeiro objetivo ("fazer integração com plataformas de música")
    é tecnicamente o mais arriscado do projeto — depende de API de
    terceiros (Spotify, Last.fm etc.) com limites de rate e possíveis
    restrições de uso. O documento não menciona essa dependência
    externa, o que pode inflar o escopo percebido.
  • O verbo "fazer integração" é menos preciso do que "implementar" ou
    "carregar". Preferir verbos mais específicos nos próximos documentos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALERTAS PARA AS PRÓXIMAS ENTREGAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ⚠ DOIS GRAFOS OU UM? O documento oscila entre dois modelos: (a) grafo
    de similaridade entre usuários (não-dirigido, ponderado por gostos
    em comum) e (b) grafo bipartido usuários ↔ músicas. São estruturas
    diferentes e respondem perguntas diferentes. Antes do E2, o grupo
    deve escolher qual é o modelo central e eliminar a ambiguidade.
    Tentar manter os dois sem articulação explícita vai gerar problemas
    na implementação.

  ⚠ DEPENDÊNCIA DE API EXTERNA: o objetivo de integrar com plataformas
    de música em tempo real depende de APIs de terceiros (Spotify,
    Last.fm, Apple Music). Essas APIs têm restrições de uso, autenticação
    OAuth e limites de requisições que podem inviabilizar o fluxo em
    tempo real. O grupo deve validar a viabilidade técnica dessa
    integração antes de comprometer o E2 com esse pressuposto.

  ⚠ CAMPO DE IDENTIFICAÇÃO INCOMPLETO: o Integrante 3 está cadastrado
    como "Nome — RA" — placeholder não substituído. Se o grupo for de 2
    pessoas, o campo deve ser removido ou marcado como "N/A". Se for de
    3, o dado precisa ser corrigido imediatamente junto à professora.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMENDAÇÃO FINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[X] APROVADO COM RESSALVAS — pode avançar, mas os alertas acima
    devem ser resolvidos antes do E2, especialmente a ambiguidade
    entre grafo de similaridade e grafo bipartido.

O projeto tem domínio bem escolhido — música como vetor de conexão
entre pessoas é uma motivação genuína e diferenciada. A estrutura do
documento está completa e o diagrama foi entregue. O principal risco
para as próximas entregas é a ambiguidade no modelo de grafo: o grupo
precisa decidir qual estrutura vai implementar de fato, pois os dois
modelos sugeridos implicam algoritmos e representações distintas. A
dependência de API externa também merece atenção antes do E2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTAGEM DE PALAVRAS (seções 1–5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Estimativa: ~310 palavras (conteúdo efetivo, excluindo tags de
comentário HTML e instruções do template)
Status: ✅ Dentro do limite (300–600) — mas na margem inferior.

Observações Gerais:

Gostei da ideia. Syncora tem um diferencial real — usar música em tempo real como critério de conexão é algo que faz sentido, tem mercado e não é só mais um clone de Tinder com outro nome. Isso conta bastante.

O contexto e motivação ficaram bons, dá pra entender o problema e por que grafos fazem sentido aqui. O diagrama foi entregue e a tabela de tipo de grafo foi preenchida, então a estrutura do documento tá completa.

Mas tem um problema técnico que precisa ser resolvido antes da próxima entrega: vocês estão descrevendo dois grafos ao mesmo tempo sem perceber. Num momento falam em grafo de similaridade entre usuários — arestas com peso representando gostos em comum. Em outro falam em grafo bipartido — usuários de um lado, músicas do outro. São modelos diferentes, respondem perguntas diferentes e levam a algoritmos diferentes. Antes do E2, vocês precisam sentar e decidir: qual é o grafo do Syncora? Essa decisão vai guiar toda a implementação.

Outro ponto de atenção: a integração com plataformas de música em tempo real é o coração do projeto, mas também é a parte mais arriscada. APIs do Spotify têm limite de requisições, exigem autenticação OAuth e têm restrições de uso que podem complicar bastante. Vale investigar isso agora, não na semana de entrega do E2.

Por fim, revisem o documento antes de entregar. As tags de comentário HTML ficaram no texto, e o campo do Integrante 3 ficou no documento. São detalhes, mas mostram que a revisão final não aconteceu.

No geral: projeto promissor, mas a modelagem precisa de mais clareza. Resolvam a ambiguidade do grafo e validem a viabilidade da API e vocês têm um E2 sólido pela frente.
