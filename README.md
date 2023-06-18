# ponderada-4
Atividade 4: Backend para transmissão e armazenamento de imagens

## Estrutura de pastas
```
.
├── assets/
│   ├── vid.mp4
│   └── vid.mp4:Zone.Identifier
├── frames
├── .gitignore
├── api.py
├── frameHandler.py
├── img_publisher.py
└── README.md
```

### assets
Esta pasta contém o(s) vídeos que são usados como exemplo para obter imagens.

### frames
Está pasta é responsável por armazenar os frames gerados pelo publisher.

## api.py
Este arquivo é o backend em sanic responsável por guardar as imagens recebidas pelo subscriber. Este possui duas rotas:
-/test: Utilizada meramente para testes de conectividade e debug.
-/upload: Responsável por armazenar as imagens recebidas na pasta frames.

## img_publisher.py
Este arquivo contém o Nó publicador responsável por seccionar o vídeo em frames e publicá-los no tópico 'video_frames'. Utiliza um timer de 0.1 segundos para mandar imagens com a ajuda da biblioteca cv_bridge.

## frameHandler.py
Este arquivo contém o Nó subscrito responsável por manusear as imagens enviadas pelo publisher e fazer requisições HTTP para o backend em sanic, além de mostrar as imagens recebidas.

## Roadmap & testes
Tentativa utilizar um backend em Node.js (app.js ainda em construção) para receber as imagens. Além disso, tentarei utilizar o Supabase e salvar as imagens diretamente em um bucket. 