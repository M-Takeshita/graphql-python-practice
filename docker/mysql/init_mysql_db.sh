docker-compose exec mysql bash -c "chmod 0775 docker-entrypoint-initdb.d/init_db.sh"
docker-compose exec mysql bash -c "./docker-entrypoint-initdb.d/init_db.sh"
