

---

### Documentation Ansible

#### 1. **Création de l'Inventaire:**
   - **Fichier d'Inventaire:**
     - Liste des hôtes sur lesquels Ansible doit opérer.
     - Peut être un fichier INI ou YAML.
   - **Exemple en INI:**
     ```ini
     [groupe1]
     hote1 ansible_host=192.168.1.1
     hote2 ansible_host=192.168.1.2
     ```
   - **Exemple en YAML:**
     ```yaml
     groupe1:
       hosts:
         hote1:
           ansible_host: 192.168.1.1
         hote2:
           ansible_host: 192.168.1.2
     ```
#### 2. **Variables de Groupe (group_vars):**
   - **Objectif:**
     - Définir des variables qui seront utilisées par tous les hôtes d'un groupe spécifique.
   - **Structure:**
     - Créer un dossier nommé `group_vars` au même niveau que le fichier d'inventaire.
     - Dans `group_vars`, créez un fichier portant le nom du groupe.
   - **Exemple:**
     - Pour un groupe nommé `groupe1`, créez `group_vars/groupe1.yml`.
     - Dans `groupe1.yml`, définissez les variables pour `groupe1`:
       ```yaml
       variable1: valeur1
       variable2: valeur2
       variable3: vault_valeur3 #Préfixe vault_ si variable stockée dans un vault
       ```


#### 3. **Ansible Vault:**
Les vaults sont un moyen pour ansible de stocker des données sensibles (e.g: mots de passe, clefs ssh privées etc...)
   - **Création de Vault:**
     ```bash
     ansible-vault create fichier_vault.yml
     ```
   - **Édition de Vault:**
     ```bash
     ansible-vault edit fichier_vault.yml
     ```
   - **Utilisation de Vault dans Playbook:**
     ```yaml
     vars_files:
       - fichier_vault.yml
     ```

#### 3. **Création de Rôles:**
   - **Structure de Rôle:**
     - `defaults/`: Valeurs par défaut des variables.
     - `tasks/`: Tâches à exécuter.
     - `handlers/`: Gestionnaires d'événements.
     - `templates/`: Modèles Jinja2.
   - **Création de Rôle:**
     ```bash
     ansible-galaxy init nom_du_role
     ```
   - **Utilisation de Rôle dans Playbook:**
     ```yaml
     roles:
       - nom_du_role
     ```

#### 4. **Exécution de Playbook:**
   ```bash
   ansible-playbook -i chemin/vers/inventaire playbook.yml --ask-vault-pass #ask-vault-pass si un fichier vault a été créé
   ```

<br>

### Installation GitLab via Ansible
Créer le fichier user.yml en copiant le ansible/inventory/dev/group_vars/virtualmachines/gitlab_vault.yml.example
Utiliser ensuite ansible vault pour remplir et crypter ce fichier. Bien noter le mot de passe.
  ```bash
  ansible-vault encrypt inventory/dev/group_vars/virtualmachines/gitlab_vault.yml
  ansible-vault edit inventory/dev/group_vars/virtualmachines/gitlab_vault.yml
  # il est aussi possible de créer directement un fichier
  # ansible-vault create inventory/dev/group_vars/virtualmachines/gitlab_vault.yml
  ```
  Puis lancer le playbook (nécessite le mot de passe ansible vault)
  ```bash
  ansible-playbook gitlab.yml -i ansible/inventory/dev/inventory.yml --ask-vault-pass
  ```

# Déploiement de la TICK Stack

TICK, c'est un ensemble de solution de monitoring qui regroupe: 
  - **t**elegraph
  - **i**nfluxdb
  - **c**hronograf
  - **k**apacitor

## Préparation des images

Toutes les images de la TICK stack sont disponible sur le docker hub.
Pour les récupérer, on utilise la commande: 
```
  $ docker pull <image>
```

On push ensuite ces images dans notre registry Docker.

La convention de nommage d'un registre distant suit cette convention de nommage:

```
  <ip_ou_domaine_de_la_vm_contenant_le_registre>/<image>:<tag>
```

**Pour push n'importe quelle image sur un registre Docker, c'est simple. Il suffit de renommer l'image souhaitée selon la convention de nommage ci-dessus. Ensuite, effectuer *Docker push <image>***

## La Docker Stack

### Structure de la Docker Stack

1. **Service**: Nous définissions et nommons notre service (ex: telegraf, influxdb)
2.  **Image**: Nous spécifions l'image à utiliser (en l'occurence l'image dans notre registre)
3. **Deploy / replicas**: Le nombre de répliques / Le nombre de conteneurs
4. **Ports**: Spécification des ports à ouvrir sur ce pattern: **"<port_machine_locale>:<port_conteneur>"** (exemple: "3005:3000" indique que le service sera accessible via le port 3005 et sera routé sur le port 3000 dans le conteneur Docker)  
5. **Volumes**: Si besoin, spécifier un volume pour persister les données en suivant ce pattern: **<chemin_local>:<chemin_conteneur>**. Tout ce que contiendra le chemin du conteneur sera disponible sur le chemin local.
6. **Configs**: Nous définissons les configurations qui seront utilisées par les services. Ces configurations sont stockées dans le Docker Swarm et peuvent être utilisées par n'importe quel service dans la stack. Dans notre cas, nous avons seulement besoin d'une configuration pour Telegraf
  - source: telegraf-config : Ceci spécifie le nom de la configuration tel qu'il est défini dans la section configs à la racine du fichier Docker Stack. Docker Swarm utilise ce nom pour rechercher la configuration.

  - target: /etc/telegraf/telegraf.conf : Ceci spécifie le chemin dans le conteneur où la configuration sera placée. Dans ce cas, la configuration sera placée dans le fichier /etc/telegraf/telegraf.conf à l'intérieur du conteneur Telegraf.


### Déploiement de la Stack

On déploie et active l'ensemble des services de la Stack en utilisant cette commande: 

```
$ docker stack deploy -c chemin/vers/nom_du_docker_stack.yml  <nom au choix>
```

Le Swarm va automatiquement distribuer les conteneurs de la stack à travers les differents noeuds que composent la Swarm.

**!! Telegraph a besoin d'un fichier conf pour fonctionner (telegraf.conf)**

### Les commandes utiles pour vérifier le bon fonctionnement de la Stack

```
$ docker ps # Afficher l'ensemble des conteneurs qui fonctionnent
$ docker ps -a # Lister tous les conteneurs (même ceux qui ne sont pas en cours d'exécution)
$ docker stack services <nom_de_la_stack> # Lister tous les services de la stack spécifique
$ docker service ps <nom_du_service> # Vérifier l'état d'un service spécifique
$ docker services logs <nom_du_service> # Vérifier les logs d'un service spécifique
$ docker stack ls # Lister toutes les stacks déployées
$ docker node ls # Vérifier l'état de tous les noeuds dans un swarm Docker
```
