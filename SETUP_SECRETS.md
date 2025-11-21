# 🔐 Configuration des Secrets GitHub

## Étape 1 : Créer un Token Docker Hub

1. Connectez-vous sur [hub.docker.com](https://hub.docker.com)
2. Cliquez sur votre avatar (en haut à droite) → **Account Settings**
3. Allez dans **Security** → **Access Tokens**
4. Cliquez sur **New Access Token**
5. Donnez un nom : `github-actions`
6. Permissions : **Read, Write, Delete**
7. Cliquez sur **Generate**
8. **COPIEZ LE TOKEN** (vous ne pourrez plus le voir après !)

## Étape 2 : Ajouter les Secrets dans GitHub

1. Allez sur votre repo GitHub : `https://github.com/Chaanani/notes-app`
2. Cliquez sur **Settings** (onglet en haut)
3. Dans le menu de gauche : **Secrets and variables** → **Actions**
4. Cliquez sur **New repository secret**

### Secret 1 : DOCKERHUB_USERNAME
- **Name** : `DOCKERHUB_USERNAME`
- **Secret** : Votre nom d'utilisateur Docker Hub (exemple: `chaanani`)
- Cliquez **Add secret**

### Secret 2 : DOCKERHUB_TOKEN
- **Name** : `DOCKERHUB_TOKEN`
- **Secret** : Le token que vous avez copié à l'étape 1
- Cliquez **Add secret**

## Étape 3 : Vérifier

Une fois les deux secrets ajoutés, vous devriez voir :
```
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

## Étape 4 : Re-déclencher le workflow

Faites un commit vide pour re-déclencher le workflow :

```bash
git commit --allow-empty -m "Trigger CI/CD after secrets setup"
git push
```

Le workflow devrait maintenant fonctionner ! ✅

---

## ⚠️ IMPORTANT

- Ne commitez **JAMAIS** vos tokens dans le code
- Les secrets GitHub sont cryptés et sécurisés
- Vous pouvez régénérer un token à tout moment sur Docker Hub
