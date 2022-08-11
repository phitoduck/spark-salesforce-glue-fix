# `spark-salesforce` development environment

## Welcome!

The purpose of this repository is to easily run PySpark code locally exactly
as it is run in AWS Glue.

## Getting Started

### 1. Have `make` installed locally

```bash
brew install make # macOS
apt-get install make # ubuntu
```

For Windows, you may need to run `docker-compose up` directly.

### 2. Make sure `docker` is installed and running

I use Docker Desktop on MacOS.

### 3. Use docker to run the ETL `make run-etl-in-docker`

This is really just a wrapper around the `docker-compose up` command.

If all goes well, you should see this error message:

```log
Caused by: [LoginFault [ApiFault  exceptionCode='INVALID_LOGIN'
exceptionMessage='Invalid username, password, security token; or user locked out.'
extendedErrorDetails='{[0]}'
```

This error validates two things about your setup:

- The AWS Glue 2.0 docker image was able to pull and run as a container.
- The `glue/salesforce-etl.py` script was able to execute and access the `spark-salesforce` JAR files in `glue/maven_jars`

### 4. Create a `.env` file

Add a `.env` file with these contents:

```ini
USERNAME=email-address-used-to-log-into-salesforce
PASSWORD=password
SECURITY_TOKEN=security token
```

[This link](https://docs.idalko.com/exalate/display/ED/Salesforce%3A+How+to+generate+a+security+token) shows how you can generate a
salesforce security token for a salesforce account.