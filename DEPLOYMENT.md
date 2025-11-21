# 🚀 Déploiement Notes App

## Configuration GitHub Secrets

Pour que le CI/CD fonctionne, ajoutez ces secrets dans GitHub :

1. Allez sur votre repo GitHub → **Settings** → **Secrets and variables** → **Actions**
2. Cliquez sur **New repository secret**
3. Ajoutez :

```
DOCKERHUB_USERNAME = votre-username-dockerhub
DOCKERHUB_TOKEN = votre-token-dockerhub
```

### Créer un Docker Hub Token

1. Connectez-vous sur [hub.docker.com](https://hub.docker.com)
2. Allez dans **Account Settings** → **Security** → **Access Tokens**
3. Créez un nouveau token avec permission **Read, Write, Delete**
4. Copiez le token et ajoutez-le dans GitHub Secrets

## CI/CD Pipeline

Le workflow GitHub Actions :
- ✅ Build automatique sur chaque push vers `main`
- ✅ Push des images vers Docker Hub
- ✅ Tag avec `latest` et le SHA du commit

## Déploiement Kubernetes

Une fois les images poussées sur Docker Hub :

```bash
# Mettre à jour les images dans les manifests K8s
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/pvc-postgres.yaml
kubectl apply -f k8s/deployment-postgres.yaml
kubectl apply -f k8s/service-postgres.yaml
kubectl apply -f k8s/deployment-backend.yaml
kubectl apply -f k8s/service-backend.yaml
kubectl apply -f k8s/deployment-frontend.yaml
kubectl apply -f k8s/service-frontend.yaml
kubectl apply -f k8s/ingress.yaml
```

## Déploiement ArgoCD

```bash
kubectl apply -f argocd/application.yaml
```

ArgoCD surveillera automatiquement le repo et déploiera les changements.

## Variables d'environnement Production

Dans `k8s/secret.yaml`, configurez :
- `DATABASE_URL` : URL PostgreSQL
- `API_TOKEN` : Token sécurisé (générez-en un nouveau !)

**Générer un token sécurisé** :
```bash
openssl rand -hex 32
```
