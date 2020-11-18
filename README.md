# Genescrape

[![CircleCI](https://circleci.com/gh/mahmoudimus/genescrape.svg?style=svg&circle-token=118c8a1aa6df1e883326ff78d3528d3d7a46deb4)](https://circleci.com/gh/mahmoudimus/genescrape)

## Getting Started

### Installation

`brew install docker-credential-gcloud`
`gcloud components install docker-credential-gcr`
`ln -s /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/bin/docker-credential-gcloud /usr/local/bin/`

`docker-credential-gcr configure-docker`
`docker-credential-gcloud configure-docker`

### Build

```bash
docker-compose up --build
```

### Running (after build)

```bash
docker-compose up scrapyd
```

```bash
docker-compose up orphanet
```

```bash
docker-compose up kibana
```

Kibana is http://localhost:5601
