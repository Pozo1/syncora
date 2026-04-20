**E1 — Proposta e Definição do Projeto** **Disciplina:** Teoria dos Grafos 

**Prazo:** 16 de março de 2026 

**Peso:** 10% da nota final 



**Identificação do Grupo** 

**Campo** 

**Preenchimento** 

Nome Aplicativo 

Syncora 

Integrante 1 

Gabriel Nascimento de Carlo — 40259927 

Integrante 2 

Rodrigo Pozo Griecco — 38707616 

Integrante 3 

Nome — RA 

Domínio de 

Aplicativo de Relacionamento e Amizade com Integração com aplicação 

Música 



**1. Contexto e Motivação** 

Descreva o problema do mundo real que será abordado. Por que ele é relevante? 

*Orientação: 2 a 3 parágrafos. Seja específico — evite generalizações. * 

*<\! - - * Hoje em dia, aplicativos de relacionamento como Tinder são muito usados, principalmente por pessoas mais jovens. Só que, na maioria das vezes, eles focam muito em aparência e em poucas informações básicas, o que acaba gerando conexões meio superficiais. Muitas vezes as pessoas dão match mas não têm quase nada em comum. * *

A música é algo que praticamente todo mundo consome no dia a dia e fala bastante sobre a pessoa. Quem tem gostos musicais parecidos normalmente se conecta mais 

fácil, tem mais assunto e até mais chance de manter uma conversa. Mesmo assim, poucos aplicativos usam isso como base principal, ainda mais considerando o que a pessoa está ouvindo naquele momento. 

Então a ideia do projeto é justamente usar isso como diferencial. A proposta é criar um aplicativo que conecta pessoas com base na música, principalmente em tempo real. 

Assim, ao invés de só ver perfil, a pessoa pode encontrar alguém que literalmente está ouvindo a mesma música que ela, o que já cria uma conexão mais natural. - - > **2. Objetivo Geral** 

O que o sistema deve ser capaz de fazer ao final? 

*Orientação: 1 frase clara e objetiva. Ex.: "O sistema deve calcular a rota de menor custo* *entre dois pontos em um mapa urbano." * 

<\! - - Desenvolver um sistema que conecte usuários com base em seus gostos musicais, permitindo matches e interação entre pessoas com interesses parecidos. - - 

> 



**3. Objetivos Específicos** 

Desmembre o objetivo geral em metas mensuráveis. 

*Orientação: liste entre 3 e 5 itens. Cada item deve ser verificável — use verbos como *

*"implementar", "calcular", "exibir", "carregar". * 

• \[ Fazer integração com plataformas de música para identificar o que o usuário está ouvindo \] 

• \[ Encontrar usuários que estejam ouvindo a mesma música ao mesmo tempo \] 

• \[ Calcular o nível de semelhança entre usuários com base no histórico musical \] 

• \[ Mostrar sugestões de pessoas com gostos parecidos \] 

• \[ Permitir conversa entre usuários dentro do aplicativo \] 



**4. Público-Alvo / Caso de Uso Principal** Para quem ou em qual cenário o sistema seria utilizado? 

*Orientação: descreva um cenário concreto de uso. Ex.: "Um entregador de aplicativo* *que precisa otimizar a sequência de entregas em um bairro." * 

*<\! - - * O aplicativo é voltado principalmente para pessoas que usam música no dia a dia e gostam de conhecer gente nova, seja para amizade ou relacionamento. * *

Um exemplo simples: a pessoa está ouvindo música no fone, no ônibus ou em casa. Ao abrir o app, ele identifica a música e mostra outras pessoas que estão ouvindo a mesma coisa naquele momento. A partir disso, pode rolar um match e os dois começam a conversar. A ideia é deixar a interação mais natural, já começando com algo em comum. - - > 



**5. Justificativa Técnica — Por que Grafos? ** 

Por que a modelagem em grafo é a abordagem mais adequada para este problema? 

*Orientação: explique quais elementos do problema mapeiam naturalmente para* *vértices e arestas. Mencione se há pesos, direção, ou restrições que reforçam a* *escolha. * 

<\! - - Grafos fazem sentido aqui porque o problema envolve conexões. Dá pra representar os usuários como vértices e as relações entre eles como arestas, por exemplo quando duas pessoas têm gostos parecidos ou estão ouvindo a mesma música. 

Também dá pra usar pesos nessas conexões, indicando o nível de similaridade entre os usuários. Isso ajuda o sistema a recomendar melhor quem tem mais a ver com quem. 

Além disso, como essas conexões mudam o tempo todo \(música que a pessoa tá ouvindo, histórico, etc.\), grafos ajudam bastante por serem flexíveis. Também permitem usar algoritmos de busca e recomendação, que são importantes pro funcionamento do app. - - > 

* *



**6. Tipo de Grafo** 

Especifique as características do grafo que o problema requer. 



**Característica** 

**Escolha** 

**Justificativa breve** 

Não-

A conexão entre usuários é 

Dirigido ou não-dirigido 

Dirigido 

dos dois lados 

Representa o nível de 

Ponderado ou não-ponderado 

Ponderado 

semelhança 

Relação entre usuários e 

Conectado / bipartido / geral 

Bipartido 

músicas 

Representação interna pretendida lista 

Lista de 

Melhor para trabalhar com 

de adjacência / matriz 

Adjacência 

muitos usuáros 



**7. Diagrama Conceitual** 

Insira aqui ao menos uma figura que ilustre o domínio do problema. 

*Pode ser uma imagem exportada do Draw.io, Excalidraw, foto de esboço à mão etc. * 



**Legenda: vértices são usuários e músicas; arestas são as conexões; pesos** **indicam o nível de similaridade. ** 



**Checklist de Entrega** 

Antes de submeter, confirme: 

• \[ x \] Texto entre 300 e 600 palavras \(seções 1 a 5\) 

• \[ x \] Todos os campos da tabela de identificação preenchidos 

• \[ x \] Tipo de grafo especificado com justificativa 

• \[ x \] Diagrama presente e referenciado no texto 

• \[ x \] Arquivo nomeado como E1\_NomeGrupo\_Grafos.docx \(versão Word\) ou PR 

aberto \(versão GitHub\) 



*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai* 




# Document Outline

+ E1 — Proposta e Definição do Projeto  
	+ Identificação do Grupo 
	+ 1. Contexto e Motivação 
	+ 2. Objetivo Geral 
	+ 3. Objetivos Específicos 
	+ 4. Público-Alvo / Caso de Uso Principal 
	+ 5. Justificativa Técnica — Por que Grafos?  
	+ 6. Tipo de Grafo 
	+ 7. Diagrama Conceitual 
	+ Checklist de Entrega



