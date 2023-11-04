up:
	docker compose up -d

migrate:
	docker compose run --rm django sh -c "python3 incident_log/manage.py makemigrations"
	docker compose run --rm django sh -c "python3 incident_log/manage.py migrate"

test:
	docker compose up -d && ./run_test.sh