# 1. Docker

#### Check docker version
```bash
docker --version
```

#### Create a docker container
```bash
docker run -it --name Ubuntu -p 2022:22 -v /home/:/root ubuntu
```
#### Start docker container
```bash
docker start Ubuntu
```

#### Enter cmd of a docker container
```bash
docker exec -it Ubuntu bash
``` 

#### Log checking

```bash
docker logs container_name
```

#### List of image

```bash
docker images
```

#### List of container

```bash
docker -ps -a
```

#### Image search

```bash
docker search mysql
```

#### Image inspect

```bash
podman image inspect 439543311e0c
```

#### Image remove
```bash
podman image rm 439543311e0c
```
#### all stopped containers, all networks not used by at least one container, all images without at least one container associated with them, all build cache

```bash
docker prune -a
```


#### Memory config
```bash
podman run -it --name Ubuntu-Development -m 32g ubuntu
```

#### CPU config: here 100k% means full or 100% cpu. 50% usage means 50000.
```bash
podman run -it --name Ubuntu-Development -m 32g --cpu-quota=50000  ubuntu
```
#### Registry, Repository, Tag, Image, Container

#### Podman pod vs Docker container: 

|Podman pod|Docker container|
|-----------|----------------|
| group of container |  single container|
| used for testing env like Kubernetes (K8s) | For application running|
| Daemonless | Daemon |