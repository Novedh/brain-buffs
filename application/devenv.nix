{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/packages/
  packages = [ ];

  # https://devenv.sh/languages/
  languages = {
    python = {
      enable = true;
      venv.enable = true;
      venv.requirements = ''
        flask
        pytest
        mysql-connector-python
        python-dotenv
      '';
    };
  };

  # https://devenv.sh/processes/
  processes.runserver = {
    exec = "python src/app.py";
  };

  # https://devenv.sh/services/
  services = {
    nginx = {
      enable = true;
      httpConfig = ''
        	  server {
                listen 8080;
                listen [::]:8080;

                location / {
                        proxy_pass http://localhost:5050;
                        proxy_set_header Host $host;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                        proxy_set_header X-Forwarded-Proto $scheme;
                }
        	  }
      '';
    };
    mysql = {
      enable = true;
      initialDatabases = [{ name = "team01"; schema = ./src/database/dump.sql; }];
      ensureUsers = [
        {
          name = "team01";
          password = "team01";
          ensurePermissions = { "team01.*" = "ALL PRIVILEGES"; };
        }
      ];
    };
  };

  env = {
    DB_USER_NAME = "team01";
    DB_PASSWORD = "team01";
    DB_DATABASE = "team01";
    DB_HOST = "localhost";
    DB_PORT = "3306";
  };

  enterShell = ''
    	echo "CSC648 Team 01 Shell"
    	python --version
    	pip list
  '';

  # https://devenv.sh/tests/
  enterTest = ''
        echo "Running tests"
    	wait_for_port 8080
    	curl -s localhost:8080 | grep "Hello, world!"
    	curl -s 127.0.0.1:5050 | grep "HELLO, WORLD!"
  '';

  # https://devenv.sh/pre-commit-hooks/
  pre-commit.hooks = {
    # lint shell scripts
    shellcheck.enable = true;
    # format Python code
    black.enable = true;
    # format HTML/CSS/Javascript/YAML files
    prettier = {
      enable = true;
      files = "\\.(html|css|js|yml|yaml)$";
    };
    # format .nix files
    nixpkgs-fmt.enable = true;
  };

  # See full reference at https://devenv.sh/reference/options/
  scripts.connect_db.exec = ''
    	mysql -u $DB_USER_NAME -h $DB_HOST -P $DB_PORT --password=$DB_PASSWORD --database=$DB_DATABASE
  '';
  scripts.connect_db_prod.exec = ''
    	source .env
      	mysql -u $DB_USER_NAME -h $DB_HOST -P $DB_PORT --password=$DB_PASSWORD --database=$DB_DATABASE
  '';
  scripts.dump_db_prod.exec = ''
      	source .env
    	mysqldump -u $DB_USER_NAME -h $DB_HOST -P $DB_PORT --password=$DB_PASSWORD $DB_DATABASE | sed 's/utf8mb4_0900_ai_ci/utf8mb4_unicode_520_ci/g'
  '';
}
