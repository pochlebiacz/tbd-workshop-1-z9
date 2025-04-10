IMPORTANT ❗ ❗ ❗ Please remember to destroy all the resources after each work session. You can recreate infrastructure by creating new PR and merging it to master.
  
![img.png](doc/figures/destroy.png)

1. Authors:

   9

   https://github.com/pochlebiacz/tbd-workshop-1-z9
   
2. Follow all steps in README.md.

3. In boostrap/variables.tf add your emails to variable "budget_channels".

4. From avaialble Github Actions select and run destroy on main branch.
   
5. Create new git branch and:
    1. Modify tasks-phase1.md file.
    
    2. Create PR from this branch to **YOUR** master and merge it to make new release. 
    
    ![image](https://github.com/user-attachments/assets/b93fba07-fb71-44ae-8371-27473b43e070)

6. Analyze terraform code. Play with terraform plan, terraform graph to investigate different modules.

    ![image](https://github.com/user-attachments/assets/9bd1083f-3f7f-4e28-ae00-7eea759191c9)

Module: VPC
This module sets up a Virtual Private Cloud (VPC) on Google Cloud. It creates a subnet with a specified IP range and regional configuration, sets up routing, and configures a Cloud Router with a NAT gateway for internet access. In addition, it applies firewall rules for secure incoming connections - including those for Identity-Aware Proxy (IAP) access and ensures all internal subnet traffic is allowed.

Inputs:
- project_name: The name of the Google Cloud project.
- region: The region where the resources will be deployed (default: europe-west1).
- network_name: The name given to the VPC.
- subnet_name: The name assigned to the subnet.
- subnet_address: The IP range designated for the subnet (default: 10.10.10.0/24).

Outputs:
- network: The identifier for the created VPC.
- subnets: A mapping detailing the subnet configuration within the VPC.
   
7. Reach YARN UI
   
```gcloud compute instances list --project=tbd-2025l-310269 --filter="zone:(europe-west1*)"```

```gcloud compute ssh tbd-cluster-m --project=tbd-2025l-310269 --zone=europe-west1-c --tunnel-through-iap -- -L 8088:localhost:8088```

   ![image](https://github.com/user-attachments/assets/51323a5e-f96f-4f62-891f-db5754ca8735)

8. Draw an architecture diagram (e.g. in draw.io) that includes:
    1. VPC topology with service assignment to subnets
  ![image](https://github.com/user-attachments/assets/58e7fb7c-4422-4e24-89dd-dd70bcf1840a)
    2. Description of the components of service accounts

      tbd-terraform: This service account is likely used for infrastructure provisioning and management via Terraform, a popular Infrastructure-as-Code (IaC) tool. It would have permissions       to create, modify, or delete cloud resources.<br />
      iac: This stands for "Infrastructure as Code" and is another service account<br />
      tbd-composer-sa: This service account is associated with Cloud Composer. It would have permissions to interact with Cloud Composer resources, such as managing Airflow DAGs, accessing        storage buckets, or interacting with other Google Cloud services on behalf of Cloud Composer.

    3. List of buckets for disposal

      tbd-conf-bucket<br />
      tbd-code-bucket<br />
      tbd-data-bucket<br />
      tbd-state-bucket

    4. Description of network communication (ports, why it is necessary to specify the host for the driver) of Apache Spark running from Vertex AI Workbech

        Apache Spark running from Vertex AI Workbench requires specifying the driver host because Spark executors must be able to establish a direct connection to the driver, which acts as the central coordinator. This necessitates opening specific ports, as well as ensuring firewall rules allow traffic between components. Proper network setup ensures stable execution of distributed Spark jobs across the VPC.
10. Create a new PR and add costs by entering the expected consumption into Infracost
For all the resources of type: `google_artifact_registry`, `google_storage_bucket`, `google_service_networking_connection`
create a sample usage profiles and add it to the Infracost task in CI/CD pipeline. Usage file [example](https://github.com/infracost/infracost/blob/master/infracost-usage-example.yml) 

   version: 1.0<br />
 usage:<br />
   google_artifact_registry.registry:<br />
     storage_gb: 100

   google_storage_bucket.tbd_code_bucket:<br />
     storage_gb: 150<br />
     monthly_class_a_operations: 50<br />
     monthly_class_b_operations: 100<br />
     monthly_egress_data_gb: 30<br />

   google_storage_bucket.tbd_data_bucket:
     storage_gb: 500<br />
     monthly_class_a_operations: 50<br />
     monthly_class_b_operations: 80<br />
     monthly_egress_data_transfer_gb:<br />
       same_continent: 80<br />
       worldwide: 200<br />
       asia: 40<br />
       china: 30<br />

   google_service_networking_connection.private_vpc_connection:<br />
     monthly_data_processed_gb: 100

   ![image](https://github.com/user-attachments/assets/62b34f33-48ea-4fdf-8a7d-dd1cb40389a5)

10. Create a BigQuery dataset and an external table using SQL
    
    ***place the code and output here***
   
    ***why does ORC not require a table schema?***

11. Find and correct the error in spark-job.py

    ***describe the cause and how to find the error***

12. Add support for preemptible/spot instances in a Dataproc cluster

    ***place the link to the modified file and inserted terraform code***
    
    
