# SoftDesk

Ceci est une API de suivi de projets pour remonter et suivre les problèmes techniques.

## Résumé des fonctionnalités

Un utilisateur peut : 
- s'inscrire, se connecter  
- créer un projet, ajouter des contributeurs au projet
- les contributeurs du projet peuvent ajouter des problèmes et des commentaires ainsi que voir ceux des autres contributeurs
- seulement les utilisteurs connectés et auteur du projet, problème ou commentaire peuvent les modifier ou supprimer

## Installation et lancement du server local

```bash
$ git clone https://github.com/tristan-mn/OPC_DA_P10_DJANGOREST_SOFTDESK.git
$ cd OPC_DA_P10_DJANGOREST_SOFTDESK
$ python3 -m venv env (Sous Windows => python -m venv env)
$ source env/bin/activate (Sous Windows => env\Scripts\activate)
$ pip install -r requirements.txt
$ cd softdesk
$ python manage.py runserver
```

## Endpoints disponibles

### connexion et inscription :

- http://127.0.0.1:8000/api/login/
- http://127.0.0.1:8000/api/register/  

### projet : 
http://127.0.0.1:8000/api/projects/
http://127.0.0.1:8000/api/projects/{{project_id}}/  

### contributeurs d'un projet :
http://127.0.0.1:8000/api/projects/{{project_id}}/users/
http://127.0.0.1:8000/api/projects/{{project_id}}/users/{{user_id}}/

### problèmes d'un projet :
http://127.0.0.1:8000/api/projects/{{project_id}}/issues/
http://127.0.0.1:8000/api/projects/{{project_id}}/issues/{{issue_id}}/

### commentaires sur un problème : 
http://127.0.0.1:8000/api/projects/{{project_id}}/issues/{{issue_id}}/comments/
http://127.0.0.1:8000/api/projects/{{project_id}}/issues/{{issue_id}}/comments/{{comment_id}}/


## Documentation

La documentation Postman est disponible en ligne :

https://documenter.getpostman.com/view/13735082/2s8YCkfW2h

