# Statbov

[![CI](https://github.com/henriquesebastiao/statbov/actions/workflows/ci.yml/badge.svg)](https://github.com/henriquesebastiao/statbov/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/henriquesebastiao/statbov/graph/badge.svg?token=PNjl5Z61RQ)](https://codecov.io/gh/henriquesebastiao/statbov)
[![LICENSE](https://img.shields.io/badge/license-MIT-green)](https://github.com/henriquesebastiao/statbov/blob/main/LICENSE)

Statbov é um projeto para pecuária de precisão com análise de métricas.

## Executando localmente

Execute os seguintes comandos para executar o projeto localmente:

```bash
git clone https://github.com/henriquesebastiao/statbov.git
cd statbov
poetry install
poetry shell
```

Configure as variáveis de ambientes descritas na seção [Dicas para desenvolvimento](CONTRIBUTING.md#dicas-para-desenvolvimento) e execute o Docker Compose:

```bash
docker-compose up -d
```

Agora você pode acessar o projeto em [http://localhost:8000](http://localhost:8000).

## Contribuindo

Caso queira contribuir com o projeto, recomendo que leia o [CONTRIBUTING.md](CONTRIBUTING.md) para entender como o projeto está organizado e como contribuir.
