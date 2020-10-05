# Gorgias SRE interview challenge

## todoapp

1. Create the required Infrastructure
2. Create the Database service
3. Create the application service

### Create Infrasturcture

make sure you have the google-cloud-sdk installed for your platform and configured with proper authentication etc.,

You can verify access to the porject by running

`gcloud projects list`

you should be seeing the project in the list.

The GKE cluster and the external static ip address used by the LB will be created using the terraform template.

`cd Infrastructure/terrafrom`

`terraform plan # this will show the plan to be executed and resources that will be created`

`terraform apply # apply the changes to the infrastructure`

You have to obtain the output values of the cluster and the external static ip as it is needed later.

generate a .kube/config entry by obtaining the cluster ctedentials by running

`gcloud container clusters get-credentials dev-cluster --zone=us-west1-a`

This step is need by the kubectl utility to interact with the cluster.

configure kubectl to use the dev-cluster as active cluster by setting the current context.


### Setup Data service

This stage will create the postgresql master and replica statefulsets with replication enabled

1. cd into `DataService/postgresql-replication` and edit `config/secret-sample.yml` to replace the password values and rename `secret-sample.yml` to `secret.yml`
2. Run `kubectl apply -f config/secret.yml` and then `cd config && ./create_configmap.sh`
3. `cd ..` and setup the master statefulset by running `kubectl apply -f statefulset-master.yml`
4. start the services by running `kubectl apply -f service.yml`
5. Now start the replica statefulset to enable replication `kubectl apply -f statefulset-replica.yml`

### Create the application service

In order for the app to work, the `todoapp` database needs to be setup on the `postgres-0` master instance.

1. from the repo root run the following command to setup the db, application user account, roles etc.,
2. `kubectl -n pg exec -i postgres-0 -- psql < sql_scripts/dbseeder.sql`
3. `kubectl -n pg exec -i postgres-0 -- psql -c "ALTER USER todoapp WITH PASSWORD '<password>';"`
4. The Dockerfile is used to build the docker image referenced by the Kubernetes manifests.
5. edit the `todoapp-secret-sample.yml` to replace the password with the password used in step 3 and apply it.
6. Now deploy the application using the helm chart by running `cd helm && helm install todoapp ./sg-todoapp`
7. verify the deployment by running `helm ls`
8. When the deployment is completed, navigate to the ip address of the load balancer to access the application.