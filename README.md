# Repositories

## Envs

Create `/envs/` directory using `/envs.example/` as template.

```bash
# django
DJANGO_DEBUG # 0 or 1 for disabled/enabled
DJANGO_SECRET_KEY # 50 characters

# postgres
POSTGRES_USERNAME # username
POSTGRES_PASSWORD # password

# webshrinker
WEBSHRINKER_ACCESS_KEY # access_key
WEBSHRINKER_SECRET_KEY # secret_key
```

You can obtain webshrinker keys from [here](https://dashboard.webshrinker.com/keys).

## Running

After creating envs run:

```bash
docker-compose up
```

This starts with failure when database is yet not created.

## Database

Setting up database, e.g. for local instance:

```bash
docker-compose up
docker-compose exec postgres bash
psql -h postgres -U postgres  # password is postgres
CREATE DATABASE websites WITH OWNER postgres ENCODING 'utf-8';
```

Now run `docker-compose up` again for backend to start without failure.

## Tests

Running tests:

```bash
docker-compose up
docker-compose exec django bash
./manage.py test api.tests
```

## Deployment

Deploy to production:

* create configuration (look into /docker-compose.yml and /Dockerfile)
    * generate envs (look into /envs/)
    * generate Djago secret with `pwgen -sy 50 1`

# Heroku deployment

Environment variables:

* Install plugin `heroku plugins:install heroku-config`.
* Use `heroku config:pull` and `heroku config:push`.

Add a database: `Heroku Postgres` in Resources.

Connect with GitHub and setup automatic `master` deployments.

Set stack to container: `heroku stack:set container`.

## Notes

* Took me 2h 50m to finish the task
