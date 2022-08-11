# start up the AWS Glue container using docker-compose;
# the entrypoint/run command defined in the compose file
# cause the container to execute salesforce-etl.py and then exit
run-etl-in-docker:
	docker-compose up

# helper to download .jar files needed for the springml/spark-salesforce
# package to ./glue/maven_jars/. Note that the package versions downloaded
# by this script were hand picked to be compatible.
fetch-maven-dependencies:
	python -m venv venv/
	source venv/bin/activate \
		&& python -m pip install -r ./glue/fetch-maven.requirements.txt \
		&& python ./glue/fetch_maven_jars.py

# this is useful for development in VS Code; you can install the
# "Remote - Containers" (id: ms-vscode-remote.remote-containers) extension
# which allows you to install VS Code into this running container. This
# is useful for getting autocompletion and syntax highlighting when editing
# the Glue python script
run-aws-glue-container-that-hangs:
	docker-compose run --entrypoint '/bin/bash -c' aws-glue cat