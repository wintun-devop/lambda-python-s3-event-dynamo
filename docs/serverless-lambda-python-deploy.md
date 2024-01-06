## Installing Serverless Nodejs Package with Global Mode(we can install from any where.)
```
npm i -g serverless
```
## create serverless.yaml file
```
# Service name
service: serverless-python-test
# Framework version constraint (semver constraint): '3', '^2.33'
frameworkVersion: '3'
#Provider Name
provider:
  name: aws
  runtime: python3.12
  region: ap-northeast-1
  stage: dev
plugins:
  - serverless-python-requirements
functions:
  testServerlessPython:
    handler: handler.main
```
## python env creation for window os
```
python -m venv lambda-python-env
```
## env activation and necessary package installation
```
lambda-python-env\Scripts\activate
```
```
pip install boto3
```

## code deployment
### deploy to lambda runtime to aws
```
serverless plugin install -n serverless-python-requirements
```
```
serverless deploy
```
