# otp_app

upgrade: ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	# pip install -qr requirements/pip-tools.txt
	# Make sure to compile files after any other files they include!
pip-compile --upgrade --allow-unsafe -o requirements/pip-tools.txt requirements/pip-tools.in
pip-compile --upgrade -o requirements/base.txt requirements/base.in
pip-compile --upgrade -o requirements/test.txt requirements/test.in


CREATE TABLE user_otp (
    user_id CHAR(36) NOT NULL PRIMARY KEY DEFAULT (UUID()),
    secret  VARBINARY(256) NOT NULL,
    last_auth DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO user_otp (user_id, secret) VALUES ("081daf82-4b77-4a7b-a110-29f513ca830c", "secreto")
CREATE TABLE user_otp (
    ->     user_id CHAR(36) NOT NULL PRIMARY KEY DEFAULT (UUID()),
    ->     secret  VARBINARY(256) NOT NULL,
    ->     last_auth DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    -> );


docker run --name otp-db -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=otp-db -d mysql:tag

