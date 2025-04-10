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
    
    
    ![image](https://github.com/user-attachments/assets/095e1f82-7660-4957-a228-0e651ff1217a)


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
   
   ***place the command you used for setting up the tunnel, the port and the screenshot of YARN UI here***
   
8. Draw an architecture diagram (e.g. in draw.io) that includes:
    1. VPC topology with service assignment to subnets
    2. Description of the components of service accounts
    3. List of buckets for disposal
    4. Description of network communication (ports, why it is necessary to specify the host for the driver) of Apache Spark running from Vertex AI Workbech
  
    ![image](https://github.com/user-attachments/assets/58e7fb7c-4422-4e24-89dd-dd70bcf1840a)

9. Create a new PR and add costs by entering the expected consumption into Infracost
For all the resources of type: `google_artifact_registry`, `google_storage_bucket`, `google_service_networking_connection`
create a sample usage profiles and add it to the Infracost task in CI/CD pipeline. Usage file [example](https://github.com/infracost/infracost/blob/master/infracost-usage-example.yml) 

   ***place the expected consumption you entered here***

   ***place the screenshot from infracost output here***

10. Create a BigQuery dataset and an external table using SQL
    
    ***place the code and output here***
   
    ***why does ORC not require a table schema?***

11. Find and correct the error in spark-job.py

    ***describe the cause and how to find the error***

12. Add support for preemptible/spot instances in a Dataproc cluster

    ***place the link to the modified file and inserted terraform code***
    
    
