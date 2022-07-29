import boto3

client = boto3.client('eks', region_name="eu-central-1")

#clusters = client.list_clusters() #returns dictionary
#print(clusters["clusters"]) #print cluster names list

clusters = client.list_clusters()["clusters"] # returns list

for cluster in clusters:
    response = client.describe_cluster(
        name=cluster
    )
    cluster_info = response["cluster"]
    cluster_status = cluster_info["status"]
    cluster_endpoint = cluster_info["endpoint"]
    cluster_version = cluster_info["version"]
    print(f"Cluster {cluster} status is {cluster_status}\nCluster endpoint is {cluster_endpoint}")
    print(f"Cluster version is {cluster_version}\n")

    response = client.list_nodegroups(
        clusterName=cluster

    )

    print(response["nodegroups"])

##todo describe nodegroup


